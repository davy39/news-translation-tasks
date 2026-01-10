---
title: Why you should care about supporting older browsers
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-01-11T17:08:34.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-care-about-supporting-older-browsers-39bbc28fb7fd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U_gLONEItc8d9fmZuGb8Fw.png
tags:
- name: Browsers
  slug: browsers
- name: CSS
  slug: css
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
seo_title: null
seo_desc: 'Supporting older browsers

  You don’t have to worry much about supporting older browsers today. They’ve been
  decent ever since Internet Explorer 8 died.

  But the question remains: How should you go about supporting Internet Explorer 9
  and other browsers...'
---

### **Supporting older browsers**

You don’t have to worry much about supporting older browsers today. They’ve been decent ever since Internet Explorer 8 died.

But the question remains: How should you go about supporting Internet Explorer 9 and other browsers? In the first place, should you even be thinking about supporting Internet Explorer 9?

We’ll look at a few things you’d want to consider.

#### Think features, not browsers

Let’s say the world contains only two features and two browsers.

1. Browser A supports feature A but not feature B.
2. Browser B supports feature B but not feature A.

It’s possible to detect what browsers support what features and act from there.

```
// This is JavaScript
```

```
if (Browser A) {  // Code for A}
```

```
if (Browser B) {  // code for B}
```

But what if there are more browsers? What if the world contains browsers C, D, and E? It gets hard to support the features you need if you’re thinking about browsers.

There’s a better way: You can check whether a feature exists. If it exists, use it. If not, provide fallback code.

The following block of code works from browser A to browser Z.

```
// This is JavaScript
```

```
if (feature A) {  // Code if browser contains feature A} else {  // Code if browser doesn't contain feature A}
```

And now you don’t have to worry about browsers.

#### Deciding whether to use a feature

Many people decide whether to use a feature depending on the number of browsers that support it. But, as I argued above, **browsers don’t matter.**

What matters is: Can you code the fallback for the feature easily? **If you can code the fallback easily, go ahead and use the feature.** If you can’t code the fallback easily, don’t use the feature.

#### Deciding what browsers to support

You still need a cutoff.

What browsers are you going to support?

What browsers are you NOT going to support? If you don’t want to support the browser, then it doesn’t make sense for you to write fallback code for it.

My best answer is: Watch who is using your site. What browsers do they use? Follow accordingly.

Yes, there may be outliers who try to visit your website on Internet Explorer 6. But do have the time and energy to write extra code for a browser that almost no one uses?

Will your energy be better spent elsewhere?

#### The level of support

I’d argue there are four levels of support:

1. everything must look and work the same in all browsers
2. the site must look the same, but functionality can be different across browsers
3. functionality must be the same, but looks can be different across browsers
4. looks and functionality can both differ across browsers

What kind of support are you providing to the older browsers? Why?

#### Wrapping up

Think about it:

1. why are you trying to support the old browser you’re trying to support?
2. what level of support are you giving?
3. is it worth the resources you’ve allocated?

### Supporting Older Browsers — CSS

There are two ways to provide fallbacks for CSS features:

1. property fallbacks
2. feature queries

#### Property fallbacks

**If a browser doesn’t recognize a property or its corresponding value, the browser will ignore the property altogether.**

When this happens, the browser uses — or falls back — to the previous value it finds.

This is the easiest way to provide a fallback.

Here’s an example:

```
.layout {  display: block;   display: grid; }
```

In this example, browsers that support CSS Grid will use `display: grid`. A browser that doesn’t support CSS Grid will fall back to `display: block`.

#### Omit default values

If the element you’re using defaults to `display: block`, you can omit the `display: block` declaration. This means you can support CSS Grid with one line of code:

```
.layout {  display: grid; }
```

Browsers that support CSS Grid will be able to read other CSS properties like `grid-template-columns`. Browsers that don’t support CSS Grid can’t.

This means you can write additional CSS Grid properties without worrying about fallback values.

```
.layout {  display: grid;   grid-template-columns: 1fr 1fr 1fr 1fr;  grid-gap: 1em; }
```

Feature queries, or `@supports`, tell you whether a CSS property or its corresponding value is supported is supported by the browser.

