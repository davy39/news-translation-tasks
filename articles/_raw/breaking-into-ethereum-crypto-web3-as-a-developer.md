---
title: How to Break into Ethereum, Crypto, and Web3 as a Developer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-18T21:04:00.000Z'
originalURL: https://freecodecamp.org/news/breaking-into-ethereum-crypto-web3-as-a-developer
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/break-into-blockchain-article.jpg
tags:
- name: Blockchain
  slug: blockchain
- name: Career Change
  slug: career-change
- name: crypto
  slug: crypto
- name: ethereum blockchain
  slug: ethereum-blockchain
- name: Web3
  slug: web3
seo_title: null
seo_desc: 'By Nader Dabit

  Lately, I''ve been talking about my move into the Web3, Ethereum, and crypto space
  since making the switch from a traditional web, mobile, and cloud background.

  Since making that move, a shocking number of people have reached out to me ...'
---

By Nader Dabit

Lately, I've been [talking](https://twitter.com/dabit3/status/1391171104757125122) about [my move](https://twitter.com/dabit3/status/1379157277660299264) into the [Web3](https://ethereum.org/en/developers/docs/web2-vs-web3/), Ethereum, and crypto space since making the switch from a traditional web, mobile, and cloud background.

Since making that move, a shocking number of people have reached out to me who are also thinking about doing the same. 

It's really great to see so many other people interested in these fields. And if I'm being honest – it feels validating to know that so many others are also on the fence and are so deeply interested in the space as well.

As for me, I was nervous about making the career switch. Moving into a completely new area of specialization, with a technology I was still getting ramped up on, and a community I was not yet involved with, was a big leap. Especially compared to a very comfortable role with a FAANG company that paid really well (and a team that I really loved).

After over a month, I have zero regrets with the change. I'm also the happiest I've been in a long time, and am excited and energized about the things I have the opportunity to work on everyday.

I decided to write this post to give a blueprint for anyone looking to get into blockchain, crypto, Ethereum, and Web3 from a traditional development background. I can point people to this blog post the next time I get asked how to get into the space.

### I'll break this article up into a few main parts:

1. Technologies and resources to learn
2. Tradeoffs and considerations
3. People to follow
4. Companies hiring and doing interesting stuff
5. General tips and landing a job

Let's dive in.

## Technologies and Resources to Learn About Ethereum and Blockchain

What I'm most interested in is usually a function of where I predict technology will be in the near future and where I see the current momentum being. So that's what I will focus on here (and this is what I am doing personally).

