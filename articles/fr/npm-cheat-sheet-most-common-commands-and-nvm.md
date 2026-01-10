---
title: npm Cheat Sheet - Commandes les plus courantes et nvm
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/npm-cheat-sheet-most-common-commands-and-nvm
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cf7740569d1a4ca3523.jpg
tags:
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: toothbrush
  slug: toothbrush
seo_title: npm Cheat Sheet - Commandes les plus courantes et nvm
seo_desc: 'npm or the Node Package Manager, is one of the most used tools for any
  Node.js developer. Here''s a list of the most common commands you''ll use when working
  with npm.

  Install package.json dependencies

  npm install


  Shorthand

  # install

  npm i <package>


  ...'
---

`npm` ou le Node Package Manager, est l'un des outils les plus utilisés pour tout développeur Node.js. Voici une liste des commandes les plus courantes que vous utiliserez lorsque vous travaillerez avec `npm`.

## **Installer les dépendances de `package.json`**

```shell
npm install
```

### Raccourcis

```shell
# installer
npm i <package>

# désinstaller
npm un <package>

# mettre à jour
npm up <package>
```

### Flags

`-S` est équivalent à `--save`, et `-D` est équivalent à `--save-dev`.

## **Lister les packages installés globalement**

```shell
npm list -g --depth=0
```

## **Désinstaller un package global**

```shell
npm -g uninstall <name> 
```

## **Mettre à jour `npm` sur Windows**

```shell
npm-windows-upgrade
```

## **Mettre à jour les packages globaux**

Pour voir quels packages doivent être mis à jour, utilisez :

```shell
npm outdated -g --depth=0
```

Pour mettre à jour les packages globaux individuellement, vous pouvez utiliser :

```shell
npm update -g <package> <package> <package>
```

## **Lister les scripts disponibles à exécuter**

```shell
npm run
```

## **Mettre à jour `npm`**

```shell
npm install -g npm@latest

# utilisez-vous windows ? Alors utilisez
npm-windows-upgrade
```

## **Version installée**

```shell
npm list # pour les packages locaux
```

## **Node Version Manager `nvm`**

`nvm` facilite le passage entre différentes versions de Node.js. Pour en savoir plus, consultez la page [GitHub du projet](https://github.com/nvm-sh/nvm).

Une fois que vous avez installé `nvm`, si vous souhaitez installer la dernière version de Node v12, exécutez simplement :

```shell
nvm install 12
```

Si vous avez plusieurs versions de Node.js installées sur votre espace de travail, vous pouvez passer à une version spécifique en écrivant :

```shell
nvm use 10.19.0
```

### **Définir une version de Node par défaut**

Pour définir une version par défaut de Node pour votre espace de travail, tapez simplement :

```shell
nvm alias default 12
```

Où la dernière version de 12 est la version que vous souhaitez utiliser par défaut.

### Mettre à jour `npm`

Si vous utilisez Node installé via `nvm`, il est bon de mettre à jour votre version de `npm` avec cette commande :

```shell
nvm install-latest-npm
```

## Plus d'informations :

* [Ces astuces NPM feront de vous un pro](https://www.freecodecamp.org/news/10-npm-tricks-that-will-make-you-a-pro-a945982afb25/)
* [Comment installer Node.js et npm sur Windows](https://www.freecodecamp.org/news/how-to-install-node-js-and-npm-on-windows/)
* [npm vs npx — Quelle est la différence ?](https://www.freecodecamp.org/news/npm-vs-npx-whats-the-difference/)