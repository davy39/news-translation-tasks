---
title: function.prototype.bind and function.prototype.length in JavaScript Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-01T22:01:00.000Z'
originalURL: https://freecodecamp.org/news/function-prototype-bind-and-function-prototype-length-in-javascript-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e57740569d1a4ca3c94.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Function Bind

  bind is a method on the prototype of all functions in JavaScript. It allows you
  to create a new function from an existing function, change the new function’s this
  context, and provide any arguments you want the new function to be called...'
---

## Function Bind

`bind` is a method on the prototype of all functions in JavaScript. It allows you to create a new function from an existing function, change the new function’s `this` context, and provide any arguments you want the new function to be called with. The arguments provided to `bind` will precede any arguments that are passed to the new function when it is called.

### **Using `bind` to change `this` in a function**

The first argument provided to `bind` is the `this` context the function will be bound to. If you do not want to change the value of `this` pass `null` as the first argument.

You are tasked with writing code to update the number of attendees as they arrive at a conference. You create a simple webpage that has a button that, when clicked, increments the `numOfAttendees` property on the confrence object. You use jQuery to add a click handler to your button, but after clicking the button the confrence object has not changed. Your code might look something like this.

```javascript
var nodevember = {
  numOfAttendees: 0,
  incrementNumOfAttendees: function() {
    this.numOfAttendees++;
  }
  // other properties
};

$('.add-attendee-btn').on('click', nodevember.incrementNumOfAttendees);
```

This is a common problem when working with jQuery and JavaScript. When you click the button the `this` keyword in the method you passed to jQuery’s `on` method references the button and not the conference object. You can bind the `this` context of your method to solve the problem.

```javascript
var nodevember = {
  numOfAttendees: 0,
  incrementNumOfAttendees: function() {
    this.numOfAttendees++;
  }
  // other properties
};

$('.add-attendee-btn').on('click', nodevember.incrementNumOfAttendees.bind(nodevember));
```

Now when the button is clicked `this` references the `nodevember` object.

### **Providing arguments to a function with `bind`**

Each argument passed to `bind` after the first will precede any arguments passed when the function is called. This allows you to pre-apply arguments to a function. In the example below, `combineStrings` takes two strings and concatenates them together. `bind` is then used to create a function that always provides “Cool” as the first string.

```javascript
function combineStrings(str1, str2) {
  return str1 + " " + str2
}

var makeCool = combineStrings.bind(null, "Cool");

makeCool("trick"); // "Cool trick"
```

The guide on [this reference](https://guide.freecodecamp.org/javascript/this-reference) has more information about how what the `this` keyword references can change.

More details on the `bind` method can be found on Mozilla’s [MDN docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind).

## **Function Length**

The `length` property on the function object holds the number of arguments expected by the function when called.

```javascript
function noArgs() { }

function oneArg(a) { }

console.log(noArgs.length); // 0

console.log(oneArg.length); // 1
```

### **ES2015 Syntax**

ES2015, or ES6 as it is commonly called, introduced the rest operator and default function parameters. Both of these additions change the way the `length` property works.

If either the rest operator or default parameters are used in a function declaration the `length` property will only include the number of arguments before a rest operator or a default parameter.

```javascript
function withRest(...args) { }

function withArgsAndRest(a, b, ...args) { }

function withDefaults(a, b = 'I am the default') { }

console.log(withRest.length); // 0

console.log(withArgsAndRest.length); // 2

console.log(withDefaults.length); // 1
```

More Information on `Function.length` can be found on [Mozilla’s MDN Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/length).

