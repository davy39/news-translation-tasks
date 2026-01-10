---
title: How to Use Callbacks and Higher Order Functions in JavaScript
subtitle: ''
author: Franklin Okolie
co_authors: []
series: null
date: '2024-01-12T18:07:08.000Z'
originalURL: https://freecodecamp.org/news/callbacks-higher-order-functions-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/higher-order-callbacks.png
tags:
- name: callbacks
  slug: callbacks
- name: functions
  slug: functions
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: The way functions are treated and used in JavaScript is quite interesting.
  They are very flexible – we can assign functions as a value to a variable, return
  them as a value from another function, and pass them as an argument to another function.
  We c...
---

The way functions are treated and used in JavaScript is quite interesting. They are very flexible – we can assign functions as a value to a variable, return them as a value from another function, and pass them as an argument to another function. We can do all this because JavaScript treats functions as **first class citizens**.

In this article, I'll go over what higher order functions and callbacks are, and how they work in JavaScript.

## Functions as First Class Citizens in JavaScript

Functions are defined as [first class citizens](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function) or first class objects in JavaScript because functions are treated like variables.

This means that functions in JavaScript can be:

* Passed as an argument to a another function.
* Assigned as a value to a variable.
* Returned as a value from a function.

It is essential to understand how functions are treated in JavaScript, as they serve as a building block to understanding higher order and callback functions in JavaScript and how they work.

## What are Higher Order Functions?

Higher order functions are functions that take functions as arguments and also return a function as a value. 

There are a lot of built-in higher order functions provided in JavaScript. We'll take a look at some and take advantage of how functions are treated as first class citizens. We'll also create our own higher order functions.

First, let's take a look at some examples of built-in higher order functions.

### Array Methods 

Array methods are usually the first introduction of higher order functions a developer will have when learning JavaScript. These include, but are not limited to, the `map`, `filter`, `forEach`, `find`, `findIndex`, `some`, and `every` array methods provided by JavaScript.  
  
These array methods or functions have a lot in common, but one of the most common feature is that they all accept a function as an argument. Below is a code snippet that demonstrates how the `forEach` array method works:

```javascript
const people = [
  { firstName: "Jack", year: 1988 },
  { name: "Kait", year: 1986 },
  { name: "Irv", year: 1970 },
  { name: "Lux", year: 2015 },
];

people.forEach(function (person) {
  console.log(person);
});

// Output:  Logs every person object in the array
```

From the code sample above, we can see that the `forEach` method accepts a function as an argument which it calls on every iteration on the array. Therefore the `forEach` array method is a higher order function.

### Timer Events

Another set of commonly used built-in higher order functions are the `setInterval` and `setTimeout` functions, known as timer events in JavaScript.

Each function accepts a function as one of its arguments and uses it to create a timed event.

Take a look at the code sample below to see how `setTimeout` works:

```javascript
setTimeout(function () {
  console.log("This is a higher order function");
}, 1000);

// Output: "This is a higher order function" after 1000ms / 1 second

```

The code snippet above is the most basic example of how a `setTimeout` function works. It accepts a function and a time duration in milliseconds and executes the function after the provided duration has passed. 

From the example above, `This is a higher order function` is printed to the console after 1000 ms, or one second.

```javascript
setInterval(function () {
  console.log("This is a higher order function");
}, 1000);

// Output: "This is a higher order function" after every 1000ms / 1 second
```

The `setInterval` function is similar to the `setTimeout` function, just like the array methods – although it functions differently. But we can see a common pattern: it also accepts a function as one of its parameters.

Unlike `setTimeout` (that executes the function after the provided duration has passed), `setInterval` executes the function over and over again every 1000ms or 1 second.

### How to Create and Use a Higher Order Function

Higher order functions are not limited to the built-in ones provided by JavaScript.

Since functions in JavaScript are treated as first class objects, we can take advantage of this behavior and build highly performant and reusable functions.

In the examples below, we'll build a couple of functions. They'll accept the name of a customer and a greeting, and then print that info to the console.

First, here is a simple function that does both of those things:

```js
function greetCustomer(firstName, lastName, salutation) {
  const fullName = `${firstName} ${lastName}`;

  console.log(`${salutation} ${fullName}`);
}

greetCustomer("Franklin", "Okolie", "Good Day");

// Output: "Good Day Franklin Okolie"
      
```

`greetCustomer` accepts 3 arguments: a first name, a last name, and a salutation. Then it prints a greeting to the customer to the console.

But there is a problem with this function – it's doing two things: composing the full name of the customer and also printing the greeting.

This is not a best practice, as functions should do only one thing and do it well. So we are going to refactor our code.

Another function should compose the customer's name so that the `greetCustomer` function only has to print the greeting to the console. So let's write a function that handles that:

```js
function composeName(firstName, lastName) {
  const fullName = `${firstName} ${lastName}`;

  return fullName;
}
```

Now that we have a function that combines the customer's first and last names, we can use that function in `greetCustomer`:

```js
function greetCustomer(composerFunc, firstName, lastName, salutation) {
  const fullName = composerFunc(firstName, lastName);

  console.log(`${salutation} ${fullName}`);
}

greetCustomer(composeName, "Franklin", "Okolie", "Good Day");

// Output: "Good Day Franklin Okolie"
```

Now this looks cleaner, and each function does just one thing. The `greetCustomer` function now accept 4 arguments, and since one of those arguments is a function, it's now a higher order function.

You might have wondered earlier, how is a function being invoked inside of another function, and why?

Now we'll take a deep dive into function invocation and answer both of those questions.

### Returning a Function as a Value

Remember that higher order functions either take a function as a parameter and/or return a function as a value.

Let's refactor the `greetCustomer` function to use fewer arguments and return a function:

```js
function getGreetingsDetails(composerFunc, salutation) {
  return function greetCustomer(firstName, lastName) {
    const fullName = composerFunc(firstName, lastName);

    console.log(`${salutation} ${fullName}`);
  };

```

The last version of `greetCustomer` accepted too many arguments. Four arguments isn't a lot, but it would still be frustrating if you messed up the order of the arguments. Generally, the fewer arguments you have, the better.

So in the example above, we have a function called `getGreetingDetails` which accepts `composerFunc` and `salutation` on behalf of the inner `greetCustomer` function. It then returns the inner `greetCustomer` function, which itself accepts `firstName` and `lastName` as arguments.

By doing this, `greetCustomer` has fewer arguments overall.

And with that, let's take a look at how to use the `getGreetingDetails` function:

```js
const greet = getGreetingsDetails(composeName, "Happy New Year!");

greet("Quincy", "Larson");

// Output: "Happy New Year Quincy Larson"
```

Now take a step back and admire this beautiful abstraction. Marvelous! We have used the magic of higher order functions to simplify the `greetCustomer` function.

Let's walk through how everything works. The higher order function named `getGreetingDetails` takes in two arguments: a function to compose the customer's first and last name, and a salutation. Then it returns a function named `greetCustomer` which accepts the first and last name of a customer as arguments.

 The returned `greetCustomer` function also uses the argument accepted by `getGreetingDetails` to execute some actions, too.

At this point you're probably wondering, how can a returned function use arguments provided to a parent function? Especially given how the function execution context works. It's possible because of [closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures). Let's learn more about them now.

### Closures Explained

A closure is a function that has access to the variable in the scope where it was created even after the scope doesn't exist anymore in the execution context. This is one of the underlying mechanism of callbacks, as callbacks can still reference and use variables created in an outer function after that outer function has been closed.

Let's take a quick example:

```js
function getTwoNumbers(num1, num2) {
  return function add() {
    const total = num1 + num2;
    console.log(total);
  };
}

const addNumbers = getTwoNumbers(5, 2);

addNumbers();

//Output: 7;
```

The code in this example defines a function called `getTwoNumbers` and shows you how closures work. Let's explore it in more detail:

