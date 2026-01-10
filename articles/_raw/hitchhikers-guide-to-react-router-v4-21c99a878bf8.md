---
title: 'The Hitchhiker’s Guide to React Router v4: recursive paths, to infinity and
  beyond!'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-08T13:14:22.000Z'
originalURL: https://freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-21c99a878bf8
coverImage: https://cdn-media-1.freecodecamp.org/images/0*lXTz6U5B8ySl0skc
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Eduardo Vedes

  Welcome to the third part of the Hitchhiker’s Guide to React Router v4. In this
  article we’re going to focus on recursive paths. If you’ve missed the first two
  parts, you can find part 1 here and part 2 here.

  What are recursive paths...'
---

By Eduardo Vedes

Welcome to the third part of the Hitchhiker’s Guide to React Router v4. In this article we’re going to focus on recursive paths. If you’ve missed the first two parts, you can find part 1 [here](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-a957c6a5aa18/) and part 2 [here](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-4b12e369d10/).

### What are recursive paths?



Recursive paths are nothing more than paths that are composed of nested routes that render the same component to show nested views.

**Example:** `http://evedes.rockz/Topics/1/2/3/2/1`

It’s commonly used to do “breadcrumbs” in websites — a navigation pattern that shows where the user is in a site organic structure, a social network friends relationship tree, solve a lot of complex graph problems, analytics, or trace any kind of information that depends on the last path. This can be the case, for example, of a computer game where you go from one room to another and the path you took to get there needs to be tracked for some reason.

Excited? Say “yeah”! ?

So, let’s do some changes in our application to test this pattern applied in React Router v4.

### The Objective



So, the idea here is to transform our Topic List.

Instead of having a list of Topics that are matched and that the user can navigate to and see each Topic Detail and get back (seen in [Part I](https://medium.freecodecamp.org/hitchhikers-guide-to-react-router-v4-a957c6a5aa18) of this guide), let’s do a nested route that starts at Topic 1 and shows the user which Topics are related to it — by showing a list of Links which can be clicked to navigate to the next related Topic Detail. Each time you choose a topic, you can navigate to it, see it’s details, and see which topics are related to it.

### routes.js

![Image](https://cdn-media-1.freecodecamp.org/images/olKeKVQse2SAHuFm3EhWOXHR58bT0sBPsD6Z)
_routes.js_

So in **routes.js** we’ve deleted the import of the **TopicDetails** component and corrected the routes to render the **TopicList** component when the path is **/Topics/:topicId**, besides the existing **Route** to **/Topics**.

Both will render the same component with different match properties.

### TopicList.js



Besides the small correction above, I’ve heavily refactored the **TopicList.js** file. Let’s have a look at what we have there:

![Image](https://cdn-media-1.freecodecamp.org/images/TjrHUIdtieZDPOCHLv3e4us0G7OaHyMgRs68)
_fig 1.-imports and const definitions_

We’ve imported **Route** and **Link** from the **react-router-dom** package because we’re going to invoke it later in the code.

We’ve created an array of objects which contains the list of topics. Each topic has a **relatedTopics** array that promotes the relationship among them.

We’ve created a **find** function that receives the topic’s id as an argument and returns the item or topic that corresponds unequivocally to the id passed into it.

The **parseInt(id, 10)** usage makes sure that even if the argument passed into the **find** function is a string, it becomes an integer on the base 10 (decimal number system).

Observe that our topics **id** and **relatedTopics** values are primitive integers.

To learn more about **parseInt** take a look [HERE](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt).

![Image](https://cdn-media-1.freecodecamp.org/images/bd3vrUgWPZrDDw7o2WsuOO14as9VFlHS4Jqs)
_fig.2-TopicDetail stateless Component_

The component **TopicDetail** starts by defining the variable **topic**. This will store the result of the function **find** which grabs the **id** that comes from the **match** object (router) when the component is invoked. It then returns the **topic** object that corresponds to that **id**.

With that **topic** object stored, it returns the **Details** of the topic and creates a dynamic unordered list with the related topics **id** and **name**.

Let’s see this in the browser:

![Image](https://cdn-media-1.freecodecamp.org/images/3xH6KmVJ6-OZkNAZBBABE65iZ8ViYFr784Ab)
_**Topic 1 Details (Info and Related Topics)**_

Nice! It’s working!

So, when you click one of the links shown, it routes you to the next topic **id**:

![Image](https://cdn-media-1.freecodecamp.org/images/JEBsBuYFBBdKTMjr0NjHe3RMNYjGPhDxaNzu)
_**Route to be invoked inside the TopicDetail Component**_

Wow! This route is outside of the **routes.js** file! This is new. Observe that technically you can create routes inside any component.

Do not forget that **isExact** is false because the **url** doesn’t entirely match the path from the **/Topics/:topicId** as previously defined in the **routes.js** component.

![Image](https://cdn-media-1.freecodecamp.org/images/tubC6XVUSQmFdxIu7-QmfYcqaZnM4QYrYXj2)
_**fig.3-TopicList stateless Component**_

In the end, we define and export the **TopicList** component which invokes **TopicDetail** with the match object above. But, as in each instance of **TopicDetails** when you’re triggering a **Route**, **TopicDetail** gets re-rendered with new **match** properties supplied by the **Router** at each instance.

So now we are done! ?

### Last but not least

I think that by this time you already have a good idea on how to start implementing recursive routes.

I’ve chosen this example because it’s easy to understand and very useful for some basic stuff.

The changes I’ve made to the application, to produce this article, can be found in my GitHub [repo](https://github.com/evedes/ReactRouter_BoilerPlate_03).

### Bibliography

To make this article, I’ve used the React Router documentation that you can find [here](https://reacttraining.com/react-router/core/guides/philosophy).

All the other sites I’ve used are linked along the document to add info or provide context to what I’ve tried to explain to you.

This article is part 3 of a series called “Hitchhiker’s Guide to React Router v4”

* **[Part I: Grok React Router in 20min](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-a957c6a5aa18/)**
* **[Part II: [match, location, history] — your best friends!](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-a957c6a5aa18/)**
* **[Part IV: route config, the hidden value of defining a route configuration array](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-c98c39892399/)**

? Thank you very much!

