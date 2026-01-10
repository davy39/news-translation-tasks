---
title: What is Pre-Caching? How to Increase Website Speed and Performance
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-19T18:05:56.000Z'
originalURL: https://freecodecamp.org/news/a-detailed-guide-to-pre-caching
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pre-caching.png
tags:
- name: caching
  slug: caching
- name: node js
  slug: node-js
- name: software architecture
  slug: software-architecture
- name: software development
  slug: software-development
- name: web performance
  slug: web-performance
seo_title: null
seo_desc: 'By Saurabh Dashora

  Speed and performance are two of the key ingredients that make a website stand out
  from its peers.

  Imagine visiting a bestseller list on the Amazon website and finding that the product
  pages take forever to show up.

  What about a bl...'
---

By Saurabh Dashora

**Speed** and **performance** are two of the key ingredients that make a website stand out from its peers.

Imagine visiting a bestseller list on the Amazon website and finding that the product pages take forever to show up.

What about a blog publishing some great stories that readers aren’t able to read because the incoming traffic exceeds the server’s capacity?

And if that’s not enough, just measure your frustration when there is a much-anticipated new movie on Netflix and all you get to see is the loading screen.

If you are the one running such a website, this is a **good problem** to have. Clearly, people are enthusiastic about the things you are offering and there is a disproportionate amount of traffic for certain pages.

However, if not handled properly, the situation can quickly spiral into chaos and end up alienating your users. Ultimately, it will result in a loss of business whether in terms of viewership time, sales, or even general user goodwill.

**So how can you avoid this situation?**

One of the most prominent techniques to boost website speed and performance is **pre-caching**.

In this post, you will get to understand the concept of pre-caching in great detail.

## What is Pre-caching?

Pre-caching is a technique used to **proactively** store or cache data in anticipation of future requests. The idea is to cache commonly accessed data or resources in advance so that when the time comes, you can deliver it to the end-user faster.

Check out the below illustration that depicts how pre-caching can work in an overall system context.

