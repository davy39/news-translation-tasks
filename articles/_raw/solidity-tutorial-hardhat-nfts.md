---
title: Solidity Tutorial – How to Create NFTs with Hardhat
subtitle: ''
author: Taisuke Mino
co_authors: []
series: null
date: '2021-05-17T14:39:55.000Z'
originalURL: https://freecodecamp.org/news/solidity-tutorial-hardhat-nfts
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/hardhat_nft-1.png
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: NFT
  slug: nft
- name: Smart Contracts
  slug: smart-contracts
- name: Solidity
  slug: solidity
seo_title: null
seo_desc: "I'm a developer who's mostly been writing JavaScript, so the Solidity development\
  \ environment was a bit hard to learn. \nAbout four months ago, I switched to Hardhat\
  \ from Truffle. This cool new kid on the block drastically improved my coding experienc..."
---

I'm a developer who's mostly been writing JavaScript, so the Solidity development environment was a bit hard to learn. 

About four months ago, I switched to [Hardhat](https://hardhat.org/) from Truffle. This cool new kid on the block drastically improved my coding experience. So today I want to share it with my fellow Solidity developers.

In this post, I will walk you through the initial set-up, compilation, testing, debugging, and finally deployment.

At the end of this post, you will be able understand how to deploy an NFT contract to the local network with Hardhat. 

The goal of this post is to make you familiar with Hardhat. I won’t talk about how to write a test or Solidity syntax. However, you should be able to follow along without any Solidity knowledge if you know how to write JavaScript.

See [this repo](https://github.com/taisukemino/hardhat-nft-tutorial) for the code.

## How to Set Up the Project

Let’s start an npm project first:

```
npm init --yes

```

Then install the Hardhat package:

```
npm install --save-dev hardhat

```

Cool! Now you are ready to create a new Hardhat project:

```
npx hardhat

```

Choose `Create an empty hardhat.config.js`:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-1.png)

This will create `hardhat.config.js` in your root directory with the solidity compiler version specified:

```js
/**
 * @type import('Hardhat/config').HardhatUserConfig
 */
module.exports = {
  solidity: "0.7.3",
};

```

## How to Write and Compile the Contract

All right, we will start writing a simple contract and then we'll compile it.

Make a new Solidity file within a new `contracts` directory:

```
 mkdir contracts && cd contracts && touch MyCryptoLions.sol

```

We'll use the open-zeppelin package to write our NFT contract. So first, install the open-zeppelin package:

```
npm install --save-dev @openzeppelin/contracts

```

Here is the contract code we will be compiling:

```solidity
pragma solidity ^0.7.3;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract MyCryptoLions is ERC721 {
    constructor(string memory name, string memory symbol)
        ERC721(name, symbol)
    {}
}

```

The first thing you need to do in any solidity file is to declare the compiler version. Then we can import the ERC721 contract (NFT contract) from open-zeppelin just like you do in JavaScript.

Solidity is a contract-oriented language. Just like an object-oriented language, contracts can have members such as functions and variables. In our code, we have only the constructor, which will be called when we deploy our contract.

Our contract inherits the ERC721 and then passes the `name` and `symbol` arguments which are going to be passed to the ERC721 contract. They literally decide the name and symbol of your NFT token.

We will pass whatever values we want to `name` and `symbol` at the point of deployment.

To compile it, run:

```
npx hardhat compile

```

You might get some warnings but we'll ignore them to keep things simple. You should see `Compilation finished successfully` at the bottom.

You should also notice that the `/arfifacts` and `/cache` directories were generated. You don’t have to worry about them for this post, but it’s good to keep in mind that you can use `abi` in the artifacts if you want to interact with the contract when you build the frontend.

## How to Test the Contract

Since smart contracts are mostly financial applications – and they're also hard to change – testing is critical.

We will use some packages for testing. Install with the command below:

```
npm install --save-dev @nomiclabs/hardhat-waffle ethereum-waffle chai @nomiclabs/hardhat-ethers ethers

```

`ethereum-waffle` is a testing framework for smart contracts. `chai` is an assertion library. We'll write tests in waffle using Mocha alongside Chai. `ethers.js` is a JavaScript SDK for interacting with the Ethereum blockchain. The other two packages are plugins for Hardhat.

Now, let’s make a new directory `test` in the root directory and make a new file called `test.js` in it:

```
mkdir test && cd test && touch test.js

```

Make sure you require `@nomiclabs/hardhat-ethers` in the `hardhat.config.js` to make it available everywhere:

```
require("@nomiclabs/hardhat-ethers");

```

Here is a simple test:

```js
const { expect } = require("chai");

describe("MyCryptoLions", function () {
  it("Should return the right name and symbol", async function () {
    const MyCryptoLions = await hre.ethers.getContractFactory("MyCryptoLions");
    const myCryptoLions = await MyCryptoLions.deploy("MyCryptoLions", "MCL");

    await myCryptoLions.deployed();
    expect(await myCryptoLions.name()).to.equal("MyCryptoLions");
    expect(await myCryptoLions.symbol()).to.equal("MCL");
  });
});

```

This code deploys our contract to the local Hardhat network and then checks if the `name` and `symbol` values are what we expect.

Run the test:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-2.png)

Awesome, it passed the test!

### How to Use console.log() in Hardhat

Now here is the coolest thing you can do with Hardhat. You can use `console.log()` just like you do in JavaScript, which was not possible before. `console.log()` alone is more than enough reason to switch to Hardhat. 

Let’s go back to your solidity file and use `console.log()`.

```
pragma solidity ^0.7.3;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "hardhat/console.sol";

contract MyCryptoLions is ERC721 {
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        console.log("name", name);
        console.log("symbol", symbol);
        console.log("msg.sender", msg.sender); //msg.sender is the address that initially deploys a contract
    }
}

```

And run the test again with `npx hardhat test`. Then the command will compile the contract again, and then run the test. You should be able to see some values logged from the contract.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-3.png)

This makes debugging a lot easier for you.

One caveat is that it supports only these data types:

* uint
* string
* bool
* address

But other than that, you can use it as if you are writing JavaScript.

## How to Deploy the Contract

All right! Now let’s deploy our contract. We can deploy our contract to one of the testing networks, the Mainnet, or even a mirrored version of the Mainnet in local. 

But in this post, we will deploy to the local in-memory instance of the Hardhat Network to keep things simple. This network is run on startup by default.

Make a new directory called `scripts` in the root directory and `deploy.js` in it.

```
mkdir scripts && cd scripts && touch deploy.js

```

Here is the deploy script. You deploy along with constructor values:

```js
async function main() {
  const MyCryptoLions = await hre.ethers.getContractFactory("MyCryptoLions");
  const myCryptoLions = await MyCryptoLions.deploy("MyCryptoLions", "MCL");

  await myCryptoLions.deployed();

  console.log("MyCryptoLions deployed to:", myCryptoLions.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });

```

You might want to remove `console.log()` before you deploy. And then run this deploy script with:

```
npx hardhat run scripts/deploy.js
MyCryptoLions deployed to: 0x5FbDB2315678afecb367f032d93F642f64180aa3

```

Boom! Now your NFT contract is deployed to the local network. 

You can target any network configured in the `hardhat.config.js` depending on your needs. You can find more about configuration [here](https://hardhat.org/config/).

## Wrapping Up

Hardhat has some other cool features like helpful stack trace, support for multiple Solidity compiler versions, a robust Mainnet forking, great TypeScript support and contract verification in Etherescan. But that’s for another time!

