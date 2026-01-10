---
title: Privacy stripped away, one email at a time
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-01T12:25:52.000Z'
originalURL: https://freecodecamp.org/news/privacy-stripped-away-one-email-at-a-time-3556dab102ff
coverImage: https://cdn-media-1.freecodecamp.org/images/1*N05XSawg2UEm4CvdxD86CA.png
tags:
- name: politics
  slug: politics
- name: privacy
  slug: privacy
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Chris Kubecka

  As the European Union General Data Protection Regulations (GDPR) looms, a privacy
  stripping email setting continues in widespread use around the world. It threatens
  sensitive communications that containing personally-identifiable inf...'
---

By Chris Kubecka

As the European Union General Data Protection Regulations (GDPR) looms, a privacy stripping email setting continues in widespread use around the world. It threatens sensitive communications that containing personally-identifiable information, intellectual property, financial information, and your most intimate photos.

You might log in to an email account to use it, but that doesn’t mean your messages are sent securely. Contrary to the assumption of privacy a username and password may provide, by default, emails are sent unencrypted unless explicitly or opportunistically secured. Email technology standards were written in a more innocent time before severe concerns about confidentiality.

Email privacy became a significant concern to the EU public after the Prism disclosures. Suddenly, the non-technical IT world began to understand how damaging lack of email encryption could be. After the Snowden revelations, providers like Gmail, Hotmail, private companies and many others decided to try and secure email communications.

Configuring explicit security is not easy. It requires overhead and certificate management.

Opportunistic security can help fill the gap. Encrypt email wherever possible, opportunistically, with a setting called Start-TLS. This opportunistically scrambles email contents to prevent eavesdropping. The setting, called Start-TLS, can provide a basic level or retain privacy protection. It’s not a guarantee, but helpful, similar to the HTTPS Encrypt Everywhere movement.

On the flip side, is a configuration which does the opposite, Strip-Start TLS. This email server setting removes any opportunistic encryption on emails, stripping them, baring the contents of the conversation.

Why is this important?

