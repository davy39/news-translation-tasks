---
title: Creating a Directory in Python – How to Create a Folder
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-03-23T13:39:03.000Z'
originalURL: https://freecodecamp.org/news/creating-a-directory-in-python-how-to-create-a-folder
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-pixabay-51191.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In this article, you will learn how to create new directories (which is\
  \ another name for folders) in Python. \nYou will also learn how to create a nested\
  \ directory structure. \nTo work with directories in Python, you first need to include\
  \ the os  modul..."
---

In this article, you will learn how to create new directories (which is another name for folders) in Python. 

You will also learn how to create a nested directory structure. 

To work with directories in Python, you first need to include the `os`  module in your project, which allows you to interact with your operating system.

The `os` module also lets you use the two methods we will cover in this article:

- the `os.mkdir()` method
- the `os.makedirs()` method

Let’s get into it!


## How To Create A Single Directory Using The `os.mkdir()` Method in Python
As mentioned earlier, to work with directories in Python, you first need to include the `os` module.

To do so, add the following line of code to the top of your file:

```python
import os
```

The code above will allow you to use the `os.mkdir()` method to create a new single directory.

The `os.mkdir()` method accepts one argument – the path for the directory.

```python
import os

# specify the path for the directory – make sure to surround it with quotation marks
path = './projects'

# create new single directory
os.mkdir(path)
```

The code above will create a  `projects` directory in the current working directory.

Note that the `./` stands for the current working directory. You can omit this part and only write `projects` when specifying the path – the result will be the same!


### How to Handle Exceptions When Using the `os.mkdir` Method in Python
But what happens when the directory you are trying to create already exists?  A `FileExistsError` exception is raised:

```
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    os.mkdir(path)
FileExistsError: [Errno 17] File exists: './projects'
```

One way to handle this exception is to check if the file already exists using an `if..else` block:

```python
import os

path = './projects'

# check whether directory already exists
if not os.path.exists(path):
  os.mkdir(path)
  print("Folder %s created!" % path)
else:
  print("Folder %s already exists" % path)
```

In the example above, I first checked whether the `./projects` directory already exists using the `os.path.exists()` method. 

If it does, I will get the following output instead of a `FileExistsError`:

```
Folder ./projects already exists
```

If the file doesn't exist, then a new `projects` folder gets created in the current working directory, and I get the following output:

```
Folder ./projects created!
```

Alternatively, you can use a `try/except` block to handle exceptions:

```python
import os

path = './projects'

try:
    os.mkdir(path)
    print("Folder %s created!" % path)
except FileExistsError:
    print("Folder %s already exists" % path)
```

If a `projects` folder already exists in the current working directory, you will get the following output instead of an error message:

```
Folder ./projects already exists
```


## How To Create A Directory With Subdirectories Using The `os.makedirs()` Method in Python
The `os.mkdir()` method does not let you create a subdirectory. Instead, it lets you create a single directory.

To create a nested directory structure (such as a directory inside another directory), use the `os.makedirs()` method.
 
The `os.makedirs()` accepts one argument – the entire folder path you want to create.

```python
import os

# define the name of the directory with its subdirectories
path = './projects/games/game01'

os.makedirs(path)
```

In the example above, I created a `projects` directory in the current working directory.

Inside projects, I created another directory, `games`. And inside `games`, I created yet another directory, `games01`.


## Conclusion
And there you have it! You now know how to create a single directory and a directory with subdirectories in Python.

To learn more about Python, check out freeCodeCamp's [Python for beginners course](https://www.freecodecamp.org/news/python-programming-course/).

Thanks for reading, and happy coding!


