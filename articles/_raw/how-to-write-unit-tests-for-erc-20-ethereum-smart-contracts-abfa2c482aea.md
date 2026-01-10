---
title: How to write Unit tests for ERC-20 Ethereum Smart Contracts
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-29T14:22:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-unit-tests-for-erc-20-ethereum-smart-contracts-abfa2c482aea
coverImage: https://cdn-media-1.freecodecamp.org/images/1*b8-UrpS2ct361i2QWAVeRw.jpeg
tags: []
seo_title: null
seo_desc: 'By Il Kadyrov

  It’s very important to write unit tests for your smart contracts, same as for any
  development project. However, unit testing in blockchain-based solutions is often
  underestimated and overlooked.

  Last year I performed more than 200 audit...'
---

By Il Kadyrov

It’s very important to write unit tests for your smart contracts, same as for any development project. However, unit testing in blockchain-based solutions is often underestimated and overlooked.

Last year I performed more than 200 audits of smart contracts written mostly for Ethereum, and also for Neo, Eos, Tron and Bitcoin blockchains.

From what I observed, nearly half of these projects didn’t write unit tests. Such oversight often resulted in poor contract performance and various security issues identified during the audit.

#### Must-have tests

![Image](https://cdn-media-1.freecodecamp.org/images/1*8fQ1Akp_3eABKt_w9t_emQ.png)

Each smart contract has common parts such as

* a constructor
* total supply
* functions for transfer to and from
* functions for approval
* and sometimes function for burning extra tokens

So it’s important to check your smart contract for correct initialization of all the parameters, and for reverts when you overflow or underflow total supply or other _uint_ values. Also, you need to check modifiers and proper rights usage.

In this article, I’ll focus specifically on Ethereum smart contracts, but this also applies to other platforms as contracts have the same structure across other crypto currencies. First, let’s test the proper initialization of token and its correct transfer to some address.

#### Checking Initialization

Tests for correct initialization are simple. You just need to create a sample contract and check for correctness of all values that must be initialized.

#### Checking Transfers

Checking the **_transfer_** function is very important, because there may be issues that would cause incorrect transfers. You must make sure that recipient’s and sender’s balances change upon transfer, try to get reverts in case the function gets wrong parameters.

For example,

* when the amount being sent exceeds the sender’s balance
* when the contract address or invalid address is sent instead of recipient address, etc.

And finally, you must check that the _transfer_ event is **logged**.

The **_transferFrom_** function is very similar to transfer, but here you also need to test that the spender has enough approved balance for sending.

Here are the tests when the spender has insufficient funds required for a transfer.

#### Checking Approvals

The **approve** function is the simplest function from the ERC20 standard. There is no need to check for zero address. It’s enough to check that the allowance array is correctly filled. Also if you don’t have increaseApproval or decreaseApproval functions, approve will overwrite all previous values.

So it is recommend to use these functions as protection from unnecessary overwrites. And of course, it’s important to check that you get correct logs from the Approval event.

#### Burning Unsold Tokens

Most smart contracts include a function for **burning** tokens left after the main sale. Lots of them have a special token holder account, sometimes it’s the owner account. So the best solution for burning unsold tokens is the following:

* get amount of tokens on holder’s address
* then subtract this amount from total supply
* and set amount of tokens on holder’s address to zero.

This will ensure that you don’t burn all the tokens, so it’s important to lay out your token burn strategy in your white paper.

#### Conclusion

It’s very important to test your smart contract before deploying it on the main network in order to prevent issues in the future. When you have written unit tests, they will guarantee that there won’t be any discrepancy between your white paper and smart contract, and your smart contract will not be hacked by calling functions which _should_ have the correct rights but _don’t_.

It’s not about just Smart Contracts: you need Unit tests for all your apps and code because it shows you all the ways your app could have failed.

