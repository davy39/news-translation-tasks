---
title: When (and why) you should use ES6 arrow functions — and when you shouldn’t
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-05T16:44:13.000Z'
originalURL: https://freecodecamp.org/news/when-and-why-you-should-use-es6-arrow-functions-and-when-you-shouldnt-3d851d7f0b26
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GRUP3Ml4piJhZQ8EOHkFDA.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Cynthia Lee

  Arrow functions (also called “fat arrow functions”) are undoubtedly one of the more
  popular features of ES6. They introduced a new way of writing concise functions.

  Here is a function written in ES5 syntax:

  function timesTwo(params) {

  ...'
---

By Cynthia Lee

Arrow functions (also called “fat arrow functions”) are undoubtedly one of the more popular features of ES6. They introduced a new way of writing concise functions.

Here is a function written in ES5 syntax:

```js
function timesTwo(params) {
  return params * 2
}

timesTwo(4);  // 8
```

Now, here is the same function expressed as an arrow function:

```js
var timesTwo = params => params * 2

timesTwo(4);  // 8
```

It’s much shorter! We are able to omit the curly braces and the return statement due to implicit returns (but only if there is no block — more on this below).

It is important to understand how the arrow function behaves differently compared to the regular ES5 functions.

### Variations

![Image](https://cdn-media-1.freecodecamp.org/images/c1-i0BPczDkbeDybCAzWCHsEyVFX0Ttg5bpL)
_Variety is the spice of life_

One thing you will quickly notice is the variety of syntaxes available in arrow functions. Let’s run through some of the common ones:

#### 1. No parameters

If there are no parameters, you can place an empty parentheses before `=&`gt;.

```js
() => 42
```

In fact, you don’t even need the parentheses!

```js
_ => 42
```

#### 2. Single parameter

With these functions, parentheses are optional:

```js
x => 42  || (x) => 42
```

#### **3. Multiple parameters**

Parentheses are required for these functions:

```js
(x, y) => 42
```

#### **4. Statements (as opposed to expressions)**

In its most basic form, a _function expression_ produces a value, while a _function statement_ performs an action.

With the arrow function, it is important to remember that statements need to have curly braces. Once the curly braces are present, you always need to write `return` as well.

Here is an example of the arrow function used with an if statement:

```js
var feedTheCat = (cat) => {
  if (cat === 'hungry') {
    return 'Feed the cat';
  } else {
    return 'Do not feed the cat';
  }
}
```

#### **5. “Block body”**

If your function is in a block, you must also use the explicit `return` statement:

```js
var addValues = (x, y) => {
  return x + y
}
```

#### **6. Object literals**

If you are returning an object literal, it needs to be wrapped in parentheses. This forces the interpreter to evaluate what is inside the parentheses, and the object literal is returned.

```js
x =>({ y: x })
```

### Syntactically anonymous

![Image](https://cdn-media-1.freecodecamp.org/images/hS7maItiZiV0IIYACtt0PiD3VStILiS1n4sd)

It is important to note that arrow functions are anonymous, which means that they are not named.

This anonymity creates some issues:

1. Harder to debug

When you get an error, you will not be able to trace the name of the function or the exact line number where it occurred.

2. No self-referencing

If your function needs to have a self-reference at any point (e.g. recursion, event handler that needs to unbind), it will not work.

### Main benefit: No binding of ‘this’

![Image](https://cdn-media-1.freecodecamp.org/images/3Rc2e8J5whHdFrH3IzPckp5GCQ-QtMvEOH1k)
_Photo by [Unsplash](https://unsplash.com/@davideragusa?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">davide ragusa</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

In classic function expressions, the `this` keyword is bound to different values based on the _context_ in which it is called. With arrow functions however, `this` is _lexically bound_. It means that it uses`this` from the code that contains the arrow function.

For example, look at the `setTimeout` function below:

```js
// ES5
var obj = {
  id: 42,
  counter: function counter() {
    setTimeout(function() {
      console.log(this.id);
    }.bind(this), 1000);
  }
};
```

In the ES5 example, `.bind(this)` is required to help pass the `this` context into the function. Otherwise, by default `this` would be undefined.

```js
// ES6
var obj = {
  id: 42,
  counter: function counter() {
    setTimeout(() => {
      console.log(this.id);
    }, 1000);
  }
};
```

ES6 arrow functions can’t be bound to a `this` keyword, so it will lexically go up a scope, and use the value of `this` in the scope in which it was defined.

### When you should not use Arrow Functions

After learning a little more about arrow functions, I hope you understand that they do not replace regular functions.

Here are some instances where you probably wouldn’t want to use them:

1. Object methods

When you call `cat.jumps`, the number of lives does not decrease. It is because `this` is not bound to anything, and will inherit the value of `this` from its parent scope.

```js
var cat = {
  lives: 9,
  jumps: () => {
    this.lives--;
  }
}
```

2. Callback functions with dynamic context

If you need your context to be dynamic, arrow functions are not the right choice. Take a look at this event handler below:

```js
var button = document.getElementById('press');
button.addEventListener('click', () => {
  this.classList.toggle('on');
});
```

If we click the button, we would get a TypeError. It is because `this` is not bound to the button, but instead bound to its parent scope.

3. When it makes your code less readable

It is worth taking into consideration the variety of syntax we covered earlier. With regular functions, people know what to expect. With arrow functions, it may be hard to decipher what you are looking at straightaway.

### When you should use them

Arrow functions shine best with anything that requires `this` to be bound to the context, and not the function itself.

Despite the fact that they are anonymous, I also like using them with methods such as `map` and `reduce`, because I think it makes my code more readable. To me, the pros outweigh the cons.

Thanks for reading my article, and share if you liked it! Check out my other articles like [How I built my Pomodoro Clock app, and the lessons I learned along the way](https://www.freecodecamp.org/news/how-i-built-my-pomodoro-clock-app-and-the-lessons-i-learned-along-the-way-51288983f5ee/), and [Let’s demystify JavaScript’s ‘new’ keyword](https://www.freecodecamp.org/news/demystifying-javascripts-new-keyword-874df126184c/).

