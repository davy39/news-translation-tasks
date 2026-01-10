---
title: Comment travailler avec Redux-Thunk – Expliqué avec des exemples
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-02-26T02:35:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-redux-thunk
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Ivory-and-Blue-Lavender-Aesthetic-Photo-Collage-Presentation--11-.png
tags:
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'State Management '
  slug: state-management
seo_title: Comment travailler avec Redux-Thunk – Expliqué avec des exemples
seo_desc: 'Redux has become the go-to state management library for many JavaScript
  applications due to its predictable state container and unidirectional data flow.

  However, handling asynchronous actions in Redux can be a bit tricky. That''s where
  Redux middlewa...'
---

Redux est devenu la bibliothèque de gestion d'état de choix pour de nombreuses applications JavaScript grâce à son conteneur d'état prévisible et son flux de données unidirectionnel.

Cependant, la gestion des actions asynchrones dans Redux peut être un peu délicate. C'est là que les middlewares Redux comme Redux-Thunk viennent à la rescousse.

En essence, Redux-Thunk améliore les capacités de Redux en fournissant un mécanisme simple et efficace pour gérer les actions asynchrones. Il permet aux développeurs d'écrire du code propre, prévisible et maintenable tout en assurant l'intégrité de la gestion d'état de l'application.

## Table des matières

