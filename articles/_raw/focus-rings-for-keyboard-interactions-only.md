---
title: How to add Focus Rings for keyboard interactions only
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-11T16:16:20.000Z'
originalURL: https://freecodecamp.org/news/focus-rings-for-keyboard-interactions-only
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca21e740569d1a4ca52b4.jpg
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
- name: Design
  slug: design
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
seo_title: null
seo_desc: 'By Ben Robertson

  One thing that inevitably makes its way into our QA process on any project is the
  unexpected appearance of focus rings.


  A wild focus ring appeared!

  We’ve had a lot of discussions about how to handle these. The project manager and
  de...'
---

By Ben Robertson

One thing that inevitably makes its way into our QA process on any project is the unexpected appearance of focus rings.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/focus-ring.png)
_A wild focus ring appeared!_

We’ve had a lot of discussions about how to handle these. The project manager and designer often suggest removing them. While that would be the easy solution, it would be a web design **anti-pattern**. Default focus rings are provided by all browsers so that keyboard users can determine which element is currently in focus. In fact, **focus rings are required to meet accessibility standards**:

> Any keyboard operable user interface has a mode of operation where the keyboard focus indicator is visible.  
> - [**W3 Web Content Accessibility Guidelines**](https://www.w3.org/TR/WCAG21/#focus-visible)

Even when we decide not to remove focus rings, designers are usually unhappy with the default styles. One question that came up recently is if focus ring styles are made for keyboard users to keep track of the focus on the page, why do they need to show up when I click on an element? Can we add focus rings for keyboard users only?

The answer is yes! We can use the [**`:focus-visible` polyfill**](https://github.com/WICG/focus-visible) to add focus rings only when a user is navigating with a keyboard.

## **How to use the `:focus-visible` polyfill**

Here’s how you can implement the `:focus-visible` in your projects right now.

If you are using ES6 modules, install the polyfill via npm:`npm install --save focus-visible`

Import the module into your main JavaScript file:

```js
import 'focus-visible';

```

When your page loads, your `<body>` will get a class of `.js-focus-visible` so you can conditionally hide default focus rings only if the polyfill is loaded. Additionally, when you are navigating via keyboard, focused elements will get a class of `.focus-visible`.

Now we can add our css:

```css
// override UA stylesheet, only when polyfill is loaded
.js-focus-visible :focus:not(.focus-visible) {
    outline-width: 0;
}

// establish desired focus ring appearance for appropriate input modalities
.focus-visible {
  outline: 2px solid $bright-brand-color;
}

```

## **Other Resources**

* [**`:focus-visible` polyfill on Github**](https://github.com/WICG/focus-visible)
* [**Focus-ring on A11y Casts**](https://www.youtube.com/watch?v=ilj2P5-5CjI&feature=youtu.be)
* [**The CSS Working Group focus-visible pseudo-class spec**](https://drafts.csswg.org/selectors-4/#the-focus-visible-pseudo)

_Want to dive deeper into building accessible websites? Join my free email course:_ ? _[**Common accessibility mistakes and how to avoid them**](https://benrobertson.io/courses/common-accessibility-mistakes/). 30 days, 10 lessons, 100% fun!_ ? [**_Sign up here_**](https://benrobertson.io/courses/common-accessibility-mistakes/)!

_This post originally appeared on [benrobertson.io](https://benrobertson.io/accessibility/focus-ring-keyboard-only)._

