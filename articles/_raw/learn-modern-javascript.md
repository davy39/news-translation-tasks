---
title: Modern JavaScript – Imports, Exports, Let, Const, and Promises in ES6+
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2020-12-07T22:47:10.000Z'
originalURL: https://freecodecamp.org/news/learn-modern-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fcb4bbce6787e098393a6fd.jpg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Over the past few years, there have been many updates to the JavaScript
  language. And these updates are very useful if you want to improve your coding.

  ​Keeping abreast of the newest developments in the language is really important.
  It can help you g...'
---

Over the past few years, there have been many updates to the JavaScript language. And these updates are very useful if you want to improve your coding.

​Keeping abreast of the newest developments in the language is really important. It can help you get a higher paying job, keep up to date with the latest trends, improve your code quality, and excel in your current job.

And you definitely need to know the latest features if you're trying to learn a JavaScript library like React or framework like Angular or Vue.

Recently, there have been many useful additions to JavaScript like the **Nullish coalescing operator**, **optional chaining**, **Promises**, **async/await**, **ES6 destructuring**, and more.

So today, we will look at some of these concepts which every JavaScript developer should be aware of.

Let's get started and dive into the things you need to know about JS.

## Let and const in JavaScript

Before ES6, JavaScript used the `var` keyword which only used function and global scope. There was no block-level scope.

With the addition of `let` and `const` JavaScript added block scoping.

### How to use let in JavaScript

When we declare a variable using the `let` keyword, we can **assign** a new value to that variable later but we cannot **re-declare** it with the same name.

```js
// ES5 Code
var value = 10;
console.log(value); // 10

var value = "hello";
console.log(value); // hello

var value = 30;
console.log(value); // 30

```

As you can see above, we have re-declared the variable `value` using the `var` keyword multiple times.

Before ES6, we were able to re-declare a variable that had already been declared before if it wasn't used meaningfully and was instead causing confusion.

But what if we already had a variable declared with the same name somewhere else and we're re-declaring it without realizing it? Then we might override the variable value, causing some difficult to debug issues.

So when you use the `let` keyword, you will get an error when you try to re-declare the variable with the same name – which is a good thing.

```js
// ES6 Code
let value = 10;
console.log(value); // 10

let value = "hello"; // Uncaught SyntaxError: Identifier 'value' has already been declared

```

But, the following code is valid:

```js
// ES6 Code
let value = 10;
console.log(value); // 10

value = "hello";
console.log(value); // hello

```

We don't get an error in the above code because we're **re-assigning** a new value to the  `value` variable. But we're **not re-declaring** `value` again.

Now, take a look at the below code:

```js
// ES5 Code
var isValid = true;
if(isValid) {
  var number = 10;
  console.log('inside:', number); // inside: 10
}
console.log('outside:', number); // outside: 10

```

As you can see in this code, when we declare a variable with the `var` keyword, it's available outside the `if` block also.

Now take a look at the below code:

```js
// ES6 Code
let isValid = true;
if(isValid) {
  let number = 10;
  console.log('inside:', number); // inside: 10
}

console.log('outside:', number); // Uncaught ReferenceError: number is not defined

```

As you can see, the `number` variable when declared using the `let` keyword is only accessible inside the `if` block. Outside the block it's not available, so we got a reference error when we tried to access it outside the `if` block.

But if there is a `number` variable outside the `if` block, then it will work as shown below:

```js
// ES6 Code
let isValid = true;
let number = 20;

if(isValid) {
  let number = 10;
  console.log('inside:', number); // inside: 10
}

console.log('outside:', number); // outside: 20

```

Here, we have two `number` variables in a separate scope. So outside the `if` block, the value of `number` will be 20.

Take a look at the below code:

```js
// ES5 Code
for(var i = 0; i < 10; i++){
 console.log(i);
}
console.log('outside:', i); // 10

```

When using the `var` keyword, `i` is available even outside the `for` loop.

```js
// ES6 Code
for(let i = 0; i < 10; i++){
 console.log(i);
}

console.log('outside:', i); // Uncaught ReferenceError: i is not defined

```

But when using the `let` keyword, it's not available outside the loop.

So as you can see from the above code samples, using `let` makes the variable available only inside that block and it's not accessible outside the block.

