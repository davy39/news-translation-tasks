---
title: What is a String in JS? The JavaScript String Variable Explained
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-02-03T19:26:12.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-string-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/cover-template--1-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When learning JavaScript or any programming language, you''ll encounter
  the keyword or term string.

  A string represents textual data, which is a fundamental part of many applications.
  You can also use strings to interact with users through prompts, al...'
---

When learning JavaScript or any programming language, you'll encounter the keyword or term string.

A string represents textual data, which is a fundamental part of many applications. You can also use strings to interact with users through prompts, alerts, and other forms of user input and output.

In this article, you will learn what a string is, how it works in JavaScript, how to create a string, and how to escape quotes and apostrophes in strings.

## What is a String in JavaScript?

In JavaScript, a string is a data type representing a sequence of characters that may consist of letters, numbers, symbols, words, or sentences.

We use strings to represent text-based data and we define them using either single quotes (`'`), double quotes (`"`), or backticks (\`\`):

```js
let name1 = 'John Doe';
let name2 = "John Doe";
let name3 = `John Doe`;
```

In the above example, you have three strings assigned to different variables. To be sure they are all strings, you can check the type of the variable:

```js
console.log(typeof(name1)); // string
console.log(typeof(name2)); // string
console.log(typeof(name3)); // string
```

It’s important to know that in JavaScript, strings are immutable. This means that once a string is created, its contents cannot be changed.

Instead, you must create a new string representing the modified version when you want to modify a string.

For example, if you have a string assigned to a variable, you cannot modify it. Instead, you will create a new string and assign the new string to the same variable like this:

```js
let name = "John Doe";
name = "Jane Doe";
```

This means that the original string `"John Doe"` still exists in memory, but the variable `name` now refers to the new string `"Jane Doe"`.

Strings in JavaScript can be transformed and processed in various ways, such as converting them to uppercase or lowercase, extracting substrings, searching for specific characters or sequences, and comparing strings to determine whether they are equal.

These capabilities make strings a versatile and powerful tool for developers. They have a number of built-in methods and properties that allow developers to manipulate and work with strings. Let’s explore some.

## String Concatenation in JavaScript

In JavaScript, string concatenation combines two or more strings into a single string with their variables. You can do this using the `+` operator, as seen in the example below:

```js
let firstName = "John";
let lastName = "Doe";
let fullName = firstName + " " + lastName;
console.log(fullName); // John Doe
```

In this example, you add an empty string (`" "`) in between to create space between both strings. Another way to concatenate strings in JavaScript is to use the `concat()` method, which is available on every string object. For example:

```js
let firstName = "John";
let lastName = "Doe";
let fullName = firstName.concat(" ", lastName);
console.log(fullName); // John Doe
```

## String Concatenation in JavaScript with Template Literals

In JavaScript, you can also use template literals for string concatenation. A template literal is a special type of string that you define using backticks (\`\`\`) instead of quotes (`'` or `"`).

Template literals can contain expressions evaluated (such as variables) and concatenated with the surrounding text, as seen in the example below:

```js
let firstName = "John";
let lastName = "Doe";
let fullName = `${firstName} ${lastName}`;
console.log(fullName); // John Doe
```

Template literals provide a concise and readable way to concatenate strings and insert expressions into strings. They also support line breaks and other special characters, making them a flexible tool for string manipulation in JavaScript.

## How to Escape Quotes and Apostrophes in Strings

In JavaScript, if you need to include a quote or apostrophe within a string, you must escape it using a backslash (`\`) because failure to do so will throw an error, as seen below:

```js
let quote = "He said, "I learned from freeCodeCamp!"";
```

This will throw the following error:

```js
Uncaught SyntaxError: Unexpected identifier 'I'
```

To fix this, you can use the opposite type of quote. For example, if your quote has a double quote, then wrap your string with a single quote and vice versa:

```js
let quote = 'He said, "I love JavaScript!"';
let apostrophe = "It's a beautiful day";
```

You can learn more about [how to escape strings in JavaScript in this article](https://www.freecodecamp.org/news/how-to-escape-strings-in-javascript/).

## How to Convert a String to Uppercase or Lowercase With JavaScript

In JavaScript, you can convert a string to uppercase or lowercase using the `toUpperCase()` and `toLowerCase()` methods, respectively. These methods return a new string with all the characters in uppercase or lowercase, as seen in the example below:

```js
let myString = "Welcome to freeCodeCamp!";
let upperCaseString = myString.toUpperCase();
let lowerCaseString = myString.toLowerCase();

console.log(upperCaseString); // "WELCOME TO FREECODECAMP!"
console.log(lowerCaseString); // "welcome to freecodecamp!"
```

Note that these methods do not modify the original string but instead return a new string with the desired case. The original string remains unchanged since strings are immutable.

## Wrapping up!

It is important for you to know that there is more to strings in JavScript, but this article is a basic introduction to strings, how they work, and how they can be used for simple operations.

You can explore [string methods](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Useful_string_methods) to know how to manipulate strings.

You can access over 180 of my articles by [visiting my website](https://joelolawanle.com/contents). You can also use the search field to see if I've written a specific article.
