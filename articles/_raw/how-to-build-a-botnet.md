---
title: What is a Botnet – Botnet Definition and How to Defend Against Attacks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-09-02T14:52:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-botnet
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-pixabay-163064.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
seo_title: null
seo_desc: "By Megan Kaczanowski\nA botnet is a collection of internet connected devices\
  \ (anything from PCs to IoT devices) which are infected by the same malware. \n\
  A hacker uses the malware the botnet is infected with to control it and launch botnet\
  \ attacks. The..."
---

By Megan Kaczanowski

A botnet is a collection of internet connected devices (anything from PCs to IoT devices) which are infected by the same malware. 

A hacker uses the malware the botnet is infected with to control it and launch botnet attacks. The attacks are more effective when launched using hundreds, or thousands, or even hundreds of thousands of linked devices. 

## What's the point of building a botnet?

Botnets can be used for a variety of attacks:

* Generate fake advertising clicks to increase site revenue or increase a site's prominence in search rankings 
* Generate spam emails for clients
* Launch DDoS attacks (distributed denial of service)
* Validate lists of leaked credentials (credential-stuffing attacks) in order to takeover various accounts. 

### Why You Should Understand How Botnets Work

As a security professional, understanding botnets is extremely important. First of all, you'll likely be tasked with defending against attacks from botnets. And you'll probably have to handle systems inside your network being infected and used as part of a botnet. 

In order to effectively defend against botnets, network defenders need to understand the tactic, techniques, and procedures (TTPs) used by bot-herders in order to identify their attacks and the signs of a compromise inside their network. 

No security team wants to find out that a number of their routers or network devices have been compromised and are being used in attacks on other organizations. 

That, like any compromise, can lead to potential problems with regulators, reputational damage, and financial losses resulting from cleaning up the damage.

## How Does a Prospective Botherder Get Started?

Building a botnet isn't just a technical enterprise – it's a business. 

Building a successful botnet requires thinking about what the goal is, whether it's creating a sustainable business plan, a target audience (whose devices are going to be infected, and what lure would appeal to them?), and processes to ensure the distribution and internal processes are secure.

Then, a prospective botnet herder needs to start with a VPN service which takes anonymous forms of payment (possibly several services to rotate between). These services need to be unlikely to quickly hand over customer records and logs to any law enforcement agencies (a 'bulletproof' service). 

The next step is getting access to 'bulletproof' hosting (either a somewhat legitimate business which is *_inefficient*_ at processing legal complaints or one specifically aimed at malware operators). 

Then, the herder needs domains from a registrar which will be unlikely to hand over customer information to law enforcement and which accepts anonymous methods of payment.

Optionally, a herder can further disguise their activity with a technique like fast flux. Fast flux can either be single or double flux.  

Single flux involves having numerous IPs attached to a single domain, swapping the IP addresses in and out very quickly with DNS record changes (using very short time-to-live (TTL) values and round-robin DNS). 

Double flux adds a second layer by also rotating the Name Server (NS) records. Essentially, fast flux enables a bot herder to quickly rotate endpoints and name servers, reducing any points of failure and evading takedown attempts from security teams.

Understanding how fast flux works can help defenders identify when it is occurring and take protective action. 

For example, a security team can reach out to a domain registrar and request that they take down the domain or block access to malicious domains within their network. 

Typically a security team will attempt to block access to the malicious domains within their network, as convincing a registrar to take down a domain is often a time-intensive process (and is often unsuccessful, as unscrupulous registrars are unlikely to perform domain takedowns without pressure from law enforcement).

