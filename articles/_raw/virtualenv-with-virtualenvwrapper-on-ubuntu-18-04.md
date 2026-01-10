---
title: How to Set Up Virtualenv with Virtualenvwrapper on Ubuntu 18.04
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-01T10:34:00.000Z'
originalURL: https://freecodecamp.org/news/virtualenv-with-virtualenvwrapper-on-ubuntu-18-04
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/1-aMYnl2Ctt9Y-RZ5bodNF2g.jpeg
tags:
- name: Developer
  slug: developer
- name: 'Integrated Development Environment  '
  slug: integrated-development-environment
- name: Ubuntu
  slug: ubuntu
- name: virtualenv
  slug: virtualenv
seo_title: null
seo_desc: 'By Goran Aviani

  Let me tell you a story. Recently, I realized that I needed to review how to set
  up virtualenvwrapper on top of virtualenv in Ubuntu 18.04. I have completed this
  process several of times on different computers, and every time it seems...'
---

By Goran Aviani

Let me tell you a story. Recently, I realized that I needed to review how to set up virtualenvwrapper on top of virtualenv in Ubuntu 18.04. I have completed this process several of times on different computers, and every time it seems to be just a little bit different than before.

I just got a new laptop and on the way home I read several tutorials on “How to set up virtualenvwrapper on Ubuntu 18.04”. And let me tell you – it seemed really easy because all of those tutorials were pretty straight forward and basically explained how to do these three 3 things:

* Install virtualenv
* Install virtualenvwrapper
* Edit .bashrc/.bash_profile or both

But even though I read all those tutorials none of them really worked for me.

I had several errors while trying to figure out what went wrong while following the tutorials. 

First I got some of “_mkvirtualenv: command not found_”, then a little of “_-bash: /usr/bin/virtualenvwrapper.sh: No such file or directory_”, and then a touch of “_ERROR: virtualenvwrapper could not find virtualenv in your path_”.

After some research I realized that all virtualenvwrapper Ubuntu 18.04 tutorials are copies an old text written before April 2016 (the release date of Ubuntu 16.04).  


I know this because from Ubuntu 16.04 and onward the location of vritualenvwrapper’s pip installation changed from `/usr/local/bin/virtualenvwrapper.sh` to `~/.local/bin/virtualenvwrapper.sh.` Note that the local directory is hidden.

So I'll start by writing a tutorial that will show you how to avoid all those issues mentioned above.

## Prerequisites

In this article I will show you how to set up virtualenvwrapper with pip3 (pip for Python 3). I chosen this version of pip instead of a Python 2 because Pythons 2's end of life was January 1. 2020.

> Python 2 will retire in… [https://pythonclock.org/](https://pythonclock.org/)

To complete this tutorial you will need a computer with Ubuntu 18.04 installed and an internet connection :). Also some knowledge about terminals and the Vim editor would be useful. I will assume you already updated and upgraded your system.

## Setting up a Virtual Environment

Now open your terminal in the home directory by right clicking and choosing the option “Open in Terminal”. You can also press the `CTRL`, `ALT`, and `T` keys on your keyboard at the same time to open the Terminal application automatically.

You first need to create a special directory that will hold all of your virtual environments. So proceed with creating a new hidden directory called virtualenv.

```
mkdir .virtualenv
```

Now you should install pip for Python3.

```
sudo apt install python3-pip
```

Confirm the pip3 installation.

```
pip3 --version
```

Now install virtualenv via pip3.

```
pip3 install virtualenv
```

To find where your virtualenv was installed, type:

```
which virtualenv
```

Install virtualenvwrapper via pip3:

```
pip3 install virtualenvwrapper
```

We are going to modify your .bashrc file by adding a row that will adjust every new virtual environment to use Python 3. We will point virtual environments to the directory we created above (.virtualenv) and we will also point to the locations of the virtualenv and virtualenvwrapper.

Now open the .bashrc file using Vim editor.

```
vim .bashrc
```

If you still haven’t used the Vim editor or you don’t have it installed on your computer you should install it now. It is a widely used Linux editor, and for good reason.

```
sudo apt install vim
```

After you've installed Vim open the file .bashrc file by typing the _vim .bashrc_ command in your terminal. Navigate to the bottom of the .bashrc file, press the letter _i_ to enter the insert mode of Vim, and add these rows:

```
#Virtualenvwrapper settings:
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_VIRTUALENV=/home/goran/.local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh
```

After you are done, press the _esc_ key. Then type `:wq` and press enter. This command will save and exit the Vim editor. Close and reopen your terminal when you’re done.

To create a virtual environment in Python3 and activate it immediately, use this command in your terminal:

```
mkvirtualenv name_of_your_env
```

You should confirm that this environment is set up for Python3:

```
Python -V
```

To deactivate the environment use the deactivate command.

```
deactivate
```

To list all available virtual environments use the command _workon_ or _lsvirtualenv_ (same result as workon but shown in a fancy way) in your terminal:

```
workon

lsvirtualenv
```

To activate one specific environment use workon + name of your environment:

```
workon name_of_your_env
```

There are several useful command you might need to use someday:

_Rmvirtualenv_ will remove a specific virtual environment located in your .virtualenv directory.

```
rmvirtualenv name_of_your_env
```

_Cpvirtualenv_ will copy the existing virtual environment to a new virtual environment and activate it.

```
cpvirtualenv old_virtual_env new_virtual_env
```

Well done! You have now created your first isolated Python 3 environment.

Thank you for reading! Check out more articles like this on [my freeCodeCamp profile](https://www.freecodecamp.org/news/author/goran/) and other fun stuff I build on [my GitHub page](https://github.com/GoranAviani).


