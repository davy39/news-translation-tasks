---
title: Remove a Directory in Linux – How to Remove folders from the Command Line
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-09-07T18:18:33.000Z'
originalURL: https://freecodecamp.org/news/remove-directory-in-linux-from-the-command-line
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Copy-of-read-write-files-python--2-.png
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: null
seo_desc: "Linux is a powerful OS with various command line utilities to help you\
  \ achieve your day-to-day tasks.\nRemoving folders is a very common operation that\
  \ allows you to either remove a single folder or remove them recursively (folders\
  \ within folders). \nI..."
---

Linux is a powerful OS with various command line utilities to help you achieve your day-to-day tasks.

Removing folders is a very common operation that allows you to either remove a single folder or remove them recursively (folders within folders). 

In this tutorial, we will see how we can delete folders from the command line.  

### But isn't the GUI enough to delete folders?

It is very simple to delete folders from the file explorer. All we need is to either use the delete button on the keyboard or right-click and delete the folder. But you can be more creative with the CLI (Command Line interface). 

With the command line, you can create a script to remove files periodically. You can also remove files that match certain criteria such as modification time or size.

Housekeeping scripts also make use of commands to delete unwanted folders to keep disk space at an optimal level. 

In short, you can automate your daily tasks using the command line.

Use caution when removing from the CLI. Once you delete a folder using the CLI, it is permanently deleted as there is no Recycle bin. The only way to recover is through a backup.

## How to Delete an Empty Folder using `rmdir`

You use the `rmdir` command to delete an empty directory. It doesn't work on non-empty directories.

**Syntax of the `rmdir` command:**

```bash
rmdir [OPTION] DIRECTORY_NAME
```

We can supply the following options:

* `-v` : displays the detailed output for every directory processed.
* `--ignore-fail-on-non-empty`: ignores if the directory is non-empty.
* `-p, --parents`: removes a directory and its ancestors. For example, `'rmdir -p a/b/c` would first remove the folder `c`, then `b` and then `a`

## How to Delete a Non-Empty Folder using `rm`

We can not use `rmdir` on non-empty folders. We have another command for that – `rm`. 

**Syntax of the `rm` command:**

```bash
 rm [OPTION] [FILE]
```

We can use the following options:

* `-r`, `-R`, `--recursive`: removes directories and their contents recursively.
* `-d`, `--dir`: removes empty directories. So we can also use `rm` to remove empty directories like the `rmdir` command.
* `-v`, `--verbose`: explains what is being done by mentioning the folder details being processed.
* `-i`: prompts before every removal.

So, the command to delete a non-empty folder would be:

```
rm -r folder-name
```

## How to Force Delete Directories

If you do not have `write` permissions, you are unable to delete the folder. If you wish to delete it anyways, use the `-f` flag. The `-f` flag doesn't display any prompts. 

## How to Safely Delete Folders in Linux

To prevent accidental deletion, use the `-i` interactive flag. This way you'll be prompted before deleting a folder and the contents inside it. 

If you want to proceed, just answer the prompts by entering `y`. On the other hand, enter `n` to skip the file.

In the example below, note how we descend into the folder and check each file one by one.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-309.png)
_Interactively deleting a folder named `find-test`_

## Conclusion

Removing directories is useful when you need to remove folders after archiving them, when deleting duplicates, when deleting unused folders, and much more.

All these tasks are targeted at creating more disk space. I hope you found this tutorial helpful.

What’s your favorite thing you learned here? Let me know on [Twitter](https://twitter.com/hira_zaira)!

Read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

