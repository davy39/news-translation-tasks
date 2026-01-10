---
title: Python IDE – Best IDEs and Editors for Python
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2022-04-12T19:28:47.000Z'
originalURL: https://freecodecamp.org/news/python-ide-best-ides-and-editors-for-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/Python-IDE---Best-IDEs-and-Editors-for-Python.png
tags:
- name: editor
  slug: editor
- name: ide
  slug: ide
- name: Python
  slug: python
seo_title: null
seo_desc: 'Much of your experience as a developer will depend on what program you''ve
  chosen to write your code in. A good integrated development environment (IDE) or
  Code Editor can really boost your productivity.

  The problem with popular languages like Python ...'
---

Much of your experience as a developer will depend on what program you've chosen to write your code in. A good integrated development environment (IDE) or Code Editor can really boost your productivity.

The problem with popular languages like Python is that every IDE or code editor under the sun seems to have good support for the language. While this can be great, choosing the best one becomes a bit tricky. 

In this article I'll introduce you to three IDEs and code editors that can make your Python journey smoother.

But before I begin I want to clarify the fact that this is not an exhaustive list. Like I said, Python is one of the most popular programming languages so it's supported by a large number of code editors and IDEs. 

I could've included as many of them as possible, but instead I chose to include the ones that I've used at some point in my life and don't mind going back to. Because I think this'll be more helpful.

Without any further ado, let's jump in!

## Table of Contents

