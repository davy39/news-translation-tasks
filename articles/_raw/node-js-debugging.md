---
title: How to Debug a Node.js Application with VSCode, Docker, and your Terminal
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-12T22:41:28.000Z'
originalURL: https://freecodecamp.org/news/node-js-debugging
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/hacking-coding-code-hack.jpg
tags:
- name: debugging
  slug: debugging
- name: Docker
  slug: docker
- name: node js
  slug: node-js
- name: terminal
  slug: terminal
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: 'By Erick Wendel

  In this article, we''ll get into some powerful tools to help you find and fix bugs
  using VSCode, Docker, and your terminal. We''ll also learn (and put into practice)
  the 6 ways to debug a Node.js application.

  Can you guess what the 6 po...'
---

By Erick Wendel

In this article, we'll get into some powerful tools to help you find and fix bugs using VSCode, Docker, and your terminal. We'll also learn (and put into practice) the 6 ways to debug a Node.js application.

Can you guess what the 6 possible ways of debugging a Node.js application are? One of the most common practices in every developer's life involves finding bugs quickly and understanding what's going on in their apps.

Most examples shown here will use Node.js, but you can also use them on your JavaScript front-end apps. You can use other editors or IDEs such as Visual Studio or Web Storm, but in this post I'll use VSCode. Just take what you learn here and apply it in your editor of choice.

By the end of this post you will have learned how to inspect your apps by using the following tools:

* Node.js Read-Eval-Print-Loop (REPL)
* Browser
* Docker
* VSCode & Local environment
* VSCode & Docker
* VSCode & Remote environment

## Requirements

In the next steps, you'll create a Web API using Node.js and debug your app using VSCode and Docker. Before starting to code make sure you have the following tools installed on your machine:

