---
title: How to Convert a Value to a Boolean in JavaScript
subtitle: ''
author: Natalie Pina
co_authors: []
series: null
date: '2022-05-20T18:06:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-value-to-boolean-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/Fashion-Sale--Banner--Landscape--.png
tags:
- name: beginner
  slug: beginner
- name: Boolean
  slug: boolean
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'A boolean is a primitive value that represents either true or false. In
  Boolean contexts, JavaScript utilizes type casting to convert values to true/false.
  There are implicit and explicit methods to convert values into their boolean counterparts.

  Thi...'
---

A boolean is a [primitive value](https://developer.mozilla.org/en-US/docs/Glossary/Primitive) that represents either true or false. In Boolean contexts, JavaScript utilizes [type casting](https://developer.mozilla.org/en-US/docs/Glossary/Type_Conversion) to convert values to true/false. There are implicit and explicit methods to convert values into their boolean counterparts.

This article provides an overview of truthy and falsy values and how to convert values into booleans in JavaScript.

### JavaScript Truthy and Falsy Values Cheatsheet

```
Boolean(false);         // false
Boolean(undefined);     // false
Boolean(null);          // false
Boolean('');            // false
Boolean(NaN);           // false
Boolean(0);             // false
Boolean(-0);            // false
Boolean(0n);            // false

Boolean(true);          // true
Boolean('hi');          // true
Boolean(1);             // true
Boolean([]);            // true
Boolean([0]);           // true
Boolean([1]);           // true
Boolean({});            // true
Boolean({ a: 1 });      // true
```

It's best to start by first understanding which values are interpreted as truthy or falsy by JavaScript. It's also important to understand [implicit coercion](https://betterprogramming.pub/implicit-and-explicit-coercion-in-javascript-b23d0cb1a750) compared to [explicit coercion](https://www.bookstack.cn/read/TypesGrammar/spilt.3.ch4.md#Explicitly:%20*%20%E2%80%94%3E%20Boolean). 

Implicit coercion is initiated by the JavaScript engine and happens automatically. Explicit coercion is performed by manually converting values, and JavaScript provides built in methods to handle this.

### The `!!` Operator

```javascript
!!value
```

You may already be familiar with `!` as the logical NOT operator. When using two in succession (`!!`), the first `!` coerces the value to a boolean and inverts it. For example `!true` would result in false. The second `!` reverses the previous inverted value, resulting in the true boolean value.

This is generally a preferred method, as it has [better performance](https://www.measurethat.net/Benchmarks/Show/11127/0/boolean-vs). A potential con to this method is a loss in readability, mainly if other developers are unfamiliar with how this operator works.

```javascript
const value = "truthy string"
!!value // true
```

Here is an example breaking this down into steps:

```javascript
const value = "truthy string";

!value; // false
!!value; // true
```

Below is a list of example output with the `!!` operator.

```javascript
// Falsy Values

!!'' // false
!!false // false
!!null // false
!!undefined // false
!!0 // false
!!NaN // false


// Truthy Values

!![] // true
!!"false" // true
!!true // true
!!1 // true
!!{} // true
```

### The `Boolean()` Function

```javascript
Boolean(value)
```

`Boolean()` is a global function that converts the value it's passed into a boolean.   
  
You shouldn't use this with the new keyword (`new Boolean`) as this creates an instance of a Boolean that has a type of object. Below is an example of the correct use of this function.

```javascript
const value = "truthy string"
Boolean(value) // true
```

## TL;DR

There are two methods to cast a value to a boolean in JavaScript.

### 1. `!!` 

```javascript
!!value

```

### 2. `Boolean()` 

```
Boolean(value)

```

```javascript
const finalThoughts = "I really enjoyed writing this article. Thanks for reading!"

!!finalThoughts // true
Boolean(finalThoughts) // true

```

