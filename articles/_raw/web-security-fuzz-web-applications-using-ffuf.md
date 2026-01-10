---
title: How to Fuzz Web Applications using FFuf – Web Security Tutorial
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2022-11-10T17:21:43.000Z'
originalURL: https://freecodecamp.org/news/web-security-fuzz-web-applications-using-ffuf
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/ffuf.png
tags:
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: Web Security
  slug: web-security
seo_title: null
seo_desc: 'Building strong authentication systems is crucial for web applications.
  Now that many businesses have a growing online presence, a malicious actor taking
  control of your website can be devastating.

  In this article, we will learn how to use Ffuf, a fa...'
---

Building strong authentication systems is crucial for web applications. Now that many businesses have a growing online presence, a malicious actor taking control of your website can be devastating.

In this article, we will learn how to use Ffuf, a fast web fuzzer written in Go. You will learn how to fuzz your way to find directories and files and bypass the authentication of a website using ffuf. Then you'll learn how to defend against these types of attacks.

Remember – to protect yourself and your websites, it helps to know how an attacker would try to get in. That way, you can more effectively keep them out.

**Note:** Before we dive into using ffuf, I would like to emphasize that this tutorial is only meant to help you defend yourself against fuzzing attacks. If you use this material for malicious purposes, I am not responsible.

## What is FFuf?

