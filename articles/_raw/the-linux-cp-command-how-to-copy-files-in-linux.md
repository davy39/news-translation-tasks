---
title: The Linux cp Command – How to Copy Files in Linux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-06T16:06:41.000Z'
originalURL: https://freecodecamp.org/news/the-linux-cp-command-how-to-copy-files-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/linux-cp-command.png
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'By Dillion Megida

  There are a couple different ways to copy and paste content when you''re working
  on your computer.

  If you spend more time in the user interface of your device, you''ll probably use
  your mouse to do this. You can copy files by right-cl...'
---

By Dillion Megida

There are a couple different ways to copy and paste content when you're working on your computer.

If you spend more time in the user interface of your device, you'll probably use your mouse to do this. You can copy files by right-clicking on the file and selecting "Copy", then going to a different directory and selecting "Paste".

For my terminal friends, you can also perform file copy-paste operations without leaving the terminal. In a Linux-based terminal, you do this using the `cp` command.

In this article, I'll explain what the `cp` command is and show you how to copy and paste files and directories in Linux using the terminal.

## What is the `cp` command?

You use the `cp` command for copying files from one location to another. This command can also copy directories (folders).

The syntax of this command is:

```bash
cp [...file/directory-sources] [destination]
```

`[file/directory-sources]` specifies the sources of the files or directories you want to copy. And the `[destination]` argument specifies the location you want to copy the file to.

To understand the rest of this article, I will use this folder structure example. Let's say a directory called **DirectoryA** has two directories in it: **DirectoryA_1** and **DirectoryA_2**. These subdirectories have many files and sub directories in them.

I'll also assume you're currently in the **DirectoryA** location in the terminal, so if you aren't, make sure you are:

```bash
cd DirectoryA
```

## How to copy files with the `cp` command

If you want to copy a file, say **README.txt** from **DirectoryA_1** to **DirectoryA_2**, you will use the `cp` command like this:

```bash
cp ./DirectoryA_1/README.txt ./DirectoryA_2
# ./DirectoryA_1/README.txt is the source file
# ./DirectoryA_2 is the destination
```

If you want to copy more than a file from **DirectoryA_1** to **DirectoryA_2**, you will use the `cp` command like this:

```bash
cp ./DirectoryA_1/README.txt ./DirectoryA_1/ANOTHER_FILE.txt ./DirectoryA_2
```

As you can see, you will put all the source files first, and the last argument will be the destination.

## How to copy directories with the `cp` command

By default, the `cp` command works with files. So if you attempt to copy a directory like this:

```bash
cp ./DirectoryA_1/Folder/ ./DirectoryA_2
```

You will get an error stating:

**./DirectoryA_1/Folder/ is a directory**

To copy directories, you have to pass the `-r` flag. This flag informs the `cp` command to recursively copy a directory and its contents (which could be files or other sub directories). So for the previous command, you can add the flag before the directory sources like this:

```bash
cp -r ./DirectoryA_1/Folder/ ./DirectoryA_2
```

This command will recursively copy the **Folder** directory in **./DirectoryA_1/** as well as all files and directories in the **Folder** directory.

## How to copy files that match a glob pattern

A glob pattern is similar to Regex, which allows you to match multiple files with names that match a specific pattern. Learn more about the difference here: [Regex vs Glob patterns](https://dillionmegida.com/p/regex-vs-glob-patterns/).

For example, if you want to copy all files in **DirectoryA_1** with the **.txt** extension, you can execute this command:


```bash
cp ./DirectoryA_1/*.txt ./DirectoryA_2
```

`./DirectoryA_1/*.txt` matches files with the `.txt` extension in their names, and the `cp` command can copy all those files to the destination.

You can check out the [glob documentation](https://linux.die.net/man/7/glob) to learn more about globbing patterns and characters you can use.

Now you know how to copy files (and directories) right from the command line. Thanks for reading!

