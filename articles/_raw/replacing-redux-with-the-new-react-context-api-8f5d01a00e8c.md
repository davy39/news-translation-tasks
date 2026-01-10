---
title: Replacing Redux with the new React context API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-25T20:34:43.000Z'
originalURL: https://freecodecamp.org/news/replacing-redux-with-the-new-react-context-api-8f5d01a00e8c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*G-vhFzhkTXo1cHSLY0y-rg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Didier FRANC

  The new context API that comes with React 16.3 is pretty neat. It was built in the
  render props style trending over these last months. Let’s explore it:

  It’s pretty nice right? Let’s go further with Flux-like implementation.

  What’s Fl...'
---

By Didier FRANC

The new context API that comes with React 16.3 is pretty neat. It was built in the _render props style_ trending over these last months. Let’s explore it:

It’s pretty nice right? Let’s go further with Flux-like implementation.

### What’s Flux ?

This talk from the excellent Jing Chen has revolutionized how we think about our applications today. If you want to know what Flux is as a concept, [take a look here](https://github.com/facebook/flux/blob/master/examples/flux-concepts/README.md).

![Image](https://cdn-media-1.freecodecamp.org/images/1*krW1XEfCCHg1eQFrPJMrqA.png)
_A basic Flux representation_

One library has democratized this concept: Dan Abramov’s [Redux](https://redux.js.org/basics) and its legendary time travel demo at React Europe 2015.

### Implementation

With the **createContext()** API example above, we already have the unidirectional **Store → View** in place.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Do6ERUrJHSj9Vmw0ngwIHg.png)

What we need is **actions** and **dispatchers** to dynamically update the store. What if our dynamic store was just the state of a root React component?

We have just passed state and actions as values of the provider. And now we can get it with **_<Consumer_** />.

I created a library to have everything we need to use this data flow easily while keeping great performance.

### [react-waterfall](https://github.com/didierfranc/react-waterfall)

![Image](https://cdn-media-1.freecodecamp.org/images/1*O6SqDvFqwhpqj9TUVzxFVw.png)
_Example repository available [**here**](https://github.com/didierfranc/react-stateful-example" rel="noopener" target="_blank" title=")_

Just import **initStore** from [**react-waterfall**](https://github.com/didierfranc/react-waterfall), set your **initial state,** and take some actions: **(state, …arg) → stateChunk** — and you’re good to go.

The created **store** gives you some cool things like:

* The enhanced **Provider** and **Consumer** presented above
* **actions** (you can access them from **Consumer**, too)
* **getState()** to get the current state
* **connect()()** to map state and actions to component props
* **subscribe()** to react to state changes

If you need deeper selectors and/or memoized computed data, you can, of course, use [**reselect**](https://github.com/reactjs/reselect)**.** Check out this example [here](https://github.com/didierfranc/react-waterfall/blob/v3/examples/reselect/src/store/selectors.js).

If you want **time travel,** it’s possible ? to just run t[his example.](https://github.com/didierfranc/react-stateful-example) The implementation is right h[ere.](https://github.com/didierfranc/react-stateful-example/blob/master/src/devtool.js)

### Comparison with Redux

![Image](https://cdn-media-1.freecodecamp.org/images/1*22lo3_HFH1lIWVSmgJdd5g.png)

ℹ️ Redux Devtools have been [integrated](https://github.com/didierfranc/react-waterfall/blob/master/src/helpers/devtools.js) by default in the version 4.0.0, you’ve nothing to do, it just works.

**Pros**

* Easier to implement
* Weight and performance
* Cleaner action return with state chunk (as in setState)

**Cons**

* It only works with React ^16.3

### You want to try it ?

I̶ ̶h̶a̶v̶e̶ ̶n̶o̶t̶ ̶f̶o̶u̶n̶d̶ ̶a̶ ̶s̶e̶x̶y̶ ̶n̶a̶m̶e̶ ̶f̶o̶r̶ ̶i̶t̶ ̶y̶e̶t̶,̶ ̶b̶u̶t̶ ̶i̶f̶ ̶y̶o̶u̶ ̶h̶a̶v̶e̶ ̶a̶n̶ ̶i̶d̶e̶a̶ ̶f̶o̶r̶ ̶i̶t̶ ̶p̶o̶s̶t̶ ̶y̶o̶u̶r̶ ̶s̶u̶g̶g̶e̶s̶t̶i̶o̶n̶s̶ ̶h̶e̶r̶e̶ ̶o̶r̶ ̶s̶e̶n̶d̶ ̶m̶e̶ ̶a̶ ̶t̶w̶e̶e̶t̶.̶ ̶F̶o̶r̶ ̶n̶o̶w̶ ̶i̶t̶’̶s̶ ̶o̶n̶l̶y̶ ̶a̶v̶a̶i̶l̶a̶b̶l̶e̶ ̶v̶i̶a̶ ̶G̶i̶t̶h̶u̶b̶.̶

> yarn add react-waterfall

?

### More

If you’re interested by new **React** key features don’t miss [**_“When react has become (even more) asynchronous”_**](https://medium.com/@DidierFranc/when-react-has-become-even-more-asynchronous-37a55c3a3d3)**_._**

If you don’t want to miss any of my articles, _follow me on twitter [@DidierFranc](http://twitter.com/didierfranc)_

