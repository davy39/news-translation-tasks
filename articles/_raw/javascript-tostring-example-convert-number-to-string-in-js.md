---
title: JavaScript toString Example – How to Convert a Number into a String in JS and
  More
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-19T21:09:06.000Z'
originalURL: https://freecodecamp.org/news/javascript-tostring-example-convert-number-to-string-in-js
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c982c740569d1a4ca1892.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Dillion Megida\nSometimes you want to convert one data type into another\
  \ data type without changing the values manually.\nFor instance, you might want\
  \ to convert a number to a string. JavaScript sometimes does this implicitly. \n\
  Like when you use the..."
---

By Dillion Megida

Sometimes you want to convert one data type into another data type without changing the values manually.

For instance, you might want to convert a number to a string. JavaScript sometimes does this implicitly. 

Like when you use the double equals operator (`==`), or when you attempt to do something on a value with a data type that is incompatible with the operation. This is called [Type Coercion](https://www.freecodecamp.org/news/js-type-coercion-explained-27ba3d9a2839/).

This said, you can also convert data types explicitly. And I'm going to show you how to do that in this article.

The string data type is a very common data type in JavaScript. For almost every other data type, you need to have a string representation. 

Just as you must have seen something similar to `"[object Object]"` when you use an object in place of an actual string.

In this article, we'll learn what the `toString` method is, and how to convert a number (and a few other data types) to a string using this method.


## The `toString` method

As the name implies, this method is used to change data to a string. Arrays, numbers, and booleans each have this method which converts their data in various ways. Let's look at them individually now.

### How to convert a number to a string

The `toString` method exists on every number literal. It converts numbers to their string representations. Here's how it is used:


```js
const num = 54;
console.log(num.toString())
// "54"
```

But there's more to this. The `toString` method for numbers also accepts a `base` argument. This argument allows you to convert a number to another base. 

The returned value is the string representation of the new number. Here's how it is used:

```js
const num = 54;
const num2 = num.toString(2);
console.log(num2);
// "110110"
```

`parseInt` is another JavaScript method which in contrast converts strings to their respective number representations. Here's how it works:

```js
const numInStr = "54";
const str = "Hello";
console.log(parseInt(numInStr));
// 54
console.log(parseInt(str));
// NaN
```

For a variable not similar to a number, `parseInt` returns `Nan` as seen above.


## How to convert an array to a string in JavaScript

Arrays also have the `toString` method. The returned value of this method is a concatenation of all values of the array (and deep-nested arrays in it) separated by commas. Here's how it is used:

```js
const arr = ["javascript", "toString", [1, "deep1", [3, 4, "array"]]];
console.log(arr.toString());
// "javascript,toString,1,deep1,3,4,array"
```

## How to convert an object to a string in JavaScript

The return value of `toString` on an object is - just as you may have often come across - `"[object Object]"`. For example:

```js
const obj = {name: 'Object'};
const obj2 = {type: 'data', number: 100};
console.log(obj.toString());
// [object Object]
console.log(obj2.toString());
// [object Object]
```

The default conversion of objects to string is `[object Object]`. Notice that there are two `object`s there, and not just one? And the other is capitalized? 

There are more representations for objects like what follows:

```js
function print() {};
const arr = [];
const obj = {};
console.log(
  Object.prototype.toString.call(print),
  Object.prototype.toString.call(arr),
  Object.prototype.toString.call(obj)
)
// [object Function] [object Array] [object Object]
```

Functions, Arrays, Objects, and even Dates and Regex are all objects. And each of them has the `toString` method. 

When `toString` is called on them, it grabs whatever class of Object the value is, and then prints it it like you see above ("Function, Array, Object).

We use `call(variable)` because the `toString` gets the object class through the `this` property.


## Conclusion

The `.toString` method returns a string conversion of the data it is used on. This is very useful for certain cases, especially `number`s. 

In this article, we learned how the JavaScript `toString` method works with `number`s, `array`s and `object`s and we also looked a little at `parseInt`.


