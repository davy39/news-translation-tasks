---
title: GitHub Codespaces – How to Code Right in Your Browser with Your Own Cloud Dev
  Environment
subtitle: ''
author: Michael Yuan
co_authors: []
series: null
date: '2020-06-09T21:34:29.000Z'
originalURL: https://freecodecamp.org/news/learn-programming-in-your-browser-the-right-way
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a61740569d1a4ca2547.jpg
tags:
- name: codespaces
  slug: codespaces
- name: GitHub
  slug: github
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
- name: Rust
  slug: rust
- name: Visual Studio Code
  slug: vscode
- name: WebAssembly
  slug: webassembly
seo_title: null
seo_desc: 'GitHub Codespaces enable you to experiment with complex software development
  stacks right from the web browser. No software to install or configure. No stress.
  No mess.


  A gif showing the setup process of a GitHub Codespace

  In the recent GitHub Satel...'
---

GitHub Codespaces enable you to experiment with complex software development stacks right from the web browser. No software to install or configure. No stress. No mess.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/SSVM-edited-without-music-1-1.gif align="left")

*A gif showing the setup process of a GitHub Codespace*

In the recent GitHub Satellite online conference, one of the most exciting product announcements was GitHub Codespaces. The idea is to have a code button on every repository.

When you click on it, it launches a fully featured VSCode IDE with all the necessarily software dependencies, including operating system level libraries, to build and run the project. This VSCode IDE runs entirely in your browser, and will not install any software or change any configuration to mess up your computer.

Sounds too good to be true? Well, watch the Github Satellite keynote segment about Codespaces yourself!

