---
title: Comment installer Node.js sur Ubuntu et mettre à jour npm vers la dernière
  version
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-30T18:18:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-node-js-on-ubuntu-and-update-npm-to-the-latest-version
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Slice-3-2-.jpg
tags:
- name: node js
  slug: node-js
- name: npm
  slug: npm
- name: Ubuntu
  slug: ubuntu
seo_title: Comment installer Node.js sur Ubuntu et mettre à jour npm vers la dernière
  version
seo_desc: "By Adebola Adeniran\nIf you try installing the latest version of node using\
  \ the apt-package manager, you'll end up with v10.19.0. This is the latest version\
  \ in the ubuntu app store, but it's not the latest released version of NodeJS. \n\
  This is because ..."
---

Par Adebola Adeniran

Si vous essayez d'installer la dernière version de Node en utilisant le gestionnaire de paquets apt, vous obtiendrez la version **v10.19.0**. Il s'agit de la dernière version disponible dans le magasin d'applications Ubuntu, mais ce n'est pas la dernière version publiée de NodeJS.

Cela est dû au fait que lorsque de nouvelles versions d'un logiciel sont publiées, il peut falloir des mois à l'équipe Ubuntu pour les tester et les publier dans le magasin officiel Ubuntu. Par conséquent, pour obtenir les dernières versions de tout logiciel, nous devons parfois utiliser des paquets privés publiés par les développeurs.

Dans ce tutoriel, ce que nous voulons faire est d'obtenir soit la version **v12.18.1** (LTS - avec support à long terme) soit la version **v14.4** de Node. Pour obtenir les dernières versions, nous pouvons utiliser soit **nodesource** soit **nvm** (node version manager). Je vais vous montrer comment utiliser les deux.

Toutes les commandes ici seront exécutées en utilisant le CLI/terminal Ubuntu.

## Utilisation de NVM - ma méthode préférée

J'aime nvm car il me permet d'utiliser différentes versions de Node pour différents projets. Parfois, vous pouvez collaborer sur un projet avec quelqu'un utilisant une version différente de Node et vous devez basculer vers la version de Node requise par le projet. Pour cela, nvm est le meilleur outil.

## Installer NVM

`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash`

Pour vérifier que nvm est installé, tapez `nvm --version`. Si vous obtenez un numéro de version comme `0.35.3`, alors vous savez que nvm a été installé avec succès.

**Redémarrez votre terminal pour que vos modifications prennent effet.**

## Installer NodeJS

Ensuite, installons la version 14.4.0 de Nodejs.

Exécutez simplement `nvm install 14.4.0`.

Vous pouvez utiliser une commande similaire pour installer n'importe quelle version de Node que vous souhaitez, par exemple `nvm install 12.18.1`.

Cette commande installe automatiquement **nodejs** ainsi que la dernière version de **npm** qui est `v6.14.5`.

Si vous devez basculer entre les versions de Node, vous pouvez simplement exécuter `nvm use <version-number>`, par exemple `nvm use v12.18.1`.

Pour lister les différentes versions de Node que vous avez installées avec nvm, exécutez `nvm ls`.

## Installer Nodesource

Exécutez la commande ci-dessous pour indiquer à Ubuntu que nous voulons installer le paquet Nodejs depuis nodesource.

`curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -`

**NB** que v14.4.0 est la dernière version de Node mais ne dispose pas actuellement de LTS - support à long terme. Pour installer la dernière version de Node avec LTS, changez `14` dans la commande ci-dessus par `12`.

Il se peut que vous soyez invité à entrer le mot de passe de votre utilisateur root. Entrez-le et appuyez sur entrée/retour.

## Installer NodeJS

Une fois que nous avons terminé la configuration de Nodesource, nous pouvons maintenant installer Nodejs v14.4.
Exécutez `sudo apt-get install -y nodejs`.

Une fois terminé, nous pouvons vérifier que nous avons la dernière version de Node installée.
Tapez simplement `nodejs -v` dans votre terminal et il devrait retourner `v14.4.0`.

Vous devriez avoir npm installé automatiquement à ce stade. Pour vérifier la version de npm que vous avez, exécutez `npm version`. Si vous n'obtenez pas un objet qui inclut la dernière version de npm à 6.14.5, `{ npm: '6.14.5' }`, alors vous pouvez mettre à jour npm manuellement en exécutant la commande suivante :

`npm install -g npm@latest`.

Si vous rencontrez des problèmes avec npm qui ne peut pas se mettre à jour car il n'est pas installé, vous pouvez d'abord installer npm en utilisant `sudo apt-get install -y npm`, puis exécuter la commande ci-dessus pour le mettre à jour.

Pour que certains paquets npm fonctionnent, nous devons également exécuter la commande suivante :
`sudo apt install build-essential`.

Et c'est tout !

Vous avez les dernières versions de NodeJS et NPM sur votre machine Ubuntu.

Allez construire de grands produits :)