---
title: A Beginner's Guide to Digital Security – How to Keep Yourself Safe Online
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-01-06T18:09:40.000Z'
originalURL: https://freecodecamp.org/news/understanding-digital-security
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-pixabay-207580--2-.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: privacy
  slug: privacy
- name: Security
  slug: security
seo_title: null
seo_desc: "Whatever your connection to technology, security should play a prominent\
  \ role in the way you think and act. \nTechnology, after all, amplifies the impact\
  \ of everything we do with it. The things we say and write using communication technologies\
  \ can be ..."
---

Whatever your connection to technology, security should play a prominent role in the way you think and act. 

Technology, after all, amplifies the impact of everything we do with it. The things we say and write using communication technologies can be read and heard by many, many more people than would be possible without. 

The ability to conveniently connect with people and collaborate on projects of all kinds is much greater. 

The tasks we can perform are, through the magic of automation, almost limitless. The scope of information we can instantly access through the simplest and least expensive devices towers far beyond anything the greatest scholars could have hoped to see in a lifetime just a few decades ago.

All that means that criminals and other individuals unconstrained by moral conscience will have yet more powerful tools to compromise the data you create and consume, and steal or damage the property you acquire. 

So you've got a strong interest in learning how to protect yourself, your property, and that of the people and organizations around you.

