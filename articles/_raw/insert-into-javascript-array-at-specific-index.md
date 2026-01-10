---
title: How to Insert into a JavaScript Array at a Specific Index – JS Push
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-04-25T18:14:43.000Z'
originalURL: https://freecodecamp.org/news/insert-into-javascript-array-at-specific-index
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/cover-template--11-.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'JavaScript arrays are an important part of the language. They allow you
  to store and manipulate collections of data.

  Sometimes, you may need to insert a new element into an array at a specific index.
  To accomplish this task, you can use the push() me...'
---

JavaScript arrays are an important part of the language. They allow you to store and manipulate collections of data.

Sometimes, you may need to insert a new element into an array at a specific index. To accomplish this task, you can use the `push()` method or the `splice()` method.

In this article, you will learn how to use both techniques in detail.

## How JavaScript Arrays Work

Before we dive into the insertion methods, let's briefly review arrays in JavaScript.

An array is a collection of data values of any data type. You can create arrays using either the array constructor or the literal notation.

Here's an example of an array created using the array constructor:

```js
const arrayConstructor = new Array(1, 2, 3);
console.log(arrayConstructor); // Output: [1, 2, 3]
```

And here's an example of an array created using literal notation:

```js
const literalArray = [1, 2, 3];
console.log(literalArray); // Output: [1, 2, 3]
```

In both cases, you have an array with three elements: `1`, `2`, and `3`.

## How to Insert into a JavaScript Array at a Specific Index With the `push()` Method

The [`push()`](https://www.freecodecamp.org/news/how-to-insert-an-element-into-an-array-in-javascript/) [method in JavaScript arrays](https://www.freecodecamp.org/news/how-to-insert-an-element-into-an-array-in-javascript/) is used to add one or more elements to the end of an array.

Let's look at the syntax of the `push()` method:

```js
array.push(element1, element2, ..., elementN);
```

Here, `array` is the array that you want to add elements to, and `element1`, `element2`, and so on, are the elements you want to add to the end of the array.

For example, let's say you have an array of fruit, and you want to add an element to the end of it:

```js
const fruits = ['apple', 'banana', 'cherry'];
fruits.push('date');
console.log(fruits); // Output: ['apple', 'banana', 'cherry', 'date']
```

In this code, `'date'` is added to the end of the `fruits` array using the `push()` method.

There may be times when you need to insert an element at a specific index in an array. In such a scenario, you can use the `push()` method in combination with array slicing.

Here are the steps to insert an element at a specific index in an array:

1. Create a new empty array.
    
2. Copy the elements before the specific index from the original array to the new array.
    
3. Add the new element to the new array.
    
4. Copy the elements after the specific index from the original array to the new array.
    

Let's illustrate these steps with an example. Suppose you have an array of numbers:

```js
const numbers = [1, 2, 4, 5];
```

And you want to insert the number `3` at index `2` (remember that JavaScript uses zero-based indexing). Here's how you can accomplish this:

```js
const index = 2;
const newNumbers = [
    ...numbers.slice(0, index),
    3,
    ...numbers.slice(index)
];
console.log(newNumbers); // Output: [1, 2, 3, 4, 5]
```

In this example, a new array `newNumbers` is created by copying the elements before index `2` using the `slice()` method. That's followed by the new element `3`, and finally you copy the remaining elements after index `2` using the `slice()` method again. The result is the new array `[1, 2, 3, 4, 5]`.

The spread operator (`...`) in the example above is used to concatenate the arrays.

But this is not a best approach because you end up using another method (`slice`), making the code difficult for a beginner to understand. Let’s explore how to use the splice method which is more straightfoward.

## How to Use the `splice()` Method to Insert into a JavaScript Array at a Specific Index

The `splice()` method in JavaScript arrays is used to add or remove elements from an array. You can use the `splice()` method to insert elements at a specific index in an array.

Here's the syntax of [the `splice()` method](https://joelolawanle.com/posts/slice-vs-splice-javascript-understanding-differences-use):

```js
array.splice(start, deleteCount, item1, item2, ..., itemN);
```

* `array` is the array that you want to modify.
    
* `start` is the index where you want to start modifying the array.
    
* `deleteCount` is the number of elements you want to remove from the array, starting at the `start` index.
    
* `item1`, `item2`, and so on are the elements you want to add to the array at the `start` index.
    

For example, let's say you have an array of numbers:

```js
const numbers = [1, 2, 4, 5];
```

And you want to insert the number `3` at index `2`. Here's how you can accomplish this using the `splice()` method:

```js
numbers.splice(2, 0, 3);
console.log(numbers); // Output: [1, 2, 3, 4, 5]
```

In this code, the `splice()` method is called on the `numbers` array, starting at index `2`, with a `deleteCount` of `0`. You then add the new element `3` to the array at the `start` index. The result is the modified array `[1, 2, 3, 4, 5]`.

## Conclusion

In this article, you have learned the two major techniques for inserting elements into a JavaScript array at a specific index.

The `splice()` method should be your preferred option as it has a better and more straightforward syntax. Knowing these techniques will allow you to manipulate JavaScript arrays more effectively.

Embark on a journey of learning! [Browse 200+ expert articles on web development](https://joelolawanle.com/contents). Check out [my blog](https://joelolawanle.com/posts) for more captivating content from me.

Have fun coding!
