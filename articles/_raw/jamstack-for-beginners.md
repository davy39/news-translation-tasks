---
title: What is the Jamstack? Tutorial for Beginners
subtitle: ''
author: Damilola Oladele
co_authors: []
series: null
date: '2022-11-10T18:30:49.000Z'
originalURL: https://freecodecamp.org/news/jamstack-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Damilola-Oladele-2.png
tags:
- name: api
  slug: api
- name: JAMstack
  slug: jamstack
- name: JavaScript
  slug: javascript
- name: markup
  slug: markup
- name: Web Applications
  slug: web-applications
seo_title: null
seo_desc: 'You may have heard the term Jamstack and have been wondering what it means.
  Well, the Jamstack is nothing more than a modern way of building web applications.

  Jamstack takes advantage of existing technologies – which we''ll discuss in a minute.
  The re...'
---

You may have heard the term Jamstack and have been wondering what it means. Well, the Jamstack is nothing more than a modern way of building web applications.

Jamstack takes advantage of existing technologies – which we'll discuss in a minute. The result is better performance, improved security, and easier scalability for web applications.

In this article, you'll learn what Jamstack means and the benefits of using this approach in your projects.

## What is the Jamstack?

Jamstack is a web development architecture. Matt Biilmann, the CEO of Netlify, popularized it with his presentation at Smashing Conference 2016.

Jamstack is an acronym for Javascript, APIs, and Markup, and is a technology stack you use to build your apps.

This is like the MERN stack (MongoDB, ExpressJS, ReactJS and NodeJS) and the MEAN stack (MongoDB, ExpressJS, Angular and NodeJS) – just with different tools.

Now let's discuss the various components of a Jamstack web application:

### Javascript

Javascript is the core programming language of the web. It has been around for decades and you can use it both on the client side and the backend with NodeJS.

Javascript is the programming language you use for handling the client side of your Jamstack applications.

### APIs

API is an acronym for **Application Programming Interface**. It's an interface which helps two or more computer programs communicate with each other.

In Jamstack apps, you use APIs to communicate with your backend.

### Markup

Markup refers to standard text-encoding systems consisting of a set of symbols inserted into a text document. Examples of markup languages are **HTML**, **XML**, and templating languages such as **JSX**.

In the Jamstack, markup refers to the content of a Jamstack application. Note that we use markup here in its broader sense. It doesn't refer to text content only but also to the assets of the web application, such as images.

## Important Features of Jamstack Apps

To consider an application a Jamstack app, it should meet the following conditions:

### Distributed Architecture

This refers to the decoupling of the client side from the backend. The client side handles the presentation of the user interface, and the backend handles business logic and data.

Communication between the frontend and backend happens via a dedicated API. This means that a change or upgrade in one will not affect the other. This results in easier maintenance of the entire web application.

### Static Sites

It is important for Jamstack applications to serve static web pages and not dynamic ones.

Traditional web applications are dynamic sites. This means that when you request a page, the backend will have to reach a database to retrieve the data. The data is then used to generate HTML files, and then sent back to the client.

The disadvantage of dynamic sites is how long it takes to complete these steps.

For static sites, the pages are already pre-rendered at build time. So every time you request a page, you get the pre-rendered page.

This eliminates the time that dynamic sites spend in obtaining data, generating HTML files, and sending it back to the client. You can serve your static sites from a [content delivery network (CDN).](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) This will lead to improved speed and reduced costs.

Examples of static site generators that you can use for your Jamstack web applications include:

* NextJS
    
* Gatsby
    
* Hugo
    
* Jekyll
    
* Nuxt
    

## Why Should You Use the Jamstack for your Web Applications?

Let's now discuss some of the reasons the Jamstack web architecture has become so popular in recent times and why you should consider adopting it:

### Jamstack Apps Are Scalable

You can serve most Jamstack applications from a CDN. This allows for the speedy transfer of assets needed for loading web pages.

As a result of the distributed nature of CDNs, your web application will also be able to handle more traffic at a reduced cost.

### Jamstack Apps Are Easy to Maintain

Jamstack applications are easier to maintain since their client side is decoupled from their backends.

This means that you can maintain one part without requiring major modifications to the other.

### Jamstack Apps Load Faster

As stated earlier, serving your site from a CDN increases the speed with which it loads.

Also, in Jamstack applications, web pages are prebuilt, saving time that would normally be spent retrieving and generating HTML files every time you make a request.

### Jamstack Apps Are Cheaper

Since Jamstack applications are easier to maintain and deploy, they are cheaper compared to their traditional counterparts.

### Jamstack Apps Are More Secure

Since you do not have to constantly maintain a server in Jamstack applications and the pages are constructed on read-only files (that is, the pages are static), you can worry less about the security of your applications.

## Conclusion

Despite the fact that more and more projects are being built using the Jamstack architecture, we're still in the relatively early stages of its adoption.

I believe that more large and small businesses will adopt it in the near future in place of costly monolithic architectures.
