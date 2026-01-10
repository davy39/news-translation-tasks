---
title: How to Write Your Own Browser Extension [Example Project Included]
subtitle: ''
author: Abhilekh gautam
co_authors: []
series: null
date: '2021-11-02T15:57:40.000Z'
originalURL: https://freecodecamp.org/news/write-your-own-browser-extensions
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/browsers.png
tags:
- name: Browsers
  slug: browsers
- name: chrome extension
  slug: chrome-extension
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: 'In this article we will talk about Browser extensions – what they are,
  how they work, and how you can build your own.

  We will finish by actually writing our own extension (Super Fun!) which allows us
  to copy any code snippet to our clipboard with a c...'
---

In this article we will talk about Browser extensions – what they are, how they work, and how you can build your own.

We will finish by actually writing our own extension (Super Fun!) which allows us to copy any code snippet to our clipboard with a click of a single button.

To continue with this article:

* You need to have a basic understanding of JavaScript.
    
* You need the Firefox browser (or any other browser will also work)
    

## What is a Browser Extension?

A browser extension is something you add to your browser which enhances your browsing experience by extending the capacity of your browser.

As an example, think about an ad blocker which you might have installed on your device. This makes your browsing experience better by blocking ads when you surf the web.

## How to Write Your Own Basic Browser Extension

Now let's start by writing a very basic extension.

To begin, we'll create a folder inside which we create a file named `manifest.json`.

### What is a manifest file?

A manifest file is a must have file in any browser extension. This file contains basic data about our extension like name, version, and so on.

Now inside the `manifest.json` file copy the following snippet:

```json
{
  "manifest_version":2,
  "version":"1.0",
  "name":"Test",
}
```

