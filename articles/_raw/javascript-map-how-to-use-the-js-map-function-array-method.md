---
title: JavaScript Map – How to Use the JS .map() Function (Array Method)
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-03-31T17:20:19.000Z'
originalURL: https://freecodecamp.org/news/javascript-map-how-to-use-the-js-map-function-array-method
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/javascript-map-function.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Sometimes you may need to take an array and apply some procedure to its\
  \ elements so that you get a new array with modified elements. \nInstead of manually\
  \ iterating over the array using a loop, you can simply use the built-in Array.map()\
  \ method.\nHere'..."
---

Sometimes you may need to take an array and apply some procedure to its elements so that you get a new array with modified elements. 

Instead of manually iterating over the array using a loop, you can simply use the built-in `Array.map()` method.

### Here's an Interactive Scrim of How to Use the JS .map() Function

<iframe src="https://scrimba.com/scrim/co93c4bf0af8e0ed2e162b818?pl=pKwWeHY&embed=freecodecamp,mini-header" width="100%" height="420"></iframe>

The `Array.map()` method allows you to iterate over an array and modify its elements using a callback function. The callback function will then be executed on each of the array's elements.

For example, suppose you have the following array element:

```js
let arr = [3, 4, 5, 6];
```

Now imagine you are required to multiply each of the array's elements by `3`. You might consider using a `for` loop as follows:

```js
let arr = [3, 4, 5, 6];

for (let i = 0; i < arr.length; i++){
  arr[i] = arr[i] * 3;
}

console.log(arr); // [9, 12, 15, 18]
```

But you can actually use the `Array.map()` method to achieve the same result. Here's an example:

```js
let arr = [3, 4, 5, 6];

let modifiedArr = arr.map(function(element){
    return element *3;
});

console.log(modifiedArr); // [9, 12, 15, 18]
```

The `Array.map()` method is commonly used to apply some changes to the elements, whether multiplying by a specific number as in the code above, or doing any other operations that you might require for your application.

## How to use map() over an array of objects

For example, you may have an array of objects that stores `firstName` and `lastName` values of your friends as follows:

```js
let users = [
  {firstName : "Susan", lastName: "Steward"},
  {firstName : "Daniel", lastName: "Longbottom"},
  {firstName : "Jacob", lastName: "Black"}
];


```

You can use the `map()` method to iterate over the array and join the values of  `firstName` and `lastName` as follows:

```js
let users = [
  {firstName : "Susan", lastName: "Steward"},
  {firstName : "Daniel", lastName: "Longbottom"},
  {firstName : "Jacob", lastName: "Black"}
];

let userFullnames = users.map(function(element){
    return `${element.firstName} ${element.lastName}`;
})

console.log(userFullnames);
// ["Susan Steward", "Daniel Longbottom", "Jacob Black"]
```

The `map()` method passes more than just an element. Let's see all arguments passed by `map()` to the callback function.

### Here's an interactive scrim about using map() to iterate over an array of objects:

<iframe src="https://scrimba.com/scrim/cLwqQ7uE?pl=pKwWeHY&embed=freecodecamp,mini-header" width="100%" height="420"></iframe>

## The complete map() method syntax

The syntax for the `map()` method is as follows:

```js
arr.map(function(element, index, array){  }, this);
```

The callback `function()` is called on each array element, and the `map()` method always passes the current `element`, the `index` of the current element, and the whole `array` object to it.

The `this` argument will be used inside the callback function. By default, its value is `undefined` . For example, here's how to change the `this` value to the number `80`:

```js
let arr = [2, 3, 5, 7]

arr.map(function(element, index, array){
	console.log(this) // 80
}, 80);
```

You can also test the other arguments using `console.log()` if you're interested:

```js
let arr = [2, 3, 5, 7]

arr.map(function(element, index, array){
    console.log(element);
    console.log(index);
    console.log(array);
    return element;
}, 80);
```

### Here's an interactive scrim that goes over the complete syntax:

<iframe src="https://scrimba.com/scrim/c7wmmJcv?pl=pKwWeHY&embed=freecodecamp,mini-header" width="100%" height="420"></iframe>

And that's all you need to know about the `Array.map()` method. Most often, you will only use the `element` argument inside the callback function while ignoring the rest. That's what I usually do in my daily projects :)

## **Thanks for reading this tutorial**

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!

