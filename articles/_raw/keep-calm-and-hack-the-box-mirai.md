---
title: Keep Calm and Hack The Box - Mirai
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2020-08-28T19:41:51.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-mirai
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/cyberpunk-city-rt-2560x1440.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: Linux
  slug: linux
- name: penetration testing
  slug: penetration-testing
seo_title: null
seo_desc: 'Hack The Box (HTB) is an online platform that allows you to test your penetration
  testing skills.

  It contains a number of challenges that are constantly updated. Some of them simulate
  real world scenarios and some of them lean more towards a CTF styl...'
---

Hack The Box (HTB) is an online platform that allows you to test your penetration testing skills.

It contains a number of challenges that are constantly updated. Some of them simulate real world scenarios and some of them lean more towards a CTF style of challenge.

**Note**: _Only write-ups of retired HTB machines are allowed._

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-19-at-23.43.57.png)

Mirai is a good example of how improperly configured IoT devices led to one of the largest attack vectors in 2016. IoT devices are actively being exploited by botnets and used for long-term persistence by attackers.

We will use the following tools to pawn the box on a [Kali Linux box](https://www.kali.org/):

* nmap
* gobuster
* Medusa
* Linux commands

Let's get started.

## **Step 1 - Reconnaissance**

The first step before exploiting a machine is to do a little bit of scanning and reconnaissance.

This is one of the most important parts as it will determine what you can try to exploit afterwards. It is always better to spend more time on this phase to get as much information as you can.

### **Port scanning**

I will use **Nmap** (Network Mapper). Nmap is a free and open source utility for network discovery and security auditing.

It uses raw IP packets to determine what hosts are available on the network, what services those hosts are offering, what operating systems they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics.

There are many commands you can use with this tool to scan the network. If you want to learn more about it, you can have a look at the documentation [here](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-00.42.40.png)

I use the following command to perform an intensive scan:

```bash
nmap -A -v 10.10.10.48
```

**`-A`:** Enables OS detection, version detection, script scanning, and traceroute

**`-v`:** Increases verbosity level

**`10.10.10.48`**:**** IP for the Mirai box

If you find the results a little bit too overwhelming, you can try this:

```bash
nmap 10.10.10.48
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-00.40.16.png)

We can see that there are 3 open ports:

**Port** 22. Secure Shell (SSH), secure logins, file transfers (scp, sftp) and port forwarding

**Port 53**. Domain Name System (DNS)

**Port** 80. Hypertext Transfer Protocol (HTTP). Here it's an IIS server.

## **Directory scanning**

I use **Gobuster**. Gobuster is a directory scanner written in Go. You can find more info on the tool [here](https://tools.kali.org/web-applications/gobuster). 

Gobuster uses wordlists on Kali which are located in the **/usr/share/wordlists** directory. I'm using wordlists from **dirb** and **dirbuster**, but you can download more wordlists from **SecLists** [here](https://github.com/danielmiessler/SecLists).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.33.47.png)

I use this command for the dirb common.txt wordlist:

```bash
gobuster dir -u 10.10.10.48 -w /usr/share/wordlists/dirb/common.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-00.46.18.png)

I can see some interesting folders. I do another directory scan with a different wordlist.

```bash
gobuster dir -u 10.10.10.48 -w /usr/share/worldlists/dirbuster/directory-list-lowercase-2.3-medium.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-14.31.32.png)

The **admin** folder is definitely one I will visit!

## **Step 2 - Visiting the web page**

From the reconnaissance phase, I decide to start with port 80. And I get a blank page.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-00.57.33.png)

From the reconnaissance phase, I found the **/admin** folder with **Gobuster**. I navigate to this endpoint:

```bash
10.10.10.48/admin
```

I arrive on a Pi-hole admin dashboard.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-01.00.10.png)

> **Pi-hole** is a Linux network-level advertisement and Internet tracker blocking application which acts as a DNS sinkhole and optionally a DHCP server, intended for use on a private network.   
>   
> Pi-hole has the ability to block traditional website advertisements as well as advertisements in unconventional places, such as smart TVs and mobile operating system advertisements - Wikipedia

You can read more [here](https://en.wikipedia.org/wiki/Pi-hole) or learn more on the [official website](https://pi-hole.net/).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-14.36.48.png)

I click on the **Login** button on the left sidebar and I'm presented with a login screen. A quick search on the Internet, and I can assume that the target is a Raspberry Pi machine, and most likely running [Raspbian](https://en.wikipedia.org/wiki/Raspberry_Pi_OS) (Raspberry Pi's OS). 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-01.00.27.png)

I also found out that the default username should be "pi" with password "raspberry". I try the default password on this login screen, but it doesn't seem to work. We need to find another way.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-14.50.47.png)

## **Step 3 - Connecting to the Pi-hole through SSH**

During the reconnaissance phase, we found out that port 22 was open. 

I use **Medusa** to check if the default credentials work with ssh. Medusa is a speedy, parallel, and modular login brute-forcer. You can find more information [here](https://en.kali.tools/?p=200) on this tool.

```bash
medusa -h 10.10.10.48 -u pi -p raspberry -M ssh
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-15.55.01.png)

