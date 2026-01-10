---
title: Remove Directory in Linux – How to Delete a Folder from the Command Line
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-02-16T15:57:04.000Z'
originalURL: https://freecodecamp.org/news/remove-directory-in-linux-how-to-delete-a-folder-from-the-command-line
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Copy-of-Cast-a-Function-in-SQL---Convert-Char-to-Int-SQL-Server-Example.png
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: null
seo_desc: "Linux CLI is a powerful tool that can help you accomplish complex tasks.\
  \ \nOne of the common operations you'll need to perform is to delete things. Just\
  \ as like creating files and folders, deleting them from the Linux command line\
  \ is something you'll ..."
---

Linux CLI is a powerful tool that can help you accomplish complex tasks. 

One of the common operations you'll need to perform is to delete things. Just as like creating files and folders, deleting them from the Linux command line is something you'll do often. 

In this post, we will discuss how to delete directories from the command line. We will discuss the syntax along with some examples. I am using Ubuntu in these examples.

## Syntax of the Linux `rm` Command

You use the `rm` command to delete something from the command line in Linux. The syntax of the `rm` command looks like this:

```bash
rm [flags] directory name
```

Some important flags you'll need to use when deleting a directory are as follows:

*  `-r`, `-R`, `--recursive` ["Recursion"] – Removes directories and their contents recursively. 
* `-v`, `--verbose` ["Verbose"] – This option outputs the details of what is being done on the CLI.
* `-f`, `--force`["Force"] – This option ignores nonexistent files and never prompts you.
* `-i`["Interactive"] – Use this flag when you want to be prompted before every removal.
* `-d`["Directory] – This works only when the directory is empty.

⚠ Be careful when using the `rm` command️ and always make sure that any important data is backed up.

## How to identify a folder to remove

As we are discussing how to delete folders, we need to be pretty sure that we are actually deleting a folder. We can identify a folder/directory with the `d` flag in the first column. Notice that files have the first flag as `-`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-55.png)

## Examples of Linux `rm` command

In our current folder, we have 2 folders `CSharpLab` and `PythonLab`. Their content is shown below.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-48.png)

Note that `CSharpLab` is an empty directory.

### How to delete a folder that's not empty

Let's delete the `PythonLab` folder first.

```bash
rm -rvi PythonLab/
```

Where,

* `-r` recursively deletes all files and folders. Note in the output below, all files (`man.py, calculator.py, palindrome.py` ) and folders (`/lib` )  were removed.
* `-v` shares details.
* `-i` makes deletion interactive, which means it will ask before removing anything.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-53.png)

### How to delete an empty folder

Let's try to delete the `CSharpLab` folder. As this folder is empty, we can use the `-d` flag.

```bash
rm -d CSharpLab/
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-50.png)
_CSharpLab directory is removed_

### How to use the `-f` "force" flag 

Let's now see how the `-f` flag works. This forces the deletion of folders without any prompts or warnings. In case of an error, `-v` still ignores, and deletes the files that are valid.

In the example below, there is a typo in the folder name. Note that the typo is ignored. The original file is intact.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-51.png)

## Wrapping up

Removing directories is useful when you need to remove folders after archiving them, when deleting duplicates, when deleting unused folders, and much more. 

All these tasks are targeted at creating more disk space. I hope you found this blog helpful.

Let's connect on [Twitter](https://twitter.com/hira_zaira)!

Read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

Let's [chat on Discord.](https://discordapp.com/users/Zaira_H#2603)

