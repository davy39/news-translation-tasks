---
title: How to optimize your JavaScript app by using service workers
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2019-09-02T12:31:08.000Z'
originalURL: https://freecodecamp.org/news/optimize-your-javascript-app-by-using-service-workers
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca08e740569d1a4ca4963.jpg
tags:
- name: JavaScript
  slug: javascript
- name: optimization
  slug: optimization
seo_title: null
seo_desc: 'Every now and then we hear about optimizing something. There are different
  kinds of optimizations we can do to make our apps faster and more efficient, or
  to save time or memory. This article will cover one of those methods — s_ervice_
  w_orkers._

  TL;...'
---

Every now and then we hear about optimizing something. There are different kinds of optimizations we can do to make our apps faster and more efficient, or to save time or memory. This article will cover one of those methods — s\_ervice\_ w\_orkers.\_

### TL;DR

This tutorial explains what a *service worker* is and how to use it, in JavaScript. There is a code example at the end of it. If you want to skip the reading, [here](https://github.com/mihailgaberov/learn-service-workers) is the Git repo and [here](https://compassionate-brahmagupta-71d9b4.netlify.com/) you may see a live demo.

### The Theory

Let’s see first what a w\_orker\_ is this ? and what s\_ervice\_ can we use it for ?.

The *service worker* is a [simple script](https://developers.google.com/web/fundamentals/primers/service-workers/). It's JavaScript code, that your browser runs in the background, separate from a web page.

It’s very convenient to use service workers for features that don’t need a web page or user interaction. One of the most common uses is intercepting and handling network requests. This includes managing a cache of responses.

The following is a simple example of how to include a service worker in your application.

Usually, in the entry point of your app, you add this code:

```js
if ('serviceWorker' in navigator) {  
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/service-worker.js');  
    });
}
```

This way of using service workers is a little bit improved than the basic one. The basic method involves directly calling the *register*() method inside the *if statement.* In this case, we use the window load event to register the service worker after the page has finished loading. After doing this, you need to add your service worker code in the *service-worker.js* file. At this point, you might want to take a look at my service worker file.

*All major browsers support Service Workers now, and you can start using them right away.*

### The Example

Enough theory, let’s build a real example app that will leverage the service workers feature.

Let’s imagine we are building an app that needs to load a big chunk of data. It could be, for example, a nice, big full-screen image we display on the front page. Or it could be a big video clip we have to wait to load. This is an ideal use case for a service worker to shine. Let’s see how. ?

In our specific case, we will use the clock time to show the benefit of using service workers. What I mean is, that we will build a simple app, showing the time. It will have a nice, big button for fetching a nice, big image. And it will provide the user with an option to choose **to use or not** a service worker.

Here is a screenshot of how it looks:

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_2K-IvfpcK017rGsX1Hsm8w.png align="left")

What this app demonstrates is, that when fetching the image (by clicking the button, wow!) with an active service worker — we don’t get blocked UI (user interface, i.e. fields, buttons, ?). If you choose not to use the service worker, you will get a frozen UI for a certain period of time. When the work completes and the main thread frees itself, it will unfreeze the UI.

If you don’t want to clone and run the code yourself, jump straight to the [live demo](https://compassionate-brahmagupta-71d9b4.netlify.com/).

### Conclusion

This demo of service workers in action shows us the advantage we get from using them. Especially when you are trying to build responsive and robust JavaScript applications. No user wants to end up in a frozen page for an unknown time, as no developer should want that for his application’s users. Keeping in mind the above, service workers are a *must* now. And we should not neglect them.

? Thanks for reading! ?
