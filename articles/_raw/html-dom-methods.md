---
title: HTML DOM Methods
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-17T23:57:00.000Z'
originalURL: https://freecodecamp.org/news/html-dom-methods
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dcb740569d1a4ca39af.jpg
tags:
- name: DOM
  slug: dom
- name: HTML
  slug: html
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'querySelector()

  The Document method querySelector() returns the first element within the document
  that matches the specified selector, or group of selectors. If no matches are found,
  null is returned.

  HTML content:

  <div id="id-example"></div>

  <div cl...'
---

## querySelector()

The Document method `querySelector()` returns the `first` element within the document that matches the specified selector, or group of selectors. If no matches are found, null is returned.

### HTML content:

```html
<div id="id-example"></div>
<div class="class-example"></div>
<a>element-example</a> 
```

### JavaScript content:

```javascript
document.querySelector("#id-example"); // Returns the element with id "id-example"
document.querySelector(".class-example"); // Returns the element with class "class-example"
document.querySelector("a"); // Returns the "a" element 
```

Note `querySelector()` returns the first matching element, to return all the matches, use the querySelectorAll() method instead.

```html
<div id="example">First</div>
<div id="example">Second</div>
```

```javascript
document.querySelector("#example"); // Returns only the element containing 'First'
```

## **innerHTML** 

The `innerHTML` prop return the HTML content inside a selected element and also let you define a new HTML content.

### Get element content

```html
<div id="demo">
  <p>Demo</p>
</div>
```

```javascript
var element = document.getElementById("demo");
console.log(element.innerHTML) //logs <p>Demo</p>
```

### Set element content

```html
<div id="demo"></div>
```

```javascript
var element = document.getElementById("demo");
element.innerHTML = "<div>Demo</div>";
```

The HTML now will be like

```html
<div id="demo">
  <div>Demo</div>
</div>
```

### Security considerations

The value that’s set to `innerHTML` should come from trusted sources, since Javascript will put anything inside that element and it will be run as plain HTML.

Example:

Setting a ”`<script>alert();</script>`” value will cause the Javascript “alert()” function to be fired:

```javascript
var element = document.getElementById("demo");

element.innerHTML = "<script>alert();</script>";
```

This type of attack is called [Cross Site Scripting, or XSS for short](https://en.wikipedia.org/wiki/Cross-site_scripting).

This is one of the most common ways of committing an XSS attack. If you want to learn a little bit more and learn to defend against it, [check out this resource](https://xss-game.appspot.com/).

## getElementById()

The `getElementById()` method returns the element that has the id attribute with the specified value. It takes one argument, which is a case-sensitive string of the id for the element you want.

This method is one of the most common methods in the HTML DOM, and is used almost every time you want to manipulate, or get info from, an element in your document. Here’s a simple example of the syntax:

**HTML content:**

```html
<div id="demo"></div>
```

**JavaScript content:**

```javascript
document.getElementById("demo"); // Returns the element with id "demo"
```

If you have more than one element with the same value of `id` (bad practice!), `getElementById` will return the first element found:

```html
<div id="demo">First</div>
<div id="demo">Second</div>
```

```javascript
document.getElementById("demo"); // Returns the element with id "demo" containing 'First'
```

#### **More Information:**

[document.getElementById()](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById)

#### **Alternative solutions:**

A commonly-used alternative to `document.getElementById` is using a jQuery selector which you read about more [here](https://github.com/freeCodeCamp/guides/tree/master/src/pages/jquery).

## More info about the HTML DOM

With the HTML DOM, JavaScript can access and change all the elements of an HTML document.

When a web page is loaded, the browser creates a **D**ocument **O**bject **M**odel of the page.

The HTML DOM model is constructed as a tree of Objects:

Each element in the DOM is also called a node.

```html
<html>
<head>
  <title> My title </title>
</head>
<body>
  <a href="#">My Link</a>
  <h1> My header </h1>
</body>
</html>
```

The DOM for the above HTML is as follows:

![DOM tree](https://www.w3schools.com/js/pic_htmltree.gif)

With the object model, JavaScript gets all the power it needs to create dynamic HTML:

* JavaScript can change all the HTML elements in the page
* JavaScript can change all the HTML attributes in the page
* JavaScript can change all the CSS styles in the page
* JavaScript can remove existing HTML elements and attributes
* JavaScript can add new HTML elements and attributes
* JavaScript can react to all existing HTML events in the page
* JavaScript can create new HTML events in the page

