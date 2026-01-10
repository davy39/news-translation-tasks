---
title: JavaScript Replace – How to Use the String.prototype.replace() Method JS Example
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-02-08T21:26:21.000Z'
originalURL: https://freecodecamp.org/news/javascript-replace-how-to-use-the-string-prototype-replace-method-js-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/replace.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'The String.prototype.replace() method searches for the first occurrence
  of a string and replaces it with the specified string. It does this without mutating
  the original string.

  This method works for regular expressions, too, so the item you''re searc...'
---

The ` String.prototype.replace() ` method searches for the first occurrence of a string and replaces it with the specified string. It does this without mutating the original string.

This method works for regular expressions, too, so the item you're searching for may be expressed as a regular expression. 

The value to return as the replaced value may be expressed as a string or function.

## Basic Syntax of the String.prototype.replace() Method

```js
const variable = variable.replace("stringToReplace", "expectedString");
```

You use the `replace()` method by: 
- assigning the initial string or strings to a variable
- declaring another variable
- for the value of the new variable, prepending the new variable name with the replace() method 
- Comma-separating the string you want to replace and the expected string in the brackets

## Examples of the String.prototype.replace() Method

A basic example would look like this:

```js
const coding = "I learned how to code from TV";
const replacedString = coding.replace("TV", "freeCodeCamp");

console.log(replacedString); // Result: I learned how to code from freeCodeCamp
```

In the example above:
- I declared a variable named coding and assigned it the string “`I learned how to code from TV`”
- I declared another variable named `replacedString` 
- For the value of the `replacedString` variable, I brought in the `replace()` method and specified that I wanted to replace “TV” from the initial variable with “freeCodeCamp”.

Below is an example demonstrating that the initial string is never mutated (changed) by the `replace()` method:

```js
const coding = "I learned how to code from TV";
const replacedString = coding.replace("TV", "freeCodeCamp");

console.log(replacedString); // Result: I learned how to code from freeCodeCamp
console.log(coding); // Result: I learned how to code from TV
```

In the example below, I used regular expressions to search for the text that matches “TV” and replaced it with “freeCodeCamp”:

```js
const coding = "I learned how to code from TV";
const replacedString = coding.replace(/TV/, "freeCodeCamp");

console.log(replacedString); // Result: I learned how to code from freeCodeCamp
```

Since the `replace()` method works for the first occurrence of some text in a string only, what do you do if you want to replace all occurrences of a word with another word in a string? You can use the `replaceAll()` method.

## How to Use the `replaceAll()` Method

A string method that is slightly similar to the `replace()` method is the `replaceAll()` method.

This method replaces all occurrences of a certain word in a string.

### Example of the `replaceAll()` Method

```js
const coding = "I learned how to code from TV. TV remains in my heart for life.";
const replacedString = coding.replaceAll("TV", "freeCodeCamp");

console.log(replacedString); // Result: I learned how to code from freeCodeCamp. freeCodeCamp remains in my heart for life.
```

Every occurrence of “TV” has been replaced with “freeCodeCamp” courtesy of the `replaceAll()` method.

With the original `replace()` method, you can achieve what `replaceAll()` does by using regular expressions to search for every occurrence of a certain word in a string and replacing it with another word.

```js
const coding = "I learned how to code from TV. TV remains in my heart for life.";
const replacedString = coding.replace(/TV/g, "freeCodeCamp");

console.log(replacedString); // Result: I learned how to code from freeCodeCamp. freeCodeCamp remains in my heart for life.
```

I was able to search for every word that matches “TV” with the `g` flag of a regular expression and replace it with “freeCodeCamp”.

## How to Pass a Function to the `replace()` Method

As I said before, you can express the value you want to return as the replaced value as a function.

In the example below, I converted the title of this article to a URL slug with the replace method:

```js
const articleTitle = "JavaScript Replace – How to Use the String.prototype.replace() Method";
const slugifyArticleTitle = articleTitle.toLowerCase().replace(/ /g, function (article) {
    return article.split(" ").join("-");
  });

console.log(slugifyArticleTitle); //Result: javascript-replace-–-how-to-use-the-string.prototype.replace()-method
```

In the script above:
- I declared a variable named `articleTitle` and assigned the title of this article
- I declared another variable named `slugifyArticleTitle` and converted the title of the article to lowercase letters with the `toLowerCase()` method
- I brought in the `replace()` method and searched for every white space with `/ /g`
- I then passed a function to the `replace()` method, and assigned it a parameter of `article`. This parameter refers to the string (title of the article) converted to lowercase letters
- Inside the function, I returned that I’m splitting the article title anywhere there is a white space. This was done with the `split()` method. 
- After splitting the article title everywhere there is whitespace, I used the `join()` method to join the individual letters in the string with a hyphen.

## Conclusion

The `String.prototype.replace()` method is a powerful string method with which you can get a lot of things done while working with strings in JavaScript.

Apart from the `String.prototype.replace()` method, I also showed you how to use the `String.prototype.replaceAll()` method – a hybrid of `String.prototype.replace()` method.

You should be careful with the `String.prototype.replaceAll()` method because it’s not yet supported by some browsers. Instead of using `replaceAll()`, I also showed you how you can achieve the same thing it does by using regular expressions to search for all values in a particular string.

If you find this article helpful, don’t hesitate to share it with your friends and family.

Thank you for reading.


