---
title: JavaScript Type Checking – How to Check Type in JS with typeof()
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-12-09T22:16:19.000Z'
originalURL: https://freecodecamp.org/news/javascript-type-checking-how-to-check-type-in-js-with-typeof
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/cover-template.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'JavaScript is a dynamically typed (or loosely typed) programming language.
  It allows you to declare variables without specifying or defining the variable type.

  You can create a variable in JavaScript without defining the type of value you can
  store i...'
---

JavaScript is a dynamically typed (or loosely typed) programming language. It allows you to declare variables without specifying or defining the variable type.

You can create a variable in JavaScript without defining the type of value you can store in the variable. This can affect your program and cause bugs during runtime because the type can change.

For example, a variable can be declared and assigned a number. But as you write more code, values might get misplaced, and you might assign the same variable a string or boolean. This would affect your code when it runs:

```js
let myVariable = 45; // => number
myVariable = 'John Doe'; // => string
myVariable = false; // => boolean
```

As you can see from the above example, a variable in JavaScript can change types throughout the execution of a program. This can be hard to keep track of as a programmer. This is one of the reasons why TypeScript is considered a superset of JavaScript.

To validate variables by checking their types in JavaScript, you can use the `typeof` operator. Type checking in JavaScript is not straightforward for non-primitive data types and specific values. This is why type-checking can become annoying, especially for inexperienced JS developers.

In this article, you will learn how to use the `typeof` operator, instances when you should not use `typeof`, and the best way to check type in JavaScript for such instances.

## JavaScript Data Types

In JavaScript, data types are classified into two groups: you have primitive and non-primitive data types. Aside from the object, which is a non-primitive data type, all other data types are primitive.

These data types include:

1. String
    
2. Number
    
3. Boolean (true and false)
    
4. null
    
5. undefined
    
6. Symbol
    

At this point, you may assume that I omitted arrays and functions. But no, I didn’t. This is because they are both objects.

## How to Check Type with the `typeof` Operator in JavaScript

The `typeof` operator accepts a single operand (a unary operator) and determines the operand's type.

There are two ways you can use the `typeof` operator. You can evaluate a single value or an expression:

```js
typeof(expression);

// Or

typeof value;
```

The `typeof` operator will return the type as a string, meaning “number”, “string”, "boolean”, and lots more.

```js
let myVariable = 45;
console.log(typeof myVariable); // returns "number"
console.log(typeof(myVariable)); // returns "number"

console.log(typeof 45); // returns "number"
console.log(typeof(45)); // returns "number"
```

