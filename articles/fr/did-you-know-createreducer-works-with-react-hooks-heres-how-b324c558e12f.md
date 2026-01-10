---
title: "Le saviez-vous\n\x14\ncreateReducer fonctionne avec les Hooks React. Voici\
  \ comment."
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-11T01:11:31.000Z'
originalURL: https://freecodecamp.org/news/did-you-know-createreducer-works-with-react-hooks-heres-how-b324c558e12f
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca782740569d1a4ca77b1.jpg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: "Le saviez-vous\n\x14\ncreateReducer fonctionne avec les Hooks React. Voici\
  \ comment."
seo_desc: 'By Yazeed Bzadough

  Don’t Use Hooks in Production yet

  At the time of this writing, Hooks are in alpha. Their API can change at any time.

  I recommend you experiment, have fun, and use Hooks in your side projects, but not
  in production code until they’r...'
---

Par Yazeed Bzadough

#### Ne pas utiliser les Hooks en production pour l'instant

Au moment de la rédaction de cet article, **les Hooks sont en version alpha. Leur API peut changer à tout moment.**

Je vous recommande d'expérimenter, de vous amuser et d'utiliser les Hooks dans vos projets secondaires, mais pas dans le code de production tant qu'ils ne sont pas stables.

### Code source et démonstration

Voici les liens [GitHub](https://github.com/yazeedb/react-createReducer-demo/) et [Codesandbox](https://codesandbox.io/s/github/yazeedb/react-createReducer-demo/tree/master/).

### useReducer

La [documentation React](https://reactjs.org/docs/hooks-reference.html#usereducer) contient un exemple d'application de compteur démontrant le Hook `useReducer`.

À des fins de démonstration, je l'ai légèrement stylisé.

![](https://cdn-media-1.freecodecamp.org/images/1*pe5b5CE-WaFteXtmzHIyHQ.gif)

#### Le code du composant

![](https://cdn-media-1.freecodecamp.org/images/1*vwqAHCV11OFG8lrjjz_05g.png)

Le JSX est simple : il affiche le `count` actuel avec 3 boutons.

Le composant `Counter` appelle `useReducer` avec un reducer et un état initial, ce qui renvoie un tableau avec l'état actuel `state` et une fonction `dispatch`.

Le fait de cliquer sur l'un des boutons appelle `dispatch` avec un objet action.

#### L'état initial

![](https://cdn-media-1.freecodecamp.org/images/1*CzA8Zc-Y2f4ATTQRV03w2w.png)

#### Le code du reducer

Le reducer décide comment l'état doit changer en fonction de l'état existant et de l'objet action qu'il reçoit.

Si vous avez travaillé avec Redux, vous connaissez cette configuration.

![](https://cdn-media-1.freecodecamp.org/images/1*WDNzQEnj2IqfDxhtmdSgpw.png)

Nous voyons qu'il prend en charge trois actions : `reset`, `increment` et `decrement`.

`reset` : Définit le `count` à 0.

`increment` : Augmente `count` de 1.

`decrement` : Diminue `count` de 1.

Toute autre action entraîne le retour de l'état donné par le reducer.

### createReducer

Vous connaissez peut-être aussi `createReducer`.

```js
function createReducer(initialState, handlers) {
  return function reducer(state = initialState, action) {
    if (handlers.hasOwnProperty(action.type)) {
      return handlers[action.type](state, action);
    } else {
      return state;
    }
  };
}
```

C'est une fonction d'assistance [issue de la documentation Redux](https://redux.js.org/recipes/reducingboilerplate) qui vous permet de décrire les reducers comme des mappages des types d'actions vers des gestionnaires.

#### Plus de cas switch

Au lieu des cas `switch`, nous pouvons utiliser des fonctions pour chaque type d'action.

Un avantage supplémentaire est que si l'action donnée ne correspond pas, `createReducer` gère le cas `default` en retournant `state`.

#### Fonctionne avec useReducer

Puisque `useReducer` est basé sur les mêmes principes, ils sont parfaitement compatibles !

Je vais créer un nouveau fichier de projet, `createReducer.js`.

![](https://cdn-media-1.freecodecamp.org/images/1*F6Mc6LYYEioMih5krutO2g.png)

Et exporter la fonction d'assistance depuis celui-ci :

![](https://cdn-media-1.freecodecamp.org/images/1*VQY7hwr2irQeUtC2v546-g.png)

Puis l'utiliser comme suit :

![](https://cdn-media-1.freecodecamp.org/images/1*l2XXR2nNj-RHeU5TK8GnqA.png)

#### Des reducers plus propres

Ceci, à mon avis, est beaucoup plus agréable.

Il suffit de lui donner l'état initial et un objet mappant les types d'actions à leurs fonctions correspondantes.

Vous pouvez accéder à `state` et `action` dans chacune de ces fonctions, donc vous avez toutes les informations dont vous avez besoin !

![](https://cdn-media-1.freecodecamp.org/images/1*pe5b5CE-WaFteXtmzHIyHQ.gif)

La fonctionnalité n'a pas changé du tout.

### Toujours juste un Reducer

Cela fonctionne parce que `useReducer` ne se soucie pas de _comment_ vous créez un reducer.

Qu'il s'agisse de `switch`, `if/else` ou `createReducer`, assurez-vous simplement que votre résultat final est un reducer.

J'espère que vous avez apprécié ce bref article !