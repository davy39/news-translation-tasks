---
title: How Does Email Work?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-30T18:56:00.000Z'
originalURL: https://freecodecamp.org/news/how-does-email-work
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99f2740569d1a4ca229b.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: email
  slug: email
- name: information security
  slug: information-security
- name: technology
  slug: technology
- name: Web Security
  slug: web-security
seo_title: null
seo_desc: "By Megan Kaczanowski\nFirst, you use a mail user agent, or MUA to read\
  \ and send email from your device (such as gmail, or the mail app on Apple devices).\
  \ These programs are only active when you're using them. \nGenerally, they communicate\
  \ with a mail t..."
---

By Megan Kaczanowski

First, you use a mail user agent, or MUA to read and send email from your device (such as gmail, or the mail app on Apple devices). These programs are only active when you're using them. 

Generally, they communicate with a mail transfer agent, or MTA (also known as a mail server, MX host, and mail exchanger), which serves to receive and store your emails. 

Emails are stored remotely until you open your MUA in order to check your email. Emails are delivered by mail delivery agents (MDA), which are generally packaged with the MTA.

Mail used to be sent to a mail server using SMTP, or Simple Mail Transfer Protocol. SMTP is a communication protocol for email. 

Even now, while many proprietary systems like Microsoft Exchange and webmail programs like Gmail use their own protocols internally, they use SMTP to transfer messages outside their systems (for example, if a Gmail user wants to send an email to an Outlook client).

Mail would then be downloaded from the server using Post Office Protocol (POP3) POP3 is an application-layer protocol which provides access via an internet protocol (IP) network for a user application to contact a mailbox on a mail server. It can connect, retrieve messages, store them on the client's computer, and delete or retain them on the server. 

It was designed to be able to manage temporary internet connections, such as dial-up (so it would just connect and retrieve email when connected, and allow you to view the messages when you were offline). This was more popular when dial-up access was more widespread.

Now, IMAP, Internet Message Access Protocol, has mostly replaced POP3. IMAP can allow multiple clients to manage the same mailbox (so you can read your email from your desktop, laptop, and phone, etc. and all of your messages will be there, organized in the same way). 

Eventually, webmail replaced both. Webmail allows you to login to a website and receive messages from anywhere or any device (yay!), however you need to be connected to the internet while using it. If the website (like gmail) is your MUA, you don't need to know SMTP or IMAP server settings.

## How is email secured?

Unfortunately, security wasn't really built into mail protocols from the beginning (like most beginning internet protocols). Servers just expected to take any message from anyone and pass it along to any other server which could help route the message to its final destination (the recipient in the to: field). 

Unsurprisingly, this became an issue when the internet expanded from a few government and research groups into something most of the world uses to do essentially everything. Pretty soon spam and phishing emails became (and remain) a huge problem for everyone. 

In response, we've collectively tried to implement several measures which prevent people from reading other's messages (encryption) and validate that messages actually came from the purported sender (authentication).  

Most places use TLS (transport layer security, the replacement for SSL, secure sockets layer), a cryptographic protocol which provides encryption in transit. It provides protection for when the message is being transmitted, but not when the data is at rest, (for example, being stored on your computer). 

This ensures that a message isn't altered or snooped on while it's traveling from MTA to MTA. However, this doesn't verify that the message wasn't modified during the trip. 

For example, if the email goes through multiple mail servers before it reaches its final destination, using TLS will ensure it is encrypted between the servers, but each server could alter the message content. In order to address that, we've created SPF, DKIM, and DMARC.

## SPF (Sender Policy Framework) 

