---
title: Node Module Exports Explained – With JavaScript Export Function Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-17T20:16:29.000Z'
originalURL: https://freecodecamp.org/news/node-module-exports-explained-with-javascript-export-function-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/cover-1.jpg
tags:
- name: JavaScript
  slug: javascript
- name: modules
  slug: modules
- name: Node.js
  slug: nodejs
seo_title: null
seo_desc: 'By Stanley Nguyen

  One of the most powerful things about software development is the ability to reuse
  and build upon the foundations of other people. This code sharing has helped software
  progress at an amazing rate.

  Such a wonderful mechanism is crit...'
---

By Stanley Nguyen

One of the most powerful things about software development is the ability to reuse and build upon the foundations of other people. This code sharing has helped software progress at an amazing rate.

Such a wonderful mechanism is critical on a micro-level for both individual projects and teams. 

For Node.js, this process of code sharing – both within individual projects and in external npm dependencies – is facilitated using `module.exports` or `exports`.

# How Node Modules Work

How do we use module exports to plug an external module, or sensibly break our project down into multiple files (modules)?

The Node.js module system was created because its designers didn't want it to suffer from the same problem of broken global scope, like its browser counterpart. They implemented [CommonJS specification](https://en.wikipedia.org/wiki/CommonJS) to achieve this.

The two important pieces of the puzzle are `module.exports` and the `require` function.

## How module.exports works

`module.exports` is actually a property of the `module` object. This is how the `module` object looks like when we `console.log(module)`:

```bash
Module {
  id: '.',
  path: '/Users/stanleynguyen/Documents/Projects/blog.stanleynguyen.me',
  exports: {},
  parent: null,
  filename: '/Users/stanleynguyen/Documents/Projects/blog.stanleynguyen.me/index.js',
  loaded: false,
  children: [],
  paths: [
    '/Users/stanleynguyen/Documents/Projects/blog.stanleynguyen.me/node_modules',
    '/Users/stanleynguyen/Documents/Projects/node_modules',
    '/Users/stanleynguyen/Documents/node_modules',
    '/Users/stanleynguyen/node_modules',
    '/Users/node_modules',
    '/node_modules'
  ]
}

```

The above object basically describes an encapsulated module from a JS file with `module.exports` being the exported component of any types - object, function, string, and so on. Default exporting in a Node.js module is as simple as this:

```js
module.exports = function anExportedFunc() {
  return "yup simple as that";
};

```

There's another way of exporting from a Node.js module called "named export". Instead of assigning the whole `module.exports` to a value, we would assign individual properties of the default `module.exports` object to values. Something like this:

```js
module.exports.anExportedFunc = () => {};
module.exports.anExportedString = "this string is exported";

// or bundled together in an object
module.exports = {
  anExportedFunc,
  anExportedString,
};

```

Named export can also be done more concisely with the module-scoped `exports` predefined variable, like this:

```js
exports.anExportedFunc = () => {};
exports.anExportedString = "this string is exported";

```

However, assigning the whole `exports` variable to a new value won't work (we will discuss why in a later section), and often confuses Node.js developers.

```js
// This wont work as we would expect
exports = {
  anExportedFunc,
  anExportedString,
};

```

Imagine that Node.js module exports are shipping containers, with `module.exports` and `exports` as port personnel whom we would tell which "ship" (that is, values) that we want to get to a "foreign port" (another module in the project). 

Well, "default export" would be telling `module.exports` which "ship" to set sail while "named export" would be loading different containers onto the ship that `module.exports` is going to set sail.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/ship-analogy.png)
_My "flagship" analogy for Node.js module.exports' role_

Now that we have sent the ships sailing, how do our "foreign ports" reel in the exported ship?

## How the Node.js require keyword works

On the receiving end, Node.js modules can import by `require`-ing the exported value.

Let's say this was written in `ship.js`:

```js
...
module.exports = {
  containerA,
  containerB,
};

```

We can easily import the "ship" in our `receiving-port.js`:

```js
// importing the whole ship as a single variable
const ship = require("./ship.js");
console.log(ship.containerA);
console.log(ship.containerB);
// or directly importing containers through object destructuring
const { containerA, containerB } = require("./ship.js");
console.log(containerA);
console.log(containerB);

```

