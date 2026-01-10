---
title: Cybersecurity Vulnerabilities – How Attackers Can Get Your Data
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-03-14T18:47:55.000Z'
originalURL: https://freecodecamp.org/news/cybersecurity-vulnerabilities
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-pixabay-38275.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: null
seo_desc: "In order to understand potential threats hanging over your organization,\
  \ you'll need to understand two things: what dangerous stuff is out there on the\
  \ internet right now, and what impact it could have were it to actually hit you.\
  \ \nOnce you have that..."
---

In order to understand potential threats hanging over your organization, you'll need to understand two things: what dangerous stuff is out there on the internet right now, and what impact it could have were it to actually hit you. 

Once you have that information, you'll be in a position to intelligently assess your risk.

That, in turn, can help you decide both _how much_ to invest in security, and _where_ your investment will be best spent. Those numbers are important, because you might be tempted to simply say "Just give me a list of every security mitigation tool available and I'll buy one of each." 

But given how many tools there are out there and how much it would cost you to build the infrastructure and institutional knowledge needed to deploy them all, purchasing "one of everything" isn't a realistic option. Instead, you're going to have to pick and choose and make the best use of the limited resources you've got.

Just about everyone who's attacking other people's digital resources is motivated by one of two aims: to gain unauthorized control of your servers and IT equipment, or to prevent your servers from operating as intended. 

The attackers might be thieves trying to steal your money, competitors or even nation states out to steal your intellectual property or make it impossible for you to function as you'd like, or activists trying to make a statement by breaking things. Whoever they are, it's either control or destruction they're after.

This article comes from my [Introduction to Cybersecurity course](https://www.udemy.com/course/intro-cyber-security-framework-planning/?referralCode=23853458BE14AFFAEFF2). If you'd like, you can follow the video version here:

%[https://www.youtube.com/watch?v=fhkL2NM8rHc&list=PLSiZCpRYoTZ5dys7oy4ReI-ltW0jnGTMO]

## Different Cybersecurity Attack Vectors

In very general terms, an attack can take place through one of four vectors.

### Physical Access

Physical, in-person attacks might involve the theft or unauthorized duplication of unencrypted data drives. This can happen because someone accidentally left a laptop or phone in a coffee shop or because someone forgot to lock the door to your server room.

My guess is that these close-up attacks are becoming increasingly rare. After all, if I had to choose between attempting a complicated, expensive, and highly risky physical infiltration of my target's offices, or sitting on my living room couch and launching a malware script I downloaded somewhere, I sure know the option I'd pick. 

And that's besides the fact that more and more mobile devices used for business are encrypted – making it very difficult to exploit what's on them even if they are stolen.

But there's another type of physical attack that's much harder to prevent: backdoor vulnerabilities built into your hardware or operating systems. A backdoor is an undocumented weakness in a system's security profile. 

Backdoors might have been added without the knowledge of vendors before product shipping as part of a criminal operation. Or they might have been intentionally incorporated into a system to permit secret access for law enforcement organizations.

The term might also be used to describe accidental design flaws that hackers can later exploit. But whatever their origin, backdoors can be really tough to identify and then close.

**What should you do?**

* Encrypt the drives of all mobile devices
* Monitor reliable online security news threads
* Lock your doors (tell me you didn't already think about that one!)

### Network Connectivity

The _second_ attack vector is the internet itself. Which, when you consider how nearly every device you're running will need connectivity, could be a common source of trouble. 

Failing to properly configure your firewall and system settings – and to incorporate cloud harm mitigation services like Cloudflare – can leave you unnecessarily vulnerable to denial of service attacks. This is where your infrastructure is flooded with enough concurrent fake requests to render your service unavailable.

Similarly, unencrypted network connections risk having their private communications intercepted and stolen. Even worse, such connections can fall victim to man-in-the-middle attacks. In these attacks, third parties can not only read private data moving between a website and its remote client, but they can even impersonate the legitimate participants and insert their own content in place of what was intended. 

Imagine how much fun a man-in-the-middle could have with customers logging into their online bank accounts.

Finally, whereas decades ago most viruses were delivered through physical floppy disks, it's now far more efficient to distribute malware online, and in particular as email attachments.

**What should you do?**

* Ensure all network connections are encrypted
* Learn more about [network security](https://www.freecodecamp.org/news/free-computer-networking-course/)

### OS Vulnerabilities

In a way, the _third_ vector through which attacks can come is your operating system. Now when I say that, I don't mean your Linux kernel is suddenly going to wake up and reach out to gangs of nefarious like-minded platforms so they can – oh, I don't know – sell your data at virtual Sunday morning flea markets. 

That's not likely to happen. Rather, what I mean is configuration weaknesses within your operating system can be discovered and exploited by hackers.

Unpatched software packages are easily the most dangerous and common vulnerability. Let me illustrate with some ancient history. You may remember how the credit bureau service Equifax suffered a security breach back in May, 2017. Private personal and financial data involving more than 160 million individuals was exposed in the breach. 

What went wrong? Hackers exploited a bug in the open source framework Apache Struts. Apache had shipped a patch for the bug in March, 2017. The problem is that Equifax admins never got around to installing the free patch. And the rest was history.

Besides running old and buggy software, bad configurations can also cause you grief. Assigning overly-broad permissions to system administration and binary files could allow unauthorized operations. And, more generally, privilege escalation exploits can make use of code or design flaws to gain access to resources that were meant to be restricted.

**What should you do?**

* Patch your OS and software
* Periodically audit your system logs

### Human Error

The fourth and final vector in my model is what they call the bio-ware sitting in front of the keyboards in your office. "Human beings" in other words. 

As a species, we're pretty good at visually identifying bad guys. After all, they usually wear black hats and rain coats with the collars turned up, right? But when it comes to threats that hide behind regular social interactions, we generally fail early and fail often.

Phishing attacks, for instance, can take the form of emails with links designed to _look like_ they lead to your bank's website or an official government service. But they'll actually misdirect you to a pirate site that'll record and then reuse the legitimate authentication credentials you innocently enter. 

Similarly, email spoofing involves forging the actual sender address on an email message to make it look like it came from a familiar or trusted source.

Social engineering techniques can include phone calls claiming to come from your organization's IT department. They might ask you to spell out your password so they can quickly fix some problem in the back-end system. 

Naturally, no real admin would ever need or ask for your password. But equally naturally, it takes awareness and confidence to push back during an unexpected direct conversation with a real human being.

Many – perhaps most – of the most devastating ransomware attacks over the past few years began with a simple set of stolen credentials. Once a ransomware gang comes into possession of valid credentials, they'll log in to your systems and spend all the time they need – sometimes many months – moving through your private network and figuring out how your organization works. 

When they decide they've learned enough, they'll encrypt as much of your data as they can and demand a lot of money in the form of cryptocurrency before restoring your access.

Of course, being criminals, it's hard to rely on their word. Historically, they've been as likely to take your money and leave you with nothing instead of keeping their promise. And even if they do send you decryption keys, you can't know that they haven't made copies of your data which they're busy selling on the dark web.

We'll talk about both prevention and recovery methodologies elsewhere. But for now it's enough to keep in mind that countless disaster stories began with an individual who, for a brief moment, slipped, accidentally revealing valuable credentials to the wrong people.

**What should you do?**

* Keep up with developments in attacker techniques
* Regularly back up your data

_This article and the accompanying video are excerpted from [my Introduction to Cybersecurity course](https://www.udemy.com/course/intro-cyber-security-framework-planning/?referralCode=23853458BE14AFFAEFF2). And there's much more technology goodness available at [bootstrap-it.com](https://bootstrap-it.com)_

