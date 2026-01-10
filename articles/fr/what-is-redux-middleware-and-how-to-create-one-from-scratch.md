---
title: Redux Middleware – Qu'est-ce que c'est et comment le construire à partir de
  zéro
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-09-09T16:38:52.000Z'
originalURL: https://freecodecamp.org/news/what-is-redux-middleware-and-how-to-create-one-from-scratch
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/redux_middleware.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
seo_title: Redux Middleware – Qu'est-ce que c'est et comment le construire à partir
  de zéro
seo_desc: "In this article, we will explore what middleware is in Redux, why it's\
  \ used, and how you can create your own middleware from scratch.\nSo let's get started.\
  \ \nWhat Is Redux Middleware?\nRedux Middleware allows you to intercept every action\
  \ sent to the r..."
---

Dans cet article, nous allons explorer ce qu'est le middleware dans Redux, pourquoi il est utilisé, et comment vous pouvez créer votre propre middleware à partir de zéro.

Alors commençons. 

## Qu'est-ce que le Middleware Redux ?

Le middleware Redux vous permet d'intercepter chaque action envoyée au reducer afin que vous puissiez apporter des modifications à l'action ou annuler l'action.  
  
Le middleware vous aide avec la journalisation, les rapports d'erreurs, la réalisation de requêtes asynchrones, et bien plus encore.

Jetez un œil au code ci-dessous :

```js
import React from "react";
import ReactDOM from "react-dom";
import { createStore } from "redux";

const reducer = (state = 0, action) => {
  switch (action.type) {
    case "INCREMENT":
      return state + action.payload;
    case "DECREMENT":
      return state - action.payload;
    default:
      return state;
  }
};

const store = createStore(reducer);

store.subscribe(() => {
  console.log("current state", store.getState());
});

store.dispatch({
  type: "INCREMENT",
  payload: 1
});

store.dispatch({
  type: "INCREMENT",
  payload: 5
});

store.dispatch({
  type: "DECREMENT",
  payload: 2
});
```

