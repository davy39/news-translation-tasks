---
title: JavaScript Modulo Operator – How to Use the Modulus in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-02-10T19:35:28.000Z'
originalURL: https://freecodecamp.org/news/javascript-modulo-operator-how-to-use-the-modulus-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/cover-template--1--1.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In JavaScript, you may need to perform mathematical calculations such as
  determining if a number is even or odd, wrapping values within a range, and converting
  between degrees and radians in trigonometry.

  To help you perform all these mathematical ca...'
---

In JavaScript, you may need to perform mathematical calculations such as determining if a number is even or odd, wrapping values within a range, and converting between degrees and radians in trigonometry.

To help you perform all these mathematical calculations, the modulo operator can be extremely useful.

This article will explain what the modulo operator in is JavaScript, how to use it, and what mathematical calculations it can perform.

## What is the Modulo Operator in JavaScript?

The modulo operator in JavaScript, also known as the remainder operator, is used to find the remainder after dividing one number by another. The modulo operator in JavaScript is represented by the percent sign (`%`).

For example, `10 modulo 3` will be 1 (I'll explain how this works after the code sample below). The short form is 10 mod 3 = 1. But for JavaScript, you will use `10 % 3`. It divides the first operand (the dividend) by the second operand (the divisor) and returns the remainder.

let dividend = 10; let divisor = 3; let result = dividend % divisor; console.log(result); // returns 1

In the above example, `10` divided by `3` results in a quotient of `3` and a remainder of `1`. The modulo operator returns this remainder, which is `1`.

## Different Ways You Can Use the Modulo Operator

You can use the modulo operator in several ways, such as checking for odd and even numbers, wrapping values within a range, and many more.

### How to check for odd or even numbers with the modulo operator

There are many ways you can check if a number is either odd or even in JavaScript. But one straightforward and often used method is using the modulo operator. You do this by checking if the result of the operation `number modulo 2` is equal to 0 – if so, the number is even. Otherwise it is odd.

```js
let n = 7;
if (n % 2 === 0) {
  console.log(n + " is even");
} else {
  console.log(n + " is odd");
}
```

In the example above, `n` stands for the number. You can try any number and confirm. For example, you can make this a function and pass in values as arguments:

```js
const checkNumber = (n) => {
  if (n % 2 === 0) {
    console.log(n + " is even");
  } else {
    console.log(n + " is odd");
  }
};

checkNumber(8); // "8 is even"
checkNumber(21); // "21 is odd"
checkNumber(17); // "17 is odd"
checkNumber(10); // "10 is even"
```

### How to wrap values within a range with the modulo operator

Wrapping a value/number in a range refers to taking a number that falls outside of a specified range (for example 0 to 360) and "wrapping" it back into the range. Wrapping numbers in a range can be used to normalize values to a specific range.

You can use the modulo operator to wrap a value within a range by using it as the basis for a modulo operation.

For example, in a simulation, you might want to ensure that angles are always between 0 and 360 degrees, even if they go beyond that range. Wrapping the angle value back into the range ensures that it remains within the desired range.

```js
let angle = 450;
let result = angle % 360;
console.log(result); // returns 90
```

In this example, the angle of `450` degrees is wrapped within the range of `0` to `360` degrees by using the modulo operator. It will return `90` which falls with the range.

## Wrapping Up!

In this article, you have learned how to use the modulo operator and seen various ways it works.

A modulo operator is a powerful tool for various mathematical operations in JavaScript. Understanding its use and applications can greatly simplify your code and make it more efficient.

You can access over 185 of my articles by [visiting my website](https://joelolawanle.com/contents). You can also use the search field to see if I've written a specific article.
