---
title: How to choose between open source libraries using popularity
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T21:40:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-choose-between-open-source-libraries-using-popularity-c71677785542
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aRTxvJrpsNRfsacu_sThaA.gif
tags:
- name: coding
  slug: coding
- name: GitHub
  slug: github
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ashish Singal

  Through my career as a product manager, I’ve worked closely with engineers to build
  many technology products (and even hacked some together myself).

  When developing technology products, one of the most critical choices we can make
  is...'
---

By Ashish Singal

Through my [career](https://www.linkedin.com/in/ashishsingal/) as a product manager, I’ve worked closely with engineers to build many technology products (and even hacked some together [myself](https://medium.com/@ashishsingal1/introducing-betalyzer-a-fintech-tutorial-110ac9abda58)).

When developing technology products, one of the most critical choices we can make is between competing sets of libraries and frameworks. One key ingredient is **relative popularity**, for several reasons:

1. **Proxy for the Best**. Especially in open source, the “market” is fairly efficient. Developers generally gravitate towards the best technologies and vote with their feet.
2. **Help**. While formal documentation is critically important, Stack Overflow questions and Medium tutorials are sometimes even more beneficial to move up the learning curve and to debug. Code snippets and tips from practitioners boost development speed and impact tremendously.
3. **Talent**. The more popular a library is, the more likely you’ll be able to find people who know how to use it to help build your product.
4. **Future Enhancements**. A vibrant user base and community ensures continued development on the project in the future, reducing the chance that it will become obsolete.

#### Proxies for Popularity

There are several ways to measure the popularity of OS libraries:

1. [Stack Overflow questions](http://stackoverflow.com)
2. [Github stars](https://github.com/)
3. [Google Trends](https://trends.google.com/trends/?geo=US)

[StackShare](https://stackshare.io) should also get an honorable mention here as a good way to find popular tools.

#### Judging Momentum

However, these measures need a time based component. Without taking into account metric momentum, the above measures are purely backward looking — they help inform what **was** the best technology, not what **is** or what **will be**.

![Image](https://cdn-media-1.freecodecamp.org/images/rGSnxIgdwWGMlYKSkEAHsWC071BMJjfzRtKm)
_Momentum helps us look into the future instead of the past_

Therefore, more often, when evaluating competing libraries, I’ll often look at charts of these statistics over time. There are several apps that allow us to do that:

1. [**Stack Overflow Trends**](http://sotagtrends.com/). [Open source](https://github.com/robianmcd/tag-trends) tool by [Rob McDiarmid](https://www.linkedin.com/in/rob-mcdiarmid-b56930140/). Also directly from [Stack Overflow](https://insights.stackoverflow.com/trends).
2. [**Github Star History**](https://timqian.com/star-history/). Similar tools include [StarTrack](https://seladb.github.io/StarTrack-js/), [Stargraph](https://stargraph.co/), and [this project](https://stars.przemeknowak.com/). Unfortunately, most use the Github API for this which seems to be quite unreliable and buggy.
3. [**Google Trends**](https://trends.google.com/trends/?geo=US), of course, works out of the box, but seems somewhat more spiky and less informative than the other two measures.

Google Cloud has also made both [Stack Overflow](https://console.cloud.google.com/marketplace/details/stack-exchange/stack-overflow?filter=solution-type:dataset&q=stack%20overflow&id=46a148ff-896d-444c-b08d-360169911f59) and [Github](https://console.cloud.google.com/marketplace/details/github/github-repos?filter=solution-type:dataset&q=github&id=46ee22ab-2ca4-4750-81a7-3ee0f0150dcb) data available as part of their [Public Datasets](https://cloud.google.com/public-datasets/) program. And here’s a [post](https://towardsdatascience.com/these-are-the-real-stack-overflow-trends-use-the-pageviews-c439903cd1a) that digs into some insights from Stack Overflow.

#### Example: Flask versus Django

Flask and Django are two popular Python web application frameworks that I personally have a lot of experience with. Flask is lighter weight and more flexible, while Django has much more built in and is more feature rich.

Let’s see how these rank using our methodologies above:

1. **Github Stars**: [Django](https://github.com/django/django) currently has 40k stars on Github while [Flask](https://github.com/pallets/flask) has 42k stars — they are neck and neck. I tried several of the Github history trackers, but they all timed out on me.
2. **Stack Overflow**: [Django](https://stackoverflow.com/questions/tagged/django) has 191k questions, while [Flask](https://stackoverflow.com/questions/tagged/flask) has 26k questions. The trend shows Flask picking up, but still a long ways away.
3. **Google Trends:** Django is currently about twice as popular as Flask, according to Google Trends.

![Image](https://cdn-media-1.freecodecamp.org/images/CBZQzcNTdVcxYMvy7DrK0trRPjyrvAxMwErI)
_Stack Overflow questions asked by month: Flask v Django_

![Image](https://cdn-media-1.freecodecamp.org/images/4jadhf1FU1Jm6a5A2vevtekWtlcWMaUc3Fsj)
_Google Trends search popularity: Flask v Django_

**Note** that of course, relative popularity is only one factor in choosing between libraries. Between Flask and Django, for example, I tend to choose Flask for quick prototyping as well as when I am developing a non traditional app and need a ton of flexibility. I tend to choose Django when I’d like out of the box functionality for things like user accounts, administration, and built in ORM.

![Image](https://cdn-media-1.freecodecamp.org/images/2tSeX16wBNz2R5HWtcHemR0I1Vhuya83NznB)
_Yes, popularity matters!_

Hope this helps! Thanks for reading.

