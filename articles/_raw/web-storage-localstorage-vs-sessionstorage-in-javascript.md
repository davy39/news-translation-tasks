---
title: Web Storage Explained – How to Use localStorage and sessionStorage in JavaScript
  Projects
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2023-10-09T16:45:31.000Z'
originalURL: https://freecodecamp.org/news/web-storage-localstorage-vs-sessionstorage-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/web-storage-explained-local-and-session-storage-objects-in-javascript-codesweetly.jpg
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: storage
  slug: storage
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Web Storage is what the JavaScript API browsers provide for storing data
  locally and securely within a user’s browser.

  Session and local storage are the two main types of web storage. They are similar
  to regular properties objects, but they persist (...'
---

**Web Storage** is what the JavaScript [API](https://codesweetly.com/application-programming-interface-api-explained) browsers provide for storing data locally and securely within a user’s browser.

Session and local storage are the two main types of web storage. They are similar to regular [properties objects](https://codesweetly.com/javascript-properties-object), but they persist (do not disappear) when the webpage reloads.

This article aims to show you exactly how the two storage objects work in JavaScript. We will also use a To-Do list exercise to practice using web storage in a web app project.

## Table of Contents

1. [What is the Session Storage Object?](#heading-what-is-the-session-storage-object)
2. [What is the Local Storage Object?](#heading-what-is-the-local-storage-object)
3. [How to Access the Session and Local Storage Objects](#heading-how-to-access-the-session-and-local-storage-objects)
4. [What are Web Storage’s Built-In Interfaces?](#heading-what-are-web-storages-built-in-interfaces)
   - [What is web storage’s `setItem()` method?](#heading-what-is-web-storages-setitem-method)
   - [What is web storage’s `key()` method?](#heading-what-is-web-storages-key-method)
   - [What is web storage’s `getItem()` method?](#heading-what-is-web-storages-getitem-method)
   - [What is web storage’s `length` property?](#heading-what-is-web-storages-length-property)
   - [What is web storage’s `removeItem()` method?](#heading-what-is-web-storages-removeitem-method)
   - [What is web storage’s `clear()` method?](#heading-what-is-web-storages-clear-method)
5. [Time to Practice with Web Storage 🤸‍♂️🏋️‍♀️](#heading-time-to-practice-with-web-storage)
   - [The Problem](#heading-the-problem)
   - [Your Exercise](#heading-your-exercise)
   - [Bonus Exercise](#heading-bonus-exercise)
6. [How Did You Go About Solving the Web Storage Exercise?](#heading-how-did-you-go-about-solving-the-web-storage-exercise)
   - [How to prevent the Session Storage pane’s To-Do items from disappearing on page reload](#heading-how-to-prevent-the-session-storage-panes-to-do-items-from-disappearing-on-page-reload)
   - [How to prevent the Local Storage pane’s To-Do items from disappearing on page reload or reopen](#heading-how-to-prevent-the-local-storage-panes-to-do-items-from-disappearing-on-page-reload-or-reopen)
   - [How to auto-display the Session section’s previously added tasks on page reload](#heading-how-to-auto-display-the-session-sections-previously-added-tasks-on-page-reload)
   - [How to auto-display the Local section’s previously added tasks on page reload or reopen](#heading-how-to-auto-display-the-local-sections-previously-added-tasks-on-page-reload-or-reopen)
   - [How to check the total items in the browser’s session storage](#heading-how-to-check-the-total-items-in-the-browsers-session-storage)
   - [How to display the local storage’s zeroth index item’s name](#heading-how-to-display-the-local-storages-zeroth-index-items-name)
   - [How to empty the browser’s session storage](#heading-how-to-empty-the-browsers-session-storage)
7. [How to Continue Practicing with Web Storage 🧗‍♀️🚀](#heading-how-to-continue-practicing-with-web-storage)
8. [Web Storage vs. Cookies: What is the Difference?](#heading-web-storage-vs-cookies-what-is-the-difference)
9. [Wrapping up](#heading-wrapping-up)

Without further ado, let’s discuss session storage.

## What is the Session Storage Object?

The session storage object (`window.sessionStorage`) stores data that persists for only one session of an opened tab.

In other words, whatever gets stored in the `window.sessionStorage` object will not disappear on a reload of the web page. Instead, the computer will delete the stored data only when users close the browser tab or window.

**Note the following:**

* The data stored inside the session storage is per-[origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin) and per-instance. In other words, `http://freecodecamp.com`’s `sessionStorage` object is different from `https://freecodecamp.com`’s `sessionStorage` object because the two origins use different [schemes](https://codesweetly.com/web-address-url#scheme) (`http` and `https`).
* Per-instance means per-window or per-tab. In other words, the `sessionStorage` object’s lifespan expires once users close the instance (window or tab).
* Browsers create a unique page session for each new tab or window. Therefore, users can run multiple instances of an app without interfering with each instance’s session storage. (Note: Cookies do not have good support for running multiple instances of the same app. Such an attempt can cause errors such as [double entry of bookings](https://html.spec.whatwg.org/multipage/webstorage.html#introduction-15).)
* Session storage is a property of the global `Window` object. So `sessionStorage.setItem()` is equivalent to `window.sessionStorage.setItem()`.

## What is the Local Storage Object?

The local storage object (`window.localStorage`) stores data that persists even when users close their browser tab (or window).

In other words, whatever gets stored in the `window.localStorage` object will not disappear during a reload or reopening of the web page or when users close their browsers. Those data have no expiration time. Browsers never clear them automatically.

The computer will delete the `window.localStorage` object’s content in the following instances only:

1. When the content gets cleared through JavaScript
2. When the browser’s cache gets cleared

**Note the following:**

* The `window.localStorage` object’s storage limit is larger than the `window.sessionStorage`.
* The data stored inside the local storage is per-[origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). In other words, `http://freecodecamp.com`’s `localStorage` object is different from `https://freecodecamp.com`’s `localStorage` object because the two origins use different [schemes](https://codesweetly.com/web-address-url#scheme) (`http` and `https`).
* There are inconsistencies with how browsers handle the local storage of documents not served from a web server (for instance, pages with a `file:` URL scheme). Therefore, the `localStorage` object may behave differently among browsers when used with non-HTTP URLs, such as `file:///document/on/users/local/system.html`.
* Local storage is a property of the global `Window` object. Therefore, `localStorage.setItem()` is equivalent to `window.localStorage.setItem()`.

## How to Access the Session and Local Storage Objects

You can access the two web storages by:

1. Using the same technique as you'd use for [accessing regular JavaScript objects](https://codesweetly.com/javascript-properties-object#how-to-access-an-objects-value)
2. Using web storage’s built-in interfaces

For instance, consider the snippet below:

```js
sessionStorage.bestColor = "Green";
sessionStorage["bestColor"] = "Green";
sessionStorage.setItem("bestColor", "Green");
```

The three statements above do the same thing—they set `bestColor`’s value. But the third line is recommended because it uses web storage’s `setItem()` method.

**Tip:** you should prefer using the web storage’s built-in interfaces to avoid [the pitfalls of using objects as key/value stores](https://2ality.com/2012/01/objects-as-maps.html).

Let’s discuss more on the web storage’s built-in interfaces below.

## What are Web Storage’s Built-In Interfaces?

The web storage built-in interfaces are the recommended tools for reading and manipulating a browser’s `sessionStorage` and `localStorage` objects.

The six (6) built-in interfaces are:

* `setItem()`
* `key()`
* `getItem()`
* `length`
* `removeItem()`
* `clear()`

Let’s discuss each one now.

### What is web storage’s `setItem()` method?

The `setItem()` method stores its `key` and `value` arguments inside the specified web storage object.

#### Syntax of the `setItem()` method

`setItem()` accepts two required [arguments](https://codesweetly.com/javascript-arguments). Here is the syntax:

```js
webStorageObject.setItem(key, value);
```

* `webStorageObject` represents the storage object (`localStorage` or `sessionStorage`) you wish to manipulate.
* `key` is the first argument accepted by `setItem()`. It is a required string argument representing the name of the web storage property you want to create or update.
* `value` is the second argument accepted by `setItem()`. It is a required string argument specifying the value of the `key` you are creating or updating.

**Note:**

* The `key` and `value` arguments are always strings.
* Suppose you provide an integer as a `key` or `value`. In that case, browsers will convert them to strings automatically.
* `setItem()` may display an error message if the storage object is full.

#### Example 1: How to store data in the session storage object

1. Invoke `sessionStorage`’s `setItem()` method.
2. Provide the name and value of the data you wish to store.

```js
// Store color: "Pink" inside the browser's session storage object:
sessionStorage.setItem("color", "Pink");

// Log the session storage object to the console:
console.log(sessionStorage);

// The invocation above will return:
{color: "Pink"}
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/setitem/js-25hgkp)

**Note:** Your browser’s session storage may contain additional data if it already uses the storage object to store information.

#### Example 2: How to store data in the local storage object

1. Invoke `localStorage`’s `setItem()` method.
2. Provide the name and value of the data you wish to store.

```js
// Store color: "Pink" inside the browser's local storage object:
localStorage.setItem("color", "Pink");

// Log the local storage object to the console:
console.log(localStorage);

// The invocation above will return:
{color: "Pink"}
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/setitem/js-2hluvw)

**Note:**

* Your browser’s local storage may contain additional data if it already uses the storage object to store information.
* It is best to serialize objects before storing them in local or session storage. Otherwise, the computer will store the object as `"[object Object]"`.

#### Example 3: Browsers use `"[object Object]"` for non-serialized objects in the web storage

```js
// Store myBio object inside the browser's session storage object:
sessionStorage.setItem("myBio", { name: "Oluwatobi" });

// Log the session storage object to the console:
console.log(sessionStorage);

// The invocation above will return:
{myBio: "[object Object]", length: 1}
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/setitem/js-n8m7hc)

You can see that the computer stored the object as `"[object Object]"` because we did not serialize it.

#### Example 4: How to store serialized objects in the web storage

```js
// Store myBio object inside the browser's session storage object:
sessionStorage.setItem("myBio", JSON.stringify({ name: "Oluwatobi" }));

// Log the session storage object to the console:
console.log(sessionStorage);

// The invocation above will return:
{myBio: '{"name":"Oluwatobi"}', length: 1}
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/setitem/js-edfh43)

We used `JSON.stringify()` to convert the object to JSON before storing it in the web storage.

**Tip:** Learn [how to convert JSON to JavaScript objects](https://codesweetly.com/json-explained#how-to-convert-a-json-text-to-a-javascript-object).

### What is web storage’s `key()` method?

The `key()` method retrieves a specified web storage item’s name (key).

#### Syntax of the `key()` method

`key()` accepts one required argument. Here is the syntax:

```js
webStorageObject.key(index);
```

* `webStorageObject` represents the storage object (`localStorage` or `sessionStorage`) whose key you wish to get.
* `index` is a required argument. It is an [integer](https://codesweetly.com/web-tech-terms-i#integer) specifying the [index](https://codesweetly.com/web-tech-terms-i#index) of the item whose key you want to get.

#### Example 1: How to get the name of an item in the session storage object

1. Invoke `sessionStorage`’s `key()` method.
2. Provide the index of the item whose name you wish to get.

```js
// Store carColor: "Pink" inside the browser's session storage object:
sessionStorage.setItem("carColor", "Pink");

// Store pcColor: "Yellow" inside the session storage object:
sessionStorage.setItem("pcColor", "Yellow");

// Store laptopColor: "White" inside the session storage object:
sessionStorage.setItem("laptopColor", "White");

// Get the name of the item at index 1:
sessionStorage.key(1);
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/key/js-tptqtg)

**Important:** The [user-agent](https://en.wikipedia.org/wiki/User_agent) defines the order of items in the session storage. In other words, `key()`’s output may vary based on how the user-agent orders the web storage’s items. So you shouldn't rely on `key()` to return a constant value.

#### Example 2: How to get the name of an item in the local storage object

1. Invoke `localStorage`’s `key()` method.
2. Provide the index of the item whose name you wish to get.

```js
// Store carColor: "Pink" inside the browser's local storage object:
localStorage.setItem("carColor", "Pink");

// Store pcColor: "Yellow" inside the local storage object:
localStorage.setItem("pcColor", "Yellow");

// Store laptopColor: "White" inside the local storage object:
localStorage.setItem("laptopColor", "White");

// Get the name of the item at index 1:
localStorage.key(1);
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/key/js-tclrbd)

**Important:** The user-agent defines the order of items in the local storage. In other words, `key()`’s output may vary based on how the user-agent orders the web storage’s items. So you shouldn't rely on `key()` to return a constant value.

### What is web storage’s `getItem()` method?

The `getItem()` method retrieves the value of a specified web storage item.

#### Syntax of the `getItem()` method

`getItem()` accepts one required argument. Here is the syntax:

```js
webStorageObject.getItem(key);
```

* `webStorageObject` represents the storage object (`localStorage` or `sessionStorage`) whose item you wish to get.
* `key` is a required argument. It is a [string](https://codesweetly.com/javascript-primitive-data-type#string-primitive-data-type) specifying the name of the web storage [property](https://codesweetly.com/javascript-properties-object#syntax-of-a-javascript-object) whose value you want to get.

#### Example 1: How to get data from the session storage object

1. Invoke `sessionStorage`’s `getItem()` method.
2. Provide the name of the data you wish to get.

```js
// Store color: "Pink" inside the browser's session storage object:
sessionStorage.setItem("color", "Pink");

// Get color's value from the session storage:
sessionStorage.getItem("color");

// The invocation above will return:
"Pink"
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/getitem/js-xk9auv)

#### Example 2: How to get data from the local storage object

1. Invoke `localStorage`’s `getItem()` method.
2. Provide the name of the data you wish to get.

```js
// Store color: "Pink" inside the browser's local storage object:
localStorage.setItem("color", "Pink");

// Get color's value from the local storage:
localStorage.getItem("color");

// The invocation above will return:
"Pink"
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/getitem/js-terw5e)

**Note:** The `getItem()` method will return `null` if its argument does not exist in the specified web storage.

### What is web storage’s `length` property?

The `length` property returns the number of [properties](https://codesweetly.com/javascript-properties-object#syntax-of-a-javascript-object) in the specified web storage.

#### Syntax of the `length` property

Here is `length`’s syntax:

```js
webStorageObject.length;
```

`webStorageObject` represents the storage object (`localStorage` or `sessionStorage`) whose length you wish to verify.

#### Example 1: How to verify the number of items in the session storage object

Invoke `sessionStorage`’s `length` property.

```js
// Store carColor: "Pink" inside the browser's session storage object:
sessionStorage.setItem("carColor", "Pink");

// Store pcColor: "Yellow" inside the session storage object:
sessionStorage.setItem("pcColor", "Yellow");

// Store laptopColor: "White" inside the session storage object:
sessionStorage.setItem("laptopColor", "White");

// Verify the number of items in the session storage:
sessionStorage.length;

// The invocation above may return:
3
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/length/js-zasgst)

**Note:** Your `sessionStorage.length` invocation may return a value greater than `3` if your browser’s session storage already contains some stored information.

#### Example 2: How to verify the number of items in the local storage object

Invoke `localStorage`’s `length` property.

```js
// Store carColor: "Pink" inside the browser's local storage object:
localStorage.setItem("carColor", "Pink");

// Store pcColor: "Yellow" inside the local storage object:
localStorage.setItem("pcColor", "Yellow");

// Store laptopColor: "White" inside the local storage object:
localStorage.setItem("laptopColor", "White");

// Verify the number of items in the local storage:
localStorage.length;

// The invocation above may return:
3
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/length/js-3f6lac)

**Note:** Your `localStorage.length` invocation may return a value greater than `3` if your browser's local storage already contains some stored information.

### What is web storage’s `removeItem()` method?

The `removeItem()` method removes a property from the specified web storage.

#### Syntax of the `removeItem()` Method

`removeItem()` accepts one required argument. Here is the syntax:

```js
webStorageObject.removeItem(key);
```

* `webStorageObject` represents the storage object (`localStorage` or `sessionStorage`) whose item you wish to remove.
* `key` is a required argument. It is a string specifying the name of the web storage property you want to remove.

#### Example 1: How to remove data from the session storage object

1. Invoke `sessionStorage`’s `removeItem()` method.
2. Provide the name of the data you wish to remove.

```js
// Store carColor: "Pink" inside the browser's session storage object:
sessionStorage.setItem("carColor", "Pink");

// Store pcColor: "Yellow" inside the session storage object:
sessionStorage.setItem("pcColor", "Yellow");

// Store laptopColor: "White" inside the session storage object:
sessionStorage.setItem("laptopColor", "White");

// Remove the pcColor item from the session storage:
sessionStorage.removeItem("pcColor");

// Confirm whether the pcColor item still exists in the session storage:
sessionStorage.getItem("pcColor");

// The invocation above will return:
null
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/removeitem/js-1mywnh)

**Note:** The `removeItem()` method will do nothing if its argument does not exist in the session storage.

#### Example 2: How to remove data from the local storage object

1. Invoke `localStorage`’s `removeItem()` method.
2. Provide the name of the data you wish to remove.

```js
// Store carColor: "Pink" inside the browser's local storage object:
localStorage.setItem("carColor", "Pink");

// Store pcColor: "Yellow" inside the local storage object:
localStorage.setItem("pcColor", "Yellow");

// Store laptopColor: "White" inside the local storage object:
localStorage.setItem("laptopColor", "White");

// Remove the pcColor item from the local storage:
localStorage.removeItem("pcColor");

// Confirm whether the pcColor item still exists in the local storage:
localStorage.getItem("pcColor");

// The invocation above will return:
null
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/removeitem/js-8doou3)

**Note:** The `removeItem()` method will do nothing if its argument does not exist in the local storage.

### What is web storage’s `clear()` method?

The `clear()` method clears (deletes) all the items in the specified web storage.

#### Syntax of the `clear()` Method

`clear()` accepts no argument. Here is the syntax:

```js
webStorageObject.clear();
```

`webStorageObject` represents the storage object (`localStorage` or `sessionStorage`) whose items you wish to clear.

#### Example 1: How to clear all items from the session storage object

Invoke `sessionStorage`’s `clear()` method.

```js
// Store carColor: "Pink" inside the browser's session storage object:
sessionStorage.setItem("carColor", "Pink");

// Store pcColor: "Yellow" inside the session storage object:
sessionStorage.setItem("pcColor", "Yellow");

// Store laptopColor: "White" inside the session storage object:
sessionStorage.setItem("laptopColor", "White");

// Clear all items from the session storage:
sessionStorage.clear();

// Confirm whether the session storage still contains any item:
console.log(sessionStorage);

// The invocation above will return:
{length: 0}
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/clear/js-an86yu)

#### Example 2: How to clear all items from the local storage object

Invoke `localStorage`’s `clear()` method.

```js
// Store carColor: "Pink" inside the browser's local storage object:
localStorage.setItem("carColor", "Pink");

// Store pcColor: "Yellow" inside the local storage object:
localStorage.setItem("pcColor", "Yellow");

// Store laptopColor: "White" inside the local storage object:
localStorage.setItem("laptopColor", "White");

// Clear all items from the local storage:
localStorage.clear();

// Confirm whether the local storage still contains any item:
console.log(localStorage);

// The invocation above will return:
{length: 0}
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/clear/js-w5vyem)

Now that we know what web storage is and how to access it, we can practice using it in a JavaScript project.

## Time to Practice with Web Storage 🤸‍♂️🏋️‍♀️

Consider the following To-Do List app:

%[https://www.youtube.com/watch?v=78MRup0PN7c]

### The Problem

The issue with the [To-Do List app](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-mgl6ie) is this:

* Tasks disappear whenever users refresh the webpage.

### Your Exercise

Use the appropriate Web Storage APIs to accomplish the following tasks:

1. Prevent the Session pane’s To-Do items from disappearing whenever users reload the browser.
2. Prevent the Local section’s To-Do items from disappearing whenever users reload or close their browser tab (or window).
3. Auto-display the Session section's previously added tasks on page reload.
4. Auto-display the Local section's previously added tasks on page reload (or browser reopen).

### Bonus Exercise

Use your browser’s console to:

1. Check the number of items in your browser’s session storage object.
2. Display the name of your local storage’s zeroth index item.
3. Delete all the items in your browser’s session storage.

[**Try the Web Storage Exercise**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-mgl6ie)

**Note:** You will benefit much more from this tutorial if you attempt the exercise yourself.

If you get stuck, don’t be discouraged. Instead, review the lesson and give it another try.

Once you’ve given it your best shot (you’ll only cheat yourself if you don’t!), we can discuss how I approached the exercise below.

## How Did You Go About Solving the Web Storage Exercise?

Below are feasible ways to get the exercise done.

### How to prevent the Session Storage pane’s To-Do items from disappearing on page reload

Whenever users click the “Add task” button,

1. Get existing session storage’s content, if any. Otherwise, return an empty array.
2. Merge the existing to-do items with the user’s new input.
3. Add the new to-do list to the browser’s session storage object.

**Here’s the code:**

```js
sessionAddTaskBtn.addEventListener('click', () => {
  // Get existing session storage's content, if any. Otherwise, return an empty array:
  const currentTodoArray =
    JSON.parse(sessionStorage.getItem('codesweetlyStore')) || [];

  // Merge currentTodoArray with the user's new input:
  const newTodoArray = [
    ...currentTodoArray,
    { checked: false, text: sessionInputEle.value },
  ];

  // Add newTodoArray to the session storage object:
  sessionStorage.setItem('codesweetlyStore', JSON.stringify(newTodoArray));

  const todoLiElements = createTodoLiElements(newTodoArray);
  sessionTodosContainer.replaceChildren(...todoLiElements);
  sessionInputEle.value = '';
});
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-txyt66)

**Note:** The three dots (`...`) preceding the `currentTodoArray` variable represent the [spread operator](https://codesweetly.com/spread-operator). We used it in the `newTodoArray` object to copy `currentTodoArray`’s items into `newTodoArray`.

### How to prevent the Local Storage pane’s To-Do items from disappearing on page reload or reopen

1. Get existing local storage’s content, if any. Otherwise, return an empty array.
2. Merge the existing to-do items with the user’s new input.
3. Add the new to-do list to the browser’s local storage object.

**Here’s the code:**

```js
localAddTaskBtn.addEventListener('click', () => {
  // Get existing local storage's content, if any. Otherwise, return an empty array:
  const currentTodoArray =
    JSON.parse(localStorage.getItem('codesweetlyStore')) || [];

  // Merge currentTodoArray with the user's new input:
  const newTodoArray = [
    ...currentTodoArray,
    { checked: false, text: localInputEle.value },
  ];

  // Add newTodoArray to the local storage object:
  sessionStorage.setItem('codesweetlyStore', JSON.stringify(newTodoArray));

  const todoLiElements = createTodoLiElements(newTodoArray);
  localTodosContainer.replaceChildren(...todoLiElements);
  localInputEle.value = '';
});
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-dpuffp)

**Note:** The `localTodosContainer.replaceChildren(...todoLiElements)` statement tells the browser to replace `localTodosContainer`’s current children elements with the list of `<li>`s in the `todoLiElements` array.

### How to auto-display the Session section’s previously added tasks on page reload

Whenever users reload the page,

1. Get existing session storage’s content, if any. Otherwise, return an empty array.
2. Use the retrieved content to create `<li>` elements.
3. Populate the tasks display space with the `<li>` elements.

**Here’s the code:**

```js
window.addEventListener('load', () => {
  // Get existing session storage's content, if any. Otherwise, return an empty array:
  const sessionTodoArray =
    JSON.parse(sessionStorage.getItem('codesweetlyStore')) || [];

  // Use the retrieved sessionTodoArray to create <li> elements:
  const todoLiElements = createTodoLiElements(sessionTodoArray);

  // Populate the tasks display space with the todoLiElements:
  sessionTodosContainer.replaceChildren(...todoLiElements);
});
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-zga551)

### How to auto-display the Local section’s previously added tasks on page reload or reopen

Whenever users reload or reopen the page,

1. Get existing local storage’s content, if any. Otherwise, return an empty array.
2. Use the retrieved content to create `<li>` elements.
3. Populate the tasks display space with the `<li>` elements.

**Here’s the code:**

```js
window.addEventListener('load', () => {
  // Get existing local storage's content, if any. Otherwise, return an empty array:
  const localTodoArray =
    JSON.parse(localStorage.getItem('codesweetlyStore')) || [];

  // Use the retrieved localTodoArray to create <li> elements:
  const todoLiElements = createTodoLiElements(localTodoArray);

  // Populate the tasks display space with the todoLiElements:
  localTodosContainer.replaceChildren(...todoLiElements);
});
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-srmnst)

### How to check the total items in the browser’s session storage

Use session storage’s `length` property like so:

```js
console.log(sessionStorage.length);
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-m4pmhf)

### How to display the local storage’s zeroth index item’s name

Use the local storage’s `key()` method as follows:

```js
console.log(localStorage.key(0));
```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-th8xr7)

### How to empty the browser’s session storage

Use the session storage’s `clear()` method as follows:

```js
sessionStorage.clear();
```

## How to Continue Practicing with Web Storage 🧗‍♀️🚀

The to-do app still has a lot of potential. For instance, you can:

* Convert it to a React TypeScript application.
* Make it keyboard accessible.
* Allow users to delete or edit individual tasks.
* Allow users to star (mark as important) specific tasks.
* Let users specify due dates.

So, feel free to continue developing what we’ve built in this tutorial so you can better understand the web storage objects.

For instance, here’s my attempt at [making the two panes functional](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-ax8tvk):

%[https://youtu.be/gDiU-ubWPD4]

Before we wrap up our discussion, you should know some differences between web storage and cookies. So, let’s talk about that below.

## Web Storage vs. Cookies: What is the Difference?

Web storage and cookies are two main ways to store data locally within a user’s browser. But they work differently. Below are the main distinctions between them.

### Storage limit

**Cookies:** Have 4 kilobytes maximum [storage limit](https://docs.devexpress.com/AspNet/11912/common-concepts/cookies-support#browser-limitations).

**Web storage:** Can store a lot more than 4 kilobytes of data. For instance, Safari 8 can store up to 5 MB, while Firefox 34 permits 10 MB.

### Data transfer to the server

**Cookies:** Transfer data to the server whenever browsers send HTTP requests to the web server.

**Web storage:** Never transfers data to the server.

**Note:** It is a waste of users’ bandwidth to send data to the server if such information is needed only by the client (browser), not the server.

### Weak integrity and confidentiality

**Cookies:** Suffer from [weak integrity](https://datatracker.ietf.org/doc/html/rfc6265#section-8.6) and [weak confidentiality](https://datatracker.ietf.org/doc/html/rfc6265#section-8.5) issues.

**Web storage:** Do not suffer from weak integrity and confidentiality issues because it stores data per [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin).

### Property

**Cookies:** Cookies are a property of the [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document) object.

**Web storage:** Web storage is a property of the [`Window`](https://developer.mozilla.org/en-US/docs/Web/API/Window) object.

### Expiration

**Cookie:** You can specify a cookie’s expiration date.

**Web storage:** Browsers determine web storage’s expiration date.

### Retrieving individual data

**Cookies:** There’s no way to retrieve individual data. You always have to recall all the data to read any single one.

**Web storage:** You can choose the specific data you wish to retrieve.

### The syntax for storing data

**Cookies:**

```js
document.cookie = "key=value";
```

**Web storage:**

```js
webStorageObject.setItem(key, value);
```

### The syntax for reading data

**Cookies:**

```js
document.cookie;
```

**Web storage:**

```js
webStorageObject.getItem(key);
```

### The syntax for removing data

**Cookies:**

```js
document.cookie = "key=; expires=Thu, 01 May 1930 00:00:00 UTC";
```

The snippet above deletes the cookie by assigning an empty value to the `key` property and setting a past expiration date.

**Web storage:**

```js
webStorageObject.removeItem(key);
```

## Wrapping up

In this article, we discussed how to use web storage and its built-in interfaces. We also used a to-do list project to practice using the local and session storage objects to store data locally and securely within users’ browsers.

Thanks for reading!

### And here’s a useful React TypeScript resource:

I wrote a book about [Creating NPM Packages](https://amzn.to/3Pa4bI4)!

It is a beginner-friendly book that takes you from zero to creating, testing, and publishing NPM packages like a pro.

[![Creating NPM Package Book Now Available at Amazon](https://www.freecodecamp.org/news/content/images/2023/09/creating-npm-package-banner-codesweetly.png)](https://amzn.to/3Pa4bI4)


