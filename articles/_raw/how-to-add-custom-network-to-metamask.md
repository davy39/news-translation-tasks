---
title: How to Add a Custom Network to Metamask with JavaScript
subtitle: ''
author: Joshua Omobola
co_authors: []
series: null
date: '2023-01-02T22:17:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-custom-network-to-metamask
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/Frame-1--3--1.png
tags:
- name: dapps
  slug: dapps
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'As a developer, you can enhance the user experience of your decentralized
  applications (DApps) by allowing users to easily add your network to their Metamask
  wallet with just one click.

  This simplifies the process of onboarding users to your applicat...'
---

As a developer, you can enhance the user experience of your decentralized applications (DApps) by allowing users to easily add your network to their Metamask wallet with just one click.

This simplifies the process of onboarding users to your application, since they don't have to manually add the network themselves.

In this article, I'll show you how to use JavaScript to programmatically add custom networks to Metamask. Let's begin!

## Step 1: Check if Metamask is Installed

The first thing you need to do is check if the Metamask plugin is installed in the user's browser. Fortunately, Metamask makes this easy by injecting an `ethereum` object into websites that have it installed.

To check for the presence of Metamask, you can simply try to access the `ethereum` object. You can do this using the following code:

```javascript
if (typeof window.ethereum !== 'undefined') {  
 console.log("Metamask is installed")
} else {
  console.log("Metamask is not installed")
}
```

## Step 2: Add a Custom Network to Metamask

To programmatically add a custom network to Metamask, you can use the `request` method of the `ethereum` object, passing it the `wallet_addEthereumChain` property.

For example, the following code demonstrates how to add the Matic Network (Polygon) to Metamask:

```javascript
window.ethereum.request({
  method: "wallet_addEthereumChain",
  params: [{
    chainId: "0x89",
    rpcUrls: ["https://polygon-rpc.com/"],
    chainName: "Matic Mainnet",
    nativeCurrency: {
      name: "MATIC",
      symbol: "MATIC",
      decimals: 18
    },
    blockExplorerUrls: ["https://polygonscan.com/"]
  }]
});
```

The `window.ethereum.request()` method takes an object as an argument with the method and params properties. The method property should be set to `wallet_addEthereumChain`, and the params property should be an array containing an object with the following properties:

* `chainId`: The chain ID of the custom network which is a 0x-prefixed hexadecimal string.
    
* `rpcUrls`: An array of RPC URLs for the custom network.
    
* `chainName`: The name of the custom network.
    
* `nativeCurrency`: An object with the properties name, symbol, and decimals, representing the name, symbol, and number of decimals of the native currency of the custom network.
    
* `blockExplorerUrls`: An array of block explorer URLs for the custom network.
    

This code will send a request to Metamask to add the Polygon (Matic) Network to the user's wallet. If the request to add the network is successful, `window.ethereum.request()` will return `null`. If not successful, it will return an error.

### Demo

To demonstrate how you can use this code, let's write a simple function that adds the Matic network when called.

```javascript
async function addMaticNetwork() {
  try {
    const result = await window.ethereum.request({
      method: "wallet_addEthereumChain",
      params: [{
        chainId: "0x89",
        rpcUrls: ["https://polygon-rpc.com/"],
        chainName: "Matic Mainnet",
        nativeCurrency: {
          name: "MATIC",
          symbol: "MATIC",
          decimals: 18
        },
        blockExplorerUrls: ["https://polygonscan.com/"]
      }]
    });
  } catch (error){
    console.log(error)
  }
```

The `addMaticNetwork` function, when called, will invoke the request to add the matic network. This function uses the async/await syntax to handle the request asynchronously, and includes a try/catch block to handle any errors that may occur.

**Note:** It's important to note that you should never automatically prompt the user to add a network without their explicit consent. Instead, this request should only be made in response to a direct user action, such as clicking a button.

This ensures that the user is fully aware of the change being made to their wallet and can choose to proceed or cancel the operation as they see fit..

## Wrapping Up

In this article, you have learned how to programmatically add custom networks to MetaMask using JavaScript.

By implementing these steps in your own DApp, you can provide a seamless onboarding experience for your users and improve their overall experience with your application.

I hope this article was helpful. Remember, the world is your code oyster.
