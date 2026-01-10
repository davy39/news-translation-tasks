---
title: What we really mean when we talk about prototypes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-14T00:26:41.000Z'
originalURL: https://freecodecamp.org/news/what-we-really-mean-when-we-talk-about-prototypes-165586f29fa9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5dxjDGWBfN796dwrZcVHaw.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Hayden Betts

  Beginning JavaScript devs often mistakenly use one word — “prototype” — to refer
  to two different concepts. But what exactly is the difference between an “object’s
  prototype” and the “prototype property” of JavaScript functions?


  But ...'
---

By Hayden Betts

Beginning JavaScript devs often mistakenly use one word — “prototype” — to refer to two different concepts. But what exactly is the difference between an “object’s prototype” and the “prototype property” of JavaScript functions?

![Image](https://cdn-media-1.freecodecamp.org/images/1*L04gw3FTaj-fQE6b-bY2Ug.png)
_But why…?_

I thought I understood the concept of “prototypes” and prototypal inheritance in JavaScript. But I continued to find myself confused by references to “prototype” in code and in the documentation.

A lot of my confusion disappeared when I realized that **in writing about JavaScript, people often casually use “prototype” to** **describe two _distinct but related_ concepts.**

1. **An object’s prototype**: The template object from which another JavaScript object inherits methods and properties. ([MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes))
2. **The [non-enumerable](https://stackoverflow.com/questions/17893718/what-does-enumerable-mean) `prototype`property on JavaScript functions**: _A convenience to facilitate a design pattern_ (that design pattern to be explained in-depth shortly!)_._   
Not meaningful in itself until deliberately set to have some inheritance-related function. Most useful when used with constructor functions and factory functions (explanation coming!). Though all JS functions have the property by default. Contains a `constructor` property, which refers to the original function.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Vmv0NSt-8jA_qOcbPuCzxA.png)
_Even trivial functions have a prototype property by default._

For a long time, I was comfortable with definition 1, but not with definition 2.

### Why does this distinction matter?

Before I understood the difference between “an object’s prototype,” and the “non-enumerable `prototype`property on functions,” I found myself confused by expressions like the following:

```
Array.prototype.slice.call([1, 2], 0, 1);// [ 1 ]
```

_(sidebar: the first — but not the only — step to understanding the above is understanding `call()`. Here’s a quick [refresher](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call) just in case!)_

A question I was not previously able to answer:

* “Why are we looking for `slice` in the `Array` constructor’s prototype? Shouldn’t the `Array` constructor itself contain the `slice` method, and its prototype just contain some really low-level methods that all objects share?”

These questions were totally cleared up as I came to understand the design pattern that the `prototype` property on `Array` constructor functions exists to enable.

### 3 steps to understanding the prototype property on JS Functions

In order to understand the`prototype` property on JS functions, you need to understand the design pattern it enables. I will build up an understanding of this pattern by first working through two less preferable alternatives.

#### Implementation 1: The Functional Class Pattern

Imagine we want to create a game in which we interact with dogs. We want to quickly create many dogs that have access to common methods like **pet** and **giveTreat.**

We could start to implement our game using the [Functional Class Pattern](https://www.thegreatcodeadventure.com/javascripts-functional-class-pattern/) as follows:

Let’s clean this up a bit by storing those methods in their own object. Then extend them inside of the `createDog` factory function.

Though this implementation is easy to reason about, and conveniently reflects class-based-inheritance in other languages, it has at least one major issue: we are copying our method definitions to every dog object we create using our factory function`createDog`.

This takes up more memory than necessary and is not [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself). Wouldn’t it be nice if instead of copying method definitions to `zeus` and `casey`, we could define our methods in one place. Then have `zeus` and `casey` point to that place?

#### Refactor 1: Implementing a “Prototypal Class” Design Pattern

Prototypal inheritance gives us exactly what we asked for above. It will allow us to define our methods in one prototype object. Then have `zeus`, `casey`, and infinitely more objects like them point to that prototype. `zeus` and `casey` will then have access to all of the methods and properties of that prototype by reference.

> _NOTE: For the less familiar, there are [many](https://guide.freecodecamp.org/javascript/prototypes/) [excellent](https://hackernoon.com/prototypes-in-javascript-5bba2990e04b) [tutorials](https://medium.freecodecamp.org/prototype-in-js-busted-5547ec68872) out there that explain the concept of prototypal inheritance in much more depth than I do here!_

> _A NOTE ON MY EXAMPLES BELOW: For pedagogical clarity, I use [factory function](https://stackoverflow.com/questions/8698726/constructor-function-vs-factory-functions)s named_ `createDog`_, rather than ES5 [constructor functions](https://stackoverflow.com/questions/8698726/constructor-function-vs-factory-functions), to implement a [prototypal model](https://medium.com/javascript-scene/3-different-kinds-of-prototypal-inheritance-es6-edition-32d777fa16c9) of inheritance. I choose to use factory functions because they have less ‘magic going on under the hood’ and ‘syntactic sugar’ than ES5 constructors. Hopefully, this makes it easier to stay focused on the issue at hand!_

Great! Now the objects corresponding to `zeus` and `casey` do not themselves contain copies of the methods `giveTreat` and `pet`. Instead, the objects look up those methods in their prototype`methodsForShowingAffection`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XDj8pysP_Qt6QUc94J7tWw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*fFxKUWpR7gkaIkoiHG4i3w.png)

But wouldn’t it be nice if `methodsForShowingAffection` were encapsulated in the `createDog` factory function? Doing so would make it clear that these methods are intended for use only with that function. So a simple refactor leaves us with:

#### Refactor 2: Prototypal Inheritance + the prototype property on factory functions

Great! But isn’t `methodsForShowingAffection` and long and strange name for a property? Why not use something more generic and predictable? It turns out that the designers of Javascript provide us with just what we are looking for. A built-in `prototype` property on every function, including one on our factory function`createDog`.

Note that there is nothing special about this `prototype` property. As shown above, we could achieve exactly the same result by setting the prototype of `createDog` to a separate object called `methodsForShowingAffection`. The normalcy of the`prototype` property on functions in Javascript suggests its intended use-case: a convenience intended to facilitate a common design pattern. Nothing more, nothing less.

**Further Reading:**

For more about the `prototype` property on functions in JavaScript, see ‘the function prototype’ section in [this](http://sporto.github.io/blog/2013/02/22/a-plain-english-guide-to-javascript-prototypes/) blogpost by [Sebastian Porto](https://www.freecodecamp.org/news/what-we-really-mean-when-we-talk-about-prototypes-165586f29fa9/undefined).

The MDN [article](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes) on prototypes.

