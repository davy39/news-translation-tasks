---
title: Python Copy File – Copying Files to Another Directory
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-04-20T14:16:43.000Z'
originalURL: https://freecodecamp.org/news/python-copy-file-copying-files-to-another-directory
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/maksym-kaharlytskyi-Q9y3LRuuxmg-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'When working with Python, there may be times when you need to copy a file.
  Copying files comes in handy when you need to create a backup.

  In this article, you will learn how to copy a file in Python using the shutil module
  and its different methods.

  ...'
---

When working with Python, there may be times when you need to copy a file. Copying files comes in handy when you need to create a backup.

In this article, you will learn how to copy a file in Python using the `shutil` module and its different methods.

The `shutil` (short for shell utility) module in Python lets you manipulate files and directories and perform file and directory operations.

Let's get into it!


## How To Copy A File Using The `shutil.copyfile()` Method In Python
To copy the contents of a file into another file, use the `shutil.copyfile()` method.

Let's look at the following example:

```python
# import module
import shutil

# copy the contents of the demo.py file to  a new file called demo1.py
shutil.copyfile('./demo.py', './demo1.py')
```

I first import the module with the `import shutil` statement.

Then, I use the `shutil.copyfile()` method which has the following syntax:

```python
shutil.copyfile('source_file', 'destination_file')
```

Let's break it down:

- `source_file` is the path to the file I want to copy – in this case, the file is the `demo.py` file in my current working directory (`./`).
- `destination_file` is the path to the new file I want to create. In this case, I want to copy the contents of the source file into a new file, `demo1.py`, in my current working directory. The destination cannot be a directory – it must be a file name.

When I run the code from the example above, a new file named `demo1.py` gets created in my current working directory with a copy of `demo.py`'s contents. If the destination file already exists, it gets replaced.

Note that the `shutil.copyfile()` method only copies the contents of the source file.  

No file metadata (such as creation dates and modification times) or file permissions are copied over to the specified destination file. 

So, the `shutil.copyfile()` method is useful when you want to rename the file you are copying and are not concerned about saving file permissions and metadata.


## How To Copy A File Using `shutil.copy()` Method In Python
To copy a file to another directory, use the `shutil.copy()` method.

Let’s look at the following example:

```python
# import the module
import shutil

# Specify the path of the file you want to copy
file_to_copy = './demo.py'

# Specify the path of the destination directory you want to copy to
destination_directory = './projects'

# Use the shutil.copy() method to copy the file to the destination directory
shutil.copy(file_to_copy, destination_directory)
```

I first import the module using the `import shutil` statement.

Then, I specify the path of the file I want to copy and save it in a variable named `file_to_copy`. In this case, I want to copy the `demo.py` file in my current working directory.

Next, I specify the directory I want to copy the file and save it in a variable named `destination_directory`. In this case, I want to save the file in the `projects` directory in my current working directory.

Lastly, I use the `shutil.copy()` method which takes two arguments: 

- The path of the file you want to copy – in this case, the variable `file_to_copy`.
- The file or directory you want to copy the file into – in this case,  the variable `destination_directory`.

When I run the code from the example above, the `shutil.copy()` method creates a copy of the `demo.py` file in the `projects` directory.

Keep in mind that if a file with the same name already exists in the destination directory, the existing file gets overwritten by the new file.

Another thing to keep in mind is that the `shutil.copy()` method copies file permissions, but it doesn’t copy metadata over to the destination directory.


## How To Copy A File Using The `shutil.copy2()` Method In Python
The `shutil.copy2()` method works similarly to the `shutil.copy()` method. 

The only difference between `shutil.copy()` and `shutil.copy2()` method is that `shutil.copy2()` preserves the original file metadata when copying.

```python
# import the module
import shutil

# Specify the path of the file you want to copy
file_to_copy = './demo.py'

# Specify the path of the destination directory you want to copy the file into
destination_directory = './projects'

# Use the shutil.copy2() method to copy the file to the destination directory
shutil.copy2(file_to_copy, destination_directory)
```


## How To Copy A File Using The `shutil.copyfileobj()` Method In Python
To copy the contents of a file object to another specified destination file object, use the `shutil.copyfileobj()` method. This method takes two file objects as arguments – a source file object and a destination file object. The destination cannot be a directory.

Let's take the following example:

```python
# import module
import shutil

# you have to open the source  file in binary mode with 'rb'
source_file =  open('demo.py', 'rb')

# you have to open the destination file in binary mode with 'wb'
destination_file = open('project.py', 'wb')

# use the shutil.copyobj() method to copy the contents of source_file to destination_file
shutil.copyfileobj(source_file, destination_file)
```

In the example above, the `shutil.copyobj()` method copies the contents of `demo.py` to the `project.py` file.

Keep in mind that this method does not preserve file permissions and it doesn't copy metadata.


## Conclusion
And there you have it! You now know how to copy files in Python using the `shutil` module and the methods it offers.

To help you choose which method to use, refer to the following table that summarises what each method does.

| Method  | Preserves permissions?  | Copies metadata?  | Can destination be a directory?  | Accepts file object?
|---|---|---|---|---|
| `shutil.copyfile()`  |  No | No  | No  | No |
|  `shutil.copy()` | Yes  | No  | Yes  | No |
| `shutil.copy2()`  | Yes  | Yes  | Yes  | No|
| `shutil.copyfileobj()`  |  No | No  | No  | Yes |


To learn more about Python, check out freeCodeCamp's [Python for beginners course](https://www.freecodecamp.org/news/python-programming-course/).

Thanks for reading, and happy coding!


