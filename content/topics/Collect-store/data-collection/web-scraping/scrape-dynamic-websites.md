---
title: "Scrape Dynamic Websites"
description: "Learn how to web scrape from dynamic websites with python. Install Selenium and make it work for Chromedriver without websites blocking you"
keywords: "scrape, webscraping, internet, beautifulsoup, website, Selenium, Chromedriver, chromedrive, dynamic website, data extraction"
weight: 2
#date: 2020-11-11T22:02:51+05:30
draft: false
aliases:
  - /scrape/dynamic-website
  - /collect-data/scrape-dynamic-websites
---

## Scrape Dynamic Websites

While it's easy to get started with Beautifulsoup, it has limitations when it comes to _scraping dynamic websites_. That is websites of which the content changes after each page refresh. Selenium can handle both static and dynamic websites and mimic user behavior (e.g., scrolling, clicking, logging in). It launches another web browser window in which all actions are visible which makes it feel more intuitive. Here we outline the basic commands and installation instructions to get you started.

## Code

### Install Selenium and make it work for Chromedriver

{{% warning %}}
The first time you will need to:

1. Install the Python package for **selenium** by typing in the command `pip install selenium`. Alternatively, open Anaconda Prompt (Windows) or the Terminal (Mac), type the command `conda install selenium`, and agree to whatever the package manager wants to install or update (usually by pressing `y` to confirm your choice).

2. Download a web driver to interface with a web browser, we recommend the **Webdriver Manager for Python**. Install it by typing in the command `pip install webdriver-manager`

{{% /warning %}}

Once Selenium and webdriver manager are installed, you can now install ChromeDriver as follows:

{{% codeblock %}}

```Python
# Make Selenium and chromedriver work for a dynamic website (here: untappd.com)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://untappd.com/"
driver.get(url)

```

{{% /codeblock %}}

If you want to block all pop-ups automatically (e.g. cookie pop-ups), you can use the following code:

{{% codeblock %}}

```Python
# Make Selenium and chromedriver work for Untappd.com

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set Chrome Options
options = Options()
options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

```

{{% /codeblock %}}

{{% tip %}}
Want to run Chromedriver manually? Check our [page](https://tilburgsciencehub.com/topics/computer-setup/software-installation/python/configuring-python-for-webscraping/) on Configuring Python for Web Scraping  
{{% /tip %}}

### Finding content in a website's source code

Running the code snippet below starts a new Google Chrome browser (`driver`) and then navigates to the specified URL. In other words, you can follow along with what the computer does behind the screens. Next, you can obtain specific website elements by tag name (e.g., `h1` is a header), similar to BeautifulSoup.

{{% codeblock %}}

```Python
import selenium.webdriver
from selenium.webdriver.common.by import By

driver = selenium.webdriver.Chrome()
driver.get("https://www.google.com")

# Manually click on cookie accept before continuing

# retrieve first H1 header
print(driver.find_element(By.TAG_NAME,"h1").text)

# Alternatively, use BeautifulSoup to extract elements from the website's source code
from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source) # ensure that the site has fully been loaded
soup.find('h1').get_text()

```

{{% /codeblock %}}

#### Selectors

Alternatively, you can specify which elements to extract through attributes, classes, and identifiers:

{{% codeblock %}}

```Python
# HTML classes
driver.find_element(By.CLASS_NAME, "<CLASS_NAME>").text

# HTML identifiers ()
driver.find_element(By.ID,"<ID_NAME>").text

# XPath
driver.find_element(By.XPATH,"<XPATH>").text

```

{{% /codeblock %}}

{{% tip %}}
Within Google Inspector you can easily obtain the XPath by right-clicking on an element and selecting: "Copy" > "Copy XPath".
{{% /tip %}}

#### User interactions

One of the distinguishable features of Selenium is the ability to mimic user interactions which can be vital to get to the data you are after. For example, older tweets are only loaded once you scroll down the page.

{{% codeblock %}}

```Python
# scroll down the page
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# click on an element (e.g., button)
element_to_be_clicked = driver.find_element(By.CLASS_NAME, "<CLASS_NAME>").text
element_to_be_clicked.click()
```

{{% /codeblock %}}

## Advanced Use Case

### Task Scheduling

See the building block on [task automation](https://tilburgsciencehub.com/topics/automation/automation-tools/task-automation/task-scheduling/) on how to schedule the execution of the web scraper (e.g., every day). Keep in mind that this only works with Python scripts, so if you're currently working in a Jupyter Notebook you need to transform it into a `.py` file first.

## See Also

- Looking for a simple solution that does the job without any bells and whistles? Try out the BeautifulSoup package and follow our [web-scraping for static websites building block](/topics/collect-data/webscraping-apis/scrape-static-websites/).
