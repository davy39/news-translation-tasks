---
title: How to design a habit-forming shopping experience
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-16T16:07:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-design-a-habit-forming-shopping-experience-af7748402e90
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VG_TGt0PQnEQ12zSkAksTw.jpeg
tags:
- name: ecommerce
  slug: ecommerce
- name: Product Design
  slug: product-design
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Mohammed Bilal

  Designing for e-commerce is an unforgiving task. Consumers — especially those in
  India — are inherently price-conscious. From mobile phone accessories to televisions,
  the cheapest listing wins.

  Whether it’s Flipkart, Amazon, or Snap...'
---

By Mohammed Bilal

Designing for e-commerce is an unforgiving task. Consumers — especially those in India — are inherently [price-conscious](http://www.livemint.com/Money/3a6pTo1Zor0fw6lY0kNKZP/Those-who-forget-Indian-consumers-are-priceconscious-pay-a.html). From mobile phone accessories to televisions, the cheapest listing wins.

Whether it’s Flipkart, Amazon, or Snapdeal, price is the main thing that matters. This leaves very little room to piggyback on loyalty.

This left Flipkart with an excruciatingly interesting problem to solve: how do you create loyal customers? How do you build a shopping experience that would help curb bargain-chasing, convenience-focused behavior?

To keep the business going, e-commerce platforms **depend on periodic events** ranging from seasonal/festive sales, clearance sales, thematic sales etc., where the sellers arrive at an agreement to offer certain discounts on their listings.

To put my organization in context, in 2015 Flipkart sold goods worth $300 million during ‘Big Billion Days’, a five day sale event very primary to Flipkart’s business. During the first hour of the sale, Flipkart sold about 500,000 products — with almost 140 orders per second, across 3200 cities and towns across India.

But the life isn’t all sunshine and rainbows — even for the e-commerce giants. Flipkart sees a rise in **number of uninstalls** right after these sale events end — a **retention rate** of ~30% on average, year-after-year since 2014. Users don’t often use the Flipkart mobile app once the sale is over, also hinting at the storage constraints Indian mobile users face. They choose to keep apps like Facebook, Whatsapp, and YouTube that they’re more habituated to, but not Flipkart.

Which led us to dig a little deeper into how various category of apps pan out in terms of customer loyalty:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ctFffUcWoTTPwWFR8aXC1Q.png)

This gave us both (me and Rahul who worked on this project at Flipkart) enough context to ask ourselves: **What does it take to build habit forming products?**

### Our approach

Habits are actions performed with little or no conscious thought. Research suggests ~40% of what we do everyday is out of habit. The video gaming industry has been using the concept of `hook` to keep the user invested & engaged in their products.

The hook starts with a trigger in user’s environment. We are familiar with **external triggers** when we see notifications of varying degrees on our products. But what’s more critical to form lasting habits is **internal triggers.**

