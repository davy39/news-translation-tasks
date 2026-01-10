---
title: String to Number in JavaScript – Convert a String to an Int in JS
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-08-30T16:38:26.000Z'
originalURL: https://freecodecamp.org/news/string-to-number-in-javascript-convert-a-string-to-an-int-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-pixabay-459653.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "When you're programming, you'll often need to switch between data types.\
  \ For example, you may need to convert a string into a number. \nThe ability to\
  \ convert one data type to another gives you great flexibility when working with\
  \ information.\nJavaScri..."
---

When you're programming, you'll often need to switch between data types. For example, you may need to convert a string into a number. 

The ability to convert one data type to another gives you great flexibility when working with information.

JavaScript has different built-in methods to convert or cast a string into a number. 

In this article, you will learn some of the built-in JavaScript methods available for converting strings to numbers, along with an introduction (or refresher!) to the basics of how strings and numbers work in JavaScript.

Here is what we will cover:

1. [What is a string in JavaScript?](#string-js)
2. [What is a number in JavaScript?](#number-js)
3. [How to check the data type of a value in JavaScript?](#typeof)
4. [How to  convert a string into a number using the `parseInt()` function](#parseint)
5. [How to convert a string into a number using the `parseFloat()` function](#parsefloat)
6. [How to convert a string into a number using the `Number()` function](#Number)
7. [How to convert a string into a number using  `Math` functions](#math-functions)
8. [How to convert a string into a number by multiplying and diving by `1`](#multiplication)
9. [How to convert a string into a number by using the Unary `+` operator](#unary)

## What Is a String in JavaScript? <a name="string-js"></a>

Strings are an effective way of communicating through text, such as storing and manipulating text. They are one of the most fundamental data types in all programming languages. 

Strings in JavaScript are a primitive data type. This means that they are built into the language by default.

A string is an ordered sequence of zero or more character values. Specifically, it is a sequence of one or more characters that can be either letters, numbers, or symbols (such as punctuation marks).

Generally, you can tell if a data value is a string if it is enclosed in quotes, such as single or double quotes.

Specifically, there are three ways you can create a string in JavaScript:

- By using single quotes.
- By using double quotes.
- By using backticks.

Here is how to create a string using single quotes:

```js
// string created using single quotes ('')
let favePhrase = 'Hello World!';
```

Here is how to create a string using double quotes:

```js
// string created using double quotes ("")
let favePhrase = "Hello World!";
```

And here is how to create a string using backticks:

```js
// string created using backticks (``)
let favePhrase = `Hello World!`;
```

The last way of creating strings in JavaScript is also known as a template literal.

## What Is A Number in JavaScript? <a name="number-js"></a>

Numbers let you represent numerical values and perform mathematical operations and calculations.

Numbers in JavaScript are a primitive data type – just like strings.

Unlike other programming languages, you do not need to specify the type of number you want to create. For example, you do not need to mention whether the number will be an integer or a float.

In JavaScript, there are several different types of numbers (both positive and negative) built into the language:

- Integers.  An integer is a numerical value that does not include a decimal part -  also known as a round or whole number. 
- Floats. A float is a number with a decimal and at least one number following the decimal point.
- Exponential numbers are numbers that can be integers or floats and are followed by an `e`. The `e` indicates multiplying a number by `10` raised to a given power.
- Binary numbers (also known as base 2 numbers). Binary is a numerical system comprised of only two numbers: `0` and `1`. It uses 8 bits to represent one byte. The number begins with a `0` followed by a `b` followed by an 8-bit number.
- Octal numbers (also known as base 8 numbers). An octal number begins with a `0` followed by octal digits which range from `0 - 7`.  
- Hexadecimal numbers (also known as base 16 numbers). A hexadecimal number begins with a `0` followed by either an `x` or `X`. After that, there can be a combination of hexadecimal digits ranging from `0 - 9` and letters ranging from `A - F` (or `a - f`). The letters `A - F` are associated with the values `10 -15`.

```js
// integer
let num = 47;

// float
let num = 47.32;

// exponential - to represent large numbers
let num = 477e2;  // equal to multiplying 477 to 10 to the power of 2 (or 100) which results in 47700

// exponential - to represent small numbers
let num = 477e-2;  // equal to dividing 477 to 10 to the power of 2 (or 100) which results in 4.77

// binary
let num = 0b1111;    // stands for 15

// octal
let num = 023; // stands for 19

// hexadecimal
let num = 0xFF; // stands for 255
```

Something to be aware of is that numbers *shouldn't* be surrounded by quotes - that will automatically make them a string.

```js
// this is a string not a number!
let num = '7';
```

## How to Check the Data Type of a Value in JavaScript? <a name="typeof"></a>

To avoid any mistakes and double-check the data type of a value in JavaScript, use the `typeof` operator.

Earlier I mentioned that numbers enclosed in quotation marks are strings.

You can check that for yourself by doing the following:

```js
let num = '7';
console.log(typeof num)

// string
```

## How to Convert a String into a Number Using the `parseInt()` Function <a name="parseint"></a>

The general syntax for the `parseInt()` function is the following:

```js
parseInt(string, radix)
```

The `parseInt()` function takes two arguments: a string as the first argument and a radix as the second optional argument. 

The string is the value that needs to be converted into a number.

The radix specifies the mathematical number system you want to use and the base of the number that will be returned – whether the number will be a base 2 (or binary), base 8 (or octal), base 10 (decimal), or base 16 (or hexadecimal) number.

If the radix is not included, then it is `10` (decimal value) by default.

```js
let num = '7';

let strToNum = parseInt(num, 10);

console.log(strToNum);
console.log(typeof strToNum);

// 7
// number
```

What if the string contains letters and numbers? It will return only the numbers from the string:

```js
let num = '7 cats 7';

let strToNum = parseInt(num, 10);

console.log(strToNum);
console.log(typeof strToNum);

// 7
// number
```

When `parseInt()` encounters a non-numerical character, it ignores it and all the characters that come after that, even if there are more numbers down the line.

Something to keep in mind is that if the string does *not* start with a number, then `NaN` (which is short for `Not a Number`) will be returned instead.

```js
let num = 'h7';

let strToNum = parseInt(num, 10);

console.log(strToNum);

// NaN
```

The `parseInt()` function will start at position `0` of the string and determine whether the character at that position can be converted into a number. If it can't, the function returns `NaN` instead, even if the string contains numbers later on.

What if you have a string that contains a float? The `parseInt()` function will round it off and will return a whole number:

```js
let num = '7.77';

let strToNum = parseInt(num, 10);

console.log(strToNum);

// returns 7 instead of 7.77
```

If this is the case and you want to perform a literal conversion, it is best to use the `parseFloat()` function instead.

## How to Convert a String into a Number Using the `parseFloat()` Function <a name="parsefloat"></a>

The general syntax for the `parseFloat()` function is the following:

```js
parseFloat(string)
```

The syntax and behaviors of the `parseFloat()` function are similar to that of the `parseInt()` function. The main difference is that `parseFloat()` takes only one argument and doesn't accept a radix as an argument.

The `parseFloat()` function accepts a string as its only argument and returns a float – a number with a decimal point.

Use the `parseFloat()` function when you want to retain the decimal part and not just the integer part of a number.

Taking the same example from the previous section, here is how you would re-write it using `parseFloat()`:

```js
let num = '7.77';

let strToNum = parseFloat(num);

console.log(strToNum);

// 7.77
```

Just like `parseInt()`, the `parseFloat()` function will return only the first number and ignore any non-numerical characters:

```js
let num = '7.77 cats 7.77';

let strToNum = parseFloat(num);

console.log(strToNum);

// 7.77
```

And just like `parseInt()` again, if the first character is not a valid number, the `parseFloat()` function will return `NaN` instead of a number as it cannot convert it into a number:

```js
let num = 'h7.77';

let strToNum = parseFloat(num);

console.log(strToNum);

// NaN
```

## How to Convert a String into a Number Using the `Number()` Function <a name="Number"></a>

The general syntax for the `Number()` function is the following:

```js
Number(string)
```

The difference between the `Number()` function and the `parseInt()` and `parseFloat()` functions is the fact that the `Number()` function tries to convert the entire string into a number all at once. The parse methods convert a string to a number piece by piece, and they move through the characters that make up the string individually and one at a time.

Let's take the following example you saw earlier that used `parseInt()`:

```js
let num = '7 cats 7';

let strToNum = parseInt(num, 10);

console.log(strToNum);

// 7
```

The minute that `parseInt()` encounters a non-numerical character, it ends the conversion.

Here is how the same example works with the `Number()` function:

```js
let num = '7 cats 7';

let strToNum = Number(num);

console.log(strToNum);

// NaN
```

Since `Number()` attempts to convert and typecast the entire string into a number all at once, it returns `NaN` since it encounters non-numerical characters and is, therefore, unable to convert to a number.

The `Number()` function is a great choice when you want the conversion to fail if the string contains non-numerical characters.

Something else to note is that the `Number()` function does not return a whole number when it encounters a decimal number, in contrast to the `parseInt()` function you saw earlier. 

```js
let num = '7.77';

let strToNum = Number(num);

console.log(strToNum);

// 7.77
```

## How to Convert a String into a Number Using `Math` Functions <a name="math-functions"></a>

The `Math` object is a built-in JavaScript object. And you can use some of its methods, such as `Math.round()`,`Math.floor()`, and  `Math.ceil()`, to convert strings to numbers.

Something to be aware of and keep in mind when using the Math methods for type conversion is when you are working with floats, they will turn them into an integer, and the float will lose its decimal part. 

The methods will convert the string to the nearest integer equivalent.

The `Math.round()` function converts a string into a number and rounds it to the nearest whole number:

```js
let num = '7.5';

let strToNum = Math.round(num);

console.log(strToNum);

// 8
```

If the value of `num` is equal to `7.4`, I will get the following result:

```js
let num = '7.4';

let strToNum = Math.round(num);

console.log(strToNum);

// 7
```

If the string contains non-numerical characters, `Math.round()` returns `NaN`. 

```js
let num = '7.5a';

let strToNum = Math.round(num);

console.log(strToNum);

// NaN
```

The `Math.floor()` function converts a string into a number and rounds it *down* to the nearest whole number:

```js
let num = '7.87';

let strToNum = Math.floor(num);

console.log(strToNum);

// 7
```

If the string contains non-numerical characters, `Math.floor()` returns `NaN`. The way this function works is that it tries to convert the whole string into a number and then evaluate the result, meaning the string must be a valid string for it to work:

```js
let num = '7.87a';

let strToNum = Math.floor(num);

console.log(strToNum);

// NaN
```

The `Math.ceil()` function is the opposite of `Math.floor()` since it converts a string into a number and rounds it *up* to the nearest whole number:

```js
let num = '7.87';

let strToNum = Math.ceil(num);

console.log(strToNum);

// 8
```

Similarly to the previous examples, the `Math.ceil()` function will return `NaN` when it encounters a non-numerical value in the string:

```js
let num = '7.87a';

let strToNum = Math.ceil(num);

console.log(strToNum);

// NaN
```

## How to Convert a String into a Number by Multiplying and Dividing by `1` <a name="multiplication"></a>

Multiplying by `1` is one of the fastest ways of converting a string to a number:

```js
let convertStringToInt = "7" * 1;

console.log(convertStringToInt);
console.log(typeof convertStringToInt);

// 7
// number
```

And if you want to perform type conversion on a float, multiplying by `1` reserves the decimal place:

```js
let convertStringToInt = "7.1" * 1;

console.log(convertStringToInt);
console.log(typeof convertStringToInt);

// 7.1
// number
```

If the string contains non-numerical characters, it will return `NaN`:

```js
let convertStringToInt = "7a" * 1;

console.log(convertStringToInt);

// NaN
```

This way of converting strings to integers also works with dividing a string by `1`:

```js
let convertStringToInt = "7" / 1

console.log(convertStringToInt);
console.log(typeof(convertStringToInt));

// 7
// number
```

At this point, it is also worth mentioning what happens when you try to add `1` to a string to convert it into an integer. If you tried to do that, this is the result you would get:

```js
let convertStringToInt = "7" + 1;

console.log(convertStringToInt);
console.log(typeof convertStringToInt);

// 71
// string
```

In the example above, `1` was concatenated with the string `"7"`, meaning it was placed side by side with the string. 


## How to Convert a String into a Number by Using the Unary `+` Operator <a name="unary"></a>

Using the unary `+` operator is also one of the fastest ways of converting a string to a number.

You place the plus operator, `+`, before the string, and it converts the string to an integer:


```js
let convertStringToInt = +"7";

console.log(convertStringToInt);
console.log(typeof convertStringToInt);

// 7
// number
```

.. or a float:

```js
let convertStringToInt = +"7.77";

console.log(convertStringToInt);

// 7.77
```

Similar to the other ways you have seen for converting a string to a number, the entire string must contain only numerical characters for the unary `+` operator to work. If the string doesn't represent a number, then it will return `NaN`:

```js
let convertStringToInt = +"7a";

console.log(convertStringToInt);

// NaN
```


## Conclusion

And there you have it! You now know some of the ways you can convert a string to a number in JavaScript.

To learn more about JavaScript, head to freeCodeCamp's [JavaScript Algorithms and Data Structures Certification](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/).

It's a free, well-thought-out, and structured curriculum where you will learn interactively. In the end, you will also build 5 projects to claim your certification and solidify your knowledge.

Thanks for reading!


