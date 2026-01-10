---
title: How to Install Node.js on Ubuntu and Update npm to the Latest Version
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-30T18:18:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-node-js-on-ubuntu-and-update-npm-to-the-latest-version
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Slice-3-2-.jpg
tags:
- name: node js
  slug: node-js
- name: npm
  slug: npm
- name: Ubuntu
  slug: ubuntu
seo_title: null
seo_desc: "By Adebola Adeniran\nIf you try installing the latest version of node using\
  \ the apt-package manager, you'll end up with v10.19.0. This is the latest version\
  \ in the ubuntu app store, but it's not the latest released version of NodeJS. \n\
  This is because ..."
---

By Adebola Adeniran

If you try installing the latest version of node using the apt-package manager, you'll end up with **v10.19.0**. This is the latest version in the ubuntu app store, but it's not the latest released version of NodeJS. 

This is because when new versions of a software are released, it can take months for the Ubuntu team to test and release in the official Ubuntu store. As a result, to get the latest versions of any software, we may have to use private packages published by developers.

In this tutorial, what we want to do is get either **v12.18.1** (LTS - with Long term support) or **v14.4** of Node. To get the latest versions, we can use either **nodesource** or **nvm** (node version manager). I'll show you how to use both.

All commands here will be run using the Ubuntu CLI/terminal.

## Using NVM - my preferred method

I like nvm because it allows me use different node versions for different projects.  
Sometimes, you may be collaborating on a project with someone using a different version of node and you need to switch node versions to what the project requires. For this, nvm is the best tool.

## Install NVM

`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash`

To check that nvm is installed, type `nvm --version`. If you get a version number back like `0.35.3`, then you know nvm was successfully installed.

**Restart your terminal for your changes to take effect.**

## Install NodeJS

Next, let's install Nodejs version 14.4. 

Simply run `nvm install 14.4.0` .

You can use a similar command to install any version of node you want, for example `nvm install 12.18.1`.

This command automatically installs **nodejs** as well as the latest **npm** version which is at  `v6.14.5`.

If you ever need to switch node versions, you can simply run `nvm use <version-number>` , for example `nvm use v12.18.1`.

To list the different node versions you have installed with nvm, run `nvm ls`.

## Install Nodesource

Run the command below to tell Ubuntu that we want to install the Nodejs  
package from nodesource.

`curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -`

**NB** that v14.4.0 is the latest version of Node but doesn't currently have LTS - long term support provided for it. To install the latest version of Node with LTS, change `14` in the command above to `12`.

You may be prompted to enter the password for your root user. Enter that and hit enter/return.

## Install NodeJS

Once we're done setting up Nodesource, we can now install Nodejs v14.4.  
Run `sudo apt-get install -y nodejs`.

Once we're done, we can check that we have the latest version of Node installed.  
Simply type `nodejs -v` into your terminal and it should return `v14.4.0`.

You should have npm automatically installed at this point. To check what npm version you have, run `npm version`. If you do not get an object that includes the latest version of npm at 6.14.5, `{ npm: '6.14.5' }`, then you can update npm manually by running the following command:

 `npm install -g npm@latest`.

If you run into any issues with npm being unable to update because it's not installed, you can install npm first by using `sudo apt-get install -y npm`, then run the command above to update it.

For certain npm packages to run, we also need to run the command below  
`sudo apt install build-essential`.

And that's it!

You've got the latest versions of NodeJS and NPM on your Ubuntu machine.

Go build great products :)