* [IDE vs Code Editor – What's the difference?](#heading-ide-vs-code-editor-whats-the-difference)
* [PyCharm](#heading-pycharm)
* [Microsoft Visual Studio Code](#heading-microsoft-visual-studio-code)
* [Sublime Text](#heading-sublime-text)
* [Conclusion](#heading-conclusion)

## IDE vs Code Editor – What's the Difference?

Before you start reading about the IDEs and Code Editors I have in store for you, let's clarify the definitions of an IDE and a Code Editor.

As you may already know, source code files are just text files with certain extensions appended to them. Any text editor that has some special feature such as syntax highlighting, automatic code indentation, and so on to make editing code files easier is called a code editor. 

Popular code editors include Visual Studio Code, Sublime Text, Atom, Notepad++ and more.

An IDE or Integrated Development Environment, on the other hand, is a much more complex suite of software that combines multiple tools such as a code editor, a file browser, a terminal emulator, a database explorer and more in a single package. 

Popular IDEs include PyCharm, IntelliJ Idea, Microsoft Visual Studio, and others.

But thanks to modern highly extensible code editors such as Microsoft Visual Studio Code, the line between an IDE and a Code Editor has started to fade away.

Now that you have a better idea of what an editor is compared to a full-blown IDE, let's look at some of the best for Python coding.

## PyCharm

The first one in our list is an IDE from JetBrains. [PyCharm](https://www.jetbrains.com/pycharm/) is one of the most used Python IDEs out there (if not the most used).

![Image](https://www.freecodecamp.org/news/content/images/2022/04/complexLook@2x.jpg)
_https://www.jetbrains.com/pycharm/_

The IDE has two editions. The professional edition will cost you $8.90 every month and $89.00 every year if billed yearly. There is also the community edition which is completely free and is built on open-source software. In this article I'll discuss the community edition.

Both editions are available for Windows, macOS, and Linux. You can download the 30 day trial of the professional edition or the community edition from the official [download page](https://www.jetbrains.com/pycharm/download/).

The installation process is pretty straightforward regardless of the platform you're on. Once you've downloaded and installed PyCharm on your computer, you should be able to start the IDE. You can use the start menu shortcut on Windows, the Applications directory on macOS, or your application launcher on Linux.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-17.png)

You can create a new Python project by clicking on the _New Project_ button.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-18.png)

In the next step, choose where you'd like to store your project. You can either create a new virtual environment or use a previously configured interpreter. In this case, I'm creating a new environment.

If you check the _Create a main.py welcome script_ option, a new Python file with some boilerplate code will be created inside your project. Once you're happy with all the choices, hit the _Create_ button.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-19.png)

This is what the code editor looks like once the project has been created. On the left side you can browse all your source files, and you can hit the play button on the top right corner of the window to run the selected scripts in the dropdown.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/run-code-pycharm.png)

As you can see, PyCharm comes with a terminal built in on the bottom of the window and you can see outputs from your program without ever leaving PyCharm.

The community edition is quite complete and you can do more or less everything you can do on the professional edition. The professional edition has better support for web frameworks like Django and some other bells and whistles.

If you're a student, you can get PyCharm Professional Edition and all other JetBrains stuff for free [by applying on their website](https://www.jetbrains.com/community/education/#students). You can also get a free license of all the JetBrains products if you're [an open-source maintainer](https://www.jetbrains.com/community/opensource/).

## Microsoft Visual Studio Code

Next in the list of my favorites is Microsoft Visual Studio Code or VSCode for short. It's an open-source, electron-powered, cross-platform code editor from Microsoft with a ton of customization options and extensions.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-21.png)

By installing the right set of extensions, you can turn Visual Studio Code into almost a fully-featured Python IDE. You can download VSCode for free from the [official download site](https://code.visualstudio.com/#alt-downloads) for Windows, macOS, and Linux.

Once you've installed VSCode on your system, open the software and go to the extensions tab by hitting the _Ctrl + Shift + X_ key combination.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-22.png)

Use the search bar to search for and install the following extensions:

* [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) – provides features such as IntelliSense (Pylance), linting, debugging, code navigation, code formatting, refactoring, variable explorer, test explorer, and more!
* [PyLance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) – works alongside Python in Visual Studio Code to provide performant language support.
* [Visual Studio IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode) – provides AI-assisted development features for Python, TypeScript/JavaScript and Java developers in Visual Studio Code.

Once you have these three installed, you're good to go. Create a directory anywhere on your machine and open that folder using VSCode. You can use the integrated terminal to run your code or execute any command in general.

You can set breakpoints by clicking on the left side of any line number. Then you can hit _F5_ to start debugging or _Ctrl + F5_ to run the program without debugging. VSCode has a lot more tricks up its sleeve that you'll find out as you keep using it.

## Sublime Text

Sublime Text is one of the OG code editors that has been used by developers for years. It's a very performant, powerful code editor with rich support for packages.

You can download Sublime Text from their [official download page](https://www.sublimetext.com/download) for Windows, macOS, and Linux. Once you have it installed, start Sublime Text like any other software.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-23.png)

Now click on _Tools > Install Package Control..._

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-24.png)

This'll install the Sublime Package Manager. Wait until a success message shows up.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-25.png)

Now go to Command Palette using the _Ctrl + Shift + P_ key combination and type _Install Package_:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-26.png)

Select the first option and search for the [Anaconda](https://packagecontrol.io/packages/Anaconda) package. This is the ultimate Python package that turns Sublime Text into a Python IDE with features like autocompletion, code linting, IDE features, autopep8 formating, McCabe complexity checker, Vagrant and Docker support, and more.

There are also more specific packages such as [Djaneiro](https://packagecontrol.io/packages/Djaneiro) for Django support and [requirementstxt](https://packagecontrol.io/packages/requirementstxt) for requirements.txt support on Sublime Text. Just look around the Package Control [website](https://packagecontrol.io/browse) and you may find some pretty useful packages.

## Conclusion

As I've already said, this is not an exhaustive list of all the popular Python IDEs and Code Editors. I've also used [Spyder](https://www.spyder-ide.org/) at a point in my life but decided to leave it off since it's targeted at scientists and engineers. 

I've also used [IDLE](https://docs.python.org/3/library/idle.html) for a brief period as well but it didn't seem like a strong enough option when it comes to larger projects. 

If you think I've left out any other good one, let me know via [Twitter](https://twitter.com/frhnhsin) or [LinkedIn](https://www.linkedin.com/in/farhanhasin/). Also, if you're native Bengali speaker, checkout freeCodeCamp's [Bengali Publication](https://www.freecodecamp.org/bengali/news/) and [YouTube Channel](https://www.youtube.com/channel/UCYl5XjGuTM1gbXUuxH1e0jA). Till the next one, stay safe and keep learning.