Back in 2014, the [EFF](https://threatpost.com/eff-calls-out-isps-modifying-starttls-encryption-commands/109325/) reviewed an engineer’s blog post from Golden Frog VPN describing the problem. The engineer could no longer send and receive encrypted emails to a customer because an ISP provider applied the Strip Start-TLS setting. Leaving communications bare to eavesdropping. Anyone, hacking tool, criminal, spy agency could potentially read the emails.

From [Wikipedia](https://en.wikipedia.org/wiki/Opportunistic_TLS) “ Opportunistic TLS is an [opportunistic encryption](https://en.wikipedia.org/wiki/Opportunistic_encryption) mechanism. Because the initial handshake takes place in plain text, an attacker in control of the network can modify the server messages via a [man-in-the-middle attack](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) to make it appear that TLS is unavailable (called a **STRIPTLS attack**). Most SMTP clients will then send the email and possibly passwords in plain text, often with no notification to the user. In particular, many SMTP connections occur between mail servers, where user notification is not practical.”

If anyone doubts how valuable email communications are, or if such all you can eat buffet programs like Prism exist. While crafting an OSINT hacking crash course for Security BSides LV 2017, four NSA Prism related subdomains popped up using a web-based reconnaissance tool.

![Image](https://cdn-media-1.freecodecamp.org/images/gb0f-qtIJNK7YPLCefjPoMwg0afXeBWVZQHn)
_Figure 1 Highlighted list of NSA subdomains listing Prism July 2017_

Have things changed much in the last few years? Sadly, a resounding no.

Even with existing data protection laws across Europe, the USA, other concerned countries, the Strip Start TLS configuration is in widespread use.

Use of the setting without notification could be contrary to the EU-US data privacy shield. Multiple USA based EU partners under new EU-US Privacy Shield agreements use strip opportunistic email encryption.

The disturbing email anti-privacy setting can be easily found. Using Censys.io tags, and two Python-based tools: ZMAP and StripTLS.

Censys.io is a web-based security researcher project, operated by the University of Michigan and based on ZMAP. A simple search yielded 11,641 in a few seconds, displaying many ISPs and email providers using the Strip Start-TLS tag. The tag is applied to a device based on metadata, technology in use and communications behavior.

![Image](https://cdn-media-1.freecodecamp.org/images/UHVE5HubcmhtIxZaTise15vvA1kGbfKy1c4V)
_Figure 2 Censys.io Strip Start-TLS global scan 10 November 2017_

The USA returns the highest percentage of stripping systems on the internet — over six times the amount of China.

There is a confusing patchwork of data privacy laws at the federal and state level in the USA. However, the federal Health Insurance Portability and Accountability Act (HIPAA) broadly covers medial data privacy via a privacy and security rule.

Second on the list is the UK, with other European countries close by its side.

![Image](https://cdn-media-1.freecodecamp.org/images/9vScZaI4wiGZYl3ZplzmZ-X0MnuFlYyQe-jd)
_Figure 3 Censys.io Strip Start-TLS top country report 10 November 2017_

Focusing on the European content, over three-thousand email stripping servers are found, resulting in too many data points to fit on the map.

Removing Russia from the list, and looking at EU GDPR locations only, the top five are: the UK, France, Italy, Germany and the Netherlands.

Some of these areas have existing data protection laws, which cover email and legislate against the widespread collection of data and communications.

![Image](https://cdn-media-1.freecodecamp.org/images/lvWwy5JLqv1MBYCYL3gPGqvlEwDRAkjQ83F3)
_Figure 4 Censys.io Strip Start-TLS European scan 10 November 2017_

![Image](https://cdn-media-1.freecodecamp.org/images/raoHPyeH0A5sSVNeTmaP0K83YXzOdTqkCqQq)
_Figure 5 Censys.io Strip Start-TLS top European country report 10 November 2017_

The UK implemented their version of data privacy regulations, complete with major fining power. Violators risk possible financial penalties.

Hidden behind the UK ISPs and data centre providers are banks, financial institutions like Rabobank and Santander, travel agency. Government councils, hosting, and other internet service providers like 1stdomains.co.uk and 1stdnsltd.co.uk.

![Image](https://cdn-media-1.freecodecamp.org/images/gbMDW8Y6pfH9FdfU4nB-ds71Br0i0Xvd6lON)
_Figure 6 Censys.io Strip Start-TLS top UK network providers report 10 November 2017_

BT on the other hand, appears to own and host several stripping systems, like the Thailand government.

Most of the ISPs in the list own and host email security stripping systems. Many ISPs in France, Germany and Italy own email stripping systems.

![Image](https://cdn-media-1.freecodecamp.org/images/X1SHyRpNnw9RtvemAZYRSvTVgXhtQrJpM5BV)
_Figure 7 Censys.io Strip Start TLS UK BT owned systems 15 November 2017_

![Image](https://cdn-media-1.freecodecamp.org/images/lAVMLL7neT4sELdX6yJhIGdZ5Vb0S4WVgmzC)
_Figure 8 Censys.io Strip Start-TLS Thailand government telecommunications systems 15 November 2017_

Currently, I use the Netherlands as a base of operations. Zooming on the Dutch findings, 174 systems, some operated by ISPs, web hosting providers and private organizations around the country.

![Image](https://cdn-media-1.freecodecamp.org/images/uFQrRsJeFIFUU-09gGU74BfBoYgCewMGLQRj)
_Figure 9 Censys.io Strip Start-TLS top NL network providers report 10 November 2017_

Similar to Thailand and other top EU countries on the tag list, most of the ISPs appear to own and host autonomous systems which strip opportunistic email encryption. KPN has several assets combined with a peering policy which stipulates data peers with KPN must also peer traffic to the USA wherever possible.

![Image](https://cdn-media-1.freecodecamp.org/images/6QsfpctExK3HCHTipMQWdTq003eglkfzh5SF)
_Figure 10 Censys.io Strip Start TLS NL KPN Static owned systems 15 November 2017_

One of the pillars of the EU GDPR is consent and awareness of what is occurring with data. Encryption appears to be going backwards, not forwards. The surprising amount of these privacy stripping email systems on European networks, ISPs, web hosting, private organizations and internet network transits is disturbing to the privacy-conscious.

Most people are unaware email security can be downgraded, or previously secured emails exposed. Until EU data regulators gain awareness and clamp down on the illegitimate usage of Strip Start-TLS. The EU GDPR is impossible to implement if downgrading privacy and security across the EU is actively defeated broadly across the European internet.

Here are some references and tools I used in this article:

* [Censys.io](https://censys.io)
* [StripTLS](https://github.com/tintinweb/striptls) python tool by tintinweb
* [ZMAP.io](https://zmap.io)

