---
title: React-cache, time slicing, and fetching with a synchronous API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-11T16:58:56.000Z'
originalURL: https://freecodecamp.org/news/react-cache-time-slicing-and-fetching-with-a-synchronous-api-2a57dc9c2e6d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*h8d-4wYLN9wwiEsLAA_5yg.jpeg
tags:
- name: Browsers
  slug: browsers
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Marvin Frachet

  Well, this year seems to be the year of React. You’ve probably heard of the new
  killer feature that is coming with the 16.7-alpha.0 — Hooks. You’ve probably also
  heard about some other great and cool stuff like Time Slicing or even ...'
---

By Marvin Frachet

Well, this year seems to be the year of React. You’ve probably heard of the new killer feature that is coming with the 16.7-alpha.0 — Hooks. You’ve probably also heard about some other great and cool stuff like Time Slicing or even Suspense.

This article **doesn’t** aim at describing how to use some of the new features but rather at proving how they may have been built. Just for the sake of understanding what we are playing with.

It’s also written in the way I have discovered the feature. It’s probably not the way it has been thought up, but this is how I got the points.

What you’ll find while reading:

* Async JavaScript and the event loop
* Algebraic Effects in React, with example
* Fiber and React Phases

### Why did I write this post?

What made me want to write this post was this special, and experimental, feature that allows the use of **asynchronous** operations using a **synchronous** API:

`const bulbasaur = ApiResource.read()`?… What the? **Synchronous**?!

