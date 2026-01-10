---
title: How to Recognize a Phishing Email – And What to Do When You Get One
subtitle: ''
author: Jose Vicente Nunez
co_authors: []
series: null
date: '2022-10-12T00:52:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-recognize-phishing-email
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725458523382/ab4b959e-8c84-4e48-88a5-bbc716255d1b.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: phishing
  slug: phishing
seo_title: null
seo_desc: 'You know the drill: you open your email client and there is it an email
  saying that you will be in trouble if you do not follow certain instructions in
  short time, no questions asked.

  All it takes is a single click, and you''re in trouble.

  This kind o...'
---

You know the drill: you open your email client and there is it an email saying that you will be in trouble if you do not follow certain instructions in short time, no questions asked.

All it takes is a single click, and you're in trouble.

This kind of email has a very [clear definition](https://www.phishing.org/what-is-phishing):

> [Phishing](https://www.knowbe4.com/phishing?hsLang=en) is a [cybercrime](https://www.merriam-webster.com/dictionary/cybercrime) in which a target or targets are contacted by email, telephone or text message by someone posing as a legitimate institution to lure individuals into providing sensitive data such as personally identifiable information, banking and credit card details, and passwords.

In this article, I'll explain what phishing is and how to recognize the signs that an email may not be legit. For that, we will learn to do the following:

* Recognize some obvious flags of a phishing email
    
* Use some command tools on Linux to carefully inspect suspicious links
    
* Analyze the suspicious emails with several free online tools
    

All this while having some fun.

## Example of a Phishing Email

Let me share a quite clever example email (some details have been changed to protect the innocent):

![Image](https://www.freecodecamp.org/news/content/images/2022/10/godaddy_phishing_emails.png align="left")

*Phishing email pretending to be GoDaddy*

Let me show you how you can quickly spot scammers, without using a single line of code

You will need the following to go through some of the steps of this tutorial:

* A Linux installation, with [curl](https://curl.se/) installed.
    
* A Web browser (Brave or Firefox are good choices)
    
* **Curiosity**
    

Now let's move on and see what we've got in our mailbox...

## Common Sense Phishing Red Flags

Right out of the box, this email violates two simple rules, despite having proper grammar and nice presentation:

First, of all, it **forces you to act immediately to fix an issue** (Urgent action required), **no questions asked** (Click the nice button).

To make it worse, there's no way to verify that the person contacting you really works for the company. Reputable companies ask you to log into their website and offer a case # so you can track the issue. Neither of those are here.

Second, despite their best efforts, **scammers make qualitative mistakes**. Do you see that *customer #* on the upper right part of the screenshot? I compared it to mine on the real website and guess what? It's a different number.

But where is the fun of analyzing this if we cannot do even a little bit of poking? Well, when I moved my mouse over the button image I could see the link and it was pointing to tiny URL (an URL shortening service):

```python
https://tinyurl.com/xszszasxdxdxdxdxdxdxdzs?a=xxx@xxxx.com
```

So whoever is doing this is trying to conceal the real URL. No problem, copy the URL address (**never click it**), change the email part of the GET request to some garbage (?a=xxx@xxx.com)) and then run it through curl. I got this:

```html
<table width="75%" bgcolor="#FFFFFF" align="center" cellpadding="10">
        <tr>
            <td>
                <h2>URL Terminated</h2>
                <p>
                    The TinyURL (xszszasxdxdxdxdxdxdxdzs) you visited was used by its creator in violation of our terms of use.
                    TinyURL has a strict no abuse policy and we apologize for the intrusion this user has caused you.
                    Such violations of our terms of use include:
                </p>
                <ul>
                    <li>Spam - Unsolicited Bulk E-mail</li>
                    <li>Fraud or Money Making scams</li>
                    <li>Malware</li>
                    <li>or any other use that is illegal.</li>
                </ul>
                <p>
```

So the good people from Tiny URL noticed this too and terminated the URL. Nice work!

[![asciicast](https://asciinema.org/a/526911.svg align="left")](https://asciinema.org/a/526911)

Let's use other tools to confirm what we know already.

## Online Tools You Can Use to Analyze Suspicious URLs

Tiny URL was nice enough to tell us about the original URL:

```text
https://parasolhealth.org/resources/sass/hgjhgbgb/%20hxghxhgcgzvzvhgxvgzhxgvvgvcgvhgvjhvxhgvzhgvshgvhgvhgvhgwvhgwvhgwvhgwvhgvhgvdshvshgvhgvhgdvhgdsvhgdvhjgdvjhdgdvhgfvhgvf/vhgvjhgvghgvghvhgvghvhgvjlnkjndkjdkjdhbgytdvghdvhvshgvshgvjsvhvahgvhvwgvhwvhvajgvsgshgvhsgvjhsvgavjgvsgvahgvahgvhgsvjgavhgsvhgsvhjvshgvahgvsjvshgvajvshvhgwvhgvehgvehgvehjvegvejhgvhgavhavhs/dhbjhjfhjfkbkjfhbjkbfjbjdbkjbsjhbdjbjkdbhbdjkbjdbjdbjhbdkjbsjbjkdbjkdhbjdbjbsjhbsjbjdkbjhdbkjhbdkjbsbdjbjdbkjhbjhbsjkhbdjbjdbjdbjhsbjhbejhbejhbjwhbjhwbjkwhbjbhbs/jdbhdhdbkjbsjbsjbwjbjwbjkbwhbehbjhbejbebebjebjbejbjhbsjhbshbahbjhsbshbjkhdbjhbjhbdbdjkbdhbjhsbjhbajhbsjbkjshbhbdjhbjdhbjkbshbsjhbsjbdbdhbdhbjehbjhebjhbrrhbjbjekhbjhbjsbjhsbjhbdjhd/jbdjhbdkjbdjhbkjabjhbsjbdjbksjbhsbjhdbjhbjkbdjhbjhbkjbejhbwkhbjkwhbjhwbjkwhbjhwbjhbwhbwkjhbwjhbjhbajhbajhbsjhbsjhbdjkhbdjhbdjhbjdhbjshbjhsbjhbjhsbkjhbdjhbsjbjabjhabjkbs/redirect.php
```

If you go to the Virus Total website and search for the URL you will see that this [was also reported here](https://www.virustotal.com/gui/url/1a5a1a3385c2d6c2c76b0ca721138ba9eeae7b8a12cc6e28c206216c103c3fc3?nocache=1):

![Image](https://www.freecodecamp.org/news/content/images/2022/10/godaddy_virustotal_malicious.png align="left")

Interestingly enough, only a single vendor reported the URL as malicious. That will do it for me :-)

Also [Abuse IP DB](https://www.abuseipdb.com/report?ip=66.85.143.2) doesn't know anything about the offending website. However keep this tool around as it is known to reports multiple other actors.

There is anything else we can learn from the original message? Most email readers allow you to copy and paste the email headers. I'm sharing mine here (with a few changes):

```text
Received: from MN2PR19MB4030.namprd19.prod.outlook.com (2603:10b6:208:1e8::11)
 by MW3PR19MB4204.namprd19.prod.outlook.com with HTTPS; Tue, 4 Oct 2022
 16:35:05 +0000
Received: from BN9PR03CA0959.namprd03.prod.outlook.com (2603:10b6:408:108::34)
 by MN2PR19MB4030.namprd19.prod.outlook.com (2603:10b6:208:1e8::11) with
 Microsoft SMTP Server (version=TLS1_2,
 cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.5676.31; Tue, 4 Oct
 2022 16:35:01 +0000
Received: from BN7NAM10FT104.eop-nam10.prod.protection.outlook.com
 (2603:10b6:408:108:cafe::cc) by BN9PR03CA0959.outlook.office365.com
 (2603:10b6:408:108::34) with Microsoft SMTP Server (version=TLS1_2,
 cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.5676.24 via Frontend
 Transport; Tue, 4 Oct 2022 16:34:59 +0000
Authentication-Results: spf=softfail (sender IP is 170.10.162.128)
 smtp.mailfrom=bounce.com; dkim=none (message not signed)
 header.d=none;dmarc=fail action=oreject header.from=godaddy.com;compauth=fail
 reason=000
Received-SPF: SoftFail (protection.outlook.com: domain of transitioning
 bounce.com discourages use of 170.10.162.128 as permitted sender)
Received: from host.solutiononellc.com (170.10.162.128) by
 BN7NAM10FT104.mail.protection.outlook.com (10.13.157.118) with Microsoft SMTP
 Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id
 15.20.5676.17 via Frontend Transport; Tue, 4 Oct 2022 16:34:59 +0000
Received: from ip250.ip-37-187-205.eu ([37.187.205.250]:38823)
	by altar47.supremepanel47.com with esmtpsa  (TLS1.2) tls TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
	(Exim 4.95)
	(envelope-from <postmaster@bounce.com>)
	id 1ofksk-0005Zd-LV
	for xxx@xxxx.com;
	Tue, 04 Oct 2022 16:34:58 +0000

Using [MXToolbox](https://mxtoolbox.com/Public/Tools/EmailHeaders.aspx?huid=4205dc8f-5147-4da5-a448-d633f2bbca61) shows that 2 of the email addresses used in the chain are **blacklisted**, another red flag.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/godaddy_scammer_mxtoolbox.png)
_2 blocked emails from this list. Another read flag_

I think that's good enough. Delete the email and move on with your life, and be sure a new email is coming your way (hopefully landing in the SPAM folder automatically).

## What's Next?

There are many tools on the Internet you can use to identify phishing emails, but there is no substitute for common sense. It if looks too good to be true then it probably is.

As usual, do not click the link right away! Do a little investigating first, just to be safe.
```
