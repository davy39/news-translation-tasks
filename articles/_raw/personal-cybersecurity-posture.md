---
title: How to strengthen your personal cybersecurity posture for when you're just
  this guy, you know?
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-10-08T13:05:00.000Z'
originalURL: https://freecodecamp.org/news/personal-cybersecurity-posture
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/cover.jpg
tags:
- name: authentication
  slug: authentication
- name: biometric authentication
  slug: biometric-authentication
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: internet
  slug: internet
- name: vpn
  slug: vpn
seo_title: null
seo_desc: '“Zaphod’s just this guy, you know?”

  – Halfrunt, Hitchhiker’s Guide to the Galaxy by Douglas Adams. The book, not the
  movie. Definitely not the movie.


  Some people (??‍) are really into cybersecurity, end-to-end encryption, and totally
  geeked out when...'
---

> _“Zaphod’s just this guy, you know?”_

> – Halfrunt, Hitchhiker’s Guide to the Galaxy by Douglas Adams. The book, not the movie. Definitely not the movie.

Some people (??‍) are really into cybersecurity, end-to-end encryption, and totally geeked out when they first learned how the [Enigma](https://en.wikipedia.org/wiki/Enigma_machine) worked. These people are likely to have an innate interest in building a less-than-laughable personal cybersecurity posture.

Most people, unfortunately, consider cybersecurity optional. Most people say things like:

_“There’s no one targeting lil ol’ me.”_  
 _“I have nothing to hide, anyway.”_  
 _“I’m too busy to learn all this stuff. Why can’t someone just give me a simple summary of best practices that I can skim in approximately seven minutes?”_

To those people, I say, hello, hypothetical incorporeal reader! Here is a simple summary of best practices that you can skim in approximately seven minutes.

#### Wait why do I care

You may have a hard time understanding why cybersecurity matters when you’re just an average person. Sure, you don’t want your devices hacked or your personal data stolen, but it’s not like anyone is coming after _you_, specifically, right?

Hey Alex, I’ll take “right,” for $400. It’s unlikely anyone is attempting to steal your _particular_ stuff, although I must admit that Persian rug of yours would really tie the room together. Instead, it can help to understand cybersecurity if you think of it in terms of low-hanging fruit.

You’ve got some fruit, I’ve got some fruit. Joe from down the block has a 1.21 gigawatt flux-capacitor-powered fruit-snatching robot. Joe doesn’t know either of us exist, but his robot goes (very quickly) from door to door, all the way around the block, looking for fruit. If my front door is locked and yours is standing open, whose fruit is Joe’s robot going to snatch?

If that sounds like boring, old, _regular_ security, you’re correct! Cybersecurity isn’t about finding some magic spell that makes your fruit maximally secure. It’s about making your fruit more secure than the fruit next to you. You do this by employing some thoughtful habits, in much the same way as you learned to lock your front door to guard against fruit-snatching robots.

Security breaches and incidents happen every day. Most of them occur because an automated scanner cast a wide net and found a person or company with lax security that a hacker could then exploit. Don’t be that guy.

#### Wait what's a security posture anyway

Here is how the National Institute of Standards and Technology defines security posture:

> _The security status of an enterprise’s networks, information, and systems based on information assurance resources (e.g., people, hardware, software, policies) and capabilities in place to manage the defense of the enterprise and to react as the situation changes._ ([NIST Special Publication 800–30, B-11](https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final#pubs-topics))

The important bit above is, _“capabilities in place to manage the defense of the enterprise.”_ In the context of personal security, you are the enterprise. Congratulations. May you boldly go where no man has gone before.

Before you explore strange new worlds (it _is_ the Internet, after all), there are steps you can take to manage your defenses. The word “capabilities” is apt, as having certain things in place will pretty much give you cybersecurity superpowers. Here are the three steps I consider most important and beneficial:

1. Use multifactor authentication
2. Use a VPN
3. Develop healthy skepticism

With these three keys in hand, your cybersecurity posture goes from being robot lunch to War Games — where the winning move for an attacker is not to play.

#### 1. Use multifactor authentication

Passwords are dead. Computationally, they are a solved problem, and cracking passwords is just [a matter of time](https://howsecureismypassword.net/). Unfortunately, many people still help to speed up the process by using the same [compromised passwords](https://haveibeenpwned.com/Passwords) for multiple accounts, putting themselves at risk for inconceivable benefit. [Pass phrases](https://pages.nist.gov/800-63-3/sp800-63b.html#a2-length) are longer and more complicated, and would take a lot more time to crack. I highly recommend them; even so, [your password ultimately doesn’t matter](https://techcommunity.microsoft.com/t5/Azure-Active-Directory-Identity/Your-Pa-word-doesn-t-matter/ba-p/731984).

The answer, at least for now, is [multifactor authentication](https://en.wikipedia.org/wiki/Multi-factor_authentication) (MFA). MFA is made up of three kinds of authentication factors:

1. Something you know, like a pass phrase;
2. Something you have, like a chip pin card or phone; and
3. Something that you are, like your face or fingerprint.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/mfa.png)

Two or more of these factors are infinitely better than a password alone, especially if [your password is on this list](https://en.wikipedia.org/wiki/List_of_the_most_common_passwords).

Multiple authentication factors are now widely supported by account providers and social media sites. If you have the choice, avoid using text messages as a way of receiving authentication codes. SMS authentication leaves you vulnerable to the [SIM swap attack](https://en.wikipedia.org/wiki/SIM_swap_scam) — please direct further questions to [Jack Dorsey](https://www.nytimes.com/2019/09/05/technology/sim-swap-jack-dorsey-hack.html). Instead, use an authenticator app like [Google Authenticator](https://google-authenticator.com/) to generate codes on your device. This ensures that you alone, using that particular device, will have the correct authentication code. No power in the ‘verse can stop you.

The Google Authenticator app works with the specific device you set it up on, so when you get a new device you will need to [move Google Authenticator to your new phone](https://support.google.com/accounts/troubleshooter/4430955?hl=en#ts=4430956). Hardware authentication keys such as the [YubiKey](https://www.yubico.com/) may present less hassle when switching devices, but aren’t yet as widely supported as authentication apps.

#### 2. Use a VPN

The difference between using a VPN and not using one is like how The Dark Knight Rises was really good and Batman v Superman was really, really bad. Same franchise, totally different standards.

Let’s say you send a lot of mail, but never bother to put your letters in envelopes or even fold them in half. Anyone who bothers to look will know that you’re not really the Dread Pirate Roberts after all. When you use a Virtual Private Network, especially if you often connect to public WiFi, it’s like putting your letters into cryptographically-sealed envelopes and sending them via a special invisible courier service. No one but the intended recipient can read your letters, and no one but you and the courier know to whom the letters are sent.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/vpnmail.png)

VPNs prevent others from reading your communications, like opportunistic attackers who scan open WiFi, and even your own Internet Service Provider (ISP) who may sell your usage data for advertising dollars.

Choosing a trustworthy VPN provider requires some research, and is in itself material enough for a separate article. As a starting point, look for providers with firm policies against logging, and expect to pay between $5-$10 USD monthly for the service. Avoid free VPN apps and services with ambiguous privacy policies; they’ll typically cost you much more than you’ll know.

#### 3. Develop healthy skepticism

Ultimately, the weakest link in your cybersecurity defense is you. All the MFA and VPNs on the Internet won’t protect you if a scam or malware bot can trick you into opening the front gates. Yes, I know it’s a very nice looking wooden horse. Also free. Did you order it? No? Then it can stay outside.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/horse.png)
_Always look a Trojan gift horse in the mouth._

Develop the habit of second-guessing things delivered to your virtual doorstep. Email, phone, and messaging scams range in sophistication, from rickety robot-assembled shotgun blasts to elaborate social engineering attacks that [use cognitive biases very effectively](https://www.youtube.com/watch?v=8bAuA1isCz0). Don’t assume you’re too clever for them; humans are very predictable creatures. After all, nobody expects the Spanish Inquisition.

Instead, ask questions. Double check communications that ask you to click on links or visit a website, even if they come from someone you know or a company you use. If you’re not certain, based on a previous in-person interaction, that your friend or bank or mother sent this email, pick up the phone and call them. Even if you think you are certain, pick up the phone and check. You don’t call your mother enough, anyway.

Oh, and if the person on the phone is from your local tax office or the IRS or the CRA and they’re about to freeze your accounts because a case of mistaken identity has resulted in you being criminally charged for not repaying a loan on a 600-foot yacht in Malibu, just hang up. You know better than that. Tax agencies don’t have phones.

#### Your personal cybersecurity starter pack

You now have three keys to open three gates to a robust personal cybersecurity posture. If those keys have also unlocked your curiosity, there’s plenty more rabbit hole to go down. I highly recommend the [Security in Five podcast](https://securityinfive.com/) for Binary Blogger’s great advice, which inspired much of this post. [Surveillance Self Defense](https://ssd.eff.org/) offers the Electronic Frontier Foundation’s tips on securing online communication. Troy Hunt also has a YouTube series entitled [Internet Security Basics](https://www.troyhunt.com/get-to-grips-with-internet-security-basics-courtesy-of-varonis/) that goes into more depth on how to protect yourself online.

For now, I hope you use your newfound cybersecurity powers for good. Mind what you have learned. Save you it can.

