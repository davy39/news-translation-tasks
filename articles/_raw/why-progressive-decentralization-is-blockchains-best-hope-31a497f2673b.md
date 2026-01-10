---
title: Why Progressive Decentralization is blockchain’s best hope
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-06T19:36:48.000Z'
originalURL: https://freecodecamp.org/news/why-progressive-decentralization-is-blockchains-best-hope-31a497f2673b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qgm9rHxUeF-oy6NxHnXv_A.png
tags:
- name: Apps
  slug: apps-tag
- name: Blockchain
  slug: blockchain
- name: decentralization
  slug: decentralization
- name: Ethereum
  slug: ethereum
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Arthur Camara

  Immutability is blockchain’s greatest strength and biggest barrier. Progressive
  decentralization could be the answer.


  When we released CryptoKitties a year ago, we opted not to fund it up front with
  an ICO but instead build it on a ...'
---

By Arthur Camara

#### Immutability is blockchain’s greatest strength and biggest barrier. Progressive decentralization could be the answer.

![Image](https://cdn-media-1.freecodecamp.org/images/4RiJaG98m8kPcAYjnVLTCKifqTzhXEys5TD-)

When we released [CryptoKitties](https://www.cryptokitties.co) a year ago, we opted not to fund it up front with an ICO but instead build it on a sustainable revenue model. That model is this: we collect a fee of 3.75% from every transaction in the game. Given that we’d be unable to change the fee once we launched — CryptoKitties is built on the Ethereum blockchain — people often ask how we arrived at that number.

It sounds like a smart, well-reasoned choice. I could spin a compelling story about how we ran simulations with advanced prediction models to find the fee that would yield optimal returns.

But that’s not true.

The truth is we made an educated guess. We picked a number that felt fair and we committed to it.

### Immutability is awesome and scary

We easily could have chosen wrong, and since you can’t change something once you add it to the blockchain, that would have been _cat-astrophic_. Fortunately for CryptoKitties, our community is so passionate and the Kitties are so adorable that 3.75% worked just fine.

Immutability, the inability to be edited, is at once the blockchain’s greatest strength and its largest barrier to meaningful adoption. The pressures of immortal code paralyze developers: you can tinker in a test environment forever, but there will always be real-world variables you can’t anticipate. Covering your eyes and hitting launch is no way to make breakthroughs. It’s more likely to produce breakdowns.

Our fee was just one decision among many: how long should breeding a Kitty take? At what rate should their breeding cooldowns slow? How much should a Gen 0 cat cost? On blockchain, even a seemingly minor choice can pose serious, even critical, consequences.

Decentralization offers everyday people immense benefits: the fairness of permanent and universal rules and the transparency of code and behavior which, combined, create security. However, because it’s often implemented with all-or-nothing immutability, blockchain makes agile development impossible and slows teams to a crawl.

Agility requires iteration. Iterating quickly is key to building the best products, and the best products spark mass adoption.

### Enter Progressive Decentralization

We encountered these barriers ourselves building CryptoKitties, which forced us to negotiate including decentralized features while building something that, ya know, works. Since then, we’ve started exploring progressive decentralization in development, an idea we briefly introduced [a while ago](https://medium.com/dapperlabs/how-we-launched-cryptokitties-latest-feature-6318ecceba9f).

Let’s take a deeper dive now.

Simply put, progressive decentralization advocates easing into decentralization in stages rather than diving in headfirst. What that looks like is building mechanisms into smart contracts that confer special powers to the creators up front, then incrementally lock those powers away in a transparent and systematic way.

The critical condition is that the locking mechanisms must be public and immutable from the start. The creator can’t decide to tweak the terms later and indefinitely extend their power. That balance is vital: done correctly, progressive decentralization allows creators the flexibility to repair their code without compromising the decentralized features of the contract.

### Progressive decentralization can take many forms

There’s no one right way to implement progressive decentralization. There are dozens of variables to consider, and the best approach will vary from project to project.

Here are a couple ways developers could approach progressive decentralization:

1. Author multiple contracts with appropriate separation of concerns and the ability to replace some of those contracts. Some decentralized apps (“dapps”) like [Decentraland](https://decentraland.org/), which features upgradable contracts, are already using this.
2. Configurable variables and permissions to change those values independently. [Etheremon](https://www.etheremon.com/), for instance, [grants special permissions](https://github.com/Etheremon/smartcontract/blob/master/EtheremonERC721.sol#L125) to groups of users who become moderators.
3. Incorporate a predefined set of ascending levels in the contract, each allowing the creators certain capabilities. The levels can only be increased, never decreased, so backtracking isn’t an option. On level 1, for example, the contract owners can play around with all gameplay variables. At level 2, their capability to modify core variables ends. At the final level, the contract revokes all their special privileges.

To die-hard decentralists, some of this probably sounds too centralized. But this is just the starting point. There are further measures to balance decentralization with iteration. The solution combines transparency of the purpose and the conditions and constraints in the contracts. These constraints could include:

1. **Selection:** Not everything can be modified, only the specific items that we need to iterate.
2. **Range:** For many of the questions around game economies, we may have a general idea but not know the precise answer. Limiting configuration to a certain range guarantees users that the iteration will land within a reasonable scope.
3. **Direction:** Similar to the “levels” concept above, allow certain variables to move only in one direction, decreasing or increasing but never backtracking.

### Holding creators accountable

All this sounds great in theory. But how do we ensure creators stay true to their roadmap and reach the fully decentralized version of their contracts? How can users opt-in early with the guarantee that the system is an application of progressive decentralization? How can we know we won’t end up with just another flawed, centralized system?

Progressive decentralization includes tenets to keep creators accountable:

#### **_Time- or block-based maturity_**

Lock certain configuration values, revoke the owner’s capabilities or move to the next level of maturity past a certain time or block number. Once that point is reached, the contract automatically changes.

Imagine, for example, that CryptoKitties had a runway of 360,000 blocks (around 60 days’ time) from the moment it launched to adjust the Kitties’ breeding _cooldown_ variables. We could tweak the cooldown mechanics until that point, giving ourselves the breathing room to perfect the balance, while still guaranteeing players that we wouldn’t have that power indefinitely.

#### **_Usage-based maturity_**

Lock those capabilities once a certain number of users or transactions are completed. This option needs to be carefully thought out to avoid exploits, but we could have, for example, built configurable fees into CryptoKitties that would lock in after 10,000 transactions.

#### **_Economic incentive_**

Align the creator’s incentives with increased decentralization. In this scenario, the creators profit more when the contract becomes more decentralized. Perhaps the fee rises with each level the developer ascends, locking in at the maximum fee when they reach full decentralization. Or, alternatively, perhaps they make no money at all until full decentralization is in place. This financial reward motivates the developer to reach decentralization at a reasonable pace.

### There’s no best approach to building on the blockchain

“Progressive decentralization” is really an umbrella encompassing many strategies, mechanisms, and tools to make building on the blockchain more viable. The best way to apply progressive decentralization will always depend on the project and use a mix of the concepts outlined above.

Progressive decentralization is not perfect. The ideal smart contract is simple and straightforward, and these measures add complexity. How and how much to incorporate it is a trade-off that needs to be evaluated on a case-by-case basis.

Although it may anger hardline decentralists, we believe progressive decentralization is far better for users in the long run: by giving developers the flexibility to adjust, the consumer gets a more useful product. That means they’ll actually use it, and once it brings value to their lives, they’ll sing its praises to the people around them. That’s how mass adoption starts.

_Authors: [Arthur Camara](https://medium.com/@arthur_camara), [Dieter Shirley](https://medium.com/@dete73), and Grady Mitchell_

