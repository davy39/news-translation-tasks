---
title: Python List Files in a Directory Guide - listdir VS system("ls") Explained
  with Examples
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-04-06T14:10:27.000Z'
originalURL: https://freecodecamp.org/news/python-list-files-in-a-directory-guide-listdir-vs-system-ls-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/listdir-vs-system-v2.png
tags:
- name: command
  slug: command
- name: Python
  slug: python
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: '🔹 Welcome

  If you want to learn how these functions work behind the scenes and how you can
  use their full power, then this article is for you.

  We will start by diving into concepts that are essential to work with listdir and
  system:


  The built-in Pyt...'
---

## 🔹 Welcome

If you want to learn how these functions work behind the scenes and how you can use their full power, then this article is for you.

We will start by diving into concepts that are essential to work with `listdir` and `system`:

* The built-in Python `os` module and how to import it.
* The concepts of "directory" and "current working directory".
* How to check and change your current working directory. 
* The difference between an absolute path and a relative path.

Then, we will dive into the functions themselves:

* How to work with the `listdir` function and when to use it.
* How to work with the `system("ls")` function and when to use it.
* Examples of both of them and how they work behind the scenes.

Let's begin! ⭐

## 🔸 The OS Module

The two functions that we will discuss: `listdir()` and `system()` belong to the `os` module. This module includes functions that are used to interact with your operating system, performing actions like:

* Making a new directory.
* Renaming an existing directory.
* Removing a directory.
* Displaying the path to your current working directory.
* Much more! 

**💡 Tips:** 

* A **directory** is what we commonly know as a "folder", where we usually store related files and/or other directories, creating a hierarchy of directories within directories that are called subdirectories. An example of a directory is your "Documents" folder.
* A **module** is a file that contains related Python code. 

### How to Import the OS Module

To use the `os` module in your script, you need to "import" it. Importing a module means gaining access to all the functions and variables that are stored within the module. We import a module when we want to use its code in our script. 

To import the `os` module, you simply need to include this line at the top of your Python script or run this line in the interactive shell:

```python
import os
```

This will give you access to all the functions defined in the `os` module.

**💡 Tip:** this module was already installed when you installed Python 3, so you will be able to use it immediately.

To be able to use the functions from the `os` module, you will need to add the prefix `os.` before the name of the function that you want to call, like this:

```python
os.<function>(<params>)
```

For example:

```
os.mkdir("New Folder")
```

### How to Import Individual Functions

If you are only going to work with one or two functions from the module, you can import them individually using this syntax:

```
from <module> import <function1>, <function2>, ...
```

For example:

```python
from os import listdir, system
```

In this case, you can call the functions in your script as you normally would, **without** adding the `os.` prefix, like this:

```python
<function>(<params>)
```

For example:

```
mkdir("New Folder")
```

## 🔹 Current Working Directory

Now let's see a very important concept that you need to know before you start working with `listdir` and `system`. Your current working directory, as the name implies, is the directory (folder) where you are currently working. 

You can check your current working directory with this function from the `os` module:

```python
os.getcwd()
```

This will show you the path to your current working directory. 

💡 **Tip:** `cwd` means "current working directory."

### From the Interactive Shell

If I run this command in the interactive shell (Windows), I see this:

```python
>>> os.getcwd()
'C:\\Users\\estef\\AppData\\Local\\Programs\\Python\\Python38-32'
```

This is the full path to my current working directory:

```python
'C:\\Users\\estef\\AppData\\Local\\Programs\\Python\\Python38-32'
```

### From a Script

If I run this command from a script, like this:

```python
import os
print(os.getcwd())
```

 I see:

```python
C:\Users\estef\Documents\freeCodeCamp\freeCodeCamp News\listdir vs system
```

The full path to the script (its location in the system, in the hierarchy of directories).

💡 **Tip:** If you run a script (a Python file), your current working directory is the directory where the script is currently in.

### How to Change your Current Working Directory

You can change your current working directory with this command from the `os` module:

```python
os.chdir(<path>)
```

