---
title: File Permissions in Linux – How to Use the chmod Command
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-01-02T22:17:02.000Z'
originalURL: https://freecodecamp.org/news/file-permissions-in-linux-chmod-command-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/Banner---File-permission-blog-1.png
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: null
seo_desc: "Just as with other operating systems, multiple users can create user accounts\
  \ and share the same machine running Linux OS. \nBut whenever different users share\
  \ a system, problems of privacy can easily arise. The first user may not wish the\
  \ next user t..."
---

Just as with other operating systems, multiple users can create user accounts and share the same machine running Linux OS. 

But whenever different users share a system, problems of privacy can easily arise. The first user may not wish the next user to view, edit, or delete their files, for example.

The Linux Terminal possesses some superpowers when it comes to handling file permissions. You can grant or revoke permissions for every file and directory from your Linux Terminal.

## What are File Permissions in Linux?

File permissions control which actions can be performed by which users. Read, Write, and Execute are the three actions possible for every file. 

Users are classified under three broad categories: Normal users, Groups, and Others. Linux allows users to set permissions at a very granular level. You can secure your file or directory in every possible location of a file system. 

This seems useful, right?

There are three important commands you'll use when managing file permissions:

1. `chmod` (Change mode)
2. `chown` (Change ownership)
3. `chgrp` (Change group)

Among these, `chmod` is one of the most important commands. We'll discuss the `chmod` command in this tutorial, and I'll get into the others in upcoming articles. 

Let’s deep dive into the `chmod` command 🏊.

### Actions you can perform on a file

Before we proceed further, I want to make sure you're clear about how the Read, Write, and Execute actions of a file work. Read and write are pretty are self-explanatory – they determine whether a user can read or write to a file.

But, what’s an executable file?

A file is said to be executable if it has a sequence of instructions to achieve something. A good example is scripting files (Shell Scripts). 

## What is the `chmod` Command?

`chmod` is a command that lets you change the permissions of a file or directory to all types of users.

Here’s the syntax of the chmod command:

```bash
chmod <Operations> <File/Directory Name>
```

You can grant or revoke the permission by replacing the Operations in the above command.

### What are the operations you can perform?

The Operations in the above syntax are divided into 2 categories. Let's explore them below.

#### User Level permissions

These operations control permissions on the user level. Here's the commands you can use:

* `u` – Grant permission to a user
* `g` – Grant permission to a group (A Group of users)
* `o` – Grant permission to others (who do not come under either of the above).

**Note:** If this option is left empty, permissions will be applied to the logged-in user. Most of the time it'll be left empty.

#### File Level permissions

These control permissions on the file level.

* `r` – Grants read permission
* `w` – Grant write permission
* `x` – Grant execute permission

These operations need to be preceded with a '+' or '-' operator.

'+' indicates adding a new permission, and '-'  indicates removing an existing permission.

Here's an example:

```bash
chmod +r sample.txt
```

The above command adds read permission for the `sample.txt` file.

Pretty straightforward, right? Let's continue.

## How to Make a File Executable in Linux

I can explain this more clearly with an example from my experience. 

Linux is the default operating system of my team. We recently hired an intern, who has zero knowledge of Linux but was curious to learn and explore. We started to train him initially by asking him to write some shell scripts, because most servers run Linux OS. He found the entire code on the internet and copied it (we gave such a task intentionally).

He saved the file but was not able to run the script. He didn't know the actual problem. He started removing a few blocks of code and tried to run it again and again.

He repeatedly got the error stating "Command not found".

Finally, he reached the 1st line. He replaced that line with a print statement (the "echo" command) and ran the file with the hope to see the output. But he still hadn't found that error.

With some frustration, he asked for help.

Let's see the issue now.

Basically, we can execute .sh files by just running them like this:

```bash
./install.sh
```

Let's see the code inside `install.sh`

```bash
echo "This is executable file 🎉"
```

He ran the same command but it did not work. This is because the file was not in executable format. So I ran the magic command to make the file executable:

```bash
chmod +x install.sh
```

