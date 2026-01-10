---
title: A Beginner’s Guide to Surviving in the Linux Shell
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-15T15:30:23.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-surviving-in-the-linux-shell-cda0f5a0698c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sviUxGylSOenBQTLmAtGnA.png
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: terminal
  slug: terminal
seo_title: null
seo_desc: 'By Puranjay Mohan

  In this article, you''ll learn how to kill your fear of the Linux shell by learning
  the ten most useful Linux commands.


  All the best people in life seem to like LINUX - Steve Wozniak


  The Linux Shell/Command-Line

  A black screen with...'
---

By Puranjay Mohan

In this article, you'll learn how to kill your fear of the Linux shell by learning the ten most useful Linux commands.

> **All the best people in life seem to like LINUX -** Steve Wozniak

### The Linux Shell/Command-Line

A black screen with white text and no graphics, yes! The Linux Shell does look daunting at first glance, but it is much more powerful than any graphical tool. 

Linux powers 70% of the servers and 90% of super-computers in the world. The learning curve for Linux is steep and to learn it you need to live inside it for some time. Once you get good at the command line, you get a skill which sets you apart from the crowd.

This article introduces and explains the 10 most useful Linux commands required to survive in the Linux shell environment. After reading this article you should be able to perform all the basic tasks like creating and deleting directories, editing text files, and so on using the command line.