**You can think of CSS feature queries like `if/else` statements in JavaScript.** They look like this:

```
@supports (property: value) {  /* Code when property or value is supported*/}
```

```
@supports not (property: value) {  /* Code when property or value is not supported */}
```

`@supports` is helpful if you want browsers to read CSS **only** if they support a specific property.

For the CSS Grid example we had above, you can do this:

```
@supports (display: grid) {  .layout {    display: grid;     grid-template-columns: 1fr 1fr 1fr 1fr;    grid-gap: 1em;     padding-left: 1em;    padding-right: 1em;  }}
```

In this example, `padding-left` and `padding-right` will only be read by browsers that support both `@supports` **and** CSS Grid.

Jen Simmons has a better example of `@supports` at work. She uses feature queries to detect whether browsers support a property like `-webkit-initial-letter`.

```
@supports (initial-letter: 4) or (-webkit-initial-letter: 4) {  p::first-letter {     -webkit-initial-letter: 4;     initial-letter: 4;     color: #FE742F;     font-weight: bold;     margin-right: 0.5em;  }}
```

![Image](https://cdn-media-1.freecodecamp.org/images/p8pNpSgs7lVe7s8qunRS66fvJSPEaEBaxsHo)

Jen’s example brings us to a question: Should sites look the same across browsers? We’ll look at this later. But first, more about feature queries.

#### Support for feature queries

Features queries have gained [great support](https://caniuse.com/#search=feature%20queries). All current major browsers support feature queries.

![Image](https://cdn-media-1.freecodecamp.org/images/qZWyleUprSdhJB7VGUL0KCSG547I7d6nduaP)

#### What if a feature is supported, but feature queries aren’t?

This used to be the tricky part. Jen Simmons and other experts have warned us of this possibility. You can read how to handle it [in this article](https://hacks.mozilla.org/2016/08/using-feature-queries-in-css/).

Here’s my take: I don’t support IE 11 anymore, so I use feature queries in the way I mentioned above.

#### Using property fallbacks and feature queries at the same time

Take look at the following code. What padding values will browsers apply?

```
@supports (display: grid) {  .layout {    display: grid;     grid-template-columns: 1fr 1fr 1fr 1fr;    grid-gap: 1em;     padding-left: 1em;    padding-right: 1em;  }}
```

```
.layout {    padding-left: 2em;   padding-right: 2em; }
```

The answer is: All browsers will apply `2em` of left and right padding.

Why?

This happens because `padding-left: 2em` and `padding-right: 2em` were declared later in the CSS file. Properties that were declared later override properties that were declared earlier.

If you want to `padding-left: 2em` and `padding-right: 2em` to **apply only** to browsers that **don’t** support CSS Grid, you can swap the property order.

```
.layout {    padding-left: 2em;   padding-right: 2em; }
```

```
@supports (display: grid) {  .layout {    display: grid;     grid-template-columns: 1fr 1fr 1fr 1fr;    grid-gap: 1em;     padding-left: 1em;    padding-right: 1em;  }}
```

**Note**: It’s always a good practice to declare fallback code first in CSS because of its cascading nature.

This also means, if you’re using both `@supports` **and** `@supports not`, you should declare `@supports not` first. It makes your code consistent.

```
/* Always write "@supports not" first if you use it */@supports not (display: grid) {  .layout {      padding-left: 2em;     padding-right: 2em;   }}
```

```
@supports (display: grid) {  .layout {    display: grid;     grid-template-columns: 1fr 1fr 1fr 1fr;    grid-gap: 1em;     padding-left: 1em;    padding-right: 1em;  }}
```

Now let’s talk about whether sites should look the same across browsers.

#### Should sites look the same across browsers?

Some people believe that sites should look the same across browsers. They think that branding is important, and stress that sites should look consistent to preserve the brand.

Other people say no. They believe they should embrace the spirit of progressive enhancement. They can give users better browsers more love.

Both views are right, but they come from different angles.

**The most important point of view comes from users.** Is your site able to provide users with what they came for?

If yes, you don’t have to be too strict on the consistency. Go ahead and give users with better browsers even better experiences!

#### Wrapping up

To provide support for CSS features, you can use:

1. Property fallbacks
2. Feature queries

When you write CSS, make sure you declare fallback code first before the other set of code for browsers with better support.

### Supporting Older Browsers — JavaScript

It’s easy to provide JavaScript support for older browsers. Most of the time you just need to use a polyfill.

But there are more things you can do.

#### What’s a polyfill?

A polyfill is a piece of code that tells browsers how to implement a JavaScript feature. Once you add a polyfill, you don’t need to worry about support anymore. It’ll work.

Here’s how a Polyfill works:

1. it checks whether the feature is supported
2. if not, it adds code to support the feature

Here’s an example of a polyfill at work. It checks if the browser supports `Array.prototype.find`. If the browser doesn’t support `Array.prototype.find`, it tells the browser how to support it.

You can find this code on [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find).

```
if (!Array.prototype.find) {  Object.defineProperty(Array.prototype, 'find', {    value: function(predicate) {     // 1. Let O be ? ToObject(this value).      if (this == null) {        throw new TypeError('"this" is null or not defined');      }
```

```
var o = Object(this);
```

```
// 2. Let len be ? ToLength(? Get(O, "length")).      var len = o.length >>> 0;
```

```
// 3. If IsCallable(predicate) is false, throw a TypeError exception.      if (typeof predicate !== 'function') {        throw new TypeError('predicate must be a function');      }
```

```
// 4. If thisArg was supplied, let T be thisArg; else let T be undefined.      var thisArg = arguments[1];
```

```
// 5. Let k be 0.      var k = 0;
```

```
// 6. Repeat, while k < len      while (k < len) {        // a. Let Pk be ! ToString(k).        // b. Let kValue be ? Get(O, Pk).        // c. Let testResult be ToBoolean(? Call(predicate, T, « kValue, k, O »)).        // d. If testResult is true, return kValue.        var kValue = o[k];        if (predicate.call(thisArg, kValue, k, o)) {          return kValue;        }        // e. Increase k by 1.        k++;      }
```

```
// 7. Return undefined.      return undefined;    },    configurable: true,    writable: true  });}
```

**Note**: A polyfill is a subset of a shim. A shim is a library that brings a new API to an older environment.

#### Using polyfills

There are two ways to use polyfills:

1. polyfill manually, like in the example above
2. adding many polyfills at once through a library

#### Polyfilling manually

First, you need to **search for the polyfill** you need. You should be able to find one if you google around. Smart developers have created polyfills for almost everything you’ll ever need.

Once you found the polyfill, **use the above process** to create provide support to older browsers.

#### Adding many polyfills at once

**Some libraries contain many polyfills.** [ES6-shim](https://github.com/paulmillr/es6-shim) is one example of such a library. It provides support for all ES6 features on older browsers.

#### Using cutting-edge JavaScript features

If you want to use cutting-edge JavaScript features, consider adding [Babel](https://babeljs.io) into your build process.

Babel is a tool that compiles JavaScript. During this compile process, it can:

1. add any shim / polyfill you need
2. compile preprocessors into JavaScript

More on the second point:

Babel works offline in your build process. It can read files you pass into it, and then convert these files into JavaScript the browser can read.

What this means is you can use cutting-edge features like Flow, TypeScript, and other cool technologies you’ve heard about. They’ll all work in browsers, provided you pass them through Babel first!

#### What if polyfills aren’t enough?

If polyfills aren’t enough to support the feature, you might want to reconsider the amount of support you provide for the browser in question.

Do you need to provide the same functionality across different browsers? Maybe you should consider progressive enhancement instead.

Maybe you can code in a way that doesn’t use the feature?

Lots of maybes, but you get the drift.

#### How to tell if a browser supports the feature?

First, I check [caniuse.com](https://caniuse.com/). Write the name of the JavaScript feature you want, and you’ll be able to see browser support levels.

Here’s an example with [Abort Controller](https://caniuse.com/#search=Abort)

![Image](https://cdn-media-1.freecodecamp.org/images/UYLLYIDxtE5PLD6AnfiGsl71ynSKewV3fBFQ)

If [caniuse.com](https://caniuse.com/) doesn’t give me any information, I check MDN. You’ll find browser support at the bottom of most articles.

Here’s the example with [Abort Controller](https://developer.mozilla.org/en-US/docs/Web/API/AbortController) again:

![Image](https://cdn-media-1.freecodecamp.org/images/1S4zvx6y-EhvCev6kXUdR2LTVjNpUTirlgQr)

#### Beware the cost of JavaScript

When you use polyfills you add more JavaScript code.

The problem with adding more JavaScript is, well, there is more JavaScript. And with more JavaScript comes more problems:

1. older browsers usually live in older computers. They may not have enough processing power.
2. JavaScript bundles can delay site load. More on this in “[The cost of JavaScript](https://medium.com/@addyosmani/the-cost-of-javascript-in-2018-7d8950fbb5d4)“ by Addy Osmani

#### Wrapping up

It’s easy to add support for JavaScript features. Most of the time, you add a polyfill and call it a day. But be aware of the cost of JavaScript when you do so!

Sometimes, it might be good to ditch the feature entirely.

### Why support older browsers?

Why you have to care about old browsers?

Who uses old browsers? Probably, users with old computers?

If they use old computers, perhaps they don’t have money to buy a new one.

If they don’t have money to buy a new computer, they probably will not buy anything from you as well.

If they will not buy anything from you, why you have to care about supporting their browsers?

To a business person, that’s a perfectly reasonable train of thought. But why do we developers still insist on supporting older browsers?

**Let’s break it down**

There are so many layers of assumptions on the original thought process.

> “Who uses old browsers? Probably, users with old computers? If they use old computers, perhaps they don’t have money to buy a new one”.

While it’s true that people use old browsers because they use old computers, we cannot assume that people cannot afford to buy new ones.

* Maybe their company doesn’t want to buy them one.
* Maybe they’re happy with their computer, and they don’t want to upgrade.
* Maybe they don’t have the knowledge to upgrade their computers.
* Maybe they don’t have access to new computers.
* Maybe they’re bound to mobile phones that don’t have good browsers.

**Don’t assume.**

> If they don’t have money to buy a new computer, they probably will not buy anything from you as well. If they will not buy anything from you, why you have to care about supporting their browsers?

We have to zoom out into other areas to talk about this point.

#### Wheelchair accessibility

If you’ve been to Singapore, you’ll notice there’s a ramp or an elevator next to almost every staircase.

But why? Why do the government and private corporations spend money on elevators and ramps? Why build them when staircases are enough to bring people from a lower elevation to a higher one?

It turns out that some people aren’t able to use stairs. They can’t walk with their feet. They have to sit in wheelchairs, and they can’t wheel themselves up a staircase. The elevators and ramps serve these people.

And it turns out that more people benefit from elevators and ramps.

1. People who have weaker knees.
2. People who have a bicycle or scooter with them.
3. Parents who’re pushing a baby trolley.

If you find yourself pushing anything with wheels, you’ll use the ramp or elevator without thinking twice. You benefit too.

But the problem is: Nobody earns a single cent from operating the ramps or the elevators? So why build them?

Because it’s worth it.

And worth doesn’t always mean money.

#### Consider global warming

You live on Earth. What do you feel about global warming?

Some people don’t care. It’s okay if forests get burned. It’s okay if companies pollute rivers and release tonnes of carbon dioxide into the air. It doesn’t affect them.

But there’s a group of people that care. They love the planet we’re living on. They want to give their children a better place to live in. There are lots of reasons why they care. And they probably want to save as many resources as possible.

Where do you stand?

Would you give money to a company that destroys the earth while it operates?

Maybe you will. Maybe you won’t. Maybe you don’t care. All three options are valid.

And once again, you see, it’s not always about the money.

#### The web is for everyone

> The dream behind the Web is of a common information space in which we communicate by sharing information.

> — Tim Berners-Lee

We frontend developers are the custodians of the web. How the web turns out is up to us. We can’t force everyone to build ramps and elevators, but we can make sure we build them ourselves.

The choice is up to you, really.

You don’t have to care if you don’t want to.

Most good frontend developers I know? They care. They choose to be inclusive. It’s what makes us frontend developers.

We care.

But sometimes we also have constraints and limits. And we work with those limits.

This article was originally posted at [my blog.](https://zellwk.com/blog/)  
Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better front-end developer.