An important point to note about this foreign port operator – `require` – is that the person is adamant about receiving ships that were **sent by `module.exports` from the other side of the sea**. This leads us to the next section where we will address a common point of confusion.

## `module.exports` vs `exports` – What is the difference and which do you use when?

Now that we have gone through the basics of module exporting and requiring, it's time to address one of the common sources of confusion in Node.js modules.

This is a common module exports mistake that people who are starting out with Node.js often make. They assign `exports` to a new value, thinking that it's the same as "default exporting" through `module.exports`. 

However, this will not work because:

* `require` will only use the value from `module.exports`
* `exports` is a module-scoped variable that refers to `module.exports` initially

So by assigning `exports` to a new value, we're effectively pointing the value of `exports` to another reference away from the initial reference to the same object as `module.exports`. 

If you want to learn more about this technical explanation, [the Node.js official documentation](https://nodejs.org/api/modules.html#modules_exports_shortcut) is a good place to start.

Back to the analogy that we made previously using ships and operators: `exports` is another port personnel that we could inform about the outgoing ship. At the start, both `module.exports` and `exports` have the same piece of information about the outgoing "ship". 

But what if we tell `exports` that the outgoing ship will be a different one (that is, assigning `exports` to a completely new value)? Then, whatever we tell them afterwards (like assigning properties of `exports` to values) won't be on the ship that `module.exports` is actually setting sail to be received by `require`.

On the other hand, if we only tell `exports` to "load some containers on the outgoing ship" (assigning properties of `exports` to value), we would actually end up loading "containers" (that is, property value) onto the ship that is actually being set sail.

Based on the common mistake explained above, we could definitely develop some good conventions around using CommonJS modules in Node.js.

## Node.js export best practices – a sensible strategy

Of course the convention offered below is entirely from my own assessments and reasonings. If you have a stronger case for an alternative, please don't hesitate to tweet me [@stanley_ngn](https://twitter.com/stanley_ngn).

The main things I want to achieve with this convention are:

* eliminating confusion around `exports` vs `module.exports`
* ease of reading and higher glanceability with regards to module exporting

So I'm proposing that we consolidate exported values at the bottom of the file like this:

```js
// default export
module.exports = function defaultExportedFunction() {};
// named export
module.exports = {
  something,
  anotherThing,
};

```

Doing so would eliminate any disadvantages in terms of conciseness that `module.exports` have versus shorthand `exports`. This would remove all incentives for us to use the confusing and potentially harmful `exports`. 

This practice would also make it very easy for code readers to glance at and learn about exported values from a specific module.

## Going beyond CommonJS

There's a new, and better (of course!) standard that's recently been introduced to Node.js called `ECMAScript modules`. [ECMAScript modules](https://nodejs.org/api/esm.html) used to only be available in code that would eventually need transpilation from [Babel](https://babeljs.io/), or as part of an experimental feature in Node.js version 12 or older. 

It's a pretty simple and elegant way of handling module exporting. The gist of it can be summed up with the default export being:

```js
export default function exportedFunction() {}

```

and the named export looking like this:

```js
// named exports on separate LOC
export const constantString = "CONSTANT_STRING";
export const constantNumber = 5;
// consolidated named exports
export default {
  constantString,
  constantNumber,
};

```

These values can then easily be imported on the receiving end, like this:

```js
// default exported value
import exportedFunction from "exporting-module.js";
// import named exported values through object destructuring
import { constantString, constantNumber } from "exporting-module.js";

```

This results in no more confusion from `module.exports` vs `exports` and a nice, human-sounding syntax! 

There are definitely projects that are yet to be migrated to Node.js version 14 and above and so can't use this new syntax. 

However, if you do have a chance (because you are starting a new project, or your project has successfully been migrated to Node.js 14 and above), there's no reason not to switch to this awesome futuristic way of doing things.

### Thank you for reading!

Last but not least, if you like my writings, please head over to [my blog](https://blog.stanleynguyen.me/) for similar commentaries and follow [me on Twitter](https://twitter.com/stanley_ngn). 🎉

