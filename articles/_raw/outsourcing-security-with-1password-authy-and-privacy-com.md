---
title: How to Outsource Your Online Security with 1Password, Authy, and Privacy.com
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-03-17T22:08:13.000Z'
originalURL: https://freecodecamp.org/news/outsourcing-security-with-1password-authy-and-privacy-com
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/cover-4.png
tags:
- name: authentication
  slug: authentication
- name: cybersecurity
  slug: cybersecurity
- name: life
  slug: life
- name: passwords
  slug: passwords
seo_title: null
seo_desc: 'Take some work off your plate while beefing up security with three changes
  you can make today.

  Unstable times are insecure times, and we’ve already got enough going on to deal
  with. When humans are busy and under stress, we tend to get lax in less-ob...'
---

Take some work off your plate while beefing up security with three changes you can make today.

Unstable times are insecure times, and we’ve already got enough going on to deal with. When humans are busy and under stress, we tend to get lax in less-obviously-pressing areas, like the security of our online accounts. 

These areas only become an obvious problem when it’s too late for prevention. Thankfully, most of the work necessary to keep up our cybersecurity measures can be outsourced.

Implementing proper cybersecurity measures can be fiddly, and I especially dislike fiddling with things that I could avoid fiddling with. 

These fiddly things include resetting forgotten passwords, transferring multifactor authentication (MFA) codes when I change devices, and dealing with the fallout of compromised payment details in the event one of my accounts is still breached.

Here are three changes I’ve made that significantly reduce the chances of needing to fiddle with any of these things again. You can too.

## 1Password

I’ve historically avoided password managers because of an irrational knee-jerk reaction to putting all my eggs in one basket. 

You know what’s great for irrational reactions? Education. To figure out if putting all my passwords into a password manager is more secure than not using one, I set out to see what some smart people wrote about it.

First, we need to know a thing or two about passwords. Troy Hunt figured out almost a decade ago that [trying to remember strong passwords doesn’t work](https://www.troyhunt.com/only-secure-password-is-one-you-cant/). In more recent times, Alex Weinert expanded on this in [Your Pa$$word doesn’t matter](https://techcommunity.microsoft.com/t5/azure-active-directory-identity/your-pa-word-doesn-t-matter/ba-p/731984). 

TL;DR: our brains aren’t better at passwords than computers, and please use MFA.

So passwords don’t matter, but complicated passwords are still better than memorable and guessable ones. 

Since I’ve next to no hope of remembering a dozen variations of `p/q2-q4!` (I’m not a [chess player](https://inbox.vuxu.org/tuhs/CAG=a+rj8VcXjS-ftaj8P2_duLFSUpmNgB4-dYwnTsY_8g5WdEA@mail.gmail.com/)), this is a task I can outsource to [1Password](https://1password.com/). I’ll still need to remember one, long, complicated master password - 1Password uses this to encrypt my data, so I really can’t lose it - but I can handle just one.

Using 1Password specifically has another, decidedly obvious, advantage. I chose 1Password because of their [Watchtower](https://support.1password.com/watchtower/) feature. [Thanks to Troy Hunt’s Have I Been Pwned](https://www.troyhunt.com/have-i-been-pwned-is-now-partnering-with-1password/), Watchtower will alert you if any of your passwords show up in a breach so you can change them. Passwords still don’t completely work, but this is probably the best band-aid there is.

One last bonus is that using a password manager is a heck of a lot more convenient. Complicated passwords need not take two tries to type. 

When it comes to sites that I only rarely use, and don’t consider important, I’m typically far more likely to end up (re)setting those passwords to something memorable, and thus something easily hacked. Even - perhaps especially - unimportant sites can open doors to your more important ones. 

Using 1Password and generated passwords, those sites are now also first-class citizens in the land of strong passwords, instead of being half-abandoned and half-open attack vectors.

So, yes, all my eggs are in one basket. A well-protected, complex, and monitored basket, as opposed to being scattered about in several of those paper cartons from the grocery store that don’t really close and certainly can’t survive a _rather gentle bump_ as you come in the doorway, Victoria, how many times do I need to remind you to be careful.

## Authy

Okay - so it’s more like one-and-a-half baskets. ??

[Authy](https://authy.com/), from the folks over at [Twilio](https://www.twilio.com), provides a 2FA solution that’s more secure than SMS (I find this to be an interesting intersection, coming from Twilio, and I applaud.) [Unlike Google Authenticator](https://authy.com/blog/authy-vs-google-authenticator/), you can choose to back up your 2FA codes in case you lose or change your phone. (1Password offers 2FA functionality as well - but, you know, redundancies.)

With Authy, your back up is encrypted with your password, similarly to how 1Password works. This makes it the second password you can’t forget, if you don’t want to lose access to your codes. If you reset your account, they all go away. I can deal with remembering two passwords; I’ll take that trade.

I’ve tried other methods of MFA, including hardware keys, which can make accessing accounts on your phone more complicated than I care to put up with. I find the combination of 1Password and Authy to be the most practical combination of convenience and security that yet exists in my knowledge.

## Privacy.com

Finally, there’s one last line of defense you can put in place in the unfortunate event that one of your accounts is still compromised. All the strong passwords and MFA in the world won’t help if you open the doors yourself, and scams and phishing are a thing.

Since it’s rather impractical to use a different real credit card every place you shop, virtual cards are just a great idea. There’s no good reason to spend an afternoon (or more) resetting your payment information on every account just to thwart a misbehaving merchant or patch up a data breach from that online shop for cute salt shakers you made a purchase at last year (just me?).

By setting up a separate virtual card for each merchant, in the event that one of those merchants is compromised, I can simply pause or delete that card. None of my other accounts or actual bank details are caught up in the process. Cards can have time-oriented limits or be one-off burner numbers, making them ideal for setting up subscriptions.

This is the sort of basic functionality that I hope, one day, becomes more prevalent from banks and credit cards. In the meantime, I’ll keep using [Privacy.com](https://privacy.com/join/Q6V3V). That’s my referral link; if you’d like to thank me by using it, we’ll both get five bucks as a bonus.

## Outsource better security

All together, implementing these changes will probably take up an afternoon, depending on how many accounts you have. It’s worth it for the time you’d otherwise spend resetting passwords, setting up new devices, or (knock on wood) recovering from compromised banking details.  

Best of all, you’ll have continual protection just running in the background - an effortless boost to your [personal cybersecurity posture](https://victoria.dev/blog/personal-cybersecurity-posture-for-when-youre-just-this-guy-you-know/).

We have the technology. Free up some brain cycles to focus on other things - or simply remove some unnecessary stress from your life by outsourcing the fiddly bits.

