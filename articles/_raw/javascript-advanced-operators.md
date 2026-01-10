---
title: Advanced JavaScript Operators – Nullish Coalescing, Optional Chaining, and
  Destructuring Assignment
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2024-01-04T15:22:39.000Z'
originalURL: https://freecodecamp.org/news/javascript-advanced-operators
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/js-advanced-operators.png
tags:
- name: JavaScript
  slug: javascript
- name: Operators
  slug: operators
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Hi Everyone! In this article, I''m going to teach you how to use three
  advanced JavaScript operators: the Nullish Coalescing, Optional Chaining, and Destructuring
  Assignment operators.

  These three operators will help you write clearer and less error-p...'
---

Hi Everyone! In this article, I'm going to teach you how to use three advanced JavaScript operators: the Nullish Coalescing, Optional Chaining, and Destructuring Assignment operators.

These three operators will help you write clearer and less error-prone code. 

## The Nullish Coalescing Operator

When you’re inspecting JavaScript code, you may find an expression using a double question mark (`??`), as in the code below:

```js
console.log(username ?? "Guest");
```

The double question mark is a logical operator that returns the expression on the right-hand side of the mark when the expression on the left-hand side is `null` or `undefined`

This operator is also known as the nullish coalescing operator. It’s a new feature introduced in JavaScript ES2020 that allows you to check for `null` or `undefined` values in a more concise way.

### Nullish Coalescing Operator Syntax

The syntax for the nullish coalescing operator is very simple. It consists of two question marks `??` placed between two operands.

Here’s an example:

```js
let firstName = null;
let username = firstName ?? "Guest";
console.log(username); // "Guest"
```

The code above assigns the `firstName` variable value as the value of the `username` variable.

When the `firstName` value is `null` or `undefined`, then the value `Guest` will be assigned to the `username` variable instead:

