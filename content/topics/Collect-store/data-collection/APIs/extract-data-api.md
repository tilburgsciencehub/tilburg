---
title: "Extract Data From APIs"
description: "Learn how to extract data from APIs."
keywords: "api, application programming interface, data collection"
#weight: 4
#date: 2020-11-11T22:02:51+05:30
draft: false
icon: "fa-solid fa-database"
category: "reproducible"
aliases:
  - /use/api
  - /collect-data/extract-data-api
---

## Extracting Data From APIs

An Application Programming Interface (_API_) is a version of a website intended for computers, rather than humans, to talk to one another. APIs are everywhere, and most are used to _provide data_ (e.g., retrieve a user name and demographics), _functions_ (e.g., start playing music from Spotify, turn on your lamps in your "smart home"), or
_algorithms_ (e.g., submit an image, retrieve a written text for what's on the image).

APIs work similarly to websites. At the core, you obtain code that computers can easily understand to process the content of a website, instead of obtaining the source code of a rendered website. APIs provide you with simpler and more scalable ways to obtain data, so you must understand how they work.

{{% warning %}}
In practice, most APIs require user authentication to get started. Each API has its workflow to generate a kind of "password" that you need to include in your requests. Therefore, you should always consult the documentation of the API you plan on using for configuration instructions. In this building block, we cover some of the common themes you encounter when working with APIs and provide examples.
{{% /warning %}}

{{% tip %}}
One of the major advantages of APIs is that you can directly access the data you need without all the hassle of selecting the right HTML tags. Another advantage is that you can often customize your API request (e.g., the first 100 comments or only posts about science), which may not always be possible in the web interface.
Last, using APIs is legitimized by a website (mostly, you will have to pay a license fee to use APIs!). So it's a more stable and legit way to retrieve web data compared to web scraping. That's also why we recommend using an API whenever possible.
In practice, though, APIs really can't give you all the data you possibly want, and web scraping allows you to access complementary data (e.g., viewable on a website or somewhere hidden in the source code). See our tutorial [web-scraping and api mining](https://tilburgsciencehub.com/topics/collect-store/data-collection/web-scraping/web-scraping-tutorial/) for all the details.

{{% /tip %}}

## Examples

### icanhazdadjoke

Every time you visit the [site](https://icanhazdadjoke.com), the site shows a random joke. From a technical perspective, each time a user opens the site, a little software program on the server makes an API call to the daddy joke API to draw a new joke to be displayed. Note that this is one of the few APIs that does not require any authentication.

{{% codeblock %}}

```Python
import requests
search_url = "https://icanhazdadjoke.com/search"

response = requests.get(search_url,
                        headers={"Accept": "application/json"},
                        params={"term": "cat"})
joke_request = response.json()
print(joke_request)
```

{{% /codeblock %}}

_Multiple seeds_  
Rather than having a fixed endpoint like the one above (e.g., always search for cat jokes), you can restructure your code to allow for variable input. For example, you may want to create a function `search_api()` that takes an input parameter `search_term` that you can assign any value you want.

{{% codeblock %}}

```Python
def search_api(search_term):
  search_url = "https://icanhazdadjoke.com/search"
  response = requests.get(search_url,
                        headers={"Accept": "application/json"},
                        params={"term": search_term})
  return response.json()

search_api("dog")
search_api("cow")
```

{{% /codeblock %}}

_Pagination_  
Transferring data is costly - not strictly in a monetary sense, but in time. So - APIs are typically very greedy in returning data. Ideally, they only produce a very targeted data point that is needed for the user to see. It saves the website owner from paying for bandwidth and guarantees that the site responds fast to user input.

By default, each page contains 20 jokes, where page 1 shows jokes 1 to 20, page 2 jokes 21 to 40, ..., and page 33 jokes 641 to 649.

You can adjust the number of results on each page (max. 30) with the limit parameter (e.g., `params={"limit": 10}`). In practice, almost every API on the web limits the results of an API call (100 is also a common cap). As an alternative, you can specify the current page number with the `page` parameter (e.g., `params={"term": "", "page": 2}`).

### Reddit

Reddit is a widespread American social news aggregation and discussion site. The service uses an API to generate the website's content and grants public access to the API.

To request data from the Reddit API, we need to include headers in our request. HTTP headers are a vital part of any API request, containing meta-data associated with the request (e.g., type of browser, language, expected data format, etc.).

{{% codeblock %}}

```python
import requests
url = 'https://www.reddit.com/r/marketing/about/moderators/.json'

headers = {'authority': 'www.reddit.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

response = requests.get(url, headers=headers)
json_response = response.json()
```

{{% /codeblock %}}

## See Also

- The Spotify Web API [tutorial](https://github.com/hannesdatta/course-odcm/blob/master/content/docs/project/resources/tutorials/apisadvanced/api-advanced.ipynb) used in the Online Data Management Collection course illustrates how to generate access tokens and use a variety of API endpoints.
