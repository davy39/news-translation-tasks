---
title: How Does Short-Circuiting Work in JavaScript?
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-12T18:38:38.000Z'
originalURL: https://freecodecamp.org/news/short-circuiting-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Copy-of-Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-3-.png
tags:
- name: JavaScript
  slug: javascript
- name: Operators
  slug: operators
seo_title: null
seo_desc: "In JavaScript, understanding truthy and falsy values is fundamental to\
  \ writing efficient and concise code. Combined with the concept of short-circuiting,\
  \ developers can write elegant solutions to common programming challenges. \nIn\
  \ this hands-on guide..."
---

In JavaScript, understanding truthy and falsy values is fundamental to writing efficient and concise code. Combined with the concept of short-circuiting, developers can write elegant solutions to common programming challenges. 

In this hands-on guide, we'll explore truthy and falsy values, and understand the mechanics of short-circuiting in JavaScript.

You can get all the source code from [here](https://github.com/dotslashbit/fcc-article-resources/blob/main/javascript-short-circuiting/index.js).

## Table of Contents

* [Understanding Truthy and Falsy Values](#heading-understanding-truthy-and-falsy-values)
* [What is Short-Circuiting in JavaScript?](#heading-what-is-short-circuiting-in-javascript)
* [Practical Use Cases](#heading-practical-use-cases)
* [Conclusion](#heading-conclusion)

## Understanding Truthy and Falsy Values

In JavaScript, every value has an inherent Boolean interpretation when evaluated in a Boolean context. Values that evaluate to `true` are considered truthy, while that evaluate to `false` are falsy. 

Let's explore some examples:

```javascript
// Truthy Values
if ('Hello') {
    console.log('Truthy!'); // Output: Truthy!
}

if (42) {
    console.log('Truthy!'); // Output: Truthy!
}

if (['apple', 'banana']) {
    console.log('Truthy!'); // Output: Truthy!
}

// Falsy Values
if ('') {
    console.log('Falsy!'); // This code block is not executed
}

if (0) {
    console.log('Falsy!'); // This code block is not executed
}

if (null) {
    console.log('Falsy!'); // This code block is not executed
}

```

Here's a breakdown of the code above:

### Truthy Values

* `'Hello'`: Any non-empty string in JavaScript is considered truthy. In this case, the string `'Hello'` is non-empty, so the condition evaluates to true.
* `42`: Any non-zero number (positive or negative) is considered truthy. Since `42` is a non-zero number, the condition evaluates to true.
* `['apple', 'banana']`: Arrays in JavaScript are considered truthy, regardless of their contents. Since the array `['apple', 'banana']` is non-empty, the condition evaluates to true.

### Falsy Values

`''` (empty string): An empty string in JavaScript is considered falsy. Therefore, the condition evaluates to false, and the code block inside the if statement will not be executed.

`0`: The number zero is considered falsy in JavaScript. Therefore, the condition evaluates to false, and the code block inside the if statement will not be executed.

`null`: The null value is considered falsy in JavaScript. Therefore, the condition evaluates to false, and the code block inside the if statement will not be executed.

In JavaScript, values other than `false`, `0`, `''` (empty string), `null`, `undefined`, and `NaN` are considered truthy. Understanding these truthy and falsy values is crucial when writing conditional statements and logical operations in JavaScript.

Understanding truthy and falsy values is crucial as they play a significant role in conditional statements and logical operations.

## What is Short-Circuiting in JavaScript?

Short-circuiting is a behavior exhibited by logical operators (`&&`, `||`) where the evaluation of the second operand is skipped if the outcome can be determined by evaluating the first operand alone. 

Let's examine how short-circuiting works with practical examples:

### The `&&` Operator

The `&&` operator returns the first falsy operand, or the last truthy operand if all operands are truthy.

```javascript
const value = 0;
const result = value && 'Truthy Value';
console.log(result); // Output: 0

```

In this example, `value` evaluates to `0`, which is a falsy value. Since the first operand is falsy, the expression short-circuits, and the result is `0`.

```javascript
const value = 'Hello';
const result = value && 'Truthy Value';
console.log(result); // Output: Truthy Value

```

Here, `value` evaluates to a non-empty string, which is truthy. Therefore, the second operand `'Truthy Value'` is returned, as it's the last truthy operand.

### The `||` Operator

The `||` operator returns the first truthy operand, or the last falsy operand if all operands are falsy.

```javascript
const name = '';
const displayName = name || 'Guest';
console.log(displayName); // Output: Guest

```

In this example, `name` evaluates to an empty string, which is falsy. Therefore, the expression short-circuits, and `'Guest'` is assigned to `displayName`.

```javascript
const name = 'Alice';
const displayName = name || 'Guest';
console.log(displayName); // Output: Alice

```

Here, `name` evaluates to a non-empty string, which is truthy. Therefore, the first operand `'Alice'` is returned, as it's the first truthy operand encountered.

## Practical Use Cases

### Providing Default Values

Short-circuiting is commonly used to provide default values for variables.

```javascript
const options = {};
const limit = options.limit || 10;
console.log(limit); // Output: 10 (default value)

```

In this example, `options` is an empty object. The code intends to assign a value to `limit` based on the `options.limit` property. However, since `options.limit` is not defined (it's undefined), the logical OR (`||`) operator is used.

The logical OR operator returns the value of the first operand if it's truthy. If the first operand is falsy (in this case, `options.limit` is undefined), it returns the value of the second operand (`10` in this case), which acts as a default value.

Therefore, `limit` will be assigned the value `10` because `options.limit` is falsy (undefined).

### Safely Accessing Nested Properties

Short-circuiting can also be used to safely access nested properties of objects.

```javascript
const user = { address: { city: 'New York' } };
const city = user.address && user.address.city;
console.log(city); // Output: New York

```

In this example, `user` is an object containing another object `address`, which contains the `city` property.

The expression `user.address && user.address.city` is utilizing short-circuiting. It checks if `user.address` exists and if it does, it further checks if `user.address.city` exists.

If `user.address` is truthy (if it exists), JavaScript proceeds to evaluate `user.address.city`. If `user.address` is falsy (if it's undefined or null), JavaScript short-circuits the evaluation and doesn't proceed to evaluate `user.address.city`. 

This prevents a potential `TypeError` if `user.address` is not defined or null.

Since `user.address` exists in this case, the expression evaluates to the value of `user.address.city`, which is `'New York'`.

This technique ensures safe access to nested properties and helps avoid runtime errors in cases where objects might not be fully populated or structured as expected.

## Conclusion

Short-circuiting can greatly enhance your development workflow. 

You can practice these concepts in your projects to become proficient in leveraging JavaScript's short-circuiting behavior effectively.

If you have any feedback, feel free to reach out to me on [Twitter](https://twitter.com/introvertedbot) and [Linkedin](https://www.linkedin.com/in/sahil-mahapatra/)

