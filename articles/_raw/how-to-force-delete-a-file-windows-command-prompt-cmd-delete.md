---
title: How to Force Delete a File – Windows Command Prompt cmd delete
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-04-08T07:11:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-force-delete-a-file-windows-command-prompt-cmd-delete
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/trash-97586_1280.png
tags:
- name: command line
  slug: command-line
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: 'On a Windows computer, you might want to delete files to free up disk space,
  or because you don''t want the file(s) on your computer anymore.

  But sometimes, it seems impossible to delete a file for various reasons. These include
  the file being open in...'
---

On a Windows computer, you might want to delete files to free up disk space, or because you don't want the file(s) on your computer anymore.

But sometimes, it seems impossible to delete a file for various reasons. These include the file being open in another program, lack of write access, a malware attack, a corrupt or out of space Recycle Bin, the file is a system file, and many others.

In this article, I will show you how to force delete a file with the command prompt so you can get rid of a stubborn, unwanted file.

## How to Force Delete a File With the Windows Command Prompt

The following steps will help you force delete a file with the `del` command.

**Step 1**: Open the Command Prompt by clicking on Start (or by hitting the Windows logo key on your keyboard), searching for "cmd", then hitting `Enter`:

![openCMD](https://www.freecodecamp.org/news/content/images/2022/04/openCMD.jpg)
 
**Step 2**: Head over to the folder containing the file, click on the folder address bar, and copy the address:

![ss1](https://www.freecodecamp.org/news/content/images/2022/04/ss1.png)

**Step 3**: In the Command Prompt, type `del`, right-click to the paste in the folder address, and append the filename with its extension (`.html`, `.txt`, `.py`, and so on).

This will look similar to `del C:\Users\user\folder-name\filename.extension`:

![ss2](https://www.freecodecamp.org/news/content/images/2022/04/ss2.png)

**Step 4**: Hit `ENTER` to run the command. Then check the folder again and you shouldn't see the file anymore:

![ss3](https://www.freecodecamp.org/news/content/images/2022/04/ss3.png)

## Conclusion

The `del` command will delete a file even if it's open in another program, with the exception of Office programs like MS Word.

So if you still find it hard to force delete a file, make sure it's not open in another program, especially an Office program.
	
Thank you for reading.


