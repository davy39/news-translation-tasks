---
title: A Javascript quirk that will catch you out
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-23T15:14:38.000Z'
originalURL: https://freecodecamp.org/news/a-javascript-quirk-that-will-catch-you-out-7895dfbae657
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VmGTvNbFTD3HrCJbyrtTeg.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By William Woodhead

  This piece describes a feature that good Javascript developers should know. And
  once you have read this piece, you can pretend you have known about it for ages
  like me.

  Note: If you are not a Javascript developer, this might be a ...'
---

By William Woodhead

This piece describes a feature that good Javascript developers should know. And once you have read this piece, you can pretend you have known about it for ages like me.

**Note:** If you are not a Javascript developer, this might be a little tricky to get your teeth into. If you are, then buckle up for an extremely short ride.

It’s all to do with _copying_ variables (or cloning, hence the sheep).

Let’s dive straight in.

### **Copying strings**

Let’s do a quick bit of coding:

```
var initialName = ‘William’;
```

```
var copyName = initialName;copyName = ‘Bill’;
```

```
console.log(initialName);   // prints ‘William’console.log(copyName);      // prints ‘Bill’
```

This all seems expected. We copy **initialName** and then change its value. **initialName** prints **_‘_William’** and **copiedName** prints ‘**Bill’**.

So far so good. Let’s try the same exercise with objects instead of strings. (_Expect the unexpected_)

### Copying Objects

```
var initialObject = { name: ‘William’ };
```

```
var copyObject = initialObject;copyObject.name = ‘Bill’;
```

```
console.log(initialObject.name);   // prints ‘Bill’console.log(copyObject.name);      // prints ‘Bill’
```

Hmmm, here is the issue. When we print the name of **initialObject**, it has changed to **Bill**.

So what has happened here?

When we set the **name** in **copyObject,** it also changed the **name** in the **initialObject**. This is because objects are copied _by reference_. **copyObject** is just a reference to the underlying data.

So when we change the **name** in **copyObject**, it also changes the **name** in the **initialObject** because it is referencing the same bit of underlying data.

### Where you might get caught out

In large applications, this could result in parts of your data structures effectively being in multiple places at the same time.

So if you alter an object in one part of your application code, you might be changing it elsewhere. This can sometimes cause undesired behaviour (like re-rendering) and may be difficult to debug and isolate.

Although this seems really simple, in complex web apps using popular frameworks, this simple base-level issue can cause severe headaches for developers.

#### Redux/React example

An example of where I have seen developers get caught by this again and again is in [Redux action creators](https://redux.js.org/docs/basics/Actions.html#action-creators) where you manipulate state before dispatching actions. By manipulating the object that is passed to the action creator without cloning it, you can actually change underlying state, or react component state before your dispatch.

### Our solution

There are many libraries that provide cloning functions for objects and arrays, for example, Lodash.

At [pilcro](https://www.pilcro.com/?utm_source=medium&utm_medium=jsquirk&utm_campaign=awareness) we use [Facebook’s Immutable.js](https://facebook.github.io/immutable-js/) to avoid this issue. Even though it is a large library, it enables our developers to write predictably functional javascript and avoid this pitfall. I couldn’t recommend it more.

So there we have it, a very simple but important feature to know about in Javascript. If you aren’t a Javascript developer, kudos for getting to the end.

If you _are_ a senior Javascript developer and this was news to you, you should feel like this:

![Image](https://cdn-media-1.freecodecamp.org/images/c4C35c05ok6vxcah56o39Yxdc3jpjiq0--sz)
_giphy_

_If you liked this story, please ? and please share with others. Also please check out my company at p[ilcro.com.](https://www.pilcro.com/?utm_source=medium&utm_medium=jsquirk&utm_campaign=awareness) Pilcro helps startups stay brand-consistent across all their different marketing channels. You will love what we are up to!_

