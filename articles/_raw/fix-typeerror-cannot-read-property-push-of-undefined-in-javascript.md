---
title: 'How to Fix TypeError: Cannot read Property ''push'' of Undefined in JavaScript'
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-10-11T23:18:26.000Z'
originalURL: https://freecodecamp.org/news/fix-typeerror-cannot-read-property-push-of-undefined-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/cover-template--13-.png
tags:
- name: error
  slug: error
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When working with JavaScript arrays, you have to be careful that you are
  not calling the push(), pop(), shift(), unShift(), or splice() methods on a variable
  that is meant to be an array but has a value of undefined.

  If you mistakenly do this, you''ll...'
---

When working with JavaScript arrays, you have to be careful that you are not calling the `push()`, `pop()`, `shift()`, `unShift()`, or `splice()` methods on a variable that is meant to be an array but has a value of `undefined`.

If you mistakenly do this, you'll get this error:

![](https://paper-attachments.dropbox.com/s_E70A1833F8285C7F5412DCD9531F13EA1E92CB215392E2D976AD0B6D0DFB9AA0_1665231049694_image.png align="left")

If you call `pop()` or any of these other methods instead of push (as in the example above), the error above will carry 'pop' (or the other method you're using) instead. This means the approach you'll learn in the article will work for all methods.

For you to properly understand this article and this error, it is essential to highlight the various reasons that can trigger this issue:

* You call the method on a variable previously set to `undefined`.
    
* You call the method on a variable before it has been initialized with an array.
    
* You call the method on an array element rather than the array itself.
    
* You call the method on an object property that does not exist or has an `undefined` value.
    

Remember that this method can be `push()`, `pop()`, `shift()`, `unShift()` or `splice()`. Let's now analyze each scenario and learn how to fix the error.

## Calling the method on a variable that was previously set to `undefined`

When working with variables and data types like strings, we tend to assign the variable's values like `undefined` and `null` before passing in the original value. Sometimes we do this when calling functions or handling certain actions.

For arrays, it doesn't work that way – else, you will get the error:

```js
let myArray = undefined;

myArray.push("John Doe"); // Uncaught TypeError: Cannot read properties of undefined (reading 'push')

console.log(myArray);
```

To fix this, You must declare that the variable is an array before array methods like the `push()`, `pop()`, and others can work on it:

```js
let myArray = [];

myArray.push("John Doe");

console.log(myArray); // ["John Doe"]
```

**Note:** When a variable is declared, it is not recognized as an array variable until it is initialized using either the `Array` constructor or using array literal notation (`[]`).

## Calling the method on a variable before it has been initialized with an array

As you just learned above, another way you can declare variables is to create them without assigning them a value.

```js
let myArray;

myArray.push("John Doe"); // Uncaught TypeError: Cannot read properties of undefined (reading 'push')

console.log(myArray);
```

This works well for data types like strings, numbers, and others but doesn't work well for an array. You must initialize arrays with the `Array` constructor or an array literal notation (`[]`).

```js
let myArray = [];

// Or

let myArray = new Array();
```

Our code will now look like this:

```js
let myArray = [];

myArray.push("John Doe");

console.log(myArray); // ["John Doe"]
```

## Calling the method on an array element rather than the array itself

Array methods are meant to be called on the array itself (meaning the array or the variable used to store the array) and not an array element.

```js
// Example of arrays
let myArray = [12, 13, 17];
let myArray2 = [];
let myArray3 = new Array();

// Example of array elements
myArray[0];
myArray[1];
myArray[2];
```

You might want to push an element to a particular position of an array and think that attaching either the `push()` or `unShift()` method to the element directly will fix that. Unfortunately, you will get the "cannot read property 'push' of undefined" error:

```js
let myArray = [12, 13, 17];

myArray[3].push(15); // Uncaught TypeError: Cannot read properties of undefined (reading 'push')

console.log(myArray);
```

To fix this, you have to call the push method on the variable itself and not on its element:

```js
let myArray = [12, 13, 17];

myArray.push(15);

console.log(myArray); // [12,13,17,15]
```

## Calling the method on an object property that does not exist or has an `undefined` value

A final scenario could be when you try to call the method on an object property that does not exist or whose value is set to `undefined`:

```js
const user = { name: 'John Doe', scores: undefined };
const user2 = { name: 'John Doe' };

user.scores.push(50);
user2.scores.push(50); 
// Uncaught TypeError: Cannot read properties of undefined (reading 'push')
```

In the scenario above, there are two objects: the first object has a key-value pair `scores` whose value is set to `undefined`, but it's meant to receive array values. While for the second object, `scores` does not exist. Both situations can cause errors.

To fix it, all you have to do is **initialize** the key, so it expects array values using the array literal:

```js
const user = { name: "John Doe", scores: [] };

user.scores.push(50);

console.log(user);
```

## Wrapping Up

In this article, you have learned how to fix the "Cannot read properties of undefined" error, which occurs when you attach these array methods to variables that are not declared or initialized as variables.

Have fun coding!
