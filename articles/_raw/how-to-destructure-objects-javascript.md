---
title: How to Destructure Objects in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-21T16:47:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-destructure-objects-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/code--f7df1e--3-.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Madison Kanna\nSince ECMAScript 6 (or ES6 for short), you can descructure\
  \ objects in JavaScript. As a JavaScript developer, you’ll likely destructure objects\
  \ as part of your daily work. \nLet's learn about why we use destructuring, and\
  \ then we'll le..."
---

By Madison Kanna

Since ECMAScript 6 (or ES6 for short), you can descructure objects in JavaScript. As a JavaScript developer, you’ll likely destructure objects as part of your daily work. 

Let's learn about why we use destructuring, and then we'll learn how to destructure JavaScript objects.

<h1>Why destructure an object?</h1>

Let's go over an example to help us understand why we would want to destructure an object in the first place. Let's create an object with the name of `pet`:

```javascript
const pet:  = {
 name: 'Captain',
 food: 'Kibble',
 color: 'Black'
};
```

Let's say we want to simply print out the pet's food. We could do so like this:

```
console.log(pet.food);
```

This would output `kibble` to the console. However, it's tedious to write out `pet.name` every time we need the food value. So before ES6, JavaScript developers would do this:

```
const food = pet.food;
```

Here, we declare a variable named `food` and said to point that variable at the value stored inside of `pet.food`, which is `kibble`. We can demonstrate that we've done this by adding this line of code:

```js
console.log(food); // output: kibble
```

However, say we want to do the same with the rest of our properties in the `pet` object:

```js
const name = pet.name;
const food = pet.food;
const color = pet.color;
```

This starts to get verbose. This is where **destructuring** comes in.

<h1>How to Destructure An Object in JavaScript</h2>

Instead of writing out `const food = pet.food`, we can utilize destructuring and simply write: 

````
const { food } = pet;
```

Now if we print out `food` again, we can see we've created the `food` variable:

```js
console.log(food); // output: kibble
```

Using destructuring, our code is now more concise and dry. This is why JavaScript developers started using destructuring once it was introduced in ES6. 

Let's pause for a moment and look at this line again: 

```
const { food } = pet;
```

What is happening here?

Remember, within a JavaScript object, a **property** is a key/value pair. The key is a string, and the value can be any data type. In the `pet` object, one of the keys is `food`, and its corresponding value is `kibble`.  

When we wrap our `food` variable in brackets, we look inside of our `pet` object for a property with the same name. We create a new variable with the name `food`, and we set its value to `kibble`, the corresponding value of that key.

If you'd like to destructure multiple properties and their keys from an object, you can do so like this:

```
const { name, food, color } = pet;
```

Now if you print out these variables, you'll see that they all now exist:

```js
console.log(name, food, color) // output: captain chewtoy black
```

In this article, we've learned how to destructure objects and why we'd want to. We've also learned how to destructure multiple properties from an object.

Thank you for reading!

**If you enjoyed this post, join my [coding club](https://madisonkanna.us14.list-manage.com/subscribe/post?u=323fd92759e9e0b8d4083d008&id=033dfeb98f), where we tackle coding challenges together every Sunday and support each other as we learn new technologies.**

**If you have feedback or questions on this post, or find me on Twitter [@madisonkanna](https://twitter.com/Madisonkanna).**

  

