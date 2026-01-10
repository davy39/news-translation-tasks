---
title: These are the features in ES6 that you should know
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-04T21:37:34.000Z'
originalURL: https://freecodecamp.org/news/these-are-the-features-in-es6-that-you-should-know-1411194c71cb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yZbFWrCpWZnlps21EJ0avQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cristian Salcescu

  ES6 brings more features to the JavaScript language. Some new syntax allows you
  to write code in a more expressive way, some features complete the functional programming
  toolbox, and some features are questionable.

  let and const

  ...'
---

By Cristian Salcescu

ES6 brings more features to the JavaScript language. Some new syntax allows you to write code in a more expressive way, some features complete the functional programming toolbox, and some features are questionable.

### let and const

There are two ways for declaring a variable (`let` and `const`) plus one that has become obsolete (`var`).

## let

`let` declares and optionally initializes a variable in the current scope. The current scope can be either a module, a function or a block. The value of a variable that is not initialized is `undefined` .

Scope defines the lifetime and visibility of a variable. Variables are not visible outside the scope in which they are declared.

Consider the next code that emphasizes `let` block scope:

```javascript
let x = 1;
{ 
  let x = 2;
}
console.log(x); //1
```

In contrast, the `var` declaration had no block scope:

```javascript
var x = 1;
{ 
  var x = 2;
}
console.log(x); //2
```

The `for` loop statement, with the `let` declaration, creates a new variable local to the block scope, for each iteration. The next loop creates five closures over five different `i` variables.

```javascript
(function run(){
  for(let i=0; i<5; i++){
    setTimeout(function log(){
      console.log(i); //0 1 2 3 4
    }, 100);
  }
})();
```

Writing the same code with `var` will create five closures, over the same variable, so all closures will display the last value of `i`.

