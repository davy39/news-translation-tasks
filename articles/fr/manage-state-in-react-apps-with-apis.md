---
title: Comment gérer l'état dans les applications React avec des APIs – Exemples avec
  Redux, Context API et Recoil
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-01-23T00:18:52.000Z'
originalURL: https://freecodecamp.org/news/manage-state-in-react-apps-with-apis
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Ivory-and-Blue-Lavender-Aesthetic-Photo-Collage-Presentation--2-.png
tags:
- name: React
  slug: react
- name: 'State Management '
  slug: state-management
seo_title: Comment gérer l'état dans les applications React avec des APIs – Exemples
  avec Redux, Context API et Recoil
seo_desc: "State management is a crucial aspect of building robust and scalable React\
  \ applications, especially when dealing with APIs. \nAs your application grows in\
  \ complexity, efficiently managing the state becomes essential for a smooth user\
  \ experience. \nIn t..."
---

La gestion d'état est un aspect crucial pour construire des applications React robustes et évolutives, surtout lorsqu'il s'agit de travailler avec des APIs.

À mesure que votre application grandit en complexité, la gestion efficace de l'état devient essentielle pour une expérience utilisateur fluide.

Dans l'écosystème React, il existe plusieurs options pour la gestion d'état, chacune avec ses propres forces et faiblesses. Dans cet article, nous explorerons trois solutions populaires de gestion d'état : Redux, Context API et Recoil, et verrons comment elles gèrent l'état dans le contexte des interactions avec les APIs.

## Introduction à la gestion d'état

Avant de plonger dans les spécificités de chaque solution de gestion d'état, comprenons brièvement ce qu'est la gestion d'état et pourquoi elle est importante dans le développement React.

### Qu'est-ce que l'état ?

Dans React, l'état représente les données qui peuvent changer au fil du temps. C'est ce qui permet à un composant de suivre des informations et de se re-rendre lorsque ces informations changent. Par exemple, un composant bouton peut avoir un état pour suivre s'il a été cliqué ou non.

### Pourquoi gérer l'état ?

À mesure que les applications React grandissent, la gestion de l'état devient plus complexe. Passer l'état entre les composants via les props peut devenir fastidieux, et cela peut conduire au "prop drilling", où vous passez des données à travers de nombreuses couches de composants.

Les bibliothèques de gestion d'état visent à résoudre ce problème en fournissant un moyen centralisé de gérer et de partager l'état entre les composants.

## Redux : Gestion d'état éprouvée

Redux est une bibliothèque de gestion d'état populaire dans l'écosystème React depuis de nombreuses années. Elle est basée sur les principes d'un flux de données unidirectionnel et fournit une source unique de vérité pour l'état de l'application.

### Comment installer Redux

Pour utiliser Redux dans un projet React, vous devez installer les paquets `redux` et `react-redux`. Ouvrez votre terminal et exécutez la commande suivante :

```bash
npm install redux react-redux
```

Cette commande installe la bibliothèque principale Redux (`redux`) et les liaisons officielles React pour Redux (`react-redux`).

### Comment configurer Redux

Redux suit un flux de données unidirectionnel, ce qui signifie que les données dans une application circulent dans une seule direction, ce qui facilite la compréhension et la gestion. La configuration de Redux implique la création d'un store pour contenir l'état de l'application, la définition d'actions pour décrire les changements d'état et la mise en œuvre de reducers pour gérer ces changements.

#### Création d'un Store Redux

Un store Redux est un conteneur qui contient l'ensemble de l'arborescence d'état de votre application. Vous créez un store en passant une fonction reducer à la fonction `createStore` du paquet `redux`.

```jsx
// store.js
import { createStore } from 'redux';

// Reducer
const counterReducer = (state = { count: 0 }, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    case 'DECREMENT':
      return { count: state.count - 1 };
    default:
      return state;
  }
};

// Store
const store = createStore(counterReducer);

export default store;
```

Dans le code ci-dessus :

* Nous créons une fonction reducer (`counterReducer`) qui prend l'état actuel et une action, puis retourne le nouvel état en fonction du type d'action.
* Le store est créé en utilisant `createStore` et initialisé avec notre reducer.

#### Comment interagir avec le Store Redux dans un composant

Pour interagir avec le store Redux dans un composant React, nous utilisons les hooks `useSelector` et `useDispatch` fournis par `react-redux`.

```jsx
// CounterComponent.js
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';

const CounterComponent = () => {
  // Sélectionner le compteur depuis le store
  const count = useSelector((state) => state.count);

  // Obtenir la fonction dispatch
  const dispatch = useDispatch();

  return (
    <div>
      <p>Compteur : {count}</p>
      <button onClick={() => dispatch({ type: 'INCREMENT' })}>Incrémenter</button>
      <button onClick={() => dispatch({ type: 'DECREMENT' })}>Décrémenter</button>
    </div>
  );
};

export default CounterComponent;
```

Dans le `CounterComponent` :

* `useSelector` nous permet d'extraire des données du store Redux. Ici, nous extrayons le `count` de l'état.
* `useDispatch` fournit l'accès à la fonction `dispatch`, nous permettant de dispatcher des actions vers le store Redux.

