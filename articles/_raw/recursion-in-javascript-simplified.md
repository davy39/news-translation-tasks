---
title: How Does Recursion Work? Simplified in JavaScript with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-07T17:51:43.000Z'
originalURL: https://freecodecamp.org/news/recursion-in-javascript-simplified
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/recursion-js.png
tags:
- name: JavaScript
  slug: javascript
- name: Recursion
  slug: recursion
seo_title: null
seo_desc: "By Dillion Megida\nRecursion works similarly to how loops do in JavaScript.\
  \ Loops allow you to execute a set of code multiple times as long as a condition\
  \ is true. \nIn this article, I will explain what Recursion is and how it works\
  \ in JavaScript.\nIn l..."
---

By Dillion Megida

Recursion works similarly to how loops do in JavaScript. Loops allow you to execute a set of code multiple times as long as a condition is true. 

In this article, I will explain what Recursion is and how it works in JavaScript.

In loops, when the condition becomes false, the execution stops. If the condition for execution forever remains true, you get an **infinite loop** which can crash your application. 

It's the same with recursion – as long as the condition for recursion remains true, recursion keeps happening until a condition stops it, else, you get an **infinite recursion**.

Here's a video version of this tutorial if you would like that: [Recursion in JavaScript, Simplified](https://www.youtube.com/watch?v=wCPU8iYiTbE)

So, now let's dive in...

## What is Recursion?

Recursion is a concept where a function calls itself, and keeps calling itself until it is told to stop.

Let's look at an example:

```js
function printHello() {
  console.log("hello")
}

printHello()
```

Here, we declare a `printHello` function that logs "hello" to the console. And then, we call the function after the definition.

In the case of recursion, we can also call the `printHello` function from within the `printHello` function like this:

```js
function printHello() {
  console.log("hello")

  printHello()
}

printHello()

// hello - first function call
// hello - second function call
// hello - third function call
// and it goes on infinitely
```

This is recursion. So when JavaScript executes `printHello()`, "hello" is printed to the console, and afterward, `printHello()` is called again. Here's how the recursion happens:

- `printHello()` is executed the **FIRST** time, "hello" printed to the console, and right there in the function, `printHello()` is called again
- `printHello()` is executed the **SECOND** time, `console.log("hello")` runs again, and `printHello()` is called again
- `printHello()` is executed the **THIRD** time, `console.log("hello")` runs again, and `printHello()` is called again
- and it keeps going on and on until the call stack reaches its maximum and the app crashes:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/call-stack-error.png)
_Maximum Call Stack Size Exceeded Error_

Let's understand the meaning of this error.

## What is the Call Stack?

The call stack is a mechanism that JavaScript uses to keep track of the function that is currently being executed.

When a function is called, it is added to the call stack. For example, this function from above:

```js
function printHello() {
  console.log("hello")
}

printHello()
```

When this function is to be executed, it is added to the call stack:

```js
// printHello()
// ----
// call stack
```

After execution (when all the code runs, or when a `return` statement is encountered), the function is popped out of the stack:

```js
// ----
// call stack
```

If the `printHello` function, for example, calls another function like this:

```js
function printHi() {
  console.log("hi")
}

function printHello() {
  console.log("hello")

  printHi()
}

printHello()
```

In this case, the call stack will look like this when `printHello` is called:

```js
// printHello()
// ----
// call stack
```

After running the `console.log("hello")` line, the next line is `printHi()`, and this call is added to the top of the stack:

```js
// printHi()
// printHello()
// ----
// call stack
```

After the `printHi()` call finishes execution, it is popped out of the stack:

```js
// printHello()
// ----
// call stack
```

After `printHello()` finishes execution, it is also popped out of the stack:

```js
// ----
// call stack
```

So how does recursion work with the call stack?

## Recursion and the Call Stack

Back to our recursion code above:

```js
function printHello() {
  console.log("hello")

  printHello()
}

printHello()
```

What happens here is, when `printHello()` is executed, it is added to the call stack:

```js
// printHello()
// ----
// call stack
```

The `console.log("hello")` is executed, then `printHello()` is executed again, and is added to the top of the call stack:

```js
// printHello()
// printHello() -- "hello"
// ----
// call stack
```

Now, we have two functions currently on the call stack: the first `printHello` and the second `printHello` which was called from the first one.

During the execution of the second `printHello`, `console.log("hello")` is executed, and `printHello` is called again. Now the stack looks like this:

```js
// printHello()
// printHello() -- "hello"
// printHello() -- "hello"
// ----
// call stack
```

