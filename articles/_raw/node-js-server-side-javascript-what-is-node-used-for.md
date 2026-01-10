---
title: Node.js Server-Side JavaScript – What is Node Used For?
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-09-27T21:34:58.000Z'
originalURL: https://freecodecamp.org/news/node-js-server-side-javascript-what-is-node-used-for
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/christina-wocintechchat-com-glRqyWJgUeY-unsplash.jpg
tags:
- name: 'Back end development '
  slug: back-end-development
- name: front end
  slug: front-end
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: node js
  slug: node-js
seo_title: null
seo_desc: 'The release of Node.js in 2009 by Ryan Dahl increased the scope of what
  developers could do with JavaScript. Prior to that, you could only use JavaScript
  on the client side (the browser) or frontend of web applications.

  With Node.js, developers can c...'
---

The release of Node.js in 2009 by Ryan Dahl increased the scope of what developers could do with JavaScript. Prior to that, you could only use JavaScript on the client side (the browser) or frontend of web applications.

With Node.js, developers can create server side applications, command line tools, and more. 

This article is not a crash course on how to use Node.js (you'll find resources for that in the last section of this article). Rather, it's an introduction to what Node.js is, its features, and what it is used for. 

## What is Node.js?

Node.js is an open source JavaScript runtime environment that lets developers run JavaScript code on the server.

If that's too complex for you to understand then you should think of it this way: Node.js is JavaScript that runs outside the browser — on the server. 

Note that Node.js is not a programming language - it's a tool.

## What Is So Special About Node.js?

In this section, we'll discuss some of the features that make Node.js cool to use. 

The aim is not to compare Node.js to other backend technologies, but to help you understand some of its functionalities. 

### Single Threaded and Asynchronous

Node.js is fast at executing tasks (receiving requests and sending back responses) because of its single threaded and asynchronous nature. 

Let's explain some of the terms above. 

By single threaded, this means that Node.js has a single source for handling requests. Multiple threaded backend technologies allocate a new thread for every new request. 

You can think of a thread as someone who renders a service to multiple people. A very popular real life example would be a restaurant. We'll explain this example further along with the asynchronous part of Node.js. 

Node.js is asynchronous because it can handle multiple requests simultaneously. Let's get back to the restaurant example.

A customer gets to a restaurant and sits down waiting for a server. The server gets to the customer's table and takes their order. The order is then taken to the kitchen. 

But the server doesn't wait for the order to be ready before proceeding to the next customer.  They'll return with what the customer ordered for when its ready – in the meantime, the server proceeds to the next customer and repeats the same process. 

The example above is similar to how Node.js works under the hood. It is able to process multiple requests using a single thread asynchronously (without waiting for one request's completion before moving to the next). 

So when the response for a request is ready, it is sent back to the client. 

The single threaded and asynchronous nature of Node.js makes it very fast and ideal for building data-intensive and real-time applications. 

### JavaScript Everywhere

Another advantage of using Node.js as a web developer is the possibility of using JavaScript on the frontend and backend of your web app. 

Before the release of Node.js, web developers had to learn a different programming language to build the backend of their web apps. 

Of course, some developers still use different languages for their backend but Node.js makes it easy to use just one language — JavaScript – if you want. 

### Fast Execution Time

Node.js is built on Google's V8 JavaScript engine which has a very high performance. This lets Node execute requests quickly. 

### Cross Platform Compatibility

Node.js supports many major platforms. So you can write your code and it will run on Windows, MacOS, LINUX, UNIX and even some mobile devices. 

## What is Node Used For?

Here are some of the cool things you can do with Node.js:

* Create HTTP web servers. 
* Generate web pages dynamically. 
* Collect and send form data to a database. 
* Create, read, update, and delete data stored in a database. 
* Create APIs. 
* Build command line tools. 
* Read, write, move, delete, and open/close files on a server. 

## Summary

In this article, we talked about Node.js. We first had a look at what it really is. 

We then talked about some the features that make Node.js stand out.

Lastly, we saw a list of how you can use Node.js.

### How to Learn Node.js

Now that you've had a brief introduction to what Node.js is, its features, and what it is used for, here are some resources that you can use to learn how to use Node.js:

* [freeCodeCamp's Back End Development and APIs certification](https://www.freecodecamp.org/learn/back-end-development-and-apis/). You'll learn how to write back end apps with Node.js and npm. You'll also build web applications with the Express framework, along with MongoDB and the Mongoose library.
* [An 8-hour course on the freeCodeCamp.org YouTube channel](https://youtu.be/Oe421EPjeBE) that'll teach you Node.js and Express. 
* [A 10-hour project based course on the freeCodeCamp.org YouTube channel](https://www.youtube.com/watch?v=qwfE7fSVaZM&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&index=2). You'll build four projects from the knowledge gained from the 8-hour course above. 

Happy Coding!

