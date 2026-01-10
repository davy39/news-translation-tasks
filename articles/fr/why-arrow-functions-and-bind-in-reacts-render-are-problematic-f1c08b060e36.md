---
title: Pourquoi les fonctions fléchées et bind dans le Render de React posent problème
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-22T14:40:09.000Z'
originalURL: https://freecodecamp.org/news/why-arrow-functions-and-bind-in-reacts-render-are-problematic-f1c08b060e36
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mcgExlgxxMzp9ZugfTc9LQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: React Native
  slug: react-native
- name: Web Development
  slug: web-development
seo_title: Pourquoi les fonctions fléchées et bind dans le Render de React posent
  problème
seo_desc: 'By Cory House

  (Hint: It makes shouldComponentUpdate and PureComponent cranky)

  In a previous post, I explained how to extract React child components to avoid using
  bind or arrow functions in render. But I didn’t provide a clear demo to show why
  this i...'
---

Par Cory House

#### (Indice : Cela rend shouldComponentUpdate et PureComponent de mauvaise humeur)

Dans un précédent article, j'ai expliqué comment [extraire les composants enfants React pour éviter d'utiliser bind ou les fonctions fléchées dans render](https://medium.freecodecamp.org/react-pattern-extract-child-components-to-avoid-binding-e3ad8310725e). Mais je n'ai pas fourni de démonstration claire pour montrer pourquoi cela est utile.

Voici un exemple rapide.

Dans cet exemple, j'utilise une fonction fléchée dans render pour lier l'ID utilisateur pertinent à chaque bouton de suppression.

%[https://codesandbox.io/s/54k49onoyl?from-embed]

À la ligne 35, j'utilise une fonction fléchée pour passer une valeur à la fonction deleteUser. C'est un problème.

Pour voir pourquoi, consultez User.js (cliquez sur l'icône hamburger en haut à gauche pour sélectionner différents fichiers dans l'exemple). Je journalise dans la console chaque fois que render est appelé. J'ai déclaré User comme un [PureComponent](https://facebook.github.io/react/docs/react-api.html#react.purecomponent). Donc User ne devrait se re-rendre que lorsque les props ou l'état changent. Mais **quand vous cliquez sur supprimer pour un utilisateur, notez que render est appelé pour _toutes_ les instances de User**.

Voici pourquoi : Le composant parent transmet une fonction fléchée dans les props. Les fonctions fléchées sont réallouées à chaque render (même histoire avec l'utilisation de bind). Donc, bien que j'aie déclaré User.js comme un PureComponent, la fonction fléchée dans le parent de User fait que le composant User voit une nouvelle fonction être envoyée dans les props pour tous les utilisateurs. Donc chaque utilisateur se re-rend lorsque **_n'importe quel_** bouton de suppression est cliqué. ?

Résumé :

> Évitez les fonctions fléchées et les binds dans render. Cela casse les optimisations de performance comme shouldComponentUpdate et PureComponent.

### Que devrais-je faire à la place ?

Pour contraste, voici un exemple qui n'utilise pas de fonction fléchée dans render.

%[https://codesandbox.io/s/jnowr0ww7v?from-embed]

Dans cet exemple, index.js n'a pas de fonction fléchée dans render. Au lieu de cela, les données pertinentes sont transmises à User.js. Dans User.js, onDeleteClick appelle la fonction onClick transmise dans les props avec l'ID utilisateur pertinent.

Avec ce changement, lorsque vous cliquez sur supprimer, notez que render n'est pas appelé pour les autres utilisateurs ! ?

### Résumé

Pour des performances optimales,

1. Évitez les fonctions fléchées et bind dans render.
2. Comment ? [Extrayez les composants enfants](https://medium.freecodecamp.org/react-pattern-extract-child-components-to-avoid-binding-e3ad8310725e), ou [transmettez des données sur l'élément HTML](https://medium.com/@mgnrsb/another-way-to-avoid-binding-in-render-in-simple-cases-like-this-where-all-you-need-is-to-remember-68af83da0258).

### Vous cherchez plus d'informations sur React ? ⚔️

J'ai écrit [plusieurs cours sur React et JavaScript](http://bit.ly/psauthorpageimmutablepost) sur Pluralsight ([essai gratuit](http://bit.ly/pstrialimmutablepost)). Mon dernier, « [Creating Reusable React Components](http://bit.ly/psreactcomponentsimmutablepost) » vient d'être publié ! ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*BkPc3o2d2bz0YEO7z5C2JQ.png)

[Cory House](https://twitter.com/housecor) est l'auteur de [plusieurs cours sur JavaScript, React, le code propre, .NET, et plus encore sur Pluralsight](http://pluralsight.com/author/cory-house). Il est consultant principal chez [reactjsconsulting.com](http://www.reactjsconsulting.com), architecte logiciel chez VinSolutions, un Microsoft MVP, et forme des développeurs logiciels à l'international sur des pratiques logicielles comme le développement front-end et le code propre. Cory tweete sur JavaScript et le développement front-end sur Twitter en tant que [@housecor](http://www.twitter.com/housecor).