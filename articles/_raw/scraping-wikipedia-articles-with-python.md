---
title: How to Scrape Wikipedia Articles with Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-24T17:24:24.000Z'
originalURL: https://freecodecamp.org/news/scraping-wikipedia-articles-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/artem-maltsev-vgQFlPq8tVQ-unsplash-1.jpg
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: null
seo_desc: "By Dirk Hoekstra\nIn this article I'm going to create a web scraper in\
  \ Python that will scrape Wikipedia pages. \nThe scraper will go to a Wikipedia\
  \ page, scrape the title, and follow a random link to the next Wikipedia page.\n\
  I think it will be fun to ..."
---

By Dirk Hoekstra

In this article I'm going to create a web scraper in Python that will scrape Wikipedia pages. 

The scraper will go to a Wikipedia page, scrape the title, and follow a random link to the next Wikipedia page.

I think it will be fun to see what random Wikipedia pages this scraper will visit!

## Setting up the scraper

To start, I'm going to create a new python file called `scraper.py`:

```
touch scraper.py
```

To make the HTTP request, I'm going to use the `requests` library. You can install it with the following command:

```
pip install requests
```

Let's use the web scraping wiki page as our starting point:

```python
import requests

response = requests.get(
	url="https://en.wikipedia.org/wiki/Web_scraping",
)
print(response.status_code)

```

When running the scraper, it should display a 200 status code:

```
python3 scraper.py
200
```

Alright, so far so good! ?

## Extracting data from the page

Let's extract the title from the HTML page. To make my life easier I'm going to use the BeautifulSoup package for this.

```
pip install beautifulsoup4
```

When inspecting the Wikipedia page I see that the title tag has the `#firstHeading` ID.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screen-Shot-2020-08-23-at-4.10.44-PM.png)

Beautiful soup allows you to find an element by the ID tag.

```python
title = soup.find(id="firstHeading")
```

Bringing it all together the program now looks like this:

```python
import requests
from bs4 import BeautifulSoup

response = requests.get(
	url="https://en.wikipedia.org/wiki/Web_scraping",
)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading")
print(title.string)

```

And when running this, it shows the title of the Wiki article: ?

```
python3 scraper.py
Web scraping
```

## Scraping other links

Now I'm going to dive deep into Wikipedia. I'm going to grab a random `<a>` tag to another Wikipedia article and scrape that page.

To do this I will use beautiful soup to find all the `<a>` tags within the wiki article. Then I shuffle the list to make it random. 

```python
import requests
from bs4 import BeautifulSoup
import random

response = requests.get(
	url="https://en.wikipedia.org/wiki/Web_scraping",
)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading")
print(title.content)

# Get all the links
allLinks = soup.find(id="bodyContent").find_all("a")
random.shuffle(allLinks)
linkToScrape = 0

for link in allLinks:
	# We are only interested in other wiki articles
	if link['href'].find("/wiki/") == -1: 
		continue

	# Use this link to scrape
	linkToScrape = link
	break

print(linkToScrape)
```

As you can see, I use the `soup.find(id="bodyContent").find_all("a")` to find all the `<a>` tags within the main article. 

Since I'm only interested in links to other wikipedia articles, I make sure the link contains the `/wiki` prefix.

When running the program now it displays a link to another wikipedia article, nice!

```
python3 scraper.py
<a href="/wiki/Link_farm" title="Link farm">Link farm</a>
```

## Creating an endless scraper

Alright, let's make the scraper actually scrape the new link.

To do this I'm going to move everything into a `scrapeWikiArticle` function.

```python
import requests
from bs4 import BeautifulSoup
import random

def scrapeWikiArticle(url):
	response = requests.get(
		url=url,
	)
	
	soup = BeautifulSoup(response.content, 'html.parser')

	title = soup.find(id="firstHeading")
	print(title.text)

	allLinks = soup.find(id="bodyContent").find_all("a")
	random.shuffle(allLinks)
	linkToScrape = 0

	for link in allLinks:
		# We are only interested in other wiki articles
		if link['href'].find("/wiki/") == -1: 
			continue

		# Use this link to scrape
		linkToScrape = link
		break

	scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])

scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")
```

The `scrapeWikiArticle` function will get the wiki article, extract the title, and find a random link. 

Then, it will call the `scrapeWikiArticle` again with this new link. Thus, it creates an endless cycle of a Scraper that bounces around on wikipedia. 

Let's run the program and see what we get:

```
pythron3 scraper.py
Web scraping
Digital object identifier
ISO 8178
STEP-NC
ISO/IEC 2022
EBCDIC 277
Code page 867
Code page 1021
EBCDIC 423
Code page 950
G
R
Mole (unit)
Gram
Remmius Palaemon
Encyclopædia Britannica Eleventh Edition
Geography
Gender studies
Feminism in Brazil
```

Awesome, in roughly 10 steps we went from "Web Scraping" to "Feminism in Brazil". Amazing!

## Conclusion

We've built a web scraper in Python that scrapes random Wikipedia pages. It bounces around endlessly on Wikipedia by following random links.

This is a fun gimmick and Wikipedia is pretty lenient when it comes to web scraping. 

There are also harder to scrape websites such as Amazon or Google. If you want to scrape such a website, you should set up a system with [headless Chrome browsers](https://github.com/puppeteer/puppeteer) and proxy servers. Or you can use a service that handles all that for you [like this one](https://scraperbox.com).

But be careful not to abuse websites, and only scrape data that you are allowed to scrape.

Happy coding!

