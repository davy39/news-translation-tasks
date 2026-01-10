---
title: Redux Thunk Expliqué avec des Exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/redux-thunk-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d13740569d1a4ca35c4.jpg
tags:
- name: Redux
  slug: redux
- name: toothbrush
  slug: toothbrush
seo_title: Redux Thunk Expliqué avec des Exemples
seo_desc: 'Redux Thunk is middleware that allows you to return functions, rather than
  just actions, within Redux. This allows for delayed actions, including working with
  promises.

  One of the main use cases for this middleware is for handling actions that might
  ...'
---

Redux Thunk est un middleware qui permet de retourner des fonctions, plutôt que simplement des actions, dans Redux. Cela permet des actions différées, y compris le travail avec des promesses.

L'un des principaux cas d'utilisation de ce middleware est la gestion des actions qui ne sont pas nécessairement synchrones, par exemple, l'utilisation d'axios pour envoyer une requête GET. Redux Thunk nous permet de dispatcher ces actions de manière asynchrone et de résoudre chaque promesse qui est retournée.

## Installation et Configuration

Redux Thunk peut être installé en exécutant `npm install redux-thunk --save` ou `yarn add redux-thunk` dans la ligne de commande.

Étant un outil Redux, vous aurez également besoin d'avoir Redux configuré. Une fois installé, il est activé en utilisant `applyMiddleware()` :

```javascript
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './reducers/index';

const store = createStore(
  rootReducer,
  applyMiddleware(thunk)
);
```

## Comment Utiliser Redux Thunk

Une fois que Redux Thunk a été installé et inclus dans votre projet avec `applyMiddleware(thunk)`, vous pouvez commencer à dispatcher des actions de manière asynchrone.

Par exemple, voici un simple compteur d'incrémentation :

```javascript
const INCREMENT_COUNTER = 'INCREMENT_COUNTER';

function increment() {
  return {
    type: INCREMENT_COUNTER
  };
}

function incrementAsync() {
  return dispatch => {
    setTimeout(() => {
      // Vous pouvez invoquer des actions synchrones ou asynchrones avec `dispatch`
      dispatch(increment());
    }, 1000);
  };
}
```

Et voici comment configurer des actions de succès et d'échec après avoir interrogé une API :

```javascript
const GET_CURRENT_USER = 'GET_CURRENT_USER';
const GET_CURRENT_USER_SUCCESS = 'GET_CURRENT_USER_SUCCESS';
const GET_CURRENT_USER_FAILURE = 'GET_CURRENT_USER_FAILURE';

const getUser = () => {
  return (dispatch) => {     // fonctions sans nom
    // Action initiale dispatchée
    dispatch({ type: GET_CURRENT_USER });
    // Retourne une promesse avec des actions de succès et d'échec
    return axios.get('/api/auth/user').then(  
      user => dispatch({ type: GET_CURRENT_USER_SUCCESS, user }),
      err => dispatch({ type: GET_CURRENT_USER_FAILURE, err })
    );
  };
};
```

## Plus d'Informations :

* [Comment implémenter le sondage de données avec React, Redux et Thunk](https://www.freecodecamp.org/news/how-to-implement-data-polling-with-react-redux-and-thunk-33cd1e47f89c/)
* [Comment Implémenter Redux en 24 Lignes de JavaScript](https://www.freecodecamp.org/news/redux-in-24-lines-of-code/)
* [Comment connecter React à Redux

a un guide diagrammatique](https://www.freecodecamp.org/news/how-to-connect-react-to-redux-a-diagrammatic-guide-d2687c14750a/)