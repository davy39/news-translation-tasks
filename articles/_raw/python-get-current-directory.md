---
title: Python Get Current Directory – Print Working Directory PWD Equivalent
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-03-28T16:27:30.000Z'
originalURL: https://freecodecamp.org/news/python-get-current-directory
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-pixabay-357514.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'In this article, you will learn how to get the current working directory
  (another name for folder) in Python, which is the equivalent of using the pwd command.

  There are a couple of ways to get the current working directory in Python:


  By using the o...'
---

In this article, you will learn how to get the current working directory (another name for folder) in Python, which is the equivalent of using the `pwd` command.

There are a couple of ways to get the current working directory in Python:

- By using the `os` module and the `os.getcwd()` method.
- By using the `pathlib` module and the `Path.cwd()` method.

Let's get started!


## How to Get The Current Directory Using the `os.getcwd()` Method in Python
The `os` module, which is part of the standard Python library (also known as stdlib), allows you to access and interact with your operating system.

To use the `os` module in your project, you need to include the following line at the top of your Python file:

```
import os
```

Once you have imported the `os` module, you have access to the `os.getcwd()` method, which allows you to get the full path of the current working directory. 

Let's look at the following example:

```python
import os

# get the current working directory
current_working_directory = os.getcwd()

# print output to the console
print(current_working_directory)

# output will look something similar to this on a macOS system
# /Users/dionysialemonaki/Documents/my-projects/python-project
```

The output is a string that contains the absolute path to the current working directory – in this case, `python-project`. 

To check the data type of the output, use the `type()` function like so:

```python
print(type(current_working_directory))

# output

# <class 'str'>
```

Note that the current working directory doesn't have a trailing forward slash, `/`.

Keep in mind also that output will vary depending on the directory you are running the Python script from as well as your Operating System.


## How to Get The Current Directory Using the `Path.cwd()` Method in Python
In the previous section, you saw how to use the `os` module to get the current working directory. However, you can use the `pathlib` module to achieve the same result.

The `pathlib` module was introduced in the standard library in Python's 3.4 version and offers an object-oriented way to work with filesystem paths and handle files.

To use the `pathlib` module, you first need to import it at the top of your Python file:

```python
from pathlib import Path
```

Once you have imported the `pathlib` module, you can use the `Path.cwd()` class method, which allows you to get the current working directory.

Let's look at the following example:

```python
from pathlib import Path

# get the current working directory
current_working_directory = Path.cwd()

# print output to the console
print(current_working_directory)

# output will look something similar to this on a macOS system
# /Users/dionysialemonaki/Documents/my-projects/python-project
```

As you can see, the output is the same as the output I got when I used the `os.getcwd()` method. The only difference is the data type of the output:

```
print(type(current_working_directory))

# output

# <class 'pathlib.PosixPath'>
```


## Conclusion
And there you have it! You now know how to get the full path to the current directory in Python using both the `os` and `pathlib` modules.

To learn more about Python, check out [freeCodeCamp's Python for beginners course](https://www.freecodecamp.org/news/python-programming-course/).

Thanks for reading, and happy coding!


