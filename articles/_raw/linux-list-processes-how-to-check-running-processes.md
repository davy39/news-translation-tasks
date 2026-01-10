---
title: Linux List Processes – How to Check Running Processes
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2021-06-29T19:47:13.000Z'
originalURL: https://freecodecamp.org/news/linux-list-processes-how-to-check-running-processes
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/article-banner.png
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'Every day, developers use various applications and run commands in the
  terminal. These applications can include a browser, code editor, terminal, video
  conferencing app, or music player.

  For each of these software applications that you open or comman...'
---

Every day, developers use various applications and run commands in the terminal. These applications can include a browser, code editor, terminal, video conferencing app, or music player.

For each of these software applications that you open or commands you run, it creates a *process* or *task*.

One beautiful feature of the Linux operating system and of modern computers in general is that they provide support for multitasking. So multiple programs can run at the same time.

Have you ever wondered how you can check all the programs running on your machine? Then this article is for you, as I'll show you how to list, manage, and kill all the running processes on your Linux machine.

## Prerequisites

* A Linux distro installed.
    
* Basic knowledge of navigating around the command-line.
    
* A smile on your face :)
    

## A Quick Introduction to Linux Processes

A process is an instance of a running computer program that you can find in a software application or command.

For example, if you open your Visual Studio Code editor, that creates a process which will only stop (or die) once you terminate or close the Visual Studio Code application.

Likewise, when you run a command in the terminal (like `curl ifconfig.me`), it creates a process that will only stop when the command finishes executing or is terminated.

## How to List Running Processes in Linux using the `ps` Command

You can list running processes using the `ps` command (ps means *process status*). The `ps` command displays your currently running processes in real-time.

To test this, just open your terminal and run the `ps` command like so:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-28-at-3.25.33-PM.png align="left")

This will display the process for the current shell with four columns:

* **PID** returns the unique process ID
    
* **TTY** returns the terminal type you're logged into
    
* **TIME** returns the total amount of CPU usage
    
* **CMD** returns the name of the command that launched the process.
    

You can choose to display a certain set of processes by using any combination of options (like `-A` `-a`, `-C`, `-c`, `-d`, `-E`, `-e`, `-u`, `-X`, `-x`, and others).

If you specify more than one of these options, then all processes which are matched by at least one of the given options will be displayed.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-28-at-3.55.10-PM.png align="left")

*The* `ps` command manual page.

> Type `man ps` in your terminal to read the manual for the `ps` command, which has a complete reference for all options and their uses.

To display all running processes for all users on your machine, including their usernames, and to show processes not attached to your terminal, you can use the command below:

```python
ps aux
```

Here's a breakdown of the command:

* `ps`: is the process status command.
    
* `a`: displays information about other users' processes as well as your own.
    
* `u`: displays the processes belonging to the specified usernames.
    
* `x`: includes processes that do not have a controlling terminal.
    

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-28-at-4.39.05-PM.png align="left")

This will display the process for the current shell with eleven columns:

* **USER** returns the username of the user running the process
    
* **PID** returns the unique process ID
    
* **%CPU** returns the percentage of CPU usage
    
* **%MEM** returns the percentage memory usage
    
* **VSV** returns the virtual size in Kbytes
    
* **RSS** returns the resident set size
    
* **TT** returns the control terminal name
    
* **STAT** returns the symbolic process state
    
* **STARTED** returns the time started
    
* **CMD** returns the command that launched the process.
    

## How to List Running Processes in Linux using the `top` and `htop` Commands

You can also use the `top` task manager command in Linux to see a real-time sorted list of top processes that use the most memory or CPU.

Type `top` in your terminal and you'll get a result like the one you see in the screenshot below:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-28-at-4.27.28-PM.png align="left")

> You can type `q` to exit the session.

An alternative to `top` is `htop` which provides an interactive system-monitor to view and manage processes. It also displays a real-time sorted list of processes based on their CPU usage, and you can easily search, filter, and kill running processes.

`htop` is not installed on Linux by default, so you need to install it using the command below or [download the binaries](https://htop.dev/downloads.html#binaries) for your preferred Linux distro.

```python
sudo apt update && sudo apt install htop
```

Just type `htop` in your terminal and you'll get a result like the one you see in the screenshot below:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-29-at-4.49.09-AM.png align="left")

## How to Kill Running Processes in Linux

Killing a process means that you terminate a running application or command. You can kill a process by running the `kill` command with the process ID or the `pkill` command with the process name like so:

```python
kill [PID]
```

or

```python
pkill [COMMAND]
```

To find the process ID of a running process, you can use the `pgrep` command followed by the name of the process like so:

```python
pgrep iTerm2
```

To kill the iTerm2 process in the screenshot above, we will use any of the commands below. This will automatically terminate and close the iTerm2 process (application).

```python
kill 25781
```

or

```python
kill iTerm2
```

## Conclusion

When you list running processes, it is usually a long and clustered list. You can pipe it through less to display the command output one page at a time in your terminal like so:

```python
ps aux | less
```

or display only a specific process that matches a particular name like so:

```python
ps aux | grep Chrome
```

I hope that you now understand what Linux processes are and how to manage them using the `ps`, `top`, and `htop` commands.

Make sure to check out the manual for each command by running `man ps`, `man top`, or `man htop` respectively. The manual includes a comprehensive reference you can check if you need any more help at any point.

Thanks for reading – cheers! 💙
