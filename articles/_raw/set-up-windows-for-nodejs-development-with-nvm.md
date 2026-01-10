---
title: How to Set Up Windows for Node.js Development with NVM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-18T20:56:58.000Z'
originalURL: https://freecodecamp.org/news/set-up-windows-for-nodejs-development-with-nvm
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/pexels-tal-haim-4481881.jpg
tags:
- name: node
  slug: node
- name: node js
  slug: node-js
- name: Windows
  slug: windows
seo_title: null
seo_desc: "By Otavio Ehrenberger\nSo you want to develop using the JavaScript run-everywhere\
  \ platform on the same computer where you game, edit videos, code C# desktop apps,\
  \ or whatever. \nYou are also aware that there are multiple Node.js versions in\
  \ active deve..."
---

By Otavio Ehrenberger

So you want to develop using the JavaScript run-everywhere platform on the same computer where you game, edit videos, code C# desktop apps, or whatever. 

You are also aware that there are multiple Node.js versions in active development and it is fairly common to find projects in the wild that only run in a handful of them. 

Then this guide is for you. So let's set up a Windows machine for Node.js with multiple version management, while also addressing common pitfalls.

## How to Install Windows Terminal

If you are using Windows 11, good news: you already have the Windows Terminal installed. If not, open the Microsoft Store and download it free of charge.

![Microsoft Store](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fnsj5h97qeq8grhtriqk.png)

This is a hardware-accelerated tabbed terminal from which you can run Powershell, CMD or WSL interfaces. And it's an important (and, some would say, pretty belated) step towards making the Windows development experience similar to other major OS's. 

Installing this terminal is highly recommended if you plan to develop on Windows, using Node.js or otherwise.

## How to Install NVM for Windows

Now, instead of installing Node.js from the official website, we should install the Node Version Manager and download Node versions from there. 

If you already have Node installed this should not be a major problem as NVM will overwrite any node-related environment variables and symlinks. Still, I'd recommend that you uninstall it anyway as this process will render the current installation completely useless.

Go to the [NVM for windows](https://github.com/coreybutler/nvm-windows) project page and download the latest available version's `nvm-setup.zip` from the [releases page](https://github.com/coreybutler/nvm-windows/releases).

Note that this is not the same as the UNIX-based [NVM](https://github.com/nvm-sh/nvm) project, although it is functionally equivalent. "Similar, not identical" as the project itself discloses.

Unzip the folder's contents and run `nvm-setup.exe`. You'll be prompted to agree with the project's terms of use (currently it's the MIT License), then the installer will ask where to install nvm. This will also be the same location as the downloaded node versions and their globally-enabled packages. The roaming app data folder under your current user should be perfectly fine.

However, you'll then be prompted to indicate where to keep the Node.js symlink, and (at least in versions up to 1.1.8) there's a catch: _you cannot keep the symlink under a path which contains whitespaces_, and unfortunately the default installation path (currently `C:\Program Files\nodejs`) steps right into this trap.

![NVM symlink path](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ng7dyyu59rm0zwoupf7z.png)

This is where I've installed my local NVM. It's only a suggestion and you can install wherever you like (as long as the path does not contain whitespace). I'd only recommend making the target folder's name something like `\nodejs` so you don't end up losing the installation, which can be removed directly from the standard uninstaller anyway.

## How to Install Node & Setup NVM

First of all, you need to run Windows Terminal with administrative privileges. One way you can do this is by looking for the terminal in the system's internal search, clicking with the right button on its icon, and then selecting 'Run as Administrator'.

![Running Windows Terminal as an Administrator](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/m2gsgaduqa8fyn9uujep.png)

Any time you feel lost while fiddling with NVM, simply type `nvm` in the terminal and a very concise manual will pop up explaining each available command and their parameters.

![NVM Manual](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ecc68wrbgdal06f7eqvz.png)

Let's make sure NVM is enabled. Just run:

```powershell
nvm on

```

And after that, let's install the current Long Term Support version, pre-aliased as `lts` (currently 14.18.1):

```powershell
nvm install lts

```

After the installation finishes, we must declare to NVM what version we'd like to use:

```powershell
nvm use 14.18.1

```

Great! Now, Node.js-specific commands such as `node` and `npm` will be mapped to that node version. Let's celebrate by installing the yarn package manager:

```powershell
npm install -g yarn

```

After the installation ends, let's check if everything went OK:

```powershell
yarn -v

```

If you get the yarn version as output, congratulations! The set-up was properly done.

## How to Manage Multiple NodeJS Versions

Now that we have the LTS version, what's the good of having a version manager if not to use different versions? Let's also install the most recent Node version, pre-aliased as `latest` (currently 16.11.1):

```powershell
nvm install latest

```

Anytime you'd like to check your locally installed versions, run

```powershell
nvm list

```

to get a list of the ones available in your system. To change your current version, simply run nvm use again, this time pointing to the newly-installed one:

```powershell
nvm use 16.11.1

```

Note that if you run `yarn -v` again you will not receive a version number as yarn is not currently installed for your local 16.11.1. _Every installed version is completely self-contained, which includes access to global packages_.

Congratulations, you are now an organized Windows Node.js developer who follows the best practices of localized version management.

## How to Troubleshoot Common Problems

### My downloads through npm/yarn are REALLY slow.

First of all, make sure the network you are connected to is classified as 'private' by Windows, as the Windows firewall can be very picky on public networks. 

In case the problem persists, whitelist the nvm directory (should be `C:\Users\<your_user_name>\AppData\Roaming\nvm` if you kept the defaults) in your antivirus software.

### Running stuff in node (e.g. transpiling a Typescript project) is REALLY slow.

Windows uses the NTFS filesystem which is particularly bad at dealing with tasks involving a very big number of small files. And Node projects are notorious for the many different modules which depend on many different other modules, so this problem is harder to mitigate. 

Short of getting an SSD, your best bet would be to set up Node on [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about) in case execution speed is unworkably slow.

### I'm getting a 145 exit code in some NVM commands.

Take a look at the _Install NVM for Windows_ part of this tutorial, especially the one regarding the symlink location. 

You must have installed NVM in a directory path with whitespaces. So just uninstall NVM and re-run `nvm-setup.exe`, this time making sure no selected paths contain whitespaces.

## Conclusion

If you can install versions from the command line and switch between them (remember you'll need to have admin privileges to switch between versions), then all the rest is up to you as a JavaScript (or TypeScript) developer. 

If you need to install a code editor, I'd recommend Visual Studio Code for convenience, Sublime Text 3 as a lightweight alternative to VSCode, or [vim](https://www.freecodecamp.org/news/vim-windows-install-powershell/) if you feel like you have the time and effort to learn a new skill.

