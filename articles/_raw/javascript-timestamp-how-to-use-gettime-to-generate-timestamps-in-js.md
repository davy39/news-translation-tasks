---
title: JavaScript Timestamp – How to Use getTime() to Generate Timestamps in JS
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-08-19T17:58:01.000Z'
originalURL: https://freecodecamp.org/news/javascript-timestamp-how-to-use-gettime-to-generate-timestamps-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/aron-visuals-BXOXnQ26B7o-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In JavaScript, timestamps are usually associated with Unix time. And there
  are different methods for generating such timestamps.

  When we make use of the different JavaScript methods for generating timestamps,
  they return the number of milliseconds th...'
---

In JavaScript, timestamps are usually associated with [Unix time](https://en.wikipedia.org/wiki/Unix_time). And there are different methods for generating such timestamps.

When we make use of the different JavaScript methods for generating timestamps, they return the number of milliseconds that has passed since 1 January 1970 UTC (the Unix time). 

In this article, you'll learn how to use the following methods to generate Unix timestamps in JavaScript:

* The `getTime()` method. 
* The `Date.now()` method. 
* The `valueOf()` method. 

## How to Use `getTime()` to Generate Timestamps in JS

```javascript
var timestamp = new Date().getTime();

console.log(timestamp)
// 1660926192826
```

In the example above, we created a `new Date()` object and stored it in a `timestamp` variable. 

We also attached the `getTime()` method to the `new Date()` object using dot notation: `new Date().getTime()`. This returned the Unix time at that point in milliseconds: 1660926192826.

To get the timestamp in seconds, you divide the current timestamp by 1000. That is:

```javascript
var timestamp = new Date().getTime();

console.log(Math.floor(timestamp / 1000))

```

## How to Use `Date.now()` to Generate Timestamps in JS

```javascript
var timestamp = Date.now();

console.log(timestamp)
// 1660926758875
```

In the example above, we got the Unix timestamp at that particular point in time using the `Date.now()` method. 

The timestamps you see in these examples will be different from yours. This is because you'll get the timestamp of the time that has elapsed from 1 January 1970 UTC to your current time. 

## How to Use `valueOf()` to Generate Timestamps in JS

```javascript
var timestamp = new Date().valueOf();

console.log(timestamp)
// 1660928777955
```

Just like the `getTime()` method, we have to attach the `valueOf()` method to a `new Date()` object in order to generate a Unix timestamp. 

The `new Date()` object, without `getTime()` or `valueOf()`, returns the information about your current time. 

## Summary

In the article, we talked about timestamps in JavaScript. There are usually associated with the Unix time. 

We saw three different methods that can be used to generate timestamps in JavaScript with code examples. 

Happy coding!

