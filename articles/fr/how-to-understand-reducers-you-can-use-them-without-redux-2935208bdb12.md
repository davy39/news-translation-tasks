---
title: 'Comment comprendre les Reducers : Vous pouvez les utiliser sans Redux'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T18:29:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-understand-reducers-you-can-use-them-without-redux-2935208bdb12
coverImage: https://cdn-media-1.freecodecamp.org/images/0*oxnWcgexaoRegwaf
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Comment comprendre les Reducers : Vous pouvez les utiliser sans Redux'
seo_desc: 'By Ryan Yurkanin

  TLDR: You can handle state with a reducer in your Class Components by having one
  function that translates actions into state changes. It centralizes all your setStates.

  ? What is a Reducer?

  Reducers are functions that take input and ...'
---

Par Ryan Yurkanin

**TLDR :** Vous pouvez gérer l'état avec un reducer dans vos composants de classe en ayant une fonction qui traduit les actions en changements d'état. Cela centralise tous vos setStates.

#### ? Qu'est-ce qu'un Reducer ?

Les reducers sont des fonctions qui prennent une entrée et décident quoi en faire en un seul endroit central. **C'est tout. ?**

Si vous avez une fonction qui détermine la vue à afficher en fonction d'une URL, c'est un reducer.

Les Redux Reducers™️ sont une utilisation spécifique des reducers qui interprètent les événements dans votre application, et comment cela change l'état de l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cK_UHSjJl7rfNUIwb8VZww.png)
_this.dispatch("RESET_COUNT_CLICKED")_

Si vous n'êtes pas familier avec Redux, l'exemple ci-dessus est généralement lancé en appelant une fonction `dispatch` avec une `action` (objet décrivant un événement). ?

Nous pouvons utiliser des reducers dès maintenant dans un composant de classe en créant une fonction qui gère la définition de l'état par un type d'action comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ze_yLCczSHAZudU7PKkkMQ.png)

Utiliser un reducer dans cet exemple simple est, à mon avis, excessif. Je suis heureux que React va fournir à la fois un hook `useState` et `useReducer` pour cette raison.

Si je remarquais que je passais des moyens de changer l'état, et que `count` devenait couplé avec quelques autres propriétés d'état, je passerais à un reducer.

Puisque Redux place tout son état dans un objet qui grandit rapidement, cela rend le modèle de reducer parfaitement adapté. Il est possible de supprimer les reducers de Redux, même si nous perdrions une tonne de fonctionnalités géniales.

Redux vous permet de `connecter` votre store global à votre composant. Vous pouvez traduire l'état en props. Ils fournissent également une fonction `dispatch` qui déclenche vos reducers.

Au lieu de passer une fonction `dispatch`, passons une fonction `update` qui fonctionne comme `setState`.

#### ? Créer une version moins bonne de Redux

![Image](https://cdn-media-1.freecodecamp.org/images/1*5JC7l1-iFIHhdtMaqGOlKA.png)

Lorsque vous appelez update, vous dites exactement comment l'état doit changer en ligne. Cela peut ou non être à côté d'autres changements d'état similaires.

**Avec un état suffisamment petit, cela semble en fait agréable et concis.** Si nous avions 5 composants ou plus changeant quelques propriétés d'état, il serait difficile de trouver la source des bugs. ? ?

Même sans changer Redux du tout, vous pouvez émuler ce modèle. Dispatcher des actions qui ressemblent à `SET_COUNT` sont des indices que nous voulons vraiment `setState`. C'est la chose facile à faire.

Si nous créons une action moins opinionnée comme `INCREMENT_BUTTON_CLICKED`, nous pourrions l'utiliser dans de nombreux reducers, et la charge utile de l'action ne varierait pas trop.

#### ? Les Reducers sont utiles pour plus que l'état

![Image](https://cdn-media-1.freecodecamp.org/images/1*61iLrIrkyPdayRLrMnySrA.png)
_L'entrée ici est l'URL actuelle, la sortie est la vue !_

Les reducers sont un excellent moyen de colocaliser les décisions. Si vous avez déjà travaillé avec react-router-4, alors le code ci-dessus devrait vous sembler assez familier.

Grâce au composant `<Switch />`, nous pouvons imbriquer ces reducers de route-vue n'importe où.

Maintenant, si quelqu'un a la question "Quelles sont toutes les façons dont l'URL peut changer ce qui est rendu", ils ont un endroit central pour chercher.

#### ? Résumer

1. Les reducers en tant que modèle existent en dehors de Redux et de Javascript et sont simples à implémenter. Ils ont une seule responsabilité : prendre une entrée et donner une sortie.
2. Les Redux Reducers transforment les événements de l'application en état. Vous n'avez pas besoin de Redux pour faire cela maintenant, vous pouvez le faire avec l'état local du composant.
3. Les reducers facilitent l'organisation et la recherche des différentes variations de ce qui peut se passer dans le code et sont utiles à mesure que les applications deviennent grandes.

Si vous avez des questions ou si vous cherchez un mentorat React en tête-à-tête, n'hésitez pas à me tweeter **@yurkaninryan** à tout moment !

Si vous aimez mon style d'écriture, voici quelques autres articles que j'ai écrits.