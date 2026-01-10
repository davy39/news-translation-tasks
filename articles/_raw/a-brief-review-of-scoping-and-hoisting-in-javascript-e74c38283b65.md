---
title: A brief review of Scoping and Hoisting in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-10T18:43:19.000Z'
originalURL: https://freecodecamp.org/news/a-brief-review-of-scoping-and-hoisting-in-javascript-e74c38283b65
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZyXTRpRSpg2rfqmzJgpJmw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Tiago Romero Garcia

  I bet that any JavaScript developer would want a better understanding of the concepts
  of Scoping and Hoisting. They can silently produce these dreaded unexplainable problems,
  also known as side-effects.

  In a nutshell, scoping a...'
---

By Tiago Romero Garcia

I bet that any JavaScript developer would want a better understanding of the concepts of Scoping and Hoisting. They can silently produce these dreaded unexplainable problems, also known as side-effects.

In a nutshell, scoping and hoisting effect how the code we write will deal with our declarations (such as var, `let`, `const` and `function`).

Let's begin our recap with the first of them: `var`.

### Dealing with var

When using `var` to declare your variables, the parent function where you declare your vars inside is your only _de facto_ scope delimiter. This way, the parent function creates and holds the scope for all the local variables declared within itself.

In other words, inside the parent function, the local variables are born, they do their work and when the function execution ends, they also die off (unless they are passed to some other function that outlives the parent function).

This is the definition of **Local Scope. A**s opposed to **Global Scope**, when the variables are declared outside your function. They are accessible by everyone and everywhere. They are omnipresent like the air we breathe, or like the `window` object in the browser.

Hence, other code blocks as conditionals and loops (such as `if`, `for`, `while`, `switch` and `try`) do not delimit scope, unlike most other languages.

Then, any `var` inside these blocks will be scoped within their parent function which contains that block.

Not only that, but during runtime, every `var` declaration that is found inside such code blocks gets moved to the beginning of its parent function (its scope). This is the definition of **Hoisting**.

That being so, you shouldn’t declare a `var` within a block and think this `var` is not leaking outside, because it might be!

Here is an example:

```
function stepSum() {  var total = 0;
```

```
  for (var i = 0; i < arguments.length; i++) {    var parameter = arguments[i];     total += parameter;    console.log(`${i}) adding ${parameter}`);  }
```

```
  // outside the loop, we can still access vars i and parameter  // even though the were declared within the for loop  console.log(`i=${i}, parameter=${parameter}`);  return total;}
```

```
console.log(`total=${stepSum(3, 2, 1)}`);
```

The output is:

```
0) adding 31) adding 22) adding 1i=3, parameter=1total=6
```

Here, we can observe that the vars `i` and `parameter` are leaking, since they both can be accessed from the parent function. That’s because they were hoisted up there, just if they were declared like this:

```
function stepSum() {  var total = 0;  var i;  var parameter;
```

```
  for (i = 0; i < arguments.length; i++) {    parameter = arguments[i];     total += parameter;    console.log(`${i}) adding ${parameter}`);  }
```

```
  console.log(`i=${i}, parameter=${parameter}`);  return total;}
```

```
console.log(`total=${stepSum(3, 2, 1)}`);
```

To avoid any confusion, it is a common practice to declare vars in the first lines of the parent function. This is done to avoid false expectations for any `var` which may get declared somewhere down the function but happened to have hold a value before that.

This is a source of confusion for programmers coming from languages with block scope (such as C or Java). They usually declare their vars right when they are about to make their first use.

#### Issues with `var`

Let’s consider this code snippet. It is similar to the last one, except it calculates each sum asynchronously:

```
function stepSum() {  var total = 0;
```

```
  for (var i = 0; i < arguments.length; i++) {    var parameter = arguments[i];
```

```
    setTimeout(function() {      total += parameter;      console.log(`${i}) adding ${parameter}, total=${total}`);    }, i*1000);  }}
```

```
stepSum(3, 2, 1);
```

The output is:

```
3) adding 1, total=13) adding 1, total=23) adding 1, total=3
```

Why did it happen? It is summing up just the last parameter 1, for three times. And also the step count is always on 3, where we would expect to see 1, 2 and 3. What is wrong here?

The answer follows: the vars `i` and `parameter` got hoisted to the beginning of the `stepSum` function, and now they are available for the whole parent function. More than that, `parameter` is actually being defined just once, and then it is being re-assigned on each iteration of the for loop.

Given that we are using `setTimeout` calls here, we can expect now that when this function executes for the first time (after a second), the `stepSum` function will be already finished. So `parameter` ended up with the value of its last assignment, which is from the last iteration of the for loop, when it was set to 1. The same thing with `i` finishing up with value 3.

That’s why these values are being picked up when the 3 `setTimeout` calls get ultimately executed.

How can we fix it? Simply by making good usage of scoping and hoisting. We can provide a new function scope to protect `i` and `parameter` from being reassigned. This creates a local scope just for them. Perhaps by using something other than var which can also give us a local scope within a block, as we can see next.

