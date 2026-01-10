---
title: Comment créer facilement une table des matières pour votre article
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-25T00:24:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-easily-create-a-table-of-contents-for-your-article-507e313b2af3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Bg43TmnKj37GvTiX8vHZCg.png
tags:
- name: medium
  slug: medium
- name: Node.js
  slug: nodejs
- name: 'tech '
  slug: tech
- name: writing
  slug: writing
- name: writing tips
  slug: writing-tips
seo_title: Comment créer facilement une table des matières pour votre article
seo_desc: 'By Adam Kelly

  In this article, I’ll discuss how you can create a table of contents for your Medium
  post, and I’ll show you how I built the feature.

  Table of Contents


  Get The URL

  Generate Your Table Of Contents

  Design

  Development

  Get the source


  Many...'
---

Par Adam Kelly

Dans cet article, je vais expliquer comment créer une table des matières pour votre publication Medium, et je vais vous montrer comment j'ai construit cette fonctionnalité.

#### Table des matières

* [Obtenir l'URL](https://medium.com/p/507e313b2af3#e2d0)
* [Générer votre table des matières](https://medium.com/p/507e313b2af3#b4b8)
* [Design](https://medium.com/p/507e313b2af3#d9a8)
* [Développement](https://medium.com/p/507e313b2af3#dca5)
* [Obtenir la source](https://medium.com/p/507e313b2af3#696e)

Beaucoup d'entre vous ont probablement vu [cet article](https://medium.freecodecamp.org/how-to-link-to-a-specific-paragraph-in-your-medium-article-2018-table-of-contents-method-e66595fea549) sur la façon de lier des parties de votre article Medium. Vous avez peut-être aussi vu [cette extension Chrome](https://medium.com/@castroalves/medium-anchor-a-must-have-chrome-extension-for-bloggers-c45dfdc6b91e), qui simplifie le processus.

Eh bien, vous pouvez faire encore mieux. Voici comment créer une table des matières pour votre article Medium, automatiquement.

### 1. Obtenir l'URL

Tout d'abord, vous avez besoin de l'URL de votre article Medium. S'il a été publié, il suffit de copier le lien depuis la barre d'adresse.

![Image](https://cdn-media-1.freecodecamp.org/images/FbUV0O6cwmoi23LHvzz2NrKX2MuiSju8xMVQ)

Si vous êtes encore en train d'écrire, cliquez sur le bouton "partager" dans le coin supérieur droit, et copiez le lien depuis là.

![Image](https://cdn-media-1.freecodecamp.org/images/VaWdhwfh2lPCB8GLINgsV4G4dgYpvVl9akgK)

### 2. Générer votre table des matières

Maintenant, la partie facile. Allez sur [www.mediumtoc.com](https://www.mediumtoc.com) et collez votre URL dans la barre d'entrée, puis cliquez sur "go".

![Image](https://cdn-media-1.freecodecamp.org/images/SeFydbL76uBcTWxPJBlP0hmWot5mc6li8H2f)

Ensuite, il devrait vous donner votre table des matières, que vous pouvez copier et coller dans votre article Medium !

![Image](https://cdn-media-1.freecodecamp.org/images/eEoCmfNhuAvDpM1-72E5vu6ZJ42NpZAPsU1w)

Vous pouvez voir cela en action en haut de cet article.

### Comment j'ai construit cela

#### Design :

J'ai d'abord conçu le site web dans [Sketch](https://www.sketchapp.com/). J'ai choisi de prendre quelques indices de design du site Medium, avec une police serif pour le titre, et j'ai également utilisé le même design de bouton.

J'ai choisi d'utiliser une barre d'entrée [https://material.io/guidelines/components/text-fields.html](https://material.io/guidelines/components/text-fields.html), car le design est fonctionnel et minimaliste, le style que je recherchais.

#### Développement :

L'architecture de cette application est largement basée sur la [JAM stack](https://jamstack.org/). Cela repose sur l'idée d'avoir du JavaScript côté client, des API réutilisables et un balisage préconstruit. Cela permet aux sites d'être hébergés sur des CDN.

L'architecture du site est :

**Front End :** [React](https://reactjs.org/) et [Preact](https://preactjs.com/) (une implémentation légère de DOM virtuel) en production

**Back End :** Express fonctionnant sur [Now](https://zeit.co/now), bien que je prévois de migrer vers AWS Lambda, car il n'y a qu'un seul point de terminaison API. Le back-end extrait les titres de l'article Medium et retourne leurs liens.

**Hébergement Front End / CDN :** Le site fonctionne sur [Netlify](https://www.netlify.com/), qui offre une intégration SSL gratuite et déploie automatiquement depuis la branche master sur GitHub.

Si quelqu'un est intéressé par l'un de ces sujets, laissez un commentaire et j'écrirai davantage à leur sujet !

Le site web a été conçu et développé sur une période de deux jours. Le premier jour était axé sur le back-end du site et le design. Le deuxième jour était consacré au développement. Il n'y a que 4 composants React, et j'ai choisi de ne pas utiliser Redux, car il n'y a pas beaucoup de changements dans l'état.

#### Obtenez la source !

Ceci est open source, donc vous pouvez obtenir tout le code sur [github.com/adamisntdead/medium-toc](https://github.com/adamisntdead/medium-toc). ✨

Un grand merci à la communauté freeCodeCamp pour leur merveilleuse [publication](http://medium.freecodecamp,com) !

### Si vous avez aimé cet article, laissez un applaudissement ! ? Vous voulez plus d'articles comme celui-ci ? S[uivez-moi.](http://medium.com/@adamisntdead/)