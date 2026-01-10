---
title: What is NodeJS? The JavaScript Engine and Runtime Explained for Beginners
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2023-07-17T14:46:01.000Z'
originalURL: https://freecodecamp.org/news/what-is-node-js-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/pexels-sevenstorm-juhaszimrus-443383--2-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: null
seo_desc: Every year another something JS enters the development sphere. With names
  such as VueJS, NextJS, and AngularJS, you may be under the impression that NodeJS
  is a JavaScript framework. Or you've heard that NodeJS is a language. But neither
  of those sta...
---

Every year another *something JS* enters the development sphere. With names such as VueJS, NextJS, and AngularJS, you may be under the impression that NodeJS is a JavaScript framework. Or you've heard that NodeJS is a language. But neither of those statements is accurate.

To define NodeJS, we will take a step back and look at how JavaScript works and discuss three components that play a significant role in JavaScript:

1. The language itself
    
2. The JavaScript engine
    
3. The JavaScript runtime
    

## The JavaScript Language Itself

JavaScript is a programming language based on ECMAScript. You may also hear it referred to as a dialect or implementation of the ECMAScript language standard.

A language standard contains a set of rules for how a language should behave. Dialects, on the other hand, are implementations of a language standard. Much like there are regional dialects of the English language, JavaScript is a dialect—the most popular dialect—of ECMAScript.

Before 2008, developers only used JavaScript to manipulate web pages. But the inability to use JavaScript outside the browser was not a limitation of JavaScript, the language, but a constraint of where this JavaScript code was being executed.

## What is the JavaScript Engine?

Before we touch on where JavaScript is executed, we will briefly touch on how.

There are compiled languages and interpreted languages. A compiled language is like a prepared meal. All the ingredients have been mixed, organized, and arranged into something that only needs to be cooked. They've been checked beforehand to ensure they meet the standard for that meal.

An interpreted language, on the other hand, is like a hibachi chef performing their artistry on the grill as you watch. They prepare your meal in real-time, make adjustments on the fly, and incorporate their unique skills and techniques to create the final dish.

In the realm of JavaScript interpretation, a JavaScript engine takes on the role of the hibachi chef, executing the code and bringing it to life on the digital grill.

As much as it may seem like an improvisational act, the JavaScript engine still implements specific rules, ensuring consistency when executing your code. (Recall many of these rules come from the ECMAScript language standard).

But it may surprise you that much of what is written by a web developer will be found nowhere in the ECMAScript standard.

You see, the DOM, for example, is part of an "outside world." And ECMAScript has no specifications about how JavaScript should interact with this outside world. These rules come from somewhere else—the JavaScript runtime.

## What is a JavaScript Runtime?

A runtime is a place or environment where your code executes. It is *not* the thing running the code itself (this is the engine) but rather an environment that provides access to certain parts of the outside world.

Imagine your code is a person inside of a house. Different rooms will have different windows which allow this person to see different parts of what is outside. The outside doesn't change, but the room that the person is in will determine what they can see. This is the essence of what a JavaScript runtime is. It is like a room that you can place your code within. And just like the person inside of the house, the room your code is in will determine which parts of the outside world it has access to.

The most common JavaScript runtime is the browser. And for the browser, the parts of the outside world it allows you to see (interact with) with are the Window object and, subsequently, the document object, or DOM.

These objects are critical for web developers because they provide the necessary APIs that allow your JavaScript to interact with web pages. Adding a

, updating some inner HTML text, or listening to window-based events are all thanks to the Web API provided by the browser runtime.

## So What is NodeJS?

By now, you may have an idea of what NodeJS is. Node is a JavaScript runtime. It's not a language or a framework. It's simply an environment that allows you to write JavaScript that interacts with different parts of the outside world other than the browser.

Instead of providing things like the Web API, it provides APIs to interact with components such as the file system, HTTP, and the operating system.

## How Node Works

Let's look at an example of what Node can do. You may need to install Node first. The easiest way to install it is to visit NodeJS.org and download the LTS (Long-Term Support) version.

*Node JS org home screen displaying download options*

We can check to ensure that it is installed correctly by opening a command line or terminal prompt and typing `node -v`.

```js
node -v
> v18.16.0
```

Let's run our first command in Node. In a terminal window, start the Node REPL by typing in `node` and pressing enter.

Once the REPL has started, we can run our first JavaScript commands within the Node runtime. Let's type `console.log(1 + 1)`:

