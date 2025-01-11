# Flask libraries
from flask import Flask, render_template, request, redirect, abort, render_template_string, send_from_directory, send_file
from flask_assets import Environment, Bundle
from flask_compress import Compress

# Base Libraries
from datetime import datetime
import os

# Models
from models import db, articles, Contributors, blogs, Topics

# Functions and Utilities
from functions import build_data_dict, fetch_contributions_for_the_single_contributor, generate_table_of_contents, \
    get_breadcrumbs, find_related_articles, calculate_reading_time, \
    fetch_meta_data, recently_published, generate_sitemap, \
    load_popular_pages, cards_data_homepage
from html_parser import htmlize, r_to_html_plaintext
from utils import get_git_commit_hash

# Redirects 
from redirectstsh import setup_redirects
import redirects_config
 
# Initialize App
app = Flask(__name__, static_url_path='/static')

# Text Compression
app.config['COMPRESS_ALGORITHM'] = 'br'  
Compress(app)

# Git Hash Injector
@app.context_processor
def inject_git_commit_hash():
    return {'git_commit_hash': get_git_commit_hash()}

# DB
db_filename = 'tsh.db'
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), db_filename))
db_uri = f'sqlite:///{db_path}'  

# Root URL
base_url = 'https://tilburgsciencehub.com'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Templates and assets
app.config['TEMPLATES_AUTO_RELOAD'] = False # Only true when Debugging
app.config['CACHE'] = True  # Only false when Debugging
app.config['ASSETS_DEBUG'] = False  # Only true for Debugging

# Security settings
app.config['SESSION_COOKIE_SECURE'] = True  # Only false when Debugging
app.config['REMEMBER_COOKIE_SECURE'] = True  # Only false when Debugging
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Only false when Debugging
app.config['REMEMBER_COOKIE_HTTPONLY'] = True  # Only false when Debugging

# Initialize SQLAlchemy with the app
db.init_app(app)

# Build & Register SCSS Bundle
assets = Environment(app)
scss_bundle = Bundle(
    'scss/bootstrap.scss',  
    output='css/main.css',
    filters='scss',
)
assets.register('scss_all', scss_bundle)

# Inject all routes with dependent variables
@app.context_processor
def inject_data():
    with app.app_context():
        # Execute function to load data
        data_dict = build_data_dict(Contributors, blogs, Topics, articles)
        popular_pages = load_popular_pages(app)
        
    return dict(data_dict=data_dict, popular_pages=popular_pages)

# Custom filter for dates
@app.template_filter('formatdate')
def formatdate(value, format="%Y-%m-%d"):
    if value is None:
        return ""
    date = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S%z")
    return date.strftime(format)

# Home Page
@app.route('/')
def home():

    # Meta Data
    data_object = {'title' : 'Home'}
    meta_data = fetch_meta_data(data_object)

    # Cards data
    cards_data = cards_data_homepage(app)

    
    recent_articles = recently_published(articles, Topics)

    return render_template('index.html', assets=assets, meta_data=meta_data, recent_articles=recent_articles, cards_data=cards_data)

# Single Example
@app.route('/examples/<article_path>')
def example(article_path):
    
    breadcrumbs = get_breadcrumbs()
    current_url = request.url
    article = None
    article = articles.query.filter_by(path=article_path).first()
    meta_data = fetch_meta_data(article)
    if article:
        example = article
        content = htmlize(example.content)
        table_of_contents = generate_table_of_contents(content)

    return render_template('examples-single.html', breadcrumbs=breadcrumbs, assets=assets, example=example, current_url=current_url, table_of_contents=table_of_contents, content=content, meta_data=meta_data)

# Single Blog
@app.route('/blog/<blog_path>')
def blogs_single(blog_path):
    
    breadcrumbs = get_breadcrumbs()
    blog_query = None
    blog_data = None
    blog_query = blogs.query.filter_by(path=blog_path).first()
    meta_data = fetch_meta_data(blog_query)
    if blog_query:
        blog_data = blog_query
        content = htmlize(blog_query.content)
        table_of_contents = generate_table_of_contents(content)

    return render_template('blog-single.html', assets=assets, breadcrumbs=breadcrumbs, blog=blog_data, table_of_contents=table_of_contents, content=content, meta_data=meta_data)

# Still needs metadata!
# List Topics
@app.route('/topics')
def topics_list():
    
    return render_template('topics-list.html', assets=assets)

# Still needs metadata!
# First Level Topic
@app.route('/topics/<first_level_topic_path>/')
def topics_first_level(first_level_topic_path):
    

    return render_template('first-level-topic.html', assets=assets, topic_path=first_level_topic_path)

# Still needs metadata!
# Second Level Topic
@app.route('/topics/<first_level_topic_path>/<second_level_topic_path>/')
def topics_second_level(first_level_topic_path,second_level_topic_path):
    
    
    return render_template('second-level-topic.html', assets=assets, topic_path=first_level_topic_path, sec_level_topic_path=second_level_topic_path)

# Still needs metadata!
# Third Level Topic
@app.route('/topics/<first_level_topic_path>/<second_level_topic_path>/<third_level_topic_path>/')
def topics_third_level(first_level_topic_path,second_level_topic_path, third_level_topic_path):
    
    
    return render_template('third-level-topic.html', assets=assets, topic_path=first_level_topic_path, sec_level_topic_path=second_level_topic_path, third_level_topic_path=third_level_topic_path)

