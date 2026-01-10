---
title: How I analyzed a million Medium articles to learn how many claps great stories
  get
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-23T19:57:30.000Z'
originalURL: https://freecodecamp.org/news/how-i-analyzed-a-million-medium-articles-to-learn-how-many-claps-great-stories-get-d688cf92759f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Fa8l3RP4Pp4872OwTocfOg.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Inspiration
  slug: inspiration
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
- name: writing
  slug: writing
seo_title: null
seo_desc: 'By Harrison Jansma

  This article is for the writers of Medium. If you have ever been frustrated with
  the response your stories get, this article can help you.

  My name is Harrison Jansma, and I write about data. Over the last few weeks, I collected
  and...'
---

By Harrison Jansma

_This article is for the writers of Medium. If you have ever been frustrated with the response your stories get, this article can help you._

My name is Harrison Jansma, and I write about data. Over the last few weeks, I collected and analyzed the claps of a million Medium stories. So I could answer the question that bothers me most as a writer on Medium. Namely,

> _How do my stories compare to those of similar writers on Medium?_

Though I am a writer, I am not a particularly creative one. To cope, I have to motivate my writing through competition. Making goals for myself based on either the performance of my past stories, or the performance of stories in my news-feed.

**Unfortunately, this comparison is slowly killing my ability to write.**

The problem is that I’m setting goals for my writing without knowing if these goals are reasonable.

