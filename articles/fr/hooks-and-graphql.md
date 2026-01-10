---
title: Comment utiliser les hooks React avec l'API GraphQL pour gérer l'état
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2019-11-04T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/hooks-and-graphql
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9fa3740569d1a4ca43bf.jpg
tags:
- name: GraphQL
  slug: graphql
- name: react hooks
  slug: react-hooks
- name: React
  slug: reactjs
- name: 'State Management '
  slug: state-management
seo_title: Comment utiliser les hooks React avec l'API GraphQL pour gérer l'état
seo_desc: 'In this blog post, we are going to learn -


  What React hooks are

  How to use hooks for state management


  Before we start working with hooks, let us take a brief moment to talk about state
  management.

  State management is managing data that flows betwee...'
---

Dans cet article de blog, nous allons apprendre -

1. Ce que sont les hooks React
2. Comment utiliser les hooks pour la gestion d'état

Avant de commencer à travailler avec les hooks, prenons un bref moment pour parler de la gestion d'état.

**La gestion d'état** consiste à gérer les données qui circulent entre les composants de notre application. Il peut s'agir de données circulant à l'intérieur d'un seul composant (état local) ou de données circulant entre plusieurs composants (état partagé). Nous devons gérer l'état car parfois les composants doivent communiquer entre eux via une source d'information fiable. Dans Redux, cette source d'information fiable est appelée le store.

## Partie 1 : Les hooks React - le quoi et le pourquoi

### Qu'est-ce que les hooks ?

Les hooks sont des fonctions qui vous permettent d'accéder à l'état sans utiliser de composant de classe. Les hooks sont une manière plus naturelle de penser à React. Au lieu de penser aux méthodes de cycle de vie à utiliser, vous pouvez maintenant écrire des composants en pensant à la manière et au moment où vos données doivent être utilisées.

Les hooks React ont été introduits en octobre 2018 et publiés en février 2019. Ils sont maintenant disponibles avec React 16.8 et versions ultérieures. Les hooks React sont devenus très populaires dès leur introduction.

### Pourquoi les hooks React sont-ils si populaires ?

1. Pas de code boilerplate : Pour utiliser les hooks, vous n'avez pas besoin d'importer de nouvelles bibliothèques ou d'écrire du code boilerplate. Vous pouvez simplement commencer à utiliser les hooks directement dans React 16.8 et versions ultérieures. 
2. Pas besoin d'utiliser des composants de classe pour utiliser l'état : Traditionnellement, si vous utilisiez un composant fonctionnel et décidiez que ce composant avait besoin de l'état React, vous deviez le convertir en un composant de classe React. Avec l'ajout des hooks, vous pouvez utiliser l'état React à l'intérieur d'un composant fonctionnel.
3. Une manière plus logique de penser à React : Vous n'avez plus à penser à quand React monte un composant et à ce que vous devriez faire dans `componentDidMount` et à vous souvenir de le nettoyer dans `componentWillUnmount`. Maintenant, vous pouvez penser plus directement à la manière dont les données sont consommées par votre composant. React s'occupe de gérer les fonctions de montage et de nettoyage pour vous. 

### Quels sont les hooks courants ?

#### 1. useState

useState est utilisé pour définir et mettre à jour l'état comme `this.state` dans un composant de classe.

```javascript
const [ state, setState] = useState(initialState); 

```

#### 2. useEffect

useEffect est utilisé pour effectuer une fonction qui fait des effets de bord. Les effets de bord pourraient inclure des choses comme la manipulation du DOM, les abonnements et les appels d'API.

```javascript
useEffect(() => {
  document.title = 'Nouveau Titre' 
});


```

#### 3. useReducer

useReducer fonctionne de manière similaire à un reducer dans Redux. useReducer est utilisé lorsque l'état est plus complexe. Vous pouvez en fait utiliser useReducer pour tout ce que vous faites avec useState. Il donne une fonction dispatch en plus d'une variable d'état. 

