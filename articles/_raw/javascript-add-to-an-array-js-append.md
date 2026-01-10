---
title: JavaScript Add to an Array – JS Append
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-10-14T18:29:54.000Z'
originalURL: https://freecodecamp.org/news/javascript-add-to-an-array-js-append
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/kelly-sikkema--1_RZL8BGBM-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "You can use arrays in JavaScript to store a group of variables, often referred\
  \ to as elements or items of the array. Each of these elements will have an index\
  \ number assigned to them starting from zero. \nBy default, you can use the index\
  \ of an elemen..."
---

You can use arrays in JavaScript to store a group of variables, often referred to as elements or items of the array. Each of these elements will have an index number assigned to them starting from zero. 

By default, you can use the index of an element in an array to access or modify its value.

But JavaScript provides different methods that you can use to add/append more elements to an array. 

## How to Add an Element to an Array in JavaScript Using the `push` Method

The `push` method takes in the element(s) to be added to the array as its parameter(s). 

Here's an example:

```javascript
let myArr = [2, 4, 6];

myArr.push(8);

console.log(myArr);
// [ 2, 4, 6, 8 ]

```

In the code above, the `myArr` array had 3 elements on initialization — `[2, 4, 6]`. 

Using the `push` method, we appended 8 to the array: `myArr.push(8)`. 

You can add more than one element when using the `push` method by passing the elements as parameters separated by commas. Here's an example:

```javascript
let myArr = [2, 4, 6];

myArr.push(8, 10, 12);

console.log(myArr);
// [ 2, 4, 6, 8, 10, 12 ]

```

## How to Add an Element to an Array in JavaScript Using the `splice` Method

You can use the `splice` method to add new elements, remove elements, and replace existing elements in an array. 

Here's what the syntax looks like:

```txt
splice(index, deleteNum, item1, ..., itemN)
```

Let's have a look at the meaning of each parameter above:

`index` denotes the starting index where the `splice` method will start its operation.

`deleteNum` denotes the number of elements to be deleted starting from `index`. 

`item1` denotes the value of the element to be inserted at `index`. 

If the explanations above seem confusing, the following examples should help you understand better. 

Here's the first example, showing how you can append an element to an array using the `splice` method:

```javascript
let myArr = [2, 4, 6];

myArr.splice(3,0,8)

console.log(myArr);
// [ 2, 4, 6, 8 ]
```

Let's break the code above down to its simplest form. Starting with the indexes – the array had three items initially:

2 => index 0  
4 => index 1  
6 => index 2

We passed in three parameters to the `splice` method: `splice(3,0,8)`. 

The first parameter — 3 — denotes the starting index for the `splice` method. Index 3 in our array comes immediately after the last element. 

The second parameter — 0 — denotes the number of elements to be deleted starting from index 3 (the index specified above).

The third parameter — 8 — denotes the value to be inserted at the specified index. So 8 is inserted at index 3. When logged to the console, we had this: `[ 2, 4, 6, 8 ]`

If you understand how the `splice` method works, then you should probably skip to the next section. Otherwise, the next example will simplify it further.

```javascript
let myArr = [2, 4, 6, 8, 10, 12, 14];

myArr.splice(3,2,16)

console.log(myArr);
// [ 2, 4, 6, 16, 12, 14 ]
```

Let's break it down like we did in the last example: 

2 => index 0  
4 => index 1  
6 => index 2  
8 => index 3  
10 => index 4  
12 => index 5  
14 => index 6

The `splice` method had three parameters: `splice(3,2,16)`. 

The first parameter is 3. This means we're starting at index three which has a value of 8. 

The second parameter is 2 which denotes how many elements are to be deleted starting from index 3. 

The third parameter is 16 which is the value to be inserted at index 3. 

If you take a look at the output, you'll notice that 16 now occupies index 3 while the two elements from the initial array (8 and 10) were deleted: `[ 2, 4, 6, 16, 12, 14 ]`. 

So the array went from:

Initial array = [2, 4, 6, 8, 10, 12, 14]. 

To deleting two elements starting from index 3 = [ 2, 4, 6, 12, 14 ]. 

To adding 16 at index 3 = [ 2, 4, 6, 16, 12, 14 ]. 

## How to Add an Element to an Array in JavaScript Using the `concat` Method

You can merge or concatenate two or more arrays using the `concat` method. Here's an example:

```javascript
let myArr1 = [2, 4, 6, 8];
let myArr2 = [10, 12, 14]

myArr = myArr1.concat(myArr2)

console.log(myArr);
// [ 2, 4, 6, 8, 10, 12, 14 ]


```

The code above is pretty straightforward. We created two different arrays — `myArr1` and `myArr2`. 

We then merged two of them into a single array, stored in the `myArr` variable: `myArr1.concat(myArr2)`.

## How to Add an Element to an Array in JavaScript Using the Spread Syntax (`...`)

You can also use the ES6 spread syntax (`...`) to merge arrays like we did in the last section.

```javascript
let myArr1 = [2, 4, 6, 8];
let myArr2 = [10, 12, 14]

myArr = [ ...myArr1, ...myArr2]

console.log(myArr);
// [ 2, 4, 6, 8, 10, 12, 14 ]


```

The spread syntax as used above copies all the values of both arrays into the `myArr` array: `myArr = [ ...myArr1, ...myArr2]`.

## Summary

In this article, we talked about the different methods you can use to add and append elements to a JavaScript array. 

We gave examples using the `push`, `splice`, and `concat` methods as well as the ES6 spread syntax (`...`). 

Happy coding!