![Image](https://lh3.googleusercontent.com/trd4dTKoxhk9Ap9xLifsuo6bD9wj4kc_i5gtDudFLQyU1gNdJLGoLoyCuJLh1FF9Yah-IG43YuR3yrrtJq48xBEYEq0QQkHMFB1n1YBiv-_fWJT95gyihZD0tjAj0ScnEmF33WRFdHJbfzTSpxSnaimyUbHlK9a2hMujE8CeyT4AoliZY5XJ_wKOsIVrPw)
_Terminal command to make a file executable_

Now it is executable. He stared at me as if I was a hacker 😂. But really, it's a pretty simple and basic concept.

## How to Remove Permissions from a File in Linux

I work with my colleague Divad on lots of projects, and he likes to try to fool me. We work together on many hobby projects and we often write shell scripts for quick deployment. 

Whenever he writes shell scripts, he always removes all the permissions from the file and pushes the changes to the remote repo. So every time I have to grant permissions using the above commands for whatever action I have to do.

Let's have a quick look at the command he uses to remove file permissions.

Here we have a file named `install.sh` which has all permissions (Read, Write, Execute). Let's remove the execute permission for this script file.

```bash
chmod -x install.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-136.png)
_Terminal command to remove execute permission from a file_

You'll not be able to execute this file now. Trying so will give you an error as shown in the above screenshot.

Let's remove the read permission from the file.

```bash
chmod -r install.sh
```

Alright, with this command we've removed the read permission. Let's try to read that file using Nano (the file editor for the Linux terminal). You will be able to see the "Permission Denied" error at the bottom.

![Image](https://lh4.googleusercontent.com/DHdaIMmV0pcFiMO-9GiLwXbUes8QZs5v6uKDLfuCu9Ltt-0SitENOM8najXPaxMXFJSQAzlI7F1u1p8i6fbqq1timsCoVGVOBdEtzUlybcmoh0W6oHWrIKyUUJr1dOjDZ_vbo0WkGE3fcLa3T7ZfvymVKVZPoKvKrDDH7ZVFSSlyeyQ1ypLixkAdD5uroA)

![Image](https://lh3.googleusercontent.com/iphPcFoH9r0VnGArokWKexbVTzGtMkaOC-EgeXECKqHyE2QJMA49sh5HK_u_ZNKDDKc_hmFPe-dM8VVy0Xu-EKGT1VpBaABcUtPxCEipSvNVhwJQWfxisGBHJbvAcosK3kO8JNsWT9qSl2-7A0cK-A8gHjWIK4cfvNAx4iofZOOPOgevXbR8mVjmDZqk0w)

The same applies to removing write permission from the file:

```bash
chmod -w install.sh
```

![Image](https://lh5.googleusercontent.com/wVL6XdsMVVBrqw3dnrjELCIsqQyDkxtQWUKcD8HyXAUJktcBQyYAK1Ln-A9P517WW1b8tfm95HGd4NmRuP9fgs9QI6w9ZrR0ZeSNyMpWIlYlGld_Vq1-_m8fDDcV9Et-BJd99Jy3RI2cs6vm26Ywp9IFJzx1su8CGVgoe38-BNJp9qDooZe7XAbqv1S88A)

You can achieve all the above together using the below command:

```bash
chmod -rwx install.sh
```

This is the core part of handling file permissions in Linux. Remember that we have barely scratched the surface of it, though. Try to understand it and play around with some sample files. Because who knows – in the future, you may get a colleague like Divad. :)

## How to Add or Remove Permissions for Directories (Folders) in Linux

If you work with Linux, you might have come across various directories such as `/etc`, `/var`, `/opt`, and others. But you may not be aware of why these directories exist. 

There's one thing in common for all these folders, though: that is, you'll not be able to create a file or folder inside them without root permission.

This setting will be pre-configured in your system when Linux OS is installed.

But, you might wonder, can I restrict my folder in a `/home` directory similar to the above directories? The answer is yes. You can achieve this by changing the permission of the directory using the `chmod` command.

Let's understand this with an example.

I created a directory named `locked_directory` and removed read permission from this directory. If I try to read the contents of the folder using the `ls` command, I'll end up seeing the "Permission Denied" error message.

```bash
chmod -r locked_directory/
```

![Image](https://lh5.googleusercontent.com/JfC_fUvfsYzwm23cEaE6ThbFRGdY-tazuXBYIxBdunGsSSema2yGIFkJrLtw0rksPpG4iSUiBqjm9Uu5bEIuTasDyNm_zX0kLAqA3Ncv30FHcmSaXe_XbOzBdIBtg4hVI9kuIwPnRIYhdBZpsfXIaPPnVGUwBP5cwvfWpFn2OPjQfjjiIkkd3rrz0w465A)
_`chmod` command to remove read permission from a directory_

But, did you know that I can create another directory inside `locked_directory` named `dir1` and read the files and folders in `dir1`?

![Image](https://lh6.googleusercontent.com/FMLRcjtvY-M1YVSANwmgdzdDwBJ9lrv4V7dLREva9RRUmal7PG8Q5p-l4XZMCi3zIznvSqIKpr68PwGlcripbREffgPzpmqOJ09OR-CvBEGrncBxYX9c9OTe0kq5-xL9rsGP1xQDO_sZP9iXPmHKpXFukFhTIYlXaFRnoHvdCRYA1FJDHcvXmFqP8dmshA)

Then what's the purpose of the command we just ran before? Removing the read permission on the parent should remove the same on child directories too, right?

Well. That's the exact thing I told you earlier. Linux manages a very granular level of file permissions.

If you want to apply the permissions to the parent directory and all its child directories, you need to pass an exclusive flag with the `chmod` command.

That flag is `-R`. It basically means applying the same permissions recursively to all sub-directories (child directories). So this permission will apply to the end child of a file/directory.

Here's the syntax for that:

```bash
sudo chmod -R <permission> <filename>
```

Remember that running the command to do a recursive operation needs root permission. So you need to add `sudo` at the beginning of this command. Here's what it looks like:

```bash
sudo chmod -R -r locked_directory
```

![Image](https://lh3.googleusercontent.com/GZGisVgUxcZjYduKGlOaYHUaTRTgI7tf3nNzdpxL8QZvDDYV_PLgwaFipmbfxzDlziG_Gy7f5Gyeibc_E7IhGvEOmReUKUe3t7yYMXZKDsRnXcxivbepHpqww3y2YSLSyjvi83i_c5Z1rgQbc_ku-Bz5hy8lMl8idzg4MtfYtEZymPFTZBNceq9xgH79ZQ)
_Terminal Command to remove read permission from a directory Recursively_

From the above screenshot, you can see that trying to view the child directory files has failed after removing the read permission recursively from the parent directory.

## Another Way to Handle File Permissions in Linux

Alternatively, you can use Octal representation to control the file permissions. 

We can use numbers to represent file permissions (the method most commonly used to set permissions). When you change permissions using the Octal mode, you represent permissions for each triplet using a number (4, 2, 1, or combination of 4, 2, and 1).

Let's see the syntax for using octal mode:

```bash
chmod <user><group><others> install.sh
```

Here's an example of octal mode:

```bash
chmod 777 install.sh
```

### How can I remove permissions using Octal Mode?

We can use `0` to remove permissions from a file. Here's an example:

```bash
chmod 000 install.sh
```

<table class=""><thead></thead><tbody><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true"><strong>Access&nbsp;</strong></td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true"><strong>Symbolic Mode</strong></td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true"><strong>Octal Mode</strong></td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">Read</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">r</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">4</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">Write</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">w</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">2</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">Execute</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">x</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">1</td></tr></tbody><tfoot></tfoot></table>

The table shows the Octal code for each file permission:

<table class=""><thead></thead><tbody><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true"><strong>Access&nbsp;</strong></td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true"><strong>Symbolic Mode</strong><br data-rich-text-line-break="true"><strong>Eg:</strong>u+rwx,g+rw,o+r</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true"><strong>Octal Mode&nbsp;</strong><br data-rich-text-line-break="true"><strong>Eg:</strong>764 ( User, Group, Others )</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">User</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">u</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">&lt;first place&gt;</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">Group</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">g</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">&lt;middle place&gt;</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">Others</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">o</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">&lt;last place&gt;</td></tr></tbody><tfoot></tfoot></table>

You might be confused 😖. Read further to understand clearly.

Let's consider a scenario.

You want to grant read, write, and execute permissions to users and read-only permission for groups and others to the `install.sh` file.

Let's see how to do that using the above two methods.

### How to manage permissions in Symbolic Mode

```bash
chmod u+rwx,go+r install.sh
```

Let's dismantle each part and try to understand them:

* `u+rwx` represents adding read, write, and execute permissions for users
* `go+r` represents adding read permission for groups and others

### How to manage permissions in Octal Mode

```bash
 chmod 744 install.sh
```

Let's dismantle each of these numbers and try to understand them:

* The first number (7) represents permission for a user: 7 = ( 4 (`read`) +2 (`write`) +1(`execute`) )
* The second number (4) represents permissions for a group: 4 (`read`)
* The third number (4) represents permissions for others: 4 (`read`)

## Which Mode is Best?

It turns out that symbolic mode is more powerful than octal mode. 

The reason is, in the symbolic mode we can mask out the permission bits we want to change. But in octal mode, permission modes are absolute and can't be used to change individual bits.

## How to Find Permissions of a File

 We can find the existing permissions of a file using ls command.

I hope you all know about `ls` command. Adding the `-l` flag and file name with the `ls` command shows some more info about the file, including the permissions. 

```bash
ls -l install.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-137.png)
_Terminal command to see the existing permission of a file_

Look at the first part of the output (`-rwxrwxrwx`) from the above screenshot. Let's explore what it means: 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/permissions-1.png)
_Existing permissions output description_

The first character indicates the type of input. 

* "-" indicates a file
* "d" indicates a directory
* "i" indicates a link (a symlink, which is a shortcut to a file/directory)

You group the next set of letters, at a maximum of 3 for each group. These groups represents corresponding permissions for user, group, and others. 

## Conclusion

In this article, you have learned about handling basic file and folder permissions.

I hope you enjoyed reading this tutorial. I have one request to all: give it a try on your own with some complicated scenarios like having permutations and combinations of permissions 😂. It'll definitely be helpful in your entire career.

Subscribe to my newsletter by visiting my [site](https://5minslearn.gogosoon.com/) and also have a look at the consolidated list of all my blogs.

Cheers!


