---
title: How Callbacks Work in Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-28T22:53:02.000Z'
originalURL: https://freecodecamp.org/news/nodejs-callbacks
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-chepte--cormani-1416530.jpg
tags:
- name: callbacks
  slug: callbacks
- name: node
  slug: node
- name: node js
  slug: node-js
seo_title: null
seo_desc: "By Aditya Gupta\nNode.js callbacks are a special type of function passed\
  \ as an argument to another function. \nThey're called when the function that contains\
  \ the callback as an argument completes its execution, and allows the code in the\
  \ callback to ru..."
---

By Aditya Gupta

Node.js callbacks are a special type of function passed as an argument to another function. 

They're called when the function that contains the callback as an argument completes its execution, and allows the code in the callback to run in the meantime.

Callbacks help us make asynchronous calls. Even Node.js APIs are written in a way that supports callbacks.

**Here's the syntax of a callback in Node:**

```javascript
function function_name(argument, callback)
```

## **How to Use Callbacks in Node**

The callback is used to define what happens when the function containing the callback as an argument completes its execution.

For example, we can define a callback to print the error and result after the function execution.

```javascript
function function_name(argument, function (error, result){ if(error){ console.log(error) } else { console.log(result) } })
```

## **How to Write Callbacks**

You can write a callback function in two ways: as an arrow function, and as a standard function without a name. Both ways will give you the same result.

### How to write a callback as a standard function without a name

You can write a callback as a regular function. You do that using a function keyword then the argument inside round brackets. Then you use curly brackets where you can define the callback body. It is not required to define the function name since it is automatically called.

**Syntax:**

```javascript
function function_name(argument, function (callback_argument){
    // callback body 
})
```

Let’s see an example of a callback using the setTimeout function. You can use this method to define a callback function that runs after a definite time.

```javascript
setTimeout(function () { 
    console.log('Callback as Standard Function'); 
}, 1000);
```

Here we define a callback that runs after 1000 milliseconds which is equivalent to 1 second.

**Output:**

![Callback Standard](https://codeforgeek.com/wp-content/uploads/2022/11/callback-standard.png)

### How to write a callback as an arrow function

It may be confusing to have multiple function keywords in a block of code. To eliminate the function keyword in the callback, you can use an arrow function. The arrow function was introduced in ES6 and helps you write cleaner code by removing the function keyword.

**Syntax:**

```javascript
function function_name(argument, (callback_argument) => { 
    // callback body 
})
```

Let’s rewrite the same example we wrote in the above section using an arrow function. Here we change the string to "Callback as Arrow Function".

```javascript
setTimeout(() => { 
    console.log('Callback as Arrow Function'); 
}, 1000);
```

**Output:**

![Callback As Arrow Function](https://codeforgeek.com/wp-content/uploads/2022/11/callback-as-arrow-function.png)

## Asynchronous Programming Using Callbacks

Asynchronous programming is an approach to running multiple processes at a time without blocking the other part(s) of the code.

By using callbacks, we can write asynchronous code in a better way. For example, we can define a callback that prints the result after the parent function completes its execution. Then there is no need to block other blocks of the code in order to print the result.

Let’s take the example of a file system module which used to interact with files in Node.js. For reading a file, we can use the `readFileSync` method.

```javascript
const fs = require('fs');

const data = fs.readFileSync('hello.txt', 'utf-8'); console.log(data);
```

**Output:**

![Output Read Sync](https://codeforgeek.com/wp-content/uploads/2022/11/output-read-sync.png)

But this way our code holds up the execution of the rest of the program until it finishes its execution and prints the result. 

Luckily, we can use a callback to write the code asynchronously without blocking the rest of the execution using the readFile method. When the reading of the file is done, then the callback gets triggered and prints the result.

```javascript
const fs = require('fs'); 

const data = fs.readFile('hello.txt', 'utf-8', function(err, result){ 
    if(err){ 
        console.log(err) 
    } else { 
        console.log(result) 
    } 
});
```

**Output:**

![Output Read Async](https://codeforgeek.com/wp-content/uploads/2022/11/output-read-sync-1.png)

## **Summary**

NodeJS callbacks are a special type of function you can use to write asynchronous code. They give you a way to execute a block of code in the meantime after the execution of a function. You can define whether it prints a result, error, or performs the extra operation of the function result. 

There are two ways to write a function: without a function name, or in the form of an arrow function. The arrow function is more convenient and results in cleaner code by removing the use of annoying function keywords. 

I hope this article helps you understand Node.js callbacks.

You can [have a look at the docs here](https://nodejs.org/en/knowledge/getting-started/control-flow/what-are-callbacks/) if you want to learn more.

