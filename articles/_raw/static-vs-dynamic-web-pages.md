---
title: Static vs Dynamic Web Pages – What's the Difference?
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-08-11T19:54:10.000Z'
originalURL: https://freecodecamp.org/news/static-vs-dynamic-web-pages
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/staticdynamic.png
tags:
- name: interview questions
  slug: interview-questions
- name: Web Development
  slug: web-development
- name: website development,
  slug: website-development
seo_title: null
seo_desc: 'Imagine that you''re interviewing for your dream job and the interviewer
  drops this question for you:

  “So can you distinguish between a static web page and a dynamic web page?”

  What would your reaction be?

  If you don’t know the answer to that question...'
---

Imagine that you're interviewing for your dream job and the interviewer drops this question for you:

*“So can you distinguish between a static web page and a dynamic web page?”*

What would your reaction be?

If you don’t know the answer to that question, or are struggling to think it up, then this article is for you.

If you're a beginner coder, you might have heard of the terms “static web pages” and “dynamic web pages” – but you might not know what they mean.

You might wonder what makes a web page static and what makes a web page dynamic.

In this article, I am going to tell you all you need to know – and why it's important. And, as usual, I will be doing so in plain English.

## What is a Web Page?

First, we need to understand what a web page and a web site are and how they differ. To do that, let’s consider an encyclopedia.

An encyclopedia (like Wikipedia, for example) consists of many pages. Each page has its own content: A header, paragraph, images, diagrams, bullet points, lists, and of course, the definitions of the terms you're looking up.

It is very common in an encyclopedia to find words on the page which refer (or link) to another page for additional information.

This is very similar to web pages and web sites.

A web page is a single document which can contain text, images, hypertext, or any other elements. We create web pages using a markup language such as HyperText Markup Language – more commonly known as HTML.

HyperText is any web document which contains hyperlinks. A hyperlink is any element in the web page which, when you click on it, links to another web page.

These interconnected web pages forms an organised network of web pages, which we then call a **website**.

Every web page accessible on the internet must have its own URL. Here’s a typical URL of a web page:

[`www.freecodecamp.org/news`](http://www.freeCodeCamp.com/news)

> N/B: In case you are wondering, the page that the above URL returns is a dynamic page. Don’t worry, we will find out what that means very shortly.

**Now, I have a simple test for you:**

Open your web browser. Navigate to the address bar and type in (or select) any random but valid URL you know. Hit enter and wait. A web page will be rendered on your browser window. Take a snapshot of the current state of the web page and close it.

Wait for some time, and then visit that URL again. Then answer the following questions:

* If you compare the current state of the page to its previous state, are there any differences in its content?
    
* Does the page’s URL ends with a document extension `/.html` for example) or did it end with an endpoint? `/profile` for example)
    
* Assuming you change your browser settings (like clearing cookies, for example), does hitting the same URL returns a different page?
    
* Are you prompted to submit a form before having the page rendered on your browser?
    

How you answer these questions (and a couple more I will ask below) will determine whether the page is a static one or a dynamic one.

## What is a Static Page?

A static page has the following characteristics:

* The page is already present even before a user requests it. A static page must be already physically present and hydrated (i.e with content) by the time a user makes a request for it. If it is not present, then it is not static.
    
* The page generally maintains the same content every time the user requests it. If hitting the same URL returns different content, then that page is not static at all. This is not to say static pages cannot be modified. But the only way to change a static page for the creator to manually edit the content (like an HTML document)
    

Here's an example of a static page:

`www.example.com/about.html`

## What is a Dynamic Page?

A dynamic page has the following characteristics:

* The page is not physically present on the server when the user makes a request for it
    
* Instead, when a user makes a request a script or program runs and ultimately cooks up a web page. It does this by interacting with a database to retrieve data which it packages and sends over as a page.
    
* On every request, every new page created may be different from the last.
    

This is because the page created is dependent on the user's information and the program. The creator does not have to manually edit the content, as with Static Web Pages.

So, for example, if a different user requests the same page, different content is returned.

Or maybe when a user changes a setting, a new page is returned.

Or maybe when the time changes, different content is returned.

To illustrate this in a more intuitive way, let’s take a look at two scenarios in a Restaurant:

*You are hungry, so you decide to go to a restaurant to eat. You order a plate of Jollof Rice (a Nigerian food). Through the transparent glass window into the kitchen, you can see that the food is already cooked. All the waiter has to do is to go over there, get the meal, and bring it to you.*

*Now let's say that you order a plate of suya (Nigerian meat). Typically, the meat is not already available and has to be prepared for you on the spot. With the information you supply to the waiter (your budget, how many onions you want, etc) the cook puts together your portion for you.*

The first scenario illustrates how a static page is rendered. The second scenario illustrates how a dynamic page is rendered.

Here's an example of a dynamic page:

`www.example.com/courses`

The /course URL is not a document extension, but rather it's an **endpoint**.

Making requests to that endpoint will trigger a program which will use the supplied user data (such as username and password) and probably some external variables (such as the time and date) to interact with database and ultimately create and return a newly formed web page.

This is also why I earlier said that freeCodeCamp's news page is dynamic – because the content changes as new articles are published.

That page never existed as a file on the server. Instead, it was created by the script that ran when the user requested it.

## Wrapping Up

A web page is a single document which contains text, images, hypertext and other elements.

A hypertext is a web document which contains hyperlinks. A hyperlink links one web page with another.

A network of organized webpages that link to each other is called a website.

For a website to be considered static, every call to the same URL returns the same web page.

One the other hand, if the content changes a lot, then that web page is dynamic. A dynamic page also ends with an endpoint, not a filepath.

So that's it. Hopefully now you can distinguish between a static web page and a dynamic web page. I really hope you got something useful from this article.

If you want more, I recently started a **weekly coding challenge series** aimed at teaching beginners how to program in JavaScript. Check it out on [my blog](https://ubahthebuilder.tech/day-1-who-likes-it).

Thank you for reading and see you soon.

> **P/S**: If you are learning JavaScript, I created an eBook which teaches 50 topics in JavaScript with hand-drawn digital notes. [Check it out here](https://ubahthebuilder.gumroad.com/l/js-50).
