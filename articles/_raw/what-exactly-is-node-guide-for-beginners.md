---
title: What Exactly is Node.js? A Guide for Beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-25T23:08:59.000Z'
originalURL: https://freecodecamp.org/news/what-exactly-is-node-guide-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/revised_node.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: null
seo_desc: 'By Amazing Enyichi Agu

  If you''re thinking about doing back-end development using JavaScript, you will
  hear the term ‘Node.js’. Node is often associated with developing powerful web servers.

  But what exactly is Node.js? Is it a JavaScript framework ju...'
---

By Amazing Enyichi Agu

If you're thinking about doing back-end development using JavaScript, you will hear the term ‘Node.js’. Node is often associated with developing powerful web servers.

But what exactly is Node.js? Is it a JavaScript framework just like [Angular](https://angular.io/)? Is it a programming language? Is it a JavaScript Library? Is it an umbrella term for a group of technologies? Or is it just another word for JavaScript?

In this article, we will dive into the world of Node.js, learning what it is, why it was created, and what it is used for. This isn't a project-based tutorial – it aims to introduce beginners to Node and how it works.

Here are the topics we will cover:

1. History of Node.js
2. What is Node.js?
3. How does Node.js work?
4. Modules in Node.js
5. Node.js looking forward

If learning about software tools and how they work is something you enjoy, then you'll enjoy reading this article. On that note, let's begin.

## History of Node.js

[Brendan Eich](https://en.wikipedia.org/wiki/Brendan_Eich), who worked for Netscape, invented JavaScript in 1995. But it was a programming language that could only run on a browser. 

Web pages initially only displayed static information. The invention of JavaScript filled the need for more interactive behavior within web pages. With this invention, developers could build more dynamic web pages.

After Brendan Eich invented JavaScript, companies made attempts to use the language to run web servers as well ([server-side scripting](https://en.wikipedia.org/wiki/Server-side_scripting)). These attempts included [Netscape’s Livewire and Microsoft’s Active Server Pages](https://dev.to/macargnelutti/server-side-javascript-a-decade-before-node-js-with-netscape-livewire-l72#the-dawn-of-serverside-javascript). 

But this never became a way of developing web servers, even though JavaScript continued to gain popularity when used in the browser.

In 2008, [Google](https://en.wikipedia.org/wiki/Google) announced a new Web Browser called [Chrome](https://en.wikipedia.org/wiki/Google_Chrome). This browser when released revolutionized the world of internet browsing. It's an optimized browser that executes JavaScript fast and has improved the user experience on the web.

The reason Google Chrome could execute JavaScript code so fast was that a JavaScript engine called [V8](https://v8.dev) ran inside Chrome. That engine was responsible for accepting JavaScript code, optimizing the code, then executing it on the computer. 

The engine was a proper solution for client-side JavaScript. Google Chrome became the leading Web Browser.

In 2009, a software engineer named Ryan Dahl criticized the popular way back-end servers were run at the time. The most popular software for building Web Servers was the [Apache HTTP Server](https://httpd.apache.org/). Dahl argued that it was limited, in that it could not handle a large number of real-time user connections (10,000 +) effectively.

This was one of the main reasons that [Ryan Dahl developed Node.js](https://www.youtube.com/watch?v=EeYvFl7li9E), a tool he built. Node.js used Google’s V8 engine to understand and execute JavaScript code outside the browser. It was a program whose purpose was to run Web Servers. 

Node.js was a great alternative to the traditional Apache HTTP server and slowly gained acceptance among the developer community.

Today, [a lot of big organizations](https://www.simform.com/blog/companies-using-nodejs/) like Netflix, NASA, LinkedIn, Paypal, and many more use Node.js. These companies leverage Node.js’s capabilities to build robust applications for their users.

Also, in the most recent [StackOverflow Developer Survey](https://survey.stackoverflow.co/2022/) at the time of writing this article, Node.js ranked as the most popular technology in the "Web Frameworks and Technology" category. This goes on to show just how popular Node.js is now.

![Most popular Web Frameworks and Technologies](https://www.freecodecamp.org/news/content/images/2023/05/image-105.png)
_Source: [https://survey.stackoverflow.co/2022/#technology-most-popular-technologies](https://survey.stackoverflow.co/2022/#technology-most-popular-technologies)_

This article will go in-depth to look at what makes Node.js stand out, and how it works. But before that, we need to define exactly what it is.

## What is Node.js?

![The Node.js Official Website](https://www.freecodecamp.org/news/content/images/2023/05/image-106.png)
_Source: [https://nodejs.org](https://nodejs.org)_

From the [Node.js official Website](https://nodejs.org), it states that:

> Node.js is an open-source, cross-platform JavaScript Runtime Environment.

For us to define Node.js, we need to break the definition into parts. The terms we'll define are:

* open-source
* cross-platform
* Runtime Environment

### What does open source mean?

Open source is generally used to describe software where the public can examine and edit its source code. This means anybody can inspect the code that makes the program work the way it does. 

An advantage of this is that the users of the program get to understand it and its capabilities more. Also, if a person spots a bug, they can contribute and fix the bug.

You can find Node's [Source Code](https://github.com/nodejs/node/) on GitHub—the most popular website for displaying Open Source code. Node.js also has a lot of contributors—people who add features and fix bugs— on GitHub. Everyone has access to the source code of Node.js, and can even make their customized version of the program if they want to.

### What does cross-platform mean?

If a program is cross-platform, it means that the program is not limited to a single Operating System or hardware architecture. 

A cross-platform program can run on multiple platforms. Node.js runs on Windows, Linux, Unix, and MacOS among other platforms. Developers can use Node.js on a lot of operating systems.

### What is a runtime environment?

The Runtime Environment of a programming language is any environment where a user can execute code written in that language. That environment provides all the tools and resources necessary for running the code. Node.js is a JavaScript runtime environment.

Apart from Node.js, another example of a JavaScript runtime environment is a Web Browser. A browser usually has all the necessary resources to execute [client-side](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools) JavaScript code. 

In the browser, we can use JavaScript to interact with the markup elements and tweak the style. The browser promptly runs the code, as it is a runtime environment.

From the three terms defined above, you can see that Node.js is not a JavaScript framework like Angular. Node.js is not a programming language, it is not a JavaScript library, nor is it an umbrella name for a group of technologies. It is also not another name for JavaScript.

Node.js is a software program that can execute JavaScript code. Put more properly, Node.js is a JavaScript runtime environment. It is an environment developed to make it possible to use JavaScript code for server-side scripting.

## How Does Node.js Work?

Node.js was written mostly with C/C++. As a program that is supposed to run web servers, Node.js needs to constantly interact with a device's operating system. 

Building Node.js with a low-level language like C made it easy for the software to access the operating system’s resources and use them to execute instructions.

But there are many more intricacies involved in how Node.js works. Node.js runs fast and efficient web servers but how exactly does it do that? This section explains the process Node.js uses to achieve its efficiency.

There are three main components we must understand to see how Node.js works. These components are:

* V8 Engine
* Libuv
* Event Loop

We'll dive into detail and explain each of these components, and how they make up Node.js.

### What is the V8 Engine?

The V8 Engine is the JavaScript engine that interprets and runs JavaScript code in the Chrome browser. Some other browsers use a different engine, for example, [Firefox uses SpiderMonkey](https://spidermonkey.dev/), and [Safari uses JavaScriptCore](https://developer.apple.com/documentation/javascriptcore). Without the JavaScript engine, a computer can not understand JavaScript.

The V8 engine contains a memory heap and call stack. They are the building blocks for the V8 engine. They help manage the execution of JavaScript code.

The memory heap is the data store of the V8 engine. Whenever we create a variable that holds an object or function in JavaScript, the engine saves that value in the memory heap. To keep things simple, it is similar to a backpack that stores supplies for a hiker. 

Whenever the engine is executing code and comes across any of those variables, it looks up the actual value from the memory heap – just like whenever a hiker is feeling cold and wants to start a fire, they can look into their backpack for a lighter.

There is a lot more depth to understanding the memory heap. Memory management in JavaScript is a topic that takes more time to explain because the real process is highly intricate. To learn more about the memory heap, [check out this resource](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_management).

The call stack is another building block in the V8 engine. It is a data structure that manages the order of functions to be executed. Whenever the program invokes a function, the function is placed on the call stack and can only leave the stack when the engine has handled that function.

JavaScript is a single-threaded language, which means that it can only execute one instruction at a time. Since the call stack contains the order of instructions to be executed, it means that the JavaScript engine has just one order, one call stack. Read more about [single threading and the call stack here](https://www.geeksforgeeks.org/why-javascript-is-a-single-thread-language-that-can-be-non-blocking/).

![Illustration of the V8 Engine](https://www.freecodecamp.org/news/content/images/2023/05/v8.png)
_Illustration of the V8 Engine_

### What is Libuv?

Apart from the V8 engine, another very important component of Node.js is [Libuv](https://libuv.org/). Libuv is a C library used for performing **Input/output (I/O)** operations. 

I/O operations have to do with sending requests to the computer and receiving responses. These operations include reading and writing files, making network requests, and so on.

![The Libuv Website](https://www.freecodecamp.org/news/content/images/2023/05/image-107.png)
_Source: [https://libuv.org](https://libuv.org)_

From Libuv’s official website, they state that:

> Libuv is a multi-platform support Library with a focus on asynchronous I/O.

This means that Libuv is cross-platform (can run on any operating system) and has a focus on Asynchronous I/O. 

The computer tends to take time to process I/O instructions, but Libuv—the library Node.js uses to interface with the computer— is focused on Asynchronous I/O. It can handle more than one I/O operation at once.

This is what makes Node.js process I/O instructions efficiently despite being single-threaded. It is all because of Libuv. Libuv knows how to handle requests asynchronously, thereby minimizing delay. But how exactly does the JavaScript engine make use of Libuv?

Whenever we pass a script to Node.js, the engine parses the code and starts processing it. The call stack holds the invoked functions and keeps track of the program. If the V8 engine comes across an I/O operation, it passes that operation over to Libuv. Libuv then executes the I/O operation.

Note that Libuv is a C Library. How do we use JavaScript code to run C instructions? There are **bindings** that connect JavaScript functions to their actual implementation in Libuv. These bindings make it possible to use JavaScript code for I/O instructions. 

Node.js uses Libuv for the actual implementation but exposes [Application Programming Interfaces (APIs)](https://www.freecodecamp.org/news/apis-for-beginners/). So, we can now use a Node.js API (which looks like a JavaScript function) to initiate an I/O operation.

One interesting thing to note is that it is true that JavaScript is a single-threaded language, but Libuv—the low-level library Node.js uses— can make use of a thread pool (multiple threads) when executing instructions in the operating system. 

Now, you don’t have to worry about these threads when using Node.js. Libuv knows how to manage them effectively. You just have to make use of the provided Node.js APIs to write the instructions.

![Illustration of Node.js Runtime](https://www.freecodecamp.org/news/content/images/2023/05/node.js.png)
_Illustration of Node.js Runtime_

Libuv was originally created for Node.js, but different programming languages now have bindings for it. [Julia](https://julialang.org/) and [Luvit (Lua-based Runtime Environment)](https://luvit.io/) have the bindings built in just like Node.js, but other languages have libraries that provide those bindings. An example is [uvloop in Python](https://pypi.org/project/uvloop/), among [others](https://github.com/libuv/libuv/blob/v1.x/LINKS.md).

### What is an Event Loop?

[The Event Loop in Node.js](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick) is a very important part of the process. From the name, we can see it is a loop. The loop starts running as Node.js begins executing a program. In this section, we'll examine what the event loop does.

When we run our JavaScript program that contains some asynchronous code (like I/O instructions or timer-based actions), Node.js handles them using the Node.js APIs. Asynchronous functions usually have instructions to be executed after the function has finished processing. Those instructions are placed in a **Callback Queue**.

The Callback Queue works with the **First In First Out (FIFO)** approach. That means the first instruction (callback) to enter the queue is the first to be invoked.

As the event loop runs, it checks if the call stack is empty. If the call stack is not empty, it allows the ongoing process to continue. But if the call stack is empty, it sends the first instruction on the callback queue to the JavaScript engine. The engine then places that instruction (function) on the call stack and executes it. This is very similar to [how the event loop works in the browser](https://www.freecodecamp.org/news/javascript-asynchronous-operations-in-the-browser/#event-loops).

So, the event loop executes callbacks from asynchronous instructions using the JavaScript V8 engine in Node.js. And it is a loop, which means every time it runs, it checks the call stack to know if it will remove the foremost callback and send it to the JavaScript engine.

![Complete Illustration of the Node.js Runtime](https://www.freecodecamp.org/news/content/images/2023/05/node.js--1-.png)
_Complete Illustration of the Node.js Runtime_

Node.js is said to have an event-driven architecture. This means Node.js is built around listening to events and reacting to them promptly when they happen. These events can be timer events, network events, and so on. 

Node.js responds to those events by using an event loop to load event callbacks to the engine after something triggers an event. It is for this reason that Node.js is excellent for real-time data transfer in applications.

## Modules in Node.js

A lot of the functionality of Node.js is housed in modules that come with the software. These modules are meant to split the building blocks of programs into manageable chunks like Lego blocks. With this in place, we only have to import the modules we need for our programs.

For example, the piece of code below imports a built-in module called `fs`.

```javascript
const fs = require('node:fs')

```

But there are other ways we can use modules in Node.js. Apart from the built-in modules, we can also use modules (or packages) other developers built.

**[Node Package Manager (NPM)](https://www.npmjs.com/)** is a software application that comes together with Node.js. It manages all the third-party modules that are available in Node.js. Whenever you need a third-party package, you install it from NPM using the `npm install` command.

![Homepage of the NPM Website](https://www.freecodecamp.org/news/content/images/2023/05/npm.jpg)
_Source: https://npmjs.com_

To import a module you installed from NPM would look something like this:

```javascript
const newModule = require('newModule')
```

## Node.js Looking Forward

Node.js has a large community of developers now. It has thousands of [contributors on GitHub](https://github.com/nodejs/node/graphs/contributors) and is used by some of the biggest companies today. But what does the future look like for Node.js?

Node.js has evolved well since it came into existence in 2009. It was originally made for back-end development, but it can do so much more now. You can use Node.js to develop desktop applications, front-end web applications, mobile applications, and command-line tools. Developers will continue to use it for more and more of these applications.

Ryan Dahl —the inventor of Node.js— [announced a new JavaScript Runtime](https://en.wikipedia.org/wiki/Deno_(software)#History) in 2018 called [Deno.](https://deno.com) He unveiled this Runtime he co-created in a talk titled “10 Things I Regret about Node.js”. 

Deno is a JavaScript Runtime Environment based on Google Chrome’s V8 engine but written in Rust. Deno is not only a Runtime environment for JavaScript but also [TypeScript](https://www.typescriptlang.org/).

Ryan Dahl created Deno because he decided he had made some wrong decisions concerning the original blueprint of Node.js. He wanted to make better architectural decisions for a JavaScript Runtime environment for Web Servers. The result was Deno.

![Homepage of the Deno Website](https://www.freecodecamp.org/news/content/images/2023/05/image-112.png)
_Source: [https://deno.com](https://deno.com)_

But Deno is yet to see massive adoption in the Developer Community. It is still a relatively new technology and needs more time to gain ground.

Also, the [OpenJS Foundation](https://openjsf.org/) which is the organization actively managing, developing, and maintaining Node.js has been fixing some of the bugs and the ultimate efficiency of Node.js. More projects are built on top of the Node.js architecture, and that will likely continue to be the case for the foreseeable future.

## Conclusion

In this article, you have learned a lot and can now confidently answer the question “What exactly is Node.js?”.

We started by going over the history of Node.js, then properly defined Node.js. After that we elaborated on how Node.js works, explaining components such as the V8 Engine, Libuv, and Event Loop. 

After that, we talked about modules in Node.js and NPM. Finally, we looked at what the future could hold for Node.js, and we concluded it will likely only power even more applications.

If you want to learn how to use Node.js to build applications, freeCodeCamp has an entire [playlist of tutorials](https://www.youtube.com/playlist?list=PLWKjhJtqVAbmGQoa3vFjeRbRADAOC9drk) dedicated to it. There is an abundance of resources to learn the technology on the internet, and more are to come.

Good luck building your next application, and see you next time.

PS: Follow me on [Twitter](https://twitter.com/enyichiA) and [LinkedIn](https://linkedin.com/in/enyichiaagu).