You will need to specify the path to the new working directory, passing it as an argument, formatted as a string. It can be either an absolute path or a relative path. 

💡 **Tip:** 

* An **absolute path** specifies all the sequence of directories that you need to go through to reach your target directory. This path starts from the root directory of your system. 

For example:

```python
>>> import os
>>> os.chdir(r"C:\Users\estef\Documents\FreeCodeCamp\freeCodeCamp News\9 - listdir vs system")

# Checking current working directory:
>>> os.getcwd()
'C:\\Users\\estef\\Documents\\FreeCodeCamp\\freeCodeCamp News\\9 - listdir vs system'
```

Notice that I added an `r` before the absolute path to convert the string into a raw string. If you use `\` and you don't add the `r`, you will get an error because the `\` symbol will be treated as a special character.

Alternatively, you could replace the backslashes  `\` with forward slashes `/` in the path:

```python
>>> os.chdir("C:/Users/estef/Documents/FreeCodeCamp/freeCodeCamp News/9 - listdir vs system")

# Checking current working directory
>>> os.getcwd()
'C:\\Users\\estef\\Documents\\FreeCodeCamp\\freeCodeCamp News\\9 - listdir vs system'
```

* A **relative path** specifies the path that you want to follow to find the target directory, but now the path starts from your **current** working directory. It's shorter and simpler than the absolute path. 

For example, if your current working directory contains a subdirectory (folder) `Directory 1`, you can move to this directory using a relative path (imagine it as a folder within another folder, and we are going deeper and deeper into the hierarchy), like this:

```python
>>> import os
>>> os.chdir(".\Directory 1")

# Check current working directory
>>> os.getcwd()
'C:\\Users\\estef\\Documents\\FreeCodeCamp\\freeCodeCamp News\\9 - listdir vs system\\Directory 1'
```

💡 **Tip:** The dot (`.`) at the beginning of the relative path `.\Directory 1` represents the current working directory. A double dot ( `..`) is used to move up the hierarchy, to the "parent" directory.

Now that you have all the background knowledge that you will need to truly understand how `listdir` and `system` work, let's see them in detail.

## 🔸 Listdir

We will start with the `listdir` function. Let's reveal its mysteries. ?

### Purpose and Return Value

According to the [Python Documentation](https://docs.python.org/3/library/os.html#os.listdir), the purpose of this function is to:

> Return a list containing the names of the entries in the directory given by _path_.

Basically, this function returns a list with the names of all files and directories that are currently found within a particular directory that you specify when you call the function.

💡 **Tip:** The list will not have a specific order, even if you usually sort the elements alphabetically.

### Syntax and Parameter

To call `listdir`, will need to use this syntax:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-9.png)

The parameter `path` is precisely that, the absolute or relative path to the directory that you want to visualize. In Python 3.2 and above, this parameter is optional. By default, the path will lead to your current working directory if you don't pass an argument. 

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-12.png)

Remember that you must import the `os` module before calling this function.

💡 **Tip:** If you use this import statement `from os import listdir` to import the function individually, you can omit the `os.` prefix, like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-10.png)

### Use Cases and Advantages

The function `listdir` is very helpful because it works on any operating system where Python runs, so if Python is installed on your device, this function will work correctly. 

Now let's talk a little bit about its return value. Since it returns a list, we can store this list in a variable and work with it in our program. 

For example, let's say that we want to do something with all the files from a given directory, such as converting images to black and white or modifying their content. We could do it using a for loop, like this:

```python
images = os.listdir(<path>)

for image in images:
	# Do something to the image

