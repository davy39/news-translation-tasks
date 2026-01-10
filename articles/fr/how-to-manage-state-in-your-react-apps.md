---
title: Comment gérer l'état dans vos applications React
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-02-18T20:55:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-state-in-your-react-apps
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/how-to-manage-state-react.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'State Management '
  slug: state-management
seo_title: Comment gérer l'état dans vos applications React
seo_desc: 'Managing state in your React apps isn’t as simple as using useState or
  useReducer.

  Not only are there are a lot of different kinds of state, but there often dozens
  of ways of managing each kind. Which should you choose?

  In this guide, we will uncover...'
---

Gérer l'état dans vos applications React n'est pas aussi simple que d'utiliser `useState` ou `useReducer`.

Non seulement il existe de nombreux types d'états différents, mais il y a souvent des dizaines de façons de gérer chaque type. Lequel choisir ?

Dans ce guide, nous allons découvrir les plusieurs types d'états dans vos applications React dont vous n'êtes peut-être pas conscient, ainsi que la manière de les gérer de la manière la plus efficace.

## Les quatre types d'états React à gérer

Lorsque nous parlons d'état dans nos applications, il est important d'être clair sur les types d'états qui comptent vraiment.

Il existe quatre principaux types d'états que vous devez gérer correctement dans vos applications React :

1. État local
2. État global
3. État serveur
4. État URL

Examinons chacun de ces types en détail :

**État local (UI)** – L'état local est une donnée que nous gérons dans un composant ou un autre.

L'état local est le plus souvent géré dans React à l'aide du hook `useState`.

Par exemple, l'état local serait nécessaire pour afficher ou masquer un composant modal ou pour suivre les valeurs d'un composant de formulaire, comme la soumission du formulaire, lorsque le formulaire est désactivé et les valeurs des entrées du formulaire.

**État global (UI)** – L'état global est une donnée que nous gérons à travers plusieurs composants.

L'état global est nécessaire lorsque nous voulons obtenir et mettre à jour des données n'importe où dans notre application, ou dans plusieurs composants au moins.

Un exemple courant d'état global est l'état de l'utilisateur authentifié. Si un utilisateur est connecté à notre application, il est nécessaire d'obtenir et de modifier ses données dans toute notre application.

Parfois, un état que nous pensons être local peut devenir global.

**État serveur** – Données provenant d'un serveur externe qui doivent être intégrées à notre état UI.

L'état serveur est un concept simple, mais peut être difficile à gérer parallèlement à tous nos états UI locaux et globaux.

Il existe plusieurs éléments d'état qui doivent être gérés chaque fois que vous récupérez ou mettez à jour des données depuis un serveur externe, y compris les états de chargement et d'erreur.

Heureusement, il existe des outils tels que SWR et React Query qui facilitent grandement la gestion de l'état serveur.

**État URL** – Données qui existent sur nos URLs, y compris le chemin et les paramètres de requête.

L'état URL est souvent omis comme catégorie d'état, mais c'est une catégorie importante. Dans de nombreux cas, de nombreuses parties majeures de notre application dépendent de l'accès à l'état URL. Essayez d'imaginer la construction d'un blog sans pouvoir récupérer un article basé sur son slug ou son id situé dans l'URL !

Il existe sans aucun doute plus d'éléments d'état que nous pourrions identifier, mais ce sont les principales catégories sur lesquelles il vaut la peine de se concentrer pour la plupart des applications que vous construisez.

## Comment gérer l'état local dans React

L'état local est peut-être le type d'état le plus facile à gérer dans React, étant donné qu'il existe tant d'outils intégrés dans la bibliothèque principale de React pour le gérer.

`useState` est le premier outil auquel vous devriez recourir pour gérer l'état dans vos composants.

