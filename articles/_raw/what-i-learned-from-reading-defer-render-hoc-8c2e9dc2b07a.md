---
title: What I learned from reading defer-render-hoc and why it’s useful.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-24T03:24:40.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-from-reading-defer-render-hoc-8c2e9dc2b07a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lrJvFE4XDFi5TU6g9Qzumg.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: user experience
  slug: user-experience
seo_title: null
seo_desc: 'By Anthony Ng


  This is another article for my Deliberate Practice. Why am I doing this? Read this
  article to learn more.


  I was reading through this article about how Twitter Lite (a React PWA) removed
  performance bottlenecks.


  _Image from [Twitter L...'
---

By Anthony Ng

> This is another article for my Deliberate Practice. Why am I doing this? [Read this article to learn more](https://medium.freecodecamp.org/deliberate-practice-becoming-an-open-sourcerer-27a4f7640940).

I was reading [through this article](https://medium.com/@paularmstrong/twitter-lite-and-high-performance-react-progressive-web-apps-at-scale-d28a00e780a3) about how Twitter Lite (a React PWA) removed performance bottlenecks.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P0WB3eCNtNZjOYzQ7Gd6Lw.gif)
_Image from [Twitter Lite article](https://medium.com/@paularmstrong/twitter-lite-and-high-performance-react-progressive-web-apps-at-scale-d28a00e780a3" rel="noopener" target="_blank" title=")_

When the user taps the `Home` button, there is a delay until the tweets are shown. This delay was caused by a large number of components mounting and unmounting. `defer-render-hoc` is an Open Source project that implements the solution given in the article.

### Let’s look at the code

`defer-render-hoc` is a Higher Order Component (HOC). To learn more about it, read the [documentation here](https://reactjs.org/docs/higher-order-components.html).

We use `defer-render-hoc` by wrapping your Expensive Component with it.

`defer-render-hoc` renders `null` on the initial render.

So when will `defer-render-hoc` render your Expensive Component? It uses `requestAnimationFrame` to wait two frames. After two frames have passed, it will render your Expensive Component.

`requestAnimationFrame` is usually used to create smooth animations ([read more about it in this article](https://developers.google.com/web/fundamentals/performance/rendering/optimize-javascript-execution)).

Here, we are using `requestAnimationFrame` to allow other components to update and give control back to the user. After the two frames, our Expensive Component takes over.

### Demo

Check out this [CodeSandbox for a demo](https://codesandbox.io/s/pjxkjjxv8m) of `defer-render-hoc`.

Click from the `Cheap page` button to the `Expensive page` button. Notice how the button stays blue as the UI freezes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*n07TLpSGmwdjHKXNQTvBHQ.png)
_(without defer-render-hoc) 624.02 ms for the click event_

Our click event takes 620ms. The click event does not finish until our Expensive Component mounts. Because of that, the screen is frozen for the user.

Now, click from the `Cheap page` button to the `Deferred Expensive page` button. Notice how the button does not stay blue, and the UI is not frozen.

![Image](https://cdn-media-1.freecodecamp.org/images/1*p12mxsrFus6uqzKBFofIxQ.png)
_(with defer-render-hoc) 16.71 ms for the click event_

Our click event takes 16ms. The click event doesn’t wait for our Expensive Component to mount; the work is deferred. The screen doesn’t freeze.

### How does this help?

The same amount of work still happens. The Expensive Component still mounts; it just mounts later. The experience itself is not faster overall. It might even be slower with the overhead of the `defer-render-hoc`. But sometimes a faster perceived experience is more important than an actual faster experience. See the below links for more information about perceived performance.

* [https://en.wikipedia.org/wiki/Perceived_performance](https://en.wikipedia.org/wiki/Perceived_performance)
* [https://medium.com/@lukejones/a-designers-guide-to-the-perception-of-performance-fedb4bd102b](https://medium.com/@lukejones/a-designers-guide-to-the-perception-of-performance-fedb4bd102b)

Depending on your project, `defer-render-hoc` might be right for you.

