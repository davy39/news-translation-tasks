---
title: Web Scraping with Python – How to Scrape Data from Twitter using Tweepy and
  Snscrape
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2022-07-12T17:58:29.000Z'
originalURL: https://freecodecamp.org/news/python-web-scraping-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/scraping-with-python-article-image.jpeg
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: null
seo_desc: 'If you are a data enthusiast, you''ll likely agree that one of the richest
  sources of real-world data is social media. Sites like Twitter are full of data.

  You can use the data you can get from social media in a number of ways, like sentiment
  analysis...'
---

If you are a data enthusiast, you'll likely agree that one of the richest sources of real-world data is social media. Sites like Twitter are full of data.

You can use the data you can get from social media in a number of ways, like sentiment analysis (analyzing people's thoughts) on a specific issue or field of interest.

There are several ways you can scrape (or gather) data from Twitter. And in this article, we will look at two of those ways: using Tweepy and Snscrape.

We will learn a method to scrape public conversations from people on a specific trending topic, as well as tweets from a particular user.

Now without further ado, let’s get started.

## Tweepy vs Snscrape – Introduction to Our Scraping Tools

Now, before we get into the implementation of each platform, let's try to grasp the differences and limits of each platform.

### Tweepy

Tweepy is a Python library for integrating with the Twitter API. Because Tweepy is connected with the Twitter API, you can perform complex queries in addition to scraping tweets. It enables you to take advantage of all of the Twitter API's capabilities.

But there are some drawbacks – like the fact that its standard API only allows you to collect tweets for up to a week (that is, Tweepy does not allow recovery of tweets beyond a week window, so historical data retrieval is not permitted).

Also, there are limits to how many tweets you can retrieve from a user's account. You can [read more about Tweepy's functionalities here](https://www.tweepy.org/).

### Snscrape

Snscrape is another approach for scraping information from Twitter that does not require the use of an API. Snscrape allows you to scrape basic information such as a user's profile, tweet content, source, and so on.

Snscrape is not limited to Twitter, but can also scrape content from other prominent social media networks like Facebook, Instagram, and others.

Its advantages are that there are no limits to the number of tweets you can retrieve or the window of tweets (that is, the date range of tweets). So Snscrape allows you to retrieve old data.

But the one disadvantage is that it lacks all the other functionalities of Tweepy – still, if you only want to scrape tweets, Snscrape would be enough.

Now that we've clarified the distinction between the two methods, let's go over their implementation one by one.

## How to Use Tweepy to Scrape Tweets

Before we begin using Tweepy, we must first make sure that our Twitter credentials are ready. With that, we can connect Tweepy to our API key and begin scraping.

If you do not have Twitter credentials, you can register for a Twitter developer account by going [here](https://developer.twitter.com/). You will be asked some basic questions about how you intend to use the Twitter API. After that, you can begin the implementation.

The first step is to install the Tweepy library on your local machine, which you can do by typing:

```javascript
pip install git+https://github.com/tweepy/tweepy.git
```

### How to Scrape Tweets from a User on Twitter

Now that we’ve installed the Tweepy library, let’s scrape 100 tweets from a user called `john` on Twitter. We'll look at the full code implementation that will let us do this and discuss it in detail so we can grasp what’s going on:

```python
import tweepy

consumer_key = "XXXX" #Your API/Consumer key 
consumer_secret = "XXXX" #Your API/Consumer Secret Key
access_token = "XXXX"    #Your Access token key
access_token_secret = "XXXX" #Your Access token Secret key

#Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)


username = "john"
no_of_tweets =100


try:
    #The number of tweets we want to retrieved from the user
    tweets = api.user_timeline(screen_name=username, count=no_of_tweets)
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.created_at, tweet.favorite_count,tweet.source,  tweet.text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))
    time.sleep(3)
```

Now let's go over each part of the code in the above block.

```python
import tweepy

consumer_key = "XXXX" #Your API/Consumer key 
consumer_secret = "XXXX" #Your API/Consumer Secret Key
access_token = "XXXX"    #Your Access token key
access_token_secret = "XXXX" #Your Access token Secret key

#Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)
```

In the above code, we've imported the Tweepy library into our code, then we've created some variables where we store our Twitter credentials (The Tweepy authentication handler requires four of our Twitter credentials). So we then pass in those variable into the Tweepy authentication handler and save them into another variable.

Then the last statement of call is where we instantiated the Tweepy API and passed in the require parameters.

```python
username = "john"
no_of_tweets =100


try:
    #The number of tweets we want to retrieved from the user
    tweets = api.user_timeline(screen_name=username, count=no_of_tweets)
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.created_at, tweet.favorite_count,tweet.source,  tweet.text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))
```

In the above code, we created the name of the user (the @name in Twitter) we want to retrieved the tweets from and also the number of tweets. We then created an exception handler to help us catch errors in a more effective way.

After that, the `api.user_timeline()` returns a collection of the most recent tweets posted by the user we picked in the `screen_name` parameter and the number of tweets you want to retrieve.

In the next line of code, we passed in some attributes we want to retrieve from each tweet and saved them into a list. To see more attributes you can retrieve from a tweet, read [this](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline).

In the last chunk of code we created a dataframe and passed in the list we created along with the names of the column we created.

Note that the column names must be in the sequence of how you passed them into the attributes container (that is, how you passed those attributes in a list when you were retrieving the attributes from the tweet).

If you correctly followed the steps I described, you should have something like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-17.png align="left")

*Image by Author*

Now that we are done, let's go over one more example before we move into the Snscrape implementation.

### How to Scrape Tweets from a Text Search

In this method, we will be retrieving a tweet based on a search. You can do that like this:

```python
import tweepy

consumer_key = "XXXX" #Your API/Consumer key 
consumer_secret = "XXXX" #Your API/Consumer Secret Key
access_token = "XXXX"    #Your Access token key
access_token_secret = "XXXX" #Your Access token Secret key

#Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)


search_query = "sex for grades"
no_of_tweets =150


try:
    #The number of tweets we want to retrieved from the search
    tweets = api.search_tweets(q=search_query, count=no_of_tweets)
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source,  tweet.text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))
```

The above code is similar to the previous code, except that we changed the API method from `api.user_timeline()` to `api.search_tweets()`. We've also added `tweet.user.name` to the attributes container list.

In the code above, you can see that we passed in two attributes. This is because if we only pass in `tweet.user`, it would only return a dictionary user object. So we must also pass in another attribute we want to retrieve from the user object, which is `name`.

You can go [here](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/user) to see a list of additional attributes that you can retrieve from a user object. Now you should see something like this once you run it:

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-18.png align="left")