Then the herder needs the actual botnet-building framework (how to control the bots they've created). It'll either be one they've created themselves (very difficult and time-intensive), one they've bought on a dark web forum (often comes with customer support), or a free (likely older and more unreliable) version available online. 

They may also need an 'injector' or two (essentially add-on modules which tell the bots what to do, such as carrying out click fraud, DDoS, and so on). 

Finally, they need an exploit tool or service in order to infect devices without triggering security alerts. Again, they can build their own (very difficult and time-intensive), buy (or rent) on a dark web forum (often comes with customer support), or use a free (likely older and more unreliable) version available online. 

Often these are software packages which can be installed on a webserver to which the attacker can direct their victims (via phishing).

Additionally, in order to evade detection, a herder can use a 'dropper' malware. This malware will encrypt the malware in order to hide its file signature and any identifying files. 

Crypter services (which create 'droppers') are freely available online or can be purchased on a number of marketplaces for the aspiring herder. Some will include 'anti-sandbox' code which aims to detect if the malware is opened on a sandboxed machine or virtual machine in order to evade analysis by security teams.

Each of these stages is a chance for defenders to identify the attacker in their network. 

Most organizations' defenses will have multiple layers:

* antivirus and endpoint detection to identify malware based on 'signatures' and on unusual behavior, 
* proxies to block traffic to known malicious domains, 
* logs fed into a security information and event management (SIEM) tool designed to identify unusual system and network behavior, etc. 

These layers are designed to catch the different stages and types of malware used by attackers. 

## Now, it's time for infection

Typically a herder will send a phishing or spam campaign targeting huge numbers of people, with the hope that a small percentage of them will click the link and download an 'exploit kit'. This kit will 'drop' malware onto the device, which allows the botnet herder to control the device.

Alternatively, the herder can scan large numbers of IP address blocks, looking for IoT devices with default usernames and passwords (the Mirai botnet followed this path). Many people never bother to change their default credentials when setting up IoT devices.

The dangers of being too successful are that if too many devices are infected, the botnet runs the risk of attracting the attention of various anti-virus (AV) or security companies. 

At this point, it becomes a constant battle between the AV companies and the botnet herders, each of whom will try to update their software to evade the other.

## How do bots communicate with the herder?

Once bots are infected, they need a way to receive commands from their herder. We can broadly group these methods into two categories – either push or pull mode, both of which require a command-and-control (C&C or C2) server to talk to the bots. 

A server can send or 'push' a command to all bots (for example an IRC server, with a secret and password-protected channel), or the bots can send a request (a 'pull') to the C&C server for updates (for example an HTTPD server). 

In recent years, there has also been an increase in peer-to-peer (P2P) networks which are used to proxy commands or locate a server. The advantage of P2P is that there's no single point of failure (as there is with any centralized C2 servers).

In general, the best option for any communication method is one which uses standard protocols, as it's harder for security tools to detect the difference between normal traffic and botnet traffic if they're both using the same protocols (especially with HTTP, as most organizations have a huge volume of legitimate HTTP traffic). 

In recent years there has been an increase in bot herders leveraging social media networks to both host their C&C platform, as well as distribute malware, exploiting the high level of trust that most folks place in their social media networks.

One way defenders can prevent this type of communication is by blocking access to social media sites, and by closely monitoring normal system traffic. 

The more familiar defenders (and their tools) are with what normal system traffic looks like, the better prepared they are to identify unusual spikes in traffic or behavior.

## How to Detect Botnets

### Honeypots

Honeypots are systems set up to look like vulnerable machines, but which lack access to sensitive information. Typically they are deployed by security teams/researchers in order to identify and track botnets as bot herders attempt to infect the honeypots. 

Since the honeypot isn't being used for any legitimate purpose, any traffic attempting to connect to them is likely malicious. That means that it is easy for a security team to separate the malicious traffic from normal traffic, observe the behavior, and take action.

### Signatures 

A malware signature is a specific pattern (like a few lines of code which launch the malware or a specific byte sequence) that is used to identify known malicious code. 

This is still used as a basic form of identification, but bot herders are increasingly using obfuscation techniques and rapidly evolving malware (so that even known malware appears new and unique to scanners) in order to evade these detections.

### IDS (Intrusion Detection System) and IPS (Intrusion Prevention System)

These are tools designed to identify suspicious network (or host) behavior and (in the case of IPS) prevent it or (in the case of IDS) alert the security team.

### Passive/Active DNS Monitoring

DNS monitoring can help detect domains which are tied to botnet activity, based on lexical features of the domains and their network features (such as TTL and number of IP subnets). 

Since bots will have to initiate connections (regularly) to the C&C server, it provides an opportunity for tracking and detection. 

Typically domains used for botnets are very quickly recycled and not necessarily intended for humans - they may even be pseudorandom letters and numbers generated by a computer (whereas a legitimate domain is likely stable and human readable). These identifying characteristics can help identify botnet domains.

Well-run botnets can be extremely difficult to permanently take down. In order to take them down, law enforcement and private organizations typically need to collaborate, often across borders. 

Security teams are more likely to be tasked with dealing with the fallout from botnets, rather than taking them down. 

They may need to defend against a DDoS attack from a botnet, or their own systems being used as part of a botnet and therefore may need to detect the botnet's presence and contain any infected machines, but aren't likely to be able to take down a botnet ('hacking back' is illegal in most jurisdictions). 

### Sources/Further information:

* [A beginner's guide to building botnets](https://arstechnica.com/information-technology/2013/04/a-beginners-guide-to-building-botnets-with-little-assembly-required/3/)
* [Bots, Botnets, DDoS Attacks, and DDoS Attack Mitigation](https://engineering.purdue.edu/kak/compsec/NewLectures/Lecture29.pdf)
* [Detection and Classification of Different Botnet C&C Channels](http://www.cse.lehigh.edu/~chuah/publications/atc11_botnet.pdf)
* [Model for HTTP Botnet Detection Based on DNS Traffic Analysis](https://www.uvic.ca/engineering/ece/isot/assets/docs/Holistic%20Model%20for%20HTTP%20Botnet%20Detection%20Based%20on%20DNS.pdf)




