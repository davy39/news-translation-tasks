---
title: npm Cheat Sheet - Most Common Commands and nvm
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/npm-cheat-sheet-most-common-commands-and-nvm
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cf7740569d1a4ca3523.jpg
tags:
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'npm or the Node Package Manager, is one of the most used tools for any
  Node.js developer. Here''s a list of the most common commands you''ll use when working
  with npm.

  Install package.json dependencies

  npm install


  Shorthand

  # install

  npm i <package>


  ...'
---

`npm` or the Node Package Manager, is one of the most used tools for any Node.js developer. Here's a list of the most common commands you'll use when working with `npm`.

## **Install `package.json` dependencies**

```shell
npm install
```

### Shorthand

```shell
# install
npm i <package>

# uninstall
npm un <package>

# update
npm up <package>
```

### Flags

`-S` is the same as `--save`, and `-D` is the same as `--save-dev`.

## **List globally installed packages**

```shell
npm list -g --depth=0
```

## **Uninstall global package**

```shell
npm -g uninstall <name> 
```

## **Upgrade `npm` on Windows**

```shell
npm-windows-upgrade
```

## **Update global packages**

To see which packages need updating, use:

```shell
npm outdated -g --depth=0
```

To update global packages individually you can use:

```shell
npm update -g <package> <package> <package>
```

## **list available scripts to run**

```shell
npm run
```

## **Update `npm`**

```shell
npm install -g npm@latest

# using windows? Then use
npm-windows-upgrade
```

## **Installed version**

```shell
npm list # for local packages
```

## **Node Version Manager `nvm`**

`nvm` makes it easy to switch between different versions of Node.js. Read more about it on the project's [GitHub page](https://github.com/nvm-sh/nvm).

Once you have `nvm` installed, if you want to install the latest version of Node v12 just run:

```shell
nvm install 12
```

If you have multiple versions of Node.js installed on your workspace, you can switch to a specific version by writing:

```shell
nvm use 10.19.0
```

### **Make a Node version default**

In order to set a default version of Node for your workspace, just type:

```shell
nvm alias default 12
```

Where the latest version of 12 is the version you want to be used by default.

### Update `npm`

If you use Node installed through `nvm`, it's good practice to update your version of `npm` with this command:

```shell
nvm install-latest-npm
```

## More information:

* [These NPM tricks will make you a pro](https://www.freecodecamp.org/news/10-npm-tricks-that-will-make-you-a-pro-a945982afb25/)
* [How to Install Node.js and npm on Windows](https://www.freecodecamp.org/news/how-to-install-node-js-and-npm-on-windows/)
* [npm vs npx — What’s the Difference?](https://www.freecodecamp.org/news/npm-vs-npx-whats-the-difference/)