1. [Introduction à Redux-Thunk](#heading-1-introduction-a-redux-thunk)

* 1.1. [Comprendre le Middleware dans Redux](#heading-11-comprendre-le-middleware-dans-redux)
* 1.2. [Le Rôle de Redux-Thunk](#heading-12-le-role-de-redux-thunk)

2. [Installation et Configuration](#heading-2-installation-et-configuration)

3. [Travailler avec Redux-Thunk](#heading-3-travailler-avec-redux-thunk)

* 3.1. [Écrire des Fonctions Thunk](#heading-31-ecrire-des-fonctions-thunk)
* 3.2. [Dispatcher des Actions Thunk](#heading-32-dispatcher-des-actions-thunk)

4. [Gestion des Opérations Asynchrones](#heading-4-gestion-des-operations-asynchrones)

* 4.1. [Effectuer des Appels API Asynchrones](#heading-41-effectuer-des-appels-api-asynchrones)
* 4.2. [Gérer les Effets de Bord avec les Thunks](#heading-42-gerer-les-effets-de-bord-avec-les-thunks)

5. [Techniques Avancées](#heading-5-techniques-avancees)

* 5.1. [Gestion des Erreurs dans les Thunks](#heading-51-gestion-des-erreurs-dans-les-thunks)
* 5.2. [Chaînage de Plusieurs Thunks](#heading-52-chainage-de-plusieurs-thunks)

6. [Bonnes Pratiques](#heading-6-bonnes-pratiques)

* 6.1. [Structurer les Thunks pour la Maintenabilité](#heading-61-structurer-les-thunks-pour-la-maintenabilite)
* 6.2. [Éviter les Pièges Courants](#heading-62-eviter-les-pieges-courants)
* 6.3. [Tester les Fonctions Thunk](#heading-63-tester-les-fonctions-thunk)

7. [Exemples Concrets](#heading-7-exemples-concrets)

* 7.1. [Intégration avec les Applications React](#heading-71-integration-avec-les-applications-react)
* 7.2. [Cas d'Utilisation dans les Projets à Grande Échelle](#heading-72-cas-dutilisation-dans-les-projets-a-grande-echelle)

8. [Considérations de Performance](#heading-8-considerations-de-performance)

9. [Alternatives à Redux-Thunk](#heading-9-alternatives-a-redux-thunk)

* 9.1. [Comparaison avec d'Autres Middlewares](#heading-91-comparaison-avec-dautres-middlewares)
* 9.2. [Quand Choisir Redux-Thunk](#heading-92-quand-choisir-redux-thunk)

[10. Conclusion](#heading-10-conclusion)

## 1. Introduction à Redux-Thunk

Redux-Thunk est un middleware pour Redux qui vous permet d'écrire des créateurs d'actions qui retournent une fonction au lieu d'un objet d'action. Cette fonction reçoit la méthode `dispatch` du store et la fonction `getState` comme arguments, lui permettant de dispatcher plusieurs actions, d'effectuer des opérations asynchrones et d'accéder à l'état actuel si nécessaire avant de dispatcher une action.

### 1.1. Comprendre le Middleware dans Redux

Avant de plonger dans Redux-Thunk, discutons brièvement de ce qu'est un middleware dans le contexte de Redux.

Le middleware fournit un moyen d'interagir avec les actions dispatchées vers le store Redux avant qu'elles n'atteignent le reducer. Il se situe entre le dispatch de l'action et le reducer, vous permettant d'intercepter, de modifier ou de retarder les actions selon les besoins.

Il fournit un moyen d'étendre les fonctionnalités de Redux en interceptant et en modifiant potentiellement les actions avant qu'elles n'atteignent les reducers.

### 1.2. Le Rôle de Redux-Thunk

Le but principal de Redux-Thunk est de gérer les actions asynchrones dans Redux. Les actions asynchrones, telles que la récupération de données depuis une API ou l'exécution de calculs asynchrones, sont courantes dans les applications web.

Redux-Thunk vous permet de dispatcher des actions de manière asynchrone, facilitant ainsi la gestion des effets de bord dans vos applications Redux.

## 2. Installation et Configuration

La configuration de Redux-Thunk dans votre projet Redux est simple. Tout d'abord, vous devez installer le package `redux-thunk` en utilisant `npm` ou `yarn` :

```bash
npm install redux-thunk
# ou
yarn add redux-thunk

```

Une fois installé, vous pouvez intégrer Redux-Thunk dans votre store Redux en l'appliquant comme middleware lors de la création du store :

```javascript
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './reducers';

const store = createStore(
  rootReducer,
  applyMiddleware(thunk)
);

```

En appliquant le middleware Redux-Thunk avec `applyMiddleware`, vous activez Redux pour reconnaître et traiter les fonctions thunk lorsqu'elles sont dispatchées.

## 3. Travailler avec Redux-Thunk

Maintenant que Redux-Thunk est configuré dans votre projet, explorons comment travailler avec efficacement.

### 3.1. Écrire des Fonctions Thunk

Écrire des fonctions thunk dans Redux implique de définir des créateurs d'actions asynchrones qui retournent une fonction au lieu d'un simple objet d'action. Ces fonctions ont accès aux méthodes `dispatch` et `getState` du store Redux, vous permettant d'effectuer des opérations asynchrones et de dispatcher des actions en fonction des résultats.

Voici comment vous pouvez écrire des fonctions thunk dans Redux :

```javascript
// actions.js
import axios from 'axios';

// Types d'actions
export const FETCH_DATA_REQUEST = 'FETCH_DATA_REQUEST';
export const FETCH_DATA_SUCCESS = 'FETCH_DATA_SUCCESS';
export const FETCH_DATA_FAILURE = 'FETCH_DATA_FAILURE';

// Créateurs d'actions
export const fetchDataRequest = () => ({
  type: FETCH_DATA_REQUEST
});

export const fetchDataSuccess = (data) => ({
  type: FETCH_DATA_SUCCESS,
  payload: data
});

export const fetchDataFailure = (error) => ({
  type: FETCH_DATA_FAILURE,
  payload: error
});

// Créateur d'action Thunk
export const fetchData = () => {
  return async (dispatch, getState) => {
    dispatch(fetchDataRequest());
    try {
      const response = await axios.get('https://api.example.com/data');
      dispatch(fetchDataSuccess(response.data));
    } catch (error) {
      dispatch(fetchDataFailure(error.message));
    }
  };
};

```

Dans cet exemple :

1. Nous avons défini des types d'actions pour différentes étapes du processus de récupération de données : demande, succès et échec.
2. Nous avons défini des créateurs d'actions pour chaque type d'action, qui retournent des objets d'action simples avec le type et la charge utile appropriés.
3. Nous avons défini un créateur d'action thunk appelé `fetchData`, qui retourne une fonction au lieu d'un simple objet d'action. Cette fonction reçoit `dispatch` et `getState` comme arguments, nous permettant de dispatcher des actions et d'accéder à l'état actuel de Redux.
4. À l'intérieur de la fonction thunk, nous dispatchons l'action `FETCH_DATA_REQUEST` pour indiquer que le processus de récupération de données a commencé.
5. Nous avons utilisé `axios` (vous pouvez utiliser n'importe quel autre client HTTP) pour faire une requête GET asynchrone afin de récupérer des données depuis un endpoint API.
6. Si la requête réussit, nous dispatchons l'action `FETCH_DATA_SUCCESS` avec les données récupérées comme charge utile.
7. Si la requête échoue, nous dispatchons l'action `FETCH_DATA_FAILURE` avec le message d'erreur comme charge utile.

Les fonctions thunk fournissent un moyen flexible et puissant de gérer les actions asynchrones dans Redux, vous permettant d'encapsuler une logique asynchrone complexe et de gérer les effets de bord efficacement.

### 3.2. Dispatcher des Actions Thunk

Vous pouvez dispatcher des actions thunk comme des actions régulières en utilisant la méthode `dispatch` fournie par le store Redux :

```javascript
store.dispatch(fetchUser());

```

Lorsque vous dispatch une action thunk, Redux-Thunk l'intercepte et invoque la fonction thunk avec la méthode `dispatch` et la fonction `getState` comme arguments.

Cela permet à la fonction thunk d'effectuer des opérations asynchrones et de dispatcher des actions supplémentaires si nécessaire.

## 4. Gestion des Opérations Asynchrones

L'un des principaux avantages de Redux-Thunk est sa capacité à gérer les opérations asynchrones de manière transparente. Explorons quelques scénarios courants où Redux-Thunk excelle :

### 4.1. Effectuer des Appels API Asynchrones

Effectuer des appels API asynchrones dans les thunks Redux est un cas d'utilisation courant pour la gestion de la récupération et de la mise à jour des données dans les applications React.

Voici comment vous pouvez effectuer des appels API asynchrones dans les thunks Redux :

#### A. Importer les Dépendances Nécessaires

Tout d'abord, assurez-vous d'avoir les dépendances nécessaires installées. Vous aurez généralement besoin de Redux, du middleware Redux Thunk et d'une bibliothèque pour effectuer des requêtes HTTP, comme Axios ou Fetch.

```bash
npm install redux redux-thunk axios

```

#### B. Créer des Créateurs d'Actions Thunk

Définissez des créateurs d'actions thunk qui dispatcheront des actions pour gérer les requêtes API. Les thunks sont des fonctions qui retournent une autre fonction, vous permettant d'effectuer des opérations asynchrones avant de dispatcher des actions.

```javascript
// actions.js
import axios from 'axios';

export const fetchDataRequest = () => ({ type: 'FETCH_DATA_REQUEST' });
export const fetchDataSuccess = (data) => ({ type: 'FETCH_DATA_SUCCESS', payload: data });
export const fetchDataFailure = (error) => ({ type: 'FETCH_DATA_FAILURE', payload: error });

export const fetchData = () => {
  return async (dispatch) => {
    dispatch(fetchDataRequest());
    try {
      const response = await axios.get('https://api.example.com/data');
      dispatch(fetchDataSuccess(response.data));
    } catch (error) {
      dispatch(fetchDataFailure(error.message));
    }
  };
};

```

#### C. Dispatcher des Actions Thunk

Dispatchez le créateur d'action thunk depuis votre composant lorsque vous devez récupérer des données. Cela déclenchera l'appel API asynchrone et mettra à jour le store Redux en conséquence.

```javascript
// SomeComponent.js
import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchData } from './actions';

const SomeComponent = () => {
  const dispatch = useDispatch();
  const { data, isLoading, error } = useSelector(state => state.someReducer);

  useEffect(() => {
    dispatch(fetchData());
  }, [dispatch]);

  if (isLoading) {
    return <div>Chargement...</div>;
  }

  if (error) {
    return <div>Erreur : {error}</div>;
  }

  return (
    <div>
      {/* Afficher les données récupérées */}
    </div>
  );
};

export default SomeComponent;

```

#### D. Mettre à Jour le Reducer

Mettez à jour le reducer pour gérer les actions dispatchées et mettre à jour l'état en conséquence.

```javascript
// reducers.js
const initialState = {
  data: null,
  isLoading: false,
  error: null
};

const someReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'FETCH_DATA_REQUEST':
      return { ...state, isLoading: true, error: null };
    case 'FETCH_DATA_SUCCESS':
      return { ...state, data: action.payload, isLoading: false };
    case 'FETCH_DATA_FAILURE':
      return { ...state, error: action.payload, isLoading: false };
    default:
      return state;
  }
};

export default someReducer;

```

#### E. Configurer le Store Redux

Enfin, configurez votre store Redux avec le middleware Redux Thunk.

```javascript
// store.js
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './reducers';

const store = createStore(rootReducer, applyMiddleware(thunk));

export default store;

```

Votre application Redux est maintenant configurée pour effectuer des appels API asynchrones en utilisant les thunks Redux. Les thunks fournissent un moyen pratique de gérer les opérations asynchrones dans Redux et s'intègrent de manière transparente avec le flux de travail Redux.

### 4.2. Gérer les Effets de Bord avec les Thunks

Gérer les effets de bord, tels que les opérations asynchrones, dans les applications Redux peut être efficacement fait en utilisant les thunks.

Les thunks vous permettent d'encapsuler une logique complexe, y compris les effets de bord, au sein des créateurs d'actions, fournissant un moyen centralisé et organisé de gérer de telles opérations.

Voici comment vous pouvez gérer les effets de bord avec les thunks :

#### A. Définir les Créateurs d'Actions Thunk

Créez des créateurs d'actions thunk qui encapsulent la logique asynchrone ou les effets de bord que vous souhaitez gérer.

Les thunks sont des fonctions qui retournent une autre fonction, vous donnant accès à la fonction `dispatch` et à la méthode `getState` du store Redux.

```javascript
// actions.js
import axios from 'axios';

export const fetchDataRequest = () => ({ type: 'FETCH_DATA_REQUEST' });
export const fetchDataSuccess = (data) => ({ type: 'FETCH_DATA_SUCCESS', payload: data });
export const fetchDataFailure = (error) => ({ type: 'FETCH_DATA_FAILURE', payload: error });

export const fetchData = () => {
  return async (dispatch) => {
    dispatch(fetchDataRequest());
    try {
      const response = await axios.get('https://api.example.com/data');
      dispatch(fetchDataSuccess(response.data));
    } catch (error) {
      dispatch(fetchDataFailure(error.message));
    }
  };
};

```

#### B. Dispatcher des Actions Thunk

Dispatchez le créateur d'action thunk depuis vos composants lorsque vous devez déclencher l'effet de bord. Cela exécutera la logique asynchrone encapsulée dans le thunk.

```javascript
// SomeComponent.js
import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchData } from './actions';

const SomeComponent = () => {
  const dispatch = useDispatch();
  const { data, isLoading, error } = useSelector(state => state.someReducer);

  useEffect(() => {
    dispatch(fetchData());
  }, [dispatch]);

  // Rendre l'UI en fonction des données récupérées, de l'état de chargement ou du statut d'erreur
};

export default SomeComponent;

```

#### C. Mettre à Jour le Reducer

Mettez à jour le reducer pour gérer les actions dispatchées et mettre à jour l'état du store Redux en conséquence. Cela implique généralement la mise à jour de l'état pour refléter l'état de chargement, le succès ou l'échec de l'opération asynchrone.

```javascript
// reducers.js
const initialState = {
  data: null,
  isLoading: false,
  error: null
};

const someReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'FETCH_DATA_REQUEST':
      return { ...state, isLoading: true, error: null };
    case 'FETCH_DATA_SUCCESS':
      return { ...state, data: action.payload, isLoading: false };
    case 'FETCH_DATA_FAILURE':
      return { ...state, error: action.payload, isLoading: false };
    default:
      return state;
  }
};

export default someReducer;

```

#### D. Configurer le Store Redux avec le Middleware Thunk

Assurez-vous d'avoir configuré votre store Redux avec le middleware Redux Thunk pour activer les créateurs d'actions thunk.

```javascript
// store.js
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './reducers';

const store = createStore(rootReducer, applyMiddleware(thunk));

export default store;

```

Avec les thunks, vous pouvez gérer les effets de bord tels que la récupération de données, les appels API ou toute opération asynchrone de manière structurée et centralisée au sein de votre application Redux.

Les thunks favorisent la séparation des préoccupations et facilitent le test et la maintenance de la logique asynchrone au sein de votre base de code Redux.

## 5. Techniques Avancées

Redux-Thunk offre plusieurs techniques avancées pour gérer des scénarios complexes. Explorons certaines d'entre elles :

### 5.1. Gestion des Erreurs dans les Thunks

La gestion des erreurs dans les thunks est essentielle pour garantir que votre application Redux se comporte de manière prévisible et gère élégamment les erreurs qui surviennent lors des opérations asynchrones, telles que les requêtes API.

Voici comment vous pouvez gérer les erreurs efficacement dans les thunks :

#### A. Capturer les Erreurs dans les Thunks

```javascript
export const fetchData = () => {
  return async (dispatch) => {
    dispatch(fetchDataRequest());
    try {
      const response = await fetch('https://api.example.com/data');
      if (!response.ok) {
        throw new Error('Échec de la récupération des données');
      }
      const data = await response.json();
      dispatch(fetchDataSuccess(data));
    } catch (error) {
      dispatch(fetchDataFailure(error.message));
    }
  };
};

```

Dans cet exemple :

* Nous avons utilisé un bloc `try...catch` pour capturer toute erreur qui survient lors de l'opération asynchrone (dans ce cas, la récupération de données depuis une API).
* Si une erreur survient, nous dispatchons une action pour gérer l'erreur (`fetchDataFailure`), en passant le message d'erreur comme charge utile.

#### B. Gérer les Erreurs de Manière Appropriée

* Dispatcher des actions d'erreur spécifiques en fonction du type d'erreur rencontré.
* Inclure des messages d'erreur significatifs ou des codes d'erreur dans les actions d'erreur pour fournir un contexte pour le débogage et les retours utilisateur.
* Envisager si certaines erreurs doivent déclencher des actions ou des effets de bord supplémentaires, tels que la journalisation des erreurs ou l'affichage de notifications d'erreur.

#### C. Centraliser la Logique de Gestion des Erreurs

```javascript
// sharedThunks.js

export const handleApiError = (error) => {
  return (dispatch) => {
    dispatch(showErrorNotification(error.message));
    dispatch(logError(error));
  };
};

```

Dans cet exemple :

* Nous avons défini un thunk partagé (`handleApiError`) responsable de la gestion des erreurs des requêtes API.
* Ce thunk dispache des actions pour afficher des notifications d'erreur et journaliser les erreurs.
* Centraliser la logique de gestion des erreurs dans des thunks partagés favorise la cohérence et la réutilisabilité dans différentes parties de votre application.

#### D. Tester les Scénarios d'Erreur

* Écrire des tests unitaires pour couvrir les scénarios de gestion des erreurs dans vos thunks.
* Simuler les requêtes API pour simuler différentes conditions d'erreur, telles que les erreurs réseau ou les erreurs serveur.
* Vérifier que le thunk dispache les actions d'erreur correctes et gère les erreurs de manière appropriée.

#### E. Envisager des Stratégies de Nouvelle Tentative

* Implémenter des stratégies de nouvelle tentative pour gérer les erreurs transitoires, telles que les problèmes réseau temporaires ou les erreurs de limitation de débit.
* Les thunks peuvent inclure une logique de nouvelle tentative pour tenter à nouveau l'opération après un délai ou un certain nombre de tentatives.

En gérant efficacement les erreurs dans les thunks, vous pouvez améliorer la robustesse et la fiabilité de votre application Redux, offrant aux utilisateurs une meilleure expérience et simplifiant les efforts de débogage et de maintenance.

### 5.2. Chaînage de Plusieurs Thunks

Les thunks peuvent être enchaînés pour effectuer des séquences complexes d'opérations asynchrones. Cela est utile lorsque vous devez effectuer plusieurs tâches asynchrones de manière séquentielle :

```javascript
const fetchUserAndPosts = () => {
  return async (dispatch, getState) => {
    try {
      // Récupérer l'utilisateur
      dispatch({ type: 'FETCH_USER_REQUEST' });
      const userResponse = await fetch('https://api.example.com/user');
      const user = await userResponse.json();
      dispatch({ type: 'FETCH_USER_SUCCESS', payload: user });

      // Récupérer les posts
      dispatch({ type: 'FETCH_POSTS_REQUEST' });
     

 const postsResponse = await fetch('https://api.example.com/posts');
      const posts = await postsResponse.json();
      dispatch({ type: 'FETCH_POSTS_SUCCESS', payload: posts });
    } catch (error) {
      dispatch({ type: 'FETCH_FAILURE', error: error.message });
    }
  };
};

```

En enchaînant plusieurs fonctions thunk ensemble, vous pouvez orchestrer des flux de travail asynchrones complexes avec facilité.

## 6. Bonnes Pratiques

Bien que Redux-Thunk offre des capacités puissantes pour gérer les actions asynchrones, il est essentiel de suivre les meilleures pratiques pour garantir que votre code reste maintenable et efficace.

Voici quelques bonnes pratiques à considérer :

### 6.1. Structurer les Thunks pour la Maintenabilité

Structurer les thunks pour la maintenabilité est crucial pour garantir que votre code Redux reste organisé, évolutif et facile à maintenir à mesure que votre application grandit.

Voici une approche recommandée pour structurer les thunks :

### Séparer les Préoccupations

#### a. Types d'Actions et Créateurs d'Actions

* Définir les types d'actions et les créateurs d'actions séparément pour promouvoir la réutilisabilité et la maintenabilité.
* Grouper les types d'actions et les créateurs liés dans des modules ou des fichiers logiques.

#### b. Fonctions Thunk

* Définir les fonctions thunk séparément des créateurs d'actions pour garder les préoccupations des opérations asynchrones distinctes des actions synchrones.

### Modulariser les Thunks

#### a. Thunks au Niveau du Module

* Grouper les fonctions thunk liées au sein de modules ou de tranches de fonctionnalités de votre application.
* Chaque module peut contenir son propre ensemble de thunks responsables de la gestion des opérations asynchrones liées à ce module.

#### b. Thunks Réutilisables

* Extraire les thunks réutilisables dans des fichiers ou des modules utilitaires séparés qui peuvent être partagés dans différentes parties de votre application.
* Les opérations asynchrones courantes, telles que la récupération de données ou l'authentification, peuvent être encapsulées en tant que thunks réutilisables.

### Encapsuler la Logique Complexe

#### a. Composition d'Actions

* Encapsuler la logique complexe liée à la composition d'actions au sein des thunks.
* Les thunks peuvent orchestrer plusieurs actions synchrones pour effectuer une opération de niveau supérieur.

#### b. Gestion des Erreurs :

* Centraliser la logique de gestion des erreurs au sein des thunks pour garantir une signalisation et des stratégies de récupération des erreurs cohérentes.
* Les thunks peuvent capturer et gérer les erreurs des opérations asynchrones avant de dispatcher les actions d'erreur appropriées.

### Utiliser Async/Await pour la Lisibilité

#### a. Syntaxe Async/Await

* Utiliser la syntaxe async/await au sein des thunks pour un code asynchrone plus propre et plus lisible.
* Les fonctions asynchrones facilitent la gestion du flux de contrôle asynchrone par rapport à l'utilisation de Promesses brutes.

### Exemple de Structure

Voici un exemple de la manière dont vous pouvez structurer les thunks pour la maintenabilité :

```plaintext
src/
├── actions/
│   ├── actionTypes.js
│   ├── feature1Actions.js
│   ├── feature2Actions.js
│   └── ...
├── thunks/
│   ├── feature1Thunks.js
│   ├── feature2Thunks.js
│   ├── sharedThunks.js
│   └── index.js
├── reducers/
│   ├── feature1Reducer.js
│   ├── feature2Reducer.js
│   └── ...
└── store.js

```

Dans cette structure :

* `feature1Thunks.js` et `feature2Thunks.js` contiennent des thunks spécifiques à différentes fonctionnalités/modules de votre application.
* `sharedThunks.js` contient des thunks réutilisables partagés dans plusieurs fonctionnalités.
* `index.js` exporte tous les thunks pour être importés dans la configuration du store Redux.
* Les types d'actions et les créateurs d'actions sont définis dans des fichiers séparés dans le répertoire `actions`.

En structurant les thunks de manière modulaire et organisée, vous pouvez améliorer la maintenabilité de votre base de code Redux.

Séparer les préoccupations, encapsuler la logique complexe et promouvoir la réutilisabilité facilitera la gestion et l'extension du comportement asynchrone de votre application au fil du temps.

### 6.2. Éviter les Pièges Courants

Éviter les pièges courants lors de l'utilisation de Redux-Thunk peut aider à maintenir un processus de développement plus fluide et garantir la fiabilité de vos applications Redux.

Voici quelques pièges courants à surveiller et comment les éviter :

#### Surutilisation des Thunks pour les Actions Synchrones

* Les thunks sont principalement destinés à la gestion des actions asynchrones. Les surutiliser pour les actions synchrones peut conduire à une complexité inutile dans votre code.
* **Solution** : Réservez les thunks pour les actions asynchrones comme la récupération de données ou les appels API. Pour les actions synchrones, définissez des créateurs d'actions réguliers qui retournent directement des objets d'action.

#### Logique Excessive dans les Thunks

* Mettre trop de logique à l'intérieur des thunks peut les rendre difficiles à comprendre, tester et maintenir.
* **Solution** : Gardez les thunks concentrés sur le dispatch d'actions et la gestion des opérations asynchrones. Extrayez la logique complexe dans des fonctions ou utilitaires séparés qui peuvent être testés indépendamment.

#### Manque de Gestion des Erreurs

* L'échec de la gestion des erreurs dans les thunks peut entraîner un comportement inattendu ou des plantages de l'application.
* **Solution** : Assurez-vous que vos thunks gèrent les erreurs de manière élégante en capturant les exceptions et en dispatchant des actions d'erreur appropriées. Cela inclut la gestion des erreurs provenant d'opérations asynchrones comme les requêtes API.

#### Récupération Inefficace des Données

* Les pratiques inefficaces de récupération de données, telles que la récupération répétée des mêmes données ou la récupération de données inutiles, peuvent impacter les performances.
* **Solution** : Implémentez des mécanismes de mise en cache pour stocker les données récupérées localement et éviter les requêtes API redondantes. Utilisez des techniques de mémoisation ou des sélecteurs pour optimiser la récupération de données et éviter les re-rendus inutiles.

#### Mauvaise Pratique de Test

* Des tests inadéquats des thunks peuvent entraîner des bugs et des régressions non détectés.
* **Solution** : Écrivez des tests unitaires complets pour vos thunks afin de couvrir différents scénarios, y compris les opérations asynchrones réussies et échouées. Simulez les dépendances externes comme les requêtes API pour isoler le comportement des thunks.

#### Effets de Bord Incontrôlés

* Les thunks qui déclenchent des effets de bord non intentionnels ou ont un comportement imprévisible peuvent conduire à des bugs et à des états d'application inattendus.
* **Solution** : Soyez conscient des effets de bord introduits par vos thunks, tels que la modification de l'état global ou l'interaction avec des systèmes externes. Gardez les effets de bord sous contrôle et documentez clairement le comportement de vos thunks.

#### Composition Complexe de Middleware

* Ajouter plusieurs couches de middleware, telles que la journalisation ou l'analyse, sans organisation et coordination appropriées peut rendre le pipeline de middleware difficile à gérer.
* **Solution** : Gardez la composition de middleware simple et bien organisée. Utilisez des bibliothèques de middleware comme Redux DevTools Extension pour déboguer et surveiller le comportement du middleware pendant le développement.

En évitant ces pièges courants et en suivant les meilleures pratiques lors de l'utilisation de Redux-Thunk, vous pouvez améliorer la fiabilité, les performances et la maintenabilité de vos applications Redux.

### 6.3. Tester les Fonctions Thunk

Tester les fonctions thunk dans les applications Redux est crucial pour garantir que les actions asynchrones se comportent comme prévu.

Lors du test des fonctions thunk, vous souhaitez vérifier que les actions correctes sont dispatchées dans diverses conditions, telles que les requêtes API réussies, les requêtes échouées ou les cas limites.

Voici comment vous pouvez tester les fonctions thunk en utilisant des frameworks de test populaires comme Jest et des utilitaires de test comme Redux Mock Store :

### Configuration de Test d'Exemple

Supposons que nous avons une fonction thunk appelée `fetchData` qui récupère des données depuis une API et dispache des actions correspondantes en fonction du résultat :

```javascript
// actions.js
export const fetchDataRequest = () => ({ type: 'FETCH_DATA_REQUEST' });
export const fetchDataSuccess = (data) => ({ type: 'FETCH_DATA_SUCCESS', payload: data });
export const fetchDataFailure = (error) => ({ type: 'FETCH_DATA_FAILURE', payload: error });

// thunks.js
import { fetchDataRequest, fetchDataSuccess, fetchDataFailure } from './actions';

export const fetchData = () => {
  return async (dispatch) => {
    dispatch(fetchDataRequest());
    try {
      const response = await fetch('https://api.example.com/data');
      const data = await response.json();
      dispatch(fetchDataSuccess(data));
    } catch (error) {
      dispatch(fetchDataFailure(error.message));
    }
  };
};

```

### Écrire des Tests

Voici comment vous pouvez écrire des tests pour la fonction thunk `fetchData` :

```javascript
// thunks.test.js
import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';
import fetchMock from 'jest-fetch-mock';
import { fetchData } from './thunks';
import { fetchDataRequest, fetchDataSuccess, fetchDataFailure } from './actions';

const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);

fetchMock.enableMocks();

describe('fetchData thunk', () => {
  beforeEach(() => {
    fetchMock.resetMocks();
  });

  it('dispatches fetchDataSuccess action after successful API request', async () => {
    const mockData = { id: 1, name: 'Example Data' };
    fetchMock.mockResponse(JSON.stringify(mockData));
    const expectedActions = [
      fetchDataRequest(),
      fetchDataSuccess(mockData)
    ];
    const store = mockStore();

    await store.dispatch(fetchData());
    expect(store.getActions()).toEqual(expectedActions);
  });

  it('dispatches fetchDataFailure action after failed API request', async () => {
    const errorMessage = 'Failed to fetch data';
    fetchMock.mockReject(new Error(errorMessage));
    const expectedActions = [
      fetchDataRequest(),
      fetchDataFailure(errorMessage)
    ];
    const store = mockStore();

    await store.dispatch(fetchData());
    expect(store.getActions()).toEqual(expectedActions);
  });
});

```

Voici ce qui se passe dans le code ci-dessus :

#### Simulation de l'API Fetch :

* Nous avons utilisé `fetchMock` de Jest pour simuler la fonction `fetch`, ce qui nous permet de contrôler son comportement pendant les tests.

#### Configuration du Store Mock Redux :

* Nous avons configuré un store Redux mock en utilisant `redux-mock-store`, ce qui nous permet de simuler le comportement du store Redux dans nos tests.

#### Dispatch de la Fonction Thunk :

* Nous avons dispatché la fonction thunk `fetchData` en utilisant le store mock et attendu sa complétion.

#### Attentes :

* Nous avons vérifié que les actions attendues sont dispatchées en fonction de différents scénarios (requêtes API réussies ou échouées).

#### Réinitialisation des Mocks :

* Nous avons réinitialisé les mocks avant chaque test pour garantir qu'ils commencent dans un état propre.

En écrivant des tests pour les fonctions thunk de cette manière, vous pouvez vérifier leur comportement dans diverses conditions, garantissant la fiabilité et la justesse des actions asynchrones de votre application Redux.

## 7. Exemples Concrets

Pour démontrer l'utilisation pratique de Redux-Thunk, examinons quelques exemples concrets de son utilisation dans une application Redux.

### 7.1. Intégration avec les Applications React

Redux-Thunk s'intègre de manière transparente avec les applications React, vous permettant de gérer la récupération de données asynchrones, les mises à jour d'état et les effets de bord de manière efficace.

Voici un exemple simple d'utilisation de Redux-Thunk avec React :

```javascript
// Component.js
import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchUser } from './redux/userThunks';

const Component = () => {
  const dispatch = useDispatch();
  const user = useSelector(state => state.user);

  useEffect(() => {
    dispatch(fetchUser());
  }, [dispatch]);

  return (
    <div>
      {user ? <div>{user.name}</div> : <div>Chargement...</div>}
    </div>
  );
};

export default Component;

```

### 7.2. Cas d'Utilisation dans les Projets à Grande Échelle

Dans les grands projets React, Redux-Thunk peut être un outil précieux pour gérer les actions asynchrones et gérer la logique complexe.

Voici quelques cas d'utilisation courants pour Redux-Thunk dans les grands projets :

#### Récupération de Données

* Les applications à grande échelle ont souvent besoin de récupérer des données depuis plusieurs API ou endpoints. Redux-Thunk vous permet d'encapsuler ces opérations asynchrones dans des créateurs d'actions.
* Vous pouvez gérer des scénarios comme la récupération des données initiales lors du montage d'un composant, la pagination à travers de grands ensembles de données, ou le rafraîchissement des données périodiquement.

#### Authentification

* La mise en œuvre des flux d'authentification, tels que la connexion, la déconnexion ou le rafraîchissement des jetons, implique souvent des opérations asynchrones comme l'envoi de requêtes API et la mise à jour de l'état d'authentification de l'utilisateur.
* Redux-Thunk peut gérer ces opérations, dispatchant des actions pour mettre à jour l'état d'authentification en fonction des réponses de l'API et gérant les erreurs qui surviennent pendant le processus.

#### Soumission de Formulaires

* Les grands formulaires avec des exigences de validation complexes et des processus de soumission peuvent nécessiter des actions asynchrones pour gérer les soumissions de formulaires.
* Redux-Thunk peut dispatcher des actions pour soumettre les données du formulaire, gérer les réponses du serveur (succès ou erreur) et mettre à jour l'état de l'application en conséquence.

#### Mises à Jour Optimistes

* Dans les applications où les interactions de l'utilisateur déclenchent des actions asynchrones avec des mises à jour d'UI optimistes, Redux-Thunk peut aider à gérer le flux d'actions.
* Vous pouvez dispatcher des actions optimistes pour mettre à jour l'UI immédiatement, puis dispatcher des actions supplémentaires en fonction du succès ou de l'échec de l'opération asynchrone.

#### Intégration WebSocket

* Les applications à grande échelle utilisent souvent des connexions WebSocket pour la communication en temps réel avec les serveurs.
* Redux-Thunk peut être utilisé pour gérer les connexions WebSocket et dispatcher des actions en réponse aux messages ou événements entrants, tels que la mise à jour des composants UI ou le déclenchement d'actions supplémentaires.

#### Logique Métier Complexe

* À mesure que les applications deviennent plus complexes, elles peuvent nécessiter une logique métier plus sophistiquée pour gérer divers scénarios et cas limites.
* Redux-Thunk vous permet d'encapsuler une logique complexe au sein des créateurs d'actions, facilitant ainsi la gestion et les tests.

#### Composition de Middleware

* Dans les grands projets, vous pouvez avoir plusieurs couches de middleware dans votre configuration Redux pour des tâches comme la journalisation, la gestion des erreurs ou l'analyse.
* Redux-Thunk peut être intégré de manière transparente dans le pipeline de middleware, vous permettant de composer plusieurs fonctions de middleware pour gérer différents aspects du comportement de votre application.

En tirant parti de Redux-Thunk dans ces cas d'utilisation, vous pouvez gérer efficacement les actions asynchrones, gérer la logique complexe de l'application et maintenir une base de code évolutive et maintenable dans les grands projets React.

## 8. Considérations de Performance

Bien que Redux-Thunk offre des capacités puissantes pour gérer les actions asynchrones, il est essentiel de considérer son impact sur les performances de votre application.

Voici quelques considérations de performance à garder à l'esprit :

#### Opérations Asynchrones

Redux-Thunk permet de gérer les opérations asynchrones, telles que l'envoi de requêtes API ou l'exécution de calculs qui prennent du temps à se terminer.

Ces opérations peuvent introduire une latence dans votre application, impactant les performances globales.

#### Blocage de la Boucle d'Événements

Les tâches synchrones de longue durée au sein des thunks peuvent potentiellement bloquer la boucle d'événements JavaScript, conduisant à des interfaces utilisateur non réactives.

Évitez de bloquer la boucle d'événements en déchargeant les calculs lourds sur des threads de travail ou en les divisant en tâches asynchrones plus petites.

#### Surcoût du Middleware

L'ajout de middleware au pipeline de middleware Redux entraîne un léger surcoût de performance, car chaque fonction de middleware doit traiter les actions dispatchées de manière séquentielle.

Bien que ce surcoût soit généralement minimal, il est essentiel de garder la composition du middleware efficace.

#### Composition des Thunks

La composition de plusieurs thunks peut impacter les performances, surtout si les thunks déclenchent des opérations asynchrones supplémentaires de manière séquentielle.

Considérez attentivement la composition des thunks pour minimiser les retards inutiles et optimiser les performances.

#### Intégration de Redux DevTools

L'activation de Redux DevTools à des fins de débogage peut impacter les performances, surtout lors de l'enregistrement ou de la relecture des actions.

Utilisez Redux DevTools de manière judicieuse, surtout dans les environnements de production, pour minimiser le surcoût de performance.

#### Mémoisation et Mise en Cache

Implémentez des techniques de mémoisation ou de mise en cache pour les données récupérées afin de réduire les calculs redondants et les requêtes API.

La mémoisation garantit que les calculs coûteux ne sont effectués que lorsque cela est nécessaire, améliorant ainsi la réactivité de l'application.

#### Fractionnement de Code et Imports Dynamiques

Envisagez de fractionner votre code lié à Redux et d'importer dynamiquement les thunks ou les reducers uniquement lorsque cela est nécessaire. Cette approche peut réduire la taille initiale du bundle de votre application et améliorer les temps de chargement, surtout pour les applications à grande échelle.

#### Test et Profilage

Testez et profilez régulièrement votre application pour identifier les goulots d'étranglement de performance et les domaines à optimiser. Utilisez des outils de profilage de performance pour mesurer l'impact de Redux-Thunk sur la réactivité de l'application et identifier les opportunités d'amélioration.

En tenant compte de ces considérations de performance et en suivant les meilleures pratiques, vous pouvez garantir que votre application basée sur Redux-Thunk reste réactive et efficace, offrant une expérience utilisateur fluide. Équilibrer la puissance de Redux-Thunk avec des optimisations de performance est essentiel pour construire des applications Redux performantes.

## 9. Alternatives à Redux-Thunk

Bien que Redux-Thunk soit un choix populaire pour gérer les actions asynchrones dans Redux, il existe des solutions de middleware alternatives qui offrent des capacités similaires ou supplémentaires.

Certaines alternatives populaires à Redux-Thunk incluent Redux-Saga, Redux-Observable.

### 9.1. Comparaison avec d'Autres Middlewares

Chaque solution de middleware a ses propres forces et faiblesses, en fonction des exigences spécifiques de votre application.

Voici une brève comparaison de Redux-Thunk avec d'autres solutions de middleware :

#### Redux-Saga

* Redux-Saga est une bibliothèque pour gérer les effets de bord dans les applications Redux. Elle utilise les générateurs ES6 pour rendre le code asynchrone plus facile à lire, écrire et tester.
* Les sagas sont définies comme des fonctions séparées qui écoutent des actions Redux spécifiques et peuvent ensuite effectuer des opérations asynchrones de manière plus déclarative et testable.
* Redux-Saga est idéal pour gérer une logique asynchrone complexe, telle que les conditions de course, les annulations et les nouvelles tentatives.

Voici un exemple d'une Redux-Saga :

```javascript
function* fetchData() {
  try {
    const data = yield call(api.fetchData);
    yield put({ type: 'FETCH_DATA_SUCCESS', payload: data });
  } catch (error) {
    yield put({ type: 'FETCH_DATA_FAILURE', payload: error });
  }
}

function* watchFetchData() {
  yield takeEvery('FETCH_DATA_REQUEST', fetchData);
}

```

#### Redux-Thunk-Extra

* Redux-Thunk-Extra est une version améliorée de Redux-Thunk avec des fonctionnalités supplémentaires comme la prise en charge des promesses et les créateurs d'actions pour démarrer, réussir et échouer les opérations asynchrones.
* Il fournit une API plus simple par rapport à Redux-Saga et peut être un bon choix si vous préférez la syntaxe familière de type thunk mais avez besoin de plus de fonctionnalités.

Voici un exemple d'utilisation de Redux-Thunk-Extra avec des promesses :

```javascript
const fetchData = () => {
  return (dispatch) => {
    dispatch({ type: 'FETCH_DATA_START' });

    api.fetchData()
      .then(data => dispatch({ type: 'FETCH_DATA_SUCCESS', payload: data }))
      .catch(error => dispatch({ type: 'FETCH_DATA_FAILURE', payload: error }));
  };
};

```

#### Redux-Observable

* Redux-Observable est un middleware pour Redux basé sur RxJS, une bibliothèque puissante pour la programmation réactive.
* Il vous permet d'exprimer des flux de travail asynchrones complexes en utilisant des flux observables, ce qui le rend adapté pour gérer des événements dans le temps, tels que les entrées utilisateur ou les connexions WebSocket.
* Redux-Observable est un bon choix pour les applications avec un fort accent sur la programmation réactive ou lorsque vous avez besoin d'un contrôle fin sur le comportement asynchrone.

Voici un exemple d'utilisation de Redux-Observable :

```javascript
const fetchDataEpic = action$ => action$.pipe(
  ofType('FETCH_DATA_REQUEST'),
  mergeMap(() =>
    ajax.getJSON('https://api.example.com/data').pipe(
      map(response => ({ type: 'FETCH_DATA_SUCCESS', payload: response })),
      catchError(error => of({ type: 'FETCH_DATA_FAILURE', payload: error }))
    )
  )
);

```

#### Fetch API avec Async/Await

* Si vos opérations asynchrones sont relativement simples et que vous préférez garder vos dépendances minimales, vous pouvez utiliser l'API Fetch combinée avec la syntaxe async/await directement dans vos créateurs d'actions sans aucun middleware.
* Cette approche fonctionne bien pour des scénarios simples de récupération de données mais peut devenir difficile à gérer pour une logique asynchrone plus complexe.

Chacune de ces alternatives a ses propres forces et cas d'utilisation, alors choisissez celle qui correspond le mieux aux exigences de votre projet et à vos préférences de codage.

### 9.2. Quand Choisir Redux-Thunk

Redux-Thunk est un excellent choix pour gérer des actions asynchrones simples à modérément complexes dans les applications Redux. Il est léger, facile à comprendre et s'intègre de manière transparente avec les bases de code Redux existantes.

Envisagez d'utiliser Redux-Thunk pour :

#### Opérations Asynchrones

* Utilisez Redux-Thunk lorsque vous devez effectuer des opérations asynchrones comme la récupération de données depuis une API, la gestion des temporisateurs ou toute opération qui ne retourne pas immédiatement une valeur.

Voici un exemple de la manière dont Redux-Thunk gère une action asynchrone, comme la récupération de données :

```javascript
// Créateur d'action avec Redux-Thunk
const fetchData = () => {
  return (dispatch) => {
    dispatch({ type: 'FETCH_DATA_REQUEST' });

    fetch('https://api.example.com/data')
      .then(response => response.json())
      .then(data => dispatch({ type: 'FETCH_DATA_SUCCESS', payload: data }))
      .catch(error => dispatch({ type: 'FETCH_DATA_FAILURE', payload: error }));
  };
};

```

#### Fonctionnalité de Middleware

* Redux-Thunk est un middleware, ce qui signifie qu'il se situe entre le moment où une action est dispatchée et le moment où elle atteint le reducer. Cela permet des fonctionnalités supplémentaires comme la journalisation, la modification des actions ou la gestion des effets de bord.
* Si vous devez effectuer des actions avant ou après qu'une action soit dispatchée, Redux-Thunk est un bon choix.

#### Configuration Simple

* Redux-Thunk s'intègre de manière transparente avec Redux, nécessitant une configuration minimale. Il est facile à ajouter à un projet Redux existant.

Voici comment vous pouvez ajouter Redux-Thunk à votre store Redux :

```javascript
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './reducers';

const store = createStore(rootReducer, applyMiddleware(thunk));

```

#### Gestion de la Logique Complexe

* Si votre application implique une logique asynchrone complexe, telle que plusieurs appels API ou un dispatch conditionnel, Redux-Thunk fournit un moyen simple de gérer une telle complexité.
* Vous pouvez encapsuler une logique complexe au sein des créateurs d'actions thunk, gardant vos composants propres et concentrés sur la présentation.

#### Support Communautaire et Ressources

* Redux-Thunk est un middleware largement utilisé pour Redux, ce qui signifie qu'il existe de nombreuses ressources, tutoriels et supports communautaires disponibles.
* Si vous êtes nouveau dans Redux ou la récupération de données asynchrones dans Redux, choisir Redux-Thunk peut vous fournir une richesse de matériaux d'apprentissage et d'exemples.

Choisissez Redux-Thunk lorsque vous devez gérer des opérations asynchrones dans votre application Redux, souhaitez garder votre configuration simple, nécessitez une fonctionnalité de middleware, devez gérer une logique complexe ou bénéficiez du support communautaire et des ressources.

## 10. Conclusion

Redux-Thunk est un middleware puissant pour gérer les actions asynchrones dans les applications Redux. En vous permettant d'écrire des fonctions thunk qui encapsulent la logique asynchrone, Redux-Thunk simplifie le processus de gestion des effets de bord et de coordination des flux de travail complexes.

Que vous récupériez des données depuis une API, effectuiez des calculs en arrière-plan ou synchronisiez l'état à travers différentes parties de votre application, Redux-Thunk fournit une solution flexible et intuitive pour gérer les actions asynchrones dans Redux.

Dans ce guide complet, nous avons couvert tout ce que vous devez savoir sur Redux-Thunk, de l'installation et de la configuration aux techniques avancées et aux meilleures pratiques.

En suivant les principes décrits dans ce guide et en les appliquant à vos projets Redux, vous serez bien équipé pour gérer les actions asynchrones efficacement et construire des applications Redux robustes et maintenables.