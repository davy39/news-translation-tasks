---
title: How to Check if a JavaScript Array is Empty or Not with .length
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-05T23:08:04.000Z'
originalURL: https://freecodecamp.org/news/check-if-javascript-array-is-empty-or-not-with-length
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/road-690087_1920.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Madison Kanna

  When you''re programming in JavaScript, you might need to know how to check whether
  an array is empty or not.

  To check if an array is empty or not, you can use the .length property.

  The length property sets or returns the number of el...'
---

By Madison Kanna

When you're programming in JavaScript, you might need to know how to check whether an array is empty or not.

To check if an array is empty or not, you can use the .length property.

The length property sets or returns the number of elements in an array. By knowing the number of elements in the array, you can tell if it is empty or not. An empty array will have `0` elements inside of it.

Let’s run through some examples.

### Here's an Interactive Scrim Showing How to Check if a JavaScript Array is Empty or Not with .length:

<iframe src="https://scrimba.com/scrim/cpJWbLud?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

## .length Example Syntax

```javascript
Const myArray = [‘Horses’, ‘Dogs’, ‘Cats’];
```

Here we create a variable pointing towards an array.

Using the length property, we can check the length of the array:

```javascript
myArray.length
```

This will return 3, because there are 3 items in the array.

To check if the array is empty or not with .length, we can do this in in three ways.

### .length example one

First, let's create a new array with no elements. 

```javascript
const arr = []
```

Now we can check if the array is empty by using `.length`.

```javascript
arr.length
```

This will return 0, as there are 0 items in the array. 

### .length example two

We can also explicitly check if the array is empty or not.

`if (arr.length === 0) { console.log("Array is empty!") }`

If our array is empty, the above message will get logged. If the array has elements in it, the code within the `if` block will not run.

Here's the third way to check whether or not an array is empty using .length. 

### .length example three

By combining the use of the length property and the logical "not" operator in JavaScript, the "!" symbol, we can check if an array is empty or not. 

The `!` operator negates an expression. That is, we can use it to return `true` if an array is empty.

For this example, let's open up our JavaScript console. To open up your console in Chrome, you can click Inpsect -> Console.

First, create an array with no items in it.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image.png)

Next, let's use the logical "not" operator, along with our .length property, to test if the array is empty or not.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-30-at-5.29.35-PM.png)

If we had not used the "not" operator, `arr.length` would have returned `0`. With the operator added, it will return `true` if its operand is `false`. Because arr.length is `0`, or false, it returns `true`. 

Let's use this with an `if` statement, and print out a message if our array is empty. 

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-2.png)

When checking if an array is empty or not, it's often best to also check if the array is indeed an array. 

Why?  

Because there might be the case when you were expecting to check the length of an array, but instead you're given a different data type, for example, a string:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-7.png)

Because the `length property` can be used on other data types, it is good to also check that your array is indeed an array as you were expecting. 

I suggest you also use the `Array.isArray()` method to confirm your array is an array. This method determines if whether what was passed in is an array or not. If what was passed in was an array, this method will return `true`. 

Let's add this method to our example.

### How to use the Array.isArray() method

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-3.png)

## Wrapping up

In this article, we learned that you can use the `length` property in JavaScript in various ways to check if an array is empty or not. The `length` property returns the number of items in an array. 

We also learned that it is best to also use the `Array.isArray` method when using the `.length` property, to check if the passed value is an array as you're expecting.

