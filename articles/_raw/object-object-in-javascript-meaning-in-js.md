---
title: '[object, object] in JavaScript – Meaning in JS'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-07-25T14:30:52.000Z'
originalURL: https://freecodecamp.org/news/object-object-in-javascript-meaning-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/clement-helardot-95YRwf6CNw8-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: object
  slug: object
seo_title: null
seo_desc: "When working with objects in JavaScript, you may have come across the [object,\
  \ object] output. While this may seem irrelevant, it's not necessarily an error.\
  \ \n[object, object] is the string representation of a JavaScript object data type.\
  \ You'll unde..."
---

When working with objects in JavaScript, you may have come across the `[object, object]` output. While this may seem irrelevant, it's not necessarily an error. 

`[object, object]` is the string representation of a JavaScript object data type. You'll understand better as we go further in this article.

There are two main contexts where you'll encounter such an output:

* When you try display an object using the `alert()` method (most common). 
* When you use the `toString()` method on an object. 

Let's take a look at some examples. 

## What Happens If You Alert an Object in JavaScript?

In this section, you'll see what happens when you use the `alert()` method to display an object in JavaScript. Here's the code example:

```javascript
const student = {
  name: "John",
  school: "freeCodeCamp",
};

alert(student)
```

In the code above, we created an object called `student`. After using the `alert()` method to display the object in the browser, we got the output below: 

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot--301-.png)

From the image above, instead of having the object and its properties displayed, `[object, object]` was displayed. 

This happens because when you use the `alert()` method to display an object in JavaScript, you get the string format displayed. 

To fix this, you can use the `JSON.stringify()` method to change the object into a string that can be popped up in the browser using the `alert()` method. Here's an example:

```javascript
const student = {
  name: "John",
  school: "freeCodeCamp",
};

alert(JSON.stringify(student));
```

When you run the code above, you should have the object and its properties displayed – similar to the image below. 

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot--303-.png)

## What Happens When You Use the `toString()` Method on an Object in JavaScript?

The `toString()` method in JavaScript returns the string format of an object. This section will help you understand what happened under the hood in the last section.

When you use the `toString()` method on an object in JavaScript, you get the string representation – `[object, object]` – returned. 

```javascript
const student = {
  name: "John",
  school: "freeCodeCamp",
};

console.log(student.toString());
// [object Object]
```

As you can see in the code above, we used the `toString()` method on an object called `student`: `student.toString()`. 

When we logged this to the console, we got `[object, object]`. 

This effect is exactly what happens when you pop up an object in the browser using the `alert()` method (as we saw in the last section).

## Summary

In this article, we talked about the odd looking `[object, object]` output in JavaScript. 

We got to understand that the output is the string representation of an object data type in JavaScript. 

You're most likely going to see such an output when you try to display an object in the browser using the `alert()` method, or when you use the `toString()` method on an object. 

We also went through some code examples and images to demonstrate how you can see `[object, object]` in JavaScript.

Happy coding!

