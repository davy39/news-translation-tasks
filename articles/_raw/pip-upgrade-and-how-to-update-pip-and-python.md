---
title: Pip Upgrade – And How to Update Pip and Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-14T21:04:29.000Z'
originalURL: https://freecodecamp.org/news/pip-upgrade-and-how-to-update-pip-and-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/updatePip.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Python is a widely used and powerful programming language that's relatively\
  \ simple to learn. \nPython releases patch updates every few months and major updates\
  \ around once in a year. Because of this, it is always a good idea to update the\
  \ version of P..."
---

Python is a widely used and powerful programming language that's relatively simple to learn. 

Python releases patch updates every few months and major updates around once in a year. Because of this, it is always a good idea to update the version of Python you have on your computer.

In addition, you need to update Python so you can get access to the exciting features they add after major updates. For example, there’s quite a speed improvement in Python 3.11 over 3.10.

There’s also a Python package manager called Pip you might need to update occasionally. It is to Python what NPM is to JavaScript. 

Starting from Python 3.4, Pip comes with the standard Python distribution. But if you don’t get it after installing Python for some reason, then you need to install it manually.

In this article, I will show you how to update Python on your Mac and Windows computer. I will also show you how to update Pip on the two operating systems.


## What We'll Cover
- [How to Update Python and Pip on Mac OS](#heading-how-to-update-python-and-pip-on-mac-os)
- [How to Update Python and Pip with Homebrew](#heading-how-to-update-python-and-pip-with-homebrew)
- [How to Update Only Pip with the Terminal](#heading-how-to-update-only-pip-with-the-terminal)
- [Conclusion](#heading-conclusion)


## How to Update Python and Pip on Mac OS
One of the easiest ways to update Python and Pip on Mac is by downloading the package from the Python official website.

When you update Python, the Pip version that comes with it is also updated.

First, check the versions of Python and Pip you have by running `python3 --version` and `pip3 --version`:

![Screenshot-2023-03-14-at-11.57.29](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-14-at-11.57.29.png)

Go to https://www.python.org/downloads/macos/ and select the release you want:

![Screenshot-2023-03-14-at-12.16.47](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-14-at-12.16.47.png)

For me, I picked `3.11` because it’s now stable.

Scroll down and download it for your OS – be it Windows or Mac. I chose Mac becuase I use Mac:

![Screenshot-2023-03-14-at-12.18.09](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-14-at-12.18.09.png)

Run the installer and follow every prompt you see.

![Screenshot-2023-03-14-at-12.19.43](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-14-at-12.19.43.png)

Confirm the installation by running `python3 --version` and `pip3 --version`:

![Screenshot-2023-03-14-at-12.21.47](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-14-at-12.21.47.png)


## How to Update Python and Pip with Homebrew
If you use Mac, you can also update Python and Pip with Homebrew.

Install `pyenv` by running `brew install pyenv`. `pyenv` is a Python version management tool. It is to Python what NVM (Node version manager) is to JavaScript.

![Screenshot-2023-03-14-at-13.29.50](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-14-at-13.29.50.png)

Install any version of Python you want, for instance, 3.9 or 2.7:

![Screenshot-2023-03-14-at-13.49.26](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-14-at-13.49.26.png)

You can also update Python by running `pyenv latest-version-number`. For example, `python 3.11`. When you install that Python version, you install Pip too.


## How to Update Only Pip with the Terminal
In cases when you want to update only Pip, open your terminal and run `pip3 install --upgrade pip`. You can then confirm the update by running `pip3 --version`:

![Screenshot-2023-03-14-at-13.02.02](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-14-at-13.02.02.png)


## Conclusion
This article took you through how to update Python and Pip by downloading the installation package and using the command line. We also looked at how you can update Pip only if you want to.

If you are using Windows and you want to update Python and Pip, you can also download the latest installer and let the installation wizard guide you through installing it.

Thanks for reading! 


