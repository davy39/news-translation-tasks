---
title: PHP Get URL – How to Get the Full URL of the Current Page
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-22T17:37:32.000Z'
originalURL: https://freecodecamp.org/news/php-get-url-how-to-get-the-full-url-of-the-current-page
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a1c740569d1a4ca239c.jpg
tags:
- name: PHP
  slug: php
- name: url
  slug: url
seo_title: null
seo_desc: "By Dan Englishby\nIn this PHP-focused article, we will explore how to get\
  \ the URL of the current page in the PHP programming language. \nYou may want to\
  \ get the current page URL for the following reasons:\n\nBuilding internal links\n\
  Using filters with GET..."
---

By Dan Englishby

In this PHP-focused article, we will explore how to get the URL of the current page in the PHP programming language. 

You may want to get the current page URL for the following reasons:

* Building internal links
* Using filters with GET requests, for example, currentURL.com?myFilterParameter=Food

PHP actually stores lots of useful information as users navigate your web application. One of these is, of course, the current URL.

PHP stores these pieces of useful information in its array of super-global variables.

### What are Superglobals?

> Superglobals are already defined variables by the PHP engine which can be used in any kind of scope. They are readily available at any one time.

There are many of these superglobals, but the one we are interested in is the $_SERVER superglobal.

### The $_SERVER Superglobal

The $_SERVER superglobal variable has many properties that are accessible with an associative style index.  

Some of the values we can access include:

* HTTP_USER_AGENT
* HTTP_HOST
* HTTP_ACCEPT_ENCODING
* HTTP_ACCEPT

<p> You can see more of these indicies in the PHP documentation <a href="https://www.php.net/manual/en/reserved.variables.server.php" rel="nofollow" target="_blank">here.</a></p>

### So, how do we get the full URL?

With the above points on superglobals and the **$_SERVER** superglobal in mind, we can go ahead and get the current page's URL. 

In the following screenshot, I've rendered a PHP application in a local environment in a page named "home." 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-91.png)

The URL is **http://localhost/home**.

In the code base of this page, I'm going to use the **$_SERVER** variable.

With this variable, we will have to use 2 separate indices to get each part of the current page's URL. The first part will be the host, localhost, and the second part will be the page name, home.

The first index we will use is **HTTP_HOST** - The current web address host, for example localhost, or example.com

The second is **REQUEST_URI** which will give us the part of the URL after the host, so this is anything after localhost or example.com

Let's see this in action:

```
$currentPageUrl = 'http://' . $_SERVER["HTTP_HOST"] . $_SERVER["REQUEST_URI"];


echo "Current page URL " . $currentPageUrl;
```

### Output

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-102.png)

And that is it - pretty straightforward!

## Summary

The **$_SERVER** superglobal variable stores a lot of vital information for modern day use-cases. As we've discovered in this instance, getting the current page's URL is made simple with the ability to access this specific variable.

It's worth checking out the documentation to see what other indices are available, though, as it's good to have in mind how helpful this variable can be.

I hope you enjoyed this article! If you did, feel free to check out my blog, [https://www.codewall.co.uk/](https://www.codewall.co.uk/)

