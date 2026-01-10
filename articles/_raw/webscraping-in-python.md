---
title: How to Scrape Websites with Python 3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-17T22:51:00.000Z'
originalURL: https://freecodecamp.org/news/webscraping-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9af8740569d1a4ca28f1.jpg
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: null
seo_desc: 'By André Jaenisch

  Web scraping is the process of extracting data from websites.

  Before attempting to scrape a website, you should make sure that the provider allows
  it in their terms of service. You should also check to see whether you could use
  an A...'
---

By André Jaenisch

Web scraping is the process of extracting data from websites.

Before attempting to scrape a website, you should make sure that the provider allows it in their terms of service. You should also check to see whether you could use an API instead.

Massive scraping can put a server under a lot of stress which can result in a denial of service. And you don't want that.

## Who should read this?

This article is for advanced readers. It will assume that you are already familiar with the Python programming language.

At the very minimum you should understand list comprehension, context manager, and functions. You should also know how to set up a virtual environment.

We'll run the code on your local machine to explore some websites. With some tweaks you could make it run on a server as well.

## What you will learn in this article

At the end of this article, you will know how to download a webpage, parse it for interesting information, and format it in a usable format for further processing. This is also known as [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load).

This article will also explain what to do if that website is using JavaScript to render content (like React.js or Angular).

## Prerequisites

Before I can start, I want to make sure we're ready to go. Please set up a virtual environment and install the following packages into it:

* beautifulsoup4 (version 4.9.0 at time of writing)
* requests (version 2.23.0 at time of writing)
* wordcloud (version 1.17.0 at time of writing, optional)
* selenium (version 3.141.0 at time of writing, optional)

