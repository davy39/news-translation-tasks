---
title: Building a super-fast and secure website with a CMS is no big deal. Or is it?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-16T17:47:25.000Z'
originalURL: https://freecodecamp.org/news/building-a-super-fast-and-secure-website-with-a-cms-is-no-big-deal-or-is-it-5ac915c691f2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rM8pXwM7Je0zXjAv_dfysQ@2x.png
tags:
- name: api
  slug: api
- name: Security
  slug: security
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ondřej Polesný

  Can I break your site? Do you have any leftover scripts there that I can take advantage
  of? Is there a way to steal your credentials and change content on your site? Can
  I access private information? No? Are you sure? Or, am I never...'
---

By Ondřej Polesný

Can I break your site? Do you have any leftover scripts there that I can take advantage of? Is there a way to steal your credentials and change content on your site? Can I access private information? No? Are you sure? Or, am I never going to find out because your page takes ages to load?

At some point when creating a website you need to think about performance and security. It does not matter if you’re working on your personal website, or your client’s website. It is the same as backing up your local files. There are people who do regular backups, and people who have not yet lost any, so are less inclined to do it.

### Traditional CMS

If you are using a traditional content management system (CMS), the situation is more complicated for you. These systems contain lots of features. They need to cover all potential use-cases any website might have. That means code. A lot of code. Thousands of files. And, that’s not all — the administration interfaces need to provide a nice UI for you to configure all these features. Potentially, another few thousand files.

#### Security

It’s not your code, right? So it should already be secure. Well, many CMS vendors try their best to ensure their implementations are secure. They still have to cover a lot of files. And, every single file may contain an error, some code that was left behind, or maybe a querystring parameter that exposes a database. That in itself can create a potential vulnerability.

Using open-source CMS can be even more dangerous, as the implementation is publicly known. Yes, you can argue that open-source is advantageous. Anyone can contribute and fix found issues. But, this only covers issues that are already known. Attackers would probably keep their exploits to themselves. Even if an issue was found and fixed, you still need to put a lot of effort into making sure your website is kept up-to-date. You have to perform upgrades every time a security hotfix is released.

