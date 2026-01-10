---
title: Node Version Manager – Guide d'installation de NVM
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
seo_title: Node Version Manager – Guide d'installation de NVM
seo_desc: "By Dillion Megida\nIn this article, I'll explain how you can install NVM,\
  \ or Node Version Manager, on Windows, Linux, and Mac.\nWhat is NVM?\nNode Version\
  \ Manager (NVM), as the name implies, is a tool for managing Node versions on your\
  \ device. \nDifferen..."
---

Par Dillion Megida

Dans cet article, je vais expliquer comment installer NVM, ou Node Version Manager, sur Windows, Linux et Mac.

## Qu'est-ce que NVM ?

Node Version Manager (NVM), comme son nom l'indique, est un outil pour gérer les versions de Node sur votre appareil.

Différents projets sur votre appareil peuvent utiliser différentes versions de Node. Utiliser une seule version (celle installée par `npm`) pour ces différents projets peut ne pas vous donner des résultats d'exécution précis.

Par exemple, si vous utilisez une version de Node **10.0.0** pour un projet qui utilise **12.0.0**, vous pourriez rencontrer des erreurs. Et si vous mettez à jour la version de Node à **12.0.0** avec npm, et que vous l'utilisez pour un projet qui utilise **10.0.0**, vous pourriez ne pas obtenir l'expérience attendue.

En fait, vous recevrez probablement un avertissement qui dit :

```bash
Ce projet nécessite la version X de Node
```

Au lieu d'utiliser npm pour installer et désinstaller les versions de Node pour vos différents projets, vous pouvez utiliser **nvm**, qui vous aide à gérer efficacement vos versions de Node pour chaque projet.

[NVM](https://github.com/nvm-sh/nvm) vous permet d'installer différentes versions de Node et de basculer entre ces versions en fonction du projet sur lequel vous travaillez via la ligne de commande.

Dans les sections suivantes, je vais vous montrer comment installer NVM sur votre appareil Windows, Linux ou Mac.

Avant de continuer, je vous recommande également de désinstaller Node.js si vous l'avez déjà installé afin de ne pas avoir de conflits entre Node.js et nvm.

## Comment installer NVM sur Windows

NVM est principalement pris en charge sur Linux et Mac. Il n'a pas de support pour Windows. Mais il existe un outil similaire créé par coreybutler pour fournir une expérience nvm sous Windows appelé [nvm-windows](https://github.com/coreybutler/nvm-windows).

`nvm-windows` fournit un utilitaire de gestion pour gérer les versions de Node.js sous Windows. Voici comment l'installer :

### 1. Cliquez sur "Download Now"

Dans le [Readme du dépôt nvm-windows](https://github.com/coreybutler/nvm-windows#readme), cliquez sur "Download Now!" :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-338.png)

Cela ouvrira une page montrant différentes versions de NVM.

### 2. Installez le fichier .exe de la dernière version

Dans la dernière version (qui, au moment de la rédaction de cet article, est [1.1.9](https://github.com/coreybutler/nvm-windows/releases/tag/1.1.9)), vous trouverez différents fichiers. Cliquez sur le fichier **nvm-setup.exe** qui est le fichier d'installation de l'outil :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-340.png)

### 3. Terminez l'assistant d'installation

Ouvrez le fichier que vous avez téléchargé et terminez l'assistant d'installation.

Une fois terminé, vous pouvez confirmer que nvm a été installé en exécutant :

```bash
nvm -v
```

Si nvm a été installé correctement, cette commande vous montrera la version de nvm installée.

## Comment installer NVM sur Linux et Mac

Puisque Linux et Mac ont quelques similitudes (ce sont tous deux des systèmes d'exploitation basés sur UNIX), vous pouvez installer nvm sur eux de manière similaire.

### 1. Exécutez l'installateur de nvm

Dans votre terminal, exécutez l'installateur de nvm comme suit :

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

# ou

wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
```

Vous pouvez utiliser `curl` ou `bash` selon la commande disponible sur votre appareil.

Ces commandes cloneront le dépôt nvm dans un répertoire `~/.nvm` sur votre appareil.

### 2. Mettez à jour votre configuration de profil

Le processus d'installation de l'étape 1 devrait également ajouter automatiquement la configuration de nvm à votre profil. Si vous utilisez zsh, ce serait `~/.zshrc`. Si vous utilisez bash, ce serait `~/.bash_profile`... ou un autre profil.

Si la configuration de nvm n'est pas ajoutée automatiquement, vous pouvez l'ajouter vous-même à votre fichier de profil :

```bash
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

La commande ci-dessus charge nvm pour l'utiliser.

### 3. Rechargez la configuration du shell

Avec votre configuration de profil mise à jour, vous allez maintenant recharger la configuration pour que votre terminal l'utilise :

```bash
source ~/.bashrc
```

Avec cette commande exécutée, nvm est prêt à être utilisé. Vous pouvez confirmer que nvm est installé correctement en exécutant :

```bash
nvm -v
```

Cela devrait afficher la version de nvm installée.

## Conclusion

Avec nvm installé, vous pouvez maintenant installer, désinstaller et basculer entre différentes versions de Node sur votre appareil Windows, Linux ou Mac.

Vous pouvez installer des versions de Node comme suit :

```bash
nvm install latest
```

Cette commande installera la dernière version de Node :

```bash
nvm install vX.Y.Z
```

Cela installera la version `X.Y.Z` de Node.

Vous pouvez également faire d'une version votre version par défaut en exécutant :

```bash
nvm alias default vX.Y.Z
```

Et si vous souhaitez utiliser une version spécifique à un moment donné, vous pouvez exécuter ce qui suit dans votre terminal :

```bash
nvm use vA.B.C
```

NVM facilite la gestion de plusieurs versions de Node.js pour différents projets nécessitant différentes versions.