### Avantages de Redux

* **Gestion d'état prévisible** : Redux impose un flux de données unidirectionnel strict, le rendant prévisible et facile à comprendre.
* **Outils de développement puissants pour le débogage** : Redux est livré avec des outils de développement puissants pour le navigateur qui permettent d'inspecter et de déboguer les changements d'état dans votre application.
* **Support des middlewares** : Redux supporte les middlewares, permettant de gérer les effets secondaires tels que les opérations asynchrones de manière propre et organisée.

### Inconvénients de Redux

* **Code boilerplate** : Redux nécessite souvent l'écriture de code boilerplate pour les actions et les reducers, ce qui peut être perçu comme répétitif.
* **Courbe d'apprentissage plus raide** : Pour les débutants, les concepts d'actions, de reducers et de middlewares peuvent présenter une courbe d'apprentissage plus raide par rapport à des solutions de gestion d'état plus simples.

Redux est une bibliothèque de gestion d'état éprouvée qui excelle dans la gestion d'états complexes dans les grandes applications. Bien qu'elle puisse introduire une certaine complexité initiale et du code boilerplate, ses avantages en termes de prévisibilité, d'outils de débogage et de support des middlewares en font un choix puissant pour des projets évolutifs.

Pour des projets plus petits, vous pourriez vouloir considérer les compromis avant d'opter pour Redux, car des alternatives plus simples comme Context API ou Recoil pourraient être plus adaptées.

## Context API : Simplicité avec une fonctionnalité intégrée à React

La Context API fait partie intégrante de React et fournit un moyen de transmettre des données à travers l'arborescence des composants sans avoir à passer manuellement des props à chaque niveau.

### Comment configurer la Context API

La Context API dans React permet de partager l'état entre les composants sans passer manuellement des props à chaque niveau de l'arborescence des composants. La configuration de la Context API implique la création d'un contexte et l'utilisation des composants `Provider` et `Consumer`.

#### Création d'un Contexte

Vous commencez par créer un contexte en utilisant la fonction `createContext`. Ce contexte contiendra l'état que vous souhaitez partager.

```jsx
// AppContext.js
import { createContext } from 'react';

const AppContext = createContext();

export default AppContext;
```

#### Fournir et Consommer le Contexte

Vous utilisez ensuite le composant `Provider` pour envelopper la partie de votre arborescence de composants qui a besoin d'accéder à l'état partagé. Le composant `Consumer` est utilisé dans les composants enfants pour accéder au contexte.

```jsx
// AppProvider.js
import React, { useReducer } from 'react';
import AppContext from './AppContext';

const initialState = { count: 0 };

const reducer = (state, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    case 'DECREMENT':
      return { count: state.count - 1 };
    default:
      return state;
  }
};

export const AppProvider = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <AppContext.Provider value={{ state, dispatch }}>
      {children}
    </AppContext.Provider>
  );
};
```

Dans cet exemple :

* Nous avons un reducer simple qui gère les changements d'état.
* Le composant `AppProvider` enveloppe ses enfants avec `AppContext.Provider`, rendant le contexte accessible à tous les descendants.
* La prop `value` dans `Provider` est définie sur un objet contenant l'état et une fonction dispatch.

#### Consommer le Contexte dans un Composant

Maintenant, tout composant à l'intérieur de `AppProvider` peut accéder à l'état partagé en utilisant le hook `useContext`.

```jsx
// CounterComponent.js
import React, { useContext } from 'react';
import AppContext from './AppContext';

const CounterComponent = () => {
  const { state, dispatch } = useContext(AppContext);

  return (
    <div>
      <p>Compteur : {state.count}</p>
      <button onClick={() => dispatch({ type: 'INCREMENT' })}>Incrémenter</button>
      <button onClick={() => dispatch({ type: 'DECREMENT' })}>Décrémenter</button>
    </div>
  );
};

export default CounterComponent;
```

### Avantages de la Context API

* **Simplicité et facilité d'utilisation** : La Context API fournit un moyen simple et direct de partager l'état entre les composants sans avoir besoin de configuration supplémentaire.
* **Pas besoin de bibliothèques supplémentaires** : La Context API est intégrée à React, éliminant le besoin de bibliothèques supplémentaires, réduisant ainsi les dépendances dans votre projet.
* **Intégrée à React** : Puisque la Context API fait partie de React, vous pouvez l'utiliser sans dépendances externes.

### Inconvénients de la Context API

* **Peut entraîner des re-rendus inutiles** : La Context API peut provoquer des re-rendus inutiles dans les composants qui consomment le contexte, surtout si la valeur du contexte change fréquemment. Cela est dû à l'absence de mécanismes d'optimisation comme la mémoisation.
* **Limitée aux cas d'utilisation plus simples** : Bien qu'adaptée à de nombreux scénarios, la Context API pourrait ne pas offrir le même niveau de contrôle et d'optimisation que des bibliothèques de gestion d'état dédiées comme Redux ou Recoil.