The [react-cache](https://github.com/facebook/react/tree/master/packages/react-cache) library creates the ability to use asynchronous operations with a synchronous API. This is the feature that made me want to learn how React is working under the hood. Here’s a presentation by presented by [Dan Abramov](https://twitter.com/dan_abramov) and [Andrew Clark](https://twitter.com/acdlite) on this library:

How is that even possible? How can we get some remote data using synchronous calls?

Let’s deep dive into this example and try to understand how [react-cache](https://github.com/facebook/react/tree/master/packages/react-cache) implements such a functionality and discover how it can work. This story starts with the [fiber architecture](https://github.com/acdlite/react-fiber-architecture).

### Controlling JavaScript operations

Fiber architecture allows React to take control over task executions. It has been built to solve multiple problems that React suffered from. Here are the two that caught my attention:

* prioritising over specific events, like user input over data fetching
* asynchronously splitting React computation to retain the main thread availability and to avoid to block it during long rendering processes

Everything that triggers a state change — not only with React — inside a JavaScript application is due to asynchronous operations. These include `setTimeout` , `fetch` , and listeners for events.

Asynchronous operations are managed through multiple JavaScript core concepts:

* tasks (micro, macro, render etc…)
* event loop
* callstack

If you’re not familiar with these concepts, I suggest you take a look at this video by [Jake Archibald](https://twitter.com/jaffathecake):

Thanks to fiber, user inputs are **resolved** before other asynchronous operations such as fetch calls.

How is this even possible?

Well, Archibald’s talk above was the first paved stone of my own path of learning about how event loop works. He says that micro tasks — generated through the Promise API, for example — are executed and flushed **before** the next macro task. This process uses callback-based methods like `setTimeout`.

So, if you remember my “user input versus fetching data” comparison, how did the team make `fetch` resolutions **after** `onChange` resolutions?

None of these concepts fit in the same spec, [WhatWG](https://fetch.spec.whatwg.org/) / [HTML5](http://w3c.github.io/html/webappapis.html#dom-globaleventhandlers-onclick) / [Ecma-262](https://www.ecma-international.org/ecma-262/6.0/#sec-promise-objects), and are provided from different places like the browser or JS engines.

I mean, how are we supposed to resolve a `Promise` after a `setTimeout`?

This sounded absolutely crazy to me and it was really hard to get an idea of how it could be working. The fact is that it takes place in a higher level.

Later, I watched the incredible talk from [Brandon Dail](https://twitter.com/aweary) at React Rally. This presents the new [Time Slicing and Suspense features](https://www.youtube.com/watch?v=nLF0n9SACd4) that have been shipped thanks to the React fiber architecture:

According to Dail, fiber is just like the usual JavaScript callstack where each item in the stack is called a **fiber**. It is different to the callstack that relies on **frames** which represent **functions (+ metadata).** Rather, a fiber represents a **component (+ metadata)**. Let’s see a fiber as a huge box around a component that knows everything about it.

There is an important difference between these two concepts.

On the first hand, the callstack is a functionality that has been built on top of the **native part driving** **JavaScript Code**. It aims to stack every JavaScript function call, and run them on their own. Each time we call a function it’s added to the stack. Without the callstack, we wouldn’t be able to have clear and detailed error stacktraces. And since the callstack is not reachable from a JavaScript code, it’s really difficult and even impossible to take control over it.

On the other hand, fibers — like a stack of fiber — represent the same concept, but built in **JavaScript code.** The tiniest unit is not functions, but a component**.** It actually runs in a JavaScript universe.

The fact that the fiber architecture is completely built in JavaScript means that we can use it, access it, and modify it. We can work on it using standard JavaScript.

What has driven me in the wrong direction was that I thought React was using a workaround to cut-off the internal way JavaScript is working. **It’s not the case**. Fibers are simply JavaScript objects that own information about React components and that can interact with their lifecycles. It can only act on React internal functionalities.

The idea is **not** to redefine how JavaScript should be working, like telling that `fetch` microtask resolution should be executed before callback tasks. It’s more on which React methods **should be called or not** in a specific context, like interrupting the different lifecycle method calls.

Hey wait! You say that fibers can control absolutely everything in a React App? But how can a component tell React to stop doing anything?

### Algebraic effects, yes, but in JavaScript please

React is able to control components, and to know if a component is running, thanks to the fiber architecture. What is missing now is a way to tell React that something has changed for a specific component, so it will handle this change.

This is where **algebraic effects** enter the game.

Algebraic effects are not something that exist in JavaScript. I will try to explain what they are with a higher level explanation.

Algebraic effects are a concept that allows to send some information somewhere, a bit like a dispatcher. The idea is to call a specific function that will **interrupt** the currently running function at a precise position to let a parent function handle a computation. When the parent computation finishes, it can resume the program to the initial position where the information has been sent.

Some languages such as [OCaml](http://ocamllabs.io/doc/effects.html) or [Eff](https://www.eff-lang.org/) benefit from these feature natively. This is a really interesting abstraction since the implementation details only rely upon the parent:

Wouldn’t it be awesome to have such a feature in JavaScript?

The React team has created a similar approach in a React context dealing with the JavaScript `try/catch` block. According to Dail, it’s the closest available concept in JavaScript.

Throwing something allows sending information to a parent, somewhere. The first parent who catches the information is able to deal with it and make computations on it.

#### An example is better than a thousand words

Imagine the following code that tries to fetch Bulbasaur **using a synchronous API**:

This piece of code may be weird since it’s not really common to fetch data using a synchronous API. Let’s jump inside the `customFetch` function implementation:

Oh wait! This absolutely doesn’t look like a fetch! I don’t get what this function aims to do at all…

Well, imagine something **around the component**, let’s say a fiber that looks like:

Take some time to read the code.

Now, let’s jump to the `customFetch` implementation:

The important part in the previous snippets is the `try/catch` block.

Let’s sum up what’s happening through these different pieces of code:

* The `Pokemon` component calls the `customFetch` method.
* The `customFetch` method tries to read its internal cache, but it’s empty. So it throws something / somewhere — algebraic effects.
* The `fiber` parent catches that information, handles it, and fetches the data. Then it populates the `customFetch` cache with the data.
* A re-render occurs in `Component(args)`and, now, the `customFetch` cache is full. The data is now available in the component using a synchronous API.

[Take a look at the `react-cache` implementation details and check the different throws.](https://github.com/facebook/react/blob/d14ba87b1bfed76900d6d25722f069003561e2e3/packages/react-cache/src/ReactCache.js#L158)

Something may have caught your attention during this process: `render` has been called twice. One for throwing the error — **pausing** the component — and one for getting the data — **resuming** the component. It’s okay with React to trigger multiple `render` calls since it’s solely a pure function — it doesn’t have any side effects on its own.

Wait… What? `render` doesn’t have any side effects? What about the DOM?

### React phases

If you’ve been working with React for a long time, you may have heard that it’s not a good practice to re-render multiple times. Before fiber architecture, every time we were calling the render function React was making some internal computations and then modified the DOM accordingly. For example, this happened when calling the render function through `setState`. The process was inlined:

`setState` →`render` → compare Virtual Nodes → update the DOM nodes

Dealing with fiber, the process is a bit different. It has introduced a concept of queue and batches that allows high performance DOM modifications.

The idea is quite simple. We assume that screens can run ~60 frames per second. From this assumption, and using the available JavaScript functions, it’s possible to make some computations and DOM modifications only every ~16.7ms. With fiber, React can enqueue multiple modifications and commit them about 60 times per second.

This kind of modification has allowed React to split into three phases with their own advantages and particularities:

![Image](https://cdn-media-1.freecodecamp.org/images/1*YPcEsrQ0f5qjGP-a5oVj7A.png)
_[Dan Abramov concerning React phases](https://twitter.com/dan_abramov/status/981712092611989509/photo/1?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E981712092611989509&amp;ref_url=https%3A%2F%2Fmedium.com%2Fmedia%2Fbda1c34a16e9f8a8e3eb244716a1da72%3FpostId%3D2a57dc9c2e6d" rel="noopener" target="_blank" title=")_

* The render phase is pure and deterministic. It has no side effects and the different functions that it’s composed of can be called multiple times. The **render phase is interruptible** — it’s not the `render` function that is in pause mode, but the whole phase
* The pre-commit phrase aims to provide access to the actual DOM state, like the scrollbar positions, in read mode.
* The commit phase actually modifies the DOM and **is not interruptible**. React can’t pause during that phase.

This set of three phases has introduced the Time Slicing capabilities. React is able to pause during the render phase, in between two component function calls, and to resume that phase when necessary.

In fiber, `render` only aims to **get the latest available representation** of a component based on its internal state to make some comparisons and know if React has to change the DOM or not. If a commit modification is required, it will add the modification to a “work in progress” queue.

The React team has made huge performance improvements thanks to React Concurrent (Time Slicing + Suspense) and the fiber architecture. They have created workarounds to counter different browser problems like event prioritisation and concurrency.

If we take a step back, isn’t that what they have shown? Prioritisation seems to be the new challenge for browser and front-end frameworks.

Other teams are also working on improving the actual state of the art and even propose future APIs. This is Google’s take:

