---
title: Automating your Windows Subsystem Linux Setup
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-16T18:07:26.000Z'
originalURL: https://freecodecamp.org/news/automating-your-windows-subsystem-linux-setup-df4c9a7b0e7b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*03UuTGdsAF5PEgaI4BwYZg.jpeg
tags:
- name: Node.js
  slug: nodejs
- name: terminal
  slug: terminal
- name: Web Development
  slug: web-development
- name: Windows 10
  slug: windows-10
- name: WSL
  slug: wsl
seo_title: null
seo_desc: 'By Scott Spence

  I’m a Windows user and have been so for as long as I can remember. I have fiddled
  around with Linux as well but have stuck to Windows as I’ve found it to be a bit
  less neckbeardy for me. Both have their pros and cons. But one of the b...'
---

By Scott Spence

I’m a Windows user and have been so for as long as I can remember. I have fiddled around with Linux as well but have stuck to Windows as I’ve found it to be a bit less [neckbeardy](http://theoatmeal.com/blog/fix_computer) for me. Both have their pros and cons. But one of the biggest cons with Windows for me when I started learning web development was the lack of all my Linux command line tools.

That was until Windows Subsystem Linux (WSL) came along ?

I love it! You can have a Bash shell in Windows and run all your Node.js Apps through it too and with the Windows 10 Fall Creators Update, WSL is really easy to set up.

Quick backstory on why I’m posting this. I nuked my laptop the other day as I was having issues with Bash on Windows related partly to using [nvm](https://github.com/Microsoft/WSL/issues/776) with WSL. I was getting frustrated with how my computer was performing. But I realise now that I overreacted.

After I brought my computer back up again, I had to set up my development environment again from scratch. Luckily for me, I keep all my settings and config information in a [GitHub repo](https://github.com/spences10/settings) in the event of me getting a new computer or to recover from a catastrophic event (like a nuked computer).

In this article, I’d like to show you how I set up my Windows Subsystem Linux for my development environment.

This is my opinionated view on my specif setup and usage of WSL and this is my step by step guide for the next time I have to spin up a development environment from scratch on Windows.

So, after installing [WSL](https://www.microsoft.com/store/productId/9NBLGGH4MSV6) from the Microsoft Store and adding your default user, the first thing is to update and upgrade everything.

```
sudo apt updatesudo apt -y upgrade
```

If you’ve not used any Linux distributions before the `-y` in the upgrade statement is to default the answer to “Yes” for any prompts that are displayed in the terminal. You might not want to do this, as there may be some programs you don’t want to update but I do.

![Image](https://cdn-media-1.freecodecamp.org/images/OXOMF6dNg6mFcLndoTphMYRDL76E880tt09a)
_Yes to all the things!_

By adding the `-y` flag, you wont have these messages ?

**Build tools**

To compile and install native add-ons from npm you may also need to install build tools, I need this for Gatsby images which uses `sharp` which in turn uses `node-gyp`:

```
sudo apt install -y build-essential
```

**Install node**

Installing Node.js via the instructions given on the nodejs.org site doesn’t set up the correct permissions for me. So when trying to `npm install` anything I get errors, I [found out](https://github.com/Microsoft/WSL/issues/776#issuecomment-266112578) that using `n` helps:

**Install node with `n`**

As it’s a fresh install then we can go ahead and use [n-install](https://github.com/mklement0/n-install) with:

```
curl -L https://git.io/n-install | bash
```

This will install the latest stable version of node ?

Once the script is complete, restart bash with:

```
. /home/my_user_name/.bashrc # displays this for you to copy paste
```

Check your node and npm versions:

```
node -v && npm -v
```

**Install fish ?**

Fish is now my go to shell purely for the auto complete/intellisense ? there’s also some nice themes you can get for it too.

![Image](https://cdn-media-1.freecodecamp.org/images/sT61-l2VWUosXNsabUdkBCH2ZJQm6COn6LEy)
_fish awesomeness ?_

```
sudo apt -y install fishsudo apt -y upgrade && sudo apt -y autoremove
```

**Install Oh My Fish | OMF**

Oh My Fish is like a package manager for Fish enabling the installation of packages and themes.

```
curl -L https://get.oh-my.fish | fish
```

**Install OMF theme**

```
omf install clearance
```

**The start of the beginning**

Ok, so that is a basic setup for WSL. You’ll probably want to get Git set up now. I have been using SSH over HTTPS for a while now on WSL.

**Note:** At the time of writing this, WSL Git integration with VSCode doesn’t work so I have added a Git install to my windows machine, you can omit this and go full Git via the terminal but I really like the VSCode Git integration.

To get SSH set up on your machine take a look at this [handy SSH setup](https://github.com/spences10/cheat-sheets/blob/master/git.md#how-to-authenticate-with-github-using-ssh). I say SSH instead of HTTPS because I had all sorts of issues with the Git credential manager and the keyring manager. In the end it was actually quicker to create an SSH key and authenticate with GitHub. The guide I linked walks you through it.

**Move your dotfiles**

If you have all your [dotfiles](https://github.com/spences10/dotfiles) backed up in a GitHub repo then now is a good time to add them to your WSL folder, the last times I did this I manually set the permissions after moving each of the the files but have since discovered `[rsync](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/)` to move all the files.

```
rsync -avzh /mnt/c/Users/dotfiles/ ~/
```

That will copy the contents of my `dotfiles` folder to the `~/` (home) directory in WSL, you can check them with:

```
ls -la ~/
```

![Image](https://cdn-media-1.freecodecamp.org/images/Uq3kAxUEXpizEGd-h7ajRZMLBBZVvlrg5t8B)

I copied across my `.gitconfig`, `.gitignore` and `.npmrc` dotfiles pictured here and you can see that the permissions are not consistent with the `.bashrc` file.

Change the file permissions with `chmod` and to get the attributes of a similar file use `stat`:

```
stat -c “%a %n” ~/.*
```

This will list out all everything that begins with a `.` here’s mine:

```
777 /home/scott/.755 /home/scott/..600 /home/scott/.bash_history644 /home/scott/.bash_logout644 /home/scott/.bashrc777 /home/scott/.cache777 /home/scott/.config777 /home/scott/.gitconfig777 /home/scott/.gitignore777 /home/scott/.local777 /home/scott/.npm777 /home/scott/.npmrc644 /home/scott/.profile644 /home/scott/.sudo_as_admin_successful
```

I only want to change `.gitconfig`, `.gitignore` and `.npmrc` here so I’m going to do this:

```
chmod 644 .gitconfig .gitignore .npmrc
```

And now my files look like this. ?

![Image](https://cdn-media-1.freecodecamp.org/images/JbMu-0tz5J581tQ3FwIjYADBvuWyqXC-xMof)

Ok now were up and running with an updated Ubuntu install, node and fish terminal. Of course there’s still the case of installing all your global npm packages you want for development now.

Good luck!

### Thanks for reading

If you thought this was interesting, leave a clap or two, subscribe for future updates or tweet me your thoughts.

If there is anything I have missed, or if you have a better way to do something then please let me know.

Get me on [Twitter](https://twitter.com/ScottDevTweets) or [Ask Me Anything](https://github.com/spences10/ama) on GitHub.

> **You can read other articles like this on [my blog](https://thelocalhost.blog/).**


