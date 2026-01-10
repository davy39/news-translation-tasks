---
title: JavaScript Execution Context and Hoisting Explained with Code Examples
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-04-27T22:53:14.000Z'
originalURL: https://freecodecamp.org/news/javascript-execution-context-and-hoisting
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/freeCodeCamp-Cover-4.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "JavaScript is an easy-to-learn programming language compared to many of\
  \ its counterparts. However, a few basic concepts need a bit more attention if you\
  \ want to understand, debug, and write better code. \nIn this article, we will learn\
  \ about two such ..."
---

JavaScript is an easy-to-learn programming language compared to many of its counterparts. However, a few basic concepts need a bit more attention if you want to understand, debug, and write better code. 

In this article, we will learn about two such concepts,

* Execution Context
* Hoisting

As a beginner to JavaScript, understanding these concepts will help you understand the `this` keyword, `scope`, and `closure` much more comfortably. So enjoy, and keep reading.

# Execution Context in JavaScript

In general, a JavaScript source file will have multiple lines of code. As developers, we organize the code into variables, functions, data structures like objects and arrays, and more. 

A `Lexical Environment` determines how and where we write our code physically. Take a look at the code below:

```js
function doSomething() {
  var age= 7;
  // Some more code
 }

```

In the above code, the variable `age` is lexically inside the function `doSomething`. 

Please note that our code does not run as-is. It has to be translated by the compiler into computer understandable byte-code. So the compiler needs to map what is lexically placed where in the meaningful and valid way.

Usually, there will be more than one `Lexical Environment` in your code. However, not all the environments get executed at once. 

The environment that helps the code get executed is called the `Execution Context`. It is the code that's currently running, and everything surrounding that helps to run it. 

There can be lots of `Lexical Environment`s available, but the one currently running code is managed by the `Execution Context`.

Check out the image below to understand the difference between a Lexical Environment and Execution Context:

![Image](https://www.freecodecamp.org/news/content/images/2021/04/lexical.gif)
_Lexical Environment vs Execution Context_

So what exactly happens in the Execution Context? The code gets parsed line-by-line, generates executable byte-code, allocates memory, and executes. 

Let's take the same function we have seen above. What do you think may happen when the following line gets executed?

```js
var age = 7;

```

There are many things happening behind the scenes. That piece of source code goes through the following phases before it is finally gets executed:

* **Tokenizing:** In this phase, the source code string breaks into multiple meaningful chunks called `Tokens`. For example, the code `var age = 7;` tokenizes into **var**, **age**, **=**, **7** and, **;**.
* **Parsing:** The next phase is parsing, where an array of tokens turns into a tree of nested elements understood by the language's grammar. This tree is called an `AST` (Abstract Syntax Tree).
* **Code Generation:** In this phase, the AST created in the parsing phase turns into executable byte-code. This executable byte-code is then optimized further by the JIT (Just-In-Time) compiler.

The animated picture below shows the transition of the source code to executable byte-code.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/execution_steps.gif)
_Source Code to Executable Byte-Code_

All these things happen in an `Execution Context`. So the execution context is the environment where a specific portion of the code executes.

There are two types of execution contexts:

* Global Execution Context (GEC)
* Function Execution Context (FEC)

And each of the execution contexts has two phases:

* Creation Phase
* Execution Phase

Let's take a detailed look at each of them and understand them a bit better.

## Global Execution Context (GEC) in JavaScript

Whenever we execute JavaScript code, it creates a Global Execution Context (also knows as Base Execution Context). The global execution context has two phases.

### Creation Phase

In the creation phase, two unique things get created:

* A global object called `window` (for the client-side JavaScript).
* A global variable called `this`.

If there are any variables declared in the code, the memory gets allocated for the variable. The variable gets initialized with a unique value called `undefined`.  If there is a `function` in the code, it gets placed directly into the memory. We will learn more about this part in the `Hoisting` section later.

### Execution Phase

The code execution starts in this phase. Here, the value assignment of the global variables takes place. Please note that no function gets invoked here as it happens in the Function Execution Context. We will see that in a while.

Let's understand both the phases with a couple of examples.

#### Example 1: Load an Empty Script

Create an empty JavaScript file with the name `index.js`. Now create an HTML file with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src='./index.js'></script>
</head>
<body>
    I'm loading an empty script
</body>
</html>
```

Note that we are importing the empty script file into the HTML file using the `<script>` tag. 

Load the HTML file in the browser and open Chrome DevTools (usually using the `F12` key) or equivalent for other browsers. Browse to the `console` tab, type `window`, and press enter. You should see the value as the browser's `Window` object.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-102.png)
_The Window object_

Now, type the word `this` and press enter. You should see the same `Window` object value printed in the browser console.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-103.png)
_Value of 'this'_

Great, now try to check if window is equal to `this`. Yes, it is.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-104.png)
_window is equal to 'this'_

Alright, so what have we learned?

* The Global Execution Context gets created when we load the JavaScript file, even when it is empty.
* It creates two special things for us in its creation phase, that is the `window` object and `this`.
* In Global Execution context, the `window` object and `this` are equal.
* There is nothing to execute as the script file is blank. So nothing happens in the execution phase.

#### Example 2: With Variables and Functions

Let's now see an example with some code in the JavaScript file. We'll add a variable (blog) with a value assigned to it. We'll also define a function with the name `logBlog`.

```js
var blog = 'freeCodeCamp';

function logBlog() {
  console.log(this.blog); 
}

