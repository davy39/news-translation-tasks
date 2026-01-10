---
title: Comment créer votre premier middleware Redux facilement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-13T07:27:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-your-first-redux-middleware-with-ease-a75e6b1384db
coverImage: https://cdn-media-1.freecodecamp.org/images/0*G6zSXWOpLVBgghzy.
tags:
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: Comment créer votre premier middleware Redux facilement
seo_desc: 'By Gabriele Cimato

  Almost every real-word React app makes extensive use of async requests. If you manage
  your app state with Redux, there are several ways to handle async actions.

  You may have heard of redux-thunkor redux-saga, the most popular solut...'
---

Par Gabriele Cimato

Presque toutes les applications React réelles utilisent intensivement des requêtes asynchrones. Si vous gérez l'état de votre application avec Redux, il existe plusieurs façons de gérer les actions asynchrones.

Vous avez peut-être entendu parler de `redux-thunk` ou `redux-saga`, les solutions les plus populaires pour gérer les actions asynchrones dans Redux. De telles approches sont pratiques lorsque vous devez suivre l'état d'une requête dans votre état.

Un modèle que j'ai vu assez souvent et qui utilise les `thunks` est le suivant :

```js
import {
  FETCH_DATA_ERROR,
  FETCH_DATA_PENDING,
  FETCH_DATA_SUCCESS,
} from 'constants/actionTypes';

function fetchMyDataError(error) {
  return {
    type: FETCH_DATA_ERROR,
    payload: error,
  };
}

function fetchDataPending() {
  return { type: FETCH_DATA_PENDING };
}

function fetchMyDataSuccess(response) {
  return {
    type: FETCH_DATA_SUCCESS,
    payload: response,
  };
}

function fetchData() {
  return (dispatch) => {
    dispatch(fetchDataPending());
    
    fetch('https://my-api.com/my-data')
      .then(res => res.json())
      .then(data => dispatch(fetchMyDataSuccess(data)))
      .catch(err => dispatch(fetchMyDataError(err)));
  };
}
```

Comme vous pouvez le voir, nous avons écrit une quantité importante de code. Cet exemple peut être simplifié et géré avec une seule fonction. Dans tous les cas, cela deviendra bientôt très répétitif et fastidieux, surtout si vous devez suivre le cycle de vie de chaque requête asynchrone dans votre application. Une telle verbosité n'aide pas avec le code standard nécessaire pour une application qui utilise Redux.

Lorsque qu'un modèle ou un bloc de code est utilisé encore et encore, il est bon de l'extraire dans une fonction. Cela abstraira la logique et ne nécessitera que le minimum de données pour « fonctionner ». C'est à ce moment-là que j'ai commencé à jouer avec l'idée d'écrire mon propre middleware. `[redux-slim-async](https://github.com/Gabri3l/redux-slim-async)` m'aide à sauter le code standard et à fournir un excellent contrôle avec une API minuscule. Voyons maintenant l'exemple précédent avec le nouveau middleware :

```js
import {
  FETCH_DATA_PENDING,
  FETCH_DATA_SUCCESS,
  FETCH_DATA_ERROR,
} from 'constants/actionTypes';

function fetchData() {
  return {
    types: [
      FETCH_DATA_PENDING,
      FETCH_DATA_SUCCESS,
      FETCH_DATA_ERROR,
    ],
    callAPI: fetch('https://my-api.com/my-data')
      .then(res => res.json()),
  }
}
```

Toutes ces fonctions maladroites ont disparu et notre `fetchData` est maintenant minimal — assez soigné ! 💡

Maintenant, allons de l'avant et construisons une version plus petite de ce middleware. Cela nous aidera à comprendre le fonctionnement interne et, hé, vous pourrez construire le vôtre ensuite !

### Créer un middleware

Permettez-moi de vous montrer le code de ce petit middleware tout de suite. Vous verrez que ce n'est pas aussi écrasant que vous pourriez le penser.

