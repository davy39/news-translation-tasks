---
title: Optimisation manuelle des builds Webpack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-22T19:49:37.000Z'
originalURL: https://freecodecamp.org/news/manually-tuning-webpack-builds-284923f47f44
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vv4_hp-NqMdSIYWCH32Psg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: webpack
  slug: webpack
seo_title: Optimisation manuelle des builds Webpack
seo_desc: 'By Jamund Ferguson

  Back in April I shifted into a platform/architect role in my job at PayPal. I was
  tasked with looking at stability, performance and quality. One of the first things
  I did was graph our JavaScript bundle sizes over time.

  After a cou...'
---

Par Jamund Ferguson

En avril, j'ai changé de rôle pour devenir architecte plateforme chez PayPal. Ma mission était d'examiner la stabilité, les performances et la qualité. L'une des premières choses que j'ai faites a été de tracer l'évolution de la taille de nos bundles JavaScript au fil du temps.

Après quelques semaines, j'ai remarqué à plusieurs reprises des pics assez importants dans la taille de notre build, totalisant près de 1 Mo. En enquêtant, j'ai découvert que nous dupliquions des éléments partout.

NPM facilite l'installation de plusieurs versions de modules. Cela pose peu de problèmes dans le code serveur, mais lors de la création de bundles pour le web, c'est un gros problème. Webpack propose quelques outils de base pour inspecter les fichiers générés, mais pour comprendre ces données, il faut quelques commandes shell supplémentaires :

Laissez-moi vous expliquer ce qui se passe ici :

* **display-modules** est un flag de **webpack** qui affiche tous les modules node inclus dans le bundle.
* **awk** réorganise les colonnes et supprime les informations inutiles.
* **grep** supprime les très petits fichiers de la sortie.
* **sort -n** place les fichiers les plus volumineux en bas.
* **tail** n'affiche que les 100 derniers (et plus grands) fichiers.

Et avec cette magie, vous obtenez une liste comme celle-ci :

**ÉDITION :** il s'avère que quelque chose de similaire est intégré à webpack.

```
webpack --display-modules --sort-modules-by size
```

La sortie est un peu moins propre, mais elle trie correctement les éléments !

![Image](https://cdn-media-1.freecodecamp.org/images/1*XejQIc5Ql1sFn_Yqnlbkbg.png)

#### Enquête sur la source de la duplication

Une fois que vous suspectez avoir plusieurs versions d'un module, utilisez **npm ls** pour déterminer comment ce module est inclus dans votre projet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zqyzstRgV03WaPv556iwbg.png)

Bien que **npm ls** affiche tout dans votre dossier **node_modules**, **webpack** n'inclut peut-être pas chacun de ces fichiers dans le bundle. Il n'inclut que les fichiers qui sont **require()** quelque part dans votre code.

#### Arrêter la folie de la duplication

À ce stade, vous ressentez probablement une certaine fatigue du terminal. Vous avez tapé beaucoup de commandes, mais comment réduire réellement votre build ?

Dans l'exemple ci-dessus, ce projet dépend directement de **React 15**, mais l'une de ses dépendances repose sur [**react-intl**](https://github.com/yahoo/react-intl)**@1.2.2**, qui dépend de **React 0.13**.

La solution dans ce cas a été de remplacer notre dépendance à **react-intl** par une bibliothèque d'internationalisation compatible avec une version plus récente de React. Cela a représenté un travail non négligeable, car nous avons finalement écrit une alternative simplifiée.

Heureusement, beaucoup des autres problèmes de notre build étaient plus faciles à résoudre. Voici quelques exemples :

**Mon lodash est bien trop volumineux**

```
244kB  /Users/.../dev/paypal/web/~/lodash/dist/lodash.compat.js
```

Il existe plusieurs plugins qui peuvent optimiser vos builds lodash pour n'inclure que les parties que vous utilisez réellement. Cela peut réduire considérablement la taille des fichiers. Si vous utilisez Babel, je vous suggère [https://github.com/lodash/babel-plugin-lodash](https://github.com/lodash/babel-plugin-lodash) ou, sinon, vous pouvez essayer [https://github.com/lodash/lodash-webpack-plugin](https://github.com/lodash/lodash-webpack-plugin).

Avant l'arrivée de ces plugins, nous avons utilisé la règle ESLint [**no-restricted-module**](http://eslint.org/docs/rules/no-restricted-modules) pour interdire **lodash** dans notre dossier **public/** (en faveur d'underscore). Cela nous empêche simplement d'importer les deux dans le projet.

**J'ai trop de jQuery**

```
259kB  /Users/jamuferguson/dev/paypal/web/~/jquery/dist/jquery.js273kB  ./lib/jquery-1.10.2.js
```

Dans ce cas, nous avons une version locale de jQuery que nous utilisons depuis longtemps et que nous avons aliasée, mais nous avons également un autre module qui dépend explicitement de la dernière version de jQuery.

La solution la plus simple est de supprimer votre copie locale et de vous appuyer sur la version installée dans NPM. Utilisez toujours la version la plus récente possible, car les dépendances futures utiliseront probablement cette version également.

Que faire si vous ne pouvez pas passer à la dernière version de jQuery en raison de problèmes de compatibilité avec les navigateurs ? Essayez le [plugin jQuery Migrate](http://jquery.com/download/#jquery-migrate-plugin) si cela pose problème, ou encouragez les mainteneurs du module (via une issue GitHub) à être plus inclusifs dans leur fichier package.json.

```
"jquery": "^1 || ^2"
```

Cette syntaxe permet à un package de dépendre soit de la version 1, soit de la version 2. Dans de nombreux cas, cela permettra la compatibilité ascendante dont vous avez besoin.

**Réduction de la taille**

Mon équipe a pu réduire la taille de notre bundle JavaScript _minifié_ de près de 800 Ko en utilisant ces techniques. D'autres ont signalé des [réductions réussies de Moment.js](http://stackoverflow.com/questions/25384360/how-to-prevent-moment-js-from-loading-locales-with-webpack) de plusieurs centaines de Ko en utilisant des plugins webpack.

Avez-vous des problèmes pour garder vos builds webpack petits ? Quelles sont les autres approches que vous avez vues pour réduire la taille du build ?