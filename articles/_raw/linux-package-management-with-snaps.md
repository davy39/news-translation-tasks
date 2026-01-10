---
title: Linux Package Management with Snaps
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-06-22T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/linux-package-management-with-snaps
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/software-snap.png
tags:
- name: Linux
  slug: linux
- name: 'snaps '
  slug: snaps
- name: software-packaging
  slug: software-packaging
seo_title: null
seo_desc: "A big part of administrating Linux machines - especially remote machines\
  \ - is managing and installing software. \nWhen something goes wrong with a local\
  \ application or when something on the file system breaks and needs fixing, you're\
  \ often going to wa..."
---

A big part of administrating Linux machines - especially remote machines - is managing and installing software. 

When something goes wrong with a local application or when something on the file system breaks and needs fixing, you're often going to want to push updates without having to travel many miles to sit down in front of a physical screen. 

A lot of problems can be solved through Bash scripts, of course, but there are still plenty of use-cases where there's no alternative to a good old fashioned binary.

Imagine that some of your remote systems need new applications installed so the team members using those computers will be able to perform some business function. Being able to leverage the integration and automation of one of the major Linux repository systems - like Debian or RPM - can make your administration tasks a whole lot easier. 

In this article we'll explore a relatively new standalone package management system: Snap.

As Linus Torvalds never tires of reminding us, the problem with many Linux software managements systems is that there are too many Linux software management systems. 

App development and even Linux adoption have, over the years, become more complicated. All the time and work you invest in preparing your software for, say, Debian repos, won't help you if you want to get them into RPM systems. And neither will help for SUSE's zypper manager.

