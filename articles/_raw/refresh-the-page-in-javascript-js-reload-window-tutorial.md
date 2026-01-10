---
title: Refresh the Page in JavaScript – JS Reload Window Tutorial
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-06-27T17:41:15.000Z'
originalURL: https://freecodecamp.org/news/refresh-the-page-in-javascript-js-reload-window-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/cover-template--4-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When you''re developing applications like a blog or a page where the data
  may change based on user actions, you''ll want that page to refresh frequently.

  When the page refreshes or reloads, it will show any new data based off those user
  interactions. G...'
---

When you're developing applications like a blog or a page where the data may change based on user actions, you'll want that page to refresh frequently.

When the page refreshes or reloads, it will show any new data based off those user interactions. Good news – you can implement this type of functionality in JavaScript with a single line of code.

In this article, we will learn how to reload a webpage in JavaScript, as well as see some other situations where we might want to implement these reloads and how to do so.

### Here's an Interactive Scrim about How to Refesh the Page in JavaScript

<iframe src="https://scrimba.com/scrim/cQ4ZKmt3?embed=freecodecamp,mini-header" width="100%" height="420"></iframe>

## How to Refresh a Page in JavaScript With `location.reload()`

You can use the `location.reload()` JavaScript method to reload the current URL. This method functions similarly to the browser's Refresh button.

The `reload()` method is the main method responsible for page reloading. On the other hand, `location` is an interface that represents the actual location (URL) of the object it is linked to – in this case the URL of the page we want to reload. It can be accessed via either `document.location` or `window.location`.

The following is the syntax for reloading a page:

```js
window.location.reload();
```

**Note:** When you read through some resources on “page reload in JavaScript”, you'll come across various explanations stating that the relaod method takes in boolean values as parameters and that the `location.reload(true)` helps force-reload so as to bypass its cache. But this isn't the case.

According to the [MDN Documentation](https://developer.mozilla.org/en-US/docs/Web/API/Location/reload), a boolean parameter is not part of the current specification for `location.reload()` — and in fact has *never* been part of any specification for `location.reload()` ever published.

Browsers such as Firefox, on the other hand, support the use of a non-standard boolean parameter known as `forceGet` for `location.reload()`, which instructs Firefox to bypass its cache and force-reload the current document.

Aside from Firefox, any parameters you specify in a `location.reload()` call in other browsers will be ignored and have no effect.

## How to Perform Page Reload/Refresh in JavaScript When a Button is Clicked

So far we have seen how reload works in JavaScript. Now let’s now see how you can implement this could when an event occurs or when an action like a button click occurs:

```js
<button type="button" onClick="window.location.reload()">
   Reload Page
</button>
```

**Note:** This works similarly to when we use `document.location.reload()`.

## How to Refresh/Reload a Page Automatically in JavaScript

We can also allow a page refersh after a fixed time use the `setTimeOut()` method as seen below:

```js
setTimeout(() => {
  document.location.reload();
}, 3000);
```

Using the code above our web page will reload every 3 seconds.

So far, we've seen how to use the reload method in our HTML file when we attach it to specific events, as well as in our JavaScript file.

## How to Refresh/Reload a Page Using the History Function in JavaScript

The History function is another method for refreshing a page. The history function is used as usual to navigate back or forward by passing in either a positive or negative value.

For example, if we want to go back in time, we will use:

```js
history.go(-1);
```

This will load the page and take us to the previous page we navigated to. But if we only want to refresh the current page, we can do so by not passing any parameters or by passing `0` (a neutral value):

```js
history.go();
history.go(0);
```

**Note:** This also works the same way as we added the `reload()` method to the `setTimeOut()` method and the click event in HTML.

## Wrapping Up

In this article, we learned how to refresh a page using JavaScript. We also clarified a common misconception that leads to people passing boolean parameters into the `reload()` method.

Thanks for reading!

Embark on a journey of learning! [Browse 200+ expert articles on web development](https://joelolawanle.com/contents). Check out [my blog](https://joelolawanle.com/posts) for more captivating content from me.