You can find the code for this project in this [git repository on GitHub](https://github.com/Ryuno-Ki/fcc-web-scraping-example).

For this example, we are going to scrape the [Basic Law for the Federal Republic of Germany](https://www.gesetze-im-internet.de/gg/index.html). (Don't worry, I checked their Terms of Service. They offer an XML version for machine processing, but this page serves as an example of processing HTML. So it should be fine.)

## Step 1: Download the source

First things first: I create a file `urls.txt` holding all the URLs I want to download:

```
https://www.gesetze-im-internet.de/gg/art_1.html
https://www.gesetze-im-internet.de/gg/art_2.html
https://www.gesetze-im-internet.de/gg/art_3.html
https://www.gesetze-im-internet.de/gg/art_4.html
https://www.gesetze-im-internet.de/gg/art_5.html
https://www.gesetze-im-internet.de/gg/art_6.html
https://www.gesetze-im-internet.de/gg/art_7.html
https://www.gesetze-im-internet.de/gg/art_8.html
https://www.gesetze-im-internet.de/gg/art_9.html
https://www.gesetze-im-internet.de/gg/art_10.html
https://www.gesetze-im-internet.de/gg/art_11.html
https://www.gesetze-im-internet.de/gg/art_12.html
https://www.gesetze-im-internet.de/gg/art_12a.html
https://www.gesetze-im-internet.de/gg/art_13.html
https://www.gesetze-im-internet.de/gg/art_14.html
https://www.gesetze-im-internet.de/gg/art_15.html
https://www.gesetze-im-internet.de/gg/art_16.html
https://www.gesetze-im-internet.de/gg/art_16a.html
https://www.gesetze-im-internet.de/gg/art_17.html
https://www.gesetze-im-internet.de/gg/art_17a.html
https://www.gesetze-im-internet.de/gg/art_18.html
https://www.gesetze-im-internet.de/gg/art_19.html
```

Next, I write a bit of Python code in a file called `scraper.py` to download the HTML of this files. 

In a real scenario, this would be too expensive and you'd use a database instead. To keep things simple, I'll download files into the same directory next to the store and use their name as the filename.

```py
from os import path
from pathlib import PurePath

import requests

with open('urls.txt', 'r') as fh:
    urls = fh.readlines()
urls = [url.strip() for url in urls]  # strip `\n`

for url in urls:
    file_name = PurePath(url).name
    file_path = path.join('.', file_name)
    text = ''

    try:
        response = requests.get(url)
        if response.ok:
            text = response.text
    except requests.exceptions.ConnectionError as exc:
        print(exc)
    
    with open(file_path, 'w') as fh:
        fh.write(text)

    print('Written to', file_path)
```

By downloading the files, I can process them locally as much as I want without being dependent on a server. Try to be a good web citizen, okay?

## Step 2: Parse the source

Now that I've downloaded the files, it's time to extract their interesting features. Therefore I go to one of the pages I downloaded, open it in a web browser, and hit Ctrl-U to view its source. Inspecting it will show me the HTML structure.

In my case, I figured I want the text of the law without any markup. The element wrapping it has an id of `container`. Using BeautifulSoup I can see that a combination of [`find`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find) and `[get_text](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#get-text)` will do what I want.

Since I have a second step now, I'm going to refactor the code a bit by putting it into functions and add a minimal CLI.

```py
from os import path
from pathlib import PurePath
import sys

from bs4 import BeautifulSoup
import requests


def download_urls(urls, dir):
    paths = []

    for url in urls:
        file_name = PurePath(url).name
        file_path = path.join(dir, file_name)
        text = ''

        try:
            response = requests.get(url)
            if response.ok:
                text = response.text
            else:
                print('Bad response for', url, response.status_code)
        except requests.exceptions.ConnectionError as exc:
            print(exc)
    
        with open(file_path, 'w') as fh:
            fh.write(text)

        paths.append(file_path)

    return paths

def parse_html(path):
    with open(path, 'r') as fh:
        content = fh.read()

    return BeautifulSoup(content, 'html.parser')

def download(urls):
    return download_urls(urls, '.')

def extract(path):
    return parse_html(path)

def transform(soup):
    container = soup.find(id='container')
    if container is not None:
        return container.get_text()

def load(key, value):
    d = {}
    d[key] = value
    return d

def run_single(path):
    soup = extract(path)
    content = transform(soup)
    unserialised = load(path, content.strip() if content is not None else '')
    return unserialised

def run_everything():
    l = []

    with open('urls.txt', 'r') as fh:
        urls = fh.readlines()
    urls = [url.strip() for url in urls]

    paths = download(urls)
    for path in paths:
        print('Written to', path)
        l.append(run_single(path))

    print(l)

if __name__ == "__main__":
    args = sys.argv

    if len(args) is 1:
      run_everything()
    else:
        if args[1] == 'download':
            download([args[2]])
            print('Done')
        if args[1] == 'parse':
            path = args[2]
            result = run_single(path)
            print(result)

```

Now I can run the code in three ways:

1. Without any arguments to run everything (that is, download all URLs and extract them, then save to disk) via: `python scraper.py`
2. With an argument of `download` and a url to download `python scraper.py download https://www.gesetze-im-internet.de/gg/art_1.html`. This will not process the file.
3. With an argument of `parse` and a filepath to parse: `python scraper.py art_1.html`. This will skip the download step.

With that, there's one last thing missing.

## Step 3: Format the source for further processing

Let's say I want to generate a word cloud for each article. This can be a quick way to get an idea about what a text is about. For this, install the package `wordcloud` and update the file like this:

```py
from os import path
from pathlib import Path, PurePath
import sys

from bs4 import BeautifulSoup
import requests
from wordcloud import WordCloud

STOPWORDS_ADDENDUM = [
    'Das',
    'Der',
    'Die',
    'Diese',
    'Eine',
    'In',
    'InhaltsverzeichnisGrundgesetz',
    'im',
    'Jede',
    'Jeder',
    'Kein',
    'Sie',
    'Soweit',
    'Über'
]
STOPWORDS_FILE_PATH = 'stopwords.txt'
STOPWORDS_URL = 'https://raw.githubusercontent.com/stopwords-iso/stopwords-de/master/stopwords-de.txt'


def download_urls(urls, dir):
    paths = []

    for url in urls:
        file_name = PurePath(url).name
        file_path = path.join(dir, file_name)
        text = ''

        try:
            response = requests.get(url)
            if response.ok:
                text = response.text
            else:
                print('Bad response for', url, response.status_code)
        except requests.exceptions.ConnectionError as exc:
            print(exc)
    
        with open(file_path, 'w') as fh:
            fh.write(text)

        paths.append(file_path)

    return paths

def parse_html(path):
    with open(path, 'r') as fh:
        content = fh.read()

    return BeautifulSoup(content, 'html.parser')

def download_stopwords():
    stopwords = ''

    try:
        response = requests.get(STOPWORDS_URL)
        if response.ok:
            stopwords = response.text
        else:
            print('Bad response for', url, response.status_code)
    except requests.exceptions.ConnectionError as exc:
        print(exc)

    with open(STOPWORDS_FILE_PATH, 'w') as fh:
        fh.write(stopwords)

    return stopwords

def download(urls):
    return download_urls(urls, '.')

def extract(path):
    return parse_html(path)

def transform(soup):
    container = soup.find(id='container')
    if container is not None:
        return container.get_text()

def load(filename, text):
    if Path(STOPWORDS_FILE_PATH).exists():
        with open(STOPWORDS_FILE_PATH, 'r') as fh:
            stopwords = fh.readlines()
    else:
        stopwords = download_stopwords()

    # Strip whitespace around
    stopwords = [stopword.strip() for stopword in stopwords]
    # Extend stopwords with own ones, which were determined after first run
    stopwords = stopwords + STOPWORDS_ADDENDUM

    try:
        cloud = WordCloud(stopwords=stopwords).generate(text)
        cloud.to_file(filename.replace('.html', '.png'))
    except ValueError:
        print('Could not generate word cloud for', key)

def run_single(path):
    soup = extract(path)
    content = transform(soup)
    load(path, content.strip() if content is not None else '')

def run_everything():
    with open('urls.txt', 'r') as fh:
        urls = fh.readlines()
    urls = [url.strip() for url in urls]

    paths = download(urls)
    for path in paths:
        print('Written to', path)
        run_single(path)
    print('Done')

if __name__ == "__main__":
    args = sys.argv

    if len(args) is 1:
      run_everything()
    else:
        if args[1] == 'download':
            download([args[2]])
            print('Done')
        if args[1] == 'parse':
            path = args[2]
            run_single(path)
            print('Done')
```

What changed? For one, I downloaded a [list of German stopwords](https://github.com/stopwords-iso/stopwords-de/) from GitHub. This way, I can eliminate the most common words from the downloaded law text.

Then I instantiate a WordCloud instance with the list of stopwords I downloaded and the text of the law. It will be turned into an image with the same basename.

After the first run, I discover that the list of stopwords is incomplete. So I add additional words I want to exclude from the resulting image.

With that, the main part of web scraping is complete.

## Bonus: What about SPAs?

SPAs - or Single Page Applications - are web applications where the whole experience is controlled by JavaScript, which is executed in the browser. As such, downloading the HTML file does not bring us far. What should we do instead?

We'll use the browser. With Selenium. Make sure to [install a driver](https://selenium-python.readthedocs.io/installation.html#drivers) also. Download the .tar.gz archive and unpack it in the `bin` folder of your virtual environment so it will be found by Selenium. That is the directory where you can find the `activate` script (on GNU/Linux systems).

As an example, I am using the [Angular website](https://angular.io/) here. Angular is a popular SPA-Framework written in JavaScript and guaranteed to be controlled by it for the time being.

Since the code will be slower, I create a new file called `crawler.py` for it. The content looks like this:

```py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wordcloud import WordCloud

def extract(url):
    elem = None
    driver = webdriver.Firefox()
    driver.get(url)

    try:
        found = WebDriverWait(driver, 10).until(
            EC.visibility_of(
                driver.find_element(By.TAG_NAME, "article")
            )
        )
        # Make a copy of relevant data, because Selenium will throw if
        # you try to access the properties after the driver quit
        elem = {
          "text": found.text
        }
    finally:
        driver.close()

    return elem

def transform(elem):
    return elem["text"]
        
def load(text, filepath):
    cloud = WordCloud().generate(text)
    cloud.to_file(filepath)

if __name__ == "__main__":
    url = "https://angular.io/"
    filepath = "angular.png"

    elem = extract(url)
    if elem is not None:
        text = transform(elem)
        load(text, filepath)
    else:
        print("Sorry, could not extract data")
```

Here, Python is opening a Firefox instance, browsing the website and looking for an `<article>` element. It is copying over its text into a dictionary, which gets read out in the `transform` step and turned into a WordCloud during `load`. 

When dealing with JavaScript-heavy sites, it is often useful to use [Waits](https://selenium-python.readthedocs.io/waits.html) and perhaps run even `[execute_script](https://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webdriver.WebDriver.execute_script)`to defer to JavaScript if needed.

## Summary

Thanks for reading this far! Let's summarise what we've learned now:

1. How to scrape a website with Python's `requests` package.
2. How to translate it into a meaningful structure using `beautifulsoup`.
3. How to further process that structure into something you can work with.
4. What to do if the target page is relying on JavaScript.

## Further reading

If you want to find more about me, you can [follow me on Twitter](https://twitter.com/AndreJaenisch) or visit [my website](https://jaenis.ch/).

I'm not the first one who wrote about Web Scraping here on freeCodeCamp. Yasoob Khalid and Dave Gray also did so in the past:

%[https://www.freecodecamp.org/news/an-intro-to-web-scraping-with-lxml-and-python-b02b7a3f3098/]

%[https://www.freecodecamp.org/news/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251/]


