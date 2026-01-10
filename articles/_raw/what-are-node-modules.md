---
title: What Are Node Modules and How Do You Use Them?
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2022-12-06T17:54:33.000Z'
originalURL: https://freecodecamp.org/news/what-are-node-modules
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/stock.jpg
tags:
- name: Express
  slug: express
- name: JavaScript
  slug: javascript
- name: modules
  slug: modules
- name: node
  slug: node
- name: npm
  slug: npm
seo_title: null
seo_desc: 'Every Node.js application has modules. These modules form part of the building
  blocks of the application. They help developers work faster and write more structured
  code.

  In this tutorial, you will learn what node modules are. You will also learn abo...'
---

Every Node.js application has modules. These modules form part of the building blocks of the application. They help developers work faster and write more structured code.

In this tutorial, you will learn what node modules are. You will also learn about the three types of node modules. And we'll go over the right way to use them in your applications.

## What is a Module in JavaScript?

In simple terms, a module is a piece of reusable JavaScript code. It could be a `.js` file or a directory containing `.js` files. You can export the content of these files and use them in other files.

Modules help developers adhere to the DRY (Don't Repeat Yourself) principle in programming. They also help to break down complex logic into small, simple, and manageable chunks.

## Types of Node Modules

There are three main types of Node modules that you will work with as a Node.js developer. They include the following.

* Built-in modules
    
* Local modules
    
* Third-party modules
    

### Built-in Modules

Node.js comes with some modules out of the box. These modules are available for use when you install Node.js. Some common examples of built-in Node modules are the following:

* http
    
* url
    
* path
    
* fs
    
* os
    

You can use the built-in modules with the syntax below.

```javascript
const someVariable = require('nameOfModule')
```

You load the module with the `require` function. You need to pass the name of the module you're loading as an argument to the `require` function.

**Note:** The name of the module must be in quotation marks. Also, using `const` to declare the variable ensures that you do not overwrite the value when calling it.

You also need to save the returned value from the `require` function in `someVariable`. You can name that variable anything you want. But often, you will see programmers give the same to the variable as the name of the module (see example below).

```javascript
const http = require('http') 

server = http.createServer((req, res) => { 
    res.writeHead(200, {'Content-Type': 'text/plain'}) 
    res.end('Hello World!')
})

server.listen(3000)
```

You use the `require` function to load the built-in `http` module. Then, you save the returned value in a variable named `http`.

The returned value from the `http` module is an object. Since you've loaded it using the `require` function, you can now use it in your code. For example, call the `.createServer` property to create a server.

### Local Modules

When you work with Node.js, you create local modules that you load and use in your program. Let's see how to do that.

Create a simple `sayHello` module. It takes a `userName` as a parameter and prints "hello" and the user's name.

```javascript
function sayHello(userName) {
	console.log(`Hello ${userName}!`)
}

module.exports = sayHello
```

First, you need to create the function. Then you export it using the syntax `module.exports`. It doesn't have to be a function, though. Your module can export an object, array, or any data type.

#### How to load your local modules

You can load your local modules and use them in other files. To do so, you use the `require` function as you did for the built-in modules.

But with your custom functions, you need to provide the path of the file as an argument. In this case, the path is `'./sayHello`' (which is referencing the `sayHello.js` file).

```javascript
const sayHello = require('./sayHello')
sayHello("Maria") // Hello Maria!
```

Once you've loaded your module, you can make a reference to it in your code.

### Third-Party Modules

A cool thing about using modules in Node.js is that you can share them with others. The Node Package Manager (NPM) makes that possible. When you install Node.js, NPM comes along with it.

With NPM, you can share your modules as packages via [the NPM registry.](https://www.npmjs.com/) And you can also use packages others have shared.

#### How to use third-party packages

To use a third-party package in your application, you first need to install it. You can run the command below to install a package.

```javascript
npm install <name-of-package>
```

For example, there's a package called `capitalize`. It performs functions like capitalizing the first letter of a word.

Running the command below will install the capitalize package:

```javascript
npm install capitalize
```

To use the installed package, you need to load it with the `require` function.

```javascript
const capitalize = require('capitalize)
```

And then you can use it in your code, like this for example:

```javascript
const capitalize = require('capitalize')
console.log(capitalize("hello")) // Hello
```

This is a simple example. But there are packages that perform more complex tasks and can save you loads of time.

For example, you can use the Express.js package which is a Node.js framework. It makes building apps faster and simple. To learn more about NPM, read this [freeCodeCamp article on the Node Package Manager](https://www.freecodecamp.org/news/what-is-npm-a-node-package-manager-tutorial-for-beginners/).

## Conclusion

In this article, you learned about what Node modules are and the three types of node modules. You also learned about how to use the different types in your application.

Thanks for reading. And happy coding!
