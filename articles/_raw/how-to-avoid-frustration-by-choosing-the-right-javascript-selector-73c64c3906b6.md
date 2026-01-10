---
title: How to avoid frustration by choosing the right JavaScript selector
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-09T21:48:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-avoid-frustration-by-choosing-the-right-javascript-selector-73c64c3906b6
coverImage: https://cdn-media-1.freecodecamp.org/images/0*M2VaorJmMb0RLa5m
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jonathan Sexton

  A quick guide on how selectors affect your code

  While working on a project, I ran into an issue in my code. I was attempting to
  define multiple HTML elements into a collection and then change those elements based
  on some preset con...'
---

By Jonathan Sexton

#### A quick guide on how selectors affect your code

While working on a project, I ran into an issue in my code. I was attempting to define multiple HTML elements into a collection and then change those elements based on some preset conditions. I struggled for roughly four hours of coding time (across two days) debugging my code and trying to figure out why I wasn’t getting my desired outcome.

Turns out I had used _document.querySelectorAll()_ to assign my elements to a variable, and then I was attempting to change those elements. The only problem is that particular JavaScript selector returns a **static [node list](https://developer.mozilla.org/en-US/docs/Web/API/NodeList)**. Since it isn’t a live representation of the elements, I wasn’t able to change them later in my code.

### **Assumptions**

In this article, I assume a few things to be true:

* You are working in “plain or vanilla” JavaScript (no framework / library)
* You have a basic understanding of JavaScript elements / selectors
* You have a basic understanding of the DOM

### The Nitty-gritty

In the event I have assumed too much, I have provided links to relevant material within the article that I hope will be helpful.

JavaScript is such a vast and rich ecosystem that it’s no surprise that there are many ways of accomplishing the same task. Depending on your task, the way it is accomplished matters to a certain degree.

You can dig a hole with your hands, but it’s much easier and more efficient to do it with a shovel.

To that end, I hope to “hand you a shovel” after you’ve read this article.

![Image](https://cdn-media-1.freecodecamp.org/images/IXLL54yngArOlJqNfITubIlTMhXOrsMuhVkk)
_“A long-exposure shot of a group of people on a beach with children digging a deep hole” by [Unsplash](https://unsplash.com/@khurtwilliams?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Khürt Williams</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### **Choosing the right tool for the job**

I’ve had the question, “Which element selector should I use?” several times. Until now, I haven’t had much desire or need to learn the difference as long as my code produced the desired result. After all, what does the color of the taxi matter as long as it gets you to your destination safely and in a timely manner…right?

Let’s start with some of the ways to select [**DOM**](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) elements in JavaScript. There are more ways (I believe) to select elements, but the ones listed here are by far the most prevalent I’ve come across.

#### [**document.getElementById()**](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById)

These will only ever return one (1) element because, by their nature, ID’s are unique and there can only be one (with the same name) on the page at a time.

It returns an object that matches the string passed into it. It returns **null** if no matching ID is found in your HTML.

> Syntax example -&g_t; document.getElementById(‘main_conten_t’)

Unlike some selectors that we’ll get to later in the article, there is no need for a # to denote element id.

#### [**_document.getElementsByTagName()_**](https://developer.mozilla.org/en-US/docs/Web/API/Element/getElementsByTagName)

Notice the “S” in elements — this selector returns **multiples** in an **array-like structure** known as an [HTML collection](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection) — all of the document is searched including the [root node](https://javascript.info/dom-navigation) (the document object) for a matching name. This element selector starts at the top of the document and continues down, searching for tags that match the passed-in string.

If you are looking to use native [array methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) you’re out of luck. That is, unless you convert the returned results into an array to iterate over them, or use the ES6 [spread operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) — both of which are beyond the scope of this article. But I wanted you to know it is possible to use array methods if you wish to.

> Syntax example -&g_t; document.getElementsByTagName(‘header_li_nks’). This selector also accep**ts p, div, body, or any other valid HTML t**ag.

#### [**_document.getElementsByClassName()_**](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementsByClassName)

Class name selector — again notice the “S” in elements — this selector returns **multiples** in an **array-like structure** known as an [HTML collection](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection) of class names. It matches the passed-in string (can take multiple class names, although they are separated by a space), searches all of the document, can be called on any element, and only returns descendants of the passed in class.

Also, no . (period) is needed to denote class name

> Syntax example: _document.getElementsByClassName(‘classNam_e’)

#### [**_document.querySelector()_**](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)

This selector will only ever return one (1) element.

Only the first element matching the passed-in string will be returned. If no matches for the provided string are found, **null** is returned.

> Syntax example: _document.querySelector(‘#side_note_’) _or document.querySelector(‘.header_link_s’)

Unlike all of our previous examples, this selector requires a . (period) to denote class or an _#_ (octothorp) to denote an ID and works with all CSS selectors.

#### [**_document.querySelectorAll()_**](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll)

This selector returns **multiples** that match the passed-in string and arranges them into another **array like structure** known as a [node list](https://developer.mozilla.org/en-US/docs/Web/API/NodeList).

As with some of the previous examples, the node list cannot make use of native [array methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) like [.forEach(](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)). So if you want to use those, you must first convert the node list into an array. If you do not wish to convert, you can still iterate over the node list with a f[or…in statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in).

The passed in string must match a valid CSS selector — id, class names, types, attributes, values of attributes, etc.

> Syntax example: _document.querySelectorAll(‘.footer_link_s’)

### Wrapping up

By choosing the right selector for your coding needs, you’ll avoid many of the pitfalls I’ve fallen into. It can be incredibly frustrating when your code doesn’t work, but by ensuring that your selector matches your situational needs, you’ll have no trouble “digging with your shovel” :)

Thank you for reading through this post. If you enjoyed it, please consider donating some claps to help others find it as well. I publish (actively managing my schedule to write more) related content on my [blog](https://www.powerofgoose.com/blog). I’m also active on [Twitter](https://twitter.com/jj_goose) and am always happy to connect with other developers!

