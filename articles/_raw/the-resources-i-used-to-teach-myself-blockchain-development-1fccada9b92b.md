---
title: Resources I Used to Teach Myself Blockchain Development
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-09T14:46:04.000Z'
originalURL: https://freecodecamp.org/news/the-resources-i-used-to-teach-myself-blockchain-development-1fccada9b92b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6bOXOdSXtre9t7aMgTr-4A.png
tags:
- name: Blockchain
  slug: blockchain
- name: dapps
  slug: dapps
- name: Ethereum
  slug: ethereum
- name: Solidity
  slug: solidity
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Gwendolyn Faraday

  I started investing in cryptocurrencies last year, and just kept going down the
  blockchain rabbit hole from there. Where I live especially, much of the blockchain
  community is focused on things like trading and investing in crypt...'
---

By Gwendolyn Faraday

I started investing in cryptocurrencies last year, and just kept going down the blockchain rabbit hole from there. Where I live especially, much of the blockchain community is focused on things like trading and investing in cryptocurrencies. Although it was fun to invest at first, I wasn’t so interested in that. So I started my own local meetup group to focus on blockchain development.

The meetup group allowed me to connect and learn alongside members of the community, and I’ve used that to compile a list of resources that I, and the other members, have found useful. These resources are arranged from the most basic blockchain explanations to the underlying systems as well as building applications on top of the blockchain.

There is a lot of noise out there. I hope this helps you make sense of it all if you are interested in becoming a blockchain professional.

### **Table of Contents:**

1. Learn the basics
2. Dapp Development with Ethereum
3. Game Theory
4. Cryptography
5. Audio/Supplementary Materials
6. Other Types of Blockchain Development
7. Research

### **The Basics — How Blockchain Technologies Work**

It can take a minute to wrap your head around the complexities of blockchain technologies. This technology encompasses so many different fields: computer science, game theory, cryptography, and economics just to name a few. Thus it’s difficult to initially learn the ins and outs of how it all works.

Here are a few resources that I think give a good, clear overview of how blockchain really works.

1. **Start with this video breaking down how it works:**

**2. Watch both videos here (there is some overlap with the prior resource, but it will cement the concepts in your mind) and play around with the demo on the site:**