Let's now connect using SSH with the following command, as we've just validated that the password is working:

```bash
ssh pi@10.10.10.48
```

To connect with SSH, you need the username and the host IP address. In our case, that would be"pi" for the username and "10.10.10.48" for the IP address. The password is "raspberry".

I get a session as:

```bash
pi@raspberrypi
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-01.45.08.png)

Once logged in as a user, I can verify whether or not the user belongs to the sudo group using either the **id** or **groups** commands:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-14.56.55.png)

The user belongs to the group **root**.

## **Step 4 - **Looking for the user.txt flag****

I list all the files/folders with the following command:

```bash
ls -la
```

I then move to the **Desktop** with

```bash
cd Desktop
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-15.00.25.png)

And I find the user flag! I can check the contents of the file with

```bash
cat user.txt
```

## **Step 5 - **Looking for the root.txt flag****

Let's find the root flag now. I navigate up to the **/** folder. You can check where you are with the command

```bash
pwd
```

which gives us the print working directory. I then move to the **/root** folder but access is denied.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-15.02.28.png)

I need to change to the root user to access this folder. I use the command

```bash
sudo -l
```

to understand which command I can run on localhost. 

The root user has unlimited privileges and can run any command on the system and we know that the user pi is part of the root group.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-01.48.25.png)

I use the command

```bash
sudo su
```

The **sudo** command allows you to run programs as another user. By default the root user. **su** means switch user. 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-01.48.58.png)

I can now navigate to the **root** folder. I find the root.txt file and check its content with

```bash
cat root.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-01.49.46.png)

Unfortunately for us, it's not the flag but a message that was left instead.

```bash
I lost my original root.txt! I think I may have a backup on my USB stick...
```

I now need to find where the usb is located with the command

```bash
lsblk
```

to list USB block storage devices. I can see there's one **usbstick** in the **/media** folder:

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-15.25.26.png)

I navigate to this folder and find another message from a user called **James**.

```bash
Damnit! Sorry man I accidentally deleted your files off the USB stick.
Do you know if there is any way to get them back?

-James
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-15.16.48.png)

When we listed all the storage devices, we saw that the usbstick was located at **sdb**, which is under **/dev/sdb/**. More info [here](https://help.ubuntu.com/lts/installation-guide/armhf/apcs04.html) on disks and partitioning.

If we use the following command:

```bash
cat /dev/sdb
```

We will have a long output with a lot of weird characters. At the end of this input you should find the **root** flag.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-15.38.56.png)

A more elegant way to see the text inside a binary or data file is to use the command **strings**. This command pulls those bits of text—called “strings”.

```bash
strings /dev/sdb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-15.41.41.png)

Congrats! You found both flags.

## **Remediations**

* You can read more about the Mirai DDoS botnet attack [here](https://www.imperva.com/blog/malware-analysis-mirai-ddos-botnet/)
* Don't use default/generic passwords
* Disable remote access to your devices when not needed

Please don’t hesitate to comment, ask questions, or share with your friends :)

You can see more articles from the series **Keep Calm and Hack the Box** [here](https://www.freecodecamp.org/news/search/?query=keep%20calm%20and%20hack%20the%20box).

You can follow me on [Twitter](https://twitter.com/SonyaMoisset) or on [LinkedIn](https://www.linkedin.com/in/sonyamoisset/).

And don't forget to #**GetSecure**, #**BeSecure** & #**StaySecure**!

![Image](https://www.freecodecamp.org/news/content/images/2020/08/cyberpunk-city-rt-2560x1440-1.jpg)

