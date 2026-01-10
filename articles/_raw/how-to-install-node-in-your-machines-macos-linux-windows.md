---
title: How to Install Node on a MacOS, Linux, or Windows Machine Using NVM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-22T21:42:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-node-in-your-machines-macos-linux-windows
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a1a740569d1a4ca238a.jpg
tags:
- name: install
  slug: install
- name: node
  slug: node
- name: node js
  slug: node-js
- name: npm
  slug: npm
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Adeel Imran

  Before you can start making super awesome apps in NodeJS, you have to install it.
  Fortunately, installing NodeJS is super simple.

  In this tutorial we will cover how to install NodeJS/NPM in


  macOS/linux

  Windows


  Once you install NodeJS...'
---

By Adeel Imran

Before you can start making super awesome apps in NodeJS, you have to install it. Fortunately, installing NodeJS is super simple.

In this tutorial we will cover how to install NodeJS/NPM in

* macOS/linux
* Windows

Once you install NodeJS/NPM, you can easily upgrade/downgrade to any Node version with one command. The following video tutorial shows you how to download NodeJS on your machine.

## Installation guide for Mac OS & Linux

%[https://www.youtube.com/watch?v=TmT_CGFnUuM&feature=youtu.be]

Open a new terminal. Type the following and hit enter:

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash

```

Close your terminal, then open a new one and type this:

```
nvm ls

```

You will see something like this:

```
system
iojs -> N/A (default)
node -> stable (-> N/A) (default)
unstable -> N/A (default)
nvm_list_aliases:36: no matches found: /Users/adeelimran/.nvm/alias/lts/*

```

Next in your terminal type:

```
nvm install 12.18.1

```

Once it is installed, it is ready to be used. To use this version, just type this in your terminal:

```
nvm use 12.18.1

```

Now that it is installed let's check it by doing the following:

```
node --v
```

And that is it – you are done. Have fun.

Now if, in the future, for some reason you want to uninstall NVM (node version manager) simply open up your terminal and type the following:

```
rm -rf $NVM_DIR ~/.npm ~/.bower

```

## Installation guide for Windows

%[https://www.youtube.com/watch?v=QWdSDo9V1Ho]

### 

First, go to `nvm-windows` repositories releases section [https://github.com/coreybutler/nvm-windows/releases](https://github.com/coreybutler/nvm-windows/releases). Select the latest release. 

Next choose the `nvm-setup.zip` file and download it.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/tempsnip.png)

Once the file is downloaded, unzip and click on the installer and follow the steps. (I am using [7zip](https://www.7-zip.org/) for .zip file extraction, because it is FREE.)

Then to check if `nvm` is properly installed, open a new command prompt terminal and type `nvm`. Once it is verified that it is installed you can move on to the next step.

Install NodeJS using `nvm` like this:

```
nvm install <version_number> // let's assume it's 12.18.1
```

The version can be a NodeJS version or "latest" (for the latest stable version).

In order to use the specific node version you just installed, in your terminal simply type the following:

```
nvm use 12.18.1;
```

Check the node version with node -v. This should output v12.18.1 in your terminal.

If you want to install another version of Node, repeat the steps with a different version.

You should now have a working version of NodeJS running on your machine. Happy coding folks. :)

Let me know if you found this guide helpful. Drop me a message on [twitter](https://twitter.com/adeelibr) ([twitter.com/adeelibr](https://twitter.com/adeelibr)).

