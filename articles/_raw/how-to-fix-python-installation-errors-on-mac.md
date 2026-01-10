---
title: How to Fix Common Python Installation Errors on macOS
subtitle: ''
author: Daniel Kehoe
co_authors: []
series: null
date: '2024-06-10T22:57:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-fix-python-installation-errors-on-mac
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/python-install-errors.png
tags:
- name: error
  slug: error
- name: macOS
  slug: macos
- name: Python
  slug: python
seo_title: null
seo_desc: "Python's popularity keeps growing as more developers adopt it for data\
  \ science and machine learning, although it is already among the most popular programming\
  \ languages. \nI recently wrote an article for freeCodeCamp titled \"How to Install\
  \ Python on a..."
---

Python's popularity keeps growing as more developers adopt it for data science and machine learning, although it is already among the most popular programming languages. 

I recently wrote an article for freeCodeCamp titled "[How to Install Python on a Mac](https://www.freecodecamp.org/news/how-to-install-python-on-a-mac/)", which provides a clear guide to installing Python on macOS. 

As a follow-up, I will discuss errors you may encounter when installing Python on macOS and how to fix them in this article.

## **Contents**

Here's what we'll cover here:

* [How to Fix the "command not found: python" Error](#heading-how-to-fix-the-command-not-found-python-error)
* [Using an Out-of-date Python](#using-an-out-of-date-python)
* [Using the System Python](#heading-using-the-system-python)
* [Using the Homebrew Python](#heading-using-the-homebrew-python)
* [Missing Pip](#heading-missing-pip)
* [Pip Package Installation Errors](#heading-pip-package-installation-errors)
* [More on Mac Python](#heading-more-on-mac-python)
* [Conclusion](#heading-conclusion)

## How to Fix the "command not found: python" Error

You may encounter this error:

```bash
$ python ...
zsh: command not found: python

```

You'll see this when trying to run Python commands in the terminal. This mostly happens because Python is yet to be installed. However, it is also possible, and more frustrating, that the Python installation is not in the Mac PATH.

If you only need to install and run a Python application, you can use [Homebrew](https://mac.install.guide/homebrew/) to [install Pipx](https://mac.install.guide/python/pipx). This will install Python as a dependency. Pipx is a tool that allows you to install and run Python applications as standalone executables, avoiding dependency conflicts that can occur when using the standard Python package manager [Pip](https://pip.pypa.io/en/stable/).

If you're going to work on a programming project in Python, [install Python with Pyenv](https://mac.install.guide/python/install-pyenv), the standard Python version manager. Better yet, [install Python with Rye](https://mac.install.guide/python/install-rye), an all-in-one tool for Python installation, virtual environment management, and package installation.

If you're seeing the `zsh: command not found: python` error, and are certain you have already installed Python, you may need to update the [Mac Python PATH](https://mac.install.guide/python/path). You'll need to find where Python is installed on your system, which takes some sleuthing because there are multiple ways to install Python on macOS.

Here are the most common locations for Python on a Mac:

1. `/usr/bin/python3` is the system Python installed with Xcode Command Line Tools. This is an alias; the actual location is `/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/bin`.
2. `/opt/homebrew/opt/python@3.12/libexec/bin/python` is the Homebrew Python.
3. `/Library/Frameworks/Python.framework/Versions/3.12/bin/python3` is the Python installed with the official Python website installer.
4. `/Users/username/.pyenv/shims/python` is the Python installed with Pyenv.
5. `/Users/username/.rye/shims/python` is the Python installed with Rye.

Enter the full pathname followed by `python --version` and see if you get a version number. If you do, you'll need to update your PATH by adding the Python installation path to your `.zprofile` file. For more information, see  [Mac  PATH](https://mac.install.guide/terminal/path).

The article [Command not found: python](https://mac.install.guide/python/command-not-found-python) goes into more detail if you need more help.

## Using an Out-of-date Python Version

The current Python version is 3.12, as of October 2023. New releases of Python come yearly, typically released in October. The next version, Python 3.13, is expected in October 2024. The [newest Python version](https://www.python.org/downloads/source/) is listed on the Python website.

Check your Mac Python version:

```bash
$ python --version
Python 3.12.4

```

You should see `Python 3.12.4` or a later version. You may not notice issues with an older Python version but it's a good idea to start any project with the newest version. The article about [updating Python on Mac](https://mac.install.guide/python/update) explains how to update Python on macOS.

## Using the System Python

Macs no longer come with Python pre-installed. But you may have installed [Xcode Command Line Tools](https://mac.install.guide/commandlinetools/) which includes Python 3.9.6, an older Python version that supports Apple development utilities.

Try `python3 --version` and `which -a python3` to check if Python was installed with Xcode Command Line Tools.

```bash
$ python3 --version
Python 3.9.6
$ which -a python3
/usr/bin/python3

```

If you have Python 3.9.6 installed at `/usr/bin/python3`, you'll likely have the system Python installed by Xcode Command Line Tools. You can confirm this with `xcode-select -p` which will show if Xcode Command Line Tools is installed.

```bash
$  xcode-select -p
/Library/Developer/CommandLineTools

```

It's possible to [alias python3 to python](https://mac.install.guide/python/alias-python3) but I would not recommend using the system Python for development. The system Python is intended for Apple utilities, not for you, so you should install Python on macOS separately if you want to run Python programs or develop in Python.

See my freeCodeCamp article [How to Install Python on a Mac](https://www.freecodecamp.org/news/how-to-install-python-on-a-mac/) to install Python for development.

## Using the Homebrew Python

If you use Homebrew as a software package manager, you can easily install Python with `brew install python`. Homebrew-installed Python is suitable for running scripts but it has drawbacks for installing Python applications or Python software development, when packages are installed.

* **Homebrew's automatic updates.** Homebrew automatically updates its Python as a dependency for other packages, potentially breaking your projects.
* **Multiple projects may need different Python versions.** Homebrew-installed Python is a single version and you may need to switch among different versions for different projects.
* **Problems with environment isolation.** Homebrew provides a single Python environment, which can cause conflicts between projects. Pip, the Python package manager, will block installation of packages unless you first create a virtual environment.

You can check if Python is installed with Homebrew:

```bash
$ brew list | grep python
python@3.12

```

For running applications, it's best to [install Pipx](https://mac.install.guide/python/pipx) and use `pipx install` instead of `pip install` to install programs. For Python development, it's best to  install Pyenv or install Rye for Python version management and virtual environments.

## Missing Pip

READMEs and tutorials often assume users are familiar with Python development tools and instruct them to install Python packages using Pip, the Python package manager. If you've followed instructions that start with `pip install <package>`, you may have run into the `zsh: command not found: pip` error.

This is the error you'll see:

```bash
$ pip install <package>
zsh: command not found: pip

```

Pip is installed automatically with Python, so it's unusual to run the `python` command successfully and then `pip` and see the error. If you have Python installed, you should be able to use the `pip` command. You can try a special command that installs Pip:

```bash
$ python -m ensurepip --upgrade

```

If Pip is not already installed, this command will install it. Otherwise, nothing will happen. With this error, it's more likely that you have a Python installation that is not in your Mac Python PATH. See the article [Command not found: pip](https://mac.install.guide/python/command-not-found-pip) for more details.

## Pip Package Installation Errors

You will need to use Pip to install Python packages, unless you are using [Rye](https://rye.astral.sh/) as an all-in-one tool. However, Pip has some drawbacks.

By default, the `pip install <package>` command installs the package "globally." This means that the package is added to the global Python `site-packages` directory, which may result in conflicts if different projects require different versions of the same package. 

For example, if project A requires `package==1.0` and project B requires `package==2.0`, installing both packages globally may result in conflicts and [dependency hell](https://en.wikipedia.org/wiki/Dependency_hell). Without proper isolation, installing one project's dependencies can cause problems for another. To avoid these conflicts, create a Python virtual environment for each project.

There are two Python tools for creating virtual environments and using different versions of packages. [Venv](https://docs.python.org/3/library/venv) is a built-in Python package. [Virtualenv](https://virtualenv.pypa.io/en/latest/) is a more powerful tool with additional features. These tools allow `pip` to install Python packages into a virtual environment that has its own installation directories and does not share libraries with other virtual environments. Pip must be used in conjunction with either Venv or Virtualenv to successfully install packages.

When you try to install a package with Pip, you may see:

```bash
$ pip install <package>
error: externally-managed-environment

```

Recent versions of `pip` implement [PEP 668](https://peps.python.org/pep-0668/) to prevent attempts to install packages globally, which results in the message [error: externally-managed-environment](https://mac.install.guide/python/externally-managed-environment). This error occurs when attempting to install a package globally without using a virtual environment. To resolve this error, create a virtual environment using Venv or Virtualenv and install the package within it.

## More on Mac Python

You'll need to do more than install Python to begin a programming project, so I've also written a longer article about [Mac Python](https://mac.install.guide/python/) that explains the fundamentals of version management, virtual environments, and package management, as well as comparing various installation options.

## Conclusion

A variety of competing development tools means that it can be difficult to get started with Python compared to other programming languages such as JavaScript, Rust, or Ruby. Python is moving towards standardization of tools, and there's rapid innovation as the community seeks to improve the developer experience.

For now, developing Python skills requires some knowledge of the Python ecosystem, the various tools, and how to use them. Still, Python is popular and powerful, and the tutorials on freeCodeCamp will help you learn the language and become a better developer.

