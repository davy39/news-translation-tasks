---
title: Python Read File – How to Open, Read, and Write to Files in Python
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-05-31T14:29:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-read-files-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/read-write-files-python--1-.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Reading and writing files is a common operation when working with any programming
  language. You can program your code to read data or instructions from a file and
  then write the data as well. This increases efficiency and reduces manual effort.

  Pytho...'
---

Reading and writing files is a common operation when working with any programming language. You can program your code to read data or instructions from a file and then write the data as well. This increases efficiency and reduces manual effort.

Python has a well-defined methodology for opening, reading, and writing files. Some applications for file manipulation in Python include: reading data for algorithm training and testing, reading files to create generative art, reporting, and reading configuration files.  

In this tutorial you will learn:

1. How to load files into the main memory and create a file handle.
2. How to use the file handle to open files for reading and writing.
3. Exception handling while working with files.

Pre-requisites:

* Ensure you have the latest Python version installed.
* Familiarity with any Python-supported text editor of your choice.
* Some familiarity with basic Python syntax.

To get quick access to Python IDE, do check out [Replit](https://replit.com/~). You can also clone [this](https://github.com/zairahira/read-files-python) repo and run it on Replit.

## Persistence and How to Load Files into the Main Memory

Files reside in the computer's secondary memory. Secondary memory is persistent, which means that data is not erased when a computer is powered off. Once you make changes to a file and save it, the changes are permanently written and saved in the secondary memory.

To work with files, we need to load them into the main memory first. Main memory is the temporary cache memory that holds requested data for a brief interval. The data is lost when the computer is powered off. 

![Files are loaded from secondary memory to the main memory and then processed by the CPU. Once the processing is done, the data is written back to the secondary memory.](https://www.freecodecamp.org/news/content/images/2022/05/image-175.png)
_Files are loaded from secondary memory to the main memory and then processed by the CPU. Once the processing is done, the data is written back to the secondary memory._

Python interacts with files loaded in the main memory through "**file handlers**". Let's look at file handlers in detail.

### How File Handlers Work

When we want to read or write a file, we must _open_ it first. Opening a file signals to the operating system to search for the file by its name and ensure that it exists. 

The OS returns a file handler if _open_ is successful. Then we can interact with our file through the file handler. 

The file handler does not contain the data itself, it just provides an interface for handling the file operations.

![A file handler provides your program access to data in the secondary memory.](https://www.freecodecamp.org/news/content/images/2022/05/image-176.png)
_A file handler provides your program access to data in the secondary memory._

### How to Open a File 

In this example, we will open the file `daffodils.txt`. Note that this file should be stored in the same folder as your Python program. You can download the file `daffodils.txt` from [this](https://github.com/zairahira/read-files-python/blob/main/daffodils.txt) GitHub link.

Do give the file a look as we will be working with its contents in our upcoming examples.

**Example:**

```python
fhand = open('daffodils.txt')
print(fhand)
```

In the example above, the OS will return the file handle in the variable `fhand` if _open_ is successful. By default, you can only read the file.

**Output:**

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-177.png)
_The output of a file handle._

In the output, we have received a file handle where `name` is the file name and `mode` is the permission which is `r` (stands for `read`) in our case. `encoding` is the encoding mechanism for the Unicode character set. You can learn more details about UTF-8 [here](https://www.freecodecamp.org/news/what-is-utf-8-character-encoding/).

**Exception:**

In case, the file does not exist, we get an exception like this:

![Exception when the file is not found.](https://www.freecodecamp.org/news/content/images/2022/05/image-178.png)
_Exception when the file is not found._

### How to Print the File

Now we have the file handle which means we can access the file. Let's print the file and see its contents.

**Example:**

```python
# Get the file handler
fhand = open('daffodils.txt')

# Loop through each line via file handler
for line in fhand:
  print(line) 

```

**Output:**

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-179.png)
_Printing the contents of a file._

We are able to access and print the file successfully. But, did you notice that we are getting extra blank lines between each line? There is an explanation for this. Let's see in the next section.

### How to Handle Extra Line Spaces

The new line character is represented in Python by `\n`. This character adds a new line when placed anywhere in a string.

There is a new line character at the end of each line which prints output to the next line. We can visualize it using the `repr` method.

According to the Python [documentation](https://docs.python.org/3/library/functions.html#repr), the `repr()` method returns a string containing a printable representation of an object. This means that we can see any special character like a `\t or a \n` that appears in a string.  

Let's run an example below and see the output.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-180.png)
_Representation of strings using `repr()`._

**Example:**

Back to our file, we can use `repr()` to check for the special characters.

```python
# Get the file handler
fhand = open('daffodils.txt')

# Loop through each line via file handler
for line in fhand:
  print(repr(line)) 

```

**Output:**

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-181.png)
_Here we can see what's going on behind the scenes._

Moreover, the print method adds a new line by default. This means that using print, we are getting another new line in the output. We can handle this extra line using two approaches.

#### Approach #1: Change the default end value of print

The snippet below shows the arguments for the `print` function. We can see that by default the value of `end` is `\n`. This means that every print statement will end with a `\n`. 

![image-22](https://www.freecodecamp.org/news/content/images/2022/03/image-22.png)
_Source: Python [documentation](https://docs.python.org/3/library/functions.html#:~:text=print(*objects%2C%20sep%3D%27%20%27%2C%20end%3D%27%5Cn%27%2C%20file%3Dsys.stdout%2C%20flush%3DFalse))._

We can change the default value `end='\n'` to a blank so that we do not get a new line at the end of each line. Let's see the example below to understand better.

```python
# By default output would go in separate lines
print("Hello")
print("World")

# Print on the same line because end = ' '
# added single space
print("Hello", end = ' ') 
print("World")

```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-182.png)
_Print on the same and different lines using `print()`._

Back to our main file, let's modify the code a bit to get the output without extra blank lines.

```python
# Get the file handler
fhand = open('daffodils.txt')

# Loop through each line and modify the default value of 'end'
for line in fhand:
  print(line, end = '')
```

**Output:**

And here we have our desired output!

![Print without extra lines using print().](https://www.freecodecamp.org/news/content/images/2022/05/image-183.png)
_Print without extra lines using `print()`._

#### Approach #2: Use the rstrip() method

We can remove certain characters around a string using the `strip()` method. 

By now we know that by default, every line in a file has `"\n"` at the end. As we are concerned with only the character on the right, we will use `rstrip()` which stands for right-strip. We'll discuss an example of `rstrip()` next.

You can learn more about the `strip()` method in this blog [post](https://www.freecodecamp.org/news/python-strip-how-to-trim-a-string-or-line/).

```python
# Get the file handler
fhand = open('daffodils.txt')

# Loop through each line and remove extra line character with rstrip()
for line in fhand:
  line = line.rstrip()
  print(line)

```

Output:

![Print without extra lines using rstrip().](https://www.freecodecamp.org/news/content/images/2022/05/image-184.png)
_Print without extra lines using rstrip`()`._

### How to Let the User Choose a File

Instead of hard coding a filename, we can make the code dynamic by letting the user choose a file. 

Let's ask the user to enter a filename. Then we will calculate the number of lines in the file.

**Example:**

```python
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
     count = count + 1
print('There are', count, 'lines in', fname)
```

**Output:**

![Request the user to enter the file name.](https://www.freecodecamp.org/news/content/images/2022/05/image-186.png)
_Request the user to enter the file name._

### How to Write a File in Python

By default, the file handler opens a file in the read mode. We can write to a file if we open the file with any of the following modes:

* `w`- (Write) writes to an existing file but erases existing content.
* `a`- (Append) appends to an existing file.
* `x` - (Create) creates a file and returns an error if the file exists. 

#### How to write to a file

Note that, if we try to open an already existing file with `w` flag, the contents are overwritten.

```
# Open file with mode 'w'
fout = open('flower.txt', 'w')
fout.write("This content would be added and existing would be discarded")
fout.close()


```

#### How to append to a file

The `a` flag appends to existing content and preserves the existing content.

```
# Open file with mode 'a'
fout = open('flower.txt', 'a')
fout.write("Now the file has more content at the end!")
fout.close()


```

#### How to create a file and write to it

The `x` mode creates a file and adds content to it. 

```
# Open file with mode 'x'
fout = open('new-file.txt', 'x')
fout.write("Now the new file has some content!")
fout.close()


```

If the file exists, we'll get an exception like this: 

```
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    fout = open('flower.txt', 'x')
FileExistsError: [Errno 17] File exists: 'flower.txt'
```

### Exception Handling

It is possible that the file we request does not exist. This blows up the program due to the exception:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-189.png)

In order to make the program more user friendly, we can handle this exception in a `try-except` block. 

The risky part of the program that is expected to blow up is written in a `try` block. In case the code executes without exception, the `except` block is skipped and the program continues to run. In case an exception is found, the `except` block runs and closes the program gracefully with the `exit` command.

```python
fname = input('Enter the file name: ')
try:
  fhand = open(fname)
except:
  print('File nout found and can not be opened:', fname)
  exit()
count=0
for line in fhand:
  count = count + 1
print('There are', count, 'lines in', fname)
```

**Output:**

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-188.png)
_Exception handling using a try-except block._

## Wrapping up

Knowing how to work with files is an essential concept in programming. In this tutorial, you learned how to open files for reading and writing in Python using file handlers. 

For reference, I have included all the code snippets and sample files in [this](https://github.com/zairahira/read-files-python) GitHub repo.

I hope you found this tutorial helpful.

What’s your favorite thing you learned from this tutorial? Let me know on [Twitter](https://twitter.com/hira_zaira)!

You can also read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

Banner credits:

* [Php vector created by svstudioart - www.freepik.com](https://www.freepik.com/vectors/php)
* [Website theme vector created by freepik - www.freepik.com](https://www.freepik.com/vectors/website-theme)

