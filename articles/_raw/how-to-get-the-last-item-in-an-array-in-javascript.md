---
title: How to Get the Last Item in an Array in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-17T21:21:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-the-last-item-in-an-array-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/web-design-g911869a8e_1920.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Madison Kanna

  When you’re programming in JavaScript, you might need to get the last item in an
  array. In this tutorial, we’ll go over two different ways to do this.

  How to Get the Last Item in a JavaScript Array

  Method 1: Use index positioning

  Use...'
---

By Madison Kanna

  
When you’re programming in JavaScript, you might need to get the last item in an array. In this tutorial, we’ll go over two different ways to do this.

## How to Get the Last Item in a JavaScript Array

### Method 1: Use index positioning

Use index positioning if you know the length of the array.

Let’s create an array:

```js
const animals = [‘cat’, ‘dog’, ‘horse’]
```

Here we can see that the last item in this array is `horse.`

To get the last item, we can access the last item based on its index:

`const finalElement = animals[2]`;

JavaScrip arrays are zero-indexed. This is why we can access the `horse` element with `animals[2].` If you aren't sure on what zero-indexed means, we'll go over it later on in this tutorial.  
  
This method of getting the final item in the array works if you know the length of the array. 

But what if you don’t know the length of the array? This array, `animals`, is very small. But you could have another array that has dozens of items in it, and you might not know its length.

### Method 2: When you don't know the array length

To get the last item in an array when you don’t know the length of that array:

`const lastItem = animals[animals.length - 1]`;

The `lastItem` variable now holds the value of `horse.`

Let's break down what's happening in the above line. First of all, let's just console log `animals.length:`

`console.log(animals.length);` 

If you aren't familiar with the `length` property, it returns the length of this array. This prints out `3`, because there are `3` items in the array.

Earlier we learned that JavaScript arrays are zero-indexed. This just means that in JavaScript arrays, you start counting from zero instead of from one. We can see this by looking at our `animals` array. `cat` is at index `0`, `dog` is at index `1`, and `horse` is at index `2`. 

You might still be confused. We just learned that `animals.length` will tell us how many items are in an array. We also learned that with JavaScript arrays, we start counting from zero instead of one. But how does this help explain why we can get the last item in this array by using `animals[animals.length - 1]?` 

Let's imagine for a moment that JS arrays were _not_ zero-indexed, and we started counting from 1, which is the way we normally count things in the real world. 

With the `animals` array, we could quickly start counting and say that `cat`, the first item, has an index of 1, `dog` has an index of `2`, and `horse` has an index of `3`. The key insight here is that, in one-based indexing, the _index of the last item is the length of the array._ If the array has a length of 3, you know that the last element in the array has an index of `3`. So `animals[3]` would evaluate to `horse`.

Yet JavaScript arrays start from `0.`So if we want to figure out the index of the last item in a JavaScript array, we can subtract 1 from the length of the array:

`animals[animals.length - 1]`;

Inside of the brackets, `animals.length - 1` evaluates to `2`. We now have the last item in the array. 

In this article, we've learned two methods for how to get the last item in a JavaScript array.

Thank you for reading!

**If you enjoyed this post, join my [coding club](https://madisonkanna.us14.list-manage.com/subscribe/post?u=323fd92759e9e0b8d4083d008&id=033dfeb98f), where we tackle coding challenges together every Sunday and support each other as we learn new technologies.**

**If you have feedback or questions on this post, or find me on Twitter [@madisonkanna](https://twitter.com/Madisonkanna).**

  


  