```

In the creation phase:

* The global object `window` and the variable `this` get created.
* Memory gets allocated for the variable `blog` and the function `logBlog`.
* The variable `blog` gets initialized by a special value `undefined`. The function `logBlog` gets placed in the memory directly.

In the execution phase:

* The value `freeCodeCamp` is assigned to the variable `blog`.
* As we have defined the function but not called it yet, the function execution does not take place. We will call the function and see what happens when we learn about the Function Execution Context.

## Function Execution Context (FEC) in JavaScript

When we invoke a function, a Function Execution Context gets created. Let's extend the same example we used above, but this time we will call the function.

```js
var blog = 'freeCodeCamp';

function logBlog() {
  console.log(this.blog); 
}

// Let us call the function
logBlog();
```

The function execution context goes through the same phases, creation and execution. 

The function execution phase has access to a special value called `arguments`. It is the arguments passed to the function. In our example, there are no arguments passed. 

Please note that the `window` object and the `this` variable created in the Global Execution Context are still accessible in this context.

When a function invokes another function, a new function execution context gets created for the new function call. Each of the function execution contexts determines the `scope` of the variables used in the respective functions.

# Hoisting in JavaScript

I hope you enjoyed learning about `Execution Context`. Let's move over to another fundamental concept called `Hoisting`. When I first heard about hoisting, it took some time to realize something seriously wrong with the name `Hoisting`.

In the English language, hoisting means raising something using ropes and pulleys. The name may mislead you to think that the JavaScript engine pulls the variables and functions up at a specific code execution phase. Well, this isn't what happens. 

So let's understand `Hoisting` using the concept of the `Execution Context`.

## Variable Hoisting in JavaScript

Please have a look at the example below and guess the output:

```js
console.log(name);
var name;


```

I'm sure you guessed it already. It's the following:

```shell
undefined

```

However, the question is why? Suppose we use similar code in some other programming language. In that case, we may get an error saying the variable `name` is not declared, and we are trying to access it well before that. The answer lies in the execution context.

In the `creation` phase,

* The memory gets allocated for the variable `name`, and
* A special value `undefined` is assigned to the variable.

In the `execution` phase,

* The `console.log(name)` statement will execute.

This mechanism of allocating memory for variables and initializing with the value `undefined` at the execution context's creation phase is called `Variable Hoisting`.

> The special value `undefined` means that a variable is declared but no value is assigned.

If we assign the variable a value like this:

```js
name = 'freeCodeCamp';
```

The execution phase will assign this value to the variable.

## Function Hoisting in JavaScript

Now let's talk about `Function Hoisting`. It follows the same pattern as `Variable Hoisting`. 

The creation phase of the execution context puts the function declaration into the memory, and the execution phase executes it. Please have a look at the example below:

```js
// Invoke the function functionA
functionA();

// Declare the function functionA
function functionA() {
 console.log('Function A');
 // Invoke the function FunctionB    
 functionB();
}

// Declare the function FunctionB
function functionB() {
 console.log('Function B');
}
```

The output is the following:

```shell
Function A
Function B
```

* The execution context creates the memory for the function and puts the entire function declaration of `functionA` in it.
* The functions create their own execution context. So a similar thing happens for `functionB` as well.
* Next, the functions get executed in their execution context respectively.

Putting the entire function declaration ahead into the memory at the creation phase is called `Function Hoisting`.

## A Few Ground Rules

Since we understand the concept of `Hoisting` now, let's understand a few ground rules:

* Always define variables and functions before using them in your code. It reduces the chances of surprise errors and debugging nightmares.
* Hoisting is only for function declaration, not initialization. Here is an example of function initialization where the code execution will break.

```js
logMe();

var logMe = function() {
  console.log('Logging...');
}
```

The code execution will break because with function initialization, the variable `logMe` will be hoisted as a variable, not as function. So with variable hoisting, memory allocation will happen with the initialization with `undefined`. That's the reason we will get the error:

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-105.png)
_Error in hoisting a function initialization_

Suppose we try to access a variable ahead of declaration and use the `let` and `const` keywords to declare it later. In that case, they will be hoisted but not assigned with the default `undefined`. Accessing such variables will result in the `ReferenceError`. Here is an example:

```js
console.log(name);
let name;
```

It will throw the error:

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-106.png)
_Error with hoisting variable declared with let and const keywords_

The same code will run without a problem if we use `var` instead of `let` and `const`. This error is a safeguard mechanism from the JavaScript language as we have discussed already, as accidental hoisting may cause unnecessary troubles.

# Before We End...

I hope you've found this article insightful, and that it helps you understand the concepts of `Execution Context` and `hoisting` better. I shall write an article on `Scope` and `Closure` soon based on these concepts. Stay tuned.

Let's connect. You will find me active on [Twitter (@tapasadhikary)](https://twitter.com/tapasadhikary). Please feel free to give a follow.

You may also like these articles:

* [The JavaScript `this` Keyword + 5 Key Binding Rules Explained for JS Beginners](https://www.freecodecamp.org/news/javascript-this-keyword-binding-rules/)
* [How to Learn Something New Every Day as a Software Developer](https://www.freecodecamp.org/news/learn-something-new-every-day-as-a-software-developer/)
* [My Favorite JavaScript Tips and Tricks](https://blog.greenroots.info/my-favorite-javascript-tips-and-tricks-ckd60i4cq011em8s16uobcelc)
* [Explain Me Like I am Five: What are ES6 Symbols?](https://blog.greenroots.info/explain-me-like-i-am-five-what-are-es6-symbols-ckeuz5sb8001qafs14of305dw)
* [16 side project GitHub repositories you may find useful](https://blog.greenroots.info/16-side-project-github-repositories-you-may-find-useful-ckk50hic406quhls1dui2d6sd)


