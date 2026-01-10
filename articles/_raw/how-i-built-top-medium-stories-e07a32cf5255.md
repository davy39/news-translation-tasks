---
title: How I built a leaderboard with the top Medium stories of all time. And how
  it almost died.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-10T11:21:01.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-top-medium-stories-e07a32cf5255
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BUxJuact-veqvL9lvnHlxw.png
tags:
- name: Life lessons
  slug: life-lessons
- name: medium
  slug: medium
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: writing
  slug: writing
seo_title: null
seo_desc: 'By Michael Deng

  Last year I built Top Medium Stories — a website that showcases the Medium’s top
  stories of all time. This is the tale of how a lone developer scraped thousands
  of stories and hitting seemingly fatal roadblocks.

  Spoiler alert: Life fi...'
---

By Michael Deng

Last year I built Top Medium Stories — a website that showcases the Medium’s top stories of all time. This is the tale of how a lone developer scraped thousands of stories and hitting seemingly fatal roadblocks.

_Spoiler alert: Life finds a way. You can check out the leaderboard — updated daily — at [TopMediumStories.com](https://topmediumstories.com/)._

### Why did I make this?

As a long-time reader on Medium, I’ve always been curious what the most popular stories were. While the personalized feed and topic pages surface many great stories, just as many slip through the cracks.

Driven to unearth the gems buried in Medium’s annals, I set a new goal in early 2017: I was going to find the most popular stories of all time on Medium and share them with the rest of the world.

My goal culminated in me publishing my list of the [Top Medium Stories By Year](https://medium.com/startup-grind/most-recommended-medium-stories-by-year-2db66605d5be).

I compiled the stories manually, which was a grueling task. Over the period of a week, I visited every top stories page since September 10, 2014 (when the top stories feature debuted). To find even earlier stories, I dug through publication archives using the Wayback Machine to fetch ancient copies of Medium pages.

I built a massive spreadsheet of every story I found. It was a ton of mind-numbing work, but I was proud of the result.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ctml_IoHbj0xWy78KyJhuw.png)
_A small section of the colossal spreadsheet ?_

But my feeling of pride was short-lived, as the list became quickly outdated. I wanted to keep it up-to-date, but doing so manually was impossible.

Then, something dawned on me. I had already determined the manual steps to collect data the first time. There was was no reason why I couldn’t just automate those steps with code. Thus, I decided to turn the list into a dynamic website.

### Automating data collection

To automate the manual steps described above, I wrote a web scraper using Python [Scrapy](https://scrapy.org/).

The scraper crawls through every top stories page since September 10, 2014 and tosses any story it sees into a Python dictionary. The dictionary is then sorted by the number of claps each story received and written to a JSON file. (Claps are Medium’s equivalent of a “like” or an “upvote” and readers can give a story up to 50 claps.)

Here’s a snippet of the JSON file:

```json
[  “We fired our top talent. Best decision we ever made.”,   {    “recommends”: 79000.0,     “pub_url”: “https://medium.freecodecamp.org",     “author”: “Jonathan Sol\u00f3rzano-Hamilton”,     “image”: “https://cdn-media-1.freecodecamp.org/images/1*4hU3Xn7wunA81I3v17JIrg.jpeg",     “year”: “2017”,     “story_url”: “https://medium.freecodecamp.org/we-fired-our-top-talent-best-decision-we-ever-made-4c0a99728fde",     “pub”: “freeCodeCamp”,     “author_url”: “https://medium.freecodecamp.org/@peachpie"  }],...
```

Before building the scraper, I checked Medium’s [robots.txt](https://medium.com/robots.txt) file to verify that I wasn’t violating any policies. I also set the scraping speed very slow (2 seconds between each request), so the scraper wouldn’t hammer Medium’s servers.

#### Converting the data to HTML

The next step was transforming the JSON file into HTML to display the stories on a web page.

I installed [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) to do this. First, I constructed an HTML template with empty tables and rows. Then, I wrote a script that uses BeautifulSoup to populate the template from the JSON file.

With a basic HTML file containing all the stories I want to display, it was time to create the actual website.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3XTqVVycq5riBcjR3h5ZgA.jpeg)

### Building a kickass website

When planning the website, I had three goals in mind:

#### 1. Minimal and elegant design

The design language is centered around plenty of whitespace and high-contrast text. This way, the focal point is on the stories its trying to highlight, not on the aesthetics of the website itself.

I also added a “Compact” view mode, which hides feature images from the website. This allows readers to skim through the list with ease.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EqIyKAmHT-FrzN4qm7b9mQ.png)
_“Compact” mode_

#### 2. Fast

The first version of the website was quite sluggish. This is because it was trying to load hundreds of feature images at once.

To solve this issue, I used “lazy loading.” When you land on the website, only the first 50 stories under “All” are loaded. If you want to see more stories, you have to click on “Load more.” This design pattern drastically reduces the initial loading time.

Also, to make navigation feel more responsive, I designed this website as a single-page web app. When you click on a button, you don’t navigate to another HTML page. Instead, jQuery switches the view instantaneously.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nU4Novi6IXdTY7CqBZPzgA.gif)
_Responsive navigation and lazy loading in action_