![Image](https://cdn-media-1.freecodecamp.org/images/G1a8qlikoBp5kKGRTMGbe01prUDNV39tSWJ5)
_Which of these is a reasonable goal?_

Stories in my home-feed range from 40 claps to 30K claps. The first three stories I wrote on Medium ranged from 80 claps to 9K claps. So do I make my goal to get thirty thousand claps? Ten thousand claps? Just how many stories actually reach that level of reader-engagement?

As long as claps appear to vary wildly from story to story, writers can never use this metric to make goals for their writing.

So I made it my goal to understand Medium’s claps better. I collected data from hundreds of thousands of Medium stories, ranging in topic from poetry, to tech, to politics. With this data I found exactly what I was looking for.

**I found a way for authors to compare the performance of their writing to other, similar stories on Medium.**

### **Scraping a million Medium stories.**

The first step was collecting information. Specifically, I had to get the claps received from A LOT of Medium articles.

So I strolled around the Medium [archives](https://medium.com/tag/data-science/archive) for a few days. Then I created a web-scraper in Python (found on [GitHub](https://github.com/harrisonjansma/Analyzing_Medium)). The web-scraper pulled data from thousands of story-cards.

![Image](https://cdn-media-1.freecodecamp.org/images/qiRCymOwTYpuCMzw-ZtM9rR94rwqy5SSNYzl)
_Example of data scraped from a story-card._

**Once data collection was completed,** **I had data on 993K Medium articles.** They covered 36 of the most popular Medium tags, all published in the last year (Aug, 2017-Aug, 2018).

![Image](https://cdn-media-1.freecodecamp.org/images/BS3XxeyXqDqzguCZTp82GsIzZ5Oe7tTAt1NJ)

### Analyzing (nearly) a million Medium stories

After removing duplicate-stories and comments from the data, I was left with 720K unique stories from 230K authors and 30K publications. The number of claps received for an article ranged from zero claps to [215K claps](https://hackernoon.com/im-harvesting-credit-card-numbers-and-passwords-from-your-site-here-s-how-9a8cb347c5b5).

To better understand Medium’s clap metric, I needed to answer two questions.

1. How many claps does the average story get?
2. How many claps does an above average story get?

Let’s start with the first question.

### How many claps does the average story get?

On Medium, most writers receive mediocre engagement from their readers. This might be because Medium is a free platform for writers. Or maybe because not every writer’s goal is to receive huge numbers of claps from their audience.

**Whatever the reason, most articles receive almost no applause**. Of the 720K articles I analyzed, 61.3% received less than 10 claps.

![Image](https://cdn-media-1.freecodecamp.org/images/AaMMtD3kRzB3-tPHI2-0n4jyYr4dSxJO76ZN)

**If you are a writer, you should not let this discourage you.**

Whether it be the time of day, or the mysteries of Medium’s recommendation engine, the engagement your stories receive is not really up to you.

However, the most successful authors on Medium didn’t get where they are by chance. They posted high-quality content (consistently) for a long time, and gradually built a following.

You can do the same.

### How many claps does an above average story get?

Now that you know how many claps most stories receive, we will look at the other end of the spectrum: the stories that received more claps than average.

Unfortunately, there isn’t a distinct number of claps an article needs to be above average. What we need is to rephrase the question a bit. Instead we ask:

**How many claps do the top 1% of stories get?**

Of the 720K stories analyzed, the top 1% most-clapped stories received more than two thousand claps.

![Image](https://cdn-media-1.freecodecamp.org/images/fgxdN41uZIlk2kNyGR-HjmKD00o-t3SycXH5)

_This cutoff falls at exactly 2000.0 claps, rather than a number like 2112 because of the way the data was collected. Once you pass one thousand claps, Medium abbreviates your claps-received (ex. 2.2K). So the strict cutoff is somewhere between 2K and 2.1K. But two thousand is much cooler sounding… Sooo…_

**So two thousand claps is the cutoff for a story being in the top 1% of Medium stories.** From now on, when you write a story, you can use this as your goal for reader engagement. You can also use this as a benchmark to measure the performance of your past articles.

Two thousand claps is also a pretty good metric for your performance as an author.

Writing a story in the top 1% is no small feat. Of the 230K authors in the data, only 1.2% had written an article with more than two thousand claps.

![Image](https://cdn-media-1.freecodecamp.org/images/8b4Mxfu9zpfXkXoActdoWcd0eCof6fD7b2ck)

Even fewer authors were able to post articles with more than two thousand claps consistently. The following graph shows what I am talking about.

![Image](https://cdn-media-1.freecodecamp.org/images/6PFhMUUA5x-1QzZb-uqeIS2BvOe-x60NIEv9)

But be advised, this cutoff for the top 1% includes articles written for vastly different genres.

Can we really compare the performance of a poetry story to that of a self-improvement story? Each has a vastly different audience, varying in size, taste, and personality.

Luckily, Medium already separates its content with tags. All we need to do is find the top 1% of each tag on Medium.

#### How many claps do the top 1% of each tag get?

Here are the 99th percentiles of claps-received by an article for each of the 36 tags in our data.

![Image](https://cdn-media-1.freecodecamp.org/images/fZorT62hzde6AUndHgZ3XNrKjRNfwjmxvumk)

Some of Medium’s most followed tags (Self-Improvement, Productivity, Life-Lessons) have the highest cutoffs for being in the top 1%. While the tag with the most stories (Travel) had the lowest cutoff.

I haven’t been able to come up with a reason for this spread, so I would love to discuss this more in the comments.

Here are the individual 99th percentiles for each of the 36 story tags.

![Image](https://cdn-media-1.freecodecamp.org/images/h5KWt2Db1WcXb0d5XB1he5pjyxmuV9YBV-Cx)

So there we have it! You can use the above numbers to compare the performance of your stories to that of similar authors on Medium.

For example, since this article has a data-science tag, I might make it my goal to get 2900 claps. If I could accomplish that level of reader-engagement, this article would be in the top 1% of data-science related articles on Medium.

### Conclusion

Most Medium stories get less than ten claps, and the top 1% of Medium’s stories receive more than two thousand claps. You can use these metrics as benchmarks to measure the performance of your articles, or as a goal in writing future articles.

I also included the cutoff for the top 1% of 36 popular story tags, so you can compare your work to that of similar authors on Medium.

#### Follow me if you want more high-quality data science articles. ?

_There were a few things I learned about Medium that aren’t directly relevant to this article. So I wrote a comprehensive analysis of everything I found**.** If you want to know who were: the most clapped authors, the biggest publications, and much more, look [here](https://github.com/harrisonjansma/Analyzing_Medium/blob/master/Medium_EDA.ipynb)._