If you are interested in real-world statistics, take a look at [hacked website report by Sucuri](http://bit.ly/2CVdyYP).

So, what would attackers want to do with your website? Essentially, they want to get hold of your data, so they can misuse your website by:

* Getting access to your database through one of the scripts. This is usually the case of custom leftover scripts, testing pages, and others.
* Compromising and misusing your secret data. Configuration files are a typical storage option for various secret keys and credentials to other services or databases.
* Modifying your website content.
* Making your website inaccessible, i.e. shut it down.

#### Performance

When you implement your website on a traditional CMS, you usually need to customize it, so there are files of the CMS and your custom files. All of them need to be compiled, and then together with precompiled libraries, brought up to the server memory before the server can actually start processing requests to your website. Or worse, if you are using a solution based on interpreted language like PHP, interpret all code for each request.

Anyway, your website seems to run fine, so why should this be a concern? Well, because:

* you pay for your server computing power
* you compile and copy code of functionalities you never intend to use
* your website visitors wait for the response

Time to first byte of these websites can be way above 1 second. Sure, it can be optimized, but then you spend time and money on figuring out how to mitigate performance issues, and usually end up boosting CPU and memory, or worse, adding an additional server.

Check your site using [Google PageSpeed](http://bit.ly/2ESQuww) or get more detailed analysis using [SpeedCurve](http://bit.ly/2EQyse6) to see how your website is doing.

### API-based Websites

Websites built on top of an API enable great flexibility. Ask yourself, do you need content management? If so, you can use a headless CMS. Do you need to [store form submissions](http://bit.ly/2P0gidP)? Perfect, use a form service. Are you building a website for mountain hotel and want to display a weather forecast? There is a weather service with its API for you.

The number of files used for such websites corresponds to its functionality. But, what about the administration interface for content editing? Don’t worry. The headless CMS is handling that part for you, with no additional code you need to host or maintain.

#### Security

When using API services, you do not need an administration service on top of your website. You configure all components when building the website. Like the weather component that should display a weather forecast for three days. Or that there should be four blog posts on the main page. The rest of the dynamic content can be managed in the headless CMS.

The main benefit of this approach is that you do not need a database. That’s right, no single point of data storage that an attacker can gain access to.

If your website is based on JavaScript, its implementation is basically open. It may be compiled, but whatever is provided to the browser is readable. This is yet another advantage. Yes, anyone can query the services endpoints directly. The published content you get from them is displayed on your website anyway, only transformed into a nicer visual. It’s like with news articles on websites, and RSS readers. For sensitive content you can always authenticate each user through another service, obtain their unique access token, and use it to ask for sensitive content over secure protocol.

If you keep in mind that the JS implementation is open to everyone, and treat sensitive data the right way, you will have much less work to do in order to make your website secure. Not having a database and consuming all API services through secure channels closes almost all doors for a potential attacker.

#### Performance

In this scenario, the webserver provides only assets. The business logic of your application is stored in a JS file. Content from various endpoints is gathered via asynchronous requests by visitor browsers.

Async requests to get content from third-party services? That must be slow, right? Well sure, they take some time. But, their delivery endpoints are usually built for speed, hosted in Cloud, and very flexible. You can also pick a headless CMS that uses a CDN for delivery, one of them is [Kentico Cloud](http://bit.ly/2QzUALM). That way the request will always be handled by the data center that is geographically closest to each of your visitors.

Even if you use multiple services to build a single page, these requests are all asynchronous. Visitors wait only for the slowest one. When a page is composed on a server using traditional CMS, all communication with the database and other services is usually synchronous. Therefore, the server waits for each transaction to finish before starting another one. And, after all this is done, everything is put together and sent back as one big response.

![Image](https://cdn-media-1.freecodecamp.org/images/ipQDewGGY6nlDDtBAL9J6ria7NOBKVnj2AdB)
_Traditional CMS — 3s; API based website — 1.3s_

Take a look how long it took the webserver to process incoming requests (light yellow background). All this time, the visitor is actively waiting, and cannot start downloading images and other assets. They will be known to the visitor’s browser only after the response is received.

An API based website is much faster, as the initial response with static HTML file is instant. The browser downloads business logic of the website as one of the assets, and generates all subsequent asynchronous requests for content. The visitor sees a fully rendered page much quicker, and they also see something is happening. When they are waiting for a server-rendered page, all they see is a preloader in the address bar of their browser. The overall performance improvement of API based website is in this case over 50%. It can be much higher depending on the website implementation.

### Static Websites

So why would we bother solving performance, if we already have an API-based website?

![Image](https://cdn-media-1.freecodecamp.org/images/1BeV156ReM5M6NFKxQ1evAwNWgOESVOl4ZOz)

Since the webserver only provides static files and assets, its performance is good. The fact that dynamic content is gathered later when the website is being rendered in visitor’s browsers can lead to some artifacts. Visitors may see an empty component that gets filled when it receives data from asynchronous request, and so on. People with a slow internet connection, or using older computers may find this disturbing.

What can we do about this? No, we won’t add any preloaders. How does it make you feel when you see an infinite preloader that just spins and spins and spins? We can make our websites static, yet keep them dynamic.

![Image](https://cdn-media-1.freecodecamp.org/images/ZrlAed2i11o1dQbZsUwydQPoqxK7UttIlHSo)

The concept of static sites is about the output of your website. It starts with the content. Editors usually don’t update content that often. The website needs to be composed upon every single request (like traditional CMSs do). The idea is similar to caching — store generated data or pages in memory. But static sites go a bit further. The whole website, all pages with all content, is generated every single time an editor publishes content. So if you have 153 blog posts in your blog, the website will now have 153 static pages (plus some others like homepage, contact, and more).

How are you going to manage 153 pages? Well, you don’t. You still manage just the implementation of a single dynamic page. The static site is generated by combining your implementation with content from a headless CMS. So when there is new content, the site is just automatically generated again.

![Image](https://cdn-media-1.freecodecamp.org/images/cFrbwPbcZ6ofl23HkQ5-NKClZPU-wUqobOfs)

You see the benefit of speed is not that significant compared to dynamic API-based websites. However:

* your visitors get the page and all content in the first response. They won’t be looking at a page that is being built. Their browsers don’t need to create additional async requests for content
* all subsequent requests behave the same way
* visitors are navigating between set of static pages which is very fast
* some tools for static sites generation enable additional cool features for visitors such as preloading of linked pages (which makes navigating to them instant) or displaying images in low quality before they are fully downloaded

All that will leave your visitors with the impression of a blazing fast website.

Of course, every website is different. You may need some personalization features, or want to display sensitive content. In those cases you may combine both approaches . Have a static website, and still use API-based services to deliver content that varies among visitors.

### Conclusion

The performance and security aspects of every site are very important. Traditional CMSs are usually more resource demanding than API based websites, but they provide more functionality out-of-the-box.

On the other hand, API based websites are much faster and more secure. They enable you to save money on hosting, and provide a better experience for your visitors.

Static sites are becoming a big hit nowadays, as their performance is the best by far. They also let you build part-static part-dynamic sites based on JavaScript that are nicely indexable by search engines.

Is your website already static? Have you used any static sites generators? Let me know about your experience in the comments section below.

In my next article I will show you how to build a website on Vue.js using static site generator.

#### Other articles in the series:

1. [How to start creating an impressive website for the first time](http://bit.ly/2Duglu1)
2. [How to decide on the best technology for your website?](http://bit.ly/2N0kXY4)
3. [How to power up your website with Vue.js and minimal effort](http://bit.ly/2zLRE8a)
4. [How to Mix Headless CMS with a Vue.js Website and Pay Zero](http://bit.ly/2CyDnhX)
5. [How to Make Form Submissions Secure on an API Website](http://bit.ly/2P0gidP)
6. **Building a super-fast and secure website with a CMS is no big deal. Or is it?**
7. [How to generate a static website with Vue.js in no time](http://bit.ly/2PN46Jy)
8. [How to quickly set up a build process for a static site](http://bit.ly/2Dv2UGS)

