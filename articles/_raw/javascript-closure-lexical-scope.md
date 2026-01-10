---
title: JavaScript Closure Tutorial – How Closures and Lexical Scope Work in JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-28T18:45:21.000Z'
originalURL: https://freecodecamp.org/news/javascript-closure-lexical-scope
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/tim-evans-Uf-c4u1usFQ-unsplash.jpg
tags:
- name: closure
  slug: closure
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: Lexical Scoping
  slug: lexical-scoping
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dave Gray

  In JavaScript, people often confuse closures with lexical scope.

  Lexical scope is an important part of closures, but it is not a closure by itself.

  Closures are an advanced concept that is also a frequent topic of technical interviews.

  Y...'
---

By Dave Gray

In JavaScript, people often confuse closures with lexical scope.

Lexical scope is an important part of closures, but it is not a closure by itself.

Closures are an advanced concept that is also a frequent topic of technical interviews.

You should have a foundational understanding of functions before attempting to understand closures.

After reading this article, I hope I will have helped you learn the following:

* The difference between lexical scope and closures.
* Why closures require lexical scope.
* How to give an example of a closure during the interview process.

## What is Lexical Scope in JavaScript?

Lexical scope describes how nested (also known as "child") functions have access to variables defined in parent scopes.

```js
const myFunction = () => {
     let myValue = 2;
     console.log(myValue);

     const childFunction = () => {
          console.log(myValue += 1);
     }

     childFunction();
}

myFunction();
```

In this example, `childFunction` has access to the variable `myValue` which is defined in the parent scope of `myFunction`. 

The lexical scope of `childFunction` allows access to the parent scope.

## What is a Closure in JavaScript?

[w3Schools.com](https://www.w3schools.com/js/js_function_closures.asp) offers a great definition of what a closure is:

> A closure is a function having access to the parent scope, even after the parent function has closed.

Let's note the first part of the sentence before the comma:

> ...a function having access to the parent scope

That's describing lexical scope!

But we need the second part of the definition to give an example of a closure...

> ...even after the parent function has closed.

Let's look at an example of a closure:

```js
const myFunction = () => {
     let myValue = 2;
     console.log(myValue);

     const childFunction = () => {
          console.log(myValue += 1);
     }

     return childFunction;
}

const result = myFunction();
console.log(result);
result();
result();
result();
```

Copy the example code above and try it out.

_Let's break down what is happening..._

In this revision, `myFunction` returns `childFunction` instead of calling it.

Therefore, when `result` is set equal to `myFunction()`, the console statement inside `myFunction` is logged, but not the statement inside `childFunction`. 

`childFunction` is not called into action. 

Instead, it is returned and held in `result`.

In addition, we need to realize that `myFunction` has closed after it was called.

The line with `console.log(result)` should show in the console that `result` now holds the anonymous function value that was `childFunction`.

Now, when we call `result()`, we are calling the anonymous function that was assigned to `childFunction`.

As a child of `myFunction`, this anonymous function has access to the `myValue` variable inside `myFunction` _even after it has closed!_

The closure we created now allows us to continue to increase the value of the `myValue` variable every time we call `result()`.

## Take Your Time with Closures

Closures are considered to be an advanced concept for good reason.

Even with a step-by-step breakdown of what a closure is, this concept can take time to understand.

Don't rush your understanding and don't be hard on yourself if it doesn't make sense at first.

When you fully understand closure, you may feel like [Neo when he sees the Matrix](https://www.google.com/search?q=neo+sees+the+matrix&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiG1MaN1rPxAhUNCM0KHQJWCtAQ_AUoAXoECAEQAw&biw=1762&bih=886). You'll see new code possibilities and realize they were there all along!

I'll leave you with a tutorial on closures from [my YouTube channel](https://www.youtube.com/davegrayteachescode). I dive a little deeper and provide a few more examples of closures to build on the discussion in this article.

%[https://www.youtube.com/watch?v=1S8SBDhA7HA]


