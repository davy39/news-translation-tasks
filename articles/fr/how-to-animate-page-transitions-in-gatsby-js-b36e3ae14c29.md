---
title: Comment animer les transitions de page dans Gatsby.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-11T18:20:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-animate-page-transitions-in-gatsby-js-b36e3ae14c29
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Bb4qv_rhVEVz3JRtHD2zOg.png
tags:
- name: animation
  slug: animation
- name: GatsbyJS
  slug: gatsbyjs
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment animer les transitions de page dans Gatsby.js
seo_desc: 'By Dimitri Ivashchuk

  I’m totally enjoying Gatsby for various reasons, and in this post I want to share
  how easy it is to add customized page transitions to your website to make it more
  lively and smooth.

  We will be using Gatsby default starter to mak...'
---

Par Dimitri Ivashchuk

Je prends énormément de plaisir à utiliser Gatsby pour diverses raisons, et dans cet article, je souhaite partager à quel point il est facile d'ajouter des transitions de page personnalisées à votre site web pour le rendre plus _vivant_ et _fluide_.

Nous utiliserons le [starter par défaut de Gatsby](https://www.gatsbyjs.org/) pour rendre cet exemple aussi isolé que possible, mais vous pouvez être sûr que cela fonctionnera également pour des starters plus complexes et des projets créés par vous à partir de zéro.

En guise de teaser, nous allons construire quelque chose de similaire à ce que vous voyez lorsque vous suivez des liens sur ce site. ?

### Mise en route ?f3c3f3ff

Si vous êtes nouveau dans Gatsby et que vous souhaitez suivre ce tutoriel, assurez-vous d'installer l'interface de ligne de commande de Gatsby ([Gatsby CLI](https://www.gatsbyjs.org/docs/)) afin de pouvoir rapidement démarrer de nouveaux projets à l'avenir.

`npm install --global gatsby-cli`

Naviguez vers votre dossier de projet et créez un nouveau projet Gatsby à l'intérieur en exécutant la commande suivante dans le terminal :

`gatsby new .`

Il créera un projet avec la configuration la plus simple possible et il devrait ressembler à ceci : (il peut varier en raison des itérations ultérieures sur la conception du starter)

![Image](https://cdn-media-1.freecodecamp.org/images/1*cl5xYdPxb87Pvw2cNOPFQg.png)
_Gatsby-default-starter_

### Installation des dépendances nécessaires f52e

Tout d'abord, nous devons installer [react-transition-group](https://github.com/reactjs/react-transition-group) qui est responsable de la surveillance des éléments entrant et sortant du DOM et de l'application d'animations à ceux-ci.

`npm install react-transition-group`

Nous installerons également [gatsby-plugin-layout](https://www.gatsbyjs.org/packages/gatsby-plugin-layout/) qui, dans notre cas, fournit la propriété de localisation requise pour que les transitions fonctionnent et injecte notre mise en page dans chaque page.

`npm install gatsby-plugin-layout`

Pour que le plugin fonctionne comme prévu, nous devons déplacer notre composant de mise en page dans le dossier des mises en page à la racine de notre projet et le renommer en `index.js`. Ajoutons également `transition.js` à notre dossier de composants où nous fournirons toute la logique de transition. Pour l'instant, laissez-le vide car nous avons un peu plus à configurer.

La dernière étape consiste à ajouter notre `gatsby-plugin-layout` à notre fichier `gatsby-config.js` qui se trouve à la racine de notre projet.

### Composant de transition ?

Cela contient toute la logique de transition qui sera appliquée lorsqu'un utilisateur décide de suivre un lien vers une autre page de notre site.

À l'intérieur de `transition.js`, ajoutez le code suivant que je vais expliquer dans les commentaires :

Maintenant, nous pouvons importer le composant `Transition` dans le composant Layout et envelopper les enfants qui représentent nos pages à l'intérieur de celui-ci.

À ce stade, vous pouvez rencontrer un bug lorsque certains éléments de votre page sont rendus deux fois. Pour résoudre cela, parcourez les fichiers dans le dossier `pages` et assurez-vous qu'ils n'importent pas le composant `<Layout>` et ne l'utilisent pas dans l'instruction return.

![Image](https://cdn-media-1.freecodecamp.org/images/1*grgRx163jrF102OjEy39mw.gif)
_Animation saccadée que nous voulons corriger_

Maintenant que tout fonctionne comme prévu et que vous profitez de vos nouvelles transitions de page, vous pouvez remarquer un léger bug saccadé qui apparaît lorsque votre page est défilée vers le bas et que l'animation commence. Notez que cela se produit lorsqu'il y a plus de contenu sur la page et que vous pouvez faire défiler.

Nous pouvons facilement corriger cela en incluant le code ci-dessous dans notre `gatsby-browser.js` que vous pouvez trouver à la racine de notre projet. Ce que nous faisons ici, c'est en fait définir un délai d'attente pour l'animation et attendre qu'elle soit exécutée jusqu'à ce que la page fasse défiler vers le haut.

Sur votre site web, cela devrait ressembler à ceci

![Image](https://cdn-media-1.freecodecamp.org/images/1*ghYOAUkIT1KOSqXcYHzw3w.gif)

J'espère que vous avez apprécié ce petit article et que vous utiliserez vos nouvelles connaissances chaque fois que vous en aurez besoin. Ici, vous pouvez trouver un [lien vers le dépôt GitHub](https://github.com/d-ivashchuk/animating-gatsby-pt) avec le code fonctionnel pour ce tutoriel. Abonnez-vous à [mon compte Twitter](https://twitter.com/DivDev_) pour ne pas manquer le prochain article sur Gatsby.js et les choses amusantes que vous pouvez faire avec !

_Publié à l'origine sur_ [https://divdev.io](https://divdev.io) qui, soit dit en passant, utilise la technique d'animation que nous avons apprise dans cet article !