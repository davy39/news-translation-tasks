---
title: How not to be afraid of JavaScript anymore
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-24T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-not-to-be-afraid-of-javascript-anymore-c40780dc071
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OQO-Q5kH6KyxOGXf.jpg
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Neil Kakkar

  Things to know to be a great Javascript developer

  Have you been there before? Where Javascript just doesn’t seem to work. Where the
  functions you write don’t do what you expect them to? Where this just doesn’t make
  sense? What is this?...'
---

By Neil Kakkar

#### Things to know to be a great Javascript developer

Have you been there before? Where Javascript just doesn’t seem to work. Where the functions you write don’t do what you expect them to? Where `this` just doesn’t make sense? What is `this`? This is `this`.

I have. So, I wrote this article. It covers everything from closures and classes to objects and hoisting.

It has helped me become a better developer. I hope it helps you too.

### Data Model

#### The types

Stick with me. I’m doing this because there are two not so well-known types I want you to know about: Symbols and Numbers.

Also the difference between undefined and null eludes many.

* [Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
* [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
* [Boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
* [Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
* [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
* [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
* [undefined](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined) and [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null)

#### Numbers

All numbers in JS are “double precision 64-bit format IEEE 754 values”. Commonly known as floats, which means there is no concept of an integer. Your integers are stored as floats.

To convert strings to numbers: use `parseInt('123', 10)` . The second argument is the base. So, when dealing with binary, you could do:

```js
> parseInt('101',2)
5
```

Similarly, `parseFloat('number')` exists for floating point numbers. The base here is always 10.

#### Symbols

The only purpose of this data type is to identify object properties. Iteration protocol and Regex are the most popular examples using Symbols. We’ll cover the iteration protocol in the next part!

You can create one via `Symbol()`. Every call generates a new symbol. Thus,

```js
console.log(Symbol(42) === Symbol(42)) // false
```

Symbols can persist across files in JavaScript. In this sense, they are different from global variables.

There exists a global symbol registry which stores all symbols encountered. To add a Symbol to the registry, use `Symbol.for()`, and to retrieve the symbol use `Symbol.keyFor()`.

More information on Symbols see [here](https://developer.mozilla.org/en-US/docs/Glossary/Symbol).

#### Undefined and Null

Why the distinction between undefined and null?

By convention, Null indicates a deliberate non-existing value. And undefined is an un-initialized value.

For example, say you have a field which stores an ID if it exists. In this case, instead of using a magic value like “NOT_EXISTS”, you can use null. If it’s supposed to exist but isn’t there right now, you can show that via undefined.

### Variables and scopes

#### Before ES2015

`var` was the only way to define variables.

Further, we had only two scopes: [**global**](https://developer.mozilla.org/en-US/docs/Glossary/global_scope) and **function** scope. Variables declared inside a function become local to that function. Anything outside the function scope couldn’t access them.

Thus, they had function scope.

#### After ES2015

ES2015 introduced two new ways of defining variables:

* `let`
* `const`

With them came the concept of **block** scope. A block is everything between two curly braces `{..}`

ES2015 is backwards compatible, so you still can use var, although their usage is discouraged.

```js
var x = 1;
{
  var x = 2;
}
console.log(x) // OUTPUT: 2, as block doesn't mean anything to var.
let x = 1;
{
  let x = 2;
}
console.log(x) // OUTPUT: 1
```

#### Variable Hoisting

JavaScript has a peculiar idea with `var` called hoisting.

```js
function something() {
  console.log(name);
  let name = 'neil';
  console.log(name);
}
```

Can you guess what would happen above?

I say a `ReferenceError`: we are using the variable name before it’s defined. It makes sense, that’s what happens.

However, if I were using `var` instead of `let`, I’d get no error.

```js
function something() {
  console.log(name); // OUTPUT: undefined
  var name = 'neil';
  console.log(name); // OUTPUT: neil
}
```

What’s happening behind the scenes?

```js
function something() {
  var name; // variable hoisting

  console.log(name); // OUTPUT: undefined
  name = 'neil';
  console.log(name); // OUTPUT: neil
}
```

This is another reason why the use of `var` is discouraged. It can lead to interesting bugs.

### Short circuit logic: && and ||

With JavaScript, something peculiar goes on with logic operations. (And in Python too.)

Something that lets you do arcane stuff like this:

```js
// o is an object
var name = o && o.name;
```

What do you think `name` is? If the object, `o` is null or undefined, `name` is null or undefined.

If `o` is defined but `o.name` is undefined, `name` is undefined.

If `o` is defined, `o.name` is defined, then `name = o.name`.

We were using a boolean logic operator right? How is this possible then?  
The answer is short circuiting and truthiness.

#### Truthiness

A value is truthy if it evaluates to true in a Boolean context. All values are truthy except for the following falsy values:

* `false`
* `0`
* `""`
* `null`
* `undefined`
* `NaN`

Note: which means, `{}` and `[]` are truthy!

A usual trick to convert something to its truthy value: `!!`

`!` converts to not — the falsy value — and `!` again converts it back to true/false.

#### Short circuiting

The idea is Boolean operators return the final value that makes the statement true or false, not whether the statement is true or false. Like we saw above, to convert it to the truthy value, you can use `!!`.

Short circuiting happens when the boolean expression isn’t evaluated completely. For example,

`null && ...`

It doesn’t matter what `...` is. `null` is falsy, so this expression would return `null`.

Same case with `[] || ...`. `[]` is truthy, so this expression would return `[]`, irrespective of what `...` is.

### Objects

An Object in JavaScript is a collection of name value pairs. If you’re coming from [How not to be afraid of Python anymore](https://neilkakkar.com/How-not-to-be-afraid-of-Python-anymore.html), don’t confuse the Python Object with the JavaScript Object.

The closest equivalence to the JavaScript `Object` is the Python `dict`.

For the types available in an Object, name: `string` or `Symbol` value: Anything.

`Arrays` are a special type of object. They have a magic property: length (and a different prototype chain. See below.) The length of the array is one more than the highest index. This is mutable, which means you can do funky stuff with it (not recommended):

```js
const funkyArray = [];
funkyArray['0'] = 'abcd';
funkyArray['length'] = 3

> console.log(funkyArray);
(3) ["abcd", empty × 2]

> funkyArray[4] = 'x';
> console.log(funkyArray);
(5) ["abcd", empty × 3, "x"]
```

Notice the use of numbers and strings as array indexes. Numbers work because Objects implicitly call `toString()` on the name.

Iterating over arrays and objects, using constructs like `for...of`, `for...in` and `forEach` is something I’ll leave for the next part. (Plus, an interesting bug when using objects as maps in JavaScript!)

#### Global object

A global object is an [object](https://developer.mozilla.org/en-US/docs/Glossary/object) that always exists in the global scope. In JavaScript, there’s always a global object defined. In a web browser, when scripts create global variables, they’re created as members of the global object [[1](https://neilkakkar.com/How-not-to-be-afraid-of-Javascript-anymore.html#fn:1)]. The global object’s interface depends on the execution context in which the script is running. For example:

* In a web browser, any code which the script doesn’t specifically start up as a background task has a Window as its global object. This is the vast majority of JavaScript code on the Web.
* Code running in a Worker has a WorkerGlobalScope object as its global object.
* Scripts running under Node.js have an object called global as their global object. [[2](https://neilkakkar.com/How-not-to-be-afraid-of-Javascript-anymore.html#fn:2)]

### Functions

In JavaScript, functions are first class objects. They can have properties and methods like any other objects. They can be passed to other functions as parameters (meta-recursion!). The way functions differ from objects is that they are callable.

All functions extend the [**Function**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function) object. This object has no properties or methods pre-defined, but inherits some from the `Function.prototype`. (This will become clear in the prototype section below). Further, this `Function` object is a constructor for functions. You can create functions in at least 4 ways:

```js
function functionDeclaration() {};
var anonymousFunctionExpression = function() {};
var namedFunctionExpression = function named() {};
var arrowFunctionExpression = () => {};
var constructorFunction = new Function(...args, functionBody); // functionBody is a string
```

The return statement can return a value at any time, terminating the function. JavaScript returns undefined if it sees no return statement (or an empty return with no value).

All arguments defined for the function go in arguments var. The default value for all the arguments is `undefined`.

Have you ever seen the three dots in JavaScript before? `...` . Like the one I used above in `constructorFunction` ? They boggled my mind the first time I saw them. They are a part of syntax in JavaScript. It’s not pseudocode (like I first thought).

They are the `rest` and `spread` parameter syntax.

The are opposites of each other. `spread` spreads arguments, `rest` brings them back together.

Here’s an example: Excuse the poorly designed function — which doesn’t need the arguments to be named — but I am making a point.

```js
const average = function( val1, val2, val3, ...otherValues) { // rest
  console.log(otherValues);
  let sum = 0;
  for (let i = 0; i < arguments.length; i++) { 
    sum += arguments[i];
  }
  return sum / arguments.length;
}
let values = [1, 2, 3, 4, 5, 6]
const averageValue = average(...values); // spread
```

What’s happening here? `otherValues` is using the rest syntax to collect an infinite number of arguments passed to average. The `console.log()` would print `[4, 5, 6]` above.

`values` is using the spread syntax to convert the array into single arguments. It works such that behind the scenes, the below is equivalent to the above.

```
const averageValue = average(1,2,3,4,5,6)
```

Another thing to note is that default argument values are evaluated every time function is called, unlike Python where it happens only once.

There are 3 interesting prototype functions available to function objects. These are `apply()`, `bind()` and `call()`. The A,B,C of JavaScript.

With the advent of spread and rest syntax, `apply()` and `call()` aren’t different anymore.

`apply()` calls a function with an array of args; `call()` calls a function with individual values.

The cool bit is, they allow you to call the function with a custom `this` object.

We will talk more about `apply()` and `bind()` once we cover the `this` object.

#### Anonymous and inner functions

```js
const avg = function () {
  let sum = 0;
  for (let i = 0, argLength = arguments.length; i < argLength; i++) { // arguments variable is an array containing all args passed to the function.
    sum += arguments[i];
  }
  return sum / arguments.length; // argLength isn't available here
};
```

The expressions `function avg()` and `var avg = function ()` are semantically equivalent.

However, there is a distinction between the function name (here anonymous — so doesn’t exist) and the variable the function is assigned to.

The function name cannot be changed, while the variable the function is assigned to can be reassigned. The function name can be used only within the function’s body. Attempting to use it outside the function’s body results in an error (or undefined if the function name was previously declared via a var statement).

This idea of functions being passed as variables gives rise to enormous power. For example, you can hide local variables:

```js
var a = 1;
var b = 2;
(function() {
  var b = 3; // hidden local variable
  a += b;
})();
a; // 4
b; // 2
```

The expression above is called an IIFE (Immediately invoked function expression) — where you create a function and immediately call it.

Further, we can nest functions inside each other too! These are called **inner functions**. The important thing to keep in mind: inner functions have access to variables defined in the parent functions, but not the other way around. This is a direct result of closures, which we will cover soon.

This lets you create functions like:

```js
let joiner = function(separator) {    // The outer function defines separator
    return function(left, right) {      
        return left + " " + separator + " " + right;    // The inner function has access to separator
    }    // This exposes the inner function to the outside world
}
let and = joiner("and");
and("red", "green"); // There's no way to change the separator for AND now; except by reassigning the function variable.
// red and green
const or = joiner("or"); // There's no way to change the separator for OR now.
or("black", "white"); 
// black or white
```

#### Function hoisting

> _With function declarations, the function definitions are hoisted to the top of the scope._  
> _With function expressions, the function definitions aren’t hoisted_.

Okay, you might be confused about what’s the difference between the terms. I was.

```js
function declaredFunction() { // this is the function declaration
    // what comes here is the function definition
}
let functionExpression = function() { // this is a function expression
    // what comes here is the function definition
}
```

### Classes and The Prototype Chain

JavaScript uses functions as classes. The recently introduced class statement is syntactic sugar over functions.

Since all data in JavaScript is an `Object`, it makes sense that our functions — which are a class constructor — will return an `Object`.

Thus, given all the basics we know about functions and objects, we can do something like this to create a class for, say _(thinks really hard to figure out a non trivial, useful and relatable example…)_  
….   
…   
..   
.  
A tweet interface! That sounds like fun.

Imagine you’re building your own front-end to show tweets, talking to the twitter API to get data for the tweets.

```js
function Tweet(id, username, content, parent = null) {
  return {
    id, // Javascript implicitly converts this into id: id
    username,
    content,
    getUrl: function() {
      return 'https://twitter.com/' + this.username + '/' + this.id;
    },
    isComment: function() {
      return parent !== null;
    }
  };
}
var t = Tweet(1, '@neilkakkar', 'How not to be afraid of JS anymore'); 
// Remember, we can fill any number of args
// the rest are undefined or default
// All args are in the arguments variable
t.getUrl(); // "https://twitter.com/@neilkakkar/1"
t.isComment(); // "false"
```

`[this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)` keyword references the current object. Using dot notation, this becomes the object on which dot was applied. Otherwise, it’s the global object.

A note from MDN:

> In most cases, the value of this is determined by how a function is called. It can’t be set by assignment during execution, and it may be different each time the function is called. ES5 introduced the `[bind()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)`method to set the value of a function’s `this` regardless of how it’s called, and ES2015 introduced arrow functions which don’t provide their own this binding (it retains the `this` value of the enclosing lexical context).

This (pun intended) is a frequent cause of mistakes. For example:

```js
const t = Tweet(1, '@neilkakkar', 'How not to be afraid of JS anymore');
const urlFetcher = t.getUrl; // assigning the function
urlFetcher(); // https://twitter.com/undefined/undefined
```

When we call `urlFetcher()` alone, without using `t.getUrl()`, `this` is bound to the global object. Since there are no global variables called `username` or `id` we get `undefined` for each one.

We can take advantage of the `this` keyword to improve our Tweet function. The idea is, instead of creating an object and returning that, we expect a new object (referenced by `this`) and modify its properties.

```js
function Tweet(id, username, content, parent = null) {
  this.id = id;
  this.username = username;
  this.content = content;
  this.getUrl = function() {
      return 'https://twitter.com/' + this.username + '/' + this.id;
  };
  this.isComment = function() {
      return parent !== null;
    }
  };
}
var t = new Tweet(1, '@neilkakkar', 'How not to be afraid of JS anymore');
```

The [new](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new) keyword creates a brand new empty object, and then calls the function specified, with `this` set to the new object. Our modified function does not return a value but merely modifies the `this` object. `new` also returns the `this` object, once the function is called on it. This is what we wanted. `new` also does some extra stuff which we want — like setting up the prototype chain — but we will get into that in a little bit.

Such functions, that are designed to be called by `new`, are called **constructor functions**. By convention, these functions are capitalized (as a reminder to call them with `new`).

Since we get a new object every time we call `Tweet`, we have two function objects (`getUrl` and `isComment`) created every time we call `Tweet`. A better way is to write these functions outside the constructor scope — and pass a reference.

If you’re coming from an OOP background, even this might not seem good enough. You don’t want this function to be used anywhere but for this `Tweet` object. You don’t want to dirty your global function list. This is where JavaScript’s “inheritance” comes in.

### Prototype

`Tweet.prototype` is an object shared by all instances of `Tweet`. It forms part of a lookup chain (that has a special name, “prototype chain”): any time you access a property of `Tweet` that isn’t set, JavaScript will check `Tweet.prototype` to see if that property exists there.

As a result, anything assigned to `Tweet.prototype` becomes available to all instances of that constructor via the `this` object.

> Each object has a private property (`__proto__`) which holds a link to another object called its prototype. That prototype object has a prototype of its own, and so on until an object is reached with null as its prototype. By definition, null has no prototype, and acts as the final link in this prototype chain.

This is an incredibly powerful tool. JavaScript lets you modify something’s prototype at any time in your program, which means you can add extra methods to existing objects at runtime (without having to call the constructor again).

```js
var t = new Tweet(1, '@neilkakkar', 'How not to be afraid of JS anymore');
t.getComments(); // TypeError on line 1: t.getComments is not a function
Tweet.prototype.getComments = function() {
  // example API call to Twitter API - let's say it exists as the twitterService object
  return twitterService.getComments(this.id);
};
t.getComments(); // "[ 'This is an amazing article, thank you!' , 'I love it' ]" 
// fictional comments
```

#### function.prototype vs __proto__

You’ve probably seen both being used interchangably. They aren’t the same. Let’s clear this up.

The `function.prototype` is a constructor for `__proto__`.

`__proto__` is the actual prototype object available on objects.

Thus, `function.prototype` is only available to constructor functions. You can’t access the prototype for a tweet as `t.prototype`, you’ll have to use `t.__proto__`.

But to set the prototype, you’d use `Tweet.prototype.getComments()` like in the above example.

#### A refresher of what we did with functions and classes

* Classes are functions. We began with a function that was creating a new object ( `return {...}`- using object literal syntax), then adding properties to it ( the class data ) and finally returning it.
* Then come constructor functions. These assume there is a given empty object ( initialized via `new` ) and just add the properties to it.
* Then comes the prototype chain, for methods that would be used by all objects of the `class`

Behind the scenes, this is how things work when using the `class` keyword.

### The New Keyword and Apply

We can now explore what happens behind the scenes with `new` and revisit `apply()` from the function prototype. We’ve already seen `bind()`.

The function of `new` is to create an object, pass it to the constructor function (where this object is available as `this`), and set up the prototype chain.

`apply()` takes an object (the `this` value) and an array of arguments to be called on that object.

Putting these two together, we get a trivial implementation of new.

```js
function newNew(constructorFunction, ...args) {
  const thisObject = {}; // create object using object literal syntax
  constructorFunction.apply(thisObject, args); // calls constructorFunction with this set to thisObject and with given args
  // setting up prototype chain is tricky. Need a new prototype for constructorFunction
  // not the Function constructor prototype
  return thisObject;
}
```

### Closures

Remember the joiner function?

```js
let joiner = function(separator) {    // The outer function defines separator
    return function(left, right) {      
        return left + " " + separator + " " + right;    // The inner function has access to separator
    }    // This exposes the inner function to the outside world
}
let and = joiner("and");
and("red", "green"); // There's no way to change the separator for AND now; except by reassigning the function variable.
// red and green
const or = joiner("or"); // There's no way to change the separator for OR now.
or("black", "white"); 
// black or white
```

A function defined inside another function has access to the outer function’s variables. Once the outer function returns, common sense would dictate that its local variables no longer exist.

But they do exist — otherwise, the joiner functions wouldn’t work. What’s more, there are two different “copies” of `joiner()`’s local variables — one in which `separator` is `and` and the other one where `separator` is `or`. How does this work?

#### Scope Object

Whenever JavaScript executes a function, it creates a ‘scope’ object to hold the local variables created within that function. The scope object is initialized with variables passed in as function parameters. This is similar to the global object — as new variables “show up”, they are added to the scope object.

Two key points:

* a brand new scope object is created every time a function starts executing
* unlike the global object, these scope objects cannot be directly accessed from your JavaScript code. There is no mechanism for iterating over the properties of the current scope object.

So when `joiner()` is called, a scope object is created with one property: `separator`, which is the argument passed to `joiner()`. `joiner()` then returns the created function.

Normally JavaScript’s garbage collector would clean up the scope object created for `joiner()` at this point, but the returned function maintains a reference back to that scope object. As a result, the scope object will not be garbage-collected until there are no more references to the function object that `joiner()` returned.

Scope objects form a chain called the scope chain, similar to the prototype chain.

> _A closure is the combination of a function and the scope object in which it was created. Closures let you save state — as such, they can often be used in place of objects_

Thus, you’re creating a closure whenever you’re creating a function inside another function.

#### Performance

To end this section, let’s talk a bit about performance. To optimize performance, get rid of closures not needed. Remember, the reference lives till the scope object is needed, containing all local variables and function arguments.

```js
function f(i) {
    var o = { };  // Some large object
    var a = [ ];  // Some large array
    // `a` and `o` are local variables and thus will get added to the closure object.
    //...
    //...
    // some use case for a and o
    var c = [ 1, 2, 3 ].filter(item => a.indexOf(item) > -1 || o[item]);
    a = undefined;  // Clean up before closure
    o = undefined;  // Clean up before closure
    return function () { // closure created
           return ++i; // we didn't need anything except i for this function,
           // so makes sense to delete everything else from the closure.
    };
}
```

### Execution Model

![Image](https://cdn-media-1.freecodecamp.org/images/lSYVzm-RGiVEPonCG-ku2EQuT7aMJ2ENqzP6)
_[Source](https://www.zeolearn.com/magazine/understanding-the-javascript-event-loop" rel="noopener" target="_blank" title=")_

How does JavaScript run?

This gif shows the different components and how they interact together. Let’s go through them.

#### Call Stack

Each function call is a frame on the stack.

This call stack is a stack of function calls to be executed in order. ( You see why it’s called a stack? )

The frame contains the function arguments and local variables. This is where the scope object, and hence closure is defined!

The functions are popped from the stack when they return.

Every script begins with a `main()` on the stack, as the function containing all other functions in the script.

#### Heap

Every object you create needs a place in memory to live. This place is the heap: A large unstructured region of memory.

If you’re coming from C++ land, heap is where things go when constructed using `new` in C++.

#### Web APIs and Events

Web APIs are low level functions present in the JavaScript runtime to interact with the OS. They are implemented by the browser / host. For ex: `setTimeout()`.

They are called from the stack and begin processing. The function returns at this point (thus popping the stack frame). This is what gives JavaScript the asynchronous characteristic. Almost all its basic APIs are non-blocking.

Have a look at the GIF above — and this bit will become clearer.

These APIs generate a message. This could be an API call to `fetch` data, in which case the message is the data. This could be `setTimeout()`, where the message is empty. This could be an event on a DOM button like `onClick`, where the message is information stored in the button.

The APIs send these messages to the callback queue. They have a callback function which is attached to the message. This callback is received from the call stack (something we provide when calling the API).

> _In web browsers, messages are added anytime an event occurs and there is an event listener attached to it. If there is no listener, the event is lost. So a click on an element with a click event handler will add a message — likewise with any other event._

#### Callback queue

This is a queue containing all tasks that have finished processing. It has a queue of messages with callback functions for each message.

To process a message, the callback function is called with the message as input — but the queue can’t do this, it’s just a message queue. This processing is achieved via the Event Loop.

**Fun-fact**: This queue is commonly known as the macrotask queue. There’s a little microtask queue lurking behind too. Not a lot of people know about this — but it comes into play when dealing with Promises. A story for a future article, perhaps? (Wow, JS is huge, isn’t it?)

#### Event Loop

To call the callbacks in the callback queue, we need to bring them back on the call stack. That’s the only way a function is called.

The Event Loop handles this bit. It’s a running loop that checks if the call stack is empty on every loop.

Once the call stack is empty, the event loop takes the first element from the callback queue and transfers the callback to the call stack.

#### Run-to-completion

In the event loop, every message runs to completion. This means, no new message is added to the call stack while the current message is executing.

#### Execution Model Refresher

Alright, we have covered a lot here. Some code follows, but before that I want to make sure things are clear.

1. Once you execute a script, the `main()` function is added to the call stack.
2. As functions are called from the script, they are added to the call stack. Popped when returned.
3. The scope objects are added with the functions to the call stack.
4. Some functions may also have a processing component — which is handled by APIs. These APIs return a message and callback.
5. The messages are added to the callback queue.
6. The event loop transfers messages from the callback queue to the call stack only when the call stack is empty ( i.e `main()` is popped too)
7. Every message runs to completion (direct consequence of new messages being added only when the stack is empty)

With this refresher in mind, let’s apply it. `setTimeout( callback, t)` is a function (API) as defined above, which takes a callback and adds a message to the callback queue after `t` seconds.

So, what would be the print order below?

```js
console.log('1');
setTimeout( () => console.log(2), 0) // t = 0;
console.log('3');
```

…

..

.

If you guessed `1 2 3`, let’s go through the example.

Initially, we have `main()` on the call stack. Then we move through the script.

We see `console.log(1)` — that gets on the call stack, prints `1` and is popped.

We see `setTimeout()` — that goes on the call stack, passes to the Web API and is popped.

At the same time, since the timeout was for 0 seconds, the callback is passed to the callback queue.

We see `console.log(3)` — that gets on the call stack, prints `3` and is popped.

The script ends, so `main()` is popped.

Now the call stack is empty, so the `setTimeout()` callback is transferred to the call stack.

That is, we have `() => console.log`(2) on the call stack. This is called with t`he n`ull message.

Hence, the order is `1 3 2`.

This is the zero delay gotcha — a handy idea to remind yourself of how the event loop works.

This seems like a good place to stop for now. I hope this article has helped you start to get a better understanding of JavaScript! :)

References:

[1] [Reintroduction to Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript)  
[2] [MDN general docs](https://developer.mozilla.org/en-US/)

[Here is Part 2](https://neilkakkar.com/js-part-2.html) on my blog.

Other stories in this series:

[How not to be afraid of GIT anymore](https://neilkakkar.com/How-not-to-be-afraid-of-GIT-anymore.html)

[How not to be afraid of Vim anymore](https://neilkakkar.com/How-not-to-be-afraid-of-Vim-anymore.html)

[How not to be afraid of Python anymore](https://neilkakkar.com/How-not-to-be-afraid-of-Python-anymore.html)

Read more of my articles on [neilkakkar.com](https://neilkakkar.com/How-not-to-be-afraid-of-Javascript-anymore.html).

