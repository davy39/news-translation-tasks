---
title: Node.js module.exports vs. exports
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-07T14:15:39.000Z'
originalURL: https://freecodecamp.org/news/node-js-module-exports-vs-exports-ec7e254d63ac
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb7b4740569d1a4cae663.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By lazlojuly

  What are they, how to use them and how not to use them

  (Note that this article was written after the Node.js 6.1.0 release)

  TL;DR


  Think of module.exports as the variable that gets returned from require(). It is
  an empty object by defaul...'
---

By lazlojuly

#### What are they, how to use them and how not to use them

(Note that this article was written after the Node.js 6.1.0 release)

#### **TL;DR**

* Think of module.exports as the variable that gets returned from require(). It is an empty object by default, and it is fine to change to anything.
* Exports? Well, “exports” itself is never returned! It is just a reference to module.exports; a convenience variable to help module authors write less code. Working with its properties is safe and recommended.

```
exports.method = function() {…} 
```

```
vs.
```

```
module.exports.method = function() {…}
```

### A simple module example

First, we need an example codebase. Let’s start with a simple calculator:

Usage:

### The module wrapper

Node.js **internally wraps** all require()-ed modules in a function wrapper:

### The module object

Variable “**module**” is an object representing the current module. It **is** **local to each module** and it is also private (only accessible from module code):

### Module.exports

* **It is the object reference that gets returned from the require() calls.**
* It is automatically created by Node.js.
* It is just a reference to a plain JavaScript object.
* It is also empty by default (our code attaches an “add()” method to it)

There are two ways we can use module.exports:

1. **Attaching public methods** to it (like we did in the calculator example).
2. **Replacing** **it** with our custom object or function.

Why replace it? When replacing, we can return any arbitrary instance of some other class. Here is an example written in ES2015:

Above, “calculator-base” exports a class.  
Let’s extend “Calculator” class and export an instance this time:

Usage:

### Exports alias

* **“exports” is just a convenience variable so module authors can write less code**
* Working with its properties is safe and recommended.   
(eg.: exports.add = function…)
* **Exports** is NOT returned by require() (module.exports is!)

Here are some good and some bad examples:

**Note:** It is common practice to replace module.exports with custom functions or objects. If we do that but still would like to keep using the “exports” shorthand; then “exports” must be re-pointed to our new custom object (also done in code above at line 12):

```
exports = module.exports = {}
```

```
exports.method = function() {...}
```

### Conclusion

A variable named **exports** that is not being entirely exported is confusing, especially for newcomers to Node.js. Even the official documentation has a slightly strange take on it too:

> As a guideline, if the relationship between exports and module.exports seems like magic to you, ignore exports and only use module.exports.

My take is that code is not magic. Developers should always seek deeper understanding of the platforms and languages they use. By doing so; programmers gain valuable confidence and knowledge which in turn positively impacts code quality, system architecture and productivity.

Thank you for reading my post. Feedback and thoughts are always welcome in the comments section.

[lazlojuly](https://twitter.com/lazlojuly)

#### Related Articles:

* [Are Node.js modules singletons?](https://medium.com/@lazlojuly/are-node-js-modules-singletons-764ae97519af)

#### Sources:

* [Node.js Documentation on Modules](https://nodejs.org/api/modules.html)

**Checkout my new blog series on unit unit testing:**

[**How to get started with Unit Testing? Part #1**](https://medium.com/@lazlojuly/how-to-get-started-with-unit-testing-part-1-7f490bbf560a)  
[_I guess many of us can relate to a situation depicted above._](https://medium.com/@lazlojuly/how-to-get-started-with-unit-testing-part-1-7f490bbf560a)  
[_A place where, unit testing is considered as a chore._medium.com](https://medium.com/@lazlojuly/how-to-get-started-with-unit-testing-part-1-7f490bbf560a)

