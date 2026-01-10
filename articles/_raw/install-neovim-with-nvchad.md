---
title: How to Install Neovim Using the nvchad Framework
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2024-03-14T14:17:07.000Z'
originalURL: https://freecodecamp.org/news/install-neovim-with-nvchad
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/How-to-Install-Neovim-Using-the-nvchad-Framework.png
tags:
- name: ide
  slug: ide
- name: 'Integrated Development Environment  '
  slug: integrated-development-environment
seo_title: null
seo_desc: "Neovim is a popular IDE and is a solid alternative to VS Code. Neovim supports\
  \ every major programming language and allows you to build anything, anywhere. \n\
  Neovim can be a bit problematic to start with, especially for newcomers. Writing\
  \ a Neovim con..."
---

[Neovim](https://neovim.io/) is a popular IDE and is a solid alternative to VS Code. Neovim supports every major programming language and allows you to build anything, anywhere. 

Neovim can be a bit problematic to start with, especially for newcomers. Writing a Neovim configuration from scratch is often difficult. To resolve this issue, we will install Neovim using the Nvchad framework. 

[Nvchad](https://nvchad.com/) is a Neovim framework/configuration provider that has a rich, beautiful UI interface, blazing-fast startup time, and helps you work productively with Neovim.

You don't need to configure everything from scratch, as most things come pre-configured. There are multiple themes, code snippets, syntax highlighting, LSP configuration, plugin management, key mapping, and other helpful features.

In this article, I'll give you step-by-step instructions on installing Neovim and nvchad from scratch in your Linux and Debian based distro.

## How to Set Up the Project

To download Neovim and nvchad in your distro, you'll need some additional command line tools. These will help you install the software:

1. [Git CLI](#heading-install-the-git-cli)
2. [Curl CLI](#heading-install-the-curl-cli)
3. [Unzip CLI](#heading-install-the-unzip-cli)
4. [Fc cache (Font Config) CLI](#heading-install-the-fc-cache-font-config-cli)

Let's go through installing these tools to make sure you have them:

### Install the Git CLI

To install Git, run the following command:

```bash
sudo apt-get install git

```

### Install the Curl CLI

To install curl, run the following command:

```bash
sudo apt-get install curl

```

### Install the Unzip CLI

To install Unzip, run the following command:

```bash
sudo apt-get install unzip

```

### Install the Fc cache (Font Config) CLI

To install the Fc cache CLI, run the following command.

```bash
sudo apt install fontconfig

```

## How to Install Neovim and nvchad

If you follow these steps, you can easily install Neovim and nvchad, even if you are a newcomer. It takes some time, but you don't need to have deep knowledge about Neovim and nvchad to get them set up.

### Install Neovim

The first step is to install Neovim on your machine. To do that, you'll need to run the following command depending on your distro:

```bash
# Ubuntu ( Snap User)
sudo snap install nvim --classic

# NixOS
nix-env -iA nixpkgs.neovim

# MacOS
brew install neovim

# Arch Linux
sudo pacman -S neovim
```

For other operating systems such as Windows, you can read the [installation documentation Page](https://github.com/neovim/neovim/blob/master/INSTALL.md). I've also written an article on [**the correct way to install Neovim**](https://medium.com/thelinux/the-correct-way-to-install-the-neovim-42f3076f9b88), which you can also check out.

## How to Install Nerd Font

The next step is to install Nerd Font on your laptop or operating system. Nerd Font is a prerequisite for nvchad. If you cannot download Nerd Font, your nvchad UI will not work.

To install Nerd Font in Debian or Debian-based distros and macOS, you can run the following command:

```bash
# Debain, Ubuntu, Linux Mint, Kali Linux, etc.
bash -c  "$(curl -fsSL https://raw.githubusercontent.com/officialrajdeepsingh/nerd-fonts-installer/main/install.sh)" 

# MacOS
brew tap homebrew/cask-fonts && brew install --cask font-<Nerd-FONT- NAME>-nerd-font

```

Before running the [nerd-fonts-installer](https://github.com/officialrajdeepsingh/nerd-fonts-installer), make sure you've installed **curl**, **unzip**, and **Fc cache** CLI in your Debian distro, following the instructions above.

## How to Install nvchad

The last and final step is to install the nvchad framework in Neovim. To do so, run the following command:

```bash
# Linux & macOS
git clone https://github.com/NvChad/starter ~/.config/nvim && nvim
```

The following command takes some time, depending on your internet speed, and installs additional plugins required by nvchad from the internet. 

## Conclusion

For a newcomer starting with Neovim, the nvchad framework is a great choice. Without nvchad, configuring Neovim from scratch is a hard task for a beginner. Choosing the Neovim framework (configuration) is the right choice for newcomers.

Before starting with Neovim, read up and make sure It is the right choice for you. I recently found a [VS Code plugin](https://marketplace.visualstudio.com/items?itemName=asvetliakov.vscode-neovim) created and maintained by Neovim. You can get the same Neovim experience inside VS Code. After that, you can decide which you prefer.

