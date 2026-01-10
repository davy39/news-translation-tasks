---
title: Python Web Scraping Tutorial – How to Scrape Data From Any Website with Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-10T17:42:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-scrape-websites-with-python-2
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/how-to-scrape-data-from-any-website-with-python.jpg
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: null
seo_desc: 'By Sorin-Gabriel Marica

  Web scraping is the process of extracting specific data from the internet automatically.
  It has many use cases, like getting data for a machine learning project, creating
  a price comparison tool, or any other innovative idea t...'
---

By Sorin-Gabriel Marica

Web scraping is the process of extracting specific data from the internet automatically. It has many use cases, like getting data for a machine learning project, creating a price comparison tool, or any other innovative idea that requires an immense amount of data.

While you can theoretically do data extraction manually, the vast contents of the internet makes this approach unrealistic in many cases. So knowing how to build a web scraper can come in handy. 

This article’s purpose is to teach you how to create a web scraper in Python. You will learn how to inspect a website to prepare for scraping, extract specific data using BeautifulSoup, wait for JavaScript rendering using Selenium, and save everything in a new JSON or CSV file.

But first, I should warn you about the legality of web scraping. While the act of scraping is legal, the data you may extract can be illegal to use. Make sure that you're not messing with any:

* Copyrighted content – since it's someone's intellectual property, it's protected by law and you can't just reuse it.
* Personal data – if the information you gather can be used to identify a person, then it's considered personal data and for EU citizens, it's protected under the GDPR. Unless you have a lawful reason to store that data, it's better to just skip it altogether.

Generally speaking, you should always read a website's terms and conditions before scraping to make sure that you're not going against their policies. If you're ever unsure how to proceed, contact the site owner and ask for consent. 

## What Will You Need for Your Scraper?

