---
title: How to scrape websites using Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-08T11:26:40.000Z'
originalURL: https://freecodecamp.org/news/scrap-websites-using-python-c0c7ad41d2dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*M0ip5ay8z72peBXvwXZSqQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: web scraping
  slug: web-scraping
seo_title: null
seo_desc: 'By Devanshu Jain

  It is that time of the year when the air is filled with the claps and cheers of
  4 and 6 runs during the Indian Premier League Cricket T20 tournament followed by
  the ICC Cricket World Cup in England. And how can we forget the election...'
---

By Devanshu Jain

It is that time of the year when the air is filled with the claps and cheers of 4 and 6 runs during the [Indian Premier League](https://www.iplt20.com/) Cricket T20 tournament followed by the ICC Cricket World Cup in England. And how can we forget the election results of the world’s largest democratic country, India, that will be out in the next few weeks?

To stay updated on who will be getting this year’s IPL title or which country is going to get the ICC World Cup in 2019 or how the country’s future will look in the next 5 years, we constantly need to be glued to the Internet. 

But if you’re like me and cannot spare much time on the Internet, but have a strong desire to stay updated with all these titles, then this article is for you. So without wasting any time, let’s get started!

![Image](https://cdn-media-1.freecodecamp.org/images/dySuWsAk2qARPtM0cOs88-YztYwzc1fWPz1F)
_Photo by [Unsplash](https://unsplash.com/photos/sScmok4Iq1o?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Balázs Kétyi</a> on <a href="https://unsplash.com/search/photos/data?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

There are two ways with which we can access the updated information. One way is through APIs provided by these media websites, and the other way round is through Web/Content Scraping. 

The API way is too simple, and probably the best way to get updated information is by calling the associated programming interface. But sadly, not all websites provide publicly accessible APIs. So the other way left for us is to Web Scrape.

### **Web Scraping**

Web scraping is a technique to extract information from websites. This technique mostly focuses on the transformation of unstructured data (HTML format) on the web into structured data (database or spreadsheet). Web scraping may involve accessing the web directly using HTTP, or through a web browser. 

In this article, we’ll be using Python to create a bot for scraping content from the websites.

### **Process Workflow**

* Get the URL of the page from which we want to extract/scrape data
* Copy/download the HTML content of the page
* Parse the HTML content and get the required data

The above flow helps us to navigate to the URL of the required page, get its HTML content, and parse the required data. But sometimes there are cases, when we first have to log in to the website and then navigate to a specific location to get the required data. In that case, that adds one more step of logging into the website.

### **Packages**

For parsing the HTML content and getting the required data, we use the **Beautiful Soup** library. It’s an amazing Python package for parsing HTML and XML documents. Do check it out [here](https://code.launchpad.net/beautifulsoup/).

For logging into the website, navigating to the required URL within the same session, and downloading the HTML content, we’ll be using the **Selenium** library. [Selenium Python](https://selenium-python.readthedocs.io/) helps with clicking on buttons, entering content in structures, and much more.

### **Dive right into the code**

First we are importing all the libraries that we are going to use.

```
# importing librariesfrom selenium import webdriverfrom bs4 import BeautifulSoup
```

Next we need to give the browser’s driver the path to Selenium to initiate our web browser (Google Chrome). And if we don’t want our bot to show the GUI of the browser, then we can add the **headless** option to Selenium. Headless browsers provide automated control of a web page in an environment similar to popular web browsers, but are executed via a command-line interface or using network communications.

```
# chrome driver pathchromedriver = '/usr/local/bin/chromedriver'options = webdriver.ChromeOptions()options.add_argument('headless')  # for opening headless browser
```

```
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
```

After the environment has been set up by defining the browser and installing libraries, we’ll be getting our hands on the HTML. Navigate to the login page and find the email, password and submit button’s field id, class or name to enter our content into the page structure.

```
# Navigating to the login pagebrowser.get('http://playsports365.com/default.aspx')
```

```
#Finding the tags by nameemail = browser.find_element_by_name('ctl00$MainContent$ctlLogin$_UserName')
```

```
password = browser.find_element_by_name('ctl00$MainContent$ctlLogin$_Password')
```

```
login = browser.find_element_by_name('ctl00$MainContent$ctlLogin$BtnSubmit')
```

Next, we’ll send the credentials into these HTML tags by clicking on the submit button to enter our content within the page structure.

```
# appending login credentialsemail.send_keys('********')password.send_keys('*******')
```

```
# clicking submit buttonlogin.click()
```

Once the login is successful, navigate to the required page and get the page’s HTML content

```
# After successful login, navigating to Open Bets Pagebrowser.get('http://playsports365.com/wager/OpenBets.aspx')
```

```
# Getting HTML content and parsing itrequiredHtml = browser.page_source
```

Now, we’ve received the HTML content and the only thing that is left is parsing this content. We’ll parse the content using the Beautiful Soup and html5lib libraries. [**html5lib**](http://code.google.com/p/html5lib/) is a Python package that implements the HTML5 parsing algorithm which is heavily influenced by current browsers. As soon as we get the normalized structure of the parsed content, we can find our data present in any child tag of the HTML tag. Our data is present in the table tag and that’s why we’re searching for that tag.

```
soup = BeautifulSoup(requiredHtml, 'html5lib')table = soup.findChildren('table')my_table = table[0]
```

Once we find the parent tag, we just need to recursively traverse within its children and print the values.

```
# fetching tags and printing valuesrows = my_table.findChildren(['th', 'tr'])for row in rows:    cells = row.findChildren('td')    for cell in cells:        value = cell.text        print (value)
```

To execute the above program, install Selenium, Beautiful Soup and html5lib libraries using [pip](https://pip.pypa.io/en/stable/installing/). After installing the libraries, typing `#python <program na`me> would print the values to the console.

By this way, we can scrape and find data from any website.

Now, if we are scraping a website which changes its content very frequently, like cricket scores or live election results, we can run this program in a cron job and set an interval for the cron job.

Apart from that, we can also have the results displayed right onto our screen instead of the console by printing the results in the notification tab that pops up onto the desktop after a particular time interval. We can even share these values onto a messaging client. Python has rich libraries that can help us with all that.

If you want me to explain how to set up a cron job and get notifications to appear on the desktop, feel free to ask me in comment section.

Until next time, bye and I hope you liked the article.

