---
title: How to communicate between Components
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T14:38:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-communicate-between-components-b48ef70bf913
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MdWVvVEI6qmBhyYfa5p4_A.jpeg
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

  Components are a tool for splitting the page in smaller pieces that are easier to
  manage and reuse. By breaking the page ...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Components are a tool for splitting the page in smaller pieces that are easier to manage and reuse. By breaking the page into smaller parts, we make their implementation simpler.

But at the same time this creates a new challenge: the communication between these small parts.

### A showcase

I’ll take as an example a page managing a list of to-dos. The user is able to see, add, and search for to-dos.

This is how the page looks:

![Image](https://cdn-media-1.freecodecamp.org/images/SdPLBMLKMH2E8k6dpvOlAXgvFtmOchIavoMe)

### Identifying components

We can split the page in three main components based on their responsibilities:

* `TodoAddForm`: the form for adding a new to-do
* `TodoSearchForm`: the form for searching a to-do
* `TodoList`: the list for displaying the to-dos

We can go even further and make every item in the list have its own component: `TodoListItem`

For the sake of this analysis, I encapsulate the text-box and button in their own component: `FormInput`, `FormButton`.

### Components are in a Tree Structure

Before analyzing how to communicate between components, we need understand that components are organized in a tree structure. If the framework doesn’t force a root component, then we’ll create one.

Now let’s create the tree structure:

![Image](https://cdn-media-1.freecodecamp.org/images/-DfvdcfTZOQTJRN-ARB6dNkbWr5cREy5r6Qk)
_Components’ Tree Structure_

### Presentation and Container Components

We can start defining the components’ responsibilities by using the Container and Presentational Pattern.

The pattern is described in [Presentational and Container Components](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0) and [Container Components](https://medium.com/@learnreact/container-components-c0e67432e005)

The presentation components communicate only through their own properties, methods, and events. They are not connected to external communication objects. This makes presentation components easier to understand and more reusable, as they are not coupled to other objects.

The container components are connected to external objects. They listen for events from these objects and do actions. They provide data to the user interface.

I’ll start with only one root container component: `TodoContainer`. All the other will be presentation components: `TodoAddForm`, `TodoSearchForm`, `TodoList`, `TodoListItem` , `FormInput` and `FormButton`.

There many means for communication at our disposal. In the end, we need to choose the one that’s appropriate for our situation.

To sum up, these means of communication are :

* Parent → Child: properties, methods
* Child → Parent: events, callbacks
* Child → Child: via parent, domain store, UI store, or global event bus.  
In short, two child components can communicate using their closest parent or a shared third object.

You can find more in the [Discover Functional JavaScript](https://www.amazon.com/dp/B07PBQJYYG) book.

Read [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2) and learn how to build apps in function style.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y&source=post_page---------------------------)**.**

You can find me on [Medium](https://medium.com/@cristiansalcescu) and [Twitter](https://twitter.com/cristi_salcescu).