### Dealing with let and const

ES2015 introduced `let` and `const` which are variables that do respect the block scope. This means they are safe to be declared within a block and won’t leak outside, as the following example:

```
function stepSum() {  let total = 0;
```

```
  for (let i = 0; i < arguments.length; i++) {    const parameter = arguments[i];     total += parameter;    console.log(`${i}) adding ${parameter}`);  }
```

```
  // outside the loop, we can no longer access i and parameter  console.log(`i=${i}, parameter=${parameter}`);  return total;}
```

```
console.log(`total=${stepSum(3, 2, 1)}`);
```

The output is:

```
0) adding 31) adding 22) adding 1Uncaught ReferenceError: i is not defined  at stepSum (<anonymous>:10:20)  at <anonymous>:13:1
```

Ok, so now that we learned how to prevent leaking and protect variables within a block scope, let’s try them out!

Back to the `setTimeout` issue above, we can now use `let` and `const` to fix our problem:

```
function stepSum() {  let total = 0;
```

```
  for (let i = 0; i < arguments.length; i++) {    const parameter = arguments[i];
```

```
    setTimeout(function() {      total += parameter;     console.log(`${i}) adding ${parameter}, total=${total}`);    }, i*1000);  }}
```

```
stepSum(3, 2, 1);
```

Voilà, now the output is what we expect:

```
0) adding 3, total=31) adding 2, total=52) adding 1, total=6
```

Keep in mind that we have created one pair of `i` and `parameter` variables for each iteration of the for loop. Compare this to before when we just had one single `i` and `parameter` being rewritten each time. This matters a little bit for memory consumption.

Finally, since we also created the `setTimeout` callback function within the same scope, they will co-live with the protected values of `i` and `parameter`. Block scope will remain preserved even after `stepSum` finished executing.

### Dealing with functions

Here's something noteworthy: declaring a `function` is different than declaring a `var` and assigning a function to it.

For instance, here is an example of declaring a `function` after it was used, to understand how hoisting works. This is valid JavaScript:

```
console.log(`total=${stepSum(3, 2, 1)}`);
```

```
function stepSum(...args) {  let total = 0;
```

```
  args.forEach((parameter, i) => {     total += parameter;    console.log(`${i}) adding ${parameter}`);  });
```

```
  return total;}
```

The output is:

```
0) adding 31) adding 22) adding 1total=6
```

Why did that work? Because the function `stepSum` was completely hoisted before it was used.

However, declaring it as a `var` causes an error:

```
console.log(`total=${stepSum(3, 2, 1)}`);
```

```
var stepSum = function(...args) {  let total = 0;
```

```
  args.forEach((parameter, i) => {     total += parameter;    console.log(`${i}) adding ${parameter}`);  });
```

```
  return total;}
```

The output is:

```
Uncaught TypeError: stepSum is not a function  at <anonymous>:1:22
```

Why did it break?

The difference here is that when a `function` is hoisted, its body is also hoisted. Compared to when a `var` is hoisted, only its declaration gets hoisted but not its assignment. So the code above would have been similar to this, where we are attempting to use `stepSum` before the function gets assigned to it.

```
var stepSum;console.log(`total=${stepSum(3, 2, 1)}`);
```

```
stepSum = function(...args) {  let total = 0;
```

```
  args.forEach((parameter, i) => {     total += parameter;    console.log(`${i}) adding ${parameter}`);  });
```

```
  return total;}
```

### Up for a challenge?

Now that you understand this, I would like to leave you a challenge so you can explain what the heck is going on with the code below:

```
function stepSum(...args) {  let total = 0;
```

```
  args.forEach((parameter, i) => {     total += parameter;    console.log(`${i}) adding ${parameter}`);    return;    function total() {}  });
```

```
  return total;}
```

```
console.log(`total=${stepSum(3, 2, 1)}`);
```

The output is:

```
0) adding 31) adding 22) adding 1total=0
```

Why the 0?? I invite you to leave your explanation at the comments section below :)

### Learn more

For more interesting scenarios on scoping and hosting, I suggest reading this clarifying article:

[**JavaScript Scoping and Hoisting**](http://www.adequatelygood.com/JavaScript-Scoping-and-Hoisting.html)  
[_This method is actually quite flexible, and can be used anywhere you need a temporary scope, not just within block…_www.adequatelygood.com](http://www.adequatelygood.com/JavaScript-Scoping-and-Hoisting.html)

And after that, you can try out your knowledge with some interview questions:

[**Function Hoisting & Hoisting Interview Questions**](https://medium.freecodecamp.org/function-hoisting-hoisting-interview-questions-b6f91dbc2be8)  
[_This is a part 2 for my previous article on Variable Hoisting titled “A guide to JavaScript variable hoisting ? with…m_edium.freecodecamp.org](https://medium.freecodecamp.org/function-hoisting-hoisting-interview-questions-b6f91dbc2be8)

This article was originally published (pre-ES2015 version) on February 4th, 2014 as [Javascript Hoisting](https://coderwall.com/p/jj635w/javascript-hoisting--2).

