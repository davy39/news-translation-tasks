---
title: 'Decentralized Applications Architecture: Back End, Security and Design Patterns'
subtitle: ''
author: Nikita Savchenko
co_authors: []
series: null
date: '2019-04-02T15:51:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-design-a-secure-backend-for-your-decentralized-application-9541b5d8bddb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sd62aH6GGS1RoCR9t4QNyQ.png
tags:
- name: Blockchain
  slug: blockchain
- name: crypto
  slug: crypto
- name: Ethereum
  slug: ethereum
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: Decentralized applications, or ÐApps, require a special system design to
  achieve high security and reliability. In this article I am going to cover several
  main principles of how to properly design and implement back end and smart contracts
  for decen...
---

[Decentralized applications](https://en.wikipedia.org/wiki/Decentralized_application), or ÐApps, require a special system design to achieve high security and reliability. In this article I am going to cover several main principles of how to properly design and implement back end and smart contracts for decentralized applications, taking [Ethereum](https://www.ethereum.org/) as a primary example, though much of it would apply to [EOS](https://eos.io/), [Tron](https://tron.network/) and other decentralized data platforms.

**Article Highlights**:

* How to store private keys on the back end without security concerns
* How to properly design smart contracts and what to “decentralize”
* Decentralized and semi-centralized applications architecture examples
* How to deal with low-level stuff like network load and failures

It’s going to be big, let’s do it!

### Decentralized Programs and Blockchain

Despite the fact that blockchain is facing a lot of adoption and regulation difficulties today, it’s a kind of technology which is here to stay, whether it’s blockchain, [hashgraph](https://en.wikipedia.org/wiki/Hashgraph), [tempo](https://www.radixdlt.com/) or any other distributed ledger technology still to come, regardless of the algorithm.

> The main value that blockchain and other similar technologies bring can be generalized as follows: they allow people to write and run programs which, practically, cannot be changed after creation nor tampered with during execution. In other words, these programs always run as designed, and no single party can influence their behavior.

This definition is valid for _many_ cryptocurrencies that exist today if we consider them as programs that define how coins can be transferred back and forth. This also explains why cryptocurrencies and many kinds of tokens have real value: they cannot be generated out of thin air, by their defined “underlying programs”.

Ethereum/EOS/Tron/… platforms, in contrast to Bitcoin, implement a more complex program layer, which in turn implements the execution environment allowing anyone to write their own decentralized programs on top of the platform. This user-defined programs always run as designed, without any exceptions, and their security is guaranteed by the platform.

### Decentralized Applications

These secure and unchangeable programs running on a decentralized network in combination with traditional front-end and back-end technologies are what we call **decentralized applications** (ÐApps) today. Through some of them can be semi-centralized, a major part of activities in the truly decentralized application should happen out of a central party’s control.

![Image](https://cdn-media-1.freecodecamp.org/images/a0d9mC2p5qPHjMfIXw8Oq0XHCy9CQdLOAWmG)
_If someone asked me to draw how DApps work today, I would probably have drawn this_

To imagine what we call decentralized applications today, take any existing centralized web resource like [_YouTube_](https://www.youtube.com/c/NikitaSavchenko) or [_Instagram_](https://instagram.com/nikitaeverywhere/) as an example and imagine that instead of a password-protected centralized account you have your “**crypto identity**” bound to the web/mobile resource.

That’s what [Wallet Software](https://metamask.io/) provides you. The [private key](https://en.wikipedia.org/wiki/Public-key_cryptography) from this identity (a secret, having which, you can act on behalf of this identity) is stored on your local device and never goes online, making no one able to control this identity but you. With this identity, you can perform different actions in both _centralized_ (web resource controlled by a central authority) and _decentralized_ (which is a different network from the traditional www, the goal of which is to eliminate the central authority) _networks_, using the website as an access point and/or as a graphical user interface. The whole point of this “crypto identity” is that your actions are cryptographically secured, and no one is able to change what have you signed nor your signature.

Today, the computational and storage capabilities of fault-tolerant decentralized networks like [Ethereum](https://www.ethereum.org/), [EOS](https://eos.io/) or [Tron](https://tron.network/) are limited. If they were scalable, we could use decentralized networks to store the whole decentralized application, including its graphical user interface, data and business logic. In this case, we would call these applications truly decentralized/distributed.

However, because those networks are not scalable today, we combine different approaches to achieve the maximum decentralization level for our applications. The “traditional” back end as we know it isn’t going anywhere. For instance:

* We use back end to host front end for a decentralized application.
* We use back end for integrations with any other existing technologies and services. Real, world-class applications cannot live in an isolated environment.
* We use back end to store and process anything big enough for a decentralized network (blockchain in particular). Practically, the whole application and its business logic are stored somewhere in the world, excluding the blockchain part only. Not to mention, [IPFS](https://ipfs.io/) and similar storage layers [cannot guarantee](https://github.com/ipfs/faq/issues/93) the accessibility of files, hence we cannot rely on them without hosting the files ourselves either. In other words, there’s always a need for a dedicated running server.

There’s no way of building a secure and partially decentralized application without using a solid back end as of today, and the whole point of this article is to explain how to do this right.

### (De)centralization and Tokens

It so happens that almost all decentralized applications today are built around so-called [tokens](https://coinmarketcap.com/tokens/) — custom-built (or just simply cloned) cryptocurrencies that drive a particular decentralized application. Tokens are simply a programmable currency or assets, that’s it.

![Image](https://cdn-media-1.freecodecamp.org/images/b-Ok08iucXB0n6VwiLcPzbW8BAWfTe7YRBxD)
_While token smart contracts determine how users can transfer tokens, application smart contracts can extend everything missing in token smart contracts. Both smart contracts run on top of decentralized networks_

Usually, a token is a “smart contract” (a custom program) written on top of the decentralized platform like Ethereum. By owning some tokens you are basically able to get different services on a web resource or mobile app, and trade this token for something else. The key point here is that the token lives on its own and it is not controlled by a central authority.

> There are many examples of applications that are build around tokens: from numerous collectible games like [CryptoKitties](https://www.cryptokitties.co/) (ERC721 tokens) to more service-oriented apps like [LOOM Network](https://loomx.io/purchase/), or even browsers like [Brave](https://brave.com/download) and gaming platforms like [DreamTeam](https://dreamteam.gg/) (ERC20-compatible tokens).

Developers themselves determine and decide how much control they will (or won’t) have over their applications. They can build the whole application’s business logic on top of smart contracts (like [CryptoKitties](https://www.cryptokitties.co/) did), or, they can make no use of smart contracts at all, centralizing everything on their servers. However, the best approach is somewhere in the middle.

### Back End for Decentralized Networks

From a technical point of view, there has to be a bridge that connects tokens and other smart contracts with the web/mobile application.

In today’s fully decentralized applications, where clients interact with smart contracts directly, this bridge is narrowed down to a [JSON RPC API](https://github.com/ethereum/wiki/wiki/JSON-RPC) capabilities of [public APIs or node pools like Infura](https://infura.io), which in turn are forced to exist because of the fact that not every device can run and support its individual network node. However, this API provides an only basic and very narrow set of functions, which barely allow making simple queries nor efficiently aggregate data. Because of this, eventually, custom back end kicks in, making the application semi-centralized.

The whole interaction with the decentralized network can be narrowed down to just one or two points, depending on the application needs:

1. **Listening to the network events** (like token transfers) / **reading the network state**.
2. **Publishing transactions** (invoking state-changing smart contract functions like token transfer).

Implementing both of these points is quite tricky, especially if we want to build a secure and reliable back-end solution. Here are the main points which we are going to break down below:

* First of all, in Ethereum, events retrieval is not production-ready out of the box. Because of multiple reasons: network nodes can fail while fetching a large number of events, events can disappear or change because of network forks, etc. We have to build an abstraction layer to sync events from the network and guarantee their reliable delivery.
* The same for transaction publishing, we have to abstract Ethereum’s low-level stuff like nonce counters and gas estimations, as well as transaction republishing, providing a reliable and stable interface. Moreover, transaction publishing implies using private keys, which requires advanced back-end security.
* Security. We are going to take it seriously and face that it’s impossible to guarantee that private keys won’t ever be compromised on a back end. Luckily, there is an approach to designing a decentralized application without even **a need** for back-end accounts to be highly secured.

In our practice, all of this made [us](https://dreamteam.gg/) create a robust back-end solution for Ethereum which we name **Ethereum Gateway**. It abstracts other microservices from Ethereum’s fun and provides a reliable API to work with it.

As a [fast-growing startup](https://dreamteam.gg/), we cannot disclose the complete solution (just yet) for obvious reasons, but I am going to share everything that you need to know to make your decentralized application work flawlessly. However, if you have any specific questions or inquiries, feel free to contact [me](https://nikita.tk/). Comments to this article are much appreciated as well!

![Image](https://cdn-media-1.freecodecamp.org/images/aR03aGoFHc3EZ5ZCBVBPn6gqQEYYWFArNVy0)
_Back End Monitoring for Ethereum. The monitor demonstrates activities mainly regarding our [recurring billing feature](https://github.com/dreamteam-gg/smart-contracts/blob/master/contracts/token/TokenRecurringBilling.md" rel="noopener" target="_blank" title=") (though you can see peaks happening each hour)._

### Decentralized Applications Architecture

This part of the article highly depends on the needs of a particular decentralized application, but we will try to sort out some basic interaction patterns on top of which these applications are built (ÐPlatform = Decentralized Platform = Ethereum/EOS/Tron/Whatever):

#### **Client ⬌ ÐPlatform**: **_fully decentralized applications_**.

The client (browser or mobile application) talks to the decentralized platform directly with the help of Ethereum “wallet” software like [Metamask](https://metamask.io), [Trust](https://trustwallet.com/) or hardware wallets like [Trezor](https://trezor.io/) or [Ledger](https://www.ledger.com/). Examples of DApps build in such manner are [CryptoKitties](https://www.cryptokitties.co/), [Loom’s](https://loomx.io/) [Delegated Call](https://delegatecall.com/), crypto wallets themselves ([Metamask](https://metamask.io/), [Trust](https://trustwallet.com/), [Tron Wallet](https://tron.network/wallet?lng=en), others), decentralized crypto exchanges like [Etherdelta](http://etherdelta.com) and so on.

#### **ÐPlatform** ⬌ **Client** ⬌ **Back End** ⬌ **ÐPlatform**: **_centralized or semi-centralized applications_**.

The client interaction with the decentralized platform and the server has little in common. The good example of this is any (**_centralized_**) crypto exchange today, like [BitFinex](https://www.bitfinex.com/) or [Poloniex](https://poloniex.com): the currencies you trade on exchanges are simply recorded in the traditional database. You can “top up” your database balance by sending assets to a specific address (ÐPlatform ⬌ Client) and then withdraw assets after some actions in the app (Back End ⬌ ÐPlatform), however, everything you do in terms of a “ÐApp” itself (Client ⬌ Back End) does not imply your direct interaction with the ÐPlatform.

Another example is [Etherscan.io](https://etherscan.io/), which uses **_semi-centralized_** approach: you can do all useful decentralized actions there, but the application itself just doesn’t make sense without their comprehensive back end (Etherscan continuously syncs transactions, parses data and stores it, ultimately providing a comprehensive API/UI).

#### **Something in between: _still,_ _centralized or semi-centralized applications_.**

The above approaches combined. For example, we can have an application which provides various services in exchange for crypto, allowing you to log in and sign information with your crypto identity.

Hopefully, the interaction pattern of fully decentralized applications (Client ⬌ ÐPlatform) does not raise any questions. By relying on such amazing services like [Infura](https://infura.io/) or [Trongrid](https://www.trongrid.io/) one can simply build an application which doesn’t require a server at all. Almost all client-side libraries like [Ethers.js](https://github.com/ethers-io/ethers.js/) for Ethereum or [Tron-Web](https://github.com/tronprotocol/tron-web) for Tron can connect to these public services and communicate with the network. However, for more complex queries and tasks, you may need to allocate your own server anyway.

The rest of the interaction patterns which involve back end make things more interesting and complex. To put all these in a picture, let’s imagine a case where our back end reacts to some event in the network. For example, the user publishes an allowance transaction which gives us permission to charge them. To make a charge, we have to publish the charge transaction in response to the emitted allowance event:

![Image](https://cdn-media-1.freecodecamp.org/images/86mjnQ0gwUrAbrBL4t8LFCXbC4HyckEsmFYQ)
_An example flow of server’s reaction to the user’s action in the decentralized network_

From the back end point of view here’s what happens:

1. We listen to a particular network event by continuously polling the network.
2. Once we get an event, we perform some business logic and then decide to publish a transaction in response.
3. Prior to publishing the transaction, we want to ensure that it will likely be mined (in Ethereum, the successful transaction gas estimation means there are no errors against the _current network state_). However, we can’t guarantee that the transaction will be mined _successfully_.
4. Using a private key, we sign and publish the transaction. In Ethereum we also have to determine the gas price and gas limit of the transaction.
5. After publishing the transaction, we continuously poll the network for its status.
6. If it takes too long and we can’t get the status of the transaction, we have to re-publish it or trigger a “fail scenario”. Transactions can be lost for various reasons: network congestion, dropping peers, network load increase, etc. In Ethereum, you can also consider re-signing a transaction with a different (actual) gas price.
7. After we finally get our transaction mined, we can perform more business logic if needed. For example, we can notify other back end services about the fact of the transaction being completed. Also, consider waiting for a couple of confirmations prior to making final decisions regarding the transaction: the network is distributed and hence the result can change in a matter of seconds.

As you can see, there’s a lot going on! However, your application may not require some of these steps, depending on what you are trying to achieve. But, building a robust and stable back end requires having a solution for all the problems mentioned above. Let’s break this down.

### Decentralized Applications Back End

Here I want to highlight some of the points which arise most of the questions, namely:

* Listening to network events and reading data from the network
* Publishing transactions & how to do it securely

#### Listening to Network Events

In Ethereum, as well as in other decentralized networks, a concept of smart contract [events (or event logs, or just logs)](https://media.consensys.net/technical-introduction-to-events-and-logs-in-ethereum-a074d65dd61e) allows off-chain applications to be aware of what is happening in the blockchain. These events can be created by smart contract developers at any point of the smart contract code.

For example, within the well-known [ERC20](https://en.wikipedia.org/wiki/ERC-20) token standard each token transfer [has to log the Transfer event](https://etherscan.io/tx/0xe7186ec76b164e44212dda60fdace62bef67cf7dc017d2e6318d517daa9b01c9#eventlog), thus letting off-chain applications know that there is a token transfer happened. By “listening” to these events we can perform any (re)actions. For instance, some mobile crypto-wallets send you a push/email notification when tokens are transferred to your address.

In fact, there’s no reliable solution for listening to network events out of the box. Different libraries allow you to track/listen to events, however, there are many cases when something can go wrong, resulting in lost or unprocessed events. To avoid losing events, we have to build a custom back end, which will maintain the events sync process.

Depending on your needs, the implementation can vary. But to put you in a picture here is one of the options of how can you build reliable Ethereum events delivery in terms of microservice architecture:

![Image](https://cdn-media-1.freecodecamp.org/images/1I5pP5C6HTNGeXpSNO1TpQeFDvxRZnDzZDnt)
_Reliable delivery of Ethereum events to all back end services_

These components work in the following way:

1. Events sync back end service constantly polls the network, trying to retrieve new events. Once there are some new events available, it sends these events to the message bus. Upon successful event submission to the message bus, as for blockchain, we can save the last event’s block in order to request new events from this block next time. Keep in mind that retrieving too many events at once may result in always failing requests, so you have to limit the number of events/blocks you request from the network.
2. The message bus (for example, [Rabbit MQ](https://www.rabbitmq.com/)) routes the event to every queue which was set up individually for each back end service. Prior to event publishing, events sync back end service specifies the routing key (for example, a smart contract address + event [topic](https://codeburst.io/deep-dive-into-ethereum-logs-a8d2047c7371)), while consumers (other back end services) create queues which are subscribed for particular events only.

As a result, each back end service gets only those events it needs. Moreover, the message bus guarantees the delivery of all events once they are published to it.

Of course, you can use something else instead of the message bus: HTTP callbacks, sockets, etc. In this case, you’ll need to figure out how to guarantee callbacks delivery yourself: manage exponential/custom callback retries, implement custom monitoring and so on.

#### **Publishing Transactions**

There are a couple of steps we have to perform in order to publish a transaction to the decentralized network:

1. Preparing the transaction. Along with transaction data, this step implies requesting the network state in order to find out whether this transaction is valid and is going to be mined (gas estimation in Ethereum) and the transaction’s sequential number (nonce in Ethereum). Some of the libraries [try to do this under the hood](https://github.com/ethers-io/ethers.js/issues/331), however, these steps are important.
2. Signing the transaction. This step implies the usage of the private key. Most likely, here you’ll want to embed the custom private key assembly solution ([for instance](https://github.com/immutability-io/vault-ethereum)).
3. Publishing and _republishing_ the transaction. One of the key points here is that your published transaction always has a chance to get lost or dropped from the decentralized network. For example, in Ethereum, the published transaction can be dropped if the network’s [gas price](https://ethgasstation.info/) suddenly increases. In this case, you have to republish the transaction. Moreover, you may want to republish the transaction with other parameters (at least with higher gas price) in order to get it mined as soon as possible. Thus, republishing the transaction can imply re-signing it, if the replacement transaction wasn’t pre-signed before (with different parameters).

![Image](https://cdn-media-1.freecodecamp.org/images/ZFZYOVlaW-CDPFpzwutxZTCVdeM4ifLqpsK8)
_The above points regarding Ethereum transaction publishing visualized_

By utilizing the above approaches you can end up building something similar to the thing which is presented in the sequence diagram below. On this particular sequence diagram, I demonstrate (in general!) how the [blockchain recurring billing](https://hackernoon.com/payments-of-tomorrow-decentralized-recurring-billing-47d126d895fd) works (there’s more in a linked article):

1. The user executes a function in a smart contract, which ultimately allows the back end to perform a successful charge transaction.
2. A back end service responsible for a particular task listens to the event of charge allowance and publishes a charge transaction.
3. Once the charge transaction is mined, this back end service responsible for a particular task receives an event from the Ethereum network and performs some logic (including setting the next charge date).

![Image](https://cdn-media-1.freecodecamp.org/images/oNsxhuB9bVacGDh7pJyMjjk25gyipzS70lJg)
_The general sequence diagram of how [blockchain recurring billing](https://hackernoon.com/payments-of-tomorrow-decentralized-recurring-billing-47d126d895fd" rel="noopener" target="_blank" title=") works, demonstrating the interaction between back-end services and Ethereum network_

### Back End Security & Smart Contracts

Transaction publishing always involves using a **private key**. You may be wondering if it is possible to keep private keys secure. Well, yes and no. [There are](https://en.wikipedia.org/wiki/Threshold_cryptosystem) [numerous](https://medium.com/gemini/cold-storage-keys-crypto-how-gemini-keeps-assets-safe-a732addcd13b) [complex](https://www.coinbase.com/security) [strategies](https://github.com/immutability-io/vault-ethereum) and [different types of software](https://www.vaultproject.io/) which allow storing private keys on the back end quite securely. Some private key storage solutions use geo-distributed databases, while others even suggest the use of special hardware. However, in any case, the most vulnerable point of a semi-centralized application is where the private key is assembled and used to sign a transaction (or, in case of special hardware, a point of triggering a transaction signing procedure). Hence, theoretically, there’s no 100% reliable solution which will enable bullet-proof protection from compromising stored private keys.

Now think this way. In many cases, you don’t even need to secure private keys on the back end that often. Instead, **you can design smart contracts and the whole application in such a manner that a private key leak won’t affect their usual behavior**. With this approach, it doesn’t matter how authorized accounts interact with the smart contract. They’re just “triggering” a smart contract to do its usual job, and the smart contract itself performs any required validation. I call it the “operational accounts pattern”.

![Image](https://cdn-media-1.freecodecamp.org/images/Vl3V0DAGGdqi07BnffXkqRsl-0YROdAkgCG6)
_Operational accounts pattern for decentralized applications, where you don’t need military-grade security for your back-end accounts_

This way, in case of emergency:

* The only thing the attacker can steal is a tiny amount of Ether (as of Ethereum) deposited to the operational accounts for transaction publishing
* The attacker won’t be able to harm the smart contract logic nor anyone who is involved in the process
* Compromised operational accounts can be quickly replaced with other ones, however, this requires either the manual replacement (generating new accounts, and reauthorizing accounts in all smart contracts) or developing an additional solution which will do all the magic with a single transaction from a super-secure (hardware or [multi-sig](https://medium.com/@yenthanh/list-of-multisig-wallet-smart-contracts-on-ethereum-3824d528b95e)) master account.

For instance, in our [recurring billing for Ethereum](https://hackernoon.com/payments-of-tomorrow-decentralized-recurring-billing-47d126d895fd) solution, no matter what happens on a back end, the recurring billing smart contract is designed in such a manner that we have a whole month of time for replacing the compromised accounts if any of them are compromised.

But still, if you want to get your back end private key storage as secure as possible, you can try using [Vault](https://www.vaultproject.io/) with a [great plugin for Ethereum](https://github.com/dreamteam-gg) which stores and manages Ethereum accounts (also, keep an eye on our [open-source modules](https://github.com/dreamteam-gg) — we are about to release something similar soon). I am not going to dive deep into the details here, though you can visit the linked projects and learn from there yourself.

This isn’t even all I have to say. However, this article turned out to be much longer than I expected so I have to stop. Subscribe to my [Medium](https://medium.com/@zitro) / [other networks](https://nikita.tk/) if you’re interested in software, crypto, [travel tips](https://instagram.com/nikitaeverywhere/) or just want to follow something interesting. Hope I’ve provided a big valuable piece of information and you’ll find it useful. Feel free to comment and spread this article!

