---
title: How to create a store using pure functions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-29T17:39:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-store-using-pure-functions-2c19b678552f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1QLyoQuirofEmDT1nE7LeA.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Pure functions produce the same output value, given the same input. They have no
  side-effects, and are easier to read, un...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Pure functions produce the same output value, given the same input. They have no side-effects, and are easier to read, understand and test.

Given all this, I would like to create a store that hides the state but at the same time uses pure functions.

### Immutability

Pure functions don’t modify their input. They treat the input values as immutable.

An immutable value is a value that, once created, cannot be changed.

[Immutable.js](https://facebook.github.io/immutable-js/) provides immutable data structures like `List`. An immutable data structure will create a new data structure at each action.

Consider the next code:

```
import { List } from "immutable";
const list = List();
const newList = list.push(1);
```

`push()` creates a new list that has the new element. It doesn’t modify the existing list.

`delete()` returns a new `List` where the element at the specified index was removed.

The `List` data structure offers a nice interface for working with lists in an immutable way, so I will use it as the state value.

### The Store

The store manages state.

State is data that can change. The store hides that state data and offers a public set of methods for working with it.

I would like to create a book store with the `add()`, `remove()` and `getBy()` methods.

I want all these functions to be pure functions.

There will be two kind of pure functions used by the store:

* functions that will read and filter the state. I will call them getters.
* functions that will modify the state. I will call them setters.

Both these kinds of functions will take the state as their first parameter.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)

