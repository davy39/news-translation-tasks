---
title: 'An introduction to the JAMstack: the architecture of the modern web'
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2019-05-17T14:59:56.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-the-jamstack-the-architecture-of-the-modern-web-c4a0d128d9ca
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xYSNCnp6eh2ZDpwQtYL6qg.jpeg
tags:
- name: api
  slug: api
- name: JAMstack
  slug: jamstack
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: I’m sure you’ve come across the word JAMstack before but you might not have
  understood what it really meant. I’ve seen this word before also but didn’t care
  to check it out until Egwuenu Gift organized JAMstack Lagos. I then realized that
  I’ve been b...
---

I’m sure you’ve come across the word JAMstack before but you might not have understood what it really meant. I’ve seen this word before also but didn’t care to check it out until [Egwuenu Gift](https://www.freecodecamp.org/news/an-introduction-to-the-jamstack-the-architecture-of-the-modern-web-c4a0d128d9ca/undefined) organized [JAMstack Lagos](https://twitter.com/jamstacklagos). I then realized that I’ve been building JAMstack applications already.

JAMstack is a modern web development architecture. It is not a programming language or any form of tool. It is more of a web development practice aimed towards enforcing better performance, higher security, lower cost of scaling, and better developer experience.

In this article, I’ll introduce you to what JAMstack means, why you should care, best practices, and how to get started. ?

### Introduction

![Image](https://cdn-media-1.freecodecamp.org/images/oE3wYE3Ygr1SlH2dTXkM5lXW-DyHPlmMrQww align="left")

According to the official [JAMstack documentation](https://jamstack.org/),

> JAMstack is a Modern web development architecture based on client-side JavaScript, reusable APIs, and prebuilt Markup.

> When we talk about “The Stack,” we no longer talk about operating systems, specific web servers, backend programming languages, or databases.

> The JAMstack is not about specific technologies. It’s a new way of building websites and apps that delivers better performance, higher security, lower cost of scaling, and a better developer experience.

**JAMstack** is a major trend in web development coined by [Mathias Biilman](https://twitter.com/biilmann), the CEO and co-founder of Netlify.

### Okay, chill! What is JAMstack?

You might have come across specific terms like **MEAN stack** and **MERN stack.** These are just terms used to classify or group some certain technologies with the aim of achieving a particular goal.

JAMstack here stands for

**J**avaScript

**A**PI

**M**arkup

> Stacks generally are just a combination of several technologies used to create a web or mobile application. So JAMstack is the combination of JavaScript, APIs and Markup. Pretty interesting right?

JAMstack projects don’t rely on server-side code — they can be distributed instead of relying on a server. Served directly from a CDN, JAMstack apps unlock speed, performance and better the user experience.

![Image](https://cdn-media-1.freecodecamp.org/images/x0eO1iqvIRKPNsEtSkFvRuLu6CbSmo7OhcFH align="left")

### Useful Terms

I’ll be using these terms in this article frequently and I thought you should know their meanings (if you don’t already):

* **API** is the acronym for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other.
    
* **CDN** (content delivery network) is a system of distributed servers (network) that deliver pages and other Web content to a user, based on the geographic locations of the user, the origin of the webpage and the content delivery server.
    
* A **Server** is a computer designed to process requests and deliver data to another computer over the internet or a local network.
    
* A **Database** is a collection of information that is organized so that it can be easily accessed, managed, and updated
    

### Why JAMstack?

![Image](https://cdn-media-1.freecodecamp.org/images/uHGkEXe8lXJsmj6cZNQmIW3bpsEzn0mU9Eun align="left")

Traditional websites or CMS sites (e.g WordPress, Drupal, etc.) rely heavily on servers, plugins and databases. But the JAMstack can load some JavaScript that receives data from an API, serving files from a CDN and markup generated using a static site generator during deploy time.

Sounds cool right?!

#### JAMstack is fast

When it comes to minimizing the time of load, nothing beats pre-built files served over a CDN. JAMstack sites are super fast because the HTML is already generated during deploy time and just served via [CDN](https://flaviocopes.com/cdn/) without any interference or backend delays.

#### JAMstack is highly secured

Everything works via an API and hence there are no database or security breaches. With server-side processes abstracted into micro service APIs, surface areas for attacks are reduced and so your site becomes highly secured.

#### JAMstack is cheaper and easier to scale

JAMstack sites only contain just a few files with minimal sizes that can be served anywhere. Scaling is a matter of serving those files somewhere else or via CDNs.

### JAMstack Best Practices

* Use CDN to distribute your files rather than servers
    
* Installing and contributing to your project should be easy and less complex. Use tools like npm and Git to ensure standard and faster setup.
    
* Use build tools and make your project compatible for all browsers (e.g Babel, Browserify, Webpack, etc.)
    
* Ensure your project is up to web standards and highly accessible
    
* Ensure your build process is automated to reduce stress.
    
* Make your deployment process automatic, you can use platforms like [Netlify](https://netlify.com) to do this
    

### How do I Get Started?

You can use some already built technologies to build JAMstack applications in a few minutes. Here are a few:

* [**Gatsby**](https://www.gatsbyjs.org/)**:** Gatsby is a free and open source framework based on React that helps developers build blazing fast **websites and** **apps**
    
* [**NuxtJS**](https://nuxtjs.org/)**:** NuxtJS is the Vue.js Framework for Universal applications, static generated applications, single page applications, progressive web apps and desktop apps
    
* [**Hugo**](http://gohugo.io)**:** Hugo is the world’s fastest framework for building websites. It is one of the most popular open-source static site generators. With its amazing speed and flexibility, Hugo makes building websites fun again.
    
* [**Netlify CMS**](https://www.netlifycms.org/)**:** Netlify CMS is an open source content management for your Git workflow which can be used with any static site generator for a faster and more flexible web project
    
* [**Contentful**](https://www.contentful.com)**:** Contentful is a smarter and seamless content management system which provides editors and developers with a unified content thereby enhancing collaboration and ensuring digital products ship to the market faster.
    
* [**Svelte**](https://svelte.dev/)**:** Svelte is a radical new approach to building user interfaces. Whereas traditional frameworks like React and Vue do the bulk of their work in the *browser*, Svelte shifts that work into a *compile step* that happens when you build your app.
    

[***and many more. . .***](https://www.staticgen.com/)

### Useful Resources

* [**JAMstack WTF**](https://jamstack.wtf/)
    
* [**How to Build a JAMstack Website**](https://cosmicjs.com/blog/how-to-build-a-jamstack-website)
    
* [**What is JAMstack and why you should try it**](https://www.giftegwuenu.com/what-is-ja-mstack-and-why-you-should-try-it)
    
* [**A JAMstack-ready CMS**](https://www.contentful.com/r/knowledgebase/jamstack-cms/)
    
* [**JAMstack for Clients: On Benefits & Static Site CMS**](https://snipcart.com/blog/jamstack-clients-static-site-cms)
    
* [**Go static: 5 reasons to try JAMstack on your next project**](https://builtvisible.com/go-static-try-jamstack/)
    
* [**Static Websites + JAMstack = ❤**](https://julian.is/article/static-websites-and-jamstack/)
    

Find more resources [here](https://jamstack.org/resources/)

%[https://www.youtube.com/watch?v=uWTMEDEPw8c] 

### Conclusion

JAMstack was invented as a way to put a nomenclature to the new way of building websites and apps that delivers better performance, higher security, lower cost of scaling, and a better developer experience.

JAMstack is not about specific technologies, it is a modern web development architecture based on client-side JavaScript, reusable APIs, and prebuilt Markup.

Join the [JAMstack community](https://jamstack.org/community/) to learn more and get more updates.

![Image](https://cdn-media-1.freecodecamp.org/images/BoR0w2G9fjZDSJDFTlZoGE4gK810ODcs8vz3 align="left")

> PS: This article was first published on my blog [here](https://bolajiayodeji.com/an-introduction-to-the-jamstack-the-architecture-of-the-modern-web-c4a0d128d9ca)
