---
title: Types of Hackers – And How to Defend Against Them
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-01T02:44:00.000Z'
originalURL: https://freecodecamp.org/news/types-of-hackers
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9694740569d1a4ca11c6.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: hacking
  slug: hacking
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: null
seo_desc: "By Megan Kaczanowski\nIf you want to protect systems, you need to understand\
  \ whom you’re defending them from. \nMany of the attackers you’ll face will fall\
  \ into several different groups. These different groups often use very different\
  \ tactics, techniqu..."
---

By Megan Kaczanowski

If you want to protect systems, you need to understand whom you’re defending them from. 

Many of the attackers you’ll face will fall into several different groups. These different groups often use very different tactics, techniques, and procedures (TTPs) for attacking systems. 

Identifying which actors or groups of actors may target your systems can help prioritize the mitigations which are most important.

## Script Kiddies:

Script kiddies are technically inexperienced hackers. Often they’re young – even teenagers. They don’t know how to write their own code or exploits, but can use tools others have developed. They're often motivated by fun.

They commonly use phishing attacks, tools they’ve bought from others on dark web marketplaces, or free tools. They’ve been associated with hacks on video game companies, [like this one](https://www.wired.com/story/xbox-underground-videogame-hackers/). 

## Cyber Criminals:

Cyber criminals range in technical sophistication from script kiddies to organized gangs, where each member fulfills a different role in the cyber crime ring. They are responsible for the [majority](https://enterprise.verizon.com/resources/reports/dbir/) of data breaches and are primarily motivated by money. They’re known for ATM fraud (‘jackpotting’), credit card and gift card theft, ransomware, and data theft (among other attacks).

The most common attack from cyber criminals is mass phishing campaigns, as these can be used to distribute ransomware or enable data theft. When an unwary user clicks the link or opens the attachment, ransomware (malicious software which will lock their files until they pay a ransom (usually in digital currency)) will infect their machine. 

Alternatively, the phishing link might ask for a user’s credentials (username and password) and then use that information to steal information or blackmail the user. 

Large scale phishing campaigns like this are very technically easy to execute, and are [extremely](https://www.businessinsider.com/scammers-squeezed-330000-people-webcam-porn-2019-2) [profitable](https://thenextweb.com/hardfork/2019/02/22/bitcoin-sex-scam-blackmailers/).

Protecting against cyber criminals is generally a matter of being more secure than your 'neighbors' as cyber criminals are looking for the easiest target. 

Automated spam filtering, scanning of email attachments and links, and measures such as DMARC, SPF, and DKIM can help reduce the number of phishing emails delivered to your users. Security awareness programs can also help users identify phishing emails missed by the filters and report them to your security team.

In the last few years, this has changed somewhat, as [big game hunting](https://arstechnica.com/information-technology/2019/10/fbi-warns-of-major-ransomware-attacks-as-criminals-go-big-game-hunting/) has become more popular. 

Essentially this is when cybercriminals choose a large entity (often one which has a low tolerance for downtime) to target and spend weeks or months working to break into the target's network, specifically looking for high value assets. 

They will then deploy ransomware and use the company's inability to deal with downtime to negotiate for a ransom (in addition to exfiltrating data and leveraging the threat of that data being leaked to induce a company to pay the ransom). 

The criminals tend to be relatively sophisticated, prioritizing stealth. Protecting against these groups is much more difficult and depends upon a layered defense (myriad protection and alerting mechanisms in order to protect systems, detect intrusions, and mitigate vulnerabilities).

## Hacktivists:

Hacktivists are motivated by issues (political, economic, religious, and so on). Some of these actors are solo actors, and some are in groups such as [Anonymous](https://www.wired.com/2011/11/anonymous-101/) (known for a series of attacks on the Church of Scientology).

These groups often use DDoS (distributed denial of service) attacks and website defacements. A DDoS attack is when an attacker overwhelms a server with so many requests that it is unable to handle the traffic and crashes (often using a botnet). Website defacements occur when a group takes down the message or images currently displayed on a website and replaces them with their own. 

Hacktivists are not generally motivated by money or data theft (unless they think if the data is exposed it will incriminate or embarrass the target), but instead want to spread their message or publicize their cause.

Protecting against these attacks is a matter of scanning public facing websites for vulnerabilities, having an incident response team (and an incident response plan!), and having protections in place to mitigate traffic spikes (for example Amazon Shield for AWS).

## Insider Threat:

Insider threat can be broadly split into two groups: malicious insiders, and accidental insiders.

* Malicious insiders are those who have been compromised by an outsider, or who have decided to steal from the organization for personal gain. People who are angry about being fired or missed over for a promotion and want revenge, or who are trying to steal information for insider trading are malicious insiders.
* Accidental insiders include those who have clicked a phishing link (and had their account compromised), misconfigured a database, or accidentally sent sensitive information to the wrong person.

Regardless of an insider’s motivations, they pose one of the [most](https://www.sentinelone.com/blog/top-7-most-disturbing-data-breaches-in-2018/) [dangerous](https://www.venafi.com/blog/deciphering-how-edward-snowden-breached-the-nsa) [threats](https://www.observeit.com/blog/5-examples-of-insider-threat-caused-breaches/) to any [organization](https://www.csoonline.com/article/3263799/insider-threat-examples-7-insiders-who-breached-security.html). The primary concern for insider threats should be data theft, as information is usually the target of those type of attacks.

Defending against insider threat should be largely driven by security awareness. People want to be helpful, which is a trait hackers will exploit through social engineering attacks to gain information. 

Security programs usually use security training, Security Champions programs, and awareness initiatives to educate their employees about this threat. In addition, comprehensive monitoring of internal networks for unusual behavior (often using user behavior analytics) can help you identify and mitigate insider threats.

## Nation State Attackers:

In 2018, nation state attackers were only responsible for 12% of all data breaches ([Verizon Data Breach Report](https://enterprise.verizon.com/resources/reports/dbir/)). However, they are generally well-trained, well-funded, and extremely motivated. 

Unlike insiders (who are often not well-trained) or cyber criminals (who are generally not motivated to attack specific targets), once nation-state attackers (also known as APT, or Advanced Persistent Threats) have targeted your organization, they are unlikely to stop until they have penetrated the organization. 

These types of attackers are often salaried employees, who are employed by intelligence agencies around the world. Nation state goals vary by country, but are generally designed to advance the country's political and economic goals.

These attackers are known for a range of tactics (anything which will help them compromise your organization), but have been known to use spear phishing attacks, custom malware, and zero day attacks. 

Unlike cyber criminals who want to quickly monetize assets, nation state attackers will often seek long term access to your infrastructure. They will do their best to gain initial access quietly (and through multiple entry points), then move quietly through your networks, mapping out as much as they can. That way, they’re less likely to be caught, more likely to find their target, and exfiltrate data without being caught.

Protecting against these organizations depends upon strong security fundamentals throughout your organization (such as patch and vulnerability management programs, security awareness programs, monitoring and detection, and effective incident response, among others), and more advanced protections (such as threat intelligence, which can help you identify the threat actors which may target your organization).

## Why does it matter what kind of attackers are targeting my organization?

Since resources aren't infinite, every security program needs to prioritize some protections over others and can't protect effectively against all attacks. They may also have limited ability to implement controls based on the needs of the business.

An effective security team needs to choose how to spend their influence wisely when recommending a security tool. 

Given that, one philosophy of how to choose which controls to prioritize is to perform ‘threat modeling’. 

At a very high level, threat modeling is designed to determine the organization's most valuable assets (or 'crown jewels') and identify the threat actors (both by high level type, and even specific groups) which are most likely to attack the organization. This may also involve determining which attacks, or types of attacks, the organization is likely to encounter. 

This information can help the  security team determine what controls will be most effective for their environment and will provide the greatest protection for the cost. Then, the team can prioritize the most important security measures for their environment, and best use limited resources and limited influence to protect their environment from the threats they're most likely to face.

