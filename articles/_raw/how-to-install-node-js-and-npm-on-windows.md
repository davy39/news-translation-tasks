---
title: How to Install Node.js and npm on Windows
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-08T22:13:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-node-js-and-npm-on-windows
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e0c740569d1a4ca3b0a.jpg
tags:
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: Windows
  slug: windows
seo_title: null
seo_desc: 'Installing Node.js and npm on Windows is very straightforward.

  First, download the Windows installer from the Node.js website. You will have the
  choice between the LTS (Long Term Support) or Current version.


  The Current version receives the latest f...'
---

Installing Node.js and npm on Windows is very straightforward.

First, download the Windows installer from the [Node.js website](https://nodejs.org/). You will have the choice between the **LTS** (Long Term Support) or **Current** version.

* The **Current** version receives the latest features and updates more rapidly
* The **LTS** version foregos feature changes to improve stability, but receives patches such as bug fixes and security updates

Once you have selected a version meets your needs, run the installer. Follow the prompts to select an install path and ensure the **npm package manager** feature is included along with the **Node.js runtime**. This should be the default configuration.

Restart your computer after the installation is complete.

If you installed under the default configuration, Node.js should now be added to your PATH. Run command prompt or powershell and input the following to test it out:

```text
> node -v
```

The console should respond with a version string. Repeat the process for npm:

```text
> npm -v
```

If both commands work, your installation was a success, and you can start using Node.js!

## More info on Node.js

According to its [GitHub repository](https://github.com/nodejs/node), Node.js is:

> Node.js is an open-source, cross-platform, JavaScript runtime environment. It executes JavaScript code outside of a browser. For more information on using Node.js, see the [Node.js Website](https://nodejs.org/).

### A breakdown of Node.js facts:

* Node.js is a JavaScript runtime built on Chrome’s V8 JavaScript engine.  
Every browser has a JavaSript engine built in it to process JavaScript files contained in websites. Google Chrome uses the V8 engine, which is built using C++. Node.js also uses this super-fast engine to interpret JavaScript files.
* Node.js uses an event-driven model.  
This means that Node.js waits for certain events to take place. It then acts on those events. Events can be anything from a click to a HTTP request. We can also declare our own custom events and make Node.js listen for those events.
* Node.js uses a non-blocking I/O model.  
We know that I/O tasks take much longer than processing tasks. Node.js uses callback functions to handle such requests.

Let us assume that a particular I/O task takes 5 seconds to execute, and that we want to perform this I/O twice in our code.

**Python**

```python
import time

def my_io_task():
  time.sleep(5)
  print("done")

my_io_task()
my_io_task()
```

**Node.js**

```node
function my_io_task() {
    setTimeout(function() {
      console.log('done');
    }, 5000);
}

my_io_task();
my_io_task();
```

Both look similar, but the time taken to execute are different. The Python code takes 10 seconds to execute while the Node.js code takes only 5 seconds.

Node.js takes less time because of its non-blocking I/O model. The first call to `my_io_task()` starts the timer and leaves it there. It does not wait for the response from the function. Instead, it moves on to call the second `my_io_task()`, starts the timer and leaves it there.

When the timer completes it’s execution taking 5 seconds, it calls the function and prints `done` on the console. Since both the timers are started together, they complete together and therefore take same amount of time.

## **Socket.io**

[Socket.io](https://socket.io/) is a Node.js library made to help make real-time communication between computers possible. To ensure this Socket.io uses WebSockets to establish a connection between the client’s browser and the server. This library uses [Engine.IO](https://github.com/socketio/engine.io) for building the connection.

### **Demos**

To get a taste of what is possible, Socket.io provides two demos to show it’s possible use-cases. You can find the demos at [https://socket.io/demos/chat/](https://socket.io/demos/chat/) and find the link to the whiteboard demo on the left.

### **Get Started**

Since Socket.io is a Node.js library you have to make sure that Node.js is installed. If it’s not set up yet get the latest version at [Nodejs.org](https://nodejs.org/)

#### **macOS**

Node.js can also be installed via [Homebrew](https://brew.sh/) a package manager for macOS.

Just type `brew install node` to install Node.js.

A [get started](https://socket.io/get-started/chat/) guide can also be found on Socket.io’s page. It shows how to easily build a real-time chat in just a couple of lines.

#### **More information**

More information about Socket.io and it’s documentation can be found at:

* [Socket.io](https://socket.io/)
* [Socket.io Documentation](https://socket.io/docs/)

### More information on Node.js

* [Official Node.js site](https://nodejs.org/)
* [Node Version Manager](https://github.com/nvm-sh/nvm)
* [n: Interactive Node.js Version Manager](https://github.com/tj/n)
* [Node.js docs](https://nodejs.org/en/docs/)