```

Of course, you would need to define what happens within the loop, but this is an example of what you could do with this function. 

This is awesome, right? 

But having files and directories in the same list can be a little bit problematic if we want to work with a for loop, right? We would need to add a conditional to check the type of each element. How can we make a list that only contains file names (no directories) or vice versa? 

Let's see! ✨

### Only Include Files

If you want to "filter" the list returned by `os.listdir()` to include only **files** (no directories) you can use this line of code:

```python
list(filter(os.path.isfile, os.listdir(<path>)))
```

💡 **Tip:** You can customize the `<path>` argument or omit it to use your current working directory.

Let's see an example with my current working directory (I'm using Windows):

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-23.png)

My directory (folder) has:

* Two subdirectories (folders within the main folder)
* One PowerPoint file
* One image (.png file)
* One Python script

If I call the `listdir` function from the `script.py` file and print the list returned:

```python
print(os.listdir())
```

This is the output:

```python
['Diagrams.ppt', 'Directory 1', 'Directory 2', 'listdir vs system.png', 'script.py']
```

You can see that all files and directories from my current working directory were included.

To filter the list to only contain files, we can use this statement:

```python
print(list(filter(os.path.isfile, os.listdir())))
```

Now the output is:

```python
['Diagrams.ppt', 'listdir vs system.png', 'script.py']
```

Notice how the directories were "filtered", exactly what we wanted.

### Only Include Directories

Similarly, if you want to "filter" the list to include only **directories**, you can use this line of code:

```python
list(filter(os.path.isdir, os.listdir(<path>)))
```

Now the output is:

```
['Directory 1', 'Directory 2']
```

Exactly what we wanted. But how does this statement work behind the scenes? Let's see.

### How `filter()` Works Behind the Scenes

The filter function is called using this syntax:

```
filter(<function>, <list>)
```

It basically "filters" the elements of the second argument (the list) based on the truth value returned by calling the function passed as the first argument (`os.path.isfile()` or `os.path.isdir()` in their respective commands):

```python
print(list(filter(os.path.isfile, os.listdir())))
```

```python
list(filter(os.path.isdir, os.listdir()))
```

These two functions:

```
os.path.isfile(<path>)

os.path.isdir(<path>)
```

Return `True` if the argument is a file or a directory, respectively.  

Based on these truth values, the elements of the list will be included (or not) in the final "filtered" list. The elements of the list returned by `os.listdir()` are passed one by one to these functions to check if they are files (or directories, respectively).

For example: If we have this line of code:

```python
filter(os.path.isfile, os.listdir())))
```

 And `os.listdir()` returns this list:

```python
['Diagrams.ppt', 'Directory 1', 'Directory 2', 'script.py']
```

The first element of the list (`'Diagrams.ppt'`) is passed as argument to `os.path.isfile()` to check if it's a file :

```python
os.path.isfile('Diagrams.ppt') # True
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-30.png)

The function call returns `True`, so it's a file and it's included in the list.

But if the element is a directory:

