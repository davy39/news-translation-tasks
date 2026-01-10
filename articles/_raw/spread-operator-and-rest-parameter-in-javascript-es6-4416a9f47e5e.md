---
title: An intro to the spread operator and rest parameter in JavaScript (ES6)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T16:53:29.000Z'
originalURL: https://freecodecamp.org/news/spread-operator-and-rest-parameter-in-javascript-es6-4416a9f47e5e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lC-MTayAodosjbtLk8zL1A.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Joanna Gaudyn

  Both the spread operator and the rest parameter are written as three consecutive
  dots (…). Do they have anything else in common?


  _[source](https://unsplash.com/photos/8AJuvX4hzws" rel="noopener" target="blank"
  title=")

  The spread op...'
---

By Joanna Gaudyn

#### Both the spread operator and the rest parameter are written as three consecutive dots (…). Do they have anything else in common?

![Image](https://cdn-media-1.freecodecamp.org/images/xVf5V7-nilHXYj2WtcgAgE8QNW-DY6I23NS5)
_[source](https://unsplash.com/photos/8AJuvX4hzws" rel="noopener" target="_blank" title=")_

### The spread operator (…)

The spread operator was introduced in ES6. It provides you with the ability to expand [iterable objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators#Iterators) into multiple elements. What does it really mean? Let’s check some examples.

```
const movies = ["Leon", "Love Actually", "Lord of the Rings"];console.log(...movies);
```

Prints:

> Leon Love Actually Lord of the Rings

```
const numbers = new Set([1, 4, 5, 7]);console.log(...numbers);
```

Prints:

> 1 4 5 7

You might notice that both the array from the first example and the set from the second one have been expanded into their individual elements (strings and digits respectively). How can this be of any use, you may ask.

The most common use is probably combining arrays. If you ever had to do this in the times before the spread operator, you probably used the `concat()` method.

```
const shapes = ["triangle", "square", "circle"];const objects = ["pencil", "notebook", "eraser"];const chaos = shapes.concat(objects);console.log(chaos);
```

Prints:

> [“triangle”, “square”, “circle”, “pencil”, “notebook”, “eraser”]

That’s not too bad, but what the spread operator offers is a shortcut, which makes your code look way more readable too:

```
const chaos = [...shapes, ...objects];console.log(chaos);
```

Prints:

> [“triangle”, “square”, “circle”, “pencil”, “notebook”, “eraser”]

Here’s what we’d get if we tried doing the same _without_ the spread operator:

```
const chaos = [shapes, objects];console.log(chaos);
```

Prints:

> [Array(3), Array(3)]

What happened here? Instead of combining the arrays, we got a `chaos` array with the `shapes` array at index 0 and the `objects` array at index 1.

![Image](https://cdn-media-1.freecodecamp.org/images/FWmzdtMxBzeGEB1G5byEABuOfQOA6QkCu82f)
_[source](https://unsplash.com/photos/DJpJDdeCrag" rel="noopener" target="_blank" title=")_

### The rest parameter (…)

You can think of the rest parameter as the opposite of the spread operator. Just as the spread operator allows you to expand an array into its individual elements, the rest parameter lets you bundle elements back into an array.

#### Assigning values of an array to variables

Let’s have a look at the following example:

```
const movie = ["Life of Brian", 8.1, 1979, "Graham Chapman", "John Cleese", "Michael Palin"];const [title, rating, year, ...actors] = movie;console.log(title, rating, year, actors);
```

Prints:

> “Life of Brian”, 8.1, 1979, [“Graham Chapman”, “John Cleese”, “Michael Palin”]

The rest parameter let us take the values of the `movie` array and assign them to several individual variables using [destructuring](https://medium.com/@aska.gaudyn/destructuring-in-javascript-es6-ee963292623a). This way `title`, `rating`, and `year` are assigned the first three values in the array, but where the real magic happens is `actors`. Thanks to the rest parameter, `actors` gets assigned the remaining values of the `movie` array, in form of an array.

#### Variadic functions

Variadic functions are functions which take an indefinite number of arguments. One good example is the `sum()` function: we can’t know upfront how many arguments will be passed to it:

```
sum(1, 2);sum(494, 373, 29, 2, 50067);sum(-17, 8, 325900);
```

In earlier versions of JavaScript, this kind of function would be handled using the [arguments object,](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments) which is an array-like object, available as a local variable inside every function. It contains all values of arguments passed to a function. Let’s see how the `sum()` function could be implemented:

```
function sum() {  let total = 0;    for(const argument of arguments) {    total += argument;  }  return total;}
```

It does work, but it’s far from perfect:

* If you look at the definition for the `sum()` function, it doesn’t have any parameters. It can be quite misleading.
* It can be hard to understand if you’re not familiar with the arguments object (as in: where the heck are the `arguments` coming from?!)

Here’s how we’d write the same function with the rest parameter:

```
function sum(...nums) {  let total = 0;    for(const num of nums) {    total += num;  }  return total;}
```

Note that the `for...in` loop has been replaced with the `[for...of](https://medium.freecodecamp.org/javascript-iterators-17ab32c3cae7)` [loop](https://medium.freecodecamp.org/javascript-iterators-17ab32c3cae7) as well. We made our code more readable and concise at once.

Hallelujah ES6!

Are you just starting your journey with programming? Here’s some articles that might interest you as well:

* [Is a coding bootcamp something for you?](https://medium.freecodecamp.org/is-a-coding-bootcamp-something-for-you-974c3b5bd3b2)
* [Is career change really possible?](https://medium.com/datadriveninvestor/is-career-change-really-possible-c29c9a0d791c)
* [Why Ruby is a great language to start programming with](https://medium.com/@aska.gaudyn/why-ruby-is-a-great-language-to-start-programming-with-2f17e0c2907a)

