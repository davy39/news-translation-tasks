---
title: How to Set Up a Python Virtual Environment on Ubuntu 20.04
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-12T14:36:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-python-virtual-environment-on-ubuntu-20-04
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/prateek-katyal-6jYnKXVxOjc-unsplash.jpg
tags:
- name: 'Integrated Development Environment  '
  slug: integrated-development-environment
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: Ubuntu
  slug: ubuntu
- name: virtualenv
  slug: virtualenv
seo_title: null
seo_desc: 'By Goran Aviani

  I recently got myself a “new” laptop – a Lenovo x270 (yay)! And once again I needed
  to set up a Python virtual environment. So of course I Googled for a solution, just
  to find my previously written article on the same topic!

  So in thi...'
---

By Goran Aviani

I recently got myself a “new” laptop – a Lenovo x270 (yay)! And once again I needed to set up a Python virtual environment. So of course I Googled for a solution, just to find my [previously written article on the same topic](https://www.freecodecamp.org/news/virtualenv-with-virtualenvwrapper-on-ubuntu-18-04/)!

So in this article, I'll update the instructions based on my newly acquired knowledge.

And let me tell you, it’s easier than before because we are going to do only two things:

* Install virtualenvwrapper
* Edit the .bashrc file

## Prerequisites

In this article I will show you how to set up virtualenvwrapper with pip3 (pip for Python 3). We are not going to use Python 2 because [it's no longer supported](https://www.python.org/doc/sunset-python-2/).

To complete this tutorial, you will need a computer with Ubuntu 20.04 installed and an internet connection. Also, some knowledge of the terminal and Vim editor would be useful.

## Setting up a Virtual Environment

Now open your terminal in the home directory by right clicking and choosing the option “Open in Terminal”. You can also press the CTRL, ALT, and T keys on your keyboard at the same time to open the Terminal application automatically.

You first need to create a special directory that will hold all of your virtual environments. So go ahead and create a new hidden directory called virtualenv:

```bash
mkdir .virtualenv
```

## pip3

Now you should install pip for Python3:

```bash
sudo apt install python3-pip
```

Confirm the pip3 installation:

```bash
pip3 -V
```

## virtualenvwrapper

virtualenvwrapper is a set of extensions for virtualenv. It provides commands like mkvirtualenv, lssitepackages, and especially workon for switching between different virtualenv environments.

Install virtualenvwrapper via pip3:

```bash
pip3 install virtualenvwrapper
```

## bashrc file

We are going to modify your .bashrc file by adding a row that will adjust every new virtual environment to use Python 3. We will point virtual environments to the directory we created above (.virtualenv) and we will also point to the locations of the virtualenv and virtualenvwrapper.

Now open the .bashrc file using the Vim editor:

```bash
vim .bashrc
```

If you still haven’t used Vim before or you don’t have it installed on your computer, you should install it now. It is one of the most widely used Linux editors and for good reason.

```bash
sudo apt install vim
```

After you've installed Vim open the .bashrc file by typing in the `vim .bashrc` command in your terminal. Navigate to the bottom of the .bashrc file, press the letter **_i_** to enter insert mode in Vim, and add these rows:

```bash
#Virtualenvwrapper settings:
export WORKON_HOME=$HOME/.virtualenvs
VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
. /usr/local/bin/virtualenvwrapper.sh

```

After you are done, press the _**esc**_ key, then type **:_wq_** and press enter. This command will save the file and exit Vim.

Now you need to reload the bashrc script. There are two ways to do it – close and reopen your terminal, or execute this command in the terminal:

```bash
source ~/.bashrc
```

To create a virtual environment in Python3 and activate it immediately use this command in your terminal:

```bash
mkvirtualenv name_of_your_env
```

To deactivate the environment use the deactivate command.

To list all available virtual environments use the command _workon_ or _lsvirtualenv_ (lsvirtualenv will show the same result as workon but in a fancier way) in your terminal:

```bash
workon
```

```bash
lsvirtualenv
```

To activate one specific environment use workon + name of your environment:

```bash
workon name_of_your_env
```

There are several useful command you might need to use someday:

_Rmvirtualenv_ will remove a specific virtual environment located in your .virtualenv directory.

```bash
rmvirtualenv name_of_your_env
```

_Cpvirtualenv_ will copy the existing virtual environment to a new virtual environment and activate it.

```bash
cpvirtualenv old_virtual_env new_virtual_env
```

Well done! You have now created your first isolated Python 3 environment.

Thank you for reading! 

Check out more articles like this on my [freeCodeCamp profile](https://www.freecodecamp.org/news/author/goran/), [Medium profile](https://medium.com/@goranaviani), and other fun stuff I build on my [GitHub page](https://github.com/GoranAviani).