```js
console.log(1+1)
> 2
```

Running commands in the REPL is great for demo purposes, but Node wouldn't be beneficial if that were the only place you could interact with the Node runtime. Fortunately, we can also create JavaScript files and run them with Node.

Let's create a JavaScript file named *main.js.* Add a console.log statement and display a message of your choice. Here is what I've created:4

```js
onst msg = 'Hello, World! Here is a message from main.js'

console.log(msg
```

From your terminal (within the same directory where you saved the file), type `node main.js` and press enter. You should see something similar to the following:

```js
node main.js
> Hello, World! Here is a message from main.js!
```

Let's do one more thing with Node and build something more complex.

In this last example, we will leverage some built-in Node modules to create an HTML file and then serve that file all with JavaScript (within the Node runtime, of course!).

First, we will import three modules: FS, OS, and HTTP. These are core modules provided by Node JS.

```js
const fs = require('fs');
const http = require('http);
const os = require('os');
```

Next, we will create the content that we will add to the index.html file we will create. We will get the operating system type of our machine and eventually populate our HTML file with that information.

```js
// Get the OS type of our machine
osType = os.type();

// Create a string of HTML content for a file we will create
htmlContent = '<html><h3>Hello, World! Your OS type is ${osType}</h3></html>
```

Now that we have the content prepared for our HTML file, it's time to create the file. Most of what we do with Node JS will be writing asynchronous code. So for our example, we will use callback functions to run any code we want to ensure runs *after* our asynchronous code.

The next code to write will create the HTML file. We use the `fs` module and the `writeFile` method to do this. This function accepts a callback. We will use this callback to ensure the file has been created before we read the file and eventually create the server.

```js
// Create an index.html file with the htmlContent variable as the content.
// Since this is async, we will provide a callback as a third argument
// that will run after the file has been created. It is in this callback that
// we will read the file. For code clarity, we won't handle errors.

fs.writeFile('./index.html', htmlContent, (err) => {
    const server = http.createServer((req, res) => {
        fs.readFile('.index.html', (err, content) => {
            res.setHeader('Content-Type', 'text/html');
            res.end(content);
        });
    });
}
```

We've created the file and prepared the server up to this point. But to serve the file, we need to start the server. We use the `listen` method on `createServer` to start the server. This function accepts several arguments. We will pass in a port number of 3000. So putting it all together:

```js
const fs = require('fs');
const http = require('http);
const os = require('os');

// Get the OS type of our machine
osType = os.type();

// Create a string of HTML content for a file we will create
htmlContent = '<html><h3>Hello, World! Your OS type is ${osType}</h3></html>

// Create an index.html file with the htmlContent variable as the content.
// Since this is async, we will provide a callback as a third argument
// that will run after the file has been created. It is in this callback that
// we will read the file. For code clarity, we won't handle errors.

fs.writeFile('./index.html', htmlContent, (err) => {
    const server = http.createServer((req, res) => {
        fs.readFile('.index.html', (err, content) => {
            res.setHeader('Content-Type', 'text/html');
            res.end(content);
        });
    });
    server.listen(3000);
}
```

Now remember, this is just a JavaScript file. The file has the code to do everything we want to do, but we need to execute the script. Let's run the script and see what happens:

```js
node main.js
>
```

It may appear that the script is stuck or broken. Remember, however, that we've started a server. Until we cancel the script, the script is running, and it may appear that is the script has timed out.

Let's cancel the server (press *ctrl + c* twice), and then add a console.log to our `listen` method to help provide some feedback when the server is running. `listen` can accept a callback as the second argument. We will pass in a callback function to log some output.

```js
server.listen(3000, () => {
    console.log('Listening on port 3000!');
});
```

Now, when we run the script we should see:

To run this file, change to the directory where the file is and run the following command:

```bash
node main.js
> Listening on port 3000!
```

The server is running. But where is our webpage?

Open a browser, enter *localhost:3000* for the URL, and hit enter. You should see something similar to this:

*The content of the index.html file we have created and served with Node!*

You've done it! You've created a straightforward web application and served it with NodeJS.

## Wrapping Up

JavaScript, the language, is written syntax executed by a JavaScript engine, which adheres to the rules set by the ECMAScript standard.

In addition to the language standard, the engine incorporates additional features for interacting with the outside world. The JavaScript runtime provides these features. The most common runtimes are the browser and Node, but there are others like Deno (similar to Node but offering additional features like native TypeScript support).