Voici une [démo Code Sandbox](https://codesandbox.io/s/focused-cori-h9iwo).

Si vous voulez comprendre comment le code ci-dessus fonctionne étape par étape, consultez mon article [Redux pour les débutants](https://www.freecodecamp.org/news/redux-for-beginners/).

Comme je l'ai expliqué dans cet article, la fonction `createStore` accepte trois arguments :

* le premier argument est une fonction généralement connue sous le nom de reducer – argument requis
* le deuxième argument est la valeur initiale de l'état – argument facultatif
* le troisième argument est un middleware – argument facultatif

## Comment créer un Middleware dans React

Pour créer un middleware, nous devons d'abord importer la fonction `applyMiddleware` de Redux comme ceci :

```js
import { applyMiddleware } from "redux";
```

Disons que nous créons un `loggerMiddleware`. Ensuite, pour définir le middleware, nous devons utiliser la syntaxe suivante :

```js
const loggerMiddleware = (store) => (next) => (action) => {
  // votre code
};
```

Le code ci-dessus est équivalent au code ci-dessous :

```js
const loggerMiddleware = function (store) {
  return function (next) {
    return function (action) {
      // votre code
    };
  };
};
```

Une fois la fonction middleware créée, nous la passons à la fonction `applyMiddleware` comme ceci :

```js
const middleware = applyMiddleware(loggerMiddleware);

```

Et enfin, nous passons le middleware à la fonction `createStore` comme ceci :

```js
const store = createStore(reducer, middleware);
```

Même si nous avons mentionné ci-dessus que le middleware est le troisième argument de la fonction `createStore`, le deuxième argument (état initial) est facultatif. Ainsi, en fonction du type d'arguments, la fonction `createStore` identifie automatiquement que l'argument passé est un middleware car il a la syntaxe spécifique de fonctions imbriquées.

Voici une [démo Code Sandbox mise à jour](https://codesandbox.io/s/recursing-heyrovsky-q8zl7?file=/src/index.js) pour le code ci-dessus.

Dans la démonstration Code Sandbox ci-dessus, le `loggerMiddleware` ressemble à ceci :

```js
const loggerMiddleware = (store) => (next) => (action) => {
  console.log("action", action);
  next(action);
};
```

Voici un [lien de prévisualisation](https://q8zl7.csb.app/) pour la démonstration Code Sandbox ci-dessus.  
  
Si vous vérifiez la console, vous verrez la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/middleware_output.png)

Avant que l'action ne soit envoyée au store, le middleware est exécuté comme nous pouvons voir l'action enregistrée dans la console. Parce que nous appelons la fonction `next` à l'intérieur du `loggerMiddleware` en passant l'action, le reducer sera également exécuté, ce qui entraîne le changement dans le store.  
  
Maintenant, que se passera-t-il si nous n'appelons pas la fonction `next` à l'intérieur du `loggerMiddleware` ?  
  
Alors l'action ne sera pas envoyée au reducer donc le store ne sera pas mis à jour.  
  
Si vous avez travaillé avec Node.js, vous pourriez trouver cela similaire au fonctionnement du middleware dans Node.js.  
  
Dans Node.js middleware également, si nous n'appelons pas la fonction _next_, la requête ne sera pas envoyée.

Voici une [démo Code Sandbox mise à jour](https://codesandbox.io/s/dry-dew-6ybfy?file=/src/index.js) avec l'appel de la fonction _next_ supprimé.

```js
const loggerMiddleware = (store) => (next) => (action) => {
  console.log("action", action);
};
```

Voici un [lien de prévisualisation](https://6ybfy.csb.app/) pour la démonstration Code Sandbox ci-dessus.  
  
Si vous vérifiez la console, vous verrez la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/middleware_removed_next.png)

Comme vous pouvez le voir, nous obtenons uniquement les actions enregistrées dans la console. Et comme l'action n'est pas transmise au reducer, elle ne sera pas exécutée – donc nous ne voyons pas le `console.log` de la fonction `store.subscribe`.  
  
Comme décrit précédemment, nous pouvons modifier l'action à partir du middleware avant qu'elle ne soit envoyée au reducer.  
  
Voici une [démo Code Sandbox mise à jour](https://codesandbox.io/s/currying-cherry-nuupf?file=/src/index.js) où nous changeons la charge utile de l'action avant qu'elle ne soit envoyée au reducer.

Le code pour le middleware ressemble à ceci :

```js
const loggerMiddleware = (store) => (next) => (action) => {
  console.log("action", action);
  action.payload = 3;
  next(action);
};
```

Voici un [lien de prévisualisation](https://nuupf.csb.app/) pour la démonstration Code Sandbox ci-dessus.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/changed_payload.png)

Selon le code, une fois l'action enregistrée dans la console, nous définissons la charge utile de l'action à une valeur de 3. Ainsi, le `type` de l'action reste le même, mais le `payload` est modifié.  
  
Nous voyons donc l'état changé à 3 initialement. Ensuite, il est à nouveau incrémenté de 3, ce qui le porte à 6. Enfin, il est décrémenté de 3, ce qui donne une valeur finale de l'état de 3.  
  
Avant que l'action ne soit envoyée au reducer, notre `loggerMiddleware` est appelé où nous modifions la valeur de la charge utile et nous la définissons toujours à 3 avant qu'elle ne soit envoyée au reducer. Ainsi, en fonction du type d'action INCREMENT ou DECREMENT, le reducer sera toujours modifié par une valeur de 3.  
  
Même si nous modifions l'action dans le code ci-dessus, il n'y a pas de problème dans ce cas car il s'agit d'un middleware et non d'un reducer.

> Les reducers doivent être une fonction pure et nous ne devons apporter aucune modification à l'état et à l'action à l'intérieur du reducer. Vous pouvez en apprendre plus à ce sujet en détail dans mon [cours Mastering Redux](https://master-redux.yogeshchavan.dev/).

Dans les exemples de code ci-dessus, nous avons créé un seul middleware. Mais vous pouvez créer plusieurs middlewares et les passer à la fonction `applyMiddleware` comme ceci :

```js
const middleware = applyMiddleware(loggerMiddleware, secondMiddleware, thirdMiddleware);

```

Tous les middlewares mentionnés dans la fonction `applyMiddleware` seront exécutés les uns après les autres.

## **Merci d'avoir lu !**

Le contenu de cet article est un petit aperçu de mon cours [Mastering Redux](https://master-redux.yogeshchavan.dev/).

Si vous voulez apprendre Redux en détail à partir de zéro et construire 3 applications ainsi que l'application complète de commande de nourriture, consultez le cours [Mastering Redux](https://master-redux.yogeshchavan.dev/).

Dans le cours, vous apprendrez :

* Redux de base et avancé
* Comment gérer l'état complexe des tableaux et des objets
* Comment utiliser plusieurs reducers pour gérer l'état complexe de Redux
* Comment déboguer une application Redux
* Comment utiliser Redux dans React en utilisant la bibliothèque react-redux pour rendre votre application réactive.
* Comment utiliser la bibliothèque redux-thunk pour gérer les appels API asynchrones
* Construire 3 applications différentes en utilisant Redux

et bien plus encore.

Enfin, nous construirons une application complète de commande de nourriture à partir de zéro avec l'intégration de Stripe pour accepter les paiements et la déployer en production.

**Vous voulez rester à jour avec du contenu régulier concernant JavaScript, React, Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).**