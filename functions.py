import random

from sqlalchemy.sql.expression import func
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from flask import request
import math 
from collections import defaultdict
import json
import xml.etree.ElementTree as ET
import os

stop_words = set(stopwords.words('english'))

# Calculate the estimated reading time for the content
# Parameters:
# - content: String containing the content to calculate reading time for
# Returns:
# - Integer representing the estimated reading time in minutes
def calculate_reading_time(content):
    if content is not None:
        words = content.split()
        reading_time = len(words) / 200  # Assume 200 words per minute
        reading_time = math.ceil(reading_time)  # Round up to the nearest minute
        return reading_time
    else:
        return 0

# Convert a given text to a URL-friendly format
# Parameters:
# - text: String to be converted to a URL-friendly format
# Returns:
# - String with hyphens instead of spaces and capitalized words
def urlize(text):
    text = text.strip()
    text = text.replace('-', ' ').replace('_', ' ')
    words = text.split()
    words = [word.capitalize() if word.lower() not in stop_words else word for word in words]
    text = ' '.join(words)
    text = text[0].capitalize() + text[1:]
    return text

# Build a data dictionary from topics and articles
# Parameters:
# - contributors:  SQLAlchemy query object for contributors 
# - blogs: SQLAlchemy query object for blogs
# - topics: SQLAlchemy query object for topics
# - articles: SQLAlchemy query object for articles
# Returns:
# - Dictionary containing structured data of topics and articles
def build_data_dict(contributors, blogs, topics, articles):
    data_dict = {}
    contributors_data = contributors.query.all()
    blogs_data = blogs.query.all()
    topics_data = topics.query.all()
    topic_dict = defaultdict(lambda: defaultdict(list))

    for topic in topics_data:
        topic_dict[topic.level][topic.parent].append(topic)

    def serialize_article(article):
        return {
            'id': article.id,
            'title': article.title,
            'path': article.path,
            'description': article.description,
            'reading_time': calculate_reading_time(article.content),
            'date': article.date,
            'draft': article.draft
        }
    def serialize_blog(blog):
        return{
            'id': blog.id,
            'title': blog.title,
            'description': blog.description,
            'path': blog.path
        }
    def serialize_contributor(contributor):
        return{
            'id': contributor.id,
            'name': contributor.name,
            'path': contributor.path,
            'description_short': contributor.description_short
        }
        
    def serialize_topic(topic, level, parent, articles):
        return {
            'id': topic.id,
            'title': topic.title,
            'path': topic.path,
            'parent': topic.parent,
            'level': topic.level,
            'draft': topic.draft,
            'childtopics': build_structure(level + 1, topic.id, articles),
            'articles': [serialize_article(article) for article in articles.query.filter_by(parent=topic.id).all()]
        }

    def build_structure(level, parent, articles):
        if level not in topic_dict:
            return []
        return [
            serialize_topic(topic, level, parent, articles)
            for topic in topic_dict[level][parent]
        ]
    
    articles_examples = articles.query.filter_by(type='examples').all()
    serialized_articles_examples = [serialize_article(article) for article in articles_examples]
    serialized_blogs = [serialize_blog(blog) for blog in blogs_data]
    serialized_contributors = [serialize_contributor(contributor) for contributor in contributors_data]

    data_dict['topics'] = build_structure(1, 1, articles)
    data_dict['examples'] = serialized_articles_examples
    data_dict['contributors'] = serialized_contributors
    data_dict['blogs'] = serialized_blogs

    return data_dict


# Recursively find the full path of a topic by its parent ID
# Parameters:
# - parent_topic_id: Integer ID of the parent topic
# - Topics: SQLAlchemy model for topics
# Returns:
# - Dictionary containing the title and full path of the topic
def get_full_topic_path(parent_topic_id, Topics):
    topic = Topics.query \
        .with_entities(Topics.id, Topics.title, Topics.path, Topics.parent) \
        .filter_by(id=parent_topic_id) \
        .first()

    if not topic:
        return None
    
    if not topic.parent:
        return {
            "title": topic.title,
            "path": topic.path
        }

    parent_topic = get_full_topic_path(topic.parent, Topics)
    if parent_topic:
        full_path = f"{parent_topic['path']}/{topic.path}"
        return {
            "title": topic.title, 
            "path": full_path
        }
    return {
        "title": topic.title,
        "path": topic.path
    }

