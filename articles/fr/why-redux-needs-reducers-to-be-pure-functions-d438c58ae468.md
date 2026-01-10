---
title: Pourquoi Redux a besoin que les reducers soient des "fonctions pures"
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-22T19:28:08.000Z'
originalURL: https://freecodecamp.org/news/why-redux-needs-reducers-to-be-pure-functions-d438c58ae468
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NkvKvkRk8RcMgQLJoIIBsQ.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Pourquoi Redux a besoin que les reducers soient des "fonctions pures"
seo_desc: 'By rajaraodv

  You may have heard that Redux depends on “pure functions” from functional programming.
  Well, what exactly does that mean?

  The picture below shows a simple Todo app from Redux examples. It currently has
  four tasks. It shows the fourth one...'
---

Par rajaraodv

Vous avez peut-être entendu dire que Redux dépend des "fonctions pures" de la programmation fonctionnelle. Mais que signifie exactement cela ?

L'image ci-dessous montre une simple application Todo provenant des [exemples Redux](https://github.com/reactjs/redux/tree/master/examples/todos). Elle contient actuellement quatre tâches. Elle montre la quatrième comme terminée et est configurée pour afficher "Toutes" les tâches — à la fois terminées et non terminées.

Le côté droit montre l'état actuel stocké dans Redux. C'est un simple objet JavaScript qui capture tous les détails en un seul endroit.

C'est la beauté de Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/4eco4msoESVRWtcsEabWFpm0WWzxEO1gDURs)
_GAUCHE : Application Todo ← → DROITE : État Redux_

Maintenant, supposons que vous avez basculé la quatrième tâche pour qu'elle ne soit pas terminée. Voici à quoi ressemblerait l'application avec un nouvel état Redux :

