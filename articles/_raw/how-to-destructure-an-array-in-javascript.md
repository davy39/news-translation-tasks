---
title: How to Destructure an Array in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-05T14:38:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-destructure-an-array-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/code-1839406_1920.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Madison Kanna

  Array destructuring is an efficient way to extract multiple values from data that’s
  stored in an array.

  In this tutorial we’ll learn about array destructuring. We''ll go over examples
  to learn the ins and outs of how array destructuri...'
---

By Madison Kanna

Array destructuring is an efficient way to extract multiple values from data that’s stored in an array.

In this tutorial we’ll learn about array destructuring. We'll go over examples to learn the ins and outs of how array destructuring works. 

I've also created a video of this tutorial:

%[https://www.youtube.com/watch?v=x-ih5R5-DCc]

Let's get started.

Let’s open up our web browser and then open up our JavaScript console where we'll be writing our code. You can find instructions for how to open the console [here](https://balsamiq.com/support/faqs/browserconsole/).

## How to Destructure Elements from an Array

Next we will create an array, called animals, and add values of dog, cat, and horse. 

`const animals = ['Dog', 'Cat', 'Horse']`

Next, say that we want to create a variable with just the value of dog. We'll call this variable `dogVar`, short for dog variable. Before array destructuring was introduced in ES6, we would do this: 

`dogVar = animals[0]`

Next say we want the value of cat and horse in their own variables as well. We would say:

`const catVar = aniamls[1]`

`const horseVar = animals[2]`

Here we’ve written 3 separate lines of code. Let’s use array destructuring instead, and write 1 line of code instead of 3.

## How Destructuring Works

With array destructuring, we could write out just 1 line of code:

`const [firstElement, secondElement, thirdElement] = animals`  
  
This looks like we are creating an array here, but we are not. We are **destructuring** this array. Destructuring makes it possible to unpack values from arrays into distinct variables.

Destructuring takes each variable on the array on the left-hand side and maps it to the element at the _same index_ in the `animals` array.

When we write out `firstElement`, we are saying we want to get access to the first element in the animals array and _assign it_ to the variable of `firstElement.` 

With `secondElement`, we are saying we want to get access to the second element in the array and assign it to the variable of `secondElement`. The same thing goes for the `thirdElement` variable.

The key takeaway here is that these names `[firstElement, secondElement, thirdElement]` don’t matter. What matters is the order. 

Looking at the _order_ of our destructuring will tell us what elements in the array are assigned to what variables.

Let's look at our 1 line of code where we destructure the array. Let's picture this part of it `[firstElement, secondElement, thirdElement]` to be an array. 

If this were an array, `firstElement` would be at position `0` of the array. JavaScript will see that this `firstElement` variable is at position `0`, then it will go into the `animals` array and find the element that's at position `0`, and assign that element to the variable `firstElement`.

(Keep in mind that arrays are zero-indexed, which just means we start counting them at 0 instead of 1.)  
  
When destructuring, we can give our variables any name we want. Again, order is what matters, not the naming. If we wanted to, we could write:

`const [dog, cat, horse] = animals` 

Now we have all of our values. If we write out `dog, cat, horse`, we can see we get all of the variable names with the correct values:

`dog // returns 'Dog'`

`cat // returns 'Cat'`

`horse // returns 'Horse'`

If we go back to our code at the start of this example, we had 3 lines of code to create variables for dog, cat, and horse. With array destructuring, we use just 1 line of code. Destructuring is just a shortcut. It's an easy, quick way to extract multiple values from an array.

But what if you only want to get one element from an array, say the second or third element in an array, and store that element in a variable?

## How to Destructure the Second or Third Element in an Array

Next, let's say we have an array, fruits:

`const Fruits = ['banana', 'apple', 'orange']`

What if we want to get just the value of apple, and assign it to the variable name of apple?

We can’t just do `const [apple] = animals`. Why not?  If we do, then the variable `apple` will incorrectly have the value of  `'banana'` assigned to it. Why is this?  
  
This is because again, order matters. With `const [apple] = fruits`, JavaScript looks at `apple`, sees that it is at position `0`, and then finds the element at position 0 in the `fruits` array, which is `'banana'`, and assigns that element to the variable of apple. 

We don't want this to happen. So what do we do?

Instead, we can write: `const [, apple] = fruits`

This comma is acting as a sort of placeholder. This comma is telling JavaScript to act as if a first element is there, and so this `apple` variable is now the second element here. In other words, `apple` is now at position `1`.

Say we just wanted the value of `orange` in a variable, and we don't care about the apple or banana elements. We could again use commas like so:

`const [, , orange] = fruits`

If we write out `orange` in our console, we see that we successfully created the orange variable and it has the value of `'orange'`.

One last thing to note is that if you learn React, you'll likely use array destructuring often with React hooks. For example, you might see something like this:

`const [count, setCount] = useState(0)`

There we go. We've learned all about array destructuring. 

Thank you for reading!

If you enjoyed this post, **join my [coding club](https://madisonkanna.us14.list-manage.com/subscribe/post?u=323fd92759e9e0b8d4083d008&id=033dfeb98f),** where we tackle coding challenges together every Sunday and support each other as we learn new technologies.

If you have feedback or questions on this post, or find me on Twitter [@madisonkanna](https://twitter.com/Madisonkanna).

  