We can also create a block by a pair of curly brackets like this:

```js
let i = 10;
{
 let i = 20;
 console.log('inside:', i); // inside: 20
 i = 30;
 console.log('i again:', i); // i again: 30
}

console.log('outside:', i); // outside: 10

```

If you remember, I said we cannot re-declare a `let` based variable in the same block but we can re-declare it in another block. As you can see in the above code, we have re-declared `i` and assigned a new value of `20` inside the block. Once declared, that variable value will be available only in that block.

Outside the block, when we printed that variable, we got `10` instead of the previously assigned value of `30` because outside the block, the inside `i` variable does not exist.

If we don't have the variable `i` declared outside, then we'll get an error as you can see in the below code:

```js
{
 let i = 20;
 console.log('inside:', i); // inside: 20
 i = 30;
 console.log('i again:', i); // i again: 30
}

console.log('outside:', i); // Uncaught ReferenceError: i is not defined

```

### How to use const in JavaScript

The `const` keyword works exactly the same as the `let` keyword in its block scoping functionality. So let's look at how they differ from each other.

When we declare a variable as `const`, it's considered a constant variable whose value will never change.

In the case of `let`, we're able to assign a new value to that variable later like this:

```js
let number = 10;
number = 20;

console.log(number); // 20

```

But we can't do that in case of `const`:

```js
const number = 10;
number = 20; // Uncaught TypeError: Assignment to constant variable.

```

We can't even **re-declare** a `const` variable.

```js
const number = 20;
console.log(number); // 20

const number = 10; // Uncaught SyntaxError: Identifier 'number' has already been declared

```

Now, take a look at the below code:

```js
const arr = [1, 2, 3, 4];

arr.push(5);

console.log(arr); // [1, 2, 3, 4, 5]

```

We said that the `const` variable is constant whose value will never change – but we have changed the constant array above. So how does that make sense?

> Note: Arrays are reference types and not primitive types in JavaScript

So what actually gets stored in `arr` is not the actual array but only the reference (address) of the memory location where the actual array is stored.

So by doing `arr.push(5);` we're not actually changing the reference where the `arr` points to, but we're changing the values stored at that reference.

The same is the case with objects:

```js
const obj = {
 name: 'David',
 age: 30
};

obj.age = 40;

console.log(obj); // { name: 'David', age: 40 }

```

Here, also we're not changing the reference of where the `obj` points to but we're changing the values stored at that reference.

So the above code will work, but the below code will not work.

```js
const obj = { name: 'David', age: 30 };
const obj1 = { name: 'Mike', age: 40 };
obj = obj1; // Uncaught TypeError: Assignment to constant variable.

```

The above code does not work because we're trying to change the reference that the  `const` variable points to.

So the key point to remember when using const is that, when we declare a variable as a constant using const we cannot re-define it. We also cannot re-assign that variable, but we can change the values stored at that location if the variable is of reference type.

So the below code is invalid because we're re-assigning a new value to it.

```js
const arr = [1, 2, 3, 4];
arr = [10, 20, 30]; // Uncaught TypeError: Assignment to constant variable.

```

But note that we can change the values inside the array, as we saw previously.

The following code of re-defining a `const` variable is also invalid.

```js
const name = "David";
const name = "Raj"; // Uncaught SyntaxError: Identifier 'name' has already been declared

```

### let and const wrap up

* The keywords `let` and `const` add block scoping in JavaScript.
* When we declare a variable as `let`, we cannot `re-define` or `re-declare` another let variable with the same name in the same scope (function or block scope) but we can `re-assign` a value to it.
* When we declare a variable as `const`, we cannot `re-define` or `re-declare` another `const` variable with the same name in the same scope (function or block scope). But we can change the values stored in that variable if the variable is of a reference type like an array or object.

Alright, let's move on to the next big topic: promises.

## Promises in JavaScript

Promises are one of the most important yet confusing and difficult to understand part of JavaScript. And most new devs, as well as experienced ones, struggle to understand them.

Promises were added in ES6 as a native implementation.

So what is a promise? A promise represents an asynchronous operation to be completed in the future.

Previously, Before ES6, there was no way to wait for something to perform some operation.

For example, when we wanted to make an API call, there was no way to wait until the results came back before ES6.

