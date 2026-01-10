---
title: What is a Dapp? A Guide to Ethereum Dapps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-13T19:08:55.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-dapp-a-guide-to-ethereum-dapps
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/clifford-photography-hiFghSs4keM-unsplash.jpg
tags:
- name: dapps
  slug: dapps
- name: Ethereum
  slug: ethereum
- name: Smart Contracts
  slug: smart-contracts
seo_title: null
seo_desc: 'By Grant Bartel

  In the cryptoverse, a lot of attention is laid on Bitcoin. But don''t let that overshadow
  the growing interest in Ethereum, which is revolutionizing the way we think of applications.

  So, what is a Dapp? A Dapp, or decentralized applica...'
---

By Grant Bartel

In the cryptoverse, a lot of attention is laid on Bitcoin. But don't let that overshadow the growing interest in Ethereum, which is revolutionizing the way we think of applications.

So, what is a Dapp? **A Dapp, or decentralized application, is a software application that runs on a distributed network. It's not hosted on a centralized server, but instead on a peer-to-peer decentralized network.**

Alright, that's the short version, but there's a lot more to unpack. Let's dive into the world of Dapps, more specifically those built on the Ethereum protocol.

## What is Ethereum?

To understand what a Dapp is, you first need to understand what Ethereum is. Now, there are other protocols that are used to build Dapps, like EOS, NEO, Stellar, Tron, and Cardano, but the big dog is Ethereum.

Ethereum is a network protocol that allows users to create and run **smart contracts** over a decentralized network. A smart contract contains code that runs specific operations and interacts with other smart contracts, which has to be written by a developer. Unlike Bitcoin which stores a number, Ethereum stores executable code.

So, why should you care?

Because Ethereum removes the need for a third party to handle transactions between peers. Since the middle man is replaced by code, all kinds of costs are reduced, including time and money.

**Just like Bitcoin removes the need for someone to hold your money, Ethereum removes the need for someone to broker a deal.**

Now you might be wondering, where are all these smart contracts? Well, they're essentially hosted on multiple computer nodes all across the world. 

These nodes contain all of the information of all the world's smart contracts, including code, transactions, etc. They're constantly working to keep this information up-to-date so they all have the exact same copy. This what makes smart contracts, and cryptocurrencies in general, decentralized.

And since all of the nodes have the same information and are spread across the world, the removal of a node won't interrupt the execution of any smart contract. Redundancy ensures uptime.

## What is a Dapp?

Now that we have a good idea of what Ethereum and smart contracts are, we can start diving into the details of what a Dapp is.

Just to be clear, a Dapp is just like any other software application you use. It could be a website or an app on your phone. What makes a Dapp different than a traditional app is that it's built on a decentralized network, like Ethereum.

When you're creating your own Ethereum smart contracts, you're actually writing a piece of the backend code for your Dapp. And while your Dapp will have a user interface like a traditional app, either all or part of the backend is built on top of Ethereum.

**Dapp = frontend + smart contract backend**

This backend code is written in an Ethereum-specific language, including Solidity (the most popular), Serpent, and Vyper. Below is an example of a simple "Hello World" contract written in Solidity.

```
pragma solidity ^0.4.22;

contract helloWorld {
 function printHelloWorld () public pure returns (string) {
   return 'Hello World!';
 }
}
```

If the smart contract is deployed onto Ethereum's mainnet (i.e., production) or even a local testnet, your Dapp can execute the code in the smart contract by calling the function **printHelloWorld()**.

But what about the frontend? Is there any specific language you need to use for your Dapp?

Nope! You can use whatever frontend language/framework you want. But it is possible to host your frontend code on decentralized storage nodes to make both your frontend and backend decentralized. 

Take a look at technologies like [Swarm](https://ethereum.stackexchange.com/questions/375/what-is-swarm-and-what-is-it-used-for?noredirect=1&lq=1) and [IPFS](https://en.wikipedia.org/wiki/InterPlanetary_File_System) to learn more about decentralized storage.

OK, so Dapps are just applications that have some or all of their backend decentralized and possibly even have a decentralized frontend. Why should you care?

The development of Dapps is another step toward a future of the Internet that's commonly referred to as Web 3.0.

## Ethereum Dapps: The Backbone of Web 3.0

Since the creation of the Internet, the amount of information and human interaction has exploded. We're able to produce and consume information at near infinite levels.

Unfortunately, the ability to control this information has become heavily centralized over time. This includes information about your social life, health, finances, and much more. Those who control this information are the ultimate owners of it and can use it as they see fit.

These are essentially middle men that hold your information on their centralized servers so they can provide you with services, like holding your money, hosting you website, connecting with family and friends, etc. And at the push of a button, they can completely remove you from accessing this (your?) information and all related services.

This is a monopoly on the information you produce and consume as well as the services you use. Thankfully, Web 3.0 changes all of that and Ethereum Dapps are playing a central role.

Web 3.0 is a lot of things, but at its core is a technology based on decentralization. By decentralizing information and services, large corporations and governments won't be able to control users of the Internet through monopolistic, authoritarian tactics.

Ethereum Dapps, with their ability to decentralize information and services, gives Web 3.0 a platform to deliver a completely free (as in freedom) and accessible Internet for everyone. No longer will there be a central point of control because there won't be middle men to facilitate the flow of information and services.

Some of the most promising Ethereum tokens and Dapps are laying the foundation for the future of the Internet, including:

* [Basic Attention Token](https://basicattentiontoken.org/) (BAT): used to improve privacy and value transfer between users, publishers, and advertisers. Used in the [Brave browser](https://brave.com/).
* [Golem](https://golem.network/) (GNT): used to run code on one or many distributed compute nodes.
* [Minds](https://www.minds.com/): a social media platform that improves value transfer between content creators and consumers.
* [TokenSets](https://www.tokensets.com/): used to manage cryptocurrency assets via tokenized automated asset management strategies.
* [Aave](https://aave.com/): used to earn interest on cryptocurrency deposits and borrow cryptocurrency assets.
* [IDEX](https://idex.market/): a decentralized cryptocurrency exchange.

## Closing Thoughts

Since the creation of Bitcoin, the first cryptocurrency, there's been a massive growth in the cryptoverse. 

Being able to store data in a decentralized way was a necessary stepping stone to the decentralization of code execution. With Ethereum, it's now possible to deploy smart contracts across the world to power the backend for existing and future Dapps. 

And as more and more Dapps are launched, we'll get closer and closer to a more free, fair, and accessible Internet.

_I’m Grant and I’m a freelance SEO and content professional. If you’re looking to grow your brand's organic search traffic, I can help with your [fintech SEO](https://www.writefintech.com/). Cheers!_  

