---
title: JavaScript Math Functions Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-18T18:25:00.000Z'
originalURL: https://freecodecamp.org/news/math-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dc6740569d1a4ca398d.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Math
  slug: math
seo_title: null
seo_desc: 'Math

  Math is one of JavaScript''s global or standard built-in objects, and can be used
  anywhere you can use JavaScript. It contains useful constants like π and Euler’s
  constant and functions such as floor(), round(), and ceil().

  In this article, we''ll...'
---

## **Math**

`Math` is one of JavaScript's global or standard built-in objects, and can be used anywhere you can use JavaScript. It contains useful constants like π and Euler’s constant and functions such as `floor()`, `round()`, and `ceil()`.

In this article, we'll look at examples of many of those functions. But first, let's learn more about the `Math` object.

### **Example**

The following example shows how to use the `Math` object to write a function that calculates the area of a circle:

```javascript
function calculateCircleArea(radius) {
  return Math.PI * Math.pow(radius, 2);
}

calculateCircleArea(1); // 3.141592653589793
```

## **Math Max**

`Math.max()` is a function that returns the largest value from a list of numeric values passed as parameters. If a non-numeric value is passed as a parameter, `Math.max()` will return `NaN`.

An array of numeric values can be passed as a single parameter to `Math.max()` using either `spread (...)` or `apply`. Either of these methods can, however, fail when the amount of array values gets too high.

### **Syntax**

```js
Math.max(value1, value2, value3, ...);
```

### **Parameters**

Numbers, or limited array of numbers.

### **Return Value**

The greatest of given numeric values, or `NaN` if any given value is non-numeric.

### **Examples**

_Numbers As Parameters_

```js
Math.max(4, 13, 27, 0, -5); // returns 27
```

_Invalid Parameter_

```js
Math.max(4, 13, 27, 'eight', -5); // returns NaN
```

_Array As Parameter, Using Spread(…)_

```js
let numbers = [4, 13, 27, 0, -5];

Math.max(...numbers); // returns 27
```

_Array As Parameter, Using Apply_

```js
let numbers = [4, 13, 27, 0, -5];

Math.max.apply(null, numbers); // returns 27
```

## Math Min

The Math.min() function returns the smallest of zero or more numbers.

You can pass it any number of arguments.

```javascript
Math.min(7, 2, 9, -6);
// returns -6
```

## Math PI

`Math.PI` is a static property of the Math object and is defined as the ratio of a circle’s circumference to its diameter. Pi is approximately 3.14149, and is often represented by the Greek letter π.

## **Examples**

```js
Math.PI \\ 3.141592653589793
```

#### **More Information:**

[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/PI)

## **Math Pow**

`Math.pow()` returns the value of a number to the power of another number.

#### **Syntax**

`Math.pow(base, exponent)`, where `base` is the base number and `exponent` is the number by which to raise the `base`.

`pow()` is a static method of `Math`, therefore it is always called as `Math.pow()` rather than as a method on another object.

#### **Examples**

```js
Math.pow(5, 2); // 25
Math.pow(7, 4); // 2401
Math.pow(9, 0.5); // 3
Math.pow(-8, 2); // 64
Math.pow(-4, 3); // -64
```

#### 

## **Math Sqrt**

The function `Math.sqrt()` returns the square root of a number.

If a negative number is entered, `NaN` is returned.

`sqrt()` is a static method of `Math`, therefore it is always called as `Math.sqrt()` rather than as a method on another object.

#### **Syntax**

`Math.sqrt(x)`, where `x` is a number.

#### **Examples**

```js
Math.sqrt(25); // 5
Math.sqrt(169); // 13
Math.sqrt(3); // 1.732050807568
Math.sqrt(1); // 1
Math.sqrt(-5); // NaN
```

#### 

## **Math Trunc**

`Math.trunc()` is a method of the Math standard object that returns only the integer part of a given number by simply removing fractional units. This results in an overall rounding towards zero. Any input that is not a number will result in an output of NaN.

Careful: This method is an ECMAScript 2015 (ES6) feature and thus is not supported by older browsers.

### **Examples**

```javascript
Math.trunc(0.1)   //  0
Math.trunc(1.3)   //  1
Math.trunc(-0.9)  // -0
Math.trunc(-1.5)  // -1
Math.trunc('foo') // NaN
```

## Math Ceil

The `Math.ceil()` is a method of the Math standard object that rounds a given number upwards to the next integer. Take note that for negative numbers this means that the number will get rounded “towards 0” instead of the number of greater absolute value (see examples).

### **Examples**

```javascript
Math.ceil(0.1)  //  1
Math.ceil(1.3)  //  2
Math.ceil(-0.9) // -0
Math.ceil(-1.5) // -1
```

## Math Floor

`Math.floor()` is a method of the Math standard object that rounds a given number downwards to the next integer. Take note that for negative numbers this means that the number will get rounded “away from 0” instead of to the number of smaller absolute value since `Math.floor()` returns the largest integer less than or equal to the given number.

### **Examples**

```javascript
Math.floor(0.9)  //  0
Math.floor(1.3)  //  1
Math.floor(0.5)  //  0
Math.floor(-0.9) // -1
Math.floor(-1.3) // -2
```

### An application of math.floor: How to Create a JavaScript Slot Machine

For this exercise, we have to generate three random numbers using a specific formula and not the general one. `Math.floor(Math.random() * (3 - 1 + 1)) + 1;`

```text
slotOne = Math.floor(Math.random() * (3 - 1 + 1)) + 1;
slotTwo = Math.floor(Math.random() * (3 - 1 + 1)) + 1;
slotThree = Math.floor(Math.random() * (3 - 1 + 1)) + 1;
```

### Another example: Finding the remainder

### Example

```text
5 % 2 = 1 because
Math.floor(5 / 2) = 2 (Quotient)
2 * 2 = 4
5 - 4 = 1 (Remainder)
```

### Usage

In mathematics, a number can be checked even or odd by checking the remainder of the division of the number by 2.

```text
17 % 2 = 1 (17 is Odd)
48 % 2 = 0 (48 is Even)
```

**Note** Do not confuse it with _modulus_ `%` does not work well with negative numbers.

## More math-related articles:

* [Converting an am/pm clock to 24 hour time](https://guide.freecodecamp.org/mathematics/converting-am-pm-to-24-hour-clock/)
* [Simpson's rule](https://www.freecodecamp.org/news/simpsons-rule/)
* [What is a Hexagon?](https://guide.freecodecamp.org/mathematics/hexagon/)

