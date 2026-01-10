---
title: 'JavaScript DOM Events: Onclick and Onload'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-20T22:43:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-dom-events-onclick-and-onload
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dab740569d1a4ca38fa.jpg
tags:
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In the early days of the internet, web pages were truly static – there
  were only text and images. Sure, sometimes that image was an animated gif, but it
  was still just an image.

  With the advent of JavaScript, it became increasingly possible to create...'
---

In the early days of the internet, web pages were truly static – there were only text and images. Sure, sometimes that image was an animated gif, but it was still just an image.

With the advent of JavaScript, it became increasingly possible to create interactive pages that would respond to actions like clicking on a button or having a scroll animation.

There are a number of DOM (Document Object Model) events that you can listen for in JavaScript, but `onclick` and `onload` are among the most common.

## **Onclick Event**

The `onclick` event in JavaScript lets you execute a function when an element is clicked.

### **Example**

```javascript
<button onclick="myFunction()">Click me</button>

<script>
  function myFunction() {
    alert('Button was clicked!');
  }
</script>
```

In the simple example above, when a user clicks on the button they will see an alert in their browser showing `Button was clicked!`.

### **Adding `onclick` dynamically**

The example above works, but is generally considered bad practice. Instead, it's better to separate the content of the page (HTML) from the logic (JS). 

To do this, the `onclick` event can be programmatically added to any element using the following code in the following example:

```javascript
<p id="foo">click on this element.</p>

<script>
  const p = document.getElementById("foo"); // Find the paragraph element in the page
  p.onclick = showAlert; // Add onclick function to element
    
  function showAlert(event) {
    alert("onclick Event triggered!");
  }
</script>
```

### **Note**

It’s important to note that using `onclick` we can add just one listener function. If you want to add more, just use `addEventListener()`, which is the preferred way for adding events.

In the above example, when a user clicks on the `paragraph` element in the `html`, they will see an alert showing `onclick Event triggered`.

### **Preventing default action**

However if we attach `onclick` to links (HTML’s `a` tag) we might want prevent default action to occur:

```javascript
<a id="bar" href="https://guide.freecodecamp.org">Guides</a>

<script>
  const link = document.getElementById("bar"); //  Find the link element
  link.onclick = myAlert; // Add onclick function to element

  function myAlert(event) {
    event.preventDefault();
    alert("Link was clicked but page was not open");
  }
</script>
```

In the above example we prevented default behavior of `a` element (opening link) using `event.preventDefault()` inside our `onclick` callback function.

## **Onload Event**

The `onload` event is used to execute a JavaScript function immediately after a page has been loaded.

### **Example:**

```javascript
const body = document.body;
body.onload = myFunction;

function myFunction() {
  alert('Page finished loading');
}

```

Which can be shortened to:

```js
document.body.onload = function() {
  alert('Page finished loading');
}

```

In the above example, as soon as the web page has loaded, the `myFunction` function will be called, showing the `Page finished loading` alert to the user.

The `onload` event is usually attached to the `<body>` element. Then once the `<body>` of the page has loaded, which includes all images, and CSS and JS files, your script will run.

#### **More Information:**

These are only two of the many DOM events you can manipulate with JavaScript, but are among the mostly commonly used.

But sometimes you don't need to listen for DOM events at all, and want to use a time based event like a countdown. For a quick tutorial on timing events, check out [this article](https://www.freecodecamp.org/news/javascript-timing-events-settimeout-and-setinterval).

