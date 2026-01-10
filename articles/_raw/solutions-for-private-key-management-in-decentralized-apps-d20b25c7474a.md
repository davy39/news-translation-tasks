---
title: How to let DApp users recover a lost private key
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-07T07:15:47.000Z'
originalURL: https://freecodecamp.org/news/solutions-for-private-key-management-in-decentralized-apps-d20b25c7474a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3GggWGvVHs4_tZ-8FyCPnA.png
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Pierre-Marie Riviere

  On Ethereum, private keys are used to access accounts, sign messages, etc. Once
  you lose access to your private key, you lose access to all funds stored with that
  account.

  How is that different from losing a credit card pin co...'
---

By Pierre-Marie Riviere

On Ethereum, private keys are used to access accounts, sign messages, etc. Once you lose access to your private key, you lose access to all funds stored with that account.

How is that different from losing a credit card pin code? You can’t ask the bank to give you a new code, because the bank doesn’t exist on Ethereum. Your funds are still credited to your address on the blockchain, but there is no way for you to withdraw them.

Accounts and [DApp-] services on the Ethereum blockchain aim to be decentralized, and no one is safekeeping access codes on your behalf.

A service storing your private key in its database would be able to access your funds at any moment — just like a bank — and this goes precisely against what the Ethereum community is trying to achieve.

**So how do we reconcile Ethereum’s call for decentralization and a user’s need for support services?**

For decentralized services providers, being financial custodians also has strong legal implications. A look into our own case: The DApact is building a Credit-as-a-Service platform atop existing lending agents in low-income countries. We define ourselves as a software company — a plug-and-play tech platform for legally registered local lenders.

Having access to user’s funds would make us a financial service provider rather than a software company, and this would imply scrutiny by local financial regulators. This would eventually translate into being required to have some kind of banking license and capital deposit in each country where The DApact is available.

In pure DApps services, there is absolutely no way to gain back access to your funds once you lose your private key. Users need to take care of backing up their recovery passphrase to a safe place themselves. The actual most effective is to literally write down the passphrase three times and keep the hard copies in different places.

![Image](https://cdn-media-1.freecodecamp.org/images/8o69I8L-ItDZY4A5KNT4Bw3YBlsLRLma83A2)
_No joke_

Certain users tend to lose this passphrase or not back it up at all in the first place. This is a significant problem for all DApps developers, and specifically for The DApact as we’re dealing with populations who often don’t have as much knowledge about tech. Therefore, recoverability solutions must be available for our users.

Users must be offered private key recoverability solutions adapted to their understanding of decentralized systems.

Such recoverability solutions should respect the following three criteria:

* **External:** Decentralized service providers cannot have access to the private key.
* **Customizable:** Users should be able to understand and configure recovery options even in the event of private keys loss.
* **Secure:** There should be no easy way to hijack the account of another person via recovery options. Only the person actually owning the account should be able to recover it.

### Existing solutions

Here is an overview of solutions being implemented, beefed-up or explored by UX designers in the Ethereum community, starting with the most rolled-out.

#### Multiple owners

MultiSig wallets allow for setting a number of owners _n_. If fewer than _n_ owners are required, the remaining owners could replace an owner in case they lose access. This solution, however, requires at least 3 owners or owner devices (2 confirmations required for transactions) and a strong degree of trust between owners.

#### Mnemonic

A mnemonic (AKA seed phrase or passphrase) is a series of words that can cryptographically derive a private key. Users need to back up their recovery mnemonic themselves and make sure to keep it safe so they could regenerate their private key if lost.

This recovery option is the standard for Ethereum addresses and wallets right now. Mnemonics have become a well understood mechanism among advanced DApps users, however a less knowledgeable user should have different options. Mnemonics are as secure as the place they are kept in. Written on a piece of paper, they are exposed to fire and floods, theft and crumbling.

#### Biometric data

A go-to solution for the industry would be biometric data like fingerprint, iris scan or face ID. Biometric data cannot be “lost” like passwords on a piece of paper. If Apple and Samsung are investing so much into biometric, it has to be a great solution right?

The problem with this option is that once biometric data of a person is exposed to the public, there is no way to secure an account with it anymore since you cannot really change you fingerprint like you can change a password or switch an account. This eventuality is becoming more and more plausible as Face Recognition is going mainstream and there is even an [OpenCV-based repo available on Github](https://github.com/ageitgey/face_recognition).

Another downside of biometrics is, different fingerprint sensors can get quite fuzzy and not match exactly — e.g. if a user cuts themselves then there might be problems.

#### Social recovery

Users could determine a group of friends that are enabled to recover access to their account on their behalf (i.e. each of them holds a piece of the signature that, combined together, would grant access to the account). Only when all friends agree, the account owner is replaced.

The biggest problem with this solution is that the group of friends could work together and steal access to the account from the owner even if the owner did not ask them to. That is why ideally, the members of the group should not know who else is part of the group.

Some sort of social recovery solution has been successfully implemented by WeChat to allow for password recovery: when a user loses their password, WeChat asks them to select people in their contact list within a big list of names. Knowing that WeChat contains sensible banking information, this is definitely a good lead for DApps.

#### Standard KYC procedures

Similar to how modern banks perform KYC procedures on new customers, users could identify themselves to KYC providers in order to regain access to their funds. Users would, however, need to perform the procedure already once to set it up so the providers know about the identity behind an address.

This solution has been used for token swap operations (e.g. Nimiq). KYC verification is usually handled by third party providers like IDnow, which is costly and somewhat contra blockchain principles.

#### Paralysis proof

This new concept is also known as _time lock recovery_ and _last resort recovery_. In case access to an account is lost, it can be marked as such. Also, the person marking it as lost may put in a deposit. Now a time period starts after which the account is replaced. During that time period the actual account owner could prove that the account is actually not lost by making a transaction. If so, the attacker loses the deposit which is transferred to the account.

As more designers are entering the blockchain space, there is hope that a great mind will come up with the killer UX for cryptographic keys management. Or who knows, maybe it will be a Middle-Age historian bringing up some old knight trick to secure gold…

![Image](https://cdn-media-1.freecodecamp.org/images/SbW9ifyUTjchPGPL1Cc8tnK-wBbTtfby88pA)

For the time being, a number of solutions (or combination of them) show good potential as per our 3 criteria (externality, customizability, security). Once the community agrees on acceptable recoverability solutions, a common design language and standardized Best Practices will need to be adopted consistently across the ecosystem so that DApps users get accustomed to recoverability patterns.

[_The DApact_](https://www.dapact.org) _is a blockchain framework for microfinance operations._

_You can follow us [on Twitter](https://twitter.com/TheDapact) or join [the Telegram](https://t.me/thedapact)_

