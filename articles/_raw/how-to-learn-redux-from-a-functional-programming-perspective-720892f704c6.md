---
title: How to learn Redux from a functional programming perspective
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T18:14:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-learn-redux-from-a-functional-programming-perspective-720892f704c6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rWN6HdC61ChO2dNs8W8wEQ.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: Redux
  slug: redux
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Redux is a state container that promotes the use of functional programming for managing
  state.

  I would say that the Redux...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Redux is a state container that promotes the use of functional programming for managing state.

I would say that the Redux ecosystem has evolved in an architectural pattern that gives best practices on how to organize an application.

### Pure Functions

Pure functions produce the same output value, given the same input. Pure functions have no side-effects.

Pure functions don’t mutate data, so the question is how can we change state and at the same time use pure functions. Redux proposes a solution: we write pure functions and let the library apply them and do the state change.

The application does state change, but the mutation is encapsulated behind the Redux store.

### Immutability

An immutable value is a value that, once created, cannot be changed.

The state value is immutable, so each time we want to change the state we need to create a new immutable value.

The value of state is immutable but state can change. There is no point to use a library to manage state that doesn’t change. We can use a plain object to store that kind of data.

### Architecture

Redux suggests that we split a practical application into the following parts:

* Presentation Components
* Action Creators (aka Synchronous Action Creators)
* Reducers
* Asynchronous Action Creators
* API Utils/Gateways
* Selectors
* Container Components

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)

