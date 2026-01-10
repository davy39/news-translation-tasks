---
title: JavaScript Onclick Event Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-14T20:01:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-onclick-event-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eb2740569d1a4ca3e93.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "The onclick event in JavaScript lets you as a programmer execute a function\
  \ when an element is clicked.\nButton Onclick Example\n<button onclick=\"myFunction()\"\
  >Click me</button>\n\n<script>\n  function myFunction() {\n    alert('Button was\
  \ clicked!');\n  }\n..."
---

The `onclick` event in JavaScript lets you as a programmer execute a function when an element is clicked.

## Button Onclick Example

```javascript
<button onclick="myFunction()">Click me</button>

<script>
  function myFunction() {
    alert('Button was clicked!');
  }
</script>
```

In the simple example above, when a user clicks on the button they will see an alert in their browser showing `Button was clicked!`.

## Adding onclick dynamically

The `onclick` event can also be programmatically added to any element using the following code in the following example:

```javascript
<p id="foo">click on this element.</p>

<script>
  var p = document.getElementById("foo"); // Find the paragraph element in the page
  p.onclick = showAlert; // Add onclick function to element
    
  function showAlert(event) {
    alert("onclick Event triggered!");
  }
</script>
```

### **Note**

It’s important to note that using onclick we can add just one listener function. If you want to add more, just use addEventListener(), which is the preferred way for adding events listener.

In the above example, when a user clicks on the `paragraph` element in the `html`, they will see an alert showing `onclick Event triggered`.

## Preventing default action

However if we attach `onclick` to links (HTML’s `a` tag) we might want prevent default action to occur:

```javascript
<a href="https://guide.freecodecamp.org" onclick="myAlert()">Guides</a>

<script>
  function myAlert(event) {
    event.preventDefault();
    alert("Link was clicked but page was not open");
  }
</script>
```

In the above example we prevented default behavior of `a` element (opening link) using `event.preventDefault()` inside our `onclick` callback function.

[MDN](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onclick)

### Other Resources

[jQuery .on() Event Handler Attachment](https://api.jquery.com/on/)

