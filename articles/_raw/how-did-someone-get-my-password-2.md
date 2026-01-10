---
title: How did someone get my password?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-30T05:46:00.000Z'
originalURL: https://freecodecamp.org/news/how-did-someone-get-my-password-2
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d47740569d1a4ca36db.jpg
tags:
- name: cyber
  slug: cyber
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: passwords
  slug: passwords
- name: phishing
  slug: phishing
seo_title: null
seo_desc: 'By Megan Kaczanowski

  Have you ever received a ''sextortion'' email telling you that your computer has
  been hacked and warning you that if you don''t pay up, they will release videos
  of an intimate nature to your entire contact list? Did the email includ...'
---

By Megan Kaczanowski

Have you ever received a ['sextortion](https://www.forbes.com/sites/zakdoffman/2019/08/05/200m-email-addresses-held-by-sextortion-attackers-is-yours-on-their-list/#4214f11f67e4)' [email](https://www.cnbc.com/2019/06/17/email-sextortion-scams-on-the-rise-says-fbi.html) telling you that your computer has been hacked and warning you that if you don't pay up, they will release videos of an intimate nature to your entire contact list? Did the email include an old password of yours as 'proof' that their claims were true? Did you wonder how they got your password?

## What is Phishing?

Statistically, this was probably from a phishing email. In 2018, 93% of all breaches globally began with a phishing or pretexting attack.

Phishing emails are extremely common and highly effective. They use emotion such as fear and shame (in sextortion emails or 'male enhancement ads'), urgency (my boss needs this now!), or greed (I won a new car??). 

They can also be sent via text message (SMiShing), voice (vishing), email (phishing), and social media phishing. 

The more people adapt, the more the hackers change in response – their tactics are constantly evolving.  

Usually phishing emails contain a link or an attachment. Once you click the link or open the attachment, they may install malware on your device or trick you into entering your credentials into a fake site (which looks just like the real site). The malware will check to see if it can exploit unpatched vulnerabilities in order to install more malware onto your system (which can then steal passwords, install keyloggers to record all of your keystrokes – and therefore your passwords! – and so on). 

Once the hacker has stolen your credentials, they can do things like exfiltrate your personal financial data or account information, or those of your customers if this happens on your corporation's device.

Phishing deserves its own article entirely, so if you're interested in learning how to phish, check out [this article](https://www.pentestgeek.com/phishing/how-do-i-phish-advanced-email-phishing-tactics).

## How can you stop phishing from impacting you?

Defending against phishing is also difficult. As an individual, the best thing you can do is use caution when opening emails – be wary of emails which play on your emotions, ask you to make quick decisions, or seem too good to be true. 

Look out for unusual senders (do you recognize the person emailing you? Is this the same email address they've used before?), or unexpected links or attachments. If you're unsure if an email is legitimate, confirm that it is with the sender via a different method of communication.

You should also use antivirus and endpoint protection software. The paid version is better than the free version, as it is updated as new malware is identified. But the free version is usually better than nothing. I like Malwarebytes for laptops.

Security teams will use a myriad of tools:

* email filtering mechanisms that attempt to reduce the phishing and spam emails which reach user's inboxes, 
* measures like SPF, DKIM, and DMARC which can help provide authentication that an email is telling the truth about where it came from, 
* user awareness training, 
* and endpoint protection mechanisms. 

Endpoint protection mechanisms can range from simple anti-virus to agents installed on every device. These will try to prevent known malware from running, identify unusual behavior, and prevent malicious processes from running by alerting a security operations team or forcing the program to quit. 

This way, even if the email gets through the filters and the user doesn't notice anything wrong, the endpoint protection will keep the malware from actually doing damage to the machine.

## How else could someone have gotten my password?

Often when a hacker breaches a company, they will sell the usernames and passwords they've obtained on the dark web. 

> **Surface Web:** What you can find on Google or other popular search engines. This is probably most of what you think of as the internet. Compared to the deep web, this is a very small portion of information which is ‘online’.

> **Deep Web:** Information which is online, but isn’t indexed (searchable) by Google and other popular browsers. This is information such as that contained in government or university databases. Often this information is hidden behind a paywall or other restriction mechanism.

> **Dark Web:** The dark web requires certain browsers, such as a ‘TOR browser’ to access. Some, though not all, of this content is illegal. This is often a place where criminals gather to talk on forums, sell illegal services and goods, and sometimes activists living under repressive regimes gather to communicate.

If you were re-using passwords and usernames between different websites (particularly since your email is probably used as your username for many websites), a hacker might already have your username and password. 

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screen-Shot-2019-10-04-at-4.06.38-PM.png)
_[https://xkcd.com/792/](https://xkcd.com/792/)_

The hacker will then perform something called 'credential stuffing'. Credential stuffing is when an attacker takes these usernames and passwords and plugs them into an automated 'account checker' which basically tries the username/password combination across many, many different sites across the internet, from social media logins to bank accounts. If the password works, the hacker now has access to the account and can drain an account, sell the data, etc. 

For a better description, check out XKCD's comic below.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-27-at-12.56.37-PM.png)
_[https://xkcd.com/2176/](https://xkcd.com/2176/)_

## How do you defend against credential stuffing?

Don't reuse your passwords. Use a password manager like 1[Password](https://1password.com/) or [LastPass](https://www.lastpass.com/solutions/business-password-manager). [KeePass](https://keepass.info/) is (in my opinion) less user friendly, but it's free!

Password managers can securely store your passwords and often have browser extensions and apps so they can autofill your passwords across many accounts. Plus, you only have to remember one master password this way. But your master password now grants access to all of your other passwords, so make sure it's very strong! 

They can also help you autogenerate very strong passwords, and some even have vaults so you can store other sensitive information (bank account details, insurance information, etc.). 

I personally use 1Password because I like the family account option – if anyone in your family ever gets locked out, someone else can reset their account password (but won't have access to your individual vault). 

You can also set up free alerts with [Have I Been Pwned](https://haveibeenpwned.com/). This site aggregates information from data breaches and provides consumers with the ability to use that information to protect themselves. You can navigate to the 'Notify Me' tab at the top and enter your email address. 

After you confirm the email address you've entered (where it will provide your current exposure), the site will send you an email anytime your email is involved in a data breach. That is, any breach the site is alerted to – their coverage is very good, but no single source will contain every leaked data breach. This way, you can just change the impacted password, and won't have to worry about it impacting any of your other accounts.

If you're working on security for a large organization, enterprise password management software (the same companies listed above provide these services) is a great idea, as well as strong password policies (mandating that your employees use sufficiently strong passwords). Have I Been Pwned also has a service which allows the domain owner to monitor for breaches which involve any email on the domain (and it's free!). 

## How else do hackers get passwords?

There are a few other possibilities – shoulder surfing, or basically watching you type your password – though this is unlikely given that the person has to be physically watching you. 

Then there's theft of passwords which have been written down, or just [pictures of written down passwords which are visible in photos](https://www.businessinsider.com/hawaii-emergency-agency-password-discovered-in-photo-sparks-security-criticism-2018-1). Again, this is much less likely than any of the above options as it typically comes from a targeted attack (which is inherently less common than crimes of opportunity).

Avoiding these two is pretty simple – don't allow someone to watch you enter your password, and don't write down your password. Use a password manager instead! If you simply have to write it down, store it someplace that someone is unlikely to search through or find by accident. I'd suggest the bottom of a box of tampons. Much more secure than a sticky note on your monitor.

## It seems really easy to get hacked. Should I be concerned? 

The most important thing to remember about hacking is that no one wants to do more work than they have to do. For example, breaking into your house to steal your password notebook is a lot harder than sending phishing emails from the other side of the world. If there's an easier way to get your password, that's probably what a nefarious actor will try first. 

That means that enabling basic cyber security best practices is probably the easiest way to prevent getting hacked. In fact, Microsoft [recently reported](https://www.zdnet.com/article/microsoft-using-multi-factor-authentication-blocks-99-9-of-account-hacks/) that just enabling Two-Factor Authentication will end up blocking 99.9% of automated attacks.  

So, enable 2FA, use a password manager to autogenerate long, complex, unique passwords for every account, and think before you click! Avoid clicking on sketchy or unexpected links and attachments, and stay vigilant.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-27-at-1.18.47-PM.png)
_[https://xkcd.com/538/](https://xkcd.com/538/)_

### 

## 

