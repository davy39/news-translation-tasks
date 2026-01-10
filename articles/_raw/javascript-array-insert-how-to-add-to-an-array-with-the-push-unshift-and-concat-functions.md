---
title: JavaScript Array Insert - How to Add to an Array with the Push, Unshift, and
  Concat Functions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-25T21:36:59.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-insert-how-to-add-to-an-array-with-the-push-unshift-and-concat-functions
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/Hello--my-name-is-Matthew.-Nice-to-meet-you..png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Nehemiah Kivelevitz\nJavaScript arrays are easily one of my favorite\
  \ data types. They are dynamic, easy to use, and offer a whole bunch of built-in\
  \ methods we can take advantage of. \nHowever, the more options you have the more\
  \ confusing it can be t..."
---

By Nehemiah Kivelevitz

JavaScript arrays are easily one of my favorite data types. They are dynamic, easy to use, and offer a whole bunch of built-in methods we can take advantage of. 

However, the more options you have the more confusing it can be to decide which one you should use. 

In this article, I would like to discuss some common ways of adding an element to a JavaScript array.

### Here's an Interactive Scrim of How to Add to an Array 

<iframe src="https://scrimba.com/scrim/cLwq7WCZ?pl=pd9ZLcW&embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>


## The Push Method

The first and probably the most common JavaScript array method you will encounter is _push()_. The push() method is used for adding an element to the end of an array. 

Let's say you have an array of elements, each element being a string representing a task you need to accomplish. It would make sense to add newer items to the end of the array so that we could finish our earlier tasks first. 

Let's look at the example in code form:

```javascript
const arr = ['First item', 'Second item', 'Third item'];

arr.push('Fourth item');

console.log(arr); // ['First item', 'Second item', 'Third item', 'Fourth item']
```

Alright, so push has given us a nice and simple syntax for adding an item to the end of our array. 

Let's say we wanted to add two or three items at a time to our list, what would we do then? As it turns out, _push()_ can accept multiple elements to be added at once. 

```javascript
const arr = ['First item', 'Second item', 'Third item'];

arr.push('Fourth item', 'Fifth item');

console.log(arr); // ['First item', 'Second item', 'Third item', 'Fourth item', 'Fifth item']
```

Now that we've added some more tasks to our array we might want to know how many items are currently in our array to determine if we have too much on our plate. 

Luckily, _push()_ has a return value with the length of the array after our element(s) have been added.

```javascript
const arr = ['First item', 'Second item', 'Third item'];

const arrLength = arr.push('Fourth item', 'Fifth item');

console.log(arrLength); // 5 
console.log(arr); // ['First item', 'Second item', 'Third item', 'Fourth item', 'Fifth item']
```

## The Unshift Method

Not all tasks are created equal. You might run into a scenario in which you are adding tasks to your array and suddenly you encounter one which is more urgent than the others. 

It's time to introduce our friend _unshift()_ that allows us to add items to the beginning of our array. 

```javascript
const arr = ['First item', 'Second item', 'Third item'];

const arrLength = arr.unshift('Urgent item 1', 'Urgent item 2');

console.log(arrLength); // 5 
console.log(arr); // ['Urgent item 1', 'Urgent item 2', 'First item', 'Second item', 'Third item']
```

You may notice in the example above that, just like the _push()_ method, _unshift()_ returns the new array length for us to use. It also gives us the ability to add more than one element at a time. 

## The Concat Method

Short for concatenate (to link together), the _concat()_ method is used for joining together two (or more) arrays. 

If you remember from above, the _unshift()_ and _push()_ methods return the length of the new array. _concat()_, on the other hand, will return a completely new array. 

This is a very important distinction and makes _concat()_ extremely useful when you're dealing with arrays you do not want to mutate (like arrays stored in React state).

Here is what a fairly basic and straightforward case might look like:

```javascript
const arr1 = ['?', '?'];
const arr2 = ['?', '?'];

const arr3 = arr1.concat(arr2);

console.log(arr3); // ["?", "?", "?", "?"] 

```

Let's say you have multiple arrays you would like to join together. No worries, _concat()_ is there to save the day!

```javascript
const arr1 = ['?', '?'];
const arr2 = ['?', '?'];
const arr3 = ['?', '?'];

const arr4 = arr1.concat(arr2,arr3);

console.log(arr4); // ["?", "?", "?", "?", "?", "?"]

```

### Here's an interactive scrim to help you understand this better:

<iframe src="https://scrimba.com/scrim/cZa9DZsz?pl=pd9ZLcW&embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

### Cloning with Concat

Remember how I said that _concat()_ can be useful when you don't want to mutate your existing array? Let's take a look at how we can leverage this concept to copy over the contents of one array into a new array.

```javascript
const arr1 = ["?", "?", "?", "?", "?", "?"];

const arr2 = [].concat(arr1);

arr2.push("?");

console.log(arr1) //["?", "?", "?", "?", "?", "?"]
console.log(arr2) //["?", "?", "?", "?", "?", "?", "?"]
```

Awesome! We can essentially "clone" an array using _concat()_. 

But there is a small 'gotcha' in this cloning process. The new array is a "shallow copy" of the copied array. This means that any object is **copied by reference** and not the actual object. 

Let's take a look at an example to explain this idea more clearly.

```javascript
const arr1 = [{food:"?"}, {food:"?"}, {food:"?"}]

const arr2 = [].concat(arr1);

// change both arr1 and arr2
arr2[1].food = "!";
// change only arr2
arr2.push({food:"*"})

console.log(arr1) // [ { food: '?' }, { food: '!' }, { food: '?' } ]

console.log(arr2) // [ { food: '?' }, { food: '!' }, { food: '?' }, { food: '*' } ] 
```

Even though we didn't **directly** make any changes to our original array, the array was ultimately affected by the changes we made on our cloned array! 

There are multiple different ways to properly do a "deep clone" of an array, but I will leave that for you as homework. 

## TL;DR

When you want to add an element to the end of your array, use _push()._ If you need to add an element to the beginning of your array, try _unshift()._ And you can add arrays together using _concat()._ 

There are certainly many other options for adding elements to an array, and I invite you to go out and find some more great array methods! 

Feel free to reach out to me on [Twitter](https://twitter.com/nehemiahkiv) and let me know your favorite array method for adding elements to an array. 

