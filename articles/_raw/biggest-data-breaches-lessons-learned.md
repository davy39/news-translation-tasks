---
title: Biggest Data Breaches of 2020 – and What Developers Should Learn From Them
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-02T17:15:11.000Z'
originalURL: https://freecodecamp.org/news/biggest-data-breaches-lessons-learned
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/photo-1550607326-2df38662b7dc.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: Web Security
  slug: web-security
seo_title: null
seo_desc: "By Andrej Kovacevic\n2020 was not a good year for hacks, data breaches,\
  \ and other cyber-attacks. As far as those things go, it was among the worst years\
  \ on record. \nBusinesses far and wide experienced some of the most damaging and\
  \ embarrassing hacks i..."
---

By Andrej Kovacevic

2020 was not a good year for hacks, data breaches, and other cyber-attacks. As far as those things go, it was among the worst years on record. 

Businesses far and wide experienced some of the most damaging and embarrassing hacks imaginable last year. And some of the incidents led to serious security failures that could end up having grave international implications.

But despite all of the problems, some of 2020's hacks can yield valuable lessons for programmers and software engineers to help them to harden their products against future attacks. 

To help them do that, here's a rundown of the biggest hacks of 2020 and what programmers can – and should – learn from them.

## MGM Resorts Database Breach

The first hack on this list is a bit of a cheat – because technically, it happened in 2019. But I included it here because the target of the attack took all the way until February of 2020 to disclose that anything had even happened. 

At that time, MGM Resorts confirmed that a database containing the personal information of 10.6 million guests had been stolen from cloud storage at some point in 2019.

The trouble is, that wasn't the end of the story. Later on in the year, another database went up for sale on the dark web containing a [staggering 142 million guest records](https://www.forbes.com/sites/leemathews/2020/07/14/mgm-142-million-guests-hacked/?sh=640b8b325294), apparently from the same initial attack. 

At that time, the hackers claimed they had gained access to the data by compromising a 3rd-party cybersecurity service that MGM Resorts had relied on to protect their systems.

The breach was extremely dangerous because the type of data it disclosed typically becomes fodder for large scale [social engineering attacks](https://www.freecodecamp.org/news/social-engineering-the-art-of-hacking-humans/) that can multiply the damage well beyond the scope of the initial incident. And the takeaways from this attack are many.

First, it's that programmers and software engineers have to start [making it a priority to use encryption](https://www.wired.com/story/field-level-encryption-databases-mongobd/) whenever we store sensitive data in a database. 

Second, we should limit the ability of 3rd-party services to peer into the inner workings of our software. 

And third, we should always design software to store as little privileged data as possible. Just what's needed to function, and no more than that.

## Nintendo's NNID Hack

Throughout this year, Nintendo's Switch gaming console experienced a resurgence in sales, fueled by quarantine restrictions forcing millions of people to find solo entertainment options. 

But the year also brought some bad news for the beloved gaming company. In April, their online game network experienced a hack that allowed attackers to [access up to 300,000 user accounts](https://www.theverge.com/2020/6/9/21285084/nintendo-nnid-switch-hack-accounts-affected-exposed) – payment options and all.

The breach stemmed from Nintendo's decision to allow owners of its previous consoles, the Wii U and Nintendo DS, to continue to access their online accounts using a deprecated login method. 

Compounding the problem, owners of the Switch had the option to link their old logins to their new system and to continue using their old login method.

The lesson here is that deprecated authentication methods are deprecated for a reason. Whenever there's a newer, more secure login method, we should update our software to use it and make it a requirement for all users. 

That's a core tenet of [modern secure coding practices](https://vpnoverview.com/internet-safety/business/what-is-secure-coding/), and no amount of user grumbling should be sufficient to prevent the steady march of software security progress.

## SolarWinds Orion Hack

In what's been described by experts as the biggest security breach in history, IT administration platform SolarWinds [suffered a devastating security breach](https://www.businessinsider.com/solarwinds-hack-explained-government-agencies-cyber-security-2020-12) late this year. 

But the hack in and of itself wasn't the notable part. It was that the hackers managed to infect SolarWinds' Orion software updates with custom-built malware that created backdoor access into any system that those updates reached.

And did they ever reach some high-value targets – 18,000 of them in total. Among them were almost every US Government agency, Cisco Systems, Microsoft, and countless other well-known organizations. 

The attack, which was executed by Russia's Foreign Intelligence Service, is at once far-reaching and massively damaging. And it also sounds a clear warning to programmers and software developers.

That warning is simple. It's that not every attempt to access protected systems will come from a frontal assault on an individual piece of software. Hackers will almost always target the most low-hanging fruit to gain privileged access to networks, which they can then use to sidestep security and access controls. 

So, going forward, software developers are going to have to start [applying zero-trust principles](https://searchsecurity.techtarget.com/tip/Zero-trust-framework-creates-challenges-for-app-dev) to their code to make sure that someone else's security failures don't become their massive data thefts.

## FireEye's Red Team Tools Theft

The last hack on the list is important because it could become the fuel for 2021's cybersecurity challenges. 

In December 2020, cybersecurity firm FireEye announced that it had been the target of yet another Russian-sponsored hacking operation. This time, the attackers broke in and [stole the very tools that FireEye uses](https://www.nytimes.com/2020/12/08/technology/fireeye-hacked-russians.html) to test client networks for vulnerabilities.

The Red Team Tools, as they're known, are made up of some of the nastiest and most dangerous malware snippets ever released into the wild. They essentially test whether targeted systems are still vulnerable to known security flaws and other attack techniques. 

But now that they're in the hands of a group that won't hesitate to use them in real-world hacking attempts, the global digital threat landscape has gotten much, much darker.

This is not because the tools represent unknown threats, but that they'll make it possible for the attackers to disguise their tracks, making detection and forensic analysis more difficult. 

But there's a lesson in this too. It's that these threats don't have to remain an issue. And it's up to us as programmers and software developers to make sure they're no longer a danger by staying up to date and patching all of these known vulnerabilities in our code. That way, the bad hackers will have to find new tactics rather than recycling old ones.

## New Year, Bigger Challenges

Even though 2020 was as difficult a year for cybersecurity as any on record, 2021's shaping up to be even tougher. 

With high-end hacking tools out in the wild, nation-states escalating their digital attacks, and cyber-criminals even more determined to take what's not theirs, there's a good chance that we're in for another long and challenging year.

But if programmers and software developers take the lessons learned this year and apply them to their work going forward, there's a good chance that the security situation will improve significantly. 

And even though there's no such thing as bulletproof security, we can all do our part to make the work of black hat hackers quite a bit harder – and that's more than worth making an effort to accomplish.

