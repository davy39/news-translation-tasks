---
title: What's New in JavaScript in 2023 – Changes with Code Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-11-29T18:09:51.000Z'
originalURL: https://freecodecamp.org/news/the-biggest-changes-in-javascript-this-year
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/What-s-new.png
tags:
- name: ecmascript
  slug: ecmascript
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Nishant Kumar\nECMAScript 2023, the 14th edition of the language, has\
  \ some great changes that will make your programming life easier. \nIn this article,\
  \ I'll go through each of the changes and explain why they're helpful. So let’s\
  \ dive in and see so..."
---

By Nishant Kumar

ECMAScript 2023, the 14th edition of the language, has some great changes that will make your programming life easier. 

In this article, I'll go through each of the changes and explain why they're helpful. So let’s dive in and see some new methods we got as an early Christmas present.

## Object.groupBy

Let’s say you have an array of objects and want to separate them based on a property value, type, or quantity.

```javascript
const inventory = [
  { name: "asparagus", type: "vegetables", quantity: 5 },
  { name: "bananas", type: "fruit", quantity: 0 },
  { name: "goat", type: "meat", quantity: 23 },
  { name: "cherries", type: "fruit", quantity: 5 },
  { name: "fish", type: "meat", quantity: 22 },
];
```

We have a new method now called `GroupBy` that lets you do just that.

To use it, use `Object.groupBy` on any array with objects, and pass a function that returns the specific key by which you want to categorize.

Here, we are having an array of objects called `inventory`. And a `myCallback` function that is taking a quantity as a parameter and returning `ok` if the quantity is more than 5, or else returning `restock`.

We are passing the inventory array and the `myCallback` function to Object,groupBy so that it groups the items in the array by quantity.

```
function myCallback({ quantity }) {
  return quantity > 5 ? "ok" : "restock";
}

const result2 = Object.groupBy(inventory, myCallback);
```

The result will be an object which contains the key which is the category and the specified data inside it.

```
{
    "restock": [
        {
            "name": "asparagus",
            "type": "vegetables",
            "quantity": 5
        },
        {
            "name": "bananas",
            "type": "fruit",
            "quantity": 0
        },
        {
            "name": "cherries",
            "type": "fruit",
            "quantity": 5
        }
    ],
    "ok": [
        {
            "name": "goat",
            "type": "meat",
            "quantity": 23
        },
        {
            "name": "fish",
            "type": "meat",
            "quantity": 22
        }
    ]
}
```

## Array.toSliced(), Array.toSorted(), and Array.toReversed()

When we use methods like `sort()`, `splice()`, and `reverse()`, they mutate the original array. This can sometimes be an issue.

But when using `toSpliced()`, `toSorted()`, and `toReversed()`, we can splice, sort, and reverse an array without mutating the source array. Here's how it works:

```javascript
const numbers = [3, 4, 1, 5, 2];

const splicedNumbers = numbers.toSpliced(1, 1);
const sortedNumbers = numbers.toSorted();
const reversedNumbers = numbers.toReversed();
```

In this example, we are using `toSpliced()` to splice the array, `toSort()` to sort the array, and `toReversed()` to reverse the array. They work just like regular splice, sort, and reverse but the catch is they will return a new array, and not mutate the original one.

## findLast() and findLastIndex()

Before ES14, if you wanted to find the last element or index in an array that satisfies some condition, you would have to reverse the array first.

```
function findLastIndexByReversing(arr, target) {
  const reversedArray = arr.slice().reverse();
  const reversedIndex = reversedArray.indexOf(target);

  if (reversedIndex !== -1) {
    const lastIndex = arr.length - 1 - reversedIndex;
    return lastIndex;
  } else {
    return -1; 
  }
}
```

In this example, `findLastIndexByReversing` creates a reversed copy of the original array using `slice().reverse()`. Then, it uses `indexOf` to find the first occurrence of the target element in the reversed array. The function calculates the corresponding index in the original array by subtracting the reversed index from the total length of the array minus 1. This gives you the last index of the element in the original array.

Or you can use a for loop that starts from the end.

```
function findLastIndex(arr, target) {
  for (let i = arr.length - 1; i >= 0; i--) {
    if (arr[i] === target) {
      return i;
    }
  }
  return -1;
}
```

In this example, the `findLastIndex` function takes an array `arr` and a target element `target`. It iterates over the array from the end `arr.length - 1` to the beginning `0`. If it finds the target element, it returns the index. If the element is not found, it returns -1.

But now, we have a method known as `lastIndexOf()` that will start from the end of the array and return the value of the first element that satisfies the condition.

```
const fruits = ['apple', 'banana', 'orange', 'banana', 'kiwi'];

const lastIndex = fruits.lastIndexOf('banana');
```

Here is the output: 

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-2023-11-29-at-11.09.16-PM.png)
_Output showing `3`_

## Wrapping Up

These were the changes that were introduced in JavaScript as ECMAScript 2023.

Thanks for reading, and I will see you in the next tutorial.

If you wish to see a short video version of the article, you can check that out here: 

%[https://youtu.be/XSfJZyTKpdA?si=Cl2UfisCzScAFeyR]