```javascript
const [ state, dispatch ] = useReducer(reducer, initialArg, init);

```

#### 4. useContext

useContext est similaire à l'API de contexte. Dans l'API de contexte, il y a une méthode Provider et une méthode Consumer. De même, avec useContext, la méthode Provider la plus proche est utilisée pour lire les données.

```javascript
const value = useContext(MyContext);

```

Pour une explication plus détaillée de comment chacun de ces hooks fonctionne, lisez [la documentation officielle](https://reactjs.org/docs/hooks-reference.html#usestate).

## Partie 2 : Comment utiliser les hooks pour la gestion d'état

Avec React 16.8, vous pouvez utiliser les hooks directement.

Nous allons construire une application pour créer une liste de chansons. Voici ce qu'elle fera -

1. Récupérer une API GraphQL pour une liste de chansons et l'afficher sur l'interface utilisateur.
2. Avoir la possibilité d'ajouter une chanson à la liste.
3. Lorsque la chanson est ajoutée à la liste, mettre à jour la liste sur le frontend et stocker les données sur le backend.

Au fait, tout le code est disponible sur [mon GitHub](https://github.com/shrutikapoor08/hooks-graphql). Pour voir cela en action, vous pouvez aller sur [ce CodeSandbox](https://codesandbox.io/embed/github/shrutikapoor08/hooks-graphql/tree/master/). 

Nous allons utiliser l'API GraphQL avec cette application, mais vous pouvez également suivre les étapes suivantes avec une API REST. 

### Étape 0 : Idée principale

L'idée principale ici est que nous allons utiliser le `contexte` pour transmettre des données à nos composants. Nous allons utiliser les hooks, `useContext` et `useReducer`, pour lire et mettre à jour cet état. Nous allons utiliser `useState` pour stocker tout état local. Pour effectuer des effets de bord tels que l'appel d'une API, nous allons utiliser `useEffect`. 

Commençons ! 

### Étape 1 : Configurer le contexte

```javascript
import { createContext } from 'react';

const Context = createContext({
  songs: []
});

export default Context
```

### Étape 2 : Initialiser votre état. Appelez cela initialState

Nous allons utiliser ce contexte pour initialiser notre état :

```javascript
 const initialState = useContext(Context);   

```

### Étape 3 : Configurer les reducers en utilisant useReducer

Maintenant, nous allons configurer les reducers avec un initialState avec `useReducer` dans App.js :

```javascript
   const [ state, dispatch ] = useReducer(reducer, initialState);

```

### Étape 4 : Déterminer quel est le composant de niveau supérieur.

Nous devrons configurer un Context Provider ici. Pour notre exemple, ce sera `App.js`. De plus, passez le dispatch retourné par useReducer ici afin que les enfants puissent avoir accès à dispatch :

```javascript
  <Context.Provider value={{state, dispatch}}>
    // composants enfants
      <App />
  </Context.Provider>

```

### Étape 5 : Maintenant, connectez les API en utilisant le hook useEffect

```javascript
  const {state, dispatch} = useContext(Context);

  useEffect(() => {
      if(songs) {
          dispatch({type: "ADD_CONTENT", payload: songs});
      }
  }, [songs]);

```

### Étape 6 : Mettre à jour l'état

Vous pouvez utiliser `useContext` et `useReducer` pour recevoir et mettre à jour l'état global de l'application. Pour l'état local comme les composants de formulaire, vous pouvez utiliser `useState`.

```javascript
  const [artist, setArtist] = useState("");
  
  const [lyrics, setLyrics] = useState("");

```

Et c'est tout ! La gestion d'état est maintenant configurée.

Avez-vous appris quelque chose de nouveau ? Avez-vous quelque chose à partager ? Tweetez-moi sur Twitter.

%[https://twitter.com/shrutikapoor08/status/1189975126705504256?s=20]