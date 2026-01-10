---
title: 'Higher Order Functions: How to Use Filter, Map and Reduce for More Maintainable
  Code'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-18T15:31:55.000Z'
originalURL: https://freecodecamp.org/news/higher-order-functions-in-javascript-d9101f9cf528
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1uudsYisszFlHUxPiMMpbw.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Guido Schmitz

  Higher order functions can help you to step up your JavaScript game by making your
  code more declarative. That is, short, simple, and readable.

  A Higher Order Function is any function that returns a function when executed, takes
  a fu...'
---

By Guido Schmitz

Higher order functions can help you to step up your JavaScript game by making your code more declarative. That is, short, simple, and readable.

A Higher Order Function is any function that returns a function when executed, takes a function as one or more of its arguments, or both. If you have used any of the `Array` methods like `map` or `filter`, or passed a callback function to jQuery’s `$.get`, you have already worked with Higher Order Functions.

When you use `Array.map`, you provide a function as its only argument, which it applies to every element contained in the array.

```javascript
var arr = [ 1, 2, 3 ];

var arrDoubled = arr.map(function(num) {
  return num * 2;
});

console.log(arrDoubled); // [ 2, 4, 6 ]
```

Higher order functions can also return a function. For example, you can make a function called `multiplyBy` that takes a number and returns a function that multiplies another number you provide by the first number provided. You can use this approach to create a `multiplyByTwo` function to pass to `Array.map`. This will give you the same result you saw above.

```javascript
function multiplyBy(num1) {
  return function(num2) {
    return num1 * num2;
  }
}

var multiplyByTwo = multiplyBy(2);

var arr = [ 1, 2, 3 ];

var arrDoubled = arr.map(multiplyByTwo);

console.log(arrDoubled); // [ 2, 4, 6 ]
```

Knowing when and how to use these functions is essential. They make your code easier to understand and maintain. It also makes it easy to combine functions with each other. This is called composition, and I will not go in much detail here. In this article I will cover the three most used higher order functions in JavaScript. These are `.filter()`, `.map()` and `.reduce()`.

## Filter

Imagine writing a piece of code that accepts a list of people where you want to filter out the people that are equal or above the age of 18.

Our list looks like the one below:

```
const people = [ { name: ‘John Doe’, age: 16 }, { name: ‘Thomas Calls’, age: 19 }, { name: ‘Liam Smith’, age: 20 }, { name: ‘Jessy Pinkman’, age: 18 },];
```

Let’s look at an example of a first order function which select people that are above the age of 18. I’m using an [arrow function](https://hacks.mozilla.org/2015/06/es6-in-depth-arrow-functions) that is part of the ECMAScript standard or ES6 for short. It’s just a shorter way of defining a function and allows you to skip typing function and return, as well as some parentheses, braces, and a semicolon.

```
const peopleAbove18 = (collection) => {  const results = [];   for (let i = 0; i < collection.length; i++) {    const person = collection[i];     if (person.age >= 18) {      results.push(person);    }  }
```

```
  return results;};
```

Now what if we want to select all the people who are between 18 and 20? We could create another function.

```
const peopleBetween18And20 = (collection) => {  const results = [];   for (let i = 0; i < collection.length; i++) {    const person = collection[i];     if (person.age >= 18 && person.age <= 20) {      results.push(person);    }  }
```

```
  return results;};
```

You may already recognize a lot of repeating code here. This could be abstracted into a more generalized solution. These two functions have something in common. They both iterate over a list and filter it on a given condition.

> “A higher order function is a function that takes one or more functions as arguments.”_— [Closurebridge](https://clojurebridge.github.io/community-docs/docs/clojure/higher-order-function/)_

We can improve our previous function by using a more declarative approach, `.filter()`.

```
const peopleAbove18 = (collection) => {  return collection    .filter((person) => person.age >= 18);}
```

That’s it! We can reduce a lot of extra code by using this higher order function. It also make our code better to read. We don’t care how things are being filtered, we just want it to filter. I will go into combining functions later in this article.

## Map

Let’s take the same list of people and an array of names that tells if the person loves to drink coffee.

```
const coffeeLovers = [‘John Doe’, ‘Liam Smith’, ‘Jessy Pinkman’];
```

The imperative way will be like:

```
const addCoffeeLoverValue = (collection) => {  const results = [];   for (let i = 0; i < collection.length; i++) {    const person = collection[i];
```

```
    if (coffeeLovers.includes(person.name)) {      person.coffeeLover = true;    } else {      person.coffeeLover = false;    }     results.push(person);  }   return results;};
```

We could use `.map()` to make this more declarative.

```
const incrementAge = (collection) => {  return collection.map((person) => {    person.coffeeLover = coffeeLovers.includes(person.name);     return person;  });};
```

Again, `.map()` is a high-order function. It allows a function to be passed as an argument.

## Reduce

I bet you will like this function when you know when and how to use it.  
The cool thing about `.reduce()` is that most of the functions above can be made with it.

Let’s take a simple example first. We want to sum up all the people’s ages. Again, we’ll look how this can be done using the imperative approach. It’s basically looping through the collection and increment a variable with the age.

```
const sumAge = (collection) => {  let num = 0;   collection.forEach((person) => {    num += person.age;  });   return num;}
```

And the declarative approach using `.reduce()`.

```
const sumAge = (collection) => collection.reduce((sum, person) => { return sum + person.age;}, 0);
```

We can even use `.reduce()` to create our own implementation of `.map()` and `.filter()` .

```
const map = (collection, fn) => {  return collection.reduce((acc, item) => {    return acc.concat(fn(item));  }, []);}
```

```
const filter = (collection, fn) => {  return collection.reduce((acc, item) => {    if (fn(item)) {      return acc.concat(item);    }     return acc;  }, []);}
```

This might be hard to understand at first. But what `.reduce()` basically does is start with a collection and a variable with an initial value. You then iterate over the collection and append (or add) the values to the variable.

## Combining map, filter and reduce

Great, that these functions exist. But the good part is that they exist on the Array prototype in JavaScript. This means these functions can be used together! This makes it easy to create reusable functions and reduce the amount of code that is required to write certain functionality.

So we talked about using `.filter()` to filter out the people that are equal or below the age of 18. `.map()` to add the `coffeeLover` property, and `.reduce()` to finally create a sum of the age of everyone combined.  
Lets write some code that actually combines these three steps.

```
const people = [ { name: ‘John Doe’, age: 16 }, { name: ‘Thomas Calls’, age: 19 }, { name: ‘Liam Smith’, age: 20 }, { name: ‘Jessy Pinkman’, age: 18 },];
```

```
const coffeeLovers = [‘John Doe’, ‘Liam Smith’, ‘Jessy Pinkman’];
```

```
const ageAbove18 = (person) => person.age >= 18;const addCoffeeLoverProperty = (person) => { person.coffeeLover = coffeeLovers.includes(person.name);  return person;}
```

```
const ageReducer = (sum, person) => { return sum + person.age;}, 0);
```

```
const coffeeLoversAbove18 = people .filter(ageAbove18) .map(addCoffeeLoverProperty);
```

```
const totalAgeOfCoffeeLoversAbove18 = coffeeLoversAbove18 .reduce(ageReducer);
```

```
const totalAge = people .reduce(ageReducer);
```

If you do it the imperative way, you will end up writing a lot of repeating code.

The mindset of creating functions with `.map()` ,`.reduce()` and `.filter()` will improve the quality of the code you’ll write. But it also adds a lot of readability. You don’t have to think about what’s going on inside a function. It’s easy to understand.

Thanks for reading! :)

Say hello on [Twitter](https://twitter.com/guidsen)