To start building your own web scraper, you will first need to have [Python](https://www.python.org/downloads/) installed on your machine. Ubuntu 20.04 and other versions of Linux come with Python 3 pre-installed. 

To check if you already have Python installed on your device, run the following command:

```
python3 -v

```

If you have Python installed, you should receive an output like this:

```
Python 3.8.2
```

Also, for our web scraper, we will use the Python packages BeautifulSoup (for selecting specific data) and Selenium (for rendering dynamically loaded content). To install them, just run these commands:

```
pip3 install beautifulsoup4
```

and

```
pip3 install selenium
```

The final step it’s to make sure you [install Google Chrome](https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=en) and [Chrome Driver](https://chromedriver.chromium.org/downloads) on your machine. These will be necessary if we want to use Selenium to scrape dynamically loaded content.

## How to Inspect the Page

Now that you have everything installed, it’s time to start our scraping project in earnest. 

You should choose the website you want to scrape based on your needs. Keep in mind that each website structures its content differently, so you’ll need to adjust what you learn here when you start scraping on your own. Each website will require minor changes to the code.

For this article, I decided to scrape information about the first ten movies from the top 250 movies list from IMDb: [https://www.imdb.com/chart/top/](https://www.imdb.com/chart/top/). 

First, we will get the titles, then we will dive in further by extracting information from each movie’s page. Some of the data will require JavaScript rendering.

To start understanding the content’s structure, you should right-click on the first title from the list and then choose “Inspect Element”.

![Image](https://lh4.googleusercontent.com/e6DE3zczzQa-VSBIynK-fR4oyAjVbpx2PztpEDKbi3K0NII9_lFkFhGQmiOjc_-Y_Kg26cM3pecnSKNiPlLZGpntqVKUrcX9E4gDWaTsolWoCFzQ6EEhj3GruBvrlEIzrUffvdjU)

By pressing CTRL+F and searching in the HTML code structure, you will see that there is only one **<table>** tag on the page. This is useful as it gives us information about how we can access the data.

An HTML selector that will give us all of the titles from the page is **`table tbody tr td.titleColumn a`**. That’s because all titles are in an anchor inside a table cell with the class “titleColumn”. 

Using this CSS selector and getting the **innerText** of each anchor will give us the titles that we need. You can simulate that in the browser console from the new window you just opened and by using the JavaScript line:

```
document.querySelectorAll("table tbody tr td.titleColumn a")[0].innerText
```

You will see something like this:

![Image](https://lh4.googleusercontent.com/T1pgLUXJHX_s3gubDKvBjwkWeK1neZxiysoneD2Q1NU3Sj_pD8defdKorTlcsiiqShlmPDEeCu3Goo5T9CgzPKCml9dq_kCCu7KUyTx7uSrU8VN9QzJZhO6AwBM-kfQ8r0uNxbn9)

Now that we have this selector, we can start writing our Python code and extracting the information we need.

## How to Use BeautifulSoup to Extract Statically Loaded Content 

The movie titles from our list are static content. That’s because if you look into the page source (CTRL+U on the page or right-click and then choose View Page Source), you will see that the titles are already there.

Static content is usually easier to scrape as it doesn’t require JavaScript rendering. To extract the first ten titles on the list, we will use BeautifulSoup to get the content and then print it in the output of our scraper.

```python
import requests
from bs4 import BeautifulSoup
 
page = requests.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup
 
links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
first10 = links[:10] # Keep only the first 10 anchors
for anchor in first10:
    print(anchor.text) # Display the innerText of each anchor

```

The code above uses the selector we saw in the first step to extract the movie title anchors from the page. It then loops through the first ten and displays the innerText of each.

The output should look like this:

![Image](https://lh3.googleusercontent.com/RrmEldjCrbz7V1-o4r6UsKNuWkj_yD2cWwfyuMMbdnRn7lk9cI0yhMi85PK4NrvX7L2KY0pY8047f9CmAeXo1W51HvFENMPxxh36ACqu3kNKuoFNNfhB_WSCMntIB-UB0usEU2n5)

## How to Extract Dynamically Loaded Content

As technology advanced, websites started to load their content dynamically. This improves the page’s performance, the user's experience, and even removes an extra barrier for scrapers.

This complicates things, though, as the HTML retrieved from a simple request will not contain the dynamic content. Fortunately, with Selenium, we can simulate a request in the browser and wait for the dynamic content to be displayed.

### How to Use Selenium for Requests

You will need to know the location of your chromedriver. The following code is identical to the one presented in the second step, but this time we are using Selenium to make the request. We will still parse the page’s content using BeautifulSoup, as we did before.

```python
from bs4 import BeautifulSoup
from selenium import webdriver
 
option = webdriver.ChromeOptions()
# I use the following options as my machine is a window subsystem linux. 
# I recommend to use the headless option at least, out of the 3
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
# Replace YOUR-PATH-TO-CHROMEDRIVER with your chromedriver location
driver = webdriver.Chrome('YOUR-PATH-TO-CHROMEDRIVER', options=option)
 
driver.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
soup = BeautifulSoup(driver.page_source, 'html.parser') # Parsing content using beautifulsoup. Notice driver.page_source instead of page.content
 
links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
first10 = links[:10] # Keep only the first 10 anchors
for anchor in first10:
    print(anchor.text) # Display the innerText of each anchor

```

Don’t forget to replace “YOUR-PATH-TO-CHROMEDRIVER” with the location where you extracted the chromedriver. Also, you should notice that instead of **`page.content`**, when we are creating the BeautifulSoup object, we are now using **`driver.page_source`**, which provides the HTML content of the page.

### How to Extract Statically Loaded Content Using Selenium

Using the code from above, we can now access each movie page by calling the click method on each of the anchors.

```python
first_link = driver.find_elements_by_css_selector('table tbody tr td.titleColumn a')[0]
first_link.click()

```

This will simulate a click on the first movie’s link. However, in this case, I recommend that you continue using **`driver.get instead`**. This is because you will no longer be able to use the **`click()`** method after you go on a different page since the new page doesn't have links to the other nine movies.

As a result, after clicking on the first title from the list, you’d need to go back to the first page, then click on the second, and so on. This is a waste of performance and time. Instead, we will just use the extracted links and access them one by one.

For “The Shawshank Redemption”, the movie page will be [https://www.imdb.com/title/tt0111161/](https://www.imdb.com/title/tt0111161/). We will extract the movie’s year and duration from the page, but this time we will use Selenium’s functions instead of BeautifulSoup as an example. In practice, you can use either one, so pick your favorite.

To retrieve the movie’s year and duration, you should repeat the first step we went through here on the movie’s page. 

You will notice that you can find all of the information in the first element with the class **`ipc-inline-list`** (".ipc-inline-list" selector) and that all of the elements of the list contain the attribute **`role`** with the value **`presentation`** (the `[role=’presentation’]` selector).

```python
from bs4 import BeautifulSoup
from selenium import webdriver
 
option = webdriver.ChromeOptions()
# I use the following options as my machine is a window subsystem linux. 
# I recommend to use the headless option at least, out of the 3
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
# Replace YOUR-PATH-TO-CHROMEDRIVER with your chromedriver location
driver = webdriver.Chrome('YOUR-PATH-TO-CHROMEDRIVER', options=option)
 
page = driver.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
soup = BeautifulSoup(driver.page_source, 'html.parser') # Parsing content using beautifulsoup
 
totalScrapedInfo = [] # In this list we will save all the information we scrape
links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
first10 = links[:10] # Keep only the first 10 anchors
for anchor in first10:
    driver.get('https://www.imdb.com/' + anchor['href']) # Access the movie’s page
    infolist = driver.find_elements_by_css_selector('.ipc-inline-list')[0] # Find the first element with class ‘ipc-inline-list’
    informations = infolist.find_elements_by_css_selector("[role='presentation']") # Find all elements with role=’presentation’ from the first element with class ‘ipc-inline-list’
    scrapedInfo = {
        "title": anchor.text,
        "year": informations[0].text,
        "duration": informations[2].text,
    } # Save all the scraped information in a dictionary
    totalScrapedInfo.append(scrapedInfo) # Append the dictionary to the totalScrapedInformation list
    
print(totalScrapedInfo) # Display the list with all the information we scraped

```

### How to Extract Dynamically Loaded Content Using Selenium

The next big step in web scraping is extracting content that is loaded dynamically. You can find such content on each of the movie’s pages (such as [https://www.imdb.com/title/tt0111161/](https://www.imdb.com/title/tt0111161/)) in the Editorial Lists section. 

If you look using inspect on the page, you'll see that you can find the section as an element with the attribute **`data-testid`** set as **`firstListCardGroup-editorial`**. But if you look in the page source, you will not find this attribute value anywhere. That’s because the Editorial Lists section is loaded by IMDB dynamically.

In the following example, we will scrape the editorial list of each movie and add it to our current results of the total scraped information. 

To do that, we will import a few more packages that make it possible to wait for our dynamic content to load.

```python
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
option = webdriver.ChromeOptions()
# I use the following options as my machine is a window subsystem linux. 
# I recommend to use the headless option at least, out of the 3
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
# Replace YOUR-PATH-TO-CHROMEDRIVER with your chromedriver location
driver = webdriver.Chrome('YOUR-PATH-TO-CHROMEDRIVER', options=option)
 
page = driver.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
soup = BeautifulSoup(driver.page_source, 'html.parser') # Parsing content using beautifulsoup
 
totalScrapedInfo = [] # In this list we will save all the information we scrape
links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
first10 = links[:10] # Keep only the first 10 anchors
for anchor in first10:
    driver.get('https://www.imdb.com/' + anchor['href']) # Access the movie’s page 
    infolist = driver.find_elements_by_css_selector('.ipc-inline-list')[0] # Find the first element with class ‘ipc-inline-list’
    informations = infolist.find_elements_by_css_selector("[role='presentation']") # Find all elements with role=’presentation’ from the first element with class ‘ipc-inline-list’
    scrapedInfo = {
        "title": anchor.text,
        "year": informations[0].text,
        "duration": informations[2].text,
    } # Save all the scraped information in a dictionary
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='firstListCardGroup-editorial']")))  # We are waiting for 5 seconds for our element with the attribute data-testid set as `firstListCardGroup-editorial`
    listElements = driver.find_elements_by_css_selector("[data-testid='firstListCardGroup-editorial'] .listName") # Extracting the editorial lists elements
    listNames = [] # Creating an empty list and then appending only the elements texts
    for el in listElements:
        listNames.append(el.text)
    scrapedInfo['editorial-list'] = listNames # Adding the editorial list names to our scrapedInfo dictionary
    totalScrapedInfo.append(scrapedInfo) # Append the dictionary to the totalScrapedInformation list
    
print(totalScrapedInfo) # Display the list with all the information we scraped

```

For the previous example, you should get the following output:

![Image](https://lh4.googleusercontent.com/geHhbKeeP2ATtz-OnIx9MATB3UvXcrobnO4eUNOLrzQll9ebPlq_2PqKaT_oT6e-3h7NmRkRh_9mrDuSvuW3Wbs3sRi1iuM3paCa8HBpTqWrZuSQc8sIu5y4EVZ_5j-60TmPs71Z)

## How to Save the Scraped Content

Now that we have all the data we want, we can save it as a .json or a .csv file for easier readability. 

To do that, we will just use the JSON and CVS packages from Python and write our content to new files:

```python
import csv
import json
 
...
        
file = open('movies.json', mode='w', encoding='utf-8')
file.write(json.dumps(totalScrapedInfo))
 
writer = csv.writer(open("movies.csv", 'w'))
for movie in totalScrapedInfo:
    writer.writerow(movie.values())

```

## Scraping Tips and Tricks

While our guide so far is already advanced enough to take care of JavaScript rendering scenarios, there are still many things to explore in Selenium. 

In this section, I will share some tips and tricks that may come in handy.

### 1. Time your requests

If you spam a server with hundreds of requests in a short time, it’s very probable that at some point, a captcha code will appear, or your IP might even get blocked. Unfortunately, there is no workaround in Python to avoid that. 

Therefore, you should put some timeout breaks between each request so that the traffic will look more natural.

```python
import time
import requests
 
page = requests.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
time.sleep(30) # Wait 30 seconds
page = requests.get('https://www.imdb.com/') # Getting page HTML through request

```

### 2. Error handling

Since websites are dynamic and they can change structure at any moment, error handling might come in handy if you use the same web scraper frequently.

```python
try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "your selector")))
    break
except TimeoutException:
    # If the loading took too long, print message and try again
    print("Loading took too much time!")
```

The try and error syntax can be useful when you’re waiting for an element, extracting it, or even when you’re just making the request.

### 3. Take Screenshots

If you need to obtain a screenshot of the web page you are scraping at any moment, you can use:

```python
driver.save_screenshot(‘screenshot-file-name.png’)
```

This can help debug when you’re working with dynamically loaded content.

### 4. Read the documentation

Last but not least, don’t forget to read the [documentation from Selenium](https://selenium-python.readthedocs.io/). This library contains information about how to do most of the actions you can do in a browser. 

Using Selenium, you can fill out forms, press buttons, answer popup messages, and do many other cool things. 

If you’re facing a new problem, their documentation can be your best friend.

## Final Thoughts

This article’s purpose is to give you an advanced introduction to web scraping using Python with Selenium and BeautifulSoup. While there are still many features from both technologies to explore, you now have a solid base on how to start scraping.

Sometimes web scraping can be very difficult, as websites start to put more and more obstacles in the developer’s way. Some of these obstacles can be Captcha codes, IP blocks, or dynamic content. Overcoming them just with Python and Selenium might be difficult or even impossible. 

So, I’ll give you an alternative as well. Try using a [web scraping API](https://webscrapingapi.com) that solves all those challenges for you. It also uses rotating proxies so that you don’t have to worry about adding timeouts between requests. Just remember to always check if the data you want can be lawfully extracted and used.