Ffuf is a fuzzer written in the [Go programming language](https://go.dev/).

Ffuf belongs to the exploitation phase in the [pentesting lifecycle](https://exploitable.manishmshiva.com/ethical-hacking-lifecycle-five-stages-of-a-penetration-test-c201e8e5bbf7). It is also the fastest open-source fuzzing tool available in the market. 

But before we start using Ffuf, let's understand what fuzzing is.

## What is Fuzzing?

Fuzzing is a method of sending malformed or abnormal data to a system in order to get it to misbehave in some way, which could lead to the discovery of vulnerabilities.

Finding hidden files, sending random data to forms, or even login attempts to web applications can be considered fuzzing.

Then you might be wondering “How is it different from Brute forcing?”.

Brute forcing can be considered a part of fuzzing. In brute force, the attacker uses valid data, for example, to check if a login attempt works. But with Fuzzing, they can send random data to break the expected behavior of a system.

For example, if you use a tool like Ffuf and load it with hundreds of username-password combinations to try on a website, it is fuzzing. And that’s exactly what we will do using Ffuf.

Make sure you have written permission if you are going to try this tool on a third-party website.

## How to Install Ffuf and Wordlists

Ffuf comes pre-packaged with the Kali Linux distribution. If you want to install Ffuf on your personal computer, [here are the instructions](http://ffuf.me/install). 

Since Ffuf is written in the Go programming language, make sure you have the Go compiler installed in your system before trying to install Ffuf.

If you are new to wordlists, a wordlist is a list of commonly used terms. This can be a [password wordlist](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt), [username wordlist](https://github.com/danielmiessler/SecLists/blob/master/Usernames/Names/names.txt), subdomain wordlist, and so on. You can find a lot of [useful wordlists here](https://github.com/danielmiessler/SecLists).

I would recommend downloading [Seclists](https://github.com/danielmiessler/SecLists). Seclists is a collection of multiple types of lists used during security assessments. This includes usernames, passwords, URLs, etc. If you are using Kali Linux, you can find seclists under /usr/share/wordlists.

To try this tool in real-time, you can either use your own website or use a practice web app like the [Damn Vulnerable Web app](https://github.com/digininja/DVWA) (DVWA). DVWA is an intentionally misconfigured vulnerable web application that is used by pen testers for practicing web application attacks.

## Fuzzing with Ffuf

Now that you understand what Fuzzing and Wordlists are, let's start using Ffuf.

We will use ffuf to fuzz the web application to discover directories, find usernames, enumerate virtual hosts, and even brute-force email/password combinations.

You can use the help command (-h) if you want to quickly look at the options provided by Ffuf. This is useful since you don't have to memorize all the options provided by Ffuf. 

```
ffuf -h
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-26.png)

Do remember that the URL (-u) and wordlist (-w) parameters are always required.

Note that I'll be using [http://localhost:3000](http://localhost:3000) for my examples. If you setup your own web app or use an existing website, you have to replace “localhost:3000” with the ip address or the domain name of the website.

### How to Enumerate URLs with Ffuf

Let's see how to find some URL paths.

Finding URLs is useful, especially if they are being hidden from being publicly indexed. We will use the [web content wordlist](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/big.txt) from seclists to fuzz the web app for hidden URLs.

You can use the following command to look for URLs:

```
ffuf -u http://localhost:3000/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt
```

Here, the “FUZZ” keyword is used as a placeholder. Ffuf will try to hit the URL by replacing the word “FUZZ” with every word in the wordlist.

Here is what I found from the DVWA:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-27.png)
_Result of looking for URLs_

Interesting. You can see that we have found a few (possibly important) locations like /config, /docs, and /server-status.

If a real-world web app had pages that were not linked anywhere but used standard names, Ffuf would easily spot them.

### How to Enumerate Files with Ffuf

What if you want to look for specific files? Thankfully, Ffuf provides us with the extension option (-e) that we can use. We can tell Ffuf to look only for files that have certain extensions – in our case, .html,.php, and .txt.

We will be using the [raft-medium-words](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/raft-medium-words-lowercase.txt) wordlist for this. Here is the command to look for specific files:

```
ffuf -u http://localhost:3000/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-words-lowercase.txt -e .php,.html,.txt
```

This command looks for all the files at the root of the domain with an extension of .html, .php, and .txt. Here is the result from DVWA:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-28.png)
_Result of looking for specific files_

We have found a long list of files. Even if some files are not served on the web app (403 status), we can learn that there are files, just that we cannot access them yet.

Let’s run the same command, but now, we will only look for files that are accessible to the public. We will use the match code (-mc) flag to only look for files with a status of 200.

Here is the command:

```
ffuf -u http://localhost:3000/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-words-lowercase.txt -e .php,.html,.txt -mc 200
```

And here is the result.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-31.png)
_Files accessible to the public_

You can see that we have found a few files that we can access. The login.php looks interesting, and we will use it for bypassing authentication in the following sections.

### How to Enumerate Sub Domains using Ffuf

You can also look for sub-domains in a web app using Ffuf.

You might have guessed the approach that we are going to use. We will replace the subdomain of the URL with the word “FUZZ” and try looking for URLs that are up.

Since my web app is hosted on my local system, it does not contain any subdomains. But in the real world, if you want to enumerate subdomains, here is the command. You can use the [sub domains wordlist](https://github.com/danielmiessler/SecLists/blob/master/Discovery/DNS/subdomains-top1million-5000.txt) from seclists. 

```
ffuf -u http://FUZZ.mydomain.com -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
```

### How to Find Usernames with Ffuf

Have you been annoyed when web applications don’t tell you whether you have the wrong username or password? They just tell you “This combination doesn’t work”.

This is to protect the web app from username/email fuzzing attacks. If authentication systems give you specific information about your login attempt, it gets easier for attackers to brute force and discover a list of usernames or emails.

Let’s assume that our web application tells you that you have the wrong username with the message “username does not exist”. We can use this error message to find valid usernames with the following command:

```
ffuf -w /usr/share/SecLists/Usernames/top-usernames-shortlist.txt -X POST -d "username=FUZZ&&password=x" -H "Content-Type: application/x-www-form-urlencoded" -u http://mydomain.com/login -mr "username already exists"
```

Here, we are sending POST requests to the login page, with the fuzzed usernames and a dummy password to check if the expected error message is returned. You can use a [username wordlist](https://github.com/danielmiessler/SecLists/blob/master/Usernames/top-usernames-shortlist.txt) from seclists for fuzzing.

The -mr flag is used to match a regular expression. You can have complicated regular expressions or a simple string message to validate the requests.

Here is a sample response.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-32.png)

### Brute Forcing using Ffuf

Now, let's do some brute forcing with Ffuf. We will try a bunch of common username/password combinations and see if anything works.

If the web application you are testing uses a combination of email and password, you can replace the username wordlist with a email wordlist.

So for this attack, we need two parameters: username and password. Also, we will be using two-word lists: as you guessed, a username wordlist and a password wordlist.

In addition the default placeholder **FUZZ,** Ffuf supports the use of variables. So we will use W1 for our username wordlist and W2 for the password wordlist.

Here is the command: 

```
ffuf -w usernames.txt:W1,/usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u http://localhost:3000/login -fc 200
```

If Ffuf finds any valid combinations, you will see the combination in the results. You can also filter by status codes (for examle filter 400 or look for 200) using the -fc or -mc flags to reduce the noise.

Here is a sample response.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-33.png)

That was fun, wasn’t it? We can find a lot of interesting information about a web app without using a complicated tool like [Burpsuite](https://www.kali.org/tools/burpsuite/).

## How to Protect Your Site from Fuzzing

But since we are not the malicious attackers, let’s look at how to defend against fuzzing.

The easiest way to protect your website from fuzzing attacks is to be careful about the type of files on the web server. If you don't want something to be found, don't put it on the web server.

To prevent authentication bypass, it is important not to allow multiple attempts to log in. Most modern websites don't allow more than 5 consecutive login attempts. It is more secure to ask your users to reset their passwords via email instead of letting them try multiple combinations.

You should also be careful about the error messages returned on failed attempts. Displaying that “Email does not exist” or “Password not correct” will let the hacker know that an email or username exists. This just makes their job easier.

Finally, you can use [Web Application Firewalls](https://www.cloudflare.com/en-gb/learning/ddos/glossary/web-application-firewall-waf/) (WAF) to monitor traffic and block suspicious IP addresses. WAFs also have options to set alerts if it comes across brute forcing attempts on your authentication methods.

## Summary

Ffuf is a great tool to have in your pentesting toolkit. It is a simple yet fast fuzzer that makes it easy to enumerate directories, discover virtual hosts, and brute-force web applications.

Ffuf also has more options that will help you to look for specific information. It has support for regular expressions, rate limiting of requests, and saving your results to a file.

Hope you enjoyed this article. You can [connect with me on Linkedin](https://www.linkedin.com/in/manishmshiva/) or [read more articles on my blog](https://blog.manishmshiva.com/). I’ll see you soon with another article.

