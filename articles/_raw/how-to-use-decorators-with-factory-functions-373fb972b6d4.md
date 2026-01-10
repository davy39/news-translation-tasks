---
title: How to use Decorators with Factory Functions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-30T00:26:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-decorators-with-factory-functions-373fb972b6d4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3ALgV0tL7sOWLtReXTVDJg.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Method decorators are a tool for reusing common logic. They are complementary to
  Object Oriented Programming. Decorators ...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Method decorators are a tool for reusing common logic. They are complementary to Object Oriented Programming. Decorators encapsulate responsibility shared by different objects.

[Consider the following code](https://jsfiddle.net/cristi_salcescu/0tv3y06p/):

```
function TodoStore(currentUser){
  let todos = [];
  
  function add(todo){
    let start = Date.now();
    if(currentUser.isAuthenticated()){
      todos.push(todo);
    } else {
      throw "Not authorized to perform this operation";
    }
            
    let duration = Date.now() - start;
    console.log("add() duration : " + duration);
  }
    
  return Object.freeze({
    add
  });  
}
```

The intent of the `add()` method is to add new to-dos to the internal state. Beside that, the method needs to check the user authorization and log the duration of execution. These two things are secondary concerns and can actually repeat in other methods.

Imagine we can encapsulate these secondary responsibilities in functions. Then we can write the code in the following way:

```
function TodoStore(){
  let todos = [];
  
  function add(todo){
    todos.push(todo);
  }
    
  return Object.freeze({
     add:compose(logDuration,authorize)(add) 
  }); 
}
```

Now the `add()` method just adds the `todo` to the list. The other responsibilities are implemented by decorating the method.

`logDuration()` and `authorize()` are decorators.

> A **function decorator** is a higher-order function that takes one function as an argument and returns another function, and the returned function is a variation of the argument function.

> Reginald Braithwaite in [Javascript Allongé](https://leanpub.com/javascript-allonge/read#decorators)

### Log Duration

A common scenario is logging the duration of a method call. [The following decorator](https://jsfiddle.net/cristi_salcescu/z8hh356e/) logs the duration of a synchronous call.

```
function logDuration(fn){
  return function decorator(...args){
    let start = Date.now();
    let result = fn.apply(this, args);
    let duration = Date.now() - start;
    console.log(fn.name + "() duration : " + duration);
    return result;
  }
}
```

Notice how the original function was called — by passing in the current value of `this` and all arguments : `fn.apply(this, args)` .

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)