To me, the most exciting parts of this space are decentralization, [DeFi](https://blog.coinbase.com/a-beginners-guide-to-decentralized-finance-defi-574c68ff43c4), [governance](https://docs.ethhub.io/ethereum-basics/governance/) / [DAOs](https://www.investopedia.com/tech/what-dao/), and [decentralized web infrastructure](https://www.youtube.com/watch?v=j2rXJLW_93o).

Because of this, I'm focusing on both Ethereum development and Solidity. With the Solidity programming language ,you can program smart contracts for Ethereum as well as for many other [EVM compatible blockchains](https://chainid.network/). 

As of this writing, Ethereum also has the powerful and important combination of momentum, developer mindshare, and existing production [dapps](https://everest.link/).

Ethereum is also currently moving to a new consensus mechanism, [proof of stake](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/). This addresses the environmental concerns I used to have about how cryptocurrency works at a core level.

Once you learn how everything works fundamentally, I encourage you to then check out other blockchains and projects outside of Ethereum and EVM. 

This will give you a better understanding of the industry as a whole. It will also help you see if there are other projects that attract you or that you believe are better approaches to achieving the goal that is Web3. 

Consider looking into [Solana](https://solana.com/), [Polkadot](https://polkadot.network/), [Near](https://near.org/), [Avalanche](https://www.avax.network/) or [Cosmos](https://cosmos.network/).

To get started learning blockchain development with Ethereum and Solidity, I suggest you do the following:

### 1. Read the Ethereum docs

Scan through the [Ethereum docs](https://ethereum.org/en/developers/docs/). Be sure to check out the section [Intro to Ethereum](https://ethereum.org/en/developers/docs/intro-to-ethereum/) as well as anything else that catches your eye.

Also be sure to check out the [dapp showcase](https://ethereum.org/en/dapps/) to get a good understanding of the successful apps being built and used in the current ecosystem.

### 2. Read the Solidity documentation

The [Solidity docs](https://docs.soliditylang.org/en/v0.8.4/) are a really good place to get started, especially [solidity by example](https://docs.soliditylang.org/en/v0.8.4/solidity-by-example.html). This gives you a few examples of popular smart contracts like voting, an auction, remote purchase, and micropayments.

You can copy and paste these contracts in the [Remix IDE](https://remix.ethereum.org/) to start executing and modifying them to see how they work.

I also did a video walkthrough of the voting contract [here](https://www.youtube.com/watch?v=GB3hiiNNDjk).

### 3. Get comfortable with the Remix IDE

It's really easy to play around with and start building smart contracts without having to set up any type of development environment by using the [Remix IDE](https://remix.ethereum.org/). It's part of the [Remix Project](https://remix-project.org/) which is funded by the [Ethereum Foundation](https://ethereum.foundation/).

This Remix IDE allows you to create, edit, and execute smart contracts directly from your browser. It offers a perfect environment for learning how solidity works. It's also great for building out various types of smart contracts and playing around with them as you are learning both solidity and how to interact with Ethereum

### 4. Try building out a full stack dapp

In addition to Solidity, the other parts of the the development stack include a local Ethereum environment like [Hardhat](https://hardhat.org/) or [Truffle](https://www.trufflesuite.com/), a wallet like [Metamask](https://metamask.io/), as well as a client-side library that allows you to interact with the blockchain, like either [Ethers.js](https://docs.ethers.io/) or [Web3.js](https://web3js.readthedocs.io/).

To understand how all of this all fits together, it's useful to build out a full stack dapp on this stack from scratch. You can set up the front end project as well as the local development environment and deploy, run, and interact with a smart contract on the blockchain.

Here are two introductory courses to get you going with this:

1. [Ethereum Programming Tutorial - DeFi, Solidity, Truffle, Web3.js](https://www.youtube.com/watch?v=xWFba_9QYmc)
2. [The Complete Guide to Full Stack Ethereum Development](https://www.youtube.com/watch?v=a0osIaAOFSE) ([and here it is in article form, too](https://www.freecodecamp.org/news/full-stack-ethereum-development/))

### 5. Consider reading these books

The space itself moves very quickly, so technical books often get out of date just as quickly. The fundamentals of what Web3 is, though, have not changed much at all. 

There are a few really great books that helped me not only grasp the current state of everything, but that also helped open my eyes to the future possibilities and opportunities that lie within it.

#### Token Economy - How the Web3 reinvents the internet

If you only read one of these books, this is the one I'd say is the most important. It is a masterful deep dive into all of the shortcomings of the web as we know it, what Web3 aims to be, how it will affect various parts of our lives as we know it, and what needs to happen for this vision to be realized.

You can view the book [here](https://shermin.net/token-economy-book/).

#### The Infinite Machine - How an Army of Crypto-hackers Is Building the Next Internet with Ethereum

This is the amazing story of how Ethereum came to be, walking you through the history of it all. It is a very thorough and entertaining account of the origin story of Ethereum, I highly recommend checking it out.

You can view the book [here](https://www.harpercollins.com/products/the-infinite-machine-camila-russo?variant=32123333836834).

#### New Village - Power Back to People

This is a really cool story of how blockchain technologies and decentralization will affect the future of the world.

You can view the book [here](https://www.amazon.com/New-Village-Power-Back-People-Blockchain/dp/1718045743)

#### How to DeFi

As you can probably tell by the title, this book focuses on how you can start using DeFi today. It gives you a good understanding about how you can use it today as well as some applications of it that we will see at some time in the future.

You can view the book [here](https://landing.coingecko.com/how-to-defi/)

#### The Spatial Web

The Spatial Web is a book that explores the future of the web and all of the implications, not only of Web3 and decentralization, but how everything will come together to enable things that we may have not yet considered. 

It does a good job weighing the positive and negatives as well as ways that we may be able to address any negative outcomes of what is to come.

You can view the book [here](https://www.goodreads.com/book/show/52816204-the-spatial-web)

And here are a couple of solidity books:

* [Hands-On Smart Contract Development with Solidity and Ethereum](https://www.oreilly.com/library/view/hands-on-smart-contract/9781492045250/)
* [Mastering Ethereum](https://www.oreilly.com/library/view/mastering-ethereum/9781491971932/)

### 6. Listen to these podcasts

Here are some good podcasts:

* [Founders of Web 3](https://outlierventures.io/podcasts/) – The people that are creating and building the next phase of the internet.
* [Bankless](http://podcast.banklesshq.com/) – The Ultimate Guide to Crypto Finance
* [Into the Ether](https://podcast.ethhub.io/) – Podcast about Ethereum
* [Crypto 101](https://player.fm/series/crypto-101)
* [Epicenter](https://player.fm/series/epicenter-learn-about-crypto-blockchain-ethereum-bitcoin-and-distributed-technologies-41400) – Learn about Crypto, Blockchain, Ethereum, Bitcoin and Distributed Technologies

### 7. Watch these YouTube channels

* [Ethereum Foundation](https://www.youtube.com/channel/UCNOfzGXD_C9YMYmnefmPH0g)
* [Eat the Blocks](https://www.youtube.com/channel/UCZM8XQjNOyG2ElPpEUtNasA) – Short videos on blockchain development
* [Finematics](https://www.youtube.com/c/Finematics/videos) – Sharing interesting DeFi videos
* [Dapp University](https://www.youtube.com/channel/UCY0xL8V6NzzFcwzHCgB8orQ) – Videos in the Ethereum space
* [BlockGeeks](https://www.youtube.com/c/BlockGeeks/featured) – General Blockchain Training
* [The Daily Gwei](https://www.youtube.com/channel/UCvCp6vKY5jDr87htKH6hgDA)
* [Austin Griffith](https://www.youtube.com/channel/UC_HI2i2peo1A-STdG22GFsA)

I've also begun doing videos and tutorials on Ethereum and Solidity, so consider checking out [my YouTube](https://www.youtube.com/channel/UC7mca3O0DmdSG2Cr80sOD7g) channel.

## Tradeoffs and Considerations of Switching Careers

There are always things to consider when making a career transition, but especially when considering this space.

There are a lot of positives, but there are also unknowns as well as negatives. Let's talk about some of them.

### It's nascent tech

While there are many existing dapps and companies already flourishing, this space is very much still coming into existence in many ways.

There are a lot of problems that we still need to solve, and there are no clear answers for many questions you'll have. The problems being solved are often complex, sometimes combining one or more aspects of distributed systems, game theory, cryptography, economics, social and political science, identity, psychology, and more.

Because of this, there are still things that we cannot yet build with the existing solutions that are available.

I personally think this is one of the more exciting things about all of it it, but it's not for everyone.

### It's a volatile space

Many of the projects are built around various types of tokens. The value of many of these tokens rises and falls dramatically, and you often see that people gain and lose excitement in the entire space based on these swings.

If you haven't fundamentally bought into the ideas behind decentralization itself, you may find these ups and downs mentally taxing.

### It's full of speculation

Because a lot of people only buy into certain tokens in a speculative way, it attracts some people who are in it only for the money.

You see things like scammers trying to get over on people and steal their money, endless talk about price swings from people who are speculating, and outright scam projects that often discredit the industry as a whole.

This is an annoying part of it and I don't really see it going away anytime soon.

### This thread

I would also check out [this Twitter thread](https://twitter.com/jonsyu/status/1389635626698297344). Although I have not experienced all of these things, he is definitely shining a light on some of the things I have seen.

## General Tips and How to Land a Blockchain or Crypto-Related Job

There are many areas within the space that you can focus on and provide a positive impact on a team. I'd look into the different areas like governance, DeFi, NFTs, and decentralized web protocols to see what interests you the most and then focus on that.

There are a lot of opportunities and a lot of ways to stand out and get noticed. If you find an interesting project and would like to get involved, jump right into their community and ecosystem and start learning. Then see where you may be able to help out. Join their Discord or look at their GitHub issues to find ways that you can contribute.

This will give you an opportunity to meet people involved in the project and will open up discussions for potentially landing a role with them. In fact, it is very common for people within the teams to take notice of active community participants, they will then often reach out and try to recruit you without you even applying.

The pay is usually [good](https://cryptocurrencyjobs.co/salaries/solidity-developer/). Depending on where you are coming from, it could be more or less, but it's probably not going to be at the high levels of what you see at FAANG companies. 

There is probably more potential upside. Most companies offer a combination of base pay + equity in the form of their digital token, so if you stick around and can help make the project successful and the value of the token goes up, you can often make more than what you would in many other areas.

## People to follow on Twitter

Here are a few people who you may consider following on Twitter:

[Vitalik](https://twitter.com/VitalikButerin)  
[Ashleigh Schapp](https://twitter.com/ashleighschap)  
[Arthur Hayes](https://twitter.com/CryptoHayes)  
[Stani Kulechov](https://twitter.com/StaniKulechov)  
[Gloria Kimbwala](https://twitter.com/gkimbwala)  
[Niran Babalola](https://twitter.com/niran)  
[Ric Burton](https://twitter.com/ricburton)  
[Dennison Bertram](https://twitter.com/dennisonbertram)  
[Mana Silvora](https://twitter.com/manasilvora)  
[Austin Griffith](https://twitter.com/austingriffith)  
[Santiago Palladino](https://twitter.com/smpalladino)  
[Zaki Manian](https://twitter.com/zmanian)  
[Anthony Sassano](https://twitter.com/sassal0x)

I also found [this comprehensive list](https://twitter.com/i/lists/869994563691319296/members) created by someone on Twitter.

A few people on my team at [Edge & Node](https://twitter.com/edgeandnode):  
[Yaniv Tal](https://twitter.com/yanivgraph)  
[Tegan Kline](https://twitter.com/theklineventure)  
[Eva Beylin](https://twitter.com/evabeylin)  
[Adam Fuller](https://twitter.com/azacharyf)  
[Brandon Ramirez](https://twitter.com/RezBrandon)

## Teams doing interesting stuff (and hiring)

[Compound](https://compound.finance/about#jobs)  
[Uniswap](https://jobs.lever.co/Uniswap)  
[Chainlink](https://chainlinklabs.com/careers)  
[Skynet Labs](https://jobs.lever.co/SkynetLabs)  
[Aave](https://aave.com/careers/)  
[Matic](https://matic.network/careers/)  
[Livepeer](https://livepeer.org/jobs)  
[Consensys](https://consensys.net/open-roles/)  
[ENS](https://medium.com/the-ethereum-name-service/ens-is-hiring-come-build-a-new-decentralized-internet-with-us-24398dea3ac)  
[OpenZeppelin](https://openzeppelin.com/jobs/)  
[Foundation](https://foundation.app/careers)  
[Zora](https://cryptocurrencyjobs.co/startups/zora/)  
[Synthetix](https://synthetix.com/careers)  
[Digital Currency Group](https://jobs.dcg.co/companies)

You can also find a pretty decent list of job opportunities in cryptocurrency [here](https://cryptocurrencyjobs.co/).

Also, my team at [Edge & Node is hiring](https://edgeandnode.com/jobs)!

## Conclusion

Did I mention this space is volatile? Be ready for some high highs and low lows, but also for some of the most fun you may have in your career. 

You'll be working alongside some of the smartest people in tech trying to solve some of the most complex problems that I think will ultimately have a massive positive impact on humanity.

