---
title: 'High Performance Apps: Multiplexing, Debouncing, System Fonts, and other tricks'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-22T17:36:58.000Z'
originalURL: https://freecodecamp.org/news/high-performance-apps-multiplexing-debouncing-system-fonts-and-other-tricks-37c6fd3d7b2d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Y9Wf1Py9tQd3nc4l0AFsCQ.png
tags:
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Atila Fassina

  Here are some performance tips for your client-side application that you can start
  using immediately.

  These will boost your app’s perceived performance significantly. And most of them
  only require quick tweaks to your app.

  Preload yo...'
---

By Atila Fassina

Here are some performance tips for your client-side application that you can start using immediately.

These will boost your app’s [perceived performance](https://en.wikipedia.org/wiki/Perceived_performance) significantly. And most of them only require quick tweaks to your app.

### Preload your resources

`rel="preload"` is a way of letting your browser know that a specific resource is important. This way, your browser will fetch the resource as quickly as possible. Then it will store it locally until it finds the expected reference in the DOM.

Here are some examples of using a `link` with this attribute:

The `as` attribute is mandatory here, because it tells the browser what filetype that it is fetching. This way it can interpret the request and add the proper headers. Otherwise, your request would have the incorrect `mime/type` so your browser wouldn’t be able to parse it.

By the way, `mime/type` is the file type declaration that developers use on the web. This is similar to the file extensions on your desktop operating system. If you have the incorrect `mime/type`, the browser won’t know how to parse the file.

Font files are a bit trickier to preload. Here are some things to keep in mind:

* `crossorigin` —The [W3C](https://en.wikipedia.org/wiki/World_Wide_Web_Consortium) requires that font fetches be anonymous. In a nutshell, this means even when the request is coming from the same domain, it will be treated as a cross-origin request.
* `type` — This specifies which format the browser should use when fetching the font.

Also, be sure to only add the first format to your `font-face` declaration. Preloading multiple font formats is against best practices, is bad UX, and wastes your users’ bandwidth.

You can [read more about preloading here](https://caniuse.com/#search=preload).

### Use Operating System-specific fonts

By using system fonts, it’s possible to emulate your users’ Operational System’s look and feel. This way, your application has a better chance of looking like a native one, while saving your user the trouble of downloading more resources.

Let's analyze more closely each of these declarations:

* _apple-system_: as the name suggests, these target OSX/iOS-related systems
* _system-ui_: these target the system font, regardless of the system
* _BlinkMacSystemFont_: Chrome’s font on MacOS
* _Segoe UI_: Windows/Windows Phone
* _Roboto_: Android

This solution is widely used even though many developers don’t yet know about it. For example, at time of writing this article, it's used at:

* GitHub
* Wordpress
* Bootstrap
* Medium
* Ghost
* Zeit

And probably others that I haven't yet heard about.

### Debounce and throttle calls to your server

Some events get fired many times more than we intend to trigger them. For example: resize, scroll, keypress/keydown/keyup, or change.

Resize and scroll, for instance, get fired on _every_ pixel. That’s an awful lot of chatter if you just want to adjust some elements on breakpoint, or add a class to a header as the user scrolls down the page.

If you get an autocomplete, for example, you don’t want to fire on every key press. In most cases, it would be good to start autocompleting after the 3rd character. Especially if you plan to fetch information for that.

**Debounce** holds up your trigger until the event stops firing for a given amount of time (usually 500 milliseconds).

**Throttle** holds up your trigger if it attempts to fire more often than a given interval (usually 25o milliseconds).

### Use async/defer

Remember the good old `window.onload` function? Or moving all the scripts to the bottom of your HTML? Yeah, well, `async` and `defer` are here to give you some better options.

**Async** will download your script during the HTML parsing. It will run it asynchronously (if possible) — regardless of where it’s declared.

**Defer** will also download your script during the HTML parsing, though it will only attempt to run your script after the parser is finished. Also, declaring multiple deferred scripts guarantees that they will be executed in declaration order.

```
<script async src="./my-async-script.js"></script><script defer src="./my-deferred-script.js"></script>
```

### data:uri and <svg>

When adding icons or small image files, an interesting technique is to use `data-uri`. A `data` URL is usually encoded as `base64` and provides an easy way of embedding files into your DOM directly. In a similar way, you can add `<s`vg> as markup. This way your SVG image will be parsed and rendered by the browser.

Note that using the `<s`vg> instead of embedding `as an` <img> or icon-font brings other functionalities that are beyond the scope of this article.

Adding the files straight into your markup instead of referencing them saves you one HTTP request each time. This is nice when your file is so small that it isn’t worth the trouble of making a roundtrip to the server. Especially while on mobile networks, since [handshakes](https://en.wikipedia.org/wiki/Handshaking) can be quite expensive.

### Use Multiplexing

If your server is already working with HTTP2, embedding files might not be worthwhile. This happens because HTTP2 has a feature called **Multiplexing.**

This means your browser can send multiple requests and receive multiple responses "_bundled_" into a single TCP connection. So the workload associated with DNS lookups and [handshakes](https://en.wikipedia.org/wiki/Handshaking) is saved for files coming from the same server.

In addition, HTTP2 also provides you with **Server Push.** This means it’s possible to send files even before the user requests them. This increases the perceived performance significantly.

I hope these tips help you improve the perceived performance of your app. If you found this article helpful, give me some claps ?. You can also give me feedback on this on T[witter.](https://twitter.com/atilafassina)

### Further Reading

#### On rel=preload:

* [SmashingMagazine — Preload What is it Good for](https://www.smashingmagazine.com/2016/02/preload-what-is-it-good-for/)
* [Zach Letherman — Preload](https://www.zachleat.com/web/preload/)

#### On system fonts:

* [Bitsofcode — The New System Font Stack?](https://bitsofco.de/the-new-system-font-stack/)
* [Normalize.css — issue#665](https://github.com/necolas/normalize.css/issues/665)