# Single Article (Topic)
@app.route('/topics/<first_level_topic_path>/<second_level_topic_path>/<third_level_topic_path>/<article_path>/')
def topic_single(first_level_topic_path, second_level_topic_path, third_level_topic_path, article_path):
    
    breadcrumbs = get_breadcrumbs()
    current_url = request.url
    article = None
    article = articles.query.filter_by(path=article_path).first()
    meta_data = fetch_meta_data(article)
    related_articles = None
    table_of_contents = None
    content = None
    reading_time = 0
    if article is None:
        file_path = 'content/topics/' + first_level_topic_path + '/' + second_level_topic_path + '/' + third_level_topic_path + '/' + article_path
        ## open file and retrieve R code content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        code_content = r_to_html_plaintext(content)
        return render_template('code_topic.html', content=code_content)
    else: 
        related_articles = find_related_articles(article_path, articles, Topics)
        content = htmlize(article.content)
        table_of_contents = generate_table_of_contents(content)
        if (len(content) > 0):
            reading_time = calculate_reading_time(article.content)

    return render_template('topic-single.html', breadcrumbs=breadcrumbs, assets=assets, article=article, current_url=current_url, table_of_contents=table_of_contents, content=content, reading_time=reading_time, meta_data=meta_data, related_articles=related_articles)

# List Examples
@app.route('/examples')
def examples():

    # Meta Data
    data_object = {'title' : 'Examples'}
    meta_data = fetch_meta_data(data_object)

    
    print(data_dict)
    return render_template('examples-list.html', assets=assets, meta_data=meta_data)

# List Blogs
@app.route('/blog')
def blog():

    # Meta Data
    data_object = {'title' : 'Blog'}
    meta_data = fetch_meta_data(data_object)

    
    blogs_data = blogs.query.all()

    # Lus door de lijst en formatteer de datum in elk item
    for blog in blogs_data:
        if blog.date:
            # Scheid de tijdzone-informatie
            date_parts = blog.date.split("+")
            date_without_timezone = date_parts[0]

            # Converteer naar een datumobject
            date_object = datetime.strptime(
                date_without_timezone, "%Y-%m-%dT%H:%M:%S")

            # Formateer de datum naar het gewenste formaat
            blog.formatted_date = date_object.strftime("%B %d, %Y")
        else:
            blog.formatted_date = None

    return render_template('blog-list.html', assets=assets, blogs_data=blogs_data, meta_data=meta_data)

# About
@app.route('/about')
def about():

    # Meta Data
    data_object = {'title' : 'About Us'}
    meta_data = fetch_meta_data(data_object)

    
    return render_template('about.html', assets=assets, meta_data=meta_data)

# Contribute
@app.route('/contribute')
def contribute():

    # Meta Data
    data_object = {'title' : 'Contribute to TSH'}
    meta_data = fetch_meta_data(data_object)

    return redirect('topics/Collaborate-share/Project-management/contribute-to-tilburg-science-hub/contribute/')

# Search Page
@app.route('/search')
def search():

    # Meta Data
    data_object = {'title' : 'Search'}
    meta_data = fetch_meta_data(data_object)

    
    return render_template('search.html', assets=assets, meta_data=meta_data)

# Contributors
@app.route('/contributors')
def contributors():

    # Meta Data
    data_object = {'title' : 'Contributors'}
    meta_data = fetch_meta_data(data_object)

    
    contributors_list = Contributors.query.all()
    return render_template('contributors-list.html', assets=assets, contributors_list=contributors_list, meta_data=meta_data)

# Still needs metadata!
# Single Contributor
@app.route('/contributors/<contributor_path>')
def contributor(contributor_path):
    
    contributor_single = Contributors.query.filter_by(
        path=contributor_path).first()
    
    if contributor_single is None:
        abort(404)
    
    contributions = fetch_contributions_for_the_single_contributor(contributor_single, articles, Topics)

    return render_template('contributors-single.html', assets=assets, contributor_single=contributor_single, contributions=contributions)

# Custom redirects
@app.route('/<path:path>', methods=['GET'])
def handle_redirect(path):
    
    redirect_info = redirects_config.REDIRECTS.get(f"/{path}")
    if redirect_info:
        new_url = redirect_info["url"]
        title = redirect_info.get("title")  # Gebruik .get() om None te krijgen als er geen titel is

        if title:
            # Render de redirect template met een titel
            return render_template('redirect.html', new_url=new_url, title=title, assets=assets)
        else:
            # Direct redirecten als er geen titel is
            return redirect(new_url, code=302)
    else:
        return render_template('404.html', assets=assets), 404

# Robots.txt
@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.static_folder, "robots.txt")

# Still needs metadata!
# Error Handler 404
@app.errorhandler(404)
def page_not_found(e):
    
    return render_template('404.html', assets=assets), 404

@app.route('/sitemap.xml')
def sitemap():
    # Pad naar de gegenereerde sitemap.xml
    sitemap_path = 'sitemap.xml'
    
    # Return het sitemap.xml bestand
    return send_file(sitemap_path, mimetype='application/xml')


# Sitemap without redirects
with app.app_context():
    data_dict = build_data_dict(Contributors, blogs, Topics, articles)
    sitemap = generate_sitemap(app, data_dict, base_url=base_url)

# Redirects
setup_redirects(app)

# Run App
if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG', False), host='0.0.0.0', port=8080)