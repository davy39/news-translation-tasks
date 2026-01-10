---
title: How to decide on the best technology for your website
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-25T11:01:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-decide-on-the-best-technology-for-your-website-815dbb92294b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jy6j0_07UVXY8cX4qg2XVQ@2x.png
tags:
- name: JavaScript
  slug: javascript
- name: Microservices
  slug: microservices
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ondřej Polesný

  You know how your website is going to look and have a good idea about the content
  structure. But no one wants to maintain a set of static pages, right? Let’s take
  a look at how to make your website dynamic and easily adjustable, so ...'
---

By Ondřej Polesný

You know how your website is going to look and have a good idea about the content structure. But no one wants to maintain a set of static pages, right? Let’s take a look at how to make your website dynamic and easily adjustable, so that with every change, you do not need to touch the code and the website’s implementation.

But where do we start?

Do we need to install any tools? Is it a good idea to use JavaScript or stick with server-side rendering using MVC or an all-in-one CMS? I will explain how to bring life into your websites and prepare them for the future.

So you want to build a modern website. A website that is fast, secure, looks good and provides the best user experience. The word modern is key here, as it also relates to our hectic time. Everyone is busy, our bosses want us to handle 120% of our assigned work, and there is hardly a half-hour to enjoy lunch every day. Therefore, creating the whole website functionality from scratch does not fit our scenario. The objective is to get it up and running as fast as possible and share it with the whole world, preferably today.

#### An all-in-one server-side solution

Using an all-in-one solution such as a content management system (CMS) will ensure your website is up and running quickly. At least its first version. Installing it and accessing the administration interface for the first time could take you just a few minutes if you already have the development environment ready (otherwise add a few hours for the installation).

Once you log in, you can configure the website, define the URL policy and then start creating templates and layouts based on the design you picked. Getting the templates and content into the CMS can be time consuming. Namely you need to:

* learn the concept of templates of each particular CMS (from documentation or e-learning)
* apply the concept on your design
* learn best practices about storing content in each CMS
* fine-tune the website to fit your expectations

All this can be done very quickly if you are familiar with the CMS. But your first few websites will probably not be candidates for the Site of the Year. ?

