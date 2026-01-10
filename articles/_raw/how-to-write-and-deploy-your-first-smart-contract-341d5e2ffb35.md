---
title: How to write and deploy your first smart contract
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-18T00:58:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-and-deploy-your-first-smart-contract-341d5e2ffb35
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZnxSoYqZH9IOH3G5WUposA.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: General Programming
  slug: programming
- name: Smart Contracts
  slug: smart-contracts
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Avadhoot Kulkarni

  Ever since Ethereum graced the crypto space with its presence in mid-2015, the revolutionary
  invention by Canadian-Russian Programmer Vitalik Buterin has given birth to many
  new decentralised applications (dApps). Along with the ...'
---

By Avadhoot Kulkarni

Ever since [Ethereum](https://ethereum.org) graced the crypto space with its presence in mid-2015, the revolutionary invention by Canadian-Russian Programmer Vitalik Buterin has given birth to many new decentralised applications (dApps). Along with the myriad of dApps being built, Ethereum’s success is mainly attributed to its implementation of smart contracts.

Interestingly enough, the invention of smart contracts dates back to 1996. Computer scientist Nick Szabo drew up the term “smart contracts,” and explains them as follows:

> “I call these new contracts “smart”, because they are far more functional than their inanimate paper-based ancestors. No use of artificial intelligence is implied. A smart contract is a set of promises, specified in digital form, including protocols within which the parties perform on these promises”  
>   
> — [Nick Szabo](http://www.fon.hum.uva.nl/rob/Courses/InformationInSpeech/CDROM/Literature/LOTwinterschool2006/szabo.best.vwh.net/smart_contracts_2.html), 1996

His work later went on to inspire many other researchers and scientists, including Vitalik, who created Ethereum.

### Basic info

Before we delve further into the guide, it is important to understand two important concepts.

The first thing that we need to understand is what the Ethereum Virtual Machine (**EVM**) is. Its sole purpose is to act as a runtime environment for smart contracts based on Ethereum. Think of it as a global super computer that runs all the smart contracts. As the name suggests, the EVM is virtual and not a physical machine. You can [read more about the EVM here](https://themerkle.com/what-is-the-ethereum-virtual-machine/).

The second concept we need to understand is what is **gas**_._ In the EVM, gas is a unit of measurement used to assign a fee to each transaction with a smart contract. Each computation that happens in the EVM requires gas. The more complex and tedious it is, the more gas is needed to execute the smart contract.

Every transaction specifies the gas price it is willing to pay in ether for each unit of gas, allowing the market to decide the relationship between the price of ether and the cost of computing operations (as measured in gas). It’s the combination of the two, total gas used multiplied by gas price paid, that results in the total fee paid by a transaction.

```
Fee for transaction = Total gas used * gas price;
```

Read more about gas [here](https://ethereum.stackexchange.com/questions/3/what-is-meant-by-the-term-gas).

Now that you have basic knowledge about what a smart contract is and how the smart contract runs, we can go straight into how we are going to make our very own smart contract!

### Setting up

We’re going to use a tool for this: Pragma. It’s an easy-to-use platform for creating and deploying smart contracts. [Sign up here](https://www.withpragma.com/) and go the editor:

![Image](https://cdn-media-1.freecodecamp.org/images/1*eyY1_mE0Kw250gdZ0B0AOg.jpeg)

Log in to Metamask. If you haven’t installed MetaMask yet, [you can start here](https://help.indorse.io/hc/en-us/articles/360001815251-Using-MetaMask-on-Indorse).

Switch to the Kovan test network both in Pragma and MetaMask.  
Just to give you a brief overview about testnets, check out [this article](https://karl.tech/intro-guide-to-ethereum-testnets/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*X-yIFMaU0inr5_32wo6d9w.jpeg)

The Ethereum mainnet is the official Ethereum network. It is more secure, and uses Ether, which has real monetary value.

Testnets are playground Ethereum networks in which the Ether is agreed to have no monetary value. Developers use these playgrounds to test applications before deploying them to the mainnet for their users.

To switch between these networks, click on the network name next to the MetaMask icon and select the network. For this tutorial, please choose **Kovan**.

### Writing the smart contract

The following contract will implement the simplest form of a cryptocurrency. It is possible to generate coins out of thin air, but only the person that created the contract is able to do that (it is trivial to implement a different issuance scheme). Furthermore, anyone can send coins to each other without needing to register with a username and password. All you need is an Ethereum keypair.

```
pragma solidity ^0.4.21; //tells that the source code is written for Solidity version 0.4.21 or anything newer that does not break functionality


contract yourToken {
    // The keyword "public" makes those variables readable from outside.
    
    address public minter;
    
    // Events allow light clients to react on changes efficiently.
    mapping (address => uint) public balances;
    
    // This is the constructor whose code is run only when the contract is created
    event Sent(address from, address to, uint amount);
    
    function yourToken() public {
        
        minter = msg.sender;
        
    }
    
    function mint(address receiver, uint amount) public {
        
        if(msg.sender != minter) return;
        balances[receiver]+=amount;
        
    }
    
    function send(address receiver, uint amount) public {
        if(balances[msg.sender] < amount) return;
        balances[msg.sender]-=amount;
        balances[receiver]+=amount;
        emit Sent(msg.sender, receiver, amount);
        
    }
    
    
}
```

This code basically lets you mint and send tokens to other accounts.

Let’s go through it line by line:

```
pragma solidity ^0.4.21;
```

This indicates that the source code is written for Solidity version 0.4.21 or anything newer that does not break functionality. This is to ensure that the code doesn’t behave differently with the new compiler versions.

```
contract yourToken
```

Everything related to yourToken goes inside this contract. Essentially, a contract in solidity is the collection of functions and state (code and data) sitting at an address on the Ethereum blockchain.

```
address public minter;
```

This is the address of the minter. The keyword “public” makes those variables readable from outside.

```
event Sent(address from, address to, uint amount);
```

Events allow light clients (UI) to react to the changes efficiently.

```
function yourToken() public {
  minter = msg.sender;
}

```

Let’s set your Ethereum address as minter of the contract. You’ll need to access the contract through your MetaMask to be able to mint. We’ll go through this again after deploying the contract.

```
function mint(address receiver, uint amount) public {
  if(msg.sender != minter) return;
  balances[receiver]+=amount;
}

```

This function lets you mint the amount of coins you want to. You can mint as many tokens as you want to. The if condition tells the system to stop executing if you’re not the minter, which is set in yourToken function.

If you are in fact the minter, it lets you mint the tokens.

```
function send(address receiver, uint amount) public {
  if(balances[msg.sender] < amount) return;
  balances[msg.sender]-=amount;
  balances[receiver]+=amount;
  emit Sent(msg.sender, receiver, amount);
}
```

This is a function that lets one address send the tokens to another address. It takes two parameters: receiver and amount. It reduces the amount from the sender’s address and adds the same amount to receiver’s address. Event Sent, which we declared earlier, is now used to do the transfer. Currently, we have kept the sender as msg.sender, which is the minter, as we do not want to complicate the contract.

That’s it. Your contract is now ready, so let’s compile it.

### Compiling and deploying the smart contract

![Image](https://cdn-media-1.freecodecamp.org/images/1*FAUfzAPntHXqVNR5rpy3Yw.jpeg)

Once the contract is compiled, let’s deploy it on the blockchain. As mentioned earlier, we’ll use Kovan testnet to deploy the contract.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5OA2_s3vB2LP21UBkjaNSg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ne5LsQuTlRr3sl5iFqB1Ng.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*G0PBdUtSixgVxrxIJNOG9g.jpeg)

Check if the smart contract is deployed.

For the contract I deployed for this tutorial, [this is the transaction](https://kovan.etherscan.io/tx/0x96a3b24fedd12e79a6e16adf0dd05970e0a011510f302fdadc9d1559ad90a8fc). You can also see it in Pragma under your contracts.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Vtsp6UMTFbCgJAs8mGzrwg.jpeg)

### Interact with the smart contract in Pragma

![Image](https://cdn-media-1.freecodecamp.org/images/1*Vtsp6UMTFbCgJAs8mGzrwg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Py8LRkKzZblALzT_hCHI3g.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*NVpHZwOZN0-8lzwpW1tm5A.jpeg)
_Let’s mint 1000000 tokens!_

![Image](https://cdn-media-1.freecodecamp.org/images/1*QJRNPSNpnvYa9LX02WB-6g.jpeg)
_Signing the transaction_

![Image](https://cdn-media-1.freecodecamp.org/images/1*pEs1g4LSvT9ufNv_ki9Big.jpeg)
_Yay!_

There you have it. Your first smart contract, deployed on blockchain. :)

A lot of new concepts were introduced along with a couple of amazingly helpful tools. It might be a little overwhelming, and that’s okay! Just try to get your head around the concepts and then run with it.

Have you created any simple but interesting smart contracts? Post them in the comments and I’ll add them in the post for reference.

Have questions? Add them in the comments or join our telegram group and [talk to us directly](https://t.me/indorseio).

