---
title: JavaScript Number to String – How to Use toString to Convert an Int into a
  String
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-03-22T13:48:42.000Z'
originalURL: https://freecodecamp.org/news/javascript-number-to-string-how-to-use-tostring-to-convert-an-int-into-a-string
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/js-number-tostring.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'The toString() method is a built-in method of the JavaScript Number object
  that allows you to convert any number type value into its string type representation.

  How to Use the toString Method in JavaScript

  To use the toString() method, you simply nee...'
---

The `toString()` method is a built-in method of the JavaScript `Number` object that allows you to convert any `number` type value into its `string` type representation.

## How to Use the toString Method in JavaScript

To use the `toString()` method, you simply need to call the method on a `number` value. The following example shows how to convert the number value `24` into its string representation. Notice how the value of the `str` variable is enclosed in double quotation marks:

```js
var num = 24;
var str = num.toString();

console.log(num); // 24
console.log(str); // "24"
```

You can also call the `toString()` method immediately on a `number` value, but you need to add parentheses `()` to wrap the value or JavaScript will respond with an `Invalid or unexpected token` error.

The `toString()` method can also convert floating and negative numbers as shown below:

```js
24.toString(); // Error: Invalid or unexpected token
(24).toString(); // "24"
(9.7).toString(); // "9.7"
(-20).toString(); // "-20"
```

Finally, the `toString()` method also accepts the `radix` or `base` parameter. The `radix` allows you to convert a number from the decimal number system (base 10) to a string representing the number in other number systems.

Valid number systems for conversion include:

* Binary system (base 2) that has 2 digits, 0 and 1
* Ternary system (base 3) that has 3 digits 0, 1, and 2
* Quaternary system (base 4) that has 4 digits, 0, 1, 2 and 3
* And so on up to the Hexatridecimal system (base 36) that has the combination of Arabic numerals 0 to 9 and Latin letters A to Z

```js
Number.toString(radix);
```

The `radix` parameters accept a `number` type data with values ranging from `2` to `36`. Here's an example of converting the decimal number `5` to its binary number (base 2) representation:

```js
var str = (5).toString(2);

console.log(str); // "101"
```

The decimal number `5` from the code above is converted to its binary number equivalent of `101` and then converted to a string.

## How to Use Other Data Types with the toString() Method

Aside from converting the `number` type, the `toString()` method is also available for converting other data types into their string representations.

For example, you can convert an `array` type into its `string` representation as follows:

```js
var arr = [ "Nathan", "Jack" ];
var str = arr.toString();

console.log(str); // "Nathan,Jack"
```

Or a `boolean` type to `string` as shown below:

```js
var bool = true;
var str = bool.toString();

console.log(str); // "true"
```

But I think you will most often use the `toString()` method to convert a `number` to a `string` instead of the others. That's what I usually do, too :)

## **Thanks for reading this tutorial**

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!

