---
title: How to Use Piping and Redirection in the Linux Terminal
subtitle: ''
author: Alvin
co_authors: []
series: null
date: '2024-04-26T23:15:26.000Z'
originalURL: https://freecodecamp.org/news/linux-terminal-piping-and-redirection-guide
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/piping-redirection-linux.png
tags:
- name: Bash
  slug: bash
- name: command line
  slug: command-line
- name: Linux
  slug: linux
- name: terminal
  slug: terminal
seo_title: null
seo_desc: 'The command line interface in Linux provides a powerful way of perfoming
  a range of tasks on your system. Because of its roots, Linux has many features baked
  into the terminal.

  Two of these powerful features are piping and redirection. These features...'
---

The command line interface in Linux provides a powerful way of perfoming a range of tasks on your system. Because of its roots, Linux has many features baked into the terminal.

Two of these powerful features are piping and redirection. These features enable you to redirect the output and input of commands to and from other commands and files.

In this article, you'll learn what piping and redirection in Linux mean, followed by a deep dive into how to use these features yourself.

## Prerequisites

To fully understand this guide, you'll need to at least have:

* Basic [understanding of the Linux operating system](https://www.freecodecamp.org/news/learn-the-basics-of-the-linux-operating-system).
* Basic experience working with the Linux command line. 
* Access to a Linux command line to try out the commands.

Take a look at this [Linux command line tutorial](https://www.freecodecamp.org/news/linux-command-line-tutorial/) if you're new or need a refresher. 

## What is Piping in Linux?

Before we dive into the how, what does piping even mean? Piping is the act of directing the output of one Linux command as an input to another command. You can direct the standard output or standard error from one command to another using piping.

A simple example of piping is when you take the output of one command and use it as an input to another command. The pipe (|) metacharacter is used to achieve this.

If you're new to the concept of metacharacters, this is just a fancy name for characters with special meaning in the command line. There are other metacharacters in Linux aside from pipe (|). Common examples include less than (<), greater than (>), and ampersand (&), to name a few.

### The Basics of Piping

The basic syntax of using the `pipe` command is as follows:

```
command1 | command2 | command3 | ... | commandN
```

In the syntax above, the terminal will execute the commands from left to right. It will start with `command1`, and then the output will be input to `command2`. Outputs of `command2` will then be used as inputs of `command3` and so on. The good thing about piping is that you can chain as many commands as you'd like.

### Piping Examples

Below are several examples of using the `pipe` command to perform various tasks.

#### 1. Counting the number of files and directories

```bash
ls -l | wc -l
```

In the example above, the first section lists all the files and directories in the current directory using the `ls` command. The additional `-l` option tells the `ls` command to list the contents in a long list format. 

The output of the `ls -l` command is then piped to the second section. The `wc -l` command counts the number of lines from the output of the `ls -l` command in the first section and prints the result to the terminal.

#### 2. Sorting a list of files and directories

```bash
ls | sort
```

In the command above, the `ls` command will output the lists of the files and directories in the current directory. The list is then piped to the `sort` command, which sorts them alphabetically and prints the result to the terminal.

#### 3. Sort and display unique words from a file

```bash
cat words.txt | sort -r | uniq
```

The third example includes three separate commands connected by two pipes. The first command outputs the contents of the `words.txt` file, which contains a list of words. 

The output is piped to the `sort -r` command, which sorts the words in reverse alphabetical order. Finally, the sorted words are piped to the `uniq` command, which removes duplicates and outputs the unique sorted words.

### Why and When Should You Apply Command Piping Linux?

Piping takes more than just knowing the syntax. The syntax is pretty simple. To effectively use piping, you should understand its essence. 

The purpose of piping is to help you chain commands, using the output of one as the input of another.

Piping is not meant to be a way to chain unrelated commands that you want to be executed sequentially. If you need to do that, write your commands in the terminal and separate them with semicolon (;) using the following syntax:

```
command1 ; command2 ; ... ; commandN
```

## What Is Redirection in Linux?

Redirection is the act of dictating where the inputs or outputs of your commands go. By default, commands receive data from standard input and then output the results in standard output.

One of the main areas where redirection proves useful is when working with commands and files. You can, for example, redirect the output of a command to a file instead of printing the output in the terminal. Alternatively, you can declare a certain file as an input to a command.

Like piping, Linux provides special characters to perform redirection. Here are important file-redirection characters in Linux and what they do:

* `>` – directs the output of a command to a given file.
* `<` – directs the contents of a given file to a command.
* `>>` – directs the output of a command to a given file. Appends the output if the file exists and has content.
* `2>` – directs error messages from a command to a given file.
* `2>>` – directs an error message from a command to a given file. Appends the error message if the file exists and has content.
* `&>` – directs standard output and error to a given file.
* `&>>` – directs standard output and error to a given file. Appends to the file if it exists and has contents.

Let's look at each file-redirection character in-depth.

### 1. Output Redirection With `>`

The `>` symbol enables you to redirect the output of a command to a certain file. Using the symbol, you can redirect the output to any existing file. If it doesn't exist, the output redirection character will automatically create a new one. 

However, you should be careful when writing to an existing file because its contents will be overwritten without a warning.

You can perform output redirection using the following syntax:

```
command > file
```

The output of running `command` will be written to the `file` instead of the standard output (or, in other words, printed to the terminal). Here's an example of how you can do output redirection:

```bash
ls -a > contents.txt
```

In the command above, the list of items in the current directory (including dotfiles, directories, and files) will be written to the `contents.txt` file. You won't see any output in the terminal due to the redirection.

### 2. Output Redirection With `>>`

`>>` lets you redirect the output of a command to a file. But, unlike using a single greater than character (`>`), `>>` will append the output if you try to write to an existing file (instead of overwriting its contents). If the file doesn't exist, it will create a new one.

The syntax is as follows:

```
command >> file
```

Here's an example of using output redirection with `>>` to perform the same action as before:

```bash
ls -a >> contents.txt
```

### 3. Input Redirection With `<`

The `<` character in the command line lets you redirect the input to a command from a file instead of the keyboard. The syntax of input redirection using `<` is as follows:

```
command < file
```

Here's an example of using input redirection:

```bash
wc -w < files.txt
```

In the example above, we're passing `files.txt` as the input to the `wc -w` command, which counts the number of words in the file. But you don't need to use the input redirection character in many scenarios because it's the default behavior. For instance, the command above is similar to the following:

```bash
wc -w files.txt
```

### 4. Error Redirection With `2>` and `2>>`

When working on the command line, you may run into errors. For instance, if you want to execute a file without appropriate permissions. Instead of letting the terminal throw an error by printing it, you can use the error redirection character to dictate where the error message should go.

A good place to redirect errors is a file dedicated to storing errors. Here's a simple example of a command trying to access the list of files in a directory that doesn't exist:

```bash
ls nonexistent 2> error.txt
```

In the example above, the terminal will throw an error since there's no file named `nonexistent`. But instead of printing it to the console, it will be stored in the `error.txt` file due to the error redirection character. However, the file will have nothing if there's no error.

If you must append an error to an existing file instead of overwriting its contents, use `2>>` instead of `2>`.

### 5. Output and Error Redirection With `&>` and `&>>`

Instead of choosing whether to redirect standard output or standard errors to a file, `&>` allows you to redirect both simultaneously. You can think of `&>` as a shorthand for combining the output redirection (>) and error redirection (2>) characters.

The syntax of using `&>` is as follows:

```
command &> output.txt
```

The error or output of the `command` is written to the `output.txt` file. Here's an example:

```bash
ls sample &> output.txt
```

In the command above, if the `sample` directory is not available or is available but you don't have read permissions, an appropriate error will be written in the `output.txt` file. But if it exists and you have read permissions, its contents will be output in the `output.txt` file.

Using `&>>` allows you to append the output to the file if it exists and has contents.

## How to Combine Piping and Redirection to Unleash the Power of the Command Line

Using piping and redirection in combination can let you perform complex operations without heavy lifting. By learning how to combine the two, you can create complex commands to perform various actions with less typing. 

Take the following command as an example:

```bash
ls | grep ".txt" > text_files.txt
```

The `ls` command lists the contents of the current directory. The output is piped to the `grep` command to filter text files. Finally, the output of the `grep` command is redirected to the `text_files.txt` file. 

This simple yet powerful example shows that when it comes to piping and redirection, the only limit is your mind.

## Conclusion

In this tutorial, you learned the basics of piping and redirection in Linux. We covered the basics together with examples of how you can use the two. 

The two features in isolation can be powerful, but you can go further by combining them in your commands, as shown in the last section.


