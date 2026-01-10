---
title: JavaScript document.ready() – Document Ready JS and jQuery Example
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-07-27T21:03:19.000Z'
originalURL: https://freecodecamp.org/news/javascript-document-ready-jquery-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/joan-gamell-ZS67i1HLllo-unsplash.jpg
tags:
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
- name: jQuery
  slug: jquery
seo_title: null
seo_desc: "When working with JavaScript and the Document Object Model (DOM), you might\
  \ want your script to run only when the DOM has loaded. \nYou can do this using\
  \ the $(document).ready() method in jQuery, or the DOMContentLoaded event in vanilla\
  \ JavaScript.\nIn..."
---

When working with JavaScript and the Document Object Model (DOM), you might want your script to run only when the DOM has loaded. 

You can do this using the `$(document).ready()` method in jQuery, or the `DOMContentLoaded` event in vanilla JavaScript.

In this article, you'll learn how to make your JavaScript code run only when the DOM has loaded using jQuery and vanilla JavaScript.

## How to Use the `$(document).ready()` Method in jQuery

Before JavaScript runs in the browser, it waits for the contents of the document to load. This includes stylesheets, images, and so on.

As a convention, placing the script element just before the closing body tag makes the script wait for the rest of the document to load before running. 

We also can make this process faster in jQuery by using the `$(document).ready()` method. The `$(document).ready()` method only waits for the DOM to load, it doesn't wait for stylesheets, images, and iframes. 

Here's an example:

```javascript
$(document).ready(function () {
  console.log("Hello World!");
});
```

In the code above, the `$(document).ready()` method will only run after the DOM has loaded. So you'll only see "Hello World!" in the console after the `$(document).ready()` method has started running. 

In summary, you can write all your jQuery code inside the `$(document).ready()` method. This way, your code will wait for the DOM to be loaded before running. 

## How to Use the `DOMContentLoaded` Event in JavaScript

Just like jQuery's `$(document).ready()` method, the `DOMContentLoaded` event fires once the DOM has loaded – it doesn't wait for stylesheets and images. 

Here's how to use the `DOMContentLoaded` event:

```javascript
document.addEventListener("DOMContentLoaded", () => {
  console.log("Hello World!");
});
```

Once the DOM has loaded, the `DOMContentLoaded` event will detect it and run.

You should use the `DOMContentLoaded`  event when:

* You have certain functionalities in your webpage that should fire immediately without waiting for the rest of the page content.
* You have a script tag placed within the head element.

## Summary

In this article, we talked about the`$(document).ready()` method in jQuery, and the `DOMContentLoaded` event in vanilla JavaScript.

We use them to execute JavaScript code when the DOM has loaded. 

The interesting part of these functionalities is that they let JavaScript code run without waiting for images and stylesheets to load completely in a web page. 

Happy coding!

