---
title: Let’s experiment with functional generators and the pipeline operator in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-11T00:13:36.000Z'
originalURL: https://freecodecamp.org/news/lets-experiment-with-functional-generators-and-the-pipeline-operator-in-javascript-520364f97448
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RJoQmQ7L6UZKQ14lYCN6EA.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!


  A generator is a function that returns the next value from the sequence each time
  it is called.


  Combining functional ge...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

> _A generator is a function that returns the next value from the sequence each time it is called._

Combining functional generators with the pipeline operator and pure functions with intention revealing names, allows to write code in a more expressive manner, without creating intermediary lists:

```js
import { sequence, filter, map, take, toList } from "./sequence";

const filteredTodos =
  sequence(todos) 
  |> filter(isPriorityTodo) 
  |> map(toTodoView)
  |> take(10)  
  |> toList;
```

Let’s see how.

I’ll start with a simple functional generator that gives the next integer each time is called. It starts from 0.

```js
function sequence() {
  let count = 0;
  return function() {
    const result = count;
    count += 1;
    return result;
  }
}

const nextNumber = sequence();
nextNumber(); //0
nextNumber(); //1
nextNumber(); //2
```

`nextNumber()` is an infinite generator. `nextNumber()` is also a closure function.

### Finite generator

Generators can be finite. Check the next example where `sequence()` creates a generator that returns consecutive numbers from a specific interval. At the end of the sequence it returns `undefined`:

```js
function sequence(from, to){
 let count = from;
 return function(){
   if(count< to){
      const result = count;
      count += 1;
      return result;
    }
  }
}

const nextNumber = sequence(10, 15);
nextNumber(); //10
nextNumber(); //12
nextNumber(); //13
nextNumber(); //14
nextNumber(); //undefined
```

### toList()

When working with generators, we may want to create a list with all the values from the sequence. For this situation, we need a new function `toList()` that takes a generator and returns all the values from the sequence as an array. The sequence should be finite.

```js
function toList(sequence) {
  const arr = [];
  let value = sequence();
  while (value !== undefined) {
    arr.push(value);
    value = sequence();
  }
  return arr;
}
```

Let’s use it with the previous generator.

```js
const numbers = toList(sequence(10, 15));
//[10,11,12,13,14]
```

### The pipeline operator

A pipeline is a series of data transformations where the output of one transformation is the input of the next one.

The pipeline operator `|>` enables us to write data transformations in a more expressive way. The pipeline operator provides syntactic sugar over function calls with a single argument. Consider the next code:

```js
const shortText = shortenText(capitalize("this is a long text"));

function capitalize(text) {
  return text.charAt(0).toUpperCase() + text.slice(1);
}

function shortenText(text) {
  return text.substring(0, 8).trim();
}
```

With the pipeline operator the transformation can be written like this:

```js
const shortText = "this is a long text" 
  |> capitalize 
  |> shortenText;
  //This is
```

At this moment the pipeline operator is experimental. You can try it using Babel:

* in `package.json` file add the babel pipeline plugin:

```json
{
  "dependencies": {
    "@babel/plugin-syntax-pipeline-operator": "7.2.0"
  }
}
```

* in the `.babelrc` configuration file add:

```
{
  "plugins": [["@babel/plugin-proposal-pipeline-operator", {
             "proposal": "minimal" }]]
}
```

### Generators over collections