```js
function createSlimAsyncMiddleware({ dispatch, getState }) {
  return next => action => {
    const {
      types,
      callAPI,
      shouldCallAPI = () => true,
    } = action;
    
    if (!actionIsValid(action)) next(action);
    if (!shouldCallAPI(getState())) {
      return Promise.resolve(getState());
    }
    
    const [pendingType, successType, errorType] = types;
    
    dispatch({ type: pendingType });
    
    return callAPI()
      .then(response => {
        dispatch({
          type: successType,
          payload: response,
        });
        
        return Promise.resolve(getState());
      })
      .catch(error => {
        dispatch({
          type: errorType,
          payload: error,
        });
        
        return Promise.reject(error);
     });
  };
}
```

Attendez une seconde… c'est tout ? Absolument !

Analysons ligne par ligne. Ce middleware est une fonction qui retourne une fonction, qui retourne une fonction qui retourne une `Promise`. Aussi étrange que cela puisse paraître, vous trouverez que c'est beaucoup plus simple que cela en a l'air.

Notre fonction middleware reçoit un objet avec deux champs : `dispatch` et `getState`. Ce sont des [paramètres nommés](http://2ality.com/2011/11/keyword-parameters.html) fournis par Redux.

* `dispatch` : comme le nom le suggère, c'est ce que nous utilisons pour dispatcher une action. Cela nous donnera le pouvoir de gérer les actions à l'intérieur du middleware.
* `getState` : il s'agit d'une fonction qui retourne l'état actuel à un moment donné. Cela peut être utile si nous voulons retourner l'état mis à jour après qu'une action a été dispatchée.

À la **première ligne**, nous avons une fonction avec un argument objet avec les champs `dispatch` et `getState`.

À la **deuxième ligne**, nous retournons une fonction qui prend un argument appelé `next`. Une telle fonction retourne une fonction qui prend une `action` et fait quelque chose. Plus sur cela plus tard. Mais à quoi sert `next` ? Pourquoi devons-nous retourner une fonction qui retourne une fonction qui fait quelque chose ?

Ce que Redux fait sous le capot est de [composer](https://github.com/reactjs/redux/blob/master/src/compose.js) les middlewares de sorte que chacun ait une référence vers… le suivant ! Le nom aide beaucoup à le rendre intuitif. Nous enveloppons la fonction officielle `dispatch` de Redux avec notre middleware. Cela construit un pipeline qu'une action doit parcourir.

Rappelez-vous que vous n'avez pas OBLIGATION d'appeler `next(action)`, mais vous devez le faire si vous ne voulez pas bloquer le processus de dispatch (nous verrons un cas spécifique dans notre middleware).

![Image](https://cdn-media-1.freecodecamp.org/images/n9N9siS5VEsMDiFEBrOSMK-ko91Zl8Z4SoFM)
*Un organigramme qui explore le pipeline de middleware de manière simplifiée*

Dans notre cas, c'est utile car nous ne voulons pas intercepter chaque action, seulement celles qui sont valides pour notre middleware. Pour simplifier, j'ai ajouté une vérification appelée `actionIsValid`. Cette fonction prend une `action` comme argument et retourne un booléen. Le booléen retourné représente la validité de cette action pour notre middleware.

`actionIsValid` est un bon endroit pour vérifier les erreurs et les `throw` si nécessaire. Si elle n'est pas valide, alors j'utiliserai notre référence au middleware `next` et je passerai l'action à celui-ci. Sinon, nous pouvons enfin utiliser l'action et « faire quelque chose » (l'organigramme ci-dessus représente une version simplifiée de cette logique).

Le reste du middleware est assez intuitif. Nous vérifions la validité de l'action pour déterminer si notre requête asynchrone doit se poursuivre ou non.

`shouldCallAPI` est un paramètre de notre API middleware. Étant donné l'état, il retourne un booléen qui détermine si notre requête doit être exécutée ou non. Le middleware fournit une valeur par défaut pour celui-ci (une fonction qui retourne `true`). Si nous n'avons pas besoin de faire l'appel API, alors nous retournons `Promise.resolve`. De cette façon, nous pouvons utiliser `.then` ou `async/await` sur toute action asynchrone qui passe par notre middleware.

```js
const [pendingType, successType, errorType] = types;
```

L'étape suivante consiste à déterminer le champ `type` de l'action passé en paramètre. Nous utilisons la [destructuration de tableau](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#Array_destructuring) pour désassembler notre paramètre de tableau `types`.

```js
dispatch({ type: pendingType });
```

Maintenant, nous pouvons enfin utiliser la méthode `dispatch`. Cela dispatch une action Redux comme vous le feriez normalement. Une telle action représente l'état « en attente » de notre requête asynchrone.

```js
return callAPI()
  .then(response => {
    dispatch({
      type: successType,
      payload: response,
    });
    
    return Promise.resolve(getState());
  })
  .catch(error => {
    dispatch({
      type: errorType,
      payload: error,
    });
    
    return Promise.reject(error);
  });
```

Nous avons enfin notre dernière instruction `return`. Ici, nous faisons l'appel API et, en fonction de la résolution de la `Promise`, nous dispatchons et retournons différentes valeurs.

* **Succès** : étant donné la réponse de l'API, nous dispatchons une action de succès. La charge utile est la réponse de la requête. Juste après cela, nous retournons une `Promise` qui se résout avec l'état à jour de notre application. Cela nous permet d'utiliser `.then(updatedState => ...do something)`
* **Erreur** : si la `Promise` est rejetée, alors nous dispatchons une action d'erreur. Dans ce cas, la charge utile est l'erreur elle-même.

C'est tout ! Comme montré précédemment, nous pouvons ensuite créer des actions et les utiliser comme suit :

```js
// Notre Action

function fetchData() {
  return {
    types: [
      FETCH_DATA_PENDING,
      FETCH_DATA_SUCCESS,
      FETCH_DATA_ERROR,
    ],
    shouldCallAPI: state => state.dataArr.length === 0,
    callAPI: () =>
      fetch('https://my-api.com/my-data').then(res => res.json()),
  }
}

// À l'intérieur du composant

class MyComponent extends Component {
  componentDidMount() {
    this.props.fetchData()
      .then(state => {
        console.log('updated state after async action:', state);
      })
      .catch(err => {
        console.log('an error occured');
      });
  }
  
// Reste du composant omis...

}
```

Dans ce cas simple, nous récupérons les données uniquement si notre tableau de données est vide. Ensuite, nous enregistrons l'état mis à jour après la requête ou un message d'erreur si la `Promise` est rejetée.

### Conclusion

Créer des middlewares Redux est intuitif. Vous avez accès au dispatcher du store et à la fonction `getState`. Utilisez-les pour accéder au dernier état de votre application ou pour dispatcher des actions.

Vous devez également vous rappeler d'utiliser `next` lorsque cela est nécessaire et de veiller à ne pas bloquer le pipeline de dispatch. Dans notre cas, si nous n'avions pas appelé `next(action)`, toute action qui n'était pas valide pour notre middleware serait essentiellement rejetée ⚠️!!

Certains détails d'implémentation ont été omis ici pour simplifier. Si vous souhaitez approfondir un peu, n'hésitez pas à explorer le middleware `redux-slim-async` [ici](https://github.com/Gabri3l/redux-slim-async).

Donnez-lui un ⭐ si vous l'aimez ! J'ai construit ce middleware et je l'utilise actuellement en production pour éviter beaucoup de code standard. N'hésitez pas à l'essayer et à fournir des commentaires à tout moment. Voici une autre ressource précieuse pour explorer davantage les middlewares, la [documentation de redux](https://redux.js.org/advanced/middleware) !

Vous pouvez également me suivre sur Twitter [@SuperGabry](https://twitter.com/SuperG4bry)