[**Blockchain Demo**](https://anders.com/blockchain/)  
[_A live blockchain demo in a browser._anders.com](https://anders.com/blockchain/)

3. **Read [the Chapter “What is Ethereum](https://github.com/ethereumbook/ethereumbook/blob/develop/what-is.asciidoc)” from the GitHub book, “[Mastering Ethereum](https://github.com/ethereumbook/ethereumbook)”**

### **Dapp Development with Ethereum**

There are many different blockchains now that allow you to create applications and smart contracts. Ethereum is by far the most popular option, with Solidity being its dominant programming language. I suggest trying out building dapps with these technologies first.

By far **the best way to learn to code with Solidity** is [Cryptozombies](http://cryptozombies.io/). It’s an interactive coding environment that teaches you how to program Solidity step by step while building a zombie game! It’s kept up to date with new versions of Solidity too, which is hard to come by in the ever-changing blockchain space.

**If you want something in addition to Cryptozombies, here are two other recommendations I have for learning solidity:**

1. [Youtube video series for dapp development](https://www.youtube.com/playlist?list=PL16WqdAj66SCOdL6XIFbke-XQg2GW_Avg) — This channel explains things very well, but the syntax isn’t totally up to date so you might have to google some things if you are getting errors. The Remix editor he uses will give you hints about what you need to change, so you should be fine.
2. [Stephen Grider on Udemy](https://www.udemy.com/ethereum-and-solidity-the-complete-developers-guide) — this is a paid course, but you can get a deal for ~$9.99 USD and it has good examples and content.

After you finish Cryptozombies, it’s a good idea to learn how to use the [Remix IDE](http://remix.solidity.com) for creating, debugging, and deploying contracts. The [docs have a quick start and lots of step-by-step instructions with screenshots](https://media.readthedocs.org/pdf/remix/latest/remix.pdf) to get you going.

You should also learn about Ethereum [clients](https://github.com/ethereumbook/ethereumbook/blob/3812a5dfa5b851a1aaa52b14c5aea6c74629e5a0/clients.asciidoc) and [wallets](https://github.com/ethereumbook/ethereumbook/blob/3812a5dfa5b851a1aaa52b14c5aea6c74629e5a0/wallets.asciidoc). Those links will explain everything you need to know. Metamask is a browser plugin and a great way to get started (it’s for Chrome or Firefox, but the Chrome one seems to work much better).

Next, learn more advanced smart contract development. Start by reading the [Solidity documentation](https://solidity.readthedocs.io/en/v0.4.24/solidity-by-example.html). It goes into more advanced concepts and has some good example dapps, too. Ethereum.org also had some good dapp examples to look through like [this one](https://www.ethereum.org/dao). You can copy the examples straight into the Remix IDE and test them out for yourself.

After you have a good grasp on Solidity and smart contracts, start looking through some open source examples. The default go-to seems to be [Crypto Kitties](https://etherscan.io/address/0x06012c8cf97bead5deae237070f9587f8e7a266d#code) (you can see the contract code at any Ethereum address at [etherscan.io](https://etherscan.io)), but there are many more that can be great learning tools. You can search GitHub and Etherscan to find more.

There is a lot of development going on in the Ethereum space around developer tools and security. Here are some awesome libraries and tools along those lines that you can check out:

* [Open Zeppelin](https://github.com/OpenZeppelin/openzeppelin-solidity)
* [Truffle Development Framework](https://www.truffleframework.com/)
* [ConsenSys — Smart Contract Best Practices](https://github.com/ConsenSys/smart-contract-best-practices)

### Game Theory

Some of the problems that blockchain aims to solve are from game theory, most notably The Byzantine Generals Problem. This problem deals with consensus between many different parties without having to trust that any individual is not malicious.

[The Great Courses Plus offers an excellent lecture series on various topics in game theory](https://www.thegreatcoursesplus.com/game-theory-in-life-business-and-beyond). They have a monthly subscription model with a two-week free trial. The 24 30-minute lectures cover a broad range of topics in game theory, and I think it’s great for an overall understanding of the subject.

### Cryptography

I am definitely not an expert here, but I am continuously learning about how cryptography works and how it can be applied to blockchain. This area does get really deep into the math, as Ethereum and many other blockchains use Eliptical Curve Cryptography.

As a noob in this space, here are some resources I have found useful:

* [Coursera Cryptography I](https://www.coursera.org/learn/crypto) — Free to audit the course; paid if you want a certificate.
* [Chapter on Cryptography in the Ethereum Mastery book](https://github.com/ethereumbook/ethereumbook/blob/3812a5dfa5b851a1aaa52b14c5aea6c74629e5a0/keys-addresses.asciidoc)

### Audio Supplementary Material

* [**Podcast:** Software Engineering Daily, Blockchain](https://itunes.apple.com/us/podcast/blockchain-software-engineering-daily/id1230807219) — This is my favorite blockchain podcast. They do a very good job at explaining complex topics and have a variety of industry leaders on the show.
* [**Podcast:** CryptoDisrupted](https://cryptodisrupted.com/) — The host brings in a lot of guests from interesting projects in the blockchain space. I’ve enjoyed most of what I’ve listened to with this podcast.

### Other Types of Blockchain Development

The Ethereum community has, by far, the most developers and learning resources, so it’s a good place to get started with blockchain development. I think you would be remiss if you did not explore other innovation in the space, however. Below are some interesting projects.

[**Lisk**](https://lisk.io/) — Makes blockchain development more accessible, as everything is built in JavaScript.

[**EOS**](https://www.eos.io/) — The creator, Dan Larimer, had built several other successful blockchain solutions before starting this project. EOS is supposed to solve some of the problems with Ethereum, like scaling and security. It’s sometimes called, “The Ethereum Killer”.

**Interchain Protocols** — These are some solutions that help facilitate transactions between different blockchains and also have interesting solutions to help blockchain scale:

1. [Cosmos](https://cosmos.network/)
2. [Polkadot](https://polkadot.network/)
3. [Interledger](https://interledger.org/)

[**Hyperledger**](https://www.hyperledger.org/) — An open source collaborative effort created to advance cross-industry blockchain technologies. It’s hosted by The Linux Foundation.

[**Holo**](https://holo.host/) — A post-blockchain technology that attempts to solve the issues of scalability and centralization in today’s blockchain technologies.

### Research & Current Development

Once you learn the basics, it’s so important to read research papers to achieve mastery in the blockchain space. Here are some places where I have had success:

* [The Morning Paper — Blockchain Articles](https://blog.acolyer.org/?s=blockchain)
* [Collection of whitepapers from ICOs](http://whitepaperdatabase.com/)
* [http://blockchain.mit.edu/](http://blockchain.mit.edu/)
* [https://www.blockchainresearchinstitute.org/](https://www.blockchainresearchinstitute.org/)

### Conclusion

I will be continuously studying blockchain development and trying to find new and interesting solutions. Please leave a comment or message me if I am missing anything here.

Right now, I am planning more articles about companies, projects, and people of interest in the blockchain space. Follow me if you are interested in any of these things.

