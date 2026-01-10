---
title: How to Update Node and NPM to the Latest Version
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-12T20:28:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-update-node-and-npm-to-the-latest-version
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-markus-winkler-4052195.jpg
tags:
- name: node js
  slug: node-js
- name: npm
  slug: npm
- name: 'update '
  slug: update
seo_title: null
seo_desc: "By Dillion Megida\nNode is a runtime environment that allows developers\
  \ to execute JavaScript code outside the browser, on the server-side. \nNPM, on\
  \ the other hand, is a package manager for publishing JavaScript packages (also\
  \ known as Node modules) t..."
---

By Dillion Megida

Node is a runtime environment that allows developers to execute JavaScript code outside the browser, on the server-side. 

NPM, on the other hand, is a package manager for publishing JavaScript packages (also known as Node modules) to the [npm registry](https://www.npmjs.com/). You can also use it to install packages to your applications.

To install Node, you have to go to the [Nodejs website](https://nodejs.org/en/) to download the installer. After downloading, you can run the installer, follow the steps, agree to the terms and conditions, and have the installer on your device.

When you install Node, you also get the `npm` CLI which you can use to manage packages in your applications.

However, Node and NPM can be updated separately to their latest versions, and in the rest of this article, I'll show you how.

## How to Update Node

### 1. Use NPM to Update Your Node Version
To update Node with NPM, you will install the [n](https://www.npmjs.com/package/n) package, which will be used to interactively manage node versions on your device.

Here are the steps:

#### Clear the NPM cache
When you install dependencies, some modules are cached to improve the speed of installation in subsequent downloads. So first, you want to clear the NPM cache.

#### Install n

```shell
npm install -g n
```

You'll need to install this package globally as it manages the Node versions at the root.

#### Install a new version of Node

```shell
n lts
n latest
```

The two commands above install the long-term support and latest versions of Node.

#### Remove previously installed versions

```shell
n prune
```

This command removes the cached versions of the previously installed versions and only keeps the latest installed version.


### 2. Use NVM to Update Your Node Version
NVM stands for Node Version Manager, and as the name implies, it helps you manage your Node Versions. With NVM, you can install Node versions and specify the version of Node that a project uses.

NVM makes it easy to test projects across various Node versions.

To update a Node Version with NVM, you have to install NVM first.

Here is the [installation guide](https://github.com/nvm-sh/nvm#installing-and-updating) for NVM.

When installed, you can install packages with:

```shell
nvm install [version]
```

You can install the latest version with:

```shell
nvm install node
```

And uninstall other versions with:

```shell
nvm uninstall [version]
```

With many versions installed, you may also want to specify the version to use at a particular time. One way to do this is by setting a default alias like this:

```shell
nvm alias default [version]
```

This way, Node executions will run with the specified version.


### 3. Download Updated Node Binaries
And you can also get the latest versions from the [Node.js](https://nodejs.org/en/) website. On it, you can find the latest and long-term support versions for your device.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-7.png)
_Node.js downloads page_

Downloading the latest version also gives you the latest version of NPM.

## How to Update NPM

Just as you use NPM to update packages, you can use NPM to update itself. Here's the command to achieve this:

```shell
npm install -g npm@latest
```

This command will install the latest version of NPM globally.

On Mac, you may have to pass the `sudo` command before NPM, as this installs NPM at the root of your device, and you need privileges to do that.

## Conclusion

In this article, we've seen how to update Node and NPM to their latest versions.

To reiterate, when you install Node, you automatically get NPM. If you also update Node by installing the binaries from the website, you get an updated NPM.

We also saw other ways to update Node and NPM globally on your device.


