---
title: Comment implémenter Redux en 24 lignes de JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-21T12:59:00.000Z'
originalURL: https://freecodecamp.org/news/redux-in-24-lines-of-code
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/cover-image-2.png
tags:
- name: Flux
  slug: flux
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Redux
  slug: redux
seo_title: Comment implémenter Redux en 24 lignes de JavaScript
seo_desc: 'By Yazeed Bzadough

  90% convention, 10% library.

  Redux is among the most important JavaScript libraries ever created. Inspired by
  prior art like Flux and Elm, Redux put JavaScript functional programming on the
  map by introducing a scalable architectur...'
---

Par Yazeed Bzadough

90% de convention, 10% de bibliothèque.

Redux est l'une des bibliothèques JavaScript les plus importantes jamais créées. Inspiré par des travaux antérieurs comme [Flux](https://facebook.github.io/flux/) et [Elm](https://elm-lang.org), Redux a mis la programmation fonctionnelle JavaScript sur le devant de la scène en introduisant une architecture évolutive basée sur trois points simples.

Si vous êtes nouveau dans Redux, envisagez de lire [la documentation officielle](https://redux.js.org/introduction/three-principles) en premier.

## Redux est principalement une convention
Considérez cette simple application de compteur qui utilise l'architecture Redux. Si vous souhaitez avancer, consultez [le dépôt Github](https://github.com/yazeedb/implement-redux-counter-app) pour cela.

![redux-counter-app-demo](https://www.freecodecamp.org/news/content/images/2019/10/redux-counter-app-demo.gif)

### L'état vit dans un seul arbre
L'état de l'application ressemble à ceci.

```js
const initialState = { count: 0 };
```

### Les actions déclarent les changements d'état
Par convention Redux, **je ne** modifie pas (mutate) directement l'état.

```js
// NE FAITES PAS cela dans une application Redux
state.count = 1;
```

Au lieu de cela, je crée toutes les actions que l'utilisateur peut utiliser dans l'application.

```js
const actions = {
  increment: { type: 'INCREMENT' },
  decrement: { type: 'DECREMENT' }
};
```

### Le réducteur interprète l'action et met à jour l'état
La dernière pièce architecturale nécessite un réducteur, une fonction pure qui retourne une nouvelle copie de votre état basée sur l'état précédent et l'action.

* Si `increment` est déclenché, incrémentez `state.count`.
* Si `decrement` est déclenché, décrémentez `state.count`.

```js
const countReducer = (state = initialState, action) => {
  switch (action.type) {
    case actions.increment.type:
      return {
        count: state.count + 1
      };

    case actions.decrement.type:
      return {
        count: state.count - 1
      };

    default:
      return state;
  }
};
```

### Aucun Redux jusqu'à présent
Avez-vous remarqué que nous n'avons pas encore touché à la bibliothèque Redux ? Nous venons de créer quelques objets et une fonction. C'est ce que je veux dire par "principalement une convention", 90% de Redux n'a pas besoin de Redux !

## Implémentons Redux
Pour utiliser cette architecture, nous devons la connecter à un store. Nous allons implémenter une seule fonction—`createStore`.

Elle est utilisée comme ceci.

```js
import { createStore } from 'redux'

const store = createStore(countReducer);

store.subscribe(() => {
  console.log(store.getState());
});

store.dispatch(actions.increment);
// logs { count: 1 }

store.dispatch(actions.increment);
// logs { count: 2 }

store.dispatch(actions.decrement);
// logs { count: 1 }
```

Et voici notre modèle initial. Nous aurons besoin d'une liste d'écouteurs et de l'état initial fourni par le réducteur.

```js
const createStore = (yourReducer) => {
    let listeners = [];
    let currentState = yourReducer(undefined, {});
}
```

Chaque fois que quelqu'un s'abonne à notre store, il est ajouté au tableau `listeners`. Cela est important car chaque fois que quelqu'un envoie une action, tous les `listeners` doivent être notifiés dans une boucle.

Appeler `yourReducer` avec `undefined` et un objet vide retourne l'`initialState` que nous avons installé ci-dessus. Cela nous donne une valeur appropriée à retourner lorsque nous appelons `store.getState()`. À ce propos, créons cette méthode.

### store.getState()
Il s'agit d'une fonction qui retourne le dernier état du store. Nous en aurons besoin pour mettre à jour notre UI chaque fois que l'utilisateur clique sur un bouton.

```js
const createStore = (yourReducer) => {
    let listeners = [];
    let currentState = yourReducer(undefined, {});
    
    return {
        getState: () => currentState
    };
}
```

### store.dispatch(action)
Il s'agit d'une fonction qui prend une `action` comme paramètre. Elle alimente cette `action` et le `currentState` à `yourReducer` pour obtenir un _nouvel_ état. Ensuite, `dispatch` notifie tout le monde abonné au `store`.

```js
const createStore = (yourReducer) => {
  let listeners = [];
  let currentState = yourReducer(undefined, {});

  return {
    getState: () => currentState,
    dispatch: (action) => {
      currentState = yourReducer(currentState, action);

      listeners.forEach((listener) => {
        listener();
      });
    }
  };
};
```

### store.subscribe(listener)
Il s'agit d'une fonction qui vous permet d'être notifié lorsque le store reçoit une action. Il est bon d'utiliser `store.getState()` ici pour obtenir votre dernier état et mettre à jour votre UI.

```js
const createStore = (yourReducer) => {
  let listeners = [];
  let currentState = yourReducer(undefined, {});

  return {
    getState: () => currentState,
    dispatch: (action) => {
      currentState = yourReducer(currentState, action);

      listeners.forEach((listener) => {
        listener();
      });
    },
    subscribe: (newListener) => {
      listeners.push(newListener);

      const unsubscribe = () => {
        listeners = listeners.filter((l) => l !== newListener);
      };

      return unsubscribe;
    }
  };
};
```

`subscribe` retourne une fonction appelée `unsubscribe` que vous pouvez appeler lorsque vous n'êtes plus intéressé à écouter les mises à jour du store.

## Tout ensemble maintenant
Connectons cela à nos boutons et voyons le code source final.

```js
// fonction createStore simplifiée
const createStore = (yourReducer) => {
  let listeners = [];
  let currentState = yourReducer(undefined, {});

  return {
    getState: () => currentState,
    dispatch: (action) => {
      currentState = yourReducer(currentState, action);

      listeners.forEach((listener) => {
        listener();
      });
    },
    subscribe: (newListener) => {
      listeners.push(newListener);

      const unsubscribe = () => {
        listeners = listeners.filter((l) => l !== newListener);
      };

      return unsubscribe;
    }
  };
};

// Pièces d'architecture Redux
const initialState = { count: 0 };

const actions = {
  increment: { type: 'INCREMENT' },
  decrement: { type: 'DECREMENT' }
};

const countReducer = (state = initialState, action) => {
  switch (action.type) {
    case actions.increment.type:
      return {
        count: state.count + 1
      };

    case actions.decrement.type:
      return {
        count: state.count - 1
      };

    default:
      return state;
  }
};

const store = createStore(countReducer);

// Éléments DOM
const incrementButton = document.querySelector('.increment');
const decrementButton = document.querySelector('.decrement');

// Relier les événements de clic aux actions
incrementButton.addEventListener('click', () => {
  store.dispatch(actions.increment);
});

decrementButton.addEventListener('click', () => {
  store.dispatch(actions.decrement);
});

// Initialiser l'affichage de l'UI
const counterDisplay = document.querySelector('h1');
counterDisplay.innerHTML = parseInt(initialState.count);

// Mettre à jour l'UI lorsqu'une action est déclenchée
store.subscribe(() => {
  const state = store.getState();

  counterDisplay.innerHTML = parseInt(state.count);
});
```

Et voici une fois de plus notre UI finale.

![redux-counter-app-demo](https://www.freecodecamp.org/news/content/images/2019/10/redux-counter-app-demo.gif)

Si vous êtes intéressé par le HTML/CSS que j'ai utilisé, voici [le dépôt GitHub](https://github.com/yazeedb/implement-redux-counter-app) à nouveau !

## Vous voulez un coaching gratuit ?
Si vous souhaitez planifier un appel gratuit pour discuter des questions de développement Front-End concernant le code, les entretiens, la carrière ou autre chose [suivez-moi sur Twitter et envoyez-moi un DM](https://twitter.com/yazeedBee).

Après cela, si vous appréciez notre première rencontre, nous pouvons discuter d'un coaching continu pour vous aider à atteindre vos objectifs de développement Front-End !

## Portez vos contributions
Si vous codez tous les jours, surtout si vous vous engagez sur GitHub, ne serait-il pas cool de porter cette carte de contribution pour que tout le monde la voie ?

[Gitmerch.com](https://gitmerch.com/) vous permet d'imprimer un t-shirt de votre carte de contribution GitHub ! Utilisez le code, **Yazeed**, lors du paiement pour obtenir une réduction.

![git-merch-screenshot-1-1](https://www.freecodecamp.org/news/content/images/2019/11/git-merch-screenshot-1-1.png)

![git-merch-screenshot-2-1](https://www.freecodecamp.org/news/content/images/2019/11/git-merch-screenshot-2-1.png)

## Merci d'avoir lu
Pour plus de contenu comme celui-ci, consultez <a href="https://yazeedb.com">https://yazeedb.com !</a>

À la prochaine fois !