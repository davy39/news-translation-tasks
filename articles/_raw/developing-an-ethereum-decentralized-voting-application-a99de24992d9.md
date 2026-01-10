---
title: A guide to developing an Ethereum decentralized voting application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-07T10:24:20.000Z'
originalURL: https://freecodecamp.org/news/developing-an-ethereum-decentralized-voting-application-a99de24992d9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cQl1eHoplkcQF2dTaWo5FA.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Timothy Ko

  After the entire cryptocurrency market passed 700 billion dollars in market cap,
  the cryptocurrency space exploded over these last couple months. But this is just
  the beginning. As blockchain systems continue to evolve and scale, one gr...'
---

By Timothy Ko

After the entire cryptocurrency market passed 700 billion dollars in market cap, the cryptocurrency space exploded over these last couple months. But this is just the beginning. As blockchain systems continue to evolve and scale, one great way to dip into this new space and leverage this technology is with decentralized applications, otherwise known as dApps.

[CryptoKitties](https://www.cryptokitties.co/), famous for its congestion of the Ethereum Blockchain, is a great example of a dApp, uniquely combining concepts of breedable and collectible cats with the blockchain. This sensational game is just one creative example out of a virtually unlimited number of opportunities.

Although seemingly very complicated, certain frameworks and tools have been developed to abstract your interactions with the blockchain and smart contracts. In this blog post, I will go over one way to create a decentralized voting app on Ethereum. I will briefly go over Ethereum, but you probably should have an understanding of it to use this guide to the fullest. In addition, I do expect you to know Javascript.

### Why make a Decentralized Voting app?

Essentially, a great decentralized application utilizing blockchain technology allows you perform the same actions you would today (like transferring money) without a trusted third party. The best dApps have a specific real world use-case that leverages the unique characteristics of blockchain.

> In essence, the blockchain is a shared, programmable, cryptographically secure and therefore trusted ledger which no single user controls and which can be inspected by anyone.- Klaus Schwab

Even though a voting app might not be a great app for consumers, I’ve chosen to use it for this guide because the main issues blockchain solves — transparency, security, accessibility, audibility — are the main problems plaguing current democratic elections.

Since a blockchain is a permanent record of transactions (votes) that are distributed, every vote can irrefutably be traced back to exactly when and where it happened without revealing the voter’s identity. In addition, past votes cannot be changed, while the present can’t be hacked, because every transaction is verified by every single node in the network. And any outside or inside attacker must have control of 51% of the nodes to alter the record.

Even if the attacker was able to achieve that while incorrectly entering user votes with their real IDs under the radar, end to end voting systems could allow voters to verify whether their vote was correctly entered in the system, making the system extremely safe.

### Core Components of Ethereum

I do expect you to have an understanding of [Blockchain](https://www.coindesk.com/information/what-is-blockchain-technology/) and [Ethereum](https://www.ethereum.org/) for the remainder of this guide. [Here](https://medium.com/@preethikasireddy/how-does-ethereum-work-anyway-22d1df506369) is an awesome guide about it, and I’ve written a brief overview of the core components I’d like you to know.

1. **Smart Contracts** act as the back-end logic and storage. A contract is written in [Solidity](http://solidity.readthedocs.io/en/develop/solidity-in-depth.html), a smart contract language, and is a collection of code and data that resides at a specific address on the Ethereum blockchain. It’s very similar to a class in Object Oriented Programming, where it includes functions and state variables. Smart Contracts, along with the Blockchain, are the basis of all Decentralized Applications. They are, like Blockchain, immutable and distributed, which means upgrading them will be a pain if they are already on the Ethereum Network. Fortunately, [here](https://consensys.github.io/smart-contract-best-practices/software_engineering/) are some ways to do that.
2. **The Ethereum Virtual Machine(EVM)** handles the internal state and computation of the entire Ethereum Network. Think of the EVM as this massive decentralized computer that contains “addresses” that are capable of executing code, changing data, and interacting with each other.
3. [**Web3.js**](https://github.com/ethereum/wiki/wiki/JavaScript-API) is a Javascript API that allows you to interact with the Blockchain, including making transactions and calls to smart contracts. This API abstracts the communication with Ethereum Clients, allowing developers to focus on the content of their application. You must have a web3 instance imbedded in your browser to do so.

### Other Tools we will use

1. [**Truffle**](http://truffleframework.com/docs/) is a popular testing development framework for Ethereum. It includes a development blockchain, compilation and migration scripts to deploy your contract to the Blockchain, contract testing, and so on. It makes development easier!
2. [**Truffle Contracts**](https://github.com/trufflesuite/truffle-contract) is an abstraction on top of the Web3 Javascript API, allowing you to easily connect and interact with your Smart Contract.
3. [**Metamask**](https://metamask.io/) brings Ethereum to your browser. It is a browser extension that provides a secure web3 instance linked to your Ethereum address, allowing you to use Decentralized Applications. We will not be using Metamask in this tutorial, but it is a way for people to interact with your DApp in production. Instead, we will inject our own web3 instance during development. For more information, check out [this](http://truffleframework.com/docs/advanced/truffle-with-metamask) link.

### Let’s Start!

For simplicity, we actually won’t be building the full voting system I described earlier. For ease of explanation, it will just be a one page application where a user can enter their ID and vote for a candidate. There will also be a button that counts and displays the number of votes per candidate.

This way, we will be able to focus the process of creating and interacting with the smart contracts within an application. The source code for this entire application will be in [this repository](https://github.com/tko22/eth-voting-dapp), and you will need to have Node.js and npm installed.

First, let’s install Truffle globally.

```
npm install -g truffle
```

To use Truffle commands, you must run them in an existing project.

```
git clone https://github.com/tko22/truffle-webpack-boilerplatecd truffle-webpack-boilerplatenpm install
```

This repository is just a skeleton of a Truffle Box, which are boilerplates or example applications that you can get in one command — `truffle unbox [box name]`. However, the Truffle box with webpack isn’t updated with the latest versions and includes an example application. Thus, I created this [repo](https://github.com/tko22/truffle-webpack-boilerplate) (the one linked in the instructions above).

#### 2. Directory Structure

Your directory structure should include these:

* `contracts/` — Folder holding all of the Contracts. **DO NOT DELETE** `Migrations.sol`
* `migrations/` — Folder holding [Migration files](http://truffleframework.com/docs/getting_started/migrations), which help you deploy your smart contracts into the Blockchain.
* `src/` — holds the HTML/CSS and Javascript files for the application
* `truffle.js` — Truffle Configuration file
* `build/` — You won’t see this folder until you compile your contracts. This folder holds the build artifacts so don’t modify any of these files! Build artifacts describe the function and architecture of your contract and give Truffle Contracts and web3 information on how to interact with your Smart Contract in the Blockchain.

### 1. Write your Smart Contracts

Enough with the setup and introduction. Let’s get into the code! First off, we’ll be writing our Smart Contract, which is written in [Solidity](http://solidity.readthedocs.io/en/develop/index.html) (the other languages aren’t as popular). It may seem scary, but it’s not.

For any application, **you want your smart contracts to be as simple as possible, even stupidly simple.** Remember that you have to pay for every computation/transaction you make, and your smart contracts will be on the Blockchain **forever.** So, you really want it to work perfectly––meaning, the more complex it is, the easier it is to make a mistake.

Our contract will include:

1. **State Variables** — variables that hold values that are permanently stored on the Blockchain. We will use state variables to hold a list and number of Voters and Candidates.
2. [**Functions**](http://solidity.readthedocs.io/en/develop/contracts.html#functions) — Functions are the executables of smart contracts. They are what we will call to interact with the Blockchain, and they have different levels of visibility, internally and externally. Keep in mind that whenever you want to change the value/state of a variable, a transaction must occur — costing Ether. You can also make `calls` to the Blockchain, which won’t cost any Ether because the changes you made will be destroyed (more on this in Section 3 when we actually make the `transactions` and `calls`).
3. [**Events**](http://solidity.readthedocs.io/en/develop/contracts.html#events) — Whenever an event is called, the value passed into the event will be logged in the transaction’s log. This allows Javascript callback functions or resolved promises to view the certain value you wanted to pass back after a transaction. This is because every time you make a transaction, a transaction log will be returned. We will use an event to log the ID of the newly created Candidate, which we’ll display (check the first bullet point of Section 3).
4. [**Struct Types**](http://solidity.readthedocs.io/en/develop/types.html#structs) — This is very similar to a C struct. Structs allow you to hold multiple variables, and are awesome for things with multiple attributes. `Candidates` will only have their name and party, but you can definitely add more attributes to them.
5. **Mappings** — Think of these like hash-maps or dictionaries, where it has a key-value pair. We will use two mappings.

There are a couple more types that aren’t listed here, but some of them are a little more complicated. These five encompass many of the structures a smart contract will generally use. These types are explained more in depth [here](http://solidity.readthedocs.io/en/develop/structure-of-a-contract.html#).

For reference, here’s the Smart Contract’s code. Note that this file should be called `Voting.sol` but I wanted the Github gist to have styling so I gave it a `.js` extension. Like the rest of this guide, I will provide comments within the code that will explain what it is doing, and I’ll explain the big picture afterwards while pointing out certain caveats and logic.

Basically, we have two Structs (types that hold multiple variables) that describe a Voter and a Candidate. With Structs, we are able to assign multiple properties to them, such as emails, address, and so on.

To keep track of Voters and Candidates, we put them into separate mappings where they are integer indexed. **A Candidate or Voter’s index/key––lets call it ID — is the sole way for functions to access them**.

We also keep track of the number of Voters and Candidates, which will help us index them. In addition, don’t forget about the event in line 8, which will log the candidate’s ID when it’s added. This event will be used by our interface, since we need to keep track of a candidate’s ID in order to vote for a candidate.

1. I know, contrary to what I said earlier about making contracts super simple, I made this contract a little more complicated in comparison to what this application actually does. However, I did this so that it would be a lot easier for you guys to make edits and add features to this application afterward (more on that at the end). If you’d like to make an even simpler voting application, the smart contract could work in less than 15 lines of code.
2. Note that the state variables `numCandidates` and `numVoters` are not declared public. By [default](http://solidity.readthedocs.io/en/develop/contracts.html#visibility-and-getters), these variables have a visibility of `internal`, which means that they can only be directly accessed by the current contract or derived contracts (don’t worry about that, we won’t be using it).
3. We are using `32bytes` for strings instead of using the `string` type. Our [EVM has a word-size of 32 bytes](https://ethereum.stackexchange.com/q/2327/42), so it is “optimized” for dealing with data in chunks of 32 bytes. (Compilers, such as Solidity, have to do more work and generate more bytecode when data isn’t in chunks of 32 bytes, which effectively leads to higher gas cost.)
4. When a user votes, a new `Voter` struct is created and added to the mapping. In order to count the number of votes a certain candidate has, you must loop through all the Voters and count the number of votes. Candidates operate on the same behavior. **Thus, these mappings will hold the history of all Candidates and Voters.**

### 2. Instantiate web3 and contracts

With our Smart Contract completed, we now need to run our test blockchain and deploy this contract onto the Blockchain. We’ll also need a way to talk to it, which will be via web3.js.

Before we start our test blockchain, we must create a file called `2_deploy_contracts.js` inside the folder `/contracts` that tells it to include your Voting Smart Contract when you migrate.

To start the development Ethereum blockchain, go to your command line and run:

```
truffle develop
```

This will live on your command line. Since Solidity is a compiled language, we must compile it to bytecode first for the EVM to execute.

```
compile
```

You should see a `build/` folder inside your directory now. This folder holds the build artifacts, which are critical to the inner workings of Truffle, so don’t touch them!

Next, we must migrate the contract. [Migrations](http://truffleframework.com/docs/getting_started/migrations) is a Truffle script that helps you alter the state of your application’s contract as you develop. Remember that your contract is deployed to a certain address on the Blockchain, so whenever you make changes, your contract will be located at a different address. Migrations help you do this and also help you move data around.

```
migrate
```

Congratulations! Your smart contract is now on the Blockchain forever. Well, not really…. because `truffle develop` refreshes every time you stop it.

If you’d like to have a persisting blockchain, consider [Ganache](http://truffleframework.com/ganache/), which is also developed by Truffle. If you are using Ganache, you will not need to call `truffle develop`. Instead, you will run `truffle compile` and `truffle migrate`. To understand what it really takes to deploy a contract without Truffle, check out this [blog post](https://medium.com/@gus_tavo_guim/deploying-a-smart-contract-the-hard-way-8aae778d4f2a).

Once we have deployed the smart contract to the Blockchain, we will have to setup a web3.0 instance with Javascript on the browser whenever the application starts. Thus, the next piece of code will be placed in the bottom of `js/app.js`. Note that we are using web3.0 version 0.20.1.

You don’t really have to worry too much if you don’t understand this code. Just know that this will be run when the application starts and will check if there already is a web3 instance (Metamask) in your browser. If there isn’t, we’ll just create one that talks to `localhost:9545`, which is the Truffle development blockchain.

If you’re using Ganache, you must change the port to `7545`. Once an instance is created, we will call the `start` function (I’ll define it in the next section).

### 3. Add functionality

The last thing we’ll need to do is to write the interface for the application. This involves the essentials for any web application––HTML, CSS, and Javascript (We’ve already written a little of the Javascript with creating a web3 instance). First, let’s create our HTML file.

This is a very simple page, with an input form for user ID, and buttons for Voting and Counting votes. When those buttons are clicked, they will call specific functions that vote, and will find the number of votes for the candidates.

There are three important div elements though, with ids: `candidate-box`, `msg`, and `vote-box`, which will hold checkboxes for each candidate, a message, and the number of votes, respectively. We also import JQuery, Bootstrap, and `app.js`.

Now, we just need to interact with the Contract and implement the functions for voting and counting the number of votes for each candidate. JQuery will manipulate the DOM, and we’ll be using Promises as we make transactions or calls to the Blockchain. Below is the code for `app.js`.

Note that the code I provided in the previous step for creating a web3 instance is also here. First, we import the necessary libraries and webpack stuff, including web3 and [Truffle Contracts](https://github.com/trufflesuite/truffle-contract). We will be using Truffle Contracts, which is built on top of web3 to interact with the Blockchain.

To use it, we’ll grab the build artifacts that were automatically built when we compiled the voting smart contract and use them to create the Truffle Contract. Finally, we set up the functions in the global variable `window` for starting the app, voting for a candidate, and finding the number of votes.

To actually interact with the Blockchain, we must create an instance of the Truffle Contract by using the `deployed` function. This, in turn, will return a promise with the instance as the return value that you will use to call functions from the smart contract.

There are two ways to interact with those functions: transactions and calls. **A transaction is a write-operation, and it will be broadcast to the entire network and processed by miners (and thus, costs Ether).** You must perform a transaction if you’re changing a state variable, since it will change the state of the blockchain.

**A call is a read-operation, simulating a transaction but discarding the change in state. Thus, it will not cost Ether.** This is great for calling getter functions (check out the four getter functions we wrote previously in our smart contract).

To make a transaction with Truffle Contracts, you write `instance.functionName(param1, param2)`, with `instance` as the instance that was returned by the `deployed` function (Check line 36 for an example). This transaction will return a promise with the transaction data as the return value. Thus, if you return a value in your smart contract function but you perform a transaction with that same function, it will not return that value.

This is why we have an event that will log whatever you want it to write into the transaction data that will be returned. In the case of lines 36–37, we make a transaction to add a Candidate. When we resolve the promise, we have the transaction data in `result`.

To get the `candidateID` that we logged with the event `AddedCandidate()` (check the smart contract to see it 0), we must go through the logs and retrieve it like this: `result.logs[0].args.candidateID`.

To really see what’s going on, use the Chrome developer tools to print out the `result` and look through its structure of `result`.

To make a call, you will write `instance.functionName.call(param1,param2)`. However, if a function has the keyword `view`, then Truffle Contracts will automatically create a call and thus you don’t need to add the `.call`.

This is why our getter functions have the `view` keyword. Unlike making a transaction, the returned promise of a call will have a return value of whatever is returned by the smart contract function.

I will now explain the 3 functions briefly but this should be very familiar if you’ve built applications retrieving/changing data from a data store and manipulating the DOM accordingly. Think of the Blockchain as your database, and the Truffle Contracts as the API to get data from your database.

#### **App.start()**

This function is called immediately after we create a web3 instance. To get Truffle Contracts to work, we must set the provider to the created web3 instance and set defaults (like which account you’re using and the amount of gas you want to pay to make a transaction).

Since we are in development mode, we can use any amount of gas and any account. During production, we would take the account provided by MetaMask and try to figure out the smallest amount of gas you could use, since it’s actually real money.

With everything set up, we will now display the checkboxes for each candidate for the user to vote. To do this, we must create an instance of the contract and get the Candidate’s information. If there aren’t any candidates, we will create them. In order for a user to vote for a candidate, we must provide the ID of that certain candidate. Thus, we make each checkbox element have an `id`(HTML element attribute) of the ID of the candidate. Additionally, we will add the number Of candidates to a global variable `numOfCandidates`, which we will use in `App.findNumOfVotes()`. JQuery is used to append each checkbox and its candidate name to `.candidate-box`.

#### **App.vote()**

This function will vote for a certain candidate based on which checkbox is clicked and its `id` attribute.

One, we will check whether the user has input their userID, which is their identification. If they didn’t, we display a message telling them to do so.

Two, we will check whether the user is voting for a candidate, checking if there is at least one checkbox that’s clicked. If none of the checkboxes were clicked, we will also display a message telling them to vote for a candidate. If one of the checkboxes is clicked, we will grab the `id` attribute of that checkbox, which is also the linked candidate’s ID, and use that to vote for the candidate.

Once the transaction has been completed, we will resolve the returned promise and display a “Voted” message.

#### **App.findNumOfVotes()**

This last function will find the number of Votes for each candidate and display them. We will go through the candidates and call two smart contract functions, `getCandidate` and `totalVotes`. We will resolve those promises and create an HTML element for that certain candidate.

Now, start the application and you’ll see it on `http://localhost:8080/`!

```
npm run dev
```

### Resources

I know, it’s a lot… You might have this article open for a while as you slowly develop this application and really understand what’s going on. But that’s learning! Please supplement this guide with all the documentation from Ethereum, Truffle, and what I have provided below. I’ve tried to hit many of the key points in this article, but it’s just a brief overview and these resources will help a lot.

* [**Everything about Solidity and Smart Contracts**](http://solidity.readthedocs.io/en/develop/index.html) — I mean Everything
* [**Everything about Truffle**](http://truffleframework.com/docs/)
* [**Truffle Contracts Docs**](https://github.com/trufflesuite/truffle-contract)
* [**Web3 Javascript API**](https://github.com/ethereum/wiki/wiki/JavaScript-API) — this will be great to know and reference, but Truffle Contracts abstracts many parts of this
* [**Useful DApp patterns**](https://github.com/ethereum/wiki/wiki/Useful-%C3%90app-Patterns)
* [**Ethereum Docs**](https://github.com/ethereum/wiki/wiki/Ethereum-introduction) — look to the side bar and there’s plenty of stuff
* [**CryptoKitties Code Explanation**](https://medium.com/loom-network/how-to-code-your-own-cryptokitties-style-game-on-ethereum-7c8ac86a4eb3) — The writer goes through the important parts of CryptoKitties’ Smart Contract
* [**Smart Contract Best Practices**](https://consensys.github.io/smart-contract-best-practices/) — a must read

### Conclusion

Building applications on Ethereum is pretty similar to a regular application calling a backend service. The hardest part is writing a robust and complete smart contract. I hope this guide helped you understand the core knowledge of decentralized applications and Ethereum and will help you kick-start your interest in developing them.

If you’d like to build off of what we’ve built, here are some ideas. I’ve actually written the smart contract in such a way that it’s easily implemented with everything I’ve given you in this guide.

* **Display the party of each Candidate.** We already get the party of a candidate when we run `getCandidate(id)`.
* **Check if the User-entered ID is unique.**
* **Ask and store more information about a User,** such as their date of birth and home address.
* **Add in an option to see whether a person with a specific id has voted or not.** You would create a new form to enter in an ID, which you would then search for that certain user in the blockchain.
* **Write a new smart contract function that counts the votes for BOTH candidates at once.** Currently, we have to make two separate calls for two candidates, requiring the contract to loop through all the Users twice.
* **Allow new Candidates to be added.** This means adding a new form to add Candidates, but also changing up a little on how we display and vote for candidates in the frontend.
* **Require Users to have an Ethereum Address to vote.** My logic for not including user addresses is because voters wouldn’t be expected to have Ethereum to participate in this voting process. However, many DApps will require users to have an Ethereum Address.

Also, here are some tips that could prevent some roadblocks from happening:

* Double and triple check your smart contract functions when something weird is happening. I spent a couple hours on a bug to figure out that I returned the wrong value in one of my functions.
* Check whether your URL and port are correct when you connect to your development blockchain. Remember: `7545` is for `truffle develop` and `9545` is for Ganache. These are **defaults,** so if you can’t connect to your blockchain, you might’ve changed them.
* I didn’t go over this because this guide would’ve been too long and I probably will make another post on this — but you should [test](http://truffleframework.com/docs/getting_started/testing) your contracts! It will help a lot.
* If you aren’t familiar with [promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), go through how they work and how to use them. Truffle Contracts uses promises and the beta for web3 will also support promises. They can, if you do them wrong, mess up a lot of the data you’re retrieving.

Cheers to working towards a decentralized and secure internet — Web 3.0!

_I hope you enjoyed reading this guide as much as I enjoyed writing it! If you have any thoughts and comments, feel free to leave a comment below or email me at tk2@illinois.edu or [tweet](https://twitter.com/timmykko6) me( I’ve recently created one)! Feel free to use my code and share it with your friends!_