For that, we used to use external libraries like Jquery or Ajax which had their own implementation of promises. But there was no browser implemented promise thing.

But now using Promises in ES6, we can make an API call ourselves and wait until it's done to perform some operation.

### How to create a Promise

To create a promise we need to use the `Promise` constructor function like this:

```js
const promise = new Promise(function(resolve, reject) {
 
});

```

The `Promise` constructor takes a function as an argument and that function internally receives `resolve` and `reject` as parameters.

The `resolve` and `reject` parameters are actually functions that we can call depending on the outcome of the asynchronous operation.

A `Promise` goes through three states:

* Pending
* Fulfilled
* Rejected

When we create a promise, it’s in a pending state. When we call the `resolve` function, it goes in a fulfilled state and if we call `reject` it will go in the rejected state.

To simulate the long-running or asynchronous operation, we will use the `setTimeout` function.

```js
const promise = new Promise(function(resolve, reject) {
 setTimeout(function() {
  const sum = 4 + 5;
  resolve(sum);
 }, 2000);
});

```

Here, we've created a promise which will resolve to the sum of `4` and `5` after a 2000ms (2 second) timeout is over.

To get the result of the successful promise execution, we need to register a callback using `.then` like this:

```js
const promise = new Promise(function(resolve, reject) {
 setTimeout(function() {
  const sum = 4 + 5;
  resolve(sum);
 }, 2000);
});

promise.then(function(result) {
 console.log(result); // 9
});

```

So whenever we call `resolve`, the promise will return back the value passed to the `resolve` function which we can collect using the `.then` handler.

If the operation is not successful, then we call the `reject` function like this:

```js
const promise = new Promise(function(resolve, reject) {
 setTimeout(function() {
  const sum = 4 + 5 + 'a';
  if(isNaN(sum)) {
    reject('Error while calculating sum.');
  } else {
    resolve(sum);
  }
 }, 2000);
});

promise.then(function(result) {
 console.log(result);
});

```

Here, if the `sum` is not a number, then we call the `reject` function with the error message. Otherwise we call the `resolve` function.

If you execute the above code, you will see the following output:

![Error without catch](https://gist.github.com/myogeshchavan97/e0be7fc4c838544e2d00afeb3a82ae10/raw/9adf1d42d876e2b87ef0ecfbf97b06a01c026eba/error_no_catch.png)

As you can see, we're getting an uncaught error message along with the message we've specified because calling `reject` function throws an error. But we have not added an error handler for catching that error.

To catch the error, we need to register another callback using `.catch` like this:

```js
promise.then(function(result) {
 console.log(result);
}).catch(function(error) {
 console.log(error);
});

```

You will see the following output:

![Error with catch](https://gist.github.com/myogeshchavan97/e0be7fc4c838544e2d00afeb3a82ae10/raw/9adf1d42d876e2b87ef0ecfbf97b06a01c026eba/error_catch.png)

As you can see, we have added the `.catch` handler, so we're not getting any uncaught error but we're just logging the error to the console.

This also avoids stopping your application abruptly.

So it's always recommended to add the `.catch` handler to every promise so your application will not stop from running because of the error.

### Promise chaining

We can add multiple `.then` handlers to a single promise like this:

```js
promise.then(function(result) {
 console.log('first .then handler');
 return result;
}).then(function(result) {
 console.log('second .then handler');
 console.log(result);
}).catch(function(error) {
 console.log(error);
});

```

When we have multiple `.then` handlers added, the return value of the previous `.then` handler is automatically passed to the next `.then` handler.

![Promise Chaining](https://gist.github.com/myogeshchavan97/e0be7fc4c838544e2d00afeb3a82ae10/raw/9adf1d42d876e2b87ef0ecfbf97b06a01c026eba/promise_chaining.png)

As you can see, adding `4 + 5` resolves a promise and we get that sum in the first `.then` handler. There we're printing a log statement and returning that sum to the next `.then` handler.

And inside the next `.then` handler, we're adding a log statement and then we're printing the result we got from the previous `.then` handler.

This way of adding multiple `.then` handlers is known as promise chaining.

### How to delay a promise's execution in JavaScript

Many times we don't want to create promise immediately but want to create one after some operation is completed.

To achieve this, we can wrap the promise in a function and return that promise from that function like this:

```js
function createPromise() {
 return new Promise(function(resolve, reject) {
  setTimeout(function() {
   const sum = 4 + 5;
   if(isNaN(sum)) {
     reject('Error while calculating sum.');
   } else {
    resolve(sum);
   }
  }, 2000);
 });
}

```

This way, we can use the function parameters inside the promise, making the function truly dynamic.

```js
function createPromise(a, b) {
 return new Promise(function(resolve, reject) {
  setTimeout(function() {
   const sum = a + b;
   if(isNaN(sum)) {
     reject('Error while calculating sum.');
   } else {
    resolve(sum);
   }
  }, 2000);
 });
}

createPromise(1,8)
 .then(function(output) {
  console.log(output); // 9
});

// OR

createPromise(10,24)
 .then(function(output) {
  console.log(output); // 34
});

```

![Output](https://gist.github.com/myogeshchavan97/e0be7fc4c838544e2d00afeb3a82ae10/raw/9adf1d42d876e2b87ef0ecfbf97b06a01c026eba/general_function.png)

**Note:** When we create a promise, it will be either resolved or rejected but not both at the same time. So we cannot add two `resolve` or `reject` function calls in the same promise.

Also, we can pass only a single value to the `resolve` or `reject` function.

If you want to pass multiple values to a `resolve` function, pass it as an object like this:

```js
const promise = new Promise(function(resolve, reject) {
 setTimeout(function() {
  const sum = 4 + 5;
  resolve({
   a: 4,
   b: 5,
   sum
  });
 }, 2000);
});

promise.then(function(result) {
 console.log(result);
}).catch(function(error) {
 console.log(error);
});

```

![Resolving object](https://gist.github.com/myogeshchavan97/e0be7fc4c838544e2d00afeb3a82ae10/raw/65fba14b45b22228f49107634d440903eb0c8dbd/object_resolve.png)

### How to use arrow functions in JavaScript

In all the above code examples, we've used regular ES5 function syntax while creating promises. But it's a common practice to use arrow function syntax instead of ES5 function syntax like this:

```js
const promise = new Promise((resolve, reject) => {
 setTimeout(() => {
  const sum = 4 + 5 + 'a';
  if(isNaN(sum)) {
    reject('Error while calculating sum.');
  } else {
    resolve(sum);
  }
 }, 2000);
});

promise.then((result) => {
 console.log(result);
});

```

You can either use ES5 or ES6 function syntax depending on your preferences and needs.

## ES6 Import And Export Syntax

Before ES6 came into play, we used multiple `script` tags in a single HTML file to import different JavaScript files like this:

```js
<script type="text/javascript" src="home.js"></script>
<script type="text/javascript" src="profile.js"></script>
<script type="text/javascript" src="user.js"></script>

```

So, if we had a variable with the same name in different JavaScript files, it would create a naming conflict and the value you were expecting would not be the actual value you got.

ES6 has fixed this issue with the concept of modules.

Every JavaScript file we write in ES6 is known as a module. The variables and functions we declare in each file are not available to other files until we specifically export them from that file and import them into another file.

So the functions and variables defined in the file are private to each file and can’t be accessed outside the file until we export them.

There are two types of exports:

* Named Exports: There can be multiple named exports in a single file
* Default Exports: There can be only one default export in a single file

### Named Exports in JavaScript

To export a single value as a named export, we export it like this:

```js
export const temp = "This is some dummy text";

```

If we have multiple things to export, we can write an export statement on a separate line instead of in front of variable declaration. We specify the things to export in curly brackets.

```js
const temp1 = "This is some dummy text1";
const temp2 = "This is some dummy text2";

export { temp1, temp2 };

```

Note that the export syntax is not an object literal syntax. So in ES6, to export something we can't use key-value pairs like this:

```js
 // This is invalid syntax of export in ES6

export { key1: value1, key2: value2 }

```

To import the things we exported as a named export, we use the following syntax:

```js
import { temp1, temp2 } from './filename';

```

Note that while importing something from the file, we don't need to add the `.js` extension to the filename as it's considered by default.

```js
// import from functions.js file from current directory 
import { temp1, temp2 } from './functions';

// import from functions.js file from parent of current directory
import { temp1 } from '../functions';

```

Here's a Code Sandbox demo: [https://codesandbox.io/s/hardcore-pond-q4cjx](https://codesandbox.io/s/hardcore-pond-q4cjx)

**One thing to note is that the name used while exporting has to match the name we use while importing.**

So if you are exporting as:

```js
// constants.js
export const PI = 3.14159;

```

then while importing you have to use the same name used while exporting:

```js
import { PI } from './constants';

```

You can't use any other name like this:

```js
import { PiValue } from './constants'; // This will throw an error

```

But if you already have the variable with the same name as the exported variable, you can use the renaming syntax while importing like this:

```js
import { PI as PIValue } from './constants';

```

Here we have renamed `PI` to `PIValue` and so we can’t use the `PI` variable name now. Instead, we have to use the `PIValue` variable to get the exported value of `PI`.

We can also use the renaming syntax at the time of exporting:

```js
// constants.js
const PI = 3.14159; 

export { PI as PIValue };

```

then while importing we have to use `PIValue` like this:

```js
import { PIValue } from './constants';

```

To export something as a named export, we have to declare it first.

```js
export 'hello'; // this will result in error
export const greeting = 'hello'; // this will work
export { name: 'David' }; // This will result in error
export const object = { name: 'David' }; // This will work

```

**The order in which we import the multiple named exports is not important.**

Take a look at the below `validations.js` file:

```js
// utils/validations.js

const isValidEmail = function(email) {
  if (/^[^@ ]+@[^@ ]+\.[^@ \.]{2,}$/.test(email)) {
    return "email is valid";
  } else {
    return "email is invalid";
  }
};

const isValidPhone = function(phone) {
  if (/^[\\(]\d{3}[\\)]\s\d{3}-\d{4}$/.test(phone)) {
    return "phone number is valid";
  } else {
    return "phone number is invalid";
  }
};

function isEmpty(value) { 
  if (/^\s*$/.test(value)) {
    return "string is empty or contains only spaces";
  } else {
    return "string is not empty and does not contain spaces";
  } 
}

export { isValidEmail, isValidPhone, isEmpty };

```

and in `index.js` we use these functions as shown below:

```js
// index.js
import { isEmpty, isValidEmail } from "./utils/validations";

console.log("isEmpty:", isEmpty("abcd")); // isEmpty: string is not empty and does not contain spaces

console.log("isValidEmail:", isValidEmail("abc@11gmail.com")); // isValidEmail: email is valid

console.log("isValidEmail:", isValidEmail("ab@c@11gmail.com")); // isValidEmail: email is invalid

```

Here's a Code Sandbox demo: [https://codesandbox.io/s/youthful-flower-xesus](https://codesandbox.io/s/youthful-flower-xesus)

As you can see, we can import only the required exported things and in any order, so we don’t need to check in what order we exported in another file. That’s the beauty of named exports.

### Default Exports in JavaScript

As I said earlier, there can be at most one default export in a single file.

You can, however, combine multiple named exports and one default export in a single file.

To declare a default export we add the default keyword in front of the export keyword like this:

```js
//constants.js
const name = 'David'; 
export default name;

```

To import the default export we don’t add the curly brackets as we did in named export like this:

```js
import name from './constants';

```

If we have multiple named exports and one default export like this:

```js
// constants.js
export const PI = 3.14159; 
export const AGE = 30;

const NAME = "David";
export default NAME;

```

then to import everything on a single line we need to use the default exported variable before the curly bracket only.

```js
// NAME is default export and PI and AGE are named exports here

import NAME, { PI, AGE } from './constants';

```

**One specialty of default export is that we can change the name of the exported variable while importing:**

```js
// constants.js
const AGE = 30;
export default AGE;

```

And in another file, we can use another name while importing

```js
import myAge from ‘./constants’; 

console.log(myAge); // 30

```

Here, we have changed the name of the default exported variable from `AGE` to `myAge`.

This works because there can be only one default export so you can name it whatever you want.

Another thing to note about default export is that the export default keyword cannot come before variable declaration like this:

```js
// constants.js
export default const AGE = 30; // This is an error and will not work

```

so we have to use the export default keyword on a separate line like this:

```js
// constants.js 

const AGE = 30; 
export default AGE;

```

We can, however, export default without declaring the variable like this:

```js
//constants.js
export default {
 name: "Billy",
 age: 40
};

```

and in another file use it like this:

```js
import user from './constants';
console.log(user.name); // Billy 
console.log(user.age); // 40

```

There is another way of importing all the variables exported in a file using the following syntax:

```js
import * as constants from './constants';

```

Here, we are importing all the named and default exports we have in `constants.js` and stored in the `constants` variable. So, `constants` will become an object now.

```js
// constants.js
export const USERNAME = "David";
export default {
 name: "Billy",
 age: 40
};

```

And in another file, we use it as below:

```js
// test.js

import * as constants from './constants';

console.log(constants.USERNAME); // David
console.log(constants.default); // { name: "Billy", age: 40 }
console.log(constants.default.age); // 40

```

Here's a Code Sandbox demo: [https://codesandbox.io/s/green-hill-dj43b](https://codesandbox.io/s/green-hill-dj43b)

If you don’t want to export on separate lines for default and named  
exports, you can combine it as shown below:

```js
// constants.js
const PI = 3.14159; const AGE = 30;
const USERNAME = "David";
const USER = {
 name: "Billy",
 age: 40 
};

export { PI, AGE, USERNAME, USER as default };

```

Here, we are exporting `USER` as the default export and others as named exports.

In another file, you can use it like this:

```js
import USER, { PI, AGE, USERNAME } from "./constants";

```

Here's a Code Sandbox demo: [https://codesandbox.io/s/eloquent-northcutt-7btp1](https://codesandbox.io/s/eloquent-northcutt-7btp1)

### In summary:

1. In ES6, data declared in one file is not accessible to another file until it is exported from that file and imported into another file.
2. If we have a single thing in a file to export like class declaration, we use default export otherwise we use named export. We can also combine default and named exports in a single file.

## Default Parameters in JavaScript

ES6 has added a pretty useful feature of providing default parameters while defining functions.

Suppose we have an application, where once the user login into the system, we show them a welcome message like this:

```js
function showMessage(firstName) {
  return "Welcome back, " + firstName;
}
console.log(showMessage('John')); // Welcome back, John

```

But what if we don’t have the user name in our database as it was an optional field while registering? Then we can show the `Welcome Guest` message to the user after login.

So we first need to check if the `firstName` is provided and then display the corresponding message. Before ES6, we would have had to write code like this:

```js
function showMessage(firstName) {
  if(firstName) {
    return "Welcome back, " + firstName;
  } else {
    return "Welcome back, Guest";
  }
}

console.log(showMessage('John')); // Welcome back, John 
console.log(showMessage()); // Welcome back, Guest

```

But now in ES6 using default function parameters we can write the above code as shown below:

```js
function showMessage(firstName = 'Guest') {
   return "Welcome back, " + firstName;
}

console.log(showMessage('John')); // Welcome back, John 
console.log(showMessage()); // Welcome back, Guest

```

**We can assign any value as a default value to the function parameter.**

```js
function display(a = 10, b = 20, c = b) { 
 console.log(a, b, c);
}

display(); // 10 20 20
display(40); // 40 20 20
display(1, 70); // 1 70 70
display(1, 30, 70); // 1 30 70

```

As you can see, we have assigned unique values to a and b function parameters but for c we're assigning the value of b. So whatever value we have provided for b will be assigned to c also if there is no specific value provided for c while calling the function.

In the above code, we have not provided all the arguments to the function. So the above function calls will be the same as below:

```js
display(); // is same as display(undefined, undefined, undefined)
display(40); // is same as display(40, undefined, undefined)
display(1, 70); // is same as display(1, 70, undefined)

```

So if the argument passed is `undefined`, the default value will be used for the corresponding parameter.

**We can also assign complex or calculated values as a default value.**

```js
const defaultUser = {
  name: 'Jane',
  location: 'NY',
  job: 'Software Developer'
};

const display = (user = defaultUser, age = 60 / 2 ) => { 
 console.log(user, age);
};
display();

/* output

{
  name: 'Jane',
  location: 'NY',
  job: 'Software Developer'
} 30 

*/

```

Now, take a look at the below ES5 code:

```js
// ES5 Code
function getUsers(page, results, gender, nationality) {
  var params = "";
  if(page === 0 || page) {
   params += `page=${page}&`; 
  }
  if(results) {
   params += `results=${results}&`;
  }
  if(gender) {
   params += `gender=${gender}&`;
  }
  if(nationality) {
   params += `nationality=${nationality}`;
  }

  fetch('https://randomuser.me/api/?' + params) 
   .then(function(response) {
     return response.json(); 
   })
   .then(function(result) { 
    console.log(result);
   }) 
   .catch(function(error) {
     console.log('error', error); 
   }); 
}

getUsers(0, 10, 'male', 'us');

```

In this code, we’re making an API call to the [Random user](https://randomuser.me/) API by passing various optional parameters in the `getUsers` function.

So before making the API call, we have added various if conditions to check if the parameter is added or not, and based on that we’re constructing the query string like this: `https://randomuser.me/api/? page=0&results=10&gender=male&nationality=us`.

But instead of adding so many if conditions, we can use the default parameters while defining the function parameters as shown below:

```js
function getUsers(page = 0, results = 10, gender = 'male',nationality = 'us') {
 fetch(`https://randomuser.me/api/?page=${page}&results=${results}&gender=${gender}&nationality=${nationality}`)
 .then(function(response) { 
  return response.json();
 }) 
 .then(function(result) {
   console.log(result); 
 })
 .catch(function(error) { 
  console.log('error', error);
  }); 
}

getUsers();

```

As you can see, we have simplified the code a lot. So when we don’t provide any argument to the `getUsers` function, it will take default values and we can also provide our own values like this:

```js
getUsers(1, 20, 'female', 'gb');

```

So it will override the default parameters of the function.

### null is not equal to undefined

But you need to be aware of one thing: `null` and `undefined` are two different things while defining default parameters.

Take a look at the below code:

```js
function display(name = 'David', age = 35, location = 'NY'){
 console.log(name, age, location); 
}

display('David', 35); // David 35 NY
display('David', 35, undefined); // David 35 NY

```

As we have not provided the third value for the location parameter in the first call to display, it will be `undefined` by default so the default value of location will be used in both of the function calls. But the below function calls are not equal.

```js
display('David', 35, undefined); // David 35 NY
display('David', 35, null); // David 35 null

```

When we pass `null` as an argument, we’re specifically saying to assign a `null` value to the `location` parameter which is not the same as `undefined`. So it will not take the default value of `NY`.

## Array.prototype.includes

ES7 has added a new function that checks if an element is present in the array or not and returns a boolean value of either `true` or `false`.

```js
// ES5 Code

const numbers = ["one", "two", "three", "four"];

console.log(numbers.indexOf("one") > -1); // true 
console.log(numbers.indexOf("five") > -1); // false
```

The same code using the Array `includes` method can be written as shown below:

```js
// ES7 Code

const numbers = ["one", "two", "three", "four"];

console.log(numbers.includes("one")); // true 
console.log(numbers.includes("five")); // false
```

So using the Array `includes` methods makes code short and easy to understand.

The `includes` method also comes in handy when comparing with different values.

Take a look at the below code:

```js
const day = "monday";

if(day === "monday" || day === "tuesday" || day === "wednesday") {
  // do something
}
```

The above code using the `includes` method can be simplified as shown below:

```js
const day = "monday";

if(["monday", "tuesday", "wednesday"].includes(day)) {
  // do something
}
```

So the `includes` method is pretty handy when checking for values in an array.

## Closing points

There are many changes that have been incorporated into JavaScript starting from ES6. And every JavaScript, Angular, React, or Vue developer should be aware of them.

Knowing them makes you a better developer and can even help you get a higher paying job. And if you're just learning libraries like React and frameworks like Angular and Vue, you'll certainly want to be familiar with these new features.

## Learn more about Modern JavaScript features

You can learn everything about the latest features added in JavaScript in my [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/) book. It is the only guide you need to learn modern JavaScript concepts.

[<img src="https://modernjavascript.yogeshchavan.dev/book_cover.jpg">](https://modernjavascript.yogeshchavan.dev/)

Subscribe to my [weekly newsletter](https://bit.ly/2HwVEA2) to join 1000+ other subscribers to get amazing tips, tricks, and articles directly in your inbox.

