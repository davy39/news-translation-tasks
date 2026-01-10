---
title: How Crowd Curation Improved Our Search Quality by 27%
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-09T22:30:29.000Z'
originalURL: https://freecodecamp.org/news/how-crowd-curation-improved-our-search-quality-by-27-84d500e751bc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qRLVVbI9mEUK2IOyLbGJ-w.jpeg
tags:
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Thanesh Sunthar

  The bigger your platform gets, the more vital search becomes. And if you run a content-heavy
  platform like ours, it’s even more critical that you get search right.

  Retrieving relevant information from millions — potentially billion...'
---

By Thanesh Sunthar

The bigger your platform gets, the more vital search becomes. And if you run a content-heavy platform like ours, it’s even more critical that you get search right.

Retrieving relevant information from millions — potentially billions — of records is not a trivial task. The problem of search is so complex that it has it’s own discipline dedicated to solving it, called _Information Science_.

![Image](https://cdn-media-1.freecodecamp.org/images/0rri81CA7EmZFg7HClsESnuYWg1aUfcYSMYy)
_Top 6 websites showing the importance of search_

The world’s six most-visited websites all feature a prominent search bar in their navigation panel. Facebook, YouTube, and Amazon have chosen to place the search bar right next to their logo, highlighting how important search has become for these platforms. Google, the world’s number one website, was initially built around this single problem — search!

### **Search is Navigation**

Search is the primary way people discover content on a platform. Few people will really put in the time to learn your platform’s hierarchy. In every category, there are many other platforms competing for your users’ time, so these hierarchies are constantly evolving, anyway.

When was the last time you used a _menu bar_? Or even used _advance search filters_? Unless you forced users to use these, they tend to naturally stay away from these. So if it isn’t easy enough for users to discover your content through search, they’ll lose interest and move on.

### **_Curating Search Results_**

When search results aren’t relevant to the user, they won’t take the next action and click on any of the results. Curation helps increase the relevance of search results.

My company, Flipp, takes weekly circulars from retailers and makes them searchable. Here’s the difference between _non-curated_ and _manually curated_ results when you search “cake” on Flipp:

![Image](https://cdn-media-1.freecodecamp.org/images/4vOcnEFNgSIPg9id9H0fadNxv2H4IxuMAFf5)
_Not curated search results VS manually curated search results_

Manual curation is the process of a human actually checking each and every search term, then manually arranging the sort order of the results. It’s clear that our manually curated version shows a much cleaner, more relevant set of search results to the user.

You can automate some aspects of manual curation, but it’s still a resource intensive task.

### **_Enter Crowd Curation_**

While manual curation is a great way to get started, it’s not a scalable solution. We need a better approach.

This is where _crowd curation_ comes into play. It uses the [wisdom of the crowd](https://en.wikipedia.org/wiki/Wisdom_of_the_crowd) to sort the order of search results.

One simple approach is to see what items users are clicking on the most, then bump them up to the top of your search results. Here’s an example of the search results for the query “bbq” both before and after crowd curation:

![Image](https://cdn-media-1.freecodecamp.org/images/eYGMBJVAEUf4b19qA2JeBYajeqtuoYr4kF77)
_Crowd curation of the search term “bbq”_

As you can see, measuring the click count on an item and sorting results based on that yields much better search results. But because items change on a daily basis in our app, our search results require a periodic tune-up. We keep search results fresh so that expired deals disappear and newer, more “newsworthy” deals rise to the top.

We have to ensure that we don’t penalize new flyer items against the older items, which have received more impressions, and therefore collected more clicks. This creates other interesting challenges for our dev team.

Search is also slightly different on mobile platforms. Because the screen size is smaller, we have to also consider what is actually displayed in the viewport.

There’s a greater chance that a user will click on an item that is shown at the top (above the fold) rather than items further down the list that they have to scroll down to (below the fold). If the user does take the effort to scroll down to find an item, then that has to also be taken into account when we improve the sort order of our search results.

### **_Measuring Search Quality_**

The most important measure of a search engine is the quality of its search results. Here, the gap between searches and clicks is widening, and search is getting worse:

![Image](https://cdn-media-1.freecodecamp.org/images/XcQYOnxEAlWX6zZ8O4tYrBokpDfCKYw89kKU)
_Searches VS Clicks_

We use [Click Through Rate](https://en.wikipedia.org/wiki/Click-through_rate) — the ratio of users who click on a specific item versus the total users who view those search results — to measure the effectiveness of our search engine.

We also use [Discounted Cumulative Gain](https://en.wikipedia.org/wiki/Discounted_cumulative_gain) to measure the quality of our ranking algorithms.

One simple way to visualize “uplift” — improvement in results — is to measure the additional clicks generated at every rank of the search result. We used this to conclude that **by using crowd curation we saw 27% uplift in clicks generated from the first result.**

Most of the clicks shifted towards the top ranks, proving that we had improved the quality and relevancy of our search results.

![Image](https://cdn-media-1.freecodecamp.org/images/xseM5VYbnXNcigoso5S1fpMCn0h5SoXIbX7Q)
_Uplift in clicks across search results_

And yes, our algorithm also weighs on how long an item has been available in search.

For example, if a circular dropped on Wednesday, the “newsworthiness” of items from that circular would degrade as we move through the week, giving more importance to items from flyers dropped more recently than Wednesday. We balance this with the number of clicks.

In other words:

_Item Rank = Formula(Age of Item, Clicks)_

This way, we’re able to somewhat mitigate [winner-takes-all](https://en.wikipedia.org/wiki/Winner_takes_all) effects.

At Flipp, we want the user experience to be magical. We’re a data-driven company that constantly looks at data to find new ways to improve the lives of millions of users. Search is just one area where we are applying this principle, but it’s an important one.

_I’m Thanesh, a senior product manager at [Flipp](https://flipp.com/). I published another version of this on the [Flipp engineering blog](http://eng.flipp.com/using-crowd-curation-to-enrich-search/). If you’re interested in reinventing the way people buy things, check out our current [job postings](https://corp.flipp.com/jobs)._

