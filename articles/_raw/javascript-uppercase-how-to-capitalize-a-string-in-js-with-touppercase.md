---
title: JavaScript Uppercase – How to Capitalize a String in JS with .toUpperCase
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-02-28T19:25:42.000Z'
originalURL: https://freecodecamp.org/news/javascript-uppercase-how-to-capitalize-a-string-in-js-with-touppercase
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/toUpperCase.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'While working with strings in JavaScript, you can perform different operations
  on them.

  The operations you might perform on strings include capitalization, conversion to
  lowercase, adding symbols within words, and many more.

  In this article, I will s...'
---

While working with strings in JavaScript, you can perform different operations on them.

The operations you might perform on strings include capitalization, conversion to lowercase, adding symbols within words, and many more.

In this article, I will show you how to convert a string to uppercase letters with the `.toUpperCase()` string method.

## Basic Syntax of the `.toUpperCase()` Method

To use the `.toUpperCase()` method, assign the string you want to change to uppercase to a variable and then prepend it with `.toUpperCase()`.

## How to Capitalize a String with .toUpperCase

As already stated, you can assign a string to a variable and then use the `.toUpperCase()` method to capitalize it

```js
const name = "freeCodeCamp";
const uppercase = name.toUpperCase();
console.log(uppercase);

// Output: FREECODECAMP
```

You can also write a function and return `.toUpperCase()` in it, so a stated parameter will be capitalized when the function is called.

```js
function changeToUpperCase(founder) {
  return founder.toUpperCase();
}

// calling the function 
const result = changeToUpperCase("Quincy Larson");

// printing the result to the console
console.log(result);

// Output: QUINCY LARSON
```

**In the script above:**
- I defined a function named `changeToUpperCase` with a placeholder of `founder`
- with the return statement inside the function, I told the function that what I want it to do is to change to uppercase letters any parameter I specify when I call it
- I then assigned the function call - `changeToUpperCase` to a variable named `result`
- with the help of the variable, I was able to print the result of the function to the console

## Conclusion

You can use the `.toUpperCase()` method, fully known as `String.prototype.toUpperCase()`, when you need to capitalize strings in your JavaScript projects. 

If you find this article helpful, please share it with your friends and family.


