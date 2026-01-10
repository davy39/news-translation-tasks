---
title: A practical ES6 guide on how to perform HTTP requests using the Fetch API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-04T16:21:47.000Z'
originalURL: https://freecodecamp.org/news/a-practical-es6-guide-on-how-to-perform-http-requests-using-the-fetch-api-594c3d91a547
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Kj2i4zLF-jKOsiLb.jpg
tags:
- name: api
  slug: api
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Dler Ari

  In this guide, I’ll show you how to use the Fetch API (ES6+) to perform HTTP requests
  to an REST API with some practical examples you’ll most likely encounter.

  Want to quickly see the HTTP examples? Go to section 5. The first part describ...'
---

By Dler Ari

In this guide, I’ll show you how to use the Fetch API (ES6+) to perform HTTP requests to an [REST API](https://jsonplaceholder.typicode.com/) with some practical examples you’ll most likely encounter.

Want to quickly see the HTTP examples? Go to section 5. The first part describes the asynchronous part of JavaScript when working with HTTP requests.

> **Note**: All examples are written in ES6 with [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions).

A common pattern in today’s current web/mobile applications is to request or show some sort of data from the server (such as users, posts, comments, subscriptions, payments and so forth) and then manipulate it by using CRUD (create, read, update or delete) operations.

To further manipulate a resource, we often use [these JS methods](https://medium.freecodecamp.org/7-javascript-methods-that-will-boost-your-skills-in-less-than-8-minutes-4cc4c3dca03f) (recommended) such as `.map()`, `.filter()` and `.reduce()`.

> If you want to become a better web developer, start your own business, teach others, or improve your development skills, I’ll be posting weekly tips and tricks on the latest web development languages.

### Here’s what we’ll address

1. Dealing with JS’s asynchronous HTTP requests
2. What is AJAX?
3. Why Fetch API?
4. A quick intro to Fetch API
5. Fetch API - CRUD examples ← the good stuff!

### 1. Dealing with JS’s asynchronous HTTP requests

One of the most challenging parts with understanding how JavaScript (JS) works is understanding how to deal with asynchronous requests, which requires and understanding in how promises and callbacks work.

In most programming languages, we are wired to think that operations happen in order (sequentially). The first line must be executed before we can move on to the next line. It make sense because that is how we humans operate and complete daily tasks.

But with JS, we have multiple operations that are running in the background/foreground, and we cannot have a web app that freezes every time it waits for a user event.

> Describing JavaScript as asynchronous is perhaps misleading. It’s more accurate to say that JavaScript is synchronous and single-threaded with various callback mechanisms. [Read more](https://stackoverflow.com/questions/2035645/when-is-javascript-synchronous).

Nevertheless, sometimes things must happen in order, otherwise it will cause chaos and unexpected results. For that reason, we may use promises and callbacks to structure it. An example could be validating user credentials before proceeding to the next operation.

### 2. What is AJAX

AJAX stands for Asynchronous JavaScript and XML, and it allows web pages to be updated asynchronously by exchanging data with a web server while the app is running. In short, it essentially means that you can update parts of a web page without reloading the whole page (the URL stays the same).

> AJAX is a misleading name. AJAX applications might use XML to transport data, but it is equally common to transport data as plain text or JSON text.  
>  — w3shools.com

#### AJAX all the way?

I’ve seen that many developers tend to get really excited about having everything in a single page application (SPA), and this leads to lots of asynchronous pain! But luckily, we have libraries such as Angular, VueJS and React that makes this process a whole lot easier and practical.

Overall, it’s important to have a balance between what should reload the whole page or parts of the page.

And in most cases, a page reload works fine in terms of how powerful browsers have become. Back in the days, a page reload would take seconds (depending on the location of the server and browser capabilities). But today’s browsers are extremely fast so deciding whether to perform AJAX or page reload is not that of a big difference.

My personal experience is that it’s a lot easier and faster to create a search engine with a simple search button than doing it without a button. And in most cases, the customer doesn’t care if it is a SPA or an extra page-reload. Of course, don’t get me wrong, I do love SPAs, but we need to consider a couple of trade-offs, if we deal with limited budget and lack of resources then maybe a quick solution is better approach.

In the end, it really depends on the use case, but personally I feel that SPAs require more development time and a bit of headache than a simple page reload.

### 3. Why Fetch API?

This allows us to perform declarative HTTP requests to a server. For each request, it creates a `Promise` which must be resolved in order to define the content type and access the data.

Now the benefit of Fetch API is that it is fully supported by the JS ecosystem, and is also a part of the [MDN Mozilla docs](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API). And last but not least, it works out of the box on most browsers (except IE). In the long-term, I’m guessing it will become the standard way of calling web APIs.

> Note! I’m well aware other HTTP approaches such as using Observable with RXJS, and how it focuses on memory-management/leak in terms of subscribe/unsubscribe and so forth. And maybe that will become the new standard way of doing HTTP requests, who knows?  
>   
> Anyway, in this article I’m only focusing on Fetch API, but may in the future write an article about Observable and RXJS.

### 4. A quick intro to Fetch API

The `fetch()` method returns a `Promise` that resolves the `Response` from the `Request` to show the status (successful or not). If you ever get this message `promise {}` in your console log screen, don’t panic — it basically means that the `Promise` works, but is waiting to be resolved. So in order to resolve it we need the `.then()` handler (callback) to access the content.

So in short, we first define the path (**Fetch**), secondly request data from the server (**Request**), thirdly define the content type (**Body**) and last but not least, we access the data (**Response**).

If you struggle to understand this concept, don’t worry. You’ll get a better overview through the examples shown below.

```
The path we'll be using for our examples 
https://jsonplaceholder.typicode.com/users // returns JSON
```

### 5. Fetch API - HTTP examples

If we want to access the data, we need two `.then()` handlers (callback). But if we want to manipulate the resource, we need only one `.then()` handler. However, we can use the second one to make sure the value has been sent.

Basic Fetch API template:

<script src="https://gist.github.com/AriPal/030365fa25e3c9260c8486e6705f9310.js"></script>

> Note! The example above is just for illustrative purposes. The code will not work if you execute it.

#### Fetch API examples

1. Showing a user
2. Showing a list of users
3. Creating a new user
4. Deleting a user
5. Updating a user

> **Note!** The resource will not be really created on the server, but will return a fake result to mimic a real server.

#### 1. Showing a user

As previously mentioned, the process of showing a single user consists of two `.then()` handlers (callback), the first one to define the object, and the second one to access the data.

> Notice just by reading the query string `/users/2` we are able to understand/predict what the API does. For more information on how to write high-quality REST API, check out these [guidelines](https://hackernoon.com/restful-api-designing-guidelines-the-best-practices-60e1d954e7c9) tip written by [Mahesh Haldar](https://www.freecodecamp.org/news/a-practical-es6-guide-on-how-to-perform-http-requests-using-the-fetch-api-594c3d91a547/undefined).

#### **Example**

<script src="https://gist.github.com/AriPal/7d80a696621a1bff97bb9516154b7e5a.js"></script>

#### 2. Showing a list of users

The example is almost identical to the previous example except that the query string is `/users`, and not `/users/2`.

#### Example

<script src="https://gist.github.com/AriPal/83c75923f680b7a0670b812d9bad8518.js"></script>

#### 3. Creating a new user

This one looks a bit different from the previous example. If you are not familiar with the HTTP protocol, it simply provides us with a couple of sweet methods such as `POST`, `GET`,`DELETE`, `UPDATE`, `PATCH` and `PUT`. These methods are verbs that simply describe the type of action to be executed, and are mostly used to manipulate the resource/data on the server.

Anyway, in order to create a new user with Fetch API, we’ll need to use the HTTP verb `POST`. But first, we need to define it somewhere. Luckily, there is an optional argument `[Init](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch)` we can pass along with the URL for defining custom settings such as method type, body, credentials, headers and so forth.

> Note: The `fetch()` method's parameters are identical to those of the `[Request()](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request)` constructor.

#### Example

<script src="https://gist.github.com/AriPal/2731c3803e2f498a0dfc8abcda8d946c.js"></script>

#### **4. Deleting a user**

In order to delete the user, we first need to target the user with `/users/1`, and then we define the method type which is `DELETE`.

#### Example

<script src="https://gist.github.com/AriPal/cb06ffac0c04408da74e8707e9e3dd6b.js"></script>

#### 5. Updating a user

The HTTP verb `PUT` is used to manipulate the target resource, and if you want to do partial changes, you’ll need to use `PATCH`. For more information on what these HTTP verbs do, [check this out](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).

#### Example

<script src="https://gist.github.com/AriPal/eb46118f720d3d71800fef7ead682a70.js"></script>

### Conclusion

Now you have a basic understanding of how to retrieve or manipulate a resource from the server using JavaScript’s Fetch API, as well as how to deal with promises. You can use this article as a guide for how to structure your API requests for CRUD operations.

Personally, I feel that the Fetch API is declarative and you can easily understand what is happening without any technical coding experience.

> All examples are shown in promised-base request where we chain the request using `_.then_` callback. This is a standard approach which many devs are familiar with, however, if you want to use `_async/await_` check this [article out](https://dev.to/johnpaulada/synchronous-fetch-with-asyncawait). The concept is the same, except `async/await` is easier to read and write.

Here are a few articles I’ve written about the web-ecosystem along with personal programming tips and tricks.

* [A comparison between Angular and React](https://www.freecodecamp.org/news/a-comparison-between-angular-and-react-and-their-core-languages-9de52f485a76/)
* [A chaotic mind leads to chaotic code](https://www.freecodecamp.org/news/a-chaotic-mind-leads-to-chaotic-code-e7d6962777c0)
* [Developers that constantly want to learn new things](https://codeburst.io/developers-that-constantly-want-to-learn-new-things-heres-a-tip-7a16e42302e4)
* [A practical guide to ES6 modules](https://www.freecodecamp.org/news/how-to-use-es6-modules-and-why-theyre-important-a9b20b480773)
* [Learn these core Web Concepts](https://www.freecodecamp.org/news/learn-these-core-javascript-concepts-in-just-a-few-minutes-f7a16f42c1b0/?gi=6274e9c4d599)
* [Boost your skills with these important JavaScript methods](https://www.freecodecamp.org/news/7-javascript-methods-that-will-boost-your-skills-in-less-than-8-minutes-4cc4c3dca03f/)
* [Program faster by creating custom bash commands](https://codeburst.io/learn-how-to-create-custom-bash-commands-in-less-than-4-minutes-6d4ceadd9590)

You can find me on Medium where I publish on a weekly basis. Or you can follow me on [Twitter](http://twitter.com/dleroari), where I post relevant web development tips and tricks along with personal stories.

_P.S. If you enjoyed this article and want more like these, please clap ❤ and share with friends that may need it, it’s good karma._

