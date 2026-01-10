---
title: What’s in an Email Header and Why Should You Care?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-29T04:06:00.000Z'
originalURL: https://freecodecamp.org/news/reading-email-headers
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ab8740569d1a4ca274f.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: email
  slug: email
- name: email marketing
  slug: email-marketing
- name: information security
  slug: information-security
seo_title: null
seo_desc: 'By Megan Kaczanowski

  Ever gotten a spam or phishing message from an email address you didn''t recognize?
  Maybe someone offered you a free trip, asked you to send them bitcoin in exchange
  for personal photos, or just sent you an unwanted marketing emai...'
---

By Megan Kaczanowski

Ever gotten a spam or phishing message from an email address you didn't recognize? Maybe someone offered you a free trip, asked you to send them bitcoin in exchange for personal photos, or just sent you an unwanted marketing email? 

Have you wondered where those emails came from? Seen a spammer spoof your email address and wondered how they did it? 

Email spoofing, or making an email appear as though the email came from a different address than it did (for example an email that appears to come from whitehouse.gov, but is actually from a scammer) is remarkably easy. 

Core email protocols don't have any method for authentication, meaning that the 'from' address is basically just a fill-in-the-blank.

Usually when you get an email, it looks something like this:

```
From: Name <name@gmail.com>
Date: Tuesday, July 16, 2019 at 10:02 AM
To: Me <Me@freecodecamp.com>
```

Below that is the subject and message.

But how do you know where that email really came from? Isn't there any additional data that can be analyzed? 

What we're looking for is the full email headers — what you see above is just a partial header. This data will give us some additional information about where the email came from and how it reached your inbox. 

If you want to look at your own email headers, here's how to access them on [Outlook](https://support.office.com/en-us/article/view-internet-message-headers-in-outlook-cd039382-dc6e-4264-ac74-c048563d212c) and [Gmail](https://support.google.com/mail/answer/29436?hl=en). Most mail programs operate in a similar manner, and a simple Google search will tell you how to view headers on alternative mail services. 

In this article we'll look at a set of real headers (though they're heavily redacted — I've changed hostnames, timestamps, and IP addresses).

We'll read the headers from top to bottom, but be aware that each new server adds their header to the top of the email body. This means we'll read each header from the final Message Transfer Agent (MTA) and work down to the first MTA to accept the message.

## Internal Transfers

```
Received: from REDACTED.outlook.com (IPv6 Address) by REDACTED.outlook.com with HTTPS via REDACTED.OUTLOOK.COM; Fri, 25 Oct 2019 20:16:39 +0000
```

This first hop shows an HTTPS line, which means that the server didn't receive the message via standard SMTP and instead created the message from input it received on a web application.

```
Received: from REDACTED.outlook.com (IPv6Address) by REDACTED.outlook.com (IPv6Address) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.1.1358.20; Fri, 25 Oct 2019 20:16:38 +0000

Received: from REDACTED.outlook.com (IPv6Address) by REDACTED.outlook.office365.com (IPv6Address) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384) id 15.20.2385.20 via Frontend Transport; Fri, 25 Oct 2019 20:16:37 +0000 Authentication-Results: spf=softfail (sender IP is REDACTEDIP)smtp.mailfrom=gmail.com; privatedomain.com; dkim=pass (signature was verified)header.d=gmail.com;privatedomain.com; dmarc=pass action=noneheader.from=gmail.com;compauth=pass reason=100Received-SPF: SoftFail (REDACTED.outlook.com: domain of transitioning gmail.com discourages use of IPAddress as permitted sender)
```

These are the first two header blocks are internal mail transfers. You can tell that these were received by Office365 servers (outlook.com), and routed internally to the correct recipient. 

You can also tell that the message is being sent via encrypted SMTP. You know this because the header lists "with Microsoft SMTP Server" and then specifies the TLS version it is using, as well as the specific cipher. 