Most frequent internal triggers are emotional, and more often than not they are negative. So users try to change this negative mood by browsing Instagram or watching [funny](https://www.youtube.com/watch?v=f8uK_mWnbr4) videos online.

We make many involuntary activities through the day to escape the negative emotional state, and this is where we thought we could experiment by showing relevant deals for the user on Flipkart.

The user would give in — anticipating a **reward —** and thus engages/**invests** into the product/app.

![Image](https://cdn-media-1.freecodecamp.org/images/1*b-cUkPvUbMivM8hKgVBy0g.png)

Every morning, when we wake up, most of us feel at least one strong emotion: a **fear of missing out**. If you find yourself checking email, Facebook, or Twitter the first thing in the morning, then this may be what’s going on inside your mind.

> _The word **FOMO (Fear of missing out)** was in fact added to the Oxford English Dictionary in 2013. Although the terminology has only recently been added to our lexicon, experiencing FOMO is nothing new._

We saw an opportunity in this to create internal triggers, and initiate the hook, in addition to our external triggers.

### Our Solution

We tried to list out various archetypes of external triggers that might draw the Indian consumers’ attention in the context of shopping. **To create a medium for external triggers, we had to think of a UI pattern that could enable this.**

We observed that the traditional notifications approach might not work very well due to many of it’s inherent issues, which include an increasing [notification blindness](https://leftrightlabs.com/notification-blindness-can-be-deadly/) among consumers.

#### 1. Daily Digest: `**Infinite VS Finite Feed**`

We thought of building a **daily digest** of a finite number of products, and refresh the digest once every day. This meant we had to move away from our infinite feed of endless products, which often leaves the user in **decision-paralysis.**

This meant our recommendation engines had to be re-built from the ground up. Flipkart is a marketplace that has over 30 million products in more than 80 categories. This sheer variety means we need to map these products to users’ interests. This led us to the next challenge: relevance.

#### 2. Relevance

It was evident that personalizing this finite feed with relevant products would be a lifeline for our app’s engagement. [Traditional recommendation systems work](http://rejoiner.com/resources/amazon-recommendations-secret-selling-online/) by crystallizing usage history and f[inding patterns in it](https://www.theverge.com/2016/2/17/11030200/netflix-new-recommendation-system-global-regional).

But for us, this would only partly solve the problem. So we [interviewed a few users](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/) to understand when do they shop online, and how. We learned that our users shop in the event of two major themes:

1. **Intent:** when there’s a strong need, where the user performs a narrow search. This is where we have to make our search a lot more clinical in capturing the intent and serving the need.
2. **Interest:** On the other end of the spectrum, there’s “window shopping” for products that the user likes. And not just products — there are themes in our lives that make us (sometimes even inspire us) to shop. Maybe you’re fitness-conscious, or you’re a travel enthusiast, or you like the brand Nautica, or you recently became a parent, or your friend’s wedding is coming up. This is where we had to gather user’s interest thoroughly.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Uk6qufMgYrHpqb15a1X1Dg.png)

#### 3. Network of Things

When we reduce many millions of products into a digestible feed of a handful products, we need to think through how we could make products from various categories accessible to the user. At Flipkart, our competitive advantage is our vast and deep inventory of products.

When we profiled users, we saw that shopping happens in themes (again, intent and interest). We decided we could assign a set of meta-tags to each product, and each tag would be a node in a cloud of thematically related product sets.

Instead of grouping and dividing by categories, we turned the tables. We grouped the products in various themes and stories.

This network can be a combination organic and inorganic nodes. This means to pushing interesting event-based content to the user. And it grows differently for each user. Below is one of such network we designed for Travel.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3SDpq1RjBs2VTh7newZOmA.png)

### Design

After some whiteboarding and sketching various components, I worked on creating interactive prototypes on Pixate while putting the mocks together on Sketch.

Here’s a short video that showcases the design solution:

#### Presentation

* There are a lot of ways to present the UX of an app, but I personally feel that a **short video** centered around a user story is the most convenient yet comprehensive form of explaining.
* Write a **script** that’s an amalgamation of the set of user stories. Spend decent amount of time refining it. Run it by the other stakeholders to make sure that the backbone of the video is well in place.
* Once the script is ready, start putting the **interactive prototypes** together, into the right sequence. It’s recommended to record the same on a device to reflect the life-like experience.
* Next is the **voice-over**. I like the tone of the voice to be a bit more candid compared to the traditional advertising voice-overs. Y hire a ou can hire a voice-over artist from [Fiverr](http://www.fiverr.com)

### Sketches

![Image](https://cdn-media-1.freecodecamp.org/images/1*d_FKTB7kzEi0yBHN90lM4w.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Di-Kns3WquyknU54-ce4Kg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*NNipQG4vELVThEA8kPggpg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fskz6eUSVsDIGDj9ELM0gQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*sRPzsS7W87U86RNA0YGVeA.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*md1BrrczBA9k2pjrAdAAnw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*IEmS61tzY1cagSl5GR8Sfg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*9W9GnM7k2ZIyr0UGDEOQ2A.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*CVGaBWB8hf-gAzntGbdwHQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*o8Ak0VEoodLHNsjm9RKr8g.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Jsg_CbqSkWJLqnwMSSMRhA.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*xyywS8vmrLM6suZMc4LFKg.jpeg)

### UI

#### Prototypes

![Image](https://cdn-media-1.freecodecamp.org/images/0*gaT3Wq7L9-9-pHjh.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*b31hiO4ynbDLRrXWEFF4aQ.png)

`**Mocks**`

![Image](https://cdn-media-1.freecodecamp.org/images/1*HJxC9wTVpkktUlxBoy2Nkw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*09HZ87-OKDDg7bBE_9cK0g.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZM6AZkwdpx041rIbObGXJg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*DfuTy-C40WofEI4Mrrme8w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*KEIBdwN9-eJh-BdbtQ_VIg.png)

#### All this led to...

We shared this thought process among various teams at Flipkart to get feedback, and slowly, we saw many buying into the idea of productizing e-commerce. We soon officiated these efforts by creating a team of 4 designers to exclusively work on such **moonshot projects** at Flipkart.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EQ_UUGaKHCl8ajOiJqQqBw.jpeg)
_Skunkworks_

Thanks for reading.

_Bilal is a product designer based out of Bangalore, India. He deeply values process-driven approach to design solutions. He has been practicing design as a full-stack executionist and prototyping is one of his strengths. Bilal’s engineering academia in Computer Science helps him design pragmatically and have effective collaborations with the developers._

![Image](https://cdn-media-1.freecodecamp.org/images/1*-SRT8je-xiHvkuIQGX36sg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Lt64aXWMFd5gf6_h_fXy8w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*BrUoUgoEDS2212DqC-wMwA.png)