It is important to know that you should always use the expression method (in the form of a function) when evaluating an [expression](https://flaviocopes.com/javascript-expressions/) rather than a single value. For example:

```js
console.log(typeof(typeof 45)); // returns "string"
```

The above returns a string because the output of `typeof 45` is evaluated as "number" (which is returned as a string), then the output of `typeof("number")` is evaluated as "string”.

Another example is if your number has a hyphen in it:

```js
// Using expression
console.log(typeof(123-4567-890)); // returns "number"

// Using single value
console.log(typeof 123-4567-890); // returns NaN
```

The single value method will return `NaN` (Not a Number) because it will first evaluate `typeof 123`, which will return a string, "number". This means you are now left with `"number" - 4567-890`, which cannot be subtracted and will return `NaN`.

### How to Check for the Number Data Type

Let’s now explore the possible instances that will return the number data type.

There are different possible values that JavaScript considers a number, such as positive and negative integers, zero, floating-point numbers, and infinity:

```js
console.log(typeof 33); // returns "number"
console.log(typeof -23); // returns "number"
console.log(typeof 0); // returns "number"
console.log(typeof 1.2345); // returns "number"
console.log(typeof Infinity); // returns "number"
```

It’s also important to know that values like NaN, even though it means Not-a-Number, will always return a type of “number”. Also, math functions will have the data type of number:

```js
console.log(typeof NaN); // returns "number"
console.log(typeof Math.LOG2E); // returns "number"
```

Finally, when you use the `Number()` constructor to explicitly typecast a string that holds a number to a number or even a value like an actual string that cannot be typecasted to an integer, it will always return a number as its data type:

```js
// Typecasting value to number
console.log(typeof Number(`123`)); // returns "number"

// Value cannot be typecasted to integer
console.log(typeof Number(`freeCodeCamp`)); // returns "number"
```

Finally, when you make use of methods like parseInt() and parseFloat(), which convert a string to a number and also round up a number, its data type will be number:

```js
console.log(typeof parseInt(`123`)); // returns "number"
console.log(typeof parseFloat(`123.456`)); // returns "number"
```

### How to Check for the String Data Type

There are just a few instances that will return “string”. These instances are the empty string, a string of characters (this can also be a number), and multiple words:

```js
console.log(typeof ''); // returns "string"
console.log(typeof 'freeCodeCamp'); // returns "string"
console.log(typeof 'freeCodeCamp offers the best free resources'); // returns "string"
console.log(typeof '123'); // returns "string"
```

Also, when you use the `String()` constructor with any value:

```js
console.log(typeof String(123)); // returns "string"
```

### How to Check for the Boolean Data Type

When you check for the `true` and `false` values, it will always return the type “boolean”. Also, when you check anything that makes use of the `Boolean()` constructor:

```js
console.log(typeof true); // returns "boolean"
console.log(typeof false); // returns "boolean"
console.log(typeof Boolean(0)); // returns "boolean"
```

Additionally, when you use the double not operator (`!!`), which works just like the `Boolean()` constructor, “boolean” will be returned:

```js
console.log(typeof !!(0)); // returns "boolean"
```

### How to Check for the Symbol Data Type

When you use the `Symbol()` constructor, the "symbol" data type will be returned even if no value is passed. Also, when you pass in a parameter or use the `Symbol.iterator` symbol, which specifies the default iterator for an object:

```js
console.log(typeof Symbol()); // returns "symbol"
console.log(typeof Symbol('parameter')); // returns "symbol"
console.log(typeof Symbol.iterator); // returns "symbol"
```

### How to Check for the Undefined Data Type

A variable is said to be `undefined` when you declare it without initiating a value. When you check for undefined, a declared variable with no value (undefined), and an undefined variable, they will always return “undefined”:

```js
// Using the undefined keyword
console.log(typeof undefined); // returns "undefined"

//variable is declared but undefined (has no value intentionally)
let a;
console.log(typeof a); // returns "undefined"

// Using undefined variable
console.log(typeof v); // returns "undefined"
```

So far, you have learned how to check for types of all primitive data types except null. It's a little tricky and I covered it in detail in my article on [Null Checking in JavaScript Explained](https://www.freecodecamp.org/news/how-to-check-for-null-in-javascript/).

But I will briefly go over how to check for `null` in this article so you can understand the basics.

### How to Check for the Object Data Type

Certain instances will always return “object”, though that of `null` is a [historical bug](https://www.turbinelabs.com/blog/the-odd-history-of-javascripts-null) that cannot be fixed, while function has its technical reason.

```js
console.log(typeof null);
console.log(typeof [1, 2, 3, "freeCodeCamp"]);
console.log(typeof { age: 12, name: "John Doe" });
console.log(typeof [1, 2, 3, 4, 5, 6]);
```

As you can see in the example above, an array will always return “object” when you use the `typeof` operation. This may not be very pleasant, but technically, an Array is a special type of object:

```js
console.log(typeof [1, 2, 3, 'freeCodeCamp']);
```

In ES6, the `Array.isArray` method was introduced, which makes it possible for you to detect an Array easily:

```js
console.log(Array.isArray([1, 2, 3, "freeCodeCamp"])); // returns true
console.log(Array.isArray({ age: 12, name: "John Doe" })); // returns false
```

Also, before the introduction of ES6, the `instanceof` operator is used to detect an Array:

```js
const isArray = (input) => {
    return input instanceof Array;
};

console.log(isArray([1, 2, 3, 'freeCodeCamp'])); // returns true
```

### How to Check for the Null Data Type

When you use the `typeof` operator to check the `null` value, it returns “object” because of a [historical bug](https://www.turbinelabs.com/blog/the-odd-history-of-javascripts-null) that cannot be fixed.

**Note:** Do not confuse null with undefined. A variable is referred to as `null` if it intentionally contains the value of `null`. In contrast, a variable is `undefined` when you declare it without initiating a value.

A very straightforward way to detect `null` is to use the strict comparison:

```js
const isNull = (input) => {
    return input === null;
}

let myVar = null;
console.log(isNull(myVar)); // returns true
```

You can read this article on [Null Checking in JavaScript Explained](https://www.freecodecamp.org/news/how-to-check-for-null-in-javascript/) for more options and detailed explanations.

## A Generic Solution to Type Checking in JavaScript

In an earlier article by [Tapas Adhikary](https://www.freecodecamp.org/news/author/tapas/) on [How to Check the Type of a Variable or Object in JS](https://www.freecodecamp.org/news/javascript-typeof-how-to-check-the-type-of-a-variable-or-object-in-js/), he added and explained a generic solution that you can use to check for type more accurately:

```js
const typeCheck = (value) => {
    const return_value = Object.prototype.toString.call(value);
    const type = return_value.substring(
    return_value.indexOf(" ") + 1,
    return_value.indexOf("]")
    );

    return type.toLowerCase();
};
```

Let’s test this:

```js
console.log(typeCheck([])); // returns 'array'
console.log(typeCheck(new Date())); // returns 'date'
console.log(typeCheck(new String("freeCodeCamp"))); // returns 'string'
console.log(typeCheck(new Boolean(true))); // returns 'boolean'
console.log(typeCheck(null)); // returns 'null'
```

## Wrapping up!

In this article, you have learned how to check for types in JavaScript with the `typeof` operator.

You also learned the limitations and how to use other methods to overcome the limitations. Remember that for most primitive data types, you can always use the `typeof` operator.

Have fun coding!
