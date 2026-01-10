---
title: Comment charger des données dans React avec redux-thunk, redux-saga, suspense
  & hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-31T16:49:30.000Z'
originalURL: https://freecodecamp.org/news/loading-data-in-react-redux-thunk-redux-saga-suspense-hooks-666b21da1569
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JL-AhMbl0HlP4Jr3YyaxbA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: Comment charger des données dans React avec redux-thunk, redux-saga, suspense
  & hooks
seo_desc: 'By Valerii Tereshchenko

  Introduction

  React is a JavaScript library for building user interfaces. Very often using React
  means using React with Redux. Redux is another JavaScript library for managing global
  state. Sadly, even with these two libraries ...'
---

Par Valerii Tereshchenko

### Introduction

[React](https://reactjs.org/) est une bibliothèque JavaScript pour construire des interfaces utilisateur. Très souvent, utiliser React signifie utiliser React avec [Redux](https://redux.js.org/). [Redux](https://redux.js.org/) est une autre bibliothèque JavaScript pour gérer l'état global. Malheureusement, même avec ces deux bibliothèques, il n'existe pas de méthode claire pour gérer les appels asynchrones à l'API (backend) ou tout autre effet de bord.

Dans cet article, j'essaie de comparer différentes approches pour résoudre ce problème. Définissons d'abord le problème.

**_Le composant X est l'un des nombreux composants du site web (ou mobile, ou application de bureau, c'est aussi possible). X interroge et affiche certaines données chargées depuis l'API. X peut être une page ou juste une partie de la page. L'important est que X soit un composant séparé qui doit être faiblement couplé avec le reste du système (autant que possible). X doit afficher un indicateur de chargement pendant la récupération des données et une erreur si l'appel échoue._**

Cet article suppose que vous avez déjà une certaine expérience dans la création d'applications React/Redux.

Cet article va montrer 4 façons de résoudre ce problème et **comparer les avantages et les inconvénients** de chacune. **Ce n'est pas un manuel détaillé sur la façon d'utiliser thunk, saga, suspense ou hooks**.

