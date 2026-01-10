---
title: How to implement a Chrome Extension
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2018-11-12T16:29:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-a-chrome-extension-3802d63b5376
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/1_IrKrGVmSj1DVh6kIsfqYyA.jpeg
tags:
- name: chrome extension
  slug: chrome-extension
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'We all like surfing the web. And we all like things to be at the touch
  of our fingertips. Why not create something that caters to these two absolute truths?

  In this article, I’ll explain the building blocks of a Chrome extension. Afterwards,
  you’ll j...'
---

We all like surfing the web. And we all like things to be at the touch of our fingertips. Why not create something that caters to these two absolute truths?

In this article, I’ll explain the building blocks of a Chrome extension. Afterwards, you’ll just have to think of a good idea as an excuse to make one.

### Why Chrome?

Chrome is by far the most popular web browser. [Some estimations are as high as **59%**](https://en.wikipedia.org/wiki/Usage_share_of_web_browsers). So, if you want to reach as many people as you can, developing a Chrome extension is the best way to do it.

⚠️ To be able to publish a Chrome extension, you need to have a developer account which entails a [$5 one-time signup fee](https://developer.chrome.com/webstore/publish).

Each Chrome extension should have these components: the **manifest file**, **popup.html** and **popup.js** and a **background** script. Lets take a look at them.

### What makes up a Chrome extension?

#### The Manifest File

What is a manifest file? It is a text file in JSON ([JavaScript Object Notation](https://en.wikipedia.org/wiki/JSON)) format that contains certain details about the extension you will be developing.

Google uses this file to acquire details about your extension when you will publish it. There are **required**, **recommended** and **optional** fields.

#### Required

```js
{
  "manifest_version": 2,
  "name": "My Chrome Extension",
  "version": "1.0",
  "default_locale": "en"
}
```

* `manifest_version` - Version of the manifest file format. As of Chrome 18, version 1 is deprecated
* `name` - Can be up to 45 characters. Used to display your extension’s name in the following places: Install dialog, Extension management UI, Chrome Web Store
* `version` - Version of your Chrome Extension. Can be up to four digits separated by dots (e.g., 1.0.0.0)
* `default_locale` - This folder resides inside the `_locals` folder and it contains the default string literals. The `_locals` folder is used for internationalization (allowing your extension to support multiple languages). It is a required field if a `_locals` folder exists, otherwise, it should not be present

If you want to support multiple languages, read more [here](https://developer.chrome.com/extensions/i18n).

#### Recommended

```js
  "description": "A plain text description",
  "author": "Your Name Here",
  "short_name": "shortName",
  "icons": {
      "128":"icon128.png",
       "48":"icon48.png",
       "16":"icon16.png"
    },
```

* `description` - You can use up to 132 characters to describe the extension
* `short_name` - Limited to 12 characters, it is used in cases where there is not enough space to display the full name of the extension (App Launcher and New Tab Page)
* `icons` - The icons that represent the extension. **Always include a 128X128 icon** because it is used by the Chrome Web Store and during the installation of your extension

Optional fields are case specific, so we won’t go into them in this article.

After covering the data needed for the manifest file, we can now move on to where we will actually be writing code for our extension, **Popup and Background**.

#### Popup and Background

The popup refers to the main page users see when using your extension. It consists of two files: **Popup.html** and a JavaScript file, **Popup.js**.

Popup.html is the layout file for how your extension will look like. Depending on what your extension will do, the markup of this file will change.

A background script is the only one that can interact with events that occur and use the Chrome API. To use background scripts you need to add the following to your manifest.json file:

```js
{
  "manifest_version": 2,
  "name": "My Chrome Extension",
  "version": "1.0",
  "background":{
    	"scripts": ["yourScript.js"],
    	"persistent": false
    }
}
```

The key `scripts` has a value of an array of script names.

`persistent` is a key with a boolean value which denotes the use of your extension with chrome.webRequest API to block or modify network requests. The Chrome.webRequest API does not work with non-persistent background pages.

![Image](https://cdn-media-1.freecodecamp.org/images/0*mFgdmSgmiXKQmhZ_)
_“open signage on door” by [Unsplash](https://unsplash.com/@belart84?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Artem Bali</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### How Your Extension Will Open

Every Chrome extension adds a little icon to the toolbar at the top of your browser. Once the user clicks that icon, you can choose how you want your extension to open in the browser:

1. It can override a new tab, so as not to disrupt the current user’s activity

2. You can open a small window in the user’s current tab, so as to keep the user in the same tab

Each choice has it’s consequences and it is up to you to decide what is the best option for you.

Below is the code needed to pull off each of the options. They will both use the same popup.html file outlined below:

```html
<html>

	<head>
		
		<title>Chrome Extension Example</title>
	</head>

	<body>

		<h1>Hello From Extension</h1>

	</body>


</html>
```

### Putting It All Together

#### Override New Tab

```js
//In manifest.json
{
    "name": "ChromeExampleNewTab",
    "version": "1.0",
    "manifest_version": 2,
    "chrome_url_overrides": {
    	"newtab": "popup.html"
    },
    "browser_action": {}, 
    "permissions":[        
    	"tabs"
    ],
    "background":{        
    	"scripts": ["background.js"],
    	"persistent": false
    }
}

//In background.js
chrome.browserAction.onClicked.addListener(function(tab) {
	chrome.tabs.create({'url': chrome.extension.getURL('popup.html')}, function(tab) {
		// Tab opened.
	});
});
```

#### Open In The Current Tab

```js
//In manifest.js
{
    "name": "ChromeExample",
    "version": "1.0",
    "manifest_version": 2,
    "browser_action": {         
      "default_popup": "popup.html"
    }
}
```

Notice how we have overridden the `browser_action` key in both examples.

We have to do this, since we don’t want the browser to open a new tab in the regular fashion.

Also, since if we want to open a new tab with our extension, we must add a permissions key to the manifest and specify the tabs value. This lets the browser know we need the user’s permission to overwrite the default behavior of opening a new tab.

There is a whole lot more to Chrome extensions (messaging, context menus and storage to name a few). I have hopefully given you some insight into Chrome extensions. Maybe just enough to intrigue you to make one of your own!

And while you are at it, check one I have made [here](https://chrome.google.com/webstore/detail/gifted/jmhifaldhcbhfdgdbneekdaloednddco).

