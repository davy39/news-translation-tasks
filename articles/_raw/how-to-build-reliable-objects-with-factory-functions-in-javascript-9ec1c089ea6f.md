---
title: How to build reliable objects with factory functions in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-25T15:46:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-reliable-objects-with-factory-functions-in-javascript-9ec1c089ea6f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LBX1CRHCljE9BkuxOZUhmg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  I suggest to take into consideration these ideas for building reliable objects in
  JavaScript:


  Split objects in two: data...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

I suggest to take into consideration these ideas for building reliable objects in JavaScript:

* Split objects in two: data objects and behavior objects
* Make the data objects immutable
* Expose behavior and hide data in behavior objects
* Build testable behavior objects

### Data vs Behavior Objects

Essentially there are two kinds of objects in an application:

* **Data Objects —** expose data
* **Behavior Objects —** expose behavior and hide data

#### Data Objects

Data objects expose data. They are used to structure and transfer data inside the application.

Let’s take the case of a to-do list application.

This is how the to-do data object, gotten from the server, may look:

```js
{ id: 1, title: "This is a title", userId: 10, completed: false }
```

And this is how a data object used to display information in the view may look:

```js
{ id: 1, title: "This is a title", userName: "Cristi", completed: false };
```

As you can see, both objects contain only data. There is a small difference between them: the data object for the view has `userName` instead of the `userId`.

Data objects are plain objects, usually built with object literals.

#### Behavior Objects

Behavior objects expose methods and hide data.

Behavior objects act on data objects. They may take data objects as inputs or return data objects.

I’ll take the case of the `TodoStore` object. The responsibility of the object is to store and manage the list of to-dos. It makes the synchronization with the server using the `dataService` object.

Read [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2) and learn how to build apps in function style.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y&source=post_page---------------------------)**.**

You can find me on [Medium](https://medium.com/@cristiansalcescu) and [Twitter](https://twitter.com/cristi_salcescu).