* [Docker](https://docs.docker.com/desktop/)
* [Node.js v14](https://nodejs.org/en/download/current/)
* [VSCode](https://code.visualstudio.com/download)

## Introduction

If you've been working as a developer for a while, you might know that it's not like it is in the movies. In fact, developers should spend 80% of their job thinking and only 20% writing code. 

But in reality, most of that 80% is spent problem solving, fixing bugs, and trying to understand how to avoid further problems. Friday nights might look like the gif below:

![developer coding when everything goes wrong](https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif)

When I realize that something weird has happened at my job I try to ask a few questions, as you'll see in the following next sections.

### Was it a spelling error?

In this case, the issue might be with some function or variable that I'm trying to call. The console will show me where the error is and a brief possible reason for throwing the error as shown in the printout below:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screen-Shot-2020-06-05-at-17.32.06.png)
_Image showing a typo in the code by calling getPhoane instead getPhone._

### Is this behavior something that should be working with the current implementation?

It could be an _if_ statement that has not evaluated my conditions or even a _loop_ that should stop after certain interactions but doesn't stop.

### What is going on here?

In this case, it could be an internal error or something I've never seen before. So I google it to figure out what has happened in my application. 

As an example, the image below shows an internal Node.js stream error which is not showing what I did wrong in my program.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screen-Shot-2020-06-05-at-17.31.21-1.png)
_Node.js stream error with message "error: write after end" as an example for internal errors._

## Debugging scripting-based languages

Usually, developers from scripting based languages such as Ruby, Python, or JavaScript doesn't need to use IDEs such as Visual Studio, WebStorm, and so on. 

Instead, they often opt to use lightweight editors such as Sublime Text, VSCode, VIM, and others. The image below shows a common practice to inspect and "debug" apps. They print out statements to verify application states and values.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/node-console-debug-1.gif)
_The console showing the program printing out values such as 'here1', 'here2', and so on._

## Getting started

The practice we looked at in the previous section is not as productive as it could be. We can confuse text names with values, print out incorrect variables, and waste time on simple bugs or spelling errors. By in the next sections I'll show you other ways to improve your search for bugs and statement validations. 

The main goal here is to show how simple it can be to debug an application. By using the most common tools, you'll be able to inspect code from simple terminal commands to remote machines from all over the world.

### Creating the sample project

Before we dive into debugging concepts, you should create an application to inspect. So first, create a Web API using the native Node.js' HTTP module. The API should get all fields from the request, sum all values from it, and then respond to the requester with the calculated results.

Choose an empty folder on your machine and let's start with the Web API. 

First, create a `Math.js` file which will be responsible for summing all fields from a JavaScript Object:

```javascript
//Math.js
module.exports = {
    sum(...args) {
        return args.reduce(
            (prev, next) => 
                Number(prev) + Number(next), 0
        )
    }
}

```

Second, create a Node.js server file using the code below. Copy the value and create your file then paste it there. I'm going to explain what's happening there later. 

Notice that this API is an event-driven API and it will handle requests by using the Node.js Streams approach.

```javascript
//server.js
const Http = require('http')
const PORT = 3000
const { promisify } = require('util')
const { pipeline } = require('stream')
const pipelineAsync = promisify(pipeline)
const { sum } = require('./Math')

let counter = 0
Http.createServer(async (req, res) => {
    try {
        await pipelineAsync(
            req,
            async function * (source) {
                source.setEncoding('utf8')
                for await (const body of source) {
                    console.log(`[${++counter}] - request!`, body)
                    const item = JSON.parse(body)

                    const result = sum(...Object.values(item))
                    yield `Result: ${result}`
                }
            },
            res
        )
    } catch (error) {
        console.log('Error!!', error)
    }
})
.listen(PORT, () => console.log('server running at', PORT))

```

OK, that might look like unusual code for a simple Web API. Let me explain what's happening.

As an alternative, this API is based on _[Node.js Streams](https://nodejs.org/api/stream.html)_. So you'll read on-demand data from income **requests**, process it, and respond to them using the **response** object. 

On line `(11)` there is a pipeline function that will manage the event flow. If something goes wrong in any stream function, it will throw an exception and we'll handle errors on the _catch_ statement from _try/catch._ 

On line `(6)` we are importing the _sum_ function from the _Math_ module and then processing incoming data on line `(19)`. Notice that on `(19)` there is an _Object.values_ function which will spread all object values and return them as an array. For example, an object `{v1: 10, v2: 20}` will be parsed to `[10, 20]` .

### Running

If you have a Unix based system you can use the `cURL` command, which is a native command to make Web requests. If you're working on the Windows Operating system, you can use [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) or [Git bash](https://git-scm.com/downloads) to execute Unix instructions.

Create a `run.sh` file with the following code. You'll create code to request your API. If you're familiar with [Postman](https://www.postman.com/) you can skip this file and execute from there.

```shell
curl -i \
    -X POST \
    -d '{"valor1": "120", "valor2": "10"}' \
    http://localhost:3000
```

Note that you need to install Node.js version `14` or higher. 

You'll need to open two terminal sessions. On mine, I spliced two terminals in my VSCode instance. On the left run `node server.js` and on the right run `bash run.sh` as follows:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/02-server.gif)
_The terminal running and requesting the server.js by using run.sh file._

## Debugging using Node.js Read-Eval-Print-Loop (REPL)

Node.js can help you create the best application possible. REPL is a mechanism for debugging and inspecting Node.js applications from the terminal. When you add the `inspect` flag after the `node` command, the program will stop right on the first code line as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/03-inspect.gif)
_Using node inspect command to stop the program before starting_

First, you'll write the `debugger` keyword right after the counter's `console.log` on line `(17)` and then execute `node inspect server.js` again.

Note that you can interact with the REPL API by using the commands listed in the [official documentation](https://nodejs.org/api/repl.html#repl_repl). 

In the next image, you'll see a practical example of how REPL works using some of the following commands:

1. `list(100)`: shows the first 100 lines of code
2.  `setBreakpoint(17)`: sets a breakpoint on the 17th line
3.  `clearBreakpoint(17)`: removes a breakpoint on the 17th line
4. `exec body`: evaluates the `body` variable and prints out its result
5.  `cont`: continues the program's execution

The image below shows in practice how it works:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/04-repl.gif)

I highly recommend that you try using the `watch` statement. As in the browser, you can watch statements on demand. In your REPL session write `watch(counter)` and then `cont`. 

To test the watch you need to choose a breakpoint – use `setBreakpoint(line)` for it. As you run `run.sh`, the program will stop on your breakpoint and show the watchers. You may see the following result on your console:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/05-repl-watch-2.gif)

## Debugging using Chromium-based browsers

Debugging in the browser is more common than debugging from terminal sessions. Instead of stopping the code on the first line, the program will continue its execution right before its initialization.

Run `node --inspect server.js`  and then go to the browser. Open the _DevTools_ menu (pressing **F12** opens the DevTools on most browsers). Then the Node.js icon will appear. Click on it. Then, in the _Sources_ section you can select the file you want to debug as shown in the image below:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/05-debug-browser-2.gif)

