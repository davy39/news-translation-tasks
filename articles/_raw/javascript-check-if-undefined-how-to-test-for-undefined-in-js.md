---
title: JavaScript Check if Undefined – How to Test for Undefined in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-07-11T17:13:42.000Z'
originalURL: https://freecodecamp.org/news/javascript-check-if-undefined-how-to-test-for-undefined-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/cover-template--9-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'An undefined variable or anything without a value will always return "undefined"
  in JavaScript. This is not the same as null, despite the fact that both imply an
  empty state.

  You''ll typically assign a value to a variable after you declare it, but thi...'
---

An undefined variable or anything without a value will always return "undefined" in JavaScript. This is not the same as null, despite the fact that both imply an empty state.

You'll typically assign a value to a variable after you declare it, but this is not always the case.

When a variable is declared or initialized but no value is assigned to it, JavaScript automatically displays "undefined". It looks like this:

```bash
let myStr;

console.log(myStr); // undefined
```

Also, when you try accessing values in, for example, an array or object that doesn’t exist, it will throw `undefined`.

```bash
let user = {
    name: "John Doe",
    age: 14
};

console.log(user.hobby); // undefined
```

Here's another example:

```bash
let myArr = [12, 33, 44];

console.log(myArr[7]); // undefined
```

In this article, you will learn the various methods and approaches you can use to know if a variable is `undefined` in JavaScript. This is necessary if you want to avoid your code throwing errors when performing an operation with an undefined variable.

In case you are in a rush, here are the three standard methods that can help you check if a variable is `undefined` in JavaScript:

```bash
if(myStr === undefined){}
if(typeof myArr[7] === "undefined"){}
if(user.hobby === void 0){}
```

Let’s now explain each of these methods in more detail.

## How to Check if a Variable is Undefined in JavaScript with Direct Comparison

One of the first methods that comes to mind is direct comparison. This is where you compare the output to see if it returns `undefined`. You can easily do this in the following way:

```bash
let user = {
    name: "John Doe",
    age: 14
};

if (user.hobby === undefined) {
    console.log("This is undefined");
}
```

This also works for arrays as you can see below:

```bash
let scores = [12, 34, 66, 78];

if (scores[10] === undefined) {
    console.log("This is undefined");
}
```

And it definitely also works for other variables:

```bash
let name;

if (name === undefined) {
    console.log("This is undefined");
}
```

## How to Check if a Variable is Undefined in JavaScript with `typeof`

We can also use the type of the variable to check if it’s `undefined`. Luckily for us undefined is a datatype for an undefined value as you can see below: ‌

```bash
let name;

console.log(typeof name); // "undefined"
```

With this we can now use the datatype to check undefined for all types of data as we saw above. Here is what the check will look like for all three scenarios we have considered:

```bash
if(typeof user.hobby === "undefined"){}
if(typeof scores[10] === "undefined"){}
if(typeof name === "undefined"){}
```

## How to Check if a Variable is Undefined in JavaScript with the `Void` Operator

The `void` operator is often used to obtain the `undefined` primitive value. You can do this using "`void(0)`" which is similar to "`void 0`" as you can see below:

```bash
console.log(void 0); // undefined
console.log(void(0)); // undefined
```

In the actual sense, this works like direct comparison (which we saw before). But we would replace undefined with `void(0)` or `void 0` as seen below:

```bash
if(typeof user.hobby === void 0){}
if(typeof scores[10] === void 0){}
if(typeof name === void 0){}
```

Or like this:

```js
if(typeof user.hobby === void(0)){}
if(typeof scores[10] === void(0)){}
if(typeof name === void(0)){}
```

## Conclusion

In this article, we learned how to check if a variable is undefined and what causes a variable to be undefined.

We also learned three methods we can use to check if a variable is undefined. All methods work perfectly. Choosing your preferred method is totally up to you.

Have fun coding!
