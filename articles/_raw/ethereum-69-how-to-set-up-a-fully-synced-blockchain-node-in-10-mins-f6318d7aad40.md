---
title: 'Ethereum 69: How to Set Up a Fully Synced Blockchain Node in 10 Minutes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-16T23:18:46.000Z'
originalURL: https://freecodecamp.org/news/ethereum-69-how-to-set-up-a-fully-synced-blockchain-node-in-10-mins-f6318d7aad40
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oS4hnBtXtJ5h0hIJ0LHnyg.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Lukas Lukac

  Welcome in the first article of our new go-ethereum series!

  In the next 10 mins you will:


  Learn the first blockchain glossary without any necessary prior ecosystem knowledge

  Setup your fully synced testing node (“client/server”) in un...'
---

By Lukas Lukac

Welcome in the first article of our new go-ethereum series!

In the next 10 mins you will:

* Learn the first blockchain glossary without any necessary prior ecosystem knowledge
* **Setup your fully synced testing node** (“client/server”) **in** **under 10mins**
* **Create your account** and receive a transaction of 8ETH from the Ethereum foundation for FREE

Our motto is, practice before theory — so let’s jump straight into the installation of a fully synced Ethereum testing node connected to a Rinkeby test network!

### Geth

`Geth` is a command line interface (CLI), a compiled binary, program, and client for running a full Ethereum node implemented in Go.

We will use **Geth** to:

* run a fully synced Ethereum node to connect to a test network called Rinkeby
* create a new account to be able to send and receive transactions
* for reading the EVM state, e.g. checking a balance of any account (want to know how much balance your girlfriend, boyfriend, wife, neighbour has? Sweet transparency!)

### Installing Geth

We can install it directly from the repositories:

**Mac**

```
brew tap ethereum/ethereumbrew install ethereum
```

**Linux**

```
sudo apt-get install software-properties-commonsudo add-apt-repository -y ppa:ethereum/ethereumsudo apt-get updatesudo apt-get install ethereum
```

**Windows**

```
Good luck :)
```

**Verify the installation:**

```
which geth> /usr/local/bin/geth
```

```
geth version> Geth> Version: 1.8.20-stable
```

Ensure you are running the same version in order to be able to perform a full sync of a Rinkeby network, as described in the next steps because Rinkeby actioned a constantinople hardfork supported by Geth 1.8.20. 

### Running a blockchain node

Well, the devil is in the details…but getting started is actually simple. Kudos to the Ethereum developers.

Let’s setup a new fully synced **Rinkeby** (Ethereum test network using the Clique PoA protocol) **node**.

The Rinkeby PoA implementation is much faster but significantly less secure. It is more centralised from the mainnet concensus PoW which is perfectly fine being a test network. Rinkeby manages to approve a new block with a bunch of transactions every 15s.

Ok, ok, ok...What do those words actually mean?

* **Rinkeby:** name of the Proof of Authority test network
* **Node:** basically a traditional server executing Ethereum client/server
* **Concensus:** an algorithm defining how the transactions will be validated, appended, and persisted in the database on every Node
* **Block:** a bunch of transactions in a complicated array dispatched around the wire between all the nodes of the network every 15s
* **Transaction:** don’t think about a bank transaction. A blockchain transaction is a **state change.** Renaming the owner of a smart contract from Alice to Bob? Changing balance of your account from 1ETH to 5ETH? Setting variable “foo” value to “foo_value_123” in your smart contract? That’s a transaction.

