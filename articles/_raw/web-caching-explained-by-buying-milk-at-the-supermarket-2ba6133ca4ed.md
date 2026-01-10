---
title: Web Caching Explained by Buying Milk at the Supermarket
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-11T04:45:23.000Z'
originalURL: https://freecodecamp.org/news/web-caching-explained-by-buying-milk-at-the-supermarket-2ba6133ca4ed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XUwza_UlWCm8VJ8up0Q1cg.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kevin Kononenko

  If you have ever bought milk at the supermarket, then you can understand server-side
  and browser-side caching.

  If you are an avid internet user (you probably are), you have benefitted from caching
  over and over again. But, you migh...'
---

By Kevin Kononenko

**If you have ever bought milk at the supermarket, then you can understand server-side and browser-side caching.**

If you are an avid internet user (you probably are), you have benefitted from caching over and over again. But, you might not know when or how it is working its magic behind the scenes.

From a developer’s perspective, caching makes it much easier to build high-performing web apps and web servers. Instead of needing to constantly optimize servers that are overwhelmed by thousands of requests, developers can implement caching protocols to make life much easier.

Since caching might make a difference between 1 second to load a page and 2 seconds, the impact can feel a little bit…underwhelming. But, it’s necessary if you want to handle a high volume of users.

After using caching in a past web app, I realized that there had to be a better way to explain it than just walking through the terminology. I noticed that it aligned very well with the pathway of milk from a farm to your refrigerator, so I figured that would be a better way to explain it.