![pre-caching in a system](https://www.freecodecamp.org/news/content/images/2023/01/image-133.png)
_How pre-caching works_

You can perform pre-caching on the **client-side** such as in the web browser. Alternatively, you can also do it on the **server-side** using Content Delivery Networks (CDNs) or other caching solutions.

Whatever may be the approach, the goal of pre-caching is to **improve the performance and user experience by reducing content load times**.

## How Pre-caching Works

The process of pre-caching requires you to store a copy of the data in a location that’s closer to the user or store the data in advance so that it is readily available when needed.

Below are the high-level steps to implement pre-caching.

* First, **identify the data or resources** that are accessed most frequently. These resources are good candidates for pre-caching. For example, most popular blog posts, bestseller product list, and so on. You could also include images, JS files, and stylesheets to the pre-caching list
* After the identification, you need to **decide on the caching system** to store the pre-cached data. This could be a local cache on the user’s device or even a distributed cache spanning multiple servers. The choice will depend on the type of resource.
* Next, you need to **pre-populate the cache** with the identified resources. This step can be performed automatically by the system during initialization phase. Alternatively, you can do it on an on-demand basis as the data is accessed by the users. Remember, pre-caching is all about being proactive.
* Once the setup is ready, you can let your system do the job. Whenever the system needs to access the pre-cached data, it can retrieve directly from the cache instead of fetching from the slower external source.

## How to Decide What to Pre-cache

The success of pre-caching depends on the **quality of data** that is pre-cached. It is important for you to choose the right data to cache.

While it can sound daunting in practice, you can follow the below rules to make the right choice:

* **Prioritize critical resources** such as the HTML, CSS, and JavaScript files that are needed for the initial page load. Usually, these are the most important resources that are required to provide a fast and smooth user experience.
* You should also consider **caching third-party resources** like fonts, libraries or scripts from other domains. These resources can be pre-cached locally to reduce frequent network requests.
* Your initial assumption about the best resources for pre-caching can change. Therefore, it is vital to **perform a regular analysis** of your web application’s usage pattern and derive insights about the user activity. This will help your pre-caching catalog stay relevant as your application evolves.
* Explore the **use of machine learning** for pre-caching. You can **build prediction models** in order to predict which resources will be requested in the future based on past usage patterns. You can train this model on historical data and use it to identify the best candidate resources for pre-caching. Of course, this is a costly approach and its use depends on the importance of pre-caching in your application context.

## The Advantages of Pre-caching

Pre-caching may sound like a lot of trouble. Why bother worrying about it?

In my view, the advantages of pre-caching can outweigh the difficulties. Here are a few important benefits of pre-caching:

* **Performance Improvement** – When you pre-cache data, you are essentially reducing the load time for the content. This leads to a faster user experience. Websites and apps that expect a high volume of traffic or deal with huge amounts of data are significantly benefited by this.
* **Improved user experience** – Who doesn’t like a good user experience? Faster load times improve the overall user experience and help reduce the bounce-rate (percentage of users leaving a website after visiting one page). Pre-caching also improves content availability even in the case of poor network connection.
* **Cost Reduction** – Pre-caching can help you reduce costs. For example, if you pre-cache data on a CDN, you are ultimately reducing the load on the origin server. This saves bandwidth and reduces the server cost.
* **Offline Access** – With pre-caching, you can also enable offline access to content using the concept of service workers. This is extremely important for mobile apps and websites that need to work in areas with poor internet connectivity.
* **Security** – Though it is an indirect benefit, you also improve the overall security of your assets using pre-caching. Basically, pre-caching blunts the impact of DoS (Denial of Service) attacks since the application won’t have to serve the pre-cached resources from the origin server.

## How to Implement Pre-caching in Node.js

Let’s look at a very basic implementation of **pre-caching in Node.js**:

```js
const express = require('express');
const nodecache = require('node-cache');
require('isomorphic-fetch');

//Setting up Express
const app = express();

//Creating the node-cache instance
const cache = new nodecache({stdTTL: 10})

//We are using the fake API available at <https://jsonplaceholder.typicode.com/>
const baseURL = '<https://jsonplaceholder.typicode.com/posts/>';

//Pre-caching Popular Posts
[1, 2, 3].map(async (id) => {
    const fakeAPIURL = baseURL + id
    const data = await fetch(fakeAPIURL).then((response) => response.json());
    cache.set(id, data);
    console.log(`Post Id ${id} cached`);
})

//API Endpoint to demonstrate caching
app.get('/posts/:id', async (req, res) => {
    const id = req.params.id;
    if (cache.has(id)) {
        console.log('Fetching data from the Node Cache');
        res.send(cache.get(id));
    }
    else {
        const fakeAPIURL = baseURL + id
        const data = await fetch(fakeAPIURL).then((response) => response.json());

        cache.set(req.params.id, data);
        console.log('Fetching Data from the API');
        res.send(data);
    }
})

//Starting the server
app.listen(3000, () => {
    console.log('The server is listening on port 3000')
})

```

The example uses the `node-cache` library to create an in-memory cache. It is borrowed from a blog post that shows [how to implement an in-memory cache in Node.js](https://progressivecoder.com/in-memory-caching-nodejs/).

To simulate how pre-caching works, it assumes that posts 1, 2, and 3 are extremely popular posts and suitable candidates for pre-caching. Therefore, the data for these posts are pre-fetched during the application startup process and stored in the `cache` object.

When a request is made for these specific posts, the application fetches the data directly from the cache instead of calling the API.

Of course, this is a very basic setup for pre-caching. But you should get the idea of the concept in action.

## Types of Pre-caching

While the previous section’s example demonstrated a particular approach to implement pre-caching, there are other methods as well.

Since the basic idea of pre-caching is quite simple, you can implement it in several different ways. Broadly, there are two main approaches: client-side pre-caching and server-side pre-caching.

### Client-side Pre-caching

The most common way of client-side pre-caching is to proactively cache resources on the browser. With **browser-based caching**, you are trying to anticipate the resources that will be requested and store them in advance using the browser’s cache-storage API.

**Browser-based caching** often relies on the caching headers to determine if a particular resource is cacheable. When a user requests a page, the browser checks its cache to see if a copy of the requested data is already available. If it is, the browser loads the data from the cache. This reduces the time it takes to load the page.

Another way of implementing browser-based caching is using the **Service Worker API.** Basically, assets are pre-cached ahead of time, usually during the process of installing a service worker.

With service worker pre-caching, key static assets and materials such as HTML, CSS, JS and image files that are necessary for offline access get downloaded and stored in a `Cache` instance. You can use the JavaScript library named **[Workbox](https://developer.chrome.com/docs/workbox/)** that makes it easy to precache resources and provides a simple API for working with the service worker cache.

### Server-Side Pre-caching

The second approach is **server-side pre-caching**. You can also do it using multiple ways.

First method is to use **Content Delivery Networks or CDNs** that store a copy of the data on servers that are distributed around the world. When a user makes a request for some data, it is delivered from the server that is closest to the user. This reduces the time to handle the request and makes your website faster for the user.

![pre-caching with content delivery networks](https://www.freecodecamp.org/news/content/images/2023/01/image-134.png)
_Pre-caching with CDN_

Second approach is to use a **Caching Proxy Server**. It is a server that sits in front of the origin server and works as a caching layer by storing a copy of the data. Next time there is a request from the user, the proxy server delivers the data directly without having to make a request to the origin server.

![caching proxy server](https://www.freecodecamp.org/news/content/images/2023/01/image-135.png)
_Caching Proxy Server_

Here’s a sample configuration to use NGINX as a caching proxy server to cache all files with extension jpeg/jpg, png, css and js for 60 seconds.

```bash
# configure the proxy server to cache all assets for 1 hour
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=static_cache:20m inactive=60m;

# set the cache control header to a max-age of 1 hour
add_header Cache-Control "public, max-age=3600";

# cache all assets
location ~* \\.(jpg|jpeg|png|css|js)$ {
    proxy_cache static_cache;
    proxy_cache_valid 200 60m;
    proxy_pass http://origin_server;
}

```

## Pre-Caching Best Practices

Pre-caching is an extremely useful technique to improve your web application’s performance. However, you should follow some best practices to ensure that pre-caching gives the desired results.

Here are a few best practices you should keep in mind while pre-caching:

* **Cache only necessary resources.** Caching too many resources can lead to wasting storage space and nullifying the advantages of pre-caching. You should only cache the resources that have the greatest impact on performance improvement.
* **Don’t forget to version pre-cached resources.** Even pre-cached resources may get updated in the future. So you should make sure to use versioning to identify the latest version of a resource. When a resource gets updated, you should also increment the version number to keep track of subsequent updates.
* **Use appropriate cache-control headers**. Cache-control headers help us ensure that the resources are cached for the right amount of time. For example, an e-commerce platform might have a list of bestselling products that’s changing frequently due to products dropping off the charts or rising up. Such resources should have a shorter cache lifetime to keep the cache relevant.
* **Use a Content Delivery Network (CDN)**. CDNs help reduce the time it takes to load the resources. You should leverage a CDN to distribute resources to the edge servers located closer to the user. Edge servers in combination with pre-caching is a powerful technique to boost your web application’s performance.
* **Use a library or framework to enable pre-caching**. Even though you might be tempted to build your solutions for pre-caching from scratch, you should consider using a library such as Workbox to enable service workers for pre-caching resources. For server-side caching, consider using a combination of CDNs and caching proxy servers.

## Drawbacks of Pre-caching

While pre-caching is a very useful technique and mostly beneficial, you should make sure to avoid the below drawbacks:

* **Stale data**: With pre-caching, you are storing data in advance. This data may not always be up-to-date. If the data changes frequently, the pre-cached version will become stale and lead to issues. To avoid this situation, you must have a proper strategy for cache invalidation that can get rid of stale data.
* **Inefficient use of resources**: While pre-caching, you are basically assuming that the data you are caching will be accessed frequently. Such assumptions may **not** always be correct and you may end up with data that’s not needed frequently. If the size of such data grows beyond a certain limit, the caching solution can become inefficient and cause wastage of precious resources that can be used for other purposes.
* **Limited scope**: Pre-caching is limited in scope. It only applies to data that is known in advance and can be pre-populated in the cache. This is mostly static data. It’s tough to implement pre-caching for data that is generated dynamically without the use of complex algorithms.

## That’s it

To conclude, pre-caching is a powerful technique that can potentially improve the speed and performance of your website.

With pre-caching, you are essentially trying to anticipate which resources a user is likely to request next and downloading them in advance.

Even on its own, **pre-caching is a game-changing technique** that can have a significant impact on the user experience of your web application.

However, it's equally important to keep in mind that pre-caching is only one aspect of the website optimization process. You should try and use it in conjunction with other techniques such as minification, compression, and code optimization.

If you liked this post and found it useful, consider sharing it with friends and colleagues.

