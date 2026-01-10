---
title: Comment créer un reducer Redux par convention
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-12T23:16:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-redux-reducer-by-convention-14f7e77bfc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xGMl8gP0E8ssx_mweswYQA.jpeg
tags:
- name: coding
  slug: coding
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: Redux
  slug: redux
- name: technology
  slug: technology
seo_title: Comment créer un reducer Redux par convention
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Redux is a very popular state management library. It simplifies the original Flux
  architecture by combining all stores an...'
---

Par Cristian Salcescu

[**Découvrez Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Redux est une bibliothèque de gestion d'état très populaire. Elle simplifie l'architecture Flux originale en combinant tous les stores et le dispatcher dans un seul objet store.

Redux promeut l'utilisation de la programmation fonctionnelle pour gérer l'état. Elle introduit le concept de fonction reducer.

### Flux de données

Examinons le flux de données à l'intérieur du store Redux.

Une action est un objet simple qui contient toutes les informations nécessaires pour effectuer cette action.

Un créateur d'action est une fonction qui crée un objet action.

### Reducer

Un reducer est une fonction pure qui prend l'état et l'action comme paramètres et retourne le nouvel état.

Il peut y avoir plusieurs reducers gérant des parties de l'état racine. Nous pouvons les combiner ensemble avec la fonction utilitaire `combineReducers()` et créer le reducer racine.

Voici à quoi pourrait ressembler le reducer `todos` :

```
import matchesProperty from "lodash/matchesProperty";
function todos(todos = [], action) {
 switch (action.type) {
  case "add_todo":
    const id = getMaxId(todos) + 1;
    const newTodo = { ...action.todo, id };
    return todos.concat([newTodo]);
  case "remove_todo":
    const index = todos.findIndex(matchesProperty("id",
                                  action.todo.id));
    return [...todos.slice(0, index), ...todos.slice(index + 1)];
  case "reset_todos":
    return action.todos;
  default:
    return state;
  }
}
export default todos;
```

L'`state` dans ce cas est la liste des tâches. Nous pouvons lui appliquer des actions comme `add_todo`, `remove_todo`, `reset_todos`.

### Reducer par convention

Je voudrais me débarrasser de l'instruction `switch` dans le reducer. Les fonctions doivent être petites et faire une seule chose.

Divisons le reducer en petites fonctions pures avec des noms correspondant aux types d'actions. J'appellerai ces fonctions des setters. Chacune d'elles prend l'état et l'action comme paramètres et retourne le nouvel état.

```
function remove_todo(todos, action) {
  const index = todos.findIndex(matchesProperty("id",
                                action.todo.id));
  return [...todos.slice(0, index), ...todos.slice(index + 1)];
}

function reset_todos(todos, action) {
  return action.todos;
}

function add_todo(todos, action) {
  const id = getMaxId(todos) + 1;
  const newTodo = { ...action.todo, id};
  return todos.concat([newTodo]);
}
```

#### redux-actions

Je voudrais combiner toutes ces petites fonctions ensemble pour créer la fonction reducer originale. Nous pouvons utiliser la fonction utilitaire `handleActions()` de [redux-actions](https://redux-actions.js.org/) pour cela.

```
import { handleActions } from "redux-actions";

const reducer = handleActions(
  { remove_todo, reset_todos, add_todo },
  []
);

export default reducer;
```

Les fonctions setters s'exécuteront par convention. Lorsqu'une action avec le type `remove_todo` arrive, la fonction setter `remove_todo()` sera exécutée.

[Voici le code exemple sur codesandbox](https://codesandbox.io/s/26m5xrxry).

[**Découvrez Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez **React fonctionnel**, de manière projet, avec [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)