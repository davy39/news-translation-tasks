---
title: How to edit PYTHONPATH on Windows
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-14T20:12:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-edit-pythonpath-on-windows-eafd19840d44
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iqGsyUGrUySN0awiYr3X8A.jpeg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: 'By Dalya Gartzman

  You are here because you are using:


  Windows OS version 10+

  Python version 3.3+

  Anaconda3


  And you would like to edit your PYTHONPATH permanently.

  TL;DR


  Go to C:\Users\<your_username>\Anaconda3\Lib\site-packages

  Create a file pytho...'
---

By Dalya Gartzman

You are here because you are using:

1. Windows OS version 10+
2. Python version 3.3+
3. Anaconda3

And you would like to edit your `PYTHONPATH` permanently.

### TL;DR

1. Go to `C:\Users\<your_username>\Anaconda3\Lib\site-pa`ckages
2. Create a file `python37.pth`
3. Edit the file to include this line `C:\\Users\\<your_username>\\my_`module

### The Long version; Do Read

#### Prologue

In most cases, editing the `PYTHONPATH` from the Settings GUI will do the trick. The trick is well explained in [this Stack Overflow answer](https://stackoverflow.com/a/4855685/2934048).  
If in the first place you are only looking to edit your path **locally**, [this helpful answer](https://stackoverflow.com/a/43072284/2934048) will do.

#### Slightly Extended Item no. 1

If you don’t have `C:\Users\<your_username>\Anaconda3\Lib\site-pa`ckages, re`place C:\Users\<your_`username> with the path to your Anaconda3.

#### Slightly Extended Item no. 2

If you are using Python3.7, create a file called `python37.pth`. Else create a file called `python<XX&g`t;.pth for whatever Python version you are using.

* Not sure which version?   
Under `C:\Users\<your_username>\Anac`onda3\ search for a file of the `form python&l`t;XX&g`t;.d`ll. The <XX> indicates the version number you nee`d fo`r naming your .pth file.
* Windows is super annoying and won’t let you create a file with a `.pth` suffix?   
There are such files in the `C:\Users\<your_username>\Anaconda3\Lib\site-pa`ckages folder. Copy one of them and edit the prefix.
* Some places say you need to create a `._pth` file instead of `.pth`?  
A `._pth` file will completely **replace** your existing path. While a `.pth` file will **append** its content to the path you already have. You can find more information [here](https://docs.python.org/3/using/windows.html#finding-modules).

#### Slightly Extended Item no. 3

Assuming the `SuperCoolClass` you wish to import is located at   
`C:\Users\<your_username>\my_project_folder\my_awesome_f`ile.py .

Then open your newly created `python<XX&g`t;.pth file with your favorite text editor (please don’t say it’s Vim) and add one `line:`  
`C:\\Users\\<your_username>\\my_pr`oject_folder.  
Yes, with those annoying dou`bl`e slashes \\ .  
No, wit`ho`ut quotes "" .

And that’s it.  
Now you can import from anywhere, like a normal person:  
`from my_awesome_file import SuperCoolClass` .

#### Epilogue

Nothing important to add here really.   
I just hope my 2 hours of frustration + 1 hour of writing this post saved you some time.  
Peace out.

![Image](https://cdn-media-1.freecodecamp.org/images/UJWkKhiuU7PpnxnwgE2nBm0DE3QLQABY6Bmh)