La Context API est une solution pratique pour partager l'état entre les composants, surtout dans les applications de petite à moyenne taille. Sa simplicité et sa nature intégrée la rendent facile à utiliser sans introduire de bibliothèques supplémentaires. Cependant, vous devez être conscient des problèmes potentiels de re-rendu et envisager des solutions alternatives de gestion d'état pour des cas d'utilisation plus complexes.

## Recoil : Une nouvelle approche de la gestion d'état

Recoil est une addition relativement nouvelle au paysage de la gestion d'état. Il est développé par Facebook et conçu pour être plus flexible et intuitif pour gérer l'état dans les applications React.

### Comment installer Recoil

Pour utiliser Recoil dans un projet React, vous devez installer le paquet `recoil`. Ouvrez votre terminal et exécutez la commande suivante :

```bash
npm install recoil
```

Cette commande installe la bibliothèque Recoil, qui est développée par Facebook et conçue pour la gestion d'état dans les applications React.

### Comment configurer Recoil

Recoil introduit le concept d'atomes pour représenter des morceaux d'état et de sélecteurs pour dériver des valeurs à partir de cet état.

#### Création d'atomes

Les atomes sont des unités d'état dans Recoil. Vous créez des atomes pour définir des morceaux individuels d'état que les composants peuvent lire et écrire.

```jsx
// atoms.js
import { atom } from 'recoil';

export const countState = atom({
  key: 'countState', // identifiant unique (par rapport aux autres atomes/sélecteurs)
  default: 0, // valeur par défaut (c'est-à-dire valeur initiale)
});
```

Dans cet exemple, nous avons créé un atome appelé `countState` avec une valeur initiale de `0`.

#### Utilisation des atomes dans les composants

Vous pouvez utiliser le hook `useRecoilState` pour lire et écrire dans les atomes de vos composants.

```jsx
// CounterComponent.js
import React from 'react';
import { useRecoilState } from 'recoil';
import { countState } from './atoms';

const CounterComponent = () => {
  const [count, setCount] = useRecoilState(countState);

  return (
    <div>
      <p>Compteur : {count}</p>
      <button onClick={() => setCount(count + 1)}>Incrémenter</button>
      <button onClick={() => setCount(count - 1)}>Décrémenter</button>
    </div>
  );
};

export default CounterComponent;
```

Dans le `CounterComponent`, `useRecoilState` est utilisé pour accéder à la valeur actuelle de `countState` et à la fonction `setCount` pour la mettre à jour.

#### Création de sélecteurs

Les sélecteurs sont des fonctions qui dérivent des valeurs à partir d'un ou plusieurs atomes ou autres sélecteurs. Ils permettent la composition d'états dérivés.

```jsx
// selectors.js
import { selector } from 'recoil';
import { countState } from './atoms';

export const doubledCount = selector({
  key: 'doubledCount',
  get: ({ get }) => {
    const count = get(countState);
    return count * 2;
  },
});
```

Dans cet exemple, nous avons créé un sélecteur appelé `doubledCount` qui double la valeur de `countState`.

#### Utilisation des sélecteurs dans les composants

Vous pouvez utiliser le hook `useRecoilValue` pour lire les valeurs des sélecteurs.

```jsx
// DoubledCounterComponent.js
import React from 'react';
import { useRecoilValue } from 'recoil';
import { doubledCount } from './selectors';

const DoubledCounterComponent = () => {
  const doubledValue = useRecoilValue(doubledCount);

  return (
    <div>
      <p>Compteur doublé : {doubledValue}</p>
    </div>
  );
};

export default DoubledCounterComponent;
```

### Avantages de Recoil

* **API intuitive avec un minimum de code boilerplate** : Recoil fournit une API simple, facilitant le travail avec l'état sans introduire beaucoup de code boilerplate.
* **Gère automatiquement la réactivité** : Recoil gère automatiquement la réactivité, garantissant que les composants se mettent à jour lorsque des morceaux pertinents de l'état changent.
* **Supporte des fonctionnalités avancées comme les sélecteurs** : Recoil supporte la création de sélecteurs, permettant de dériver des valeurs d'état complexes basées sur des atomes ou d'autres sélecteurs.

### Inconvénients de Recoil

* **Relativement nouveau, support communautaire limité** : Étant un nouvel entrant dans l'espace de la gestion d'état, Recoil pourrait ne pas avoir un support communautaire ou des paquets tiers aussi étendus que des bibliothèques plus établies comme Redux.

Recoil est une bibliothèque de gestion d'état prometteuse qui offre une API simple mais puissante pour gérer l'état dans les applications React. Elle excelle dans les projets qui privilégient la simplicité, la réactivité et la flexibilité.

Mais assurez-vous de considérer la maturité de la bibliothèque et les besoins spécifiques de vos projets lors du choix de Recoil par rapport à des alternatives plus établies comme Redux ou Context API. À mesure que Recoil évolue et gagne plus de support communautaire, il a le potentiel de devenir une solution de référence pour la gestion d'état dans les applications React.

## Gestion d'état avec les APIs

Maintenant que nous avons une compréhension de base de Redux, Context API et Recoil, explorons comment chacune de ces solutions gère l'état dans le contexte des interactions avec les APIs.

### Comment récupérer des données depuis une API en utilisant Redux

