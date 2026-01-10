---
title: How to Copy a Directory in Linux with the cp Command
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-24T22:21:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-copy-a-directory-in-linux-with-the-cp-command
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Shittu-Olumide-How-to-Copy-a-Directory-in-Linux-with-the-cp-Command.png
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: "By Shittu Olumide\nCopying directories is an essential task in Linux. It\
  \ allows you to duplicate directories, create backups, or transfer data between\
  \ different locations. \nOne of the most commonly used commands for copying files\
  \ and directories in Li..."
---

By Shittu Olumide

Copying directories is an essential task in Linux. It allows you to duplicate directories, create backups, or transfer data between different locations. 

One of the most commonly used commands for copying files and directories in Linux is `cp`.

In this tutorial, we will explore how to copy directories effectively using the `cp` command, along with various options and techniques to customize the copying process.

## The Linux `cp` command

You use the `cp` command in Linux to copy files and directories from one location to another. It stands for "copy" and is a fundamental command-line utility for file management. 

The `cp` command follows a specific syntax for copying directories. Understanding the basic structure of the command is crucial for successful directory copies. 

### The `cp` command syntax

```bash
cp [options] source_directory destination_directory

```

Here's an explanation of each component of the syntax:

* `cp`: This is the command itself, which stands for "copy."
* `[options]`: This represents optional flags and parameters that can modify the behavior of the `cp` command. Options are typically preceded by a hyphen (-) or double hyphen (--) and can be used to specify additional functionalities, such as preserving attributes, enabling recursion, or displaying progress.
* `source_directory`: This is the directory that you want to copy. It can be specified as a relative or absolute path.
* `destination_directory`: This is the directory where you want to copy the source directory. It can also be specified as a relative or absolute path.

Here are some key concepts and features of the `cp` command:

1. **Copying files**: The `cp` command can be used to copy individual files. We provide the path and name of the source file, followed by the destination directory or filename.
2. **Copying directories**: The `cp` command can also copy entire directories. To copy a directory and its contents, we need to include the `-r` (or `--recursive`) option, which enables recursive copying. This option ensures that all subdirectories and files within the directory are copied.
3. **Preserving file attributes**: By default, the `cp` command copies files without preserving their attributes such as permissions, timestamps, and ownership. However, we can use the `-p` (or `--preserve`) option to preserve file attributes during the copy process.
4. **Handling existing files**: When copying files or directories, the `cp` command handles conflicts when there are existing files or directories with the same names in the destination location. By default, it overwrites the existing files without prompting. We can use the `-i` (or `--interactive`) option to prompt before overwriting existing files.
5. **Copying across file systems**: The `cp` command can handle copying between different file systems. It automatically adjusts the behavior and performs the copy accordingly.

Let's demonstrate how to do this:

```bash
cp -r /Desktop/welcome /Desktop/tutorial

```

In the above command:

* `-r` flag stands for "recursive" and allows the `cp` command to copy directories and their contents.
* `/Desktop/welcome`  is the path of the directory we want to copy.
* `/Desktop/tutorial` is the path where we want to copy the directory to.

## Conclusion

With the knowledge and understanding of the `cp` command's syntax, we can efficiently copy directories and their contents.

Throughout this article, we have explored the step-by-step process of copying directories to different locations, recursively copying directories with their contents. We have also discussed some important features of the `cp` command. 

So go ahead and try it out :)

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

