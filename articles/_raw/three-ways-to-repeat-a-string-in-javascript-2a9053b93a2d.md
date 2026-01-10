---
title: Three ways to repeat a string in JavaScript
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2017-02-13T19:45:18.000Z'
originalURL: https://freecodecamp.org/news/three-ways-to-repeat-a-string-in-javascript-2a9053b93a2d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5xZaBnyrMAe9JkgajD3NbA.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'In this article, I’ll explain how to solve freeCodeCamp’s “Repeat a string
  repeat a string” challenge. This involves repeating a string a certain number of
  times.

  There are the three approaches I’ll cover:


  using a while loop

  using recursion

  using ES...'
---

In this article, I’ll explain how to solve freeCodeCamp’s “[Repeat a string repeat a string](https://www.freecodecamp.com/challenges/repeat-a-string-repeat-a-string)_”_ challenge. This involves repeating a string a certain number of times.

There are the three approaches I’ll cover:

1. using a while loop
2. using recursion
3. using ES6 repeat() method

### The Algorithm Challenge Description

> _Repeat a given string (first argument) `num` times (second argument). Return an empty string if `num` is not a positive number._

```js
function repeatStringNumTimes(str, num) {
  return str;
}
repeatStringNumTimes("abc", 3);
```

### Provided test cases

```js
repeatStringNumTimes("*", 3) should return "***".

repeatStringNumTimes("abc", 3) should return "abcabcabc".

repeatStringNumTimes("abc", 4) should return "abcabcabcabc".

repeatStringNumTimes("abc", 1) should return "abc".

repeatStringNumTimes("*", 8) should return "********".

repeatStringNumTimes("abc", -2) should return "".
```

### Approach #1: Repeat a String with a While Loop

A while statement executes its statement as long as a specified condition evaluates to true.

A while statement looks like this:

```js
while (condition)
  statement
```

with a condition which is evaluated before each pass through the loop. If the condition is true, the statement is executed. If the condition is false, the execution continues with any statement after the while loop.

The statement is executed as long as the condition is true. Here’s the solution:

```js

function repeatStringNumTimes(string, times) {
  // Step 1. Create an empty string that will host the repeated string
  var repeatedString = "";

  // Step 2. Set the While loop with (times > 0) as the condition to check
  while (times > 0) { // As long as times is greater than 0, the statement is executed
    // The statement
    repeatedString += string; // Same as repeatedString = repeatedString + string;
    times--; // Same as times = times - 1;
  }
  /* While loop logic
                      Condition       T/F       repeatedString += string      repeatedString        times
    First iteration    (3 > 0)        true            "" + "abc"                  "abc"               2
    Second iteration   (2 > 0)        true           "abc" + "abc"               "abcabc"             1
    Third iteration    (1 > 0)        true          "abcabc" + "abc"            "abcabcabc"           0
    Fourth iteration   (0 > 0)        false
    }
  */
  
  // Step 3. Return the repeated string
  return repeatedString; // "abcabcabc"
}

repeatStringNumTimes("abc", 3);
```

And again, without comments:

```js
function repeatStringNumTimes(string, times) {
  var repeatedString = "";
  while (times > 0) {
    repeatedString += string;
    times--;
  }
  return repeatedString;
}
repeatStringNumTimes("abc", 3);
```

### Approach #2: Repeat a String using a Conditional and Recursion

Recursion is a technique for iterating over an operation by having a function call itself repeatedly until it arrives at a result. There are a few key features of recursion that must be included in order for it to work properly.

* The first is a **_base case_**: this is a statement, usually within a conditional clause like `if`, that stops the recursion.
* The second is a **_recursive case_**: this is the statement where the recursive function is called on itself.

Here’s the solution:

```js
function repeatStringNumTimes(string, times) {
  // Step 1. Check if times is negative and return an empty string if true
  if (times < 0) {
    return "";
  }
  
  // Step 2. Check if times equals to 1 and return the string itself if it's the case.
  if (times === 1) {
    return string;
  }
  
  // Step 3. Use recursion
  else {
    return string + repeatStringNumTimes(string, times - 1); // return "abcabcabc";
  }
  /* 
    First Part of the recursion method
    You need to remember that you won’t have just one call, you’ll have several nested calls
                     times       string + repeatStringNumTimes(string, times - 1)
      1st call         3                 "abc" + ("abc", 3 - 1)
      2nd call         2                 "abc" + ("abc", 2 - 1)
      3rd call         1                 "abc" => if (times === 1) return string;
      4th call         0                  ""   => if (times <= 0) return "";
    Second part of the recursion method
      4th call will return      ""
      3rd call will return     "abc"
      2nd call will return     "abc"
      1st call will return     "abc"
    The final call is a concatenation of all the strings
    return "abc" + "abc" + "abc"; // return "abcabcabc";
  */
}
repeatStringNumTimes("abc", 3);
```

And again, without comments:

```js
function repeatStringNumTimes(string, times) {
  if(times < 0) 
    return "";
  if(times === 1) 
    return string;
  else 
    return string + repeatStringNumTimes(string, times - 1);
}
repeatStringNumTimes("abc", 3);
```

### Approach #3: Repeat a String using ES6 repeat() method

For this solution, you’ll use the String.prototype.repeat() method:

* The `**repeat()**` method constructs and returns a new string which contains the specified number of copies of the string on which it was called, concatenated together.

Here’s the solution:

```js

function repeatStringNumTimes(string, times) {
  //Step 1. If times is positive, return the repeated string
  if (times > 0) { // (3 > 0) => true
    return string.repeat(times); // return "abc".repeat(3); => return "abcabcabc";
  }
  
  //Step 2. Else if times is negative, return an empty string if true
  else {
    return "";
  }
}

repeatStringNumTimes("abc", 3);
```

And again, without comments:

```js
function repeatStringNumTimes(string, times) {
  if (times > 0)
    return string.repeat(times);
  else
    return "";
}
repeatStringNumTimes("abc", 3);
```

You can use a **ternary operator** as a shortcut for the if/else statement, like this:

```js
times > 0 ? string.repeat(times) : "";
```

This can be read as:

```js
if (times > 0) {    
    return string.repeat(times);
} else {
    return "";
}
```

You can then return the ternary operator in your function:

I hope you found this helpful. This is part of my “How to Solve FCC Algorithms” series of articles on the freeCodeCamp Algorithm Challenges, where I propose several solutions and explain step-by-step what happens under the hood.

[**Two ways to confirm the ending of a String in JavaScript**](https://medium.freecodecamp.com/two-ways-to-confirm-the-ending-of-a-string-in-javascript-62b4677034ac)  
_[In this article, I’ll explain how to solve freeCodeCamp’s “Confirm the Ending” challenge.](https://www.freecodecamp.org/news/two-ways-to-confirm-the-ending-of-a-string-in-javascript-62b4677034ac/)_

[**Three Ways to Reverse a String in JavaScript**](https://medium.freecodecamp.com/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb)  
_[This article is based on Free Code Camp Basic Algorithm Scripting “Reverse a String”](https://www.freecodecamp.org/news/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb/)_

[**Three Ways to Factorialize a Number in JavaScript**](https://medium.freecodecamp.com/how-to-factorialize-a-number-in-javascript-9263c89a4b38)  
_[This article is based on Free Code Camp Basic Algorithm Scripting “Factorialize a Number”](https://www.freecodecamp.org/news/how-to-factorialize-a-number-in-javascript-9263c89a4b38/)_

**[Two Ways to Check for Palindromes in JavaScript](https://www.freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7/)**  
_[This article is based on Free Code Camp Basic Algorithm Scripting “Check for Palindromes”.](https://www.freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7/)_

**[Three Ways to Find the Longest Word in a String in JavaScript](https://www.freecodecamp.org/news/three-ways-to-find-the-longest-word-in-a-string-in-javascript-a2fb04c9757c/)**  
_[This article is based on Free Code Camp Basic Algorithm Scripting “Find the Longest Word in a String”.](https://www.freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7/)_

**[Three Ways to Title Case a Sentence in JavaScript](https://www.freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27/)**  
_[This article is based on Free Code Camp Basic Algorithm Scripting “Title Case a Sentence”.](https://www.freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27/)_

If you have your own solution or any suggestions, share them below in the comments.

Or you can follow me on [**Medium**](https://medium.com/@sonya.moisset)**, [Twitter](https://twitter.com/SonyaMoisset), [Github](https://github.com/SonyaMoisset)** and [**LinkedIn**](https://www.linkedin.com/in/sonyamoisset), right after you click the green heart below ;-)

‪#‎StayCurious‬, ‪#‎KeepOnHacking‬ & ‪#‎MakeItHappen‬!

### Additional Resources

* [while loop — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
* [repeat() method — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/String/repeat)
* [recursion — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#Recursion)
* [Ternary Operator — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)