# Fetch the most recently published articles
# Parameters:
# - articles: SQLAlchemy query object for articles
# - Topics: SQLAlchemy model for topics
# Returns:
# - List of dictionaries containing the title and path of recent articles
def recently_published(articles, Topics):
    base_url = request.host_url.rstrip("/")
    recent_articles_query = articles.query \
        .with_entities(articles.title, articles.path, articles.parent) \
        .order_by(func.coalesce(articles.date_modified, articles.date).desc()) \
        .limit(4) \
        .all()

    recent_articles_dict = []

    for article in recent_articles_query:
        title = article.title
        article_path = article.path
        article_parent = article.parent

        parent_topic_path = get_full_topic_path(article_parent, Topics)

        if parent_topic_path:
            full_path = f"{base_url}/{parent_topic_path['path']}/{article_path}"
            full_dict = {"title": title, "path": full_path}
            recent_articles_dict.append(full_dict)
        else:
            full_path = f"{base_url}/{article_path}"
            recent_articles_dict.append({"title": title, "path": full_path})

    return recent_articles_dict

# Generate a table of contents from HTML content
# Parameters:
# - content_html: String containing the HTML content
# Returns:
# - List of dictionaries representing the table of contents
def generate_table_of_contents(content_html):
    soup = BeautifulSoup(content_html, 'html.parser')
    headings = soup.find_all(['h2', 'h3'])
    table_of_contents = []
    current_h2 = None

    for heading in headings:
        level = heading.name
        text = heading.text.strip()
        anchor = text.lower().replace(' ', '-')

        if level == 'h2':
            current_h2 = {'text': text, 'anchor': anchor, 'subheadings': []}
            table_of_contents.append(current_h2)
        elif level == 'h3' and current_h2 is not None:
            current_h2['subheadings'].append({'text': text, 'anchor': anchor})

    return table_of_contents

# Generate breadcrumbs for the current page
# Parameters:
# - None
# Returns:
# - List of dictionaries representing breadcrumb items
def get_breadcrumbs():
    base_url = request.host_url.rstrip("/")
    current_url = request.url
    path = current_url.replace(base_url, "")
    url_parts = path.strip("/").split("/")
    breadcrumbs = [{"name": "Home", "url": base_url}]

    for i in range(1, len(url_parts)):
        breadcrumb = {
            "name": url_parts[i].replace("-", " ").title(),
            "url": f"{base_url}/{'/'.join(url_parts[:i + 1])}/"
        }
        if "?utm_" in url_parts[i]:
            continue
        else:
            breadcrumbs.append(breadcrumb)

    return breadcrumbs

# Find related articles for a given article path
# Parameters:
# - article_path: String representing the path of the current article
# - articles: SQLAlchemy query object for articles
# - Topics: SQLAlchemy model for topics
# Returns:
# - List of dictionaries containing related articles' title, path, keywords, and description
def find_related_articles(article_path, articles, Topics):
    current_article = articles.query.filter_by(path=article_path).first()

    if not current_article:
        return []

    related_articles_query = articles.query \
        .filter(articles.parent == current_article.parent, articles.id != current_article.id) \
        .limit(3) \
        .all()

    if len(related_articles_query) < 1:
        parent_topic = Topics.query.filter_by(id=current_article.parent).first()

        if parent_topic:
            sibling_categories = Topics.query \
                .filter(Topics.parent == parent_topic.parent, Topics.id != current_article.parent) \
                .all()

            sibling_articles = []
            for sibling in sibling_categories:
                sibling_articles.extend(
                    articles.query.filter_by(parent=sibling.id).all()
                )

            related_articles_query.extend(random.sample(sibling_articles, min(3 - len(related_articles_query), len(sibling_articles))))

    base_url = request.host_url.rstrip("/")
    top_related_articles = []

    for article in related_articles_query:
        parent_topic_path = get_full_topic_path(article.parent, Topics)
        if parent_topic_path:
            full_path = f"{base_url}/{parent_topic_path['path']}/{article.path}"
        else:
            full_path = f"{base_url}/{article.path}"

        top_related_articles.append({
            "title": article.title,
            "path": full_path,
            "keywords": article.keywords,
            "description": article.description
        })

    return top_related_articles

