---
title: Vim Windows Install Guide – How to Run the Vim Text Editor in PowerShell on
  your PC
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2020-05-06T17:21:00.000Z'
originalURL: https://freecodecamp.org/news/vim-windows-install-powershell
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b34740569d1a4ca2a64.jpg
tags:
- name: vim
  slug: vim
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: 'Vim is a powerful code editor. So powerful that both Linux and Mac have
  it installed by default.

  But if you are using Windows as your operating system, you will need to install
  Vim separately.

  Fortunately, Microsoft makes it very easy to install Vim ...'
---

Vim is a powerful code editor. So powerful that both Linux and Mac have it installed by default.

But if you are using Windows as your operating system, you will need to install Vim separately.

Fortunately, Microsoft makes it very easy to install Vim and get it running on your PC.

## How to Download Vim

You can [download the latest version of the Vim Text Editor straight from Vim themselves](https://www.vim.org/download.php).

They have built a special self-executing installer that walks you through the process of installing Vim in the right location on your hard drive.

## How to Install Vim

Note that for Windows you will technically download something called gVim, which is a version of Vim that includes a basic graphic user interface (GUI). You can [install it by downloading this executable installer](https://ftp.nluug.nl/pub/vim/pc/gvim82.exe).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/signal-attachment-2020-05-07-144326_005-1.png)
_A screenshot of what you'll se when you attempt to open the file. Because this is an .exe file, Windows will ask your permission first._

Once you've downloaded the file, you just need to run it, and you'll see a nice installation wizard that looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/signal-attachment-2020-05-07-144326_004.png)
_A screenshot of the wizard you'll see when you first run the Vim installer_

They have a recommended "typical" installation. but if you have a reasonably large hard drive, there's no harm in going ahead with installing everything by choosing the "full" option:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/signal-attachment-2020-05-07-144326_003.png)
_A screenshot of the Vim installer where you can choose what parts of Vim you want to install._

## How to Run Vim in PowerShell

Then, once you've installed Vim, you should be able to launch it from your Windows command prompt. 

Note that as of 2020, PowerShell has all of the same functionality as CMD, plus a whole lot more. I recommend using PowerShell for everything.

You can open PowerShell from the Windows menu bar by typing "powershell" in the search field on the start bar.

Windows will open PowerShell, and you'll get a command prompt that looks something like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/signal-attachment-2020-05-07-144326_001.png)
_A screenshot of the Windows PowerShell prompt._

Once you're in PowerShell, here's how to run Vim itself. All you have to do is type "vim" and press enter. This will open up Vim. Once Vim is open, this is what you should see:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/signal-attachment-2020-05-07-144326_002.png)
_A screenshot of Vim when you open it for the first time._

Congratulations – you now have Vim installed.

## How to run Vim inside VS Code

If you are already using VS Code, and want a lot of the speed of Vim without losing the functionality of VS Code, I have good news. It is possible to run a Vim-like experience right within VS Code.

[Here is a Vim plugin for VS Code](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim) that will help you do this. At the time of me writing this, this plugin has been installed nearly 2 million times.

## How to Learn How to Use Vim Properly

Vim is a powerful code editor, and it will take you a lot of practice to get comfortable with it. 

Here are a few Vim tutorials that will really help you quickly grasp the basics and get your fingers flying in no time.

For starters, one way Vim is different from other code editors is that Vim has "modes". Here are [all of Vim's modes explained, with examples](https://www.freecodecamp.org/news/vim-editor-modes-explained/).

Vim can be intimidating. There is so much to learn. But this guide will show you [how not to be afraid of Vim anymore](https://www.freecodecamp.org/news/how-not-to-be-afraid-of-vim-anymore-ec0b7264b0ae/).

If you're already using VS Code and want to switch completely to Vim, [this article will explain how you can do so](https://www.freecodecamp.org/news/vim-for-people-who-use-visual-studio-code/).

And [here are 7 Vim Tips That Changed #100DaysOfCode founder Alex Kallaway's life](https://www.freecodecamp.org/news/7-vim-tips-that-changed-my-life/). In this article, he not only explain these, but shows demos of these tips in action.

## Vim: Learn it, live it, love it.

In the 30 years since Bram Moolenaar first created Vim, its influence has spread far and wide. And even today, the Vim project is actively maintained and constantly improving.

I've met so many developers over the years who swear by Vim.

I hope this guide has helped you get running Vim on your Windows PC. And I hope these other tutorials I've shared with you here will help you go from zero-to-sixty within the coming months.

The key is to keep practicing and not get discouraged by how many Vim shortcuts there are to remember. Eventually, all of these will become muscle memory, and you'll be flying from one file to another, banging out code like a terminator.

There is no feeling quite as cool as being able to drop into a codebase and immediately start making changes without ever even reaching for a mouse or trackpad. That is the power that Vim promises, and delivers in spades.

