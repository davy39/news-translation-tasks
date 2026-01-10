---
title: How to handle event handling in JavaScript (examples and all)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-19T18:14:18.000Z'
originalURL: https://freecodecamp.org/news/event-handling-in-javascript-with-examples-f6bc1e2fff57
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dhtbZon7OPebZuUO9-yyjw.jpeg
tags:
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Honey Thakuria

  In this blog, I will try to make clear the fundamentals of the event handling mechanism
  in JavaScript, without the help of any external library like Jquery/React/Vue.

  I will be explaining the following topics in this article:


  The d...'
---

By Honey Thakuria

In this blog, I will try to make clear the fundamentals of the event handling mechanism in JavaScript, without the help of any external library like Jquery/React/Vue.

I will be explaining the following topics in this article:

1. The **document** and **window** objects, and adding **Event Listeners** to them.
2. The **Event.preventDefault()** method and it’s usage.
3. The **Event.stopPropagation()** method with an example.
4. **How to remove** an event **listener** from an element.

### **Document** and **window** objects with **Event Listeners**

The Window object represents the tab. In case you are reading this blog on your corresponding browser, then your current tab represents the Window object.

The window object has access to such information as the toolbar, height and width of the window, prompts, and alerts. Let’s see how we can add an event listener (mousedown) to the window object and analyze some of its properties.

#### **How to add the listener on the window object**

The **addEventListener** method is the most preferred way to add an event listener to **window**, **document** or any other **element** in the DOM.

There is one more way called “on” property onclick, onmouseover, and so on. But is not as useful, as it does not allow us to add multiple event listeners on the same element. The other methods allow it.

An **event** object is passed as an argument (optional) to the handler which contains all the information related to the event (in our case, mousedown) on the window.

Open the developer tools (Inspect Element) on this page and copy paste the following code in the console panel and hit enter.

```js
window.addEventListener("mousedown",function(event){
 alert("window");
 console.log(event);
});
```

After that, you can go over to any section of the current tab and **right click** to see the console and the info related to this event, as shown below in the snapshot.

**Note**: If you go to any other tab and right click, then this event will not get fired as it belongs to this tab (Window object) only.

![Image](https://cdn-media-1.freecodecamp.org/images/OkOuvlALsx7sPyDl7NJ2AfcjV7yCSoVpN2TK)

#### The details of the mousedown event

In the next few lines, I will explain some of the important captured property corresponding to the **mousedown** event we just performed.

**button**: As this was the mousedown event, it will tell you the button you clicked. For the mouse, Left, middle, and right correspond to 0, 1, and 2 respectively. If you click the right button, you can see the value 2.

**clientX** and **clientY**: Position relative to the upper left of the content area (Viewport). Just analyze the value of these properties with the place you clicked, and you can see how they’re related. Even if you scroll down the page, these properties remain the same. ScreenX and ScreenY reference from the top left of the screen (Monitor).

**altkey / ctrlkey**: If you keep any of these keys pressed while performing your right click operation, then you can see these values are true. Otherwise, they’re false as in our case.

**target:** It corresponds to the element you performed the action upon. Whatever element you might have clicked on, you can see the information corresponding to this property in the console

#### **What is a document object**?

The document consists of what is inside the inner window. The **document** **object** is the root of every node in the DOM. If you are loading an HTML page in the browser, then the document represents that entire page.

### **The Event.preventDefault()** method and its usage

Sometime we don’t want an HTML element to behave in the way it is supposed to behave in default. In such a case, we can use this method.

**Example**: Clicking the anchor element will make the browser redirect to that page by default. Let’s try to avoid that.

```html
<html>

<body>

  <a href="https://google.com/">Google</a>

  <script>
    let link = document.querySelector("a"); // It is the method to access the first matched element
    link.addEventListener("click", function(event) {
      console.log("Redirecting Stopped");
      event.preventDefault();
    });
  </script>
</body>

</html>
```

You can create an HTML file and check out this code.

### **The Event.stopPropagation()** method

**Events flow outwards.** There are certain cases, such as when you have nested elements and you perform some event on a child and it ends up performing some action on the parent, too, that you want to avoid. In such cases, this method is a useful one.

It sounds bit confusing, but I hope the below example will make it clear to you.

Imagine you have a button inside a paragraph and you have attached a mousedown event to both of them. You want to achieve the following use cases:

1. If you right click the button, then it should show that it has been clicked and does not propagate to the parent element (that is, the paragraph).
2. If you left click on the button, then it should propagate outwards normally and fire the paragraph event listener, too.

Solution:

```html
<html>

<body>
  <p id="demo"> Hello Ho<button id="button12"> Button2 </button> </p>
  <script>
    // Event Listener on the Button and it's logic
    document.getElementById("button12").addEventListener("mousedown", function(event) {
      alert("button clicked");
      if (event.button == 2) // Right Click
        event.stopPropagation();
    });
    // Event Listener on the paragraph element with it's logic:
    document.getElementById("demo").addEventListener("mousedown", function(event) {
      alert("Paragraph clicked");
    });
  </script>
</body>

</html>
```

### **Removing** an **event listener** from an element

In order to remove an event listener from an element, we need to call the **removeEventListener** method with the event name and the function name.

**Note**: when anonymous functions are passed, they don’t have memory mapping. So we need to define those functions outside the callback and then reference them here in the removeEventListener callback.

```js
Document.getElementbyId("id_name").removeEventListener("click",fn_name)
```

If you have reached this point, you should have a decent understanding of how Event Listeners work in the JavaScript.

If, while working with your favorite library/Frameworks, you ever get stuck in the Events Handling part, then these basics should help you to resolve the issue.

