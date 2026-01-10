---
title: The Virtual DOM is slow. Meet the Memoized DOM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-18T13:01:37.000Z'
originalURL: https://freecodecamp.org/news/the-virtual-dom-is-slow-meet-the-memoized-dom-bb19f546cc52
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pwD6vakbORJiYCsD0NppHw.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: vue
  slug: vue
seo_title: null
seo_desc: 'By Sindre Osen Aarsaether

  Moving beyond the Virtual DOM and State Management


  The virtual DOM was a fantastic innovation. It brought about a much more productive
  way of writing web applications by allowing us to write our views in a declarative
  manne...'
---

By Sindre Osen Aarsaether

#### Moving beyond the Virtual DOM and State Management

![Image](https://cdn-media-1.freecodecamp.org/images/hAPVXQJeNHcW4WTZqiRiAHQvAcyLP9HjEIDC)

The virtual DOM was a fantastic innovation. It brought about a much more productive way of writing web applications by allowing us to write our views in a declarative manner.

This big benefit has little to do with performance of the initial render. Instead, it is the process of updating the DOM to reflect changes in your state has become much faster.

This process of bringing the DOM in sync with the state is often referred to as [DOM reconciliation](https://reactjs.org/docs/reconciliation.html).

If we had an infinitely fast reconciler, we could vastly simplify our applications by **rendering everything on every single frame**. The state layer would never need to know about views at all — much less send out events and track which views need to react when certain parts of the state change. The view would always be in sync with the data, no matter what you threw at it.

Sadly, virtual DOM implementations are _not_ infinitely fast. They are, in fact, surprisingly slow. Thankfully, many have jumped on the Immutability™ bandwagon, in which case the virtual DOM thanks you! Others wrap all state in observables (e.g. mobx), and keep track of which view depends on what state. This allows you to reconcile only parts of your view, but comes with its own set of drawbacks.

The biggest issue is that we tend to decide how to manage our application state based on our view layer. What if we could get **better** performance in a world where the data layer and view layer don’t really know or care about each other?

### Meet the Memoized DOM

[Imba](https://github.com/somebee/imba) is a programming language for the web. It powers the interactive screencasting platform [scrimba.com](https://scrimba.com), of which I am the lead developer. Imba was born to make developing web applications fun again. It features a clean and readable syntax inspired by Ruby. It compiles to readable and performant JavaScript, and works inside the existing ecosystem.

![Image](https://cdn-media-1.freecodecamp.org/images/2SSQxsAdonLBrSsgBWEtRsC-CTjqS4VI9g8c)
_The whole stack of scrimba.com is written in [Imba](http://imba.io/guides" rel="noopener" target="_blank" title="), but the language can easily be used just for the view layer._

Besides a clean and readable syntax, the biggest benefit of Imba is that it truly treats DOM elements as first-class citizens, on a much deeper level than JSX. It allows you to write views declaratively, yet it **does not use a virtual DOM.** Instead, Imba compiles views to a **memoized DOM,** which turns out to be **an order of magnitude faster**.

#### How it works

The general idea is that we create lightweight wrappers around DOM elements, and compile declarative views to chains of setters, each modifying the underlying DOM directly.

```jsx
tag AppView
    def render
        <self>
            <h1.title> "Welcome"
            <p.desc .red=(Math.random > 0.5)> "Roulette"
```

The Imba view above will roughly compile into the following javascript:

```jsx
class AppView extends Imba.Tag {
  render() {
    var $ = this.$; // inline cache for tag
    return this.setChildren($.$ = $.$ || [
      Imba.tag('h1',$).flag('title').setText("Welcome"),
      Imba.tag('p',$).flag('desc').setText("Roulette")
    ]).synced(
      $[1].flagIf('red',Math.random() > 0.5)
    );
  }
}
```

This is a _very_ simple example to illustrate the basic concept. During compilation we split creation and updates into separate branches. The first time render is called for an `<AppVi`ew> the children will be created and static attributes will be set. On all subsequent calls the only real work we do is flip the className o`f o`ur <p>. Albeit much more complex, the same concept is used for conditionals, loops, and everything else inside tag trees.

If you’re interested in how it really works I recommend reading [this intro](http://imba.io/guides/advanced/performance#performance).

### Benchmark

> React is fast, they said. React is fast enough, they said. React Fiber will be fast enough, they said.

Most benchmarks test things like “insert/shuffle/remove 1000 rows”. This gives little indication about real-world performance. When there are hundres of changes, most of the difference is eaten up by actual DOM mutations, repainting, etc. It fails to measure the most important metric.

If you truly want to test the performance of DOM reconciliation, you need to look at how quickly the implementation brings the DOM in sync with the state, **_especially_ when there are few/no changes**.

So, to capture a realistic view of the reconciler performance, we could change a small part of the application state in each iteration, and then measure the time it takes to forcefully bring the view in sync with this changed state. The view should not be listening to any part of the state, and the state should not need to notify anyone whether it has changed.

![Image](https://cdn-media-1.freecodecamp.org/images/TVVy8hfU5Sda4vHDAJRtYAWOUZxWC9X6FMzw)
_Screenshot from [dom-reconciler-bench](https://somebee.github.io/dom-reconciler-bench/index.html" rel="noopener" target="_blank" title=")_

[This benchmark](https://somebee.github.io/dom-reconciler-bench/index.html) steps through a deterministic sequence of state alterations, doing at most **one change per iteration**. We are measuring the time it takes to reconcile _the whole application view_ after:

1. Toggling the completion of a task
2. Removing a task
3. Inserting a task
4. Renaming a task
5. Doing nothing

### Results

Running the benchmark on an iMac (4GHz i7) yields the following results:

#### Safari 11

* Imba 1.3: **360458** ops / sec
* React 16.2: **9752** ops / sec — **36.96x slower**
* Vue 2.5: **8719** ops / sec — **41.34x slower**

#### Chrome 65

* Imba 1.3: **282484** ops / sec
* React 16.2: **8882** ops / sec — **31.81x slower**
* Vue 2.5: **8103** ops / sec — **34.86x slower**

#### Firefox 58

* Imba 1.3: **234334** ops / sec
* React 16.2: **5075** ops / sec — **46.17x slower**
* Vue 2.5: **3119** ops / sec — **75.13x slower**

This seems outrageous right? Surely, it cannot be right.

* All implementations are _really_ reconciling on every step.
* All implementations are blocking, synchronous, and deterministic.
* All implementations are performing the same amount of DOM mutations.
* Yes, we are using the minified production build of React. The development version is **200x slower** than Imba on the same test.
* The memoized DOM creates practically no garbage during an iteration, uses less memory overall, and is conceptually very simple.

All the implementations can probably be optimized more. I’m very happy to accept pull-requests at [GitHub](https://github.com/somebee/dom-reconciler-bench). To be clear, I have tremendous respect for what React has achieved, and I truly love Vue. Imba has taken a lot of inspiration from it. I suspect it should be possible to compile Vue templates using a similar approach, and would love for someone to give it a go!

### Profiling

Let’s test the raw reconciler performance when there aren’t even any changes. This removes the time spent doing actual DOM mutations from the equation, and gives us a good picture about how much work is going on during reconciliation. The charted CPU profile from Chrome gives a visual indication of how much less work is done with the memoized DOM technique.

#### Imba 1.3

![Image](https://cdn-media-1.freecodecamp.org/images/nlYhyzt27JL8sd3ayEyVJiWTg1F0eTVMauLr)
_Imba completes 100000 iterations in 99.7ms — 5.1ms spent in GC_

#### React 16.2

![Image](https://cdn-media-1.freecodecamp.org/images/zUVYDsdcUzXcgRZ5ZdjlWMJtH5QN5wSWkIPw)
_React completes 100000 iterations in 8312.7ms (83.4x slower) — 100.4ms spent in GC_

#### Vue 2.5

![Image](https://cdn-media-1.freecodecamp.org/images/JU5nkcDdF25gJGK18rtJIwj0emDqdV7v0egC)
_Vue completes 100000 iterations in 8514.7ms (85.4x slower) — 308.4ms spent in GC_

### Does it scale?

> “There are A LOT, and I mean, A LOT of small little projects that claim more speed, easier development, but on closer inspection usually lack very important features (such as module life cycle hooks) and, of course without them the performance is higher, but the flexibility to use those libraries beyond a todo list application is limited.”

This is a quote from someone who read through an early draft of this article, and I would like to tackle it head on. The performance difference is not limited to a simple test, quite the contrary. [Imba](http://imba.io) has been used in production for several years at [scrimba.com](https://scrimba.com), but it is still not for the faint of heart. For most developers the massive ecosystems for Vue and React will be hard (and probably unwise) to leave behind. The [Imba documentation](http://imba.io/guides/essentials/introduction) still leaves a lot to be desired, but we are improving it every day.

### Does it matter?

I’m sure you’ve heard that React is fast enough. But fast enough for what? It doesn’t really matter if React was 15% faster, but with an order of magnitude improvement we can start to explore simpler ways to build applications.

![Image](https://cdn-media-1.freecodecamp.org/images/fLiP6wWOXcRKJ4ULiU-Cc6dqBoO2ePluCgSb)

It’s not about the _perceived_ speed, but about what it lets you do. At [scrimba.com](https://scrimba.com) we don’t worry about keeping the view in sync with the state. We don’t worry about tracking when state has changed. Our data models are not observable. We just render. Whenever. **And it’s liberating.**

