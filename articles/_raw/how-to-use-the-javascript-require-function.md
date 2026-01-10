---
title: JavaScript Require – How to Use the require() Function in JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-01-31T00:07:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-javascript-require-function
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/cover-template--11-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'In JavaScript, modules refer to a file that holds JavaScript code which
  performs a specific purpose.

  Modules are self-contained, making it easy to add, remove, and update functionalities
  without affecting your entire code because they are decoupled f...'
---

In JavaScript, modules refer to a file that holds JavaScript code which performs a specific purpose.

Modules are self-contained, making it easy to add, remove, and update functionalities without affecting your entire code because they are decoupled from other pieces of code.

When you have these modules in separate JavaScript files, you'll want to use them within the original JavaScript file.

In this article, you will learn what the `require()` function does, how you can use it, and some distinct differences between the require and import functions.

For a long time, the CommonJS module system has been the default module system within the Node.js ecosystem. But a new module system was introduced in [Node.js v8.5.0](https://github.com/nodejs/node/blob/master/doc/changelogs/CHANGELOG_V8.md#8.5.0), which is the ES module system.

CommonJS and EMCAScript modules (ES modules) now work perfectly in Node.js. The major difference between them is their execution.

## How to Execute CommonJS and ES Modules

In the browser, JavaScript module execution depends upon `import` and `export` statements. These statements load and export ES modules, respectively. This is the standard and official way to reuse modules in JavaScript, and it’s what most web browsers natively support.

Node.js, by default, supports the CommonJS module format, which loads modules using the `require()` function, and exports them with `module.exports`.

## What is the JavaScript require() Function?

The `require()` function is a built-in CommonJS module function supported in Node.js that lets you include modules within your project. This is because, by default, Node.js treats JavaScript code as CommonJS modules.

### How to Use the require() Function in JS

The `require()` function is straightforward to use and understand, as all you have to do is assign the function to a variable.

In this function, you will pass the location name as an argument. Here is the general syntax:

```js
const varName = require(locationName);
```

Suppose you have a CommonJS module that exports a function `*getFullName*` as seen below:

```js
// utils.js
const getFullName = (firstname, lastName) => {
    return `My fullname is ${firstname} ${lastName}`;
};
module.exports = getFullName;
```

Then you can use the require() function to use/include this module within your JavaScript file:

```js
// index.js
const getFullName = require('./utils.js');
console.log(getFullName('John', 'Doe')); // My fullname is John Doe
```

The module is located within a local file in the above code, which is why the local address is referenced using the file name.

But in a situation when you want to include an external module from the web, then you make use of the web-based location:

```js
const myVar = require('http://web-module.location');
```

## require() vs import() Functions

The require and import functions/statements are used to include modules within your JavaScript file, but they possess some differences. The two major differences are:

* The require() function can be called from anywhere within the program, whereas import() cannot be called conditionally. It always runs at the beginning of the file.
    
* To include a module with the require() function, that module must be saved with a .js extension instead of .mjs when the import() statement is used.
    

## Wrapping Up

In this article, you have learned what the require() function does, how it works, and when you can use it in Node.js.

It's crucial to understand that the import statement is only allowed in ES modules and cannot be used in embedded scripts without the `type="module"` attribute. Also, to use ES modules in Node.js, you must save such modules with an extension of .mjs:

```js
// utils.mjs
export const getFullName = (firstname, lastName) => {
    return `my fullname is ${firstname} ${lastName}`;
};

// index.js
import { getFullName } from './utils.mjs';
console.log(getFullName('John', 'Doe')); // My fullname is John Doe
```

Have fun coding!

You can access over 180 of my articles by [visiting my website](https://joelolawanle.com/contents). You can also use the search field to see if I've written a specific article.
