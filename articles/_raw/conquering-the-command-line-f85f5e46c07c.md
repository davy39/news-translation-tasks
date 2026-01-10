---
title: Conquering the Command Line
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-05T17:11:11.000Z'
originalURL: https://freecodecamp.org/news/conquering-the-command-line-f85f5e46c07c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NvuIEr51nwGNxv7O3TXcpA.png
tags:
- name: mac
  slug: mac
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: terminal
  slug: terminal
- name: unix
  slug: unix
seo_title: null
seo_desc: 'By Monica Powell

  A brief guide to getting started on UNIX/Mac OS terminal

  When I was first introduced to the command line I really had to adjust to navigating
  my computer in a black box with just text. So I avoided the command line as much
  as possibl...'
---

By Monica Powell

#### A brief guide to getting started on UNIX/Mac OS terminal

When I was first introduced to the command line I really had to adjust to navigating my computer in a black box with just text. So I avoided the command line as much as possible. I was accustomed to the visual cues and feedback that a computer usually provides. In many ways it felt like I was re-learning how to use a computer via the command line.

Yet, since first learning how to navigate my computer using UNIX commands I’ve learned that the command line doesn’t have to be a scary thing just because there’s no visual feedback when typing a password in on the command line. As security, nothing shows up as you type in your password to indicate that any characters have been entered.

#### What is the command line?

The command line is a software that executes commands or instructions for a computer to manipulate or interact with its file system.

### What is UNIX?

#### Why Use the Command Line?

* Faster to modify, navigate between files
* Able to install software as a superuser
* Can see hidden dotfiles  
dotfiles are UNIX configuration files, they tend to be files that are proceeded with a `.` and are hidden to normal users.  
You can [learn more about getting started with dotfiles in this article](https://medium.com/@webprolific/getting-started-with-dotfiles-43c3602fd789)).

In order to get started on the command line you should navigate to your applications and open the **Terminal** application.

![Image](https://cdn-media-1.freecodecamp.org/images/0wX7Il6ZWb4qFXWhJ1rAvbrEAquvv0mWSDcV)
_Above is the Terminal Icon on Mac._

### Create a Basic Website Folder on the Command Line

![Image](https://cdn-media-1.freecodecamp.org/images/q-nEv8AuA5alFW0jj8uEDZfN7Re2bCsyWNbV)
_Folder structure of sample project_

A folder with the above structure can be create on the command line by typing the commands inside of an empty directory:

![Image](https://cdn-media-1.freecodecamp.org/images/skROBs72rmbM9R19Xll-9fVTzLXZoEi1VHrc)
_We start inside of an empty directory!_

* Make a directory (also known as a folder) called personal-website  
`mkdir personal-website`

![Image](https://cdn-media-1.freecodecamp.org/images/nXYWE7E1AQgDoGiFXHYRmmop7jAGy7HR7Xt-)
_We’ve created a folder named personal-website_

* Navigate to inside of the directory called personal-website  
`cd personal-website`
* create a directory, inside of the personal-website folder called assets  
`mkdir assets`

![Image](https://cdn-media-1.freecodecamp.org/images/hwOipEstl7aPZxV1youY746JZnJqcuv8j5VU)
_We’ve created a folder inside of personal-website to contain all of our assets_

* Navigate inside of the assets folder which is inside of the personal-website folder  
`cd assets`
* create a directory, inside of the assets folder named images  
`mdkir images`
* create a directory, inside of the assets folder named js  
`mkdir js`
* create a directory, inside of the assets folder named css  
`mkdir css`

![Image](https://cdn-media-1.freecodecamp.org/images/VjWywXJ3fXn8IIUSS1rUS82fWBelN6qVwg28)
_We’ve created folders inside of personal-website/assets to store our project’s assets_

![Image](https://cdn-media-1.freecodecamp.org/images/loq-rOeylfEFovUlcja88GAhSSXTq4JRjjbC)

Woops! We forgot to create an index.html file :(

We are in the assets folder and want an index.html file in our main personal-website folder. Typing `cd ..` will move us out of the assets folder and into the directory above which is personal-website. Now that we are in the personal-website folder if we type `touch index.html` a blank index.html file will be created.

![Image](https://cdn-media-1.freecodecamp.org/images/ws7T-u5nT2AWqrsKAipU2E5upuEmeN18gCC5)

### Some frequently used terminal commands are:

#### commands to navigate/manipulate the filesystem

**ls**  
 **list** the contents of a directory

**pwd**  
**print working directory** for the terminal to display the directory you are currently working on

**touch**   
create or open a file without making any changes  
very handy when wanting to create empty files without leaving the command line

**sudo**   
this allows you to run commands as a **super user**

**mv**   
**move** a file or directory  
this can be used to move or rename a file by updating the file path

**cd**   
**change the current directory** you are working on so that you can access files on a different part of the system  
`cd` moves you to the root directory (top level folder on computer — usually the current User)  
`cd .` current directory   
`cd ..` navigates to directory two levels up

**mkdir**   
**make** a new **directory** (or a folder)

#### **Commands to Install Software**

You can install some software from the command line using the following commands:

* in Python `pip install <package nam`e>.   
Pip is a software package manager for Python.
* in JavaScript `npm install <package na`me>   
NPM is a package manager for JavaScript pages.

#### Commands to Run Software

In order to run a script on the command line you need to provide a command prompt and file name. Some examples are:

* in Java `javac filename.java` and then `java filename` compiles java projects and then runs them.
* in Python `python filename` runs python scripts.

If you find you are repeating a lot of commands you can scroll through your recent commands using the up/down arrows and edit them and re-run by navigating to them and then pressing enter.

#### Additional Resources to Get Started with Command Line Prompts

* [MIT Terminus (interactive game to learn command line)](http://web.mit.edu/mprat/Public/web/Terminus/Web/main.html)
* [Codecademy Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line)
* [Learn Python the Hard Way’s Command Line Crash Course](https://learnpythonthehardway.org/book/appendixa.html)

#### Decorating the Command Line

You can completely customize the colors and outputs on the command line to better suit your visual and aesthetic needs.

Here’s how I’ve made my command line prettier :

How to install Tomorrow Night  
[https://github.com/chriskempson/tomorrow-theme/blob/master/OS%20X%20Terminal/Tomorrow%20Night.terminal](https://github.com/chriskempson/tomorrow-theme/blob/master/OS%20X%20Terminal/Tomorrow%20Night.terminal)

[**Customize the terminal**](https://mindthecode.com/customize-the-terminal/)  
[_I love the terminal. Besides the fact it makes you look awesome while using it, it can also do about a gazillion…_mindthecode.com](https://mindthecode.com/customize-the-terminal/)

_If you enjoyed reading this article consider tapping the clap button ?. Wanna see more of my work? Check out m[y GitHub](https://github.com/M0nica/) to view my code and learn more about my development experience at h[ttp://aboutmonica.com.](http://aboutmonica.com)_

