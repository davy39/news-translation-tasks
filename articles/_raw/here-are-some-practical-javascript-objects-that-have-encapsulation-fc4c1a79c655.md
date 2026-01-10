---
title: Here are some practical JavaScript objects that have encapsulation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-05T00:59:03.000Z'
originalURL: https://freecodecamp.org/news/here-are-some-practical-javascript-objects-that-have-encapsulation-fc4c1a79c655
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lMkY1zO_hMbQURoXEMuLgA.png
tags:
- name: coding
  slug: coding
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Encapsulation means information hiding. It’s about hiding as much as possible of
  the object’s internal parts and exposing...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Encapsulation means information hiding. It’s about hiding as much as possible of the object’s internal parts and exposing a minimal public interface.

The simplest and most elegant way to create encapsulation in JavaScript is using closures. A closure can be created as a function with private state. When creating many closures sharing the same private state, we create an object.

I’m going to build a few objects that can be useful in an application: Stack, Queue, Event Emitter, and Timer. All will be built using factory functions.

Let’s start.

### Stack

Stack is a data structure with two principal operation: `push` for adding an element to the collection, and `pop` for removing the most recent element added. It adds and removes elements according to the Last In First Out (LIFO) principle.

Look at the next example:

```
let stack = Stack();
stack.push(1);
stack.push(2);
stack.push(3);
stack.pop(); //3
stack.pop(); //2
```

[Let’s implement the stack](https://jsfiddle.net/cristi_salcescu/6a1btczx/) using a factory function.

```
function Stack(){
  let list = [];
  
  function push(value){ list.push(value); }
  function pop(){ return list.pop(); }
  
  return Object.freeze({
    push,
    pop
  });
}
```

The stack object has two public methods `push()` and `pop()`. The internal state can only be changed through these methods.

```
stack.list; //undefined
```

I can’t modify directly the internal state:

```
stack.list = 0;//Cannot add property list, object is not extensible
```

You can find more in the [Discover Functional JavaScript](https://www.amazon.com/dp/B07PBQJYYG) book.

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)

