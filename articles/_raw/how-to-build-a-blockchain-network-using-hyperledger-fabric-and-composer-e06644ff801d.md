---
title: How to build a blockchain network using Hyperledger Fabric and Composer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-24T22:54:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-blockchain-network-using-hyperledger-fabric-and-composer-e06644ff801d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*iGuxOX8a2_jCdQEd
tags:
- name: Blockchain
  slug: blockchain
- name: Cryptocurrency
  slug: cryptocurrency
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Haardik

  A tutorial for new blockchain developers


  _Photo by [Unsplash](https://unsplash.com/@alexacea?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Alexandru Acea on <a href="https://unsplash.com?utm_source=medium&...'
---

By Haardik

#### A tutorial for new blockchain developers

![Image](https://cdn-media-1.freecodecamp.org/images/0*iGuxOX8a2_jCdQEd)
_Photo by [Unsplash](https://unsplash.com/@alexacea?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Alexandru Acea</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Before I begin, Hyperledger Fabric **only** runs on Unix-based operating systems. As a result, it will not be able to run on Windows and you’ll have restrictions on what you can do. I suggest setting up a virtual machine if you are running Windows before continuing.

This article assumes some knowledge of Javascript. It isn’t a tutorial aimed at beginner programmers, but rather at programmers who are beginners in the blockchain space.

### What are we building?

So, you want to build a blockchain application but have no idea where to start? Don’t worry. Through this tutorial, we will set up a trading cards network. Different `Trader`s who own `TradingCard`s of Baseball, Football, and Cricket players, will be able to trade cards among themselves.

We’ll also set up a REST API server to allow client side software to interact with our business network. Finally, we will also generate an Angular 4 application which uses the REST API to interface with our network.

You can find the full final code of what we are about to build on this [Github repo](https://github.com/haardikk21/cards-trading-network)

Are you ready to get started?

### Table of Contents

* Introduction to Hyperledger Fabric and related applications
* Installing the prerequisites, tools, and a Fabric runtime
* Creating and deploying our business network
* Testing our business network
* Generating a REST API server
* Generating an Angular application which uses the REST API

### Introduction to Hyperledger Fabric and related applications

![Image](https://cdn-media-1.freecodecamp.org/images/0*Ma2ZQgFeXiAUYGeb)
_Development environment overview for Hyperledger_

**Hyperledger Fabric** is an open source framework for making private (permissioned) blockchain business networks, where identities and roles of members are known to other members. The network built on fabric serves as the back-end, with a client-side application front-end. SDK’s are available for Nodejs and Java to build client applications, with Python and Golang support coming soon.

**Hyperledger Composer** is a set of Javascript based tools and scripts which simplify the creation of Hyperledger Fabric networks. Using these tools, we can generate a **business network archive (BNA)** for our network. Composer broadly covers these components:

* Business Network Archive (BNA)
* Composer Playground
* Composer REST Server

**Business Network Archive** — Composer allows us to package a few different files and generate an archive which can then be deployed onto a Fabric network. To generate this archive, we need:

* **Network Model** — A definition of the resources present in the network. These resources include Assets, Participants, and Transactions. We will come back to these later.
* **Business Logic** — Logic for the transaction functions
* **Access Control Limitations —** Contains various rules which define the rights of different participants in the network. This includes, but is not limited to, defining what Assets the Participants can control.
* **Query File (optional) —** A set of queries which can be run on the network. These can be thought of as similar to SQL queries. You can read more on queries [here](https://hyperledger.github.io/composer/latest/reference/query-language).

**Composer Playground** is a web based user interface that we can use to model and test our business network. Playground is good for modelling simple Proofs of Concept, as it uses the browser’s local storage to simulate the blockchain network. However, if we are running a local Fabric runtime and have deployed a network to it, we can also access that using Playground. In this case, Playground isn’t simulating the network, it’s communicating with the local Fabric runtime directly.

**Composer REST Server** is a tool which allows us to generate a REST API server based on our business network definition. This API can be used by client applications and allows us to integrate non-blockchain applications in the network.

### Installing the prerequisites, tools, and a Fabric runtime

#### **1. Installing Prereqs**

Now that we have a high level understanding of what is needed to build these networks, we can start developing. Before we do that, though, we need to make sure we have the prerequisites installed on our system. An updated list can be found [here](https://hyperledger.github.io/composer/latest/installing/installing-prereqs.html).

* Docker Engine and Docker Compose
* Nodejs and NPM
* Git
* Python 2.7.x

For Ubuntu users, Hyperledger has a bash script available to make this process extremely easy. Run the following commands in your terminal:

Unfortunately, Mac users have to manually install the aforementioned tools and make sure they have all the prerequisites on their system. [This page](https://hyperledger.github.io/composer/latest/installing/installing-prereqs.html) is kept up to date with installation instructions.

#### 2. **Installing tools to ease development**

Run the following commands in your Terminal, and make sure you’re **NOT** using sudo when running npm commands.

**composer-cli** is the only essential package. The rest aren’t core components but will turn out to be extremely useful over time. We will learn more about what each of these do as we come across them.

#### 3. **Installing a local Hyperledger Fabric runtime**

Let’s go through the commands and see what they mean. First, we make and enter a new directory. Then, we download and extract the tools required to install Hyperledger Fabric.

We then specify the version of Fabric we want, at the time of writing we need 1.2, hence **hlfv12**. Then, we download the fabric runtime and start it up.

Finally, we generate a `PeerAdmin` card. Participants in a Fabric network can have business network cards, analogous to real life business cards. As we mentioned before, Fabric is a base layer for private blockchains to build upon. The holder of the PeerAdmin business card has the authority to deploy, delete, and manage business networks on this Fabric runtime (aka YOU!)

If everything went well, you should see an output like this:

![Image](https://cdn-media-1.freecodecamp.org/images/0*xUjx4TYAN4gnsyWa)

Also, if you type `ls` you’ll see this:

![Image](https://cdn-media-1.freecodecamp.org/images/0*uF_L4sB42hB8TqnH)

Basically what we did here was just download and start a local Fabric network. We can stop is using `./stopFabric.sh` if we want to. At the end of our development session, we should run `./teardownFabric.sh`

**NOTE:** This local runtime is **meant to be frequently started, stopped, and torn down** for development use. For a runtime with more persistent state, you’ll want to deploy the network outside the dev environment. You can do this by running the network on Kubernetes or on managed platforms like IBM Blockchain. Still, you should go through this tutorial first to get an idea.

### Creating and deploying our business network

Remember the packages `yo` and `generator-hyperledger-composer` we installed earlier?

`yo` provides us a generator ecosystem where generators are plugins which can be run with the yo command. This is used to set up boilerplate sample applications for various projects. `generator-hyperledger-composer` is the Yo generator we will be using as it contains specs to generate boilerplate business networks among other things.

#### **1. Generating a business network**

Open terminal in a directory of choice and type `yo hyperledger-composer`

![Image](https://cdn-media-1.freecodecamp.org/images/0*l7HZjX-AphNyrorr)

You’ll be greeted with something similar to the above. Select `Business Network` and name it `cards-trading-network` as shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/0*4RUkLM9_We2YorAa)

#### 2. **Modeling our business network**

The first and most important step towards making a business network is identifying the resources present. We have four resource types in the modeling language:

* Assets
* Participants
* Transactions
* Events

For our `cards-trading-network` , we will define an asset type`TradingCard` , a participant type `Trader` , a transaction `TradeCard` and an event `TradeNotification`.

Go ahead and open the generated files in a code editor of choice. Open up `org.example.biznet.cto` which is the modeling file. Delete all the code present in it as we’re gonna rewrite it (except for the namespace declaration).

This contains the specification for our asset `TradingCard` . All assets and participants need to have a unique identifier for them which we specify in the code, and in our case, it’s `cardId`

Also, our asset has a `GameType cardType` property which is based off the enumerator defined below. Enums are used to specify a type which can have up to N possible values, but nothing else. In our example, no `TradingCard` can have a `cardType` other than `Baseball`, `Football`, or `Cricket`

Now, to specify our `Trader` participant resource type, add the following code in the modeling file

This is relatively simpler and quite easy to understand. We have a participant type `Trader` and they’re uniquely identified by their `traderId`s.

Now, we need to add a reference to our `TradingCard`s to have a reference pointing to their owner so we know who the card belongs to. To do this, add the following line inside your `TradingCard` asset:

`--> Trader ow`ner

so that the code looks like this:

This is the first time we’ve used `--&`gt; and you must be wondering what this is. This is a relationship pointe`r`. o a`nd` --> are how we differentiate between a resource’s own properties vs a relationship to another resource type. Since the owner `is a` Trader which is a participant in the network, we want a reference to `that` Trader directly, and that’s exactly `wh`at --> does.

Finally, go ahead and add this code in the modeling file which specifies what parameters will be required to make a transaction and emitting an event.

#### 3. **Adding logic for our transactions**

To add logic behind the `TradeCard` function, we need a Javascript logic file. Create a new directory named `lib` in your project’s folder and create a new file named `logic.js` with the following code:

**NOTE:** The decorator in the comments above the function is very important. Without the `@param {org.example.biznet.TradingCard} trade` , the function has no idea which `Transaction` the code refers to from the modeling language. Also, make sure the parameter name being passed (i.e. `trade`) is the one you’re passing along in the function definition right after.

This code basically checks if the specified card has `forTrade == true` and updates the card’s owner in that case. Then, it fires off the `TradeNotification` event for that card.

#### 4. **Defining permissions and access rules**

Add a new rule in `permissions.acl` to give participants access to their resources. In production, you would want to be more strict with these access rules. You can read more about them [here](https://hyperledger.github.io/composer/latest/reference/acl_language).

#### 5. **Generating a Business Network Archive (BNA)**

Now that all the coding is done, it’s time to make an archive file for our business network so we can deploy it on our local Fabric runtime. To do this, open Terminal in your project directory and type this:

`composer archive create --sourceType dir --sourceName .`

This command tells Hyperledger Composer we want to build a BNA from a directory which is our current root folder.

![Image](https://cdn-media-1.freecodecamp.org/images/0*MiI9-KZeQWmuhf1V)

**NOTE:** The BNA name and version come from the `package.json` file. When you add more code, you should change the version number there to deploy unique archives capable of upgrading existing business networks.

#### 6. **Install and Deploy the BNA file**

We can install and deploy the network to our local Fabric runtime using the `PeerAdmin` user. To install the business network, type

`composer network install --archiveFile cards-trading-network@0.0.1.bna --card PeerAdmin@hlfv1`

![Image](https://cdn-media-1.freecodecamp.org/images/0*nOI-6kbYiD76HuzM)

To deploy the business network, type

`composer network start --networkName cards-trading-network --networkVersion 0.0.1 --networkAdmin admin --networkAdminEnrollSecret adminpw --card PeerAdmin@hlfv1 --file cards-trading-admin.card`

![Image](https://cdn-media-1.freecodecamp.org/images/0*o5dJtBPYS0YsqaH-)

The `networkName` and `networkVersion` must be the same as specified in your `package.json` otherwise it won’t work.

`--file` takes the name of the file to be created for THIS network’s business card. This card then needs to be imported to be usable by typing

`composer card import --file cards-trading-admin.card`

![Image](https://cdn-media-1.freecodecamp.org/images/0*7ONVFnE8dQGxMFG6)

Amazing. We can now confirm that our network is up and running by typing

`composer network ping --card admin@cards-trading-network`

`--card` this time takes the admin card of the network we want to ping.

If everything went well, you should see something similar to this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*5EE453FFFQp4O0LO3PIg5Q.png)
_**Your network version will be 0.0.1 or whatever your package.json specifies —** I actually forgot to take this screenshot and uploaded it after I was done writing the tutorial and making edits_

### Testing our Business Network

Now that our network is up and running on Fabric, we can start Composer Playground to interact with it. To do this, type `composer-playground` in Terminal and open up `[http://localhost:8080/](http://localhost:8080/)` in your browser and you should see something similar to this:

![Image](https://cdn-media-1.freecodecamp.org/images/0*QX21rhAmdnKKwEZJ)

Press Connect Now for `admin@cards-trading-network` and you’ll be greeted with this screen:

![Image](https://cdn-media-1.freecodecamp.org/images/0*3VAwop80uPvM8sYb)

The **Define** page is where we can make changes to our code, deploy those changes to upgrade our network, and export business network archives.

Head over to the **Test** page from the top menu, and you’ll see this:

![Image](https://cdn-media-1.freecodecamp.org/images/0*Ba4OQmMecPDEsaQU)

Select `Trader` from Participants, click on **Create New Participant** near the top right, and make a new `Trader` similar to this:

![Image](https://cdn-media-1.freecodecamp.org/images/0*UjUZmOLt9tOfpDOB)

Go ahead and make a couple more `Trader`s. Here are what my three traders look like with the names Haardik, John, and Tyrone.

![Image](https://cdn-media-1.freecodecamp.org/images/0*HPPva_cp92xBKtxy)

Now, let’s make some Assets. Click on `TradingCard` from the left menu and press **Create New Asset**. Notice how the `owner` field is particularly interesting here, looking something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/0*Q_ZmrJorW6RcUxUe)

This is a relationship. This is what the `--&`gt; means. We specify the exact resource type followed by their unique identifier and voila, we have a relationship pointer.

Go ahead and finish making a `TradingCard` something similar to this:

![Image](https://cdn-media-1.freecodecamp.org/images/0*A7wT8ywp1aO63Eo4)

Notice how the `owner` fields points to `Trader#1` aka `Haardik` for me. Go ahead and make a couple more cards, and enable a couple to have `forTrade` set to true.

![Image](https://cdn-media-1.freecodecamp.org/images/0*wMA5-OcEJnbyEAPg)

Notice how my `Card#2` has `forTrade == true`?

Now for the fun stuff, let’s try trading cards :D

Click on **Submit Transaction** in the left and make `card` point to `TradingCard#2` and `newOwner` point to `Trader#3` like this:

![Image](https://cdn-media-1.freecodecamp.org/images/0*GAb88nhGlD2xPRm9)

Press **Submit** and take a look at your `TradingCard`s, you’ll see that `Card#2` now has owner `Trader#3` :D

### Generating a REST API Server

Doing transactions with Playground is nice, but not optimal. We have to make client-side software for users to provide them a seamless experience, they don’t even have to necessarily know about the underlying blockchain technology. To do so, we need a better way of interacting with our business network. Thankfully, we have the `composer-rest-server` module to help us with just that.

Type `composer-rest-server` in your terminal, specify `admin@cards-trading-network` , select **never use namespaces**, and continue with the default options for the rest as follows:

![Image](https://cdn-media-1.freecodecamp.org/images/0*VukFOTRBvtOMeGRG)

Open `[http://localhost:3000/explorer/](http://localhost:3000/explorer/)` and you’ll be greeted with a documented version of an automatically generated REST API :D

### Generating an Angular application which uses the REST API

Remember the `yo hyperledger-composer` generator? It can do more than generating a business network. It can also create an Angular 4 application running against the REST API we created above.

To create the Angular web application, type `yo hyperledger-composer` in your Terminal, select Angular, choose to connect to an existing business network with the card `admin@cards-trading-network`, and connect to an existing REST API as well. (**Edit:** Newer versions of the software may ask for the card file instead of just the name of the card)

![Image](https://cdn-media-1.freecodecamp.org/images/0*WkNRiy0grt6DD_M5)

This will go on to run `npm install` , give it a minute, and once it’s all done you’ll be able to load up `[http://localhost:4200/](http://localhost:4200/)` and be greeted with a page similar to this:  
**Edit:** Newer versions of the software may require you to run `npm install` yourself and then run `npm start`

![Image](https://cdn-media-1.freecodecamp.org/images/0*1GrawK-jGkN9cvqO)

You can now play with your network from this application directly, which communicates with the network through the REST server running on port 3000.

Congratulations! You just set up your first blockchain business network using Hyperledger Fabric and Hyperledger Composer :D

You can add more features to the cards trading network, setting prices on the cards and giving a balance to all `Trader`. You can also have more transactions which allow the `Trader`s to toggle the value of `forTrade` . You can integrate this with non blockchain applications and allow users to buy new cards which get added to their account, which they can then further trade on the network.

The possibilities are endless, what will you make of them? Let me know in the comments :D

### KNOWN BUG: Does your Angular web app not handle Transactions properly?

At the time of writing, the angular generator has an issue where the purple Invoke button on the Transactions page doesn’t do anything. To fix this, we need to make a few changes to the generated angular app.

![Image](https://cdn-media-1.freecodecamp.org/images/0*owNwB2hjvpxTSvxE)

#### **1. Get a modal to open when you press the button**

The first change we need to make is have the button open the modal window. The code already contains the required modal window, the button is just missing the `(click)` and `data-target` attributes.

To resolve this, open up `/cards-trading-angular-app/src/app/**TradeCard/TradeCard.component.html**`

The file name can vary based on your `transaction` name. If you have multiple `transaction`s in your business network, you’ll have to do this change across all the transaction resource type HTML files.

Scroll down till the very end and you shall see a `<butt`on> tag. Go ahead and add these two attributes to that tag:

`(click)="resetForm();" data-target="#addTransactionModal"`

so the line looks like this:

`<button type=”button” class=”btn btn-primary invokeTransactionBtn” data-toggle=”modal” (click)=”resetForm();” data-target=”#addTransactionModal”>Invoke<`;/button>

The `(click)` attribute calls `resetForm();` which sets all the input fields to empty, and `data-target` specifies the modal window to be opened upon click.

Save the file, open your browser, and try pressing the invoke button. It should open this modal:

![Image](https://cdn-media-1.freecodecamp.org/images/0*9Q6opS0G8rrwk4YA)

#### 2. **Removing unnecessary fields**

Just getting the modal to open isn’t enough. We can see it requests `transactionId` and `timestamp` from us even though we didn’t add those fields in our modeling file. Our network stores these values which are intrinsic to all transactions. So, it should be able to figure out these values on it’s own. And as it turns out, it actually does. These are spare fields and we can just comment them out, the REST API will handle the rest for us.

In the same file, scroll up to find the input fields and comment out the divs responsible for those input fields inside `addTransactionModal`

![Image](https://cdn-media-1.freecodecamp.org/images/1*EogUHWeTnXKV-EkmjXP7Pw.png)

Save your file, open your browser, and press Invoke. You should see this:

![Image](https://cdn-media-1.freecodecamp.org/images/0*W2O1PD-7qW0a-f2v)

You can now create transactions here by passing data in these fields. Since `card` and `newOwner` are relationships to other resources, we can do a transaction like this:

![Image](https://cdn-media-1.freecodecamp.org/images/0*lRrhv1lZIgFSggbY)

Press **Confirm**, go back to the **Assets** page, and you will see that `TradingCard#2` now belongs to `Trader#1`:

![Image](https://cdn-media-1.freecodecamp.org/images/0*teBdk1zFVR2hj2Tx)

Congratulations! You have successfully built and deployed a blockchain business network on Hyperledger Fabric. You also generated a REST API server for that network and learnt how to make web apps which interact with that API.

If you have any questions or doubts, drop it in the comments and I will get back to you.  
Email: hhaardik@uwaterloo.ca  
LinkedIn: [https://www.linkedin.com/in/haardikkk](https://www.linkedin.com/in/haardikkk)

