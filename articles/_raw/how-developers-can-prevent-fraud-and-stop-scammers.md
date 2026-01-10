---
title: How Developers Can Prevent Fraud and Stop Scammers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-20T22:32:41.000Z'
originalURL: https://freecodecamp.org/news/how-developers-can-prevent-fraud-and-stop-scammers
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/48332996261_4f1a1657fc_b.jpg
tags:
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: null
seo_desc: "By Dmitry Dragilev\nOnline frauds and scams have shot past projections\
  \ in the last decade, and no one seems to be immune to them—including developers.\
  \ \nThe shift to serverless cloud management has opened doors for hackers to try\
  \ new attack surfaces an..."
---

By Dmitry Dragilev

Online frauds and scams have shot past projections in the last decade, and no one seems to be immune to them—including developers. 

The shift to serverless cloud management has opened doors for hackers to try new attack surfaces and the impact is right in front of us. [90% of web applications are vulnerable to cybercriminals](https://www.freecodecamp.org/news/what-is-devsecops/https://www.freecodecamp.org/news/what-is-devsecops/), and a majority of these vulnerabilities can be traced back to direct dependencies.

Thanks to cloud migrations, DevOps teams can roll out product iterations faster and improve customer management KPIs. But this also means they lose control over custom code infrastructure and servers. Companies that have traded custom security for cloud efficiency are more susceptible to cybercriminals today.

In this article, we'll look into the most common scams faced by developers, how they work, and what developers can do to mitigate the risks.

## What is a Fraud or Scam?

Fraud is the illegal attempt to deceive a person, entity, or organization to gain access to confidential assets. 

Scams are the smaller steps that help criminals commit fraud and they almost always involve money. 

If you have been scammed there's a good chance you've lost money. Frauds, however, may not always lead to financial ruin as the impact can be much larger than that.

DevOps teams are increasingly vulnerable to fraud and scams because these are built on deception and social engineering. Since access management is a major security pitfall of modern IT development, fraudsters look to access developers’ credentials to compromise systems and steal money and information.

## Four Common Scams and How They Work

Hackers today use precise strategies to create the biggest impact. They have gone from “tried and tested” to highly targeted and innovative attacks that end up fooling even the most security-aware victims such as developers.

To better understand how these work here are a few examples:

### 1. DDos Attacks

Distributed denial-of-service (DDoS) attacks are one of the most common types of cyberattacks that plague developers today. With a DDoS attack, criminals try to overwhelm a network or web application by sending a huge amount of access requests, effectively shutting it down. 

Since most businesses today rely on their digital infrastructure to operate, an offline website or application at crucial moments can lead to massive loss—both financial and reputational.

[DDoS attacks](https://www.bigcommerce.com/blog/denial-of-service-attack/) use compromised machines and IoT devices as zombies (or bots) to send millions of pings within a short amount of time. Attackers can target the server architecture by spoofing SYN data packets, stress the software resources by using HTTP flood, or dump huge traffic on the website with DNS amplification.

Since it's difficult to detect botnet requests from authentic requests, victims often have a hard time separating the two. On top of that, the distributed nature of the attack means blocking off one IP address won't solve the issue.

![Image](https://lh5.googleusercontent.com/JWZmINyPOstdWofeQ078TRQ8xDhYUzskB9-3RJpuSpyhhMpw-6JCMgucZ-3e1pC5pVTaThM7A6Kw-IgVToxVWCVEyGrcu-yJjvTYG4vDAZzsVxm9yjgpsVYdiYSA2wP80H6LB3eXzr6DJwFf1puTXeQ)
_Weird TTL responses with odd values which obviously tell you they did not come from the original server, but rather some intermediate device. [Source](https://blog.erratasec.com/2015/04/pin-pointing-chinas-attack-against.html)_

One of the most famous examples of DDoS attacks was the 2015 attack on GitHub by Chinese attackers. It started with injecting browsers used to visit Baidu and Baidu analytics-enabled websites with JavaScript code run by a telecom company called China Unicom. 

The malicious code created a botnet of affected browsers and triggered the browsers to send a massive amount of HTTP requests to specific GitHub pages. The attack lasted for five days and many parts of GitHub were inaccessible. 

### 2. Credit Card Scams

DevOps teams often have a lax attitude towards financial compliance, making them a gateway to credit card scams. These types of scams either look to get ahold of employee credit cards or gather enough data to carry out card-not-present (CNP) frauds.

[Credit card scams can happen in several ways](https://www.aura.com/learn/credit-card-scams) and attackers are still trying new methods to deceive victims. 

It can start with simple shoulder surfing where an attacker monitors you entering the PIN or showing card details to advanced keyloggers and card skimmers placed at shady ATMs. Fake charities and rewards are also popular ways to get hold of credit card details. 

On top of that, criminals can use personally identifiable information (PII) to apply for a new credit card or request updates to your old card and block it. They can go as far as intercepting cards from the mail or assaulting victims to steal credit cards.

Even if they don't get ahold of your card, CNP frauds allow them to make huge transactions online, which might ruin the victim’s credit score and put their finances in a tough spot.

### 3. SIP Trunking Fraud

Modern business communication relies on [VoIP phone systems](https://www.nextiva.com/products/voip-phone-system.html) to reach customers, vendors, and stakeholders and uses omnichannel flexibility to improve productivity. It all sounds great on paper but VoIP used by small businesses often falls victim to SIP trunking fraud.

Session initiation protocol (SIP) trunk is the technology that connects a company's existing phone system or PBX with the cloud, allowing VoIP to work across the globe. It's a crucial piece of technology that is often exploited by hackers. Here's how it usually goes down:

* Cybercriminals use IP scanners to look for vulnerable phone systems to gain access to the SIP trunks
* They either steal passwords or use brute force attacks on weak systems
* Once they have the access, attackers often spoof caller IDs to extract sensitive data such as credit card and login details or eavesdrop on texts and calls on public IP connections.
* Apart from this, attackers might commit toll fraud by rerouting calls to [virtual phone numbers](https://www.nextiva.com/blog/what-is-a-virtual-phone-number.html) in premium domestic and international territories and stealing the revenue earned from those calls.

![Image](https://lh3.googleusercontent.com/qmcSLLBIb_MXtMDC-ajfsAKdfJ8bBkmJYHsQ3a3EoVXBLUy6dZZI7t4MivBQR01BoLZbxtp8WzHL82qHSP8iokj-8i28GGWj4mRpyerRL1ij1x0hZIexF-e0pDU6TpEBEuDORP2CoapU1FLQP0_4PY0)
_Twilio is flagging fraudulent calls by using their 3rd party anti-fraud database. [Source](https://www.twilio.com/blog/2018/03/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions.html)_

If SIP trunking fraud is left unchecked, a business can lose thousands of dollars within a few hours.

### 4. SIM Swapping

SIM swapping can happen to anyone and developers have no additional security against these types of scams. SIM swapping is convincing your network provider to transfer your SIM to their device, effectively taking over your phone number and everything tied to it.

[SIM swapping doesn't happen in a vacuum](https://www.aura.com/learn/how-to-prevent-sim-swapping)—it requires long-term planning and social engineering. Here's how it works:

* A scammer calls your SIM provider and requests to transfer the phone number because they claim the device is destroyed or stolen.
* Now the representative asks for ID proof to authenticate the transfer and it usually requires personal information such as an address, email ID, IMEI, or last four digits of the credit card.
* If the scammer can prove your identity to fool the operator, they can activate a new SIM in their phone.

This is where long-term strategies come into play. Before executing a SIM swap, attackers use phishing emails, malware, and data breaches to collect snippets of personal data and piece them together to convince the SIM provider.

![Image](https://lh6.googleusercontent.com/q6I7_Md5LIl7ladti5IWTOGlMD8nj2cHmBGOpH-Hcbm9LQm_QXTjIlgy5x1WqDZvBYM0n75XXqQiQB2BQccskFFAyGP16cn7-jcDkKx0mGJkAqcMSvI6NNTrHMHuIbqQmVSDIkTphkzgHOobLhi7VOs)
_Example of a SIM Swapping scam text message. [Source](https://www.phonearena.com/news/Cops-bust-gang-that-used-stolen-SIM-cards-to-access-bank-accounts_id107701)_

A few years ago, a disgruntled T-Mobile employee exposed customer data to hackers who would swap out SIM and take over accounts.

Once the attackers have your SIM, they can bypass two-factor authentication (2FA) for all transactions, and get hold of your bank details, SSN, and personal media. SIM swap opens the floodgates to all kinds of crimes that require your phone number in the first place.

## How DevOps Can Prevent Fraud and Scams

Security risks come in abundance but developers are familiar with the concepts. By following a few steps you can detect, address, and mitigate most of these scams.

### How to Prevent DDoS Attacks

DDoS attacks are hard to distinguish without harming real traffic, which makes mitigation a difficult job. But you still try a few methods.

#### 1. Detect signs of a DDos attack

Know the symptoms of DDoS to detect attacks early on. If an online asset is suddenly slow or unresponsive, you might have to look for DDoS signs. These include:

* an unusually high volume of traffic at odd hours of the day
* hordes of requests coming from the same IP address, location, device, or browser, and targeting a specific page or part of the application.

You can react quickly if you have monitored and documented the usual traffic patterns of your company.

#### 2. Deploy anti-DDoS measures.

Start by using hardware and applications that are built to prevent DDoS attempts and restore assets, [decentralizing data centers and servers](https://www.freecodecamp.org/news/how-to-manage-data-storage/), using a web application firewall (WAF), and migrating to the cloud to increase bandwidth. 

AWS Shield Advanced is an easy-to-configure managed DDoS protection service that can detect and mitigate large-scale and complicated attacks. 

Apart from using anti-DDoS tools, you should also close [security loopholes in your network](https://www.algosec.com/resources/security-policy/) and practice cyber hygiene daily.

![Image](https://lh3.googleusercontent.com/KEsXtxDCDaRlXcQkDNq8AKHzcnIqvZfiHkKS2Sq0iXgmZ-myJ4aob6FLYf_lDWj3X_NhTsZKVC28wiXsF4Y26VSdpMJ4pc4gjPDP4VC9Xt7fdSnHkDEi5EQuSz7UbH-PbmER46qo-0AepFMsOnqK-rU)
_Example of AWS configuration for DDoS mitigation. [Source](https://www.youtube.com/watch?v=hyGuV2e8SDw)_

#### 3. Have a DDoS response plan in place to prevent further damage.

This should include documented steps, a well-prepared team, and clear communication channels for internal and external stakeholders. 

Modern multi-factor DDoS attacks combine multiple pathways so the more complex and thorough your plans are the better you can protect the company.

### How to Prevent SIP Trunking Scams

SIP trunking is a common method of phone fraud, but you have some weapons in your armory to prevent these.

#### 1. Set up a maximum default rate for outbound calls to prevent toll fraud.

When you set a limit for the number of calls, you'll be notified if your business crosses that threshold—allowing you to monitor calls made by hackers.

On top of that, use a solid [VoIP service](https://www.nextiva.com/solutions/small-business-phone-service.html) to identify outbound and inbound calls and log as much information as possible. Hackers will call to and from random numbers so it becomes easier for you to set up call barring for suspicious numbers.

![Image](https://lh5.googleusercontent.com/49d4N6OJbwXWHNYsTiVUDk4WynrVv0O7tN3kD6aGB5B_-67KAaDnj2ODAQYzNQcXOX881MO0mbNPDh2vbDh819n4_KTI57AfkkiXTnrUsokQYH19ued4tTSNtHPVSxX4SU9-Kv2VO7ctjd2JWxXQkFA)
_VOIP vendor settings to disallow inbound calls which have characterists of robocalls. [Source](https://telnyx.com/resources/add-rate-limits-outbound-profiles)_

#### 2. Activate IP-based authentication to manage network access.

With this enabled, users would need to be part of your network to make and receive calls. Even though IP addresses are not completely hidden, you'll be notified of any effort to breach your network. By mandating a static IP address, you can easily set up IP-based authentication and monitor calls.

#### 3. Reinforce PBX security.

You can protect your phone system by using new and complex passwords, regularly changing and storing them safely, properly installing SBC configuration, and using TLS and SRTP for superior encryptions. On top of that, you should also restrict access to hardware to prevent data breaches.

### How to Prevent Credit Card Scams

Credit card scams can open Pandora's box and as a developer, you should be wary of the consequences. Here are some steps you can take to prevent credit card scams:

#### 1. Employees using company credit cards are the easiest victims of scams.

You can help them mitigate the risks with training. A series of training modules and frequent seminars should include identifying ways credit card details can be stolen (as discussed above) and quickly acting in case of theft. 

These should also encourage employees to access only HTTPS websites, use VPNs every time they use personal devices or public WiFi, and help them identify malware and phishing attempts. 

On top of that, you should use an [identity theft protection service](https://www.aura.com/learn/how-much-does-identity-theft-protection-cost) to limit the consequences of credit card scams.

#### 2. As a developer, you're bound by compliance standards (and ethics) to secure the credit card details of employees and customers.

While writing code for software meant to process and store credit cards, you should distribute duties to protect yourself and the business. Not many developers follow the PCI DSS guidelines regarding this and trap themselves in compliance red tape.

[PCI DSS](https://www.pcisecuritystandards.org/resources-overview/) sections 6,7 and 8 clearly lays out third-party code review rules along with role and access management. Following compliance standards and leaving access keys to admin are best practices to mitigate potential credit card scams.

### How to Prevent SIM Swapping

SIM swapping starts long before convincing SIM providers to activate a new SIM which is why you have to take several measures:

#### 1. Phishing and other social engineering methods are used to mimic you, so be wary of these crimes.

Be on the lookout for [phishing emails](https://www.freecodecamp.org/news/how-to-recognize-phishing-email/) and SMSs, malware injections, compromised websites, and fake calls that coax you into sharing personal details such as birthdays, physical and email addresses, and SSNs. Scammers use this information while calling your operator. 

Another way you can prevent this is by limiting how much personal data you share online in the first place. Here’s an example of a nicely crafted phishing email impersonating PayPal. All you have to do is check the sender’s address to find the scam

![Image](https://lh6.googleusercontent.com/loP48E4iNW0LGxX73HUtt-sA_Wzx2Fxq2WzYSY0BQW_m1mhZF6Li2SGfvgsbeIzafSiHzoldzX7CXhq_Vuup9hq4inQdgOJ1VGYfZj5oV8RuKQ1tkaFt1pQEHvvMONjt92FynXRpm4QyvtqQbIRwQck)
_Example of a Paypal Scam. [Source](https://www.pickr.com.au/how-to/2021/how-to-spot-a-paypal-phishing-email/)_

#### 2. Don't make your phone number the central part of your security.

Since SMS is not a secure mode of 2FA in case of device theft and SIM swapping, use biometrics such as fingerprint or face IDs and authentication apps such as Authy to [protect 2FAs](https://www.freecodecamp.org/news/user-authentication-methods-explained/). 

Speaking of third-party apps, you should also use a password manager to create and maintain unique, complex, and 14-character-long alphanumeric passwords to make sure attackers cannot use your personal information to guesstimate logins.

#### 3. Activate alerts so that banks can monitor when your SIM is reactivated on an unknown device.

Work with businesses that use callbacks to verify identities for transactions and don't forget to activate the PIN lock by the carrier to prevent unauthorized porting.

## Final Word

Cybercrimes and social engineering tactics have grown by leaps and bounds and developers working on critical projects must make sure they don't become a security liability. 

By following the above steps you can protect your employer, colleagues, and yourself from nasty surprises.   
  