Considérons un scénario où nous devons récupérer des données depuis une API et les afficher dans notre application React. Nous utiliserons la bibliothèque `axios` pour faire des requêtes API.

Dans cet exemple, nous utilisons Redux pour gérer l'état des posts récupérés depuis une API.

#### `actions.js`

```jsx
// actions.js
import axios from 'axios';

// Créateur d'action pour récupérer les posts
export const fetchPosts = () => async (dispatch) => {
  try {
    // Faire une requête GET à l'API
    const response = await axios.get('https://jsonplaceholder.typicode.com/posts');

    // Dispatcher une action pour mettre à jour l'état avec les posts récupérés
    dispatch({ type: 'FETCH_POSTS', payload: response.data });
  } catch (error) {
    // Dispatcher une action en cas d'erreur
    dispatch({ type: 'FETCH_ERROR', payload: error.message });
  }
};
```

* Ce fichier contient une fonction créatrice d'action appelée `fetchPosts`.
* Le créateur d'action est une fonction asynchrone qui dispache des actions en fonction du résultat de la requête API.
* Nous utilisons `axios.get` pour faire une requête GET à l'endpoint API spécifié.
* Si la requête réussit, nous dispatchons une action de type `'FETCH_POSTS'` avec le payload étant les données reçues de l'API.
* Si une erreur survient pendant la requête, nous dispatchons une action de type `'FETCH_ERROR'` avec le message d'erreur.

#### `postsReducer.js`

```jsx
// postsReducer.js
const postsReducer = (state = { posts: [], error: null }, action) => {
  switch (action.type) {
    case 'FETCH_POSTS':
      // Mettre à jour l'état avec les posts récupérés et effacer toute erreur existante
      return { posts: action.payload, error: null };
    case 'FETCH_ERROR':
      // Mettre à jour l'état avec une erreur et un tableau vide de posts
      return { posts: [], error: action.payload };
    default:
      // Retourner l'état actuel si le type d'action ne correspond pas
      return state;
  }
};

export default postsReducer;
```

* Ce fichier contient une fonction reducer nommée `postsReducer`.
* Le reducer prend l'état actuel (qui a un tableau `posts` et une `error`) et une action.
* Dans le cas où le type d'action est `'FETCH_POSTS'`, il met à jour l'état avec les posts récupérés et efface toute erreur existante.
* Dans le cas de `'FETCH_ERROR'`, il met à jour l'état avec un message d'erreur et définit le tableau `posts` sur un tableau vide.
* Si le type d'action ne correspond à aucun des cas, il retourne l'état actuel inchangé.

#### Comment cela fonctionne

**Créateur d'action (`fetchPosts`) :**

* Le créateur d'action `fetchPosts` est appelé lorsque vous souhaitez initier le processus de récupération des posts.
* Il fait une requête API asynchrone en utilisant `axios.get`.
* Si la requête réussit, il dispache une action de type `'FETCH_POSTS'` avec les données récupérées comme payload.
* Si une erreur survient, il dispache une action de type `'FETCH_ERROR'` avec le message d'erreur.

**Reducer (`postsReducer`) :**

* Le `postsReducer` gère les actions dispatchées.
* Lorsqu'il reçoit une action de type `'FETCH_POSTS'`, il met à jour l'état avec les posts récupérés et efface toute erreur existante.
* Lorsqu'il reçoit une action de type `'FETCH_ERROR'`, il met à jour l'état avec un message d'erreur et définit le tableau `posts` sur un tableau vide.
* Si le type d'action ne correspond à aucun des cas, il retourne l'état actuel inchangé.

Dans l'architecture Redux, les actions sont dispatchées vers les reducers, qui mettent ensuite à jour l'état de l'application. Cet exemple démontre comment Redux peut être utilisé pour gérer les changements d'état lors de la récupération de données depuis une API. L'état est mis à jour de manière prévisible, facilitant la gestion de différents scénarios au sein de l'application.

### Comment récupérer des données depuis une API en utilisant la Context API

Dans ce scénario, la Context API est utilisée pour gérer l'état des posts récupérés depuis une API et les rendre accessibles aux composants dans toute l'application React.

#### `AppContext.js`