![Image](https://www.freecodecamp.org/news/content/images/2024/01/nullish-coalescing-output.png)
_Result of using the nullish coalescing operator_

You can also write it this way:

```js
let username = undefined ?? "Guest";
console.log(username); // "Guest"
```

As you can see, you don’t need an `if-else` statement to check for `null` or `undefined` values.

### Why JavaScript Needs This Operator

The nullish coalescing operator was created as an improved alternative to the OR operator `||`.

The OR operator was originally created to provide a default or fallback value when the left-hand expression is falsy, or evaluates to `false`.

But after some real-world uses, it’s clear that there are times when developers want to return values that are considered falsy, such as `0` and an empty string (`""`)

The use of the OR operator will prevent you from returning any falsy values at all. Consider the following example:

```js
// empty string evaluates to false in JavaScript:
let firstName = "";
let username = firstName ?? "Guest";
console.log(username); // ""

// When you use OR operator:
username = firstName || "Guest";
console.log(username); // "Guest"
```

By using the nullish coalescing operator, you will only replace **exactly** `null` and `undefined` values with the right-hand value.

The nullish coalescing operator can be used with any type of value, including numbers, strings, and objects.

### Nullish Coalescing Operator Use Cases

The nullish coalescing operator is useful in a variety of situations where you need to check for `null` or `undefined` values and provide a default value.

Here are several examples of common use cases:

#### Handling Missing Function Arguments

When a function is called, it’s possible that some of the arguments may be omitted.

The Nullish Coalescing Operator can be used to provide default values for a missing argument as follows:

```js
function greet(name) {
  console.log(`Hello, ${name ?? "Guest"}!`);
}

greet(); // 'Hello, Guest!'
greet("John"); // 'Hello, John!'
```

#### Accessing Object Properties

When working with objects, it’s possible that a property may not exist or is `undefined`.

The Nullish Coalescing Operator can be used to safely access object properties and provide a default value when the property is missing:

```js
let user = { name: "John Doe" };
let email = user.email ?? "N/A";
console.log(email); // 'N/A'
```

#### Choosing Between a Variable and a Constant

You may want to select a value from a variable or a constant if the variable is `null` or `undefined`:

```js
let value = null;
const DEFAULT_VALUE = 'Default';

let result = value ?? DEFAULT_VALUE;

console.log(result); // 'Default'
```

As you can see, the Nullish Coalescing Operator is a great feature that can make your code more concise and reliable.

### Using `??` with the `||` and `&&` Operators

For safety reasons, the double question mark can’t be used together with JavaScript OR (`||`) and AND (`&&`) operators without parentheses `()` separating the operators.

For example, the following code tries to see if either `firstName` or `lastName` variable can be used as the value of `username` before using `"Guest"` as its value:

```js
let firstName = "John";
let lastName = "Stone";
let username = firstName || lastName ?? "Guest";
// Error: Unexpected token '??'

console.log(username);
```

This is because JavaScript won’t be able to determine which operator it needs to evaluate first. You need to use parentheses to clearly indicate the priority of the evaluations.

The following code will first evaluate the expressions inside the parentheses:

```js
let firstName = null;
let lastName = undefined;
let username = (firstName || lastName) ?? "Guest";

console.log(username); // "Guest"
```

And that’s how you combine the nullish coalescing operator with either AND or OR operator.

## The Optional Chaining Operator

Like the nullish coalescing operator, the optional chaining operator is a modern addition to JavaScript that offers a better way to do things.

The optional chaining operator `?.` gives you a safe way to access properties and methods of an object, avoiding an error in the process.

One of the most common problems in JavaScript is that you can get an error when you access a property of an `undefined` value.

For example, suppose you have a `car` object as follows:

```js
const car = {};

console.log(car.manufacturer); // undefined
console.log(car.manufacturer.address); // ❌ TypeError!
```

In the example above, accessing the `manufacturer` property returns `undefined`, but when you try to access the `address` property of the `manufacturer` property, JavaScript returns an error.

Even though this is how JavaScript works, a better way to handle the non-existent property would be to just return an `undefined` back, just like when we try to access the `manufacturer` property.

This is why the optional chaining operator was created. The operator returns either the value of the property, or `undefined` when the property is `null` or `undefined`.

To use the operator, just add a question mark in front of the dot `.` notation:

```js
const car = {};

console.log(car.manufacturer?.address); // undefined
```

The optional chaining operator can be added anytime you use the dot notation to access a property or method.

This operator allows you to avoid the TypeError that occurs when accessing a property or calling a method from a non-existent property:

```js
const car = {};

console.log(car.manufacturer?.address); // undefined
console.log(car.manufacturer?.drive()); // undefined
```

Note that the optional chaining operator only checks the value before it. If the `car` variable can be `null`, then you need to add the operator after when accessing the `car` object as well.

See the following example:

```js
const car = null;

console.log(car?.manufacturer?.address); // undefined
console.log(car.manufacturer?.address); // TypeError: Cannot read properties of null
```

And that’s how the optional chaining operator works. It’s really useful when you’re working with objects in your project.

Next, let’s learn about the destructuring assignment.

## Destructuring Assignment Operator

The destructuring assignment is a special operator that allows you to "unpack" or "extract" the values of JavaScript arrays and objects. It has become one of the most useful features of JavaScript language for two reasons:

* It helps you to avoid code repetition.
* It keeps your code clean and easy to understand.

Let’s see how you can destructure an array and an object next.

### Destructuring Arrays

Here’s how you normally assign an array values to variables:

```js
const sampleArray = ['Jane', 'John'];

const firstIndex = sampleArray[0];
const secondIndex = sampleArray[1];
```

The code above works, but you need two lines of code to get two elements from an array. Using the destructuring assignment, you can assign array elements into variables in one short line:

```js
const sampleArray = ['Jane', 'John'];

const [firstIndex, secondIndex] = sampleArray;
```

The above code will return the same value for `firstIndex` and `secondIndex` variable. No matter how many elements you have, the destructuring will start from the zero index.

To create a destructuring assignment, you need to add square brackets `[]` after the `let`/ `const` keyword. When you add square brackets after the assignment (`=`) operator, it’s an array. If you add them before the assignment operator, it’s a destructuring assignment.

You can also use the rest operator `…​` to copy the rest of the values after your assignment. Take a look at the following example:

```js
const sampleArray = ['Jane', 'John', 'Jack', 'Aston'];

const [one, two, ...rest] = sampleArray;
```

The `rest` variable will contain an array with values of `['Jack','Aston']`.

You can also put default values for these variables when the extracted value is undefined:

```js
const [a = 'Martin', b = 10] = [true];

// a will return true
// b will return 10
```

You can also immediately assign the return of a function into assignments. This is frequently used in libraries like React:

```jsx
const [a, b] = myFunction();

function myFunction() {
  return ['John', 'Jack'];
}
```

The variable `a` will return "John" and `b` will return "Jack".

Finally, you can also ignore some variables by skipping the assignment for that index:

```js
const [a, , b] = [1, 2, 3];

// a will return 1
// b will return 3
```

Destructuring assignment makes unpacking array values easier and shorter, with less repetition.

### Object Destructuring

Just like arrays, you can destructure objects the same way, but instead of using the square brackets (`[]`) you need to use the curly brackets (`{}`):

```js
const user = {
  firstName: 'Jack',
  lastName: 'Smith',
};

const { firstName, lastName } = user;
```

You can use the colon delimiter (`:`) to assign the property into a different name. The example below assign the value of `firstName` into `name`:

```js
const user = {
  firstName: 'Jack',
  lastName: 'Smith',
};

const { firstName: name, lastName } = user;
```

Note that you still only create two variables: `name` and `lastName`. The `firstName` is assigned to `name`, so it won’t create a separate variable.

Just like arrays, you can destructure an object returned by a function immediately:

```js
function myFunction() {
  return { firstName: 'Jack', lastName: 'Austin' };
}

const { firstName, lastName } = myFunction();

```

Also, you can destructure an object from the function parameters, exactly when you define the function:

```js
function myFunction({ firstName, lastName }) {
  return firstName + ' ' + lastName;
}

const user = {
  firstName: 'Jack',
  lastName: 'Austin',
};

const name = myFunction(user);
```

The destructuring assignment is a useful addition to JavaScript that makes it easier to unpack values from objects and arrays. You’re going to use it frequently when you code using a library like React.

## Conclusion

JavaScript is constantly improving every year, and the three operators explained in this article are a great addition that can help you produce more concise and readable code.

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!  