# Fetch meta data from a data object
# Parameters:
# - data_object: Object or dictionary containing meta data attributes
# Returns:
# - Dictionary containing the meta data
def fetch_meta_data(data_object):
    meta_data = {}

    if isinstance(data_object, dict):
        title = data_object.get('title')
        description = data_object.get('description')
        keywords = data_object.get('keywords')
    else:
        title = getattr(data_object, 'title', None)
        description = getattr(data_object, 'description', None)
        keywords = getattr(data_object, 'keywords', None)

    if title:
        meta_data['title'] = title
    if description:
        meta_data['description'] = description
    if keywords:
        meta_data['keywords'] = keywords

    return meta_data

# Fetch contributions for a single contributor
# Parameters:
# - Contributor: SQLAlchemy model for contributors
# - Articles: SQLAlchemy query object for articles
# - Topics: SQLAlchemy model for topics
# Returns:
# - List of dictionaries containing contributions with their full paths
def fetch_contributions_for_the_single_contributor(Contributor, Articles, Topics):
    base_url = request.host_url.rstrip("/")
    contributions = Articles.query.filter_by(author=Contributor.name).with_entities(Articles.id, Articles.title, Articles.path, Articles.parent).all()
    contributions_with_full_path = []

    for contribution in contributions:
        parent_topic_path = get_full_topic_path(contribution.parent, Topics)
        if parent_topic_path:
            full_path = f"{base_url}/{parent_topic_path['path']}/{contribution.path}"
        else:
            full_path = f"{base_url}/{contribution.path}"
        
        contributions_with_full_path.append({
            "id": contribution.id,
            "title": contribution.title,
            "path": full_path
        })
    return contributions_with_full_path

def add_url_element(urlset, loc, date=None, priority="0.8", changefreq="monthly"):
    url = ET.SubElement(urlset, "url")
    
    loc_element = ET.SubElement(url, "loc")
    loc_element.text = loc.lower()
    
    priority_element = ET.SubElement(url, "priority")
    priority_element.text = priority
    
    changefreq_element = ET.SubElement(url, "changefreq")
    changefreq_element.text = changefreq
    
    if date:
        lastmod_element = ET.SubElement(url, "lastmod")
        lastmod_element.text = str(date)

def generate_sitemap(app, data, base_url="https://www.example.com"):
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    def process_topics(topics, parent_path=""):
        for topic in topics:
            if topic['draft'] != 'true':
                full_path = f"{parent_path}/{topic['path']}".strip("/")
                add_url_element(urlset, f"{base_url}/topics/{full_path}/")
                process_topics(topic.get('childtopics', []), full_path)
                for article in topic.get('articles', []):
                    if article['draft'] != 'true':
                        article_path = f"{full_path}/{article['path']}"
                        article_path = article_path.lower()
                        add_url_element(urlset, f"{base_url}/topics/{article_path}/", date = article['date'])

    # Process topics and articles
    process_topics(data['topics'])

    # Process examples
    for example in data.get('examples', []):
        if example['draft'] != 'true':
            example_path = f"{base_url}/examples/{example['path']}/"
            example_path = example_path.lower()
            add_url_element(urlset, example_path, date=example.get('date'))
    
    # Process blogs
    for blog in data.get('blogs', []):
        blog_path = f"{base_url}/blog/{blog['path']}/"
        blog_path = blog_path.lower()
        add_url_element(urlset, blog_path)
    
    # Process contributors
    for contributor in data.get('contributors', []):
        contributor_name_path = contributor['path'].replace('-', '')
        contributor_path = f"{base_url}/contributors/{contributor_name_path}/"
        contributor_path = contributor_path.lower()
        add_url_element(urlset, contributor_path)

    # Non dynamic routes
    rules = list(app.url_map.iter_rules())
    if not rules:
        print("No routes were registered.")
    else:
        for rule in app.url_map.iter_rules():
            if "GET" in rule.methods and "<" not in rule.rule and len(rule.arguments) == 0:
                if "/building-blocks" not in rule.rule and "/tutorials" not in rule.rule:
                    add_url_element(urlset, f"{base_url}{rule.rule}", priority="0.5")
    
    tree = ET.ElementTree(urlset)
    tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)

def load_popular_pages(app):
# Load pages.json
    json_path = os.path.join(app.static_folder, 'json', 'pages.json')
    with open(json_path, 'r') as f:
        return json.load(f)
    
def cards_data_homepage(app):
# Load cards.json
    json_path = os.path.join(app.static_folder, 'json', 'cards.json')
    with open(json_path, 'r') as f:
        return json.load(f)