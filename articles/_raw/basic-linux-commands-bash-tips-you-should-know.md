---
title: Linux Commands - Basic Bash Command Line Tips You Should Know
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2020-01-05T22:19:00.000Z'
originalURL: https://freecodecamp.org/news/basic-linux-commands-bash-tips-you-should-know
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e28740569d1a4ca3ba8.jpg
tags:
- name: Bash
  slug: bash
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: null
seo_desc: "Linux has a ton of commands, but most people only use a fraction of them.\
  \ Here are some of the most used Linux commands to use in the terminal. \nFirst,\
  \ we'll cover some tips that will make the command line easier to use:\n\nUse tab\
  \ for autocompletion. ..."
---

Linux has a ton of commands, but most people only use a fraction of them. Here are some of the most used Linux commands to use in the terminal. 

First, we'll cover some tips that will make the command line easier to use:

* Use tab for autocompletion. After you start typing something in the Linux terminal, hit tab and it will suggest possible options that start with the string you have typed so far.
* Use `ctrl+r search_term` to search commands you have previously used.
* Quickly move to the beginning or end of a line with `ctrl+a` and `ctrl+e`.
* Reuse the previous command in the present command with `!!`.
* You can run multiple commands in a single line by separating commands with a `;`.

It's time to learn the common Linux commands. You can get more information about any of these commands by using the `man` command. This will bring up the manual page for a command. For example, if you type `man cat` into a linux terminal, you will get more information about the `cat` command.

### ls

List directory contents.  
_Example:_ `ls /applications` will display all the files and folders stored in the applications folder.

### cd

Change to a directory.  
_Example:_ Change from the current directory to _/usr/local_ with `cd /usr/local`.

**mv**   
Rename or move file(s) or directories.  
_Example:_ the command `mv todo.txt /home/qlarson/Documents` would move "todo.txt" to the "Documents" directory.

### mkdir

Create a new directory.  
_Example:_ `mkdir freecodecamp` will make a directory named "freecodecamp".

### rmdir

Delete empty directories.

### touch

Create an empty file with the specified name.

### rm

Remove file(s) and/or directories.  
_Example:_ `rm todo.txt` will delete the file.

### locate 

Locate a specific file.  
_Example:_  `locate -i vacuum*mop` command will search for any file that contains the word "vacuum" and "mop". The `-i` makes the search case-insensitive.

### clear

Clear a command line screen/window for a fresh start.

### cp

Copy files and directories.  
_Example:_ the command `cp todo.txt /home/qlarson/Documents` would create a copy of "todo.txt" to the "Documents" directory.

### alias 

Create an alias for Linux commands.   
_Example:_ `alias search=grep` will allow you to use `search` instead of `grep`_._

### cat

Display the contents of a file on the screen.   
_Example:_ `cat todo.txt` will show the text of "todo.txt" on the screen.

### chown

Change who owns a file.  
_Example:_ `chown qlarson todo.txt` will make "qlarson" the owner of "todo.txt".

### chmod

Change a file’s permissions.  
_Example:_ `chmod 777 todo.txt` will make "todo.txt" readable, writable, and executable by everyone. The digits in "777" specify the permissions for user, group, and others, in that order.

### sudo

Perform tasks that require administrative or root permissions.  
Example: Use `sudo passwd quincy` to change the password of user "quincy".  
["Sudo make me a sandwich."](https://xkcd.com/149/)

### find 

Search for files matching a provided pattern. This command is for searching file(s) and folder(s) using filters such as name, size, access time, and modification time.  
_Example:_ `find /home/ -name todo.txt`  will search for a file named "todo.txt" within the home directory and its subdirectories.

### grep 

Search files or output for a particular string or expression. This command searches for lines containing a specified pattern and, by default, writes them to the standard output.  
_Example:_ `grep run todo.txt` will search for the word "run" in the "todo.txt" file. Lines that contain "run" will be displayed.

### date

Display or set the system date and time.

### df

Display report on the system’s disk space usage.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-114.png)

### du

Show how much space each file takes up. This will show the size in disk block numbers. If you want to see it in bytes, kilobytes, and megabytes, add the `-h` argument like this: `du -h`.

### file

Determine the type of a file.   
_Example:_ `file todo.txt` would likely show the type of "ASCII text".

### history 

Shows the command history.

### kill 

Stop a process.  
_Example:_ Stop a process with a PID of 485 using the command `kill 485`. Use the `ps` command (below) to determine the PID of a process.

### less

View the contents of a file one page at a time.  
_Example:_ `less todo.txt` will display the contents of "todo.txt".

**ps**   
Display a list of the currently running processes. This can be used to determine PIDs needed to `kill` processes.

### pwd 

Display the pathname for the current directory. "**p**rint **w**orking **d**irectory"

### ssh 

Remotely log in to another Linux machine, over the network.   
_Example:_ `ssh quincy@104.25.105.32` will login to 104.25.105.32 using the username "quincy".

**tail** - Display the last 10 lines of a file. See fewer or more lines by using the -n (number) option.  
_Example:_ `tail -n 5 todo.txt` will display the last 5 lines of "todo.txt".

### tar

Store and extract files from a tarfile (.tar) or tarball (.tar.gz or .tgz).

### top 

Displays the resources being used on your system, similar to the task manager in Windows.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-115.png)