Il peut accepter n'importe quelle valeur de données valide, y compris les valeurs primitives et les objets. De plus, sa fonction de définition peut être transmise à d'autres composants en tant que fonction de rappel (sans avoir besoin d'optimisations comme `useCallback`).

```javascript
import { useState } from "react";

function Layout() {
  const [isSidebarOpen, setSidebarOpen] = useState(false);

  return (
    <>
      <Sidebar isSidebarOpen={isSidebarOpen} closeSidebar={() => setSidebarOpen(false)} />
      {/* ... */}
    </>
  );
}

```

`useReducer` est une autre option qui peut être utilisée pour l'état local ou global. Il est similaire à bien des égards à `useState` sous le capot, bien qu'au lieu de simplement un état initial, il accepte un réducteur.

L'avantage de `useReducer` est qu'il fournit un moyen intégré d'effectuer un certain nombre d'opérations d'état différentes avec l'aide de la fonction de réducteur, ce qui le rend plus dynamique globalement que `useState`.

Vous pouvez voir l'avantage de `useReducer` par rapport à `useState` dans cet exemple de suivi de votes. Tout ce que nous avons à faire pour mettre à jour l'état est de passer à la fonction de rappel `dispatch` une chaîne (qui est ensuite passée au réducteur) au lieu du nouvel état lui-même.

```javascript
const initialState = { votes: 0 };

function reducer(state, action) {
  switch (action.type) {
    case 'upvote':
      return {votes: state.votes + 1};
    case 'downvote':
      return {votes: state.votes - 1};
    default:
      throw new Error();
  }
}

function VoteCounter() {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <>
      Current Votes: {state.votes}
      <button onClick={() => dispatch({type: 'upvote'})}>Upvote</button>
      <button onClick={() => dispatch({type: 'downvote'})}>Downvote</button>
    </>
  );
}

```

## Comment gérer l'état global dans React

Une fois que vous essayez de gérer l'état à travers plusieurs composants, les choses deviennent un peu plus compliquées.

Vous atteindrez un point dans votre application où des motifs comme "remonter l'état" et passer des rappels pour mettre à jour votre état depuis des composants entraînent de nombreuses et nombreuses props.

Que faites-vous si vous voulez mettre à jour l'état d'un composant depuis pratiquement n'importe où dans votre application ? Vous le transformez en état global.

Pour le gérer, cependant, vous devriez opter pour une solution tierce. De nombreux développeurs sont enclins à utiliser des fonctionnalités intégrées de React comme l'API Context pour gérer leur état.

> Pour être clair : l'API Context n'est pas une solution de gestion d'état. C'est un moyen d'éviter des problèmes comme le perçage de props (créer un tas de props dans des composants qui n'en ont pas besoin), mais elle n'est utile que pour lire l'état, pas pour le mettre à jour.

La raison de ne pas utiliser Context pour la gestion de l'état global réside dans son fonctionnement. Le comportement par défaut de Context est de re-rendre tous les composants enfants si la valeur fournie en tant que prop change.

Par exemple, il est mauvaise pratique de combiner `useReducer` et `useContext` :

```javascript
function App() {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <StateProvider.Provider value={{ state, dispatch }}>
      <ComponentA />
      <ComponentB />
      <ComponentC />
    </StateProvider.Provider>
  )
}

```

Dans de nombreux cas, vous ne voulez pas que tous les enfants se mettent à jour en réponse à une mise à jour de l'état global, car tous les enfants ne consomment pas ou ne dépendent pas de cet état global. Vous ne voulez re-rendre que si leurs props ou leur état change.

> Pour gérer votre état global, utilisez des bibliothèques tierces éprouvées comme **Zustand**, **Jotai** et **Recoil**.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/zustand-jotai-redux-toolkit.jpg)
_Bibliothèques Zustand, Jotai et Redux Toolkit_

Redux est également excellent, mais assurez-vous de commencer à utiliser Redux Toolkit.

L'avantage d'une bibliothèque comme Zustand est qu'elle est petite, fait de tout votre état global un hook personnalisé, et pour lire ou mettre à jour l'état, vous appelez simplement ce hook dans vos composants.

Pour utiliser Zustand, exécutez `npm install zustand`. Après cela, créez un fichier ou un dossier dédié pour votre store et créez votre store :

```javascript
import create from 'zustand'

const useStore = create(set => ({
  votes: 0,
  upvote: () => set(state => ({ vote: state.votes + 1 })),
  downvote: () => set(state => ({ vote: state.votes - 1 })),
}))

function VoteCounter() {
  const { votes, upvote, downvote } = useStore();

  return (
    <>
      Current Votes: {votes}
      <button onClick={upvote}>Upvote</button>
      <button onClick={downvote}>Downvote</button>
    </>
  );
}

```

Une grande raison pour laquelle je recommande d'utiliser Zustand plutôt qu'une bibliothèque comme Redux est qu'il vous offre toutes les fonctionnalités dont vous avez besoin sans le code standard et la surcharge conceptuelle des actions, des réducteurs, etc.

De plus, vous n'avez pas besoin d'envelopper vos composants dans un Context Provider. Il suffit d'installer et de commencer !

## Comment gérer l'état serveur dans React

L'état serveur peut être trompeusement difficile à gérer.

Au début, il semble que vous devez simplement récupérer des données et les afficher dans la page. Mais ensuite, vous devez afficher un indicateur de chargement pendant que vous attendez les données. Ensuite, vous devez gérer les erreurs et les afficher à l'utilisateur au fur et à mesure qu'elles surviennent.

