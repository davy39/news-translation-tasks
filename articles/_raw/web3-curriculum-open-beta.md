---
title: freeCodeCamp's Web3 Curriculum Open Beta – And How to Run it
subtitle: ''
author: Tom Mondloch
co_authors: []
series: null
date: '2022-09-21T14:45:56.000Z'
originalURL: https://freecodecamp.org/news/web3-curriculum-open-beta
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/thomas-habr-wprOCzLIEYI-unsplash.jpg
tags:
- name: Blockchain
  slug: blockchain
- name: Web3
  slug: web3
seo_title: null
seo_desc: 'Update January 2023: The first group of projects is now fully available.
  The "Available interactive projects" section has been added to list the completed
  practice projects. The newly available projects are "Learn Digital Ledgers by Building
  a Blockc...'
---

_Update January 2023: The first group of projects is now fully available. The ["Available interactive projects"](#heading-available-interactive-projects) section has been added to list the completed practice projects. The newly available projects are "Learn Digital Ledgers by Building a Blockchain", "Learn Proof of Work Consensus by Building a Block Mining Algorithm", and "Learn Digital Signatures by Building a Wallet"._

Over the past 11 months, we've made considerable progress on our Web3 curriculum. Today I'm thrilled to say that parts of this curriculum are now in open beta. You can try them today.

Before we get into the details, I want to thank the KaijuKingz community, who made a donation to freeCodeCamp that made development of these courses possible. You can [read more about their gift to the freeCodeCamp community here](https://www.freecodecamp.org/news/carbon-neutral-web3-curriculum-plans/).

## How to Approach These Web3 Courses

As a prerequisite for this course, we recommend first learning full stack web development. You can do this by working through the first 7 [freeCodeCamp certifications](https://www.freecodecamp.org/learn/) and building their projects:

1. [Responsive Web Design](https://www.freecodecamp.org/learn/2022/responsive-web-design/)
1. [JavaScript Algorithms and Data Structures](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/)
1. [Front End Development Libraries](https://www.freecodecamp.org/learn/front-end-development-libraries/)
1. [Data Visualization](https://www.freecodecamp.org/learn/data-visualization/)
1. [Relational Database](https://www.freecodecamp.org/learn/relational-database/)
1. [Back End Development and APIs](https://www.freecodecamp.org/learn/back-end-development-and-apis/)
1. [Quality Assurance](https://www.freecodecamp.org/learn/quality-assurance/)

We also recommend you know some knowledge of basic blockchain development concepts. freeCodeCamp has [an in-depth 32-hour course that covers this](https://www.freecodecamp.org/news/learn-blockchain-solidity-full-stack-javascript-development/), taught by developer and instructor Patrick Collins.

We also recommend learning some Rust, which you can learn interactively using [freeCodeCamp's Rust course](https://www.freecodecamp.org/news/rust-in-replit/).

Again, these prerequisites are just our recommendations. Feel free to just dive in and return to those resources as you see fit.

Right now, we have designed five integrated Web3 projects for you to complete:

1. Build a Video Game Marketplace Blockchain
1. Build a Fundraising Smart Contract
1. Build a Peer-to-Peer Network
1. Build a Web3 Client-Side Package for your dApp
1. Build a Smart Contract in Rust

Each of these projects has its own set of instructions with tasks for you to fulfill, and tests to ensure you've implemented your project correctly. Complete all the tasks and get all the tests to pass to finish each project.

## These 5 projects are just the beginning

We are also developing 10 interactive Web3 practice projects.

These will walk you through all the Web3 concepts you need to know to build these 5 integrated projects we're releasing today. 

Why are we releasing the hard part (the 5 integrated projects) first? For the die-hard Web3 enthusiasts who don't mind using watching [Patrick's course](https://www.freecodecamp.org/news/learn-blockchain-solidity-full-stack-javascript-development/), reading official documentation, and referencing the many other free Web3 tutorials out there.

Soon it will be a smoother ride for anyone to learn these tools and concepts. But we wanted to first get something out there for the hardcore crowd.

## Available interactive projects

As of January 2023, the first group of interactive practice projects is now fully available. They will teach you the concepts you need to know to complete the first integrated project. The new courses are:

1. Learn Digital Ledgers by Building a Blockchain
1. Learn Proof of Work Consensus by Building a Block Mining Algorithm
1. Learn Digital Signatures by Building a Wallet

## The Web3 Curriculum is in open beta. We welcome your feedback and bug reports.

Note that these are in open beta – meaning that we will continue to refine them with your feedback.

You can help by joining our new [Web3 Curriculum Discord server](https://discord.gg/9KngwWzvd4), introducing yourself, and helping other people who get stuck trying to build these 5 integrated projects.

You can also sign up for updates These will make it a lot easier to build these 5 integrated projects So in a way, you actually doing the hardest, most ambiguos  part [Sign up for updates below](#heading-sign-up-for-updates) for when new courses are released.

## How will it work?

The courses will run in a docker container using VS Code and the [freeCodeCamp Courses extension.](https://marketplace.visualstudio.com/items?itemName=freeCodeCamp.freecodecamp-courses)

### Here's a sample

%[https://www.youtube.com/watch?v=EAidlZ6FZwE]

## How to Run the Courses

Follow the steps below to run the courses

### Developer Environment Prerequisites
Before you get started, make sure you have these installed on your computer:

1. [Docker Engine](https://docs.docker.com/engine/)
1. [VS Code](https://code.visualstudio.com/download) and the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension
1. Git

### How to Run the Curriculum in Docker
Follow these instructions to clone the repo and run the courses:

1. Open a terminal and clone the [web3-curriculum](https://github.com/freeCodeCamp/web3-curriculum) repo with:
```console
git clone https://github.com/freeCodeCamp/web3-curriculum.git
```
2. Navigate to the `web3-curriculum` directory, and open it in a VSCode workspace with:
```console
code .
```

3. Press `Ctrl / Cmd + Shift + P` to open the command palette, and run `Dev Containers: Rebuild Container and Reopen in Container`. VS Code will build the container to run the projects in, it will take a few minutes the first time.
4. Once it's finished, press `Ctrl / Cmd + Shift + P` again and run `freeCodeCamp: Run Course` to start the courses. This will also take a moment.
5. The simple browser will open when it's done. If it's a blank white page, use the refresh button to update it and see the courses home page.
6. Click on one of the available projects to start a project.
7. Follow the instructions to complete the project.
8. Have fun!

If you want to switch projects, click the freeCodeCamp logo at the top to get back to the home page.

<h2 id="sign-up">Sign up for updates</h2>

Fill out [this google form](https://docs.google.com/forms/d/e/1FAIpQLSdaKRd34e36eGVA7ne1g1x3kLPjTbLF0YoNqLWH6L7P2AmpxA/viewform?usp=sf_link) to receive updates when new courses are released.


## Other Courses
We are also creating courses around the Solana and NEAR protocols.

View the [Solana announcement article.](https://www.freecodecamp.org/news/solana-curriculum/)
View the [NEAR announcement article.](https://www.freecodecamp.org/news/near-curriculum/)

Or, check out the [web3.freecodecamp.org](https://web3.freecodecamp.org/) domain where we showcase all the courses.


