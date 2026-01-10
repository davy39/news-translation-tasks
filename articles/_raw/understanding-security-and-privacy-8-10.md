---
title: Security and Privacy – What You Should Know to Protect Your Data
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-03-01T18:36:46.000Z'
originalURL: https://freecodecamp.org/news/understanding-security-and-privacy-8-10
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-photomix-company-96612.jpg
tags:
- name: information security
  slug: information-security
- name: privacy
  slug: privacy
- name: Security
  slug: security
seo_title: null
seo_desc: 'I''ve talked a lot about security and privacy in my "A Beginners Guide
  to Digital Security" and "What Is Digital Privacy" articles. So why are we flogging
  this certifiably dead horse now?

  Because it''s not dead. Security and privacy are as or more impo...'
---

I've talked a lot about security and privacy in my "[A Beginners Guide to Digital Security](https://www.freecodecamp.org/news/understanding-digital-security/)" and "[What Is Digital Privacy](https://www.freecodecamp.org/news/beginners-guide-to-digital-privacy/)" articles. So why are we flogging this certifiably dead horse now?

Because it's not dead. Security and privacy are as or more important than anything else in IT. Most of us don't think about them enough, but it's something you can't really overdo. 

As an outstanding IT professional I once worked with would have said: "Paranoid is only the beginning." And besides, there are still some urgent and fascinating topics we haven't addressed.

So we'll spend some time exploring how the core security tools (like authentication controls and encryption) can be applied to solve a much wider range of security and privacy problems. And we'll also go face to face with a couple of significant threats that exist thanks to the very devices we've come to love.

