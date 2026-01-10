---
title: Let’s explore objects in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-10T17:37:32.000Z'
originalURL: https://freecodecamp.org/news/lets-explore-objects-in-javascript-4a4ad76af798
coverImage: https://cdn-media-1.freecodecamp.org/images/1*o9elBqm0t6G25Jt1WhkF4w.jpeg
tags:
- name: coding
  slug: coding
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

  Objects are dynamic collections of properties, with a “hidden” property to the object’s
  prototype.

  A property has a key a...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Objects are dynamic collections of properties, with a “hidden” property to the object’s prototype.

A property has a key and a value.

### Property key

The property key is a unique string.

There are two ways to access properties: dot notation and bracket notation. When the dot notation is used, the property key must be a valid identifier.

```
let obj = {  message : "A message"}
```

```
obj.message //"A message"obj["message"] //"A message"
```

Accessing a property that doesn’t exist will not throw an error, but will return `undefined` .

```
obj.otherProperty //undefined
```

JavaScript treats primitives, objects, and functions like objects.

Objects are dynamic in nature and can be used as maps.

Objects inherit from other objects. Constructor functions and class are sugar syntax for creating objects that inherit from other prototype objects.

`Object.create()` can be used for single inheritance and `Object.assign()` for multiple inheritance.

Factory functions can build encapsulated objects.

Read [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2) and learn how to build apps in function style.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y&source=post_page---------------------------)**.**

You can find me on [Medium](https://medium.com/@cristiansalcescu) and [Twitter](https://twitter.com/cristi_salcescu).