```jsx
// AppContext.js
import { createContext, useContext, useReducer, useEffect } from 'react';
import axios from 'axios';

// Création d'un Contexte
const AppContext = createContext();

// État initial pour le contexte
const initialState = { posts: [], error: null };

// Fonction reducer pour gérer les changements d'état
const reducer = (state, action) => {
  switch (action.type) {
    case 'FETCH_POSTS':
      // Mettre à jour l'état avec les posts récupérés et effacer toute erreur existante
      return { posts: action.payload, error: null };
    case 'FETCH_ERROR':
      // Mettre à jour l'état avec une erreur et un tableau vide de posts
      return { posts: [], error: action.payload };
    default:
      // Retourner l'état actuel si le type d'action ne correspond pas
      return state;
  }
};

// Composant Fournisseur de Contexte
export const AppProvider = ({ children }) => {
  // Hook useReducer pour gérer l'état et dispatcher des actions
  const [state, dispatch] = useReducer(reducer, initialState);

  // Hook useEffect pour récupérer les données lorsque le composant est monté
  useEffect(() => {
    const fetchData = async () => {
      try {
        // Faire une requête GET à l'API
        const response = await axios.get('https://jsonplaceholder.typicode.com/posts');

        // Dispatcher une action pour mettre à jour l'état du contexte avec les posts récupérés
        dispatch({ type: 'FETCH_POSTS', payload: response.data });
      } catch (error) {
        // Dispatcher une action en cas d'erreur
        dispatch({ type: 'FETCH_ERROR', payload: error.message });
      }
    };

    // Récupérer les données lorsque le composant est monté
    fetchData();
  }, []); // Tableau de dépendances vide pour exécuter l'effet une seule fois lorsque le composant est monté

  // Fournir la valeur du contexte à ses descendants
  return (
    <AppContext.Provider value={{ state, dispatch }}>
      {children}
    </AppContext.Provider>
  );
};

// Hook personnalisé pour consommer facilement le contexte
export const useAppContext = () => {
  return useContext(AppContext);
};
```

**Création d'un Contexte :**

* `createContext` est utilisé pour créer le AppContext, qui sert de conteneur pour l'état à partager entre les composants.

**État initial et Reducer :**

* L'objet `initialState` représente l'état initial du contexte, incluant un tableau vide de posts et aucune erreur.
* La fonction `reducer` gère les changements d'état en fonction des actions dispatchées. Elle met à jour l'état en fonction du type d'action.

**Fournisseur de Contexte (`AppProvider`) :**

