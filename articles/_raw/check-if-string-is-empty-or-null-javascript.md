---
title: How to Check if a String is Empty or Null in JavaScript – JS Tutorial
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-05-03T17:26:58.000Z'
originalURL: https://freecodecamp.org/news/check-if-string-is-empty-or-null-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/cover-template--13-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In JavaScript, it''s important to check whether a string is empty or null
  before performing any operation. Trying to operate on an empty or null string can
  lead to errors, bugs, and unexpected results.

  In this tutorial, we''ll explore the different way...'
---

In JavaScript, it's important to check whether a string is empty or null before performing any operation. Trying to operate on an empty or null string can lead to errors, bugs, and unexpected results.

In this tutorial, we'll explore the different ways of checking whether a string is empty or null in JavaScript and some best practices to follow when doing so.

## What are Empty and Null Strings?

An empty string is a string that has no characters, while a null string is a string that has no value assigned to it. It's important to differentiate between the two, as they are not the same.

For example, you have a form where a user can input their name. If the user doesn't input anything, the input field's value will be an empty string. However, the value will be null if the input field is not even created.

## How to Check for Empty or Null Strings

JavaScript has several ways to check whether a string is empty or null. Let's explore some of them.

### Using the if Statement and typeof Operator

One way to check for an empty or null string is to use the `if` statement and the `typeof` operator. Here's an example:

```js
let str = "";

if (typeof str === "string" && str.length === 0) {
  console.log("The string is empty");
} else if (str === null) {
  console.log("The string is null");
} else {
  console.log("The string is not empty or null");
}
```

In this example, we're checking whether the `str` variable is a string and whether its length is zero. If it is, then we know that it's an empty string. If the `str` variable is `null`, then we know that it's a null string. Otherwise, we know that the string is not empty or null.

### Using the length Property

Another way to check for an empty string is to use the `length` property. Here's an example:

```js
let str = "";

if (str.length === 0) {
  console.log("The string is empty");
} else {
  console.log("The string is not empty");
}
```

In this example, we're checking whether the `str` variable's length is zero. If it is, then we know that it's an empty string. Otherwise, we know that the string is not empty.

### Using the trim Method

Sometimes, a string might contain whitespace characters that make it appear non-empty even when it is. In such cases, we can use the `trim` method to remove any leading or trailing whitespace characters before checking for emptiness. Here's an example:

```js
let str = "   ";

if (str.trim().length === 0) {
  console.log("The string is empty");
} else {
  console.log("The string is not empty");
}
```

In this example, we're first using the `trim` method to remove any leading or trailing whitespace characters from the `str` variable, then checking whether the resulting string has zero length. If it does, then we know that the string is empty. Otherwise, we know that the string is not empty.

## Best Practices for Checking Empty or Null Strings

Here are some best practices to follow when checking for empty or null strings in JavaScript:

* Always use triple equals (`===`) when comparing a string to `null`. This ensures that the types are checked, and you don't accidentally compare a string to the number `0` or `false`.
    
* Use strict equality (`===`) when checking for an empty string. This ensures you don't compare an empty string to a string containing only whitespace characters.
    
* Use the `trim` method to remove leading and trailing whitespace characters before checking for an empty string. This ensures that strings with only whitespace characters are also considered empty.
    
* Use regular expressions for more complex checks, such as checking for a string that only contains digits or checking for a string that matches a certain pattern.
    

For example:

```js
let str = "12345";
let digitRegExp = /^\d+$/;

if (digitRegExp.test(str)) {
  console.log("The string contains only digits");
} else {
  console.log("The string does not contain only digits");
}
```

## Conclusion

In this article, we've learned how to check whether a string is empty or null in JavaScript. We've explored different methods for doing so, such as using the `if` statement and `typeof` operator, the `length` property, and the `trim` method.

If you would like to learn more about JavaScript and web development, [browse 200+ expert articles on web development](https://joelolawanle.com/contents) written by me, and also check out [my blog](https://joelolawanle.com/posts) for more captivating content.

Have fun coding!
