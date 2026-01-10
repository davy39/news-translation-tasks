---
title: Arrow Function JavaScript Tutorial – How to Declare a JS Function with the
  New ES6 Syntax
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T15:38:35.000Z'
originalURL: https://freecodecamp.org/news/arrow-function-javascript-tutorial-how-to-declare-a-js-function-with-the-new-es6-syntax
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/nick-fewings-zF_pTLx_Dkg-unsplash-1.jpg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: js
  slug: js
- name: learn to code
  slug: learn-to-code
- name: programing
  slug: programing
seo_title: null
seo_desc: 'By Amy Haddad

  You’ve probably seen arrow functions written a few different ways.

  //example 1

  const addTwo = (num) => {return num + 2;};


  //example 2

  const addTwo = (num) => num + 2;


  //example 3

  const addTwo = num => num + 2;


  //example 4

  const addTw...'
---

By Amy Haddad

You’ve probably seen arrow functions written a few different ways.

```JS
//example 1
const addTwo = (num) => {return num + 2;};

//example 2
const addTwo = (num) => num + 2;

//example 3
const addTwo = num => num + 2;
 
//example 4
const addTwo = a => {
 const newValue = a + 2;
 return newValue;
};
```

Some have parentheses around the parameters, while others don’t. Some use curly brackets and the `return` keyword, others don’t. One even spans multiple lines, while the others consist of a single line.

Interestingly, when we invoke the above arrow functions with the same argument we get the same result.

```JS
console.log(addTwo(2));
//Result: 4
```

How do you know which arrow function syntax to use? That’s what this article will uncover: how to declare an arrow function.

## A Major Difference

Arrow functions are another—more concise—way to write function expressions. However, they don’t have their own binding to the **`this`** keyword. 

```JS
//Function expression
const addNumbers = function(number1, number2) {
   return number1 + number2;
};

//Arrow function expression
const addNumbers = (number1, number2) => number1 + number2;
```

When we invoke these functions with the same arguments we get the same result.

```JS
console.log(addNumbers(1, 2));
//Result: 3
```

There's an important syntactical difference to note: arrow functions use the arrow **`=>`** instead of the **`function`** keyword. There are other differences to be aware of when you write arrow functions, and that’s what we’ll explore next.

## Parentheses

Some arrow functions have parentheses around the parameters and others don't.

```JS
//Example with parentheses
const addNums = (num1, num2) => num1 + num2;

//Example without parentheses
const addTwo = num => num + 2;
```

As it turns out, the number of parameters an arrow function has determines whether or not we need to include parentheses.

An arrow function with **zero parameters** requires parentheses.

```JS
const hello = () => "hello";
console.log(hello());
//Result: "hello"
```

An arrow function with **one parameter** does _not_ require parentheses. In other words, parentheses are optional. 

```JS
const addTwo = num => num + 2;
```

So we can add parentheses to the above example and the arrow function still works.

```JS
const addTwo = (num) => num + 2;
console.log(addTwo(2));
//Result: 4
```

An arrow function with **multiple parameters** requires parentheses.

```JS
const addNums = (num1, num2) => num1 + num2;
console.log(addNums(1, 2));
//Result: 3
```

Arrow functions also support **rest parameters** and **destructuring**. Both features require parentheses.

This is an example of an arrow function with a **rest parameter**.

```JS
const nums = (first, ...rest) => rest;
console.log(nums(1, 2, 3, 4));
//Result: [ 2, 3, 4 ]
```

And here’s one that uses **destructuring**.

```JS
const location = {
   country: "Greece",
   city: "Athens"
};

const travel = ({city}) => city;

console.log(travel(location));
//Result: "Athens"
```

To summarize: if there’s only one parameter—and you’re not using rest parameters or destructuring—then parentheses are optional. Otherwise, be sure to include them.

## The Function Body

Now that we’ve got the parentheses rules covered, let’s turn to the function body of an arrow function.

An arrow function body can either have a [“concise body” or “block body”](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions#:~:text=An%20arrow%20function%20expression%20is,cannot%20be%20used%20as%20constructors.). The body type influences the syntax.

First, the “concise body” syntax.

```JS
const addTwo = a => a + 2;
```

The “concise body” syntax is just that: it’s concise! We don’t use the `return` keyword or curly brackets. 

If you have a one-line arrow function (like the example above), then the value is implicitly returned. So you can omit the `return` keyword and the curly brackets. 

Now let’s look at “block body” syntax.

```JS
const addTwo = a => {
    const total = a + 2;
    return total;
}
```

Notice that we use _both_ curly brackets and the `return` keyword in the above example. 

You normally see this syntax when the body of the function is more than one line. And that’s a key point: wrap the body of a multi-line arrow function in curly brackets and use the `return` keyword.

### Objects and Arrow Functions

There’s one more syntax nuance to know about: wrap the function body in parentheses when you want to return an [object literal expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions).

```JS
const f = () => ({
 city:"Boston"
})
console.log(f().city)
```

Without the parentheses, we get an error.

```JS
const f = () => {
   city:"Boston"
}
//Result: error
```

If you find the arrow function syntax a bit confusing, you’re not alone. It takes some time to get familiar with it. But being aware of your options and requirements are steps in that direction.

_I write about learning to program and the best ways to go about it (_[amymhaddad.com](https://amymhaddad.com/)).  