* Le hook `useReducer` est utilisé pour gérer l'état et dispatcher des actions.
* Le hook `useEffect` est employé pour récupérer les données lorsque le composant est monté (`[]` comme tableau de dépendances garantit qu'il ne s'exécute qu'une seule fois).
* À l'intérieur de `fetchData`, Axios est utilisé pour faire une requête GET à l'endpoint API spécifié.
* En fonction de la réussite ou de l'échec de la requête, le reducer dispache des actions pour mettre à jour l'état du contexte.

**Consommateur de Contexte (`useAppContext`) :**

* Le hook personnalisé `useAppContext` utilise `useContext` pour consommer facilement la valeur du contexte au sein des composants.

#### Comment il est utilisé dans les composants :

Les composants à l'intérieur de `AppProvider` peuvent utiliser le hook `useAppContext` pour accéder à l'état partagé et dispatcher des actions :

```jsx
// ExampleComponent.js
import React from 'react';
import { useAppContext } from './AppContext';

const ExampleComponent = () => {
  // Utilisation du hook personnalisé pour accéder au contexte
  const { state, dispatch } = useAppContext();

  return (
    <div>
      <h2>Posts</h2>
      {state.posts.map((post) => (
        <div key={post.id}>
          <h3>{post.title}</h3>
          <p>{post.body}</p>
        </div>
      ))}
      {state.error && <p>Erreur : {state.error}</p>}
    </div>
  );
};

export default ExampleComponent;
```

* `useAppContext` est utilisé pour consommer le contexte au sein du `ExampleComponent`.
* Le composant rend une liste de posts si disponible et affiche un message d'erreur s'il y a une erreur lors de la récupération des données.

La Context API, associée à l'utilisation des hooks `useReducer` et `useEffect`, permet de gérer et de partager l'état entre les composants. Le `AppProvider` configure le contexte, récupère les données de l'API et met à jour l'état du contexte en fonction des résultats. Les composants à l'intérieur du fournisseur peuvent ensuite utiliser le hook `useAppContext` pour accéder à l'état partagé et dispatcher des actions selon les besoins.

### Comment récupérer des données depuis une API en utilisant Recoil

Dans ce scénario, Recoil est utilisé pour gérer l'état des posts récupérés depuis une API et les rendre accessibles aux composants dans toute l'application React.

#### `atoms.js`

```jsx
// atoms.js
import { atom, selector } from 'recoil';
import axios from 'axios';

// Atome pour l'état des posts
export const postsState = atom({
  key: 'postsState',
  default: selector({
    key: 'postsState/default',
    get: async () => {
      try {
        // Faire une requête GET à l'API pour récupérer les posts
        const response = await axios.get('https://jsonplaceholder.typicode.com/posts');
        return response.data;
      } catch (error) {
        // Lancer une erreur si la requête API échoue
        throw error;
      }
    },
  }),
});
```

* L'atome `postsState` est créé en utilisant la fonction `atom` de Recoil.
* Il a une valeur par défaut définie par un `selector` qui fait un appel API asynchrone en utilisant `axios.get`.
* Si l'appel API réussit, les données récupérées sont retournées. Si une erreur se produit pendant l'appel API, elle est lancée.

#### `PostsComponent.js`

```jsx
// PostsComponent.js
import React from 'react';
import { useRecoilValue } from 'recoil';
import { postsState } from './atoms';

const PostsComponent = () => {
  // Utilisation du hook useRecoilValue pour accéder à l'atome postsState
  const posts = useRecoilValue(postsState);

  return (
    <div>
      <h2>Posts</h2>
      {posts.map((post) => (
        <div key={post.id}>
          <h3>{post.title}</h3>
          <p>{post.body}</p>
        </div>
      ))}
    </div>
  );
};

export default PostsComponent;
```

* Le `PostsComponent` utilise le hook `useRecoilValue` pour accéder à la valeur de l'atome `postsState`.
* Il rend ensuite la liste des posts, en parcourant le tableau et en affichant le titre et le corps de chaque post.

#### Comment il est utilisé dans les composants :

Les composants à l'intérieur de RecoilRoot peuvent utiliser les hooks Recoil pour lire et écrire dans les atomes. Dans ce cas, `useRecoilValue` est utilisé pour lire la valeur de l'atome `postsState`.

```jsx
// Exemple d'utilisation de PostsComponent dans un RecoilRoot
import React from 'react';
import { RecoilRoot } from 'recoil';
import PostsComponent from './PostsComponent';

const App = () => {
  return (
    <RecoilRoot>
      <div>
        <h1>Mon Application React</h1>
        <PostsComponent />
      </div>
    </RecoilRoot>
  );
};

export default App;
```

* Le `PostsComponent` est utilisé à l'intérieur d'un `RecoilRoot`, qui est un fournisseur de contexte pour Recoil.
* Cela garantit que les composants à l'intérieur du `RecoilRoot` peuvent accéder à l'état Recoil et utiliser les hooks Recoil.

Recoil simplifie la gestion d'état dans une application React. Dans cet exemple, l'atome `postsState` est utilisé pour gérer l'état des posts récupérés depuis une API. Le hook `useRecoilValue` permet aux composants de lire efficacement la valeur de l'atome et d'afficher les données dans l'interface utilisateur. La structure fournie par Recoil permet une manière propre et centralisée de gérer et de partager l'état entre les composants.

### Comment mettre à jour des données via une API en utilisant Redux

Maintenant, explorons comment chaque solution de gestion d'état gère la mise à jour des données via des requêtes API. Commençons par Redux.

#### `actions.js`

```jsx
// actions.js
export const updatePost = (postId, updatedData) => async (dispatch) => {
  try {
    // Faire une requête PATCH pour mettre à jour un post spécifique par son ID
    const response = await axios.patch(`https://jsonplaceholder.typicode.com/posts/${postId}`, updatedData);

    // Dispatcher une action pour mettre à jour l'état avec le post mis à jour
    dispatch({ type: 'UPDATE_POST', payload: response.data });
  } catch (error) {
    // Dispatcher une action en cas d'erreur
    dispatch({ type: 'FETCH_ERROR', payload: error.message });
  }
};
```

* Le créateur d'action `updatePost` est défini pour gérer la mise à jour d'un post en faisant une requête `PATCH` à l'API.
* Il prend deux paramètres : `postId` (l'ID du post à mettre à jour) et `updatedData` (les nouvelles données pour le post).
* En cas de requête réussie, il dispache une action de type `'UPDATE_POST'` avec les données du post mis à jour.
* Si une erreur survient pendant la requête API, il dispache une action de type `'FETCH_ERROR'` avec le message d'erreur.

#### `postsReducer.js`

```jsx
// postsReducer.js
const postsReducer = (state = { posts: [], error: null }, action) => {
  switch (action.type) {
    case 'UPDATE_POST':
      // Mettre à jour l'état avec le post mis à jour
      const updatedPosts = state.posts.map((post) =>
        post.id === action.payload.id ? action.payload : post
      );
      return { posts: updatedPosts, error: null };
    // Autres cas...
    default:
      // Retourner l'état actuel si le type d'action ne correspond pas
      return state;
  }
};
```

* Dans le `postsReducer`, un cas `'UPDATE_POST'` est ajouté pour gérer l'action de mise à jour.
* L'état est mis à jour en parcourant les posts existants et en remplaçant celui avec l'ID correspondant par le post mis à jour.
* Cela garantit que l'état est correctement mis à jour avec les nouvelles données.

Pour utiliser cette fonctionnalité dans un composant React, vous dispachez l'action `updatePost`, en fournissant l'ID du post et les données mises à jour. Par exemple :

```jsx
// Exemple d'utilisation de updatePost dans un composant React
import React from 'react';
import { useDispatch } from 'react-redux';
import { updatePost } from './actions';

const UpdatePostComponent = () => {
  const dispatch = useDispatch();

  const handleUpdatePost = () => {
    // Exemple : Mise à jour du post avec l'ID 1 et fourniture de nouvelles données
    dispatch(updatePost(1, { title: 'Titre Mis à Jour', body: 'Corps Mis à Jour' }));
  };

  return (
    <div>
      <h2>Mettre à jour le Post</h2>
      <button onClick={handleUpdatePost}>Mettre à jour le Post</button>
    </div>
  );
};