## Debugging in VSCode

Going back and forth to the browser isn't really that fun as long as you write code in an editor. The best experience is to run and debug code in the same place. 

But it's not magic. You configure and specify which is the main file. Let's configure it following the steps below:

1. You'll need to open the `launch.json` file. You can open it by pressing `Ctrl` + `Shift` + `P` or `Command` + `Shift` + `P` on macOS, then writing _launch_. Choose the _Debug: Open launch.json_ option. Additionally, you can press **F5** and it might open the file as well.
2. In the next step of the wizard, click on the _Node.js_ option.
3. You may have seen a JSON file on the editor with the pre-configuration for debugging. Fill in the **program** field with your filename – this tells VSCode which is the main file. Notice that there is a `${workspaceFolder}` symbol. I wrote it to specify that the file is in the current folder I'm working on:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "node",
            "request": "launch",
            "name": "Launch Program", 
            "skipFiles": [
                "<node_internals>/**"
            ],
            "program": "${workspaceFolder}/server.js"
        }
    ]
}
```

Almost there! Go to the source code on `server.js` and set a breakpoint on the 16th line by clicking on the left side of the code line indicator. Run it by pressing **F5** and trigger the _server.js_ using the _run.sh,_ which will show the following output:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/07-debug-vscode.gif)

## Debugging Docker-based applications

I personally love using Docker. It helps us stay as close as possible to the production environment while isolating dependencies in a receipt file. 

If you want to use Docker you need to configure it in a Docker config file. Copy the code below, and create a new file beside the `server.js` and paste it in.

```dockerfile
FROM node:14-alpine

ADD . .

CMD node --inspect=0.0.0.0 server.js
```

First, you'll need to execute the _Docker_ build command on your folder to build the app running `docker build -t app .` . Second, you'll need to expose the _debug_ port (9229) and the _server_ port (3000) so either the browser or VSCode can watch it and attach a debugger statement.

```shell
docker run \
    -p 3000:3000 \
    -p 9229:9229 \
    app
```

If you run the _run.sh,_ file again, it should request the server which is running on Docker. 

Debugging Docker apps on VSCode is not a tough task. You need to change the configuration to attach a debugger on a remote root. Replace your _launch.json_ file with the code below:

```json
{
    "configurations": [
        {
            "type": "node",
            "request": "attach",
            "name": "Docker: Attach to Node",
            "remoteRoot": "${workspaceFolder}",
            "localRoot": "${workspaceFolder}"
        }
    ]
}
```

As long as your app is running on Docker and exposing the default _debug port_ (9229) the configuration above will link the app to the current directory. Running **F5** and triggering the app will have the same outcome as running locally.

## Debugging remote code using VSCode

Remote debugging is exciting! You should keep in mind a few concepts before starting to code:

1. What's is the IP Address of the target?
2. How is the remote working directory set up?

I'll change my _launch.json_ file and add the remote address. I have another PC at home which is connected to the same network. Its IP address is **192.168.15.12**.

Also, I have the Windows Machine's working directory here: _c://Users/Ana/Desktop/remote-vscode/._ 

The macOS is based on Unix systems so the folder structure is different than on my Windows machine. The directory structure mapping must change to _/Users/Ana/Desktop/remote-vscode/_.

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "node",
            "request": "attach",
            "name": "Attach to Remote",
            "address": "192.168.15.12",
            "port": 9229,
            "localRoot": "${workspaceFolder}",
            "remoteRoot": "/Users/Ana/Desktop/remote-vscode/",
            "trace": true,
            "sourceMaps": true,
            "skipFiles": [
                "<node_internals>/**"
            ]
        }
    ]
}
```

In this particular case, you'll need at least two different machines to test it. I made a short video showing how it works in practice below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/s6ggU9grLNo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Stop using console.log for debugging!

My tip for you today is about being lazy for manual stuff. Learn one new shortcut or tool per day to improve productivity. Learn more about the tools you've been working on every day and it will help you spend more time thinking than coding.

In this post, you saw how VSCode can be a helpful tool for debugging apps. And VSCode was just an example. Use whatever is most comfortable for you. If you follow these tips, the sky is the ?

## Thank you for reading

I really appreciate the time we spent together. I hope this content will be more than just text. I hope it will have made you a better thinker and also a better programmer. Follow me on [Twitter](https://twitter.com/erickwendel_) and check out my [personal blog](https://erickwendel.com) where I share all my valuable content.

See ya! ?

