---
title: How to Use the "this" Keyword in JavaScript
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2023-01-31T23:40:14.000Z'
originalURL: https://freecodecamp.org/news/the-this-keyword-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/brad-_Js9c6w_FDk-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Hey everyone! In this article we''re going to talk about the THIS keyword
  in Javascript.

  This used to be a concept that confused me a little bit, so I''ll try to break it
  down for you so you can understand its uses and in what situations can it be usef...'
---

Hey everyone! In this article we're going to talk about the THIS keyword in Javascript.

This used to be a concept that confused me a little bit, so I'll try to break it down for you so you can understand its uses and in what situations can it be useful. Let's go!

# Table of Contents

* [What's the THIS keyword](#heading-whats-the-this-keyword)
    
* [Calling THIS by itself](#calling-this-by-itself)
    
* [THIS in an object method](#this-in-an-object-method)
    
* [THIS in a function](#this-in-a-function)
    
    * [A note about arrow functions](#heading-a-note-about-arrow-functions)
        
    * [A note about strict-mode](#heading-a-note-about-strict-mode)
        
* [THIS in an event](#this-in-an-event)
    
* [THIS methods (call, apply and bind)](#heading-this-methods-call-apply-and-bind)
    
    * [Call](#call)
        
    * [Apply](#apply)
        
    * [Bind](#bind)
        
* [Wrap up](#wrap-up)
    

# What's the THIS keyword?

Ok, so let's start by defining what the `this` keyword is. In JavaScript, the `this` keyword always refers to an **object**. The thing about it is that the object it refers to will vary depending on how and where `this` is being called.

And there's a few different ways in which you can use the `this` keyword, so let's see the most common cases and how it behaves in each of them.

An important comment is that `this` is not a variable – it's a keyword, so its value can't be changed or reassigned.

# How to Call `this` By Itself

If we call `this` by itself, meaning not within a function, object, or whatever, it will refer to the global window object.

If you print it like `console.log('this alone', this);` you'll get this in your console: `[object Window]`.

Or this if you expand it:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-367.png align="left")

*Expanded result of calling* `this` by itself

# How to Call `this` in an Object Method

But if we call `this` within an object method, like in the following example:

```plaintext
const person = {
    firstName: "John",
    lastName : "Doe",
    id       : 5566,
    getThis : function() {
      return this;
    }
};

console.log('this in object method', person.getThis());
```

We'll see that `this` no longer refers to the object itself:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-368.png align="left")

*Result of calling* `this` within an object method

And given this, we can use `this` to access other properties and methods from the same object:

```javascript
const person = {
    firstName: "John",
    lastName : "Doe",
    id       : 5566,
    getFullName : function() {
      return this.firstName + ' ' + this.lastName;  // Corrected to use `this.firstName`
    }
};

console.log('this in object method', person.getFullName());
```

# How to Call `this` in a Function

If we call `this` within a function like in the following example:

```javascript
function test() {
    console.log('this in a function', this);
}

test()
```

`this` will now refer again to the general window object, and we'll get this in our console: `[object Window]`.

## A note about arrow functions

In arrow functions, JavaScript sets the `this` lexically. This means that the arrow function doesn't create its own [execution context](https://www.javascripttutorial.net/javascript-execution-context/) but inherits the `this` from the outer function where the arrow function is defined.

In most cases, this means `this` will refer to the window object as well:

```javascript
const show = () => this

console.log('arrow function this', show())
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-374.png align="left")

It's important to notice this because, for example, if we try to implement an arrow function to it as an object method, we won't be able to access the object through the `this` keyword:

```javascript
const person = {
    name: 'Pedro',
    surname: 'Sanchez',
    sayName: () => this.name + ' ' + this.surname
}

console.log(person.sayName());
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-375.png align="left")

## A note about strict-mode

When using [strict-mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode), calling `this` within a function will return `undefined`.

```javascript
"use strict";

function show() {
    console.log(this);
}

show();
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-370.png align="left")

As a side comment, if you're not familiar with what strict-mode is, following the [MDN docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode):

> JavaScript's strict mode is a way to *opt in* to a restricted variant of JavaScript, thereby implicitly opting-out of "[sloppy mode](https://developer.mozilla.org/en-US/docs/Glossary/Sloppy_mode)". Strict mode isn't just a subset: it *intentionally* has different semantics from normal code.

Strict mode makes several changes to regular JavaScript semantics:

* Eliminates some JavaScript silent errors by changing them to throw errors.
    
* Fixes mistakes that make it difficult for JavaScript engines to perform optimizations: strict mode code can sometimes be made to run faster than identical code that's not strict mode.
    
* Prohibits some syntax likely to be defined in future versions of ECMAScript.
    

# How to Use `this` in an Event Listener

When using `this` in an event listener, `this` will refer to the DOM element that fired the event.

```javascript
document.getElementById('testBtn').addEventListener('click', function() {
    console.log('this in a event', this);
})
```

In our case, we added the event listener to a button element: `<button id="testBtn">TEST</button>`

And after clicking it, we get the following in our console:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-369.png align="left")

# `this` Methods (call, apply and bind)

To complicate the subject a little more, javascript provides three native methods that can be used to manipulate the way the `this` keyword behaves. These methods are `call`, `apply` and `bind`. Let's see how they work.

## How to Use the Call Method

With `call` we can invoke a method passing an owner object as an argument. Said in a simpler way, we can call a method indicating to which object the keyword `this` will refer to.

Let's see an example:

```javascript
const person1 = {
    name: 'Pedro',
    surname: 'Sanchez',
    sayName: function() {
        return this.name + " " + this.surname;
    }
}

const person2 = {
    name: 'Jimena',
    surname: 'Juarez'
}

console.log(person1.sayName.call(person2));
```

Here we have two person objects. Each with its `name` and `surname` properties, and the `person1` object has a `sayName` method.

Then we call the `person1` `sayName` method in the following way: `person1.sayName.call(person2)`.

By doing this, we're indicating that when the `sayName` method executes, the `this` keyword won't refer to the object that "owns" the method (`person1`) but to the object we passed as parameter (`person2`). As a consequence, we get this in our console:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-376.png align="left")

Keep in mind that if the given method accepts arguments, we can pass them as well when we invoke it with `call`:

```javascript
const person1 = {
    name: 'Pedro',
    surname: 'Sanchez',
    sayName: function(city, country) {
        return this.name + " " + this.surname + ", " + city + ", " + country;
    }
}

const person2 = {
    name: 'Jimena',
    surname: 'Juarez'
}

console.log(person1.sayName.call(person2, "DF", "Mexico"));
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-377.png align="left")

## How to Use the Apply Method

The `apply` method works very similarly to `call`. The only difference between them is that `call` accepts parameters as a list separated by colons (as the last example we saw), and `apply` accepts them as an array.

So if we want to replicate the same example using `apply` we'd have to do it like this:

```javascript
const person1 = {
    name: 'Pedro',
    surname: 'Sanchez',
    sayName: function(city, country) {
        return this.name + " " + this.surname + ", " + city + ", " + country;
    }
}

const person2 = {
    name: 'Jimena',
    surname: 'Juarez'
}

console.log(person1.sayName.apply(person2, ["DF", "Mexico"]));
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-378.png align="left")

## How to Use the Bind Method

Same as `call` and `apply` , the `bind` method indicates the object to which the `this` keyword will refer when a given method executes.

But the difference with `bind` is that it will return a **new function**, without executing it. While with `call` and `apply` the function executed right away, using `bind` we must execute it separately.

Let's see this in an example:

```javascript
const person1 = {
    name: 'Pedro',
    surname: 'Sanchez',
    sayName: function() {
        return this.name + " " + this.surname
    }
}

const person2 = {
    name: 'Jimena',
    surname: 'Juarez'
}

const sayPerson2Name = person1.sayName.bind(person2)

console.log(sayPerson2Name())
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-381.png align="left")

# Wrapping Up

Well everyone, as always, I hope you enjoyed the article and learned something new.

If you want, you can also follow me on [LinkedIn](https://www.linkedin.com/in/germancocca/) or [Twitter](https://twitter.com/CoccaGerman). See you in the next one!

![Image](https://www.freecodecamp.org/news/content/images/2023/01/baby-yoda-bye-bye-icegif.gif align="left")
