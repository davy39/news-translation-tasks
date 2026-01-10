---
title: module.exports – How to Export in Node.js and JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-25T21:03:11.000Z'
originalURL: https://freecodecamp.org/news/module-exports-how-to-export-in-node-js-and-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-conrad-marshall-615670.jpg
tags:
- name: JavaScript
  slug: javascript
- name: modules
  slug: modules
- name: node js
  slug: node-js
seo_title: null
seo_desc: "By Dillion Megida\nIn programming, modules are components of a program\
  \ with one or more functions or values. \nThese values can also be shared across\
  \ the entire program and can be used in different ways.\nIn this article, I will\
  \ show you how to share fu..."
---

By Dillion Megida

In programming, modules are components of a program with one or more functions or values. 

These values can also be shared across the entire program and can be used in different ways.

In this article, I will show you how to share functions and values by exporting and importing modules in Node.js.

## Why Export Modules?

You'll want to export modules so that you can use them in other parts of your application. 

Modules can serve different purposes. They can provide simple utilities to modify strings. They can provide methods for making API requests. Or they can even provide constants and primitive values.

When you export a module, you can import it into other parts of your applications and consume it.

Node.js supports [CommonJS Modules](https://nodejs.org/api/modules.html) and [ECMAScript Modules](https://nodejs.org/api/esm.html).

For the rest of this article, we'll focus on CommonJS Modules, the original approach to packaging modules in Node.js.

If you want to learn more about ES Modules (along with CommonJS modules), you can [check out this in-depth guide](https://www.freecodecamp.org/news/modules-in-javascript/).

## How to Export Modules in Node

Node.js already exports in-built modules which include [fs](https://nodejs.dev/learn/the-nodejs-fs-module), [path](https://nodejs.dev/learn/the-nodejs-path-module), and [http](https://nodejs.dev/learn/the-nodejs-http-module) to name a few. But you can create your own modules.

Node.js treats each file in a Node project as a module that can export values and functions from the file.

Say, for example, that you have a utility file `utility.js` with the following code:

```js
// utility.js

const replaceStr = (str, char, replacer) => {
  const regex = new RegExp(char, "g")
  const replaced = str.replace(regex, replacer)
  return replaced
}
```

`utility.js` is a module which other files can import things from. But `utility.js` currently does not export anything. 

You can verify this by examining the global `module` object in each file. When you print the `module` global object in this utility file, you have:

```js
console.log(module)

// {
//   id: ".",
//   path: "...",
//   exports: {},
//   parent: null,
//   filename: "...",
//   loaded: false,
//   children: [],
//   paths: [
//     ...
//   ],
// }
```

The `module` object has an `exports` property which, as you can see, is an empty object. 

So any attempt to import anything from this file will throw an error.

The `utility.js` file has a `replaceStr` method which replaces characters in a string with some other characters. We can export this function from this module to be used by other files.

Here's how:

```js
// utility.js

const replaceStr = (str, char, replacer) => {
  const regex = new RegExp(char, "g")
  const replaced = str.replace(regex, replacer)
  return replaced
}

module.exports = { replaceStr }
// or
exports.replaceStr = replaceStr
```

Now, `replaceStr` is available for use in other parts of the application. To use it, you import it like this:

```js
const { replaceStr } = require('./utility.js')

// then use the function anywhere
```

## module.exports vs exports in Node

You can export functions and values from a module by either using `module.exports`:

```js
module.exports = { value1, function1 }
```

or by using `exports`:

```js
exports.value1 = value1
exports.function1 = function1
```

What's the difference?

These methods are pretty identical. Basically, `exports` serves as a reference to `module.exports`. To understand this better, let's populate the `exports` object by using the two ways of exporting values:

```js
const value1 = 50
exports.value1 = value1

console.log(module)
// {
//   id: ".",
//   path: "...",
//   exports: { value1: 50 },
//   parent: null,
//   filename: "...",
//   loaded: false,
//   children: [],
//   paths: [
//     ...
//   ],
// }

const function1 = function() {
  console.log("I am a function")
}
module.exports = { function1, ...module.exports }

console.log(module)

// {
//   id: ".",
//   path: "...",
//   exports: { function1: [Function: function1] },
//   parent: null,
//   filename: "...",
//   loaded: false,
//   children: [],
//   paths: [
//     ...
//   ],
// }
```

There are two things to notice here:

- The `exports` keyword is a reference to the `exports` object in the `modules` object. By doing `exports.value1 = value1`, it added the `value1` property to the `module.exports` object, as you can see in the first log.
- The second log does not contain the `value1` export anymore. It only has the function exported using `module.exports`. Why is this so?

`module.exports = ...` is a way of reassigning a new object to the `exports` property. The new object only contains the function, so the `value1` is no longer exported.

So what's the difference?

Exporting values with just the `exports` keyword is a quick way to export values from a module. You can use this keyword at the top or bottom, and all it does is populate the `module.exports` object. But if you're using `exports` in a file, stick to using it throughout that file.

Using `module.exports` is a way of explicitly specifying a module's exports. And this should ideally only exist once in a file. If it exists twice, the second declaration reassigns the `module.exports` property, and the module only exports what the second declaration states.

So as a solution to the previous code, you either export like this:

```js
// ...
exports.value1 = value1

// ...
exports.function1 = function1
```

or like this:

```js
// ...
module.exports = { value1, function1 }
```

## Wrap up

Each file in a Node.js project is treated as a module that can export values to be used by other modules. 

`module.exports` is an object in a Node.js file that holds the exported values and functions from that module.

Declaring a `module.exports` object in a file specifies the values to be exported from that file. When exported, another module can import this values with the `require` global method.


