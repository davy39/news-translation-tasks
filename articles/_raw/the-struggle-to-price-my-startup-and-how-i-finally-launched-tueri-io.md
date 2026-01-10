---
title: Why I Struggled to Price My Startup, and How I Finally Launched Tueri.io
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-14T16:36:05.000Z'
originalURL: https://freecodecamp.org/news/the-struggle-to-price-my-startup-and-how-i-finally-launched-tueri-io
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/photo-1543286386-2e659306cd6c.jpg
tags:
- name: Business development
  slug: business-development
- name: pricing
  slug: pricing
- name: startup
  slug: startup
- name: ' Startup Lessons'
  slug: startup-lessons
- name: Startups
  slug: startups
seo_title: null
seo_desc: 'By Dane Stevens

  Pricing can be the life or death of a bootstrapped startup.

  When I started the process of trying to price my startup I became overwhelmed with
  questions and doubts. Should we have usage-based or a tiered pricing model? How
  much storag...'
---

By Dane Stevens

## Pricing can be the life or death of a bootstrapped startup.

When I started the process of trying to price my startup I became overwhelmed with questions and doubts. Should we have usage-based or a tiered pricing model? How much storage can we offer at each tier? Should we offer a free plan? What should the base price be? What if no one wants to pay for this? What if Tueri is a failure?