Le code de ces exemples est disponible sur [GitHub](https://github.com/ValeraT1982/react-data-load).

### Installation initiale

#### Serveur Mock

À des fins de test, nous allons utiliser [json-server](https://github.com/typicode/json-server). C'est un projet incroyable qui permet de construire des API REST fictives très rapidement. Pour notre exemple, cela ressemble à ceci.

```js
const jsonServer = require('json-server');
const server = jsonServer.create();
const router = jsonServer.router('db.json');
const middleware = jsonServer.defaults();

server.use((req, res, next) => {
   setTimeout(() => next(), 2000);
});
server.use(middleware);
server.use(router);
server.listen(4000, () => {
   console.log(`JSON Server is running...`);
});
```

Notre fichier db.json contient des données de test au format json.

```json
{
 "users": [
   {
     "id": 1,
     "firstName": "John",
     "lastName": "Doe",
     "active": true,
     "posts": 10,
     "messages": 50
   },
   ...
   {
     "id": 8,
     "firstName": "Clay",
     "lastName": "Chung",
     "active": true,
     "posts": 8,
     "messages": 5
   }
 ]
}
```

Après avoir démarré le serveur, un appel à [_http://localhost:4000/users_](http://localhost:4000/users) retourne la liste des utilisateurs avec une imitation de délai — environ 2s.

### Projet et appel API

Maintenant, nous sommes prêts à commencer à coder. Je suppose que vous avez déjà un projet React créé en utilisant [create-react-app](https://github.com/facebook/create-react-app) avec Redux configuré et prêt à l'emploi.

Si vous avez des difficultés avec cela, vous pouvez consulter [ceci](https://facebook.github.io/create-react-app/) et [ceci](https://medium.com/backticks-tildes/setting-up-a-redux-project-with-create-react-app-e363ab2329b8).

L'étape suivante consiste à créer une fonction pour appeler l'API (_api.js_) :

```json
const API_BASE_ADDRESS = 'http://localhost:4000';

export default class Api {
   static getUsers() {
       const uri = API_BASE_ADDRESS + "/users";
       
       return fetch(uri, {
           method: 'GET'
       });
   }
}
```

### Redux-thunk

[Redux-thunk](https://github.com/reduxjs/redux-thunk) est un middleware recommandé pour la logique de base des effets secondaires de Redux, telle que la logique asynchrone simple (comme une requête à l'API). Redux-thunk lui-même ne fait pas grand-chose. Ce n'est que [14!!! lignes](https://github.com/reduxjs/redux-thunk/blob/master/src/index.js) [de](https://github.com/reduxjs/redux-thunk/blob/master/src/index.js) [code](https://github.com/reduxjs/redux-thunk/blob/master/src/index.js). Il ajoute simplement un peu de "sucre syntaxique" et rien de plus.

Le diagramme ci-dessous aide à comprendre ce que nous allons faire.

![Image](https://cdn-media-1.freecodecamp.org/images/AWinRkydsUiojdtNEqS9O7NO6xtGirYJR50Z)

À chaque fois qu'une action est effectuée, le réducteur change l'état en conséquence. Le composant mappe l'état aux propriétés et utilise ces propriétés dans la méthode **_render()_** pour déterminer ce que l'utilisateur doit voir : un indicateur de chargement, des données ou un message d'erreur.

Pour que cela fonctionne, nous devons faire 5 choses.

#### 1. Installer thunk

```
npm install redux-thunk
```

#### 2. Ajouter le middleware thunk lors de la configuration du store (configureStore.js)

```js
import { applyMiddleware, compose, createStore } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './appReducers';

export function configureStore(initialState) {
 const middleware = [thunk];
 
 const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
 const store = createStore(rootReducer, initialState, composeEnhancers(applyMiddleware(...middleware)));
 
 return store;
}
```

Aux lignes 12–13, nous configurons également [redux](https://github.com/zalmoxisus/redux-devtools-extension) [devtools](https://github.com/zalmoxisus/redux-devtools-extension). Un peu plus tard, cela aidera à montrer l'un des problèmes avec cette solution.

#### 3. Créer des actions (redux-thunk/actions.js)

```js
import Api from "../api"

export const LOAD_USERS_LOADING = 'REDUX_THUNK_LOAD_USERS_LOADING';
export const LOAD_USERS_SUCCESS = 'REDUX_THUNK_LOAD_USERS_SUCCESS';
export const LOAD_USERS_ERROR = 'REDUX_THUNK_LOAD_USERS_ERROR';

export const loadUsers = () => dispatch => {
   dispatch({ type: LOAD_USERS_LOADING });
   Api.getUsers()
       .then(response => response.json())
       .then(
           data => dispatch({ type: LOAD_USERS_SUCCESS, data }),
           error => dispatch({ type: LOAD_USERS_ERROR, error: error.message || 'Unexpected Error!!!' })
       )
};
```

Il est également recommandé d'avoir vos créateurs d'actions séparés (cela ajoute un peu de codage supplémentaire), mais pour ce cas simple, je pense qu'il est acceptable de créer des actions "à la volée".

#### 4. Créer un réducteur (redux-thunk/reducer.js)

```js
import {LOAD_USERS_ERROR, LOAD_USERS_LOADING, LOAD_USERS_SUCCESS} from "./actions";

const initialState = {
   data: [],
   loading: false,
   error: ''
};

export default function reduxThunkReducer(state = initialState, action) {
   switch (action.type) {
       case LOAD_USERS_LOADING: {
           return {
               ...state,
               loading: true,
               error:''
           };
       }
       case LOAD_USERS_SUCCESS: {
           return {
               ...state,
               data: action.data,
               loading: false
           }
       }
       case LOAD_USERS_ERROR: {
           return {
               ...state,
               loading: false,
               error: action.error
           };
       }
       default: {
           return state;
       }
   }
}
```

#### 5. Créer un composant connecté à redux (redux-thunk/UsersWithReduxThunk.js)

```js
import * as React from 'react';
import { connect } from 'react-redux';
import {loadUsers} from "./actions";

class UsersWithReduxThunk extends React.Component {
   componentDidMount() {
       this.props.loadUsers();
   };
    
   render() {
       if (this.props.loading) {
           return <div>Loading</div>
       }
       
       if (this.props.error) {
           return <div style={{ color: 'red' }}>ERROR: {this.props.error}</div>
       }
    
       return (
           <table>
               <thead>
                   <tr>
                       <th>First Name</th>
                       <th>Last Name</th>
                       <th>Active?</th>
                       <th>Posts</th>
                       <th>Messages</th>
                   </tr>
               </thead>
               <tbody>
               {this.props.data.map(u =>
                   <tr key={u.id}>
                       <td>{u.firstName}</td>
                       <td>{u.lastName}</td>
                       <td>{u.active ? 'Yes' : 'No'}</td>
                       <td>{u.posts}</td>
                       <td>{u.messages}</td>
                   </tr>
               )}
               </tbody>
           </table>
       );
   }
}

const mapStateToProps = state => ({
   data: state.reduxThunk.data,
   loading: state.reduxThunk.loading,
   error: state.reduxThunk.error,
});

const mapDispatchToProps = {
   loadUsers
};

export default connect(
   mapStateToProps,
   mapDispatchToProps
)(UsersWithReduxThunk);
```

J'ai essayé de rendre le composant aussi simple que possible. Je comprends que cela semble horrible :)

Indicateur de chargement

![Image](https://cdn-media-1.freecodecamp.org/images/8QkfJzj7pl5LgP2-BgjeVPXDdf7jFmPxCXIp)

Données

![Image](https://cdn-media-1.freecodecamp.org/images/TxQRy0VYOb-Z1EwwwwdIfVHa8xYSd7443FuG)

Erreur

![Image](https://cdn-media-1.freecodecamp.org/images/u2AmrUXMxuxeEHJ0RRtm0Et9YpkQDbSJhZx3)

**Voilà : 3 fichiers, 109 lignes de code (13(actions) + 36(réducteur) + 60(composant)).**

#### Avantages :

* Approche "recommandée" pour les applications react/redux.
* Aucune dépendance supplémentaire. Presque, thunk est minuscule :)
* Pas besoin d'apprendre de nouvelles choses.

#### Inconvénients :

* Beaucoup de code dans différents endroits
* Après la navigation vers une autre page, les anciennes données sont toujours dans l'état global (voir l'image ci-dessous). Ces données sont obsolètes et constituent des informations inutiles qui consomment de la mémoire.
* Dans le cas de scénarios complexes (appels conditionnels multiples dans une seule action, etc.), le code n'est pas très lisible

![Image](https://cdn-media-1.freecodecamp.org/images/TfXqLWBchdCUCvNjDXbfWihuWZNV2BVQaH3r)

### Redux-saga

[Redux-saga](https://github.com/redux-saga/redux-saga) est une bibliothèque de middleware redux conçue pour faciliter la gestion des effets secondaires et la rendre lisible. Elle utilise les générateurs ES6 qui nous permettent d'écrire du code asynchrone qui semble synchrone. De plus, cette solution est facile à tester.

D'un point de vue général, cette solution fonctionne de la même manière que thunk. Le diagramme de l'exemple thunk est toujours applicable.

Pour que cela fonctionne, nous devons faire 6 choses.

#### 1. Installer saga

```
npm install redux-saga
```

#### 2. Ajouter le middleware saga et ajouter toutes les sagas (configureStore.js)

```js
import { applyMiddleware, compose, createStore } from 'redux';
import createSagaMiddleware from 'redux-saga';
import rootReducer from './appReducers';
import usersSaga from "../redux-saga/sagas";

const sagaMiddleware = createSagaMiddleware();

export function configureStore(initialState) {
 const middleware = [sagaMiddleware];
    
 const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
 const store = createStore(rootReducer, initialState, composeEnhancers(applyMiddleware(...middleware)));
    
 sagaMiddleware.run(usersSaga);
    
 return store;
}
```

Les sagas de la ligne 4 seront ajoutées à l'étape 4.

#### 3. Créer une action (redux-saga/actions.js)

```js
export const LOAD_USERS_LOADING = 'REDUX_SAGA_LOAD_USERS_LOADING';
export const LOAD_USERS_SUCCESS = 'REDUX_SAGA_LOAD_USERS_SUCCESS';
export const LOAD_USERS_ERROR = 'REDUX_SAGA_LOAD_USERS_ERROR';

export const loadUsers = () => dispatch => {
   dispatch({ type: LOAD_USERS_LOADING });
};
```

#### 4. Créer des sagas (redux-saga/sagas.js)

```js
import { put, takeEvery, takeLatest } from 'redux-saga/effects'
import {loadUsersSuccess, LOAD_USERS_ERROR, LOAD_USERS_LOADING, LOAD_USERS_SUCCESS} from "./actions";
import Api from '../api'

async function fetchAsync(func) {
   const response = await func();
    
   if (response.ok) {
       return await response.json();
   }
    
   throw new Error("Unexpected error!!!");
}

function* fetchUser() {
   try {
       const users = yield fetchAsync(Api.getUsers);
       
       yield put({type: LOAD_USERS_SUCCESS, data: users});
   } catch (e) {
       yield put({type: LOAD_USERS_ERROR, error: e.message});
   }
}

export function* usersSaga() {
   // Permet des récupérations concurrentes d'utilisateurs
   yield takeEvery(LOAD_USERS_LOADING, fetchUser);
    
   // Ne permet pas de récupérations concurrentes d'utilisateurs
   // yield takeLatest(LOAD_USERS_LOADING, fetchUser);
}

export default usersSaga;
```

Saga a une courbe d'apprentissage assez raide, donc si vous ne l'avez jamais utilisée et n'avez jamais lu quoi que ce soit sur ce framework, cela pourrait être difficile à comprendre. Brièvement, dans la fonction **_userSaga_**, nous configurons saga pour écouter l'action **LOAD_USERS_LOADING** et déclencher la fonction **_fetchUsers_**. La fonction **_fetchUsers_** appelle l'API. Si l'appel réussit, alors l'action **LOAD_USER_SUCCESS** est dispatchée, sinon l'action **LOAD_USER_ERROR** est dispatchée.

#### 5. Créer un réducteur (redux-saga/reducer.js)

```js
import {LOAD_USERS_ERROR, LOAD_USERS_LOADING, LOAD_USERS_SUCCESS} from "./actions";

const initialState = {
   data: [],
   loading: false,
   error: ''
};

export default function reduxSagaReducer(state = initialState, action) {
   switch (action.type) {
       case LOAD_USERS_LOADING: {
           return {
               ...state,
               loading: true,
               error:''
           };
       }
       case LOAD_USERS_SUCCESS: {
           return {
               ...state,
               data: action.data,
               loading: false
           }
       }
       case LOAD_USERS_ERROR: {
           return {
               ...state,
               loading: false,
               error: action.error
           };
       }
       default: {
           return state;
       }
   }
}
```

Le réducteur ici est absolument le même que dans l'exemple thunk.

### 6. Créer un composant connecté à redux (redux-saga/UsersWithReduxSaga.js)

```js
import * as React from 'react';
import {connect} from 'react-redux';
import {loadUsers} from "./actions";

class UsersWithReduxSaga extends React.Component {
   componentDidMount() {
       this.props.loadUsers();
   };
    
   render() {
       if (this.props.loading) {
           return <div>Loading</div>
       }
       
       if (this.props.error) {
           return <div style={{color: 'red'}}>ERROR: {this.props.error}</div>
       }
    
       return (
           <table>
               <thead>
                   <tr>
                       <th>First Name</th>
                       <th>Last Name</th>
                       <th>Active?</th>
                       <th>Posts</th>
                       <th>Messages</th>
                   </tr>
               </thead>
               <tbody>
                   {this.props.data.map(u =>
                       <tr key={u.id}>
                           <td>{u.firstName}</td>
                           <td>{u.lastName}</td>
                           <td>{u.active ? 'Yes' : 'No'}</td>
                           <td>{u.posts}</td>
                           <td>{u.messages}</td>
                       </tr>
                   )}
               </tbody>
           </table>
       );
   }
}

const mapStateToProps = state => ({
   data: state.reduxSaga.data,
   loading: state.reduxSaga.loading,
   error: state.reduxSaga.error,
});

const mapDispatchToProps = {
   loadUsers
};

export default connect(
   mapStateToProps,
   mapDispatchToProps
)(UsersWithReduxSaga);
```

Le composant est également presque le même ici que dans l'exemple thunk.

**Voici donc 4 fichiers, 136 lignes de code (7(actions) + 36(réducteur) + sagas(33) + 60(composant)).**

#### Avantages :

* Code plus lisible (async/await)
* Bon pour gérer des scénarios complexes (appels conditionnels multiples dans une seule action, une action peut avoir plusieurs écouteurs, annulation d'actions, etc.)
* Facile à tester unitairement

#### Inconvénients :

* Beaucoup de code dans différents endroits
* Après la navigation vers une autre page, les anciennes données sont toujours dans l'état global. Ces données sont obsolètes et constituent des informations inutiles qui consomment de la mémoire.
* Dépendance supplémentaire
* Beaucoup de concepts à apprendre

### Suspense

Suspense est une nouvelle fonctionnalité de React 16.6.0. Elle nous permet de différer le rendu d'une partie du composant jusqu'à ce qu'une certaine condition soit remplie (par exemple, les données de l'API chargées).

Pour que cela fonctionne, nous devons faire 4 choses (c'est définitivement mieux :) ).

#### 1. Créer un cache (suspense/cache.js)

Pour le cache, nous allons utiliser un [simple-cache-provider](https://www.npmjs.com/package/simple-cache-provider) qui est un fournisseur de cache de base pour les applications react.

```js
import {createCache} from 'simple-cache-provider';

export let cache;

function initCache() {
 cache = createCache(initCache);
}

initCache();
```

#### 2. Créer une limite d'erreur (suspense/ErrorBoundary.js)

Ceci est une limite d'erreur pour attraper les erreurs lancées par Suspense.

```js
import React from 'react';

export class ErrorBoundary extends React.Component {
 state = {};

 componentDidCatch(error) {
   this.setState({ error: error.message || "Unexpected error" });
 }

 render() {
   if (this.state.error) {
     return <div style={{ color: 'red' }}>ERROR: {this.state.error || 'Unexpected Error'}</div>;
   }

   return this.props.children;
 }
}

export default ErrorBoundary;
```

#### 3. Créer un tableau d'utilisateurs (suspense/UsersTable.js)

Pour cet exemple, nous devons créer un composant supplémentaire qui charge et affiche les données. Ici, nous créons une ressource pour obtenir des données de l'API.

```js
import * as React from 'react';
import {createResource} from "simple-cache-provider";
import {cache} from "./cache";
import Api from "../api";

let UsersResource = createResource(async () => {
   const response = await Api.getUsers();
   const json = await response.json();
    
   return json;
});

class UsersTable extends React.Component {
   render() {
       let users = UsersResource.read(cache);
       
       return (
           <table>
               <thead>
               <tr>
                   <th>First Name</th>
                   <th>Last Name</th>
                   <th>Active?</th>
                   <th>Posts</th>
                   <th>Messages</th>
               </tr>
               </thead>
               <tbody>
               {users.map(u =>
                   <tr key={u.id}>
                       <td>{u.firstName}</td>
                       <td>{u.lastName}</td>
                       <td>{u.active ? 'Yes' : 'No'}</td>
                       <td>{u.posts}</td>
                       <td>{u.messages}</td>
                   </tr>
               )}
               </tbody>
           </table>
       );
   }
}

export default UsersTable;
```

#### 4. Créer un composant (suspense/UsersWithSuspense.js)

```js
import * as React from 'react';
import UsersTable from "./UsersTable";
import ErrorBoundary from "./ErrorBoundary";

class UsersWithSuspense extends React.Component {
   render() {
       return (
           <ErrorBoundary>
               <React.Suspense fallback={<div>Loading</div>}>
                   <UsersTable/>
               </React.Suspense>
           </ErrorBoundary>
       );
   }
}

export default UsersWithSuspense;
```

**4 fichiers, 106 lignes de code (9(cache) + 19(ErrorBoundary) + UsersTable(33) + 45(composant)).**

**3 fichiers, 87 lignes de code (9(cache) + UsersTable(33) + 45(composant)) si nous supposons que ErrorBoundary est un composant réutilisable.**

#### Avantages :

* Pas besoin de redux. Cette approche peut être utilisée sans redux. Le composant est entièrement indépendant.
* Aucune dépendance supplémentaire ([simple-cache-provider](https://www.npmjs.com/package/simple-cache-provider) fait partie de React)
* Délai d'affichage de l'indicateur de chargement en définissant la propriété dellayMs
* Moins de lignes de code que dans les exemples précédents

#### Inconvénients :

* Le cache est nécessaire même lorsque nous n'avons pas vraiment besoin de mise en cache.
* Certains nouveaux concepts doivent être appris (qui font partie de React).

### Hooks

Au moment de la rédaction de cet article, les hooks n'ont pas encore été officiellement publiés et sont disponibles uniquement dans la version "next". Les hooks sont indiscutablement l'une des fonctionnalités révolutionnaires à venir qui peuvent changer beaucoup de choses dans le monde React très bientôt. Plus de détails sur les hooks peuvent être trouvés [ici](https://reactjs.org/docs/hooks-intro.html) et [ici](https://reactjs.org/docs/hooks-overview.html).

Pour que cela fonctionne pour notre exemple, nous devons faire **une(!)** chose :

#### 1. Créer et utiliser des hooks (hooks/UsersWithHooks.js)

Ici, nous créons 3 hooks (fonctions) pour "accrocher" l'état React.

```js
import React, {useState, useEffect} from 'react';
import Api from "../api";

function UsersWithHooks() {
   const [data, setData] = useState([]);
   const [loading, setLoading] = useState(true);
   const [error, setError] = useState('');
    
   useEffect(() => {
       async function fetchData() {
           try {
               const response = await Api.getUsers();
               const json = await response.json();

            setData(json);
           } catch (e) {
               setError(e.message || 'Unexpected error');
           }

           setLoading(false);
       }

       fetchData();
   }, []);
    
   if (loading) {
       return <div>Loading</div>
   }
    
   if (error) {
       return <div style={{color: 'red'}}>ERROR: {error}</div>
   }

   return (
       <table>
           <thead>
           <tr>
               <th>First Name</th>
               <th>Last Name</th>
               <th>Active?</th>
               <th>Posts</th>
               <th>Messages</th>
           </tr>
           </thead>
           <tbody>
           {data.map(u =>
               <tr key={u.id}>
                   <td>{u.firstName}</td>
                   <td>{u.lastName}</td>
                   <td>{u.active ? 'Yes' : 'No'}</td>
                   <td>{u.posts}</td>
                   <td>{u.messages}</td>
               </tr>
           )}
           </tbody>
       </table>
   );
}

export default UsersWithHooks;
```

**Et c'est tout — juste 1 fichier, 56 lignes de code !!!**

#### Avantages :

* Pas besoin de redux. Cette approche peut être utilisée sans redux. Le composant est entièrement indépendant.
* Aucune dépendance supplémentaire
* Environ 2 fois moins de code que dans les autres solutions

#### Inconvénients :

* À première vue, le code semble bizarre et difficile à lire et à comprendre. Il faudra un certain temps pour s'habituer aux hooks.
* Certains nouveaux concepts doivent être appris (qui font partie de React)
* Pas encore officiellement publié

### Conclusion

Organisons d'abord ces métriques sous forme de tableau.

![Image](https://cdn-media-1.freecodecamp.org/images/Em2SE0unpxwElJ45-SaSNQZ15H0eGDdJQqIj)

* Redux est toujours une bonne option pour gérer l'état global (si vous en avez un)
* Chaque option a des avantages et des inconvénients. Quelle approche est meilleure dépend du projet : sa complexité, ses cas d'utilisation, les connaissances de l'équipe, quand le projet passe en production, etc.
* Saga peut aider avec des cas d'utilisation complexes
* Suspense et Hooks valent tous deux la peine d'être considérés (ou au moins appris) surtout pour les nouveaux projets

C'est tout — profitez et bon codage !