In [Make your code easier to read with Functional Programming](https://medium.freecodecamp.org/make-your-code-easier-to-read-with-functional-programming-94fb8cc69f9d) I had an example of processing a list of `todos` . Here is the code:

```js
function isPriorityTodo(task) {
  return task.type === "RE" && !task.completed;
}

function toTodoView(task) {
  return Object.freeze({ id: task.id, desc: task.desc });
}

const filteredTodos = todos.filter(isPriorityTodo).map(toTodoView);
```

In this example, the `todos` list goes through two transformations. First a filtered list is created, then a second list with the mapped values is created.

With generators, we can do the two transformations and create only one list. For this, we need a generator `sequence()` that gives the next value from a collection.

```js
function sequence(list) {
  let index = 0;
  return function() {
    if (index < list.length) {
      const result = list[index];
      index += 1;
      return result;
    }
  };
}
```

#### filter() and map()

Next, we need two decorators `filter()` and `map()`, that work with functional generators.

`filter()` takes a generator and creates a new generator that only returns the values from the sequence that satisfies the predicate function.

`map()` takes a generator and creates a new generator that returns the mapped value.

Here are the implementations:

```js
function filter(predicate) {
  return function(sequence) {
    return function filteredSequence() {
      const value = sequence();
      if (value !== undefined) {
        if (predicate(value)) {
          return value;
        } else {
          return filteredSequence();
        }
      }
    };
  };
}

function map(mapping) {
  return function(sequence) {
    return function() {
      const value = sequence();
      if (value !== undefined) {
        return mapping(value);
      }
    };
  };
}
```

I would like to use these decorators with the pipeline operator. So, instead of creating `filter(sequence, predicate){ }` with two parameters, I created a curried version of it, that will be used like this: `filter(predicate)(sequence)`. This way, it works nicely with the pipeline operator.

Now that we have the toolbox, made of `sequence`, `filter`, `map` and `toList` functions, for working with generators over collections, we can put all of them in a module (`"./sequence"`). See below for how to rewrite the previous code using this toolbox and the pipeline operator:

```js
import { sequence, filter, map, take, toList } from "./sequence";

const filteredTodos =
  sequence(todos) 
  |> filter(isPriorityTodo) 
  |> map(toTodoView) 
  |> toList;
```

Here is a [performance test](https://jsperf.com/functional-generators-vs-array-methods/1) measuring the difference between using array methods and using functional generators. It seems that the approach with functional generators is 15–20% slower.

#### reduce()

Let’s take another example that computes the price of fruits from a shopping list.

```js
function addPrice(totalPrice, line){
   return totalPrice + (line.units * line.price);
}

function areFruits(line){
   return line.type === "FRT";
}

let fruitsPrice = shoppingList.filter(areFruits).reduce(addPrice,0);
```

As you can see, it requires us to create a filtered list first and then it computes the total on that list. Let’s rewrite the computation with functional generators and avoid the creation of the filtered list.

We need a new function in the toolbox: `reduce()`. It takes a generator and reduces the sequence to a single value.

```js
function reduce(accumulator, startValue) {
  return function(sequence) {
    let result = startValue;
    let value = sequence();
    while (value !== undefined) {
      result = accumulator(result, value);
      value = sequence();
    }
    return result;
  };
}
```

`reduce()` has immediate execution.

Here is the code rewritten with generators:

```js
import { sequence, filter, reduce } from "./sequence";

const fruitsPrice = sequence(shoppingList) 
  |> filter(areFruits) 
  |> reduce(addPrice, 0);
```

#### take()

Another common scenario is to take only the first `n` elements from a sequence. For this case we need a new decorator `take()`, that receives a generator and creates a new generator that returns only the first `n` elements from the sequence.

```js
function take(n) {
  return function(sequence) {
    let count = 0;
    return function() {
      if (count < n) {
        count += 1;
        return sequence();
      }
    };
  };
}
```

Again, this is the curried version of `take()` that should be called like this: `take(n)(sequence)`.

Here is how you can use `take()` on an infinite sequence of numbers:

```js
import { sequence, toList, filter, take } from "./sequence";

function isEven(n) {
  return n % 2 === 0;
}

const first3EvenNumbers = sequence()  
  |> filter(isEven) 
  |> take(3) 
  |> toList;
  //[0, 2, 4]
```

I remade the previous [performance test](https://jsperf.com/functional-generators-vs-array-methods/4) and use `take()` to process only the first 100 items. It turns out that the version with functional generators is a lot faster (like 170 times faster).

```js
let filteredTodos = todos
 .filter(isPriorityTodo)
 .slice(0, 100)
 .map(toTodoView);
//320 ops/sec

let filteredTodos =
const filteredTodos =
  sequence(todos) 
  |> filter(isPriorityTodo) 
  |> map(toTodoView)
  |> take(100)
  |> toList;
//54000 ops/sec
```

### Custom generators

We can create any custom generator and use it with the toolbox and the pipeline operator. Let’s create the Fibonacci custom generator:

```js
function fibonacciSequence() {
  let a = 0;
  let b = 1;
  return function() {
    const aResult = a;
    a = b;
    b = aResult + b;
    return aResult;
  };
}

const fibonacci = fibonacciSequence();
fibonacci();
fibonacci();
fibonacci();
fibonacci();
fibonacci();

const firstNumbers = fibonacciSequence()  
  |> take(10) 
  |> toList;
  //[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Conclusion

The pipeline operator makes data transformation more expressive.

Functional generators can be created over finite or infinite sequences of values.

With generators we can do list processing without creating intermediary lists at each step.

You can check all the samples on [codesandbox](https://codesandbox.io/s/rj2r9mxl0n).

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)

