---
title: How to Delete a File in Python – And Remove a Directory, Too
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-09T15:24:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-delete-a-file-in-python-and-remove-a-directory-too
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/12.-delete-files-directories.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Dillion Megida

  Python offers many standard utility modules which enable several functions in the
  applications we build. In this article, we''ll learn about the modules for deleting
  files and directories.

  One of the most popular modules exposed in P...'
---

By Dillion Megida

Python offers many standard utility modules which enable several functions in the applications we build. In this article, we'll learn about the modules for deleting files and directories.

One of the most popular modules exposed in Python is the `os` module. This is one of the standard utility modules. This module offers various functions for interacting with the operating system of a device. It allows us to work with files and directories.

Another module is `shutil` which is used for high-level file operations.

In this article, I'll be showing you how to use these modules in Python to delete files and remove directories. I'll be testing the examples here on my Mac device, but you can also test them on any other type of device you have with Python installed.

## Overview of the `os` Module

The `os` module allows us to execute operating system tasks on Windows, Mac, and Linux.

To use this module, you first have to import it:

```python
import os
```

This module has different properties and functions that we can use to access different information about the OS and to also run some file-related tasks.

For example, there's the `name` property which returns the name of the operating system module imported for the device you use the module on. On my Mac device, after running `python test.py` (where `test.py` is the file with my code) here's the result I get:

```python
import os

print(os.name)
# posix
```

There's also the `environ` object which contains all the environment variables and their values:

```python
import os

print(os.environ)
# {
#   ...
#   'SHELL': '/bin/zsh',
#   'HOMEBREW_REPOSITORY': '/opt/homebrew',
#   ...
#   'ZSH': '/Users/dillion/.oh-my-zsh',
#   'NVM_DIR': '/Users/dillion/.nvm',
#   'USER': 'dillion'
#   ...
# }
```

After running this on my device, I get a bunch of environment variables. I've listed a few above, and you can see the `SHELL`,`ZSH`, and `USER` variables.

To get the value of a specific variable, you can use the `get()` method. Here are some examples:

```python
import os

homeEnv = os.environ.get('HOME')
# /Users/dillion

shellEnv = os.environ.get('SHELL')
# /bin/zsh

zshEnv = os.environ.get('ZSH')
# /Users/dillion/.oh-my-zsh

userEnv = os.environ.get('USER')
# dillion
```

## Overview of the `shutil` Module

While the `os` module is more focused on operating system tasks (depending on the operating system in use), the `shutil` module is for high-level file operations from Python such as copying and removing files.

To use this module, you also have to import it first:

```python
import shutil
```

This module also has methods that you can use for file and directory operations. Let's see some examples.

There's the `move` directory, which allows you to move a file from one location to a destination. Here's a `test.py` example:

```python
import shutil

shutil.move("./test.py", "temp/")
```

When I run `python test.py`, the **test.py** file is moved to the **temp** directory. If the file or the directory does not exist, you get an error.

Another method of this module is `copytree`, which copies a directory's contents to a destination. Let's say we have a folder called **directory1/** with the following files:

```bash
directory1
├── file1.py
└── test
   └── file2.py
```

This directory has a file named **file1.py** and a directory called **test** which in turn contains a file named **file2.py**.

Now let's see how to move these files from **directory1** to a new directory called **directory2**:

```python
import shutil

shutil.copytree("directory1/", "directory2/")
```

When you run the code above, `directory2` is created, and the contents of `directory1` are copied to `directory2`.

Now that we've seen some examples, let's see how to delete a file and remove a directory.

## How to Delete a File in Python

The `os` module has a `remove()` method which allows you to remove (delete) a file. Such files are deleted permanently – not in the recycle bin. Here's an example:

```python
import os

os.remove('./temporary.txt')
```

This method accepts the file path argument, where you specify the location of the file you want to remove. If such a file does not exist, running the command above produces an error like this:

```bash
FileNotFoundError: [Errno 2] No such file or directory: './temporary.txt'
```

So let me first create the file. I'll do this on my command line like this:

```bash
touch temporary.txt
echo "new file" > temporary.txt
```

Now I have the **temporary.txt** file with the "new file" text. When I run my Python above, this file will be removed:

```bash
python test.py
#  file now deleted
```

Another way to improve your code is to first check if the file exists, before calling the `remove` method. You can do this using the `path.isfile()` method. Here's how:

```python
import os

fileExists = os.path.isfile('./temporary.txt')

if fileExists:
    os.remove('./temporary.txt')
```

First, we check if **temporary.txt** exists by calling the `isfile()` method on the `path` property of the `os` module. This method returns `True` or `False` depending on the existence of that file. You can then use an `if` statement to test the returned boolean before calling the `remove` method.

## How to Delete a Directory in Python

The `os` module also has the `rmdir` method which you can use to delete a folder. But, the folder has to be empty. Here's an example:

```python
import os

os.rmdir('directory1/')
```

If **directory1** exists and is empty, it will be deleted. If it does not exist, you get a **No such file or directory** error. If it exists but is not empty, you get a **Directory not empty** error. So how do you delete non-empty directories?

Remember I said `shutil` is for high-level file operations? Well, this is where it's also useful – for deleting empty and non-empty directories.

`shutil` has the `rmtree` method which is used for removing a directory (and all its contents such as files, sub-files, sub-directories, and so on).

Here's an example:

```python
import shutil

shutil.rmtree('directory2/')
```

If **directory2** does not exist, you get a **No such file or directory** error. But if the directory exists and is non-empty, it will be deleted. Even if it's empty, it will also be deleted.

## Wrapping Up

When building applications, sometimes you want to create, delete, modify, copy or perform other file operations. Thanks to some standard modules exposed from Python, these operations are possible.

In this article, I've shown you how to use the `os` and `shutil` standard modules from Python to delete files and directories on a device.



