---
title: 'How to Style Accessibility: a Web Components Approach'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-19T23:24:05.000Z'
originalURL: https://freecodecamp.org/news/styling-accessibility-a-web-components-approach-dc2aa8123eb2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Q8AgfDVFkz3mTgQujCC_sA.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cristiano Correia

  a11y and the new Web Standards

  The new Web Standards are evolving fast, and sometimes it’s hard to actually know
  the current state of a particular subject in a sea of subjects. I often realize
  that the vast majority of web projec...'
---

By Cristiano Correia

### **a11y and the new Web Standards**

The new Web Standards are evolving fast, and sometimes it’s hard to actually know the **current state** of a particular subject in a sea of subjects. I often realize that the vast majority of web projects start without having Accessibility (a11y) in mind and it becomes daunting to go back and fix it.

Since there are still many Web Components projects yet to be born, I decided to gather up the 101’s about those particular subjects and guide anyone sailing in these seas for the first time. So in this article, you will find:

* The basics about Accessibility
* The basics about Web Components
* What’s new regarding CSS
* How can you make your Web Components more accessible

Let’s sail.

### **Basics #1. What’s Web Accessibility?**

> _“Accessibility is often viewed as making your site work on screen readers. In reality, web accessibility is a subset of User Experience (UX) focused on making your websites usable by the widest range of people possible, including those who have disabilities.”_