\[**2025 Update**: Chrome [currently only supports version 3](https://developer.chrome.com/docs/extensions/reference/manifest) for manifest.json\]

### How to load the extension file

For Firefox users, follow these steps:

In the address bar, search for this:

```javascript
about:debugging#/runtime/this-firefox
```

You will see an option to *Load Temporary Add-on*. Click on that option and choose the `manifest.json` file from the directory.

For Chrome users:

In the address bar search for this:

```javascript
chrome://extensions
```

* Enable Developer Mode and switch into it.
    
* Click the Load unpacked button and select the extension directory.
    

Hurray! You've installed the extension successfully. But the extension doesn't do anything currently. Now let's add some functionality to our extension. To do this, we'll edit our `manifest.json` file like this:

```json
{
  "manifest_version":2,
  "version":"1.0",
  "name":"Test",
  "content_scripts":[
    {
     "matches":["<all_urls>"],
     "js":["main.js"]
    }
  ]
}
```

In the above code, we added a content script to `manifest.json`. Content scripts can manipulate the Document Object Model of the web page. We can inject JS (and CSS) into a web page using a content script.

`"matches"` contains the list of domains and subdomains where the content script should be added and `js` is an array of the JS files to be loaded.

Now inside the same directory create a `main.js` file and add the following code:

```js
alert("The test extension is up and running")
```

Now reload the extension and when you visit any `URLs` you will see an alert message.

**Don't forget to reload the extension anytime you edit the code.**

## How to Customize Your Browser Extension

Now let's have some more fun with our extension.

What we are going to do now is create a web extension that changes all the images of a webpage we visit to an image we choose.

For this, just add any image to the current directory and change the `main.js` file to:

```js
console.log("The extension is up and running");

var images = document.getElementsByTagName('img')

for (elt of images){
   elt.src = `${browser.runtime.getURL("pp.jpg")}`
   elt.alt = 'an alt text'
}
```

Let's see whats going on here:

```js
var images = document.getElementsByTagName('img')
```

This line of code selects all the elements in the web page with the `img` tag .

Then we loop through the array images using a for loop where we change the `src` attribute of all the `img` elements to a URL with the help of the `runtime.getURL` function.

Here `pp.jpg` is the name of the image file in the current directory in my device.

We need to inform our content script about the `pp.jpg` file by editing the `manifest.json` file to:

```js
{
  "manifest_version":2,
  "version":"1.0",
  "name":"Test",
  "content_scripts":[
   {
    "matches":["<all_urls>"],
    "js":["main.js"]
   }
  ],
  "web_accessible_resources": [
        "pp.jpg"
  ]
}
```

Then just reload the extension and visit any URL you like. Now you should see all the images being changed to the image which is in your current working directory.

### How to add icons to your extension

Add the following code in the `manifest.json` file:

```json
"icons": {
  "48": "icon-48.png",
  "96": "icon-96.png"
}
```

### How to add a toolbar button to your extension

Now we'll add a button located in the toolbar of your browser. Users can interact with the extension using this button.

To add a toolbar button, add the following lines to the `manifest.json` file:

```json
"browser_action":{
   "default_icon":{
     "19":"icon-19.png",
     "38":"icon-38.png"
   }
  }
```

All the image files should be present in your current directory.

Now, if we reload the extension we should see an icon for our extension in the toolbar of our browser.

### How to add listening events for the toolbar button

Maybe we want to do something when a user clicks the button – let's say we want to open a new tab every time the button is clicked.

For this, we'll again add the following to the `manifest.json` file:

```json
"background":{
        "scripts":["background.js"]
  },
  "permissions":[
      "tabs"
  ]
```

Then we'll create a new file named `background.js` in the current working directory and add the following lines in the file:

```js
function openTab(){
    
    var newTab = browser.tabs.create({
        url:'https://twitter.com/abhilekh_gautam',
        active:true
    })
}

browser.browserAction.onClicked.addListener(openTab)
```

Now reload the extension!

Whenever someone clicks the button, it calls the `openTab` function which opens a new tab with the URL that links to my twitter profile. Also, the active key, when set to true, makes the newly created tab the current tab.

Note that you can use APIs provided by browsers in the background script. For more about APIs refer to the following article: [Javacript APIs](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API).

Now that we've learned some of the basics of browser extensions, let's create an extension that we as developers can use in our daily lives.

## Final Project

Alright, now we're going to write something that will be useful for us in daily life. We'll create an extension that allows you to copy code snippets from StackOverflow with a single click. So our extension will add a `Copy` button to the webpage which copies the code to our clipboard.

### Demo

![Image](https://www.freecodecamp.org/news/content/images/2021/10/demo.png align="left")

First we'll create a new folder/directory, inside which we'll add a `manifest.json` file.

Add the following code to the file:

```json
{
  "manifest_version":2,
  "version":"1.0",
  "name":"copy code",
  "content_scripts":[
    {
     "matches":["*://*.stackoverflow.com/*"],
     "js":["main.js"]
    }
  ]
}
```

Look at the `matches` inside the `content script` – the extension will only work for StackOverflow's domain and subdomain.

Now create another JavaScript file called `main.js` in the same directory and add the following lines of code:

```js
var arr =document.getElementsByClassName("s-code-block")

for(let i = 0 ; i < arr.length ; i++){
 var btn = document.createElement("button")
 btn.classList.add("copy_code_button")
 btn.appendChild(document.createTextNode("Copy"))
 arr[i].appendChild(btn)
 //styling the button
 btn.style.position = "relative"
 
 if(arr[i].scrollWidth === arr[i].offsetWidth && arr[i].scrollHeight === arr[i].offsetHeight)
  btn.style.left = `${arr[i].offsetWidth - 70}px`

  else if(arr[i].scrollWidth != arr[i].offsetWidth && arr[i].scrollHeight === arr[i].offsetWidth)
   btn.style.left = `${arr[i].offsetWidth - 200}px`
 else 
   btn.style.left = `${arr[i].offsetWidth - 150}px`
  
 if(arr[i].scrollHeight === arr[i].offsetHeight)
   btn.style.bottom = `${arr[i].offsetHeight - 50}px`
   
 else
   btn.style.bottom = `${arr[i].scrollHeight - 50}px`
 //end of styling the button
   
   console.log("Appended")
}
```

First of all, I selected all the elements with the class name `s-code-block` – but why? This is because when I inspected StackOverflow's site I found that all the code snippets were kept in a class with that name.

And then we loop through all those elements and append a button in those elements. Finally, we just position and style the button properly (the styling's not perfect yet – this is just a start).

When we load the extension using the process we went through above and visit StackOverflow, we should see a copy button.

### How to add functionality to the button

Now, when the button is clicked we want the entire snippet to be copied to our clip board. To do this, add the following line of code to the `main.js` file:

```js
var button = document.querySelectorAll(".copy_code_button")
 button.forEach((elm)=>{
  elm.addEventListener('click',(e)=>{
    navigator.clipboard.writeText(elm.parentNode.childNodes[0].innerText)
    alert("Copied to Clipboard")
  })
 })
```

First of all, we select all the buttons we have added to the site using `querySelectorAll`. Then we listen for the click event whenever the button is clicked.

```js
navigator.clipboard.writeText(elm.parentNode.childNodes[0].innerText)
```

The above line of code copies the code to our clipboard. Whenever a snippet is copied we alert the user with the message `Copied to clipboard` and we are done.

## Final Words

Web Extensions can be useful in various way and I hope with the help of this article you will be able to write your own extensions.

All the code can be found in [this GitHub](https://github.com/Abhilekhgautam/Copy-Code) repository. Don't forget to give a pull request anytime you come up with some good styling or a new feature like clipboard history and others.

**Happy Coding!**
