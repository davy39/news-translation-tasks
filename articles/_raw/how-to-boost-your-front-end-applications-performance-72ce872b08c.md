---
title: How to boost your front-end application’s performance
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-18T19:19:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-boost-your-front-end-applications-performance-72ce872b08c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Vmq3ETGdUZPZe9vZu6CkVg.png
tags:
- name: JavaScript
  slug: javascript
- name: performance
  slug: performance
- name: General Programming
  slug: programming
- name: software
  slug: software
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dimitris Kiriakakis

  If your website takes longer than 3 seconds to load, you could already be losing
  nearly half of your visitors.

  Yes this is a fact, proven by several research studies. Long loading times can have
  a devastating impact on your app...'
---

By Dimitris Kiriakakis

If your website takes longer than 3 seconds to load, you could already be losing nearly half of your visitors.

Yes this is a fact, proven by several research studies. Long loading times can have a **devastating** impact on your application’s conversion rates. On the other hand, optimising page load time leads to noticeable improvements in customer experience, conversion rates, SEO and ultimately, your product’s **success**.

So let’s say that you have recently built a website or a frontend application using a modern JS framework (Angular, React, VueJS etc.). How can we make sure that performance is not going to hold it back from success?

First things first. We have to somehow gather some **data**. When it comes to measuring a frontend application’s performance, the tools I trust the most are:

* Google chrome’s [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
* [Speedcurve](https://speedcurve.com/)

Both tools can help you keep track of all the major performance KPIs (Pagespeed Index, Time to Interactive, First Contentful Paint, etc.).

**Lighthouse** is included in your Chrome’s dev-tools, and by analysing your website/web-app, it can give you some really useful hints on how to boost it up.

![Image](https://cdn-media-1.freecodecamp.org/images/To1jGG1giiJeWCpEVTGl1v2Hznyz4eKcRncT)
_Chrome’s lighthouse can give you some really helpful hints_

With **Speedcurve** you can have all these KPIs, plus the ability to monitor them across time.

So now that we are able to measure our success, let’s move on with optimising the parts of our website that play the biggest role.

### Images

Images are a key part of every website. On average, images make up for more than 60% of data that are loaded on web pages. Being such a critical component of almost all websites, image optimisation is, in my opinion, the most important, and perhaps the lowest hanging fruit.

#### 1. Resize your images and make them responsive.

The most important thing to check is that you are not using a bigger resolution than the one you really need. So you have to resize your images to fit exactly the requirements of your layout.

![Image](https://cdn-media-1.freecodecamp.org/images/PqV7uCLjZMyaZwwkQbMDtml61iC9UktvPOjm)
_Responsive layouts need responsive images_

Furthermore, you have to make sure that your images are as **responsive** as your layout is. There is a great tool that I have been using lately, which can help you generate all the different versions of the images that you might need and also generate the HTML5 code that can utilise them. It’s called [Responsive Image Breakpoints Generator](https://www.responsivebreakpoints.com/). I usually prefer generating 8–10 different images.

Of course you can use the generated HTML5 code in any frontend app or website. In addition, if you are into gulp, you could automate this process with the [gulp-responsive](https://github.com/mahnunchik/gulp-responsive) plugin.

#### 2. Make sure they are lazy loaded.

Lazy loading basically means that we defer the loading of images that are not required immediately. Typically, any image that is not visible to the users on their current viewport, can be loaded at a later point in time, when the image enters or is about to enter the viewport.

No matter which framework you are using, you can find a plugin that can lazy-load the images for you (e.g. [v-lazy-image](https://github.com/alexjoverm/v-lazy-image) in VueJS), however you could build your own implementation too. Just make sure that you are utilising the modern way to detect when an element enters or exits the browser’s viewport, the [IntersesectionObserver API](https://github.com/alexjoverm/v-lazy-image).

#### Bonus: Use a CDN for image delivery

If you have already optimised the size and the number of images that your website loads, and especially if it’s going to be available globally, you could also use a **content delivery network** (CDN) to serve them.

In a few words, a CDN caches your images on its globally distributed network of servers. So if a user from Australia requests an image from your website, instead of retrieving that image from your server in Europe, the CDN is going to deliver it from another one, closer to that user in Australia. This cuts down the round trip time needed to load the image.

### CSS, JS and HTML

All modern frameworks optimise your code during the production build time (code-splitting, tree-shaking, minification, etc.). What you can do on top of that?

#### 1. Optimise the main HTML document

HTML is the backbone of nearly every web app. When it comes to referencing resources within your HTML document there are a few best practices you should follow. It is recommended to:

* Place CSS references at the top of your HTML document’s header in order to ensure progressive rendering.
* Place JavaScript attributes at the bottom of your HTML body and [prefer async script loading](https://www.w3schools.com/tags/att_script_async.asp). This will prevent any `<scri`pt> tags from blocking the HTML rendering process.

#### 2. Make sure you only load what you need

![Image](https://cdn-media-1.freecodecamp.org/images/YjYDfAVFIYx91chGjMBSGUhruQJs4vWHxMKB)
_Lazy loading components and modules_

Angular, React, and VueJS all provide you with lazy-loading features. You only have to split your code properly, according to your own needs and load only the modules that you need, as soon as you really need them. For instance, if you have an e-commerce app, you have to make sure that the Basket module or the Payments module are not loaded when the user is in the home page.

### Compression & Caching

In general, for all the assets that are essential to your frontend (images & code) you should apply compression and cache them properly.

File compression will make your app’s assets a bit lighter and decrease the round trip time needed to serve them. One of the most commonly used file compression methods is **Gzip**, an excellent method for shrinking code chunks, documents, images and audio files.

[**Brotli**](https://github.com/google/brotli) is another file compression algorithm, and it’s growing in popularity. This open source algorithm is regularly updated by software engineers from Google and other organisations. It has proven itself to compress files at a **much better ratio** than other existing methods.

You can enable your preferred compression method on nginx, apache or whichever server you are using, by modifying their configuration files ([enabling brotli on nginx](https://www.howtoforge.com/tutorial/how-to-install-nginx-with-brotli-compression-on-ubuntu-1804/) or [enabling brotli on apache](https://ayesh.me/apache-brotli)).

When it comes to caching, the most commonly used caching technique (also recommended by Lighthouse) is called **Leverage Browser Caching**. Again, you can enable it by modifying your server’s configuration files ([enabling Leverage Browser Caching](https://www.keycdn.com/blog/leverage-browser-caching)).

### Summary

When it comes to websites and frontend applications, performance is a huge topic and we should take it seriously.

I hope this article helped you understand and enabled you to tackle some of the most important things that we need to take care of when we want to improve an application’s performance.

For a detailed checklist, make sure that you check out the [Front-End-Performance-Checklist](http://ront-End-Performance-Checklist).

Cheers! ?

