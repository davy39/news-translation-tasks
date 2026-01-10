---
title: Learn the fundamentals of functional programming — for free, in your inbox
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-20T16:24:44.000Z'
originalURL: https://freecodecamp.org/news/learning-the-fundamentals-of-functional-programming-425c9fd901c6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Zy10ES24gQ6soFqjRNpZVg.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: learning to code
  slug: learning-to-code
- name: 'self-improvement '
  slug: self-improvement
seo_title: null
seo_desc: 'By Preethi Kasireddy

  If you’re a software developer, you’ve probably noticed a growing trend: software
  applications keep getting more complicated.

  It falls on our shoulders as developers to build, test, maintain, and scale these
  complex systems. To d...'
---

By Preethi Kasireddy

If you’re a software developer, you’ve probably noticed a growing trend: **software applications keep getting more complicated.**

It falls on our shoulders as developers to build, test, maintain, and scale these complex systems. To do so, we have to create well-structured code that is easy to understand, write, debug, reuse, and maintain.

But actually writing programs like this requires much more than just practice and patience.

In my upcoming course, _Learning Functional JavaScript the Right Way_, I’ll teach you how to use functional programming to create well-structured code.

But before jumping into that course (and I hope you will!), there’s an important prerequisite: building a strong foundation in the _underlying principles of functional programming_.

So I’ve created a new [free email course](https://preethikasireddy.typeform.com/to/yC9qQr) that will take you on a fun and exploratory journey into understanding some of these core principles.  
   
Let’s take a look at what the email course will cover, so you can decide how it fits into your programming education.

### What is functional programming?

So. What is “functional programming,” exactly?

Functional programming isn’t a framework or a tool, but a _way_ of writing code. In functional programming, we place a major emphasis on writing code using **functions as “building blocks.”**

Your program is defined in terms of one main function. This main function is defined in terms of other functions, which are in turn defined in terms of still more functions — until at the bottom level the functions are just language primitives like “number” or “string.”

![Image](https://cdn-media-1.freecodecamp.org/images/AziWGQ2dGtkvzvUL0v1RIWwIJu6V-h6W7c-e)

If you’re reading this thinking, _“Hmm, but wait? Doesn’t every language use functions to write code?”_ then good ?. It means you’re paying attention.   
  
You’re right — every programming language has functions. But functional programming takes it to a **whole ‘nother level ?**

![Image](https://cdn-media-1.freecodecamp.org/images/UDgSl91kyBG7odfIYdysSd-StB-rNoXxcCjw)
_Functions to a whole ‘nother level_

To understand what I mean, let’s rewind and start with the basics.  
  
Every software program has two things:

1. Behavior
2. Data

When we’re learning about a programming paradigm — like functional programming — it’s often helpful to consider how the paradigm approaches behavior and data respectively.   
   
**Behavior**, for example, is handled purely using functions in functional programming.   
   
**Functions** are “self contained” pieces of code that accomplish a specific task. It defines a relationship between a set of possible inputs and a set of possible outputs — they usually take in data, process it, and return a result. Once a function is written, it can be used over and over and over again.  
   
**Data** is, well, data. In functional programming, data is immutable — meaning it can’t be changed. Rather than changing data they take in, functions in functional programming take in data as input and produce **new** values as output. Always.   
   
Functions and immutable data are the only two things you need to ever deal with in functional programming. To make it even simpler, functions are treated no differently than data.

Put another way, **functions in functional programming can be passed around as easily as data.** You can refer to them from _constants_ and _variables_, pass them as _parameters_ to other functions, and return them as _results_ from other functions.   
   
This is the most important thing to understand when approaching functional programming.

![Image](https://cdn-media-1.freecodecamp.org/images/oqb79dext6W9vY7dpo80KccktAKfwUgHp8U-)

By treating functions as nothing more special than a piece of data and by only using data that is immutable, we are given a lot more freedom in terms of how we can use functions.

Namely, it allows us to create small, independent functions that can be reused and combined together to build up increasingly complex logic. We can **break any complex problem down into smaller sub-problems, solve them using functions, and finally combine them together to solve the bigger problem.**   
   
Considering the ever-growing complexity of software applications, this kind of “building-block” approach makes a huge difference in keeping programs simple, modular, and understandable. This is also why developers strive to make their functions as **general-purpose** as possible, so that they can be **combined** to solve large, complex problems and **reused** to speed up development time for subsequent programs.

![Image](https://cdn-media-1.freecodecamp.org/images/vE7OgoYjLrRIs1QUL3dmD-QHmwvwfYijiMUD)
_Function composition_

Ultimately, the reason that functions are so powerful in functional programming is because the functions follow certain core tenets. Those tenets will be the subject of my email course:

* Functions are pure
* Functions use immutable data
* Functions guarantee referential transparency
* Functions are first-class entities

After that, I’ll briefly touch on how functional programming applies these tenets to encourage us to think carefully about our data and the functions that interact with it.

By the end, you’ll be able to understand how this approach leads to code that is:

* Easier to understand (that is, “expressive”)
* Easier to reuse
* Easier to test
* Easier to maintain
* Easier to refactor
* Easier to optimize
* Easier to reason about

Sound exciting? Come along for the ride!

[Sign up for the free email course now](https://preethikasireddy.typeform.com/to/yC9qQr). Then you’ll receive the first lesson in your inbox within 1–3 days of signing up ?

