---
title: Un guide rapide de Redux pour débutants
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-02-02T11:23:43.000Z'
originalURL: https://freecodecamp.org/news/a-quick-guide-to-redux-for-beginners-971d18c0509b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-E5k6l1Bbi5U9BHSLAk4dg.jpeg
tags:
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Un guide rapide de Redux pour débutants
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  Redux is a state manager that’s usually used along with React. It’s not tied to
  that library, and can be used with other technologies as well. But we’ll stick to
  React for the sake of...'
---

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)

Redux est un gestionnaire d'état qui est généralement utilisé avec React. Il n'est pas lié à cette bibliothèque et peut être utilisé avec d'autres technologies également. Mais nous allons nous en tenir à React pour les besoins de cet article.

React a sa propre façon de gérer l'état, et vous pouvez lire mon introduction à la gestion de l'état dans React dans mon [Guide du débutant React](https://flaviocopes.com/react-beginners-guide/).

Ce que je n'ai pas mentionné dans cet article, c'est que l'approche dont j'ai discuté **ne s'adapte pas**.

Déplacer l'état vers le haut dans l'arborescence fonctionne dans des cas simples, mais dans une application complexe, vous pourriez vous retrouver à déplacer presque tout l'état vers le haut et vers le bas en utilisant des props. Une meilleure approche serait d'utiliser un **magasin global externe**.

Redux est un moyen de gérer l'état d'une application.

Il y a quelques concepts à saisir, mais une fois que vous les avez compris, Redux est une approche très simple du problème.

Juste pour le noter à nouveau : Redux est très populaire avec les applications React, mais il n'est en aucun cas unique à React. Il existe des liaisons pour presque tous les frameworks populaires. Cela dit, je vais partager quelques exemples en utilisant React puisque c'est si courant.

### Quand devriez-vous utiliser Redux ?

Redux est idéal pour les applications moyennes à grandes. Vous ne devriez l'utiliser que lorsque vous avez des difficultés à gérer l'état avec la gestion d'état par défaut de React (ou toute autre bibliothèque que vous utilisez).

Les applications simples n'en ont pas besoin du tout (et il n'y a rien de mal avec les applications simples).

### Arbre d'état immuable

Dans Redux, l'état entier de l'application est représenté par **un** objet JavaScript, appelé **state** ou **state tree**.

Nous l'appelons **immutable state tree** parce qu'il est en lecture seule : il ne peut pas être changé directement.

Il ne peut être changé qu'en dispatchant une **Action**.

### Actions

Une **Action** est **un objet JavaScript qui décrit un changement de manière minimaliste** (juste avec les informations nécessaires) :

```
{   type: 'CLICKED_SIDEBAR' } 
```

```
// par exemple, avec plus de données {   type: 'SELECTED_USER',   userId: 232 }
```

La seule exigence d'un objet action est d'avoir une propriété `type`, dont la valeur est généralement une chaîne de caractères.

### Les types d'actions doivent être des constantes

Dans une application simple, un type d'action peut être défini comme une chaîne de caractères (comme je l'ai fait dans l'exemple de l'article précédent).

Lorsque l'application grandit, il est préférable d'utiliser des constantes :

```
const ADD_ITEM = 'ADD_ITEM' const action = { type: ADD_ITEM, title: 'Troisième élément' }
```

et de séparer les actions dans leurs propres fichiers, et de les importer :

```
import { ADD_ITEM, REMOVE_ITEM } from './actions'
```

### Créateurs d'actions

Les **Action Creators** sont des fonctions qui créent des actions.

```
function addItem(t) {   return {     type: ADD_ITEM,     title: t   } }
```

Vous exécutez généralement des créateurs d'actions en combinaison avec le déclenchement du dispatcher :

```
dispatch(addItem('Lait'))
```

ou en définissant une fonction de dispatch d'action :

```
const dispatchAddItem = i => dispatch(addItem(i)) dispatchAddItem('Lait')
```

### Réducteurs

Lorsque qu'une action est déclenchée, quelque chose doit se passer et l'état de l'application doit changer.

C'est le travail des **reducers**.

### Qu'est-ce qu'un reducer

Un **reducer** est une **fonction pure** qui calcule le prochain arbre d'état basé sur l'arbre d'état précédent et l'action dispatchée.

```
(currentState, action) => newState
```

Une fonction pure prend une entrée et retourne une sortie sans changer l'entrée ou autre chose. Ainsi, un reducer retourne un objet d'arbre d'état complètement nouveau qui remplace le précédent.

### Ce qu'un reducer ne devrait pas faire

Un reducer devrait être une fonction pure, donc il ne devrait **pas** :

* muter ses arguments
* muter l'état — il devrait plutôt en créer un nouveau avec `Object.assign({}, ...)`
* générer des effets secondaires (aucun appel d'API changeant quoi que ce soit)
* appeler des fonctions non pures, qui sont des fonctions qui changent leur sortie en fonction de facteurs autres que leur entrée (par exemple, `Date.now()` ou `Math.random()`)

Il n'y a pas de renforcement, mais vous devriez respecter les règles.

### Plusieurs reducers

Puisque l'état d'une application complexe pourrait être vraiment large, il n'y a pas un seul reducer, mais de nombreux reducers pour chaque type d'action.

### Une simulation d'un reducer

À sa base, Redux peut être simplifié avec ce modèle :

#### L'état

```
{   list: [     { title: "Premier élément" },     { title: "Deuxième élément" },   ],   title: 'Liste de courses' }
```

#### Une liste d'actions

```
{ type: 'ADD_ITEM', title: 'Troisième élément' } { type: 'REMOVE_ITEM', index: 1 } { type: 'CHANGE_LIST_TITLE', title: 'Liste de voyage' }
```

#### Un reducer pour chaque partie de l'état

```
const title = (state = '', action) => {  if (action.type === 'CHANGE_LIST_TITLE') {     return action.title   } else {     return state   } } 
```

```
const list = (state = [], action) => {   switch (action.type) {     case 'ADD_ITEM':       return state.concat([{ title: action.title }])     case 'REMOVE_ITEM':       return state.map((item, index) =>         action.index === index           ? { title: item.title }           : item     default:       return state   } }
```

#### Un reducer pour tout l'état

```
const listManager = (state = {}, action) => {   return {     title: title(state.title, action),     list: list(state.list, action),   } }
```

### Le Store

Le **Store** est un objet qui :

* **contient l'état** de l'application
* **expose l'état** via `getState()`
* vous permet de **mettre à jour l'état** via `dispatch()`
* vous permet de (dés)enregistrer en tant qu'**écouteur de changement d'état** en utilisant `subscribe()`

Un store est **unique** dans l'application.

Voici comment un store pour l'application listManager est créé :

```
import { createStore } from 'redux' import listManager from './reducers' let store = createStore(listManager)
```

### Puis-je initialiser le store avec des données côté serveur ?

Bien sûr, **il suffit de passer un état initial** :

```
let store = createStore(listManager, preexistingState)
```

### Obtenir l'état

```
store.getState()
```

### Mettre à jour l'état

```
store.dispatch(addItem('Quelque chose'))
```

### Écouter les changements d'état

```
const unsubscribe = store.subscribe(() =>   const newState = store.getState() ) 
```

```
unsubscribe()
```

### Flux de données

Le flux de données dans Redux est toujours **unidirectionnel**.

Vous appelez `dispatch()` sur le Store, en passant une Action.

Le Store se charge de passer l'Action au Reducer, générant le prochain State.

Le Store met à jour le State et alerte tous les Listeners.

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)