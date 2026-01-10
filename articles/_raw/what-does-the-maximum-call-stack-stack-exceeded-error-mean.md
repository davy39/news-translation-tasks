---
title: What does the "Maximum call stack exceeded" error mean?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-30T07:56:07.000Z'
originalURL: https://freecodecamp.org/news/what-does-the-maximum-call-stack-stack-exceeded-error-mean
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/29-maximum-call-stack-exceeded.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Dillion Megida

  Have you ever gotten an error similar to this? This error occurs because the call
  stack has exceeded its limit. But what does this mean?

  First, let''s understand what the call stack is.

  The Call Stack

  The call stack is a data structu...'
---

By Dillion Megida

Have you ever gotten an error similar to this? This error occurs because the call stack has exceeded its limit. But what does this mean?

First, let's understand what the call stack is.

## The Call Stack

The call stack is a data structure in JavaScript that contains the function(s) being executed. This structure is in a last-in-first-out format. Let's see an example:

```js
function printName() {
  console.log("Dillion")
}

printName()
// Dillion
```

At first, the call stack is empty. When `printName` is declared, the call stack is still empty. When `printName()` is to be executed, it is added to the call stack:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-47.png)

When the function completes, it is removed from the call stack. Function completion happens when:

* all the lines in the function have been executed OR
* a `return` statement is encountered in the function

This way, the call stack can keep track of what function is currently being executed, and from what scope.

Let's see another example:

```js
function printName() {
  function printFirstName() {
    console.log("Dillion")
  }
  
  function printLastName() {
    console.log("Megida")
  }
  
  printFirstName()
  printLastName()
  
  console.log("Dillion Megida")
  
}

printName()
// "Dillion"
// "Megida"
// "Dillion Megida"
```

In this example, we have declared a function called `printName`. In this function, we declare two other functions: `printFirstName` and `printLastName`. Both functions are called, and then the statement `console.log("Dillion Megida")`.

When `printName()` is to be executed, it is added to the call stack:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-49.png)

In `printName()`, when `printFirstName()` is to be executed, it is also added to the call stack (above `printName()` because it has not finished execution yet):


![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-53.png)

After `printFirstName()` has completed execution (which logs "Dillion" to the console), it is removed from the call stack. `printLastName()` is now to be executed, so it is added to the call stack:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-51.png)

After the execution of `printLastName()` (which logs "Megida" to the console), it is removed from the call stack:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-52.png)

`printName()` continues execution which now executes `console.log("Dillion Megida")`. You can see "Dillion Megida" in the console. `printName()` is now done, and removed from the call stack:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-54.png)

This is how the call stack works to keep track of the current function(s) being executed. But the call stack has a maximum size. When you have more functions than is allowed in the call stack, you get the **maximum call stack size exceeded** error.

One popular case in which you can exceed the maximum call stack size is in **recursion**

I have a [video explaining this](https://youtu.be/D71LzJBdaKw) that you can also check out.

## Recursion and the call stack

Take a look at this example:

```js
function printNames() {
  console.log("Dillion")
  
  printNames()
  
  console.log("Megida")
}

printNames()
// "Dillion" - first call
// "Dillion" - second call
// "Dillion" - third call
// "Dillion" - fourth call
// "Dillion" - fifth call
// and so on, until max
```

In this example, we have declared `printNames`. In this function, we first have `console.log("Dillion")`, then we have `printNames()`.

Let's see what happens when we call `printNames()` after the function declaration.

`printNames()`--this is added to the call stack:


![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-55.png)

`console.log("Dillion")` is executed. "Dillion" is logged to the console. Then `printNames()` is executed again, which is added to the call stack as the active function:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-56.png)

We have two functions in the call stack now. The first call of `printNames` and the second call of `printNames` which is called from the first one.

In this second call of the function, `console.log("Dillion")` is executed which logs "Dillion" to the console. Then the line `printNames()` is executed again. A third call, which is added to the call stack as the now active function:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-57.png)

Now we have three functions in the call stack. Since nothing stops these function calls, it's going to happen infinitely until "the call stack cannot take it anymore" 😂:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-58.png)

The call stack has a maximum size of functions that it can hold at the same time. This size might be different in different browsers. When that size has been exceeded, you get the **maximum call stack size exceeded** error.

This would also cause your JavaScript application to be unresponsive. And you definitely do not want this for your users.

When creating recursions in your JavaScript programs, you should also have a **base case**, which terminates the recursions after some calls. This is important so as not to exceed the call stack size and have your application crash.

Here's an example of a base case:

```js
let counter = 0;

function printNames() {
  console.log("Dillion")
  counter++
  
  if (counter < 5) {
    printNames()
  }
  
  console.log("Megida")
}

printNames()

// Dillion
// Dillion
// Dillion
// Dillion
// Dillion
// Megida
// Megida
// Megida
// Megida
// Megida
```

I've updated the code now to have a base case. The base case here is that "if the counter variable is no longer less than 5, stop the recursion". So when the function is called, `printNames()` is added to the call stack. We have `counter` as 0, then we log "Dillion" to the console. After that, we increase `counter` by 1. We then have the condition "if counter is less than 5". Since `counter` is less than 5, we execute `printNames()`.

Now the call stack has the first and second `printNames()` calls.

On the fifth call of `printNames`, the call stack would have 5 calls of `printNames()`:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-59.png)

Remember that the first 4 function calls have not finished. Before they finished, they called another function which was added to the call stack.

At this fifth call, "Dillion" is logged to the console for the fifth time. `counter`, at 4, is incremented by 1 to 5. Then the condition "if counter is less than 5" is checked. `counter` (as 5) is not less than 5, so this is the base case that **tells the recursion to stop**.

Since the function doesn't call itself again, it proceeds to the next line.

Then the next line in the function is executed which is `console.log("Megida")`. After this line, the fifth function in the call stack finishes its execution, and now leaves the call stack.

Now that the fifth function has finished execution, the fourth function can continue from where it stopped. The next line in the fourth function is `console.log("Megida")` which logs "Megida" to the console when executed. Then the fourth function leaves the stack:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-60.png)

And the remaining functions on the stack will finish execution until the stack becomes empty:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-61.png)

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-62.png)

## Wrap up

When you come across the error "Maximum call stack exceeded", the simple meaning is that "the call sack now contains more active functions than it can contain".

The call stack stores the currently executing function or functions. When there are too many functions being executed, the call stack might exceed its size and then throw an error. This usually occurs in cases of recursions that do not have base cases.

If you enjoyed this article, kindly share it with others :)


