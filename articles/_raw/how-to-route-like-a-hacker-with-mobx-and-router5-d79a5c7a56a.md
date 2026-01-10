---
title: How to route like a hacker with MobX and router5
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-23T09:10:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-route-like-a-hacker-with-mobx-and-router5-d79a5c7a56a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HFkjeBT-TZJ2e-4idMK3Gw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Eugen Kiss

  Routing that fits your app — not the other way round


  _Photo by [Unsplash](https://unsplash.com/photos/AyYW_bUWerc?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">Rob Bates on ...'
---

By Eugen Kiss

#### **Routing that fits your app** — not the other way round

![Image](https://cdn-media-1.freecodecamp.org/images/1*HFkjeBT-TZJ2e-4idMK3Gw.jpeg)
_Photo by [Unsplash](https://unsplash.com/photos/AyYW_bUWerc?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Rob Bates</a> on <a href="https://unsplash.com/search/photos/route?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

There are many ways to approach routing in client-side apps. Frameworks like Android provide powerful but also complex and sometimes restrictive routing mechanisms. The same applies to full-fledged routing libraries in the frontend like React Router.

The good news is that you can write your own routing layer that is simpler without giving up control: **Routing that fits your app**—not the other way around!

To illustrate these concepts, let’s write a HackerNews app and **take control of routing**. We will use [React](https://reactjs.org/), [MobX](https://mobx.js.org/) and [router5](http://router5.github.io/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*2cCaL3YcvzflnIjfzyMAmw.png)

This is the [live](https://codesandbox.io/s/github/eugenkiss/hacker-routing-mobx-router5) result:

The example uses [HNPWA API](https://github.com/tastejs/hacker-news-pwas/blob/master/docs/api.md). [Here’s the Github project](https://github.com/eugenkiss/hacker-routing-mobx-router5/).

Let’s start by defining the _Feed_ route:

The properties `name`, `path`, and `comp` are obvious. With `link` you have **type-assisted reverse routing.** In the lifecycle function `activate` , you update global state and perform API requests. The dependency `store` is your central state management and action control panel. In the last line, you add `FeedRoute` to your route registry `routes`.

The cool thing about `FeedRoute` is that **everything relevant for routing to/from the _Feed_ screen is defined in one place**. Plus, you don’t need a container component for performing API requests.

Here’s how you render the current route:

The observable property `store.route` contains the current route. In your route registry `store.routes` you find the corresponding route definition. So, you know which component to render. If you’re on `/` the component will be `<FeedScree`n/>. By being an obse`rve`r, App rerenders whenever the obser`vable store`.route changes.

**That’s the gist!**

#### Getting it set up

How do you set all this up with [MobX](https://mobx.js.org/) and [router5](http://router5.github.io/)? Who updates the current route? What does `store` look like? To find out, read on!

_Aside_: Although a routing library is not required, I do recommend router5. It gives you a more convenient API (+ hooks and utilities) than the browser’s native one.

The router5 plugin definition:

A [router5 plugin](http://router5.github.io/docs/plugins.html) implements lifecycle functions. On a successful transition, you deactivate the previous route. Then you set `store.route` to the next route and activate the next route. Deactivation performs cleanup. Activation performs API requests and other initialization logic. The rest of the code is router5 API specific.

Here are the relevant parts from `store`:

The selected feed is derived from the URL. **There is no duplication of state thanks to [MobX’s propagation power](https://hackernoon.com/becoming-fully-reactive-an-in-depth-explanation-of-mobservable-55995262a254)**!

_Aside_: I use a special fetching helper which will be a topic for another article.

In my own [HackerNews client](https://github.com/eugenkiss/hnclient/) ([live](https://hn.eugenkiss.com/)), a history stack keeps track of the visited routes. It is used to render the screens on top of each other. All but the top-most screen have `display` set to `none`. This makes going back to the previous screen on mobile devices **much faster**!

My router also performs view state restoration. Think scroll position. But you can just as well keep it as minimal as shown here. Remember, you are in control of routing: do it in a way best suited to your app. See also React Router’s [scroll restoration](https://reacttraining.com/react-router/web/guides/scroll-restoration) discussion and router5’s [loading async data](http://router5.github.io/docs/async-data.html) dicussion.

The presented approach is inspired by:

* [How to decouple state and UI (you don’t need componentWillMount)](https://hackernoon.com/how-to-decouple-state-and-ui-a-k-a-you-dont-need-componentwillmount-cc90b787aa37)
* [A different approach to routing in Single-Page Applications](https://vincent.is/testing-a-different-spa-routing/)

If you enjoyed this article, please recommend and share. Happy Routing!