export default UpdatePostComponent;
```

* Le composant utilise le hook `useDispatch` pour obtenir la fonction `dispatch`.
* Il définit une fonction `handleUpdatePost` qui dispache l'action `updatePost` avec l'ID du post (1 dans cet exemple) et les données mises à jour.
* Cette fonction pourrait être déclenchée par un clic sur un bouton ou toute autre action de l'utilisateur.

Cette configuration Redux permet une manière propre et centralisée de gérer la mise à jour des données via des requêtes API. Le créateur d'action (`updatePost`) est responsable de la requête API, et le reducer (`postsReducer`) garantit que l'état est correctement mis à jour en fonction des données reçues. Les composants peuvent utiliser le hook `useDispatch` pour initier ces mises à jour depuis l'UI.

### Comment mettre à jour des données via une API en utilisant la Context API

#### `AppContext.js`

```jsx
// AppContext.js
export const AppProvider = ({ children }) => {
  // Hook useReducer pour gérer l'état et dispatcher des actions
  const [state, dispatch] = useReducer(reducer, initialState);

  // Fonction pour mettre à jour un post via une API
  const updatePost = async (postId, updatedData) => {
    try {
      // Faire une requête PATCH pour mettre à jour un post spécifique par son ID
      const response = await axios.patch(`https://jsonplaceholder.typicode.com/posts/${postId}`, updatedData);

      // Dispatcher une action pour mettre à jour l'état du contexte avec le post mis à jour
      dispatch({ type: 'UPDATE_POST', payload: response.data });
    } catch (error) {
      // Dispatcher une action en cas d'erreur
      dispatch({ type: 'FETCH_ERROR', payload: error.message });
    }
  };

  // Fournir la valeur du contexte avec l'état, le dispatch et la fonction updatePost
  return (
    <AppContext.Provider value={{ state, dispatch, updatePost }}>
      {children}
    </AppContext.Provider>
  );
};
```

* La fonction `updatePost` est ajoutée au contexte, qui fait une requête `PATCH` pour mettre à jour un post spécifique par son ID.
* Si la requête réussit, elle dispache une action de type `'UPDATE_POST'` avec les données du post mis à jour.
* En cas d'erreur pendant la requête API, elle dispache une action de type `'FETCH_ERROR'` avec le message d'erreur.
* La fonction `updatePost` est ensuite fournie dans la valeur du contexte avec l'état et le dispatch.

#### Comment il est utilisé dans les composants :

Les composants à l'intérieur de `AppProvider` peuvent utiliser le hook `useContext` pour accéder à l'état partagé, au dispatch et à la fonction `updatePost`.

```jsx
// Exemple d'utilisation de AppContext dans un composant
import React, { useContext } from 'react';
import { AppContext } from './AppContext';

