---
title: How to Use Python to Scrape App Store Reviews
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-16T18:04:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-python-to-scrape-app-store-reviews
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Shittu-Olumide-How-to-use-Python-to-scrape-App-Store-reviews-Freecodecamp.png
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: null
seo_desc: "By Shittu Olumide\nData scraping, commonly referred to as web scraping,\
  \ is a technique for getting data and content from the internet.\nYou usually keep\
  \ this information in a local file so that you can change and inspect it as needed.\
  \ \nWeb scraping is ..."
---

By Shittu Olumide

Data scraping, commonly referred to as web scraping, is a technique for getting data and content from the internet.

You usually keep this information in a local file so that you can change and inspect it as needed. 

Web scraping is basically just copying and pasting content from a website into an Excel spreadsheet on a very small scale.

The main goal of this article is to help you get started in web scraping using quick and easy steps. You will learn how to scrape app store reviews using the `app_store_scraper` library in Python. There are other tools and libraries you can use such as `Scrapy`, `Pandas`, and `BeautifulSoup` ,but here we will use the use the  `app_store_scraper`. 

Depending on the mechanism you select for web scraping, it might be either really simple or quite complex. 

Fortunately, there is straightforward and excellent software that can help you gather reviews about your app from the Apple app store and use them for further sentiment analysis.

### Why is web scraping even useful?

Data analytics professionals employ web scraping for a variety of tasks, including lead creation, market analysis, consumer sentiment analysis, and data integration.

You can also use web scraping to track stock prices, online opportunities (such as scholarships, employment, internships, and so on), competitors' inventory data, and customer reviews and ratings.  
  
In this article, you will learn how to use Python to scrape app store reviews in 4 easy steps. 

Before you start, here's something to keep in mind: some sites don't allow you to scrape their content, so be sure you check before doing so. Web scraping isn't precisely forbidden, but you should take care to know when/where you can scrape. I strongly recommend that you scrape for informational and educational purposes only.

## Step 1 – Install and Setup Packages

First, you have to install and setup the necessary packages. In this step you will install the `app_store_scraper` using the Python package installer.

```py
pip install app_store_scraper 

#or

pip3 install app_store_scraper

```

## Step 2 – Get App's Name and ID

I will be using a random app and I will be scraping its reviews for the sake of this demo. But if have a personal app that you built and you have it on app store, you can use that app with these same techniques. You just need to get the app's name and ID, which you can find by typing the name of the app into Google using your PC. 

Example: "_Slack app on apple app store_"

![Image](https://www.freecodecamp.org/news/content/images/2022/09/slack-google-search.PNG)

You should click on the first result which will redirect you to the official Apple store. There you will find the "Slack app" and everything about it. 

Once the page loads in the URL you will see the app name (Slack) and app ID (618783545). Copy it down in your notepad.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/slack-app-name-app-id.PNG)

Now you'll need to import some packages and run some code:

```py
import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore
slack = AppStore(country='us', app_name='slack', app_id = '618783545')

slack.review(how_many=2000)

```

In the code above, you will import the `pandas` library which helps you add evaluations/reviews to a dataframe. You'll also import the `numpy` library for data transformation and modification. Finally, you'll get the `app_store_scraper` package itself for scraping the reviews from the website. 

You will have to create and instance of the `Appstore` class, then pass in the arguments `country`, `app_name`, and the `app_id`. 

![Image](https://www.freecodecamp.org/news/content/images/2022/09/slack-web-scraping.PNG)
_slack app ratings_

The reviews are all stored in the `slack` variable, so run the command below to see the reviews stored in JSON format.

```py
slack.reviews

```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/slack-reviews.PNG)
_slack app scraped reviews_

## Step 3 – Convert Data from JSON

To make data more readable and properly formatted, you need to convert it from JSON format to a Pandas dataframe. You can do that with the following code:

```py
slackdf = pd.DataFrame(np.array(slack.reviews),columns=['review'])
slackdf2 = df.join(pd.DataFrame(slackdf.pop('review').tolist()))
slackdf2.head()

```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/slack-generated-reviews.PNG)
_generated reviews in pandas dataframe_

## Step 4 – Convert the Dataframe to CSV

Here is the final step: you will covert the dataframe into CSV (comma-separated value) format so that you can have it on your local machine. Then you can view it in a spreadsheet and also share it with a colleague.

```py
slackdf2.to_csv('Slack-app-reviews.csv')

```

Finally, you should have your "Slack-app-reviews.csv" file saved into your project folder and you're ready to go. 

## Conclusion

In this short article, you were able to scrape Slack app store reviews into a dataframe and then save it into your local machine using 4 easy steps. I hope you enjoyed it, cheers.

Here is the [GitHub repo](https://github.com/zenUnicorn/App-rating-scraper-with-python) where I hosted the code, feel free to star the repository.

