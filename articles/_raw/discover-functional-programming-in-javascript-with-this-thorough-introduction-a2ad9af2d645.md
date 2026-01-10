---
title: Discover Functional Programming in JavaScript with this thorough introduction
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-04T00:53:10.000Z'
originalURL: https://freecodecamp.org/news/discover-functional-programming-in-javascript-with-this-thorough-introduction-a2ad9af2d645
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PU20rbKCMm3C2BLEM24dgg.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: Productivity
  slug: productivity
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  JavaScript is the first language to bring Functional Programming to the mainstream.
  It has first-class functions and clos...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

JavaScript is the first language to bring Functional Programming to the mainstream. It has first-class functions and closures. They open the way for functional programming patterns.

# First-Class Functions

Functions are first-class objects. Functions can be stored in variables, objects or arrays, passed as arguments to other functions or returned from functions.

```javascript
//stored in variable
function doSomething(){
}

//stored in variable
const doSomething = function (){ };

//stored in property
const obj = { 
   doSomething : function(){ } 
}

//passed as an argument
process(doSomething);

//returned from function
function createGenerator(){
  return function(){
  }
}
```

## Lambdas

_A lambda is a function that is used as a value._

In JavaScript, functions are first-class objects, so all functions can be used as values. All functions can be lambdas with or without a name. I actually suggest favoring named functions.

# Functional Array Toolbox

## [Basic Toolbox](https://jsfiddle.net/lorinoata/s5b9m6ut/)

`filter()` selects values from a list based on a predicate function that decides what values should be kept.

```javascript
const numbers = [1,2,3,4,5,6];
function isEven(number){
  return number % 2 === 0;
}
const evenNumbers = numbers.filter(isEven);
```

A predicate function is a function that takes one value as input and returns `true`/`false` based on whether the value satisfies the condition. `isEven()` is a predicate function.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)

