---
title: How we grew our SEO to bring our site 70K+ visitors a month
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-04T22:32:49.000Z'
originalURL: https://freecodecamp.org/news/how-we-grew-our-seo-to-bring-our-site-70k-visitors-a-month-73e650a05c28
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca6dc740569d1a4ca7340.jpg
tags:
- name: engineering
  slug: engineering
- name: marketing
  slug: marketing
- name: SEO
  slug: seo
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Zain Manji

  At Fiix (www.fiix.io), SEO is a big customer acquisition channel for us. We get
  more than 70K unique visitors a month from it, and a percentage of those visitors
  convert into actual paying customers.

  In this reading, I’ll show you our j...'
---

By Zain Manji

At [Fiix (www.fiix.io)](http://www.fiix.io), SEO is a big customer acquisition channel for us. We get more than 70K unique visitors a month from it, and a percentage of those visitors convert into actual paying customers.

In this reading, I’ll show you our journey of how we built our SEO.

If you have any questions throughout, feel free to send me a message through [Twitter](https://twitter.com/ZainManji) ?

![Image](https://cdn-media-1.freecodecamp.org/images/2gzV2cwJO2L63fq6wlek8f2K2gsVAAMxf8Xk)
_Fiix — Google Analytics_

### What is SEO?

SEO (Search Engine Optimization) is the process of growing organic visibility in search engine results through a non-paid manner. In simpler terms, it’s the process of aiming to have your website shown as the first result in Google (or other search engine) for specific search queries without needing to pay for ads to do so.

![Image](https://cdn-media-1.freecodecamp.org/images/zsh1wsRHej93yB9cQB4y4J9897ZErcJvSPOp)

![Image](https://cdn-media-1.freecodecamp.org/images/ZOMmuN8bKMV48aEsLLuRPicy7TwTyxBmNFD3)
_SEMRush (www.fiix.io)_

![Image](https://cdn-media-1.freecodecamp.org/images/C3Op-kmNI1tLMFizzcqtho5DZFyJhdXOr2aN)
_SpyFu (www.fiix.io)_

#### What does Google care about most when assessing webpages?

Relevance and authority.

People go to Google to ask questions and receive answers. Google’s #1 priority is to answer the user’s question as quickly, as accurately, and as reliably as possible. If someone visits Google and has trouble finding the answer they’re looking for, Google considers that a poor experience. Therefore, Google is very particular about which websites they display first.

### Why is SEO important?

SEO is one of the few acquisition channels with true scale. If done correctly, it gives your website an immense amount of traffic for free, which you can then convert to users/customers. The only cost to develop SEO is engineering opportunity cost.

Some of the best companies today rely heavily on SEO to grow and retain their user base: Pinterest, Amazon, Yelp, Trivago, GrubHub, Expedia, and more.

### How did we decide to build out our SEO?

To give a little more context, [Fiix](http://www.fiix.io) sends expert, licensed mechanics to people’s homes, offices, or locations to repair their vehicles. Our target customer is anyone that owns a car and needs a car repair. So when thinking about the decision making process an individual goes through when they experience an issue with their car, they either do one of the following primary actions:

(1) Ask the car expert in their close circle for help (e.g. parent, friend, etc).

(2) Go to the closest repair shop to them.

(3) Go to Google to find some answers to problems they’re experiencing.

When we asked ourselves what the best method to tackle #3 was, we found that SEO was the clear solution ?.

### What was our goal with SEO?

Our goal was to entice our target customers to visit our website to purchase an auto repair service that would be conducted at their home. When a car owner searches any topic to do with their car on Google, we wanted to be the website that shows up first after the user types in their query and be the place that a user can rely on to find answers.

### Okay, cool… so what did we do start?

#### 1. Start by leveraging Google Adwords (SEM) and Google Keyword Planner

SEM (Search Engine Marketing) is the process of gaining visibility in search engine results through **paid** methods. For example, if you pay Google to run an advertisement campaign for you, they can put you in the ad section at the top of the search results after searching in Google.

![Image](https://cdn-media-1.freecodecamp.org/images/rm4xzDQivREwm00xwlj-tfLWyRsX5MGAOhg8)

SEM is great for short-term/immediate results and SEO is great for consistent, long-term results. Even though we knew SEO would be an important channel for our customer acquisition, we also knew that we could not expect immediate, next-day results from it. It takes a while for Google to index your webpage, for Google to analyze and assess whether your website is popular and trustworthy, and for you to see organic traffic build up from there.

Knowing this, our goal with SEM was to not only create profitable, successful ad campaigns, but also to identify which keywords/queries were yielding us our highest ROI and acquiring us our target customers.

**Metrics we would track in our SEM campaign would be:**

(1) **Impressions**: How many people saw our ads for a given query.   
_This would tell us whether the keyword/query we were targeting was highly searched or not._

(2) **CTR (Click Through Rate)**: Total # of clicks / total # of impressions.   
_This would tell us how enticing our ad copy was to users. A high CTR was a very good sign and would influence how we construct our metadata and content for our organic webpages when it came time to develop SEO for the keyword._

(3) **CPC (Cost Per Click)**: The total $$$ amount we had to pay every time someone clicked on one of our ads for a given query.   
_This helped tell us whether the query was a competitive query or not, and whether our ad had a good quality score or not._

(4) **Conversion Rate**: # of clicks (interactions) with our ad / # of conversions.   
_This would tell us which keywords/queries were yielding us paying customers._

**Note**: to get some of this info, you don’t have to run an SEM campaign. You can instead use [Google Keyword Planner](https://adwords.google.com/ko/KeywordPlanner/Home) to figure out some general statistics. We did SEM because we wanted to create profitable Adwords campaigns regardless.

After a few experimentations, we were able to see which keywords our target customers were searching for and whether they were converting into paying customers. From this, we now knew which keywords we needed to focus on and target when developing our SEO.

**What were our findings from SEM:**

From our SEM efforts, we then figured out which keywords and queries users were searching for and that worked well for us. From this we knew we had to create pages and content on our website that would target these keywords, as these were what our customers were searching for on Google.

#### 2. Instead of manually creating webpages, dynamically create them by leveraging data.

The most time-consuming thing we could have done when creating our webpages would be to manually type out all the content we wanted on your website. It’s not truly scalable, it’s annoying, it’s time consuming, and can easily be automated with proper programming.

In our database we had a ton of information regarding all types of information related to our service offering. So what we did was dynamically create hundreds of thousands of pages with this data and form content that was specific to each data category.

All of these pages were dynamically generated through templates we created for each page and by populating the templates with content from our databases based on the given URL and query params.

This allowed us to hit every long-tail keyword/query we wanted to target.

![Image](https://cdn-media-1.freecodecamp.org/images/ZhX8OUjBEOa22NghhRgPvOXN2vn6ivTbAdtO)

The way we thought of creating this engine for developing pages on our website was sparked through [Andrew Chen (Partner at Andreesen Horowitz) and Reforge, in their lesson about developing growth loops within your product](https://www.reforge.com/blog/growth-loops) **(highly recommend you check it out)**.

#### 3. Now that we had our keywords and content, how did we optimize for SEO?

It was one thing to have content and pages across our entire website, but if it was not structured and presented in a way that makes it easy for Googlebot to crawl, then we would have difficulties showing up on Google.

**Wait, what’s Googlebot?**

Googlebot is Google’s web crawling bot (also referred to as “spider”). Crawling is the process by which Googlebot discovers new and updated pages to be added to the Google index.

When Googlebot is crawling our website, our main goal is to make sure that Googlebot is able to extract and interpret all the relevant info as easily as possible.

**So what do we improve and optimize for then?**

**On-Page factors. These are factors that are controlled by you or by the code on your page.**

* Proper use of HTML elements and structuring throughout each web page (e.g. h1, h2, h3, title, meta, etc)
* Uniqueness throughout every webpage. Each page’s content needs to be at least 70% unique compared to every other page on the website and contain barely any duplicate content.
* Discoverability in each webpage. Content displayed on a webpage should be displayed in text and not so much images, JavaScript, or CSS. Even though Googlebot is intelligent, it has a much easier time parsing text.
* Freshness throughout every webpage. Content on each page should be updated periodically to show Google that the website is actively being maintained and staying relevant.
* Placement of targeted keywords in important places in the HTML structure. For example, placing important keywords in the first <h1> tag, in the title tags, and other metadata spots.
* Having diversity of content throughout page (images, lists, videos, text, etc). It shows Googlebot that the page is rich in content.
* Server-side rendering, not client-side rendering when rendering content on the webpage. We didn’t want our content to be loaded dynamically after the page loads, because Googlebot crawls pages as soon as the browser receives the HTML response from the server.

![Image](https://cdn-media-1.freecodecamp.org/images/JYISIH6evvf8uW06Zqu7lg0BV6GpibhrnOT4)
_Google structured snippet_

* Using Google structured snippets whenever we could, so that Googlebot can parse it easier and also be able to showcase content better within the search results such as in the image to the left.
* Making use of internal links throughout the webpage so that GoogleBot can continue crawling the website and so that in can pass on SEO juice to others pages of the website.

**User Experience (UX)**:

* Making sure webpages are mobile responsive.
* Making sure webpages load quickly.

**Off-Page factors. These are factors that are not directly controlled by you.**

* **Backlinks. The quantity and quality of external links linking to your webpages is a** **very important factor. It helps Google understand how authoritative the website is. If a lot of high-authoritative domains linked to our website, it signals to Google that our website must be authoritative as well.**
* Anchor text of links. Ideally the anchor text should be consistent to the target keyword for the page it’s linking to.
* Metrics from search engines. A high bounce rate tells Google that the user went to our website with a question in mind and likely didn’t get that question answered from it. A high CTR tells Google that users are intrigued with our website and want to learn from it.

**Micro-Optimizations**

* Making sure filenames had target keywords in it.
* Making sure the hierarchy and sitemap of the website was well structured so that SEO juice can flow nicely and to our highest ROI pages first.
* Not unnecessarily linking to other websites and keeping as much SEO juice within our website.
* Increasing page session time of a user with interactive applications, online chat sessions (e.g. [Intercom](http://intercom.com)), and more.
* Using [Hotjar](https://www.hotjar.com/) or [FullStory](https://www.fullstory.com/) to see how users were interacting with our webpage and whether they were getting confused or not.
* A/B testing metadata (titles, description) to increase CTR. We did this internally and used [RankScience](https://www.rankscience.com/) as well.

### How do you measure SEO? How do you know it’s improving?

There are a bunch of websites out there that automatically measure SEO efforts. However the accuracy of them is unsure. Some of these websites are: SpyFu, SEMRush, Ahrefs, Moz, and more.

We personally use [Google Analytics](https://analytics.google.com/analytics/web/) and [Google Search Console](https://search.google.com/search-console/about) to measure most of our efforts as we can get precise numbers on traffic, CTR, rankings, and more in an aggregate view and on a precise keyword level.

**At this point, doing all of this immediately made us way better than our competition.**

### But how can we improve past the basics?

After reading some more talks from Casey Winters and Andrew Chen, we strived to do 2 more things.

**(1) Grow our SEO through “User Generated Content”**

**(2) Create custom content, manually**

User generated content is an important growth loop that can greatly boost SEO. By allowing users to create high quality content on our website, we could tackle more long-tail keywords, continue to provide answers to other users’ questions, and encourage more and more content to be made.

The way we went about this was by developing a “Stack Overflow for Mechanics”, where users can ask any car related question they had, and other users and staff members can answer any question.

We decided to create custom content manually as well, as there was some content we knew users would search for that just needed to be authored manually.

![Image](https://cdn-media-1.freecodecamp.org/images/67nxjuertJtCQu2qV6uvHvqXaBNAPNKADsQS)

### What do we still need to do?

1. More user-generated content throughout the website
2. Integrating more of Google’s technologies to make the UX of the website better, such as Google’s Accelerated Mobile Pages ([https://www.ampproject.org/](https://www.ampproject.org/))
3. More natural, organic backlinks for authoritative domains (e.g. press articles, blogs, influencers, etc)

### That’s it!

And with all that, we built the foundation of our website and let Google and time take over to bake our SEO. Now, we have 70K+ visitors a month. And even though we’ve achieved this, we still have a lot to do to make our SEO even better.

If you have any questions throughout, feel free to send me a message through Twitter: [www.twitter.com/ZainManji](https://twitter.com/ZainManji) ?

Please share with anyone you feel may find value from it as well ?

And lastly, feel free to subscribe to my free newsletter as well, where I periodically post articles just like this one: [https://zainmanji.substack.com](https://zainmanji.substack.com) ?

### Kudos ???

Thank you to the following people who helped us learn more about SEO and shape our growth efforts.

**Gustaf Alstromer**  
Twitter: www.[twitter.com/gustaf](https://twitter.com/gustaf)

**Andrew Chen**  
Website: [www.andrewchen.co/](https://andrewchen.co/)  
Twitter: [www.twitter.com/andrewchen](https://twitter.com/andrewchen)

**Casey Winters**  
Website: [www.caseyaccidental.com/](https://caseyaccidental.com/)  
Twitter: [www.twitter.com/onecaseman](https://twitter.com/onecaseman)

**Julian Shapiro**  
Website: [www.julian.com](http://www.julian.com)  
Twitter: [www.twitter.com/Julian](https://twitter.com/Julian)

**RankScience**  
Website: [https://www.rankscience.com/](https://www.rankscience.com/)

