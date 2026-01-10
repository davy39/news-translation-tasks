---
title: Removing JavaScript’s “this” keyword makes it a better language. Here’s why.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T21:55:27.000Z'
originalURL: https://freecodecamp.org/news/removing-javascripts-this-keyword-makes-it-a-better-language-here-s-why-db28060cc086
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tLIXa6jWWjxfB-6AYjm2Hg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cristian Salcescu

  Read Functional Architecture with React and Redux and learn how to build apps in
  function style.

  this is of course the source of much confusion in JavaScript. The reason being that
  this depends on how the function was invoked, no...'
---

By Cristian Salcescu

Read [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2) and learn how to build apps in function style.

`this` is of course the source of much confusion in JavaScript. The reason being that `this` depends on how the function was invoked, not where the function was defined.

JavaScript without `this` looks like a better functional programming language.

### this losing context

Methods are functions that are stored in objects. In order for a function to know on which object to work, `this` is used. `this` represents the function’s context.

`this` loses context in many situations. It loses context inside nested functions, it loses context in callbacks.

Let’s take the case of a timer object. The timer objects waits for the previous call to finish before making a new call. It implements the recursive setTimeout pattern. [In the next example](https://jsfiddle.net/cristi_salcescu/h3pbc42u/), in nested functions and callbacks, `this` loses context:

```js
class Timer {
 constructor(callback, interval){
    this.callback = callback;
    this.interval = interval;
    this.timerId = 0;
  }
  
 executeAndStartTimer(){
   this.callback().then(function startNewTimer(){
       this.timerId =  
       setTimeout(this.executeAndStartTimer, this.interval);
   });
 }
    
 start(){
   if(this.timerId === 0){
     this.executeAndStartTimer();
   }
 }
 stop(){
   if(this.timerId !== 0){
     clearTimeout(this.timerId);
     this.timerId = 0;
   }
 }
}

const timer = new Timer(getTodos, 2000);
timer.start();
function getTodos(){
  console.log("call");
  return fetch("https://jsonplaceholder.typicode.com/todos");
}
```

`this` loses context when the method is used as an event handler. Let’s take the case of a React component that builds a search query. In both methods, used as event handlers, `this` loses context:

```js
class SearchForm extends React.Component {
  handleChange(event) {
    const newQuery = Object.freeze({ text: event.target.value });
    this.setState(newQuery);
  }
  search() {
    const newQuery = Object.freeze({ text: this.state.text });
    if (this.props.onSearch) this.props.onSearch(newQuery);
  }
  render() {
    return (
      <form>
      <input onChange={this.handleChange} value={this.state.text} />
      <button onClick={this.search} type="button">Search</button>
      </form>
    );
  }
}
```

There are many solutions for these issues : the `bind()` method, the that/self pattern, the arrow function.

For more on how to fix `this` related issue issues, take a look at [What to do when “this” loses context](https://medium.freecodecamp.org/what-to-do-when-this-loses-context-f09664af076f).

### this has no encapsulation

`this` creates security problems. All members declared on `this` are public.

```js
class Timer {
 constructor(callback, interval){
    this.timerId = "secret";
  }
}

const timer = new Timer();
timer.timerId; //secret
```

### No this, no custom prototypes

What if, instead of trying to fix `this` losing context and security problems, we get rid of it all together?

Removing `this` has a set of implications.

No `this` basically means no `class`, no function constructor, no `new`, no `Object.create()`.

Removing `this` means no custom prototypes in general.

### A Better Language

JavaScript is both a functional programming language and a prototype-based language. If we get rid of `this`, we are left with JavaScript as a functional programming language. That is even better.

At the same time, without `this`, JavaScript offers a new, unique way, of doing Object Oriented Programming without classes and inheritance.

### Object Oriented Programming without this

The questions is how to build objects without `this`.

There will be two kind of objects:

* pure data objects
* behavior objects

#### Pure Data Objects

Pure data objects contain only data and have no behavior.

Any computed field will be fill-in at creation.

Pure data objects should be immutable. We need to `Object.freeze()` them at creation .

#### Behavior Objects

Behavior objects will be collections of closures sharing the same private state.

[Let’s create](https://jsfiddle.net/cristi_salcescu/8z7mLkca/) the Timer object in a `this`-less approach.

```js
function Timer(callback, interval){
  let timerId;
  function executeAndStartTimer(){
    callback().then(function makeNewCall(){
      timerId = setTimeout(executeAndStartTimer, interval);
    });
  }
  function stop(){
    if(timerId){
      clearTimeout(timerId);
      timerId = 0;
    }
  }
  function start(){
    if(!timerId){
      executeAndStartTimer();
    }
  }
  return Object.freeze({
    start,
    stop
  });  
}

const timer = Timer(getTodos, 2000);
timer.start();
```

The `timer` object has two public methods: `start` and `stop`. Everything else is private. There are no `this` losing context problems as there is no `this`.

For more on why to favor a `this`-less approach when building behavior objects take a look at [Class vs Factory function: exploring the way forward](https://medium.freecodecamp.org/class-vs-factory-function-exploring-the-way-forward-73258b6a8d15).

#### Memory

The prototype system is better at memory conservation. All methods are created only once in the prototype object and shared by all instances.

The memory cost of building behavior objects using closures is noticeable when creating thousands of the same object. In an application we have a few behavior objects. If we take for example a store behavior object, there will be only one instance of it in the application, so there’s no extra memory cost when using closures to built it.

In an application there may be hundreds or thousand of pure data objects. The pure data objects don’t use closures, so no memory cost.

### Components without this

`this` may be required by many components’ frameworks, like React or Vue for example.

In React, we can create stateless functional components, without `this`, as pure functions.

```js
function ListItem({ todo }){
  return (
    <li>
      <div>{ todo.title}</div>
      <div>{ todo.userName }</div>
    </li>
  );
}
```

We can also create stateful components without `this` with [React Hooks](https://reactjs.org/docs/hooks-overview.html). [Take a look at the next example](https://codesandbox.io/s/31v5w58wo1):

```js
import React, { useState } from "react";
function SearchForm({ onSearch }) {
  const [query, setQuery] = useState({ text: "" });
  function handleChange(event) {
    const newQuery = Object.freeze({ text: event.target.value });
    setQuery(newQuery);
  }
  function search() {
    const newQuery = Object.freeze({ text: query.text });
    if (onSearch) onSearch(newQuery);
  }
  return (
    <form>
      <input type="text" onChange={handleChange} />
      <button onClick={search} type="button">Search</button>
    </form>
  );
};
```

### Removing arguments

If we get rid of `this`, we should also get rid of `arguments` as they have the same dynamic binding behavior.

Getting rid of `arguments` is pretty simple. We just use the new rest parameter syntax. This time the rest parameter is an array object:

```js
function addNumber(total, value){
  return total + value;
}

function sum(...args){
  return args.reduce(addNumber, 0);
}

sum(1,2,3); //6
```

### Conclusion

The best way to avoid `this` related problems is to not use `this` at all.

JavaScript without `this` can be a better functional programming language.

We can build encapsulated objects, without using `this`, as collections of closures.

With React Hooks we can create `this`-less stateful components.

That being said, `this` can’t be removed from JavaScript without breaking all existing applications. However, something can be done. We can write our own code without `this` and let it be used in libraries.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** **[Functional React](https://www.amazon.com/dp/B088FZQ1XN).**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)

