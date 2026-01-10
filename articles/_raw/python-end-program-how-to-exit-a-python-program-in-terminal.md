---
title: Python End Program – How to Exit a Python Program in the Terminal
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-05-16T16:48:59.000Z'
originalURL: https://freecodecamp.org/news/python-end-program-how-to-exit-a-python-program-in-terminal
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/jake-walker-MPKQiDpMyqU-unsplash.jpg
tags:
- name: Python
  slug: python
- name: terminal
  slug: terminal
seo_title: null
seo_desc: "You can execute Python code in a terminal just like you would in an IDE\
  \ like VS Code, Atom, and so on. You can do this in both Windows and Unix operating\
  \ systems like Linux and macOS. \nIn this article, you'll learn how to exit a Python\
  \ program in the..."
---

You can execute Python code in a terminal just like you would in an IDE like VS Code, Atom, and so on. You can do this in both Windows and Unix operating systems like Linux and macOS. 

In this article, you'll learn how to exit a Python program in the terminal using the following methods:

* The `exit()` and `quit()` functions in Windows and macOS (and other Unix-based systems – we'll use macOS to represent them). 
* The `Ctrl + Z` command in Windows. 
* The `Ctrl + D` command in macOS. 

## How to Run a Python Program in the Terminal

To run Python in the terminal, you have to open your terminal and run the `python` command. 

Note that the `Python` command will only work in your terminal if you have Python installed on your computer. 

After running the command, you should have something like this in the terminal:

```bash
C:\Users\USER>python
Python 3.10.8 (main, Nov  6 2022, 23:27:16)  [GCC 12.2.0 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/py-in-terminal.PNG)
_Python command in the terminal_

I am using Command Prompt for Windows but this should work the same way if you're using macOS or Linux.

Now you can run Python code in the terminal: 

```bash
>>> print("Welcome to Py in the terminal!")
Welcome to Py in the terminal!
```

## How to Exit a Python Program in the Terminal Using the `exit()` and `quit()` Functions

You can use the `exit()` and `quit()` functions to exit a Python program in Windows and macOS. 

```bash
>>> print("Welcome to Py in the terminal!")
Welcome to Py in the terminal!
>>> exit()

C:\Users\USER>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/py-in-terminal-exit.PNG)
_exit() command in Python terminal_

In the example above, we printed "Welcome to Py in the terminal!" before exiting the terminal using the  `exit()` function. 

After the function is executed, you'll be able to use the terminal the regular way (with the Python environment). 

The process is the same for the `quit()` function:

```bash
>>> print("Welcome to Py in the terminal!")
Welcome to Py in the terminal!
>>> quit()

C:\Users\USER>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/py-in-terminal-quit.PNG)
_exit() command in Python terminal_

## How to Exit a Python Program in the Terminal Using the `Ctrl +` Command

You can exit a Python program running in a Windows terminal using the `Ctrl + Z` command: 

```bash
>>> print("Welcome to Py in the terminal!")
Welcome to Py in the terminal!
>>> ^Z


C:\Users\USER>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/py-in-terminal-ctrl-z.PNG)
_ctrl + z command to exit Python terminal in Windows_

Similarly, you can use the `Ctrl + D` command in macOS. 

## Summary

In this article, we talked about running a Python program in the terminal. 

We saw how to run Python in the terminal using the `Python` command. 

We also saw how to exit a Python program in the terminal using a couple different methods. 

The `exit()` and `quit()` functions can exit a Python program in the terminal for both Windows and macOS. 

Alternatively, you can use the `Ctrl + Z` command to exit a Python program in the terminal in Windows and `Ctrl + D` in macOS. 

Happy coding! You can learn more about Python on [my blog](https://ihechikara.com/).

