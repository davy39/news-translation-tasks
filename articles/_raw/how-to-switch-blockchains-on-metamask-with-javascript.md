---
title: How to Switch Blockchains on MetaMask with JavaScript
subtitle: ''
author: Joshua Omobola
co_authors: []
series: null
date: '2023-01-26T23:15:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-switch-blockchains-on-metamask-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Custom-Network--1-.jpg
tags:
- name: Blockchain
  slug: blockchain
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'With over 10,000 blockchains currently operating, there are endless possibilities
  for deploying your smart contracts.

  For anybody to be able to use your Decentralized Application (DApp), they need to
  be connected to the blockchain where you''ve deploy...'
---

With over 10,000 blockchains currently operating, there are endless possibilities for deploying your smart contracts.

For anybody to be able to use your Decentralized Application (DApp), they need to be connected to the blockchain where you've deployed your smart contract.

This article will show you how to prompt your users to switch to your preferred blockchain using JavaScript.

This guide requires that you have the MetaMask extension installed. Also, I assume you have a little bit of experience connecting with MetaMask—perhaps you've previously built a DApp. If you need a quick intro, [check out this brilliant piece by MetaMask to get started](https://docs.metamask.io/guide/create-dapp.html#basic-action-part-1).

Alright, Let’s dig in!

## Step 1 — Check if the User Has MetaMask Installed

The first thing to do is to verify if the user has installed the MetaMask extension.

If they have another wallet installed besides MetaMask, switching networks using the method we are about to learn might not work. So it's a good idea to check first.

Let's check if the `ethereum` context has been injected into the browser. The code sample below shows how to do this:

```javascript
const { ethereum } = window;

if (typeof ethereum !== 'undefined' && ethereum.isMetaMask) {  
 console.log("MetaMask is installed")
} else {
  console.log("MetaMask is not installed")
}
```

Here's what we're doing:

At `const { ethereum } = window;` we destructure the `ethereum` property from the windows object and assign it to a variable of the same name.

If you are unfamiliar with this syntax, destructuring involves simply extracting the content of an object or array and assigning it to a variable. [Read up on this piece to learn more about destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment).

Then we check if `ethereum` actually does exist using the if statement. Also, in the same condition we want to verify if the wallet installed is MetaMask.

Good! Let's see the next step.

## Step 2 — How to Switch the Active Blockchain

Once we have verified that the user has MetaMask installed, the next thing to do is trigger the RPC method for switching the MetaMask active blockchain. The code looks like this:

```javascript
// MetaMask Docs
try {
  await ethereum.request({
    method: 'wallet_switchEthereumChain',
    params: [{ chainId: '0xf00' }],
  });
} catch (switchError) {
// This error code indicates that the chain has not been added to MetaMask.
  if (switchError.code === 4902) {
  	// Do something
  }
}
```

Here's what we are doing:

We invoke the `ethereum.request` method, passing it an object with two properties.

In the method property, we specify the `wallet_switchEthereumChain` RPC method, which allows Ethereum applications (DApps) to request that MetaMask switches its active Ethereum chain.

Then, the params property is an array that takes an object with the chain ID of the blockchain to switch to. `chainId` must be hexadecimal, hence the 0x in the sample code.

We wrap our request in a try/catch block to handle errors.

`null` is returned if the active chain is switched.

If the requested chain does not exist in the user's wallet, the request throws an error code `error.code` of `4902`. If this happens, you can request to add the chain to the wallet.

You can follow this guide to see [how to add a new chain to MetaMask using JavaScript.](https://www.freecodecamp.org/news/how-to-add-custom-network-to-metamask/)

Great! That's all it takes to switch the active chain on MetaMask with Javascript.

Let's have a quick demo in the next section.

## Demo

For this example, let's write a function that, when invoked, will prompt users to switch to the Polygon chain.

```javascript
const SwitchChainToPolygon = () => {
	const { ethereum } = window;
    if (typeof ethereum !== 'undefined' && ethereum.isMetaMask) return;
    
    try {
      await ethereum.request({
        method: 'wallet_switchEthereumChain',
        params: [{ chainId: '0x89' }],
      });
    } catch (switchError) {
      if (switchError.code === 4902) {
        // You can make a request to add the chain to wallet here
        console.log('Polygon Chain hasn't been added to the wallet!')
      }
    }
}
```

In the function `SwitchChainToPolygon` above, we destructured `ethereum` from the windows object, as we learned in Step 1.

Next, we verified whether `ethereum` does exist or not. If the `ethereum` is unavailable, that is if MetaMask is not installed, the function will exit/break.

If `ethereum` exists, we call the `ethereum.request` method to make an RPC call. For the `method` property, we give it a value of `wallet_switchEthereumChain`. For the `params`, `chainId` will have the value of `0x89` ( `167` in decimal) which is the chainId for the polygon blockchain.

That's all folks!

## Conclusion

In this article, you have learned how to switch blockchains on MetaMask with JavaScript. This will help you provide a frictionless user experience for your users.

Thank you for taking the time to read this. I hope you found it useful. Please feel free to connect and chat with me on [Twitter](https://twitter.com/kohawithstuff) and [YouTube](https://youtube.com/@kohawithstuff). See you soon in my next article!
