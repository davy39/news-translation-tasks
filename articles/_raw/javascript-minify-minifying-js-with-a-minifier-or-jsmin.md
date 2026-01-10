---
title: JavaScript Minify – Minifying JS with a Minifier or jsmin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-02T23:50:39.000Z'
originalURL: https://freecodecamp.org/news/javascript-minify-minifying-js-with-a-minifier-or-jsmin
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/3.-minifying-js.png
tags:
- name: JavaScript
  slug: javascript
- name: performance
  slug: performance
- name: web performance
  slug: web-performance
seo_title: null
seo_desc: 'By Dillion Megida

  You might be wondering – what is minification and how does it improve your JavaScript
  applications? What tools can you use to minify your JS? I''ll answer these questions
  in this article.

  What is Minification?

  Minification is the pro...'
---

By Dillion Megida

You might be wondering – what is minification and how does it improve your JavaScript applications? What tools can you use to minify your JS? I'll answer these questions in this article.

## What is Minification?

Minification is the process of "minimizing" code by removing the irrelevant parts of the code. What does this look like?

Take a look  at the following JavaScript code:

```js
const variable = "Variable";

function print() {
  console.log(variable);
};

print(); // "Variable"
```

Here we have the `variable` declaration, the `print` declaration, and the `print()` execution. We also have a comment.

In JavaScript, we know that a semi-colon is used to end a statement. This helps the interpreter differentiate between statements.

In our code above, you can see the semi-colons at the end of some lines to show where the statement ends.

A "minified" version of the JavaScript code above would look like this:

```js
const variable="Variable";function print(){console.log(variable);};print();
```

Both versions will produce the same results. The difference is that the first version is easily readable, while the second version isn't. So the first version is good for **development** while the second version is fit for **production** (you'll understand this as you continue reading).

The size of the first version on my computer is **100 bytes**, while the second is **75 bytes**. Of course, this is quite insignificant here – but in large codebases such as the image below, the difference would be obvious:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-242.png)
_Screenshot gotten from [StackOverflow](https://stackoverflow.com/questions/51766230/difference-between-the-output-of-minified-js-and-css-files)_

## The JavaScript Interpreter Doesn't Need Whitespaces and Comments

The interpreter for executing JavaScript code does not need **whitespaces** (spaces, line breaks, and so on). It also doesn't need comments for its execution. 

Spacing and commenting out our code are things we do as developers to improve our development experience. These things make code easier to read, and help us remember why we made certain decisions. But they're for us as developers, not your browser. Your browser **DOESN'T NEED** these things.

What happens then is that if you have a lot of comments/whitespaces in your code, it could make the file size unnecessarily large.

With minification, the unnecessary whitespaces and the comments get removed. The minified code produces the same execution result as the original, only that the minified one is compressed, and will have a smaller file size.

## Why Does File Size Matter?

When you go to a URL on your browser, the browser fetches the resources stored on the server for that URL. It fetches the `.html` file, which in turn fetches the linked stylesheet and script files. 

With everything fetched correctly, you see a page on your browser with elements styled and interactions (done with JavaScript) working.

Two things that can make the process of receiving the requested resources slow are:

* weak internet connection
* large sizes of the resources

You cannot control the internet connection that users of your web applications may have, but you can control the sizes of your files.

### Smaller file size improves load times

The larger the file size, the longer the download (fetching) takes to complete. And the smaller the file size, the faster the download completes.

By minifying your JavaScript files, you can **improve resource load times**  as the browser will require less time to completely download such files.

### Smaller file size improves initial parse time

When the browser fetches a JavaScript file, the JavaScript engine first tries to parse the file. Parsing involves going through the code line by line, explicitly ignoring whitespaces and comments, and checking if the code is syntactically correct. 

If it is not, you get errors. If it is, then the code is translated to machine code that can be understood by the browser.

The larger the file size, the more time it will take to parse the file. The smaller the size, the less time the parser will take.

So, minifying your JavaScript files **improves initial parse time**.

These things can improve the general performance and response time of your web applications.

## Minification Tools for JS

So how do you use whitespaces, comments, and other things you need for a good development experience but still deliver minified files for production? The idea is to have a **development** and **production** version of your code.

The former is for when you're writing code and building the application, and the latter is what you store on the server that is delivered to the browser.

You don't have to do this minification process yourself. That's almost impossible. I'll share two minifying tools you can use.

### Minify

This tool removes whitespace, strips comments, combines files, and optimizes a few common programming patterns. You install the tool on your device and configure it in your code with the JavaScript path that you want you to minify for production.

You can refer to [the repository](https://github.com/matthiasmullie/minify) to learn more about the tool, and see how it is used.

### jsmin

This NPM library works similarly with Minify, for removing comments and whitespaces in JavaScript files. 

As a Node.js module, you can install it globally and using the CLI command, minify your JavaScript project.

Check out the [library on NPM](https://www.npmjs.com/package/jsmin) to learn more about it, the installation, and how to use it.

## Wrapping Up

Minification is a process that improves the performance of your applications by reducing load times and bandwidths for fetching files from servers. You can perform this process for various code files such as HTML, CSS, and JavaScript.

In this article, I've explained what minification is, why it's beneficial, and how it can be applied to JavaScript files. You can also learn about [CSS Minification here](https://www.freecodecamp.org/news/minify-css-css-minifying-and-compression-explained/).


