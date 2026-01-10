---
title: How to visualize what you have been tweeting
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-18T15:46:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-visualize-what-you-have-been-tweeting-81c75f00546d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c4JfsP1tnptisFAUvMMVJg.png
tags:
- name: data analysis
  slug: data-analysis
- name: data visualization
  slug: data-visualization
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Deepal Dsilva

  A wordcloud experiment in R


  Have you ever wondered what you tweet about the most? Or you’re attending your favorite
  conference, and you want to know what’s the buzz around it?Or perhaps you want to
  know what’s the talk about the lat...'
---

By Deepal Dsilva

#### A wordcloud experiment in R

![Image](https://cdn-media-1.freecodecamp.org/images/M4fM-FrOINbwdMvYqE8Sr3EBh9d-vgCU9S5L)

Have you ever wondered what you tweet about the most? Or you’re attending your favorite conference, and you want to know what’s the buzz around it?  
Or perhaps you want to know what’s the talk about the latest movie that got released?

Well, WordClouds are where you should be looking. They are simple to set up, provide stunning visualizations, and are easily customizable.

### **Wait! But first, what is a WordCloud?**

It is an image composed of words used in a particular text or subject, in which the size of each word indicates its frequency or importance.

Now that you know the basics, let’s get started in R.

#### **Load up the required libraries**

```
library(twitteR)library(ROAuth)library(stringr)library(tm)library(wordcloud2)library(tidytext)
```

#### **Twitter App set up**

We are going to use Twitter data to build our wordcloud, so get a Twitter account if you do not have one. I’ll wait…

Next, we are going to need a Twitter App. This is a one-time setup.

You need to authenticate yourself on Twitter so that you can send a request for tweets and so that Twitter to send them back to you.

I’ll not go into the detailed steps. You can use [this tutorial](https://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/) to set it up.

Next, we pass on the token to the setup_twitter_oauth function to authenticate ourselves.

```
consumer_key <- "xxxx"      #Your Consumer Key (API Key)consumer_secret <- "xxxx"   #Your Consumer Secret (API Secret)access_token <- "xxxx"      #Your Access Tokenaccess_secret <- "xxxx"     #Your Access Token Secretsetup_twitter_oauth(consumer_key, consumer_secret, access_token, access_secret)
```

#### **Extracting Twitter Data**

You can either extract tweets based on a user’s profile or any keywords/hashtags. Here are both the examples.

```
#Query a hashtagtweets <- searchTwitter("#rstats",n=3000,lang="en", resultType = "popular")
```

```
#OR
```

```
#Query a user you follow or yourselftweets <- userTimeline("dsilvadeepal",n=3200,includeRts = FALSE)
```

#### **Text Mining your tweets**

We now need to extract the text from the tweets to a vector.

And we are first going to remove graphical parameters. This removes visible characters (anything except spaces and control characters) to avoid input errors.

```
tweets.txt <- sapply(tweets, function(t)t$getText())tweets.txt <- str_replace_all(tweets.txt,"[^[:graph:]]", " ")
```

Now let’s create a function to clean out tweets. Here we are going to remove digits, punctuation, spaces, HTTP links, and retweets (RTs). You can customize this function based on the data you are processing.

```
clean.text = function(x){    x = tolower(x)                   # tolower  x = gsub("rt", "", x)            # remove rt  x = gsub("@\\w+", "", x)         # remove at  x = gsub("[[:punct:]]", "", x)   # remove punctuation  x = gsub("[[:digit:]]", "", x)   # remove numbers  x = gsub("http\\w+", "", x)      # remove links http  x = gsub("[ |\t]{2,}", "", x)    # remove tabs  x = gsub("^ ", "", x)            # remove leading blank spaces   x = gsub(" $", "", x)            # remove trailing blank spaces    return(x)}
```

```
clean_tweet <- clean.text(tweets.txt)
```

Next, we build a Corpus. A Corpus is a collection of text documents and the VectorSource points to the vector where the tweets are stored.

We are also going to create a vector to remove English stop words and any more words that are irrelevant (we’ll identify these words in a later step). Some common English stop words are “the,” “I,” and “he.”

```
tweets <- Corpus(VectorSource(clean_tweet))wordsToRemove <- c(stopwords('en'), 'tco', 'https')clean_tweet <- tm_map(tweets, removeWords, wordsToRemove)
```

We now create a Term Document Matrix (TDM) which tells us the number of times each word in the corpus is found.

```
dtm <- TermDocumentMatrix(clean_tweet, control = list(wordLengths = c(1, Inf)))m <- as.matrix(dtm)v <- sort(rowSums(m),decreasing=TRUE)d <- data.frame(word = names(v),freq=v)head(d, 10)   #inspect our word list and remove any irrelevant words  in the stop words step above
```

Finally for the fun part!

#### **Creating our wordcloud**

Here we are going to use the WordCloud2 package — this is a newer package to the WordCloud package, and provides a lot more customization.

```
wordcloud2(d, shape = "triangle", color="random-light", backgroundColor = "white", minRotation = -pi/4, maxRotation = -pi/4, size = 0.5)
```

![Image](https://cdn-media-1.freecodecamp.org/images/M67dhbljBs8VnU5nWSxM6YzFXSJKc9uYISh4)

And there you have it! Here’s a link to the [code](https://github.com/dsilvadeepal/Data-Science/blob/master/Projects/Wordclouds/Twitter%20Wordcloud.Rmd) in Github.

Thanks for reading!

_Note: The Twitter API limits the number of tweets a user can get from a particular timeline to be 3200._

