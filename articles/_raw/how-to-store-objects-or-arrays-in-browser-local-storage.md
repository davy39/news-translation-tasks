---
title: How to store objects or arrays in browser local storage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-30T07:55:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-store-objects-or-arrays-in-browser-local-storage
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/30-objects-arrays-localstorage.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Dillion Megida

  The local storage of browsers only accepts strings, but sometimes you want to store
  objects or arrays. How do you go about that? We''ll see how in this article.

  The browser local storage, is a Web Storage API that allows us to store ...'
---

By Dillion Megida

The local storage of browsers only accepts strings, but sometimes you want to store objects or arrays. How do you go about that? We'll see how in this article.

The browser local storage, is a Web Storage API that allows us to store data for a domain across browser sessions. Such data will be available and accessible by that domain forever, until it is deleted. It looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-81.png)

You can access this view by inspecting any webpage, going to the Application section, then the Storage section, and selecting Local Storage. You would see all the data that has been saved in local storage for the domain of the webpage.

Local storage is useful for data that you want to quickly access, without having to make an API request to a backend server. A common use case is personalization settings for a user like color scheme or other settings that you do not want to always reach out to the server for.

However, you can only store strings in this storage:

```js
localStorage.setItem("key", "value")
```

Any attempt to store an object or an array would result in the value being stringified. An object like `{name: "Dillion"}` would be stringified to `"[object Object]"` and an array like `[1,2]` will be stringified to `"1,2"`.

In the case of the array, you can retain the values, but for the object, those values are gone. So how do you correctly store an object and array?

I have a [video on this topic](https://youtu.be/E2rvDpubmnA) which you can also check out.

## Stringifying Objects and Arrays

Since we know that local storage works with string values, we can stringify the objects and arrays ourselves, in such a way that the contents of the value are not lost. We do this using `JSON.stringify()` method.

The `stringify` method of the `JSON` object converts a value to a JSON string, which we can store instead. Let's see an example:

```js
const obj = {
  name: "Dillion",
  color_scheme: "dark"
}

const stringifiedObj = JSON.stringify(obj)

localStorage.setItem(
  "userInfo",
  stringifiedObj
)
```

As you can see here, we convert `obj` to a JSON string, then store it in local storage. Here's what it looks like:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-86.png)

When you click on the item in storage, your browser might also show you the value like an actual object below the table (as you can see above).

We can do the same for arrays:

```js
const interests = [
  "football",
  "fashion",
  "cooking"
]

const stringifiedInterests =
  JSON.stringify(interests)
  
localStorage.setItem(
  "interests",
  stringifiedInterests
)
```

And the local storage view:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-85.png)

Again, you see that even though we actually stored a string, the browser recognizes that it's a stringified array, so by clicking on the item, you see the actual array.

Since they have the values as strings, how do we convert them back to objects and arrays when we want to use them?

## Parsing Stringified Objects and Arrays

The `JSON` object also has a `parse` method which is to parse a JSON string into the original value. We can use this method to get the original object:

```js
const userInfo =
  localStorage.getItem('userInfo')
  
const userInfoParsed = JSON.parse(userInfo)

console.log(userInfoParsed.name)
// Dillion

console.log(userInfoParsed.color_scheme)
// dark
```

And we can use it to get the original array:

```js
const interests =
  localStorage.getItem('interests')
  
const interestsParsed = JSON.parse(interests)

console.log(interestsParsed[1])
// fashion

console.log(interestsParsed[2])
// cooking
```

## Wrap up

Storing objects in local storage allows you to store a group of properties together instead of having multiple items in the storage. For example, instead of storing `userName` and  `userColorScheme` separately in the storage, you can store one object with `name` and `color_scheme` properties.

But considering that local storage only allows string values, you have to convert your object or array into a string first.

In this article, we've seen how to do that, as well as get the original values when retrieving from the local storage.

If you enjoyed this article, please share it with others :)


