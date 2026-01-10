---
title: Learn Truffle and Ganache – How to Create and Deploy a Smart Contract
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-20T16:08:22.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-truffle
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/ff-2.png
tags:
- name: Blockchain
  slug: blockchain
- name: Smart Contracts
  slug: smart-contracts
seo_title: null
seo_desc: "By Jagruti Tiwari\nLearning a new technology often means learning a new\
  \ framework, programming language, IDE, or deployment method. And the blockchain\
  \ is no different. \nIn this tutorial, I am going to show you how to get started\
  \ with Truffle, a Node.j..."
---

By Jagruti Tiwari

Learning a new technology often means learning a new framework, programming language, IDE, or deployment method. And the blockchain is no different. 

In this tutorial, I am going to show you how to get started with [Truffle](https://trufflesuite.com/docs/vscode-ext/installation-guide/), a Node.js blockchain framework, in Visual Studio Code.

# How to Install Truffle
To install Truffle you need to have [Node and NPM](https://nodejs.org/en/download/) along with [Python](https://www.python.org/downloads/) setup on your machine. 

If you do not have them already, you can install them from their official websites ([Node](https://nodejs.org/en/) and [Python](https://www.python.org/)). Once you're done with that, you are all set to install Truffle.

We will use npm to install Truffle. Enter the following command in your command prompt:

`npm install -g truffle`

![Screenshot-2022-07-16-190328](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-190328.png)

While the installation runs, if you come across the following error, I have got you covered:

`gyp ERR! stack Error: Could not find any Visual Studio installation to use`

Google shows a bunch of solutions for the above error. What actually worked for me was installing [Visual Studio](https://visualstudio.microsoft.com/downloads/) along with 'Desktop Development with C++'.

After you download Visual Studio and run the installer you will see the following screen:

![Screenshot-2022-07-16-190639](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-190639.png)

Under the 'Desktop and mobile' section, check 'Desktop Developement with C++' and continue with the installation process.

Once this is done you can run the Truffle installation command again.

To verify if Truffle is installed successfully, run:

`truffle version` 

in your command prompt. You should see an output like the image below:

![Screenshot-2022-07-17-201823](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-17-201823.png)

Congratulations! You have installed Truffle.

# How to Use Truffle in Visual Studio Code 

Visual Studio Code comes with it's own extension for Truffle. We will install it to make our work easier. 

![Screenshot-2022-07-16-191633](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-191633.png)

In the marketplace search bar, type "Truffle for VS Code" and click on install (similar to the image below).

![Screenshot-2022-07-16-191836](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-191836.png)

VS Code requires you to have other extensions for it to work, so just check the ones you don't have installed and continue the setup:
![Untitled](https://www.freecodecamp.org/news/content/images/2022/07/Untitled.png)

If you do not see the Truffle logo in the left bar you might have to restart VS Code.

# How to Set Up Ganache in VS Code
Ganache comes with the Truffle suite to deploy DApps. 

Click on the 'Networks' > 'Create a new network' in Truffle explorer.

![Screenshot-2022-07-16-195911](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-195911.png)

From the dropdown box select 'Ganache service'. 

![Screenshot-2022-07-16-195943](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-195943.png)

Select type 'local' or 'fork'. Since this a local setup I will select 'local'.

![Screenshot-2022-07-16-200019](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-200019.png)

Next, you will be asked to enter your 'local project's name'. Enter any name of your choice and hit enter. 

![Screenshot-2022-07-16-200046](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-200046.png)

Your network setup is complete. 

![Screenshot-2022-07-16-200242](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-200242.png)

To start the network, right click on the network name and click on 'Start Ganache'.

When you start the Ganache service, you will see a command line output as follows:
![Screenshot-2022-07-16-200504](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-200504.png)

The output displays a set of things to speed up. We do not need to worry about them just yet. 

# How to Start a Tuffle Project
To start a project in Truffle, go into a directory and type the init command.

`truffle init`

![Screenshot-2022-07-16-193451](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-193451.png)

This will create a new Truffle project.

# How to Create a Contract in Truffle
The following commands creates a contract in Truffle:

`truffle create contract <contract name>`

![Screenshot-2022-07-16-202855](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-202855.png)

Here we created a contract named 'SimpleStorage'.

# How to Run Tests in Truffle
To run test in Truffle, just enter this command:

`truffle test` 

![Screenshot-2022-07-17-171254](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-17-171254.png)

All the tests will be run one by one.
# How to Deploy in Truffle

We will use Ganache to deploy in Truffle. 

`truffle develop` 

You use the above command to start the deployment process.

Ganache has some accounts and private key ready for this purpose.

![Screenshot-2022-07-17-171755](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-17-171755.png)

In the above image at the bottom you will see `truffle (develop)>` console.

![Screenshot-2022-07-17-172106](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-17-172106.png)

Type `migrate --reset` in the console.

![Screenshot-2022-07-17-172204](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-17-172204.png)

You will see that the initial migrations are made and the deployment process starts. In the end you will get a summary (the cost and number of deployments) of the deployment.

# Conclusion
We progress more quickly when we can learn from each other's mistake. I have just started learning Blockchain, and it took me a while to get the setup running. So here I am sharing my findings. Happy learning!


