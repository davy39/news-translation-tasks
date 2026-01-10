---
title: How to Make Your Own VS Code Extension
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-04T04:05:00.000Z'
originalURL: https://freecodecamp.org/news/making-vscode-extension
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/0-lDZSUwewtGWo6M4J.jpeg
tags:
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: Visual Studio Code
  slug: visual-studio-code
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: "By Pramono Winata\nI just made my first VS Code extension. And it felt\
  \ good! This article will cover basic steps to help you create your own VS Code\
  \ extension. Along the way I'll share what I learned from making one for the first\
  \ time. \nI am not an ex..."
---

By Pramono Winata

I just made my first VS Code extension. And it felt good! This article will cover basic steps to help you create your own VS Code extension. Along the way I'll share what I learned from making one for the first time. 

I am not an expert at this yet, but I can truly say that **nothing is as hard as it seems.** ?

## Let's talk about VS Code and its Extension Marketplace

If you opened this article, you have probably at least heard about VS Code (or Visual Studio Code). If not, it's basically a light-weight code editor developed by Microsoft.

Since VS Code is a code editor, it can perform much faster and lighter than a typical IDE such as Eclipse. But with that performance comes one disadvantage: IDEs often provide better tools such as built-in linters, better code templates, code versioning tools, and some features such as auto complete.

But where VS Code actually shines is the power of the community. It allows you to install extensions that come directly from the VS Code marketplace itself. These extensions allow you to customize it however you wish. You can, for example, add a linter or any other features like colorful brackets. You can even put a nyan cat in your VS Code!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-from-2020-05-31-23-42-52.png)
_Who doesn't like a nyan cat?_

## Why should you create a VS Code extension?

