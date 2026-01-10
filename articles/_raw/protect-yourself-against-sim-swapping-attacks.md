---
title: How to Protect Yourself Against SIM Swapping Attacks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-02T20:05:26.000Z'
originalURL: https://freecodecamp.org/news/protect-yourself-against-sim-swapping-attacks
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/pexels-photomix-company-887751.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
seo_title: null
seo_desc: "By Megan Kaczanowski\nWhat is a SIM swap?\nSIM swapping is when a hacker\
  \ convinces your cell phone carrier to switch your phone number to a different SIM\
  \ - one that they own. \nThis is a relatively normal thing for a retail employee\
  \ to do, which means t..."
---

By Megan Kaczanowski

### What is a SIM swap?

SIM swapping is when a hacker convinces your cell phone carrier to switch your phone number to a different SIM - one that they own. 

This is a relatively normal thing for a retail employee to do, which means that someone asking for a swap doesn’t raise red flags. (Imagine that you bought a different phone and now needed to switch where your cell service was so you could continue receiving texts/calls on your new device).  

It doesn’t require a hacker to have any technical knowledge, just a SIM card and a phone call to your provider. Curious as to how easy this is? Check out [this video](https://www.youtube.com/watch?v=lc7scxvKQOo) of a woman breaking into someone’s phone carrier account in under 2 minutes. 

Even if the phone provider realizes that the action they’re being asked to take is unusual, often hackers will bribe customer service reps with upwards of $100 per swap (which is a huge incentive for employees who make ~$10/hour). 

Once the swap has been done, it is very difficult to reverse, as your phone will no longer work. Plus, you'll likely have to go to your carrier in person in order to prove that the swap was incorrect and that you are the owner of the account. 

Also, until you're able to do this, a hacker can intercept all your phone calls and messages – including SMS-based authentication codes for 2FA, and text-based password reset options. This could allow the attacker to access your online accounts, or blackmail you with information they've gleaned from text messages and phone calls.

## Have SIM swaps happened before?

Yes! The FTC's lead technologist was [hacked this way in 2016,](https://www.wired.com/2016/06/even-ftcs-lead-technologist-can-get-hacked/) as well as a number of [Instagram accounts](https://mashable.com/2018/08/13/instagram-hack-locked-out-of-account/). There's even [an entire crime ring](https://www.vice.com/en_us/article/j5bpg7/sim-hijacking-t-mobile-stories) dedicated to SIM swapping in order to sell instagram handles for bitcoin, as well as other criminal activities.

## What else can SIM swap attackers do?

[One victim reported that,](https://www.wired.com/2012/08/apple-amazon-mat-honan-hacking/)

> IN THE SPACE of one hour, my entire digital life was destroyed. First my Google account was taken over, then deleted. Next my Twitter account was compromised, and used as a platform to broadcast racist and homophobic messages. And worst of all, my AppleID account was broken into, and my hackers used it to remotely erase all of the data on my iPhone, iPad, and MacBook. [...]  
>   
> Had I been regularly backing up the data on my MacBook, I wouldn't have had to worry about losing more than a year’s worth of photos, covering the entire lifespan of my daughter, or documents and e-mails that I had stored in no other location.

If your phone number is tied to any online accounts, the hacker can often reset your password via text, meaning that the hacker now has access to all of your accounts. 

They can quickly reset your primary email address password, and then use that email address to trigger password resets for other accounts like Amazon, online banking, social media sites, and so on.

Here's [one example](https://www.wired.com/2012/08/apple-amazon-mat-honan-hacking/), 

> “_Apple tech support confirmed to me twice over the weekend that all you need to access someone’s AppleID is the associated e-mail address, a credit card number, the billing address, and the last four digits of a credit card on file. I was very clear about this._   
>   
> _During my second tech support call to AppleCare, the representative confirmed this to me. “That’s really all you have to have to verify something with us,” he said.”_ 

All of this information is relatively easy to find. Attackers can quickly look up addresses on sites like WhitePages and Spokeo, and there are [dedicated email lookup services](https://kinsta.com/blog/find-email-address/). 

Also, Apple needs any credit card number, not necessarily the one on file. The last 4 digits of a credit card on file is a little harder, but far from impossible. 

If an attacker has already compromised your primary email by resetting the password, they can use this information to reset access to accounts like Amazon (which show the last four digits of the credit cards on file). The hacker can then use this information to gain access to your AppleID and reset your password – as well as accessing all of your data on iCloud. 

If you’re like many people, and you store passwords or personal data on your phone (in your notes app) or in your iCloud backup, the hacker now has access to all of this information. They can steal it for blackmail purposes or delete it for the 'lulz'. Typically this information is unrecoverable.

## But I don’t have anything to hide!

This isn’t just about data, though most people would dislike having every text, email, and picture they have made public (or deleted!).  

After SIM swapping, hackers can place large orders on your Amazon account, break into your bank accounts, cryptocurrency wallets, or retirement accounts and empty them. They can also hijack your social media sites to spread disinformation, or views antithetical to your own (racist, homophobic, or otherwise offensive).

They can destroy your online life, then start on your friends and family. Often attackers will use your (compromised) email to reach out and phish them. 

Some of this might be reversible. Much of it is not. Once your online identity has been stolen, it’s very difficult to prove to various online platforms that you are the true owner. This becomes even harder when you don't control the platform's means of verification (like an email account or phone number).

## But no one would target me!

The most important thing to remember here is that often this isn’t a targeted attack on _you_. It’s unlikely that someone would say, ‘oh let's target this specific person’. However, hackers may target an account without knowing who the owner is. 

For example, common targets include cryptocurrency accounts or unique social media handles (‘the OG handles’ such as ‘@awesome’ – handles you would have needed to be first to a particular platform to claim).

Then the hacker will track down the owner, swap their SIM, and take what they want. This hack requires low levels of technical sophistication, time, and money, and is **extremely** lucrative (OG handles sell for between $500-$5000 each, while siphoning bank or retirement accounts can net upwards of thousands of dollars), making it extremely popular among hackers. 

Many of the hackers in the forums dedicated to SIM swapping are teenagers. They often don’t think about the long-term consequences of their actions, and are just pursuing fun. They’re not rational actors, and often don’t have to think about their victims as people whose lives they’re destroying as they never interact with them. 

It is also a very difficult hack to prosecute. Attribution is extremely difficult to ascertain for cyber attacks and the sheer volume of attacks taking place makes it really tough for law enforcement to keep up (particularly local law enforcement which often lags behind in technical sophistication and and legislation surrounding computer crimes). 

As one law enforcement agent noted,

>  “_For the amounts being stolen and the number of people being successful at taking it, the numbers are probably historic,” Tarazi said. “We’re talking about kids aged mainly between 19 and 22 being able to steal millions of dollars in cryptocurrencies._   
>   
> _I mean, if someone gets robbed of $100,000 that’s a huge case, but we’re now dealing with someone who buys a 99 cent SIM card off eBay, plugs it into a cheap burner phone, makes a call and steals millions of dollars. That’s pretty remarkable.”_ – [Source](https://krebsonsecurity.com/2018/11/busting-sim-swappers-and-sim-swap-myths/)

## Recommendations for everyone to keep your SIM safe

* Use a method of 2FA other than SMS, such as an app like Google Authenticator, or a hardware key like YubiKey. You should use this for as many sites as offer 2FA (at minimum it should be used for your primary email address).
* Use a [password manager](https://megankaczanowski.com/digital-security/)
* Add a PIN to your cell phone plan (not 100% effective, but better than nothing). All four major carriers in the United States offer this service. Many carriers in Africa (including in Mozambique, South Africa, Kenya, and Nigeria), the UK, and Australia have implemented protections to enable banks to check if the customer has swapped their SIM recently when processing a transaction (so if there was a recent SIM swap, they can refuse the transaction). This limits the damage an attacker can do, but it is still wise to remain wary to these types of attacks.
* Act immediately if you notice that your cell phone stops functioning. Call your cell phone service provider on a different device and lock down your accounts right away.
* Use services like Privacy or Blur which provide single use credit/debit cards for purchases in order to avoid linking a single credit card to many accounts.

### Additional recommendations for high-risk targets:

* Use a hardware key for your primary email address, and app-based 2FA for other accounts. Enable 2FA for as many accounts as offer it.
* If you use Gmail as your primary personal email account, enroll in their [Advanced Protection Program.](https://landing.google.com/advancedprotection/)
* Do not link your phone number to any accounts – this often enables password reset via text without warning you. If you must add a phone number to your account, set up a separate phone number with a service like MySudo or Google Voice. Do not use that phone number for ANYTHING else.

Thank you for reading – and stay safe.

### Sources/Further Reading:

* [How Apple and Amazon Security Flaws Led to My Epic Hacking](https://www.wired.com/2012/08/apple-amazon-mat-honan-hacking/)
* [Busting SIM Swappers and SIM Swappers](https://krebsonsecurity.com/2018/11/busting-sim-swappers-and-sim-swap-myths/)
* [How to Protect Yourself Against a SIM Swap Attack](https://www.wired.com/story/sim-swap-attack-defend-phone/)
* [The SIM Hijackers](https://www.vice.com/en/article/vbqax3/hackers-sim-swapping-steal-phone-numbers-instagram-bitcoin)
* [Hackers Are Breaking Into Telecom Companies to Take Over Customer Phone Numbers](https://www.vice.com/en/article/5dmbjx/how-hackers-are-breaking-into-att-tmobile-sprint-to-sim-swap-yeh)

