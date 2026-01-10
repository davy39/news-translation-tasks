---
title: Social Engineering — The Art Of Hacking Humans
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-09-28T19:16:11.000Z'
originalURL: https://freecodecamp.org/news/social-engineering-the-art-of-hacking-humans
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/wall-2.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: social engineering
  slug: social-engineering
seo_title: null
seo_desc: 'Social engineering is the act of manipulating someone into divulging information
  or doing something that''s not usually in their best interest. In this article,
  we will look at a few common ways Social Engineers try to manipulate you.


  Disclaimer: My ...'
---

Social engineering is the act of manipulating someone into divulging information or doing something that's not usually in their best interest. In this article, we will look at a few common ways Social Engineers try to manipulate you.

> _Disclaimer: My articles are purely educational. If you read them and cause damage to someone, that's on you. I don't encourage any malicious activity or black hat practices. [Read the code of ethics here](https://www.sans.org/security-resources/ethics)._

One common type of scam is the [Spanish Prisoner](https://en.wikipedia.org/wiki/Spanish_Prisoner), which dates back to the 18th century and has lots of modern incarnations. 

It usually involves someone who's in trouble and needs your help to access their fortune. You just need to wire a few thousand dollars, then they'll pay you back ten times over. But you can guess how that ends.

There are similar scams that have circulated the internet: The IRS scam, Lottery scams, and so on. These are broadly classified as [Advance offer scams](https://en.wikipedia.org/wiki/Advance-fee_scam). You have something waiting for you but you have to pay an advance to receive it.

To the average person, these will seem like poorly executed scam attacks. But these scams have caused thousands of people to lose their hard-earned money. In some cases, [their life savings](https://www.youtube.com/watch?v=_1sRz6CHPFs&ab_channel=NEWSCENTERMaine).

These are all examples of social engineering in action.

The idea behind social engineering is to take advantage of a potential victim’s natural tendencies and emotional reactions. Fear and greed are the most vulnerable emotions that are usually taken advantage of by Social Engineers. 

Below is a great example of a real-world Social engineering attack.

%[https://youtu.be/fHhNWAKw0bY]

## Types of Social Engineering Attacks

Social engineering can be broadly classified into five types of attacks based on the type of approach used to manipulate a target. Let's go through each one of them.

### Spamming (Email, Text, Whatsapp)

Spamming involves sending messages to large groups of people whose contact info is usually obtained through nefarious methods. Spamming is a general term used to define both malicious and non-malicious message broadcasting.

Non-malicious spamming is used by advertisers who try to promote their products to random strangers by emailing them in bulk. Their motive is not to cause damage, but to try and get people to buy their products or promote their services.

Malicious spamming includes messages that try to lure users to the attacker’s website to divulge personal information. This information is then used to craft targeted phishing/vishing attacks on the potential victim.

### Phishing (and Vishing)

When the attacker uses text messaging, email, or voice calling (voice phishing = vishing), it is called Phishing. 

Phishing is used to make the target believe they are being called by a legitimate institution or an entity in order to extract valuable information from the target.

If someone calls your company pretending to be your printer supplier, they might be able to gain specific information about the printer — the model, IP address (if connected to the internet), and so on. 

And once this information is given, the printer might be attacked in order to gain access to your internal network.

Email-based phishing attacks are also common. An attacker can email someone in your company pretending to be Facebook. Once a team member clicks a link, they will end up on a page that looks like Facebook, asking them for their login information. This login information will be sent to the attacker’s server after which they have complete access to the victim’s Facebook account.

The major difference between Phishing and Scamming is that phishing attacks are highly targeted. The attacker knows whom they want to attack and what type of information they are looking for.

### Baiting

Baiting involves designing a trap and waiting for the potential victim to walk into the trap. As a simple example, if an attacker drops a few USB drives in your company’s parking lot, chances are, one of your employees will try and plug it into their computer to check the contents of the USB drive.

This might sound silly but there have been numerous instances where simple tricks by Social Engineers have resulted in massive corporate data breaches. It is usually easy to bait people with scams such as the Advance offer scams that are still circulating the internet, feeding on gullible people.

Another common type of baiting is found in pirated software. The attacker will embed malicious software within a popular operating system or a movie for the victim to download. Once the victim downloads and runs the software, the malicious code executes on the victim’s system, and the attacker gains full access to the victim’s machine.

### PiggyBacking

PiggyBacking means using someone else to attack a potential victim. The attacker will use a third-party (usually innocent) who has access to the victim in order to carry out a piggybacking attack.

There are many variations of Piggybacking. If an attacker follows your employee to your office using their access card, this is one form of piggybacking called tailgating.

There have been many cases of piggybacking attacks, especially for classified information. Vendor companies that supply hardware/software to government organizations are usually the target of piggybacking attacks.

Once these vendors are compromised, it is easy to attack the target institution since the vendor already has a level of access to the target.

Piggybacking is also associated with some forms of [active Wiretapping](https://whatis.techtarget.com/definition/wiretapping). The attacker will use a legitimate connection of the victim in order to eavesdrop on the network.

[I recently wrote an article on Wireshark which you might find interesting.](https://medium.com/manishmshiva/wireshark-a-walkthrough-of-the-best-packet-analyzer-in-the-world-9af0358ed9a1)

### Water Holing

Water Holing takes into account the routine actions of the target and using one of those actions to gain unauthorized access. For example, an attacker will find the websites that the target uses on a daily basis and tries to install malware on one of those websites.

The name “Water Holing” is derived from the fact that predators in the wild often wait for their prey near their common watering holes.

An example is the 2019 [Holy Water Campaign,](https://www.techrepublic.com/article/holy-water-watering-hole-attack-targets-visitors-of-certain-websites-with-malware/) which targeted Asian religious and charity groups. The website was compromised after which the visitors were asked to install Adobe Flash on their browsers.

Since Adobe Flash has a number of vulnerabilities, it was easy for the attackers to then execute malicious code on the victim’s machines. Watering hole attacks are uncommon but they pose a considerable threat since they are very difficult to detect.

## Protecting Yourself From Social Engineering

Now that we have seen the different types of approaches used by social engineers, let's look at how we can protect ourselves and our organization from social engineering attacks.

### Install email & spam filters

Though spam filters cannot catch highly targeted attacks, they will prevent most of the spam and malicious emails from reaching your account.

### Keep Antivirus and firewall updated

Similar to spam filters, an updated antivirus software will protect against most of the common [viruses, trojans, and malware](https://medium.com/manishmshiva/penetration-testing-100-terms-you-need-to-know-a723c38cd8c8).

### Ask for verification 

Always ask for verification when someone calls you claiming to represent an organization, for example your bank. Never share confidential details such as credit card numbers or passwords over phone or email.

### Create awareness

The best way to prevent your organization from getting exploited is to create security awareness programs. Educating your employees is a great long-term investment to keep your company secure.

### If it seems too good to be true, it is

Finally, if something sounds too good to be true, it usually is. Never trust strangers promising to get you rich quick. As someone once said, “trying to get rich quick is the quickest way to lose all your money”.

## Conclusion

Social Engineers are masters of manipulation. Unless a company’s employees are trained in social engineering awareness, it is very hard for them to avoid falling into a social engineer’s trap.

Social engineers work with people’s emotions, usually fear and greed. So whenever you are performing an action based on these two emotions, you might want to take a step back and see if you are being manipulated.

There is a famous TED talk where someone started a conversation with a spammer. [Watch the full video here](https://www.youtube.com/watch?v=LiLS7U7YIdc&ab_channel=EisseCatherineWade).

[**_You can get a summary of my articles_**](https://tinyletter.com/manishmshiva) _and videos sent to your email every Monday morning. You can also_ [**_learn more about me_**](https://www.manishmshiva.com/) _here._

