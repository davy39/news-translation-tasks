---
title: Learn Vue.js in this free course! ?✨
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-10T21:03:18.000Z'
originalURL: https://freecodecamp.org/news/learn-vue-js-in-our-free-course-85d5df41e47f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*G1PUKcevhmpXSKUeX9XnLA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Vue.js
  slug: vuejs
seo_title: null
seo_desc: 'By ZAYDEK

  Let’s make something Vueseful

  Before I get to the article, I just want to share that I’m building a product, and
  I would love to collect some data about how to better serve web developers. I created
  a short questionnaire to check out before...'
---

By ZAYDEK

#### Let’s make something Vueseful

Before I get to the article, I just want to share that I’m building a product, and I would love to collect some data about how to better serve web developers. I created a [short questionnaire](https://twitter.com/username_ZAYDEK/status/1103914471267790854) to check out before or after reading this article. Please check it out — thanks! And now, back to our regular scheduled programming.

![Image](https://cdn-media-1.freecodecamp.org/images/1*G1PUKcevhmpXSKUeX9XnLA.png)

### Hello Internet!

You might not know what Vue is — and that’s OK — and heck, you might not, definitely not, know who I am! I’m [Zaydek](http://twitter.com/username_ZAYDEK), and I’m an experienced graphic designer and programmer. [I just released a free course](https://scrimba.com/g/glearnvue) to help developers learn some Vue! I’m here to enlighten you about all the possibilities that learning and using this amazing open-source framework present.

In this article, I detail how to think about Vue. I also iterate the building-blocks needed to start programming static and dynamic websites with an order of magnitude more ease than with vanilla JavaScript. ? Vue is both a paradigm for writing web apps and an idiomatic guide to learning and programming JavaScript.

#### I also teach the JavaScript ?✨ needed to get started in the Vue course I just released. Learn Vue from the basics, and how to build a few things, too. C[lick here to enroll for free!](https://scrimba.com/g/glearnvue)

![Image](https://cdn-media-1.freecodecamp.org/images/1*q-pzfW25_QfFrGQg2T3FOA.png)
_Click to enroll in my free Vue course!_

The course is taught on [Scrimba.com](https://scrimba.com/g/glearnvue), which is a **new and interactive website for learning and sharing how to code**. Screencasts can be interrupted and edited, making learning active and fun to experiment with.

### Vue is not one thing

A framework can be thought of as a general-use toolbox, equipped with tools that solve different problems but all together help with some task. That task, where Vue is concerned, is building maintainable and idiomatic web apps with ease — really — and having fun while we’re at it!

Let’s put things into perspective. Vue can be as simple as a script tag that we can include in our websites to turn them into web apps. But it can also be an entire ecosystem that relies on a build-process to make engineering complex and powerful web apps easier.

In this article and in the course, I focus on learning the core concepts Vue presents, and assume no knowledge of the command-line or what a build-process is.

### What the course covers

![Image](https://cdn-media-1.freecodecamp.org/images/1*ixssvvdIf64KQONR4Ugn7Q.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*spoAQtMm1OBMU1iciAZmzg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*_mu96vH6fakViESA8XOmQg.png)

The course is three parts:

1. learning the minimum JavaScript needed to get started with Vue
2. learning the core concepts of Vue, and
3. an overview of two more advanced examples (two cute and fun web apps I made: Schrödinger’s Div ? and a ? Color Picker).

What I love about Vue is that it proposes some interesting ideas for how to think about and how to build web apps. There are a few ideas that I think are most interesting — though this is not suggestive of all that Vue can do:

* separating the data from the DOM
* idiomatic JavaScript
* templating and component-based HTML
* managing event-handling

But before we can get into that, let’s first cover how to connect Vue via a simple script tag to a website:

![Image](https://cdn-media-1.freecodecamp.org/images/1*5FJnYPPjV1EKLtk4xk5r2w.png)

You can think of a web app as being inside or on top of a website. So a web app begins it’s life at the `<div id="ap`p">, where from inside the script tag it is plugged i`n via new Vue({ el: "#a`pp" }). That is how we create a relationship from the JavaScript to the HTML (`wh`ere el is short for element).

This is the first of what are known as options, and Vue supports a lot of options, such as `data` and `methods`. These are analogous to variables and functions for our web app.

**Note:** Vue comes in two flavors: ? there’s both the d[evelopment](https://cdn.jsdelivr.net/npm/vue/dist/vue.js) and p[roduction](https://cdn.jsdelivr.net/npm/vue) version. The development version emits detailed error messages and warnings to support developers while working in Vue. The production version is optimized for speed and size.

In addition to all of this, [there’s an official Chrome extension](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd) that makes managing the app’s state and debugging painless.

### Separating the data from the DOM

![Image](https://cdn-media-1.freecodecamp.org/images/1*h6PJeo6PHIpzinqCLkjYCw.jpeg)
_Credit [Daniel Cheung](https://unsplash.com/photos/bO4UR1VzQu8" rel="noopener" target="_blank" title=")_

As mentioned earlier, one great suggestion Vue proposes is separating the data from the DOM. DOM stands for document-object-model, which can be thought of as the tree of elements that compose our website. The text in between the opening and closing elements is what I’m referring to as the data. In Vue we don’t hardcode it — we separate it and put in the aforementioned `data` object from inside of our Vue instance.

This idea is also referred to as the Virtual DOM. This might seem insignificant, but the truth is that having the data in one place means that we know how and where to update it. And because Vue is reactive, whenever we update said data, that change gets propagated throughout our web app. Because of this relationship, data can be thought of as much more alive in Vue than in vanilla HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/1*s961WYdfXbFGEVR6bkGtdg.png)

[These ideas are explored in the third screencast.](https://scrimba.com/g/glearnvue)

### Idiomatic JavaScript

![Image](https://cdn-media-1.freecodecamp.org/images/1*uJNE1s0MwUXnlRlA7hly8Q.jpeg)
_Credit [Daniel Cheung](https://unsplash.com/photos/ZqqlOZyGG7g" rel="noopener" target="_blank" title=")_

For me, Vue makes JavaScript a language worth learning, because it makes sense of JavaScript. What I mean is that from inside of a `new Vue({ ... })` is how and where we learn to wrangle JavaScript. Variables are key-value pairs attached to the `data` object as shown above, and functions are attached as key-value pairs attached to a second object: `methods`. And both objects data and methods are optional — remember, these are our web app’s options.

But Vue goes a lot further: Vue features a lot of options that come in the form of objects we hook into in our Vue instance. Altogether, this resembles an idiomatic guide and approach to programming in JavaScript. Therefore, few architectural decisions are left for the programmer. This means that writing and reading Vue has a sort of coherence and elegance that makes it easier to pick up than deconstructing how a vanilla JavaScript app works.

[These ideas are explored in the fourth screencast.](https://scrimba.com/g/glearnvue)

### Templating HTML

![Image](https://cdn-media-1.freecodecamp.org/images/1*OqJU7uN6drj41M8LTMzH_w.jpeg)
_Credit [Daniel Cheung](https://unsplash.com/photos/dDppsuM_UpE" rel="noopener" target="_blank" title=")_

Most people wouldn’t consider [HTML a programming language](https://www.youtube.com/watch?v=4A2mWqLUpzw). But I think a reasonable definition of the purpose of a programming language is this: to interpret and transform data, such as reading and compiling source code.

Given Vue’s attributes, such as `v-for`, `v-if`, and so on, for me HTML begins to resemble a programming language with control-flow. This means that we can better control the flow of our program’s data (for example, our website’s content or what I keep calling the data).

For what it’s worth, templating frameworks, like [Jekyll](https://jekyllrb.com/) and [Hugo](https://gohugo.io/), were created to aid developers with authoring static-based websites using a kind of control-flow. As nice as this is, it’s limited to static websites, because these frameworks compile to HTML rather than interpret HTML.

Having access to realtime control-flow, like for-loops and if-statements, means that Vue can do a lot more and do it in realtime. This is one of the big differences between websites and web apps (static versus dynamic content).

[These ideas are explored in the fifth screencast.](https://scrimba.com/g/glearnvue)

### Components and props

![Image](https://cdn-media-1.freecodecamp.org/images/1*po1kpbyVVzwXrxtKC6A7Bw.jpeg)
_Credit [James Pond](https://unsplash.com/photos/jnL0gfo_5Rg" rel="noopener" target="_blank" title=")_

Something that took me far too long to appreciate is the difference between variables and properties. Variables store data, whereas properties are variables attached to an object in JavaScript. So components can be thought of as HTML mixins. A what? A mixin is like a function, but instead of returning data, it mixes-in data into the document. For example, it writes HTML for us so we don’t have to repeat ourselves!

And this isn’t a small thing. The benefit of components and props in Vue means we can refactor entire HTML code blocks into one-liners that can be customized via props. This means we can now author custom elements that expose access to their internals without overcomplicating the public HTML. This is a big win for both maintainable and readable code.

[These ideas are explored in the sixth screencast.](https://scrimba.com/g/glearnvue)

### Managing event-handling

![Image](https://cdn-media-1.freecodecamp.org/images/1*7qN47N73nxf62SJem67Txw.jpeg)
_Credit [James Pond](https://unsplash.com/photos/gQ-h3k7vHjc" rel="noopener" target="_blank" title=")_

While everything we’ve talked about so far is fascinating, it doesn’t speak to user-interaction, which is one of the key differences between a website versus a web app. A website conventionally means something that is more-or-less static and isn’t designed or intended to interact with the user much, outside of perhaps collecting data. In an actual web app, something reminiscent of a native app, interaction is paramount. ? This idea is also referred to as a dynamic website or web app.

Since Vue is both a framework and an ecosystem, it has idiomatic solutions for this, too. The simplest one that I teach in the course is the `@click="function()"` handler which we plug into an element as an HTML attribute. This simple snippet gives us a means to interact with our data, as simple as an attribute that we plug into an element. This means that we can defer to JavaScript and not HTML or CSS for rich user-interaction.

[These ideas are explored in the seventh screencast.](https://scrimba.com/g/glearnvue)

#### There’s a lot more to learning Vue, so I wrote two more articles on the subject matter. Please, after this article, have a look!

![Image](https://cdn-media-1.freecodecamp.org/images/1*spoAQtMm1OBMU1iciAZmzg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*_mu96vH6fakViESA8XOmQg.png)
_Left: “[ow to make a ? color picker with Vue!” ](https://medium.freecodecamp.org/building-schr%C3%B6dingers-div-with-vue-4068f6423830" rel="noopener" target="_blank" title="">Building Schrödinger’s div ? with Vue!”</a> Right: “H<a href="https://medium.freecodecamp.org/how-to-make-a-color-picker-with-vue-9640043b6c82" rel="noopener" target="_blank" title=")_

### Vue makes the web make sense

Before Vue, I was acquainted with HTML and CSS. I was comfortable enough to make some alluring websites, but nothing more. I explored some frameworks (like those I discussed in this article concerning static compilation), and peered into Angular and React, but I didn’t get the right feeling when exploring those. What I wanted was something lightweight and intuitive, and I believe I’ve found that with Vue.

In the end, it doesn’t matter which tools we use if we can create what we set out to build. But the thing is, it’s hard to separate the tools from the thinking used to build a product or service. This is both a good and bad thing. On the one hand, it can make us narrow-minded. But on the other end of the spectrum, the tools we use can also serve as a teaching instrument for learning new and interesting ideas. I love tools that can’t help but teach me at the same time, and I couldn’t recommend Vue more for this reason!

So please, go out into the beautiful world and learn you some Vue! You can(!) make amazing things and even change people’s lives, even your own. **And if it helps, [try the free course](https://scrimba.com/g/glearnvue)!**

![Image](https://cdn-media-1.freecodecamp.org/images/1*q-pzfW25_QfFrGQg2T3FOA.png)

