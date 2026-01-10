---
title: JavaScript Modules – How to Create, Import, and Export a Module in JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-28T20:42:29.000Z'
originalURL: https://freecodecamp.org/news/javascript-modules
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Add-a-subheading--1-.png
tags:
- name: JavaScript
  slug: javascript
- name: modules
  slug: modules
seo_title: null
seo_desc: "By Dapo Adedire\nJavaScript, like most programming languages, was initially\
  \ used for small tasks. But as its popularity grew, so did the amount of code that\
  \ needed to be written. \nHaving a large amount of code in a single file can be\
  \ problematic, so i..."
---

By Dapo Adedire

JavaScript, like most programming languages, was initially used for small tasks. But as its popularity grew, so did the amount of code that needed to be written. 

Having a large amount of code in a single file can be problematic, so it's helpful to split the code into multiple parts. This is where modules come in handy.

## What is a Module?

JavaScript modules are a way to organize and structure code. They allow developers to break their code into smaller, reusable pieces. You can think about them as smaller pieces of code that you can import and export between different parts of an application.

Throughout this article, we'll go through how use modules in your program and the best ways to do it.

But first, let's talk about some more reasons to use modules.

## The Benefits of Using Modules

Your code will still run if you put it all in the same file. But you might be causing some problems for yourself. Let's talk about some benefits of using modules in your program.

### More Organized Code

Using modules in your application makes everything well-sorted and arranged. It also makes your work easier to understand for anyone that wants to go through your code. 

You probably wouldn't be excited to find a variable called "username" on line 431 or to need to start renaming a variable or function name everywhere it is used in an application.

### Code Reusability

By breaking down your code into smaller, modular components, you can easily reuse those components in other parts of your application or in entirely new applications. 

This can save you a lot of time and effort, as you don't have to rewrite the same code over and over again. 

Also, if you make changes to a module, those changes will be reflected everywhere that module is used, making it easier to maintain and update your codebase.

### No Naming Conflicts

Using JavaScript modules helps you avoid naming conflicts. When working on a large project, it's common for developers to write multiple functions and variables with the same name. This can lead to naming conflicts where two or more pieces of code have the same name, causing unexpected behavior and errors. With modules, you don't have this problem.

## How to Use Modules in JavaScript

### How to Define a Module

Here is the basic way to define a module. Imagine 2 files names, `main.js` and `generate.js`.

Here's main.js:

```javascript
let name = "Muhammad Ali"

```

And here's generate.js:

```javascript
function generateUserCertificate(userName, date): 
    # generate user certificate. 
const myName = name
generateUserCertificate(myName, "2023-09-04")

```

To use the "name" variable inside the generate.js file, you need to export it from the main.js file and import it into the generate.js file.

There are a lot of techniques you can use to import and export files.

We'll go through them one by one.

## Types of File Exports in JavaScript

### Default Exports

Here's how to perform a default export in a JavaScript file:

```javascript
function getAllUser():

export default getAllUser

```

Note that you can only use one default export in a JavaScript file. You can also export before the declaration, like this:

```javascript
export default function getAllUser():

```

This is easier to read, right?

### Named Exports

Named exports allow you to share multiple modules from a file, unlike default exports which can only have one in a file. 

You won't need to use the "default" syntax when using named exports. Named exports also need to be enclosed in curly brackets if you are exporting more than one module.

Here's an example:

```javascript
const name = "Muhammad Ali"

export name;

```

You can also export before the declaration. Here's how to do that:

```javascript
export function sayHi(user) {
  alert(`Hello, ${user}!`);
}

export function sayHello(user) {
  alert(`Hello, ${user}!`);
}

```

You can also export multiple variables, functions, or classes using named exports in a single statement. Here's an example:

```javascript
const name = "Muhammad Alli"

function sayHello(user) {
  alert(`Hello, ${user}!`);
}

export {name, sayHello};

```

Note: It is possible to have both default and named export in a module.

```javascript
const age = 404;

const name = "Muhammad Alli"

export default function sayHello(user) {
  alert(`Hello, ${user}!`);
}

export {age, name};

```

### How to Rename Exports

It's also possible to rename your modules before exporting them. Here's how you'd do that:

```javascript
export function sayHello(user) {
  alert(`Hello, ${user}!`);
}

export { sayHello as greet };

```

## How to Import Modules

### How to Import a Single Default Export

Here is how to import a default export:

```javascript
import getAllUser from "getuser.js";

```

That's all – you can then proceed to use the `getAllUser` function anywhere in that file.

### How to Import a Single Named Export

Here is how to import a single named export.

```javascript
import {name} from "username.js"

```

### How to Import Multiple Named Exports

Here is how to export multiple named exports.

```javascript
 import {name, sayHello} from 'user.js'

```

### How to Rename Imports

You can also rename exports before using them in a JavaScript file. Here's how to do it:

```javascript
import {userName as name, greet as sayHello} from 'user.js'

```

It basically imports the name and 1sayHello1 module and renames them, so you can only make reference to "userName" and "greet" in this current module.

### How to Import an Entire Module

What if there are a lot of modules to import and it's a waste of time to create a single line of named exports for them? Then you can export them this way:

```javascript
import * as User from 'user.js'

```

Here is how you can use it in the module exported to:

```javascript
import * as User from 'user.js'

User.name
User.sayHi

```

## Conclusion

Modules are a powerful feature in JavaScript that allow developers to organize and structure their code for improved readability and reusability. They also help you avoid naming conflicts. 

By breaking down large codebases into smaller, manageable modules, developers can write more efficient and maintainable code. 

This article has covered the basics of defining, exporting, and importing modules in JavaScript, including default exports, named exports, renaming exports, and importing entire modules. 

By mastering the use of modules, you can take your JavaScript programming skills to the next level and write more efficient and scalable code.

You can share your thoughts with me on [Twitter](https://twitter.com/dapo_adedire) here.

Happy coding! ^-^

