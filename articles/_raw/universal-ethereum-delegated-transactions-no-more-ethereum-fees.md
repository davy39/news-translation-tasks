---
title: 'Universal Ethereum Delegated Transactions: No More Transaction Fees'
subtitle: ''
author: Nikita Savchenko
co_authors: []
series: null
date: '2019-09-30T15:53:22.000Z'
originalURL: https://freecodecamp.org/news/universal-ethereum-delegated-transactions-no-more-ethereum-fees
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/you-need-some-ether-1.png
tags:
- name: Blockchain
  slug: blockchain
- name: crypto
  slug: crypto
- name: Cryptocurrency
  slug: cryptocurrency
- name: Ethereum
  slug: ethereum
- name: ethereum blockchain
  slug: ethereum-blockchain
- name: token economy
  slug: token-economy
- name: Tokenization
  slug: tokenization
seo_title: null
seo_desc: 'TL;DR Check this back end and front end solutions for delegated transactions.
  It is universal for any token which supports the delegation of its functions. Read
  more below.


  This mostly technical article provides a universal framework and a working s...'
---

> TL;DR Check this [back end](https://github.com/ZitRos/ethereum-delegated-tx-service) and [front end](https://zitros.github.io/ethereum-delegated-tx-widget/) solutions for delegated transactions. It is universal for any token which supports the delegation of its functions. Read more below.

This mostly technical article provides a **universal framework** and a **working solution** for Ethereum tokens and applications that eliminates the need to pay fees in Ether, a problem that is practically killing the user experience of many blockchain applications.

> _Imagine spending dollars and then being asked to also hand over some_ [_Hryvnias_](https://en.wikipedia.org/wiki/Ukrainian_hryvnia) _as a transaction fee. That's how Ethereum tokens work so far._

In other words, for example, to transfer any Ethereum token (like [Tether](https://coinmarketcap.com/currencies/tether/), [DAI](https://coinmarketcap.com/currencies/dai/), [BAT](https://coinmarketcap.com/currencies/basic-attention-token/), [DREAM](https://token.dreamteam.gg/), etc.), the user has to also spend some [Ether](http://ethereum.org/use/#_2-what-is-eth-and-how-do-i-get-it) (internal Ethereum platform currency). This introduces a big inconvenience that prevents the mass adoption of DApps: users have to purchase multiple currencies instead of just one to interact with the blockchain network.

# The Problem

Tokens, as we imagine them today are just fuel for applications and services on top of blockchain networks. Organizations create their own tokens (using ICOs, IEOs, etc) and run services/applications that utilize them, introducing their own micro-economy (widely known as a [token economy](https://medium.com/@pentremont/token-economy-101-or-why-blockchain-powered-decentralized-networks-are-important-310de1cc8bac)). But almost every token turns out to be quite a complex currency itself. By design of how blockchain networks work, in order to do something with your tokens, you also need another currency — often Ether (for Ethereum) to be able to transfer tokens.

To illustrate the problem, let's look into how users come to use different blockchain-powered services and applications like:

* [Trickle](https://trickle.gg/) - where you create secure, hourly-based contracts with an untrusted party in any token
* [Loom](https://loomx.io/) - where you use Loom tokens to create sidechains in Loom Network
* [Cryptokitties.co](https://www.cryptokitties.co/) - where you breed, trade and transfer kitties (ERC721 tokens)
* [Others](https://www.stateofthedapps.com/) (there are a lot!)

All these applications use tokens, as well as they require you to purchase Ether. The complexity of using crypto tokens as we know them today is one of the biggest reasons why 99% of crypto startups fail (or avoid adopting real crypto, for example, by replacing it with virtual coins).

As you may already know, the harder it is to use the application, the fewer users it will get right from the beginning. This is something known as [The User Onboarding Funnel](https://www.appcues.com/blog/user-onboarding-funnel-amplitude), which is still a big pain for blockchain-powered applications and services:

![Image](https://lh3.googleusercontent.com/XJyaZoGARI3TF4DOjODJerEUNwn3qFm2D8WSZBrxwYE81oSHaw5h3MOweymV5VV9Jby-2OBUE7o1FGkVqZxWvONW0GLuoezAKqt8HmB-N-vPwHL_ouohPO2whDyS1jiXHLIQv9am)
_The typical user onboarding funnel of a decentralized, blockchain-based application_

To understand why I put 0.001% of users prior to the service use, let's see what exactly purchasing some Ether means:

* Creating a crypto wallet
* Registering on Exchange (and learning all the exchange rules, including country policies!)
* Passing KYC (though it's getting easier, still, many countries have limited access to exchanges)
* Purchasing a minimum allowed amount of Ether (usually, it's [whopping $50](https://changelly.com/widget-settings) while you need just nearly $0.05 to perform one or two transactions)
* Withdrawing Ether to your wallet
* Not to mention reading lengthy guides on how to perform all these steps properly

Instead of just:

* Creating a crypto wallet

Of course, it highly depends on how the application or service is made. But, so far, there was no better simplification of the onboarding flow as just cutting crypto tokens from there, or making them fake, "virtual" currency with deposit and withdrawal function. Unfortunately, the latter approach is now the common one across all startups and companies adopting crypto, for many good reasons. Another reason could be a monetization strategy, but this is another big story worth a dedicated article (Interested? Comment out!).

Getting back to the transaction fees problem, we can state the following, which is hard to argue with.

> _It is natural for the user to purchase **only** the cryptocurrency they really need (for instance, tokens:_ [_Tether_](https://coinmarketcap.com/currencies/tether/)_,_ [_DAI_](https://coinmarketcap.com/currencies/dai/)_,_ [_BAT_](https://coinmarketcap.com/currencies/basic-attention-token/)_,_ [_DREAM_](https://token.dreamteam.gg/)_, etc.), and they would normally expect to pay any transaction fees **in this cryptocurrency**._

So why not just allow them to do so? Because it's quite complex indeed. Let's see why, and how this has just got easier with our open-sourced solution (at least for Ethereum).

# Existing Approaches

From the very beginning of blockchain existence, there were a couple of solutions that could simplify the user onboarding flow to the flow depicted below, avoiding the step of purchasing an intermediate currency like Ether. Still, creating a blockchain wallet is not an easy step, but some users who do understand the value of the application/service go through this step quite well.

![Image](https://lh3.googleusercontent.com/B_D585TaVcYR9qXA-0q3MfvAv1DjGzAulIup0XT1X8Va3eeekX32jAtayKbFCmKoISotoBk_WOyq9jGAdqJzfAnz5q61foOPjgxeVbcfq8bXlA9X25iqzKczy6qmjPvZJgBYsRrL)
_The user onboarding funnel with delegated transactions_

The solution which allows to avoid using intermediate currencies (Ether for Ethereum) is called "delegated transactions", or "meta transactions". 

> _In short, delegated transaction, or "meta transaction" in blockchain is the type of transaction which performs an intended action on one account's behalf, while it is conducted (published) by another account (delegate), who actually pays fees for the transaction._

There are [multiple](https://medium.com/@austin_48503/ethereum-meta-transactions-90ccf0859e84) [approaches](https://fravoll.github.io/solidity-patterns/proxy_delegate.html) [around](https://medium.com/@e2toe4/ethereum-meta-transactions-36f10448619) [the](https://github.com/ethereum/EIPs/issues/1035) [internet](https://github.com/ethereum/EIPs/issues/1228) of the generalized concept of delegated transactions I am presenting in this article. But it seems that none of them are still widely adopted, as these approaches are quite complex by its nature, very specific as for the implementation, as well as some of them are **quite complex to standardize**. To be more constructive, existing approaches can be divided into 3-4 groups: those which use proxy smart contracts, those which embed delegation into a smart contract itself and, theoretically, there is an opportunity for the blockchain-native implementation (say, Ethereum 2.0).

## 1. Delegated transactions approaches which use proxy-contracts

Proxy contracts, or, in this context, identity contracts are tiny contracts deployed to replace the user account which wants to avoid paying fees. This smart contract is programmed to act as a wallet, as well as a "caller" (sender) of other smart contract's functions. The key is that it is a delegate account that triggers all the actions, while the true "owner" of this smart contract is another user. The user just generates correct signatures in order to control their funds stored on a smart contract address (= in their wallet).

![Image](https://lh3.googleusercontent.com/BqoXbK-n6UmpKY-nu8_GuibFbfA3a2Lrghc_fHSoJOzMqv_MYL2BNzIUzyZPgT1aSM00WC0fJoyErLQKc0Dtu3D92NRdYB3Cm4bJ8vZAnbfHVaSe4pCxrEsI8rvEiNCbQriStqfx)
_A visualization of how identity contracts look like_

**Pros of this approach:**

* It works with any tokens and contracts which are already deployed to the network

**Cons of this approach:**

* Users don't see tokens in their wallet, because they are physically on an identity smart contract
* As a result, a need to develop custom UIs and custom tools/wallets
* Identity smart contract deployment and assignment initial fees, as opposed to no fees at all
* Requires a comprehensive standard to be widely adopted

## 2. Semi-delegated transactions via "Operator" pattern ([ERC777](https://eips.ethereum.org/EIPS/eip-777))

There is a token standard that describes this approach — [ERC777](https://eips.ethereum.org/EIPS/eip-777). In short, any token holder can authorize any other account to freely manage their tokens. I won't call it delegated transactions but nevertheless, I need to mention that, as here we somewhat delegate control over your tokens to other accounts.

![Image](https://lh6.googleusercontent.com/Sf3WEbL4fRfefAZLZIBzxD8nAhLnFt75uIZUSO0SjifRwqbiIwSOUnWf4QkN6v6kmWXBazs05bGnG6w1AOTNZIEXwuVUf6GIPdBNtD60mAwiU5r7Oe4MMlNEGLy5htCrk51zsfwi)
_A visualization of ERC777 standard's "operator" pattern_

**Pros of this approach:**

* Standardized

**Cons of this approach:**

* Highly centralized around the "operator" accounts
* Weak security due to operators have 100% control over your tokens
* Initial fees for approval transaction
* Requires additional UIs/tools development

## 3. Delegated transactions embedded directly into a (token) smart contract

Just the same as it is possible to implement custom fees in a proxy smart contract, paying fees in tokens can be implemented directly in a token smart contract. For example, using the approach I described in [my previous article](https://hackernoon.com/you-dont-need-ether-to-transfer-tokens-f3ae373606e1), it is possible to implement a function in a smart contract, which will transfer tokens accepting the user's signature, instead of requiring the user to call this function directly. We have implemented this approach in our [DREAM Token](https://token.dreamteam.gg/), which is used on our [dreamteam.gg](https://dreamteam.gg/) platform.

![Image](https://lh3.googleusercontent.com/NTd44yatekkdfGEOfSDdsXi1S8cmtRdkQLXmUKSIm-nFzMMQdOM1Rox1nML6Y2Z8gYh9t_sMIsPvr7L7AHxTPlYXp0ENnVWQBLf5g85Cue-CiR2zb1Xw4Ym4G407MQOhCUUnSrrQ)
_A visualization of how embedding delegation into the token contract looks like_

As you may notice, in contrast to the previous approach there is no identity contract anymore, and there is an optional way to call other smart contracts directly from the token contract.

**Pros of this approach:**

* Users see their tokens as usual on their wallet's balance
* No initial fees for account initialization
* May not even require a standard (continue reading)

**Cons of this approach:**

* If you have a (token) smart contract that is already deployed to the network, you cannot apply this approach to it directly. While you can always deploy a new token and, for example, a "migration" utility, which will allow other users to swap tokens (burn the old token and mint a new one)
* Because a standard for this approach is yet not well-defined, implementation can drastically vary
* A need to develop custom UI/tools for delegated transactions (continue reading — solved!)

## 4. Delegated transactions on the (blockchain) platform level

This is far the best one of all the described approaches above but also the one **which is not implemented anywhere yet** (by anywhere I mean the most popular blockchain platforms). There is a hope that its support comes with Ethereum 2.0 release, or at least I've heard from Vitalik that they are in progress with something cool there.

Theoretically, we can imagine this approach as being able to make an "offline" signature of two transactions at a time: one which does something useful for the signing account which wants to avoid paying fees (for example, transferring tokens) and another one which does something useful for the delegate (for example, paying fee in tokens to the account which executes these two transactions).

![Image](https://lh5.googleusercontent.com/R1S5_YVazRlh2mfzuMLaKAnix8GmXJy4swBQyxzWFzhIZhE5nDTZ4gfOLp9G51dx-ydW7sLQCsWkic6k_nVj_1CD8JkHjGjRYSMwt17wGSLAG58Vs2ve02KS3L5m5L2oTCMWfxlG)
_A visualization of how platform-native delegated transactions could look like_

But the problem is, regarding Ethereum 2.0, this feature has a chance to land only in 2022 or even later. I also suppose that this feature will still require a dedicated back end (similar to the one which is introduced within this article), as it is hard to imagine how miners will accept fees in tokens. Simply put, if some of them refuse to accept fees in tokens than it makes little sense to do it on a "mining" level at all, not to mention how much would it take to track all token prices and volumes across exchanges, in a decentralized manner.

**Pros of this approach:**

* No need to change smart contracts that were already deployed
* No initial fees for account initialization
* May not even require a custom UI/tools if standardized

**Cons of this approach:**

* Most likely, will still require a centralized back end (the "delegate")
* Not yet implemented on a platform level (as of 2019)

# The Solution

From the four approaches above, except for the platform-level approach which is yet to be implemented and standardized in 2022+, the most appealing one is **the third approach**, where we embed delegated functions directly to the token smart contract. Thus, we save the standard token paradigm allowing wallets to normally work with the smart contract and have no need to wait until delegated transactions will land natively in one of the top blockchain platforms. We will stick to this approach and make it **universal** just below.

Delegated transactions support programmed right in the token smart contract is awesome. But how to deal with its cons? In fact, the only problem which is tough to deal with (as you cannot modify existing smart contracts), **you will need to deploy a new token smart contract if you have already deployed it without delegated functions** (for instance, standard ERC20 or ERC721 tokens). The next step, in this case, would be adding a way to migrate tokens from one smart contract to another. For example, you can decide to implement one more function in the new smart contract that will allow token holders to migrate their assets from the old smart contract.

Token migration function implementation can vary, starting from implementing _receiveApproval_ in the new token, if the previous token supports _approveAndCall_, or ending with utilizing _approve_ + _transferFrom_ framework if you have just a bare minimal ERC20 (the user _approve_s tokens to the new token contract address and then calls a function in the new contract which burns old tokens and mints new ones — but this requires a standard fee for the user for the approval transaction). Actually, there is more: you can decide not to burn old tokens but to "lock" them on a new token smart contract, minting new tokens — this opens an opportunity to implement **two-sided token migration**, which is awesome — **you won't need to list the "new" token on the exchange**, while the users will still be able to send the old token to exchanges without fees in Ether! If you are interested, please fill the issue [here](https://github.com/ZitRos/ethereum-delegated-tx-service/issues) if you want to know more details on how to do it, because this approach is worth a whole new article.

In my [previous article](https://hackernoon.com/you-dont-need-ether-to-transfer-tokens-f3ae373606e1), I provided an example of the token smart contract which supports delegation of such functions like _transfer_, _transferFrom_, _approve_ and _approveAndCall_. Exactly these "delegated" functions allow users to pay fees in tokens, instead of Ether.

![Image](https://lh6.googleusercontent.com/K95psDr4YlNLWPFIByI6HmE5DOz-uIGmD9xfNODmhfj6oRfkIlGJwkZLPYBEVof4MwitQe5Li6SbUNptplVKL2MfERLbVHLJru5jJkTpCVDnDaQbpMd24wtbWOTp81hX7CHtiRtR)
_How delegation works in Ethereum, in short. Read more in [this article](https://hackernoon.com/you-dont-need-ether-to-transfer-tokens-f3ae373606e1)._

But that wasn't enough to start the mass adoption. In this article, I am providing a complete [universal back end solution](https://github.com/ZitRos/ethereum-delegated-tx-service) (Transaction Publisher in the picture above), as well as a [configurable widget](https://github.com/ZitRos/ethereum-delegated-tx-widget) ([check it here](https://zitros.github.io/ethereum-delegated-tx-widget/)), which allows you to replace Ether fees for token fees today.

Some key points before we dive in:

* This delegated transactions back end is made to be universal, or **standard-free**, meaning that you can have **any implementation** of delegated functions and **use any signature standard(s)** in your token. From the back end standpoint, you just need to write a manifest file for your token, describing its usage.
* Currently, converting collected fees in tokens back to Ether is a manual action on exchanges. But it could be a potential improvement for automation in the future (if needed).

# The Concept Behind the Universal Solution

What does it mean that the token supports delegated transactions? Let's look at it using the ERC20 standard token as an example.

## Smart Contract

As for the token smart contract, the approach is quite straightforward. In addition to every method like **transfer(to, value)** which we want to be "delegatable", we add a companion function which, instead of inspecting **msg.sender**, accepts the signature of a user and does the same what the original function meant to do by validating this signature inside the smart contract. Thus, for example, for **transfer(to, value)** function we can add **transferViaSignature(to, value, ...aditionalParams)** function. As you know from [public-key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography), no one can create a valid signature except private key owner, so that's why this approach is as secure as Ethereum itself.

And the coolest part is that the delegated function implementation, as well as its signature doesn't matter much, from the delegate back end standpoint. You can even decide to implement one "call by signature" function for all other functions that the smart contract supports. Delegate back end just need to know **how** to call this function, which is solved by providing an off-chain contract manifest for the delegate back end. For example, the argument _additionalParams_ in **transferViaSignature** can vary and can include anything from this list, if not more: fee, fee recipient address, expiration timestamp, a signature standard used, a signature itself, nonce number or any other unique delegated transaction ID and so on. Regarding the smart contract design, in order to understand why exactly these arguments, read my [previous article](https://hackernoon.com/you-dont-need-ether-to-transfer-tokens-f3ae373606e1).

We also want to allow "delegates" to earn something in order to cover their Ether spending, as well as to be profitable. Thus, we have to add a fee, but a much more natural fee than Ether: a fee in the token itself. So that, for example, if you need to transfer 100 tokens, you pay 3 more tokens to the delegate depending on its price and network conditions to perform a transfer, and this should be preserved in a smart contract logic.

## Back End

All right, now we have a token that allows transferring someone else's tokens by using their signature. Now, the crucial part is to automate the process of requesting and publishing such transactions. And here where our open-sourced [back end](https://github.com/dreamteam-gg/ethereum-delegated-tx-service) (and a [front end](https://github.com/dreamteam-gg/ethereum-delegated-tx-widget)) kicks in.

Below is the sequence diagram describing how front end (client) communicates with the back end from the delegated transaction request to its publishing to the network:

1. (hidden on the diagram) The client requests information from the delegated back end to understand which contracts does it support, as well as which functions can it delegate.
2. The client requests a particular smart contract's function to be delegated. Most importantly, the back end returns the fees it charges and a data to be signed by the client.
3. The client signs the data in their wallet. Signing is a free operation, unlike publishing transaction to the network.
4. The client sends their signature back, thus confirming their intent to perform this particular delegated transaction. The back end validates this transaction against the current network.
5. Finally, the back end publishes a transaction to the network.
6. (hidden on the diagram) The client constantly polls the back end for the delegated request status until it receives a mined status. Note: it is important to poll the back end instead of using a transaction hash to understand when the transaction is mined. It is a very common case when the gas price suddenly increases, and, in order for the transaction to be mined quickly, the back end may republish it with a higher gas price. Though it is currently not implemented, it is very likely to be implemented soon.

![Image](https://lh5.googleusercontent.com/X2SADmcB2aMcJoUgN291XXPdk73sVNi4ebruRwN6TCcDgVWi7ILZs02Mlz0WSR4ufOnzXqxrHIdTSJyijeSKsTw1Z89vB0zjwD8dvQ3Jop6Z4xPKET1TWBnNDBad5QDlD8y0jptG)
_Sequence diagram representing the simplified flow of how delegated transaction is delivered to the network_

This approach is universal, and only requires the manifest file for the back end to understand how to calculate fees and which signature standard to use on the client side. Here is another visualization of the components of the system and their interaction sequence:

![Image](https://lh4.googleusercontent.com/EmfRndRu7BJyU9UTYVGt_rKlQIE83v21s7UywoeTeZQ3Y832Z85KgYRQgmB4o9bqUS7OExMGy2ace6kc3v7QEL-t0bcsvsg9xu9zqLdKDUrzHWXrhHnwoOQWUkd8GBAOWwLww5e8)
_Component diagram_

We've provided a comprehensive [documentation](https://github.com/dreamteam-gg/ethereum-delegated-tx-service#delegated-transactions-concept) for this solution. You can check how the back end [API is structured](https://github.com/dreamteam-gg/ethereum-delegated-tx-service#api), as well as find the token [manifest file](https://github.com/dreamteam-gg/ethereum-delegated-tx-service/blob/master/config/contracts/mainnet/0x82f4ded9cec9b5750fbff5c2185aee35afc16587/manifest.js) which describes how to work with a [particular token contract](https://etherscan.io/address/0x82f4ded9cec9b5750fbff5c2185aee35afc16587#code). We encourage you to contribute your own tokens there!

And you don't need much setup: it's already there with the universal front end!

## Front End

[Open-sourced front end part](https://github.com/dreamteam-gg/ethereum-delegated-tx-widget) of the delegated transactions is the user interface which is **set up for every token**: just run your delegated transactions back end and you are ready to go!

![Image](https://lh4.googleusercontent.com/8TagMGFbuyXbiIEe8_x7cmBycjrAxcpE8zyURXmDIF1cQET-K64NchEmK0lWfNpwR5mzcJIQ5YLp--hLSCksLlMflOAPBbDCf2frPrF4xm6cEZ92GNXH-QDA3MBKpokX4O2tZoUq)
_What [it](https://send-token.dreamteam.gg) looks like_

It is made to be an embeddable widget, which will guide the user through the procedure of sending tokens. You can plug any back end, token or call any token function with it by utilizing [additional URL parameters](https://github.com/dreamteam-gg/ethereum-delegated-tx-widget#embedding) you can specify.

Using this widget, and by implementing something similar to widely used, but not standardized _**approveAndCall**_ function in your token smart contract, you will be able to call other smart contracts with arbitrary data by paying fees in tokens!

Here is a quick guide for you if you want to play with this UI yourself:

1. Access the widget via [this link](https://zitros.github.io/ethereum-delegated-tx-widget/?contractAddress=0xcc7e25e30b065ea61814bec6ecdb17edb0f891aa).
2. It will ask you to switch to the Kovan test network.
3. Get some test Ether using [any available Kovan faucet](https://www.google.com/search?q=ethereum+kovan+faucet).
4. Use test Ether to mint some [test tokens](https://kovan.etherscan.io/address/0xcc7e25e30b065ea61814bec6ecdb17edb0f891aa#writeContract): call [mintTokens](https://kovan.etherscan.io/dapp/0xcc7e25e30b065ea61814bec6ecdb17edb0f891aa#writeContract) function in a token smart contract which will give you 10 test tokens.
5. Now, get back to [the widget](https://zitros.github.io/ethereum-delegated-tx-widget/?contractAddress=0xcc7e25e30b065ea61814bec6ecdb17edb0f891aa) and try to transfer these tokens!

If you open up the browser's developer tools, you may notice that there are a couple of back ends connected by default — they provide the front end with all required information to make a delegated request according to given widget URL parameters. All backends are requested during the widget load and, if any of them can provide a delegation for a particular contract's function, then the widget requests additional information: fees, supported signatures, etc. If there are multiple back ends which can delegate the same contract function, all of them are requested and the back end which provides the best fee will be used for the transaction.

Transaction mining time is seemingly fixed, but it can vary because of the network conditions. The back end uses an actual network fee when calculating the token fee, however, it may change before the user decides to execute the transaction. Thus, the "underpriced" transaction is submitted to the network and can be pending for a while. While the back end is currently not programmed to deal with this case, it might be implemented in future — transactions will be republished with higher gas fees in case of the network fee increases. But, we will also need to count this into the token fee.

## Signature Standards

The last question which you may be wondering is — which signature standard to use for your token. There are several available: _eth_sign_ (deprecated), _eth_personalSign_ (note that old [Trezor](https://trezor.io/) and [Ledger](https://www.ledger.com/) produce a different signatures because of ambiguity in a standard, so you may want to include both), _eth_signTypedData_ (deprecated), [_eth_signTypedData_v3_](https://medium.com/metamask/eip712-is-coming-what-to-expect-and-how-to-use-it-bb92fd1a7a26) and so on. I would recommend supporting at least two: ageless _eth_personalSign_ and new [_eth_signTypedData_v3_](https://medium.com/metamask/eip712-is-coming-what-to-expect-and-how-to-use-it-bb92fd1a7a26) (as of 2019).

![Image](https://lh3.googleusercontent.com/TZhSpdfJF_035M1uCARZVYixZC4W8hsiG1jbs2zTyYZQC5fpwJUR3W7x14WaLofyklmEaR9O4Cgt7EkKb7MCb1RHK6geJfxKb-oGVVxlOXBOu6dh5c6nRtNwblF5B0sZ07Gf6mV7)
_Signature standards comparison — what the user sees_

The front end is programmed to always prefer the user-readable standard like [eth_signTypedData_v3](https://medium.com/metamask/eip712-is-coming-what-to-expect-and-how-to-use-it-bb92fd1a7a26) to any others eth_personalSign. So if your token supports many signature standards, and you added all of them to the [manifest file](https://github.com/dreamteam-gg/ethereum-delegated-tx-service/blob/master/config/contracts/mainnet/0x82f4ded9cec9b5750fbff5c2185aee35afc16587/manifest.js) of your token, it will display [eth_signTypedData_v3](https://medium.com/metamask/eip712-is-coming-what-to-expect-and-how-to-use-it-bb92fd1a7a26) prompt first.

# Conclusion

Delegated transactions are great: they solve one of the biggest problems of blockchain application adoption, which eases the mass adoption of crypto overall. I will put a couple of thesis in a Q&A format here for you to answer the last questions that you may still have after reading this article:

* Our open-source solution is free to use and production-ready, feel free to apply it to your applications or tokens!
* The described approach does not compromise security nor centralization. Think this way: the centralized back end is only a helper for someone who wants to transfer tokens without fee in Ether. If the back end is hacked, or it is just unavailable, there's no problem to interact with the network just as it was before, by paying fees in Ether. As well as the back end cannot harm or trick the user to steal their tokens when a proper signature standard is used (it's up to your token implementation).
* There is a way to support delegated transactions for existing, already-deployed tokens. However, it requires the additional Ether-consuming step to migrate existing tokens to a new token contract. And, by programming a new token contract properly, as well as designing your application to work with both tokens you can even avoid a need to list a new token on exchanges.
* By using the [existing tokens as an example](https://github.com/zitros/ethereum-delegated-tx-service/blob/master/config/contracts/mainnet/0x82f4ded9cec9b5750fbff5c2185aee35afc16587/manifest.js), which is available in delegated transactions [back end](https://github.com/zitros/ethereum-delegated-tx-service) and [front end](https://github.com/zitros/ethereum-delegated-tx-widget) repositories, you can produce your own manifest for your own token.
* [Read the instructions](https://github.com/zitros/ethereum-delegated-tx-service#setup) on how to set up your own back end for a token, and then add it to the URL of your widget (or commit to the open-source repository).
* Have a token which already supports delegated transactions? Plug it into [our UI](https://zitros.github.io/ethereum-delegated-tx-widget) with these three quite simple steps: (1) create a manifest for your token and put your token abi file while setting up the delegate back end, (2) run this back end, exposing a public API URL and (3) use URL parameters in a widget to reference your back end or commit it directly to our open-source repository. Read more about it in GitHub's readme file.

I hope that was a really helpful piece of information for all the searchers of incredible. Feel free to contact [me](https://nikita.tk/) or fill the issue [here](https://github.com/ZitRos/ethereum-delegated-tx-service/issues) if I missed something. Have fun, let the token economy be simple!

