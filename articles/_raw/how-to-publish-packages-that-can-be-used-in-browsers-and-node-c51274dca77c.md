---
title: How to publish packages that can be used in browsers and Node
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-05-02T15:49:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-publish-packages-that-can-be-used-in-browsers-and-node-c51274dca77c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bpaO04etYhqF8-OFxen63w.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'When you create a package for others to use, you have to consider where
  your user will use your package. Will they use it in a browser-based environment
  (or frontend JavaScript)? Will they use it in Node (or backend JavaScript)? Or both?

  If you want ...'
---

When you create a package for others to use, you have to consider where your user will use your package. Will they use it in a browser-based environment (or frontend JavaScript)? Will they use it in Node (or backend JavaScript)? Or both?

If you want to create a package that’s usable in both browsers and Node, this article is here to help.

You’ll learn:

1. How to write packages for use in browsers

2. How to write packages for use in Node

3. How to publish your packages for use in both browsers and Node

### **Writing a package for use in browsers**

If you want to include a library in frontend JavaScript, you have to link the library first with a `script` tag. You can use the library anytime after you link it.

```
<!-- This is html -->
```

```
<script src="link-to-jquery.js"></script>
```

```
<script>  // You can use jQuery anytime after you link to it  console.log(jQuery)</script>
```

This works because JavaScript in browsers shares one global scope. It doesn’t matter how many JavaScript files you link to. They behave as if they’re one big JavaScript file.

With this information, we can begin writing a library for use in the frontend world.

Let’s say you want to create a library called `peachBlossom`. `peachBlossom` has a `bloom` function. You write this `bloom` function in a separate JavaScript file, `peach-blossom.js`.

```
// This is js
```

```
// peach-blossom.jsfunction bloom () {  console.log('Bloom!')}
```

You can include `peachBlossom` in your frontend JavaScript by linking to the `peach-blossom.js` file. Once you do this, you can use `bloom` anywhere.

```
<!-- This is html -->
```

```
<script src="peach-blossom.js"></script><script src="main.js"></script>
```

```
// This is js
```

```
// main.jsbloom() // Bloom!
```

Libraries usually have more than one piece of code. We don’t want to pollute the global scope with little variables. What we can do is wrap the functions we want to expose in an immediately-invoked function expression (IIFE).

This means:

1. We create a function and run it immediately  
2. We return the library from within the function so we can use the library later.

In code, it looks somewhat like this:

```
// This is js
```

```
// peach-blossom.js const peachBlossom = (function () {  // Write as much code as you want here
```

```
// Return what others can use  return {    bloom: function () {      console.log('Bloom!')    }  }})()
```

You can then use `bloom` anywhere by writing `peachBlossom.bloom`.

```
// This is js
```

```
// main.jspeachBlossom.bloom() // Bloom!
```

This is the basics of writing a frontend library.

Now, let’s talk about writing a library for Node.

### **Writing a package for Node**

Adding a library to Node is different from adding a library to browsers. This is because Node doesn’t have HTML files and `<scri`pt> tags.

Let’s make sure you know how to run Node before we begin writing a library for Node.

#### Running Node

