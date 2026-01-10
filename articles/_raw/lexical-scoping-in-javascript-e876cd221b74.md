---
title: An easy intro to Lexical Scoping in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-10T18:26:21.000Z'
originalURL: https://freecodecamp.org/news/lexical-scoping-in-javascript-e876cd221b74
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LoVCoRxQBamxz5xRTYaXeA.jpeg
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
seo_desc: 'By Michael McMillan

  Lexical scoping is a topic that frightens many programmers. One of the best explanations
  of lexical scoping can be found in Kyle Simpson’s book You Don’t Know JS: Scope
  and Closures. However, even his explanation is lacking becaus...'
---

By Michael McMillan

Lexical scoping is a topic that frightens many programmers. One of the best explanations of lexical scoping can be found in Kyle Simpson’s book [You Don’t Know JS: Scope and Closures](https://www.amazon.com/You-Dont-Know-JS-Closures/dp/1449335586). However, even his explanation is lacking because he doesn’t use a real example.

One of the best real examples of how lexical scoping works, and why it is important, can be found in the famous textbook, “The Structure and Interpretation of Computer Programs” (SICP) by Harold Abelson and Gerald Jay Sussman. Here is a link to a PDF version of the book: [SICP](https://web.mit.edu/alexmv/6.037/sicp.pdf).

SICP uses Scheme, a dialect of Lisp, and is considered one of the best introductory computer science texts ever written. In this article, I’d like to revisit their example of lexical scoping using JavaScript as the programming language.

#### Our example

The example Abelson and Sussman used is computing square roots using Newton’s method. Newton’s method works by determining successive approximations for the square root of a number until the approximation comes within a tolerance limit for being acceptable. Let’s work through an example, as Abelson and Sussman do in SICP.

The example they use is finding the square root of 2. You start by making a guess at the square root of 2, say 1. You improve this guess by dividing the original number by the guess and then averaging that quotient and the current guess to come up with the next guess. You stop when you reach an acceptable level of approximation. Abelson and Sussman use the value 0.001. Here is a run-through of the first few steps in the calculation:

```
Square root to find: 2First guess: 1Quotient: 2 / 1 = 2Average: (2+1) / 2 = 1.5Next guess: 1.5Quotient: 1.5 / 2 = 1.3333Average: (1.3333 + 1.5) / 2 = 1.4167Next guess: 1.4167Quotient: 1.4167 / 2 = 1.4118Average: (1.4167 + 1.4118) / 2 = 1.4142
```

And so on until the guess comes within our approximation limit, which for this algorithm is 0.001.

### A JavaScript Function for Newton’s Method

After this demonstration of the method the authors describe a general procedure for solving this problem in Scheme. Rather than show you the Scheme code, I’ll write it out in JavaScript:

```
function sqrt_iter(guess, x) {  if (isGoodEnough(guess, x)) {    return guess;  }    else {    return sqrt_iter(improve(guess, x), x);  }}
```

Next, we need to flesh out several other functions, including isGoodEnough() and improve(), along with some other helper functions. We’ll start with improve(). Here is the definition:

```
function improve(guess, x) {  return average(guess, (x / guess));}
```

This function uses a helper function average(). Here is that definition:

```
function average(x, y) {  return (x+y) / 2;}
```

Now we’re ready to define the isGoodEnough() function. This function serves to determine when our guess is close enough to our approximation tolerance (0.001). Here is the definition of isGoodEnough():

```
function isGoodEnough(guess, x) {  return (Math.abs(square(guess) - x)) < 0.001;}
```

This function uses a square() function, which is easy to define:

```
function square(x) {  return x * x;}
```

Now all we need is a function to get things started:

```
function sqrt(x) {  return sqrt_iter(1.0, x);}
```

This function uses 1.0 as a starting guess, which is usually just fine.

Now we’re ready to test our functions to see if they work. We load them into a JS shell and then compute a few square roots:

```
> .load sqrt_iter.js> sqrt(3)1.7321428571428572> sqrt(9)3.00009155413138> sqrt(94 + 87)13.453624188555612> sqrt(144)12.000000012408687
```

The functions seem to be working well. However, there is a better idea lurking here. These functions are all written independently, even though they are meant to work in conjunction with each other. We probably aren’t going to use the isGoodEnough() function with any other set of functions, or on its own. Also, the only function that matters to the user is the sqrt() function, since that’s the one that gets called to find a square root.

### Block Scoping Hides Helper Functions

The solution here is to use block scoping to define all the necessary helper functions within the block of the sqrt() function. We are going to remove square() and average() from the definition, as those functions might be useful in other function definitions and aren’t as limited to use in an algorithm that implements Newton’s Method. Here is the definition of the sqrt() function now with the other helper functions defined within the scope of sqrt():

```
function sqrt(x) {  function improve(guess, x) {    return average(guess, (x / guess));  }  function isGoodEnough(guess, x) {    return (Math.abs(square(guess) - x)) > 0.001;  }  function sqrt_iter(guess, x) {    if (isGoodEnough(guess, x)) {      return guess;    }    else {      return sqrt_iter(improve(guess, x), x);    }  }  return sqrt_iter(1.0, x);}
```

We can now load this program into our shell and compute some square roots:

```
> .load sqrt_iter.js> sqrt(9)3.00009155413138> sqrt(2)1.4142156862745097> sqrt(3.14159)1.772581833543688> sqrt(144)12.000000012408687
```

Notice that you cannot call any of the helper functions from outside the sqrt() function:

```
> sqrt(9)3.00009155413138> sqrt(2)1.4142156862745097> improve(1,2)ReferenceError: improve is not defined> isGoodEnough(1.414, 2)ReferenceError: isGoodEnough is not defined
```

Since the definitions of these functions (improve() and isGoodEnough()) have been moved inside the scope of sqrt(), they cannot be accessed at a higher level. Of course, you can move any of the helper function definitions outside of the sqrt() function to have access to them globally as we did with average() and square().

We have greatly improved our implementation of Newton’s Method but there’s still one more thing we can do to improve our sqrt() function by simplifying it even more by taking advantage of lexical scope.

### Improving Clarity with Lexical Scope

The concept behind lexical scope is that when a variable is bound to an environment, other procedures (functions) that are defined in that environment have access to that variable’s value. This means that in the sqrt() function, the parameter x is bound to that function, meaning that any other function defined within the body of sqrt() can access x.

Knowing this, we can simplify the definition of sqrt() even more by removing all references to x in function definitions since x is now a free variable and accessible by all of them. Here is our new definition of sqrt():

```
function sqrt(x) {  function isGoodEnough(guess) {    return (Math.abs(square(guess) - x)) > 0.001;  }  function improve(guess) {    return average(guess, (x / guess));  }  function sqrt_iter(guess) {    if (isGoodEnough(guess)) {      return guess;    }    else {      return sqrt_iter(improve(guess));    }  }  return sqrt_iter(1.0);}
```

The only references to parameter x are in computations where x’s value is needed. Let’s load this new definition into the shell and test it:

```
> .load sqrt_iter.js> sqrt(9)3.00009155413138> sqrt(2)1.4142156862745097> sqrt(123+37)12.649110680047308> sqrt(144)12.000000012408687
```

Lexical scoping and block structure are important features of JavaScript and allow us to construct programs that are easier to understand and manage. This is especially important when we begin to construct larger, more complex programs.

![Image](https://cdn-media-1.freecodecamp.org/images/S2PRBM-GSiBQBuXWf1q614LInt0MBmr9rTuN)

