---
title: Do we still need JavaScript frameworks?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T16:58:19.000Z'
originalURL: https://freecodecamp.org/news/do-we-still-need-javascript-frameworks-42576735949b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aZspWn6gQ0bzfIy7nWswmw.png
tags:
- name: Angular
  slug: angular
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Luke Joliat

  As a web developer, I try to assess my toolbox regularly and determine if I can
  do without this or that tool. Recently, I have been investigating just how easy
  it is to develop a complex front end application without a front end framew...'
---

By Luke Joliat

As a web developer, I try to assess my toolbox regularly and determine if I can do without this or that tool. Recently, I have been investigating just how easy it is to develop a complex front end application without a front end framework.

#### **What is a JavaScript framework?**

Put simply, a JavaScript framework is a tool that you can leverage to develop advanced web applications, especially SPAs.

Back in the day, web developers would implement front end logic by relying heavily on vanilla JS and jQuery. But, as front end applications became more and more complex, the tools rose to meet that complexity.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PNlbgb05IwSxOhAz0aA2rg.png)

The frameworks that are popular today have a few core commonalities. Most front end frameworks/libraries, from Vue to React, provide some combination of the following:

* Synchronization of state and view
* Routing
* A Template System
* Reusable components

#### **Are Frameworks still necessary?**

It depends on how you stress the word _necessary._ Many would argue that front end frameworks are not and never have been necessary. They’re very useful tools, though.

So the question is: are frameworks today’s jQuery? Will the problems they solve be addressed by changes like those to the DOM API?

![Image](https://cdn-media-1.freecodecamp.org/images/1*rSC0B8I9cLTDhiArUeildw.jpeg)

It’s hard to say, but advances in native JS, the web component spec, and easily configurable build tools, have made developing a SPA without a framework as easy as it has ever been.

To examine this further, I developed a single page application using only vanilla JavaScript, native Web Components, and Parcel. There were a handful of pitfalls and difficulties along the way that highlighted the strengths of JS frameworks.

At the same time, once I passed the initial hurdles, I was surprised by how simple it was to create a single page application with just vanilla JS.

#### Overview

The application is simple. It is a recipes application with basic CRUD capabilities. The user can create, edit, delete, favorite, and filter a list of recipes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qJ5c-HSAPNo5CW8L_K8j1A.png)
_The Home Screen_