The above quote (from Dave Ruppert on “[Myth: Accessibility is ‘blind people’](https://a11yproject.com/posts/myth-accessibility-is-blind-people/)” for the a11y project) reflects the biggest challenge about Web Accessibility: knowing exactly what it is.

Web Accessibility is essentially a way of giving access your product to all your potential users.

The **5 categories of accessibility** to take into account are:

* Visual (e.g. non-sighted, myopia, color blindness, etc.)
* Auditory
* Motor
* Cognitive
* Temporarily disabled users (e. g. one-handed phone users)

If we need to **translate those into a product**, it usually means being concerned about:

* Semantics
* Keyboard inputs
* Text alternatives
* Color Contrast

In order to take that **into account while developing** a product, you should:

* Make sure you convey meaning through not only color but also form
* Make sure your product is resizable
* Make sure your content subjects are distinguishable
* Make sure you follow the [guidelines from the W3C](https://www.w3.org/TR/WCAG20/) in general

…and don’t forget about the **Accessibility Tree!** It is the

> _“structure produced by platform Accessibility APIs running parallel to the DOM, which exposes accessibility information to assistive technologies such as screen readers”_ ([source](https://egghead.io/lessons/html-5-what-is-the-accessibility-tree)).

### Basics #2: A Brief History of Web Components

Web Components, in their essence, are actually “nothing”: Web Components are a set of **new Web Standards** that help us achieve a native way of making **Components**. In broad strokes, I would define Web Components as:

> **A native way** to achieve a **small and re-usable** set of logic, behaviors and interface elements, through a series of **browsers standards**.

So, what are the building blocks of Web Components?

* HTML Templates
* Shadow DOM
* Custom Elements
* …and HTML Imports (-ish)

#### HTML Templates

HTML Templates are a form of re-using pieces of HTML without the original “template” being rendered on the page.

It works as follows:

Which will render something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*pzf_L1AF5M3CmIG-ZS67fQ.png)

You can check how HTML Templates are currently being supported by browsers on this [caniuse page](https://caniuse.com/#feat=template).

#### Shadow DOM

Shadow DOM is a way to achieve CSS scoping, DOM encapsulation, and composition, making it easier to build isolated components.

There’s two modes of achieving Shadow DOM: “closed” and “open”. The difference is that when you instance `element.shadowRoot`, the “open” mode returns the HTML node and the “closed” mode returns `null`. Both modes return `null` when you try to query the DOM. Bear in mind that you have to set a mode to use Shadow DOM since there is no default value for it.

It works as follows:

Which will render something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*u-0sv8xHko8XvLRdg5JywQ.png)

And the DOM tree will look something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*PyqhU8gFZSc8Z4wc3LbyOQ.png)

You can check how Shadow DOM is currently supported by browsers on this [caniuse page](https://caniuse.com/#feat=shadowdomv1).

#### Custom Elements

Custom Elements are the way to achieve full re-usable encapsulated pieces of logic and have the best from Shadow DOM and HTML Templates, including **slots**.

All this can be achieved by the following:

Which will render something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*HDfc7fGk0bNyoEtOspoVkQ.png)
_You can see the Template “Slots” being replaced accordingly_

You can check how Custom Elements are currently supported by browsers on this [caniuse page](https://caniuse.com/#feat=custom-elementsv1).

#### …and the -ish: HTML Imports vs. ES Modules

HTML Imports were a big part of the Web Components standards, but they’ve stopped being supported and no longer are listed on the Web Components page (being replaced by **ES Modules**). They’re no more than a footnote at this point in Web Components history. As Wilson Page from the Firefox OS team [puts it](https://hacks.mozilla.org/2015/06/the-state-of-web-components/):

> _“We’ve been working with Web Components in Firefox OS for over a year and have found using existing module syntax (AMD or Common JS) to resolve a dependency tree, registering elements, loaded using a normal <script> tag seems to be enough to get stuff_ done.”

If you want to know more about the state of the HTML Imports vs. ES Modules, you can check out this [page](https://github.com/w3c/webcomponents/blob/gh-pages/proposals/HTML-Imports-and-ES-Modules.md).

Web Components are way more than this. Make sure you continue to search for more information about them, specially regarding _custom events_, _observedAttributes_, _testing_ and _performance_.

### Bonus round: the new CSS “theories”

If you check back on the code snippets on this article, you’ve already glimpsed a few new offerings from CSS:

* **Scoped CSS** (through Shadow DOM) solves one of the biggest problems with CSS, the “over-ruling”
* With **:host** we can select to style a shadow host
* There is also **:host()** and **:host-context()** — the first one targeting the host that is passed inside the parenthesis (e.g. :host(.some-custom-element)) and the second one targeting the content of a shadow host (e.g. :host-context(h2) targets the h2’s inside a shadow host)

#### “theories” you shouldn’t use

Since Web Components are standards that are continuously evolving, there are a few things that have come and gone (like the already mentioned HTML Imports). That’s also the case for various aspects of CSS, and is especially true for the **Shadow Piercing Combinators,** which were forms of styling shadowed elements. If you come across these, please avoided them :) They are:

* ::shadow
* /deep/
* >>>

#### But wait, CSS Variables!

…and yes. There are proper forms of styling shadowed elements: CSS Variables. You can re-use generic styling inside (and actually, outside) Web Components. Let’s check out how:

The `h2` inside the shadowRoot will render as the content of the `— main-text-color` if it exists. If it does not exist, it will be rendered as blue. The result is something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*SZFlTLPiP3jVwEZ4uIVsbA.png)
_In this case, the content of the — main-text-color variable is yellow._

You can check how CSS Variables are currently supported by browsers on this [caniuse page](https://caniuse.com/#feat=css-variables,css-grid).

#### ::part() and ::theme()

::part() and ::theme() are very recent proposals to CSS that came to our aid as alternatives to style shadowed elements. Instead of trying to explain them, I’m just going to redirect you to [this article by Monica Dinculescu which is excellent](https://meowni.ca/posts/part-theme-explainer/). They are very recent proposals to CSS so it’s quite possible that when you read this article they will still not be supported by your browser.

### So, how can we make our components accessible?

Firstly…

#### Basics, basics, #3. The basics about accessibility:

There are a few things that we can do to our product from the ground-up that will immensely help in making it accessible to our users.

One thing to remember is the _blueberry theory_ (an idea “_stolen”_ again from a talk of Monica Dunculescu):

![Image](https://cdn-media-1.freecodecamp.org/images/0*pXyF-ks0XH1GlZJd)
_Photo by [Unsplash](https://unsplash.com/@kaitlynraeann?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Kaitlyn Chow</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

What makes a blueberry muffin is not adding blueberries to an existing muffin, is actually cooking a blueberry muffin from the beginning. Making a product accessible is not adding a few roles and ARIA labels after it’s built, but it is actually having accessibility in mind from the very start.

So…

#### Role

Role is a way of telling a new element to behave as a different one. Quick example:

#### TabIndex

TabIndex is a way of making an element focusable (essential for a screen reader). If you set it as 0, it’s focusable on the right order, if it’s -1 it’s focusable out of the normal order (as in, you can trigger programmatically the focus of the element). If you set it to any other positive number, you change the actual order of the focus (highly avoidable). Quick example:

#### Focus indicator

The focus indicator is something (usually) native to the browser and serves as a visual aid to which element is focused at the current moment. If you’ve ever thought that the _design is not perfect_, please don’t remove it (e.g. on Chrome you might see it as an orange or blue glow around an input) with `{ outline: none; }` on the CSS, for example. It’s extremely useful for everyone who uses screen readers — if you want to redesign it, please make sure you follow the accessibility guidelines.

#### ARIA

Aria is a way to improve how you label your components. There’s tons of them, so I won’t bother you with the huge list :) — you can find them [here](https://www.w3.org/TR/wai-aria-1.0/states_and_properties) — just a quick example:

Without the ARIA labels, a screen reader would perceive the input as “5, slider” but with them, it would read it as “ARIA: amount of problem. 5, slider. min: 0, max: 10”.

Here’s an excellent (and quick) tutorial on how to label a custom element:

#### Keyboard input

Like I mentioned at the beginning of the article, it’s quite important to bind the behavior to the keyboard. The native elements from HTML should have this covered but if you write a custom element, never forget that `onkeydown`, `onkeypress` and `onkeyup` events are your best friends.

### **So, what’s really new?**

#### The short answer:

Extending HTML interfaces.

#### The long answer:

Extending HTML interfaces :)

Let me explain.

Although a native element should be fully accessible, it might not provide the exact functionality you need or look the way you want. We can for sure write something adapted to our actual needs but we would have to take care of all the accessibility needs since custom elements have no implicit semantics or keyboard support.… So, why can’t we **extend** the functionality of a native element? Now we can. Or “can”.

#### Element interfaces

[Here is the list](https://html.spec.whatwg.org/multipage/indices.html#element-interfaces) of the existing HTML interfaces. With them, you can extend the native behavior. We can revisit our example for Custom Elements and extend `HTMLButtonElement` to add our own behavior. Here’s how:

If you remember the previous examples, I added (_for dramatic effect :)_) a CSS rule that all text would be white. This goes against the native look for a button and makes it unreadable. While extending the normal element with the text being black, we made it a bit more accessible (plus, I added an extra label on it).

The differences here are:

* `extends HTMLButtonElement` instead of `HTMLElement`
* When we define the customElement, we pass as a third parameter an object with which element is extended (in this case “button”)
* And we use it by referencing a native button element with `is="accessible-button"`.

This renders something like:

![Image](https://cdn-media-1.freecodecamp.org/images/1*zpNCljDYJ5e1wFlqV6Q6VQ.png)

The first button is not extended so it still has the color as white; The second one is extended so it now has the color black (plus, an ARIA label) and the third one does not work… Why? Because extending a HTML interface needs be done through the `is` attribute and not be referenced through the normal custom element tag.

**Beware**: if you check the “[Extending custom HTML elements](https://developers.google.com/web/fundamentals/web-components/customelements#extendhtml)” page by google, there is a very important note:

> Only Chrome 67 supports customized built-in elements ([status](https://www.chromestatus.com/feature/4670146924773376)) right now. Edge and Firefox will implement it, but Safari has chosen not to implement it. This is unfortunate for accessibility and progressive enhancement. If you think extending native HTML elements is useful, voice your thoughts on [509](https://github.com/w3c/webcomponents/issues/509) and [662](https://github.com/w3c/webcomponents/issues/662) on Github.

It’s not the safest feature to use just yet, so always check where your product should be used before using any of the features referenced on this article, specially this one.

### So if Web Components are not supported everywhere yet, what should I do?

There’s an in-between state :)

#### Polyfills

First and foremost, there are polyfills. [Check them out here](https://www.webcomponents.org/polyfills).

#### Libraries that makes your life easier

[Angular Elements](https://angular.io/guide/elements), [Polymer](https://www.polymer-project.org/) and [Stencil](https://stenciljs.com/) are just a few examples of libraries that can help you to use Custom Elements supported on multiple browsers.

![Image](https://cdn-media-1.freecodecamp.org/images/1*k_pjGVXlRBVafs7tiocySA.png)
_From left to right: Angular Elements, Polymer and Stencil_

#### Tools

There’s a bunch of tools to help you make your components more accessible. A favorite of mine is the [Accessibility Developer Tools](https://chrome.google.com/webstore/detail/accessibility-developer-t/fpkknkljclfencbdbgkenhalefipecmb/related?hl=en), offered by Google Accessibility. It’s an excellent Chrome extension.

There’s also a lot of _linters_ out there to keep an eye on you (e.g., the current project I’m working on is a React one, so I’m using the **eslint- plugin-jsx-a11y** to keep an eye on me).

### TL;DR

Essential for accessibility are:

* Semantics
* Keyboard inputs
* Text alternatives
* Color Contrast

The building blocks of Web Components are:

* HTML Templates
* Shadow DOM
* Custom Elements
* …and a bit more

The basics for our code to be accessible are:

* Using the Role model
* Making our elements focusable
* Conveying a visual aid for the focused element
* Using ARIA labels
* Binding events to the keyboard

There’s also a way to extend the native behavior of an element through Extending HTML Interfaces.

### Finally, a lot of people that know way more than I do…

Regarding the accessibility of Web Components:

* [The Future of Accessibility for Custom Elements](http://robdodson.me/the-future-of-accessibility-for-custom-elements/), by Rob Dodson
* [Accessibility of Web Components](https://marcysutton.github.io/accessibility-of-web-components/slides.html#/slide5), by Marcy Sutton
* [How to Make Accessible Web Components](https://www.sitepoint.com/accessible-web-components/), by Artem Tabalin
* [Making Web Components Accessible](https://www.grapecity.com/en/blogs/making-web-components-accessible), by Bernardo de Castilho

Regarding accessibility in general:

* [Heck yes, accessibility — let’s make the future awesome](https://uxdesign.cc/future-tech-accessibility-e93600e8917e), by Mischa Andrews
* [Myth: Accessibility is ‘blind people’](https://a11yproject.com/posts/myth-accessibility-is-blind-people/), by Dave Rupert
* [Accessible UI Components for the Web](https://medium.com/@addyosmani/accessible-ui-components-for-the-web-39e727101a67), by Addy Osmani
* [The Accessibility Tree](https://developers.google.com/web/fundamentals/accessibility/semantics-builtin/the-accessibility-tree), by Meggin Kearney, Dave Gash and Alice Boxhall

Regarding Web Components in general:

* [Practical lessons from a year of building web components](https://www.youtube.com/watch?v=zfQoleQEa4w), by Monica Dinculescu
* [Accessibility is My Favorite Part of the Platform](https://www.youtube.com/watch?v=2qjgxH384Nc), by Rob Dodson
* [Polymer: making Web Components accessible](https://www.youtube.com/watch?v=_IBiXfxhF-A), by Google Developers (although a bit old, still makes perfect sense)

### …and the presentation.

_This article is based on a talk first lectured at a meet-up that happened on the [December 5th, 2018](https://www.meetup.com/landing_jobs/events/256720438/). You can find that presentation [here](http://cristianocorreia.com/styling-accessibility/)._

Thanks for reading, see you next time.