This tutorial (taken from my book, [Keeping Up: Backgrounders to All the Big Technology Trends You Can't Afford to Ignore](https://amzn.to/3FXXAfb)) will present a brief overview of what's at stake in the technology security domain. 

We'll define the kinds of threats we face and discuss the key tools at our disposable for pushing back against those threats.

If you're interested in digging deeper into the topic, my LPI Security Essentials book is entirely devoted to giving you the full picture.

If you'd prefer to watch this chapter as a video, feel free to follow along here:

%[https://www.youtube.com/watch?v=OJf27vq_PTo]

# Hacking? What's Hacking?

Defining computer hacking in a way that doesn't anger someone, somewhere, is like talking about politics at work. Be prepared for long, awkward silences and possibly violence. 

You see, purists might insist that the term hacking should apply exclusively to individuals focused on forcibly re-purposing computer hardware for non-standard purposes. 

Others reserve the title for people who bypass authentication controls to break into networks for criminal or political purposes. 

And how about those who wear the title as a sign of their practical expertise in all things IT? (And then, of course, there are crackers.)

But this is my book, so I'm going to use the term any way I want. I therefore decree that hacking is all about plans the _bad guys_ have for _your_ digital devices. Specifically, their plans to get in without authorization, get out without being noticed, and (sometimes) take your stuff with them when they leave. 

Using the term this way gives us a useful way to organize a discussion of some common and particularly scary threats.

## How Hackers Get In to Your System

The trick is to find a way through your defenses (like passwords, firewalls, and physical barriers). In most cases, passwords probably provide the weakest protection:

* Passwords are often short, use a narrow range of characters, and are easy to guess.
* If a device came with a simple factory default password (like "admin" or "1234") just meant to get you in for the first time, then the odds are pretty good that many users will never get around to trading it in for something better.
* Even strong passwords can be stolen by deceptive phishing email scams ("Click here to login to your bank account..."), social engineering ("Hi, it's Ed from IT. We're having some trouble with your corporate account. Would you mind telling me your password over the phone so I can quickly fix it?"), and keyboard tracking software.

We'll talk more about firewalls later in this tutorial. And physical barriers? I think you already know what a locked door looks like. But it's probably worth spending a few moments thinking about other kinds of digital attacks.

The big prize is usually getting to your data and making off with copies. But for some, simply destroying the originals can be just as satisfying.

Obviously, logging into your devices using stolen passwords is the most straightforward approach. But access can also be achieved by intercepting your data as it travels across an insecure network. 

One approach that's commonly used here is known as a man-in-the-middle attack. This is where data packets can be intercepted in transit and altered without authorized users at either end knowing anything's wrong. 

Properly encrypting your network connections (and avoiding unsafe public networks altogether) is an effective protection against this kind of threat. We'll talk more about encryption a bit later.

If the hardware you're using has an undocumented "back door" built in, then you're pretty much toast whatever you do. We'll talk more about back doors later in the book but, for now, I'll just note that there have been no shortage of factory-supplied laptops, rack servers, and even high-end networking equipment that's been intentionally designed to include serious access vulnerabilities. Be very careful where you purchase your compute devices.

If the attackers find a way into your physical building (sometimes posing as employees of a delivery company), they could quietly plug a tiny listening device into on unused ethernet jack on your network. That'll give them a nice platform to watch and even influence all your activities from the inside. 

Protecting your physical infrastructure and carefully monitoring network activity is your best hope against that kind of intrusion.

Even if your home or office is all fortressed up, there's no guarantee that data moving around on mobile devices (like smartphones or laptops) won't find its way into the wrong hands. 

And even if you've been careful to use only the best passwords for those devices, the data drives themselves can still be easily mounted as external partitions on a thief's own machine. Once mounted, your files and account information will now be wide open. 

The only way to protect your mobile devices from this kind of threat is to encrypt the entire drive using a strong passphrase.

## What Hackers Are After

Now that entire economies are run on computers directly connected to public networks, there's money and value to be had through well-planed corporate, academic, or political espionage efforts...and through old fashioned, traditional theft. 

Whether the goal is building up a military or commercial competitive advantage, completely destroying the competition, or just getting your hands on "free" money, illegally accessing other people's data has never been easier.

So what are hackers likely to be after? All the important financial and other sensitive information you'd prefer they didn't have. Including, it should be noted, the kind of information you use to identify yourself to banks, credit card companies, and government agencies. 

Once the bad guys have got important data points like your birth date, home address, government-issued ID numbers, and some basic banking details, it's usually not hard to present themselves as though they're you, completely taking over your identity in the process.

Digital attacks can also be used as blackmail to force victims to pay to undo the damage they've done. 

That's the objective of most _ransomware_ attacks, where hackers encrypt all the data on a victim's computers and refuse to send the decryption keys needed to restore your rightful access unless you send them lots of money. 

Such attacks have already effectively brought down critical infrastructure like the IT systems powering hospitals and cities.

The very best defense against ransomware is to have full and tested backups of your critical data and a reliable system for quickly restoring it to your hardware. That way, if you're ever hit with a ransomware attack, you can simply wipe out your existing software and replace it with fresh copies, populated with your backed up data. 

But you should also beef up your general security settings to make it harder for ransomware hackers to get into your system in the first place.

When their primary goal is to prevent you or your organization from going about its business, hackers can remain at a safe distance and launch a distributed denial of service (DDoS) attack against your web infrastructure. 

Historical DDoS attacks have used massive swarms of thousands of illegally hijacked network-connected devices to transmit crippling numbers of requests against a single target service. When large enough, DDoS attacks have managed to bring down even huge enterprise-scale companies using sophisticated defenses for hours at a time. 

The site hosting one of my favorite online open source collections was hit hard more than a year ago and still hasn't fully recovered.

# What is Encryption?

If your data is unreadable, there's a lot less bad stuff that unauthorized individuals will be able to do with it. But if it's unreadable, there's probably not a whole lot you'll be able to do with it either. 

Wouldn't it be nice if there was some way to present your data as unreadable in every scenario except where there's a legitimate reason? Well waddaya know? There is, and it's called data encryption.

## How to Encrypt Data in Transit

Encryption algorithms encode information in a way that makes it hard, or even impossible, to be read. 

A simple (and ancient) example is symbol replacement, where every letter "a" in a message would be replaced with, say, the letter three positions on in the alphabet (which would be "d"). Every "b" would become "e" and so on. "Hello world" would be "khoor zruog". People subsequently coming across the message would be unable to understand it.

Of course, it wouldn't take long for a modern computer (or even a smart 8-year-old) to decode that one. But some very clever cryptologists have been working hard over most of the past century to produce much more effective algorithms. 

There are some significant variations of modern cryptography. But the general idea is that people can apply an encryption algorithm to their data and then safely transmit the encrypted copy over insecure networks. Then the recipient can apply a decryption key of some sort to the data, restoring the original version.

Encryption is now widely available for many common activities, including sending and receiving emails. You can similarly ensure that the data you request from a website is the same data that's eventually displayed in your browser by checking the lock icon in your browser's address bar. The icon confirms that the website server employs Transport Layer Security (TLS) encryption.

Over the past few years, the Let's Encrypt project (letsencrypt.org) has encouraged millions of new websites to use encryption by provided free encryption certificates and simple-to-use tools to help server administrators install them.

## How to Encrypt Data at Rest

TLS will protect your data when it's out and about, but what'll keep it safe even when it's relaxing in its comfy storage disk? File and drive encryption, that's what. 

All operating systems now offer integrated software for encrypting all or part of a storage disk either at installation time or later. Each time you power up an encrypted disk, you'll be prompted to enter the passphrase you created when you enabled encryption.

The thing is that if you forget your passphrase, you're pretty much permanently locked out of your system and the data is as good as gone forever. 

But the other thing is that if you _don't_ encrypt your system then, as we noted earlier, anyone who steals the hardware will have easy and instance access to your private information. It's a tough world out there, isn't it?

# What Does a Firewall Do?

You can think of a firewall as a filter. Just like, say, a water filter is able to block certain impurities, allowing only clean water through, a firewall can inspect every packet of data coming into or leaving your infrastructure, blocking access where appropriate. 

Besides not needing to be replaced every few weeks, the big advantage of a firewall over a water filter is that it can be closely configured to permit and refuse entry to exactly match your security and functional needs. Then you can update it later should your needs change.

## Hardware Firewalls

A hardware firewall is a purpose-built physical networking device that's commonly used within enterprise environments. Such firewalls are installed at the edge of a private network and set to block potentially dangerous incoming traffic, redirect other traffic to remote destinations, or permit traffic to access hosts within the local network.

Hardware firewalls are sold by companies like Cisco and Juniper, and general equipment manufacturers like HP and Dell. They can be used to manage traffic for networks comprised on many thousands of hosts. 

Firewalling appliances tend to be very expensive, often costing many thousands of dollars. They're normally only deployed to manage enterprise infrastructure.

## Software Firewalls

A software firewall is an application that runs on a regular PC that can perform just about any function that you'd otherwise expect from a hardware firewall. There are two important differences:

* Firewall software (like the Linux iptables utility) is often free and, while complicated, enjoys the benefits of vast documentation resources. The software can also be installed any old PC that's just lying around, reducing the overall cost to nearly nothing.
* You won't want to use such a firewall within a busy business environment however, since such a PC probably won't have the compute power to manage high volumes of network traffic. Nor, in most such cases, will it be reliable enough to provide mission-critical services 24/7.

There's another flavor of software firewall that's used as part of consumer-grade operating systems. Such firewalls allow you to better secure your OS by setting rules for what kind of activities you want to allow. These can be especially useful for mobile devices that frequently move from network to network.

Cloud computing platforms – like Amazon Web Services (AWS) and Microsoft's Azure – provide a firewall-like technology for use with the resources you might deploy within their systems. Firewall policies might exist in objects with names like "security group" or "access control list" that can be applied to whichever resource requires them.

# Who Does Security Best?

In the not too distant past, you would often hear IT professionals swearing they would never run their IT operations on infrastructure they didn't physically control. This was common when referring to outsourcing to third party, offsite companies or to cloud computing platforms. 

Whether it was because those administrators didn't trust the reliability and security of compute infrastructure run by strangers, or because regulatory restrictions required that sensitive workloads remained local, the sentiment was widely shared. And it made sense.

But the past is a foreign country. Today, it can be forcefully argued, the most secure and reliable environments can be found in the biggest public cloud providers. 

Why? They've got the money and incentive to hire the very best engineers, and the money and incentive to build the very best infrastructure. 

Beyond that, cloud providers maintain data centers in political jurisdictions around the world, and go to great lengths to ensure their deployments comply with industry and government standards.

Let me illustrate. Remember the DDoS threat we discussed a bit earlier in the chapter? Well, [back in the summer of 2020](https://www.zdnet.com/article/aws-said-it-mitigated-a-2-3-tbps-ddos-attack-the-largest-ever), an unnamed organization deploying resources on AWS was hit with a DDoS attack peaking at 2.3 Tbps. That is, each and every second, requests hit that organization's public-facing service with 2.3 terabytes of data.

What does "2.3 terabytes" actually mean? Well, a megabyte is (approximately) one million bytes of information (a PDF version of this book would probably take up six megabytes or so). A gigabyte is one thousand million bytes of information. A terabyte is one thousand thousand million bytes of information. That would be the equivalent of around 165,000 PDF books. 2.3 terabytes would be the rough equivalent of 380,000 PDF books.

Now try to imagine all the text characters used to fill 380,000 PDF books being thrown at a web service _each second._

Got that image in your mind? Now here's what happened to that web service: Nothing. It just carried on working as though it hadn't a care in the world. How on earth is that even possible? Amazon's AWS Shield service simply mitigated the attack. The customer didn't have to do a thing.

_That_ is why moving your workloads to the public cloud doesn't necessarily involve compromising your standards.

## Thanks for reading!

YouTube videos of all ten chapters from this book are [available here](https://www.youtube.com/playlist?list=PLSiZCpRYoTZ6UWl4xialvwLOKyHYYJUiC). Lots more tech goodness – in the form of books, courses, and articles – [can be had here](https://bootstrap-it.com). And consider enjoying [my LPI Essentials resources here](https://bootstrap-it.com/lpi-essentials/).

