---
title: JavaScript Interview Prep Cheatsheet – Ace Your Coding Interviews with These
  Concepts
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-07T15:43:17.000Z'
originalURL: https://freecodecamp.org/news/javascript-interview-prep-cheatsheet
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/JS-Interview--2-.png
tags:
- name: coding interview
  slug: coding-interview
- name: Interview tips
  slug: interview-tips
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By rajat gupta

  I''ve carefully gone through over 50 resources, I''ve been through 10 JavaScript
  interviews, and I''ve landed a job at a unicorn startup.

  And throughout this entire process, I started to see a pattern in the most frequently
  asked JS inter...'
---

By rajat gupta

I've carefully gone through over **50** resources, I've been through **10** JavaScript interviews, and I've landed a **job** at a unicorn startup.

And throughout this entire process, I started to see a _pattern_ in the most frequently asked JS interview questions. 

In this article, I have tried to list the concepts which will cover **80%** of any good JS interview.

So, if you are prepping for your next JS interview this is the perfect cheatsheet for you to review and solidify your skills. Go through this and you'll be ready to rock. 💃

## 📝Prerequisites
* Basic knowledge of the web and programming
* Familiarity with HTML/CSS and JavaScript (especially ES6+ syntax)

## Table Of Contents 📜     
* [JavaScript Basics](#heading-javascript-basics) – JS Variables and Array Methods
* [Functional Programming in JavaScript](#heading-functional-programming-in-javascript) – Scope, Closures, and Hoisting
* [Objects in JavaScript](#heading-objects-in-javascript) – Prototypes and "this"
* [Asynchronous JavaScript](#heading-asynchronous-javascript) – Event Loops, Timers, and Promises
* [Advanced JavaScript Concepts to Know](#heading-advanced-javascript-concepts-to-know) - Async/defer, Polyfills, Debouncing, and Throttling 
* [Storage in JavaScript](#heading-storage-in-javascript)

**Caveat:** The focus here will largely be to cover concepts relevant to the interview and not to create a comprehensive booklet for learning the language. Treat this more like a cheatsheet.

If you want to dive in deeply and learn more JS concepts, check out [freeCodeCamp's curriculum](https://www.freecodecamp.org/learn/).

With that out of the way - let's go!

## JavaScript Basics 👶

Let's start off with some basic concepts every JS developer needs to know.

### Variables in JavaScript 📥

Variables are the building blocks of every programming language. You use them to store values. A variable can be a number, string, and many other types. 

Now, JS is a *loosely-typed* language. You don't have to state the type of variable. You can just declare it, and JS will figure it out on its own. 

Now, in JavaScript we have **3** ways to declare variables: `var`, `let`, and `const`.

Here are the key differences: 

![-wnr0JLxh](https://www.freecodecamp.org/news/content/images/2021/06/-wnr0JLxh.png)

Let's try to understand them through examples.

We will cover scope later on. For now, let's focus on the other differences.

```javascript
var a = 3
var a = 4

console.log(a) // 4 as var variables can be redeclared + updated

let b = 3
let b = 4

console.log(b) // Syntax Error as let variables cannot be redeclared

// If we just do, it will work because it can be updated
b = 4 

const c = 3
const c = 4

console.log(c) // Syntax Error as const variables cannot be redeclared or updated

const d

// Will this throw an error? Go through the table and try to find the answer.
```

**Note:** In JavaScript, putting a semi-colon after the end of statement is optional. I will be skipping it here for the sake of readability.

### == vs === in JavaScript

Let's compare some variables. There are two ways you can do that.

`==` only checks for the value

`===` checks for value + type

```javascript

let a = 5 // number
let b = '5' // string

console.log(a == b) // true

console.log(a === b) // false

```

### Arrays in JavaScript

Now that we know a bit about variables, let's move on to arrays and array-methods. 

If we have declared a lot of variables, it makes sense to store them somewhere. Otherwise it will be difficult to keep track of all of them. Arrays are one way of storing a variable. 

```javascript

let a = 4
const b = 5
var c = 'hello'

const array = [a, b, c]

// or you can just directly do

const arr = [4,5,'hello']
```

But only storing variables in an array is kind of boring. We can do more *stuff* with this array (like accessing these variables or changing the order in which they are stored or how they are stored). 

For that, JS has a lot of methods. Let's look at some of them now.

## JavaScript Array Methods 🧰


The most frequently used array methods in JS are: `map`, `filter`, `find`, `reduce`, and `forEach`.

Let's cover `map`, `filter`, and `forEach`. You can explore more in [this helpful article](https://www.freecodecamp.org/news/complete-introduction-to-the-most-useful-javascript-array-methods/).

### The `map` array method

`map` creates a new copy of the original array. We use it when we want to do something with the elements of the original array but don't want to change it.

`map` iterates over the original array and takes a callback function (which we'll cover later) as an argument. In the callback function, we tell it what to do with the elements.

```javascript
const a = [1,2,3,4,5]

// Create a new array which multiplies every element by 2

const d = a.map(function(item){ return item*2 })

console.log(d) // [2,4,6,8,10]
```


### The `filter` array method 

`filter` creates a new array with elements that meet the given condition(s).

Let's look at an example. I have used [arrow functions](https://www.freecodecamp.org/news/arrow-function-javascript-tutorial-how-to-declare-a-js-function-with-the-new-es6-syntax/) here. If you are a little uncomfortable with functions, you can cover the next section first and come back.

```javascript
// Return the words with more than 6 letters
const words = ['react', 'script', 'interview', 'style', 'javascript']

const ans = words.filter((word) => word.length > 6)

console.log(ans) // ['interview', 'javascript']
```

Try to do the exercises yourself first to test your knowledge. If you come up with different or better solutions, let me know!

Generally, a follow up to this: can you do it without the array method?


```javascript
let newArr = []

for (let i = 0; i < words.length; i++) {
  if (words[i].length > 6) {
    newArr.push(words[i])
  }
}
console.log(newArr)
``` 


### The `forEach` array method

`forEach` is very similar to `map` but has two key differences:

First of all, `map` returns a new Array, but `forEach` doesn't.

```javascript
// Return a new array where even numbers are multiplied by 2 
let arr = [1, 2, 3, 4, 5, 6, 7]

function consoleEven(arr) {
  let data = arr.map((num) => (num % 2 === 0 ? num * 2 : num * 1))
  
  console.log(data)  // [1,  4, 3, 8, 5, 12, 7]
}


// ? is the ternary operator. If the condition is true - first statement is returned otherwise the second one.


consoleEven(arr) 

```

```javascript

function consoleEven(arr) {
  let data = arr.forEach((num) => (num % 2 === 0 ? num * 2 : num * 1))
  console.log(data) // undefined
}

consoleEven(arr)
```

And second, you can do method chaining in `map` but not in `forEach`.

```javascript

// Convert  the new array back to original

function consoleEven(arr) {
  let data = arr
    .map((num) => (num % 2 === 0 ? num * 2 : num * 1))
    .map((item) => (item % 2 === 0 ? item / 2 : item / 1))
    
  console.log(data)
}

consoleEven(arr)
```

**Note:** `map` and `forEach` don't mutate (change) the original array.

## Functional Programming in JavaScript 🛠

We have already used functions above. Let's cover them in more detail now. 

Just like how we used variables to store values, we can use functions to store a piece of code which we can reuse.

You can make function in two ways:

```javascript
function a(){
 console.log('I am a normal function');
 }
 
const b = () => {
console.log('I am an arrow function')
}

// They are essentially the same but with a few differences which we will cover as we go along this tutorial. 

// We can pass variables as arguments

const c = (name) => {
console.log(`My name is ${name}`)
}

// `` template literal are a new addition to the language. Very useful for string formatting. Values are accessed using ${} inside them.


// We can even pass functions as arguments to a function. Will see more on this when we try to understand closures.

const greet = () =>  {
    const prefix = 'Mr'
    return (name) => {
        console.log(`${prefix} ${name}, welcome!`)
    }
}

console.log(greet()('Jack'))
```

Now, let's cover some important concepts related to functions.

### Function Scope in JavaScript 🕵️

Scope determines from where the variables are accessible.

There are three types of scope:

* Global (declaration outside of any function)
* Function (declaration inside a function)
* Block (declaration inside a block)

Remember from before that `var` is globally scoped whereas `let` and `const` are block scoped. Let's understand that now.

```javascript

var a = 5 // we can access this a anywhere

function adder(){
    let b = 7
    console.log(a + b)
 }
 
console.log(adder())

console.log(b) // Error as b is not accessible outside the function

{
const c = 10
console.log(c) // 10
}

console.log(c) // Error as c is not accessible outside the block 
```

### Closures in JavaScript (❗important) 🔒

We have already used a closure without even realizing it. In the example below, `prefix` is a closed-over-variable.

```
const greet = () =>  {
    const prefix = 'Mr'
    return (name) => {
        console.log(`${prefix} ${name}, welcome!`)
    }
}

console.log(greet()('Jack'))
```

This section will have a lot of fancy words, so bear with me. We will cover them one by one.

MDN says:

> A function bundled together with its lexical environment forms a closure.

Okay, what is a lexical environment?

It is essentially the surrounding state – the **local memory** along with the lexical environment of its parent.

Whaaat? 🤯 I know it's a bit of a doozy. Let's understand it with a simple example.

```javascript
function x() {
  var a = 7
  function y() {
    console.log(a)
  }
  return y
}

var z = x()
console.log(z) // [Function: y]
z()
```

When x is invoked, y is returned. Now, y is waiting to be executed. Kind of like a loaded gun waiting to be shot! 🔫

So, when we finally invoke z, y is invoked. Now, y has to log `a` so it first tries to find 🔍 it in the **local memory** but it's not there. It goes to its parent function. It finds `a` there.

Voila! There you have it - [this is closure](https://www.freecodecamp.org/news/closures-in-javascript/).

Even when functions are returned (in the above case y) they still remember their lexical scope (where it came from)

Totally unrelated quote for kicks 👻:

> They may forget what you said - but they will never forget how you made them feel - Carl W. Buehner

I swear the rest of the article is legit 🤞 Keep reading.

### Advantages of Closures in JavaScript 😎

- Currying

```javascript
let add = function (x) {
  return function (y) {
    console.log(x + y)
  }
}

let addByTwo = add(2)
addByTwo(3)
```

- Data Hiding/Encapsulation

Suppose you want to create a counter application. Every time you call it, the count increases by 1. But you don't want to expose the variable outside the function. How to do it?

You guessed it – closures!

```javascript
function Counter() {
  var count = 0
  this.incrementCount = function () {
    count++
    console.log(count)
  }
}

console.log(count) // Error: count is not defined
var adder = new Counter()
adder.incrementCount() // 1
```

Don't worry about `this` and `new`. We have a whole section devoted to them down below.

### Disadvantages of Closures in JavaScript 😅

- Overconsumption of memory or memory leaks can happen.

For example, the closed-over-variable will not be garbage collected. This is because, even if the outer function has run, the returned inner function still has a reference to the closed-over-variable.

**Note:** Garbage collection basically removes unused variables from the memory automatically.


### Hoisting in JavaScript 🚩


This is JavaScript's default behavior of moving declarations to the top of the program.

- `var` declaration is hoisted up and initialized with `undefined`.
- `let` and `const` declarations are hoisted up but not initialized.
- `function` definitions are also hoisted up and stored as they are.

Let's look at an example:

```javascript
function consoleNum() {
  console.log(num)
  var num = 10
}

consoleNum() // undefined

// Why no error?

// This is how runtime sees this
{
  var num
  console.log(num)
  num = 9
}

// If instead of var -> let, it will give an error as let values are not initialized
```

Phew! I am done with functions here, but if you want more [check out this amazing talk by Anjana Vakil](https://youtu.be/e-5obm1G_FY) on functional programming.

## Objects in JavaScript 🔮

Just like arrays, objects are a way of storing data. We do so with the help of key-value pairs.

```javascript

    const developer = {
        name: "Raj",
        age: 22
        }
```

`name` is the `key` and `Raj` is the `value`. Keys are generally the name of the properties of the object.

We can store all sorts of data like functions inside an object. You can explore more here on the [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object).

### What is `this` in JavaScript?

Now, working with objects is different in JS than in other popular programming languages like C++. And to understand that properly, we need a good grasp of the `this` keyword.

Let's try to understand it step-by-step.

In a program, at times, we need a way to point at stuff. Like saying this function right here belongs to this object. `this` helps us get this context.

You will understand what I am saying better when we look at some examples.

For now, think of `this` as something which provides context. And remember this important thing: its value depends on how and where it is called.

I know, I know. A lot of `this` 😬. Let's go over all this slowly.

Start a new program and just log `this`.

```javascript

console.log(this)

```

It will point to the window object.

Now, let's take an example with an object:

```javascript
function myFunc() {
    console.log(this)     
  }
 
const obj = {
  bool: true,
  myFunc: myFunc,
}

obj.myFunc()
``` 

Now, `this` will point to the object. So what's happening here?

In the first example, we had nothing left of the `.` so it defaulted to the `window` object. But in this example, we have the object `obj`.

If you do:

```javascript

myFunc() // window

```

We again get the `window` object. So, we can see that the value of `this` depends on how and where are we doing the calling.

What we just did above is called **Implicit Binding**. The value of `this` got bound to the object.

There is another way to use `this`. **Explicit binding** is when you force a function to use a certain object as its `this`.

Let's understand why we need explicit binding through an example.

```javascript

const student_1 =  {
    name: 'Randall',
    displayName_1: function displayName() {
        console.log(this.name)
    }
}
const student_2 =  {
    name: 'Raj',
    displayName_2: function displayName() {
        console.log(this.name)
    }
}

student_1.displayName_1()
student_2.displayName_2()

```

We are using `this` properly, but can you see the problem with the above code?

We are repeating code. And one of the principles of good programming is keep your code DRY! (Don't Repeat Yourself)

So, let's get rid of `displayName_2` and simply do:

```javascript

student_1.displayName_1.call(student_2) // Raj

```

`call` forced `displayName_1` to use the second object as its `this`.

There are a lot of other ways we can do this.

![call-bind-apply.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1622489263380/UwpR9Rscv.png)

Try to solve the given problem yourself.

```javascript
const myData = {
  name: 'Rajat',
  city: 'Delhi',
  displayStay: function () {
    console.log(this.name, 'stays in', this.city)
  },
}
myData.displayStay()

// create an object yourData and try to use displayStay
const yourData = {
 name: 'name',
 city: 'city'
}


// answer
myData.displayStay.call(yourData)
```


Finally, remember that I said that there are differences between arrow and regular functions. 

The case of `this` is one of them.

For an arrow function, the value depends on the lexical scope – that is to say, the outer function where the arrow function is declared.

So, if we make the `displayName()` from above an arrow function, nothing will work.

Arrow functions basically inherit the parent's context which in the above case is the `window`.


### Prototypes and Prototypal Inheritance in JavaScript 👪

> Whenever we create anything (like an object or function) in JavaScript, the JS Engine automatically attaches that thing with some properties and methods.

All this comes via `prototypes`.

`__proto__` is the object where JS is putting it all.

Let's see some examples. Fire up your consoles!

```javascript
let arr = ['Rajat', 'Raj']
console.log(arr.__proto__.forEach)
console.log(arr.__proto__) // same as Array.prototype
console.log(arr.__proto__.__proto__) // same as Object.prototype
console.log(arr.__proto__.__proto__.__proto__) // null
```

All this is called a `prototype chain`.

We can do the same with objects and functions as well.

We will always find `Object.prototype` behind the scenes. That's why you may have heard that everything in JS is an object. 🤯


### What is Prototypal Inheritance in JavaScript?


```javascript
let object = {
  name: 'Rajat',
  city: 'Delhi',
  getIntro: function () {
    console.log(`${this.name}, ${this.city}`)
  },
}

let object2 = {
  name: 'Aditya',
}
```

**Note:** Don't modify prototypes this way. It's just for understanding. [Here's the right way to do it](https://javascript.plainenglish.io/how-prototypal-inheritance-works-in-javascript-and-how-to-convert-it-to-class-based-inheritance-632e31e6350d).

```javascript
object2.__proto__ = object
```

By doing this, `object2` gets access to the object's properties. So, now we can do:

```javascript
console.log(object2.city)
```

This is **prototypal inheritance**.

## Asynchronous JavaScript ⚡

So, JS is a *single-threaded* language. Things happen one at a time. Only after one thing is done can we move to the next thing. 

But this creates problems in the real world, especially, when we are working with browsers.

For example, when we need to fetch data from the web - often times we don't know how long will it take to get it. And whether we will be able to get the data successfully. 

To help with this, asynchronous JS comes into play. 

And the most important concept to understand is the event loop.

### Event Loops in JavaScript ➰

Instead of providing a half-baked explanation here, I highly recommend watching this video by Philip Roberts if you haven't already:

[Learn all about event loops in JS here](https://youtu.be/8aGhZQkoFbQ).


### Timers in JavaScript – setTimeout, setInterval, clearInterval ⏱️

I hope you watched the video. It mentioned timers. Let's talk about them more now. These are very frequently asked about in interviews.

The `setTimeout()` method calls a function or evaluates an expression after a specified number of milliseconds.

`setInterval()` does the same for specified intervals.

```javascript

setTimeout(() => {
    console.log('Here - I am after 2 seconds')
}, 2000);

const timer = setInterval(() => {
    console.log('I will keep on coming back until you clear me')
}, 2000);

```

You use `clearInterval()` to stop the timer.

```
clearInterval(timer)
```

Let's go over some questions that use these concepts.

```javascript
  console.log('Hello')
  setTimeout(() => {
    console.log('lovely')
  }, 0)
  console.log('reader')

  // output
  Hello
  reader
  lovely
``` 

Here's a slightly trickier one:

```javascript
  for (var i = 1; i <= 5; i++) {
    setTimeout(function () {
      console.log(i)
    }, i * 1000)
  }

// output
6
6
6
6
6
```

And here's a short explanation of what's going on there: when `setTimeout` comes again into the picture, the entire loop has run and the value of ` i` has become 6,

Now, let's say we want the outcome to be 1 2 3 4 5 – what do we do?

Instead of `var` ➡️ use `let`.

Why this will work?

`var` is globally scoped but `let` is locally scoped. So for `let` a new `i` is created for every iteration.


### Promises in JavaScript (❗important) 🤝

Promises are at the heart of Asynchronous JS.

> The Promise object represents the eventual completion (or failure) of an asynchronous operation and its resulting value.

A promise can be in one of these three states:

- Pending: initial state, neither fulfilled nor rejected
- Fulfilled: operation was completed successfully
- Rejected: operation failed

```javascript
const promise = new Promise((resolve, reject) => {
  let value = true
  if (value) {
    resolve('hey value is true')
  } else {
    reject('there was an error, value is false')
  }
})

promise
  .then((x) => {
    console.log(x)
  })
  .catch((err) => console.log(err))
```

**Note:** `resolve` and `reject` are just conventional names. Call it pizza🍕 if you like.

Instead of `then/catch`, we can also use `async/await`:

```javascript
async function asyncCall() {
  const result = await promise
  console.log(result)
}

asyncCall()
```

One of the advantages of promises is that they are a much cleaner syntax. Before we had promises, we could easily get stuck in [callback hell](http://callbackhell.com/) 🌋

## Advanced JavaScript Concepts to Know

### 📚 Polyfills in JavaScript

> A polyfill is a piece of code (usually JavaScript on the Web) used to provide modern functionality on older browsers that do not natively support it. [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Polyfill)

- Let's implement it for `map`:

```javascript
// this - array
// this[i] - current value
Array.prototype.myMap = function (cb) {
  var arr = []
  for (var i = 0; i < this.length; i++) {
    arr.push(cb(this[i], i, this))
  }
  return arr
}

const arr = [1, 2, 3]
console.log(arr.myMap((a) => a * 2)) // [2, 4, 6]
```

Notice how we use `this`. Here, we have basically created a new array and are adding values to it.


### Async and defer in JavaScript ✔️

These concepts are frequently asked about in interviews by big corporations like Amazon, Walmart, and Flipkart. 🏢

To understand `async` and `defer`, we need to have an idea of how browsers render a webpage. First, they parse the HTML and CSS. Then DOM trees are created. From these, a render tree is created. Finally, from the render tree - a layout is created and the painting happens.

For a more detailed look, check out [this video](https://youtu.be/SmE4OwHztCc).

Async and defer are `boolean` attributes which can be loaded along with the script tags. They are useful for loading external scripts into your web page.

Let's understand with the help of pictures.

![18-async-defer.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1621781371965/PciAdUTCL.png)
![19-async-defer.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1621781403795/VgIYFtP5T.png)
![20-async.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1621781415787/mJEkxqe_i.png)
![21-defer.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1621781428927/2nUaI8fjr.png)

If there are multiple scripts which are dependant on each other, use `defer`. Defer script are executed in the order which they are defined.

If you want to load external script which is not dependant on the execution of any other scripts, use `async`. 

**Note:** The async attribute does not guarantee the order of execution of scripts.


### Debouncing in JavaScript ⛹️‍♂️

Debouncing is another favorite topic of interviewers.

Let's understand it by creating a search bar.

**Demo:** https://codesandbox.io/s/debounce-input-field-o5gml

Create a simple input field in `index.html` like this:

```javascript
<input type='text' id='text' />
```

Now, in `index.js`. Don't forget to add it to `index.html` first:

```javascript
const getData = (e) => {
  console.log(e.target.value)
}
const inputField = document.getElementById('text')

const debounce = function (fn, delay) {
  let timer
  return function () {
    let context = this
    clearTimeout(timer)
    timer = setTimeout(() => {
      fn.apply(context, arguments)
    }, delay)
  }
}

inputField.addEventListener('keyup', debounce(getData, 300))
```

First, we have selected the input and added an `event listener` to it. Then we created a debounce function which takes a callback function and delay.

Now, inside the debounce function we create a timer using `setTimeout`. Now, this timer's job is to make sure that the next call for `getData` only happens after 300 ms. This is what debouncing is.

Also, we use `clearTimeout` to remove it. Don't want too many of them hanging out there taking up memory space!

Phew! Lots of theory. Let's do a fun challenge. You must have seen the countdown before a game starts (it goes like 10, 9, 8, .... with some delay in between). Try to write a program for it.

Here's how you'd do it:

```javascript
let count = 10

for (let i = 0; i < 10; i++) {
  function timer(i) {
    setTimeout(() => {
      console.log(count)
      count--
    }, i * 500)
  }
  timer(i)
}
```

Were you able to solve it? Did you do it differently? Let me know your solution.


### Throttling in JavaScript 🛑

Let's look at an example again. Suppose that on every window resize event we call an expensive function. Now, we want it such that the expensive function will only be executed once in the given time interval. This is what throttling is.

Create an `index.html` and an `index.js` with the following code:

```javascript
const expensive = () => {
  console.log('expensive')
}

const throttle = (fn, limit) => {
  let context = this
  let flag = true
  return function () {
    if (flag) {
      fn.apply(context, arguments)
      flag = false
    }
    setTimeout(() => {
      flag = true
    }, limit)
  }
}
const func = throttle(expensive, 2000)
window.addEventListener('resize', func)
```

Almost the same as debouncing. The key difference is the `flag` variable. Only, when it's true we are invoking the callback function. And it is set to `true` inside the `setTimeout`. So the value is `true` only after the desired time limit.

### So, what's the difference between debounce and throttling❓

Let's take the search bar 🔍 example from above. When we are debouncing the input field, we are saying to only fetch the data when the difference between two `keyup` events is at least 300 ms.

In the case of throttling, we make a function call only after a certain period of time. 

Suppose that you are searching for an encyclopedia in the search bar. The first call is made on `e` and it took us 300 ms to reach `p`. The next call will be made then only. All the events in between will be ignored.

So, to summarize, debouncing is when the difference between two `keyup` events is 300 ms. And throttling is when the difference between two function calls is 300 ms. Basically, the function is called after a certain interval of time.

## Storage in JavaScript 💾

Finally, a small but important topic to wrap things up.

**localStorage:** Data persists even after closing your session

**sessionStorage:** You lose your data when your session is over, like when you close the browser on the tab.


```javascript
// save
localStorage.setItem('key', 'value')
// get saved data
let data = localStorage.getItem('key')
// remove saved data
localStorage.removeItem('key')
// Same for sessionStorage
``` 

And we are done! 🏁 I hope you feel more confident about your next JS interview now. I wish you all the best.

If you have any queries / suggestions / feedback, you can reach me on Twitter: [https://twitter.com/rajatetc](https://twitter.com/rajatetc).

## 🗃️ Main References
- [MDN Docs](https://developer.mozilla.org/en-US/)
- [Akshay Saini](https://www.youtube.com/channel/UC3N9i_KvKZYP4F84FPIzgPQ)
- [Coding Addict](https://www.youtube.com/channel/UCMZFwxv5l-XtKi693qMJptA)
- [Javascript_Interviews](https://www.instagram.com/javascript_interviews/)