![Image](https://cdn-media-1.freecodecamp.org/images/98wBtN9xnRdYspAeLkK5MDYo5ibGqQI7nIM-)

### Why should one learn the Linux command line?

#### Perks of being good at using the command line.

* **You get to know much more about your operating system.**  
The shell exposes you to the filesystem more directly than the graphical file browser, it makes you understand the hierarchy and structure of the OS. You also get to play with the configuration files directly and this gives you the power to control your operating system more efficiently.
* **You can control computers and servers remotely.**  
Network protocols like **SSH** and **Telnet** allow you to remotely connect to computers on a network, but they only provide you with the shell and not the graphical interface. Therefore you can use these protocols only if you are familiar with the shell.
* **You can install Arch Linux without anyone’s help**  
Arch Linux is a Linux distribution which scares many beginners because of its installation method. To install Arch Linux you need to do all the steps manually from disk partitioning to user creation, using the shell. You need to be very good at the Linux shell to install Arch Linux.
* **You can get paid to configure and administer Linux Servers.**  
Most companies have a job posting titled, “Linux System Administrator”. The role of the person at this position is to maintain the Linux computers and make changes and configurations to them as per the requirements. The person at this role has to be very good at the Linux Shell and should know all the commands required to configure a Linux system.

### The Linux Command Prompt

When you open the terminal app in your Linux distribution, you will see a black screen with your name and some other information printed. After which, you will see a cursor ready to receive commands. The information shown by the prompt is configurable but is beyond the scope of this tutorial.

![Image](https://cdn-media-1.freecodecamp.org/images/zzllZ1dcG-XhRNdpyGEmSghbZmhQdYXQB4JB)
_[username@hostname current-directory]$_

The Prompt provides information about the username, the host name (your computer’s name as it appears on the network), the present working directory and a ‘$’, which signifies that you are a normal user and not the root user (root user has all privileges and rights in Linux).

### The 10 basic commands

These 10 commands will enable you to experience the shell in a way where you will be able to perform all the tasks that you have been doing in the Graphical User Interface environment, like creating and deleting directories, writing, editing and deleting files etc., in the shell without facing any problems.

### 1. pwd

The print working directory (pwd) command prints the complete path to the directory that you are working in. When you open the terminal app it usually starts the shell at your home folder, therefore running the `pwd` command will print “/home/(your-username). ‘~’ represents home in the prompt.

![Image](https://cdn-media-1.freecodecamp.org/images/q6g9sTGABPXyjHqygPu9WrAntYD36G3tbEC5)
_pwd command in the home folder_

### 2. cd

Change Directory (cd) command changes the working directory to the directory whose name is given after cd. Writing `cd myfolder` will change the working directory to ‘myfolder’ and its name will appear in the prompt, but it will throw an error if ‘myfolder‘ doesn’t exist in the current directory.

![Image](https://cdn-media-1.freecodecamp.org/images/0T5iCKOE7JlCPyhM0aU8TMik9-UN4862-AYN)
_cd to myfolder and then running pwd_

Running ‘pwd’ command after the above step will show the path to the directory, which we switched to.

Running `cd ..` command will change the working directory to the previous directory in the hierarchy. In this case, it will change back to the home directory.

![Image](https://cdn-media-1.freecodecamp.org/images/CjYtnXGLppUpsrd6vfQxjeO9L9XfVlthV1JG)
_running ‘cd ..’ to change to the previous directory and then running pwd._

You can also provide the absolute path to the directory, to which you wish to switch. Absolute paths are complete paths starting from the root directory. For example, the absolute path to ‘myfolder’ will be ‘/home/puranjay/myfolder’, which is the same path shown by pwd command.

### 3. ls

List (ls) command prints the contents of the current working directory, it prints the names of all the files and directories present in the current directory. Running `ls` in the ‘myfolder’ directory will show its contents, i.e. file1, file2, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/TaePljLT3fT2nJCjxvnPyvJKkdUn-DzEP0BF)
_ls command running in the myfolder directory_

You can also provide the absolute path to the directory whose contents you wish to see. For example, if the working directory is home and `ls /boot` is run, the shell will print the contents of the ‘boot’ folder present in the root(/) directory. The working directory will not change. Also ‘boot’ and ‘/boot’ don’t imply the same meaning to the shell. ‘boot’ means a directory or a file in the current working directory but ‘/boot’ means a directory or a file present in the root(/) directory. Running `ls boot` will print an error message because there is no file or folder named ‘boot’ in the current working directory(home).

![Image](https://cdn-media-1.freecodecamp.org/images/48xdRf17CmuwqY1VPoU2UhdRD7uKDlaJZc5l)
_ls /boot shows contents of boot directory in root, but ls boot shows an error_

### 4. man

man(manual) command will open the manual page for the command given after man. Manual pages contain documentation about all commands available in Linux, they provide information about the correct use of the command and different options available for the command.

To exit from man page press ‘**q**’.

For example, running the `man ls` will open the manual page for ls command.

![Image](https://cdn-media-1.freecodecamp.org/images/JCZU2ozbykb3h7XWxcNHjydpFhQbQ5l-fHLi)
_The manual page for ls command_

### 5. mkdir

Make-directory (mkdir) command creates a new directory of the name given after the command, in the current working directory. For example, running `mkdir hello` will create a folder named ‘hello’ inside the current directory. After the directory has been created, running `cd hello` will change the current directory to the newly built ‘hello’ directory, ‘~’ will change to ‘hello’.

![Image](https://cdn-media-1.freecodecamp.org/images/hLfshSo4P6YvuXovTirK3orqrs7We64Yroa6)
_creating a directory named ‘hello’ and then changing into it._

### 6. rmdir

Remove directory (rmdir) removes/deletes the directory with the name given after the command. Running `rmdir hello` will delete the previously created ‘hello’ directory. A directory cannot be deleted by running rmdir inside the same directory, which is to be deleted. The command `cd ..` can be used to go out of the directory and then `rmdir hello` can be run to delete it.

![Image](https://cdn-media-1.freecodecamp.org/images/CTZDh51AjPqZCIECZ3gioTMyMz5k25OE3Yz3)
_moving out of ‘hello’ directory and then deleting it._

If a directory is not empty and `rmdir` is run to delete this directory, then it will fail with an error stating that the directory being deleted is not empty.

![Image](https://cdn-media-1.freecodecamp.org/images/LAtnIwDlG-0AiKkaW9WmQXSofw9qzZ7DrDed)
_‘hello’ contains a file named ‘file1’, therefore rmdir fails with an error._

To overcome this error and delete directories which are not empty, the `-- ignore-fail-on-non-empty` flag can be passed to rmdir.

For example, running rmdir `--ignore-fail-on-non-empty hello` will delete the hello directory although it is not empty.

![Image](https://cdn-media-1.freecodecamp.org/images/QILE4pb42NKSHyTcaMva1GqQV5Jc0LIUVD1d)
_deleting hello folder which is not empty_

### 7. clear

Clear command cleans the shell and removes all previous outputs. It comes in handy when you want to clear the clutter on the terminal.

### 8. nano

Nano is a terminal based text editor, which can be used to create and edit text files and also edit configuration files. It is similar to any other text editor like notepad, the only difference being that it works through the shell and doesn’t have a GUI. It comes pre-installed with most of the Linux distributions.  
Running `nano` in the shell opens the nano text editor and provides an interface where text can be typed.

![Image](https://cdn-media-1.freecodecamp.org/images/zq8NxPxsqyD9POpd6kN4h9paPhYWdnwQ80rj)
_Nano running in the Linux Terminal_

To exit nano, press `CTRL+X`, it will ask you if you want to save the file.

![Image](https://cdn-media-1.freecodecamp.org/images/h0-TOHFeaAS-YS4wbvHHGygujfasDRHtXxIP)
_Pressing ‘Y’ will save the file._

If you press ‘Y’, it will ask you to enter the name for the file and pressing ‘ENTER’ after typing the name will close nano. A file with the name you gave will be created in the current directory.

![Image](https://cdn-media-1.freecodecamp.org/images/zFnHFjfM12jMK4exVqKDWuhAd7XT-3OS94Lp)
_saving the file as testfile.txt_

### **9. cat**

Cat command is used to print the contents of a file on the shell console, it is mostly used when you want to see what is present inside a file. To use the cat command, `cat filename` can be run in the shell, it will output the contents of the file on the screen.

![Image](https://cdn-media-1.freecodecamp.org/images/TwM-2qx7s6pXkSKhI6fmQJGFBTfCspCsA5c4)
_running cat command on the previously created text file._

### 10. rm

Remove(rm) command is similar to the `rmdir` command but it deletes files instead of directories. To use this command, `rm filename` can be run in the shell. It will delete the file if it is present in the current directory.

![Image](https://cdn-media-1.freecodecamp.org/images/8OHhC5Y-oTjhX16iw0xJtByyGtUHJZLlCDGD)
_deleting the previously created text file._

### **11. mv (Bonus Command)**

mv command can be used for moving or renaming files. Renaming is just moving a file to another name. The mv command has the format, `mv source destination`. You need to provide the complete path to the source and destination if it is outside the current working directory.

![Image](https://cdn-media-1.freecodecamp.org/images/2gb8qFl079Dpdp-evt5JxeiIta2JOmhSvEar)

### Side notes and points to be remembered:

* Linux shell is case-sensitive, therefore ‘desktop’ and ‘Desktop’ don’t imply the same meaning.
* Care should be taken while writing paths in Linux because ‘boot’ and ‘/boot’ are two different folders.
* The only way to master the Linux shell is by spending time in it and using it every day. It is an added advantage if your main OS is Linux.
* Anything that you do in the Linux OS, try to find a way to do the same thing but from within the shell. [Stack Overflow](https://stackoverflow.com/) is a great place to get your Linux questions answered.
* If you really want to hone your Linux skills and become a Linux master, then you can read the [Linux Bible](https://www.oreilly.com/library/view/linux-bible-9th/9781118999875/), which is the most in-depth Linux guide ever written.

### Conclusion:

My first encounter with the Linux terminal was 5 years ago and I too was very intimidated by it. For these five years, I have been learning something new about Linux every day. The energy and time that you spend while learning Linux is completely worth it and will never go in vain. Linux is the biggest and the oldest Open-Source project and learning it is the first step in the process of contributing to it.

Feel free to point out any mistakes you find, constructive criticism does no harm.

Thank You.