The third header block marks the transition from a local mail server to a mail filtering service. You know this because it went "via Frontend Transport" which is a Microsoft-Exchange specific protocol (and therefore it wasn't strictly SMTP). 

This block also includes some email checks. Outlook.com's header is detailing their SPF/DKIM/DMARC results here. An SPF softfail means that this IP address isn't authorized to send emails on gmail.com's behalf. 

"dkim=pass" means that the email is from its purported sender and was (most likely) not altered in transit.  

DMARC is a set of rules telling the mail server how to interpret SPF and DKIM results. Pass likely means that the email continues on to its destination.

For more on SPF, DKIM, and DMARC, check out [this article](https://www.freecodecamp.org/news/p/1fb5b1b8-7bd9-40fc-8a76-d64c979df748/www.freecodecamp.org/news/how-does-email-work/).

## Internal/External Transition

```
Received: from Redacted.localdomain.com (IP address) byredacted.outlook.com (IP address) with Microsoft SMTPServer (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384) id15.20.2305.15 via Frontend Transport; Fri, 25 Oct 2019 20:16:37 +0000

Received-SPF: None (Redacted.localdomain.com: no senderauthenticity information available from domain ofsender@gmail.com) identity=xxx; client-ip=IPaddress;receiver=Redacted.localdomain.com;envelope-from="sender@gmail.com";x-sender="sender@gmail.com"; x-conformance=sidf_compatible


Received-SPF: Pass (Redacted.localdomain.com: domain ofsender@gmail.com designates sending IP as permittedsender) identity=mailfrom; client-ip=IPaddress2;receiver=Redacted.localdomain.com;envelope-from="sender@gmail.com";x-sender="sender@gmail.com"; x-conformance=sidf_compatible;x-record-type="v=spf1"; x-record-text="v=spf1ip4:35.190.247.0/24 ip4:64.233.160.0/19 ip4:66.102.0.0/20ip4:66.249.80.0/20 ip4:72.14.192.0/18 ip4:74.125.0.0/16ip4:108.177.8.0/21 ip4:173.194.0.0/16 ip4:209.85.128.0/17ip4:216.58.192.0/19 ip4:216.239.32.0/19 ~all"
```

This is Google's SPF record - telling the receiving server that the email which says it is coming from gmail.com, is coming from a Google approved server.

```
Received-SPF: None (redacted.localdomain.com: no senderauthenticity information available from domain ofpostmaster@redatedgoogle.com) identity=helo;client-ip=IPaddress; receiver=Redacted.localdomain.com;envelope-from="sender@gmail.com";x-sender="postmaster@.google.com";x-conformance=sidf_compatibleAuthentication-Results-Original: Redacted@localdomain.com; spf=Nonesmtp.pra=sender@gmail.com; spf=Pass smtp.mailfrom=sender@gmail.com;spf=None smtp.helo=postmaster@redacted.google.com; dkim=pass (signatureverified) header.i=@gmail.com; dmarc=pass (p=none dis=none) d=gmail.comIronPort-SDR: IronPort-PHdr: =X-IronPort-Anti-Spam-Filtered: trueX-IronPort-Anti-Spam-Result: =X-IronPort-AV: ;d="scan"X-Amp-Result: SKIPPED(no attachment in message)X-Amp-File-Uploaded: False
```

This shows some additional SPF/DKIM/DMARC checks, as well as the results from an IronPort scan. 

Ironport is a popular email filter used by many corporations to look for spam, viruses, and other malicious emails. It scans the links and attachments in the email and determines if the email is malicious (and should be dropped), if it is likely legitimate and should be delivered, or if it is suspicious in which case it can attach a header to the body which tells users to be wary of the email.

```
Received: from redacted.google.com ([IPAddress])by Redacted.localdomain.com with ESMTP/TLS/ECDHE-RSA-AES128-GCM-SHA256; Fri, 25 Oct 2019 16:16:36 -0400

Received: by redacted.google.com with SMTP idfor recipient@localdomain.com; Fri, 25 Oct 2019 13:16:35 -0700 (PDT)

X-Received: by IPv6:: with SMTP id; Fri, 25 Oct 2019 13:16:35 -0700 (PDT) Return-Path: sender@gmail.com

Received: from senderssmacbook.fios-router.home (pool-.nycmny.fios.verizon.net. [IP address redacted])by smtp.gmail.com with ESMTPSA id redacted IP(version=TLS1 cipher=ECDHE-RSA-AES128-SHA bits=128/128);Fri, 25 Oct 2019 13:16:34 -0700 (PDT)

Received: from senderssmacbook.fios-router.home (pool-.nycmny.fios.verizon.net. [IP address redacted])by smtp.gmail.com with ESMTPSA id redacted IP(version=TLS1 cipher=ECDHE-RSA-AES128-SHA bits=128/128);Fri, 25 Oct 2019 13:16:34 -0700 (PDT)
```

This section shows the internal hops the email took from the sender's initial device through gmail's routing system and to the outlook environment of the recipient. From this we can see that the initial sender was from a Macbook, using a home router, with Verizon Fios in NYC. 

This is the end of the hops showing the route the email has taken from sender to recipient. Past this, you'll see the body of the email (and the headers you typically see like "from:", "to:", etc.), perhaps with some formatting based on the media type and email client (for example the MIME Version, content type, boundary, etc). It may also contain some user-agent information, which is details on what type of device sent the message. 

In this case we already know that the sending device was a Macbook due to Apple's naming convention, but it may also contain details on the CPU type, version, even the browser and version which were installed on the device. 

In some cases, but not all, it might also contain the IP address of the sending device (though many providers will hide that information without a subpoena).

## What can email headers tell you?

Email headers can help identify when emails are not being sent from their purported senders. They can provide some information on the sender - though it usually isn't enough to identify the true sender. 

Law enforcement can often use this data to subpoena the information from the right ISP, but the rest of us can mostly just use it to help inform investigations, generally into phishing. 

This process is made harder by the fact that headers can be faked by malicious servers or hackers. Without contacting each server's owner and individually verifying that the headers in your email match their SMTP logs, which is painstaking and time-consuming, you won't be certain the headers are accurate (other than the headers attached by your own mail servers). 

Without contacting each server's owner and individually verifying that the headers in your email match their SMTP logs, which is painstaking and time-consuming, you won't be certain the headers are all accurate.. 

DKIM, DMARC and SPF can all help with this process, but aren't perfect, and without them, there's no verification at all.

Don't want to analyze your own headers? [This site](https://mailheader.org/) will do it for you.