You can read more about the Rinkeby PoA proposal here: [https://github.com/ethereum/EIPs/issues/225](https://github.com/ethereum/EIPs/issues/225)

```
geth --rinkeby --datadir=~/.gophersland_ethereum_r1 --port=30304 --cache=2048 --rpc --rpcport=8546 --rpcapi=eth,web3,net,personal --syncmode=fast
```

The above command will:

* initialize a new directory where all data will be stored in `~/.gophersland_ethereum_r1`. The default directory would be: `~/.ethereum`
* start downloading the Ethereum history necessary to become a new fully valid, synced Node of the network
* the communication will happen over port 30304
* cache, a kind of a buffer, will be set to 2GB to speed up the sync process
* additional RPC API will launch so we can communicate with our node through consoles, nice GUI over on port 8546, later on

![Image](https://cdn-media-1.freecodecamp.org/images/1*vABGraHKLDKTR5jWoVYsoA.png)

Wait for few hours until the blockchain is fully synced.

The current block number as of 24th of September is: 3039786. On my AMD Ryzen 5 2600, 3.4Ghz, the sync process took 3 hours. Oh yes, I have a new gaming PC!

Meanwhile you can [follow Web3Coach on Twitter](https://twitter.com/Web3Coach) or prepare dinner, probably breakfast as well, go to the gym… let’s just say, blockchain is not the fastest database :)

Eventually the printed message will be:

* INFO [<time>] Imported new chain segment count=1
* INFO [<time>] Imported new chain segment count=1
* INFO [<time>] Imported new chain segment count=1
* INFO [<time>] Imported new chain segment count=1

**Congratulation, you are now part of the blockchain revolution in less than 10mins!!!**

### Creating your first blockchain account

#### Keystore

All the Ethereum accounts and their keys are stored in a directory called the “**keystore**”. The directory is empty by default as we haven’t created our own account yet!

```
enchanter@lukas-gaming:~$ ls -la ~/.gophersland_ethereum_r1/
```

```
drwx------  4 enchanter enchanter 4096 sep 24 15:26 .drwxr-xr-x 18 enchanter enchanter 4096 sep 24 11:51 ..drwx------  4 enchanter enchanter 4096 sep 24 15:26 gethsrw-------  1 enchanter enchanter    0 sep 24 15:26 geth.ipcdrwx------  2 enchanter enchanter 4096 sep 23 09:54 keystore
```

```
enchanter@lukas-gaming:~$ ls -la ~/.gophersland_ethereum_r1/keystore/
```

```
drwx------ 2 enchanter enchanter 4096 sep 23 09:54 .drwx------ 4 enchanter enchanter 4096 sep 24 15:26 ..
```

#### Account

To create a new account, execute the following, already familiar, **geth** cmd.

```
geth --datadir=~/.gophersland_ethereum_r1 account new
```

You will be prompted to enter a passphrase (this is your SUPER SECRET PASSWORD). This is required for decrypting your newly generated private key associated with your new Ethereum address, as it allows you to use it later on for signing transactions on the blockchain. Note it down somewhere, since we will need it later. But don’t worry if you forget it, this is just a test network anyway.

```
enchanter@lukas-gaming:~$ ls -la ~/.gophersland_ethereum_r1/keystore/
```

```
drwx------ 2 enchanter enchanter 4096 sep 23 09:54 .drwx------ 4 enchanter enchanter 4096 sep 24 15:26 ..
```

```
enchanter@lukas-gaming:~$ geth --datadir=~/.gophersland_ethereum_r1 account new
```

```
INFO [09-24|15:36:33.566] Maximum peer count                       ETH=25 LES=0 total=25
```

```
Your new account is locked with a password. Please give a password. Do not forget this password.
```

```
Passphrase: Repeat passphrase:
```

```
Address: {ceee57f2b700c2f37d1476a7974965e149fce2d4}
```

```
enchanter@lukas-gaming:~$ ls -la ~/.gophersland_ethereum_r1/keystore/
```

```
drwx------ 2 enchanter enchanter 4096 sep 24 15:36 .drwx------ 4 enchanter enchanter 4096 sep 24 15:26 ..-rw------- 1 enchanter enchanter  491 sep 24 15:36 
```

```
UTC--2018-09-24T13-36-43.069452577Z--ceee57f2b700c2f37d1476a7974965e149fce2d4
```

**Woohoo! My new Ethereum address is alive:** `ceee57f2b700c2f37d1476a7974965e149fce2d4.`

You will normally encounter this address prefixed with “**0x**” to indicate the address encoding, **HEX**.

The newest format of the keyfiles is: `UTC--<created_at UTC ISO8601>-<your address in hex` encoding>. The order of accounts when listing is lexicographic, but as a consequence of the timespamp format, it is actually in order of creation.

If you are curious what is inside of the file, feel free to open it! You will see:

* **Address:** your new hex address
* **Crypto:** bunch of mathematical variables responsible for representing your private key in encrypted form, don’t worry about that magic for now

**Interesting note:** the account generation happens in offline mode and doesn’t require a synced blockchain node. Curious how is it possible to generate a unique address in an offline mode from the technical perspective? We will check out the **go-ethereum** source code itself in the next article.

**Spoiler:** it’s because the address is a hash of your public key which is based on your unique, private key.

Okay I have a new shinny Ethereum account, what’s my balance and how do I deposit some testing **Ether**?

Speaking of Ether… what is it actually?

#### Ether

Ether is the cryptocurrency powering the Ethereum network. It’s used as a unit of value and for paying miners for validating, appending, and persisting the transactions to the collective DB. But mainly its a technique for preventing SPAM because miners are rewarded 5 (since last month “just” 3) ETH for each successfully mined block. Yes, that’s $600 at the current price on 24th of September, every 15s. Not a bad business.

### How to receive a transaction of 8ETH from the Ethereum foundation for FREE

#### Checking account balance

Let’s make sure our account balance is 0 first, unless someone already managed to send some Ether out of the goodness of their heart.

**Geth** provides a JavaScript console that can be attached to the executable binary for interacting with the blockchain conveniently. We can connect to it by specifying a socket file that is exposed once **Geth** boots up. Socket files are very useful for “inter process communication on the same machine”, aka IPC.

You can locate this file in the the default data directory while the Geth program is running:

```
enchanter@lukas-gaming:~$ ls -la ~/.gophersland_ethereum_r1/
```

```
drwx------  4 enchanter enchanter 4096 Sep 24 15:44 .drwxr-xr-x 18 enchanter enchanter 4096 Sep 24 15:47 ..drwx------  4 enchanter enchanter 4096 Sep 24 15:44 gethsrw-------  1 enchanter enchanter    0 Sep 24 15:44 geth.ipcdrwx------  2 enchanter enchanter 4096 Sep 24 15:47 keystore
```

Let’s interact with the Rinkeby network using the “**geth attach**” cmd in another terminal while your blockchain node is still running. Make sure to pass the absolute path to the IPC file, otherwise you will get an error.

```
enchanter@lukas-gaming:~$ geth attach ipc:/home/enchanter/.gophersland_ethereum_r1/geth.ipc
```

```
Welcome to the Geth JavaScript console!
```

```
instance: Geth/v1.8.15-stable-89451f7c/linux-amd64/go1.10.1coinbase: 0xceee57f2b700c2f37d1476a7974965e149fce2d4at block: 3044891 (Mon, 24 Sep 2018 16:42:36 CEST)
```

```
datadir: /home/enchanter/.gophersland_ethereum_r1modules: admin:1.0 clique:1.0 debug:1.0 eth:1.0 miner:1.0 net:1.0 personal:1.0 rpc:1.0 txpool:1.0 web3:1.0
```

```
&gt; eth.accounts["0xceee57f2b700c2f37d1476a7974965e149fce2d4"]
```

```
&gt; eth.syncingfalse
```

```
&gt; eth.getBalance("0xceee57f2b700c2f37d1476a7974965e149fce2d4")0
```

#### Query blockchain:

**eth.accounts:** to check your currently available accounts

**eth.syncing:** to make sure our state, DB is fully up to date with rest of the network to ensure the getBalance response will be based on the latest state

**eth.getBalance(“<your address&**gt;”): to query the DB.

#### Receiving a transaction of 8ETH from the Ethereum foundation for FREE

The Ethereum foundation has a very neat program called “**Faucet**” available online for assigning Ether to accounts requesting it in real-time.

Requesting Ether:

1. Publish your account address on one of the public social networks
2. E.g, post a tweet containing your Ethereum address anywhere in the tweet like this one [https://twitter.com/EnchanterIO/status/1044238559224483841](https://twitter.com/EnchanterIO/status/1044238559224483841), make sure you tag [@Web3Coach](https://twitter.com/Web3Coach) and [@freeCodeCamp](https://twitter.com/freecodecamp) and let us know if you like the tutorial!
3. Open [https://www.rinkeby.io/#faucet](https://www.rinkeby.io/#faucet) and paste the tweet URL
4. Click on “Give me Ether”, choose between 3, 7.5 or 18.75 Ether
5. Wait few seconds
6. Query your account balance again

![Image](https://cdn-media-1.freecodecamp.org/images/0*Zd4RuYRAIiyqy8Jf)
_Rinkeby Faucet_

![Image](https://cdn-media-1.freecodecamp.org/images/0*TM_yQ3hRp8c8tyf8)

### Voilà

You are rich… in a test network. Congratulation for getting so far. 

You can continue expanding your blockchain skills by [building one from scratch in Go!](https://www.freecodecamp.org/news/build-a-blockchain-in-golang-from-scratch/)"