SPF allows the owner of a domain (like google.com) to set a TXT record in its DNS that states which servers are allowed to send mail from that domain (for instructions on how to do this for a variety of hosting providers check out [this site](https://support.knowbe4.com/hc/en-us/articles/115015835387-How-Can-I-Add-a-TXT-Record-to-My-DNS-Records-)).

### How does this work?

This record lists the devices (typically by IP) that are allowed and can end in one of the following options: 

-all = If the check fails (the source of the email is not one of the listed devices) the result is a HardFail. Most mail systems will mark these messages as spam.

?all = = If the check fails (the source of the email is not one of the listed devices) the result is neutral. This is typically used for testing, not production domains.

~all =  If the check fails (the source of the email is not one of the listed devices) the result is a SoftFail. This means that this message is suspicious, but isn't necessarily a known bad. Some mail systems will mark these messages as spam, but most will not.

SPF headers can be helpful to the servers themselves, as they're processing messages. For example if a server is at the edge of a network, it knows messages it receives should come from servers in the sender's SPF record. This helps servers get rid of spam faster. While this sounds great, unfortunately, there are a few major problems with SPF. 

1. SPF doesn't tell a mail server what to do with the message - meaning that a message can fail an SPF check and still be delivered. 
2. An SPF record isn't looking at the 'from' address that the user sees, it's looking at the 'return-path'. This is basically the equivalent of the return address you write on a letter. It tells mail servers that handle the letter where to return the message (and it is stored in the email headers - essentially technical information servers use to process email).   
That means I can put whatever I want into the from: address and it won't impact the SPF check. In fact, both of those email addresses can be relatively spoofed by a hacker. Because there is no encryption involved, SPF headers can't be fully trusted. 
3. SPF records need to be keep constantly up to date which can be difficult in large, ever changing organizations.
4. Forwarding breaks SPF. This is because if an email from, say google.com, is forwarded by bob@bobsburgers.com, the envelope sender remains unchanged (the from address still says google.com). The receiving mail server thinks it is claiming to be from google.com, but is coming from bobsburgers.com, so it fails the SPF check (even though the mail actually is coming from google.com). 

For more reading on SPF check out t[hese](https://postmarkapp.com/guides/spf) [articles](http://knowledge.ondmarc.com/en/articles/1148885-spf-hard-fail-vs-spf-soft-fail). You can check if a specific domain has SPF and DMARC records configured [here.](https://domain-checker.valimail.com/google.com)

## DKIM (DomainKeys Identified Mail)

DKIM is similar to SPF. It uses TXT records in the sending domain's DNS as well, and it provides some authentication of the message itself. It attempts to provide verification that messages weren't altered in transit. 

### How does this work?

The sending domain generates a public/private key pair and puts the public key in the domain's DNS TXT record (if you don't know what a public/private key pair is, check out [this article](https://www.freecodecamp.org/news/how-to-send-secret-messages/) on cryptography). 

Then, the domain's mail servers (on the outer boundary - the servers which are sending mail outside of the domain (ex. from gmail.com to outlook.com)) use the private key to generate a signature of the entire message body, including headers. 

Generating a signature usually requires the text to be hashed and encrypted (for more details on this process, check out [this article](https://www.freecodecamp.org/news/understanding-encryption-algorithms/)). 

Receiving mail servers use the public key in the DNS TXT record to decrypt the signature and then hash the message and relevant headers (any headers which were created while the mail was inside the sender's infrastructure - for example if multiple gmail servers processed the email before it was sent externally to outlook.com). 

The server will then check to make sure the two hashes match. If they do, the message is likely unaltered (unless someone has compromised the sender's private key) and legitimately from the purported sender. If the hashes do not match, the message is was either not from the purported sender, or it was altered by some other server in transit, or both.

DKIM does a very good job at one very specific task - answering the question 'was this email altered in transit or not from the purported sender?'. However, that's all it does. It doesn't tell you how to deal with emails which fail this test, which server may have altered the message, or what alterations were made.  

DKIM is also used by some ISPs, or Internet Service Providers, to determine the reputation of your domain (are you sending lots of spam? Do you have low engagement? How often do your emails bounce?).

For more reading on DKIM check out this [article](https://postmarkapp.com/guides/dkim). You can validate a DKIM record [here](https://www.dmarcanalyzer.com/how-to-validate-a-domainkey-dkim-record/).

## DMARC (Domain-Based Message Authentication, Reporting, and Conformance)

DMARC is essentially instructions for mail servers on how to handle SPF and DKIM records. It doesn't perform any tests of its own, but it tells mail servers how to handle the checks which SPF and DKIM perform.

Participating ISPs will look at published DMARC records and use them to determine how to deal with DKIM or SPF fails. So for example, a commonly spoofed brand might publish a DMARC record which says that if DKIM or SPF fail, drop the message. 

Often ISPs will also send reports on your domain's activity to you with source of the email and whether it passed/failed DKIM/SPF. This means that you'll get to see when people are spoofing (purporting to send from) your domain or altering your messages.

In order to implement DMARC, you need to create a DMARC record, based on your needs (from monitoring your email traffic to figure out what all your email sources are to asking actions be taken, like rejecting any emails which fail DKIM or SPF). You can learn more about doing that [here](https://blog.returnpath.com/build-your-dmarc-record-in-15-minutes-v2/) and [here](https://blog.returnpath.com/demystifying-the-dmarc-record/).

For more reading on DMARC check out [this article](https://postmarkapp.com/guides/dmarc). You can check if a specific domain has SPF and DMARC records configured [here.](https://domain-checker.valimail.com/google.com)

## Wrap up

None of these security measures are perfect, but together, they do a decent job of helping us to improve the security of email systems worldwide. 

The more organizations that adopt these measures (either using open source implementations or paying for a product) the better off everyone will be. Security added on after a protocol or product is developed is usually more expensive, less effective, and harder to implement, than is security built into the product. 

However, most of the protocols which the current internet relies upon were designed for the early internet - for a small group of enthusiasts, scientists, and government folks - not a worldwide network on which we run buildings, smart devices, public transit, nuclear plants(!), and so on. 

Thus, as the internet has continued to expand, we need to continue to adapt and develop new ways to secure the systems we rely upon.

