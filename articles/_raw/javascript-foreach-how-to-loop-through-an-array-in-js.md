---
title: JavaScript forEach – How to Loop Through an Array in JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-06T17:20:04.000Z'
originalURL: https://freecodecamp.org/news/javascript-foreach-how-to-loop-through-an-array-in-js
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99d8740569d1a4ca2204.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Cem Eygi\nThe JavaScript forEach method is one of the several ways to\
  \ loop through arrays. Each method has different features, and it is up to you,\
  \ depending on what you're doing, to decide which one to use. \nIn this post, we\
  \ are going to take a cl..."
---

By Cem Eygi

The JavaScript forEach method is one of the several ways to loop through arrays. Each method has different features, and it is up to you, depending on what you're doing, to decide which one to use. 

In this post, we are going to take a closer look at the JavaScript forEach method.

Considering that we have the following array below:

```javascript
const numbers = [1, 2, 3, 4, 5];
```

Using the traditional "for loop" to loop through the array would be like this:

```javascript
for (i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
} 
```

## What makes the forEach( ) method different?

The forEach method is also used to loop through arrays, but it uses a function differently than the classic "for loop". 

The forEach method passes a [callback function](https://www.freecodecamp.org/news/javascript-callback-functions-what-are-callbacks-in-js-and-how-to-use-them/) for each element of an array together with the following parameters: 

* Current Value (required) - The value of the current array element
* Index (optional) - The current element's index number
* Array (optional) - The array object to which the current element belongs

Let me explain these parameters step by step. 

Firstly, to loop through an array by using the forEach method, you need a callback function (or anonymous function): 

```javascript
numbers.forEach(function() {
    // code
});
```

The function will be executed for every single element of the array. It must take at least one parameter which represents the elements of an array:

```javascript
numbers.forEach(function(number) {
    console.log(number);
});
```

That's all we need to do for looping through the array:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Ads-z-2.png)

Alternatively, you can use the ES6 arrow function representation for simplifying the code:

```javascript
numbers.forEach(number => console.log(number));
```

## Optional Parameters

### Index

Alright now let's continue with the optional parameters. The first one is the "index" parameter, which represents the index number of each element. 

Basically, we can see the index number of an element if we include it as a second parameter:

```javascript
numbers.forEach((number, index) => {
    console.log('Index: ' + index + ' Value: ' + number);
});
```

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Ads-z-3.png)

### Array

The array parameter is the array itself. It is also optional and can be used if necessary in various operations. Otherwise, if we call it, it will just get printed as many times as the number of elements of the array:

```javascript
numbers.forEach((number, index, array) => {
    console.log(array);
});
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Ads-z.png)

You can see the example usage of the forEach( ) method in this video:

%[https://youtu.be/E2GawbHDFfs]

## Browser Support

The Array.forEach method is [supported](https://caniuse.com/#search=Array.foreach) in all browsers expect IE version 8 or earlier:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Ads-z.png)
_[caniuse.com](https://caniuse.com)_

**If you want to learn more about Web Development, feel free to visit my [Youtube Channel](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q?view_as=subscriber).**

Thank you for reading!

