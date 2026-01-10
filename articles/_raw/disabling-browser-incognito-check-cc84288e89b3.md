---
title: How to outsmart incognito block
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-27T05:34:54.000Z'
originalURL: https://freecodecamp.org/news/disabling-browser-incognito-check-cc84288e89b3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BgAlYI-fuv9BrHQHPnNZoQ.jpeg
tags:
- name: hacking
  slug: hacking
- name: incognito
  slug: incognito
- name: JavaScript
  slug: javascript
- name: Tampermonkey
  slug: tampermonkey
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Mátyás Fodor

  Recently I came across several sites that showed a warning or paywall because I
  was using incognito mode. I think it is unfair. I should be allowed to use whatever
  browser and mode I want. This is a way to enforce their tracking tools...'
---

By Mátyás Fodor

Recently I came across several sites that showed a warning or paywall because I was using incognito mode. I think it is unfair. I should be allowed to use whatever browser and mode I want. This is a way to enforce their tracking tools. I know that [incognito is not safe](https://thevpn.guru/is-incognito-mode-safe-secure/) but it’s the bare minimum you can do to avoid ads to track you.

The whole thing took me about two hours and I learned a lot about browser extensions and hacking client-side code as an end user. I thought this might be worth sharing.

First, I had to look up how to detect private mode. As per my best knowledge, there’s no browser API to detect private mode directly, so I was pretty sure it is a sneaky little script. [This](https://stackoverflow.com/a/27805491/2419215) StackOverflow answer gave me a hint, so I knew I’d have to look for `webkitRequestFileSystem`. I found [this](https://gist.github.com/matyasfodor/15e8863ab15baf4791a5fa4c748b64af) bit in one of those private loathing sites’ minified JavaScript code. Here’s the exciting part:

I could test the [module](https://gist.github.com/matyasfodor/15e8863ab15baf4791a5fa4c748b64af) by pasting it in incognito and public browser window dev console and run:

```
var module = {};incognito(null, module);module.exports.detectIncognito().then(console.log)
```

Bingo! This is it, I just have to find a way not to call the error callback in `window.webkitRequestFileSystem(..)`. The easiest way is to monkey patch the function:

```
(function(webkitRequestFileSystem) {  window.webkitRequestFileSystem = function(t, s, success, error) {    webkitRequestFileSystem(t, s, success, success);  }})(window.webkitRequestFileSystem);
```

If you’re not familiar with the technique, [monkey patching](https://www.audero.it/blog/2016/12/05/monkey-patching-javascript/) is a way to add, modify, or suppress the default behavior of a piece of code at runtime without changing its original source code.

**Detour 1:** First I started writing my own chrome extension using [Extensionizr](https://extensionizr.com). It’s a great tool generating Chrome extension boilerplate code. But in the end, I found an easier solution.

Whenever it comes to customizing websites I use [Tampermonkey](https://tampermonkey.net/) (for example [hiding job ads](https://gist.github.com/rjrudman/a472924d3fb078bd73bb12066e0319a0) on Stack Overflow when I really shouldn’t spend time on looking for new positions). You don’t have to install a n+1th extension, and it provides a nice interface to manage your scripts. Ok, nice is probably an exaggeration, it’s ugly but handy.

So I added the monkey patch script I referenced above, already giggling how easy it was, but bummer, it didn’t work. I tried a few other things for example:

```
window.foobar = 'baz';
```

But in the dev console, this property was absent from the `window` variable. It turned out [content scripts](https://stackoverflow.com/a/20513730/2419215) are running in an isolated environment, they only share the DOM with the webpage’s scripts. I started to work with the referenced solution from SO. There was one very important thing though, I had to execute this code before the current page’s code. Here’s what I came up with:

```
function injectScript(file_path, node) {        var element = document.createElement('script');        element.setAttribute('type', 'text/javascript');        element.setAttribute('src', file_path);        element.setAttribute('async', false);        node.appendChild(element);}injectScript(url, document.documentElement);
```

**Detour 2:** As I started with an extension, loading another JavaScript file was trivial. However it’s not the case with Tampermonkey scripts (at least I don’t know about it). So I decided to put my code in a GitHub gist, and tried to load the [raw file](https://gist.githubusercontent.com/matyasfodor/ab6c92e32a35ebae0bebedff8e7cf569/raw/4f97a8fb702ae8710ba9542b5a7a8127495cf9e4/fakepublic.js). But then the browser was complaining about its MIME type. Finally I ended up using [https://rawgit.com/](https://rawgit.com/), which was exactly the right tool for this.

I realized that I should add those few lines of monkey patch code as a string, and fill in the script element’s text with that. Here’s my final solution:

An important thing to know if you work with Tampermonkey in incognito mode: your changes made in incognito mode won’t appear in normal mode, and vice versa: you have to close all your private windows if you want to try your latest changes made in public mode.

**Be careful!** If you decide to use my script, you have to know that this _might_ (although not very likely) break some web pages. You can always turn these off in Tampermonkey. Use it at your own risk.

