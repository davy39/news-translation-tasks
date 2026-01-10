---
title: How to Get the First Line of a Multiline String in JavaScript
subtitle: ''
author: Furkan Emin Can
co_authors: []
series: null
date: '2024-01-24T23:33:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-the-first-line-of-a-multiline-string-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Cover.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In JavaScript, getting the first element of an array or string is pretty
  easy. But when it comes to getting the first line of a multiline string, some approaches
  can hurt your app''s performance in certain cases.

  In this article, we will look at the t...'
---

In JavaScript, getting the first element of an array or string is pretty easy. But when it comes to getting the first line of a multiline string, some approaches can hurt your app's performance in certain cases.

In this article, we will look at the three best ways you can get the first line of a multiline string in JS. 

For those of you in a hurry, here is the best solution:

```javascript
input.slice(0, input.indexOf("\n"));
```

And now if you want to learn more, let's dive deep into the details.

## The Problem

The main problem in most solutions is that, in order to simply get the first line of the string, you have to operate over the entire string. If the input is too big, this operation takes an unnecessarily long time and consumes many resources.

Let's explain with an example.

Let's say, I have a gigantic string that contains 10 million lines of text and I want to get the first line of it. So I choose to use the `Array.split` method like in the following example:

```javascript
input.split("\n")[0];

```

In this code, the `split` method operates over the entire 10 million lines to get only the first line. As a result, to get only the first item, I have an array containing 10 million items.

This operation takes approximately `1.7` seconds on my PC. This is unnecessarily long for such a small operation.

Let's look at the solutions to overcome this problem.

## The Solutions

After some research, I found the three best ways of doing this operation:

1. Using the `String.indexOf` and `String.slice` methods.
2. Using the `Array.split` method.
3. Using the `String.match` method.

Here are the benchmark results of each solution:

![Image](https://www.freecodecamp.org/news/content/images/2024/01/benchmarks.png)
_Benchmark results_

Also, you can access the benchmark results from [this link](https://perf.link/#eyJpZCI6InhzeG9lOGh6cDgzIiwidGl0bGUiOiJHZXR0aW5nIHRoZSBmaXJzdCBsaW5lIG9mIGEgbXVsdGlsaW5lIHN0cmluZyIsImJlZm9yZSI6ImNvbnN0IGlucHV0ID0gQXJyYXkuZnJvbShBcnJheSgxMDAwKSwgKF8sIGkpID0%2BIGBJIGFtIHRoZSBsaW5lICR7aSArIDF9YCkuam9pbignXFxuJyk7IiwidGVzdHMiOlt7Im5hbWUiOiJTdHJpbmcuc2xpY2Ugd2l0aCBTdHJpbmcuaW5kZXhPZiIsImNvZGUiOiJpbnB1dC5zbGljZSgwLCBpbnB1dC5pbmRleE9mKCdcXG4nKSk7IiwicnVucyI6WzQ4MzUwMDAsNjQ5OTAwMCwxNDA0MDAwLDQ5NDYwMDAsMjM5MjAwMCwxMjg1MDAwLDcyNDIwMDAsNTg1OTAwMCwyMjk0MDAwLDM0OTIwMDAsNzM5NTAwMCwzOTI3MDAwLDE2NTEwMDAsNTg1OTAwMCw2MTAwMCwxMzY3MDAwLDUwODgwMDAsMTkyMDAwMCw3MzcyMDAwLDEyNjQwMDAsNTczMTAwMCwxNzgxMDAwLDE4NzkwMDAsNjk3ODAwMCw3MzYwMDAwLDU3MzEwMDAsNDA5MDAwMCw2ODI2MDAwLDQ3MzQwMDAsOTUxMDAwLDY0MzAwMCw1MTEwMDAsNjE3NjAwMCw3OTYzMDAwLDE3MjUwMDAsNDYyNjAwMCw0MTQwMDAsNDcwNzAwMCwxODg4MDAwLDcwNzIwMDAsMTcyNzAwMCwxMzMxMDAwLDQ5NDcwMDAsMjYwNDAwMCwyNzc4MDAwLDI5MDkwMDAsMjI4NDAwMCw4NDk2MDAwLDQ5MTIwMDAsNjU4OTAwMCwxNDcwMDAwLDY2MjMwMDAsNDA4MTAwMCwxMTkyMDAwLDUyMzEwMDAsMTY3ODAwMCwyNjIzMDAwLDYwODYwMDAsMzgwNDAwMCwxOTg0MDAwLDYzODUwMDAsMTA2MzAwMCw1MjY5MDAwLDEzOTEwMDAsMTk3ODAwMCw3NTkwMDAwLDIwMTAwMDAsODc0MDAwLDE0OTIwMDAsNjk1NjAwMCw4NzMwMDAsNzEzODAwMCw1NDcwMDAsMjc5NjAwMCw2OTQwMDAsNDA0OTAwMCwzMzYwMDAsMjE4MTAwMCwzOTEwMDAsMjUyNDAwMCw2NTMzMDAwLDE4MTAwMDAsMjEwMjAwMCwxMjcyMDAwLDcyNDUwMDAsNjA4MDAwMCwyNjkzMDAwLDcwMDQwMDAsMjg4ODAwMCwxNDYxMDAwLDUwOTAwMCw5MTAwMDAwLDE0MzQwMDAsMTE5MjAwMCw3NTAwMCwxMDAwMCwyNDc2MDAwLDQ0ODUwMDAsMTQ4OTAwMCw0OTkzMDAwXSwib3BzIjozNTI2NzUwfSx7Im5hbWUiOiJTdHJpbmcuc3BsaXQiLCJjb2RlIjoiaW5wdXQuc3BsaXQoJ1xcbicsIDEpWzBdOyIsInJ1bnMiOlsyMDIzMDAwLDQxMTkwMDAsNzU4MDAwLDI1MzMwMDAsMjE3MDAwMCw3NTkwMDAsMjM5MTAwMCwyNTYwMDAwLDE2NjIwMDAsMTU0NTAwMCwzMTI4MDAwLDE4OTAwMDAsMTI5MDAwMCw0NDQ5MDAwLDE4MDAwLDEzNzcwMDAsMjEyNjAwMCw5NzEwMDAsMjk1MTAwMCwxMzU4MDAwLDIzNTcwMDAsMTY5OTAwMCwxMjcxMDAwLDQyMTgwMDAsMjgxMDAwLDIzNDYwMDAsMzM1MDAwLDI3NjAwMDAsMTgzMjAwMCw2OTUwMDAsNDM4MDAwLDM2MDQwMDAsMjU2MzAwMCw0ODA1MDAwLDE2MzYwMDAsMzgwNTAwMCwxMjgwMDAsMjk0NjAwMCwxMzczMDAwLDUxNzQwMDAsNTkxMDAwLDQ1MDEwMDAsMjAyNTAwMCwxNzQyMDAwLDIwODEwMDAsMTQ5MjAwMCw3MTkwMDAsMzYyMTAwMCwxMzYwMDAwLDM1MzAwMDAsMTQ3OTAwMCwyNDMzMDAwLDMzNTkwMDAsMTQ2MjAwMCwxOTgzMDAwLDE3MTUwMDAsMTI4OTAwMCwzNDY5MDAwLDE3MTEwMDAsMTcxNTAwMCwzMTY3MDAwLDIwNTgwMDAsMjgwODAwMCw2ODcwMDAsMTcwOTAwMCwyODU4MDAwLDEyOTAwMDAsMTA0MjAwMCwxMjU3MDAwLDM0NzUwMDAsMTIxMjAwMCw0MzcxMDAwLDEyMjYwMDAsMjA0OTAwMCwzNzg3MDAwLDIzMDMwMDAsNDUzMDAwLDEyOTAwMDAsMjg4MDAwLDE4NzAwMDAsNDU2MDAwMCwxODg5MDAwLDE0OTkwMDAsNDA4MjAwMCwzNTk0MDAwLDM1NjcwMDAsMTc1MjAwMCwyODgwMDAwLDE0OTQwMDAsMTA3NzAwMCwzNjI3MDAwLDcyODAwMCwzNzUwMDAwLDEyOTAwMDAsMTAwMCwyOTcwMDAwLDI2NjAwMDAsMzEyODAwMCw4MTIwMDAsMjIxMjAwMF0sIm9wcyI6MjEzMzkzMH0seyJuYW1lIjoiU3RyaW5nLm1hdGNoIiwiY29kZSI6ImlucHV0Lm1hdGNoKC8uKig%2FPVxcbikvKVswXTsiLCJydW5zIjpbMjI3MDAwMCwyMzU5MDAwLDI0NTEwMDAsNTU1MDAwLDExNzIwMDAsMjQ3MTAwMCwxODMwMDAwLDEwMDAsMTAwMCwxMDg3MDAwLDIzNjMwMDAsMjQ2MDAwLDE2NDYwMDAsMjIzNTAwMCw2NzYxMDAwLDE3NTcwMDAsMTE3MjAwMCwyOTE5MDAwLDI3NjIwMDAsMjAwMDAwLDMwNzIwMDAsMTExMDAwLDM0ODMwMDAsMTc3ODAwMCwxNTAwMDAsMjgxNjAwMCwyODY0MDAwLDE1NDcwMDAsMTAwMCw5ODkwMDAsMzg1MzAwMCwxNTAyMDAwLDI1MjUwMDAsMjc5NDAwMCwxMDAwLDI2NzcwMDAsMjQ4ODAwMCw5MjgwMDAsMjM3ODAwMCwyOTUwMDAwLDIyODkwMDAsMzI0MDAwMCwxMDAwLDEwMDAsMTgzOTAwMCw0NjYwMDAsMTg3MDAwLDIxOTYwMDAsMTAwMCwyMzc4MDAwLDM3MDYwMDAsNjEyMDAwLDIzNjIwMDAsNzcwMDAwLDc4MDAwLDExMjIwMDAsMTg4NDAwMCwzMDczMDAwLDE1NjYwMDAsMzE5NDAwMCwxMDcyMDAwLDMzOTMwMDAsMTI5NTAwMCwyODcwMDAsMTMwMjAwMCwzOTgzMDAwLDI1MjIwMDAsNDUzMDAwLDI5NTIwMDAsMzQzODAwMCw1MzQwMDAsNDA2MzAwMCwyNTYwMDAsMTQ4MjAwMCwyMjMwMDAwLDgxODAwMCw0MTAwMCw0NTMwMDAsMjAwMDAsMjI2NDAwMCwyODkwMDAwLDc2NzAwMCwyNDE2MDAwLDE3MzEwMDAsMTk0MDAwMCwzMTU3MDAwLDI3NzgwMDAsMTY2MzAwMCw3MDUwMDAsMzEyNTAwMCwxODE5MDAwLDIwMTEwMDAsMTQ0MDAwMCw3NDcwMDAsMTAwMCwxMzAwMDAwLDEzMDIwMDAsMjI0ODAwMCw1MDYwMDAsMTMwMjAwMF0sIm9wcyI6MTcyODM2MH1dLCJ1cGRhdGVkIjoiMjAyNC0wMS0yMlQxOTowNDoxMS4zMzRaIn0%3D) and perform benchmarks yourself, too.

Let's explore each solution separately.

### 1. Using the `String.indexOf` and `String.slice` Methods

In this solution, we will use the `String.indexOf` method to find the index of the new line (`\n`) character, and then will slice the string to this index with the `String.slice` method.

```javascript
input.slice(0, input.indexOf("\n"));
```

This solution takes first place in the benchmark results.

### 2. Using the `Array.split` Method

As you have seen in the problem, the `Array.split` method operates over the entire string. But it also accepts an optional `limit` parameter. We can leverage this parameter to avoid unnecessary operations.

```javascript
input.split("\n", 1)[0];

```

In this code, we took advantage of the optional `limit` parameter and so the operation stops after the first split operation.

This solution takes second place in the benchmark results.

### 3. Using the `String.match` Method

This approach is for those of you who particularly want to use regex.

We will use the `String.match` method in this case. We will create a regex literal that matches with any character group which is followed by a new line character, and pass it to the method. The first element of the returned array (which is the match) is the first line.

```javascript
input.match(/.*(?=\n)/)[0];

```

This solution takes third place in the benchmark results and performs two times slower than the first solution.

According to [the MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#literal_notation_and_constructor):

> Before regular expressions can be used, they have to be compiled.

The performance downgrade is probably because of that.

## Conclusion

In this article, we have looked at three different approaches to get the first line of a multiline string.

As developers, even for such a small operation, we should consider edge cases to avoid potential problems in the future.

Thank you for reading. You can connect with me on [Twitter](https://twitter.com/femincan) or explore more on [my personal blog](https://femincan.dev). Feel free to reach out — I'd love to hear from you!

