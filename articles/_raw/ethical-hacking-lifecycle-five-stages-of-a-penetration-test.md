---
title: The Ethical Hacking Lifecycle — Five Stages Of A Penetration Test
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-09-09T20:34:06.000Z'
originalURL: https://freecodecamp.org/news/ethical-hacking-lifecycle-five-stages-of-a-penetration-test
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/hacking.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: penetration testing
  slug: penetration-testing
seo_title: null
seo_desc: "Penetration testing is the process of exploiting an organization’s network\
  \ in order to figure out how defend it better. \nIn this article, we'll discuss\
  \ the five steps involved in a successful penetration test.\nBefore we get into\
  \ the article, a quick ..."
---

Penetration testing is the process of exploiting an organization’s network in order to figure out how defend it better. 

In this article, we'll discuss the five steps involved in a successful penetration test.

_Before we get into the article,_ a quick disclaimer: _I would like to emphasize that I am not responsible for any damage you do trying to attack systems._ 

_It_'_s illegal_ to pen test without permission, so make sure you have it in writing _before you even try to scan a system or a network._

With that out of the way, let's get started.

## What is Cybersecurity?

Cybersecurity is one of the hottest fields to be in, thanks to so many companies going remote. Cyber threats are increasing and cybercriminals are finding new ways to exploit systems.

Penetration testing is how ethical hackers work. They think like bad hackers and attack their own systems. This helps them understand their strengths and weaknesses and protect their organizational assets.

A pen-test is comprised of multiple stages. You cannot simply get into a system by using a tool unless the target is hopelessly vulnerable.

In most cases, systems are secured via firewalls, antivirus software, default operating system configurations, and so on. It takes the right tools, a strong skill set, and most importantly, patience, in order to successfully exploit a network.

So let's look at the five main stages a penetration tester will go through along with the tools they use to break into a network.

You can also find the [article I wrote on the top 10 tools cybersecurity professionals use here](https://www.freecodecamp.org/news/10-tools-you-should-know-as-a-cybersecurity-engineer/).

## Reconnaissance

> "Give me six hours to chop down a tree and I will spend the first four sharpening the axe." — Abraham Lincoln

Reconnaissance is the most important part of a penetration test. It is where you gain information about the target.

Reconnaissance is important because the more information you have about the target, the easier it gets when you try to gain access. Once you map out an entire network, you can identify the weakest spot and start from there.

Commonly used recon tools include [Google (yeah!)](https://en.wikipedia.org/wiki/Google_hacking) and social media sites where you can gather information about the target. If you are performing an audit of a company, you can go through the company’s job postings to see the type of technologies they use.

Once you have gained enough information, you can use a tool like [Maltego](https://www.maltego.com/) to map the targets.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/maltego.jpg)
_Maltego_

Maltego also supports has the ability to automatically import data from social networks, DNS records, and custom plugins like [FullContact](https://www.fullcontact.com/).

The important thing to remember in terms of recognisance is that you NEVER touch the target. Reconnaissance is similar to scouting and looking for information while you are far away from the target.

## Scanning

This is the part where you come in contact with the target. Scanning involves sending packets of data to the target and interpreting their response.

Scanning gives you useful information about the target like open ports, IP addresses, operating system information, services installed, and so on.

[Nmap is the best scanner to scan a network](https://medium.com/manishmshiva/nmap-a-guide-to-the-greatest-scanning-tool-of-all-time-3bd1a973a5e5). It will help you map out the network and provide detailed information about the target systems.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/nmap.png)
_Nmap_

Nmap also provides a number of CLI options including scan exports that you can then import into exploitation tools.

[Nessus](https://en.wikipedia.org/wiki/Nessus_(software)) is another scanning tool, but it is a commercial product. While Nmap will give you information about the target, Nessus will tell you how you can exploit the target by matching the vulnerabilities from the [Common Vulnerabilities and Exposures database](https://www.exploit-db.com/).

[OpenVas](https://www.openvas.org/) is another open-source alternative that is similar to Nessus.

## Exploitation

This is the part where you gain access to the system. A successful exploit should give you control of the system to at least a user level. From there you perform [privilege escalation](https://searchsecurity.techtarget.com/definition/privilege-escalation-attack) to gain root access to the target.

When it comes to exploitation, [Metasploit is hands down the best tool in the market](https://medium.com/manishmshiva/metasploit-a-walkthrough-of-the-powerful-exploitation-framework-6974c4ed0ea7). It is open-source (with a commercial version as well) and is easy to work with.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/metasploit.png)
_Metasploit_

Metasploit is updated frequently with new exploits published in the Common Vulnerabilities and Exposures (CVE) database. So you can match your scan results with the available exploits and use that exploit from Metasploit to attack the target.

Metasploit has an advanced payload called [Meterpreter](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/). Once you have gained access to the target system, Meterpreter gives you options like opening webcams, dumping password hashes, and so on. Meterpreter also lives in the memory of the target, so it is very hard to detect.

For example, if your scan results tell you that the target has Samba version 3.5, you can use the [Samba CVE-2017–7494 Remote Code Execution Vulnerability](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-7494) to send a payload through Metasploit and gain access to the target system.

Metasploit also has a GUI tool called Armitage. Armitage helps you visualize targets and it recommends exploits by matching the vulnerabilities with the exploits database.

## Maintaining Access

Gaining access to systems is not easy, especially on corporate networks. After all the hard work you have done to exploit a system, it won't make sense to go through the same process to exploit the target again.

This is where maintaining access comes in. You can install backdoors, keyloggers, and other pieces of code that let you into the system whenever you want.

Metasploit gives you tools like keyloggers and Meterpreter backdoors to maintain access to an exploited system. You can also install custom [Rootkits](https://www.veracode.com/security/rootkit) or Trojans after gaining access.

A rootkit is a piece of code that lets the attacker have admin access to the system it is attached to. Rootkits can also be installed when you download files from malicious websites.

Trojan horses are software that looks like useful software (for example, adobe photoshop) but can contain a hidden piece of malicious software. This is common among pirated software where attackers embed trojans within popular software like MS Office.

## Reporting

Reporting is the final part of a penetration test. It is what differentiates between an attacker and an ethical hacker.

Once your penetration test is complete, you summarize all the steps you have taken from recon to gaining access. This will help the organization to understand its security architecture and defend itself better.

A report is also useful when you are working as a team. You will not be able to conduct a penetration test for a large organization alone. Reports also make the client understand the efforts of the team and help justify the compensation.

[Here is a sample report created after a successful penetration test](https://www.offensive-security.com/reports/sample-penetration-testing-report.pdf).

## Summary

Cybersecurity is a great career choice, especially during these uncertain times. More devices are exposed to the network every single day. It is the job of the penetration tester to help defend an organization’s network.

Hope this article helped you understand the different stages of a penetration test. To learn more about Ethical Hacking or Artificial Intelligence, [you can visit my blog](https://medium.com/manishmshiva). 