```python
os.path.isfile('Directory 1') # False
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-31.png)

The function call returns `False`, so it's not included in the list. This process continues for every element in the list until the new list only contains file names.

Then, since `filter()` returns an iterable, we make a list from this iterable using `list()`:

```python
list(filter(os.path.isfile, os.listdir()))
```

And we print it since we are working with a Python file (script):

```python
print(list(filter(os.path.isfile, os.listdir())))
```

💡 **Tip:** You can visually identify if an element of the list represents a file or a directory by seeing if it has an extension (type) after its name. For example: `Diagrams.ppt` has a `.ppt` extension that tells you that it's a PowerPoint file but a directory doesn't have an extension, like `'Directory 1'`.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-32.png)

## 🔹 System("ls")

Now that you know how to work with `listdir`, let's see how the `system()` function works behind the scenes and how you can use it. 

### Purpose 

According to the [Python Documentation](https://docs.python.org/3/library/os.html#os.system), the purpose of the `system()` function is to:

> Execute the command (a string) in a subshell

Basically, this function takes a command (as a string) and executes it. 

In this case, the command that we are passing is `'ls'` , a Unix command used in Linux to display the content of a directory as standard output. 

Unlike `listdir`, the `system()` function **will not return a list** if we pass the `'ls'` command, it will only **display** the list of files and directories as standard output. Therefore, you should use it if you only want to visualize the list without actually working with it in your program.

### Syntax and Parameter

To call this function, you will need to use this syntax:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-15.png)

Its only argument is the command that you want to execute formatted as a string (surrounded by double quotes or single quotes).

Particularly, the `ls` command lets you see the content of your current working directory. 

For example: if this is my working directory (three Python files and one subdirectory):

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-17.png)

And I call the `system()` function, like this:

```python
>>> import os
>>> os.system("ls")
```

This is the output:

```python
'Directory 1'  'file 1.py'  'file 2.py'   main.py
0
```

We can see the standard output in the console (the list of files and directories):

```python
'Directory 1'  'file 1.py'  'file 2.py'   main.py
```

and the return value:

```python
0
```

💡 **Note:** For these examples of the `system()` function, I'm working with an online command line tool called Repl.it since my computer has Windows installed and the command `ls` is not recognized by the default command prompt. 

### Limitations

One of the main limitation of this function is that the command passed as argument has to be recognized by the operating system or environment that you are working with. 

For example, the `ls` command will not be recognized in Windows by default in the command prompt. You will see this error if you try to run it:

> 'ls' is not recognized as an internal or external command, operable program or batch file.

A similar command in Windows would be the `'dir'` command:

```python
os.system('dir')
```

**💡 Tip:** There are alternative ways to run the `ls` command on Windows, such as using terminal programs that recognize Unix commands, but by default Windows does not recognize the `'ls'` command.

### Return Value

According to the [Python documentation](https://docs.python.org/3/library/os.html#os.system):

> On Unix, the return value is the exit status of the process encoded in the format specified for [`wait()`](https://docs.python.org/3/library/os.html#os.wait).

and...

> On Windows, the return value is that returned by the system shell after running _command_.

💡 **Tip:** Note that this function does not return a list. It simply displays the list as standard output, so you can't store it in a variable like you did with `listdir`.

### Variations of the `ls` command

A key feature of `os.system('ls')` is that it has many helpful and interesting options to customize how present the output. Let's see some of them.

**Option 1:** We can show more information about files and directories such as their size, location, and modification date and time using the command `ls -l`.

```python
>>> import os
>>> os.system('ls -l')
total 12
drwxr-xr-x 1 runner runner  0 Apr  3 18:23 'Directory 1'
-rw-r--r-- 1 runner runner 11 Apr  3 18:38 'file 1.py'
-rw-r--r-- 1 runner runner 11 Apr  3 18:38 'file 2.py'
-rw-r--r-- 1 runner runner 11 Apr  3 18:38  main.py
0
```

**Option 2:** To be able to visually recognize directories faster, we can use `ls -F`, which adds a forward slash `/` to the end of their names (see `'Directory 1/'` below).

```python
>>> import os
>>> os.system('ls -F')
'Directory 1'/  'file 1.py'  'file 2.py'   main.py
0
```

**Option 3:** To sort the files by size, we can use the command `ls -lS`.

```python
>>> import os
>>> os.system('ls -lS')
total 12
-rw-r--r-- 1 runner runner 11 Apr  3 18:38 'file 1.py'
-rw-r--r-- 1 runner runner 11 Apr  3 18:38 'file 2.py'
-rw-r--r-- 1 runner runner 11 Apr  3 18:38  main.py
drwxr-xr-x 1 runner runner  0 Apr  3 18:23 'Directory 1'
0
```

There are many more options for customization that can be helpful for your particular goal. [Here you can find more information](https://en.wikipedia.org/wiki/Ls) about the `-ls` command and how you can use its full power.

## 🔸 Summary of listdir vs. system("ls")

* **Purpose:** `listdir` returns the list of file names and directories in the path specified (by default, the current working directory) while `system("ls")` only displays them as standard output.
* **Operating System:** `listdir` can be used independently of the operating system that you are working with. In contrast, `system('ls')` has to be executed in an operating system or environment that recognizes the `'ls'` command. 
* **Customization:** you can filter the list returned by `listdir` if you need to remove files or directories using the `filter()` function and you can pass options to customize the output of `system('ls')`.

**I really hope that you liked my article and found it helpful.** Now you can work with these functions in your Python projects. [Check out my online courses](https://www.udemy.com/user/estefania-cn/). Follow me on [Twitter](https://twitter.com/EstefaniaCassN). ⭐️