As things are, we do not have any condition that stops the recursion, so `printHello` continues calling itself and filling the stack:

```js
// ...
// printHello() -- "hello"
// printHello() -- "hello"
// printHello() -- "hello"
// printHello() -- "hello"
// printHello() -- "hello"
// printHello() -- "hello"
// ----
// call stack
```

And then, we get the call stack size error:


![Image](https://www.freecodecamp.org/news/content/images/2022/10/call-stack-error-1.png)
_Maximum Call Stack Size Exceeded Error_

To avoid this infinite recursion that maxes out the call stack, we need a condition that stops the recursion.

## General Case and Base Case in Recursion

A General case (also called Recursive case) in recursion is the case that causes the function to keep recursing (calling itself).

A Base case in recursion is the halting point of the recursive function. It is the condition you specify to stop the recursion (just like stopping a loop).

Here's an example:

```js
let counter = 0

function printHello() {
  console.log("hello")
  counter++
  console.log(counter)

  if (counter > 3) {
    return;
  }

  printHello()
}

printHello()
```

Here, our general case is not stated explicitly, but implicitly: **if the counter variable IS NOT GREATER than 3, the function should keep calling itself**.

While the base case, explicitly stated, is, **if the counter variable IS GREATER than 3, the function should end execution**. This case will cause all the recursive functions on the call stack to be popped out, since the recursion has ended.

This is what the call stack would look like when `printHello()` is called the first time:

```js
// printHello()
// ----
// call stack
```

Then "hello" is logged, the `counter` variable is incremented by 1 (which makes it **1**), and the `counter` variable is also logged. The base case is checked. "`counter` is not greater than **3**", so the condition isn't met yet. 

The next line in the function is `printHello()` and in the call stack:

```js
// printHello()
// printHello() -- "hello" -- 1
// ----
// call stack
```

"hello" is logged again, and the `counter` variable is incremented and also logged. The base case is not met as "`counter` is still not greater than **3**". Then, the `printHello()` in the second function is called and the call stack looks like this:

```js
// printHello()
// printHello() -- "hello" -- 2
// printHello() -- "hello" -- 1
// ----
// call stack
```

The same cycle happens, and `printHello()` is called again:

```js
// printHello()
// printHello() -- "hello" -- 3
// printHello() -- "hello" -- 2
// printHello() -- "hello" -- 1
// ----
// call stack
```

After "hello" is logged to the console, `counter` is incremented by 1 (making it **4**). "4 is greater than 3" which meets our base case, so the `return` statement is executed. 

It doesn't matter what we are returning, but `return` stops the execution of a function. This means that the fourth `printHello()` in our call stack will not be able to call `printHello()` again as that line is not reached.

What happens next is that the fourth `printHello()` is popped out of the call stack as it has finished execution:

```js
// printHello() -- "hello" -- 3
// printHello() -- "hello" -- 2
// printHello() -- "hello" -- 1
// ----
// call stack
```

For the third `printHello()`, after the line where it calls itself, there's nothing left in the function to be executed. So this means that the third `printHello()` has also completed its execution, and will be popped out of the call stack:

```js
// printHello() -- "hello" -- 2
// printHello() -- "hello" -- 1
// ----
// call stack
```

Same thing for the second and first `printHello()`, thereby making the call stack empty:

```js
// ----
// call stack
```

So you see how we have avoided an infinite recursion by providing a base case. A recursive function should have **AT LEAST ONE BASE CASE** (you can have as many as you want) to ensure that the recursion doesn't run forever.

There are different ways you can write base cases. Here is one where the general case is explicit, while the base case is implicit:

```js
let counter = 0

function printHello() {
  console.log("hello")
  counter++
  console.log(counter)

  if (counter < 4) {
      printHello()
  }

  return;
}

printHello()
```

Here, we have the general case which tells the function to keep recursing. The case here is **if counter IS LESS than 4**. So if this case is met, the recursion keeps happening.

But the base case which is not as explicit as the former example is **if counter is NO LONGER LESS than 4**, proceed to the next line. This executes `return` and the function ends. Then everything on the call stack starts popping off as they have completed execution.

## Wrapping up

Recursion is not exactly a replacement for loops. But in some cases, recursion can be more effective and easier to read with fewer lines of code.

In this article, you've learned the concept of recursion, which is when a function calls itself for as long as a general case is met until a base case stops it. You've also seen how it compares to loops, and how it works with the call stack.

As a real-life example, check out my post here where I explain [How to find the factorial of a number using Recursion in JavaScript](https://dillionmegida.com/p/factorial-with-recursion-in-js)