First, you need to make sure you have Node installed on your computer. You can install Node from [Node’s website](https://nodejs.org/en/) if you don’t have it installed already.

Once you have Node installed, you’ll want to create a folder to store your Node project. In this case, let’s call it “node-project”.

The command to create a folder is this:

```
# This is bash
```

```
mkdir node-project
```

Then, you need to navigate to the `node-project` directory. You can do it with `cd`:

```
# This is bashcd node-project
```

If you’re having problems with the command line, you can use [this guide](https://zellwk.com/blog/fear-of-command-line/) to help you out.

Next, we want to create a file. This will be a JavaScript file. (We will run Node on this file). Let’s call it `index.js`.

```
# This is bash
```

```
touch index.js
```

![Image](https://cdn-media-1.freecodecamp.org/images/f0BgtmtrZh4oc2U58UuNiCxOVxx-ibcLd4nE)

In `index.js`, we’re going to write a `console.log` statement. This is for us to know if we run the file.

```
// This is js
```

```
// index.jsconsole.log('Running index.js!')
```

Finally, you can use `node` to run `index.js`. Here’s the command:

```
# This is bash
```

```
node index.js
```

Once you run `index.js`, you should see the `console.log` in the terminal. That’s how we know the file has run.

![Image](https://cdn-media-1.freecodecamp.org/images/b-KuiWqcDHmAGXKBJ6uVsJPwU6bdeRYTCow9)

#### Adding libraries to Node

To add libraries to Node, you have to use the `require` statement. Once you add a library, you can use the library anywhere in the same JavaScript file.

Here’s an example:

```
// This is js
```

```
const fs = require('fs')console.log(fs)
```

![Image](https://cdn-media-1.freecodecamp.org/images/tuH9M9aEGONU-7bU7OlXhK4knqSm0h7WLmN3)

When you use `require`, Node looks for the library you specified in three places:

First, it checks whether the library is built into Node. In this example, `fs` is built directly into Node. You can use `fs` anytime if you use Node.

Second, it checks whether the library exists in the `node_modules` folder. These are user-installed libraries. You can add a library to the `node_modules` folder by running `npm install`.

Here’s an example where we install `express`, then require express in Node:

```
# This is bash
```

```
# Run this in the command linenpm install express
```

```
// This is js 
```

```
// Index.js const express = require('express')console.log(express)
```

![Image](https://cdn-media-1.freecodecamp.org/images/bcyHIXmeoXF45Sr4heQfBSnhFRiTMscQ1iIr)

Third, if you add `./` to `require`, Node will look for a file located in the current directory. This is where we can begin writing the `peach-blossom` library.

#### Writing your first library for Node

Let’s start by creating a `peach-blossom.js` file. This file should be in the same directory as `index.js`.

```
// This is js
```

```
touch peach-blossom.js
```

![Image](https://cdn-media-1.freecodecamp.org/images/vHap18-jDq8MyfYna0XkLMbHFqeVF7EPQmXP)

We can add `peach-blossom.js` to `index.js` by using `require`. Here’s what it looks like:

```
// This is js 
```

```
const peachBlossom = require('./peach-blossom')
```

In Node, there’s no concept of a shared global scope. Each file has its own scope. So, if you write `peach-blossom.js` as if it’s used for frontend JavaScript, you won’t be able to use it. You’ll get an error.

```
// This is js
```

```
// peach-blossom.js const peachBlossom = (function () { // Write as much code as you want here
```

```
// Return what others can use return { bloom: function () { console.log(‘Bloom!’) } }})()
```

```
// This is js
```

```
// index.js const peachBlossom = require(‘./peach-blossom’)
```

![Image](https://cdn-media-1.freecodecamp.org/images/DeVVpx8tTDzGn56qpevFYrfJnDX1RzQTIBcy)

To pass variables from one file to another in Node, you have to write `module.exports`. Variables passed to `module.exports` can be retrieved from another file.

This means we must write `module.exports` in `peach-blossom.js`.

```
// This is js 
```

```
// Write as much code as you want here const peachBlossom = { bloom () { console.log(‘Bloom!’) }}
```

```
// Exports peachBlossom for use in other filesmodule.exports = peachBlossom
```

Once we have exported `peachBlossom`, we can use it in other files:

```
// This is js
```

```
// index.js const peachBlossom = require('./peach-blossom')peachBlossom.bloom() // Bloom!```
```

This format of passing variables around in Node with `require` and `module.exports` is called **CommonJS**.

#### Publishing your library as an npm package

In short, to make your module work in Node, you have to export a variable with `module.exports`. Other people can then `require` this module in their code.

At this point, you can move `peach-blossom` into a separate project folder and publish it as an npm package. You can use [this guide](https://zellwk.com/blog/publish-to-npm/) to find out more about publishing the process.

### Writing modules that are usable in both frontend and backend JavaScript

Let’s take a moment to reconcile what we know.

To write a library for the frontend, we need to declare it as a variable. As much as possible, we want to expose one variable only.

```
// This is js
```

```
const peachBlossom = (function () {  // Write as much code as you want here
```

```
// Return what others can use  return {    bloom: function () {      console.log('Bloom!')    }  }})()
```

To write a library for the Node, we need to export the variable with `module.exports`. Here, we only expose one variable.

```
// This is js// Write as much code as you want here const peachBlossom = {  bloom () {    console.log('Bloom!')  }}
```

```
// Exports peachBlossom for use in other filesmodule.exports = peachBlossom
```

But these are two completely different formats! How can we write a library once and use it in both contexts?

Enter UMD.

#### UMD

[UMD (Universal Module Definition](https://github.com/umdjs/umd)) is a block of code we can use to wrap around our library. This block of code makes it possible to use a library both on the frontend and in Node.

It kinda looks like this:

```
// This is js
```

```
(function (root, factory) {    if (typeof define === 'function' && define.amd) {        // AMD. Register as an anonymous module.        define(['b'], factory);    } else if (typeof module === 'object' && module.exports) {        // Node.        module.exports = factory(require('b'));    } else {        // Browser globals (root is window)        root.returnExports = factory(root.b);    }}(typeof self !== 'undefined' ? self : this, function (b) {    // Use b in some fashion.
```

```
// Just return a value to define the module export.    // This example returns an object, but the module    // can return a function as the exported value.    return {};}));
```

Whoa! This is confusing! Hold up!

In practice, we don’t have to know how to UMD-ify our code by ourselves. Many tools, like Webpack and Parcel, gives us the ability to UMD-ify our code through them.

Here are some examples (and their relevant setup instructions):

1. [Gulp-umd](https://github.com/eduardolundgren/gulp-umd)  
2. [Webpack](https://webpack.js.org/guides/author-libraries/)  
3. [Parcel](https://parceljs.org/cli.html#expose-modules-as-umd)  
4. [Rollup](https://rollupjs.org/guide/en)

This, means you have to set up these tools if you want to write packages that can be used for both Frontend JavaScript and in Node. Yes, it complicates the authoring process, but there’s nothing much we can do about it at this point.

### Wrapping up

If you want your library to work both on Frontend JavaScript and in Node, you need to wrap your module with UMD (Universal Module Definition).

If you want to UMD-ify your code, you need to use a build tool when you author your package. This makes the authoring process more complicated. But the tradeoff can be worth it for providing users with an option to use your library anywhere.

This article was originally posted on [_my blog_](https://zellwk.com/blog/publishing-npm-packages-that-can-be-used-in-browsers-and-node).  
Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better frontend developer.

