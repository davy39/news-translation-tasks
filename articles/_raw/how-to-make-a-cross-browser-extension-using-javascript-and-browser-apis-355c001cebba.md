---
title: How to make a cross-browser extension using JavaScript and browser APIs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-09T02:33:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-cross-browser-extension-using-javascript-and-browser-apis-355c001cebba
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yRHXdpa4NCqkvmpuCwHwMQ.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By ryanwhocodes

  This tutorial will cover how to create a web extension that works across multiple
  browsers. It will show you how to structure a project and write JavaScript code
  to interact with the browser’s tabs, depending on which browser is being...'
---

By ryanwhocodes

This tutorial will cover how to create a web extension that works across multiple browsers. It will show you how to structure a project and write JavaScript code to interact with the browser’s tabs, depending on which browser is being used. This means you can code and then distribute one extension package to multiple browsers’ web stores.

![Image](https://cdn-media-1.freecodecamp.org/images/kUuZFfmNI4Oy6b0fZAn1Cyx-AHBtKs-bAekJ)

![Image](https://cdn-media-1.freecodecamp.org/images/ioSMcz0YSIxxxsjw7wG2zZhQ0wVevvnj4ZiE)
_Chrome Web Store and Firefox Add-ons are two places you can distribute your browser extension_

> This post will focus on the Chrome and Firefox browsers, along with distributing extensions via the [Chrome Web Store](https://chrome.google.com/webstore/category/extensions) and [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/) websites. Other browsers and distribution options are also available for web extensions.

Get started with a [template](https://github.com/ryanwhocodes/template-browser-extension) — copy, edit and publish!

To see a completed example, here’s a link to an extension I made called [Link Formatter](https://github.com/ryanwhocodes/link-formatter), with the cross-browser JavaScript within [popup.js](https://github.com/ryandav/link-formatter/blob/master/extension/js/popup.js). The same package is listed in both the Chrome and Firefox web stores.

![Image](https://cdn-media-1.freecodecamp.org/images/zaNl7-PsZ7FadRblrl2a9GMWp9m-WJ85n5mq)

### Browser extensions

Extensions are a fantastic way to extend the functionality of your browser, and they allow you to improve your experience online. If you are building your first one or want to learn more about them, I recommend the following tutorials:

* [Browser Extensions — Mozilla | MDN](https://developer.mozilla.org/en-US/Add-ons/WebExtensions)
* [What are extensions? — Google Chrome](https://developer.chrome.com/extensions)
* [Anatomy of an extension — Mozilla | MDN](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension)

#### Load your extension locally on your computer

When developing your extension, you can load it locally without having to publish and download it from an external website. The way you do this depends on which browser you are using.

**Chrome**

* Visit `chrome://extensions/` in your Chrome browser
* Click `Load Unpacked`
* Select the extension’s folder

**Firefox**

* Visit `about:debugging`
* Click on `Load Temporary Add-on`
* Select the `manifest.json` within the extension’s folder

**Debugging tip**: to view the console, (for example to see errors), right click/control click on the web extension icon or popup and select `inspect`

![Image](https://cdn-media-1.freecodecamp.org/images/8q3DZtGdXpJCA2r2EflBZeKZur0rnMFZYXPK)

### Writing JavaScript for your browser extension

There are many JavaScript API’s that can be used in your browser extension. This post will focus on the tabs API.

**For** **more on web extension APIs,** see [JavaScript APIs — Mozilla | MDN](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/API).

A browser extension that includes a popup HTML page when the user clicks on the icon in the browser’s toolbar could have a project structure like this:

```
extension├── css│   └── style.css├── js│   └── popup.js├── manifest.json└── popup.html
```

The `popup.html` page would then run the `js/popup.js` script at the bottom of the page. You would add your JavaScript here.

**Note**: other project structures could have a folder for library code, as well as JavaScript files that run in other areas of the extension. For example, in the extension’s [background scripts](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts), and in any other documents bundled with the extension, including [browser action](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_action) or [page action](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Page_actions) popups, [sidebars](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Sidebars), [options pages](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Options_pages), or [new tab pages](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json/chrome_url_overrides).

### Browser tab APIs

When writing a web extension, you need to use the tabs API to interact with the tabs in the browser. You also need to request permission from the user to do this.

#### Requesting permissions to access tabs

Permissions need to be set in `[manifest.json](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json)`. When a user tries to install the extension, it will prompt the user to confirm that this action is allowed.

```
"permissions": [    "tabs"  ]
```

![Image](https://cdn-media-1.freecodecamp.org/images/WPztqE9nS1rnC3FVnHjLcjsddLzCIqKc7dEV)
_Firefox is one of the browsers that uses the browser.tabs API_

#### Querying tabs with the browser API

Browsers, such as Firefox, use the `browser.tabs` API to interact with the browser’s tabs. To request info about the window’s tabs, you use the `query` method, which returns a promise with an array of tabs.

```
browser.tabs.query(  queryInfo  // object)
```

Read more about browser.tabs.query at [tabs.query() — Mozilla | MDN](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/API/tabs/query)

To request the active tab for the browser window, you would write the following JavaScript:

```
browser.tabs.query({active: true, currentWindow: true}) .then(logCurrentTabData)
```

To get the current tab, you retrieve the first tab from the returned array of tabs. Following this structure, you can get the data from the browser tab.

```
const logCurrentTabData = (tabs) => {  currentTab = tabs[0]  console.log(currentTab.title);  console.log(currentTab.url);}
```

However, when you try to open the extension in Chrome…

![Image](https://cdn-media-1.freecodecamp.org/images/Pipl2PdMBJPLrYhzJabKcSHspt21ODPRk07o)
_Trying to use the browser API in Chrome throws an error_

![Image](https://cdn-media-1.freecodecamp.org/images/MYFHaS25HFuF5JwfCgHRfxwDVdFWp6phcRKa)
_The Chrome browser uses the chrome.tabs API_

#### Querying tabs with the chrome API

Chrome has its own API for tabs queries. This follows the syntax `chrome.tabs` → your query

```
chrome.tabs.query(object queryInfo, function callback)
```

Read more about Chrome’s tabs API here: [chrome.tabs — Google Chrome](https://developer.chrome.com/extensions/tabs).

So to use this method call, you would write the following in your browser extension:

```
chrome.tabs.query(   {active: true, currentWindow: true},   (arrayOfTabs) => { logCurrentTabData(arrayOfTabs) });
```

### Combining tab queries

#### Detect which API to use

You can then include both types of browser queries in your extension by using a conditional statement to determine which one to use.

```
if(chrome) {  chrome.tabs.query(    {active: true, currentWindow: true},    (arrayOfTabs) => { logCurrentTabData(arrayOfTabs) }  );} else {  browser.tabs.query({active: true, currentWindow: true})    .then(logCurrentTabData)}
```

#### Adding more code for each browser type

Within each side of the condition, you can then add other pieces of code that depend on the different APIs, for example to create new tabs.

```
chrome.tabs.create()browser.tabs.create()
```

Here is the code with the extra methods added in that opens a link in a new tab.

```
if(chrome) {  chrome.tabs.query(    {active: true, currentWindow: true},    (arrayOfTabs) => { logCurrentTabData(arrayOfTabs) }    );  $('a').click( (event) => { chrome.tabs.create({url:event.target.href}) } )} else {  browser.tabs.query({active: true, currentWindow: true})    .then(logCurrentTabData)  $('a').click( (event) => { browser.tabs.create({url:event.target.href}) } )}
```

### Publishing your extension

With this code in place, you can now interact with the current browser without having to write two or more different web extension projects. You can now package your extension and publish to multiple web stores with the same file!

* [Publish in the Chrome Web Store — Google Chrome](https://developer.chrome.com/webstore/publish)
* [Developer Hub :: Add-ons for Firefox](https://addons.mozilla.org/en-US/developers/)

#### Read more from Medium

* [How to link to a specific paragraph in your Medium article (2018 Table of Contents method)](https://medium.freecodecamp.org/how-to-link-to-a-specific-paragraph-in-your-medium-article-2018-table-of-contents-method-e66595fea549) by [Quincy Larson](https://www.freecodecamp.org/news/how-to-make-a-cross-browser-extension-using-javascript-and-browser-apis-355c001cebba/undefined) in [freeCodeCamp](https://medium.freecodecamp.org/)
* [Improving the Medium Experience: One browser extension at a time](https://medium.freecodecamp.org/improving-the-medium-experience-one-browser-extension-at-a-time-7df7e233c984) by in [cedric amaya](https://www.freecodecamp.org/news/how-to-make-a-cross-browser-extension-using-javascript-and-browser-apis-355c001cebba/undefined) in [freeCodeCamp](https://medium.freecodecamp.org/)

#### Read more from [ryanwhocodes](https://www.freecodecamp.org/news/how-to-make-a-cross-browser-extension-using-javascript-and-browser-apis-355c001cebba/undefined)

* [How you can make a progressive web app in an hour](https://medium.freecodecamp.org/how-you-can-make-a-progressive-web-app-in-an-hour-7e36d560610e)
* [Mind your programming language: How to use Github Linguist and gitattributes to detect your app’s code type accurately](https://medium.freecodecamp.org/mind-your-programming-language-38e340a430a1)
* [Make your terminal more colourful and productive with iTerm2 and Zsh!](https://medium.com/the-code-review/make-your-terminal-more-colourful-and-productive-with-iterm2-and-zsh-11b91607b98c)

