---
title: Run Python Script – How to Execute Python Shell Commands in the Terminal
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-14T15:24:17.000Z'
originalURL: https://freecodecamp.org/news/run-python-script-how-to-execute-python-shell-commands-in-terminal
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-jan-kopr-iva-3280908.jpg
tags:
- name: Python
  slug: python
- name: shell script
  slug: shell-script
- name: terminal
  slug: terminal
seo_title: null
seo_desc: "By Suchandra Datta\nWhen you're starting out learning a new programming\
  \ language, your very first program is likely to be one that prints \"hello world!\"\
  . \nLet's say you want to do this in Python. There are two ways of doing it: using\
  \ the Python shell ..."
---

By Suchandra Datta

When you're starting out learning a new programming language, your very first program is likely to be one that prints "hello world!". 

Let's say you want to do this in Python. There are two ways of doing it: using the Python shell or writing it as a script and running it in the terminal. 

## What is a Shell?

An operating system is made up of a bunch of programs. They perform tasks like file handling, memory management, and resource management, and they help your applications run smoothly. 

All the work we do on computers, like analyzing data in Excel or playing games, is facilitated by the operating system. 

Operating system programs are of two types, called **shell** and **kernel** programs.

Kernel programs are the ones who perform the actual tasks, like creating a file or sending interrupts. Shell is another program, whose job is to take input and decide and execute the required kernel program to do the job and show the output. 

The shell is also called the **command processor**. 

## What is a Terminal?

The terminal is the program that interacts with the shell and allows us to communicate with it via text-based commands. This is why it's also called the command line. 

To access the terminal on Windows, hit the Windows logo + R, type cmd, and press Enter.

To access the terminal on Ubuntu, hit Ctrl + Alt + T.

## What is the Python Shell?

Python is an interpreted language. This means that the Python interpreter reads a line of code, executes that line, then repeats this process if there are no errors. 

The Python Shell gives you a command line interface you can use to specify commands directly to the Python interpreter in an interactive manner. 

You can get a lot of detailed information regarding the Python shell in the [official docs](https://docs.python.org/3/tutorial/interpreter.html#).

## How to Use the Python Shell

To start the Python shell, simply type `python` and hit Enter in the terminal:

```
C:\Users\Suchandra Datta>python
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>print("hello world!")



```

The interactive shell is also called REPL which stands for read, evaluate, print, loop. It'll read each command, evaluate and execute it, print the output for that command if any, and continue this same process repeatedly until you quit the shell. 

There are different ways to quit the shell:

* you can hit Ctrl+Z on Windows or Ctrl+D on Unix systems to quit
* use the exit() command
* use the quit() command

```
C:\Users\Suchandra Datta>python
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("HELLO WORLD")
HELLO WORLD
>>> quit()

C:\Users\Suchandra Datta>
```

```
C:\Users\Suchandra Datta>python
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()

C:\Users\Suchandra Datta>
```

```
C:\Users\Suchandra Datta>python
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> ^Z


C:\Users\Suchandra Datta>
```

## What Can You Do in the Python Shell?

You can do pretty much everything that the Python language allows, from using variables, loops, and conditions to defining functions and more. 

The `>>>` is the shell prompt where you type in your commands. If you have commands that span across several lines – for example when you define loops – the shell prints the `...` characters which signifies that a line continues.

Let's see an example:

```
>>>
>>> watch_list = ["stranger_things_s1", "stranger_things_s2", "stranger_things_s3","stranger_things_s4"]
>>>
>>>
```

Here we defined a list with some TV show names via the Python shell.

Next, let's define a function that accepts a list of shows and randomly returns a show:

```
>>> def weekend_party(show_list):
...     r = random.randint(0, len(show_list)-1)
...     return show_list[r]
...
```

Note the continuation lines (`...`) of the Python shell here.

Finally to invoke the function from the shell, you simply call the function the way you would do in a script:

```
>>> weekend_party(watch_list)
'stranger_things_s1'
>>>
>>>
>>> weekend_party(watch_list)
'stranger_things_s3'
>>>
>>>
>>> weekend_party(watch_list)
'stranger_things_s2'
>>>
>>>
>>> weekend_party(watch_list)
'stranger_things_s2'
>>>
>>>
>>> weekend_party(watch_list)
'stranger_things_s3'
>>>

```

You can inspect Python modules from the shell, as shown below:

```
>>>
>>>
>>> import numpy
>>> numpy.__version__
'1.20.1'
>>>
```

You can see what methods and attributes a module offers by using the `dir()` method:

```
>>>
>>> x = dir(numpy)
>>> len(x)
606
>>> x[0:3]
['ALLOW_THREADS', 'AxisError', 'BUFSIZE']
```

Here you can see that Numpy has 606 methods and properties in total.

## How to Run Python Scripts

The Python shell is useful for executing simple programs or for debugging parts of complex programs. 

But really large Python programs with a lot of complexity are written in files with a .py extension, typically called Python scripts. Then you execute them from the terminal using the `Python` command. 

The usual syntax is:

```
python filename.py
```

All the commands we executed previously via the shell, we can also write it in a script and run in this way. 

## Conclusion

In this article, we learnt about the shell, terminal, how to use the Python shell. We also saw how to run Python scripts from the command line.

I hope this article helps you understand what the Python shell is and how you can use it in your day to day lives. Happy learning!