1. `getTwoNumbers` is defined as a function that takes two parameters, `num1` and `num2`.
2. Inside `getTwoNumbers`, it returns another function, which is an inner function named `add`.
3. The `add` function, when invoked, calculates the sum of `num1` and `num2` and logs the result to the console.
4. Outside the `getTwoNumbers` function, we create a variable called `addNumbers` and assign it the result of invoking `getTwoNumbers(5, 2)`. This effectively sets up a closure where `addNumbers` now "remembers" the values `5` and `2` as `num1` and `num2`.
5. Finally, we call `addNumbers()` to execute the inner `add` function. Since `addNumbers` is a closure, it still has access to the `num1` and `num2` values, which were set to `5` and `2`, respectively. It calculates their sum and logs `7` to the console.

If you want to learn more about [closures, read more here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures).

Back to our higher order function. The returned function `greetCustomer` gets returned as a value which we store in a variable named `greet`.

Doing that makes the `greet` variable itself a function, meaning we can invoke it as a function and pass in arguments for a first and last name.

And violà There you have it. These concepts can be a bit complex to grasp at first, but once you get the hang of them, they never leave you.

I encourage you to read through the previous sections again, play with the code in your editor, and to get the hang of how everything works together.

Now that you have an in-depth understanding about how higher order functions work, let's talk about callback functions.

## What are Callback Functions?

A callback function is a function that is passed into another function as an argument.

Again, one of the defining factors of functions as first class citizens is its ability to be passed as an argument to another function. This is called the **act of passing callbacks**.

Let go back and take a look at the timing events we discussed earlier when we were learning about the built-in functions provided in JavaScript. Here's the `setTimeout` function again:

```js
setTimeout(function () {
  console.log("This is a higher order function");
}, 1000);

// Output: "This is a higher order function" after 1000ms / 1 seconds
```

We've established that the `setTimeout` function is a higher order function because it accepts another function as an argument.

The function that's passed as an argument to the `setTimeout` function is called a callback function. This is because it is invoked or executed inside of the higher order function it's passed into.

To get a better understanding of callback functions, let's take another look at the `greetCustomer` function from earlier:

```js
// THIS IS A CALLBACK FUNCTION
// IT IS PASSED AS AN ARGUMENT TO A FUNCTION

function composeName(firstName, lastName) {
  const fullName = `${firstName} ${lastName}`;

  return fullName;
}

// THIS IS A HIGHER ORDER FUNCTION
// IT ACCPEPTS A FUNCTION AS A ARGUMENT

function greetCustomer(composerFunc, firstName, lastName, salutation) {
  const fullName = composerFunc(firstName, lastName);

  console.log(`${salutation} ${fullName}`);
}

greetCustomer(composeName, "Franklin", "Okolie", "Good Day");

// Output: "Good Day Franklin Okolie"
```

The `composeName` is a callback function that is passed as an argument into the `greetCustomer` function a higher order function and it is executed inside this function.

## The Difference Between Higher Order Functions and Callback Functions

It's important that we understand the difference between these two terms so we can communicate more clearly with teammates and during technical interviews:

* **Higher Order Function**: A function that accepts a function as an argument and/or returns a function as its value.
* **Callback Function**: A function that's passed as a argument to another function.

### A Bag and Book

To further understand these terms, I'll share a simple analogy.

Imagine you have a bag and a book. You carry the book in your bag while attending a meeting, going to class, going to church, and so on.

In this scenario, the bag accepts your book to carry it, and also returns it when you want to use it. So the bag is like a higher order function.

The book is kept inside of the bag until it's ready to be used, so it's like a callback function.

### Fuel and Fuel Tank

Let's take a look at another analogy; fuel and a fuel tank.

To fuel a car, we have to pour the fuel through the fuel tank, the fuel tank recieves the fuel – just like a higher order function.

The fuel is poured into the fuel tank – like a callback function.

I hope these analogies help to further simplify higher order and callback functions and the difference between them.

## Conclusion

As you can see, functions in JavaScript are very flexible, and can be used in a lot of helpful ways. This flexibility also lead to two common technical terms in JavaScript, higher order functions and callback functions.

If you want to learn more about these topics, check out the MDN documentation on functions as [first class citizens](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function), [higher order functions](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function), and [callback functions](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function).

I hope you learned a lot from this article, and I hope you use your newfound knowledge to communicate your thoughts more clearly during pair coding sessions or during technical interviews.

For more JavaScripts tips, follow me on [Twitter](https://twitter.com/developeraspire).

Thanks for reading! See you next time.

