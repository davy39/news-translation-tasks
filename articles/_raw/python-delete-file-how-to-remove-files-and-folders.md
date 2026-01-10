---
title: Python Delete File – How to Remove Files and Folders
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-13T12:24:56.000Z'
originalURL: https://freecodecamp.org/news/python-delete-file-how-to-remove-files-and-folders
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pyDeleteFilesAndFolders.png
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: null
seo_desc: 'Many programming languages have built-in functionalities for working with
  files and folders. As a rich programming language with many exciting functionalities
  built into it, Python is not an exception to that.

  Python has the OS and Pathlib modules wi...'
---

Many programming languages have built-in functionalities for working with files and folders. As a rich programming language with many exciting functionalities built into it, Python is not an exception to that.

Python has the `OS` and `Pathlib` modules with which you can create files and folders, edit files and folders, read the content of a file, and delete files and folders.

In this article, I’ll show you how to delete files and folders with the `OS` module.


## What We'll Cover
- [How to Delete Files with the `OS` Module](#heading-how-to-delete-files-with-the-os-module)
- [How to Delete Files with the `Pathlib` Module](#heading-how-to-delete-files-with-the-pathlib-module)
- [How to Delete Empty Folders with the `OS` Module](#heading-how-to-delete-empty-folders-with-the-os-module)
- [How to Delete Empty Folders with the `Pathlib` Module](#heading-how-to-delete-empty-folders-with-the-pathlib-module)
- [How to Delete a Non-Empty with the `shutil` Module](#heading-how-to-delete-a-non-empty-with-the-shutil-module)
- [Conclusion](#heading-how-to-delete-a-non-empty-with-the-shutil-module)

## How to Delete Files with the `OS` Module
To delete any file with the `OS` module, you can use it's `remove()` method. You then need to specify the path to the particular file inside the `remove()` method. But first, you need to bring in the `OS` module by importing it:

```py
import os

os.remove('path-to-file')
```

This code removes the file `questions.py` in the current folder:

```py
import os

os.remove('questions.py')
```

If the file is inside another folder, you need to specify the full path including the file name, not just the file name:

```py
import os

os.remove('folder/filename.extension')
```

The code below shows how I removed the file `faq.txt` inside the `textFiles` folder:
```py
import os

os.remove('textFiles/faq.txt')
```

To make things better, you can check if the file exists first before removing it:

```py
import os

# Extract the file path to a variable
file_path = 'textFiles/faq.txt'

#check if the file exists with path.exists()
if os.path.exists(file_path):
    os.remove('textFiles/faq.txt')
    print('file deleted')
else:
    print("File does not exists")
```

You can also use `try..except` for the same purpose:

```py
import os

try:
    os.remove('textFiles/faq.txt')
    print('file deleted')
except:
    print("File doesn't exist")
```


## How to Delete Files with the `Pathlib` Module
The `pathlib` module is a module in Python's standard library that provides you with an object-oriented approach to working with file system paths. You can also use it to work with files.

The pathlib module has an `unlink()` method you can use to remove a file. You need to get the path to the file with `pathlib.Path()`, then call the `unlink()` method on the file path:

```py
import pathlib

# get the file path
try:
    file_path = pathlib.Path('textFiles/questions.txt')
    file_path.unlink()
    print('file deleted')
except:
    print("File doesn't exist")
```


## How to Delete Empty Folders with the `OS` Module
The `OS` module provides a `rmdir()` method with which you can delete a folder.

But the way you delete an empty folder is not the same way you delete a folder with files or subfolders in it. Let’s see how you can delete empty folders first. 

Here’s how I deleted an empty `client` folder:

```py
import os

try:
    os.rmdir('client')
    print('Folder deleted')
except:
    print("Folder doesn't exist")
```

If you attempt to delete a folder that has files or subfolders inside it, you’ll get the `Directory not empty error`:

```py
import os

os.rmdir('textFiles') # OSError: [Errno 66] Directory not empty: 'textFiles'
```


## How to Delete Empty Folders with the `Pathlib` Module
With the `pathlib` module, you can extract the path of the folder you want to delete into a variable and call `rmdir()` on that variable:

```py
import pathlib

# get the folder path
try:
    folder_path = pathlib.Path('docs')
    folder_path.rmdir()
    print('Folder deleted')
except:
    print("Folder doesn't exist")
```

To delete a folder that has subfolders and files in it, you have to delete all the files first, then call `os.rmdir()` or `path.rmdir()` on the now empty folder. But instead of doing that, you can use the `shutil` module. I will show you this soon.


## How to Delete a Non-Empty with the `shutil` Module
The `shutil` module has a `rmtree()` method you can use to remove a folder and its content – even if it contains multiple files and subfolders.

The first thing you need to do is to extract the path to the folder into a variable, then call `rmtree()` on that variable.

Here’s how I deleted a folder named `subTexts` inside the `textFiles` folder:

```py
import shutil

try:
    folder_path = 'textFiles/subTexts'
    shutil.rmtree(folder_path)
    print('Folder and its content removed')
except:
    print('Folder not deleted')
```

And here’s how I removed the whole `textFiles` folder (it has several files and a subfolder):

```py
import shutil

try:
    folder_path = 'textFiles'
    shutil.rmtree(folder_path)
    print('Folder and its content removed') # Folder and its content removed
except:
    print('Folder not deleted')
```


## Conclusion
This article took you through how to remove a file and empty folder with the `os` and `pathlib` modules of Python. Because you might also need to remove non-empty folders too, we took a look at how you can do it with the `shutil` module.

If you found the article helpful, don’t hesitate to share it with your friends and family.



