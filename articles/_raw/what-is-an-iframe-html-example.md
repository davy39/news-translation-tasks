---
title: What is an iframe? HTML iframe Example
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2022-04-02T04:00:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-an-iframe-html-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pine-watt-3_Xwxya43hE-unsplash.jpg
tags:
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
seo_title: null
seo_desc: "An iframe is an HTML document embedded inside another HTML document on\
  \ a website. Think of it as a \"webpage within a web page.\" \nPerhaps you've seen\
  \ the movie Inception, which deals with dreams within dreams. Or played with one\
  \ of those Russian neste..."
---

An iframe is an HTML document embedded inside another HTML document on a website. Think of it as a "webpage within a web page." 

Perhaps you've seen the movie Inception, which deals with dreams within dreams. Or played with one of those Russian nested dolls. This is the same concept.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/1280px-Matryoshka_transparent.png)
_[Photo by BrokenSphere (CC BY-SA 3.0)](https://commons.wikimedia.org/w/index.php?curid=3773186)_

## HTML iframe tag Example

The iframe HTML tag is used to specify the URL of the document to be embedded.

Iframes are often used to embed videos, maps, and other media on a web page. You can also use them to embed another web page into a web page. Here are a few examples of code using `iframe` to embed an external resource:

```html
<iframe src="http://www.example.com/">

<iframe src="http://www.example.com/" width="400" height="300">

<iframe src="http://www.example.com/" style="border: 0;">

```

Here are a couple of examples of embedding interactive resources in HTML. This particular code will embed a Vimeo video player:

```html
<iframe src="https://player.vimeo.com/video/76979872" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
```

Iframes have been around since the early days of the web. Developers originally used them to embed external content on a web page, such as a video from YouTube.

There are also "toolbar" type websites like Stumbleupon that would add their toolbar on top of a website. Stumbleupon would do this by rendering the website on their own page using an iframe.

## Why developers have mostly stopped using iframes in their websites

Nowadays, developers still use iframes are still used for embedding media and other content on a web page. But due to security considerations, many web development frameworks discourage this.

At the end of the day, an iframe running inside of another web page will not be an ideal user experience. Iframes can look particularly bad on mobile phones, and break otherwise responsive web design layouts. This is why iframes have largely fallen out of favor.

I hope you've found this helpful. If you want to learn more about programming and technology, try [freeCodeCamp's core coding curriculum](https://www.freecodecamp.org/learn). It's free.

