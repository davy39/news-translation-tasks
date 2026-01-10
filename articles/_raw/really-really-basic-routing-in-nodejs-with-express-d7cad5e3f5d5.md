---
title: Really, really basic routing in Node.js with Express
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-03T04:19:40.000Z'
originalURL: https://freecodecamp.org/news/really-really-basic-routing-in-nodejs-with-express-d7cad5e3f5d5
coverImage: https://cdn-media-1.freecodecamp.org/images/0*FWsvE-8X-T1wNDj5.
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: routing
  slug: routing
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Pau Pavón

  The goal of this story is to briefly explain how routing works in Express while
  building a simple — very simple — Node app.

  We’ll also use EJS, a template engine that “lets you generate HTML markup with plain
  JavaScript,” according to th...'
---

By Pau Pavón

The goal of this story is to briefly explain how routing works in Express while building a simple — very simple — Node app.

We’ll also use EJS, a template engine that “lets you generate HTML markup with plain JavaScript,” according to [their website](http://ejs.co/). Basically, it’ll let us create HTML pages that can vary depending on the request the client makes. We won’t be using this last feature, but it’s a great one. At the end of this article, you’ll find some resources where you can learn more.

### What is routing? (In 2-ish lines)

First of all, let’s take a quick (really quick) glance at what routing is:

> somewebsite.com/someroute

It’s basically taking the user (or some data) from one place to another. That place is the route. I told you I was going to make it quick.

### Creating the project

We’re going to build a fancy website to learn how routing works in Express. Check it out:

![Image](https://cdn-media-1.freecodecamp.org/images/zKy5qHElo1OJCfcnBBlTS0rU2RqIvIaPPHRc)

Cool, right? But it’s everything we need for the moment.

First, let’s create the project and install the packages. Just run the following in the command line:

> npm install express

> npm install ejs

You can additionally add the _dash dash save_ (I write — as “_dash”_ because Medium automatically formats it, and it doesn’t look well for this purpose) to save it in your _package.json_ file. But how this works is a story for another day.

Then we will require Express and set the view engine to EJS in our _app.js_ file as follows:

```
var express = require('express');var app = express();app.set('view engine', 'ejs');
```

We’ll also include the following line so our app listens for requests:

```
app.listen(3000);
```

### Handling GET requests

Congratulations, everything is ready to handle requests! There are several types of requests in HTTP, but we’ll only be handling GET requests, which are used to retrieve data from the server. To handle this kind of request in Express, we use the following method:

```
app.get('/about', function(req, res) {  res.render('about');});
```

Let’s take a look at what’s happening here. We’re telling our server that, whenever someone types in _somewebsite.com/about_, we want to fire a function. That function takes two parameters, _req_ (request) and _res_ (response). Using the response object, we render the _about page_.

For this to work, we’ll have to create a page named _about.ejs_ in HTML. We’ll also place it in a folder called _views_ inside our project folder. This is the folder where Express will look to render the view. Here you have the mega-complex about page we’ll be using for this example:

![Image](https://cdn-media-1.freecodecamp.org/images/xHlH6J5GdxC1m8GhzCNtf5WRI71Lv-QEUYgt)

Nice! But, what if the user doesn’t type in any route? Just like we do most of the times, _somewebsite.com_? Well, really easy. Change _/about_ to just _/,_ and render whatever page you like:

```
app.get('/', function(req, res) {  res.render('home');});
```

### Handling non-existing routes

But what if someone types in a route that doesn’t exist? We probably don’t want a default error page to show up. Instead, we want a custom, cool error page.

Well, the good news is that it’s extremely easy to make one with Express. Just replace the route parameter in the get method with an asterisk and render your own error page like so:

```
app.get('*', function(req, res) {  res.render('error');});
```

### Trying it out!

Finally, let’s run our server from the command line (assuming the server is named _app.js_)

> node app

and see if it works! Let’s type in the name of our server (_localhost_, as it’s a local server running on our computer) and the port (_3000_ in this case) in our browser:

> localhost:3000

![Image](https://cdn-media-1.freecodecamp.org/images/1KFP8uvz25ry2d2pNQ2QsSdQnacvlqM3E2ex)
_localhost:3000 or localhost:3000/_

![Image](https://cdn-media-1.freecodecamp.org/images/eDCDZV5wyUWUoLFsLQQnZU5hHa9P8rgxDirO)
_localhost:3000/about_

![Image](https://cdn-media-1.freecodecamp.org/images/hkwkh0YVUHuY-0LWm6zUmlMXUXYrr2P6hSZj)
_localhost:3000/anythingthatwehaventsetaroutefor_

Amazing!

### Further reading

You can learn everything you need to know about routing in the [Express guide](http://expressjs.com/en/guide/routing.html), and there’s a lot of handy things in the [EJS website](http://ejs.co) as well!

I hope this article was helpful for you. If it was, please leave a comment and clap it up!

Happy coding… **_Or happy routing, I guess!_**

