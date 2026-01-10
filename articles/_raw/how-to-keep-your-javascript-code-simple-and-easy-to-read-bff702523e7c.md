---
title: How to keep your JavaScript code simple and easy to read
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-02T17:25:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-keep-your-javascript-code-simple-and-easy-to-read-bff702523e7c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ecVfURF6VRf5Yxf2yaRteg.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Arthur Arakelyan

  There are many ways to solve the same problem, but some solutions are complex, and
  some are even ridiculous. In this article, I want to talk about bad and good solutions
  for the same problems.

  Let’s start with the problem that req...'
---

By Arthur Arakelyan

There are many ways to solve the same problem, but some solutions are complex, and some are even ridiculous. In this article, I want to talk about bad and good solutions for the same problems.

Let’s start with the problem that requires us to remove duplicate values from an array.

#### **Complex - Removing duplicates using forEach**

First, we create a new empty array, then we use the [**forEach()**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach) method to execute a provided function once for each array element. Eventually, we check if the value doesn’t exist in the new array, and if not, we add it.

```
function removeDuplicates(arr) {     const uniqueVals = [];      arr.forEach((value,index) => {            if(uniqueVals.indexOf(value) === -1) {           uniqueVals.push(value);       }     });  return uniqueVals;}
```

#### **Simple - Removing duplicates using filter**

The [**filter**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) method creates a new array with all elements that pass the test implemented by the provided function. Basically, we iterate over the array and, for each element, check if the first position of this element in the array is equal to the current position. Of course, these two positions are different for duplicate elements.

```
function removeDuplicates(arr) {  return arr.filter((item, pos) => arr.indexOf(item) === pos)}
```

#### **Simple - Removing duplicates using Set**

ES6 provides the [**Set**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) object, which makes things a whole lot easier. **Set** allows only unique values, so when you pass in an array, it removes any duplicate values.

However, if you need an array with unique elements, why not use **Set** right from the beginning?

```
function removeDuplicates(arr) {   return [...new Set(arr)];}
```

Let’s move on and solve the second problem which requires us to write a function that takes an array of distinct non-negative integers, make them consecutive, and return the count of missing numbers.

For `const arr = [4, 2, 6, 8]`, the output should be  
`countMissingNumbers(arr) = 3`

As you can see `3`, `5`and `7` are missing

#### **Complex - Solving by using sort and for loop**

To obtain the smallest and largest numbers we need to [**sort**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort) them in ascending order, and for that purpose, we use `sort` method. Then we loop from the smallest number to the largest number. Each time, we check whether a sequential number exists in the array or not, and if not we increase the counter.

```
function countMissingNumbers(arr) {    arr.sort((a,b) => a-b);        let count = 0;        const min = arr[0];        const max = arr[arr.length-1];    for (i = min; i<max; i++) {      if (arr.indexOf(i) === -1) {          count++;               }          }            return count;}
```

#### **Simple - Solving by using Math.max and Math.min**

This solution has a simple explanation: the `[**Math.max()**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/max)` function returns the largest number in the array and the `[**Math.min()**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/min)` returns the smallest number in the array.

First, we find how many numbers would be in the array if there weren’t missing numbers. For that, we use the following formula `maxNumber - minNuber + 1`, and the difference between the result of this and the array length will give us the count of missing numbers.

```
function countMissingNumbers(arr) {      return Math.max(...arr) - Math.min(...arr) + 1 - arr.length;}
```

The last problem I want to bring as an example is to check whether the string is a **palindrome** or not.

_*A **palindrome** is a string that reads the same left-to-right and right-to-left._

#### **Complex - Checking By using for loop**

In this option, we loop over the string starting from the first character until half of the string length. The index of the last character in a string is string.length-1, the second to last character is string.length-2, and so on. So here we check whether the character at the specified index from the start is equal to the character at the specified index at the end. If they are not equal, we return false.

```
function checkPalindrome(inputString) {    let length = inputString.length   for (let i =0; i<length / 2; i++) {        if (inputString[i] !== inputString[length - 1 -i]) {             return false                }   }  return true}
```

#### **Simple - Checking by using reverse and join**

I think that this simple solution doesn't require an explanation, as it speaks for itself. We simply create an array from the string using the [**spread operator**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax), then [**reverse**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse) the array, then turn it into a string again using the [**join**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join) method and compare it with the original string.

```
function checkPalindrome(string) {   return string === [...string].reverse().join('');}
```

#### Keep it simple!

Why complicate when there are simpler ways? I hope you found this article interesting. Have a good day and try not to complicate simple things in life as well :)

Thanks for your claps ?

