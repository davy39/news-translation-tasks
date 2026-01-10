---
title: JavaScript Replace – How to Replace a String or Substring in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-02-28T02:24:34.000Z'
originalURL: https://freecodecamp.org/news/javascript-replace-how-to-replace-a-string-or-substring-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/cover-template--3-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When working with JavaScript, you might need to replace a string or substring
  with a new one.

  For example, you might want to replace a certain string (like "color” — American
  English) or substring in a larger text or document with a different string ...'
---

When working with JavaScript, you might need to replace a string or substring with a new one.

For example, you might want to replace a certain string (like "color” — American English) or substring in a larger text or document with a different string (“colour” — British English). You may also want to replace certain characters or symbols from a string to make sure your program will work.

In this article, you will learn how to use JavaScript's `replace()` method to replace a string or substring.

## How to Replace a String or Substring with the `replace()` Method

In JavaScript, you can use the `replace()` method to replace a string or substring in a string. The `replace()` method returns a new string with the replacement. The `replace()` method takes two arguments:

1. The first argument is the string or regular expression to be replaced.
    
2. The second argument is the string that will replace the matched string or regular expression.
    

```js
// Syntax
string.replace(searchValue, replaceValue)
```

In the syntax above, `string` is the string you want to perform the replacement on. The `searchValue` parameter is either a string or a regular expression that you want to search for in the `string`. The `replaceValue` parameter is the string that will replace the `searchValue`.

**Note:** Only the first instance will be replaced. If you want to replace all instances, you will have to use the `replaceAll()` method.

## JavaScript String `replace()` Examples

Suppose you have a string that uses “color” which is America English and want to change “color” to “colour”, the British English form. Here is an example of how you can do this:

```js
let originalString = "The color of the sky changes throughout the day.";

let newString = originalString.replace("color", "colour");

console.log(newString);
```

This will replace “color” in the string and return a new string assigned to the variable `newString`.

```bash
"The colour of the sky changes throughout the day."
```

In a situation where you have more than one occurence of such substring, you can use the replaceAll method:

```js
let originalString = "The color of the sky changes throughout the day, and sometimes the color of the clouds creates a beautiful contrast. The color of a flower can indicate its species, and the color of clothing can affect someone's mood.";

let newString = originalString.replaceAll("color", "colour");

console.log(newString);
```

This will replace all instances of “color” in the string and return a new string assigned to the variable `newString`.

```bash
"The colour of the sky changes throughout the day, and sometimes the colour of the clouds creates a beautiful contrast. The colour of a flower can indicate its species, and the colour of clothing can affect someone's mood."
```

## How to Replace Multiple Strings and Substring with the `replace()` Method

Sometimes you may want to change more than one string or substring in one string variable. For example, in the text below, you may want to change “color” to “colour” and “JS” to “JavaScript”.

```js
let originalString = "Using JS, you can change the color of a webpage's background, text, and elements."
```

You can do that by chaining as many `replace()` methods as needed:

```js
let originalString = "Using JS, you can change the color of a webpage's background, text, and elements.";

let newString = originalString
    .replace("color", "colour")
    .replace("JS", "JavaScript");

console.log(newString);
```

This will return a new string with both instances replaced:

```js
"Using JavaScript, you can change the colour of a webpage's background, text, and elements."
```

Also, you may want to replace multiple strings or substrings with just one string. For example, you may want to replace where “quick”, “fox”, and “brown” with one string — “hello”:

```js
let originalString = "The quick brown fox jumps over the lazy dog.";
let newString = originalString.replace(/quick|brown|fox/g, "hello");

console.log(newString); // Output: "The hello hello hello jumps over the lazy dog."
```

## How to Use `replace()` with Regular Expressions

In JavaScript, you can use the `replace()` method with regular expressions to replace strings and substrings with more flexibility and power. For example:

```js
let originalString = "Today is a sunny day. I love sunny days!";
let newString = originalString.replace(/sunny/g, "cloudy");

console.log(newString); // Output: "Today is a cloudy day. I love cloudy days!"
```

In this example, the regular expression `/sunny/g` matches all occurrences of the substring "sunny" in the `originalString`. The `g` flag specifies that all matches should be replaced. The replacement string "cloudy" replaces all matched substrings, resulting in the `newString` "Today is a cloudy day. I love cloudy days!"

Regular expressions can also be used to match patterns or groups of characters. For example:

```js
let originalString = "My phone number is (123) 456-7890";
let newString = originalString.replace(/\D/g, "");

console.log(newString); // Output: "1234567890"
```

In this example above, the regular expression `/\D/g` matches all non-digit characters in the `originalString`. The `\D` character class matches any character that is not a digit. The `g` flag specifies that all matches should be replaced.

## Case-sensitive Replacement with Regular Expressions

Regular expressions make it possible for you to perform advanced search and replace operations. For example, using the `i` flag, you can replace only strings and substrings whose case matches perfectly:

```js
const originalString = "I love JavaScript and javascript loves me";
const newString = originalString.replace(/JavaScript/i, "Python");

console.log(newString); // Output: "I love Python and javascript loves me"
```

In this example, the `replace()` method replaces the first occurrence of the word "JavaScript" with "Python" in the `originalString` variable. The `/i` flag is used to perform a case-insensitive search.

## Wrapping Up

In this article, you have learned how to replace a string or substring in JavaScript with the `replace()` method and the various instances in which the `replace()` method can work.

Hopefully, this article has given you a better understanding of how to use the `replace()` and `replaceAll()` method in JavaScript.

Have fun coding!

You can access over 188 of my articles by [visiting my website](https://joelolawanle.com/contents). You can also use the search field to see if I've written a specific article.