*Image by Author.*

Alright, that just about wraps up the Tweepy implementation. Just remember that there is a limit to the number of tweets you can retrieve, and you can not retrieve tweets more than 7 days old using Tweepy.

## How to Use Snscrape to Scrape Tweets

As I mentioned previously, Snscrape does not require Twitter credentials (API key) to access it. There is also no limit to the number of tweets you can fetch.

For this example, though, we'll just retrieve the same tweets as in the previous example, but using Snscrape instead.

To use Snscrape, we must first install its library on our PC. You can do that by typing:

```javascript
pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git
```

### How to Scrape Tweets from a User with Snscrape

Snscrape includes two methods for getting tweets from Twitter: the command line interface (CLI) and a Python Wrapper. Just keep in mind that the Python Wrapper is currently undocumented – but we can still get by with trial and error.

In this example, we will use the Python Wrapper because it is more intuitive than the CLI method. But if you get stuck with some code, you can always turn to the GitHub community for assistance. The contributors will be happy to help you.

To retrieve tweets from a particular user, we can do the following:

```python
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Created a list to append all tweet attributes(data)
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:john').get_items()):
    if i>100:
        break
    attributes_container.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    
# Creating a dataframe from the tweets list above 
tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets"])
```

Let's go over some of the code that you might not understand at first glance:

```python
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:john').get_items()):
    if i>100:
        break
    attributes_container.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    
  
# Creating a dataframe from the tweets list above 
tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets"])
```

In the above code, what the `sntwitter.TwitterSearchScaper` does is return an object of tweets from the name of the user we passed into it (which is john).

As I mentioned earlier, Snscrape does not have limits on numbers of tweets so it will return however many tweets from that user. To help with this, we need to add the enumerate function which will iterate through the object and add a counter so we can access the most recent 100 tweets from the user.

You can see that the attributes syntax we get from each tweet looks like the one from Tweepy. These are the list of attributes that we can get from the Snscrape tweet which was curated by Martin Beck.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Sns.Scrape.png align="left")

*Credit: Martin Beck*

More attributes might be added, as the Snscrape library is still in development. Like for instance in the above image, `source` has been replaced with `sourceLabel`. If you pass in only `source` it will return an object.

If you run the above code, you should see something like this as well:

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-19.png align="left")

*Image by Author*

Now let's do the same for scraping by search.

### How to Scrape Tweets from a Text Search with Snscrape

```python
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('sex for grades since:2021-07-05 until:2022-07-06').get_items()):
    if i>150:
        break
    attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    
# Creating a dataframe to load the list
tweets_df = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])
```

Again, you can access a lot of historical data using Snscrape (unlike Tweepy, as its standard API cannot exceed 7 days. The premium API is 30 days.). So we can pass in the date from which we want to start the search and the date we want it to end in the `sntwitter.TwitterSearchScraper()` method.

What we've done in the preceding code is basically what we discussed before. The only thing to bear in mind is that until works similarly to the range function in Python (that is, it excludes the last integer). So if you want to get tweets from today, you need to include the day after today in the "until" parameter.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-21.png align="left")

*Image of Author.*

Now you know how to scrape tweets with Snscrape, too!

### When to use each approach

Now that we've seen how each method works, you might be wondering when to use which.

Well, there is no universal rule for when to utilize each method. Everything comes down to a matter preference and your use case.

If you want to acquire an endless number of tweets, you should use Snscrape. But if you want to use extra features that Snscrape cannot provide (like geolocation, for example), then you should definitely use Tweepy. It is directly integrated with the Twitter API and provides complete functionality.

Even so, Snscrape is the most commonly used method for basic scraping.

# Conclusion

In this article, we learned how to scrape data from Python using Tweepy and Snscrape. But this was only a brief overview of how each approach works. You can learn more by exploring the web for additional information.

I've included some useful resources that you can use if you need additional information. Thank you for reading.

%[https://github.com/JustAnotherArchivist/snscrape] 

%[https://docs.tweepy.org/en/stable/index.html] 

%[https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af]
