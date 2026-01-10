---
title: The Future of Browser History
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-07T15:08:13.000Z'
originalURL: https://freecodecamp.org/news/browserhistory-2abad38022b1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LQcSLDoKyWBuwAEgcwKNyw.png
tags:
- name: Browsers
  slug: browsers
- name: Design
  slug: design
- name: internet
  slug: internet
- name: search
  slug: search
- name: Web Design
  slug: web-design
seo_title: null
seo_desc: 'By Patryk Adaś

  I am really unsatisfied with the current state of Browser History. I think that
  this is the most underestimated feature of every modern web browser. Let’s take
  the most popular browser as an example.

  Before we talk about browsers histo...'
---

By Patryk Adaś

I am really unsatisfied with the current state of Browser History. I think that this is the most underestimated feature of every modern web browser. Let’s take [the most popular browser](http://www.w3schools.com/browsers/browsers_stats.asp) as an example.

Before we talk about browsers history, we need to understand how we tend to browse nowadays.

Sometimes I want to know how to convert 1 foot to centimeters.

![Image](https://cdn-media-1.freecodecamp.org/images/3Zbc8a23p4y7pKpzdDsCmxiy-epvY-7l2Cvu)

Sometimes, on the other hand, I want to know why and how things happen.

For the second kind of search, the standard pattern of match retrieval does not really cut it.

#### Problem

I can search for the term in Google, but I’m not going to get a single result that answers my question. Rather, I’m going to get a lot of results, and all of those results will have bits and pieces of information that are relevant to me.

Then I’m going to go exploring through the internet, collecting lots of tabs along the way. Some of those tabs will be duds, so I close them.

Some of those tabs will be relevant and will have twenty more links, so I open them all, and in this way I keep crawling.

![Image](https://cdn-media-1.freecodecamp.org/images/sdqxpVVN6iLU-HDDFSI2M2ov7vtUJHVRrNbZ)
_Tabs, tabs, tabs_

Then after a while I have a cloud of pages in my head that I visited and the answer is more or less complete.

**But if I try to revisit this later, it’s impossible. I can remember what I found, but it wasn’t a linear progression, therefore my browser history is useless.**

Despite living in a data-driven society, as more and more databases are brought online, the complex and varied information available to be discovered is dependent on how well we can search.

In formal ways, we have transitioned from the [**Classic Retrieval Model**](https://en.wikipedia.org/wiki/Standard_Boolean_model), to what is called, [**Berrypicking Search**](https://en.wikipedia.org/wiki/Cognitive_models_of_information_retrieval#Berrypicking).

![Image](https://cdn-media-1.freecodecamp.org/images/kq3EfxFUeLeWb1wntudhJaJawNOoGdjTAyvR)
_Classic Retrieval Model_

The query is satisfied not by a single final retrieved set, but by a series of selections of individual references and bits of information at each stage of the ever-modifying search.

In other words, we do not usually search for something that leads to a single result that answers our question, rather we search for terms and then explore the internet, connecting bits and pieces of the answer as we read through the web of tabs that our search starts for us.

![Image](https://cdn-media-1.freecodecamp.org/images/bfDZQyAshRHDuNX4RLXVvqYkR8az7d-gdMjT)
_Berrypicking Search_

Our search needs, and in turn our browser history, are not being met with single query anymore. We move through a variety of sources with every new piece of information giving us new ideas and directions to follow. Without us ever knowing it, our search queries are constantly fluctuating.

![Image](https://cdn-media-1.freecodecamp.org/images/-PZnFv6lzqobD-nn87cTRtPsjtDYqeoZXJeC)
_Current Google Chrome History_

Unfortunately, our current solution to finding a not-bookmarked webpage, is to retrace own steps through different links.

It demands that users have enough information to decipher the desired page from all others by recognizing headers, obscure URLs or timestamps.

Our browser’s history should reflect our behavior on the internet and help us understand the process behind it. It is crucial to actually understand and question the way we use the internet, and without the suitable tools, it is not possible.

#### Solution

I find answers in maps.

![Image](https://cdn-media-1.freecodecamp.org/images/UgFIwp8RE5sFo5ZFDHjIgG3pDF1Yx6FeiCw2)
_Main Page_

![Image](https://cdn-media-1.freecodecamp.org/images/EKCbMxudMvj1vOh1F7ph8R54uO317fBT0mM-)
_:hover_

On top there is a timeline, positions are still displayed chronologically, but users can also see connections.

Not only is this a different approach to browsing our own content, it is now possible to see patterns of my search queries and behaviors. In this way, our browser history does not only perform a retrieval function, but also writes a narrative.

I will finally understand why I ended up reading about the influence of plants on soil properties, when I started with a Texas BBQ query.

With this method, I am able to see at a glance how different pieces of information are connected, how they relate to each other and how I formed conclusions. I see how I actually cognized things that are relevant. It is not only about the goal, but also about the journey.

In the proposed interface, with a simple hover action I receive essential pieces of information. I am able to understand my thought process and points of interest. It is also easier to actually remember the page thanks to particular color schemes and meta sections.

![Image](https://cdn-media-1.freecodecamp.org/images/uS98aCp5AzUUav4iC-EkcthYwsDedM7kIPqp)
_Single page_

Let’s say I already found what I was looking for and I’m satisfied with my information retrieval process.

How many times have I visited this website? How much time have I spent using it? When did I see something interesting? How often do I visit it? How does my generated traffic look like, from perspective of particular page?

![Image](https://cdn-media-1.freecodecamp.org/images/uvDfyeWH951-UfwVjzrxjdM7eXMlJEnFveOJ)
_Delete dropdown_

They say to [never trust a person with an empty history](https://twitter.com/davidwalshblog/status/535608920908115968).

![Image](https://cdn-media-1.freecodecamp.org/images/3RdQ71ITn210Me0thEnFVqqkOxG63waFoZnc)
_Search_

Google is one of the best search engines available and yet, in Browser History there is not even a place for auto-suggestion. How come?

I’d love to search by topic, dates, colors.

![Image](https://cdn-media-1.freecodecamp.org/images/5OmsuEIWT39ZWi5--jCprileKve8zNJVOhIV)
_Searches_

In order to re-create our experience — or to just see the overall topics of our interests — it would be useful to provide users with a list of past searches. Once you clicked a particular search result, it would expand with visited links based on that very query, and would redirect you to the map with the highlighted path.

![Image](https://cdn-media-1.freecodecamp.org/images/S45tdCAfOZ-mSsN46vsBrym8SiHHCxuCQNER)
_Analytics_

Currently, I am really missing the analytics screen. It is crucial to be able to understand one’s own behavior, especially as there is no distinction between offline and online anymore. [**Filter Bubble**](https://en.wikipedia.org/wiki/Filter_bubble) shows that information we see is selective.

We become separated from information that disagrees with our viewpoint. As a result, we are more and more comforted in our own domain. We have stopped questioning.

I want to see how much time I spend browsing Internet, how I collect information, and how I form my views.

We live in times when understanding your browser behaviors and search patterns is becoming crucial in cognitivism process.

[_I suppose it is tempting, if the only tool you have is a hammer, to treat everything as if it were a nail._](https://en.wikipedia.org/wiki/Law_of_the_instrument)

_Bibliography and inspiration:_

[1](http://theory.isthereason.com/?p=1790) [2](https://developer.chrome.com/extensions/history) [3](https://www-s.acm.illinois.edu/macwarriors/projects/trailblazer/)

_If you would like to collaborate please feel free to [write](mailto:patryk.adas@gmail.com)._

