---
title: What Does 'this' Mean in JavaScript? The this Keyword Explained with Examples
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-06-15T21:19:12.000Z'
originalURL: https://freecodecamp.org/news/what-is-this-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/0001-2550990419_20210608_114432_0000.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'To understand what this truly means in JavaScript, let''s take a look at
  a very similar concept in the English Language: Polysemy.

  Let''s consider the word "run". Run is a single word which could mean many different
  things depending on the context.


  “I...'
---

To understand what `this` truly means in JavaScript, let's take a look at a very similar concept in the English Language: **Polysemy.**

Let's consider the word "**run**". Run is a single word which could mean many different things depending on the **context**.

* “I will run home” – means to move quickly on foot
    
* “She ran the 1500m” – means to run in a race
    
* “He is running for president” – means vying for an official position
    
* “The app is running” – means the software application is still open and active
    
* “Go for a run” – means running as a form of exercise
    

*and the list goes on.*

A similar scenario plays out when you use the `this` keyword in your JavaScript code. When you do so, it automatically resolves to an object or scope depending on the context at which is was defined.

What are the possible contexts? And how can we use that information to deduce which object a `this` call will resolve to?

## `this` Context

When used in a function, the `this` keyword simply points to an object to which it is bound. It answers the question of **where it should get some value or data from:**

```js
function alert() { 
  console.log(this.name + ' is calling'); 
}
```

In the function above, the `this` keyword is referring to an object to which it is bound **so it gets the "name" property from there**.

But how do you know which object the function is bound to? How do you find out what `this` is referring to?

To do so, we need to take a detailed look at how functions are bound to objects.

## Types of Binding in JavaScript

There are generally four kinds of bindings:

* Default Binding
    
* Implicit Binding
    
* Explicit Binding
    
* Constructor Call Binding
    

### Default Binding in JavaScript

One of the first rules to remember is that if the function housing a `this` reference is a **standalone function**, then that function is bound to the **global object.**

```javascript
function alert() { 
  console.log(this.name + ' is calling'); 
}

const name = 'Kingsley'; 
alert(); // Kingsley is calling
```

As you can see, `name()` is a standalone, unattached function, so it is bound to the **global scope**. As a result, the `this.name` reference resolves to the global variable `const name = 'Kingsley'`.

This rule, however, doesn't hold if `name()` were to be defined in strict mode:

```js
function alert() { 
  'use strict'; 
  console.log(this.name + ' is calling'); 
}

const name = 'Kingsley'; 
alert(); // TypeError: `this` is `undefined`
```

When set in strict mode, the `this` reference is set to undefined.

### Implicit Binding in JavaScript

Another scenario to look out for is whether the function is attached to an object (its context) **at the call site.**

According to the binding rule in JavaScript, a function can use an object as its context only if that object is bound to it at the call site. This form of binding is known as implicit binding.

Here is what I mean by that:

```js
function alert() { 
  console.log(this.age + ' years old'); 
}

const myObj = {
  age: 22,
  alert: alert
}

myObj.alert() // 22 years old
```

Put simply, when you call a function using dot notation, `this` is implicitly bound to the object the function is being called from.

In this example, since `alert` is being called from `myObj`, the `this` keyword is bound to `myObj`. So when `alert` is called with `myObj.alert()`, `this.age` is 22, which is the `age` property of `myObj`.

Let's look at another example:

```js
function alert() { 
  console.log(this.age + ' years old'); 
}

const myObj = {
  age: 22,
  alert: alert,
  nestedObj: {
    age: 26,
    alert: alert
  }
}

myObj.nestedObj.alert(); // 26 years old
```

Here, because `alert` is ultimately being called from `nestedObj`, `this` is implicitly bound to `nestedObj` instead of `myObj`.

An easy way to figure out which object `this` is implicitly bound to is to look at which object is to the left of the dot (`.`):

```js
function alert() { 
  console.log(this.age + ' years old'); 
}

const myObj = {
  age: 22,
  alert: alert,
  nestedObj: {
    age: 26,
    alert: alert
  }
}

myObj.alert(); // `this` is bound to `myObj` -- 22 years old
myObj.nestedObj.alert(); // `this` is bound to `nestedObj` -- 26 years old
```

### Explicit binding in JavaScript

We saw that implicit binding had to do with having a reference in that object.

But what if we want to **force** a function to use an object as its context without putting a property function reference on the object?

We have two utility methods to achieve this: `call()` and `apply()`.

Along with a couple other set of utility functions, these two utilities are available to all functions in JavaScript via the \[\[Prototype\]\] mechanism.

To explicitly bind a function call to a context, you simply have to invoke the `call()` on that function and pass in the context object as parameter:

```js
function alert() { 
  console.log(this.age + ' years old'); 
}

const myObj = {
  age: 22
}

alert.call(myObj); // 22 years old
```

Now here's the fun part. Even if you were to pass around that function multiple times to new variables (currying), every invocation will use the same context because it has been locked (explicitly bound) to that object. This is called **hard binding**.

```js
function alert() { 
  console.log(this.age); 
} 

const myObj = { 
  age: 22 
}; 

const bar = function() { 
  alert.call(myObj); 
}; 

bar(); // 22
setTimeout(bar, 100); // 22 
// a hard-bound `bar` can no longer have its `this` context overridden 
bar.call(window); // still 22
```

Hard binding is a perfect way to lock a context into a function call and truly make that function into a method.

### Constructor Call Binding in JavaScript

The final and perhaps most interesting kind of binding is the new binding which also accentuates the unusual behavior of JavaScript in comparison to other class-based languages.

When a function is invoked with the `new` keyword in front of it, otherwise known as a **constructor call**, the following things occur:

1. A brand new object is created (or constructed)
    
2. The newly constructed object is \[\[Prototype\]\]-linked to the function that constructed it
    
3. The newly constructed object is set as the `this` binding for that function call.
    

Let's see this in code to get a better understanding:

```js
function giveAge(age) { 
  this.age = age; 
} 

const bar = new giveAge(22); 
console.log(bar.age); // 22
```

By calling `giveAge(...)` with `new` in front of it, we’ve constructed a new object and set that new object as the `this` for the call of `foo(...)`. So `new` is the final way that you can bind a function call’s `this` .

## Wrapping Up

In summary,

* The `this` keyword, when used in a function, binds that function to a context object
    
* There are four kinds of bindings: *default binding, implicit binding, explicit binding and constructor call binding* (*new*)
    
* Knowing these four rules will help you easily discern the context for a `this` reference.
    

![An Image Explaining the 'this' keyword](https://www.freecodecamp.org/news/content/images/2021/06/12.png align="left")

*An Image Explaining the 'this' keyword*

![An Image Explaining the 'this' keyword](https://www.freecodecamp.org/news/content/images/2021/06/13.png align="left")

*An Image Explaining the 'this' keyword*

If you liked or benefited from this article and would like to support me, you can buy me a coffee [here](https://buymeacoffee.com/ubahthebuilder).

You can also reach me on [Twitter](https://twitter.com/UbahTheBuilder). Be sure to check out my [blog](https://ubahthebuilder.tech) for more JavaScript and programming related content.

Thanks and see you soon.
