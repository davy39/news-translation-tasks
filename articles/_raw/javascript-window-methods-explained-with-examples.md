---
title: JavaScript Window Methods Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-window-methods-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d1d740569d1a4ca35fa.jpg
tags:
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Window location Method

  The window.location object can be used to get information on the current page address
  (URL) and to redirect the browser to a new page.

  The window.location object can be written without the window prefix, as just location.

  Some ...'
---

## **Window location Method**

The `window.location` object can be used to get information on the current page address (URL) and to redirect the browser to a new page.

The `window.location` object can be written without the `window` prefix, as just `location`.

## Some examples:

* `window.location.href` returns the href (URL) of the current page
* `window.location.hostname` returns the domain name of the web host
* `window.location.host` returns both the host name and any associated port
* `window.location.pathname` returns the path and filename of the current page
* `window.location.protocol` returns the web protocol used (http: or https:)
* `window.location.assign()` loads a new document

### More Information:

[MDN](https://developer.mozilla.org/docs/Web/API/Window/location)

## **Window setInterval Method**

The `setInterval()` method calls a function or evaluates an expression at specified intervals (in milliseconds).

```js
setInterval(function(){ 
  alert("Hello");
}, 3000); 
```

The `setInterval()` method will continue calling the function until `clearInterval()` is called, or the window is closed.

The `setInterval()` method can pass additional parameters to the function, as shown in the example below.

```js
setInterval(function, milliseconds, parameter1, parameter2, parameter3); 
```

The ID value returned by `setInterval()` is used as the parameter for the `clearInterval()` method.

Tips:

* 1000 ms = 1 second.
* To execute a function only once, after a specified number of milliseconds, use the `setTimeout()` method.

## Window setTimeout Method

The `setTimeout()` method sets a timer in milliseconds, then calls a function or evaluates an expression when the timer runs out.

Notes:

* `setTimeout()` uses milliseconds, and 1000 ms is equal to 1 second
* This method only executes the function or expression you pass to it once. Use the `setInterval()` method if you need to repeat the execution multiple times
* To stop the function or expression passed to it, use the `clearTimeout()` method

The syntax of the `setTimout()` method is as follows:

```js
setTimeout(function, milliseconds, param1, param2, ...);
```

For example:

```js
setTimeout(function() { 
  alert("Hello");
}, 3000);
```

A very important thing to remember about `setTimeout()` is that it's executed asynchronously:

```js
console.log("A");
setTimeout(function() { console.log("B"); }, 0);
console.log("C");

// The order in the console will be
// A
// C
// B
```

The order of the console logs is probably not what you expected. To solve this problem and make sure that your code is executed synchronously, you just need to nest the last `console.log` statement in the function:

```js
console.log("A");
setTimeout(function() {
    console.log("B");
    console.log("C");
}, 0);

// The order in the console will be
// A
// B
// C
```

## **Window clearTimeout Method**

The `clearTimeout()` method is used stop a timer set with the `setTimeout()` method.

```js
    clearTimeout(setTimeout_ID); 
```

To be able to use the `clearTimeout()` method, you must use a global variable. See the example below

The `clearTimeout()` method works by using the id that's returned by `setTimeout()`. Because of this, it's often a good idea to use a global variable to store `setTimeout()`, then clear that when necessary:

```js
const myTimeout = setTimeout(function, milliseconds);

...

// Later, to clear the timeout
clearTimeout(myTimeout);
```

## **Window clearInterval Method**

The `clearInterval()` method is used to clear a timer set with the `setInterval()` method.

```js
clearInterval(setInteval_ID); 
```

The `clearTimeout()` method works by using the id that's returned by `setInterval()`. Because of this, it's often a good idea to use a global variable to store `setInterval()`, then clear that when necessary:

```js
const myInterval = setInterval(function, milliseconds);

...

// Later, to clear the timeout
clearInterval(myInterval);
```

## Window localStorage Method

`localStorage` provides a way for your web applications to store key/value pairs locally within the user’s browser.

Before HTML5 and `localStorage`, web app data had to be stored in cookies. Every HTTP request includes cookies, and these were once a legitimate method for storing application data locally on client devices. However, a lot of the same data was being transmitted with cookies, and since they were limited to around 4 KB of data, it was difficult to store everything your application needed.

The storage limit for `localStorage` is 10 MB of data per domain, and it is considered more efficient because the information stored in it is never transferred to the server with every request.

### **Types of Web Storage**

`localStorage` is one of two modern methods for browsers to store data locally:

* `localStorage`: This stores data with no expiration date. The data in `localStorage` persists even when the user’s browser is closed and reopened.
* `sessionStorage`: This is similar to `localStorage`, except that it stores data for one session only. This data is removed once the user closes their browser.

### **HTML5 localStorage Methods**

`localStorage` comes with a few different JavaScript methods that makes it very easy to work with.

To set data:

```javascript
localStorage.setItem('Name', 'somevalue');
```

To retrieve some data from storage:

```javascript
localStorage.getItem('Name');
```

To remove or delete some data:

```javascript
localStorage.removeItem('Name');
```

To clear everything in storage (not just an individual item):

```javascript
localStorage.clear();
```

To get the number of properties in storage:

```javascript
localStorage.length;
```

Note: All of the methods above also work with `sessionStorage`. Simply replace `localStorage` with `sessionStorage`.

## Window open Method

The Window `open()` method is used to open a new browser window or tab, depending on the parameters and the user's browser settings. This method is typically used for popups, and is blocked by default in a lot of modern browsers.

The syntax of the `open()` method is:

```js
const window =  window.open(url, windowName, windowFeatures);
```

### Parameters

* `url`: A string for the resource you want to load.
* `windowName`: A string indicating the target name of the new window or tab. Note that this will not be used as the title for the new window/tab.
* `windowFeatures`: An optional comma-separated list of strings of features such as the size of the new window, its position, whether or not to display the menu bar, and so on.

### Example

```javascript
let windowObjectReference;
const strWindowFeatures = "menubar=yes,location=yes,resizable=yes,scrollbars=yes,status=yes";

function openRequestedPopup() {
  windowObjectReference = window.open("https://www.freecodecamp.org/", "fCC_WindowName", strWindowFeatures);
}

openRequestedPopup();
```

The above code will attempt to open a popup to the freeCodeCamp landing page. 

## **Window Confirm Method**

You can use the `confirm` method to ask a user to double check a decision on a web page. When you call this method, the browser will display a dialog box with two choices along the lines of “OK” and “Cancel.”

For example, say someone has just clicked a Delete button. You could run the following code:

```javascript
if (window.confirm("Are you sure you want to delete this item?")) {
  // Delete the item
}
```

The message “Are you sure you want to delete this item?” will appear in the dialog box. If the user clicks OK, the confirm method will return `true` and the browser will run the code inside the if statement. If he or she clicks Cancel, the method will return `false` and nothing else will happen. This provides some protection against someone accidentally clicking Delete.

