---
title: NVM for Windows – How to Download and Install Node Version Manager in Windows
  10
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-08-11T16:00:37.000Z'
originalURL: https://freecodecamp.org/news/nvm-for-windows-how-to-download-and-install-node-version-manager-in-windows-10
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/nvmWindows.png
tags:
- name: node
  slug: node
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: Windows
  slug: windows
seo_title: null
seo_desc: 'Different software development tools might require specific versions of
  Node.js and NPM (Node Package Manager). NPM is a tool for managing packages installed
  from the NPM registry.

  In addition, if you are making an NPM package, you might need to test...'
---

Different software development tools might require specific versions of Node.js and NPM (Node Package Manager). NPM is a tool for managing packages installed from the NPM registry.

In addition, if you are making an NPM package, you might need to test it with different versions of Node.js. This is why you should have NVM installed.

NVM, short for Node Version Manager, is a command line tool for managing and switching to different versions of Node.js.

In this article, I will show you how to download and install NVM on Windows 10 – even though there’s no “NVM” for Windows.

I will also show you how to set up and use different versions of Node.js and NPM on your Windows computer.

## What We'll Cover
- [How to Download and Install Node Version Manager in Windows 10](#heading-how-to-download-and-install-node-version-manager-in-windows-10)
  - [Follow the steps below to download nvm-windows](#heading-follow-the-steps-below-to-download-nvm-windows)
- [How to Use NVM on Windows 10](#heading-how-to-use-nvm-on-windows-10)
  - [How to Install Different Versions of Node.js and NPM with NVM](#heading-how-to-install-different-versions-of-nodejs-and-npm-with-nvm)
- [Recap](#heading-recap)

## How to Download and Install Node Version Manager in Windows 10

As I mentioned earlier, there’s no “NVM” for Windows, as NVM is only supported on Linux and Mac. 

What you will be using on your Windows machine is “nvm-windows”. nvm-windows is similar to NVM, but not identical to it.

**N.B.**: If you have Node.js installed already, you need to uninstall it so it doesn’t lead to errors when using different versions of Node and installing packages from the NPM registry. 

Restart your PC after that, open the command prompt or PowerShell, and run `node -v` to confirm Node has been uninstalled.

![ss1-2](https://www.freecodecamp.org/news/content/images/2022/08/ss1-2.png)

In addition, if you have yarn installed, uninstall it and reinstall it after installing NVM. You don’t want to get weird errors while installing and using packages from the NPM registry.

### Follow the steps below to download nvm-windows

- **Step 1**: Head over to the [nvm-windows repository](https://github.com/coreybutler/nvm-windows#installation--upgrades) and click on Download Now!”
![ss2-2](https://www.freecodecamp.org/news/content/images/2022/08/ss2-2.png)

You’ll be taken to a page containing different versions of nvm-windows.

- **Step 2**: Click on the latest version to download it. For now, it is the April 28, 2022 version.
![ss3-2](https://www.freecodecamp.org/news/content/images/2022/08/ss3-2.png)

- **Step 3**: Locate the installer on your computer and open it. Follow the installation wizard to install it.
![ss4-2](https://www.freecodecamp.org/news/content/images/2022/08/ss4-2.png)
![ss5-3](https://www.freecodecamp.org/news/content/images/2022/08/ss5-3.png)

- **Step 4**: Open up PowerShell or Command Prompt and run `nvm -v` to confirm the installation.
![ss6-2](https://www.freecodecamp.org/news/content/images/2022/08/ss6-2.png)

If you get the same message I got above, then nvm-windows has been successfully installed. Congrats!

## How to Use NVM on Windows 10

To use NVM, you need to open PowerShell or Command Prompt as an admin. You can also use Git bash.

- To open PowerShell as admin, right-click on Start and select “PowerShell (Admin)”.
![powershell-admin](https://www.freecodecamp.org/news/content/images/2022/08/powershell-admin.png)

- To open Command Prompt as admin, search for “cmd” and select “Open as Administrator” on the right.
![cmd-admin](https://www.freecodecamp.org/news/content/images/2022/08/cmd-admin.png)


### How to Install Different Versions of Node.js and NPM with NVM
The superpower NVM gives you is the ability to have multiple versions of Node.js installed on your machine. 

To install the latest version of Node, run `nvm install latest`.
![ss7-1](https://www.freecodecamp.org/news/content/images/2022/08/ss7-1.png)

It is always better to install the long-term support (LTS) version of Node because it is less buggy.

To install the LTS version of Node, run `nvm install lts`.
![ss8-1](https://www.freecodecamp.org/news/content/images/2022/08/ss8-1.png)

To install a specific version of Node, you need to run `nvm list available` first so you can see the versions of Node that are available.
![ss9-1](https://www.freecodecamp.org/news/content/images/2022/08/ss9-1.png)

To install that specific version, run `nvm install node-version-number`. For example, `nvm install 14.20.0`.
![ss10-1](https://www.freecodecamp.org/news/content/images/2022/08/ss10-1.png)

**N.B.**: Once you install a version of Node, the corresponding version of NPM is installed for you. So you don’t need to install NPM separately. 

If the version of NPM you want to use is not available, run `npm install @npm version-number -g` to install it.

Now, to see the list of Node versions you have installed on your Windows machine, run `nvm list`.
![ss11-1](https://www.freecodecamp.org/news/content/images/2022/08/ss11-1.png)

To use a specific version of Node, run: 
- `nvm use latest` to use the latest version 
- `nvm use lts` to use the long-term support version
- `nvm use version-number` to use any other version you have installed
![ss12-1](https://www.freecodecamp.org/news/content/images/2022/08/ss12-1.png)

## Recap

This article showed you how to install NVM on Windows 10 (nvm-windows) and how to use it to install and manage different versions of Node.

As a reminder, here are the common commands you’ll be using with nvm-windows:
- `nvm install node-version` – install a version of Node 
- `nvm list` – see the versions of Node you have installed on your machine
- `nvm use node-version` – use a specific version of Node

Thank you for reading and keep coding :)


