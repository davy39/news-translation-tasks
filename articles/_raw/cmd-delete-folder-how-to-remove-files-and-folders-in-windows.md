---
title: cmd Delete Folder – How to Remove Files and Folders in Windows
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-11-13T04:35:00.000Z'
originalURL: https://freecodecamp.org/news/cmd-delete-folder-how-to-remove-files-and-folders-in-windows
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fc9bc71e6787e098393991d.jpg
tags:
- name: command
  slug: command
- name: command line
  slug: command-line
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: 'Sometimes it''s just faster to do things with the command line.

  In this quick tutorial we''ll go over how to open Command Prompt, some basic commands
  and flags, and how to delete files and folders in Command Prompt.

  If you''re already familiar with basi...'
---

Sometimes it's just faster to do things with the command line.

In this quick tutorial we'll go over how to open Command Prompt, some basic commands and flags, and how to delete files and folders in Command Prompt.

If you're already familiar with basic DOS commands, feel free to [skip ahead](#how-to-delete-files-with-the-del-command).

## How to open Command Prompt

To open Command Prompt, press the Windows key, and type in "cmd". 

Then, click on "Run as Administrator":

![Screenshot showing how to open Command Prompt as an administrator](https://www.freecodecamp.org/news/content/images/2020/12/run-command-prompt-as-administrator.jpg)

After that, you'll see a Command Prompt window with administrative privileges:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/command-prompt-new-window.jpg)
_Screenshot of Command Prompt window_

If you can't open Command Prompt as an administrator, no worries. You can open a normal Command Prompt window by clicking "Open" instead of "Run as Administrator".

The only difference is that you may not be able to delete some protected files, which shouldn't be a problem in most cases.

## How to delete files with the `del` command

Now that Command Prompt is open, use `cd` to change directories to where your files are.

I've prepared a directory on the desktop called Test Folder. You can use the command `tree /f` to see a, well, tree, of all the nested files and folders:

![Screenshot after running tree /f in target directory](https://www.freecodecamp.org/news/content/images/2020/12/command-prompt-tree.jpg)

To delete a file, use the following command: `del "<filename>"`.

For example, to delete `Test file.txt`, just run `del "Test File.txt"`. 

There may be a prompt asking if you want to delete the file. If so, type "y" and hit enter.

**Note:** Any files deleted with the `del` command cannot be recovered. Be very careful where and how you use this command.

After that, you can run `tree /f` to confirm that your file was deleted:

![Screenshot after deleting file with del command](https://www.freecodecamp.org/news/content/images/2020/12/del-tree-check.jpg)

Also, bonus tip – Command Prompt has basic autocompletion. So you could just type in `del test`, press the tab key, and Command Prompt will change it to `del "Test File.txt"`.

### How to force delete files with the `del` command

Sometimes files are marked as read only, and you'll see the following error when you try to use the `del` command:

![Screenshot of error after trying to delete a read only file](https://www.freecodecamp.org/news/content/images/2020/12/read-only-error.jpg)

To get around this, use the `/f` flag to force delete the file. For example, `del /f "Read Only Test File.txt"`:

![Screenshot after deleting file with the force flag](https://www.freecodecamp.org/news/content/images/2020/12/del-force-flag.jpg)

## How to delete folders with the `rmdir` command

To delete directories/folders, you'll need to use the `rmdir` or `rd` command. Both commands work the same way, but let's stick with `rmdir` since it's a bit more expressive.

Also, I'll use the terms directory and folder interchangeably for the rest of the tutorial. "Folder" is a newer term that became popular with early desktop GUIs, but folder and directory basically mean the same thing.

To remove a directory, just use the command `rmdir <directory name>`.

**Note:** Any directories deleted with the `rmdir` command cannot be recovered. Be very careful where and how you use this command.

In this case I want to remove a directory named Subfolder, so I'll use the command `rmdir Subfolder`:

![Screenshot of a directory not empty error](https://www.freecodecamp.org/news/content/images/2020/12/directory-not-empty.jpg)

But, if you remember earlier, Subfolder has a file in it named Nested Test File.

You could `cd` into the Subfolder directory and remove the file, then come back with `cd ..` and run the `rmdir Subfolder` command again, but that would get tedious. And just imagine if there were a bunch of other nested files and directories!

Like with the `del` command, there's a helpful flag we can use to make things much faster and easier.

### How to use the `/s` flag with `rmdir`

To remove a directory, including all nested files and subdirectories, just use the `/s` flag:

![Screenshot after running rmdir with the /s flag](https://www.freecodecamp.org/news/content/images/2020/12/rmdir-s-flag.jpg)

There will probably be a prompt asking if you want to remove that directory. If so, just type "y" and hit enter.

And that's it! That should be everything you need to know to remove files and folders in the Windows Command Prompt.

All of these commands should work in PowerShell, which is basically Command Prompt version 2.0. Also, PowerShell has a bunch of cool aliases like `ls` and `clear` that should feel right at home if you're familiar with the Mac/Linux command line.

Did these commands help you? Are there any other commands that you find useful? Either way, let me know over on Twitter.

