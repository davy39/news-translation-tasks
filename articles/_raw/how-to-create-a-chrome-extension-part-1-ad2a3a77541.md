---
title: How to create a Chrome Extension
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-12T12:52:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-chrome-extension-part-1-ad2a3a77541
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7aJPlxn8gwhI7JjcBFr-tQ.jpeg
tags:
- name: Google Chrome
  slug: chrome
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Erika Tan

  In this article, I will be teaching you how to make a Chrome Extension of your own.
  I’m basing it off of lessons learned while creating TalkToMe, a Chrome Extension
  that helps the visually impaired by reading website content and navigati...'
---

By Erika Tan

In this article, I will be teaching you how to [make a Chrome Extension of your own](https://developer.chrome.com/extensions/getstarted). I’m basing it off of lessons learned while creating [TalkToMe](https://github.com/PalashTanejaPro/BlindHelper), a Chrome Extension that helps the visually impaired by reading website content and navigating to other web pages.

I’m going to cover the basics of setting up your extension, including:

* Configuring the files for setup
* Getting it ready to put onto the Chrome store

> I won’t be covering how to manage audio features, such as handling mic permissions. This has been covered in [this article](https://medium.com/@tanejapalash/handling-mic-input-permissions-and-speech-recognition-in-chrome-extensions-ff7e3ca84cb0) by my friend Palash and also uses the [TalkToMe](https://github.com/PalashTanejaPro/BlindHelper) extension as an example.

#### Configuring the files for setup

First, go to **chrome://extensions** in your browser, or simply click “More Tools” and “Extensions” on the Chrome menu. This should lead you to the Extension Management page, where you can **turn on Developer Mode** (it should be in the top right corner).

Then, you’ll need to make a `manifest.json` file in a new directory for your extension. This file provides important information for your extension to function, such as permissions and the script files that you’ll be linking your project to. This is what the contents of your manifest should look like:

```
{    "name": "Chrome Extension Example",    "version": "1.0",    "description": "Build an Extension!",    "manifest_version": 2}
```

To upload your directory to the Extension Management page, click the “Load Unpacked” button and select your directory. This will link your files to the web-based UI.

Another important file that you’ll have to configure is `background.js`, which is the background script of your project.

A sample background script has this type of structure:

```
chrome.runtime.onInstalled.addListener(function() {    // add an action here});
```

It will always be running while your extension is turned on and is useful for listening to different events, such as keyboard presses, or for navigating to different pages.

You can even have multiple background scripts. You just need to register all of them in your manifest file first. To do this, simply structure `manifest.js` like this, which is what the manifest file to our extension looks like:

```
{    "name": "Chrome Extension Example",    ...
```

```
    "background": {        "scripts": [            "js/es6-promise.auto.min.js",            "js/defaults.js",            "js/speech.js",            "js/document.js",            "js/events.js",            "js/stt.js",            "js/listen.js"        ],        "persistent": false    }}
```

Now, you’ll need a file for not just the function of your extension, but also the UI. To do this, make a file called `popup.html`. The popup is a small window that appears once your extension icon is clicked. For example, here’s the popup for the Cookie Manager Firefox extension.

![Image](https://cdn-media-1.freecodecamp.org/images/ZG-VIUmxMhxR8qzkGKdB7NOwtl598vzxmG7n)

The `popup.html` file can be quite simple. Below is some code to make a popup with a single button. It’s as easy as adding opening and closing button tags into the body of the document and a few style rules.

```
<!DOCTYPE html>  <html>    <head>      <style>        button {          height: 30px;          width: 30px;          outline: none;        }      </style>    </head>;    <body>      <button></button>    </body>  </html>
```

Of course, the `popup.html` code for our extension has many more components than this. Feel free to add more buttons, stylesheets, and anything else you see fit for your extension idea.

Time to configure the popup code and the icon. For the icon, however, you’ll need to add code into two places, “default_icon” and “icons”. The “default_icon” property is used for toolbar icons, and “icons” is used for the images displayed on the Extension Management page.

Go back to `manifest.json` and add in the following lines of code, replacing the image paths for the default icon with your own images. You can also put the same images in for both “default_icon” and “icons”. And, you don’t _need_ to put in pictures of the same dimensions as the ones specified below. For example, if you only have images that are 16 x 16 and 48 x 48, feel free to delete the other two lines that specify 32 and 128 pixels.

```
{   "name": "Chrome Extension Example",    ...
```

```
    "page_action": {        "default_popup": "popup.html",        "default_icon": {            "16": "images/img16.png",            "32": "images/img32.png",            "48": "images/img48.png",            "128": "images/img128.png"        }    },    "icons": {        "16": "images/img16.png",        "32": "images/img32.png",        "48": "images/img48.png",        "128": "images/img128.png"    }}
```

So these are the files that are essential in building a chrome extension:

* a manifest file,
* background scripts, and
* a popup file

Some other files that you might want to configure are:

* `options.html` and
* `options.js`

`options.js` will give your users a wider variety of options when it comes to using your extension. It will take care of how your options page looks (it’s very similar to `popup.html`), while `options.js` will handle the functionality.

These files are optional, but if you decide to add them, don’t forget to configure `options.html` in the manifest and link your `options.js` file by adding `<script src=”options.js”><`;/script> right before your ending HTML tag.

```
{    "name": "Chrome Extension Example",    ...    "options_page": "options.html"}
```

To see your extension in action, save all of your files and click “Reload” while you’re on the Extension Management page. You should see your icon in the toolbar. To view your options page, you can also click “Details” under your extension and scroll down to where it says “Extension options”.

#### Publishing your project to the web store

So you’ve developed and tested your extension. Now you need to distribute it!

To begin uploading your project, first convert it to a .zip file. The file should, at a minimum, contain the `manifest.json` file. Then, make sure you have a developer account by visiting the [Chrome Webstore Developer Dashboard](https://chrome.google.com/webstore/developer/dashboard).

Click the “Add new item” button and it should let you upload your `.zip` file there. Unless you want to register payments for your app, you can skip the step about setting up a payment system. You will have to pay a $5 one-time developer fee, however, when you put your project onto the web store.

Also, don’t forget to include a detailed description and pictures of your extension so that potential users will know exactly what your project does!

Once all of this is complete, you’ll receive an app ID and an OAuth token. The app ID is used for making requests to Google APIs, while the OAuth token is used for making Web Store payments.

Congratulations, you have now published your extension! ?

If you enjoyed this post, check out [this next article](https://medium.com/@tanejapalash/handling-mic-input-permissions-and-speech-recognition-in-chrome-extensions-ff7e3ca84cb0). We’ll be diving deeper into how to configure audio features in your Chrome extension, just like we did for TalkToMe.

