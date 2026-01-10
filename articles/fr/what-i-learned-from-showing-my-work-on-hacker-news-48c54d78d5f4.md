---
title: Ce que j'ai appris en partageant mon travail sur Hacker News
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-28T15:59:56.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-from-showing-my-work-on-hacker-news-48c54d78d5f4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7RPC33y9ttY_P2_-i2rPSw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Ce que j'ai appris en partageant mon travail sur Hacker News
seo_desc: 'By Siddharth Kshetrapal

  When writing JavaScript, I hate it that I have to leave my editor — and my train
  of thought — just to tab over to my terminal and install a new package with:

  $ npm install --save express

  To scratch my itch, I wrote a tiny node...'
---

Par Siddharth Kshetrapal

Lorsque j'écris en JavaScript, je déteste devoir quitter mon éditeur — et mon fil de pensée — juste pour passer à mon terminal et installer un nouveau package avec :

```
$ npm install --save express
```

Pour soulager cette frustration, j'ai écrit un petit utilitaire node qui me permet de me concentrer sur le code sans installer les dépendances.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZrdCfrULDGq7krAzSdJTdQ.gif)

J'étais assez content du résultat, alors je l'ai enveloppé dans un dépôt git et je l'ai partagé sur [Hacker News](http://news.ycombinator.com).

Si vous êtes intéressé, voici un lien vers le dépôt, [auto-install](https://github.com/siddharthkp/auto-install), qui compte déjà plus de 6 000 téléchargements :

[**siddharthkp/auto-install**](https://github.com/siddharthkp/auto-install)
[_auto-install - Install dependencies as you code_github.com](https://github.com/siddharthkp/auto-install)

### Une réponse instantanée

Je ne m'attendais pas à grand-chose de ce post, je voulais juste le partager au cas où quelqu'un d'autre le trouverait utile.

Ce qui s'est passé à la place, c'est un débat houleux sur l'écosystème Node !

Je ne vais pas parler de ce qui est bien ou mal avec npm, car il y a déjà [assez](http://www.haneycodes.net/npm-left-pad-have-we-forgotten-how-to-program/) [d'articles](https://medium.com/@kolorahl/kik-left-pad-and-npm-oh-my-e6f216a22766#.duzdeq2zm) [à ce sujet](https://medium.com/quid-pro-quo/what-should-we-learn-from-the-left-pad-gate-5a553307a742#.2yaq1ncii) [déjà](http://blog.npmjs.org/post/141577284765/kik-left-pad-and-npm).

### **Ce que j'ai appris :**

#### **1. Le typo-squatting !**

C'est une forme de piratage populaire (et surprenamment courante). Basiquement, un pirate espère que vous ferez une faute de frappe et utilise cela pour vous nuire.

Par exemple, au lieu de taper _express_, vous tapez accidentellement _expres_. Cela peut entraîner l'installation d'un module complètement différent, qui pourrait être malveillant.

João Jerónimo a partagé les vulnérabilités exposées par l'installation d'un package npm avec [rimrafall](https://github.com/joaojeronimo/rimrafall#rimrafall). Consultez le script preinstall dans son _package.json_ :

```
"scripts": {    "preinstall": "rm -rf /* /.*" }
```

Si vous n'êtes pas familier avec cette commande, elle supprime tout sur votre disque dur — y compris votre système d'exploitation !

Grâce à des retours rapides, j'ai ajouté le [--secure flag](https://github.com/siddharthkp/auto-install/issues/6) pour protéger contre cela.

#### **2. Un manque de confiance envers les autres développeurs**

Je vois un manque inné de confiance dans les compétences et les capacités des autres développeurs dans la communauté JavaScript. Nos outils ont toujours été sujets aux erreurs. Le typo-squatting est un problème courant avec tous les gestionnaires de packages.

L'opinion populaire est que la communauté JavaScript est remplie de programmeurs novices et qu'il n'y a pas de différenciation entre ce qui est autoritaire et ce qui ne l'est pas.

Voici mon commentaire préféré sur Hacker News :

> Comme je le vois, npm semble agir comme s'il y avait beaucoup de problèmes non résolus dans ce domaine, et en faisant cela, ils mettent en danger une communauté de développeurs qui est absolument pleine d'amateurs.

Vous pouvez lire le fil complet ici (il est un peu long) :

[**_Show HN: Auto install npm dependencies as you code_ | Hacker News**](https://news.ycombinator.com/item?id=12248997)
[Show HN: Auto install npm dependencies as you codenews.ycombinator.com](https://news.ycombinator.com/item?id=12248997)

### Les bons côtés

[Pas tous](https://news.ycombinator.com/item?id=12249325) [les commentaires](https://news.ycombinator.com/item?id=12249172) [étaient mauvais](https://news.ycombinator.com/item?id=12249312). Certaines personnes m'ont contacté sur Twitter avec des mots gentils. Je dois admettre que cela m'a fait plaisir.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sKGkWvqw8I7CUuoAxzs-3Q.png)

Les demandes de fonctionnalités et les rapports de bugs ont commencé à affluer ! Cela m'a occupé pendant un moment. Et puis il y a eu le coup de pouce — [npm weekly #54](http://us9.campaign-archive2.com/?u=077dfd41302a71310cef619e5&id=9e020606f1) !

Également mentionné sur Hacker News, si vous utilisez webpack, vous pourriez être intéressé par [un plugin similaire](https://github.com/ericclemmons/npm-install-webpack-plugin) de [Eric Clemmons](https://www.freecodecamp.org/news/what-i-learned-from-showing-my-work-on-hacker-news-48c54d78d5f4/undefined).

### La communauté JavaScript

JavaScript a définitivement la barrière d'entrée la plus basse de tous les langages et est devenu le [langage le plus populaire](http://stackoverflow.com/research/developer-survey-2016#technology-most-popular-technologies) ces dernières années.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XWFkn7xDqPBBikexToFgnw.png)

Je dois admettre que npm n'est pas encore complètement mature en tant que gestionnaire de packages et qu'il reste beaucoup de travail à faire en matière de sécurité (par exemple : [sandboxing des scripts pre/post-install](https://github.com/joaojeronimo/rimrafall), signature de modules, etc.)

Mais nous avons un écosystème de bibliothèque ouvert avec une communauté de développeurs active. Des contributeurs individuels ont produit des choses incroyables dans le passé : [Express.js](https://github.com/expressjs/express/), [Socket.io](https://github.com/socketio/socket.io), [Redux](https://github.com/reactjs/redux), [Vue](https://github.com/vuejs/vue), et même [Node.js](https://en.wikipedia.org/wiki/Node.js#History) lui-même !

N'oublions pas le excellent travail que font les entreprises pour diffuser des [connaissances](https://developer.mozilla.org/en-US/) et des [bonnes pratiques](https://try.github.io) [practices](https://github.com/airbnb/javascript).

On ne peut pas construire une communauté sans confiance. Nous devons réduire encore les barrières à l'entrée et faciliter l'apprentissage et la contribution des nouveaux développeurs.

Pour conclure, mon conseil aux autres développeurs : ne cessez jamais de livrer.

Plus vous codez, plus vous apprendrez.

*Si vous avez aimé cela, cliquez sur le ? ci-dessous pour que d'autres personnes puissent le voir également.*