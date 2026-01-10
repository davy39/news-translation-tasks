---
title: Node Version Manager – NVM Install Guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-09T18:23:56.000Z'
originalURL: https://freecodecamp.org/news/node-version-manager-nvm-install-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/install-nvm.png
tags:
- name: node
  slug: node
seo_title: null
seo_desc: "By Dillion Megida\nIn this article, I'll explain how you can install NVM,\
  \ or Node Version Manager, on Windows, Linux, and Mac.\nWhat is NVM?\nNode Version\
  \ Manager (NVM), as the name implies, is a tool for managing Node versions on your\
  \ device. \nDifferen..."
---

By Dillion Megida

In this article, I'll explain how you can install NVM, or Node Version Manager, on Windows, Linux, and Mac.

## What is NVM?

Node Version Manager (NVM), as the name implies, is a tool for managing Node versions on your device. 

Different projects on your device may be using different versions of Node. Using only one version (the one installed by `npm`) for these different projects may not give you accurate execution results.

For example, if you use a Node version of **10.0.0** for a project that uses **12.0.0**, you may get some errors. And if you update the Node version to **12.0.0** with npm, and you use it for a project that uses **10.0.0**, you may not get the expected experience. 

In fact, you would most likely get a warning that says:

```bash
This project requires Node version X
```

Instead of using npm to install and uninstall Node versions for your different projects, you can use **nvm**, which helps you effectively manage your node versions for each project.

[NVM](https://github.com/nvm-sh/nvm) allows you to install different versions of Node, and switch between these versions depending on the project that you're working on via the command line.

In the next sections, I'll show you how to install NVM on your Windows, Linux, or Mac device.

Before proceeding, I also recommend that you uninstall Node.js if you have it installed already so that you do not have any conflicts with Node.js and nvm.

## How to Install NVM on Windows

NVM is mostly supported on Linux and Mac. It doesn't have support for Windows. But there's a similar tool created by coreybutler to provide an nvm experience in Windows called [nvm-windows](https://github.com/coreybutler/nvm-windows).

`nvm-windows` provides a management utility for managing Node.js versions in Windows. Here's how to install it:

### 1. Click on "Download Now"

In the [nvm-windows repository Readme](https://github.com/coreybutler/nvm-windows#readme), click on "Download Now!":

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-338.png)

This will open a page showing different NVM releases.

### 2. Install the .exe file of the latest release

In the latest release (which as of the time of writing this is [1.1.9](https://github.com/coreybutler/nvm-windows/releases/tag/1.1.9)), you'll find different assets. Click on the **nvm-setup.exe** asset which is the installation file for the tool:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-340.png)

### 3. Complete the Installation Wizard

Open the file that you have downloaded, and complete the installation wizard.

When done, you can confirm that nvm has been installed by running:

```bash
nvm -v
```

If nvm was installed correctly, this command will show you the nvm version installed.

## How to Install NVM on Linux and Mac

Since Linux and Mac have some similarities (they are both UNIX-based OSes), you can install nvm on them in similar ways.

### 1. Run the nvm installer

In your terminal, run the nvm installer like this:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

# or

wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
```

You can use `curl` or `bash` depending on the command available on your device.

These commands will clone the nvm repository to a `~/.nvm` directory on your device.

### 2. Update your profile configuration

The installation process from step 1 should also automatically add the nvm configuration to your profile. If you're using zsh, that would be `~/.zshrc`. If you're using bash, that would be `~/.bash_profile`...or some other profile.

If it doesn't automatically add nvm configuration, you can add it yourself to your profile file:

```bash
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

This command above loads nvm for use.

### 3. Reload the shell configuration

With your profile configuration updated, now you will reload the configuration for your terminal to use:

```bash
source ~/.bashrc
```

With this command executed, nvm is ready for you to use. You can confirm that nvm is installed correctly by running:

```bash
nvm -v
```

This should show the version of nvm installed.

## Wrapping up

With nvm installed, you can now install, uninstall, and switch between different Node versions in your Windows, Linux, or Mac device.

You can install Node versions like this:

```bash
nvm install latest
```

This command will install the last version of Node:

```bash
nvm install vX.Y.Z
```

This will install the `X.Y.Z` Node version.

You can also make a version your default by running:

```bash
nvm alias default vX.Y.Z
```

And if you want to use a specific version at any point, you can run the following in your terminal:

```bash
nvm use vA.B.C
```

NVM makes it easier to manage multiple versions of Node.js across different projects that require different versions.


