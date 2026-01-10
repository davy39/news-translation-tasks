---
title: Discover the power of first class functions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-26T16:47:18.000Z'
originalURL: https://freecodecamp.org/news/discover-the-power-of-first-class-functions-fd0d7b599b69
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Q1WNr4yLLdQuQs01--TCKg.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  In JavaScript, functions are first-class objects, which means they can be:


  stored in a variable, object, or array

  passed...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

In JavaScript, functions are first-class objects, which means they can be:

* stored in a variable, object, or array
* passed as an argument to a function
* returned from a function

### Storing a function

Functions can be stored in three ways:

* store in a variable : `let fn = function doSomething() {}`
* store in an object : `let obj = { doSomething : function(){} }`
* store in an array : `arr.push(function doSomething() {})`

In the first and third example, I used a named function expression.

The function expression defines a function as part of a larger expression. The line of code doesn’t start with `function` .

### Function as an argument

In the next example, the function `doSomething` is sent as an argument to `doAction()`.

```
doAction(function doSomething(){});
```

`doSomething` is a callback.

A callback is a function passed as an argument to another function.

#### Higher order functions

> A higher order function is a function that takes another function as an input, returns a function or does both.

You can find more in the [Discover Functional JavaScript](https://www.amazon.com/dp/B07PBQJYYG) book.

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)

