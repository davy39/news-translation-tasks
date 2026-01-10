---
title: JavaScript Convert String to Number – JS String to Int Example
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-06-29T00:04:12.000Z'
originalURL: https://freecodecamp.org/news/javascript-convert-string-to-number-js-string-to-int-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/cover-template--5-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When you''re working with data from various sources, some of these data
  may arrive in the incorrect format. And you''ll need to correct those formats before
  performing certain actions on the data.

  This is just one of the many reasons you might want to ...'
---

When you're working with data from various sources, some of these data may arrive in the incorrect format. And you'll need to correct those formats before performing certain actions on the data.

This is just one of the many reasons you might want to learn how to convert a string to a number in JavaScript.

In this article, we will learn how to convert string to number by going through the various methods and providing examples for each.

Before we begin, a common way to distinguish a string value is that it is always enclosed in either a single or double quote, whereas a number is not:

```js
"John Doe" -> String
'John Doe' -> String
"12" -> String
12 -> Number
```

Suppose we have our string stored in a variable. A good way to check if a variable is a string is by using the `typeof` operator:

```js
let name = "John Doe";

console.log(typeof name) // "string"
```

Let’s now learn how to convert a string to a number.

## How to Convert a String to a Number Using the `Number()` Function

The Number function is a powerful method that you can use to convert strings or other values to the Number type. This method will also return `NaN` if the value can't be converted:

```js
console.log(Number('212'))  // 212
console.log(Number("2124"))  // 2124
console.log(Number('0.0314E+2')); // 3.14

console.log(Number("Hello World"))  // NaN
console.log(Number(undefined))  // NaN
```

This also works with variables:

```js
let age = "12";
let password = "John12";

console.log(Number(age)) // 12
console.log(Number(password)) // NaN
```

This is one of the easiest methods to use as it also works with decimal values and returns the values without manipulating them:

```js
let answer = "12.0";
let answer = "12.0267";

console.log(Number(answer)) // 12.0
console.log(Number(answer)) // 12.0267
```

## How to Convert a String to a Number Using the `parseInt()` and `parseFloat()` Functions

Both the `parseInt()` and `parseFloat()` functions takes in a string as a parameter, and then convert that string to an integer/number.

You can also use `parseInt()` for converting a non-integer number to an integer, while `parseFloat()` is the more powerful method as it can maintain floats and some mathematical logic:

```js
console.log(parseInt('12')) // 12
console.log(parseInt('12.092')) // 12.092
console.log(parseInt('  3.14  ')) // 3
console.log(parseInt('0.0314E+2')) // 0
console.log(parseInt('John Doe')) // NaN

console.log(parseFloat('12')) // 12
console.log(parseFloat('12.092')) // 12.092
console.log(parseFloat('  3.14  ')) // 3.14
console.log(parseFloat('0.0314E+2')) // 3.14
console.log(parseFloat('John Doe')) // NaN
```

As usual this also works with variables:

```js
let age = "12";

console.log(parseInt(age)) // 12
console.log(parseFloat(age)) // 12
```

Note: The `parseFloat()` function will always return NaN when the character of the string cannot be converted to number:

```js
console.log(parseFloat('N0.0314E+2')) // NaN
```

## How to Convert a String to a Number Using the Unary Plus Operator (`+`)

The is one of the fastest and easiest ways to convert something into a number. I said “something” because it converts far more than just string representations of numbers and floats – it also works on the non-string values `true`, `false`, and `null` or an empty string.

One advantage (or also disadvantage) of this method is that it does not perform any other operations on the number like rounding up or converting it to an integer.

Let’s take a look at some examples:

```js
console.log(+'100'); // 100
console.log(+'100.0373'); // 100.0373
console.log(+''); // 0
console.log(+null); // 0
console.log(+true); // 1
console.log(+false); // 0
console.log(+'John Doe'); // NaN
console.log(+'0.0314E+2'); // 3.14
```

As expected this also works with variables:

```js
let age = "74";

console.log(+age); // 74
```

If you compare `ParseInt()` and the plus Unary Operator, you might end up using the plus Unary Operator over the `parseInt()` method in some situations.

For example, let's say you're getting random values – let’s say a UUID value which at some point might start with numbers and at other points can start with letters. This means using the `parseInt()` function might sometime return `NaN` and other times return the first characters that are numbers:

```js
console.log(parseInt("cb34d-234ks-2343f-00xj")); // NaN
console.log(parseInt("997da-00xj-2343f-234ks")); // 997


console.log(+"cb34d-234ks-2343f-00xj"); // NaN
console.log(+"997da-00xj-2343f-234ks"); // NaN
```

## How to Convert a String to a Number Using JavaScript Math Methods

Another way to convert strings to number is by using some JavScript math methods.

You can use the `floor()` method, which will round down the passed value to the nearest integer. The `ceil()` method, which is the opposite of `floor()`, rounds up to the nearest integer. Lastly the `round()` method, which is between both, just rounds the number to the nearest integer (either up or down depending on the closeness).

### How to Convert a String to a Number Using the `Math.floor()` JavaScript Method

Just like I explained above, this will always return an integer. Suppose we pass a float value – it will round down the value to the nearest integer. This will return `NaN` if we pass letters as a string or any other non-integer character:

```js
console.log(Math.floor("14.5")); // 14
console.log(Math.floor("654.508")); // 654
console.log(Math.floor("0.0314E+2")); // 3
console.log(Math.floor("34d-234ks")); // NaN
console.log(Math.floor("cb34d-234ks-2343f-00xj")); // NaN
```

### How to Convert a String to a Number Using the `Math.ceil()` JavaScript Method

This is quite similar and will only round up our float values to always return a whole number:

```js
console.log(Math.ceil("14.5")); // 15
console.log(Math.ceil("654.508")); // 655
console.log(Math.ceil("0.0314E+2")); // 3
console.log(Math.ceil("34d-234ks")); // NaN
```

### How to Convert a String to a Number Using the `Math.round()` JavaScript Method

This works like both methods but just returns the whole number after rounding up to the nearest integer:

```js
console.log(Math.round("14.5")); // 15
console.log(Math.round("654.508")); // 655
console.log(Math.round("0.0314E+2")); // 3
console.log(Math.round("34d-234ks")); // NaN
```

All the above Math methods also work with variables:

```js
let age = "14.5";

console.log(Math.floor(age)); // 14
console.log(Math.ceil(age)); // 15
console.log(Math.round(age)); // 15
```

## How to Convert a String to a Number Using some Mathematical Operations

This isn't really a method, but it's worth knowing. So far, we've discussed direct methods for achieving this conversion – but in some cases, you might just want to perform these mathematical operations to help with the conversion.

These includes multiplication by `1`, division by `1` and also subtraction by `0`. When we perform any of these operations on a string, they will be converted to integers:

```js
console.log("14.5" / 1); // 14.5
console.log("0.0314E+2" / 1); // 3.14

console.log("14.5" * 1); // 14.5
console.log("0.0314E+2" * 1); // 3.14

console.log("14.5" - 0); // 14.5
console.log("0.0314E+2" - 0); // 3.14
```

As usual this also works with variables:

```js
let age = "14.5";

console.log(age / 1); // 14.5
console.log(age * 1); // 14.5
console.log(age - 0); // 14.5
```

## Conclusion

In this article, we looked at various methods and approaches for converting strings to integers in JavaScript.

It is best to be aware that many methods exist so that you can choose what works best for you and apply it in any situation.