![Image](https://cdn-media-1.freecodecamp.org/images/6WaOKohJOCgbgJGvAoYokKhcZR-wNmDYWVBc)
_Redux met à jour son état lorsque l'application change_

Maintenant, si vous regardez le Reducer pour "TOGGLE_TODO" — celui qui bascule l'état d'un élément Todo entre terminé et non terminé — il ressemble à ceci ([voici le code source](https://github.com/reactjs/redux/blob/master/examples/todos/src/reducers/todos.js#L9-L17)) :

![Image](https://cdn-media-1.freecodecamp.org/images/-jheepAaXFn835dchdmurqshr8-d1Dm7AVDV)

Lorsque vous basculez l'état d'un élément Todo, voici ce qui se passe : la fonction reducer prend un objet qui représente l'état "ancien" (c'est-à-dire l'entrée d'une fonction), puis crée un tout nouvel objet en copiant tous les détails de l'ancien objet (comme **id** et **text**) et en remplaçant les anciennes propriétés par de nouvelles (**propriété completed**).

![Image](https://cdn-media-1.freecodecamp.org/images/Moec8tswLUsuI8-zFNT5gs-Y0HKMSAm6nqSe)

### Fonctions pures

À un niveau fondamental, toute fonction qui ne modifie pas les données d'entrée et qui ne dépend pas de l'état externe (comme une base de données, le DOM ou une variable globale) et qui fournit de manière cohérente la même sortie pour la même entrée est une fonction "pure".

Par exemple, la fonction **add** ci-dessous ne modifie pas "a" ou "b", ne dépend pas de l'état externe et retourne toujours la même sortie pour la même entrée.

```
const add = (a, b) => a + b // fonction pure
```

Maintenant, si vous regardez notre fonction reducer, c'est une fonction "pure" car elle possède les mêmes caractéristiques.

### Mais _pourquoi_ le reducer doit-il être une fonction "pure" ?

Voyons ce qui se passe si nous rendons notre reducer "impur". Commentons la section où il crée un nouvel objet, et à la place, modifions directement la propriété completed de l'état.

```
case 'TOGGLE_TODO':      if (state.id !== action.id) {        return state;      }
```

```
            // return {      //   ...state,      //   completed: !state.completed      // }
```

```
      state.completed = !state.completed;// modifie l'objet original      return state;
```

```
default: ...
```

Maintenant, si nous essayons de basculer le TODO après cette modification, rien ne se passe !

Voyons ce qui se passe dans le code source de Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/lxQkKAq1x7nWzokdsojlcF9gjhQi3ZUNM38Z)

Redux prend un état donné (objet) et le passe à chaque reducer dans une boucle. Et il s'attend à un _tout nouvel_ objet de la part du reducer s'il y a _des_ changements. Et il s'attend également à recevoir l'ancien objet si aucun changement n'a été apporté.

Redux vérifie simplement si l'ancien objet est le même que le nouvel objet en comparant les emplacements mémoire des deux objets. Donc, si vous modifiez la propriété de l'ancien objet à l'intérieur d'un reducer, le "nouvel état" et l'"ancien état" pointeront tous deux vers le même objet. Par conséquent, Redux pense que rien n'a changé ! Donc cela ne fonctionnera pas.

Cependant, cela ne répond toujours pas à certaines questions clés comme :

* Pourquoi Redux est-il conçu ainsi ?
* Pourquoi Redux ne peut-il pas simplement faire une copie de l'ancien état quelque part, puis comparer les propriétés des objets des reducers ?
* Pourquoi Redux impose-t-il ce fardeau aux développeurs individuels ?

La réponse : il n'y a qu'une seule façon de savoir si deux objets JavaScript ont les mêmes propriétés. Les comparer en profondeur.

Mais cela devient extrêmement coûteux dans les applications réelles, en raison des objets généralement volumineux et du nombre de fois où ils doivent être comparés.

Une solution consiste donc à **avoir une politique** demandant aux développeurs de créer un **nouvel** objet chaque fois qu'il y a un changement, puis de l'envoyer au framework. Et s'il n'y a pas de changements, alors renvoyer l'ancien objet tel quel. **En d'autres termes, les nouveaux objets représentent de nouveaux états.**

Notez que vous devez cloner les anciens états en utilisant slice — ou un mécanisme similaire — pour copier les anciennes valeurs dans un nouvel objet.

Maintenant, avec cette politique en place, vous pouvez comparer les emplacements mémoire de deux objets en utilisant `!==` sans avoir à comparer chaque propriété au sein de chaque objet. Et si les deux objets ne sont pas les mêmes, alors vous savez que l'objet a changé d'état (c'est-à-dire qu'une propriété quelque part dans l'objet JavaScript a changé). C'est exactement la stratégie que Redux emploie pour faire fonctionner les choses.

C'est pourquoi Redux a besoin que les "Reducers" soient des fonctions pures !

Merci d'avoir lu ! Si vous avez aimé l'article, n'oubliez pas de le liker ? et de le partager sur Twitter ! ??

### Certains de mes autres articles

#### Performance React :

1. [_Deux moyens rapides pour réduire la taille d'une application React en production_](https://medium.com/@rajaraodv/two-quick-ways-to-reduce-react-apps-size-in-production-82226605771a#.6lepbl7ae)
2. [_Utiliser Preact au lieu de React_](https://medium.com/@rajaraodv/using-preact-instead-of-react-70f40f53107c#.7fzp0lyo3)

#### Programmation Fonctionnelle

1. [_JavaScript est Turing Complete — Expliqué_](https://medium.com/@rajaraodv/javascript-is-turing-complete-explained-41a34287d263#.6t0b2w66p)
2. [_Programmation Fonctionnelle en JS — Avec des Exemples Pratiques (Partie 1)_](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-1-87c2b0dbc276#.fbgrmoa7g)
3. [_Programmation Fonctionnelle en JS — Avec des Exemples Pratiques (Partie 2)_](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e#.r2mglxozr)
4. [_Pourquoi Redux a besoin que les Reducers soient des "Fonctions Pures"_](https://medium.com/@rajaraodv/why-redux-needs-reducers-to-be-pure-functions-d438c58ae468#.bntrywxrf)

#### ES6

1. [_5 "Mauvais" Côtés de JavaScript qui sont Corrigés dans ES6_](https://medium.com/@rajaraodv/5-javascript-bad-parts-that-are-fixed-in-es6-c7c45d44fd81#.7e2s6cghy)
2. [_Est-ce que "Class" dans ES6 est la Nouvelle "Mauvaise" Partie ?_](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65#.4hqgpj2uv)

#### WebPack

1. [_Webpack — Les Parties Confuses_](https://medium.com/@rajaraodv/webpack-the-confusing-parts-58712f8fcad9#.6ot6deo2b)
2. [_Webpack & Hot Module Replacement [HMR]_](https://medium.com/@rajaraodv/webpack-hot-module-replacement-hmr-e756a726a07#.y667mx4lg) _(sous le capot)_
3. [_HMR de Webpack et React-Hot-Loader — Le Manuel Manquant_](https://medium.com/@rajaraodv/webpacks-hmr-react-hot-loader-the-missing-manual-232336dc0d96#.fbb1e7ehl)

#### Draft.js

1. [_Pourquoi Draft.js et Pourquoi Vous Devriez Contribuer_](https://medium.com/@rajaraodv/why-draft-js-and-why-you-should-contribute-460c4a69e6c8#.jp1tsvsqc)
2. [_Comment Draft.js Représente les Données de Texte Rich_](https://medium.com/@rajaraodv/how-draft-js-represents-rich-text-data-eeabb5f25cf2#.hh0ue85lo)

#### React et Redux :

1. [_Guide Pas à Pas pour Construire des Applications React Redux_](https://medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a#.s7zsgq3u1)
2. [_Un Guide pour Construire une Application React Redux CRUD_](https://medium.com/@rajaraodv/a-guide-for-building-a-react-redux-crud-app-7fe0b8943d0f#.g99gruhdz) _(application de 3 pages)_
3. [_Utilisation des Middlewares dans les Applications React Redux_](https://medium.com/@rajaraodv/using-middlewares-in-react-redux-apps-f7c9652610c6#.oentrjqpj)
4. [_Ajout d'une Validation de Formulaire Robuste aux Applications React Redux_](https://medium.com/@rajaraodv/adding-a-robust-form-validation-to-react-redux-apps-616ca240c124#.jq013tkr1)
5. [_Sécurisation des Applications React Redux avec des Tokens JWT_](https://medium.com/@rajaraodv/securing-react-redux-apps-with-jwt-tokens-fcfe81356ea0#.xci6o9s6w)
6. [_Gestion des E-mails Transactionnels dans les Applications React Redux_](https://medium.com/@rajaraodv/handling-transactional-emails-in-react-redux-apps-8b1134748f76#.a24nenmnt)
7. [_L'Anatomie d'une Application React Redux_](https://medium.com/@rajaraodv/the-anatomy-of-a-react-redux-app-759282368c5a#.7wwjs8eqo)
8. [_Pourquoi Redux a besoin que les Reducers soient des "Fonctions Pures"_](https://medium.com/@rajaraodv/why-redux-needs-reducers-to-be-pure-functions-d438c58ae468#.bntrywxrf)
9. [_Deux moyens rapides pour réduire la taille d'une application React en production_](https://medium.com/@rajaraodv/two-quick-ways-to-reduce-react-apps-size-in-production-82226605771a#.6lepbl7ae)

#### Salesforce

1. [_Développement d'Applications React Redux dans Visualforce de Salesforce_](https://medium.com/@rajaraodv/developing-react-redux-apps-in-salesforce-s-visualforce-3ad7be560d1c#.f6bao6mtu)