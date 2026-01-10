---
title: What are Falsy Values in JavaScript? Explained with Examples
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2024-01-30T15:27:25.000Z'
originalURL: https://freecodecamp.org/news/what-are-falsey-values-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-29-at-12.22.42-AM.png
tags:
- name: Conditionals
  slug: conditionals
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'In JavaScript, every value has a boolean equivalent. This means it can
  either be evaluated as true (truthy value) or false (falsy value) when used in a
  boolean context.

  But what is a boolean context? It''s a situation where a boolean value is expected...'
---

In JavaScript, every value has a boolean equivalent. This means it can either be evaluated as true (truthy value) or false (falsy value) when used in a boolean context.

But what is a boolean context? It's a situation where a boolean value is expected. Examples include if statements, logical operators, and so on. When you use a non-boolean value in a boolean context, JavaScript will convert the value to its boolean equivalent.

In this article, you will learn about falsy values in JavaScript and how to check if a value is falsy. The article also covers some best practices to consider when checking the boolean equivalent of a value.

Let's get started!

## Table of Contents

* [The Six Falsy Values in JavaScript](#the-six-falsy-values-in-javascript)
    
* [How to Check if a Value is Falsy](#how-to-check-if-a-value-is-falsy-in-javascript)
    
* [Truthy Values That May Appear as Falsy Values](#truthy-values-that-may-appear-as-falsy-values)
    
* [Best Practices When Checking Boolean Equivalent](#best-practices-when-checking-boolean-equivalent)
    
* [Conclusion](#conclusion)
    

## The Six Falsy Values in JavaScript

Falsy values in JavaScript are unique because there are only six of them. Apart from these six, all other values are truthy values.

You can commit these falsy values to memory. That way, when you come across any value that isn't one of the six, you know it's a `truthy` value.

Here are the six falsy values in JavaScript:

* `false`: The boolean value `false`.
    
* `0`: The number zero.
    
* `""` or `''` or \`\`\`\`: An empty string.
    
* `null`: The null keyword, representing the absence of any object value.
    
* `undefined`: The undefined keyword, representing an uninitialized value.
    
* `NaN`: Stands for "Not a Number". It represents a special value returned from an operation that should return a numeric value but doesn't.
    

Now, let's see some practical examples of these falsys valsues in JavaScript.

### Example 1 – The boolean value `false`.

```javascript
let isOnline = false

function checkStatus(status) {
  return Boolean(status) ? "ONLINE" : "OFFLINE"
}

checkStatus(isOnline) // "OFFLINE"
```

When you pass the `isOnline` variable to the `checkStatus` function, it returns the string `"OFFLINE"`. And this is because the value is `false` in this context. Here, we are using a tenary operator based on the boolean value of the `status` argument.

### Example 2 – The number zero.

```javascript
let unreadMessages = 0
let hasUnreadMessages = Boolean(unreadMessages)
console.log(hasUnreadMessages) // false
```

This examples checks whether a user has unread messages or not. We use the in built `Boolean` function to get the boolean value of the `unreadMessages` variable. This means anytime the number of `unreadMessages` is zero, `hasUnreadMessages` will be `false`.

### Example 3 – An empty string.

```javascript
let userInput = "";
let defaultText = "No input provided";

let displayText = Boolean(userInput) || defaultText;

console.log(displayText); // No input provided
```

This example uses the logical OR operator `||` to determine the value of the `displayText`. It will assign the value of `userInput` to `displayText` if it's a truthy value. Or it will assign the `defaultText` to `displayText` if `userInput` is a falsy value as it is in this case.

### Example 4 – `null`

```javascript
let user = null;

if (user && user.name) {
    console.log("Welcome, " + user.name + "!");
} else {
    console.log("Please log in to access the website.");
}
```

The following example assumes the `user` isn't logged in and so the value of `user` object is `null`. This means the `if` statement will evaluate to `false`. The expected behaviour then will be that the code executes the `else` block.

### Example 5 – `undefined`

```javascript
let age;
if (age === undefined) {
    console.log("The age is undefined.");
}
```

When a variable is declared but not initialized with a value, JavaScript assigns it the value `undefined` by default. In the code example above, since the `age` variable is declared but not assigned a value, its value is `undefined`. This means the code in the `if` statement will run.

### Example 6 – `NaN`

```javascript
let value1 = "Ten"
let value2 = 10

let result = value1 / value2

if (isNaN(result)) {
    console.log("The result is not a number.");
} else {
    console.log(result);
}
```

This example divides `value1` (a string) by `value2` (a number). This will result in a `NaN` value because you cannot divide a string by a number. This means the code in the `if` block will run. And log `The result is not a number` to the console.

## How to Check if a Value is Falsy in JavaScript

A safe way to check whether a value is falsy or not is to use the `Boolean` function. The `Boolean` function returns the boolean value of the value of the argument passed to it.

Example:

```javascript
console.log(Boolean(false))
console.log(Boolean(0))
console.log(Boolean(""))
console.log(Boolean(null))
console.log(Boolean(undefined))
console.log(Boolean(NaN))
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-23-at-6.16.42-PM.png align="left")

*Boolean log results for all six falsy values.*

Here, we are checking the boolean value of all six falsy values. And as expected, each returns `false`.

When you pass any other value that's not one of these six falsy values to the Boolean function, it will return `true`.

Example:

```javascript
console.log(Boolean('hello'))
console.log(Boolean(24))
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-23-at-6.24.35-PM.png align="left")

*Example boolean log results for truthy values.*

## Truthy Values that May Appear as Falsy Values

There are some truthy values that, at a glance, may appear to be falsy values but aren't. As already mentioned, only six values in JavaScript are falsy values. Anything else is a truthy value.

The following are some of those values that aren't falsy but may appear as such.

```javascript
console.log(Boolean('false')) // An empty object
console.log(Boolean(' ')) // An empty object
console.log(Boolean('0')) // An empty object
console.log(Boolean([])) // An empty array
console.log(Boolean({})) // An empty object
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-24-at-8.09.17-AM.png align="left")

*Log results for truthy values that appear as falsy.*

The first three strings contains text that may look like falsy values. First is the string with the text `"false"`, another one with some whitespace, and the third with zero.

Remember that the only string considered a falsy value is an empty string. All non-empty strings in JavaScript are truthy values including strings with only whitespace.

Also, note that unlike strings, both an empty array and an empty object return `true` in a boolean context.

## Best Practices When Checking Boolean Equivalent

The following tips will help make your code more readable and easier to maintain.

### 1\. Use the Boolean function

It's always better to use the built-in `Boolean` function when you want to check whether a value is truthy or falsy. The function works by coercing any value into its corresponding boolean. It also makes your intention clear to anyone reading the code.

Example:

```javascript
// Example without the Boolean function
const value = ''; 

if (value) {
    console.log('It is a TRUTHY value');
} else {
    console.log('It is a FALSY value');
}

// Example with the Boolean function
const value = ''

if (Boolean(value)) {
    console.log('It is a TRUTHY value');
} else {
    console.log('It is a FALSY value');
}
```

Both examples do the same thing. But in the second example, it's explicit that you're checking the boolean representation of the given value.

### 2\. Use strict equality `===` instead of loose equality `==`

When you're comparing values for truthiness or falsiness, it's recommended to use strict equality (`===`) over loose equality (`==`). Strict equality compares both the value and the type. Loose equality performs type coercion before comparing the values, and this can lead to unexpected results.

Example:

```javascript
// Strict Equality Example

if (1 === [1]) {
  console.log('EQUAL')
} else {
  console.log('NOT EQUAL')
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-28-at-11.31.28-PM.png align="left")

*Log result for strict equality example.*

```javascript
// Loose Equality Example
if (1 == [1]) {
  console.log('EQUAL')
} else {
  console.log('NOT EQUAL')
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-28-at-11.32.20-PM.png align="left")

*Log result for loose equality example.*

Both examples above compare the same values. But the strict equality example logs "NOT EQUAL". This is because the number 1 is not equal to an array containing the number 1. With the loose equality, it coerces the type of the values to make them of the same type. That is why it logs "EQUAL" to the console.

### 3\. Add comments to document your code

To make your code more readable and easier to maintain, consider adding comments when necessary to explain your logic when dealing with truthy and falsy values.

Documenting your code is a good practice to help developers on your team (or your future self) understand the intended behaviour of a piece of code.

Example:

```javascript
let selectedUser = USER_OBJ

// Check if no user is selected
if (!selectedUser) {
    console.log("Please select a user.");
} else {
    console.log("User address: " + selectedUser.address);
}
```

In the example above, the comment added before the `if` statement makes it clear that the code is checking if no user has been selected.

Using the logical NOT operator (`!`) can make it seem like you're checking if a user is selected rather than checking if no user is selected. So a comment in an instance like helps provide clarity.

## Conclusion

In this article, you have learned about the six falsy values in JavaScript and how they differ from truthy values. You also learned about some truthy values that may appear as falsy, but actually aren't. And you also saw some best practices to consider when working with falsy values.

A good understanding of the concept of falsy and truthy values and how they affect comparisons and conditional statement will come in handy when debugging JavaScript applications.

Thanks for reading. And happy coding! For more in-depth tutorials, feel free to [subscribe to my YouTube channel](https://www.youtube.com/@DevAfterHours).
