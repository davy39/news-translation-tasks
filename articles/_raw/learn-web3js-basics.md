---
title: Learn Web3.js Basics – Ethereum Development for Beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-11-27T22:39:24.000Z'
originalURL: https://freecodecamp.org/news/learn-web3js-basics
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Learn-Web3.js-Basics---Ethereum-Development.png
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: Web3
  slug: web3
seo_title: null
seo_desc: "By Oluwatise Okuwobi\nEthereum is one of the major pioneers in the decentralized\
  \ ecosystem. And Web3.js is an essential tool if you're working on Ethereum-based\
  \ projects. \nTo fully understand why this tool is important, we must first take\
  \ a deeper div..."
---

By Oluwatise Okuwobi

Ethereum is one of the major pioneers in the decentralized ecosystem. And Web3.js is an essential tool if you're working on Ethereum-based projects. 

To fully understand why this tool is important, we must first take a deeper dive into Ethereum development.

Grab your coffee, young Web3 enthusiast. We're going on a journey that will change your Web3 career forever.

## Prerequisites

Before you can carry on with this tutorial, you'll need to understand the basics of JavaScript, and should be able to install npm packages. 

If you've worked with JavaScript before, the rest of this tutorial should be a breeze. 

## What is Ethereum Development?

Ethereum is a decentralized open-source blockchain platform that lets developers build decentralized applications, popularly known as dAPPs. These dApps are built on top of the Ethereum blockchain, harnessing some of the core features of the Ethereum network. 

Ethereum is written in Solidity, which is the primary programming language used in the Ethereum ecosystem. You can use Solidity to design smart contracts, which are basically self-executing contracts that power a lot of dApps.

If you want to work in Ethereum development, understanding smart contracts is extremely important. 

Smart contracts consist of the terms of the agreement between buyer and seller that are directly written into the lines of code. This code is written in Solidity, which can only exist in the blockchain network.

To become an Ethereum developer, you are going to work mainly around the network, building smart contracts and dApps. 

Let's talk about the tools you are going to need:

* Solidity
* Ether.js
* JavaScript/React for front-end visual interaction

## The World of Web3.js

Now that you have an idea of what Ethereum development is, we can begin to understand Web3.js a little better. 

Web3.js is a collection of libraries that allow you to interact with a local or remote Ethereum node, using HTTP, IPC, or Web Sockets (which is my personal favorite). It is written in JavaScript, and to put it simply, it lets you interact with the blockchain more efficiently.

By reading data from the blockchain, you will be able to make transactions and deploy smart contracts live on the mainnet.

## How to Set Up Web3.js

Web3.js can access blockchain information from both the back end and front end to make transactions and deploy smart contracts. 

You are going to need Node.js, which you can easily [download from the official website](https://nodejs.org/en/). The installation process is pretty straightforward. 

After you've successfully installed Node and npm (the official package manager for Node), open your command line in the root folder of your project and type the following command:

```javascript
npm install web3 --save
```

Then you'll be able to import Web3.js into a Node script using this simple code:

```javascript
const Web3 = require("web3")
```

We've got some of the hard part locked down. Now we just need our project to communicate directly with the blockchain. 

To initiate our Web3 provider, we must instantiate, which just means creating a Web3 instance, and pass a constructor to the URL of the provider. 

In this case, we'll have to find an Ethereum node that we can connect to and start crafting magic. 

There are multiple node providers like Alchemy, Chainstack, and Moralis, and there's a lot of documentation when it comes to getting a direct access.

You can make use of the Ganache instance as well, which will essentially help you set up the environment for anything you need to work in your local environment.

To understand [how to set up Ganache](https://medium.com/coinmonks/get-started-with-building-ethereum-dapps-and-smart-contracts-d86b9f7bd1c), you can read the linked guide that covers everything you need to know.

You simply place this below your code like so:

```javascript
const Web3 = require("web3")
const web3 = new Web3("http://localhost:8545")
```

To test that you have successfully configured everything, you can write some simple code to get the latest block number on the blockchain:

```javascript
var Web3 = require("web3")
const web3 = new Web3("http://localhost:8545"")

web3.eth.getBlockNumber(function (error, result) {
  console.log(result)
})

```

This function simply accepts a callback as a parameter, then prints the result as an integer. Running this would just give you a block number on your console. 

There are many other functions you can use. The web3 [official documentation](https://docs.web3js.org/) provides a comprehensive list of functions that you can learn about and try out.

## Conclusion

If you're wanting to get into Ethereum development, Web3.js will be a vital part of your stack. Throughout your journey, you are going to be interacting with the Ethereum node more frequently and Web3.js will come in handy.

There are other alternatives like Ether.js, which also strive to provide a complete library that can interact with the Ethereum node. But Web3 is known to have a larger network of support, a larger community of developers, and more mature documentation that you can refer to regarding problems of any sort.

Hopefully this article has given all of the insights you need for you to start your Ethereum journey. I'm available on [Twitter](https://www.twitter.com/tiseysoft), if you have any questions.


