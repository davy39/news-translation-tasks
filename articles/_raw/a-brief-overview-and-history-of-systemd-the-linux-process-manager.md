---
title: A brief overview and history of systemd — the Linux process manager
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-07-24T13:30:00.000Z'
originalURL: https://freecodecamp.org/news/a-brief-overview-and-history-of-systemd-the-linux-process-manager
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca13f740569d1a4ca4d86.jpg
tags:
- name: history
  slug: history
- name: Linux
  slug: linux
seo_title: null
seo_desc: Intelligently running Linux services includes knowing how to test for their
  status which, in turn, requires understanding how modern Linux distributions manage
  processes. This article  will briefly explore the function and history of systemd — the
  pr...
---

Intelligently running Linux services includes knowing how to test for their status which, in turn, requires understanding how modern Linux distributions manage processes. This article  will briefly explore the function and history of systemd — the process manager that seems to be loved, feared, and hated in equal parts.

Something on your Linux box isn’t running? Troubleshooting is your friend. But before you even get there, shouldn’t you make sure the underlying service is actually running? Sometimes the configuration files are by default set to inactive.

You can use _systemctl status_ to find out whether a service — OpenSSH in this example — is running on your machine:

$ systemctl status ssh  
● ssh.service - OpenBSD Secure Shell server  
   Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)  
   Active: active (running) since Mon 2017-05-15 12:37:18 UTC; 4h 47min ago    
 Main PID: 280 (sshd)   <2>  
    Tasks: 8  
   Memory: 10.1M  
      CPU: 1.322s  
   CGroup: /system.slice/ssh.service  
           ├─ 280 /usr/sbin/sshd -D  
           ├─ 894 sshd: ubuntu [priv]   
           ├─ 903 sshd: ubuntu@pts/4    
           ├─ 904 -bash  
           ├─1612 bash  
           ├─1628 sudo systemctl status ssh  
           └─1629 systemctl status ssh  
[...]

In this case, as you can see from the Active line of the output, everything is fine. If you did have to crank it up yourself though, you’d use systemctl once again, but this time with _start_ in place of _status_. Bored with your new toy? `systemctl stop` will put it away for you.

`# systemctl stop ssh`

That systemctl fellow seems nice enough, but we’ve barely had the chance to meet him. Let’s dig a big deeper.

## Linux process management

First, just what is systemctl and what’s it actually doing? To properly answer that question, you’ll have to think for a bit about how Linux manages system processes in general. And since it’s always nice to meet new friends, you will also learn about some process tracking tools to make understanding the way things work easier.

Software, as I’m sure you already know, is programming code containing instructions to control computer hardware on behalf of human users. An operating system is a tool for organizing and managing software packages so that they can effectively leverage a computer’s hardware resources.Organizing and managing processes for a complex multi-process and multi-user operating environment is no simple task. To make it work, you’ll need some kind of traffic cop to tightly control the many moving parts. Let me introduce you to systemctl, a hard-working officer in the traffic division of the Linux Police Department.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OD9MOvg4XlBFYezYqwUSMA.png)
_The availability and responsiveness of many system services are managed by systemd’s systemctl process manager_

## Viewing processes with the ps command

Let’s pull out an electron microscope and see if we can’t spot an actual process in its natural habitat. The very first process to wake up and get everything else going when a Linux computer boots is called init (although as we’ll soon discover, that name can be misleading). You can see for yourself that init is first by running the following ps command exactly the way it’s printed here — I’ll explain the details in just a minute.

$ ps -ef | grep init   
root         1     0  0 12:36 ?        00:00:00 /sbin/init   
ubuntu    1406   904  0 16:26 pts/4    00:00:00 grep --color=auto init

The rightmost column of output (/sbin/init on the first line) represents the location and name of the file behind the process itself. In this case, it’s a file called “init” that lives in the /sbin directory. The leftmost column on this first line contains the word _root_ and tells us that the owner of this process is the root user. The only other piece of information that interests us right now is the number 1, which is the process ID (PID) of the init process. The only way you’re going to get PID 1 is by getting there before anyone else.

By the way, the second line displayed by that ps command is the process assigned to the grep command itself. Note how its owner is ubuntu (my username) and its PID is much higher than 1.

Before moving on it’s worth spending a bit more time with ps. As you’ve seen, ps displays information about active processes. It’s often important to have access to process-related information so we can properly plan and troubleshoot system behavior. You can expect to use ps early and often.