%[https://www.youtube.com/watch?v=fQbH3meWNQ8] 

A key benefit of Github Codespaces is how quickly you can on-board new developers to a project. A new developer can get set up in minutes, instead of days, and immediately start contributing to the project. It is a great learning tool for new languages, frameworks, and software tools.

Under the hood, it starts a Docker container on a remote server, installs the entire software stack required by the project, and runs tasks like compiling and debugging in the remote Docker.

The web browser acts as a front end UI for the Docker instance. This approach requires no software install on the developer’s machine. But the trade-off is that all software installation from the operation system all the way to the final application happens on the server.

GitHub must start a fresh server for each Codespaces instance. That requires a lot of data center resources. In fact, the [GitHub Codespaces web page](https://github.com/features/codespaces/) has a waiting list as of today (June 2020).

![Image](https://www.freecodecamp.org/news/content/images/2024/04/codespaces-beta.png align="left")

Personally, I cannot wait for GitHub Codespaces to become available. But a time machine does exist. You can experience all the features in GitHub Codespaces today, for free.

## VS Codespaces

The software behind GitHub Codespaces is actually based on a Microsoft VSCode product called [VS Codespaces](https://online.visualstudio.com/). VS Codespaces is available today to all Microsoft Azure users. And yes, it allows you to open GitHub repositories in VSCode IDE directly from a browser window.

In this tutorial, I will show you how to use Codespaces in your own development work today.

To make Codespaces available in your GitHub repositories, you just need to add the following HTML button anywhere on your web pages.

When an Azure user clicks on the button, it asks the user to log into VS Codespaces and walks the user through opening the repository in the online IDE. You can see how it works in the examples in the next section.

```html
<p>
  <a href="https://online.visualstudio.com/environments/new?name=My%20Project&repo=username/reponame">
    <img src="https://img.shields.io/endpoint?style=social&url=https%3A%2F%2Faka.ms%2Fvso-badge">
  </a>
</p>
```

> VS Codespaces runs entirely in your browser and costs around $1 per work day. It is cheaper than a cup of coffee in the office.

## Examples

Now, let's look into several examples of how you might learn new programming skills using VS Codespaces.

Rust is one of the fastest growing programming languages today. It is voted as the most beloved programming language by Stackoverflow users four years in a row.

But to experiment with Rust requires a complex toolchain of compiler, linker, package manager, tool manager and so on.

VS Codespaces provides an easy way to [learn Rust](https://www.secondstate.io/articles/how-to-learn-rust-without-installing-any-software/). Just click on the VS Codespaces button in [this repository](https://github.com/second-state/learn-rust-with-github-actions) and you now have a working Rust project to experiment with!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/learn-rust-20-seconds.gif align="left")

[*https://github.com/second-state/learn-rust-with-github-actions*](https://github.com/second-state/learn-rust-with-github-actions)

As a system language, Rust is well positioned to build high performance server side applications. The most promising stack is to compile and run Rust functions in a WebAssembly container, and then access those high performance functions from an existing web application framework, such as Node.js.

However, as you can already see, this “best practice” setup requires a complex stack of software.

Clicking on the VS Codespaces button in [this repository](https://github.com/second-state/ssvm-nodejs-starter) gives you a fully functional Node.js project that uses [Rust functions in WebAssembly](https://www.secondstate.io/articles/getting-started-with-rust-function/) as modules. You can immediately start to modify the Rust and JavaScript code and run the Node.js application from inside the web browser IDE.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/SSVM-edited-without-music.gif align="left")

[*https://github.com/second-state/ssvm-nodejs-starter*](https://github.com/second-state/ssvm-nodejs-starter)

[Server-side Rust and WebAssembly](https://www.secondstate.io/articles/why-webassembly-server/) sound cool. But do we actually have a more complete example that demonstrate the power and performance of Rust beyond a simple hello world?

[This repository](https://github.com/second-state/rust-wasm-ai-demo) is such an example. Open it in VS Codespaces and you will have a project for a [Rust + JavaScript app that utilizes Tensorflow to perform image recognition](https://www.secondstate.io/articles/artificial-intelligence/). Since the app runs inside Node.js, it provides a template for AI-as-a-Service web applications.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/68747470733a2f2f626c6f672e7365636f6e6473746174652e696f2f696d616765732f414961617325323033307365636f6e64732e676966.gif align="left")

[*https://github.com/second-state/rust-wasm-ai-demo*](https://github.com/second-state/rust-wasm-ai-demo)

What if you want to stay on the bleeding edge and use Rust-based web runtime Deno instead of the C-based Node.js? Well, there is a VS Codespaces [template for running Deno as an Azure Function](https://github.com/anthonychu/azure-functions-deno-worker) too!

## How it works

If you look closely, each VS Codespaces-enabled repository has a `.devcontainer` folder. Inside that folder, the `Dockerfile` specifies how to build the Docker container for the development environment.

For example, the Node.js Docker container is based on Ubuntu Linux with Node.js and selected NPM packages pre-installed. [Check out an example here](https://github.com/second-state/ssvm-nodejs-starter/tree/master/.devcontainer).

The `devcontainer.json` file specifies the configuration for the VSCode IDE on the remote Docker. For example, it configures the VSCode extensions to install, the terminal and debugger commands to use, and the host ports to forward to for testing and debugging.

Microsoft provides [quite a few `.devcontainer` templates](https://github.com/microsoft/vscode-dev-containers) for you to modify and use. They cover most of the common software development stacks today.

You could further customize the user’s VSCode experience by providing launch and tasks definitions in the `.vscode` folder. [Check them out](https://github.com/second-state/ssvm-nodejs-starter/tree/master/.vscode)!

## Conclusion

With VS Codespaces, and GitHub Codespaces when it launches, the barriers and friction for software development are further reduced. You can get started with complex software stacks without leaving your web browser. [Try it today](https://www.secondstate.io/articles/getting-started-rust-nodejs-vscode/)!

Finally, watch the full length GitHub Satellite presentation on GitHub Codespaces.

%[https://www.youtube.com/watch?v=dy2eYaNxaQc] 

[Subscribe to my newsletter](https://webassemblytoday.substack.com/) and stay in touch.

<iframe src="https://webassemblytoday.substack.com/embed" width="480" height="320" style="border:1px solid #EEE;background:white"></iframe>