Que se passe-t-il en cas d'erreur réseau ? Dois-je vraiment interroger mon serveur chaque fois que mon utilisateur visite la page d'accueil si les données n'ont pas changé ? Dois-je ajouter `useState` et `useEffect` dans chaque composant où je veux récupérer mes données ?

Pour résoudre cela, il existe quelques excellentes bibliothèques qui rendent la récupération de données dans React très facile : **SWR** et **React Query**.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/swr-react-query.jpg)
_Bibliothèques SWR et React Query_

Non seulement elles nous offrent un hook pratique pour obtenir et modifier des données depuis une API, mais elles gardent également une trace de tous les états nécessaires et mettent en cache les données pour nous.

Voici un exemple de récupération du profil d'un utilisateur depuis une API sur le client. Nous appelons `useSWR` et spécifions le point de terminaison à partir duquel demander les données, qui est passé à notre fonction `fetcher` et `useSWR` nous donne à la fois les états `data` et `error`.

```javascript
import useSWR from 'swr'

const fetcher = url => fetch(url).then(r => r.json())

function User() {
  const { data, error } = useSWR('/api/user', fetcher)

  if (error) return <div>failed to load</div>
  if (!data) return <div>loading...</div>
  
  return <div>hello {data.name}!</div>
}

```

SWR facilite grandement la gestion des requêtes infructueuses et rend nos composants beaucoup plus agréables à regarder.

De plus, si vous effectuez la même opération encore et encore, vous pouvez utiliser `useSWR` dans votre propre hook personnalisé pour le réutiliser dans votre application.

```javascript
function useUser (id) {
  const { data, error } = useSWR(`/api/user/${id}`, fetcher)

  return {
    user: data,
    isLoading: !error && !data,
    isError: error
  }
}

function Avatar ({ id }) {
  const { user, isLoading, isError } = useUser(id)

  if (isLoading) return <Spinner />
  if (isError) return <Error />

  return <img src={user.avatar} />
}

```

Et enfin, vous pouvez fournir des options globales à `useSWR`, y compris votre fonction `fetcher` (pour ne pas avoir à la passer à chaque fois) ainsi qu'un certain nombre de fois pour récupérer à nouveau les données après une erreur.

```javascript
import useSWR, { SWRConfig } from 'swr'

function Admin () {
  // pas besoin de passer la fonction fetcher
  const { data: courses } = useSWR('/api/courses')
  const { data: orders } = useSWR('/api/orders')
  const { data: users } = useSWR('/api/users')

  // ...
}

function App () {
  return (
    <SWRConfig 
      value={{
        errorRetryCount: 2, 
        errorRetryInterval: 5000,
        fetcher: (resource, init) => fetch(resource, init).then(res => res.json())
      }}
    >
      <Admin />
    </SWRConfig>
  )
}

```

Ce n'est qu'un aperçu des avantages de la bibliothèque SWR, et React Query vous offre tout autant d'avantages, sinon plus.

Assurez-vous d'utiliser l'une ou l'autre pour gérer votre état serveur. Cela rendra votre vie beaucoup plus facile.

## Comment gérer l'état URL dans React

Pour terminer un sujet difficile sur une note positive, l'état URL est largement déjà géré pour vous si vous utilisez un framework comme Next.js ou la version actuelle de React Router.

L'état URL est assez facile à gérer, généralement grâce à des hooks personnalisés qui nous donnent toutes les informations dont nous avons besoin sur notre emplacement, notre historique et notre chemin.

Si vous utilisez React Router, vous pouvez obtenir toutes les informations dont vous avez besoin en utilisant `useHistory` ou `useLocation`.

```javascript
import { useHistory, useLocation } from 'react-router-dom';

function BlogPost() {
  const history = useHistory();
	console.log("you are here: ", history.location);
	
	const location = useLocation();
  console.log('your pathname is: ', location.pathname);

  // ...
}

```

De plus, si vous avez des paramètres de route que vous devez utiliser, par exemple pour récupérer des données basées sur ceux-ci, vous pouvez utiliser le hook `useParams`.

```javascript
import { useParams } from 'react-router-dom';

function ChatRoom() {
  const { roomId } = useParams();
  const { chatRoom, isLoading, isError } = useChatRoom(roomId);

  // ...
}

```

Si vous utilisez Next.js, presque tout peut être accessible directement en appelant `useRouter`.

```javascript
function Orders() {
  const router = useRouter();
  console.log('the entire url is: ', router.asPath);
  console.log('your current route is: ', router.pathname);
  console.log('your query params are: ', router.query);

  function handleSubmit(item) {
    setQuery("");
    // push to new route
    router.push(item.href);
    closeDropdown();
  }

  // ...
}

```

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre tout seul.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*