This chapter was taken from the book, [Keeping Up: Backgrounders to All the Big Technology Trends You Can't Afford to Ignore](https://amzn.to/3FXXAfb). If you'd prefer to watch this chapter as a video, feel free to follow along here:

%[https://www.youtube.com/watch?v=FOlJEp4UEiA&list=PLSiZCpRYoTZ6UWl4xialvwLOKyHYYJUiC&index=8]

# Blockchains and Security

The new-technology-hype machine just loved blockchains when they first came to public attention. There were frequent gushing articles in the media about how this was _it_: blockchains were poised to change the world, ushering in a golden age of endless joy and fluffy fairy unicorns. Rejoice! Salvation is come.

But despite all that, blockchain technologies are, in fact, a big deal. Before we go there, though, just what is this stuff all about?

A blockchain is a distributed string of digital records used to record and validate transactions. The goal is to maintain a reliable and incorruptible public "ledger" of transactions to secure and improve the way financial and commodity operations are recorded.

The _blocks_ in _blockchains_ are actually data packets containing some identifying meta information (including a timestamp) and a cryptographic hash. 

The hash – which is produced by software running on the computer that generates the block – is derived from the unique contents of the previous block in the chain which, in turn, was based on the block that preceded it.

Because the contents of one block are dependent on the state of others, no single block can be modified without leaving behind some obvious and easily traceable evidence. 

This explains why it's called a _chain_, because if any one link (block) is altered, the entire chain will break. In effect, a chain will never be trusted unless it maintains the clear consensus of the creators of all its blocks.

Generating the hashes for blockchains is compute-intensive and can incur significant costs in compute power and electricity. 

This is by design, since it all but forces blockchains into the hands of distributed communities, rather than individuals or small groups. This decentralization makes chains less vulnerable to attack and adds robust reliability to the data that's being managed.

## Blockchains and Cryptocurrency

Like most people, I first heard about blockchains in the context of cyptocurrencies like Bitcoin and Ethereum. Cryptocurrencies are digital assets that can be used as alternatives to fiat money (that is, the kind of virtual and mutually accepted representations of value found in exchange instruments like national currencies).

Using the funds in a cryptocurrency account, I could pay for goods or services while, in many cases, retaining anonymity. Of course, this very anonymity carries significant risks.

Cryptocurrencies have, for instance, been used to support criminal activities. The people behind ransomware attacks will often demand cryptocurrency payments in exchange for the decryption keys that you _hope_ will restore access to your lost data. 

And the contents of large cryptocurrency accounts have been effectively lost when controlling servers crashed (or were forced down) or, in at least one case, when the administrator of a currency worth millions of dollars died without sharing his authentication information.

It's worth noting that the relative value of funds in the account itself – when measured against the ability to exchange them for fiat money – has historically been volatile, unpredictably suffering from violent market fluctuations.

## Blockchains and Accounting

Blockchains can solve many of the same old problems addressed by traditional accounting practices. Specifically, integrating blockchain verification into a business's financial processes can provide secure transactions and on-demand access to immutable and transparent records. 

The ongoing, real-time existence of such records could possibly remove the need for periodic audits and monthly reconciling.

Many of those same features could profoundly change the very nature and value of contracts – a change that could spill over beyond accounting, in to the practice of law.

## Blockchains and Insurance

The potential security and privacy features of properly designed blockchains can also create efficiencies and value in the insurance industry. 

For one example, having a single blockchain where all the insurers within a particular market can reliably share their customer account information can help reduce claims fraud. Suspicious behavior and multiple claims for a single event will be more readily visible within a transparent and highly accessible system that includes data from all participating parties.

Being able to reduce administrative duplication can also greatly streamline the processing of legitimate claims. 

You'll appreciate this when you consider how a victim's insurer will often process their customer's claim using similar steps to those used by the insurer you're claiming from. But if both companies are able to openly share their data, the process can be unified and, even better, automated.

Perhaps most significantly, the delivery of healthcare can be enhanced and made more efficient if critical personal records can be safely and instantly accessed. And – you guessed it – blockchains can be helpful here, too.

What kinds of automation are we talking about? Well, going back to accident claims, a "smart contract" is software that regularly checks for changes to the status of associated objects. The simple mouse click approval of an insurance appraiser, for instance, could set into motion all the events necessary to pay a claim, notify all related parties, and update existing records.

Maybe – just maybe – insurance isn't as boring as people think.

# What is Multi-Factor Authentication?

Passwords are terrible things. Sure, we can't just leave our devices and online accounts open to anyone. But who decided that asking people to memorize long strings of meaningless text (like _sIIkdm^&sv234LKi_) was the solution? 

Sure, you could choose easy-to-remember passwords like _mysecret_ or this clever variation: _mysecret22_. But anything that's that easy to remember is equally easy to guess. And double that if you're using the same password for multiple accounts. In other words, that kind of protection is just not worth the effort.

There are, by the way, two ways to improve your passwords:

* Use a password vault to generate and safely store insanely complex passwords that you won't need to remember: you can just copy and paste them into any login pages you visit.
* Use long (15-20 character) passwords that incorporate memorable, but unconnected, words. Something like: _house-seventy-warfare-calf_.

Mathematically speaking, it's highly unlikely that anyone will have the compute power and time needed to crack that one. And it's not so hard to memorize.

But when it comes to particularly sensitive sites – like the ones where you do your banking – even good passwords aren't good enough. For that reason, more and more organizations are incorporating multi-factor authentication (MFA) into their security profiles.

A website or application configured with MFA requires you to present more than one kind of evidence that you are who you claim to be. 

One could be based on something you know, and another could be evidence based on something you have. "Something you know" could be a password, while "something you have" could be a standalone MFA device or an app running on your smartphone. 

It'll often work by having the application send a short-lived code via instant message to a preset phone number. You'll be expected to enter the code onto the authentication login page.

# What Are Federated Identities?

Once you've got the basics of authentication out of the way, through strong passwords and/or MFA, there's the question of authorization. In other words, what resources your logged in account will be able to access. 

Individual systems will control users through some kind of access controls. Microsoft Windows, for example, uses Active Directory, Linux has object permissions, and cloud providers like Amazon Web Services can apply roles and policies.

But if you want your users to be able to move _between_ services without having to log in to each service individually, or if you would just prefer not to have to manage authentication at all, you can implement a federated identity.

You've probably already experience federation without even knowing it. Logging into a third party web service using your Google account is one form of federation. 

The service integrates its authentication system with a federation provider using an identity technology like Security Assertion Markup Language (SAML) or OAuth. 

When you accept the terms and log in, the provider will share just enough of your identity information with the third party service to enable an account.

# Digital Surveillance

Because it can both protect you from harm and also invade your privacy, surveillance is a two-edged sword. But _digital_ surveillance is a two-edged sword that's a whole lot sharper. Let me explain why that is.

Closed circuit video cameras have been in use within security systems since at least the 1930's, but they really did only one thing: record images that were usually stored locally and then, after a few days or so, overwritten with new recordings. 

That was helpful but, to be useful, you would need to physically get to the tape and then laboriously search through, find, and view any images of interest.

Digital surveillance cameras are certainly cheaper than their analog equivalents, much easier to physically hide, and easy to access through networks. 

But there's also a lot more you can do with digital video feeds. You can, for instance, configure email alerts whenever the camera detects motion. Or you can redirect a video stream to cloud services (like Amazon's Kinesis) where it can be integrated with your data analytics and machine learning operations or interpreted in near real-time by an object and face recognition service (like Amazon's Rekognition).

All of those tools can be used in the service of both positive and harmful goals. The fact is that there are now countless millions of such cameras deployed around the world that are, in many cases, connected to large-scale surveillance operations. At the very least you should be aware of the potential as well as the risk that such technologies present.

# What is a Backdoor?

A _backdoor_ is a hardware or software-based vulnerability that was intentionally built into a device or the operating system that runs it.

In some cases, the backdoor exists with the full knowledge of the customer, as it was intended to enable remote support or the automated installation of patches and updates. But that's not always the case.

Governments, government-associated companies, and criminal organizations have been caught shipping sensitive compute and networking devices with dangerous backdoors. Such vulnerabilities have been used to bypass encryption protection to monitor communications, steal research data, and harvest authentication information.

Backdoors can take the form of active malware that collects local data and then sends it to remote attack servers, or passively permits remote logins through insecure network environments.

Protecting yourself from backdoors requires defence on multiple levels, including:

* Careful vetting of potential hardware vendors (taking into account their home countries and associations)
* Regular monitoring of reliable technology information sources for news of new vulnerability discoveries
* Careful monitoring of your devices' network activities
* Regular patching of your networking and compute systems
* Blind, stupid luck in large doses

Thanks for reading! Hopefully you now have a better idea of why security and privacy are so important and how to protect your own.

_YouTube videos of all ten chapters from this book [are available here](https://www.youtube.com/playlist?list=PLSiZCpRYoTZ6UWl4xialvwLOKyHYYJUiC). Lots more tech goodness - in the form of books, courses, and articles - [can be had here](https://bootstrap-it.com). And consider taking my [AWS, security, and container technology courses here](https://www.udemy.com/user/david-clinton-12/)._

