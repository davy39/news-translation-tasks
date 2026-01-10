---
title: How to Use LocalStorage in JavaScript
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2024-02-20T21:37:46.000Z'
originalURL: https://freecodecamp.org/news/use-local-storage-in-modern-applications
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/JavaScript-localStorage-freeCodeCamp-Benjamin-Semah.png
tags:
- name: JavaScript
  slug: javascript
- name: localstorage
  slug: localstorage
- name: storage
  slug: storage
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'In modern web development, having a way to persist data helps developers
  improve performance and create a better user experience. And using local storage
  is an effective way of persisting data in an application.

  In this article, you will learn what l...'
---

In modern web development, having a way to persist data helps developers improve performance and create a better user experience. And using local storage is an effective way of persisting data in an application.

In this article, you will learn what local storage is and how to use it in modern web applications. You will also learn the advantages of using local storage, as well as some of its limitations.

## Table of Contents

* [What is Local Storage?](#what-is-local-storage)
    
* [Differences Between Local Storage and Session Storage](#differences-between-local-storage-and-session-storage)
    
* [How to Use Local Storage](#how-to-use-local-storage)
    
* [A Practical Example](#a-practical-example)
    
* [How to View Local Storage in DevTools](#how-to-view-local-storage-in-devtools)
    
* [Benefits of Using Local Storage](#benefits-of-using-local-storage)
    
* [Limitations of Local Storage](#limitations-of-using-local-storage)
    
* [Conclusion](#conclusion)
    

## What is Local Storage?

Local storage is a feature in web browsers that allows developers to save data in the user’s browser. It’s part of the web storage API, together with session storage.

Local storage works by accepting data in key-value pairs. It retains the data even when the user refreshes the page or closes the tab or browser.

## Differences Between Local Storage and Session Storage

As I mentioned earlier, the web storage API in modern browsers provides two main features for data storage. These are local storage and session storage.

The key differences between the two are the lifespan of the stored data and their scope.

Data in local storage remains available even when the tab/browser is closed. But closing the tab/browser clears any data stored in session storage.

Also, data in local storage is accessible across multiple browser tabs and windows. On the other hand, data in session storage is only accessible within specific browser tabs and is not shared.

## How to Use Local Storage

The local storage object provides different methods you can use to interact with it. With these methods, you can add, read, and delete data from local storage.

### How to Store Data in Local Storage

To store data in local storage, you use the `setItem()` method. This method takes in two arguments, a key and a value.

```javascript
localStorage.setItem(key, value)
```

If the key does not exist in local storage, the `setItem()` method will create a new key and assign the given value to it. But if a key with the same name exists in local storage, it will update the value of the key with the provided value.

### How to Read Data From Local Storage

To retrieve and use data from local storage, you use the `getItem()` method. This method takes in a key as an argument.

```javascript
localStorage.getItem(key)
```

If the given key exists in local storage, the method returns the value of that key. If it doesn’t, the method returns `null`.

### How to Store and Read Complex Data Values in Local Storage

Local storage can only store strings. This means if you need to store values like objects or arrays, you first need to get a string representation of the value. You do this using the `JSON.stringify()` method.

Example:

```javascript
const userObj = {
  username = "Maria",
  email: "maria@mail.com"
}

localStorage.setItem('user', JSON.stringify(userObj))
```

The `JSON.stringify()` method converts the `userObj` object into a string representation before sending it to local storage.

Now, when you want to retrieve the data back from local storage, you also need to change it from its string representation back to the original form. And you do that using the `JSON.parse()` method.

Example:

```javascript
const storedUserData = localStorage.getItem('user')

if (storedUserData) {
  const userData = JSON.parse(storedUserData)
  // You can use userData here...
} else {
  console.log('User data not found in local storage')
}
```

In the example above, we first check if there is data for ‘user’ in local storage before using the `JSON.parse()` method. This is important because if it does not exist in local storage, `JSON.parse()` will be applied to a `null` value (which will result in an error).

### How to Delete Data from Local Storage

There are two methods available for deleting data from local storage. One is the `removeItem()` method and the other is the `clear()` method.

You use the `removeItem()` method when you want to delete a single item from local storage. The method takes in a key as an argument and deletes the corresponding key-value pair from local storage.

```javascript
localStorage.removeItem(key)
```

But what if, instead of deleting a single key-value pair, you want to clear all data from the local storage? Well, local storage has a method for that - the `clear()` method.

```javascript
localStorage.clear()
```

The `clear()` method deletes all key-value pairs in the local storage for the current domain.

### How to Get the Name of a Key in Local Storage

If you want to get the name of a key at a particular index in local storage, you can use the `key()` method. It takes in a number as an argument and returns the name of the key at that specified index.

Example:

```javascript
localStorage.key(0)
```

The example above will return the name of the key at index 0. If there is no key at the specified index, the method will return null.

## A Practical Example

The following shows a practical demo of the difference between local storage and session storage.

In this example, we'll save the user's name in local storage and save the age in session storage.

```html
<!-- HTML --> 
<body>

  <h1 class="userName"></h1>
  <h2 class="userAge"></h2>

  <input type="text" class="name" placeholder="Enter name here"/>
  <button class="saveNameBtn">Save Name</button>
  
  <br />

  <input type="text" class="age" placeholder="Enter age here"/>
  <button class="saveAgeBtn">Save Age</button>
  
</body>
```

The markup includes two header elements. One for `userName` and the other for `userAge`. It also includes two input elements for name and age. Each input has an associated button we'll use for saving the data.

Now, let's use the `querySelector` method to select the various elements.

```javascript
const userNameText = document.querySelector(".userName")
const userAgeText = document.querySelector(".userAge")

const saveNameButton = document.querySelector(".saveNameBtn")
const saveAgeButton = document.querySelector(".saveAgeBtn")
```

### Code Example for Local Storage

```javascript
saveNameButton.addEventListener("click", () => {
  const userName = document.querySelector(".name").value
  userNameText.textContent = userName
  localStorage.setItem("name", userName)
})
```

First, we get the value of the name input, set it as the `textContent` of `userNameText`. And then use the `setItem()` of local storage to save the `userName` value in local storage.

Next, let's see how we can get the name value from local storage when we need it.

```javascript
function displayUserName () {
  const nameFromLocalStorage = localStorage.getItem("name")

  if (nameFromLocalStorage) {
    userNameText.textContent = nameFromLocalStorage
  } else {
    userNameText.textContent = "No name data in local storage"
  }
}

displayUserName()
```

The `displayUserName` function gets `nameFromLocalStorage` using the `getItem()` method. If the value exists in local storage, we set it as the `textContent` of the `userNameText` element. If it's `null` or doesn't exist, then we set `textContent` to the string *"No name data in local storage"*.

### Code Example for Session Storage

Now, let's do the same thing for the `age` value. The only difference here will be using session storage instead of local storage.

```javascript

saveAgeButton.addEventListener("click", () => {
  const userAge = document.querySelector(".age").value
  userAgeText.textContent = userAge
  sessionStorage.setItem("age", userAge)
})

function displayUserAge () {
  const ageFromSessionStorage = sessionStorage.getItem("age")

  if (ageFromSessionStorage) {
    userAgeText.textContent = ageFromSessionStorage
  } else {
    userAgeText.textContent = "No age data in session storage"
  }
}

displayUserAge()
```

The `setItem` and `getItem` methods also works for session storage.

### Demo:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/demo.gif align="left")

*Local storage and session storage demo.*

As you can see from the demo above, when you close and reopen the page, the `name` data from local storage persists. But the `age` data from session storage is cleared once the page closes.

[Try your hands on the code sample on StackBlitz](https://stackblitz.com/edit/vitejs-vite-hb86sa?file=index.html,main.js&terminal=dev)

## How to View Local Storage in DevTools

You can follow the steps below to inspect the contents of local storage in your browser's developer tools.

First, open DevTools. You can do that by right clicking on the web page and selecting "Inspect".

![Image](https://www.freecodecamp.org/news/content/images/2024/02/STEP-ONE.gif align="left")

*Demo of how to open the DevTools.*

Then, select the "Application" tab on the DevTools panel. Depending on your browser, this panel may have a different name. For example, it's called "Storage" in Safari and Firefox.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/STEP-TWO.gif align="left")

*Demo of how to open the "Application" panel in DevTools.*

Locate the "Storage" section on the sidebar showing a list of the various web storage options.

Click on "Local Storage" to expand and view its contents.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/STEP-THREE.gif align="left")

*Demo of how to open the local storage tab in the storage panel.*

You can click on individual items to view the corresponding key-value pair.

## Benefits of Using Local Storage

The following are some of the benefits local storage has over other storage mechanisms in modern web development.

1. **Persistent data:** When you use local storage, the stored data remains even when the user closes the tab or the browser. This is useful for saving user preferences, settings, and other relevant data. It can help create a seamless user experience.
    
2. **Offline access:** You can use local storage as a means to cache data which can be accessed even with limited or no internet. This makes it a useful feature for apps that rely on caching data for offline use like news readers, productivity apps, and so on.
    
3. **More storage capacity:** Compared to other storage means, local storage has a relatively high capacity. For example, cookies are limited to 4 kilobytes per domain. But local storage can store up to 5 megabytes of data per domain.
    

## Limitations of Using Local Storage

1. **Stores only strings:** As you learned earlier, local storage can only store string values. You can use the JSON `stringify` and `parse` methods to work around it. But some web developers may not prefer it as it can lead to writing complex code that’s difficult to debug.
    
2. **Security concerns:** Data in the local storage can be prone to attacks like cross-site scripting (XSS). As such, you should be cautious when working with sensitive information. It’s advisable to assess security implications and consider other alternatives where necessary.
    
3. **Not accessible to web workers:** Local storage is part of the Window object. As such, it’s tied to the main execution thread of the web page. This means it's not accessible to web workers. So if you run any background processes, you cannot use local storage within the web worker scripts.
    

## Conclusion

Local storage is a feature in modern web browsers that makes it easy for web developers to store and persist data between browser sessions.

Compared to traditional cookies, it provides larger storage capacities. Also, unlike cookies, it does not rely on server-side processes. This reduces the need for frequent server requests and helps improve performance.

In this article, you learn about how to use local storage. We covered saving, retrieving, and deleting data from local storage. You also learned about some of the benefits of using local storage in your project, and some of its limitations too.

Thanks for reading. And happy coding! For more in-depth tutorials, feel free to [subscribe to my YouTube channel](https://www.youtube.com/@DevAfterHours).
