---
title: JavaScript TypeOf – How to Check the Type of a Variable or Object in JS
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2020-11-09T22:07:19.000Z'
originalURL: https://freecodecamp.org/news/javascript-typeof-how-to-check-the-type-of-a-variable-or-object-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/cover.png
tags:
- name: beginner
  slug: beginner
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Data types and type checking are fundamental aspects of any programming
  language.

  Many programming languages like Java have strict type checking. This means that
  if a variable is defined with a specific type it can contain a value of only that
  type.

  ...'
---

Data types and type checking are fundamental aspects of any programming language.

Many programming languages like Java have strict type checking. This means that if a variable is defined with a specific type it can contain a value of only that type.

JavaScript, however, is a loosely typed (or dynamically typed) language. This means that a variable can contain a value of any type. JavaScript code can execute like this:

```js
let one = 1;
one = 'one';
one = true;
one = Boolean(true);
one = String('It is possible');

```

With this in mind, it is critical to know the type of a variable at any given time.

The type of a variable is determined by the type of the value assigned to it. JavaScript has a special operator called `typeof` which lets you get the type of any value.

In this article, we will learn how `typeof` is used, along with a few gotchas to watch out for.

# **JavaScript Data Types**

Let's take a quick look at JavaScript data types before we dig into the `typeof` operator.

In JavaScript, there are seven primitive types. A primitive is anything that is not an object. They are:

1. String
2. Number
3. BigInt
4. Symbol
5. Boolean
6. undefined
7. null

Everything else is an `object` – even including `array` and `function`. An object is a collection of key-value pairs.

# **The JavaScript typeof Operator**

The `typeof` operator takes only one operand (a unary operator). It evaluates the type of the operand and returns the result as a string. Here is how you use it when you're evaluating the type of a number, 007.

```js
typeof 007;  // returns 'number'

```

There is alternative syntax for the `typeof` operator where you can use it like a `function`:

```js
typeof(operand)

```

This syntax is useful when you want to evaluate an expression rather than a single value. Here is an example of that:

```js
typeof(typeof 007); // returns 'string'

```

In the above example, the expression `typeof 007` evaluates to the type number and returns the string 'number'. `typeof('number')` then results in `'string'`.

Let's look at another example to understand the importance of the parenthesis with the `typeof` operator.

```js
typeof(999-3223); // returns, "number"
```

If you omit the parenthesis, it will return, `NaN`(Not a Number):

```js
typeof 999-3223; // returns, NaN
```

This is because, first `typeof 999` will result in a string, "number". The expression `"number" - 32223` results in NaN as happens when you perform a subtraction operation between a string and number.

### **JavaScript typeof Examples**

The following code snippet shows the type check result of various values using the `typeof` operator.

```js
typeof 0;  //'number'
typeof +0;  //'number'
typeof -0;  //'number'
typeof Math.sqrt(2);  //'number'
typeof Infinity;  //'number'
typeof NaN;  //'number', even if it is Not a Number
typeof Number('100');  //'number', After successfully coerced to number
typeof Number('freeCodeCamp');  //'number', despite it can not be coerced to a number

typeof true;  //'boolean'
typeof false;  //'boolean'
typeof Boolean(0);  //'boolean'

typeof 12n;  //'bigint'

typeof '';  //'string'
typeof 'freeCodeCamp';  //'string'
typeof `freeCodeCamp is awesome`;  //'string'
typeof '100';  //'string'
typeof String(100); //'string'

typeof Symbol();  //'symbol'
typeof Symbol('freeCodeCamp');  //'symbol'

typeof {blog: 'freeCodeCamp', author: 'Tapas A'};  //'object';
typeof ['This', 'is', 101]; //'object'
typeof new Date();  //'object'
typeof Array(4);  //'object'

typeof new Boolean(true);  //'object'; 
typeof new Number(101);  //'object'; 
typeof new String('freeCodeCamp');  //'object';
typeof new Object;  //'object'

typeof alert;  //'function'
typeof function () {}; //'function'
typeof (() => {});  //'function' - an arrow function so, parenthesis is required
typeof Math.sqrt;  //'function'

let a;
typeof a;  //'undefined'
typeof b;  //'undefined'
typeof undefined;  //'undefined'

typeof null;  //'object'

```

