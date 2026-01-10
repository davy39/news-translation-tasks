---
title: How Web Storage Works – Local vs Session Storage Explained
subtitle: ''
author: Tooba Jamal
co_authors: []
series: null
date: '2022-10-12T14:08:46.000Z'
originalURL: https://freecodecamp.org/news/how-web-storage-works
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/webstorage-1-1.png
tags:
- name: data
  slug: data
- name: localstorage
  slug: localstorage
- name: storage
  slug: storage
seo_title: null
seo_desc: 'Anyone who works with the web needs to store data for a later use. Backend
  developers have some powerful databases in their toolkit. But if you are a frontend
  developer, you can still store and process data using web storage.

  In this article, you''ll ...'
---

Anyone who works with the web needs to store data for a later use. Backend developers have some powerful databases in their toolkit. But if you are a frontend developer, you can still store and process data using web storage.

In this article, you'll learn what is a web storage, the different types of web storage, and when to use each one of them.

## What is Web Storage?

Web storage is an HTML5 feature that allows you to store data in key value pairs in the browser. This enables applications to store data in the client side so you can access it or manipulate it later. All data stored in web storage stays in the browser and is not transferred anywhere else.

## Types of web storage

The two main types of web storage are‌‌ local storage‌‌ and session storage‌‌. Each one has its own unique characteristics. 

But one thing they have in common is that they store the data in the particular browser the user uses to access the webpage. You won't be able to access the same data through another browser. 

Now let's discuss both of them in detail.

### Local Storage

Local storage can store 5MB of data per app for the lifetime of the app. Closing the browser will not affect the data in any way – it stays there unless you delete it. 

You can only access the local storage object through `localStorage`. The methods you can use to perform operations on the localStorage object are:

```javascript
localStorage // to access the localStorage object 
localStorage.setItem('name', 'John') // sets name equal to john localStorage.getItem('name') // "John" 
localStorage.removeItem('name') // removes name from the localStorage localStorage.clear() // clears the localStorage
```

`localStorage.setItem()` takes a key and value as parameters and sets a new item in the local storage object equal to the given key value pair. 

`localStorage.getItem()` takes a key as a parameter and returns the value stored to that key in the storage. 

`localStorage.clear()` clears the whole localStorage object.

`localStorage.removeItem()` takes in a key as a parameter and removes the corresponding key-value pair. ‌‌

Any item that you store in localStorage will be stored as a string. This means that you need to convert other data types such as arrays or objects to strings – otherwise you lose their structure. 

See the example below:       

```javascript
const scores = [10, 8, 6, 3, 9] 
const scoresJSON = JSON.stringify(scores) 
localStorage.setItem('scores', scoresJSON) 
localStorage // output >> {scores: '[10, 8, 6, 3, 9]', length: 1}
```

In the example above, we first created an array score, then converted it into a string using JSON.stringify(), and finally saved the stringified scores array in localStorage. 

Take your time to have a look at the output I get when I run the same code snippet in my browser console.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/localstorage-3.png)
_Example code in browser console_

Note that the key scores has a value equal to our stringified scores array. But if we don't convert the scores array into a string, our array will loose it's structure and the items will be saved as a string like below:

```javascript
const scores = [10, 8, 6, 3, 9] 
localStorage.setItem('scores', scores) 
localStorage // output >> {scores: '10, 8, 6, 3, 9', length: 1}

```

Let's also run the code in the browser console to see what is logs to the console:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/localstorage-2.png)
_Saving an array without converting it into a string_

See how our scores array is converted into a string when we do not convert it into a string using JSON.stringify()?

### Session Storage

Session storage allows you to store data in the browser depending on the system memory and the data stored in the browser until the browser is closed. In other words, closing the browser will clear all the data stored in session storage. 

Like localStorage, you can access session storage by typing sessionStorage in the browser console.

```javascript
sessionStorage // access the session storage 
sessionStorage.setItem('name', 'John') // add name to session storage with value john 
sessionStorage.getItem('name') // get the name item from session storage sessionStorage.removeItem('name') // remove name item from the session storage sessionStorage.clear() // clear the session storage
```

`sessionStorage.setItem()` takes a key and value as parameters and sets a new item in the local storage object equal to the given key value pair.

`sessionStorage.getItem()` takes key as a parameter and returns the value stored to that key in the storage. 

`sessionStorage.removeItem()` takes in a key as parameter and removes the corresponding key-value pair. 

`sessionStorage.clear()` clears the whole localStorage object. ‌‌

Like localStorage, any item stored in sessionStorage will be stored as a string. This means we need to convert them into strings before storing in the sessionStorage.

## Web Storage Example Use Cases

You can use **local storage** when you want your data to be made available when the user revisits the web page, such as for a shopping cart or game/quiz score. Just keep in mind that the information saved in local storage should not be sensitive.‌‌

You can use **session storage** when the data that needs to be saved is sensitive. User authentication is an example of data that you would like to clear as soon as the user closes the tab.

## Conclusion

In this article, you have learned the modern ways of storing temporary data in the browser. I hope this has helped you understand how and when to use both types of web storage in your projects. 

Interested in connecting on LinkedIn? Hit me up at [Tooba Jamal](https://www.linkedin.com/in/tooba-jamal/).