![Image](https://cdn-media-1.freecodecamp.org/images/1*wpy9DOp8LnB2JrQ8rcHKow.png)
_Create Recipe Screen_

#### Components

Creating a web component is also straightforward. You create a class that extends `HTMLElement` (or `HTMLParagraphElement` and so on), and then use that class to define a custom element.

You can also make use of lifecycle hooks such as _connectedCallback, disconnectedCallback, attributeChangedCallback._

#### Routing

The routing for the recipes application is also quite simple. Given a navigation event, I set the application’s content to the corresponding web component.

Initially, I was using an npm package called Vanilla JS Router. With the [browser history API](https://developer.mozilla.org/en-US/docs/Web/API/History), it isn’t all that complex to implement your own in less than 100 lines of code! Note: I am not implementing really complex logic such as route guards.

That is a quick summary. I want to keep this article to a reasonable length. I may write a follow-up post with a more thorough explanation of the application. I implemented some fun features like infinite scrolling, a custom drag and drop uploader, and more!

### Retrospective

After creating the application, I took some time to think about the pros and cons of the whole process from start to finish. I’ll start with the bad news.

### Cons

#### The spec is still in flux

![Image](https://cdn-media-1.freecodecamp.org/images/1*wCpfEUhah-4JgDR068I3hQ.png)

The web component spec is both old and new. It has been around for a lot longer than I had originally thought. _Web Components were [introduced by Alex Russell](https://en.wikipedia.org/wiki/Web_Components#cite_note-16) at Fronteers Conference 2011 for the first time._ However, the push behind web components has really grown in the past year or two. As such, there is still a lot of turmoil in the spec. For instance, HTML imports have been abandoned, though most of the documentation/resources still reference them.

#### Testing

![Image](https://cdn-media-1.freecodecamp.org/images/1*BuoxeY29sd0U2GYmJ29GVA.png)

There aren’t a lot of dedicated resources for testing native web components out there. There are some promising tools such as [skatejs ssr](https://github.com/skatejs/skatejs/tree/master/packages/ssr) and the [web component tester](https://github.com/Polymer/tools/tree/master/packages/web-component-tester) from Polymer. But these tools are really meant for use with their respective libraries. This presents some difficulties for use with native web components.

#### Change Detection

Having an underlying system that automatically keeps the view in sync with the data model is incredible. It is what drew many to Angular and other frameworks in the first place.

Keeping state in sync with the view is not so difficult at a small scale. But it can get out of control very quickly, and you find yourself adding tons of event listeners and query selectors.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xlSabT49zJjvW6xjrgykJg.png)

#### The Shadow DOM

I am really torn about the shadow DOM. On one hand, I love the idea of encapsulation. It is a sensible design pattern, makes your style cascade more manageable, simplifies your concerns, and so on. However, it also presents problems when you do want certain things to penetrate that encapsulation (such as a shared style sheet), and there are ongoing debates about [the best way of doing this.](https://www.smashingmagazine.com/2016/12/styling-web-components-using-a-shared-style-sheet/)

#### Generating DOM structures

Part of the magnificence of frameworks/libraries like Angular and React is that they are masters of their DOMain. That is, they are excellent at efficiently rendering and re-rendering structures in the DOM. From the [Angular University blog](https://blog.angular-university.io/why-angular-angular-vs-jquery-a-beginner-friendly-explanation-on-the-advantages-of-angular-and-mvc/):

> _Angular is not generating HTML and then passing it to the browser to have it parsed, instead Angular is generating DOM data structures directly!_

Angular for example, unlike jQuery, renders DOM data structures directly. That is, instead of passing HTML to the browser to be parsed, and then rendered into DOM data structures. This is more performant as it eliminates that parsing step. The Virtual DOM is also quite useful, as they prevent you from re-rendering everything each time you need to update your view.

### Pros

On the other hand, there are some undeniable benefits to developing applications this way:

#### Bundle Size

The final product can be (emphasis on _can_) so much smaller and more compact than anything developed with a modern framework. For example, the final build of my fully featured recipes app was less than half the size of a fresh Angular build.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z0SqFAFZ2StMTBcHK_hvuA.png)
_Angular bundle size_

![Image](https://cdn-media-1.freecodecamp.org/images/1*EvAcQ6E__FUVjwiCkxdRmw.png)
_Recipes app bundle_

![Image](https://cdn-media-1.freecodecamp.org/images/1*dCm_mrJfj1B2761WIb8vQA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*RLLfjCifUd6QwuXIQhYggg.png)

Note: These are the updated, optimized bundle sizes.

#### Understanding

![Image](https://cdn-media-1.freecodecamp.org/images/1*YkPg-F5x1xzLjJ6vQ0KIjA.png)

If you’ve only really developed with a framework and its CLI, it can be a great exercise to make a web application without extra tools. As someone who wants to achieve a certain level of mastery (to the extent that it’s possible) of web development, it has been essential for me to get more hands-on experience with build tools, browser APIs, design patterns, etc.

#### Performance

![Image](https://cdn-media-1.freecodecamp.org/images/1*tEpzCAu3z7YMMiJayzjKGQ.jpeg)

What these front end frameworks and libraries are doing behind the scenes is amazing. However, you can pay a performance price if you decide to use any of them; there is no such thing as a free lunch. There are many potential performance drags at scale: whether it’s wasted re-renders, redundant listeners, deep object comparison, or unnecessary and large DOM manipulations. You can cut out a lot of complexity here by implementing things from scratch.

The Angular and React teams seem aware of these pitfalls, and have provided things like _shouldUpdate_ method overrides and _onPush_ ChangeDetection as a means of further optimizing performance.

#### Simplicity and code ownership

![Image](https://cdn-media-1.freecodecamp.org/images/1*e7jkx0XuOzlMh9jypofNgQ.jpeg)

You take a risk whenever you bring in 3rd party code. This risk is reduced with tried and tested libraries/frameworks, but never truly eliminated. If you can get away with writing code yourself or with your team, you can reduce that risk and maintain a codebase that you know in and out.

#### Notes and interesting tidbits

I had a blast working with Parcel. It felt a bit more limited than Webpack at times when trying to work around certain edge cases, but I found the, ‘zero config’ tag line to hold true, for the most part.

It is also clear to me that many label React a ‘library’ and Vue a ‘progressive’ framework. While I understand the reasons for this, I think React, Vue and Angular solve many of the same problems. Thus, I am considering them all together under the term ‘frameworks.’

Why not use Stencil or Polymer? I wanted to avoid the use of packages, libraries, and frameworks as much as possible. I wanted to see how far web standards had risen to meet modern development (aside from build tools).

There are I’m sure many other ways of developing a SPA or front end application in general without a major framework or library, I tried one way here, and I’d love to hear about others!

### Summary

A great heuristic for the decision to use or not use a framework is what I call, “the tipping point.” There comes a point as your application grows, where you end up creating your own framework in order to reuse functionality and structure. For example, you have a bunch of forms and you want to create reusable logic for reactive validation.

If you end up at this point, you have to decide whether or not it is worth investing the time in creating systems to accomplish what you can quickly accomplish with a framework or library. There will be different tipping points depending on what your time constraints or budget constraints are, but frameworks are still very relevant given the right scenarios.

That said, much of what frameworks do will probably become easier to do with smaller libraries and/or native code as time goes on. Take my application as an example. At the same time, if the large frameworks and libraries remain versatile they may morph, adapt, and stick around. If not, they may end up like jQuery — a tool of the past for the most part.

### Conclusion

In conclusion, there are promising ways of developing complex front end applications without frameworks. However, the spec for things like web components is still evolving and there are kinks to be worked out. The frameworks still do a lot of amazing things and can make development much smoother.

At this time, as far as I can tell, the pros of using a framework often outweigh the cons. However, if frameworks do not start solving new problems and continuing to evolve, they will eventually fade away.

### Resources

[**Angular For Beginners Guide: Why Angular? The Top Benefits**](https://blog.angular-university.io/why-angular-angular-vs-jquery-a-beginner-friendly-explanation-on-the-advantages-of-angular-and-mvc/)  
[_Note: This post is part of the ongoing Angular for Beginners series, here is the complete series: Angular For Beginners…_blog.angular-university.io](https://blog.angular-university.io/why-angular-angular-vs-jquery-a-beginner-friendly-explanation-on-the-advantages-of-angular-and-mvc/)[**Comparison with Other Frameworks - Vue.js**](https://vuejs.org/v2/guide/comparison.html#Runtime-Performance-1)  
[_Vue.js - The Progressive JavaScript Framework_vuejs.org](https://vuejs.org/v2/guide/comparison.html#Runtime-Performance-1)[**Optimizing Performance - React**](https://reactjs.org/docs/optimizing-performance.html)  
[_Internally, React uses several clever techniques to minimize the number of costly DOM operations required to update the…_reactjs.org](https://reactjs.org/docs/optimizing-performance.html)[**Web Components**](https://developer.mozilla.org/en-US/docs/Web/Web_Components)  
[_As developers, we all know that reusing code as much as possible is a good idea. This has traditionally not been so…_developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/Web_Components)[**The deepest reason why modern JavaScript frameworks exist**](https://medium.com/dailyjs/the-deepest-reason-why-modern-javascript-frameworks-exist-933b86ebc445)  
[_I’ve seen many, many people using a modern framework like React, Angular or Vue.js blindly. These frameworks provide…_medium.com](https://medium.com/dailyjs/the-deepest-reason-why-modern-javascript-frameworks-exist-933b86ebc445)[**Styling Web Components Using A Shared Style Sheet**](https://www.smashingmagazine.com/2016/12/styling-web-components-using-a-shared-style-sheet/)  
[_Web components are an amazing new feature of the web, allowing developers to define their own custom HTML elements…_www.smashingmagazine.com](https://www.smashingmagazine.com/2016/12/styling-web-components-using-a-shared-style-sheet/)

