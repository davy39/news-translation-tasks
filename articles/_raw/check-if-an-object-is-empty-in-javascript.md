---
title: How to Check if an Object is Empty in JavaScript – JS Java isEmpty Equivalent
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-11-28T15:29:23.000Z'
originalURL: https://freecodecamp.org/news/check-if-an-object-is-empty-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/cover-template--21-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "An object is one of the most commonly used data types in programming. An\
  \ object is a collection of related data stored as key-value pairs. For example:\n\
  let userDetails = {\n  name: \"John Doe\",\n  username: \"jonnydoe\",\n  age: 14,\n\
  }\n\nWhen working with ob..."
---

An object is one of the most commonly used data types in programming. An object is a collection of related data stored as key-value pairs. For example:

```js
let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14,
}
```

When working with objects, you may need to check if an object is empty before performing a function.

In JavaScript, there are various ways you can check if an object is empty. In this article, you will learn the various ways you can do this, the options that can be attached, and why.

**Note:** An object is considered empty when it has no key-value pair.

In case you are in a rush, here is a basic example:

```js
const myEmptyObj = {};

// Works best with new browsers
Object.keys(myEmptyObj).length === 0 && myEmptyObj.constructor === Object

// Works with all browsers
_.isEmpty(myEmptyObj)
```

Both methods will return `true`. Let’s now understand these and more options you can use to check if an object is empty in JavaScript.

## How to Check if an Object is Empty with `Object.keys()`

The `Object.keys()` method is a static object method introduced in ECMAScript6 (ES6) and is supported in all modern browsers. This method returns an array with the keys of an object. For example:

```js
let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14
};

console.log(Object.keys(userDetails)); // ["name","username","age"]
```

With this, you can now apply the `.length` property. If it returns zero (0), the object is empty.

```js
let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14
};

let myEmptyObj = {};

console.log(Object.keys(userDetails).length); // 3
console.log(Object.keys(myEmptyObj).length); // 0
```

You can now use this method to check if an object is empty with an if statement or create a function that checks.

```js
const isObjectEmpty = (objectName) => {
  return Object.keys(objectName).length === 0
}
```

This will return either `true` or `false`. If the object is empty, it will return `true`, otherwise, it will return `false`.

```js
let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14
};

let myEmptyObj = {};

const isObjectEmpty = (objectName) => {
  return Object.keys(objectName).length === 0
}

console.log(isObjectEmpty(userDetails)); // false
console.log(isObjectEmpty(myEmptyObj)); // true
```

**Note:** Checking the length alone is not the best option when checking if an object is empty or for any datatype. It is always best to confirm if the data type is correct.

To do this, you can use the constructor check:

```js
const isObjectEmpty = (objectName) => {
  return Object.keys(objectName).length === 0 && objectName.constructor === Object;
}
```

This way, you are liable to get a more thorough check.

Thus far, everything has worked fine. But you might also want to avoid throwing a `TypeError` when a variable is `undefined` or a value of `null` is passed instead of `{}`. To fix this, you can add an extra check:

```js
const isObjectEmpty = (objectName) => {
  return (
    objectName &&
    Object.keys(objectName).length === 0 &&
    objectName.constructor === Object
  );
};
```

In the code above, an extra check is added. This means that it will return either `null` or `undefined` if it is not an empty object, as shown in the example below:

```js
let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14
};

let myEmptyObj = {};
let nullObj = null;
let undefinedObj;

const isObjectEmpty = (objectName) => {
  return (
    objectName &&
    Object.keys(objectName).length === 0 &&
    objectName.constructor === Object
  );
};

console.log(isObjectEmpty(userDetails)); // false
console.log(isObjectEmpty(myEmptyObj)); // true
console.log(isObjectEmpty(undefinedObj)); // undefined
console.log(isObjectEmpty(nullObj)); // null
```

**Note:** This applies to other object static methods, meaning you can make use of `Object.entries()` or `Object.values()` instead of `Object.keys()`.

## How to Check if an Object is Empty with a `for…in` Loop

Another method you can use is the ES6 `for…in` loop. You can use this loop alongside the `hasOwnProperty()` method.

```js
const isObjectEmpty = (objectName) => {
  for (let prop in objectName) {
    if (objectName.hasOwnProperty(prop)) {
      return false;
    }
  }
  return true;
};
```

The method above will loop through each object property. If it finds a single iteration, the object is not empty. Also, the `hasOwnProperty()` will return a boolean indicating whether the object has the specified property as its property.

```js
let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14
};

let myEmptyObj = {};

const isObjectEmpty = (objectName) => {
  for (let prop in objectName) {
    if (objectName.hasOwnProperty(prop)) {
      return false;
    }
  }
  return true;
};

console.log(isObjectEmpty(userDetails)); // false
console.log(isObjectEmpty(myEmptyObj)); // true
```

## How to Check if an Object is Empty with `JSON.stringify()`

You can also make use of the `JSON.stingify()` method, which is used to convert a JavaScript value to a JSON string. This means it will convert your object values to a sting of the object. For example:

```js
let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14
};

console.log(JSON.stringify(userDetails)); 

Output:
"{'name':'John Doe','username':'jonnydoe','age':14}"
```

This means when it is an empty object, then it will return `"{}"`. You can make use of this to check for an empty object.

```js
const isObjectEmpty = (objectName) => {
  return JSON.stringify(objectName) === "{}";
};
```

This will return `true` if the object is empty, otherwise `false`:

```js
let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14
};

let myEmptyObj = {};

const isObjectEmpty = (objectName) => {
  return JSON.stringify(objectName) === "{}";
};

console.log(isObjectEmpty(userDetails)); // false
console.log(isObjectEmpty(myEmptyObj)); // true
```

## How to Check if an Object is Empty with Lodash

Finally, some of the methods I've explained here might work for older browser versions, while others may not work. If you are concerned about a solution that will work for both old and modern browser versions, you can use [Lodash](https://lodash.com/).

Lodash is a modern JavaScript utility library that can perform many JavaScript functionalities with very basic syntax.

For example, if you want to check if an object is empty, you only need to use the "isEmpty" method.

```js
_.isEmpty(objectName);
```

Installing Lodash into your project is quite easy. All you have to do is make use of this command:

```js
$ npm install lodash
```

You can now initialize the underscore method and make use of this method.

```js
const _ = require('lodash');

let userDetails = {
  name: "John Doe",
  username: "jonnydoe",
  age: 14
};

let myEmptyObj = {};

const isObjectEmpty = (objectName) => {
  return _.isEmpty(objectName);
};

console.log(isObjectEmpty(userDetails)); // false
console.log(isObjectEmpty(myEmptyObj)); // true
```

## That's It! 💪

I've enjoyed exploring the various ways you can check if an object is empty. Feel free to use the best method that fits your project or task.

Have fun coding!

Embark on a journey of learning! [Browse 200+ expert articles on web development](https://joelolawanle.com/contents). Check out [my blog](https://joelolawanle.com/posts) for more captivating content from me.
