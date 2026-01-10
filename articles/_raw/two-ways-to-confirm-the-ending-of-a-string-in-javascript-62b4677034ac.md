---
title: Two ways to confirm the ending of a String in JavaScript
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2017-02-06T13:18:27.000Z'
originalURL: https://freecodecamp.org/news/two-ways-to-confirm-the-ending-of-a-string-in-javascript-62b4677034ac
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bvdSF4jzFsH7foKJYEoNaA.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'In this article, I’ll explain how to solve freeCodeCamp’s “Confirm the
  Ending” challenge. This involves checking whether a string ends with specific sequence
  of characters.

  There are the two approaches I’ll cover:


  using the substr() method

  using end...'
---

In this article, I’ll explain how to solve freeCodeCamp’s “[Confirm the Ending](https://www.freecodecamp.com/challenges/confirm-the-ending)_”_ challenge. This involves checking whether a string ends with specific sequence of characters.

There are the two approaches I’ll cover:

1. using the substr() method
2. using endsWith() method

### The Algorithm Challenge Description

> _Check if a string (first argument, `str`) ends with the given target string (second argument, `target`)._  
>   
> _This challenge can be solved with the `.endsWith()` method, which was introduced in ES2015. But for the purpose of this challenge, we would like you to use one of the JavaScript substring methods instead._

```js
function confirmEnding(string, target) {
  return string;
}
confirmEnding("Bastian", "n");
```

### Provided test cases

```js
confirmEnding("Bastian", "n") should return true.

confirmEnding("Connor", "n") should return false.

confirmEnding("Walking on water and developing software from a specification are easy if both are frozen", "specification") should return false.

largestOfFour([[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]]) should return [9, 35, 97, 1000000].

confirmEnding("He has to give me a new name", "name")should return true.
confirmEnding("Open sesame", "same") should return true.

confirmEnding("Open sesame", "pen") should return false.

confirmEnding("If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing", "mountain") should return false.

Do not use the built-in method .endsWith() to solve the challenge.
```

### Approach #1: Confirm the Ending of a String With Built-In Functions — with substr()

For this solution, you’ll use the String.prototype.substr() method:

* The `**substr()**` method returns the characters in a string beginning at the specified location through the specified number of characters.

Why are you using `string.substr(-target.length)`?

If the target.length is negative, the substr() method will start the counting from the end of the string, which is what you want in this code challenge.

You don’t want to use `string.substr(-1)` to get the last element of the string, because if the target is longer than one letter:

```
confirmEnding("Open sesame", "same")
```

…the target won’t return at all.

So here `string.substr(-target.length)` will get the last index of the string ‘Bastian’ which is ‘n’.

Then you check whether `string.substr(-target.length)` equals the target (true or false).

```js

function confirmEnding(string, target) {
  // Step 1. Use the substr method
  if (string.substr(-target.length) === target) {
  
  // What does "if (string.substr(-target.length) === target)" represents?
  // The string is 'Bastian' and the target is 'n' 
  // target.length = 1 so -target.length = -1
  // if ('Bastian'.substr(-1) === 'n')
  // if ('n' === 'n')
  
  // Step 2. Return a boolean (true or false)
    return true;
  } else {
    return false;
  }
}

confirmEnding('Bastian', 'n');
```

Without comments:

```js

function confirmEnding(string, target) {
  if (string.substr(-target.length) === target) {
    return true;
  } else {
    return false;
  }
}
confirmEnding('Bastian', 'n');
```

You can use a **ternary operator** as a shortcut for the if statement:

```
(string.substr(-target.length) === target) ? true : false;
```

This can be read as:

```
if (string.substr(-target.length) === target) {
    return true;
} else {
    return false;
}
```

You then return the ternary operator in your function:

```js

function confirmEnding(string, target) {
  return (string.substr(-target.length) === target) ? true : false;
}
confirmEnding('Bastian', 'n');
```

You can also refactor your code to make it more succinct by just returning the condition:

```js
function confirmEnding(string, target) {
  return string.substr(-target.length) === target;
}
confirmEnding('Bastian', 'n');
```

### Approach #2: Confirm the Ending of a String With Built-In Functions — with endsWith()

For this solution, you’ll use the String.prototype.endsWith() method:

* The `endsWith()` method determines whether a string ends with the characters of another string, returning `true` or `false` as appropriate. This method is case-sensitive.

```js
function confirmEnding(string, target) {
  // We return the method with the target as a parameter
  // The result will be a boolean (true/false)
  return string.endsWith(target); // 'Bastian'.endsWith('n')
}
confirmEnding('Bastian', 'n');
```

I hope you found this helpful. This is part of my “How to Solve FCC Algorithms” series of articles on the freeCodeCamp Algorithm Challenges, where I propose several solutions and explain step-by-step what happens under the hood.

[**Three ways to repeat a string in JavaScript**  
_In this article, I’ll explain how to solve freeCodeCamp’s “Repeat a string repeat a string” challenge. This involves…_](https://www.freecodecamp.org/news/three-ways-to-repeat-a-string-in-javascript-2a9053b93a2d/)

[**Three Ways to Reverse a String in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Reverse a String”_](https://www.freecodecamp.org/news/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb/)

[**Three Ways to Factorialize a Number in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Factorialize a Number”_](https://www.freecodecamp.org/news/how-to-factorialize-a-number-in-javascript-9263c89a4b38/)

[**Two Ways to Check for Palindromes in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Check for Palindromes”._](https://www.freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7/)

[**Three Ways to Find the Longest Word in a String in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Find the Longest Word in a String”._](https://www.freecodecamp.org/news/three-ways-to-find-the-longest-word-in-a-string-in-javascript-a2fb04c9757c/)

[**Three Ways to Title Case a Sentence in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Title Case a Sentence”._](https://www.freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27/)

If you have your own solution or any suggestions, share them below in the comments.

Or you can follow me on [**Medium**](https://medium.com/@sonya.moisset)**, [Twitter](https://twitter.com/SonyaMoisset), [Github](https://github.com/SonyaMoisset)** and [**LinkedIn**](https://www.linkedin.com/in/sonyamoisset), right after you click the green heart below ;-)

‪#‎StayCurious‬, ‪#‎KeepOnHacking‬ & ‪#‎MakeItHappen‬!

### Additional Resources

* [substr() method — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substr)
* [endsWith() method — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith)
* [Ternary Operator — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)

