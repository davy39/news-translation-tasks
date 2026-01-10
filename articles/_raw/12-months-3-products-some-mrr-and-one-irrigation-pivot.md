---
title: I left my full-time job one year ago to ride the indie hacker road. This is
  what I've learned.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-07T06:00:00.000Z'
originalURL: https://freecodecamp.org/news/12-months-3-products-some-mrr-and-one-irrigation-pivot
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/1_tiAicAxobXZwIwERPf03tA.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: product development
  slug: product-development
- name: product hunt
  slug: product-hunt
- name: startup
  slug: startup
- name: ' Startup Lessons'
  slug: startup-lessons
seo_title: null
seo_desc: 'By Pierre de Wulf

  My partner Kevin and I have been working and talking about different side projects/startups
  for over 5 years. Two years ago we released our first product to the public, but
  it was one year ago that we decided to go full time on the ...'
---

By Pierre de Wulf

My partner Kevin and I have been working and talking about different side projects/startups for over 5 years. Two years ago we released our first product to the public, but it was one year ago that we decided to go full time on the indie hacker road. In this post, I’m going to explain our journey, our background and how we did it after many failed attempts.

This post is not about some magic product we launched in 2 days while getting 10k signups and reaching $20k MRR in one month while working 4 hours a week in Hawaï. This post is more about the small wins and loses we had during our first year in the Indie Hacker world, and the things we wish we knew before starting.

This post is about 3 products: one irrigation pivot, one startup pivot, and of course, some MRR.

