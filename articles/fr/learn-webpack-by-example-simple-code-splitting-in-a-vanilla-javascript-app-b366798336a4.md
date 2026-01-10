---
title: 'Apprendre Webpack par l''exemple : le code-splitting simple dans une application
  vanilla JavaScript'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-10T19:00:23.000Z'
originalURL: https://freecodecamp.org/news/learn-webpack-by-example-simple-code-splitting-in-a-vanilla-javascript-app-b366798336a4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*omrsDb09E3ZcHc9lQmTCJw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: webpack
  slug: webpack
seo_title: 'Apprendre Webpack par l''exemple : le code-splitting simple dans une application
  vanilla JavaScript'
seo_desc: 'By Kalalau Cantrell

  Using webpack 4 and dynamic imports


  A tasty split

  This article is part of an episodic guide for learning Webpack through various examples.
  If you need a refresher on what loaders and plugins are as far as Webpack goes,
  or what a ...'
---

Par Kalalau Cantrell

#### Utilisation de webpack 4 et des imports dynamiques

![Image](https://cdn-media-1.freecodecamp.org/images/1*omrsDb09E3ZcHc9lQmTCJw.jpeg)
_Un split appétissant_

Cet article fait partie d'un guide épisodique pour apprendre Webpack à travers divers exemples. Si vous avez besoin d'un rappel sur ce que sont les **loaders** et les **plugins** en ce qui concerne Webpack, ou à quoi ressemble un fichier `webpack.config.js` de base, consultez [cet article](https://medium.freecodecamp.org/learn-webpack-by-example-blurred-placeholder-images-4ad8b1751709) que j'ai écrit et qui se concentre sur ces bases.

Si vous êtes comme je l'étais, vous avez déjà entendu le terme code-splitting et en avez [lu quelque chose](https://webpack.js.org/guides/code-splitting/). Mais peut-être que vous continuiez à tomber sur des articles expliquant comment le faire avec tel ou tel framework, plutôt que sur des explications de son utilité et un exemple de base illustrant cette utilité.

Bien que j'accorde une grande valeur aux frameworks et à la vitesse et la structure qu'ils apportent au codage, surtout au sein des équipes, j'accorde également de l'importance à la compréhension des concepts de programmation aussi profondément que possible.

Cela signifie souvent que si j'essaie d'apprendre un nouveau concept, je vais essayer de le décomposer en sous-concepts plus petits, puis étudier chacun d'eux isolément avant de les intégrer tous ensemble.

Pour prendre un exemple non lié à la programmation, si je voulais apprendre à faire du longboard, je voudrais me concentrer fortement sur le fait de simplement garder mon équilibre en restant debout sur le longboard avant de m'inquiéter d'aller vite, de faire des figures ou de personnaliser mon setup de longboard.

Ainsi, pour apprendre le code-splitting, j'ai décidé que je voulais créer une application aussi petite et simple que possible, ce qui pour moi signifiait pas de frameworks et rien de compliqué.

### Aperçu de l'application

Je veux partager la petite application que j'ai créée pour m'aider à explorer le code-splitting avec Webpack. Mon espoir est qu'elle puisse également vous aider à mieux comprendre le sujet. Tout ce que nous allons faire, c'est créer l'application monopage représentée dans le gif ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PAgEvQIem4yR82UpPZfpVg.gif)
_Un itinéraire appétissant_

Si vous souhaitez suivre dans votre éditeur de code, consultez le code dans la branche `code-split` de [ce dépôt](https://github.com/klcantrell/webpack-through-example-blog). Une fois que vous avez installé les packages, `npm start` exécutera un serveur de développement pour vous si vous souhaitez voir le code-splitting en action.

Notre application a deux routes : une route **accueil**, sur laquelle l'utilisateur commence, et une route **tasty**. La vue pour la route **accueil** est très basique : juste un en-tête et un lien vers la route **tasty**.

La vue pour la route **tasty**, cependant, a beaucoup plus de contenu. Elle présente une délicieuse animation de donut réalisée avec SVG et tout le balisage et le CSS qui vont avec ce genre de chose. C'est beaucoup de code comparé à notre route **accueil**. P.S. merci à [Ben Visser](https://codepen.io/benvisser/) pour avoir créé l'animation.

Est-il judicieux de faire télécharger à l'utilisateur _tout_ le code de cette application immédiatement, y compris le code pour la route **tasty** et son animation ? Seulement si vous souhaitez causer des temps de chargement initiaux lents et de la frustration, sans parler de la peur de manquer ce qui aurait pu se passer si l'utilisateur était resté pour que votre application se charge ;). Alors, découvrons comment faire du code-splitting pour cette application.

Tout d'abord, voici un aperçu de haut niveau du code derrière l'application. L'application est écrite en vanilla JS. J'ai utilisé une seule bibliothèque externe, `[navigo](https://www.npmjs.com/package/navigo)`, pour gérer notre routage côté client. Regardons le fichier `index.js` :

Et voici ce que fait le module `App` :

Et voici un exemple de composant UI, notre composant `Home` :

### Pas de code-splitting

Sans code-splitting, vous enverriez à votre utilisateur un gros bundle de code lorsqu'il charge initialement votre application. Établissons une base en regardant la taille de notre bundle ici sans code-splitting.

Vous pouvez voir dans l'image ci-dessous que la taille de notre bundle est de **22,8K**. Bien que ce ne soit pas très grand comparé aux applications réelles dans le monde, faisons semblant que c'est le cas pour l'apprentissage.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_nm-Y524qO9uVDh-NEr5EQ.gif)

### Code-splitting avec des imports dynamiques

Maintenant, introduisons le code-splitting ! Rappelez-vous, ce que nous voulons faire, c'est empêcher l'utilisateur de devoir télécharger le code nécessaire pour rendre la route **tasty** jusqu'à ce qu'il en ait besoin.

Pour y parvenir, nous allons utiliser une fonctionnalité qui arrive en JavaScript appelée **imports dynamiques**. Même si cette fonctionnalité n'a pas encore été intégrée à la spécification ECMAScript, Webpack et Babel nous permettent de l'utiliser dès maintenant.

Un import dynamique nous permet de récupérer un module de manière asynchrone. Il retourne une promesse. Dans le callback de la promesse, nous pouvons spécifier quoi faire avec le module une fois qu'il est chargé. La syntaxe pour un import dynamique ressemble à ceci :

```
import('./path/to/module')
```

Lorsque Webpack voit un import dynamique comme celui-ci, il ne bundle pas le module importé dans le bundle actuel. Au lieu de cela, il divise le bundle en deux morceaux plus petits.

Le morceau actuel peut être chargé de manière synchrone (comme notre chargement initial de page), mais le module qui est importé par notre import dynamique est chargé de manière asynchrone. Dans notre cas, le module pour la route **tasty** est chargé lorsque l'utilisateur visite cette route.

Pour accéder à la fonctionnalité d'import dynamique, nous devons `npm install` quelques packages Babel dans notre processus de build : `babel-core`, `babel-loader` et `babel-plugin-syntax-dynamic-import` sont définitivement nécessaires.

Selon le navigateur que vous utilisez, vous n'aurez peut-être pas besoin de `babel-preset-env` (par exemple, la version actuelle de Chrome prend en charge toute l'autre syntaxe JavaScript que nous utilisons), mais installons-le quand même, juste pour être sûr.

Ensuite, nous configurons Webpack pour Babel :

Enfin, nous pouvons écrire notre import dynamique :

Voici ce que ce code dit de faire : lorsque la route **tasty** est déclenchée, d'abord récupérer le composant `Tasty`. Ensuite, une fois qu'il a fini de charger, le rendre sur la page.

Voyons ce que cela fait pour nous. Dans l'image ci-dessous, vous pouvez voir que le chargement initial de la page télécharge maintenant un bundle qui fait **10,8K** au lieu de **22,8K** — bien mieux ! Ensuite, lorsque l'utilisateur clique pour aller à la route **tasty**, un autre morceau de bundle de **13,6K** est téléchargé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AcjPAOjrzFkj0eVZ9FINKQ.gif)

