---
title: Comment mettre à jour Node et NPM vers la dernière version
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-12T20:28:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-update-node-and-npm-to-the-latest-version
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-markus-winkler-4052195.jpg
tags:
- name: node js
  slug: node-js
- name: npm
  slug: npm
- name: 'update '
  slug: update
seo_title: Comment mettre à jour Node et NPM vers la dernière version
seo_desc: "By Dillion Megida\nNode is a runtime environment that allows developers\
  \ to execute JavaScript code outside the browser, on the server-side. \nNPM, on\
  \ the other hand, is a package manager for publishing JavaScript packages (also\
  \ known as Node modules) t..."
---

Par Dillion Megida

Node est un environnement d'exécution qui permet aux développeurs d'exécuter du code JavaScript en dehors du navigateur, côté serveur. 

NPM, quant à lui, est un gestionnaire de paquets pour publier des paquets JavaScript (également connus sous le nom de modules Node) sur le [registre npm](https://www.npmjs.com/). Vous pouvez également l'utiliser pour installer des paquets dans vos applications.

Pour installer Node, vous devez vous rendre sur le [site web de Nodejs](https://nodejs.org/en/) pour télécharger l'installateur. Après le téléchargement, vous pouvez exécuter l'installateur, suivre les étapes, accepter les termes et conditions, et avoir l'installateur sur votre appareil.

Lorsque vous installez Node, vous obtenez également la CLI `npm` que vous pouvez utiliser pour gérer les paquets dans vos applications.

Cependant, Node et NPM peuvent être mis à jour séparément vers leurs dernières versions, et dans le reste de cet article, je vais vous montrer comment.

## Comment mettre à jour Node

### 1. Utiliser NPM pour mettre à jour votre version de Node
Pour mettre à jour Node avec NPM, vous allez installer le paquet [n](https://www.npmjs.com/package/n), qui sera utilisé pour gérer interactivement les versions de Node sur votre appareil.

Voici les étapes :

#### Vider le cache NPM
Lorsque vous installez des dépendances, certains modules sont mis en cache pour améliorer la vitesse d'installation lors des téléchargements ultérieurs. Donc, tout d'abord, vous voulez vider le cache NPM.

#### Installer n

```shell
npm install -g n
```

Vous devrez installer ce paquet globalement car il gère les versions de Node à la racine.

#### Installer une nouvelle version de Node

```shell
n lts
n latest
```

Les deux commandes ci-dessus installent les versions à support long terme et les dernières versions de Node.

#### Supprimer les versions précédemment installées

```shell
n prune
```

Cette commande supprime les versions mises en cache des versions précédemment installées et ne conserve que la dernière version installée.


### 2. Utiliser NVM pour mettre à jour votre version de Node
NVM signifie Node Version Manager, et comme son nom l'indique, il vous aide à gérer vos versions de Node. Avec NVM, vous pouvez installer des versions de Node et spécifier la version de Node qu'un projet utilise.

NVM facilite le test de projets sur diverses versions de Node.

Pour mettre à jour une version de Node avec NVM, vous devez d'abord installer NVM.

Voici le [guide d'installation](https://github.com/nvm-sh/nvm#installing-and-updating) pour NVM.

Une fois installé, vous pouvez installer des paquets avec :

```shell
nvm install [version]
```

Vous pouvez installer la dernière version avec :

```shell
nvm install node
```

Et désinstaller d'autres versions avec :

```shell
nvm uninstall [version]
```

Avec plusieurs versions installées, vous pouvez également vouloir spécifier la version à utiliser à un moment particulier. Une façon de faire cela est de définir un alias par défaut comme ceci :

```shell
nvm alias default [version]
```

De cette manière, les exécutions de Node s'exécuteront avec la version spécifiée.


### 3. Télécharger les binaires mis à jour de Node
Et vous pouvez également obtenir les dernières versions depuis le [site web de Node.js](https://nodejs.org/en/). Sur celui-ci, vous pouvez trouver les dernières versions et les versions à support long terme pour votre appareil.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-7.png)
_Page de téléchargements de Node.js_

Le téléchargement de la dernière version vous donne également la dernière version de NPM.

## Comment mettre à jour NPM

Tout comme vous utilisez NPM pour mettre à jour des paquets, vous pouvez utiliser NPM pour se mettre à jour lui-même. Voici la commande pour y parvenir :

```shell
npm install -g npm@latest
```

Cette commande installera la dernière version de NPM globalement.

Sur Mac, vous devrez peut-être passer la commande `sudo` avant NPM, car cela installe NPM à la racine de votre appareil, et vous avez besoin de privilèges pour cela.

## Conclusion

Dans cet article, nous avons vu comment mettre à jour Node et NPM vers leurs dernières versions.

Pour réitérer, lorsque vous installez Node, vous obtenez automatiquement NPM. Si vous mettez également à jour Node en installant les binaires depuis le site web, vous obtenez un NPM mis à jour.

Nous avons également vu d'autres façons de mettre à jour Node et NPM globalement sur votre appareil.