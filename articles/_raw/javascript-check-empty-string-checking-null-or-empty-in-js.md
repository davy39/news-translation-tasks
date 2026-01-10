---
title: JavaScript Check Empty String – Checking Null or Empty in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-07-05T22:43:13.000Z'
originalURL: https://freecodecamp.org/news/javascript-check-empty-string-checking-null-or-empty-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/cover-template--7-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'There are a number of reasons why you might need to check if a string is
  empty or not. One of the most important reasons is when you''re retrieving data
  from a database, API, or input field.

  In this article, you will learn how to check if a sting is e...'
---

There are a number of reasons why you might need to check if a string is empty or not. One of the most important reasons is when you're retrieving data from a database, API, or input field.

In this article, you will learn how to check if a sting is empty or null in JavaScript. We will see many examples and methods you can use so that you can understand them and decide which one to use and when.

## What's the Difference Between Null and Empty?

Before we begin, you need to understand what the terms Null and Empty mean, and understand that they are not synonymous.

For example, if we declare a variable and assign it an empty string, and then declare another variable and assign it the Null value, we can tell them apart by looking at their datatype:

```js
let myStr1 = "";
let myStr2 = null;

console.log(typeof myStr1); // "string"
console.log(typeof myStr2); // "object"
```

Looking at the code above, we can see that the compiler/computer interprets each value differently. So when it comes time to check, we must pass conditions for both types of values because we as humans frequently refer to `null` as empty.

## How to Check for Empty or Null in JavaScript

We now know that an empty string is one that contains no characters. It is very simple to check if a string is empty. We can use two major methods that are somewhat similar because we will use the strict equality operator (`==`).

### How to Check for an Empty String in JavaScript with the `length` Property

In this first method, we will check for the length of the string by adding the length property. We'll check if the length is equal to `0`. If it’s equal to zero, it means that the string is empty, as we can see below:

```bash
let myStr = "";

if (myStr.length === 0) {
  console.log("This is an empty string!");
}
```

The above will return this:

```bash
"This is an empty string!"
```

But this approach unfortunately might not work in all situations. For example, if we have a string that has white spaces as seen below:

```bash
let myStr = "  ";

if (myStr.length === 0) {
  console.log("This is an empty string!");
}else{
  console.log("This is NOT an empty string!");
}
```

This will return:

```bash
"This is NOT an empty string!"
```

We can easily fix this error by first removing the white spaces using the `trim()` method before checking for the length of such string to see if it’s empty as seen below:

```bash
let myStr = "  ";

if (myStr.trim().length === 0) {
  console.log("This is an empty string!");
}else{
  console.log("This is NOT an empty string!");
}
```

This will now return the following:

```bash
"This is an empty string!"
```

Note: If the value is null, this will throw an error because the `length` property does not work for null.

To fix this, we can add an argument that checks if the value's type is a string and skips this check if it is not:

```bash
let myStr = null;

if (typeof myStr === "string" && myStr.trim().length === 0) {
  console.log("This is an empty string!");
}
```

### How to Check for an Empty String in JavaScript by String Comparison

Another way to check if a string is empty is by comparing the string to an empty string.

For example:

```bash
let myStr = "";

if (myStr === "") {
  console.log("This is an empty string!");
}
```

As with the previous method, if we have white spaces, this will not read the string as empty. So we must first use the `trim()` method to remove all forms of whitespace:

```bash
let myStr = "   ";

if (myStr.trim() === "") {
  console.log("This is an empty string!");
} else {
  console.log("This is NOT an empty string!");
}
```

Just as we did for the `length` method, we can also check for the type of the value so that this will only run when the value is a string:

```bash
let myStr = null;

if (typeof myStr === "string" && myStr.trim() === "") {
  console.log("This is an empty string!");
}
```

## How to Check for Null in JavaScript

So far, we've seen how to check if a string is empty using the length and comparison methods.

Now, let's see how to check if it's `null`, and then check for both. To check for `null`, we simply compare that variable to null itself as follows:

```bash
let myStr = null;

if (myStr === null) {
  console.log("This is a null string!");
}
```

This will return:

```bash
"This is a null string!"
```

## How to Check for a Null or Empty String in JavaScript

At this point we have learned how to check for an empty string and also if a variable is set is null. Let’s now check to for both this way:

```js
let myStr = null;

if (myStr === null || myStr.trim() === "") {
  console.log("This is an empty string!");
} else {
  console.log("This is not an empty string!");
}
```

This will return:

```bash
"This is an empty string!"
```

## Conclusion

In this article, we learned how to check for an empty string or null and why they are not the same thing.

Have fun coding!
