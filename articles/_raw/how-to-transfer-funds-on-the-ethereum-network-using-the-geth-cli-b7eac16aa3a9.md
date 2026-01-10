---
title: How to Transfer Funds on the Ethereum Network Using the GETH CLI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-08T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-transfer-funds-on-the-ethereum-network-using-the-geth-cli-b7eac16aa3a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eS0bXFKKeapljk0Ep3tw4A.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: golang
  slug: golang
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Lukas Lukac

  In my previous article, you learned how to set up a fully synced blockchain node
  in 10 mins. It’s now time to learn how to perform a transaction on the Ethereum
  network using the GETH CLI.

  To be on the same page, go through all the ste...'
---

By Lukas Lukac

In my [previous article](https://medium.freecodecamp.org/ethereum-69-how-to-set-up-a-fully-synced-blockchain-node-in-10-mins-f6318d7aad40), you learned how to set up a fully synced blockchain node in 10 mins. It’s now time to learn how to perform a transaction on the Ethereum network using the GETH CLI.

To be on the same page, go through all the steps from [previous article](https://medium.freecodecamp.org/ethereum-69-how-to-set-up-a-fully-synced-blockchain-node-in-10-mins-f6318d7aad40) first.

Done? Perfect.

At this point you know:

* how to run a fully synced Ethereum blockchain node
* how to attach `GETH console`
* how to query a balance of an Ethereum account

```
geth attach ipc:/home/enchanter/.gophersland_ethereum_r1/geth.ipc 
```

```
eth.getBalance("0xceee57f2b700c2f37d1476a7974965e149fce2d4")
```

```
> 7500000000000000000
```

I do, you might think, but wait for a second Lukas…why is `7.5ETH` is displayed as `7500000000000000000` in the `Geth console`?

### Ether vs Wei

The Ethereum Virtual Machine does not support decimals or floats. Apparently, calculations in finance are easier in integers.

Therefore, to be able to send a fraction of 1 ETH, the Ethereum foundation decided to create their own metric system where the smallest unit would be 1 Wei, and 1 Ether is 1e18 Wei.

But no worries, there are tools that can make your life easier. For example, I highly recommend the Ether to Wei online converter:

[https://etherconverter.online](https://etherconverter.online/)

In order to send $15 worth of Ether, where 1 ETH == $200 (good old times…), you would make a transaction sending 0.0740 ETH which would be, and must be represented in Wei as, 74000000000000000.

**Online Ether to Wei converter:**

![Image](https://cdn-media-1.freecodecamp.org/images/-X6USQnRm1wGPZSS-YeRAmi7DB83wPZatPzN)

**Overview of the Ethereum metric system:**

![Image](https://cdn-media-1.freecodecamp.org/images/QZtIr5o2rsnE7fSADFwq0m-GnMaAqUg8Wsqe)

Practice makes mastery. Let’s actually send 74000000000000000 Wei ($15) to another account.

### Sending Ether to another account using the GETH CLI

In one terminal, remember to run a fully synced blockchain node:

```
geth --rinkeby --datadir=~/.gophersland_ethereum_r1 --port=30304 --cache=2048 --rpc --rpcport=8546 --rpcapi=eth,web3,net,personal --syncmode=fast
```

In another terminal, we will create our second Ethereum account, exactly like in Part 1.

```
ls -la ~/.gophersland_ethereum_r1/keystore/> drwx------ 2 enchanter enchanter 4096 sep 24 15:36 .> drwx------ 4 enchanter enchanter 4096 sep 24 15:26 ..> -rw------- 1 enchanter enchanter  491 sep 24 15:36 
```

```
UTC--2018-09-24T13-36-43.069452577Z--ceee57f2b700c2f37d1476a7974965e149fce2d4geth --datadir=~/.gophersland_ethereum_r1 account new> INFO [09-24|15:36:33.566] Maximum peer count ETH=25 LES=0 total=25> Your new account is locked with a password. Please give a password. Do not forget this password.
```

```
> Passphrase: > Repeat passphrase: > Address: {7aa4a14286a25e3a275d7a122c23dc3c107a636a}ls -la ~/.gophersland_ethereum_r1/keystore/> drwx------ 2 enchanter enchanter 4096 oct 25 20:14 .> drwx------ 4 enchanter enchanter 4096 oct 25 19:48 ..> -rw------- 1 enchanter enchanter  491 sep 24 15:36 
```

```
UTC--2018-09-24T13-36-43.069452577Z--ceee57f2b700c2f37d1476a7974965e149fce2d4
```

Now, let’s attach the Geth Console to the currently running blockchain node as we did in the previous article in order to transfer $15 to this newly created account by executing the `eth.sendTransaction` command.

```
geth attach ipc:/home/enchanter/.gophersland_ethereum_r1/geth.ipc 
```

```
eth.sendTransaction({from: "0xceee57f2b700c2f37d1476a7974965e149fce2d4",to: "0x7aa4a14286a25e3a275d7a122c23dc3c107a636a", value: "74000000000000000"})
```

**Error: authentication needed: password or unlock.**

You should get an error. This is because sending Ether is a “transaction,” and a transaction changes state, costs gas, and spends funds. Which means it needs to be signed with our Private Key that is stored in the **Keystore.** In order to decrypt the key, we must provide a password, or in other words, unlock the account.

Execute the following command to unlock your account for the next 60s, and execute the sendTransaction command once again.

```
web3.personal.unlockAccount(web3.personal.listAccounts[0], null, 60) 
```

```
eth.sendTransaction({from: "0xceee57f2b700c2f37d1476a7974965e149fce2d4", to: "0x7aa4a14286a25e3a275d7a122c23dc3c107a636a", value: "74000000000000000"})
```

We could have also passed the password as a second argument instead of null. But this way is safer as your password is only in a buffer and not stored in any log or visible on the screen.

![Image](https://cdn-media-1.freecodecamp.org/images/LrxhDzbd71gAsfm-Jl545xh0Goc06CATzgmL)

**This time the command succeeded, and a Transaction hash receipt was returned! Oh yeah!**

As we are connected to the Rinkeby network, we can take advantage of the Rinkeby GUI explorer to check the status of this transaction, gas spent, gas price, etc.

1. Open the [explorer](https://www.rinkeby.io/#explorer)
2. Paste the Transaction receipt hash to the search bar
3. Done, we spent 21,000 of Gas (standard for sending funds) and the Transaction succeeded!

![Image](https://cdn-media-1.freecodecamp.org/images/LC9XhANCXPxhEUGnp4kNCj7SSxc3JbBeRTiK)

You can now query the balances of both accounts and see the changed state:

```
eth.getBalance("0xceee57f2b700c2f37d1476a7974965e149fce2d4") > 7425979000000000000 
```

```
eth.getBalance("0x7aa4a14286a25e3a275d7a122c23dc3c107a636a") > 74000000000000000
```

**Works like a charm.**

Congratulations! You:

* learned the difference between Ether and Wei and how to convert them
* submitted your first transaction across global Ethereum test network, Rinkeby

You can continue expanding your blockchain skills by [building one from scratch in Go!](https://www.freecodecamp.org/news/build-a-blockchain-in-golang-from-scratch/)"  

