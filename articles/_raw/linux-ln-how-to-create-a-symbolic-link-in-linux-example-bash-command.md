---
title: Linux ln – How to Create a Symbolic Link in Linux [Example Bash Command]
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-02-21T16:05:08.000Z'
originalURL: https://freecodecamp.org/news/linux-ln-how-to-create-a-symbolic-link-in-linux-example-bash-command
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/gabriel-heinzer-4Mw7nkQDByk-unsplash.jpg
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
seo_title: null
seo_desc: "A symlink (symbolic) is a type of file that points to other files or directories\
  \ (folders) in Linux. \nYou can create a symlink (symbolic) by using the ln command\
  \ in the command line. \nSymbolic links are useful because they act as shortcuts\
  \ to a file ..."
---

A symlink (symbolic) is a type of file that points to other files or directories (folders) in Linux. 

You can create a symlink (symbolic) by using the `ln` command in the command line. 

Symbolic links are useful because they act as shortcuts to a file or directory. 

In this article, I will go over how to use the `ln` command to create a symlink to a file or directory. 

## What is the difference between soft and hard links in Linux? 

A soft link or symbolic link will point to the original file on your system. A hard link will create a copy of the file.

Soft links can point to other files or directories on a different file system, whereas hard links cannot. 

## How to create a symlink to a file

You can find the command line using the Terminal application on Mac or using the Command Prompt on Windows. 

Here is the basic syntax for creating a symlink to a file in your terminal.

```bash
ln -s existing_source_file optional_symbolic_link

```

You use the `ln` command to create the links for the files and the `-s` option to specify that this will be a symbolic link. If you omit the `-s` option, then a hard link will be created instead.

The existing_source_file represents the file on your computer that you want to create the symbolic link for. 

The optional_symbolic_link parameter is the name of the symbolic link you want to create. If omitted, then the system will create a new link for you in the current directory you are in. 

Let's take a look at an example to better understand how this works.

On my Desktop I have a file called `example_fcc_file.txt`. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-19-at-7.48.02-PM.png)

I will need to first open up my terminal, and then make sure I am in the Desktop directory. I can run the command `cd Desktop` to navigate to my Desktop.

After running that command, you should see you are now in the Desktop. 

```bash
jessicawilkins@Dedrias-MacBook-Pro-2 ~ % cd Desktop
jessicawilkins@Dedrias-MacBook-Pro-2 Desktop % 
```

I can then use the `ln` command to create a new symbolic link called `fcc_link.txt`.

```bash
ln -s example_fcc_file.txt fcc_link.txt
```

When you run that command in the terminal, you will notice that nothing was returned. That is because when the `ln` command is successful, there will be no output and it will return zero.

```bash
jessicawilkins@Dedrias-MacBook-Pro-2 Desktop % ln -s example_fcc_file.txt fcc_link.txt


jessicawilkins@Dedrias-MacBook-Pro-2 Desktop % 
```

To check that your symbolic link was successful, you can use the `ls` command. The `ls` command will list information about files and the `-l` flag represents the symbolic link. 

```bash
ls -l fcc_link.txt
```

When you run that command, you should see this type of result in the terminal. 

```bash
lrwxr-xr-x  1 jessicawilkins  staff  20 Feb 19 19:56 fcc_link.txt -> example_fcc_file.txt

```

The `fcc_link.txt -> example_fcc_file.txt` portion of the output shows you that the symbolic link is pointing to the file called `example_fcc_file.txt`. 

You should also see that new symbolic link show up in your directory.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-19-at-8.11.09-PM.png)

## How to create a symbolic link to a directory

In this example, we want to create a symbolic link called `my_music` that will point to my Music folder in the home directory of my computer.

First, make sure you are in the home directory. You can run  `cd` to get back to your home directory in the command line.

```bash
jessicawilkins@Dedrias-MacBook-Pro-2 Desktop % cd
jessicawilkins@Dedrias-MacBook-Pro-2 ~ % 
```

You can then use the `ln` command to create a symlink to the Music directory.

```bash
ln -s /Users/jessicawilkins/Music ~/my_music

```

If successful, you should see it in the home directory.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-19-at-8.38.14-PM.png)

## How to remove a symbolic link

To remove symlink you can either use the `unlink` or `rm` command.

If we wanted to remove the `fcc_link.txt` symlink we created earlier, then we can use either of these commands:

```bash
rm fcc_link.txt
```

```bash
unlink fcc_link.txt
```

Now we should see that the symlink was removed from our directory.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-19-at-8.47.30-PM.png)

## How to overwrite symlinks

If we try to create a new symlink called `fcc_link.txt`, then it will result in an error because it is already being used and pointing to another file. 

```bash
ln: fcc_link.txt: File exists

```

You can overwrite this error by using the force (`-f`) option.

```bash
ln -sf example_fcc_file.txt fcc_link.txt
```

## How to learn more about the ln command

If you want to learn more about the `ln` command, then you can read about it in the `man` pages (manual for using Linux commands).

Run `man ln`  in your terminal and you should see the man pages for the `ln` command.

```
LN(1)                     BSD General Commands Manual                    LN(1)

NAME
     link, ln -- make links

SYNOPSIS
     ln [-Ffhinsv] source_file [target_file]
     ln [-Ffhinsv] source_file ... target_dir
     link source_file target_file

DESCRIPTION
     The ln utility creates a new directory entry (linked file) which has the same modes as the original file.  It is
     useful for maintaining multiple copies of a file in many places at once without using up storage for the
     ``copies''; instead, a link ``points'' to the original copy.  There are two types of links; hard links and sym-
     bolic links.  How a link ``points'' to a file is one of the differences between a hard and symbolic link.

     The options are as follows:

     -F    If the target file already exists and is a directory, then remove it so that the link may occur.  The -F
           option should be used with either -f or -i options.  If none is specified, -f is implied.  The -F option
           is a no-op unless -s option is specified.

     -h    If the target_file or target_dir is a symbolic link, do not follow it.  This is most useful with the -f
           option, to replace a symlink which may point to a directory.

     -f    If the target file already exists, then unlink it so that the link may occur.  (The -f option overrides
```

## Conclusion

A symlink (symbolic) is a type of file that points to other files or directories (folders) in Linux. You can create a symlink (symbolic) by using the `ln` command in the command line. 

Symbolic links are useful because they act as shortcuts to a file or directory. 

Here is the basic syntax for creating a symlink to a file using the terminal:

```bash
ln -s existing_source_file optional_symbolic_link
```

Here is the basic syntax for creating a symlink to a directory using the terminal:

```bash
ln -s path_to_existing_directory name_of_symbolic_link

```

To remove symlink you can either use the `unlink` or `rm` command:

```bash
rm name_of_symbolic_link
```

```bash
unlink name_of_symbolic_link
```

If you need to remove a symlink then you can use this command:

```bash
ln -sf path_to_existing_directory name_of_symbolic_link
```

I hoped you enjoyed this article on symbolic links and best of luck on your programming journey. 


