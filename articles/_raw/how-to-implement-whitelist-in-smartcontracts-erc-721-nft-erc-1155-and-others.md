---
title: How to Implement a Whitelist in Smart Contracts (ERC-721 NFT, ERC-1155, and others)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-12T14:12:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-whitelist-in-smartcontracts-erc-721-nft-erc-1155-and-others
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/whitelist-1.jpg
tags:
- name: Blockchain
  slug: blockchain
- name: digital-signature
  slug: digital-signature
- name: merkle tree
  slug: merkle-tree
- name: Smart Contracts
  slug: smart-contracts
- name: whitelist
  slug: whitelist
seo_title: null
seo_desc: 'By Igor Gaponov

  In this article I will show you three ways you can create a whitelist in a smart
  contract.

  Here''s what we''ll discuss:


  On-chain whitelists

  Digital signatures

  Merkle trees


  All methods are available in the repo here.

  A whitelist is use...'
---

By Igor Gaponov

In this article I will show you three ways you can create a whitelist in a smart contract.

Here's what we'll discuss:

* On-chain whitelists
* Digital signatures
* Merkle trees

All methods are available in the [repo here](https://github.com/gapon2401/smartcontract-whitelist).

A whitelist is useful if you want to restrict access to a certain function or want to grant privileges to a certain group of users. 

To compare these methods, I'm going to use very minimalistic smart contracts to reduce the unnecessary spending of gas. 

Let's dive into it.

## How to Create an On-Chain Whitelist

The main idea is to store all whitelist addresses in the smart contract.

Take a look at this schema:

![On-chain whitelist](https://www.freecodecamp.org/news/content/images/2022/10/Untitled--3-.png)
_On-chain whitelist_

When user calls the smart contract function, it checks if the address is in the whitelist. If it is, the function executes. 

If you want to add or remove addresses from the whitelist, you can do it in the smart contract with additional `external` functions.

Pros:

* easy to implement
* all addresses are stored in the smart contract and only the owner can edit them

Cons: 

* it's the most expensive method
* you have to spend gas to add and remove the addresses

Here's what the smart contract looks like:

```js
contract OnChainWhitelistContract is Ownable {

    mapping(address => bool) public whitelist;

    /**
     * @notice Add to whitelist
     */
    function addToWhitelist(address[] calldata toAddAddresses) 
    external onlyOwner
    {
        for (uint i = 0; i < toAddAddresses.length; i++) {
            whitelist[toAddAddresses[i]] = true;
        }
    }

    /**
     * @notice Remove from whitelist
     */
    function removeFromWhitelist(address[] calldata toRemoveAddresses)
    external onlyOwner
    {
        for (uint i = 0; i < toRemoveAddresses.length; i++) {
            delete whitelist[toRemoveAddresses[i]];
        }
    }

    /**
     * @notice Function with whitelist
     */
    function whitelistFunc() external
    {
        require(whitelist[msg.sender], "NOT_IN_WHITELIST");

        // Do some useful stuff
    }
}
```

All addresses will be stored in the `whitelist` variable.

The function `addToWhitelist` allows the owner to add an array of addresses. Keep in mind that each address in the list will spend about 22904 gas units. To call that function costs 23994 gas units.

The function `removeFromWhitelist` allows you to remove addresses from the whitelist.

And the function `whitelistFunc` checks if the address belongs to the whitelist.

Gas spending:

![Gas spending for on-chain whitelist](https://www.freecodecamp.org/news/content/images/2022/10/on-chain-gas.jpg)
_Gas spending for on-chain whitelist_

## How to Create a Digital Signature Whitelist

The main idea is to create signatures for addresses and check them inside the smart contract.

![Digital signature whitelist](https://www.freecodecamp.org/news/content/images/2022/10/Digital-signature-1.png)
_Digital signature whitelist_

You store the whitelist on your server. Before making a call to the smart contract, you should check if the address is in the whitelist or not. If yes, create a signature for the address and pass that signature to the smart contract. Inside the smart contract you have to validate that signature.

Pros:

* No gas for adding or removing addresses from the whitelist.
* No need to interact with the smart contract about the whitelist

Cons:

* Whitelist is located in a database that can be compromised. If the audience trusts the owner of the project, then this is not a problem
* The most expensive price for contract deployment and whitelist validating

Here's the smart contract:

```js
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.14;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

contract DigitalSignatureWhitelistContract is Ownable {

    using ECDSA for bytes32;

    /**
     * @notice Used to validate whitelist addresses
               Replace this wallet address to your own!
     */
    address private signerAddress = 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266;

    /**
     * @notice Verify signature
     */
    function verifyAddressSigner(bytes memory signature) private 
    view returns (bool) {
        bytes32 messageHash = keccak256(abi.encodePacked(msg.sender));
        return signerAddress == messageHash.toEthSignedMessageHash().recover(signature);
    }
    
     /**
     * @notice Function with whitelist
     */
    function whitelistFunc(bytes memory signature) external
    {
        require(verifyAddressSigner(signature), "SIGNATURE_VALIDATION_FAILED");

        // Do some useful stuff
    }
}

```

### How to implement a digital signature

First, you'll need to create a new wallet address. It will be signer address.

ATTENTION: Do not send any funds to that wallet. It will be used only for making signatures.

Let's assume, that the signer wallet address is `0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266`

Specify it in the smart contract here:

```js
address private signerAddress = 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266;
```

In the root of your web project, create a `.env` file with private key of that wallet:

```
SIGNER_PRIVATE_KEY=0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80
```

Specify only your own public and private keys, because these are publicly known.

Next, create the whitelist database. It can be PostgreSQL, MySQL, MongoDB – any one you want. You can easily add or remove addresses.

Then when it's time to interact with the smart contract, the user clicks a button on your website. You send the request to your server with the user's address.

If the user is in the whitelist, create the signature for the address on your server:

```js
import { ethers } from 'ethers'

export default async function handler() {
    
  // Whitelist array from you database
  const whitelist = [
    '0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC',
    '0x90F79bf6EB2c4f870365E785982E1f101E93b906',
    '0x15d34AAf54267DB7D7c367839AAf71A00a2C6A65',
    '0x9965507D1a55bcC2695C58ba16FB37d819B0A4dc',
    '0x976EA74026E726554dB657fA54763abd0C3a0aa9',
  ]

  // This variable will contain the signature we need
  let signature = ''
  
  // Parse params passed to server and get user wallet address
  const userWalletAddress = ''

  if (whitelist.includes(userWalletAddress)) {
    const signer = new ethers.Wallet(process.env.SIGNER_PRIVATE_KEY!)
    const addressHash = ethers.utils.solidityKeccak256(['address'], [userWalletAddress.toLowerCase()])
    const messageBytes = ethers.utils.arrayify(addressHash)
    signature = await signer.signMessage(messageBytes)
  }

  // Return signature to web
}
```

Then pass the signature to the smart contract function, where `verifyAddressSigner` will validate it according to the sender's address. 

Gas spending:

![Gas spending for digital signature whitelist](https://www.freecodecamp.org/news/content/images/2022/10/digital-signature-gas.jpg)
_Gas spending for digital signature whitelist_

## How to Create a Merkle Tree Whitelist

What is the Merkle tree?

> Merkle tree is a tree in which every "leaf" (node) is labelled with the cryptographic hash of a data block, and every node that is not a leaf (called a branch, inner node, or inode) is labelled with the cryptographic hash of the labels of its child nodes. – [Source](https://en.wikipedia.org/wiki/Merkle_tree)

How does it connect to the whitelist problem?

We will use it to hash all addresses into one root hash.

![Merkle tree](https://www.freecodecamp.org/news/content/images/2022/10/Merkle-tree-structure.png)
_Merkle tree_

This is the schema of work:

![Merkle tree whitelist](https://www.freecodecamp.org/news/content/images/2022/10/Merkle-tree-1.png)
_Merkle tree whitelist_

Like in the digital signature method, you need a database for the whitelisted addresses. When you are ready to start the sale or something else, you need to create the Merkle root hash and save it in the smart contract. This hash will validate all the addresses.

When the user wants to make a request to the smart contract, you need to create a Merkle proof for him, based on the Merkle tree of all addresses. Then you need to send proof to the smart contract. You can store the tree locally. 

After editing the whitelist you should update the Merkle root hash and rewrite it to the smart contract. You should also update the local Merkle tree. 

Pros:

* Deployment of the smart contract is much cheaper than the digital signature method
* Validating addresses in the smart contract is also cheaper
* No gas for adding or removing addresses from whitelist, until you start a sale

Cons:

* After the sale has started, it will be complicated to change the whitelist. You will need to update the smart contract and Merkle tree each time. Therefore, gas will be spent.
* You need to know how to create a Merkle root and update the smart contact. It's impossible to change the whitelist without interacting with the smart contract.

Here's the smart contract:

```js
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.14;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract MerkleTreeWhitelistContract is Ownable {

    /**
     * @notice Merkle root hash for whitelist addresses
     */
    bytes32 public merkleRoot = 0x09485889b804a49c9e383c7966a2c480ab28a13a8345c4ebe0886a7478c0b73d;

    /**
     * @notice Change merkle root hash
     */
    function setMerkleRoot(bytes32 merkleRootHash) external onlyOwner
    {
        merkleRoot = merkleRootHash;
    }

    /**
     * @notice Verify merkle proof of the address
     */
    function verifyAddress(bytes32[] calldata _merkleProof) private 
    view returns (bool) {
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        return MerkleProof.verify(_merkleProof, merkleRoot, leaf);
    }

    /**
     * @notice Function with whitelist
     */
    function whitelistFunc(bytes32[] calldata _merkleProof) external
    {
        require(verifyAddress(_merkleProof), "INVALID_PROOF");

        // Do some useful stuff
    }
}

```

### How to implement a Merkle tree on the web

First, create the whitelist database. It can be PostgreSQL, MySQL, MongoDB or any other you want. You can easily add or remove addresses.

When it's time to interact with the smart contract, create a Merkle root hash:

```js
import { ethers } from 'ethers'
import { MerkleTree } from 'merkletreejs'

// Your whitelist from database
const whitelist = [
  '0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC',
  '0x90F79bf6EB2c4f870365E785982E1f101E93b906',
  '0x15d34AAf54267DB7D7c367839AAf71A00a2C6A65',
  '0x9965507D1a55bcC2695C58ba16FB37d819B0A4dc',
  '0x976EA74026E726554dB657fA54763abd0C3a0aa9',
]

const { keccak256 } = ethers.utils
let leaves = whitelist.map((addr) => keccak256(addr))
const merkleTree = new MerkleTree(leaves, keccak256, { sortPairs: true })

// Save this value to smartcontract
const merkleRootHash = merkleTree.getHexRoot()
// 0x09485889b804a49c9e383c7966a2c480ab28a13a8345c4ebe0886a7478c0b73d
```

 Then save the Merkle root hash in the smart contract. 

Specify it before the deployment:

```js
bytes32 public merkleRoot = 0x09485889b804a49c9e383c7966a2c480ab28a13a8345c4ebe0886a7478c0b73d;
```

Or use a function `setMerkleRoot` for it:

```js
function setMerkleRoot(bytes32 merkleRootHash) external onlyOwner
{
    merkleRoot = merkleRootHash;
}
```

When the user clicks a button on your website, you send the request to your server with the user's address. If the user is in the whitelist, create the Merkle proof on your server:

```js
import { ethers } from 'ethers'
import { MerkleTree } from 'merkletreejs'

export default async function handler() {
    
  // Whitelist array from you database
  const whitelist = [
    '0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC',
    '0x90F79bf6EB2c4f870365E785982E1f101E93b906',
    '0x15d34AAf54267DB7D7c367839AAf71A00a2C6A65',
    '0x9965507D1a55bcC2695C58ba16FB37d819B0A4dc',
    '0x976EA74026E726554dB657fA54763abd0C3a0aa9',
  ]

  // This variable will contain the signature we need
  let proof = []

  // Parse params passed to server and get user wallet address
  const userWalletAddress = ''

  if (whitelist.includes(userWalletAddress)) {
    const { keccak256 } = ethers.utils
    let leaves = whitelist.map((addr) => keccak256(addr))
    const merkleTree = new MerkleTree(leaves, keccak256, { sortPairs: true })
    let hashedAddress = keccak256(userWalletAddress)
    proof = merkleTree.getHexProof(hashedAddress)
  }

  // Return proof to web
}

```

Then pass proof to the smart contract function, where `verifyAddress` will validate it according to the sender's address. 

Gas spending:

![Gas spending for Merkle tree whitelist](https://www.freecodecamp.org/news/content/images/2022/10/merkle-tree-gas.jpg)
_Gas spending for Merkle tree whitelist_

## Summary

Below you will find a comparison table of the gas units these different methods spend:


| Property                      | On-chain | Digital signature | Merkle tree |
|-------------------------------|----------|-------------------|-------------|
| Deployment                    | 329 724  | 486 182           | 352 790     |
| Add to whitelist 1 address    | 46 898   | 0                 | 28 986      |
| Add to whitelist 10 addresses | 253 010  | 0                 | 28 986      |
| Remove from whitelist         | 24 930   | 0                 | 28 986      |
| Call function with whitelist  | 23 443   | 29 365            | 26 065      |

Long story short:

* An on-chain whitelist easy to implement, but expensive to use. I would not recommend using it.
* A digital signature whitelist is a universal tool that does not require additional interactions with the smart contract. You can easily edit the whitelist at any time. But you have to pay for versatility. Deployment and function with the whitelist are the most expensive. If your addresses change frequently, then use digital signature. 
* Merkle tree is the best option if your whitelist addresses will not change after you start presale or whatever you want. For example, it costs nothing to collect addresses and edit them in your database. When the sale starts, you stop editing the whitelist, create the root hash, save it to the smart contract and that's it. In that case the Merkle tree is better than digital signature. 

 What exactly to use is up to you!

Finally, I want to show you how to calculate gas price.

### How to calculate gas price

Use the following formula:

```
(gas units) * (gas price per unit) = gas fee in gwei
```

Use [https://ethgasstation.info/](https://ethgasstation.info/) or any other website to find gas price per unit. At the moment of writing this article, gas price is 22.

![Gas price per unit](https://www.freecodecamp.org/news/content/images/2022/10/gas-price.jpg)
_Gas price per unit_

The value can change depending on the time of day.

Let's calculate how much it will cost to deploy a digital signature smart contract.

```js
Deployment = 486 182 * 22 = 10 696 004 gwei = 0,010696004 ETH
```

Now since the ETH/USD price is $1,324, it means that deployment to the Mainnet will cost about $14.

Maybe you want to convert the comparison table to USD?  
 `Gas price per unit` = 22, `ETH` = $1,324


| Property                      | On-chain | Digital signature | Merkle tree |
|-------------------------------|----------|-------------------|-------------|
| Deployment                    | $9.6     | $14.16            | $10.28      |
| Add to whitelist 1 address    | $1.37    | 0                 | $0.84       |
| Add to whitelist 10 addresses | $7.37    | 0                 | $0.84       |
| Remove from whitelist         | $0.73    | 0                 | $0.84       |
| Call function with whitelist  | $0.68    | $0.86             | $0.76       |



Thank you for reading! ❤

