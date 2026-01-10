---
title: Features of the Chrome API you should know
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2018-12-28T17:27:17.000Z'
originalURL: https://freecodecamp.org/news/features-of-the-chrome-api-you-should-know-bf5c8b6c7733
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Got1zk0gpNuHC0V1
tags:
- name: Google Chrome
  slug: chrome
- name: coding
  slug: coding
- name: development
  slug: development
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: So you think you know your way around building a Chrome extension? Well,
  that’s all fine and dandy, but have you heard about context menus? Messaging between
  scripts? Adding a badge to your extension’s icon? If all this sounds fascinating,
  you’re in ...
---

So you think you know your way around building a Chrome extension? Well, that’s all fine and dandy, but have you heard about context menus? Messaging between scripts? Adding a badge to your extension’s icon? If all this sounds fascinating, you’re in luck. We’ll go over some cool features the Chrome API grants us.

If you are interested in reading about how to build a Chrome extension, you can read my previous article [here](https://medium.freecodecamp.org/how-to-implement-a-chrome-extension-3802d63b5376). If you want to know how to publish one, you can read all about it [here](https://medium.freecodecamp.org/chrome-extension-how-to-publish-dd8400a3d53)

### [Context Menu](https://developer.chrome.com/extensions/contextMenus)

To put it simply, the context menu is the menu that appears when you right-click anywhere inside the browser. You can add your Chrome extension to that menu with a few simple steps:

1. Add **context-menus** to the **permissions** key in the manifest
2. Add a 16x16 icon (as it will be used in the context menu)
3. Add the following code to your background script:

### [Storage](https://developer.chrome.com/extensions/storage)

Similar to [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API#localStorage), the Chrome API allows saving data as objects, which persists even when the browser is closed and reopened. Here are the necessary steps to allow storage usage in your extension:

1. Add **storage** to the **permissions** key in the manifest
2. To put data in the storage, you use:

3. To pull data from the storage you use:

> ⚠️ Do NOT put sensitive user data in the storage since it is not encrypted

### [Messaging](https://developer.chrome.com/extensions/messaging#simple)

Chrome has another nifty feature which lets you pass messages along between scripts. For example, in your extension, you have your popup.js file that deals with things related to the popup window and you have a background script. If you wanted to have those two scripts communicate with each other you could use the following methods:

**SendMessage**

**Listen In On Incoming Messages**

### Badges

You know them, you love them, and you can add them to the icon of your extension. Make sure to be aware that due to its small size, the text you want to display is limited to **_four characters_**.

To set the background color of the badge you use:

To set the text of the badge you use:

In both methods, the callback is an optional parameter you can use after the method finishes its action.

Have other Chrome APIs you want to know about? Want to ask something? Feel free to reach out.

_If you liked this article, clap away so that others can enjoy it as well! ?_