I have spent countless hours trying to answer these questions and pricing has been the single most daunting part of launching [Tueri](https://tueri.io). Tueri is a completely bootstrapped startup and ultimately, pricing can be the life or death of it. Investor money is non-existent, meaning the company needs to be profitable at every stage of growth.

It boils down to these two essential questions:

1. Can I provide exceptional value and service to my customers at this price?
2. At this price, can Tueri continue to grow and be on the leading-edge so I can continue to deliver exceptional value and service?

These two questions may seem at odds, but they are essential for building a long-term, customer-centric company.

## What is Tueri?

The word **Tueri** is a Latin word that means: preserve. Tueri is an image management and optimization platform based on the idea of an **immutable** master image.

Tueri uses just-in-time image transformation, compression and conversion to deliver the perfect image to each one of your users in just milliseconds.

The idea for Tueri came during my work as an application developer. As a developer, I build customer-incentive applications for automotive parts companies. The basic premise for these sites is the more auto parts a customer (mechanic shop) buys, the more points they earn. Customers redeem points online for everything from golf clubs to TVs to vacations.

These websites receive daily file feeds from vendors with new, discontinued, and updated products. There are _thousands_ of products and no standardization on image dimensions, file sizes or image hosting HTTP protocol. I built Tueri to solve these problems.

The first version of Tueri was a simple proxy server designed to fetch remote HTTP images and re-serve them over HTTPS, removing insecure-content warnings on our customer-incentive sites.

The next version was a simple one-page PHP script using GraphicsMagick. This script fetched a remote image, resized the image if it was over a predefined width, stored it on the server and served the image over HTTPS.

These iterations soon progressed in scope and features and somewhere along the way, I realized it was saving me obscene amounts of time.

**I needed to share this with other developers.**

After a lot of work converting a personal project into something I could host for others, I was ready to launch. The only problem was, I had no idea how to price it.

## Should we offer a free plan?

Here are some reasons why a free plan makes sense:

* User Acquisition — Offering a free plan can help you acquire a ton of new users. This, in turn, should drive growth through word of mouth marketing.
* Upselling — A user on the free plan can be upsold to a paid plan.
* Supporting the Community — In my jobs as a developer, I have relied on countless free services and have benefited greatly from the open-source community.

My fear of not offering a free plan was that I would have a very hard time acquiring new users. I struggled with this question what seemed like hundreds of times, so I did some research.

I researched countless other startups. I wanted to know whether they offered a free plan, what features they included, what percentage of users were on it and if they were profitable.

I discovered the following:

* Free users will drive growth through word of mouth, but they will drive more free plan growth.
* A free plan will help you acquire more users, but only a very small percentage of those users will ever convert to a paid plan.
* A huge percentage of support is dedicated to free users.
* A free plan product is often inferior due to costs associated with back-end services.
* This inferior product is the product that people come to know your business by.

### The Free Plan Decision

I have decided not to offer a free plan in order to dedicate 100% of our resources to our paying customers. This ensures both the quality of the product and exceptional customer service.

## Should we have a usage-based or tiered pricing model?

#### Usage-Based Pricing

Pros:

* Only pay for what you use.
* Better for companies with seasonal usage fluctuations.
* Better for individual developers where low monthly spend is a priority.

Cons:

* Difficult to understand what your actual monthly bill will be.
* Potentially drastic monthly bill fluctuations.
* Harder for a developer to pitch to their company.
* Customer mentality is focused on limiting usage to keep costs down, thus decreasing the perceived value of the product.

#### Tiered Pricing

Pros:

* Easy to understand your monthly bill.
* No monthly bill fluctuations.
* A fixed monthly amount is an easy pitch for a developer to make to their company.
* Customer mentality is focused on getting the most value out of their plan, thus increasing the perceived value of the product.

Cons:

* Harder to appeal to all use cases.
* Not as ideal for seasonal use customers.
* Hard to appeal to individual developers with a minimal budget.

I scoured hundreds of pricing pages from different Software as a Service (Saas) companies; some simple, some complex. I continually gravitated toward tiered pricing models based on the fact that they were easier to understand. Many companies with usage-based pricing dedicate an entire page to explaining how to calculate your monthly bill. Even after following the examples I still could not say for certain what they would cost me.

Let's talk about an example of usage-based pricing for Tueri. Let's say its priced per image transformation. You have a simple responsive website with 10 pages and 10 images per page for a total of 100 images. You check Google Analytics for device usage: you have one desktop resolution, one laptop resolution, two tablet resolutions (portrait and landscape) and two mobile resolutions (portrait & landscape). If every image on every page gets viewed ten times by each resolution you have a total of 6,000 transformations.

Easy right? Not exactly.

In reality, you may have 10,000, 50,000, 100,000 or more page views a month. You could have 20+ different resolutions, HiDPI displays, pages with varying levels of views, and new images added regularly.

You can see how this gets complicated.

### The Pricing Model Decision

While it was not an easy decision to make, I concluded that tiered pricing was right for Tueri due to its transparency and simplicity.

## What should the base price be?

This has to be the single most difficult question to answer, at least it was for me. One that I will continue to ask and re-evaluate throughout the lifetime of Tueri.

I had to assess:

* Are we a premium or a value company?
* What type of users do we want to focus our service on?
* Do we want to serve millions of customers at a low price or thousands of customers at a higher price?
* Can we continue to provide exceptional service to our customers at this price?
* What is the time value we are providing to our customers?
* What is the monetary value we are providing to our customers?
* What does our competition charge, are they profitable, and is their business sustainable?

It boils down to defining priorities:

* I want to provide an exceptional level of service to fewer customers.
* I am in this for the long-haul and our pricing needs to be sustainable.

### The Base Price Decision

Pricing should not be static, you should assess it over time based on feedback from customers, the added value from new features, and operating costs.

We are constantly evaluating our pricing and [I would love to know](mailto:dane.stevens@tueri.io) your use case and if our pricing works for you.

## Conclusion

I finally realized that I was never going to have it all figured out, so I made the best decisions I could with the available information and launched.

There is no definitive answer to pricing your startup, but keep these things in mind and you won't go wrong:

* Exceed your customer's expectations in the service and value you provide.
* Price your business for growth.
* Launch your startup.
* Reevaluate your pricing continually.

---

Do you have any tips or questions about pricing your startup? Get in touch at [dane.stevens@tueri.io](mailto:dane.stevens@tueri.io).

---

_Originally published at [Tueri.io](https://tueri.io/blog/2019-08-14-the-struggle-to-price-my-startup-and-how-i-finally-launched-tueri/?utm_source=Freecodecamp&utm_medium=Post&utm_campaign=Pricing)_