The `log()` function is a closure. For more on closures, take a look at [Discover the power of closures in JavaScript](https://medium.freecodecamp.org/discover-the-power-of-closures-in-javascript-5c472a7765d7).

## const

`const` declares a variable that cannot be reassigned. It becomes a constant only when the assigned value is immutable.

An immutable value is a value that, once created, cannot be changed. Primitive values are immutable, objects are mutable.

`const` freezes the variable, `Object.freeze()` freezes the object.

The initialization of the `const` variable is mandatory.

## Modules

Before modules, a variable declared outside any function was a global variable.

With modules, a variable declared outside any function is hidden and not available to other modules unless it is explicitly exported.

Exporting makes a function or object available to other modules. In the next example, I export functions from different modules:

```js
//module "./TodoStore.js"
export default function TodoStore(){}

//module "./UserStore.js"
export default function UserStore(){}
```

Importing makes a function or object, from other modules, available to the current module.

```js
import TodoStore from "./TodoStore";
import UserStore from "./UserStore";

const todoStore = TodoStore();
const userStore = UserStore();
```

## Spread/Rest

The `…` operator can be the spread operator or the rest parameter, depending on where it is used. Consider the next example:

```js
const numbers = [1, 2, 3];
const arr = ['a', 'b', 'c', ...numbers];

console.log(arr);
["a", "b", "c", 1, 2, 3]
```

This is the spread operator. Now look at the next example:

```js
function process(x,y, ...arr){
  console.log(arr)
}
process(1,2,3,4,5);
//[3, 4, 5]

function processArray(...arr){
  console.log(arr)
}
processArray(1,2,3,4,5);
//[1, 2, 3, 4, 5]
```

This is the rest parameter.

### arguments

With the rest parameter we can replace the `arguments` pseudo-parameter. The rest parameter is an array, `arguments` is not.

```js
function addNumber(total, value){
  return total + value;
}

function sum(...args){
  return args.reduce(addNumber, 0);
}

sum(1,2,3); //6
```

### Cloning

The spread operator makes the cloning of objects and arrays simpler and more expressive.

The object spread properties operator will be available as part of ES2018.

```js
const book = { title: "JavaScript: The Good Parts" };

//clone with Object.assign()
const clone = Object.assign({}, book);

//clone with spread operator
const clone = { ...book };

const arr = [1, 2 ,3];

//clone with slice
const cloneArr = arr.slice();

//clone with spread operator
const cloneArr = [ ...arr ];
```

### Concatenation

In the next example, the spread operator is used to concatenate arrays:

```js
const part1 = [1, 2, 3];
const part2 = [4, 5, 6];

const arr = part1.concat(part2);

const arr = [...part1, ...part2];
```

### Merging objects

The spread operator, like `Object.assign()`, can be used to copy properties from one or more objects to an empty object and combine their properties.

```js
const authorGateway = { 
  getAuthors : function() {},
  editAuthor: function() {}
};

const bookGateway = { 
  getBooks : function() {},
  editBook: function() {}
};

//copy with Object.assign()
const gateway = Object.assign({},
      authorGateway, 
      bookGateway);
      
//copy with spread operator
const gateway = {
   ...authorGateway,
   ...bookGateway
};
```

## Property short-hands

Consider the next code:

```js
function BookGateway(){
  function getBooks() {}
  function editBook() {}
  
  return {
    getBooks: getBooks,
    editBook: editBook
  }
}
```

With property short-hands, when the property name and the name of the variable used as the value are the same, we can just write the key once.

```js
function BookGateway(){
  function getBooks() {}
  function editBook() {}
  
  return {
    getBooks,
    editBook
  }
}
```

Here is another example:

```js
const todoStore = TodoStore();
const userStore = UserStore();
    
const stores = {
  todoStore,
  userStore
};
```

## Destructuring assignment

Consider the next code:

```js
function TodoStore(args){
  const helper = args.helper;
  const dataAccess = args.dataAccess;
  const userStore = args.userStore;
}
```

With destructuring assignment syntax, it can be written like this:

```js
function TodoStore(args){
   const { 
      helper, 
      dataAccess, 
      userStore } = args;
}
```

or even better, with the destructuring syntax in the parameter list:

```js
function TodoStore({ helper, dataAccess, userStore }){}
```

Below is the function call:

```js
TodoStore({ 
  helper: {}, 
  dataAccess: {}, 
  userStore: {} 
});
```

## Default parameters

Functions can have default parameters. Look at the next example:

```js
function log(message, mode = "Info"){
  console.log(mode + ": " + message);
}

log("An info");
//Info: An info

log("An error", "Error");
//Error: An error
```

## Template string literals

Template strings are defined with the ``` character. With template strings, the previous logging message can be written like this:

```js
function log(message, mode= "Info"){
  console.log(`${mode}: ${message}`);
}
```

Template strings can be defined on multiple lines. However, a better option is to keep the long text messages as resources, in a database for example.

See below a function that generates an HTML that spans multiple lines:

```js
function createTodoItemHtml(todo){
  return `<li>
    <div>${todo.title}</div>
    <div>${todo.userName}</div>
  </li>`;
}
```

## Proper tail-calls

> _A recursive function is tail recursive when the recursive call is the last thing the function does._

The tail recursive functions perform better than non tail recursive functions. The optimized tail recursive call does not create a new stack frame for each function call, but rather uses a single stack frame.

ES6 brings the tail-call optimization in strict mode.

[The following function](https://jsfiddle.net/cristi_salcescu/4t2j3uho/) should benefit from the tail-call optimization.

```js
function print(from, to) 
{ 
  const n = from;
  if (n > to)  return;
  
  console.log(n);
    
  //the last statement is the recursive call 
  print(n + 1, to); 
}

print(1, 10);
```

Note: the tail-call optimization is not yet supported by major browsers.

## Promises

_A promise is a reference to an asynchronous call. It may resolve or fail somewhere in the future._

Promises are easier to combine. [As you see in the next example](https://jsfiddle.net/cristi_salcescu/eqyhq2e3/), it is easy to call a function when all promises are resolved, or when the first promise is resolved.

```js
function getTodos() { return fetch("/todos"); }
function getUsers() { return fetch("/users"); }
function getAlbums(){ return fetch("/albums"); }

const getPromises = [
  getTodos(), 
  getUsers(), 
  getAlbums()
];

Promise.all(getPromises).then(doSomethingWhenAll);
Promise.race(getPromises).then(doSomethingWhenOne);

function doSomethingWhenAll(){}
function doSomethingWhenOne(){}
```

The `fetch()` function, part of the Fetch API, returns a promise.

`Promise.all()` returns a promise that resolves when all input promises have resolved. `Promise.race()` returns a promise that resolves or rejects when one of the input promises resolves or rejects.

A promise can be in one of the three states: pending, resolved or rejected. The promise will in pending until is either resolved or rejected.

Promises support a chaining system that allows you to pass data through a set of functions. [In the next example](https://jsfiddle.net/cristi_salcescu/kgxnay46/), the result of `getTodos()` is passed as input to `toJson()`, then its result is passed as input to `getTopPriority()`, and then its result is passed as input to `renderTodos()` function. When an error is thrown or a promise is rejected the `handleError` is called.

```js
getTodos()
  .then(toJson)
  .then(getTopPriority)
  .then(renderTodos)
  .catch(handleError);

function toJson(response){}
function getTopPriority(todos){}
function renderTodos(todos){}
function handleError(error){}
```

In the previous example, `.then()` handles the success scenario and `.catch()` handles the error scenario. If there is an error at any step, the chain control jumps to the closest rejection handler down the chain.

`Promise.resolve()` returns a resolved promise. `Promise.reject()` returns a rejected promise.

## Class

Class is sugar syntax for creating objects with a custom prototype. It has a better syntax than the previous one, the function constructor. [Check out the next exemple](https://jsfiddle.net/cristi_salcescu/aLg8t632/):

```js
class Service {
  doSomething(){ console.log("doSomething"); }
}

let service = new Service();
console.log(service.__proto__ === Service.prototype);
```

All methods defined in the `Service` class will be added to the`Service.prototype` object. Instances of the `Service` class will have the same prototype (`Service.prototype`) object. All instances will delegate method calls to the `Service.prototype` object. Methods are defined once on`Service.prototype` and then inherited by all instances.

### Inheritance

“Classes can inherit from other classes”. Below is an [example of inheritance](https://jsfiddle.net/cristi_salcescu/1xo96yt8/)where the `SpecialService` class “inherits” from the `Service` class:

```js
class Service {
  doSomething(){ console.log("doSomething"); }
}

class SpecialService extends Service {
  doSomethingElse(){ console.log("doSomethingElse"); }  
}

let specialService = new SpecialService();
specialService.doSomething();
specialService.doSomethingElse();
```

All methods defined in the `SpecialService` class will be added to the `SpecialService.prototype` object. All instances will delegate method calls to the `SpecialService.prototype` object. If the method is not found in `SpecialService.prototype`, it will be searched in the `Service.prototype`object. If it is still not found, it will be searched in `Object.prototype`.

### Class can become a bad feature

Even if they seem encapsulated, all members of a class are public. You still need to manage problems with `this` losing context. The public API is mutable.

`class` can become a bad feature if you neglect the functional side of JavaScript. `class` may give the impression of a class-based language when JavaScript is both a functional programming language and a prototype-based language.

Encapsulated objects can be created with factory functions. Consider the next example:

```js
function Service() {
  function doSomething(){ console.log("doSomething"); }
  
  return Object.freeze({
     doSomething
  });
}
```

This time all members are private by default. The public API is immutable. There is no need to manage issues with `this` losing context.

`class` may be used as an exception if required by the components framework. This was the case with React, but is not the case anymore with [React Hooks](https://reactjs.org/docs/hooks-overview.html).

For more on why to favor factory functions, take a look at [Class vs Factory function: exploring the way forward](https://medium.freecodecamp.org/class-vs-factory-function-exploring-the-way-forward-73258b6a8d15).

### Arrow functions

Arrow functions can create anonymous functions on the fly. They can be used to create small callbacks, with a shorter syntax.

Let’s take a collection of to-dos. A to-do has an `id` , a `title` , and a `completed` boolean property. Now, consider the next code that selects only the `title` from the collection:

```js
const titles = todos.map(todo => todo.title);
```

or the next example selecting only the `todos` that are not completed:

```js
const filteredTodos = todos.filter(todo => !todo.completed);
```

### this

Arrow functions don’t have their own `this` and `arguments`. As a result, you may see the arrow function used to fix problems with `this` losing context. I think that the best way to avoid this problem is to not use `this` at all.

### Arrow functions can become a bad feature

Arrow functions can become a bad feature when used to the detriment of named functions. This will create readability and maintainability problems. Look at the next code written only with anonymous arrow functions:

```js
const newTodos = todos.filter(todo => 
       !todo.completed && todo.type === "RE")
    .map(todo => ({
       title : todo.title,
       userName : users[todo.userId].name
    }))
    .sort((todo1, todo2) =>  
      todo1.userName.localeCompare(todo2.userName));
```

[Now, check out the same logic](https://jsfiddle.net/cristi_salcescu/pm7n2ab5/) refactored to pure functions with intention revealing names and decide which of them is easier to understand:

```js
const newTodos = todos.filter(isTopPriority)
  .map(partial(toTodoView, users))
  .sort(ascByUserName);

function isTopPriority(todo){
  return !todo.completed && todo.type === "RE";
}
  
function toTodoView(users, todo){
  return {
    title : todo.title,
    userName : users[todo.userId].name
  }
}

function ascByUserName(todo1, todo2){
  return todo1.userName.localeCompare(todo2.userName);
}
```

Even more, anonymous arrow functions will appear as `(anonymous)` in the Call Stack.

For more on why to favor named functions, take a look at [How to make your code better with intention-revealing function names](https://medium.freecodecamp.org/how-to-make-your-code-better-with-intention-revealing-function-names-6c8b5271693e).

Less code doesn’t necessary mean more readable. [Look at the next example](https://jsfiddle.net/cristi_salcescu/wc8be2gn/)and see which version is easier for you to understand:

```js
//with arrow function
const prop = key => obj => obj[key];

//with function keyword
function prop(key){
   return function(obj){
      return obj[key];
   }
}
```

Pay attention when returning an object. In the next example, the `getSampleTodo()` returns `undefined`.

```js
const getSampleTodo = () => { title : "A sample todo" };

getSampleTodo();
//undefined
```

## Generators

I think the ES6 generator is an unnecessary feature that makes code more complicated.

The ES6 generator creates an object that has the `next()` method. The `next()` method creates an object that has the `value` property. ES6 generators promote the use of loops. [Take a look at code below](https://jsfiddle.net/cristi_salcescu/edq7vfwm/):

```js
function* sequence(){
  let count = 0;
  while(true) {
    count += 1;
    yield count;
  }
}

const generator = sequence();
generator.next().value;//1
generator.next().value;//2
generator.next().value;//3
```

The same generator can be simply implemented with a closure.

```js
function sequence(){
  let count = 0;
  return function(){
    count += 1;
    return count;
  }
}

const generator = sequence();
generator();//1
generator();//2
generator();//3
```

For more examples with functional generators take a look at [Let’s experiment with functional generators and the pipeline operator in JavaScript](https://medium.freecodecamp.org/lets-experiment-with-functional-generators-and-the-pipeline-operator-in-javascript-520364f97448).

# Conclusion

`let` and `const` declare and initialize variables.

Modules encapsulate functionality and expose only a small part.

The spread operator, rest parameter, and property shorthand make things easier to express.

Promises and tail recursion complete the functional programming toolbox.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)

