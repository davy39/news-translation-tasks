---
title: The Best Linux Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-19T17:44:00.000Z'
originalURL: https://freecodecamp.org/news/linux-example-bash-command-line
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f30740569d1a4ca4148.jpg
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'Linux is a powerful operating system that powers most servers and most
  mobile devices. In this guide, we will show you examples of how to use some of its
  most powerful features. This involves using the Bash command line.

  12 Simple and Useful Linux Co...'
---

Linux is a powerful operating system that powers most servers and most mobile devices. In this guide, we will show you examples of how to use some of its most powerful features. This involves using the Bash command line.

## 12 Simple and Useful Linux Commands

The commands listed here are basic, and will help you get started quickly. But they’re also powerful, and they’ll continue to be useful as your Linux expertise expands.

1. `echo` Command: This takes the text you give it and sends it somewhere— back to the screen, to a file, or to another command. Example: `echo "hello!"`
2. `cat` Command: To display the contents of a text file, just type `cat myfile`.
3. `find` Command: It does what it says, and it’s good at it. Use it to locate files by path, size, date, owner and a bunch of other useful filters. Example: `find . -type f -mtime -1h # List files in this directory modified in the past hour`.
4. `date` Command: Just type date when you want to know what time it is. Example: `date "+It's %l:%m%p on %A"`. Use it in a script to name files according to the current date.
5. `ls` Command: What’s in this directory? Combine `ls` with some useful flags to display and sort directory contents by date and size. It also gives you lots of options for formatting the output.
6. `pwd` Command: Where am I? Linux can be unforgiving, particularly when you delete something. Make sure you know are before you issue your commands.
7. `mail` Command: Linux’s mail program isn’t good looking, but it can be really helpful. You can create a message and add text, recipients, and attachments all in one command. Example: `echo "We're having a great time." | mail -s "Wish you were here!" -A postcard.png -t mom@example.com`
8. `cut` Command: When you have a string with separators in it, use `cut` to filter out certain fields. Example: `echo "this, that, and the other" | cut -d, -f2 # "that"`
9. `grep` Command: To find lines of text that contain a certain string, use grep. Example: `grep 'root' /etc/passwd # root:x:0:0:root:/root:/bin/bash`
10. `sed` Command: Use `sed` to find and change a substring in a piece of text. Example: `echo "this, that, and the other" | sed 's/that/those/' # "this, those, and the other"`
11. `shutdown` Command: Use this command to shut down the system and turn off the power. Example: `shutdown -h now` shuts down system immediately. `shutdown -h +5` shuts down system after five minutes.
12. `wget` Command: Use `wget` to download files from the command line.  
Example: `wget [http://ftp.gnu.org/gnu/wget/wget-1.5.3.tar.gz](http://ftp.gnu.org/gnu/wget/wget-1.5.3.tar.gz)`

Use these commands in scripts and at the command line. They’re all very powerful commands, and Linux’s main page has a lot more information about each one.

## Linux User Management Commands Example

Also, important commands used for System Administrators are following:

1. `uptime` Command: In Linux, the uptime command shows how long your system has been running and the number of users are currently logged in. It also displays load average for 1,5 and 15 minutes intervals.
2. `w` Command: This will display users currently logged in and their process, along with load averages. Also shows the login name, tty name, remote host, login time, idle time, JCPU, PCPU, command and processes.
3. `users` Command: displays currently logged in users. This command don’t have other parameters other than help and version.
4. `who` Command: the who command simply returns the user name, date, time and host information. The who command is similar to the w command. Unlike the w command, who doesn’t print what users are doing. 
5. `whoami` Command: the whoami command prints the name of the current user. You can also use “who am i” to display the current user. If you are logged in as a root using sudo command, “whoami” returns root as current user. Use “who am i” if you want to know the exact user logged in.
6. `ls` Command: ls displays a list of files in human readable format.
7. `crontab` Command: list schedule jobs for current user with the crontab command and -l option.
8. `less` Command: the less command allows you to quickly view a file. You can page up and down. Press ‘q‘ to quit from the less window.
9. `more` Command: the more command allows you to quickly view a file and shows details in percentage. You can page up and down. Press ‘q‘ to quit out from the more window.
10. `cp` Command: Copy a file from its source to its destination while preserving the same mode.

## **How to Create a User**

#### **Use the `adduser` or `useradd` command to add a new user to your system.**

```text
$ sudo adduser username
```

Be sure to replace `username` with the user that you want to create.

#### **Use the `passwd` command to update the new user’s password.**

```text
$ sudo passwd username
```

A strong password is highly recommended!

## **How to Create a Sudo User**

To create a `sudo` user, you need to create a regular user first using the command above, then add this user to the group of `sudoers` using the `usermod` command.

##### **On Debian systems (Ubuntu/LinuxMint/ElementryOS), members of the `sudo` group have sudo privileges.**

```text
$ sudo usermod -aG sudo username
```

##### **On RHEL based syatems (Fedora/CentOs), members of the `wheel` group have sudo privilages.**

```text
$ sudo usermod -aG wheel username
```

## **How to Delete a User**

##### **For Debian (Ubuntu)**

```text
$ sudo deluser username
```

##### **For RHEL (Fedora/CentOS)**

```text
$ sudo userdel username
```

##### **Creating groups and adding users**

```text
$ sudo groupadd editorial
$ sudo usermod -a -G editorial username
```

#### **Note: All the above commands can be executed without sudo in `root` mode**

To switch to root on ubuntu, run the  `su -i` command followed by the password of the user logged in. Prompt changes to `#` instead of `$`.

##### **On Debian systems (Ubuntu/LinuxMint/ElementryOS), members of the `sudo` group have sudo privileges.**

```text
$ sudo usermod -aG sudo username
```

