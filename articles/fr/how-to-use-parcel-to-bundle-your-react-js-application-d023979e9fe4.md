---
title: Comment utiliser Parcel pour bundler votre application React.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-31T16:10:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-parcel-to-bundle-your-react-js-application-d023979e9fe4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QrpgyDDba-3XhpRIDiPx-Q.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: reactjs
- name: technology
  slug: technology
seo_title: Comment utiliser Parcel pour bundler votre application React.js
seo_desc: 'By Michael Ozoemena

  What’s Parcel?

  Parcel is a web application bundler which offers a blazingly fast performance utilizing
  multicore processing and requires zero configuration.

  So like Webpack? Yes, like Webpack, but lighter and with no configuration...'
---

Par Michael Ozoemena

#### **Qu'est-ce que Parcel ?**

[Parcel](https://parceljs.org/) est un bundler d'applications web qui offre des performances extrêmement rapides en utilisant le traitement multicœur et ne nécessite aucune configuration.

Donc, comme Webpack ? Oui, comme Webpack, mais plus léger et sans configuration requise.

#### **Ce que cet article offre.**

Dans cet article, je vais vous montrer comment utiliser Parcel pour bundler votre application React.js de base construite avec JavaScript (ES6), HTML et CSS. Nous allons créer une application React.js à partir de "zéro" sans utiliser d'outils comme `create-react-app` ou autre.

### **Mise en route.**

La première chose à faire est de configurer notre projet. J'ai créé quelques fichiers de démarrage sur GitHub, que vous pouvez consulter [ici](https://github.com/THEozmic/getting-started-parcel). Une fois le projet cloné sur votre ordinateur, exécutez `git checkout beginning` et `npm install` pour mettre les choses en position de "départ" (notez qu'à ce stade, le projet ne fonctionne pas vraiment car nous n'avons pas encore de fichiers bundlés).

### **Bundler les fichiers.**

Maintenant, nous avons un simple serveur `express` configuré pour servir des fichiers depuis le dossier `dist/`. La raison pour laquelle vous voyez `cannot GET /` lorsque vous exécutez `npm start` et allez sur `localhost:5000/` est qu'aucun build n'a encore eu lieu. Ainsi, le dossier `dist/` est vide/inexistant.

Pour commencer à bundler nos fichiers et avoir quelque chose qui s'affiche lorsque vous allez sur `localhost:5000/`, nous devons faire quelques choses :

1. Installer Parcel en exécutant `npm install parcel-bundler --save`.
2. Créer des scripts de build.
3. Exécuter les scripts de build et démarrer notre serveur.
4. Charger `localhost:5000/` dans le navigateur.

### **Création de scripts de build et bundling des fichiers.**

Avant de passer à la création réelle des scripts de build et à leur ajout dans notre fichier `package.json`, apprenons un peu plus sur le bundling des fichiers.

**Notez** que la commande `parcel` ne fonctionnera pas si vous avez uniquement installé `parcel` dans le dossier `node_modules` de votre projet et non globalement avec le flag `-g`.

Une fonctionnalité intéressante qui vient avec Parcel (en plus d'autres choses incroyables) est le `dev-server` intégré avec [hot module replacement](https://parceljs.org/hmr.html). Vous pouvez simplement utiliser ce `dev-server` en exécutant `parcel index.html` où `index.html` est votre fichier HTML d'entrée.

Malheureusement, nous n'utiliserons pas la fonctionnalité `dev-server` dans notre projet de démonstration, car nous avons construit notre propre petit serveur `express`, mais cela ne signifie pas que nous n'aurons pas encore le `hot module replacement`. N'hésitez pas à essayer le `dev-server` par vous-même.

Les commandes que nous voulons utiliser à la place sont :

* `parcel watch index.html` pour bundler nos fichiers dans le dossier `dist/` et pour "surveiller" les changements de nos fichiers pendant le mode développement, et
* `parcel build index.html` pour simplement bundler nos fichiers et les déposer dans le dossier `dist/` (utile pour le mode production).

Si nous avions exécuté `npm install parcel-bundler -g` au lieu de `npm install parcel-bundler --save`, alors les commandes des paragraphes précédents s'exécuteront sans problème — mais nous ne l'avons pas fait. Nous avons installé Parcel dans notre dossier local `node_modules`, donc au lieu d'exécuter `parcel index.html`, nous exécuterons `./node_modules/.bin/parcel index.html` pour bundler nos fichiers.

Maintenant que nous avons appris tout cela, nous pouvons procéder à l'édition de notre fichier `package.json` et ajouter nos scripts de build.

```json
"scripts": {
    "parcel:dev": "./node_modules/.bin/parcel index.html",
    "parcel:watch": "./node_modules/.bin/parcel watch index.html",
    "parcel:build": "./node_modules/.bin/parcel build index.html"
  }
```

Comme vous pouvez le voir, j'ai créé trois `scripts npm`. Maintenant, lorsque nous exécutons `npm run parcel:watch`, nos fichiers seront bundlés dans le dossier `dist/`. Nous aurons également Parcel qui surveillera les changements que nous apportons lors de l'édition de nos fichiers CSS, HTML et JavaScript afin qu'il recharge à chaud la page pour nous.

### **Visualisation des résultats.**

Pour visualiser notre simple application React.js dans le navigateur, nous pouvons exécuter `npm start` (un script déjà existant) pour démarrer notre serveur `express`, qui devrait alors écouter sur `localhost:5000/`.

#### **Points clés à retenir.**

1. Vous pouvez démarrer avec Parcel avec absolument zéro configuration. Tout ce que vous avez à faire est de l'installer et d'exécuter les commandes.
2. Parcel est adapté aux modes développement et production.
3. Parcel dispose d'un `dev-server` intégré et d'un `hot module replacement` pour vous aider à avancer rapidement.
4. Il y a plus à Parcel que ce qui est dans cet article, alors assurez-vous de consulter la [documentation](https://parceljs.org/) pour obtenir plus de détails.

J'espère que vous avez apprécié. Si c'est le cas, n'oubliez pas de laisser un commentaire et quelques applaudissements.