![Image](https://www.freecodecamp.org/news/content/images/2020/06/0-EErfJXzBUg_qzUsI.jpeg)

Yes, ‘why’ is the keyword here. It's the first and most important thing to talk about when you want to start doing something. 

Ask yourself why do you want to make it? Most people usually answer because they want to **learn something** or **gain fame,** or maybe even both. But the more reasons there are, the more motivation you will have.

One thing I can say is that you don’t need to think big yet. Just make a tool that is very specific, that maybe only you will use. The first step is always the hardest. And at the end of day at least you've helped yourself with your extension.

As for myself, I built an extension because of one particular reason: I wanted to make a tool that I could use to increase my productivity. And that would maybe even help a small part of the community near me. (Spoiler: it's golang unit test generator)

That’s why the extensions that I've made are very precise and have a very specific use case. I'm not going for a big mark, I am aiming to increase my productivity and learn something new. I think that is enough reason for me.

And of course everything seemed impossible at the start. Making VS Code extensions looks like some genius level piece art of work (but of course it's not). Since I have a lot of free time on my hands at the moment, I figured I might as well try it out.

## The Very first step of Building a VS Code Extension

To get started, you have to have VS Code installed. In case you don’t have it yet, I will just put the download link [here](https://code.visualstudio.com/download).

VS Code extensions support two main languages: JavaScript and TypeScript. So having some knowledge of either of these is pretty mandatory.

Also, make sure you have Node.js installed, since we are going to use a lot of npm packages here.

## How to Generate a VS Code Extension Template

Ah, templates. How very convenient. VS Code already has its own template generator, so let’s jump straight into it.

First, install your template generator with `npm install -g yo generator-code`

Afterwards, let's run it with `yo code`. And it will prompt out this weird head thing (?) and language selection. Just pick your preferred language and proceed. (I picked JavaScript here).

![Image](https://www.freecodecamp.org/news/content/images/2020/06/yo-code.png)
_yo code_

Afterwards, you will need to edit your extension name and description. You can just proceed with anything you prefer.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-from-2020-05-26-23-07-28.png)
_or maybe just enter all the way_

Now, a folder called hellovscode will be created in your home directory. Open it with VS Code by simply typing `code hellovscode` in the folder directory.

Use the `F5` key to run your extension and another window will popup. Now press `ctrl+shift+p` and find the `Hello World` command, run it, and a popup should come out in the bottom right corner. Like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/sample-hello.gif)
_Magic? Nope. Just collection of code._

Voilà! You've just run your first extension. But what is actually happening with all that? Don’t worry, I will explain some bits below, mainly regarding two files: `extension.js` and `package.json`.

## What is the Extension.js File in VS Code?

This is where you will spend most of your time coding. This file will contain all your code blocks and logic flow.

There isn’t much difference between this and normal Node code. But one of the main differences is registering your commands. You will come upon this block `vscode.commands.registerCommand('hellovscode.helloWorld'`.

In a nutshell, it will register your function call to be used.

Another difference is the frequent usage of the VS Code API – but we will come back to that later on.

If you looked through the code, you will see this too: `vscode.window.showInformationMessage('Hello World from hellovscode!');` 

As an experiment, try changing the value of the message and try running it again.

### Package.json

This file is the one that basically will link the commands you created from `extension.js` with the commands that you defined.

You will see the command that you have registered above `hellovscode.helloWorld` being put as a part of the command titled `Hello World`. And that’s how the command actually links to your code.

Apart from this, this file will also enable the command to be put on the right click bar. It will also filter where the command should appear (file type).

## How to Publish Your VS Code Plugin

Just in case you might want to publish your extension, I will show you how to do that here:

Step 1: First and foremost, install vsce with `npm install -g vsce`. We will use this most of the time to publish.

Step 2: If you don’t have a Microsoft account yet, you should [register here](https://signup.live.com/) since we will be needing the access token you'll get.

Step 3: Once you have the account sign in to the [marketplace](https://marketplace.visualstudio.com/VSCode). Create your [organization](https://aex.dev.azure.com/me?mkt=en-US) and click on it (you should see something like the below).

![Image](https://www.freecodecamp.org/news/content/images/2020/06/ss.png)

Step 4: Now click on the upper right corner where the red circle is and select Personal Access Token. Create your personal access token and choose all accessible organizations with full access.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-from-2020-05-29-23-56-42.png)

Step 5: Remember your token since you'll use it when uploading your extension.

Step 6: You will need to create your publisher identity now. So go to your command prompt and type `run vsce create-publisher YOUR_PUBLISHER_NAME` .  
Insert your own name, email, and personal access token when prompted. Your publisher account should successfully be created.

Step 7: It’s publishing time! Prepare your extension environment in the command prompt and type `vsce package`. This will package your extension to marketplace format. Then type `vsce publish`.

And that’s it, your extension will be published.

On a side note, when publishing you should modify your readme (at least the first part where it says `This is Readme for..` ) since vsce will detect it and ask you to modify it.

## Some Additional Tips for Building VS Code Extensions

Now you should have some basic understanding of how VS Code extensions work. Here, I will share some things that I have learned.

### Utilizing VS Code's API

VS Code itself has provided a lot of APIs for you to use to make your extension. You might encounter several common obstacles when building your extension, like getting your cursor position, getting the line position, or maybe getting the highlighted word. Those all can be tackled with using the VS Code API.

You should read through their [documentation](https://code.visualstudio.com/api/references/vscode-api) and experiment with their API. You can even try reading through their API code! With the amount of documentation inside the code itself, you should be able to somewhat figure out which API will be most helpful.

### Googling things (read the docs or code)

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-169.png)

Most of the time in our programming life, when we are stuck there is always Google or [Stack Overflow](https://stackoverflow.com/) that can provide quick help.

But this time it will not always save you.

First of all, googling for help in this case is quite tricky. For example, say you want to highlight a word on cursor – you might search for `vs code extension how to get total line...` or something similar.

But let me tell you, most of the time it will direct you to the real extension itself or give you manual on how to use VS Code.

One way you can make it easier for yourself is by adding the "API" keyword in your search, like `vs code extension api how to ...`.

Also, it is pretty hard to find the relevant answers in Google, because the developer community is not that huge, and VS Code extensions may look intimidating for many newcomers. But truthfully, **it is not exactly that hard**.

That’s why sometimes the best way to learn how to develop a VS Code extension is by reading the documentation or the code.

## A VS Code Extension GitHub Example Repository

I have provided a text manipulation example in my [GitHub repository](https://github.com/pramonow/vscode-extension-ut) which might help for code references (watch out for some messy code though!). The code will generate some template unit tests in the Go language.

## Wrapping up

What I have covered here are just the basics of creating a VS Code extension. One message I want you to take to heart is that **it is not as hard as it looks.** Sometimes you just need to push yourself a bit and try it out.

You might come across some challenges along the way, but if you never even start you are missing out completely.

In the end, thanks for taking the time to read this. I hope you enjoyed it and started to understand all the things I just explained.

And hopefully you will also start making an extension too!

_Happy coding to you all in this social distancing time._

