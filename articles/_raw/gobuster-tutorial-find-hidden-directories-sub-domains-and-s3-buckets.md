---
title: Gobuster Tutorial – How to Find Hidden Directories, Sub-Domains, and S3 Buckets
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2022-12-05T23:40:58.000Z'
originalURL: https://freecodecamp.org/news/gobuster-tutorial-find-hidden-directories-sub-domains-and-s3-buckets
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/Stealth-Security---Blog-Banner--25-.png
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
seo_desc: 'There’s much more to web servers and websites than what appears on the
  surface.

  The first step an attacker uses when attacking a website is to find the list of
  URLs and sub-domains. Web developers often expose sensitive files, URL paths, or
  even sub-...'
---

There’s much more to web servers and websites than what appears on the surface.

The first step an attacker uses when attacking a website is to find the list of URLs and sub-domains. Web developers often expose sensitive files, URL paths, or even sub-domains while building or maintaining a site.

This is a great attack vector for malicious actors.

For example, if you have an e-commerce website, you might have a sub-domain called “admin”. This might not be linked anywhere on the site but since the keyword “admin” is common, the URL is very easy to find. This is why you must often scan your websites to check for unprotected assets.

The usual approach is to rely on passive enumeration sites like [crt.sh](http://crt.sh/) to find sub-domains. But these passive approaches are very limited and can often miss critical attack vectors.

Gobuster is a tool that helps you perform active scanning on web sites and applications. Attackers use it to find attack vectors and we can use it to defend ourselves.

In this article, we’ll learn to install and work with Gobuster. We will also look at the options provided by Gobuster in detail. Finally, we will learn how to defend against these types of brute-force attacks.

Note: **All my articles are for educational purposes.** If you use this information illegally and get into trouble, I am not responsible. Always get permission from the owner before scanning / brute-forcing / exploiting a system.

## **What is Gobuster?**

Written in the [Go language](https://go.dev/), Gobuster is an aggressive scanner that helps you find hidden Directories, URLs, Sub-Domains, and S3 Buckets seamlessly.

This is where people ask: [What about Ffuf](https://blog.stealthsecurity.io/fuzzing-web-applications-using-ffuf-c4ad74190b72)?

Ffuf is a wonderful web fuzzer, but Gobuster is a faster and more flexible alternative. Gobuster also has support for extensions with which we can amplify its capabilities. Gobuster also can scale using multiple threads and perform parallel scans to speed up results.

## **How to Install Gobuster**

Let’s see how to install Gobuster. If you are using Kali or Parrot OS, Gobuster will be pre-installed.

If you are using Ubuntu or Debian-based OS, you can use `apt` to install Gobuster.

```
$ apt install gobuster
```

To install Gobuster on Mac, you can use Homebrew.

```
$ brew install gobuster
```

To install Gobuster on Windows and other versions of Linux, you can find the [installation instructions here](https://github.com/OJ/gobuster).

Once you have finished installing, you can check your installation using the help command.

```
$ gobuster -h 
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-1.png)
_Gobuster help command_

## **What are Wordlists?**

If you are new to wordlists, a wordlist is a list of commonly used terms. This can be a [password wordlist](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt), [username wordlist](https://github.com/danielmiessler/SecLists/blob/master/Usernames/Names/names.txt), subdomain wordlist, and so on. You can find a lot of [useful wordlists here](https://github.com/danielmiessler/SecLists).

I would recommend downloading [Seclists](https://github.com/danielmiessler/SecLists). Seclists is a collection of multiple types of lists used during security assessments. This includes usernames, passwords, URLs, etc. If you are using Kali Linux, you can find seclists under /usr/share/wordlists.

To try Gobuster in real-time, you can either use your own website or use a practice web app like the [Damn Vulnerable Web app](https://github.com/digininja/DVWA) (DVWA). DVWA is an intentionally misconfigured vulnerable web application that is used by pen testers for practicing web application attacks.

## **How to Work with Gobuster**

Now that we have installed Gobuster and the required wordlists, let’s start busting with Gobuster.

Note: I have DWVA running at 10.10.171.247 at port 80, so I ll be using that for the examples. Just replace that with your website URL or IP address. I'll also be using Kali linux as the attacking machine.

If you look at the help command, we can see that Gobuster has a few modes.

1. dir — Directory enumeration mode.
2. dns — Subdomain enumeration mode.
3. fuzz — Fuzzing mode.
4. s3 — S3 enumeration mode.
5. vhost — Vhost enumeration mode.

In this article, we will look at three modes: dir, dns, and s3 modes.

Each mode serves a unique purpose and helps us to brute force and find what we are looking for. Let's look at the three modes in detail.

### How to use directory mode (dir)

Gobuster's directory mode helps us to look for hidden files and URL paths. This can include images, script files, and almost any file that is exposed to the internet.

Here is the command to run the dir mode:

```
$ gobuster dir -u <url> -w <wordlist>
```

We can also use the help mode to find the additional flags that Gobuster provides with the dir mode.

```
$ gobuster dir -h
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-2.png)
_Gobuster dir mode help_

Now let’s try the dir mode. Here is the command to look for URLs with the common wordlist.

```
$ gobuster dir -u 10.10.171.247:80 -w /usr/share/wordlists/dirb/common.txt
```

And here is the result. We can see that there are some exposed files in the DVWA website.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-3.png)
_dir enumeration results_

If we want to look just for specific file extensions, we can use the -x flag. Here is a sample command to filter images:

```
$ gobuster dir -u 10.10.171.247:80 -w /usr/share/wordlists/dirb/common.txt -x jpg,png,jpeg
```

### How to use DNS mode (dns)

You can use DNS mode to find hidden subdomains in a target domain. For example, if you have a domain named mydomain.com, sub-domains like admin.mydomain.com, support.mydomain.com, and so on can be found using Gobuster.

Let’s start by looking at the help command for dns mode.

```
$ gobuster dns -h
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-4.png)
_Gobuster dns help_

To execute a dns enumeration, we can use the following command:

```
$ gobuster dns -d mydomain.com -w /usr/share/wordlists/dirb/common.txt
```

Since we can't enumerate IP addresses for sub-domains, we have to run this scan only on websites we own or the ones we have permission to scan.

```
$gobuster s3 -h
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-5.png)
_Gobuster S3 mode help_

S3 mode was recently added to Gobuster and is a great tool to discover public S3 buckets. Since S3 buckets have unique names, they can be enumerated by using a specific wordlist.

For example, if we have a company named Acme, we can use a wordlist with acme-admin, acme-user, acme-images, and so on. This wordlist can then be fed into Gobuster to find if there are public buckets matching the bucket names in the wordlist.

Here is the command to execute an S3 enumeration using Gobuster:

```
$gobuster s3 -w bucket_list.txt
```

## **How to Defend Against Gobuster**

Gobuster is a remarkable tool that you can use to find hidden directories, URLs, sub-domains, and S3 Buckets.

But this enables malicious hackers to use it and attack your web application assets as well. So how do we defend against Gobuster?

You can use the following steps to prevent and stop brute-force attacks on your web application.

1. **Audit yourself:** Use Gobuster on your own applications and perform an audit. This will help you find the information that will be visible to the attackers.
2. **Apply security policies:** To prevent resources like S3 from being exposed on the internet, use AWS bucket policies to prevent unauthorized access.
3. **Use bot protection solutions:** Bot protection services like Cloudflare will stop any brute-force attacks making it incredibly difficult to attack your web application.

## **Conclusion**

Gobuster is a fast brute-force tool to discover hidden URLs, files, and directories within websites. This will help us to remove/secure hidden files and sensitive data.

Gobuster also helps in securing sub-domains and virtual hosts from being exposed to the internet. Overall, Gobsuter is a fantastic tool to help you reduce your application’s attack surface.

_Loved this article? Join_ [_Stealth Security Weekly Newsletter_](https://tinyletter.com/stealthsecurity) _and get articles delivered to your inbox every Friday. You can also_ [_connect with me_](https://www.linkedin.com/in/manishmshiva/) _on Linked_I_n._

  

