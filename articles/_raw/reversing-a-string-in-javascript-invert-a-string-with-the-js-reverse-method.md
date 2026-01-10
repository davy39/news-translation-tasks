---
title: Reversing a String in JavaScript – Invert a string with the JS .reverse() Method
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-07-07T17:01:57.000Z'
originalURL: https://freecodecamp.org/news/reversing-a-string-in-javascript-invert-a-string-with-the-js-reverse-method
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/cover-template--8-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Reversing strings in JavaScript is something you''ll need to do often on
  your web development journey. You might need to reverse a string during interviews,
  when solving algorithms, or when doing data manipulation.

  We will learn how to reverse a strin...'
---

Reversing strings in JavaScript is something you'll need to do often on your web development journey. You might need to reverse a string during interviews, when solving algorithms, or when doing data manipulation.

We will learn how to reverse a string in JavaScript using built-in JavaScript methods as well as the JavaScript `reverse()` method in this article.

For those in a rush, here is one line of code to help you reverse a string in JavaScript:

```bash
let myReversedString = myString.split("").reverse().join("");
```

Or you can use this:

```bash
let myReversedString = [...myString].reverse().join("");
```

Let’s now discuss these methods and the role they play in helping us reverse strings in JavaScript.

## How to Reverse a String With JavaScript Methods

Using JavaScript methods to reverse a string is simple. This is because we will use only three methods that perform different functions and are all used together to achieve this one common goal.

In general, we split the particular string into an array using either the spread operator or the `split()` method. Then we use the `reverse()` method, which can only be used to reverse elements in an array. And finally, we join this array together as a string using the `join()` method.

Let's try each of these methods separately.

### How to Split a String in JavaScript

There are two major methods of splitting a string in JavaScript: using the spread operator or the `split()` method.

#### How to Split String With the split() Method

The `split()` method is a very powerful method which you use to break a string into an ordered list of substrings based on a given pattern.

For example, if we have a sting of months separated by commas that we want to split up into an array of months, we could have something like this:

```bash
const months_string = 'Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec';

console.log(months_string.split(','))
```

This will output the following array:

```bash
["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
```

In our case our string might be a regular string with nothing separating each character. Then all we have to do is pass an empty string with no spaces, as seen below:

```bash
let myString = "Hello World";

console.log(myString.split("")); // ["H","e","l","l","o"," ","W","o","r","l","d"]
console.log(myString.split(" ")); // ["Hello","World"]
```

#### How to Split String with the Spread Operator

The spread operator is an ES6 addition that makes it easy to split up a string into an array. It does way more than just splitting a string:

```bash
let myString = "Hello World";

console.log([...myString]); // ["H","e","l","l","o"," ","W","o","r","l","d"]
```

### How to Reverse an Array of Strings with the `reverse()` Method

So far, we've learned how to split a string. And the `split()` method, of course, divides the string into an array. And now you can apply the reverse array method to it, as shown below:

```bash
let myString = "Hello World";

let splitString1 = myString.split("");
let splitString2 = myString.split(" ");

console.log(splitString1.reverse()); // ["d","l","r","o","W"," ","o","l","l","e","H"]
console.log(splitString2.reverse()); // ["World","Hello"]
```

We can also apply this to the spread operator this way, but we will no loner be able to define how we want to split our string:

```bash
let myString = "Hello World";

console.log([...myString].reverse()); // ["d","l","r","o","W"," ","o","l","l","e","H"]
```

### How to Join an Array of Strings Together with the `join()` Method

This is another powerful method that works in the opposite direction of the `split()` method. It creates a new string by concatenating all the elements in an array that are separated by commas or any other string specified as a separator.

For example, if we have an array of strings that we want to join into a single string separated by a dash (-), we can do something like this:

```js
let monthArray = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
console.log(monthArray.join("-"));
```

And this will return the following:

```bash
"Jan-Feb-Mar-Apr-May-Jun-Jul-Aug-Sep-Oct-Nov-Dec"
```

In our case, we have already reversed the string, and we don’t want anything in between. This means that we will just pass an empty string this way:

```bash
let myString = "Hello World";

let splitString1 = myString.split("");
let splitString2 = myString.split(" ");

let reversedStringArray1 = splitString1.reverse();
let reversedStringArray2 = splitString2.reverse();

console.log(reversedStringArray1.join("")); // "dlroW olleH"
console.log(reversedStringArray2.join("")); // "WorldHello"
```

At the end, we can perform all these operations with just one line of code by bringing all the methods together in the proper order:

```bash
let myString = "Hello World";

let myReversedString = myString.split("").reverse().join("");

console.log(myReversedString); // "dlroW olleH"
```

And the same applies to the spread operator:

```js
let myString = "Hello World";

let myReversedString = [...myString].reverse().join("");

console.log(myReversedString); // "dlroW olleH"
```

## Conclusion

In this tutorial, we learned how to reverse a string using the `reverse()` method, as well as other JavaScript methods. We also saw how the methods work with examples.

Have fun coding!
