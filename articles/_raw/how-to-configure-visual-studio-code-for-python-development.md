---
title: How to Configure Visual Studio Code for Python Development
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2023-07-17T17:13:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-configure-visual-studio-code-for-python-development
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/visual-studio-code-for-python.png
tags:
- name: Python
  slug: python
- name: Visual Studio Code
  slug: visual-studio-code
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: 'Visual Studio Code is one of the most versatile code editors out there.
  Even though it''s a code editor, the sheer extensibility of the program makes it
  almost as capable as some of the JetBrains products out there.

  In this article, I''ll walk you thro...'
---

Visual Studio Code is one of the most versatile code editors out there. Even though it's a code editor, the sheer extensibility of the program makes it almost as capable as some of the JetBrains products out there.

In this article, I'll walk you through the entire process of configuring Visual Studio Code for Python development. It's not a universal setup, but this is something that I use personally and have found it to be really comfortable.

The first step is to install Visual Studio Code on your computer. I'm on Debian 12 at the moment and I have the editor ready to go. Platform specific [installation instructions](https://code.visualstudio.com/docs/setup/setup-overview) are available in the documentation.

Assuming you are past the installation step, now I'll introduce you to a set of essential extensions that will elevate your Python development experience to the next level.

## Python Extension

The first extension that you need to install is the [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from Microsoft.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-86.png)
_https://marketplace.visualstudio.com/items?itemName=ms-python.python_

This is actually an extension pack that contains two extensions. The first extension is the Python extension. It lays the foundation for Python development in Visual Studio Code.

The other one is [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance), which is a very performant language server for Python.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-88.png)
_https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance_

This extension provides rich intellisense support and is powered by [Pyright](https://github.com/microsoft/pyright), the static type checker from Microsoft. The next thing you need to think about is linting.

## Ruff Linter

A linter is a program that analyses your code statically and provides valuable insights on possible errors.

The Pylance extension does an excellent job of finding out fatal errors within your code, but there is more to code than just that.

When working on a big project, it's pretty common to leave unwanted mess within your codebase. Things like unused imports and variables, bad code practices, and so on.

A good linter can point out code smells like this and make your code cleaner. Now, the go-to choice when it comes to Python linters is Pylint.

Pylint has been around for ages and works quite well, but I think there is a better alternative.

Ruff is an extremely fast Python linter written in Rust that imposes stricter linting rules than Pylint. The tool also has an [official extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff).

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-89.png)
_https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff_

It's a plug n' play extension and doesn't require any additional configuration whatsoever. So once you have it installed, you're good to go.

## Isort

Like a linter, [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort) is another utility that's sole purpose is sorting import statements.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-95.png)
_https://marketplace.visualstudio.com/items?itemName=ms-python.isort_

The utility sorts all the imports alphabetically, while also dividing them into sections.

The extension is very straightforward. Once you have the extension, it'll render squiggly lines under any import statement that seems out of place.

You can then use the quick action menu to sort them. Or, you can also use the command palette to quickly access the isort command.

## Mypy Type Checker

Before I start talking about this extension, let me explain what [mypy](https://mypy-lang.org/) actually is.

According to the info on their homepage:

> Mypy is an optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing and static typing. Mypy combines the expressive power and convenience of Python with a powerful type system and compile-time type checking.

In simpler words, mypy forces you to add essential type annotations to your Python programs, making them easier to comprehend.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-90.png)
_https://mypy-lang.org/_

Recently, Microsoft has published [an extension](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker) that adds type checking functionality using mypy to their beloved editor.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-91.png)
_https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker_

Once you have installed the extension, it'll perform necessary checks on your code and report any missing type annotations as compile-time errors.

While having type annotations is not mandatory, it's highly recommended.

## IntelliCode

[IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode) provides AI assisted code completion in Visual Studio Code. It may sound similar to GitHub Copilot, but in reality it's a lot smaller than that.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-93.png)
_https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode_

Where GitHub Copilot or Tabnine provides full-blown code blocks, IntelliCode autocompletes lines of code pretty flawlessly.

In most cases, this extension can help you type less of the same code by suggesting the right thing while also keeping out of your way.

## Error Lens

While not related to Python specifically, [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens) is a great extension that embeds errors right by the side of the line of code.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-94.png)

I often work on my 14 inch Thinkpad and like to turn off the terminal pane. Error Lens eradicates the need to look at the terminal now and then to see my errors and warnings.

As useful as it may be, sometimes your editor can look cluttered due to all the warning and error outputs, so decide accordingly.

## Indent Rainbow

Unlike other programming languages, an incorrect level of indentation can literally break your program in Python.

Visual Studio Code already does a good job of visualizing indentation levels within your code, but if you want to add some color to it, the [indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) package is what you need.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-92.png)
_https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow_

It adds different colors to the different levels of indentation. Personally, I don't use this one on a regular basis, but you may find it useful.

## Conclusion

Like I said, these extensions and my personal configuration are not a silver bullet. But this setup is something that I've been using for quite a while and I hope it's useful to you as well.

I often install specialized extensions depending on the projects I work on. For example, I use the [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django) or [Jinja](https://marketplace.visualstudio.com/items?itemName=wholroyd.jinja) project when I work on a Django or Flask project.

Or I install the [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extension while working on a Jupyter Notebook. So feel free to install whatever you need, just don't overdo it.