When I used CMS systems in the past, sooner or later I always ended up creating custom controls (that is, custom code), as the HTML output of standard controls was not sufficient or directly went against new industry standards, like [Accelerated Mobile Pages](http://bit.ly/2QEMfX1). I consider this the biggest caveat of CMS systems, they limit you in various ways as they position themselves as a master engine of your website. I always found myself solving small tasks 80% of the time.

Another problem that I encountered almost every time was during deployment. First deployment is easy, you just put everything on a remote FTP and restore the database on your hosting provider’s server. It’s the subsequent deployments that complicate things. Although these systems usually feature a way to bring your development (or just local) changes to the live site, it tends to be a part of higher pricing tiers and it takes some time to learn and configure it.

#### Headless approach

I explained the advantages of microservice architecture in [another article](http://bit.ly/2Duglu1). Nowadays, everyone calls this approach headless, because the key part of microservice architecture is headless CMS (for example [Kentico Cloud](http://bit.ly/2QzUALM)). It acts as a place where you store all the content and ensures delivery. The main benefit is that it is just another service. You are the new head of your website. You say how services are going to work with each other and which of them you will leverage. Headless CMS is just another service in the whole stack. But how do you do that?

Let me show you that on my personal website. When a visitor comes, they expect to see something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/lNhIQF0NgiekbYntIVZj8gAdJ-ca1Kq1ePeN)

The homepage of my website is just a simple HTML code with content. Now, there are two ways this HTML code can be created. Either we stick with the standard approach of building it all on the server:

![Image](https://cdn-media-1.freecodecamp.org/images/Y3QJf9uDimVupmPa1FDr2nKf9mnJZ-Mefoq0)

Or we cut our webserver some slack and compose the HTML code on the client:

![Image](https://cdn-media-1.freecodecamp.org/images/HgaJ5JgDKX262v43hpGFUN5wLQ0luIZo5p1k)

You see, the visitor’s browser accepts only data, not the whole HTML structure with content in it. But how does the browser know what to display? How to process the data and output them in our design?

### Modern JavaScript

We will tell the browser what to do through JavaScript. In the past, JavaScript was frowned upon. It has always been a rule of thumb that whenever you created JavaScript functionality, you had to do the alternative noscript version. But times have changed and browsers have developed. You still need to comply with some rules in order to make your website accessible, but more on that later.

Using JavaScript for building a website has never been easier. There are many frameworks that help you achieve your goal even with minimal knowledge of plain JavaScript. And the best thing is that for some of them you do not need to install anything. Just your browser and favorite text editor are enough. But let’s start with the basics and select the best framework for our new websites.

Overall there are 3 major JS frameworks that have a lot of traction and a great community around them. That ensures continuous development and support. A lot of successful websites are built on top of them, some of which you may use on a daily basis.

#### 1. AngularJS

Angular has the greatest history of these three. It was founded almost 10 years ago in 2009! It is developed and maintained by Google. Compared to other frameworks, it has more complex syntax based on TypeScript and will require you to set up a build process. However, it supports modularity and an MVVM model which allows applications built on top of Angular to be very robust.

I remember using it for the first time in 2013 for a semi-government project where it enabled us to create fast front-end for managing all kinds of entities. It was so easy to create rich listings with paging, filtering and sorting functionalities.

#### 2. ReactJS

React was originally founded and open-sourced by Facebook in 2013. It is component-based which makes it easy to learn. Its components are implemented using JSX syntax, which sits between JavaScript and HTML. It is also easy to figure out initial architecture, as each component is like a module contributing to the output HTML. If you like Legos, you will like React!

It is possible to include it in website as a JS library or set up a build process and use TypeScript. React also has the biggest community and has a sibling called React Native which lets you build native mobile applications.

#### 3. VueJS

Vue was released in 2014 and is quickly growing — currently, it gets the biggest increase of traction in the community. It is very similar to React, but slightly easier for beginners. It shines with its detailed documentation and very easy integration. Components are based on simple HTML which makes it very easy for JavaScript beginners. It is also the lightest of these three.

I personally used it on more advanced shopping cart scenarios in Prestashop and was amazed how quickly I was able to get it all working together without any previous Vue knowledge.

If you wish to look at the comparison in depth, refer to great article by [TechMagic](http://bit.ly/2xEJpcE) or [comparison by Jens Nauhaus](http://bit.ly/2MYz1S5) on Medium.

#### Selecting the right framework

When it comes to selecting the right framework, developers usually go for the one they have a previous experience with (if it was a good experience). But if you are new to front-end development, you need to look at the goals you set up for your website. The right choice highly depends on the project you are building. So let me summarize my expectations:

* Fast learning curve - I need to build the website as fast as possible
* Lightweight implementation - the site will be quite small, so I want to minimize loading time
* Easy integration - I do not want to set up build processes, but start working on the website immediately
* Good documentation - whenever I am new to something, I find myself browsing through the documentation all the time for specific use-cases
* Easy routing - there are multiple pages in my website so I need a router to handle various URLs
* Simple content delivery - I will use a Content-as-a-Service system so I need an easy way how to get content in JavaScript

So you can see that in my case Vue.js fits the best. It is easy to use and integrate for beginners and has awesome documentation with easy tutorials. Write down your expectations and see if Vue.js fits them too.

The last point about content delivery is very important. All those JavaScript frameworks enable you to get content via REST API, but implementing raw API calls will be very time consuming and is not at all fun. Some headless CMS systems like [Kentico Cloud](http://bit.ly/2QzUALM) provide an [SDK for JavaScript](http://bit.ly/2xbiwNf) which is a wrapper around REST communication with many additional features. That will make content gathering much easier.

The final architecture of the new website can look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/5Vpup0NRAEU90P2YVdBUe0VL7i03o-6MGD6c)

The first request for the website is resolved by returning a main HTML template with JavaScript files. When the browser starts processing the JavaScript logic, Vue.js will be initialized and it will bring our components to life. Each of those components then acts independently - displays HTML, fetches data from headless CMS, or posts data of form submissions to a forms webservice.

This architecture enables us to build our websites very quickly while actually enjoying it. It is like building a car with Legos. The website will be lightweight, fast and overall, much more cost-effective. But let’s leave the economics for another article. What is your experience? Have you tried microservices already?

#### Other articles in the series:

1. [How to start creating an impressive website for the first time](http://bit.ly/2Duglu1)
2. How to decide on the best technology for your website (this article)?
3. [How to power up your website with Vue.js and minimal effort](http://bit.ly/2zLRE8a)
4. [How to Mix Headless CMS with a Vue.js Website and Pay Zero](http://bit.ly/2CyDnhX)
5. [How to Make Form Submissions Secure on an API Website](http://bit.ly/2P0gidP)
6. [Building a super-fast and secure website with a CMS is no big deal. Or is it?](http://bit.ly/2QVSm9a)
7. [How to generate a static website with Vue.js in no time](http://bit.ly/2PN46Jy)
8. [How to quickly set up a build process for a static site](http://bit.ly/2Dv2UGS)

