---
title: How to Run Commands on Multiple Linux Hosts Using PSSH
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-01-09T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/running-commands-linux-hosts-using-pssh
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e08740569d1a4ca3af6.jpg
tags:
- name: Linux
  slug: linux
- name: Orchestration
  slug: orchestration
- name: ssh
  slug: ssh
- name: virtualization
  slug: virtualization
seo_title: null
seo_desc: I'm sure you've heard that all the cool kids are playing with orchestration
  automation these days. But do you know why? Well first, the resources consumed by
  modern microservices workloads are becoming much more complex and deploy to far
  more instanc...
---

I'm sure you've heard that all the cool kids are playing with orchestration automation these days. But do you know why? Well first, the resources consumed by modern microservices workloads are becoming much more complex and deploy to far more instances than ever before. And second, more and more of those resources are virtual rather than physical - so many of them will only exist for minutes or even seconds.

All of which means that even if you wanted to go around logging into each of your many servers, it just wouldn't make sense. In most cases in fact, it wouldn't even be possible. Instead, you're going to be running a lot of clever scripts. And the tools you use to run those kinds of scripts are generally called orchestrators.

I'm sure you've encountered at least one or two members of the orchestration club. Besides Ansible, there's Terraform, Chef, Puppet and others. But there are also lower-level tools that work as add-ons to core Linux tools like SSH. Although, seeing how it'll run natively on Windows and, of course, macOS, I'm not sure it's quite correct to call SSH a "Linux" tool any more. 

One of those SSH add-ons is a tool set called pssh - which stands for Parallel SSH. That's what we're going to be learning about in this article - which is excerpted from my new [Pluralsight course, Linux System Optimization](https://pluralsight.pxf.io/RqrJb).

For now, though, I'm going to tell you a bit about the lab I'm using so that you can more easily reproduce it and follow along at home. I've got three Ubuntu [LXD containers](https://www.freecodecamp.org/news/linux-containers-lxc-lxd/) running. The base for all of our operations will be the one with an IP address of 10.0.3.140, while the two host nodes we'll be remotely provisioning will use 10.0.3.93 and 10.0.3.43.

Everything we'll do assumes that we've got passwordless SSH access from my base container to each of the two nodes. If you're not sure how to do that, you can view the SSH module of my [Protocol Deep Dive: SSH and Telnet course](https://pluralsight.pxf.io/9DYVe) on Pluralsight. If you're in a hurry, [this Red Hat tutorial](https://www.redhat.com/sysadmin/passwordless-ssh) will get you to the same place.

Installing pssh on Ubuntu is simple and quick: `sudo apt install pssh`. It doesn't get any harder on CentOS.

I created a simple host inventory file called sshhosts.txt that contains nothing more than the IP addresses of my two nodes:

```
$ less sshhosts.txt
10.0.3.93
10.0.3.43

```

Now I'm going to run the pssh parallel-ssh command to execute a single command on my hosts.

```
$ parallel-ssh -i -h sshhosts.txt df -ht ext4


```

-i tells the program to run as interactive - otherwise we wouldn't be shown any command output. -h points to the hosts file that I called sshhosts.txt. And the command itself will be the old Unix utility df. That'll return a list of drives attached to the system along with their mount points and usage information. The -h here will display disk space in human readable units and the t will restrict access to only drives formatted as ext4. 

Why do I care about that ext4 business? Because Ubuntu uses the snap package manager and each snap creates its own virtual device. So what? Well, I don't want to have to comb through a dozen or so virtual devices reporting 0 free space just to get to the real drives reporting actual usage.

```
$ parallel-ssh -i -h sshhosts.txt df -ht ext4
[1] 22:02:00 [SUCCESS] 10.0.3.43
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda2       457G  131G  304G  30% /
[2] 22:02:00 [SUCCESS] 10.0.3.93
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda2       457G  131G  304G  30% /

```

And there you go! Full disk space information about both of my nodes. I'm sure you noticed that the information is identical. That's because these are both containers running on my workstation, so as far as they know, they both have full access to my own drive.

For my next trick, I'll collect the /etc/group files from each of my nodes. This is the kind of operation that could be useful to quickly monitor the security status of your nodes. You could add a script that parses the incoming data and alerts you if there are any anomalies. 

Before I begin, I'll create a directory locally called host-files. Then I'll use the `parallel-slurp` command - whose name wonderfully describes its function. Again, -h points to the hosts file. The `-L` sets the host-files directory as the target location for writing the data we're going to generate, `/etc/group` is the remote file we want to slurp up, and `group` is the name we'd like to assign the data locally.

```
mkdir host-files
parallel-slurp -h sshhosts.txt -L host-files/ /etc/group group

```

When it's done, your host-files directory will contain sub-directories named after the IP address of each of your nodes. As you can see, there's a file called "group" that contains the /etc/group data from each node.

```
$ tree host-files/
host-files/
├── 10.0.3.43
│   └── group
└── 10.0.3.93
    └── group

```

Does pssh come with any other treats? Yup. And running `apropos` gives you the whole list.

```
$ apropos parallel
parallel-nuke (1)    - parallel process kill program
parallel-rsync (1)   - parallel process kill program
parallel-scp (1)     - parallel process kill program
parallel-slurp (1)   - parallel process kill program
parallel-ssh (1)     - parallel ssh program

```

_This article is based on content in my [Pluralsight course, "Linux System Optimization."](https://pluralsight.pxf.io/RqrJb) There's much more administration goodness in the form of books, courses, and articles available at [bootstrap-it.com](https://bootstrap-it.com)._

