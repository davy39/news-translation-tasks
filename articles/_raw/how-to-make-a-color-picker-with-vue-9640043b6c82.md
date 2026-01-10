---
title: How to make a ? color picker with Vue!
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-16T19:40:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-color-picker-with-vue-9640043b6c82
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_mu96vH6fakViESA8XOmQg.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
seo_title: null
seo_desc: 'By ZAYDEK

  Caution: colors may appear cuter than they are!

  Before I get to the article, I just want to share that I’m building a product, and
  I would love to collect some data about how to better serve web developers. I created
  a short questionnaire t...'
---

By ZAYDEK

#### Caution: colors may appear cuter than they are!

Before I get to the article, I just want to share that I’m building a product, and I would love to collect some data about how to better serve web developers. I created a [short questionnaire](https://twitter.com/username_ZAYDEK/status/1103914471267790854) to check out before or after reading this article. Please check it out — thanks! And now, back to our regular scheduled programming.

![Image](https://cdn-media-1.freecodecamp.org/images/V-DOiGlgMR2tBo5RNps7uY2WwC9tbEX9e6uF)

### Hello Internet!

I’m [Zaydek](https://twitter.com/username_ZAYDEK) and I’m newish to web development. I come from a background in graphic design and programming, so picking up the frontend has been fascinating for me.

The web is like the offspring of a graphic designer and programmer — it’s both visual and programmatic. So today, I’m going to introduce you to [Vue.js](https://vuejs.org/) and component-based web design — that is, modern web development. I’ll take you from a newbie web developer to an all-powerful, all-knowing web developer seer!

> _How can you make such claims, sir?_

> — Fancy you

Well, the thing is, most people learned how to Internet before we (as a whole) understood how to Internet! Including me! ? Which, to be honest, is probably why I refused to learn web development for the longest time. It just felt so broken!

But times they are a-changin’ and web development has never been more accessible or streamlined. So it is my great honor, and privilege, to introduce you to how to Internet in 2018, and perhaps even beyond!

#### I also teach how this ? works and a whole lot more in the Vue course I just released. Learn Vue from the basics and how to build a few things, too! C[lick here to enroll for free!](https://scrimba.com/g/glearnvue)

![Image](https://cdn-media-1.freecodecamp.org/images/nehx34-E7AQRjhDTfRXmz0fTCXevirAjWeOf)
_[Click to enroll in my free Vue course!](https://scrimba.com/g/glearnvue" rel="noopener" target="_blank" title=")_

#### [Scrimba.com](https://scrimba.com/g/glearnvue) is a new and interactive website for learning and sharing how to code. Screencasts can be interrupted and edited, making learning active and fun to experiment with!

### So, what’s the deal with Vue?

So why [Vue](https://vuejs.org/)? It’s a great and fair question you should be asking. Some people protest and scorn the idea of using any framework, and I think this is a dangerous idea. I do, however, suggest that for whatever tool it is that you use, to be very deliberate and thoughtful in why you’re using it.

I picked up Vue because I want to use newer tools that are not too mainstream. I wanted them to have learned from tools that have come before them (or in other words, are not too trailblazing). They should have [best-in-class documentation](https://vuejs.org/v2/guide/), and have a critical mass of users.

Since Vue, in the last weeks, [surpassed React is stars in GitHub](https://hasvuepassedreactyet.surge.sh/), that is evidence to me that Vue has a critical mass. ?

![Image](https://cdn-media-1.freecodecamp.org/images/vCpg0aDDKpn7wSPw4iEbuE0eK9fHyAIF41aE)
_By the way, [this website](https://hasvuepassedreactyet.surge.sh" rel="noopener" target="_blank" title=") was made using Vue.js! ?_

Furthermore, [Vue is an extraordinary open-source project](https://github.com/vuejs/vue), [is publicly-funded](https://www.patreon.com/evanyou), and has a great developer-experience! Like user-experience but for developers. This has the wonderful consequence that the common developer can now create interactive websites intuitively. And Vue builds on one of the most successful ideas from the Angular-React wars which is the Virtual DOM. So let’s talk about that now.

> _Virtual WUT?_

> — Internet You

Virtual DOM, yo. LOL sorry. So let’s back up — DOM is short for document-object-model. I think of the DOM as a paradigm for how we think about text as data structures to compose what we call web pages. And a virtual DOM is a clever abstraction for dealing with the text that goes between the elements, like `<p>hello, worl`d!</p>. In an idiomatic Vue-based website it’s som`ething like <p>`;{{ message }}</p>, where the data is stored inside of the JavaScript instead!

> _Why rely on JavaScript for a simple website?_

> — Innocent You

That’s a great (and fair) point. But there’s a significant benefit to relying on some JavaScript to compose websites, static or dynamic. We can write and build websites programmatically instead of copypasta’ing data around. Once the data is separate from the HTML, just like having CSS separate from the HTML, that’s when magical things can start to happen. ?

The good news is that because we’ve come to expect so much from websites, it’s fair to assume that the majority of people will have JavaScript enabled by default. So we’d have no reason to disable it. I might have disagreed with this a few years ago, but I can now appreciate just how much the benefits of using JavaScript far outweigh whatever possible concerns may arise.

### So… what about that color picker, eh?

![Image](https://cdn-media-1.freecodecamp.org/images/VNZfvY7c9sYl-1JCG5tll3QJPgWjXNTYgD8z)

![Image](https://cdn-media-1.freecodecamp.org/images/rBvQ8vNQMBafRf3hmnV8-cyALn5xd01lh81P)

![Image](https://cdn-media-1.freecodecamp.org/images/jkR1hOGbO8JVeb6T-Z7KXc7aPDgHPFNyWBSC)
_Click to pick a color, any color!_

Sorry for blabbering! It’s hard for me not to talk about this at length, partly because it’s so exciting. And also partly because of the gamut of possibilities that present themselves when a sole developer can be responsible for building beautiful and interactive web apps/businesses. Businesses you say? Yes — [Follow me on Twitter](https://twitter.com/username_ZAYDEK) and I’ll be be sure to follow up! ?

Without further ado, here’s the HTML for the website:

![Image](https://cdn-media-1.freecodecamp.org/images/AVS2iaAAgowtEcDXSlKWV6dPHUldlCE8EvCV)

Psst… the full code is available in the [ninth screencast](https://scrimba.com/p/pZ45Hz/crVeyTd).

Feeling shocked? The thing is, let’s think about the inherent complexity of the website I’ve shown you. It’s really just a box with two cells, one with an emoji and one with text, repeating 12 times. Yes, there’s some padding, there are some gradients, but the fundamental design is unchanged. So what if the code’s complexity was proportional to the design’s complexity?

![Image](https://cdn-media-1.freecodecamp.org/images/zhdMTMFVhE-GWzYCcw9lhK90NVViglhCJqn2)

![Image](https://cdn-media-1.freecodecamp.org/images/wHs5kNPsPAY3xGrQTbbqUFWr2iN4-OfWXu45)
_This is what I call a CSS debugger. You can learn more about it (and how to use it) by [clicking here](https://gist.github.com/zaydek/6b2e55258734deabbd2b4a284321d6f6" rel="noopener" target="_blank" title=")._

Here I’ve applied a [CSS debugger](https://gist.github.com/zaydek/6b2e55258734deabbd2b4a284321d6f6) to disambiguate the design, but this only goes as far as the CSS is concerned. What’s more important here, the real significance of Vue, is how we can think about our website in terms of data and not in terms of HTML elements.

So look again at those images. If we think about our website purely in terms of data, how much data is there?

Allow me to now share the underlying data structure used:

![Image](https://cdn-media-1.freecodecamp.org/images/7b0uUS6QZGfjM3FEpeh6z-j4rQqHggb7kole)
_emojify() is a helper function_

The following sentence is possibly the most important: **Vue frees us to think about our website in terms of data, separate from the HTML; this is a revolution for how we can build for the web!**

To be explicit, what I’m showing you is an array of anonymous objects each with two keys: `emoji`, and `color`. Now that we can represent the website in terms of data, we just iterate over the data using Vue’s `v-for` and a custom component.

### Yeah, right. So what about components?

Components — yes! Second to separating the data from the HTML, one of the coolest things Vue offers is component-based design. Components can help us abstract blocks of HTML/CSS/JS into a reusable unit: a component.

**A quick note**: I decided it would be best to first learn how to use Vue without a build-process, meaning I’m not making use of single-file-components. But I am making use of components via `Vue.component()`.

Remember the `<swat`ch> element I demo’d earlier in the source code? That’s a custom component I engineered using Vue to abstract the element from the implementation. This is a significant concept, because it means we can start to think more functionally than imperatively.

What’s the difference? Functional design cares about the result, whereas imperative design cares about the result **and** the implementation. Designing a component is an imperative process, whereas using one is a functional. ?

![Image](https://cdn-media-1.freecodecamp.org/images/Aix-LCVU5Ffx7zQfjKXdoFQKFcYHkHWtKqkR)

This is the implementation for the `swatch` element shown earlier. How it works is that Vue scans the DOM for instances of `swatch` and replaces it with the quotes HTML inside of the component’s `template` value. This means we can do major refactoring to better understand our website in terms of concepts, rather than being worried about how something ought to be engineered all the time.

#### There’s a lot more to learning Vue, so I wrote two more articles on the subject matter. Please, after this article, have a look!

![Image](https://cdn-media-1.freecodecamp.org/images/ozARrBWWUuMdflw5O99w8TL9fpmXkq-IrWxz)

![Image](https://cdn-media-1.freecodecamp.org/images/Bjc0ppEmnmqc5KQKLRIHCXPHnOTVdTpmf0Lj)
_Left: “[uilding Schrödinger’s div ? with Vue!” ](https://medium.freecodecamp.org/learn-vue-js-in-our-free-course-85d5df41e47f" rel="noopener" target="_blank" title="">Learn Vue.js in this free course! ?✨”</a> Right: “B<a href="https://medium.freecodecamp.org/building-schr%C3%B6dingers-div-with-vue-4068f6423830" rel="noopener" target="_blank" title=")_

### Well, you’ve changed my mind..

I know this might be a lot to take in, especially for something appearing so harmless as a ? color picker. But what I’ve shown you is (besides the CSS) 90% of the codebase. There are at least a few helper functions I’m omitting, but the point is that the techniques and ideologies discussed add up to a lot more than a cute web app. It means that a sole individual can create beautiful and functional web-based products and services for others.

I’m also suggesting that Vue is a lot more than a framework. If paired with the right backend language (let’s hear it for [Go](https://golang.org/)!), learning and using Vue adds up to a lot more. Idiomatic Vue can also teach what modern software development means, and how to access the billions(!) of us that are now connected, without the same technical barriers that come with app development.

#### So please, go out into the beautiful world and learn you some Vue! You can(!) make amazing things and even change people’s lives, even your own. And if it helps, [try the free course](https://scrimba.com/g/glearnvue)!

![Image](https://cdn-media-1.freecodecamp.org/images/xdrJi-5Z3EID6sEgh8dvUk7u335SFakRO4SX)

