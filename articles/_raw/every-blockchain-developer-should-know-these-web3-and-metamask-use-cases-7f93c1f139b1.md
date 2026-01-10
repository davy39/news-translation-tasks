---
title: Every blockchain developer should know these Web3 and Metamask use cases
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-15T19:00:24.000Z'
originalURL: https://freecodecamp.org/news/every-blockchain-developer-should-know-these-web3-and-metamask-use-cases-7f93c1f139b1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*JVmq6javfae3gzTA.jpg
tags:
- name: Blockchain
  slug: blockchain
- name: Cryptocurrency
  slug: cryptocurrency
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web3
  slug: web3
seo_title: null
seo_desc: 'By Igor Yalovoy

  Update

  On November 2nd MetaMask and other dapp browsers will stop exposing user accounts
  by default. This will make some code from this paper to break. I will publish updated
  version with web3 1.0 and new MetaMask interface.

  Metamask ...'
---

By Igor Yalovoy

### Update

On [November 2nd](https://medium.com/metamask/https-medium-com-metamask-breaking-change-injecting-web3-7722797916a8) MetaMask and other dapp browsers will stop exposing user accounts by default. This will make some code from this paper to break. I will publish updated version with web3 1.0 and new MetaMask interface.

[Metamask](https://ylv.io/10-web3-metamask-use-cases-ever-blockchain-developer-needs/Metamask.io) is the de facto standard for dApps on the web. It injects a Web3 instance into a window object making it available for JavaScript code.

We are going to use Web3 0.20 version, not Web3 1.0. The code for Web3 1.0 would be different.

Every dApp has its mission, but the way they interact with Metamask is similar. In this article, we’ll cover the ten most common practices to handle Web3/Metamask interactions.

### #1. Detect Metamask and instantiate Web3

According to [docs](https://github.com/MetaMask/faq/blob/master/DEVELOPERS.md#partly_sunny-web3---ethereum-browser-environment-check), here’s the best way to do it.

What is going on here? First, we check if Web3 was injected. If it is injected we create a new instance using the injected provider. Why is that? Because we want to use our library version, not the one injected by Metamask.

If Web3 is not present, we try to connect to a localhost provider, like [ganache](https://truffleframework.com/ganache).

### #2. Check if Metamask is locked

Metamask can be installed but locked. In order to interact with a user account and send transactions, the user has to unlock Metamask.

### #3. Check the current network

There are many test networks beyond the main network. Typically your contract is deployed to a certain network. You want to be sure that the user runs Metamask on the same network.

### #4. Get the current account

A user may have multiple accounts at Metamask, but they expect the dApp to interact with the current one.

You should always grab the account from the Web3 instance. Do not keep and reuse it, because the user may change their account at any time.

### #5. Get the balance on the current account

Here we use the function `getAccount` from #4 and call `getBalance`. Easy.

### #6. Detect that the current account has changed

A user may change their account at any time. You dApp should be ready for that and react properly.

### #7. Detect whether Metamask is locked/unlocked

Similar to #6. A user may lock/unlock anytime. Your dApp should handle it correctly.

### #8. Handle cancel/confirm

Once a user interacts with your dApp, you have to send a transaction using the Web3 API. A user may press the cancel or confirm button on the Metamask popup. This may lead to UI inconsistency if not handled correctly.

In order to return instantly with the transaction hash, call `contract.methodName.sendTransaction`.

### #9. Get the transaction receipt

Once your dApp transaction is mined, a transaction receipt becomes available. Yet there is no event/notification, so we have to implement a poll mechanism.

### #10. Listen for Web3 events

Solidity events are great. They allow switching from ugly polling to just a push mechanism, assuming your contract implements all necessary events. You can completely avoid polling and just react to events. Event callback [returns](https://github.com/ethereum/wiki/wiki/JavaScript-API#callback-return) a lot of data, but we are mostly interested in `args`.

### Summary

Whatever your dApp is about, it still has to perform common tasks, such as detecting Web3, getting the account state and balance, recognizing the current network, and handling transactions and events. We’ve gone over how it can be done using ten code snippets.

### P.S.

A lot of examples here use methods which might throw an error because of Metamask’s state or some variables being undefined at the moment of a call. You should wrap them in `try/catch` in a production environment.  
 Async/await has been used here for simplicity. It can be replaced with Promise then/catch.

### Social

* Connect with me on [LinkedIn](https://www.linkedin.com/in/ylv-io/).
* Follow me on [twitter](https://twitter.com/ylv_io).

### Want More?

[**How to Create and Deploy Your Own EOS Token**](https://hackernoon.com/how-to-create-and-deploy-your-own-eos-token-1f4c9cc0eca1)  
[_We are going to figure out what is EOS token and how you can create and deploy one yourself._hackernoon.com](https://hackernoon.com/how-to-create-and-deploy-your-own-eos-token-1f4c9cc0eca1)[**How Much Does It Cost to Run DApp in 2018**](https://hackernoon.com/how-much-does-it-costs-to-run-dapp-in-2018-87ee11fe1d5d)  
[_You think your AWS or Digital Ocean bill for your website is killing you?_hackernoon.com](https://hackernoon.com/how-much-does-it-costs-to-run-dapp-in-2018-87ee11fe1d5d)[**Difference Between Ethereum and EOS Tokens**](https://medium.com/coinmonks/difference-between-ethereum-and-eos-tokens-f2399051c0b6)  
[_Ethereum has ERC-20 token and EOS has EOSIO.Token. They serve the same purpose, but are they the same?_medium.com](https://medium.com/coinmonks/difference-between-ethereum-and-eos-tokens-f2399051c0b6)

_Originally published at [ylv.io](https://ylv.io/10-web3-metamask-use-cases-ever-blockchain-developer-needs/) on October 15, 2018._

