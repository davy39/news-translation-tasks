---
title: How to Save and Exit Nano in Terminal – Nano Quit Command
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-26T16:57:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-save-and-exit-nano-in-terminal-nano-quit-command
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/nano.png
tags:
- name: editor
  slug: editor
- name: Linux
  slug: linux
- name: nano
  slug: nano
seo_title: null
seo_desc: "Nano is a command line-based code editor known for its simplicity compared\
  \ to other editors like Vim and Emacs.\nBut if you are new to Nano, performing basic\
  \ operations like creating files, saving the file, and exiting the editor might\
  \ be confusing. \n..."
---

Nano is a command line-based code editor known for its simplicity compared to other editors like Vim and Emacs.

But if you are new to Nano, performing basic operations like creating files, saving the file, and exiting the editor might be confusing. 

So, in this article, I want to show you how to save your code in Nano and exit it as well.

I’ll be using the Windows Subsystem for Linux (WSL) in this article. But it’s fine if you’re on Linux itself. The commands are the same.

## What We'll Cover
- [How to Save a File in Nano](#heading-how-to-save-a-file-in-nano)
- [How to Exit Nano](#heading-how-to-exit-nano)
- [Wrapping Up](#heading-wrapping-up)


## How to Save a File in Nano
**Step 1**: Open WSL, type “nano” and hit `ENTER` to get into the Nano code editor
![ss1-4](https://www.freecodecamp.org/news/content/images/2022/07/ss1-4.png) 

**Step 2:** Write your code in any language. In the screenshot below, I wrote some PHP.
![ss2-5](https://www.freecodecamp.org/news/content/images/2022/07/ss2-5.png) 

**NB:** If you don’t get syntax highlighting, enable it by pressing `ALT` + `4`. If you still don’t get syntax highlighting, then you need to save the file.

**Step 3:** Press `CTRL` + `O` to save the file, type the file name, and hit `ENTER`.
![ss3-4](https://www.freecodecamp.org/news/content/images/2022/07/ss3-4.png) 

Now, syntax highlighting is enabled:
![ss4-4](https://www.freecodecamp.org/news/content/images/2022/07/ss4-4.png) 

If you already opened the file by typing `nano file_name` in WSL… 

When you are done making your changes, press `CTRL + O` and hit `ENTER` to save the changes.
![save-exit-nano](https://www.freecodecamp.org/news/content/images/2022/07/save-exit-nano.gif) 

## How to Exit Nano
To exit nano, all you need to do is to press `CTRL` + `X`.
![ss5-5](https://www.freecodecamp.org/news/content/images/2022/07/ss5-5.png) 

If you have any changes that have not been saved, you’ll be prompted to save the changes before you quit the editor.
![save-nano](https://www.freecodecamp.org/news/content/images/2022/07/save-nano.gif)

## Wrapping Up
I hope this article helped you learn how to save a file in Nano and exit the editor whenever you want to.

Don’t forget:
- Typing `nano` gets you into the Nano editor in WSL
- `CTRL` + `O` saves a Nano file
- `CTRL` + `X` exits Nano

Thank you for reading. If you find the article helpful, don’t hesitate to share it with your friends and family.