const UpdatePostComponent = () => {
  // Utilisation du hook useContext pour accéder à la valeur du contexte
  const { updatePost } = useContext(AppContext);

  const handleUpdatePost = async () => {
    try {
      // Exemple : Mise à jour du post avec l'ID 1 et fourniture de nouvelles données
      await updatePost(1, { title: 'Titre Mis à Jour', body: 'Corps Mis à Jour' });
    } catch (error) {
      // Gérer l'erreur si nécessaire
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Mettre à jour le Post</h2>
      <button onClick={handleUpdatePost}>Mettre à jour le Post</button>
    </div>
  );
};

export default UpdatePostComponent;
```

* Le `UpdatePostComponent` utilise le hook `useContext` pour accéder au `AppContext`.
* Il extrait la fonction `updatePost` de la valeur du contexte.
* Le composant définit une fonction `handleUpdatePost` qui appelle `updatePost` avec l'ID du post (1 dans cet exemple) et les données mises à jour.
* Cette fonction pourrait être déclenchée par un clic sur un bouton ou toute autre action de l'utilisateur.

La Context API, associée à l'utilisation des hooks `useReducer` et `useContext`, fournit un moyen de gérer et de partager l'état entre les composants. Le `AppProvider` configure le contexte, y compris la capacité de mettre à jour les données via des requêtes API. Les composants à l'intérieur du fournisseur peuvent utiliser le hook `useContext` pour accéder à l'état partagé, au dispatch et à la fonction `updatePost`, permettant une manière centralisée de gérer les mises à jour dans l'application.

### Comment mettre à jour des données via une API en utilisant Recoil

#### `atoms.js`

```jsx
// atoms.js
export const postState = atomFamily({
  key: 'postState',
  default: (postId) => selector({
    key: `postState/${postId}`,
    get: async () => {
      try {
        // Faire une requête GET pour récupérer un post spécifique par son ID
        const response = await axios.get(`https://jsonplaceholder.typicode.com/posts/${postId}`);
        return response.data;
      } catch (error) {
        // Lancer une erreur si la requête API échoue
        throw error;
      }
    },
  }),
});
```

* Le `postState` est défini comme un `atomFamily`, qui permet la création d'atomes séparés pour chaque post en fonction de son ID.
* Chaque atome est un `selector` avec une fonction `get` qui fait une requête `GET` pour récupérer un post spécifique par son ID.
* Si la requête réussit, elle retourne les données du post. Si une erreur survient, elle lance une erreur.

#### `EditPostComponent.js`

```jsx
// EditPostComponent.js
import React, { useState } from 'react';
import { useRecoilState, useRecoilValue } from 'recoil';
import { postState } from './atoms';

const EditPostComponent = ({ postId }) => {
  // Utilisation de useRecoilValue pour obtenir les données du post
  const post = useRecoilValue(postState(postId));

  // Utilisation de useRecoilState pour obtenir et définir l'état du post
  const [updatedTitle, setUpdatedTitle] = useState(post.title);
  const [updatedBody, setUpdatedBody] = useState(post.body);

  const handleUpdate = async () => {
    try {
      // Effectuer une requête PATCH pour mettre à jour le post spécifique par son ID
      // avec le titre et le corps mis à jour
      // Note : Le code de la requête API est manquant dans l'exemple fourni
      // Vous devez implémenter la logique de la requête API ici
      console.log(`Mise à jour du post ${postId} avec le titre : ${updatedTitle}, corps : ${updatedBody}`);
    } catch (error) {
      // Gérer l'erreur si nécessaire
      console.error(error);
    }
  };

  return (
    <div>
      <input type="text" value={updatedTitle} onChange={(e) => setUpdatedTitle(e.target.value)} />
      <textarea value={updatedBody} onChange={(e) => setUpdatedBody(e.target.value)} />
      <button onClick={handleUpdate}>Mettre à jour le Post</button>
    </div>
  );
};

export default EditPostComponent;
```

* Le `EditPostComponent` utilise `useRecoilValue` pour obtenir l'état actuel du post spécifique.
* Il utilise `useRecoilState` pour obtenir et définir l'état local pour le titre et le corps mis à jour.
* Le composant rend des champs de saisie pour le titre et le corps, permettant aux utilisateurs de saisir les valeurs mises à jour.
* La fonction `handleUpdate` est appelée lorsque le bouton "Mettre à jour le Post" est cliqué. Elle doit effectuer une requête `PATCH` pour mettre à jour le post spécifique avec le nouveau titre et le nouveau corps. La logique de la requête API est manquante dans l'exemple fourni et doit être implémentée selon l'endpoint API.

#### Comment il est utilisé dans les composants :

Pour utiliser le `EditPostComponent` dans un RecoilRoot, vous le rendez dans un composant qui est enveloppé avec `RecoilRoot`.

```jsx
// Exemple d'utilisation de EditPostComponent dans un RecoilRoot
import React from 'react';
import { RecoilRoot } from 'recoil';
import EditPostComponent from './EditPostComponent';

const App = () => {
  return (
    <RecoilRoot>
      <div>
        <h1>Mon Application Recoil</h1>
        <EditPostComponent postId={1} />
      </div>
    </RecoilRoot>
  );
};

export default App;
```

* Le `EditPostComponent` est utilisé dans un `RecoilRoot`, qui est un fournisseur de contexte pour Recoil.
* Cela garantit que les composants dans le `RecoilRoot` peuvent accéder à l'état Recoil et utiliser les hooks Recoil.

Recoil's `atomFamily` est utilisé pour gérer l'état des posts individuels, et le `EditPostComponent` démontre comment utiliser les hooks Recoil pour gérer la mise à jour des données via des requêtes API pour un post spécifique. Le `EditPostComponent` permet aux utilisateurs de saisir de nouvelles valeurs pour le titre et le corps, et la fonction `handleUpdate` doit être étendue pour inclure la logique réelle de la requête API afin de mettre à jour le post spécifique.

## Conclusion

Dans cet article, nous avons exploré trois solutions populaires de gestion d'état pour les applications React : Redux, Context API et Recoil. Chacune a ses propres forces et faiblesses, et le choix entre elles dépend des besoins spécifiques et de la complexité de votre projet.

**Redux :** Une solution éprouvée avec une approche de gestion d'état prévisible. Elle excelle dans la gestion d'états complexes dans les grandes applications, mais vient avec une courbe d'apprentissage plus raide et du code boilerplate.

**Context API :** Une fonctionnalité intégrée à React qui offre simplicité et facilité d'utilisation. Elle est adaptée aux projets plus petits ou lorsque la complexité de Redux pourrait être excessive.

**Recoil :** Une addition relativement nouvelle avec une API intuitive et flexible. Recoil est un excellent choix pour les projets qui privilégient la simplicité et la réactivité sans sacrifier les fonctionnalités avancées.

En ce qui concerne la gestion de l'état dans le contexte des interactions avec les APIs, les trois solutions peuvent être utilisées efficacement. Redux avec son support des middlewares, Context API avec sa simplicité, et Recoil avec ses fonctionnalités de réactivité offrent toutes des moyens de gérer l'état tout en interagissant avec les APIs. La clé est de choisir celle qui correspond aux exigences de votre projet et à la familiarité de votre équipe avec la solution choisie.

N'oubliez pas que les exemples fournis dans cet article sont simplifiés, et dans les applications réelles, des considérations supplémentaires telles que la gestion des erreurs, les états de chargement et les stratégies d'optimisation doivent être prises en compte.

En conclusion, la gestion d'état est un aspect crucial de la construction d'applications React, et comprendre les forces et les compromis de Redux, Context API et Recoil vous permettra de prendre des décisions éclairées en fonction des besoins de votre projet.

À mesure que l'écosystème React continue d'évoluer, rester à jour sur les meilleures pratiques et explorer de nouvelles solutions contribuera à construire des applications plus maintenables et évolutives.