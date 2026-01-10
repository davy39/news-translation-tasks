---
title: How to keep your JavaScript code simple and increase its readability
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-14T12:34:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-keep-your-javascript-code-simple-and-increase-its-readability-94d6a949afc4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XsmvUvDELQVWAl3zhTvvlQ.jpeg
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Leonardo Lima

  After a few years working almost exclusively with Ruby on Rails and some jQuery,
  I changed my focus to front-end development. I discovered the beauties of JavaScript
  ES6 syntax and the exciting modern libraries such as React and Vue....'
---

By Leonardo Lima

After a few years working almost exclusively with Ruby on Rails and some jQuery, I changed my focus to front-end development. I discovered the beauties of JavaScript ES6 syntax and the exciting modern libraries such as React and Vue. I started to implement new features using nothing but ES6 Vanilla JavaScript, and fell instantly in love with all this new class abstraction and those arrow functions.

Nowadays, I’m generating large amounts of JavaScript code. But, since I consider myself a JavaScript Padawan, there’s yet a lot of room for improvement. Through my studies and observations, I’ve learned that even with the use of syntactic sugars featured in ES6, if you don’t follow the main principles of [SOLID](https://hackernoon.com/solid-principles-made-easy-67b1246bcdf), your code has a high chance of becoming complex to read and maintain.

To demonstrate what I’m talking about, I’ll walk you through one fantastic Code Review session I had last week with a [buddy](https://github.com/anderson06) of mine. We are going to start with a 35-lines JavaScript Class and will finish with a beautiful 11-lines code piece using only slick functions. With patience and resilience, you will be able to observe and apply the pattern to your own codebase.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2Dp7SafVzM24sQg_6YrmfA.gif)
_Refactoring process featured in this arcticle_

### The feature

What I needed to do was quite simple and trivial: get some information from the page and send a request to a third-party tracking service. We were building an event tracker on the client side and tracking some page actions along with it.

The code examples below implement the same task using different code design tactics.

#### Day 1 — Using ES6 Class syntax (aka Object Prototype Pattern wrapper)

You can notice above that I started smart: isolating the generic tracker `SuccessPlanTracker` to be reused in another page besides the Empty Index.

But, wait a minute. If this is an empty index tracker, what on earth is this foreigner `TrackNewPlanAdd` doing there?

#### Day 2 — Getting rid of Class boilerplate code

Okay, now the file name clearly reflects the feature responsibility and, look at that, there is no more `EmptyIndexTracker` class giving us less boilerplate code. Learn more [here](https://gist.github.com/indiesquidge/f8c486795d7dd455c0327ce7e0aa8c16) and [here](https://www.accelebrate.com/blog/javascript-es6-classes-and-prototype-inheritance-part-1-of-2/). We are using simple functions variables and, man, what a good catch using those shining [ES6 Object Spread](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_operator) dots.

I find out that the [querySelectorAll](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelectorAll) method already returns a List, so we are able to remove the `Array.from()` function from `Array.from(document.getElementsByClassName('js-empty-index-tracking')) `.` Remember that [getElementsByClassName](https://developer.mozilla.org/en-US/docs/Web/API/Element/getElementsByClassName) method returns an object.

Also, since the central responsibility is to bind HTML elements, the `document.addEventListener('DOMContentLoaded')` function invocation doesn’t belongs to the file anymore.

Good job!

#### Day 3 — Removing ES5 old practices and isolating responsibilities even more.

If you pay close attention, there is no `SuccessPlanTracker` class in the code above — it suffered the same fate as the old `EmptyIndexTracker`. The class-killing mindset, once installed, spreads and multiplies itself. But don’t fear, my good lad.

Remember, always try to keep your JavaScript files simple. There is no need to know about the states of class instances, and the classes were exposing practically only one method.

Don’t you think using the ES6 class abstraction was a little bit of overkill?

Did you also notice that I removed the variables instances from the top of the file? This practice remounts to ES5, and we don’t need to worry so much about it now that we have ES6+ syntax.

Finally, the last major change in this third version. Our empty index tracker binder now does only one thing: elements binding.

Following those steps brought the code very close to the Single Responsibility Principle — one of the most important SOLID principles.

#### Day 4 — Avoiding DOM sloppy manipulation

Hey, there are more lines now, you liar!

The thing is that our third version was a little broken. We were inappropriately mutating DOM Elements datasets in the line `properties.emptyIndexAction = button.dataset.trackingIdentifier;`.

The property of one button was being passed to another button, generating messed up tracking events. To solve this situation, we removed the responsibility of assigning the `emptyIndexAction` property from the binding loop to a proper function by creating its own scoped method `trackAction()`.

By adding those extra lines, we improved our code, better encapsulating each action.

#### Finally, to wrap up and write down

* If you want to design and write marvelous pieces of code, you need to be willing to explore further and go beyond the limits of a proper and modern syntax.
* Even if the first version of your code ended up being simple and readable, it doesn’t necessarily mean that the system has a good design or that it follows at least one of the [SOLID](https://hackernoon.com/solid-principles-made-easy-67b1246bcdf) principles.
* It’s essential to accept constructive code reviews and let other developers point out what you can do better.
* To keep your code simple, you need to think bigger.

Thank you very much for reading the article. Have another refactoring example or code review lesson to share? Please drop a comment below! Also, you can help me share this message with others by clapping and sharing it.

**ProTip to-go**: Here’s a very useful ES6 (ES2015+) [cheatsheet](https://devhints.io/es6)

_*Cheers to [@anderson06](https://github.com/anderson06) for being such a good code ‘pal giving me awesome feedbacks._