The table below shows the type-check values of `typeof`:

<table style="box-sizing: inherit; margin: 0.5em 0px 2.5em; padding: 0px; border: 0px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-variant-numeric: inherit; font-variant-east-asian: inherit; font-weight: 400; font-stretch: inherit; line-height: inherit; font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 1.6rem; vertical-align: top; border-spacing: 0px; border-collapse: collapse; display: inline-block; overflow-x: auto; max-width: 100%; width: auto; white-space: nowrap; background: radial-gradient(at left center, rgba(0, 0, 0, 0.2) 0px, transparent 75%) 0px center / 10px 100% no-repeat scroll, radial-gradient(at right center, rgba(0, 0, 0, 0.2) 0px, transparent 75%) 100% center / 10px 100% scroll rgb(255, 255, 255); color: rgb(10, 10, 35); letter-spacing: normal; orphans: 2; text-align: start; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><thead style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><th style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: 700; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 1.2rem; vertical-align: baseline; color: var(--gray85); letter-spacing: 0.2px; text-align: left; text-transform: uppercase; background-color: var(--gray10);"><strong style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 12px; vertical-align: baseline; color: var(--gray85);">TYPE</strong></th><th style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: 700; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 1.2rem; vertical-align: baseline; color: var(--gray85); letter-spacing: 0.2px; text-align: center; text-transform: uppercase; background-color: var(--gray10);"><strong style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 12px; vertical-align: baseline; color: var(--gray85);">RETURN VALUE OF TYPEOF</strong></th></tr></thead><tbody style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">String</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'string'</code></td></tr><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">Number</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'number'</code></td></tr><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">BigInt</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'bigint'</code></td></tr><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">Symbol</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'symbol'</code></td></tr><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">Boolean</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'boolean'</code></td></tr><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">undefined</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'undefined'</code></td></tr><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">Function object</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'function'</code></td></tr><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">null</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'object'</code>(see below!)</td></tr><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">Any other objects</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'object'</code></td></tr></tbody></table>

# **Common Gotchas with `typeof`**

There are cases where the `typeof` operator may not return types you'd expect. This may cause confusion and errors. Here are a few cases.

### **The type of NaN is a number**

```js
typeof NaN;  //'number', even if it is Not a Number
```

The `typeof NaN` is `'number'`. This is strange, as we shouldn't be detecting a `NaN` using `typeof`. There are better ways to deal with it. We will see them in a minute.

### **The type of `null` is the object**

```js
  typeof null;  //'object'

```

In JavaScript, `typeof null` is an object which gives a wrong impression that, `null` is an object where it is a primitive value.

This result of `typeof null` is actually a bug in the language. There was an attempt made to fix it in past but it was rejected due to the backward compatibility issue.

### **The type of an undeclared variable is undefined**

Before ES6, a type check on an undeclared variable used to result in `'undefined'`. But this is not an error-safe way to deal with it.

With ES6 we can declare block-scoped variables with the `let` or `const` keywords. If you use them with the `typeof` operator before they are initialized, they will throw a `ReferenceError`.

```js
 typeof cat; // ReferenceError
 let cat = 'brownie'; 
```

### **The type of a constructor function is an object**

All constructor functions, except for the `Function` constructor, will always be `typeof`  'object'.

```js
typeof new String('freeCodeCamp'); //'object'
```

This may lead to some confusion, as we expect it to be the actual type (in the above example, a `string` type).

### **The type of an Array is an object**

Though technically correct, this could be the most disappointing one. We want to differentiate between an Array and Object even if an Array is technically an Object in JavaScript.

```js
typeof Array(4);  //'object'
```

Fortunately there are ways to detect an Array correctly. We will see that soon.

# **Beyond `typeof` – Better Type Checking**

Now that we've seen some of the limitations with the `typeof` operator, let's see how to fix them and do better type checking.

### **How to Detect NaN**

In JavaScript, NaN is a special value. The value NaN represents the result of an arithmetic expression that can't actually be represented. For example,

```js
let result = 0/0;
console.log(result);  // returns, NaN

```

Also, if we perform any arithmetic operations with `NaN`, it will always result in a `NaN`.

```js
console.log(NaN + 3); // returns, NaN

```

