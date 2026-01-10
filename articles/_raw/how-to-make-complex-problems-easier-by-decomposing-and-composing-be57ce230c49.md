---
title: How to make complex problems easier by decomposing and composing
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-13T14:48:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-complex-problems-easier-by-decomposing-and-composing-be57ce230c49
coverImage: https://cdn-media-1.freecodecamp.org/images/0*4H9f_YZRxP-lUtYx
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Our natural way of dealing with complexity is to break it into smaller pieces and
  then put everything back together.

  This...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Our natural way of dealing with complexity is to break it into smaller pieces and then put everything back together.

This is a two step process:

* decompose the problem into smaller parts
* compose the small parts to solve the problem

We decompose in smaller parts because they are easier to understand and implement. The smaller parts can be developed in parallel.

The process of decomposition is about assigning responsibilities and giving names. This makes it easy to talk and reason about. Once we identify a responsibility, we can reuse it.

Composition is about combining the small parts together and establishing a relationship between them. We decide the way these pieces communicate, the order in which they execute, and how data flows between them.

We find a system hard to understand even if it is split in smaller parts, if there is a high number of relations between these parts. In order to make a system easier to understand, we need to minimize the number of possible connections between its parts.

### Object decomposition

Objects are more than state and behavior working together. Objects are things with responsibilities.

#### Decompose

In [How to create a three layer application with React](https://medium.freecodecamp.org/how-to-create-a-three-layer-application-with-react-8621741baca0), I take a to-do list application and split the responsibilities between the following objects :

* `TodoDataService` : responsible for the communication with the server Todo API
* `UserDataService` : responsible for the communication with the server User API.
* `TodoStore` : the domain store for managing to-dos. It is the single source of truth regarding to-dos.
* `UserStore` : the domain store for managing users.
* `TodoListContainer` : the root container component displaying the list of to-dos.

As you can see, when decomposing, I assign responsibilities and give names.

#### Compose

Next, I compose them together in a single function. This is the place where all objects are created and dependencies injected. It is called Composition Root.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)

