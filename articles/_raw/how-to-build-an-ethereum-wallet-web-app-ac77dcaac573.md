---
title: How to build an Ethereum Wallet web app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T16:27:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-ethereum-wallet-web-app-ac77dcaac573
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TzOKAf_ykKIz8qC0VrJHGA.png
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Paul Laux

  A review of the coolest parts of eth-hot-wallet

  This article is a technical review of the interesting parts of eth-hot-wallet, an
  Ethereum wallet web app with erc20 token native support. The source code can be
  found on GitHub (MIT Licens...'
---

By Paul Laux

#### A review of the coolest parts of eth-hot-wallet

This article is a technical review of the interesting parts of **eth-hot-wallet**, an [Ethereum wallet](http://eth-hot-wallet.com) web app with erc20 token native support. The source code can be found on [GitHub](https://github.com/PaulLaux/eth-hot-wallet) (MIT License).

![Image](https://cdn-media-1.freecodecamp.org/images/1*6wrsZ2k5DdEHIpS8u-4p1A.png)
_eth-hot-wallet preview_

**Table of contents:**

* Ethereum wallet as a web app
* The stack
* The containers of eth-hot-wallet
* Unified Design for Ethereum Wallet
* Redux and Redux-Saga
* _Secure_ password generator
* eth-lightwallet and SignerProvider
* Encrypted offline storage
* Sending Ethereum using Web3.js
* Sending erc20 tokens using Web3.js
* Subscribing to Ethereum transaction life-cycle using Web3.js V1 and Redux-Saga channels
* Polling Ethereum blockchain and price data using Redux-Saga
* Keeping an eye on the bundle size
* Conclusion

### Ethereum wallet as a web app

When software is deployed as a web app, wide accessibility is the first thing that comes to mind. After all, the web is the most widely accessible cross device platform. Eth-hot-wallet is a PWA (progressive web app) that can be used from any modern web-browser.

Moreover, [recent improvements in PWA support](https://medium.com/appscope/designing-native-like-progressive-web-apps-for-ios-1b3cdda1d0e8) significantly improve the user experience on mobile.

Pros:

* No additional software is required
* No installation of any kind is necessary
* Ability to use modern web development tools.
* Easy to deploy and to upgrade

Cons:

* More prone to phishing attacks.
* Browser plugins might inject malicious code into the page.
* High loading time on slow internet connections
* Limited access to device storage

The fact that malicious browser extensions might inject JavaScript code in an attempt to extract the keys is significant. To migrate this risk, the user should be encouraged to turn off extensions (i.e. by using in incognito mode) or integrate the web with an external web3 provider such as MetaMask or Trust browser. Converting the web app into a desktop app is also a viable option.

As for phishing, the user should be encouraged to bookmark the page and access it via google search. It is highly unlikely for a phishing site to rank above the real site in search results.

**Bottom line: a web app will allow you to reach the widest audience with minimum friction**. In my opinion, the web is the best target platform for new apps.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TzOKAf_ykKIz8qC0VrJHGA.png)
_eth-hot-wallet logo_

### The stack

Most of the code is dedicated to the **front-end:**

The final package consists of many packages as can be seen in [package.json](https://github.com/PaulLaux/eth-hot-wallet/blob/master/package.json).

Top level components include:

* [Eth-lightwallet](https://github.com/ConsenSys/eth-lightwallet) — Lightweight JS Wallet for Node and the browser for keystore management
* React, Redux, saga.js, immutableJS and reselect wrapped by the offline-first [react-boilerplate](https://github.com/react-boilerplate/react-boilerplate)
* [Ant design](https://github.com/ant-design/ant-design) — excellent set of UI components for react
* [Webpack](https://webpack.github.io/) — A bundler for JavaScript and friends.

And for the **back-end:**

The final bundle is deployed directly to GitHub pages from a dedicated branch in the repository. There is no need for a back-end in the traditional scene.

To create the Testnet Ethereum faucet, we’ll use a [Serverless framework](https://serverless.com/framework/docs/getting-started/). It significantly improves the developer experience when using AWS Lambda. It is a very cost-effective solution that obliterates the need to maintain infrastructure, especially on low volume applications.

### The containers of eth-hot-wallet

![Image](https://cdn-media-1.freecodecamp.org/images/1*ufHAtmbsMCMSNwGKX63Zjg.png)
_eth-hot-wallet homepage container_

When using the combination of React, Redux, Saga.js and Reselect, each container (may) consist of the following ingredients:

* index.js — for rendering the GUI
* actions.js
* reducer.js
* saga.js
* selectors.js
* constants.js

As [Dan Abramov](https://www.freecodecamp.org/news/how-to-build-an-ethereum-wallet-web-app-ac77dcaac573/undefined) stated, there is [more than one approach](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0) for whether to use a component or a container. From my experience, if a component has more then ~8 attributes inside the application state, it should be separated into a new container. This is just a rule of thumb. The number of attributes may bloat over time. With complex components, it’s better to have a unique container than to cluster the state of the main Container.

Not every container needs to have all the ingredients. In eth-hot-wallet, the `[sendToken](https://github.com/PaulLaux/eth-hot-wallet/tree/master/app/containers/SendToken)`[container](https://github.com/PaulLaux/eth-hot-wallet/tree/master/app/containers/SendToken) does not use its own Saga.js. We separated it so as not to burden the state of the homepage component.

#### The Homepage container

![Image](https://cdn-media-1.freecodecamp.org/images/1*eqJKGRGa7YpBigSGKBYBQw.jpeg)
_eth-hot-wallet homepage container_

The primary container, where most of the action takes place, is the [homepage container](https://github.com/PaulLaux/eth-hot-wallet/tree/master/app/containers/HomePage). In the homepage container, Saga.js is responsible for dealing with side effects. Besides GUI, its main responsibility will be dealing with **keystore operations**.

The ETH-Lightwallet package provides the keystore. All related operations including keys, seeds, encryption, importing, exporting are done in this section.

#### The Header container

[The header](https://github.com/PaulLaux/eth-hot-wallet/tree/master/app/containers/Header) demonstrates the fact that a container is much more than just a GUI component:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ckDt0s8GbB2YeynBss4Qug.jpeg)
_eth-hot-wallet header container_

This container might look simple at first with only a logo and a network selector. Does it even need to be in its own container? The answer is that in eth-hot-wallet **every network communication-related action and state management is done inside the header container**. More than enough for any container.

#### The SendToken container

[SendToken](https://github.com/PaulLaux/eth-hot-wallet/tree/master/app/containers/SendToken) is a modal that appears while the user selects to send Ether/ tokens.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DFy9RyZievPsl3gyCTYC4A.png)
_eth-hot-wallet SendToken container_

The modal includes some basic input verification, like amount and Ethereum address check. It does not use Saga.js to initiate side effects, but instead uses actions provided by the homepage and header containers.

**We separated it into a new container to reduce clustering the state of the homepage container.**

#### TokenChooser container

[Token Chooser](https://github.com/PaulLaux/eth-hot-wallet/tree/master/app/containers/TokenChooser) appears when the user wants to select what token the wallet will manage.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XY_vFMJBjz_HFka9SpTZGA.png)
_eth-hot-wallet TokenChooser container_

The `TokenChooser` name was selected in order not to be confused with the term “selector” which appears many times through the wallet code in a different context ([reduxjs/reselect: Selector library for Redux](https://github.com/reduxjs/reselect)).

Same as with the `SendToken` container, `TokenChooser` does not use its own Saga.js file but calls actions from the homepage container when needed.

### A Unified design for Ethereum Wallet

Since the appearance of the ERC20 standard ([EIP20](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20-token-standard.md)), it was obvious that tokens were going to be an important part of the Ethereum ecosystem. The Ethereum wallet was designed with a unified design approach in mind. **Ether and token should be treated equally from the user’s perspective.**

Under the hood, the API for sending Ether and sending tokens is quite different. So is checking the balance, but they will appear the same on the GUI.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2IKgDyCw0ogdCKZhWsx2_w.png)
_[A Unified design for Ethereum Wallet](https://eth-hot-wallet.com" rel="noopener" target="_blank" title=")_

To send Ether, we need to use native functions provided by the web3.js library, while sending tokens and checking balances involves interaction with a smart contract. More on this issue later.

### Redux and Redux-Saga

Using Redux store as a single source of truth greatly benefits the wallet. GUI actions and user-triggered flows can be relatively easily managed by actions and reducers provided by Redux.

Aside from keeping the UI state, the Redux store also holds the key-store object (a partially encrypted JavaScript object supplied by eth-lightwallet). This makes the keystore accessible throughout the app by using a selector.

[Redux-Saga](https://github.com/redux-saga/redux-saga) is what makes the entire setup shine.

> `redux-saga` is a library that aims to make application side effects (i.e., asynchronous things like data fetching and impure things like accessing the browser cache) easier to manage, more efficient to execute, easy to test, and better at handling failures.

Saga.js uses Generators to make **asynchronous flows easy to read and write**. By doing so, these asynchronous flows look like your standard synchronous JavaScript code (kind of like `async`/`await` but with more customization options).

In the case of Ethereum wallet, by using Saga we get a comfortable way to handle asynchronous actions such as rest API calls, keystore actions, Ethereum blockchain calls via web3.js, and more. All the requests are cleanly managed in one place, no callback hell, and very intuitive API.

**Example usage for redux-saga:**

### _Secure_ password generator

![Image](https://cdn-media-1.freecodecamp.org/images/1*IkEbKHk8GAENsl9M3pGuog.png)
_A seed and a secure password is auto-generated for the user_

To adequately secure the user’s keystore, we need to encrypt it with a strong password. When using eth-lightwallet, the password needs to be provided during the initiation of the [hd-wallet](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&cad=rja&uact=8&ved=2ahUKEwiV_JvMw4_dAhWMDcAKHfGpANYQFjACegQICBAB&url=https%3A%2F%2Fethereum.stackexchange.com%2Fquestions%2F33395%2Fwhat-is-a-hd-wallet-for-ether-and-how-to-create-one-using-nodejs%3Frq%3D1&usg=AOvVaw2P31H_vW_U9Dc8tZHEcrNA).

Let’s assume that we have a function called `generateString`, which can provide genuinely random strings at any length.

If the user wants to generate a new wallet, we will produce the following parameters:

We can ask the user to confirm the password and the seed or generate a new set on its behalf. Alternatively, we can ask the user for their own existing seed and password.

`generateString` implementation: We will use the relatively new [**window.crypto API**](https://developer.mozilla.org/en-US/docs/Web/API/Window/crypto) to get random values (currently [supported by all major browsers](https://caniuse.com/#feat=getrandomvalues)).

[Eth-hot-wallet implementation](https://github.com/PaulLaux/eth-hot-wallet/blob/master/app/utils/crypto.js) is based on the following code to generate **random but human-readable strings**:

After the user has accepted the password and the seed, we can use the values and generate the new wallet.

### eth-lightwallet and SignerProvider

1. LightWallet is intended to be a signing provider for the [Hooked Web3 provider](https://github.com/ConsenSys/hooked-web3-provider).
2. Hooked Web3 provider has been deprecated, and currently the author recommends the package [ethjs-provider-signer](https://github.com/ethjs/ethjs-provider-signer/) as an alternative.
3. At the moment of writing, there is a bug in ethjs-provider-signer that prevents the display of error messages. The bug was fixed but didn’t merge back into the main branch. Those error messages are critical for this setup to function correctly.

**Bottom line**: Use eth-lightwallet with this version of ethjs-provider-signer: [https://github.com/ethjs/ethjs-provider-signer/pull/3](https://github.com/ethjs/ethjs-provider-signer/pull/3) to save time on trial and error.

### **Encrypted offline storage**

The lightwallet keystore vault JSON object is encrypted, and it requires from us an external `passwordProvider` to safely keep the encryption key. The keystrore object is always encrypted. The app is responsible for safekeeping the password and provides it with any action.

eth-hot-wallet uses [Store.js](https://github.com/marcuswestin/store.js) — _Cross-browser storage for all use cases, used across the web_. Store.js allows us to store the encrypted keystore easily and extract it back from storage when the webpage is accessed.

When the wallet is loaded for the first time, it will check if there is a keystore in local storage and will auto load it to Redux state if so.

At this point, we can read the public data of the keystore but not the keys. To display public data before the user enters the encryption password, we need an additional operation mode: **loaded and locked.** In this mode, the wallet will display the addresses and fetch the balances but will not be able to perform operations such as sending transactions or even generating new addresses. Triggering any of those actions will prompt for the user’s password.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QICvgsfhKmpOSVMMgWbo4A.png)
_locked wallet after loading from local storage_

### Sending Ethereum using Web3.js

When using Web3.js@0.2.x, the function `sendTransaction` is provided in the following form:

`web3.eth.sendTransaction(transactionObject [, callback])`

The callback will return the TX as a result in case of success.

However, to properly integrate it into our saga.js flow, we need to wrap `[sendTransaction](https://github.com/PaulLaux/eth-hot-wallet/blob/master/app/containers/Header/saga.js#L203)` [function with a promise](https://github.com/PaulLaux/eth-hot-wallet/blob/master/app/containers/Header/saga.js#L203):

This way we continue regular Saga.js execution after `sendTransaction` is called.

### Sending erc20 tokens using Web3.js

The Ethereum blockchain does not provide primitives that encapsulate token functionality, nor should it. Every token deployed on Ethereum is, in fact, a program that corresponds to the [**eip20 specification**](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md). Since the Ethereum virtual machine (EVM) is Turing complete (with some restrictions), every token might have a different implementation (even for the same functionality). What unifies all those programs under the term “token” is that they provide the same API as defined by the specification.

**When we are sending a token on Ethereum, we are interacting with a smart contract.** To communicate with a smart contract we need to know its API, the format for sharing contract’s API called [Ethereum Contract ABI](https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI).

We will store the [erc20 ABI](https://github.com/PaulLaux/eth-hot-wallet/blob/master/app/utils/contracts/abi.js) as part of our JavaScript bundle and instantiate a contract during the program run-time:

`const erc20Contract = web3.eth.contract(erc20Abi);`

After contract setup, we can easily interact with it programmatically using the [Web3.js contract API](https://github.com/ethereum/wiki/wiki/JavaScript-API#web3ethcontract).

For each token we will need a dedicated contract instance:

`const tokenContract = erc20Contract.at(tokenContractAddress);`

After the creation of contract instance, we can access the contract functions by calling the desired function straight from JavaScript:

See [Web3.js contract API](https://github.com/ethereum/wiki/wiki/JavaScript-API#web3ethcontract) for the full details.

We will promisify the `tokenContract.transfer.sendTransaction` to use it with our redux-saga flow:

It is possible to use [es6-promisify](https://github.com/digitaldesignlabs/es6-promisify) or similar instead of writing the promise directly, but I prefer the direct approach in this case.

### Subscribing to Ethereum transaction life-cycle using Web3.js V1 and redux-saga channels

_eth-hot-wallet uses web3.js v0.2.x and does not support this feature at the moment_. _The example is provided by another project. It is an important feature and should be used extensively._

The new version of Web3.js (V1.0.0) is shipped with a [new contract API](https://web3js.readthedocs.io/en/1.0/web3-eth-contract.html#methods-mymethod-send) that can inform us about transaction life-cycle changes.

Enter the `PromiEvent`: A [promise combined event emitter](https://web3js.readthedocs.io/en/1.0/callbacks-promises-events.html#promievent).

```
web3.eth.sendTransaction({...}).once('transactionHash', function(hash){ ... }).once('receipt', function(receipt){ ... }).on('confirmation', function(number, receipt){ ... }).on('error', function(error){ ... }).then(function(receipt){    //fired once the receipt is mined});
```

`web3.eth.sendTransaction()` will return an object (a promise) that will resolve once the transaction is mined. The same object will allow us to subscribe to `‘transactionHash’`, `‘receipt’`, `‘confirmation’` and `‘error’` events.

**This API is far more informative and elegant than the one provided with 0.2.x version of Web3.js**. We will see how we can integrate it into our web app with the help of [Saga.js channels](https://redux-saga.js.org/docs/advanced/Channels.html). The motivation is to update the application state (Redux store) once a change to the transaction state is detected.

In the following example, we will create a ‘commit’ transaction to an arbitrary smart contract and update app state when we get `‘transactionHash’`, `‘receipt’` and `‘error’` events.

We need to initialize the new channel and fork a handler:

The handler will catch all channel events and will call the appropriate Redux action creator.

Once the channel and the handler are both ready and the user initiates the transaction, we need to register to the generated events:

In fact, we don't need a new channel for each transaction and can **use the same channel for all types of transactions.**

[The full source code of this example](https://github.com/Monetary-Foundation/PreDistribution-DApp/blob/1003631ad6a7ca53e6ed02772f6fec6a36b7628c/app/containers/Dashboard/saga.js#L412) can be found here.

### Polling Ethereum blockchain and price data using redux-saga

There are several ways to watch for blockchain changes. It is possible to use Web3.js to [subscribe to events](https://web3js.readthedocs.io/en/1.0/web3-eth-subscribe.html) or we can poll the blockchain by ourselves and have more control over some aspects of polling.

In eth-hot-wallet, the wallet is polling the blockchain periodically for balance changes and [Coinmarketcap API](https://api.coinmarketcap.com/v1/ticker/?convert=EUR) for price changes.

This redux-saga pattern will allow us to poll any data source or API:

After the `CHECK_BALANCES` action is seen by the default saga, the `checkAllBalances` function is called. It can end with one of two possible outcomes: `CHECK_BALANCES_SUCCESS` or `CHECK_BALANCES_ERROR` . Each one of them will be caught by `watchPollData()` to wait X seconds and call `checkAllBalance` again. This routine will continue until `STOP_POLL_BALANCES` is caught by `watchPollData` . After that, it is possible to resume the polling by submitting `CHECK_BALANCES` action again.

### Keeping an eye on the bundle size

When building web apps using JavaScript and npm, it might be tempting to add new packages without analyzing the footprint increase. Eth-hot-wallet uses [webpack-monitor](http://webpackmonitor.com/) to display a chart of all the dependencies and **the differences between each build**. It allows the developer to see the bundle size change clearly after each new package is added.

![Image](https://cdn-media-1.freecodecamp.org/images/1*x_Mis7ppLuj5_Q_ifDCOZQ.jpeg)
_webpack-monitor example chart_

Webpack monitor also can help in finding the most demanding dependencies and might even surprise the developer by **highlighting the dependencies that do little for the app but contribute a lot to the bundle size.**

Webpack-monitor is easy to integrate and is definitely worth including in any webpack based web app.

### Conclusion

The issues presented in this article are only part of the challenges that need to be solved when building an Ethereum wallet. However, overcoming those issues will create a solid foundation and will allow us to continue and create a successful wallet.

Building a wallet can also be a great introduction to the world of Ethereum since most [distributed applications](https://github.com/ethereum/wiki/wiki/Decentralized-apps-(dapps)) (DApps) require a similar set of capabilities both from the front-end and blockchain perspective.

[**ETH Hot Wallet - Ethereum Wallet with ERC20 support**](https://eth-hot-wallet.com)  
[_ETH Hot wallet is an Ethereum wallet with ERC20 Support. The keys are generated inside the browser and never sent…_eth-hot-wallet.com](https://eth-hot-wallet.com)

In case you have any questions regarding eth-hot-wallet or any related subject, feel free to contact me via [Twitter](https://twitter.com/dr_laux) or open an [issue on GitHub](https://github.com/PaulLaux/eth-hot-wallet).

