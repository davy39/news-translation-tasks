---
title: What I learned from analyzing more than 80 job rejections with Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-19T17:49:55.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-from-analyzing-more-than-80-job-rejections-with-python-11044ee6927b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ux_ov2BCOxHApB3e1DBt2Q.png
tags:
- name: Data Science
  slug: data-science
- name: jobs
  slug: jobs
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Conor Dewey

  We’ve all gotten those emails at one point or another. You know, the ones that start
  with “Thank you for your interest” and end with shattered dreams and self-doubt.
  Okay, maybe that’s a bit extreme. Nonetheless, getting job rejections...'
---

By Conor Dewey

We’ve all gotten those emails at one point or another. You know, the ones that start with “Thank you for your interest” and end with shattered dreams and self-doubt. Okay, maybe that’s a bit extreme. Nonetheless, getting job rejections can be difficult.

Trust me, I know. I’ve received over 80 explicit job rejection emails over the past year while applying for internships. Let’s take a look at [my experience](https://github.com/conordewey3/DS-Career-Resources) by the numbers to provide a little context before we dive into the data.

* Applications: 234
* Replies: 93
* Rejections: 90
* Offers: 3

It’s worth pointing out that, at least for internships, getting no response at all is not uncommon. In fact, over 60% of applications that I filled out saw no response whatsoever. In a lot of ways, this can cause even more anxiety than getting back a clear-cut “no” response back. At least in that case you can move on with your search instead of focusing on a lost cause.

As you might imagine, after hearing “no” 80+ times, you develop a sort of resistance to it. This resistance coupled with a bit of curiosity is what ultimately sparked the idea for this project. In short, I wanted to investigate what made these automated rejection emails tick and how they differed between companies. If you want to skip to the code itself, feel free to head on over to the [GitHub repo](https://github.com/conordewey3/Job-Rejection-Analysis) and have at it.

**Throughout the rest of this post, I’ll go into how I scraped the rejection emails. Then I’ll answer some interesting questions regarding the timing and content of them.**

![Image](https://cdn-media-1.freecodecamp.org/images/yL8CxM6pQ7p8Rll7JNTycja8mhNwLJk4dZwb)

![Image](https://cdn-media-1.freecodecamp.org/images/HPr5bUL5vWLq9g6rYNEWbI3b4fvr0nKTxl3s)
_Everything happens for a reason, right?_

### Data collection

First things first, let’s get the data. Upon querying my Gmail inbox, I found over 1,000 emails containing the words “intern” and “application”. This made things a bit tricky from an automation perspective.

I went through and sorted out the job rejections by each company. I provided each one with a “Job Rejection” label within Gmail. Once that was done, it was time to leverage the power of Python. I was able to log in with `imaplib` and scrape specific parts of the emails with the `email` package. For content analysis, I had to tokenize the text with `nltk` , and remove any punctuation and stopwords for analysis.

### Common words & phrases

Ever think to yourself that these emails seem to all use the same general language? Personally, I’ve noticed a lot of the same phrases and lines used from company to company. This isn’t to say that there aren’t some creative attempts to soften the blow, but they are definitely few and far between.

![Image](https://cdn-media-1.freecodecamp.org/images/NmdkH6IZPYQxSha-hss4eFo19KGwZJCqRtmh)
_A little optimism goes a long way, thanks AT&amp;T_

Let’s take a look at the most common words and phrases used in the subject lines of these emails. You know, so you can, at least, see it coming.

![Image](https://cdn-media-1.freecodecamp.org/images/omf6WkUYUdKXfYoxSfLONbJoAEoK9j4v1oPn)

As you can see above, popular word choices include “application” and “your” among others. Just glancing at this, you can probably piece together the most likely subject headers without too much effort:

* Thank you for your interest.
* Update on your [Insert role] application.

There appears to be small variations of these same tried and true subject lines, but these words often serve as the initial bearer of bad news.

### Time patterns

Let’s take things a step further and look at how the timing of these emails breaks down. This reminded me of the age-old advice to never to fire someone on a Friday, since they can’t really take any steps towards new employment over the weekend. While not quite as severe as letting someone go, it’s still fascinating to think about the thought processes used when companies choose to deliver the bad news.

Let’s follow this idea and look at the day of the week breakdown for rejection emails. I’ll dive into the time of day breakdown afterwards.

![Image](https://cdn-media-1.freecodecamp.org/images/zPiBcFgH9gvbudyO0cNq4p291TkUkktPzP69)

It appears that “hump day” is the clear winner here. Thursday comes in at second place, with the rest of weekdays looking pretty consistent. Weekends look like smooth sailing for the most part, aside from a few notable anomalies that were sent on Saturday. Shame…

![Image](https://cdn-media-1.freecodecamp.org/images/KqWxUcKLONzjcRC65edwX4Qj5eSXhMw77MNu)

For hour of day, it looks like the normal distribution we would expect. There appear to be spikes in rejection counts at 9 am and noon. These times signal the start of the workday for the EST and PST time zones, respectively. Only one single rejection came after 5pm PST (hour 20). Lookin’ at you P&G.

This wraps up the analysis portion of the post. Once again, you can check out the code and original analysis on [GitHub](https://github.com/conordewey3/Job-Rejection-Analysis) or in the gist linked below.

### Final words

I found this project to be a fun exploration of job rejection emails. More than that, I found it to be a useful reflection on [my job search](https://github.com/conordewey3/DS-Career-Resources) and dealing with rejection in general. Not enough people out there value the ability to deal with failure as a practical skill or even a [super power](https://www.ted.com/talks/jia_jiang_what_i_learned_from_100_days_of_rejection) in some ways.

> “I’ve failed over and over again in my life… and that is why I succeed” — Michael Jordan

After 80+ explicit rejections, you begin to get used to the notion of failure. I found myself becoming increasingly less hesitant to apply to positions at prestigious companies or cold-email recruiters. This allowed me to obtain opportunities that initially I didn’t think were within reach.

If you’re reading this, take those chances, reach a little further, go out there and fail. Get back up. Then fail some more. It’s only through this process that improvement and, ultimately, success can be achieved. And when you do accomplish that next success, don’t forget to look back to all the failures that brought you there and say one thing:

> _Thank you for your interest._

Thanks for reading! If you enjoyed the post, go ahead and show the clap button some love and check out some of my related posts below:

* [Deconstructing Metrics on Medium](https://towardsdatascience.com/deconstructing-metrics-on-medium-bf5b4863bf96?source=friends_link&sk=8bd7eb3ae6d762eccb2111788c7a8933)
* [The Big List of DS/ML Interview Resources](https://towardsdatascience.com/the-big-list-of-ds-ml-interview-resources-2db4f651bd63?source=friends_link&sk=e229d4fc3452514bd8d560ae898809cc)
* [Python for Data Science: 8 Concepts You May Have Forgotten](https://towardsdatascience.com/python-for-data-science-8-concepts-you-may-have-forgotten-i-did-825966908393?source=friends_link&sk=f8daac7acb936a5a7eaa65e80cfda01f)

If you’re interested in more posts to come, make sure to [follow me](https://medium.com/@conordewey3) and subscribe to [my newsletter](https://www.conordewey.com/newsletter/) below to receive any new content. For more on me and what I’m up to, check out [my website](https://www.conordewey.com/).