Webpack nomme automatiquement ces morceaux — si vous voulez contrôler cela, consultez [cette section](https://webpack.js.org/api/module-methods/#import-) de la documentation de webpack.

### Améliorations de l'UX

C'est génial que nous ayons évité à l'utilisateur d'avoir à attendre un temps supplémentaire pour que la page se charge initialement. Mais, pouvez-vous deviner ce qui se passerait si l'utilisateur était sur une connexion super lente et essayait de charger la route **tasty** ?

Avec la façon dont nous avons actuellement configuré les choses, la page resterait simplement en suspens jusqu'à ce que le module `Tasty` soit entièrement chargé. Ces quelques moments de suspension pourraient laisser l'utilisateur se demander si notre application fonctionnait même.

Améliorons cette expérience en donnant à l'utilisateur un signal que notre application fait quelque chose pendant qu'il attend :

Maintenant, notre application affichera un spinner de chargement pendant que le composant `Tasty` se charge. Bien que cela puisse augmenter quelque peu la taille de notre bundle initial, cela donne à l'utilisateur une indication que quelque chose se passe pendant qu'il attend.

Ce compromis échange un peu de performance pour une meilleure expérience utilisateur — trouver cet équilibre, c'est tout l'art !

![Image](https://cdn-media-1.freecodecamp.org/images/1*rVRdOSa88XmWID8yzDwl2Q.gif)

### Conclusion et lectures complémentaires

J'espère que cet exemple a servi de représentation simple du bénéfice du code-splitting ainsi que de la façon d'utiliser un outil comme Webpack pour vous aider à le faire.

J'espère également qu'il a montré que le code-splitting n'est pas une technique utile uniquement pour certains frameworks. En fait, les applications vanilla JS peuvent utiliser le code-splitting, et même les applications qui sont principalement rendues côté serveur mais qui ont des widgets interactifs intégrés ici et là peuvent utiliser cette technique.

Si vous souhaitez approfondir le code-splitting granulaire que webpack vous permet de faire, regardez le plugin `[optimization.splitChunks](https://webpack.js.org/plugins/split-chunks-plugin/)` qui vient avec webpack 4.

**Merci d'applaudir si cela vous a aidé à apprendre quelque chose, commentez ci-dessous avec vos questions, et n'hésitez pas à dire bonjour à [moi](https://twitter.com/kalalaucantrell) sur Twitter.**