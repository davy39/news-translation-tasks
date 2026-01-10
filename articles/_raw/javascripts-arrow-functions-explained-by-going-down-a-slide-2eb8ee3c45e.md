---
title: JavaScript’s arrow functions explained by going down a slide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-24T22:23:35.000Z'
originalURL: https://freecodecamp.org/news/javascripts-arrow-functions-explained-by-going-down-a-slide-2eb8ee3c45e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HVh2O4VIKLxLoPH9CjZztA.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kevin Kononenko

  If you have ever gone down a water slide, then you can understand arrow functions.


  If you have been using JavaScript for a few years, you are probably familiar with
  this syntax:

  function addTen(num){  return num + 10;});

  console.l...'
---

By Kevin Kononenko

#### If you have ever gone down a water slide, then you can understand arrow functions.

![Image](https://cdn-media-1.freecodecamp.org/images/Au60r4itPIeaPi5dHkcuwlKSk37qb2FjvroV)

If you have been using JavaScript for a few years, you are probably familiar with this syntax:

```
function addTen(num){  return num + 10;});
```

```
console.log(addTen(2));//12
```

This function syntax was popular in ES5, or ECMAScript 5.

There is one major advantage to this syntax: It includes the word function, so it is obvious that you are writing a function!

A function clearly takes in anywhere from 0 to many arguments and runs a specific set of statements every time that it is called.

But then the world of JavaScript took a leap forward with ES6 in 2015.

Now, the same function as above would be written like this:

```
let addTen = (num) => num + 10;
```

```
console.log(addTen(2));//12
```

Now, there is no _function_ keyword, and no return statement! Functions in ES6 are much more terse, or concise.

So, since those obvious clues have been removed, you might be having a little bit of a hard time with understanding the different parts of arrow functions.

Fortunately, as you will soon see with a few animations, arrow functions are pretty easy to understand once you learn to visualize the arrow “=>” in a new way.

So here is how arrow functions are just like a water slide. In order to fully understand this tutorial, it might help to know about [map functions](https://blog.codeanalogies.com/2018/02/20/javascript-map-method-explained-by-going-on-a-hike/) and [scoping](https://blog.codeanalogies.com/2017/11/22/how-javascript-variable-scoping-is-just-like-multiple-levels-of-government/).

### Arrow Functions Visualized

Let’s explore the addTen function a little more deeply.

```
let addTen = (num) => num + 10;
```

```
console.log(addTen(2));//12
```

This function will transform one parameter and output that parameter with 10 added.

The transformation happens with that subtle “=>” arrow.

I like to transform that arrow into a tube slide in my mind to show what is actually happening. Here is what I mean:

![Image](https://cdn-media-1.freecodecamp.org/images/Ps5SxrF558e8ywvcBoSFDzNQUKwussni3Ci-)

The equals sign is like the tube slide and the arrow is like the landing pad.

Arrow functions follow this pattern:

(parameters) => {statements}

So let’s add those to the diagram with our addTen function example.

![Image](https://cdn-media-1.freecodecamp.org/images/fXH4R-oTUpaYcc8kWG3nhLRuBmL5LlirC1o-)

The last thing we need to show is how the parameter, which is 10 in this case, goes down the slide and becomes available in the statements of the function. Here’s what that looks like.

![Image](https://cdn-media-1.freecodecamp.org/images/eS7jMV7kl-h6mChbh1VVJ9Rq5HbDk6ArTM6R)

That’s all it is! Pretty straightforward.

Now, let’s look at an example where there are two different parameters. Here is our new function:

```
let multiply = (num1, num2) => {return num1 * num2};
```

```
console.log(multiply(2, 10));//20
```

In this case we are just multiplying the two parameters together. Both will go down the slide together. Like this:

![Image](https://cdn-media-1.freecodecamp.org/images/dsHfwfhAlIBdb3jU7erDG0lSf-6dvWv6DAxr)

There’s one more example you should know about- combining the map() method with arrow functions.

The map() method will send every element in an array into the arrow function, in order.

Let’s go through an example: imagine that you have an array of numbers, and you want to get the square root of each one.

Here’s the code.

```
let nums = [1, 4, 9];
```

```
let squares = nums.map((num) => {  return Math.sqrt(num);});
```

```
console.log (squares)// [1, 2, 3]
```

You need to know a little about the map method to understand this one. But, you will probably notice the terse syntax yet again — the map() method is much shorter than writing a for() loop.

Here’s what is happening in this code:

![Image](https://cdn-media-1.freecodecamp.org/images/NiM1EAFP57EsIPOVr-Q5bQUD7AgCkHgK7b5B)

1. There are three elements in the _nums_ array, so the _num_ parameter goes down the slide 3 times.
2. The Math.sqrt() method takes the square root of the number each time.
3. The result is stored in the _squares_ array each time.

### The Difference Between Arrow Functions And Traditional Functions

You might be wondering… is this simply a difference in syntax?

Actually, there is one important way that the traditional ES5 functions and ES6 functions work differently.

The big change is that arrow functions do not have their own scope. Therefore, if you try to use the _this_ keyword, you will be surprised when it does not refer to the scope of the arrow function.

To go back to our slide analogy, this means that _this_ is the same at the top and bottom of the slide. If we were using ES5 functions, then _this_ would be different at the top and bottom of the slide.

To quickly recognize this in code, just look for the _function_ keyword. If you see it, that means that a new scope is being created. If not, assume that you are using the scope of the enclosing function.

### Enjoy this Visual Tutorial?

If you enjoyed this tutorial, give it a “clap”! Or, if you would like to read more visual tutorials about HTML, CSS and JavaScript, check out the [main CodeAnalogies site](http://codeanalogies.com/) for 50+ tutorials.

