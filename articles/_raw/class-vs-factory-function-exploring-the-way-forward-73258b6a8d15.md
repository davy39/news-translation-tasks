---
title: 'Class vs Factory function: exploring the way forward'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-25T05:23:38.000Z'
originalURL: https://freecodecamp.org/news/class-vs-factory-function-exploring-the-way-forward-73258b6a8d15
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2g8eIVimndik43W_Jl_OCA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  ECMAScript 2015 (aka ES6) comes with the class syntax, so now we have two competing
  patterns for creating objects. In ord...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

ECMAScript 2015 (aka ES6) comes with the `class` syntax, so now we have two competing patterns for creating objects. In order to compare them, I’ll create the same object definition (TodoModel) as a class, and then as a factory function.

**[TodoModel as a Class](https://jsfiddle.net/cristi_salcescu/m9dhpzfx/)**

```
class TodoModel {
    constructor(){
        this.todos = [];
        this.lastChange = null;
    }
    
    addToPrivateList(){
        console.log("addToPrivateList"); 
    }
    add() { console.log("add"); }
    reload(){}
}
```

**[TodoModel as a Factory Function](https://jsfiddle.net/cristi_salcescu/bcta6yyv/)**

```
function TodoModel(){
    var todos = [];
    var lastChange = null;
        
    function addToPrivateList(){
        console.log("addToPrivateList"); 
    }
    function add() { console.log("add"); }
    function reload(){}
    
    return Object.freeze({
        add,
        reload
    });
}
```

### Encapsulation

The first thing we notice is that all members, fields, and methods of a class object are public.

```
var todoModel = new TodoModel();
console.log(todoModel.todos);     //[]
console.log(todoModel.lastChange) //null
todoModel.addToPrivateList();     //addToPrivateList
```

The lack of encapsulation may create security problems. Take the example of a global object that can be modified directly from the Developer Console.

When using factory function, only the methods we expose are public, everything else is encapsulated.

```
var todoModel = TodoModel();
console.log(todoModel.todos);     //undefined
console.log(todoModel.lastChange) //undefined
todoModel.addToPrivateList();     //taskModel.addToPrivateList
                                    is not a function
```

### this

`this` losing context problems are still there when using class. For example, `this` is losing context in nested functions. It is not only annoying during coding, but it’s also a constant source of bugs.

```
class TodoModel {
    constructor(){
        this.todos = [];
    }
    
    reload(){ 
        setTimeout(function log() { 
           console.log(this.todos);    //undefined
        }, 0);
    }
}
todoModel.reload();                   //undefined
```

or `this` is losing context when the method is used as a callback, like on a DOM event.

```
$("#btn").click(todoModel.reload);    //undefined
```

There are no such problems when using a factory function, as it doesn’t use `this` at all.

```
function TodoModel(){
    var todos = [];
        
    function reload(){ 
        setTimeout(function log() { 
           console.log(todos);        //[]
       }, 0);
    }
}
todoModel.reload();                   //[]
$("#btn").click(todoModel.reload);    //[]
```

#### this and arrow function

The arrow function partially solves the `this` loosing context issues in classes, but at the same time creates a new problem:

* `this` is no longer loosing context in nested functions
* `this` is loosing context when the method is used as a callback
* arrow function promotes the use of anonymous functions

[I refactored the `TodoModel` using the arrow function](https://jsfiddle.net/cristi_salcescu/y0k18og2/). It’s important to note that in the process of refactoring to the arrow function we can loose something very important for readability, the function name. [Look for example](https://jsfiddle.net/cristi_salcescu/y0k18og2/) at:

```
//using function name to express intent
setTimeout(function renderTodosForReview() { 
      /* code */ 
}, 0);

//versus using an anonymous function
setTimeout(() => { 
      /* code */ 
}, 0);
```

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)