If you were to type just ps and run it, you’d probably get only two results: the first, a process called bash that represents the Bash command interpreter being used by your current shell session, and the most recent command (which, of course, was ps). But by looking at the PID assigned to Bash (7447, in this example), you just know there are lots and lots of other processes already hard at work somewhere on your system. These will have been spawned by parent shells going all the way back to the init process itself.

$ ps  
 PID TTY          TIME CMD  
7447 pts/3    00:00:00 bash  
8041 pts/3    00:00:00 ps

Adding the -e argument to ps as we did above will return not only the processes running in your current child shell, but all the processes from all parent shells right back up to init.

A parent shell is a shell environment from within which new (child) shells can subsequently be launched and through which programs run. You can think of your GUI desktop session as a shell, and the terminal you open to get a command line as its child. The top level shell (the grandparent?) is the one that is run first when Linux boots.

If you want to visualize parent and child shells/processes, you can use the `pstree` commmand (adding the -p argument to display the PID numbers for each process). Note how the very first process (assigned PID 1) is _systemd_. On older versions of Linux, this would have been called _init_ instead.

$ pstree -p  
systemd(1)─┬─agetty(264)   
           ├─agetty(266)  
           ├─agetty(267)  
           ├─agetty(268)  
           ├─agetty(269)  
           ├─apache2(320)─┬─apache2(351)  
           │              ├─apache2(352)  
           │              ├─apache2(353)  
           │              ├─apache2(354)  
           │              └─apache2(355)  
           ├─cron(118)  
           ├─dbus-daemon(109)  
           ├─dhclient(204)  
           ├─dockerd(236)─┬─docker-containe(390)─┬─{docker-containe}(392)  
           │              │                      └─{docker-containe}(404)  
           │              ├─{dockerd}(306)  
           │              └─{dockerd}(409)  
           ├─mysqld(280)─┬─{mysqld}(325)  
           │             ├─{mysqld}(326)  
           │             └─{mysqld}(399)  
           ├─nmbd(294)  
           ├─rsyslogd(116)─┬─{in:imklog}(166)  
           │               ├─{in:imuxsock}(165)  
           │               └─{rs:main Q:Reg}(167)  
           ├─smbd(174)─┬─smbd(203)  
           │           └─smbd(313)  
           ├─sshd(239)───sshd(840)───sshd(849)───bash(850)───pstree(15328)  
           ├─systemd-journal(42)  
           └─systemd-logind(108)

Go ahead and try all these commands on your own machine. Even on a quiet system, you’ll probably see dozens of processes; a busy desktop PC or server can easily have thousands.

## Working with systemd

There’s something interesting about that /sbin/init file we just saw. “file” is a venerable Unix program that gives you insider information about a file. If you run _file_ with /sbin/init as its argument, you’ll see that the init file is not actually a program, but simply a symbolic link to a program called systemd.

$ file /sbin/init  
/sbin/init: symbolic link to /lib/systemd/systemd

After many years of fragmentation and some vigorous political infighting, nearly all Linux distributions now use the same process manager: systemd. systemd is a drop-in replacement for the init process. By “drop-in replacement” I mean that, even if the way it gets things done can be quite different, to the casual observer, systemd functions just like init always did. That’s why the /sbin/init file is now really nothing more than a link to the systemd program.

This is all a bit theoretical since you’ll probably never actually invoke the systemd program itself by name — either directly or through its /sbin/init front end. This is because, as you’ve already seen, the key administration tasks are handled by systemctl on behalf of systemd.

Technically, systemd’s primary job is to control the ways individual processes are born, live their lives, and then die. The systemctl command we used above is the tool of choice for those tasks. But — somewhat controversially — the systemd developers expanded the functionality far beyond the traditional role of process management to take control over various system services. Included under the new systemd umbrella are tools like a logging manager (journald), network manager (networkd), and device manager (you guessed it: udevd). Curious? The “d” stands for daemon; a background system process.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ufSpWkBfRakYB-Ex.jpg)

_This article is adapted from chapter 3 (Remote connectivity: safely access networked machines) of my_ [_Manning “Linux in Action” book_](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9)_. There’s lots more fun where this came from — including_ [_Linux and Docker admin courses on Pluralsight_](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton) _and a hybrid course called_ [_Linux in Motion_](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1) _that’s made up of more than two hours of video and around 40% of the text of Linux in Action. Who knows…you might also enjoy [my other books and courses.](https://bootstrap-it.com)_

