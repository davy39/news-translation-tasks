---
title: JavaScript Modulo, Division, Remainder and Other Math Operators Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-31T18:43:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-arithmetic-math-operators-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d3b740569d1a4ca369f.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Math
  slug: math
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'JavaScript provides the user with five arithmetic operators: +, -, *, /
  and %. The operators are for addition, subtraction, multiplication, division and
  remainder (or modulo), respectively.

  Addition

  Syntax

  a + b

  Usage

  2 + 3          // returns 5

  true...'
---

JavaScript provides the user with five arithmetic operators: `+`, `-`, `*`, `/` and `%`. The operators are for addition, subtraction, multiplication, division and remainder (or modulo), respectively.

## **Addition**

**Syntax**

`a + b`

**Usage**

```text
2 + 3          // returns 5
true + 2       // interprets true as 1 and returns 3
false + 5      // interprets false as 0 and returns 5
true + "bar"   // concatenates the boolean value and returns "truebar"
5 + "foo"      // concatenates the string and the number and returns "5foo"
"foo" + "bar"  // concatenates the strings and returns "foobar"
```

_Hint:_ There is a handy [increment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Arithmetic_Operators#Increment_()) operator that is a great shortcut when you’re adding numbers by 1.

## **Subtraction**

**Syntax**

`a - b`

**Usage**

```text
2 - 3      // returns -1
3 - 2      // returns 1
false - 5  // interprets false as 0 and returns -5
true + 3   // interprets true as 1 and returns 4
5 + "foo"  // returns NaN (Not a Number)
```

_Hint:_ There is a handy [decrement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Arithmetic_Operators#Decrement_(--)) operator that is a great shortcut when you’re subtracting numbers by 1.

## **Multiplication**

**Syntax**

`a * b`

**Usage**

```text
2 * 3                // returns 6
3 * -2               // returns -6
false * 5            // interprets false as 0 and returns 0
true * 3             // interprets true as 1 and returns 3
5 * "foo"            // returns NaN (Not a Number)
Infinity * 0         // returns NaN
Infinity * Infinity  // returns Infinity
```

## **Division**

**Syntax**

`a / b`

**Usage**

```text
3 / 2                // returns 1.5
3.0 / 2/0            // returns 1.5
3 / 0                // returns Infinity
3.0 / 0.0            // returns Infinity
-3 / 0               // returns -Infinity
false / 5            // interprets false as 0 and returns 0
true / 2             // interprets true a 1 and returns 0.5
5 + "foo"            // returns NaN (Not a Number)
Infinity / Infinity  // returns NaN
```

## **Remainder**

**Syntax**

`a % b`

**Usage**

```text
3 % 2          // returns 1
true % 5       // interprets true as 1 and returns 1
false % 4      // interprets false as 0 and returns 0
3 % "bar"      // returns NaN
```

## **Increment**

**Syntax**

`a++ or ++a`

**Usage**  
// Postfix x = 3; // declare a variable y = x++; // y = 4, x = 3  
// Prefix var a = 2; b = ++a; // a = 3, b = 3

## **Decrement**

**Syntax**

`a-- or --a`

**Usage**  
// Postfix x = 3; // declare a variable y = x—; // y = 3, x = 3  
// Prefix var a = 2; b = —a; // a = 1, b = 1 _!Important!_ As you can see, you **cannot** perform any sort of operations on `Infinity`.

## More on math in JavaScript:

* [JavaScript math functions explained](https://www.freecodecamp.org/news/math-in-javascript/)
* [JavaScript's math.random() method explained](https://www.freecodecamp.org/news/p/b988fbe9-a282-435b-8df0-71eb9193ad5c/)