As I show in [my Pluralsight course: Linux System Maintenance and Troubleshooting](https://pluralsight.pxf.io/VMKQj), one promising solution to the software silo problem is to distribute applications with their own self-contained environments that'll work on any Linux distribution. 

The two big standards in this young and growing field are AppImage and snap. We'll start with snaps.

## Working with Snaps

The snap system - under the guidance of Canonical, the company that sponsors Ubuntu - installs each individual application on your system within its own virtual partition. All those loop partitions sure make a royal mess of the output of the df command, but they also represent a rational approach to distributing a single version of software across any and all Linux installations.

```
$ df
Filesystem     1K-blocks      Used Available Use% Mounted on
udev             7101884         0   7101884   0% /dev
tmpfs            1432092      3936   1428156   1% /run
/dev/sda2      479152840 183520724 271222724  41% /
tmpfs            7160452    329336   6831116   5% /dev/shm
tmpfs               5120         4      5116   1% /run/lock
tmpfs            7160452         0   7160452   0% /sys/fs/cgroup
/dev/loop2           384       384         0 100% /snap/gnome-characters/539
/dev/loop4         56320     56320         0 100% /snap/core18/1705
/dev/loop5         56320     56320         0 100% /snap/core18/1754
/dev/loop3        145664    145664         0 100% /snap/slack/23
/dev/loop0          2560      2560         0 100% /snap/gnome-calculator/730
/dev/loop6         15360     15360         0 100% /snap/aws-cli/130
[...]
/dev/loop21       521216    521216         0 100% /snap/onlyoffice-desktopeditors/38
/dev/loop22       145664    145664         0 100% /snap/slack/22
/dev/loop23       185472    185472         0 100% /snap/spotify/36
/dev/loop25        96128     96128         0 100% /snap/core/8935
/dev/loop26       319104    319104         0 100% /snap/onlyoffice-desktopeditors/43
/dev/loop27         1152      1152         0 100% /snap/drawing/16
/dev/loop24        56192     56192         0 100% /snap/gtk-common-themes/1502
/dev/loop31         2560      2560         0 100% /snap/gnome-calculator/748
/dev/sda1         523248      6152    517096   2% /boot/efi
tmpfs            1432088        12   1432076   1% /run/user/121
tmpfs                100         0       100   0% /var/lib/lxd/shmounts
tmpfs                100         0       100   0% /var/lib/lxd/devlxd
tmpfs            1432088        68   1432020   1% /run/user/1000

```

In this demo, I'm going to show you how to package a GitHub-based application as a snap. With such a package, you would theoretically be able to submit it to the official snap store where, if accepted, it would be freely available to anyone on earth.

Now, I could pretend that I worked tirelessly to figure out the very best way to get all this done from the command line - but that wouldn't be completely honest. Actually, it wouldn't be honest at all. 

In fact, I simply used the "first snap" tutorial on [the snapcraft.io website](https://snapcraft.io/) that lets you select a language and then helpfully guides you through each step of the process. At the very end, it shows you how to submit your snap to the official snap store. 

I'm going to take you through the process from the command line but, if you're doing this for yourself, it would probably make sense to check out the website to make sure nothing has changed.

So let's begin. You'll first need to make sure that the virtual machine manager Multipass is properly installed, since that's what snap uses to create the VMs where the images will be build. Naturally, Multipass itself is available as a snap. 

Likewise, you'll need the snapcraft package. After installing snapcraft, you should follow it up with "hash -r" to refresh the list of places your shell will look for known programs.

```
$ sudo snap install multipass --classic
$ sudo snap install snapcraft --classic
$ hash -r

```

As I went with Python for my language, the tutorial provided me with a link to the GitHub site of an open source Python email backup project called OfflineIMAP. Don't feel you're restricted to Python, for that matter. And, obviously, you can substitute your own project for the example. 

When I've cloned the project locally, I'll cd into the new offlineimap directory. Next, I'll use wget to download the special Python-specific version of the YAML configuration file. 

Since there's already a file with that name in the directory, this one will get an alternative name, so I'll just overwrite the old copy by changing the name of the new one. We'll then open the file and edit the three places where the word "name" appears in curly braces. I need to replace those with the name I'd actually like to use.

```
$ git clone https://github.com/snapcraft-docs/offlineimap
$ cd offlineimap
$ wget https://snapcraft.io/first-snap/python/snapcraft.yaml

```

From here, running "snapcraft" will take care of the packaging process. This can be a long process, especially if there's software you need - like Multipass - that's not yet installed and set up. You may see some errors, but the odds are that the install script with automatically fix them on the fly. 

When that's all died down, you can install the snap locally using the regular "snap install" command, but you'll need to add --devmode and --dangerous because this isn't an official, supported snap so, technically, no one knows what might happen when you start it up. 

You can prove it's installed by running "snap list" and then confirm that everything worked by running the test-offlineimap-mysnap command with -h to get the help screen. 

Enjoy the software - I know that this kind of email backup is something I've been meaning to get to for years.

```
$ snapcraft
$ sudo snap install --devmode --dangerous *.snap
$ snap list
$ test-offlineimap-mysnap -h

```

If you're interested in learning how to manage snaps within your Linux environment, you might also enjoy my "[How to manage Ubuntu Snaps: the stuff no one tells you](https://www.freecodecamp.org/news/managing-ubuntu-snaps/)" and "[snapd Makes Administering Nextcloud a Snap](https://www.freecodecamp.org/news/snapd-nextcloud/)" articles.

## Working with other package managers

We just got a pretty good look at snaps. But perhaps now is the perfect time to admit that I've left out some other big players in the alternative package manager world, in particular [Flatpak](https://flatpak.org/setup/) and [AppImages](https://appimage.org/). 

I discuss AppImages in some depth [here](https://opensource.com/article/20/6/appimages), but a quick word or two about Flatpak wouldn't be out of place here.

Flatpak's primary goal is to let developers build their applications into a single package and then distribute them to any Linux distribution. As an end-user, you would install the Flatpak system using your regular software manager - like Apt on Ubuntu or Yum on CentOS. Flatpak is installed by default on Fedora. From there, it's pretty much smooth sailing. Solves all the right problems, doesn't it?

Perhaps. There's been some [recent criticism](https://flatkill.org/) over possible (and significant) security weaknesses in the fundamental design of Flatpak. I'll let you decide for yourself.

_There's much more administration goodness in the form of books, courses, and articles available at my [bootstrap-it.com](https://bootstrap-it.com/)._

