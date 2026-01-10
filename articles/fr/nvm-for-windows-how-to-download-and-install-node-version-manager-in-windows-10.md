---
title: NVM pour Windows – Comment télécharger et installer Node Version Manager sur
  Windows 10
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
seo_title: NVM pour Windows – Comment télécharger et installer Node Version Manager
  sur Windows 10
seo_desc: 'Different software development tools might require specific versions of
  Node.js and NPM (Node Package Manager). NPM is a tool for managing packages installed
  from the NPM registry.

  In addition, if you are making an NPM package, you might need to test...'
---

Différents outils de développement logiciel peuvent nécessiter des versions spécifiques de Node.js et NPM (Node Package Manager). NPM est un outil pour gérer les packages installés depuis le registre NPM.

De plus, si vous créez un package NPM, vous pourriez avoir besoin de le tester avec différentes versions de Node.js. C'est pourquoi vous devriez avoir NVM installé.

NVM, abréviation de Node Version Manager, est un outil en ligne de commande pour gérer et basculer entre différentes versions de Node.js.

Dans cet article, je vais vous montrer comment télécharger et installer NVM sur Windows 10 – même s'il n'existe pas de « NVM » pour Windows.

Je vais également vous montrer comment configurer et utiliser différentes versions de Node.js et NPM sur votre ordinateur Windows.

## Ce que nous allons couvrir
- [Comment télécharger et installer Node Version Manager sur Windows 10](#heading-comment-telecharger-et-installer-node-version-manager-sur-windows-10)
  - [Suivez les étapes ci-dessous pour télécharger nvm-windows](#heading-suivez-les-etapes-ci-dessous-pour-telecharger-nvm-windows)
- [Comment utiliser NVM sur Windows 10](#heading-comment-utiliser-nvm-sur-windows-10)
  - [Comment installer différentes versions de Node.js et NPM avec NVM](#heading-comment-installer-differentes-versions-de-nodejs-et-npm-avec-nvm)
- [Récapitulatif](#heading-recapitulatif)

## Comment télécharger et installer Node Version Manager sur Windows 10

Comme je l'ai mentionné précédemment, il n'existe pas de « NVM » pour Windows, car NVM n'est pris en charge que sur Linux et Mac. 

Ce que vous allez utiliser sur votre machine Windows est « nvm-windows ». nvm-windows est similaire à NVM, mais pas identique.

**N.B.** : Si vous avez déjà installé Node.js, vous devez le désinstaller pour éviter des erreurs lors de l'utilisation de différentes versions de Node et de l'installation de packages depuis le registre NPM. 

Redémarrez votre PC ensuite, ouvrez l'invite de commande ou PowerShell, et exécutez `node -v` pour confirmer que Node a été désinstallé.

![ss1-2](https://www.freecodecamp.org/news/content/images/2022/08/ss1-2.png)

De plus, si vous avez installé yarn, désinstallez-le et réinstallez-le après avoir installé NVM. Vous ne voulez pas rencontrer des erreurs étranges lors de l'installation et de l'utilisation de packages depuis le registre NPM.

### Suivez les étapes ci-dessous pour télécharger nvm-windows

- **Étape 1** : Rendez-vous sur le [dépôt nvm-windows](https://github.com/coreybutler/nvm-windows#installation--upgrades) et cliquez sur « Download Now! »
![ss2-2](https://www.freecodecamp.org/news/content/images/2022/08/ss2-2.png)

Vous serez redirigé vers une page contenant différentes versions de nvm-windows.

- **Étape 2** : Cliquez sur la dernière version pour la télécharger. Pour l'instant, il s'agit de la version du 28 avril 2022.
![ss3-2](https://www.freecodecamp.org/news/content/images/2022/08/ss3-2.png)

- **Étape 3** : Localisez l'installateur sur votre ordinateur et ouvrez-le. Suivez l'assistant d'installation pour l'installer.
![ss4-2](https://www.freecodecamp.org/news/content/images/2022/08/ss4-2.png)
![ss5-3](https://www.freecodecamp.org/news/content/images/2022/08/ss5-3.png)

- **Étape 4** : Ouvrez PowerShell ou l'invite de commande et exécutez `nvm -v` pour confirmer l'installation.
![ss6-2](https://www.freecodecamp.org/news/content/images/2022/08/ss6-2.png)

Si vous obtenez le même message que moi ci-dessus, alors nvm-windows a été installé avec succès. Félicitations !

## Comment utiliser NVM sur Windows 10

Pour utiliser NVM, vous devez ouvrir PowerShell ou l'invite de commande en tant qu'administrateur. Vous pouvez également utiliser Git bash.

- Pour ouvrir PowerShell en tant qu'administrateur, faites un clic droit sur Démarrer et sélectionnez « PowerShell (Admin) ».
![powershell-admin](https://www.freecodecamp.org/news/content/images/2022/08/powershell-admin.png)

- Pour ouvrir l'invite de commande en tant qu'administrateur, recherchez « cmd » et sélectionnez « Ouvrir en tant qu'administrateur » à droite.
![cmd-admin](https://www.freecodecamp.org/news/content/images/2022/08/cmd-admin.png)


### Comment installer différentes versions de Node.js et NPM avec NVM
Le superpouvoir que NVM vous donne est la possibilité d'avoir plusieurs versions de Node.js installées sur votre machine. 

Pour installer la dernière version de Node, exécutez `nvm install latest`.
![ss7-1](https://www.freecodecamp.org/news/content/images/2022/08/ss7-1.png)

Il est toujours préférable d'installer la version à support long terme (LTS) de Node car elle est moins boguée.

Pour installer la version LTS de Node, exécutez `nvm install lts`.
![ss8-1](https://www.freecodecamp.org/news/content/images/2022/08/ss8-1.png)

Pour installer une version spécifique de Node, vous devez d'abord exécuter `nvm list available` afin de voir les versions de Node disponibles.
![ss9-1](https://www.freecodecamp.org/news/content/images/2022/08/ss9-1.png)

Pour installer cette version spécifique, exécutez `nvm install node-version-number`. Par exemple, `nvm install 14.20.0`.
![ss10-1](https://www.freecodecamp.org/news/content/images/2022/08/ss10-1.png)

**N.B.** : Une fois que vous installez une version de Node, la version correspondante de NPM est installée pour vous. Vous n'avez donc pas besoin d'installer NPM séparément. 

Si la version de NPM que vous souhaitez utiliser n'est pas disponible, exécutez `npm install @npm version-number -g` pour l'installer.

Maintenant, pour voir la liste des versions de Node que vous avez installées sur votre machine Windows, exécutez `nvm list`.
![ss11-1](https://www.freecodecamp.org/news/content/images/2022/08/ss11-1.png)

Pour utiliser une version spécifique de Node, exécutez : 
- `nvm use latest` pour utiliser la dernière version 
- `nvm use lts` pour utiliser la version à support long terme
- `nvm use version-number` pour utiliser toute autre version que vous avez installée
![ss12-1](https://www.freecodecamp.org/news/content/images/2022/08/ss12-1.png)

## Récapitulatif

Cet article vous a montré comment installer NVM sur Windows 10 (nvm-windows) et comment l'utiliser pour installer et gérer différentes versions de Node.

Pour rappel, voici les commandes courantes que vous utiliserez avec nvm-windows :
- `nvm install node-version` – installer une version de Node 
- `nvm list` – voir les versions de Node que vous avez installées sur votre machine
- `nvm use node-version` – utiliser une version spécifique de Node

Merci d'avoir lu et continuez à coder :)