In order to understand this guide, you just need to know about the [basics of web servers](https://blog.codeanalogies.com/2018/04/26/web-servers-explained-by-running-a-microbrewery/). Let’s get into it!

### What would the internet look like without caching?

Before we get into caching, let’s think about what the internet would look like without caching. Imagine, for a moment, that you are living in the 1700s or 1800s in a rural area. You own a farm, and there is no refrigeration available. You have a few cows on your farm, but their milk is not nearly as valuable since it will spoil quickly.

Quick interruption: Some cultures still do not have access to refrigeration. They will either drink raw milk directly from a cow’s udder, or [mix milk with grains and let it ferment](https://seymourjacklin.co.uk/2010/11/01/milk-monday-dairy-in-the-days-before-pasteurisation-and-refrigeration/). Interesting.

ANYWAYS, you want to sell your milk to others in your village. But, they will have a very limited time to drink the milk. Let’s say that one of your cows can produce a gallon of milk per day. But, if too many people show up to your farm looking for milk, you will need to send some home and ask them to wait til the next day.

![Image](https://cdn-media-1.freecodecamp.org/images/0*UqjXaIdDFuVLfE5k)

Also, you can’t even think about adding more cows and scaling up your operation since you have such limited distribution. Only the other members of your village can buy your milk. You have some clear limits.

![Image](https://cdn-media-1.freecodecamp.org/images/0*LaOWTms2NkZtDFj5)

Without caching, you are limited by the computing power of your servers. Caching is used to load static assets, like:

* Images
* CSS
* Static HTML files
* JavaScript files

A server, by default, must submit a new response for every incoming request. But, a request to load a page could actually mean 4 separate requests — one from each of the categories above. When you take into account larger image files, your servers can become overwhelmed by users all over the world. Then, users will experience slow load times as they wait for their page to load.

![Image](https://cdn-media-1.freecodecamp.org/images/0*4ajis8HoFZeo7SRf)

Ideally, you would want to ease the demand on your servers by storing responses to common requests. Your server would not need to handle each new individual request, but instead, your cache could deliver an immediate response. You could always pay for more servers, but that can lead to uncontrollable expenses.

### What is server-side caching?

Back to our farm scenario. Know what would make it a LOT easier to run a successful dairy farm?

A supermarket with refrigeration!

That way, people will not need to show up to your farm and consume the milk immediately. You will be able to keep it safely stored for a couple weeks at a time.

The supermarket removes a lot of the stress on your farm, because your cows will not be expected to produce in real-time. The supermarket will handle the demand. You just need to keep the cows productive on a daily basis. Even better, residents of all the surrounding villages can now buy milk from your farm, because it will always be available in the refrigerator.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kko1_aNf6X-cZzUy9IwF-A.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*jwi2U9sBznjtd_zZoszx6w.jpeg)

Just like a supermarket, a [server-side cache](https://www.digitalocean.com/community/tutorials/web-caching-basics-terminology-http-headers-and-caching-strategies) will handle popular requests and deliver content much more quickly and reliably.

In the image above, I use the term **caching proxy**. A caching proxy is a server that stores the static files that are used to respond to common requests. A caching proxy will intercept common requests and quickly deliver a response. It prevents those requests from stressing your main web servers.

You probably have a bunch of questions like,

1. What determines a “popular” request?
2. How long will the proxy cache the responses?

That would require a longer tutorial on setting up caching, but for now, you should know about one important concept called **freshness**. The caching proxy will have different files that have been cached at different times, and it needs to decide whether it should still serve these files. This will depend on your **caching policy**.

This also works just like milk in a supermarket. A supermarket manager needs to decide how long they will hold your milk before throwing it out. Caching proxies measure their success through a **cache hit ratio —** the percentage of content that can be served through the caching server.

### What is a CDN?

So far, there is one grocery store selling your milk. Although that is a big improvement, you still have no way to get your milk to people outside the range of this local store. You are going to need to add more stores if you want to scale up your operation.

So, let’s say you start distributing your milk to more supermarkets. Now, you can satisfy customers across a much larger geographic range. This is similar to a content delivery network, or a CDN. A CDN is a series of proxy servers (like we discussed above) located all over the world.

As an end-user, you probably feel that high-speed internet allows most sites to load very quickly. However, this is only because they use CDNs to deliver static files at rapid speed!

If you are located in England and you are trying to load a file cached in a server in Virginia, you will experience some delay since the original signal can only travel so quickly along thousands of miles of cable. A local caching proxy in the United Kingdom would allow the site to load faster.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RvgDAlDHt24dcvBImoxCZQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*H8xPw2BZp_bAwgaUKeI2eA.jpeg)

So, your servers can send a copy of static assets to each of these proxy servers within your CDN network, and they can handle local requests until the assets are no longer “fresh”. Some common CDN providers include Rackspace, Akamai, and Amazon Web Services.

### What about browser caching?

Now, people across the country (or the world) can bring home cold milk from your farm. There’s just one issue — they have no way to store it in their own homes. Your customers still need to drink the milk pretty quickly after they buy it, and then return to the grocery store for more. So, this system still doesn’t serve customers particularly well.

The solution? A refrigerator!

With a fridge, you can store the milk locally and avoid a return trip to the supermarket. In caching terms, we’re talking about a completely separate location for storing static assets since it is on the client-side, or on the same computer as the browser. Our proxy server was located in a remote location.

This is great for sites like Facebook or Amazon that you might frequently visit. It’s great for their server costs too, since they can reduce the number of requests they need to handle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RncfZ7NATKE9ciV-F54ODg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wct_mY7Bbuvsd4pwyQJ5Dg.jpeg)

One key thing to note — we are NOT saying that milk magically arrives in your refrigerator! You still need to make that initial request that reaches either the server or the proxy server. After that, you can cache some of the files locally.

How does your browser know when to request new files from the server? Otherwise, you would never experience updated versions of these local files.

Well, just like milk producers put a date on their milk packaging, servers will add some sort of identifier within the HTTP response header. There are actually [4 separate systems for HTTP caching](https://betterexplained.com/articles/how-to-optimize-your-site-with-http-caching/). The scenario shown above closely resembles the “expiration date” method. Some of the other methods still require your browser to check with the server before sending the cached file.

![Image](https://cdn-media-1.freecodecamp.org/images/0*7yAXQNZN-0XzIQHB)

### When To Start Using Caching

Let’s say that you are building your first web app. Until you have thousands of users, you probably won’t need to worry about caching protocols, since server costs will still be low. However, as you scale up, you will need to implement caching if you want your app to load quickly.

Heroku, for example, is a great tool for deploying your first web app. But, it requires you to use a [separate service to implement caching](https://devcenter.heroku.com/articles/http-caching), like Amazon’s CloudFront or CloudFlare. That will take more time to learn.

On the browser-side, you have probably experienced caching when you are trying to reload a page with new static assets, but the page simply won’t change. No matter how many times you refresh the page, nothing changes.

This is usually because of some caching protocol on the browser-side. To bypass your browser’s cache and request new assets from the server, you can use **Cmd+Shift+R** on a Mac or **Ctrl+Shift+R** on PC.

### Get More Visual Tutorials

Did you enjoy this tutorial? Give it a “clap”! Or, sign up here to get my latest visual tutorials from the CodeAnalogies blog.

