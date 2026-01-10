---
title: How to Set Up an Integrated Development Environment (IDE)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-17T21:25:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-an-integrated-development-environment-ide
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f42740569d1a4ca41a5.jpg
tags:
- name: beginner
  slug: beginner
- name: C
  slug: c
- name: ide
  slug: ide
- name: 'Integrated Development Environment  '
  slug: integrated-development-environment
- name: JavaScript
  slug: javascript
- name: learn to code
  slug: learn-to-code
- name: Python
  slug: python
- name: Tutorial
  slug: tutorial
- name: tutorial purgatory
  slug: tutorial-purgatory
seo_title: null
seo_desc: 'By M. S. Farzan

  If you''re moving from online tutorials to building your own projects, you might
  be overwhelmed by the idea of setting up your own integrated development environment
  (IDE), or wonder why you even need one to get your work done.

  In this...'
---

By M. S. Farzan

If you're [moving from online tutorials to building your own projects](https://www.freecodecamp.org/news/how-to-choose-a-programming-language-and-escape-tutorial-purgatory/), you might be overwhelmed by the idea of setting up your own integrated development environment (IDE), or wonder why you even need one to get your work done.

In this article, I'll discuss what an IDE _is_ and give you some ideas about what yours might look like, particularly if you're working in JavaScript, although the information will be applicable irrespective of language or project type.

Here's a video version of this post if you'd prefer (28 minute watch):

%[https://youtu.be/f-JWTicIOwI]

## What is an Integrated Development Environment?

An integrated development environment, put simply, is everything a programmer needs to get their work done.  The actual makeup of an IDE will vary between programming languages, types of projects, and even between programmers, but there are some things that are common among a lot of IDEs, which I'll cover below.

The simplest way to understand an IDE is to consider an "all-in-one" solution like [Unity](https://unity.com/). As a fully-featured game engine, Unity has everything you'll need to create a 2D or 3D game: a GUI that allows you to build your game world, a code editor (Visual Studio) where you can write scripts, a way to download dependencies and assets, and even GitHub integration so that you can keep track of build versions and collaborate on projects.  For smaller projects, Unity can be thought of as a fully functional integrated development environment, where everything is already set up for you after downloading the game engine.

Other IDEs can vary greatly in complexity, particularly if you're coming from an online tutorial that allows you to code right in the browser.  One of my gripes with common answers to the question, "what programming language should I learn?" is the notion that learning JavaScript is easier because "it just runs in your browser."

Tell that to anyone who's attempted to set up an IDE for Create React App, which requires several components to get up and running - none of which are apparent when you're working through online tutorials.  To actually do work as a developer, you'll need four main things to set up your integrated development environment: a code editor, command line interface (CLI), version control system, and package manager.

Major caveat: your IDE may vary greatly depending on programming language or type of project, but you'll likely need one or more of the following in any case!

## IDE Tool #1: Code Editor (and Compiler)

A whole bunch of online tutorials allow you to just code in the browser, which is great for understanding basic programming concepts, but in the long run, you'll need an editor that allows you to save your code (and compile it, if you're using a language like C# or C++).

There are a lot of code editors out there, such as [Atom](https://atom.io/) (lightweight, free, and open source), [Sublime](https://www.sublimetext.com/) (super popular with tons of integrations), and [Visual Studio / Visual Studio Code](https://visualstudio.microsoft.com/) (supported by Microsoft and wonderful to work with).  It would be reductive to say that they're "all the same thing," as each one provides a different approach to supporting your coding workflow, so you might try one or two before deciding which one you like best.

## IDE Tool #2: Command Line Interface (CLI)

If you have a computer, you've undoubtedly used your file explorer or some other navigational GUI to access the file system, create folders, delete files, and so on.

The command line interface (CLI) allows you to do the same thing...in plain text.  Which might seem super archaic or annoying at first, but once you wrap your head around chaining commands together and integrating them into your workflow, you'll begin to see the power of the CLI and how essential it is to most development environments.

On Mac, you might be using the Terminal.  Because I've installed GitHub for Windows (more on GitHub below) on my machine, I use Git Bash for my work.  There are several options here for you, and it might do to check out a few command line tutorials to understand some of the basic principles so that you feel comfortable using it in your IDE.

## IDE Tool #3: Version Control System

There are several [resources](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) out there that provide overviews of what is version control and why you should use it. Suffice it to say that when you're building anything other than a simple project, you'll need a way to back up your work, share your code with collaborators, and keep track of the different build versions so that you can muck with parts of the code base and not others.

[GitHub](https://github.com/) isn't the only version control system out there, but it is the gold standard at the moment, and it would be worth your while to look up a few tutorials to learn how to take advantage of its features, even if you just wind up using it as a remote backup method.

Additionally, while there are several addons to integrate GitHub right into your code editor (or game engine), the standard practice for doing Git-related tasks is by using the command line interface, which provides another reason for becoming proficient with your CLI of choice.

## IDE Tool #4: Package Manager

For some IDEs, like with our Unity example above, all you need to do is download and install software to get started with building your projects.  Most of the dependencies that you'll need will be included with your initial download, and if not, there will be a way to access them from within the game engine (e.g. Unity's [Asset Store](https://assetstore.unity.com/)).

For other, more choose-your-own-adventure IDEs, you'll need to piece things together yourself, and one of the essential components will be a package manager like [NPM](https://www.npmjs.com/) or [Conda](https://docs.conda.io/en/latest/).

Package managers do a lot of things, and at their most basic functionality, they'll help you to install all the dependencies you'll need to get your work done.  If you want to get started on a React project, for example, you'll navigate to a folder through your CLI, and, after installing NPM (which is bundled with [Node.js](https://nodejs.org/en/)) type:

```
npx create-react-app my-app 
cd my-app 
npm start
```

The first line basically says: "Hey, NPM! Download all the dependencies for Create React App, and put them in a folder called 'my-app.'"

The second line then tells your CLI: "Navigate to the new directory called 'my-app.'"

The third line gets the action going: "NPM, it's me again. Start a development server that displays my project in a browser and updates it whenever I make changes to the code."

Once you've installed all of the necessary dependencies using your package manager, you'll begin working in your code editor and using the command line interface to make pull requests or push code to a remote repository using your version control system.

In summary, an integrated development environment comprises all of the things you need to get your work done, and varies based on language, project type, and your personal preference.  Ordinarily, IDEs include a code editor (and compiler), command line interface, version control system, and package manager, but your integrated development environment might have different requirements or a combination thereof.

You can do it!

If you enjoyed this article, please consider [checking out my games and books](https://www.nightpathpub.com/), [subscribing to my YouTube channel](https://www.youtube.com/msfarzan?sub_confirmation=1), or [joining the _Entromancy_ Discord](https://discord.gg/RF6k3nB).

**M. S. Farzan, Ph.D.** has written and worked for high-profile video game companies and editorial websites such as Electronic Arts, Perfect World Entertainment, Modus Games, and MMORPG.com, and has served as the Community Manager for games like _Dungeons & Dragons Neverwinter_ and _Mass Effect: Andromeda_. He is the Creative Director and Lead Game Designer of _[Entromancy: A Cyberpunk Fantasy RPG](https://www.entromancy.com/rpg)_ and author of _[The Nightpath Trilogy](http://nightpathpub.com/books)_. Find M. S. Farzan on Twitter [@sominator](http://www.twitter.com/sominator).

