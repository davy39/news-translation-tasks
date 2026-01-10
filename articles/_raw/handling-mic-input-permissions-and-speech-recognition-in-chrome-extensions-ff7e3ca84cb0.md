---
title: How to handle mic input permissions and speech recognition in Chrome extensions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-12T13:00:42.000Z'
originalURL: https://freecodecamp.org/news/handling-mic-input-permissions-and-speech-recognition-in-chrome-extensions-ff7e3ca84cb0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kCWG1pjJyxUfKwblYn1gKA.jpeg
tags:
- name: Google Chrome
  slug: chrome
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Palash Taneja

  This tutorial assumes that you have a basic understanding of Chrome extensions and
  the associated configuration files. If not, then you can refer to this article which
  sets up the files for this tutorial.

  Setting up microphone record...'
---

By Palash Taneja

This tutorial assumes that you have a basic understanding of Chrome extensions and the associated configuration files. If not, then you can refer to [this article](https://medium.freecodecamp.org/how-to-create-a-chrome-extension-part-1-ad2a3a77541) which sets up the files for this tutorial.

Setting up microphone recording permissions in a Chrome extension is a gray area. There is no officially documented way to do it, and developers are forced to use a “hack” to get mic permissions for their Chrome extension.

In this short article, we use the `options.html` page to get microphone permissions and use the popular `[annyang.js](https://github.com/TalAter/annyang)` [library](https://github.com/TalAter/annyang) for detecting speech from the user.

### 1. Creating a permissions trigger script and page

To get around Chrome’s restrictions, we use a web page from our extension like `options.html` and`popup.html` to get mic permissions for the entire extension.

First, we need to create a JavaScript file to get mic permissions on a web page. I created a minimal file that requests permission to use the mic from chrome.

```js
$(document).ready(function(){
    navigator.mediaDevices.getUserMedia({audio: true})
});
```

If you’re not a fan of using JQuery, then you can embed this JS code at the end of the HTML page file that you intend to use as a permission trigger.

For our extension, TalkToMe, we used `options.html` as our permission trigger page.

### 2. Opening the trigger page automagically

The mic permission popup will only be opened if the trigger page was opened in the current browser session. Having the user manually open it everytime is bad UX. We created a background script to get around this.

```js
setTimeout(() => {
    navigator.mediaDevices.getUserMedia({ audio: true })
    .catch(function() {
        chrome.tabs.create({
            url: chrome.extension.getURL("options.html"),
            selected: true
        })
    });
}, 100);
```

It tries to access the mic every 100 ms, and opens the permission-trigger page if the request is denied by Chrome.

For the script to work, you need to add it to your `manifest.json` with other background scripts.

```js
... 

"background": {
    "scripts": [
      ..
      "js/auto-trigger.js", // add the script here
      ..
    ],
    "persistent": false
  },

...
```

### 3. Hooking up Annyang for speech recognition

Annyang provides a versatile library for speech recognition, and it is 100% free to use.

It works on a command-based structure, in that it calls functions based on the user’s speech. This feature made it a perfect fit for TalkToMe.

You can add the `annyang.js` code to a background script and start using it. Here I am showing you the Hello World example from the docs.

```js
if (annyang) {
  // Let's define a command.
  var commands = {
    'hello': function() { alert('Hello world!'); }
  };

  // Add our commands to annyang
  annyang.addCommands(commands);

  // Start listening.
  annyang.start();
}
```

And ta-da, just like that you have replicated our hours of searching StackOverflow for adding mic permissions to your chrome extension.

If this tutorial helped you, we’d really ❤️ if you could give your thoughts on our extension [TalkToMe](https://chrome.google.com/webstore/detail/talktome/nefaaifpggpfdjlfhfbcgfcjimlgpocc), even if you may not be a visually impaired user.

