---
title: Learn to Speak the Security Lingo – Interview Prep for Cybersecurity Job Interviews
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-01T16:01:00.000Z'
originalURL: https://freecodecamp.org/news/learn-to-speak-the-security-lingo
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9692740569d1a4ca11bd.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: hacking
  slug: hacking
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: null
seo_desc: 'By Megan Kaczanowski

  This article will serve as a quick and dirty guide to some of the most commonly
  asked interview questions for entry-level security jobs.

  What''s the difference between an allowlist and a denylist?

  With an Allowlist, everything is ...'
---

By Megan Kaczanowski

This article will serve as a quick and dirty guide to some of the most commonly asked interview questions for entry-level security jobs.

## What's the difference between an allowlist and a denylist?

**With an Allowlist**, everything is denied access, except items which are on the list. 

For example, a company might compile a list of all authorized company applications, and block all applications not on this list from running.

 This is a very effective way to prevent problematic software from running in your environment, as it blocks by default.

**With a Denylist**, only items on the list are denied access. 

For example, a company might deny certain websites, or categories (like porn, gaming, and so on). 

This is somewhat effective, however given how categories are sometimes incorrect, and malicious software changes extremely quickly, it is not as effective as allowlisting and is often more reactive.

## What's the difference between a penetration test and a bug bounty? Which one is better?

**A Pen Test (or Penetration Test)** is where a company hires a tester or firm (with non-disclosure agreements, or NDAs) to simulate an attacker. They will operate within a pre-defined scope during a limited time period, write up a report on their findings, and include recommended remediation steps. 

Pen testers aren’t designed to find every weakness in a system (though they will try to identify as many vulnerabilities as possible). These are generally used by mature organizations (because for the test to be effective, an organization needs to be able to remediate any identified vulnerabilities).

**Bug Bounties**, on the other hand, open up the process of searching a company’s system for vulnerabilities to everyone on the bug bounty platform. 

This leverages crowds (and therefore might find more vulnerabilities), but the number of vulnerabilities found likely depends on the interest of the crowd (continuous coverage isn’t guaranteed). Also, it doesn’t guarantee the same level of reporting as does a pen test (you might not have enough hackers who have the specific skill set testing your tool/application/website requires). 

Further, a bug bounty program shouldn’t be undertaken without a plan in place for remediation of vulnerabilities (the security posture of the company should be relatively mature).

**Further Reading:** What are [Bug Bounties](https://www.freecodecamp.org/news/whats-a-bug-bounty-program/), how do they work, and who should use them?

## What's the difference between threat, vulnerability, and risk? How do you decide what to focus on?

A **threat** is a negative event which leads to an unwanted result. This includes an employee who clicks on a phishing link, a developer who misconfigures a database instance, or an earthquake which destroys your data center.

A **threat actor** is the person, group, or entity which is responsible for the event.

A **vulnerability** is a weakness in a system (such as lack of physical access control to a data center, SQL injection, and so on) that a threat actor can exploit.

A **risk** is the chance of a negative event (how likely is the bad thing to happen) and the impact of that event (how bad is the bad thing). A risk is commonly calculated by multiplying the likelihood x the impact.

**Threat modeling** is a process for identifying threats to a particular target, understanding them, and prioritizing them. This process is designed to answer the questions, ‘what type of actor is likely to target me?’ ‘where am I most vulnerable?’ ‘what are my high value assets?’.

**Further Reading:** [An intro to threat modeling](https://redcanary.com/blog/threat-modeling/).

## What's the difference between red, blue, and purple teams?

**Red Team:** Red teams are offense (breaking into systems).

**Blue Team:** Blue teams are on defense (defending systems).

**Purple Team:** Ideally a team which integrates the red and blue team in a way which facilitates them learning from each other and improves the security of the overall organization.

## What's the difference between an event, an alert, and an incident?

An **event** is an aberration from normal system behavior.

An **alert** is a notification set to be sent when a specific event or series of events occurs.

An **incident** is an event with a negative impact on the organization (examples: a user downloads malware onto the network and it spreads, credential are pasted online by an attacker, and so on). Not every event becomes an incident.

## Whats the difference between encoding, encryption, and hashing?

**Encoding** is a way of converting data from one format to another (for example from text to ASCII). It's not inherently a security function. 

**Encryption** is a way of hiding a message with the intent of only allowing the intended recipient to understand the meaning of the message. 

It is a two way function (you need to be able to undo whatever scrambling you’ve done to the message). This is designed to protect data in transit.

**Hashing** is a one-way function (it can't be reversed) which converts a variable length message to a fixed length string which is unique for each message. 

Hashes are used as a space-efficient way to store data, and a secure way to store passwords. If a password is stored as a hash, even if the computer is compromised the data is still safe (because the function can't be reversed). When the user enters a password, the computer can just use the same hashing function to convert the password into a hash, which it can compare to the stored hash to see if they match. 

Hashing functions are also used to create message digests in order to verify that a message hasn't been changed in transit.

**Further Reading:** Learn more about what [hashing is here](https://www.freecodecamp.org/news/an-intro-to-password-cracking/), and how [encryption works here](https://www.freecodecamp.org/news/why-a-little-salt-can-be-great-for-your-passwords/).

## Should you encrypt or compress data first? 

Compress, then encrypt. If you encrypt first, you’ll only have random data to work with, which removes the benefits of compression.

## What is salting?

**Salting** is the process of adding random values to the end of data, like a password, and then hashing the value. 

This protects against brute force attacks (when an attacker tries every possible combination of letters and numbers until the password is found) as it makes it harder for an attacker to guess.

**Further Reading:** Learn more about [salting here](https://www.freecodecamp.org/news/why-a-little-salt-can-be-great-for-your-passwords/).

## Is TLS, SSL, or HTTPS more secure?

**TLS (Transport Layer Security)** is a cryptographic protocol which helps secure communications over a network.

**SSL (Secure Sockets Layer)** is the predecessor to TLS, and is largely depreciated.

**HTTPS (Hypertext Transfer Protocol Secure)** is just HTTP encrypted with SSL or TLS (typically TLS, since it has largely replaced SSL). Since you can't have HTTPS without SSL or TLS, this is a trick question.

## What port does ping work over?

Again, a trick question, as ping is a layer 3 protocol which uses ICMP and doesn't work over a port at all.

## What protocol does DNS use?

**UDP** is used for name and regular or reverse queries, as well as any information smaller than 512 bytes.

**TCP** is used for zone transfer and information larger than 512 bytes. Also, if a client doesn't get a response, it will retransmit the data using TCP.

### Looking for more interview prep resources? 

* [60 Cybersecurity Interview Questions](https://danielmiessler.com/study/infosec_interview_questions/)
* [Lesley Carhart's Infosec Career Advice](https://tisiphone.net/category/security-education/)
* [Troy Hunt's Career Advice](https://www.troyhunt.com/careers-in-security-ethical-hacking-and-advice-on-where-to-get-started/)
* [Local BSides Events](http://www.securitybsides.com/w/page/12194156/FrontPage)
* [WiCyS Career Resources](https://www.wicys.org/career-central)

