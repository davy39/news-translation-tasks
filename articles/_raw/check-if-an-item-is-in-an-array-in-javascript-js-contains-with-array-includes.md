---
title: Check if an Item is in an Array in JavaScript – JS Contains with Array.includes()
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-28T22:28:00.000Z'
originalURL: https://freecodecamp.org/news/check-if-an-item-is-in-an-array-in-javascript-js-contains-with-array-includes
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/pankaj-patel-1IW4HQuauSU-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "You can use the includes() method in JavaScript to check if an item exists\
  \ in an array. You can also use it to check if a substring exists within a string.\
  \ \nIt returns true if the item is found in the array/string and false if the item\
  \ doesn't exist...."
---

You can use the `includes()` method in JavaScript to check if an item exists in an array. You can also use it to check if a substring exists within a string. 

It returns `true` if the item is found in the array/string and `false` if the item doesn't exist.

In this article, you'll see how to use the `includes()` method in JavaScript to check if an item is in an Array, and if a substring exists within a string. 

## How to Check if an Item is in an Array in JavaScript Using `Array.includes()`

Here's the syntax for using the `includes()` method to check if an item is in an array: 

```txt
array.includes(item, fromIndex)
```

Let's break down the syntax above:

`array` denotes the name of the array which will be searched through to check if an item exists.

The `includes()` method takes in two parameters – `item` and `fromIndex`. 

* `item` is the particular item you are searching for. 
* `fromIndex`, which is an optional parameter, specifies the index from which to start the search. If you don't include this parameter, the default index will be set to 0 (the first index). 

Here are some examples to show how to use the `includes()` method to check if an item exists in an array:

```javascript
const nums = [ 1, 3, 5, 7];
console.log(nums.includes(3));
// true
```

In the example above, we created an array called `nums` with four numbers – 1, 3, 5, 7. 

Using dot notation, we attached the `includes()` method to the `nums` array.

In the `includes()` method's parameter, we passed in 3. This is the item we want to search for. 

We got `true` returned because 3 exists in the `nums` array. 

Let's try searching for a number that doesn't exist in the array. 

```javascript
const nums = [ 1, 3, 5, 7];
console.log(nums.includes(8));
// false

```

As expected, we got `false` returned in the example above because 8 is not an item in the `nums` array. 

## How to Check if an Item is in an Array in JavaScript Using `Array.includes()` Starting From a Specified Index

In the last section, we saw how to check if an item existed in an array without using the second parameter in the `includes()` method. 

As a reminder, the second parameter is used to specify the index to start from when searching for an item in an array. 

The index of an array starts from 0. So the first item is 0, the second item is 1, the third item is 2, and so on. 

Here's an example to show how we can use the `includes()` method's second parameter:

```javascript
const nums = [ 1, 3, 5, 7];
console.log(nums.includes(3,2));
// false
```

The example above returned `false` even though we had 3 as an item in the array. Here's why:

Using the second parameter, we told the `includes()` method to search for the number 3 but starting from index 2: `nums.includes(3,2)`.

This is the array:  [ 1, 3, 5, 7]

Index 0 = 1.

Index 1 = 3.

Index 2 =  5.

Index 3 = 7.

So starting from the second index which is 5, we have only 5 and 7 ([5,7]) to be searched through. This is why searching for 3 from index 2 returned `false`.

If you change the index to start the search from to 1 then you'd get `true` returned because 3 can be found within that range. That is:

```javascript
const nums = [ 1, 3, 5, 7];
console.log(nums.includes(3,1));
// true
```

## How to Check if a Substring is in a String in JavaScript Using the `includes()` Method

Similar to the previous examples, you have to attach the `includes()` method to the name of the string to be searched through using dot notation. 

Here's what the syntax looks like:

```txt
string.includes(substring, fromIndex)
```

Here's an example:

```javascript
const bio = "I am a web developer";
console.log(bio.includes("web"));
// true
```

In the example above, the `bio` variable had a value of "I am a web developer". 

Using the `includes()` method, we searched for the substring "web". 

We got `true` returned because "web" is in the `bio` string.

You can also use the second parameter to specify where the search will begin, but note that each character in a string represents an index and the spaces between each substring also represents an index.

Here is an example to demonstrate that:

```javascript
let bio = "I am a web developer";
console.log(bio.includes("web",9));
// false
```

We are getting `false` because index 9 is the e in "web". 

Starting from index 9, the string would look like this: "eb developer". The substring "web" doesn't exist in the string so `false` gets returned.

## Summary

In this article, we talked about the `includes()` method in JavaScript. You use it to check if an item exists in an array. You can also use it to check if a substring can be found within a string.

We saw some examples that explained its use to check for an item in an array starting from the first index, then another example from a specified index.

Lastly, we saw how to use the `includes()` method to check if a substring exists within a string from the first index and from a specified index. 

Happy coding!

