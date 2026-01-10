---
title: How to Manage Browser Defaults with event.preventDefault() and event.stopPropagation()
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-04T19:59:02.000Z'
originalURL: https://freecodecamp.org/news/manage-default-behavior-in-browser
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-startup-stock-photos-7359.jpg
tags:
- name: Browsers
  slug: browsers
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Dillion Megida\nBrowsers have default interactions and behaviors for\
  \ different events. \nFor example, when a user clicks a \"submit\" button on a form,\
  \ the form is submitted to a URL by default. \nWhen the child of an element is clicked,\
  \ the click even..."
---

By Dillion Megida

Browsers have default interactions and behaviors for different events. 

For example, when a user clicks a "submit" button on a form, the form is submitted to a URL by default. 

When the child of an element is clicked, the click event also occurs on the element because it is the main container.

In some cases, you may want to override these defaults. In this article, we will learn what the `event.preventDefault()` and `event.stopPropagation()` methods are and how to use them to cancel some default actions that occur in the browser.

## event.preventDefault()

This method prevents default actions that browsers make when an event is triggered. 

Here are some examples of default actions on webpages and how to override them with `event.preventDefault()`.

### How to override default form submission

When a user submits a form (the submit button clicked), the default action of the form is to submit the form's data to a URL that processes the data.

Form elements have the `action` and `method` attributes which specify the URL to submit the form to and the type of request (`get`, `post`, and so on), respectively. 

If these attributes are not provided, the default URL is the current URL the form was submitted on, and the method is `get`.

For example, this code:

```html
<form>
  <input name="email" />
  <input name="password" />
  <input type="submit" />
</form>
```

produces this page:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-9.png)

On submitting the form with input "dillion" and "password", you can see a `get` request submitted to `127.0.0.1:5500/index.html` like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-10.png)

This action is how browsers handle forms by default. 

But you may want to do more things to the data before sending a request. This is especially common in today's approach to handling forms. 

You may want to do some data validation, data checks, processing, configuring headers, and so on before sending the request to a URL. 

In these scenarios, you'll want to prevent the form's default action. Here's how:

```html
<form id='form'>
  ...
</form>
```

```js
const form = document.getElementById('form')

form.addEventListener('submit', (event) => {
  event.preventDefault()
  
  // process data and submit a request manually
})
```

This way, submitting the form is in your hands.

### How to override default action when clicking a link

When you click a link (an anchor tag `a` with a `href` attribute), the default action is a navigation on the browser to the clicked link.

What if you wanted to intercept that action and maybe do something before the navigation? For example, checking that the user has access to the page they want to navigate to. Here is how you'd do that:

```html
<a id="link" href="https://google.com">Google</a>
```

```js
const link = document.getElementById("link")

link.addEventListener("click", event => {
  event.preventDefault()

  // do something and navigate
})
```

You can test it out. When you click the "Google" link, no navigation occurs – because you have prevented the default navigation action. Now, you have to handle the navigation yourself.


## event.stopPropagation()

Propagation is the act of spreading something, in this case, events. The `stopPropagation` method is used to prevent the spreading of events when an event is triggered on an element.

In JavaScript, when you trigger an event on an element, it bubbles up the tree to the parents and ancestors of that element. Basically, the element with the event is "inside" the parent's container, so the parent also receives the events.

To explain this better, I'll use an example.

### Clicking the child of an element

Let's say you have the following elements:

```html
<div>
  <button>Click me</button>
</div>
```

When you click on the `button`, you are also clicking on the `div` container because the button is in the container. This logic means that the click event propagates from the button to the container, and the event keeps spreading to all the grandparents until it gets to the root.

To verify this, I will explain how this works with this code:

```html
<div id="div">
  <button id="button">Click me</button>
</div>
```

```js
const div = document.getElementById('div')
const button = document.getElementById('button')

button.addEventListener('click', () => {
  console.log('button clicked')
})

div.addEventListener('click', () => {
  console.log('div container clicked')
})
```

When you try to run this on your browser and you click the button, you will get this result:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-4.png)

The `div` container also receives the click event, so the click callback function is also called.

Event propagations are the default behaviour of events and elements, but in some cases, you may not want some behaviours. Amongst many examples, here is one.

Here is the Gmail New Message popup:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-6.png)

At the top, you have the three action buttons. One minimizes the popup, one makes the popup fullscreen, and one closes the popup.

But the top bar, with the "New Message" text, also has a click handler, so that when it's clicked, it minimizes the popup:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-8.png)

One thing you want to avoid here is that, on clicking any of the buttons, you do not want the click event to propagate to the top bar and also execute the function for that event. What I mean is, on clicking the close button, for example, you do not want the top bar to also minimize. 

In cases like this, you want to stop the propagation.

Let's say the popup is built like this:

```html
<div id='top-bar'>
  <!-- The Message Element -->
  <!-- The Buttons -->
</div>
```

```js
const topBar = document.getElementById('top-bar')
const closeButton = document.getElementById('close-btn')

topBar.addEventListener('click', () => {
  // minimize or maximize popup
})

closeButton.addEventListener('click', () => {
  // close popup
})
```

You will also want to add the `stopPropagation` method to the button's listener, to avoid spreading the event to the top bar. To do so, you will update the button's listener to:

```js
closeButton.addEventListener('click', (event) => {
  event.stopPropagation()
  // close popup
})
```

With this in place, the top bar will only receive the click event when it is directly clicked on.

## Wrapping Up

The difference between `event.preventDefault()` and `event.stopPropagation()` is that the former prevents default actions made by the browser, while the latter prevents the default behaviors of events –propagating up the tree.

These default actions and behaviors are not mistakes, and you do not have to worry about them while you code. But there are scenarios where you want to override them, as we have seen in the examples in this article.