_(Disclaimer: ScrapingBee was initially launched as ScrapingNinja, but due to some copyright issues we had to quickly rebrand it. We'll talk about it in a future blog post.)_

## Background

It started when we were both employed in different startups as software developers. We had lots of ideas and we loved to build side-projects for fun.

Kevin and I were doing lots of Web Scraping in our jobs. Kevin worked at a Fintech startup called Fiduceo which was acquired by a big French bank, and they were doing bank account aggregation, like [Mint.com](http://mint.com/) in the US. He was leading a small team handling the web scraping code and infrastructure.

I worked in the US and then came back to France to work in the biggest French real-estate data provider as a data engineer. Part of my job was to find, gather, extract and load new data sets from the web.

So we both had experience with Web Scraping and data at scale.

## Our first project: ShopToList

One of the first “mini-success” we had was [Shoptolist.com](https://www.shoptolist.com/), a B2C website/browser extension which is a universal wishlist that sends you alerts if it sees any price drop. It was really just a fun side project that was never meant to be more.

It allowed us to try many different things and to discover that acquisition is really, really, really hard. We quickly reached 1k users by just submitting our product on frugal/fashion subreddits. We were very happy about it because it was just an experiment. 

Every day we had a script that scraped each product in our database to update its price, and we were sending an email in case of a price drop. The links in the email were affiliate links, so we took a small percentage if the user ended up buying the product.

In theory, this model works great, but in practice here is what happened:

* Out of 1000 emails sent, about 20–30% were opened
* 2% click on the product links that were on sale
* Out of this 2 %, 5–10% buy the product

The percentage we earned was very small, depending on the niche it was 0.5–5%, so this business model only works with millions of users.

And this is where we hit a wall, we did not manage to create sustainable growth. We tested many things, content marketing, affiliation, some paid advertising, but we just did not manage to create growth. And since it was just a little side project that only took us 2 weeks to build, we were ok with that.

For us, this was a very good experience, because this was the first project we really shipped to real users, and we learned a lot.

By digging into the database we noticed that a few users had thousands of products saved inside ShopToList. It seems strange unless they were crazy impulsive buyers, the majority of users had like 20 products saved on average…

So after a little “investigation”, we discovered that these users were E-commerce owners that were “spying” on their competitor…

## Our first pivot: PricingBot

We assumed that those people were doing this to receive alerts when their competitor’s products were changing the price. There were many solutions on the web that allowed someone to do this, but ShopToList allowed them to monitor thousands of products for free when other solutions were quite expensive.

We did a small market research and discovered that many tools offered to monitor your competitor’s product, however, all those tools seemed either really difficult to use or really expensive.

Because we felt we could do better, the PricingBot idea was born. I quit my job and we both decided to commit full-time on this. Side project era was over ?.

We made a landing page explaining our value proposition, nothing fancy but something clear and nice enough so people could trust us. We got 60 signups from different E-commerce owners in different niches.

While technically challenging, extracting E-commerce product data was something we knew how to do thanks to ShopToList, so building the MVP was pretty quick.

We launched our beta on ProductHunt on November 2018 and it was a big success, followed by a big crash, the classic **startup trough of sorrow.**

![Image](https://www.freecodecamp.org/news/content/images/2019/10/1_t_YsErGF5PCdAzpwaQ7Vzw.jpeg)
_ProductHunt launch_

You had to upload a CSV file with your product catalog, and for each product match it with a competitor product URL.nIt’s ok for several dozens of products, but people had often hundreds or thousands of product in their online store.

So with this feedback, we created some integration with popular E-commerce platforms like Shopify and Woocommerce to let people import their catalog in one click.

Our activation **tripled ? ,** we were very happy about how things were going. One thing to note, though, is that until this moment the product was completely free and we did not ask people for money.

At this point in time here are the few numbers we had that made use happy:

* We managed to have around 200 signups with $0 spent
* 20 users seemed to use the product and had their account fully set up

What could go wrong right?

We decide to close the beta and start asking our user to pay for our software with a classic SaaS model with three plans, $29/$99/$299 per month based on volume.

The first day was magic because literally several seconds after sending the email announcing the end of the beta we got our first customer for a $29 plan ?

We also managed to signup a $299 soon after, but for him, we had to manually set up his account and manually match 1000 products across 10 websites. It was long but we felt it was worth it. We were wrong! Just before renewing he churned telling us PricingBot was very good but not useful enough for him. We were sad and angry, mostly at ourselves, but decided to move forward and continue.

It seemed we were on a good path and that we just needed to go all-in on marketing. And that’s what we did. Content marketing, cold outreach, affiliation, SEO you name it!

But before diving into this, let’s talk again about our activation

## Mistake #1: bad metrics leads to bad conclusion, bad conclusion leads to bad decisions (in Yoda’s voice)

When we first decided to monitor our activation rate we assumed that one user was activated when he did two things:

* Add at least one of his product, (or link his store with our built-in integration)
* Add at least one of his competitor’s product

And so, with that definition, we had around 10% of our users that were “activated”. Considering that at that time most of our users were coming from ProductHunt and that hunters are known to easily signup to products they don’t plan to use and just for the sake of it we were happy with these numbers.

But we were wrong.

This definition meant that someone who owns a Shopify store with 4000 products, and who adds only one competitor’s product, was activated. This was silly. Someone who only adds one competitor’s product out of 4000 of is own catalog won’t use PricingBot to do price monitoring and surely won’t pay for it. We learned this the hard way.

Because soon after we had this first paying customer, nobody followed, literally nobody. At first, we did not understand. Then it was obvious: out of 200 signups, we had 20 active users, out of 20 active users we had 1 paying customers, so the only solutions were to have more signups.

This was another mistake.

## Mistake #2: Thinking our only problem was acquisition

We thought we only needed more users and just went full marketing. Because we did not know the e-commerce community very well we had some trouble starting. But we eventually managed to write some piece of content that was shared on relevant Facebook/Reddit/LinkedIn group that brought in a few leads.

We also did some paid advertising and cold outreach but it failed miserably.

One month later, we needed to see the obvious: we were not on the right path.

Our leads used the product but did not pay, and even if all the leads we brought in paid, it would have not been sustainable.

At this point in time we finally decide to understand better why users don’t use our product more and with feedback request and lots of analytics insight we discover two things:

* For most of our users, PricingBot was a nice to have, but it was not something worth paying for 
* Most of our users didn't want to do the setup because it is too tedious, but they didn't want to pay us to do it for them.

Next thing we knew we revamped our whole onboarding process and try to automate as much as possible. But it was still not working.

When you want, as an e-commerce owner, to monitor your competitors, you first have to link your products with your competitors - and this was the hard part. This part alone meant approximately 1 hour of work per 100 products you want to match. This was way too much time for an e-commerce owner working alone with a 10k products catalog.

## Fear, Uncertainty, and Doubt

To help you understand how we felt at that point in time let me just recap the timeline:

* January 2018: ? we launch ShopToList
* July 2018: ? I quit my job and we decide to build PricingBot
* October 2018: ? After a busy summer and 1 month of code we launch the MVP in beta
* January 2019: ? First paying customer
* February-March 2019: Acquisition, product dev

Back in May 2019 we kind of hit a wall. Nothing we did really worked and it was hard staying motivated. The only silver lining was that we managed to rank well on Google so we had, every day, around 3 new signups without any acquisition.

But we still did not manage to make them pay. And we still did not manage to make them configure their account.

This period of time was hard because it was full of negativity. My cofounder and I both knew that we were not moving forward. While this did not degrade our working relationship, it certainly degraded our working productivity.

We both felt that no matter what we did, we were not able to move any meaningful needle that could have boosted our business.

We improved the product a lot, managed to gather some signups along the way but it was not enough. Here is a look at our revenue.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/1__V2G-InXFLPChcA2eF2Wpg.jpeg)

## One agricultural pivot to build, one startup pivot to make

Mid-June 2019 things are not looking good, we only have 3 months to launch a successful business. We both agreed in 2018 that we gave ourselves 1 year to launch something that worked, 1 year to reach “[ramen profitability](http://www.paulgraham.com/ramenprofitable.html)” ?.

We had a long talk beginning of June and we both agreed that we needed to step back. We currently had 3 options:

1. Continue with PricingBot hoping that some magic happens and that we cross 4k MRR in 3 months
2. Leaving the company and start going our own way
3. Building something else

Point 1 was hard because we were both fed up with the product. Everything we did seemed useless and it was not working. Point 2 needed to be addressed, but although it was not a success we felt that working together was working really well (in the human side of things). It would be a pity to give up. 

But we chose option 3, and we are both very happy with the outcome of that talk and full of energy. We only needed one thing: to choose what we would build.

We also decide to do something we should have done earlier, we sold ShopToList. The whole deal was done in less than 1 month thanks to [1kprojects.com](http://1kprojects.com/) and it brought some welcomed money in our company bank account.

In the same time, my father in law, a farmer in the south of France called because he needed help assembling an irrigation pivot. The heatwave was supposed to be hard in June (and guess what, it was), and it was an urgent job. We both decided that this was a good opportunity to take a break, to think, each on our side, about the future product, and to come back full of ideas and motivation.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/1_tiAicAxobXZwIwERPf03tA-1.jpeg)

It was kind of ironic because this pivot kind of funded our pivot.

_Disclaimer: If you ever need to buy an irrigation pivot_ I _strongly suggest that you look into Valley pivot (PS: this post was not sponsored by Valley in any way)_

## ScrapingBee

Two weeks later, we both found ourselves with a bullet list of product ideas, some good, some bad, some crazy, some boring, some exciting, well, you get the idea. Both lists were diverse. However we quickly agreed on one idea, because it really stood out from the others. Let me explain.

While working on Shoptolist and Pricingbot, and also in our previous work experience, there were three things that we always needed to do for our web scraping infrastructure: 

* Transforming websites into a structured API, 
* Running headless browsers at scale, 
* and managing a pool of proxies.

When you extract data from lots of different websites, you always have to deal with Javascript-heavy websites / Single Page application, and you don’t really have other choices than running headless browsers to render all this Javascript.

Running a headless browser like Chrome is really painful because the same thing happening on your desktop (high memory usage, poorly coded Single page application eating 100% of your CPU) will happen on your servers. So it is not only painful but very expensive to do this on your own when you don’t know what you are doing.

When doing web scraping at scale, you often have to use proxies for different reasons. The website you are visiting with your bot may show different information based on your location - for example, a price in Euro in the Euro-zone and a price in dollars in the US.

Dealing with proxies is painful too. There are lots of shady companies selling bad quality proxies so you either have to run your own proxies or test dozens of proxy companies to make sure your proxy pool is always up.

We used to solve all those problems using APIs that were either not really efficient or crazy expensive. These are problems that we solve multiple times in our projects so we thought about packaging it into an API and leveraging our experience to make all kinds of web scraping APIs.

We decided this time, to make things right and to try to avoid doing the mistakes we made with PricingBot while creating [ScrapingBee](https://www.scrapingbee.com/).

## Mistake avoided #1: creating a product you won’t use

One of the biggest problems we had with PricingBot was to find where our potential users gathered online. What group did they follow, what blog did they read, what influencers did they listen to. And the reason was simple, having never worked with or in the e-commerce industry except for some freelancing gigs, the whole landscape was unknown to us.

With ScrapingBee we would be our own users and it changed everything. I know this advice is not new, but often this advice is meant to build a better product. And sure, being one of your own users allows you to build a better product.

But for us, the game-changing fact was that being our own users meant that we knew exactly where to find and how to reach potentials leads.

Kevin and I also have our own blogs running for quite a bit of time and I wrote last year a book dedicated to web scraping in Java. This directly translated into 20k monthly visits that we could leverage to promote ScrapingBee.

And it worked. In about 2 months, we reached 150 beta signup, 4 times the amount of beta testers we had for PricingBot.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/1_s0LCG7DV7ZRrtQL2dN3HsQ.jpeg)

## Mistake avoided #2: Spending too much money

While building PricingBot, we spent a lot of money on useless infrastructure, APIs and software without reaching Product-Market Fit.

We got to get our money back thanks to ShopToList sale and my agricultural skills before we launched ScrapingBee, but this time, we were way more careful about how we spent it.

I know spending several thousand dollars to bootstrap a project is not a lot of money but we weren’t comfortable with spending more. So we decided to be careful with how we would spend it with ScrapingBee.

We basically reduced our costs by only finding deals (❤ AWS Credits) like [Secret](https://www.joinsecret.com/) which basically give you 6 months free for lots of SaaS or a huge discount.

We decided to do more with what we had, and so far we don’t regret it.

I’ll talk more about products and tools we used in a future blog post, this one is already long enough.

## ? Launch ? and mistake avoided #3: not asking for money from day one

One thing that did not work well with PricingBot is that for months, we built a product that was free to use. I know this is a classic mistake, but this is not the worst part. The worst part is that we knew it was a mistake. In the last 4 years, we’ve read tons of books, interview, blog posts about startup and everyone seems to agree that the sooner you ask for money the better.

But it was easier said than done and we did not dare ask for money while building PricingBo. We just did not think anyone would pay for an unfinished product.

We did for ScrapingBee. The pricing for ScrapingBee is again a classic three plan SaaS based on API call volume/feature starting at $9 / $29 / $99 per month and an Enterprise plan.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/1_u8GtUK5YwugRzzDPJ11BBA.jpeg)

We “soft-launched” first to our mailing list and got our first few small paying customers. Again, we had the same experience with PricingBot but this time it was different. With PricingBot, every paying customer we had was really hard to get, we had sent them tons and tons of email and they took a long time to finally pay.

With ScrapingBee it was different. Our first 2 customers had never talked with us before.

We then started to blog and got tons of leads along with a few more paying customers including a big Enterprise plan as you can see in the MRR chart below.

Then it all went quickly, Kevin and I both having blogged about programming, creating insightful content about Web scraping is not a problem for us, and we knew how and where to promote it.

One particular piece of content we wrote, a [web scraping guide](https://www.scrapingninja.co/blog/web-scraping-without-getting-blocked) completely exceed our expectations.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/1_afh6y24VhYabHLd0vFbCbA.png)

  
This post alone meant that in 2 months we had 3 times the traffic we had in one year of PricingBot. This post not only brought traffic but also customers with real $. It also allowed us to signup the first big enterprise plan that allowed us to reach and cross $1000 MRR.

## The future

Of course, it’s really early to say if [ScrapingBee](https://www.scrapingninja.co/) will be a success or not.

This big enterprise customers thanks to the success of our first blog post could only be an outlier phenomenon that won’t reproduce in the future. Maybe it will. But one thing is certain, things are looking way better with ScrapingBee.

We have lots of engagement from our users and leads, the conversion rate from trial to paying customer being close to 5%.

We also love to talk with our potential customers (❤️ Zoom) and we have the feeling that ScrapingBee is really a must-have for them, instead of a “nice to have”. (small tips: we offer 10 000 free API credits for users that accept to have a small 15 minutes talk with us, this already allowed us to have 50 real conversations with real people about ScrapingBee)

![Image](https://www.freecodecamp.org/news/content/images/2019/10/1_qr_1khM2_jK0eooATk8JbQ.png)
_In-app message to incentivize users to schedule a call with us._

In the months to come a big challenge will be to find profitable and scalable acquisition channels. We hope that content marketing will continue to work and that it will improve our SEO to get organic traffic. Writing a good piece of content may not be enough and we really have to discover other acquisition channels.

The other big challenge is to prioritize features in the API-store. Meaning figuring out what users **need** not blindly implementing what they want, and hopefully, manage to get them to pay before the feature is implemented.

We still don’t know what we want to do with PricingBot, we seriously think about selling it but are a bit afraid of all the paperwork involved (it was much easier with ShopToList because ShopToList did not bring any money in, so no bank account, Stripe account, etc…)

We also still have a lot to learn and a lot to prove before being able to say that we build a sustainable and profitable business but for the first time in our lives, we feel that it can be done, time will tell us if we’re right.

I really hope you liked our little story and that your learned some interesting bits along the way. We plan to do this kind of posts every 3 months at least, please tell me if you'd like to read the next one ;).

