---
title: How to Make a File in Linux from the Command Line – Create a File in the Terminal
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2023-01-05T18:58:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-file-in-linux-from-the-command-line-create-a-file-in-terminal
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Copy-of-Copy-of-read-write-files-python--3-.png
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: "Managing files from the command line is one of the most common tasks for\
  \ a Linux user. \nFiles are created, edited, deleted, and used by many of the background\
  \ OS processes. Files are also used by regular users to accomplish daily tasks such\
  \ as taking..."
---

Managing files from the command line is one of the most common tasks for a Linux user. 

Files are created, edited, deleted, and used by many of the background OS processes. Files are also used by regular users to accomplish daily tasks such as taking notes, writing code, or simply duplicating content.

In this article, we will see three methods through which we can create files using the terminal. The three commands that we'll discuss are `touch`, `cat` and `echo`.

### Pre-requisites:

You should have access to the Linux terminal to try out the commands mentioned in this tutorial. You can access the terminal in either of the following ways:

* Install a Linux distro of your choice on your system. 
* Use WSL (Windows Subsystem for Linux), if you want to use Windows and Linux side by side. [Here](https://www.freecodecamp.org/news/how-to-install-wsl2-windows-subsystem-for-linux-2-on-windows-10/) is a guide to do that.
* Use [Replit](https://replit.com/) which is a browser-based IDE. You can create a Bash project and access the terminal right away.

## Method #1: How to Create Files Using the `touch` Command 

The `touch` command creates empty files. You can use it to create multiple files as well.

**Syntax of the `touch` command:**

```bash
 touch FILE_NAME
```

**Examples of the `touch` command:**

Let's create a single empty file using the syntax provided above.

```bash
touch access.log
```

Next, we'll create multiple files by providing the file names separated with spaces after the `touch` command. 

```bash
touch mod.log messages.log security.log
```

The above command will create three separate empty files named `mod.log`, `messages.log`, and `security.log`.

## Method #2: How to Create Files Using the `cat` Command 

The `cat` command is most commonly used to view the contents of a file. But you can also use it to create files.

**Syntax of the `cat` command:**

```bash
cat > filename
```

This will ask you to enter the text that you can save and exit by pressing `ctrl+c`.

```bash
cat > sample.txt
```

 When I enter the above command, my terminal output looks like this:

```bash
zaira@Zaira:~$ cat > sample.txt
This is a sample file created using the "cat" command
^C
```

Note the `^C` sign, which corresponds to `Ctrl+c` and signals to the terminal to save and exit.

Here are the contents of the created file:

```bash
zaira@Zaira:~$ more sample.txt
This is a sample file created using the "cat" command
```

## Method #3: How to Create Files Using the `echo` Command 

The `echo` command is used to add and append text to files. It also creates the file if it doesn't already exist.

**Syntax of the `echo` command:**

```bash
echo "some text" > sample.txt
```

or

```bash
echo "some text" >> sample.txt
```

The difference between `>` and `>>` is that `>` overwrites the file if it exists whereas `>>` appends to the existing file. 

If you would like to follow along with the video tutorial of this article, here is the link:

%[https://youtu.be/IQ8R7br-EuY]

## Conclusion

In this article, we discussed three different methods to create files in the Linux command line. I hope you found this tutorial helpful.

What’s your favorite thing you learned from this tutorial? Let me know on [Twitter](https://twitter.com/hira_zaira)!

You can read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