#### 3. Lightweight

To keep the website light, I chose to forgo most popular frontend libraries. I didn’t use Bootstrap, and I kept JavaScript/jQuery usage to a minimum.

Taking a glance at the project repo reveals a very minimal setup. A few HTML files, a CSS file, a couple scripts, and a handful of data files.

As a result, the website doesn’t have many moving parts and dependencies. It’s very simple to maintain and debug.

### **Testing and launching**

I shared the prototype with a couple of friends and asked them to rip it apart. Using their feedback, I iterated on the design twice. Then, I launched on Product Hunt.

I could barely sleep that night. I still remember constantly refreshing the page checking for new comments until I passed out from exhaustion.

The next morning, I scrambled out of bed and clawed open my computer. I couldn’t believe my eyes! Top Medium Stories was at the top of Product Hunt’s homepage. At the end of the day, it was awarded the #2 product of the day.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4XuWJfp8NxmYqJjul8qVRg.png)
_[Product Hunt page for Top Medium Stories](https://www.producthunt.com/posts/top-medium-stories" rel="noopener" target="_blank" title=")_

### The sudden death of Medium Top Stories

The Product Hunt launch exceeded my wildest expectations, and I was on cloud nine for a long time. But I knew I wasn’t done until I shared my project on Medium. I started this post half a year ago and I finally finished it a few weeks ago. I was beyond excited to publish it.

Before submitting, I decided to run the data collection script one more time to update the website.

The script failed catastrophically.

“No big deal. Either Medium has an outage or my internet isn’t working,” I thought. But I was so wrong. When I realized what actually happened, I slumped into my chair and dragged my fingers down my face in frustration.

I kid you not, two days prior Medium had removed the top stories page from their website. They scuttled the very page my scraper depended on to function!

I emailed Medium promptly, asking them to consider reverting the top stories page. I didn’t get the response I was looking for.

![Image](https://cdn-media-1.freecodecamp.org/images/1*h6hNC0_A-gXqzce1xzDliA.png)

But I didn’t blame them. My website wasn’t officially supported — they weren’t obligated to do anything. Even if they didn’t make this particular change, eventually one of their updates would break my website. It was inevitable.

I felt hopeless. Since the website couldn’t be updated anymore, it was no more than a static list that was soon to be obsolete. In my mind, Top Medium Stories was dead on arrival.

### The sprouts of new life

For a while, I worked on other stuff and didn’t look at Top Medium Stories at all. But I couldn’t stop thinking about the unfinished story of the website. I wanted to publish a postmortem — even if it didn’t have a happy ending. It felt like a good way close out the project.

I closed the article with:

> “So, I hope you enjoyed reading about Top Medium Stories. It was an amazing experience and I’m proud of what I made — I’m sorry it had to end this way. There will always be things you can’t predict or control, and they can wipe away your work in a heartbeat. That’s life.”

As I stared at my finished draft, I realized something. **I hate sad endings.**

Suddenly, my eyes locked on that same JSON blob I mentioned earlier.

```json
[  “We fired our top talent. Best decision we ever made.”,   {    “recommends”: 79000.0,     “pub_url”: “https://medium.freecodecamp.org",     “author”: “Jonathan Sol\u00f3rzano-Hamilton”,     “image”: “https://cdn-media-1.freecodecamp.org/images/1*4hU3Xn7wunA81I3v17JIrg.jpeg",     “year”: “2017”,     “story_url”: “https://medium.freecodecamp.org/we-fired-our-top-talent-best-decision-we-ever-made-4c0a99728fde",     “pub”: “freeCodeCamp”,     “author_url”: “https://medium.freecodecamp.org/@peachpie"  }],...
```

And I had a revelation. I didn’t need the top stories page to update the website. Instead, I could visit each url in the JSON file and pull the data directly from the story’s webpage.

To fetch new stories, I could scrape the new Popular on Medium page, which would give me the top stories published recently.

Having refactored my code, I realized something: it is possible that not every single popular new story will end up being showcased on the Popular on Medium page. So if you happen to read a story that you think should be on Top Medium Stories but isn’t, please let me know. Just send the story’s url to **michaeldeng18@gmail.com**, and I’ll add it in right away. Together, we can ensure the leaderboards are as comprehensive as possible.

There is always the risk that Medium might one day restrict scraping completely, or even release their own ranking of stories. Either of these changes could make Top Medium Stories obsolete.

But in the meantime, I will continue maintaining Top Medium Stories, the best website for discovering awesome stories.

If by this point you still have not seen Top Medium Stories, [go check it out](https://topmediumstories.com/)! It’d make me very happy if the site helps you find extraordinary stories that you would’ve otherwise never stumbled upon.

Thanks for reading!

