---
title: Comment installer Neovim en utilisant le Framework NvChad
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
seo_title: Comment installer Neovim en utilisant le Framework NvChad
seo_desc: "Neovim is a popular IDE and is a solid alternative to VS Code. Neovim supports\
  \ every major programming language and allows you to build anything, anywhere. \n\
  Neovim can be a bit problematic to start with, especially for newcomers. Writing\
  \ a Neovim con..."
---

[Neovim](https://neovim.io/) est un IDE populaire et une alternative solide à VS Code. Neovim supporte tous les principaux langages de programmation et vous permet de construire n'importe quoi, n'importe où. 

Neovim peut être un peu problématique pour commencer, surtout pour les nouveaux venus. Écrire une configuration Neovim à partir de zéro est souvent difficile. Pour résoudre ce problème, nous allons installer Neovim en utilisant le Framework NvChad. 

[NvChad](https://nvchad.com/) est un fournisseur de framework/configuration pour Neovim qui possède une interface UI riche et belle, un temps de démarrage ultra-rapide, et vous aide à travailler de manière productive avec Neovim.

Vous n'avez pas besoin de configurer tout à partir de zéro, car la plupart des choses sont pré-configurées. Il y a plusieurs thèmes, extraits de code, surlignage de syntaxe, configuration LSP, gestion de plugins, mappage de touches, et d'autres fonctionnalités utiles.

Dans cet article, je vais vous donner des instructions étape par étape pour installer Neovim et NvChad à partir de zéro dans votre distribution Linux et basée sur Debian.

## Comment configurer le projet

Pour télécharger Neovim et NvChad dans votre distribution, vous aurez besoin de certains outils de ligne de commande supplémentaires. Ceux-ci vous aideront à installer le logiciel :

1. [Git CLI](#heading-installation-de-linterface-git-cli)
2. [Curl CLI](#heading-installation-de-linterface-curl-cli)
3. [Unzip CLI](#heading-installation-de-linterface-unzip-cli)
4. [Fc cache (Font Config) CLI](#heading-installation-de-linterface-fc-cache-font-config-cli)

Passons en revue l'installation de ces outils pour vous assurer de les avoir :

### Installation de l'interface Git CLI

Pour installer Git, exécutez la commande suivante :

```bash
sudo apt-get install git

```

### Installation de l'interface Curl CLI

Pour installer curl, exécutez la commande suivante :

```bash
sudo apt-get install curl

```

### Installation de l'interface Unzip CLI

Pour installer Unzip, exécutez la commande suivante :

```bash
sudo apt-get install unzip

```

### Installation de l'interface Fc cache (Font Config) CLI

Pour installer l'interface Fc cache CLI, exécutez la commande suivante.

```bash
sudo apt install fontconfig

```

## Comment installer Neovim et NvChad

Si vous suivez ces étapes, vous pouvez facilement installer Neovim et NvChad, même si vous êtes un nouveau venu. Cela prend un certain temps, mais vous n'avez pas besoin d'avoir des connaissances approfondies sur Neovim et NvChad pour les configurer.

### Installer Neovim

La première étape consiste à installer Neovim sur votre machine. Pour ce faire, vous devrez exécuter la commande suivante en fonction de votre distribution :

```bash
# Ubuntu (Utilisateur Snap)
sudo snap install nvim --classic

# NixOS
nix-env -iA nixpkgs.neovim

# MacOS
brew install neovim

# Arch Linux
sudo pacman -S neovim
```

Pour d'autres systèmes d'exploitation tels que Windows, vous pouvez lire la [page de documentation d'installation](https://github.com/neovim/neovim/blob/master/INSTALL.md). J'ai également écrit un article sur [**la bonne façon d'installer Neovim**](https://medium.com/thelinux/the-correct-way-to-install-the-neovim-42f3076f9b88), que vous pouvez également consulter.

## Comment installer Nerd Font

L'étape suivante consiste à installer Nerd Font sur votre ordinateur portable ou votre système d'exploitation. Nerd Font est un prérequis pour NvChad. Si vous ne pouvez pas télécharger Nerd Font, votre interface utilisateur NvChad ne fonctionnera pas.

Pour installer Nerd Font dans Debian ou les distributions basées sur Debian et macOS, vous pouvez exécuter la commande suivante :

```bash
# Debain, Ubuntu, Linux Mint, Kali Linux, etc.
bash -c  "$(curl -fsSL https://raw.githubusercontent.com/officialrajdeepsingh/nerd-fonts-installer/main/install.sh)" 

# MacOS
brew tap homebrew/cask-fonts && brew install --cask font-<Nerd-FONT- NAME>-nerd-font

```

Avant d'exécuter [nerd-fonts-installer](https://github.com/officialrajdeepsingh/nerd-fonts-installer), assurez-vous d'avoir installé **curl**, **unzip**, et **Fc cache** CLI dans votre distribution Debian, en suivant les instructions ci-dessus.

## Comment installer NvChad

La dernière et dernière étape consiste à installer le framework NvChad dans Neovim. Pour ce faire, exécutez la commande suivante :

```bash
# Linux & macOS
git clone https://github.com/NvChad/starter ~/.config/nvim && nvim
```

La commande suivante prend un certain temps, selon votre vitesse Internet, et installe les plugins supplémentaires requis par NvChad à partir d'Internet. 

## Conclusion

Pour un nouveau venu commençant avec Neovim, le framework NvChad est un excellent choix. Sans NvChad, configurer Neovim à partir de zéro est une tâche difficile pour un débutant. Choisir le framework Neovim (configuration) est le bon choix pour les nouveaux venus.

Avant de commencer avec Neovim, lisez et assurez-vous que c'est le bon choix pour vous. J'ai récemment trouvé un [plugin VS Code](https://marketplace.visualstudio.com/items?itemName=asvetliakov.vscode-neovim) créé et maintenu par Neovim. Vous pouvez obtenir la même expérience Neovim à l'intérieur de VS Code. Après cela, vous pouvez décider lequel vous préférez.