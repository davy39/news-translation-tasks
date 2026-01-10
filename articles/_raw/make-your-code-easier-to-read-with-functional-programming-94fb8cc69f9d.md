---
title: Make your code easier to read with Functional Programming
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-18T10:15:52.000Z'
originalURL: https://freecodecamp.org/news/make-your-code-easier-to-read-with-functional-programming-94fb8cc69f9d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uFGSHrjaQSpCC6_rTKT3Lg.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Pure functions are easier to read and understand. All the function’s dependencies
  are in its definition and are therefore...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Pure functions are easier to read and understand. All the function’s dependencies are in its definition and are therefore easier to see. Pure functions also tend to be small and do one thing. They don’t use `this`, a constant source of confusion.

### Chaining

> **Chaining** is a technique used to simplify code where multiple methods are applied to an object one after another.

[Let’s look and compare](https://jsfiddle.net/cristi_salcescu/5va5dkq7/) the two styles: imperative and functional. In the functional style, I use the basic toolbox for list operations `filter()` and `map()` . Then I chain them together.

I took the case of a collection of tasks. A task has an `id`, a description (`desc`) a boolean `completed`, a `type` and an assigned `user` object. The user object has a `name` property.

```
//Imperative style
let filteredTasks = [];
for(let i=0; i<tasks.length; i++){
    let task = tasks[i];
    if (task.type === "RE" && !task.completed) {
        filteredTasks.push({ ...task, userName: task.user.name });
    }
}

//Functional style
function isPriorityTask(task){
   return task.type === "RE" && !task.completed;
}

function toTaskView(task) {
   return { ...task, userName: task.user.name };
}

let filteredTasks = tasks.filter(isPriorityTask).map(toTaskView);
```

Notice the callbacks for `filter()` and `map()` as **pure functions with intention revealing names.**

> `_map()_` transforms a list of values to another list of values using a mapping function.

Here is a [performance test](https://jsperf.com/make-code-easier-to-read-imperative-vs-functional) measuring the difference between the two styles. It seems that the functional approach is 60% slower. When the imperative process finishes in 10 milliseconds, the functional approach will finish in 16 milliseconds. [In that case](https://jsfiddle.net/cristi_salcescu/v5jegr61/) using the imperative loop will be a premature optimization.

### Point-free style

In the previous example, I have used the point-free style when composing functions. Point-free is a technique that improves readability by eliminating the unnecessary arguments. Consider the next code:

```
tasks.filter(task => isPriorityTask(task)).map(task => toTaskView(task));
```

In a point-free style it is written without arguments:

```
tasks.filter(isPriorityTask).map(toTaskView);
```

For more on point-free look at [How point-free composition will make you a better functional programmer](https://medium.freecodecamp.org/how-point-free-composition-will-make-you-a-better-functional-programmer-33dcb910303a)

### Partial Application

Next, I want to look into how we can improve readability and also reuse an existing function. Before doing that, we need a new function in our toolbox.

> **Partial application** refers to the process of fixing a number of arguments to a function.

> It’s a way to go from generalization to specialization.

For partial application we can use the `partial()` function from a popular library like [underscore.js](http://underscorejs.org/#partial) or [lodash.js](https://lodash.com/docs/4.17.5#partial). The `bind()` method can also do partial application.

Let’s say we want to refactor [the following imperative code](https://jsfiddle.net/cristi_salcescu/9p0ffasn/) to a functional, easier to read, style:

```
let filteredTasks = [];
for(let i=0; i<tasks.length; i++){
    let task = tasks[i];
    if (task.type === "NC") {
        filteredTasks.push(task);
    }
}
```

As I said, this time we want to create a generic function that can be used for filtering by any task type. `isTaskOfType()` is the generic function. The `partial()` function is used to create a new predicate function `isCreateNewContent()` that filters by a specific type.

> **A predicate function** is a function that takes one value as input and returns true/false based on whether the value satisfies the condition.

```
function isTaskOfType(type, task){
  return task.type === type;
}

let isCreateNewContent = partial(isTaskOfType, "NC");
let filteredTasks = tasks.filter(isCreateNewContent);
```

Notice the predicate function. It has a name expressing its intention. When I’m reading `tasks.filter(isCreateNewContent)` I clearly understand what kind of `tasks` I’m selecting.

> `filter()` selects values from a list based on a predicate function that decides what values should be kept.

### Reduce

[I will start a new example](https://jsfiddle.net/cristi_salcescu/zo9zkrcc/) using a shopping list. Here is how the list may look like:

```
let shoppingList = [
   { name : "orange", units : 2, price : 10, type : "FRT"},
   { name : "lemon", units : 1, price : 15, type : "FRT"},
   { name : "fish", units : 0.5, price : 30, type : "MET"}
];
```

I will compute the total price and the price for fruits only. Below is the imperative style:

```
let totalPrice = 0, fruitsPrice = 0;
for(let i=0; i<shoppingList.length; i++){
   let line = shoppingList[i];
   totalPrice += line.units * line.price;
   if (line.type === "FRT") {
       fruitsPrice += line.units * line.price;
   }
}
```

Taking the functional approach in this case will require the use of `reduce()` to compute the total price.

> `reduce()` reduces a list of values to one value.

As we did before, we create new functions for the required callbacks and give them intention revealing names : `addPrice()` and `areFruits()`.

```
function addPrice(totalPrice, line){
   return totalPrice + (line.units * line.price);
}

function areFruits(line){
   return line.type === "FRT";
}

let totalPrice = shoppingList.reduce(addPrice,0);
let fruitsPrice = shoppingList.filter(areFruits).reduce(addPrice,0);
```

### Conclusion

Pure functions are easier to read and reason about.

Functional Programming will break list operations in steps like: filter, map, reduce, sort. At the same time, it will require to define new pure small functions to support those operations.

Combining Functional Programming with the practice of giving intention revealing names greatly improves the readability of the code.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)