## **How to Create a Group**

To create a group, use the command `groupadd`

```text
$ sudo groupadd groupname
```

## **How to delete group**

To delete a group, use the command ‘groupdel’

```text
$ sudo groupdel grouname
```

## The Linux Find Command Example

### Using the Find Command

The Linux find command is a powerful tool to help you locate files and directories on your server. With a little practice, you can easily track things down based on name, type, size, or date (when they were created or last updated).

Think of find as your eager helper:

You: “I’m looking for something on my server.”

Find: “I can help! What can you tell me about it?”

You: “It was a file, bigger than 2GB, somewhere under my home directory, updated in the last 48 hours.”

Find: “Tada!”

Find is a program, so really you’d have to tell it `find ~ -type f -size +2G`.

Here are some sample commands using find:

* `find ~ -type d # Show me all the subdirectories inside my home directory`
* `find / -type f -name 'todo.txt' # Show me files named 'todo.txt' anywhere under the root directory (i.e. anywhere)`

The first parameter always names the directory in which we’ll look. In our examples above, these are ~ (home directory of the current user) and / (root directory of the filesystem).

Other parameters are optional and can be combined in any ways you find useful:

* The type parameter allows you to constrain the search for files only (f), directories only (d) or symbolic links (l). If you omit the type parameter, you’ll be searching for all of these types.
* The name parameter lets you specify what you want to find by name, either with a literal string (‘filename.txt’) or using wildcards (‘file?.*’).

`man find` will show you many more parameters, and is worth reviewing. Find can locate files by name, user, creation date, size and much more. Next time you’re looking for something, find it!

## **Linux dd Command Example**

The “dd” command can be used to create a file of a specific size. This is useful if you would like to test download speeds, or any other tests, and need a file of a specific size.

```text
dd if=/dev/zero of=file_name.txt bs=1024k count=10
```

This will create a file of 1MB called file_name.txt.

bs is your byte size and count represent the number of blocks. An easy way to look at is 1024K X 10.

Here is an even simpler way to create a 1MB file:

```text
dd if=/dev/zero of=file_name.txt bs=1MB count=1
```

## Example of how to write a Linux Bash Script

### Writing a Bash Script

By typing commands on the Linux command line, you can give the server instructions to get some simple tasks done. A shell script is a way to put together a series of instructions to make this easier. Shell scripts become even more powerful when you add logic like `if` and `while` to automatically control how they behave as circumstances change.

### What’s Bash?

Bash is the name of a command line interpreter, a program that makes sense of the Linux commands you enter at the command prompt, or in your script.

### What’s in a Script?

A script is just a file. A basic script is made up of an introductory line that tells the server what to make of it, and one or more instructions to execute. Here’s an example:

```text
#!/bin/bash
echo "Hi. I’m your new favorite bash script."
```

The first line has special meaning, which we’ll discuss below. The second line is just a Linux command, one you could type out on the command line.

### What’s a Comment?

Comments are text you add to your script that you intend bash to ignore. Comments start with a pound sign, and are useful for annotating your code so you and other users can understand it. 

To add a comment, type the `#` character, followed by any text that’s helpful you. Bash will ignore the `#` and everything after it.

**Note:** the first line of the script is not a comment. This line is always first, always starts with `#!` and has special meaning to bash.

Here’s the script from before, commented:

```text
#!/bin/bash # Designates the path to the bash program. Must start with '#!' (but isn't a comment).
echo "Hi. I’m your new favorite bash script." # 'echo' is a program that sends a string to the screen.
```

### Executing a Script

You can open a text editor, paste that example code and save the file, and you’ve got a script. Scripts are conventionally named ending in ‘.sh,’ so you might save that code as myscript.sh.

The script won’t execute until we do 2 things:

**First, make it executable.** (We’ll only have to do this once.) Linux relies extensively on file permissions. They determine a lot about how your server behaves. There’s a lot to know about permissions, but for now we only need to know this: you can’t run your script until you give yourself execute permissions. To do that, type:

`chmod +x my script.sh`

**Second, run it.** We execute the script from the command line just like any other command like `ls` or `date`. The script name is the command, and you need to precede it with a ‘./’ when you call it:

`./myscript.sh # Outputs "Hi. I'm your new favorite bash script." (This part is a comment!)`

### Conditionals

Sometimes you want your script to do something only if something else is true. For example, print a message only if a value is below a certain limit. Here’s an example of using `if` to do that:

```text
#!/bin/bash

count=1 # Create a variable named count and set it to 1

if [[ $count -lt 11 ]]; then # This is an if block (or conditional). Test to see if $count is 10 or less. If it is, execute the instructions inside the block.
    echo "$count is 10 or less" # This will print, because count = 1.
fi # Every if ends with fi
```

Similarly, we can arrange the script so it executes an instruction only while something is true. We’ll change the code so that the value of the count variable changes:

```text
#!/bin/bash

count=1 # Create a variable named count and set it to 1

while [[ $count -lt 11 ]]; do # This is an if block (or conditional). Test to see if $count is 10 or less. If it is, execute the instructions inside the block.
    echo "$count is 10 or less" # This will print as long as count <= 10.
    count=$((count+1)) # Increment count
done # Every while ends with done
```

The output of this version of myscript.sh will look like this:

```text
"1 is 10 or less"
"2 is 10 or less"
"3 is 10 or less"
"4 is 10 or less"
"5 is 10 or less"
"6 is 10 or less"
"7 is 10 or less"
"8 is 10 or less"
"9 is 10 or less"
"10 is 10 or less"
```

## **Real World Scripts**

These examples aren’t terribly useful, but the principles are. Using `while`, `if`, and any command you might otherwise type manually, you can create scripts that do valuable work.