The type checking on NaN using the `typeof` operator doesn't help much as it returns the type as a `'number'`. JavaScript has a global function called `isNaN()` to detect if a result is NaN.

```js
isNaN(0/0); // returns, true

```

But there is a problem here, too.

```js
isNaN(undefined); // returns true for 'undefined'

```

In ES6, the method `isNaN()` is added to the global `Number` object. This method is much more reliable and so it's the preferred one.

```js
Number.isNaN(0/0); // returns, true
Number.isNaN(undefined); // returns, false

```

Another interesting aspect of `NaN` is that it is the only JavaScript value that is never equal to any other values including itself. So this is another way to detect NaN for the environments where ES6 is not supported:

```js
function isNaN (input) {
  return input !== input;
}

```

### **How to Detect null in JavaScript**

We have seen, detecting null using the `typeof` operator is confusing. The preferred way to check if something is null is by using the strict equality operator(`===`).

```js
function isNull(input) {
 return input === null;
}

```

Make sure not to use the `==` by mistake. Using the `==` in place of `===` will result in misleading type detection.

### **How to Detect an Array in JavaScript**

From ES6 onwards, we can detect an array using the `Array.isArray` method.

```js
Array.isArray([]); // returns true
Array.isArray({}); // returns false

```

Prior to ES6, we could use the `instanceof` operator to determine an Array:

```js
function isArray(input) {
  return input instanceof Array;
}

```

# **A Generic Solution to Type Checking in JavaScript**

There is a way we can create a generic solution to type checking. Have a look at the method, `Object.prototype.toString`. This is very powerful and extremely useful for writing a utility method for type checking.

When `Object.prototype.toString` is invoked using `call()` or `apply()`, it returns the object type in the format: `[object Type]`. The `Type` part in the return value is the actual type.

Let's see how it works with some examples:

```js
// returns '[object Array]'
Object.prototype.toString.call([]); 

// returns '[object Date]'
Object.prototype.toString.call(new Date()); 

// returns '[object String]'
Object.prototype.toString.call(new String('freeCodeCamp'));

// returns '[object Boolean]'
Object.prototype.toString.call(new Boolean(true));

// returns '[object Null]'
Object.prototype.toString.call(null);

```

So this means that if we just take the return string and take out the `Type` part, we will have the actual type. Here is an attempt to do this:

```js
function typeCheck(value) {
  const return_value = Object.prototype.toString.call(value);
  // we can also use regex to do this...
  const type = return_value.substring(
           return_value.indexOf(" ") + 1, 
           return_value.indexOf("]"));

  return type.toLowerCase();
}

```

Now, we can use the `typeCheck` function to detect the types:

```js
typeCheck([]); // 'array'
typeCheck(new Date()); // 'date'
typeCheck(new String('freeCodeCamp')); // 'string'
typeCheck(new Boolean(true)); // 'boolean'
typeCheck(null); // 'null'

```

# **In Summary**

To Summarize what we've learned in this article:

* JavaScript type checking is not as strict as other programming languages.
* Use the `typeof` operator for detecting types.
* There are two variants of the `typeof` operator syntax: `typeof` and `typeof(expression)`.
* The result of a `typeof` operator may be misleading at times. We need to rely on other available methods (`Number.isNaN`,  `Array.isArry`, and so on) in those cases.
* We can use `Object.prototype.toString` to create a generic type detection method.

# **Before we end...**

Thank you for reading this far! Let's connect. You can @ me on [Twitter (@tapasadhikary)](https://twitter.com/tapasadhikary) with comments.

You may also like these other articles:

* [JavaScript undefined and null: Let's talk about it one last time!](https://blog.greenroots.info/javascript-undefined-and-null-lets-talk-about-it-one-last-time-ckh64kmz807v848s15kdkg3dd)
* [JavaScript: Equality comparison with ==, === and Object.is](https://blog.greenroots.info/javascript-equality-comparison-with-and-objectis-ckdpt2ryk01vel9s186ft8cwl)
* [The JavaScript `this` Keyword + 5 Key Binding Rules Explained for JS Beginners](https://www.freecodecamp.org/news/javascript-this-keyword-binding-rules/)

That's all for now. See you again with my next article soon. Until then, please take good care of yourself.

