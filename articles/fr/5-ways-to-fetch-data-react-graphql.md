---
title: Comment récupérer des données dans React à partir d'une API GraphQL
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-05-03T17:20:56.000Z'
originalURL: https://freecodecamp.org/news/5-ways-to-fetch-data-react-graphql
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/5-ways-to-fetch-data-in-react-with-graphql-2.png
tags:
- name: apollo client
  slug: apollo-client
- name: axios
  slug: axios
- name: GraphQL
  slug: graphql
- name: React
  slug: react
seo_title: Comment récupérer des données dans React à partir d'une API GraphQL
seo_desc: 'Let''s go through the five best ways that you can fetch data with React
  from a GraphQL API.

  While there are a couple of popular libraries which are made to interact with GraphQL
  APIs from a React application, there are many different ways to fetch dat...'
---

Passons en revue les cinq meilleures façons de récupérer des données avec React à partir d'une API GraphQL.

Bien qu'il existe plusieurs bibliothèques populaires conçues pour interagir avec les API GraphQL à partir d'une application React, il existe de nombreuses façons différentes de récupérer des données avec GraphQL.

J'ai inclus des exemples de code qui vous montrent comment récupérer ou « interroger » (query) des données avec le code le plus court possible et comment être opérationnel avec chacune de ces différentes méthodes de connexion de React à GraphQL.

## Pour commencer

Dans ces exemples, nous utiliserons l'API GraphQL de SpaceX pour récupérer et afficher les 10 dernières missions effectuées par SpaceX.

N'hésitez pas à utiliser le code ci-dessous si vous tentez de connecter votre application React à une API GraphQL. Dans ces exemples, nous allons passer de la bibliothèque client GraphQL la plus avancée pour React à l'approche la plus simple pour interroger un endpoint GraphQL.

## 1. Apollo Client

La bibliothèque GraphQL la plus populaire et la plus complète est Apollo Client.

Non seulement vous pouvez l'utiliser pour récupérer des données distantes avec GraphQL, ce que nous faisons ici, mais elle nous permet également de gérer les données localement, à la fois via un cache interne et via une API complète de gestion d'état (state management).

Pour commencer avec Apollo Client, vous devez installer la dépendance principale Apollo Client, ainsi que GraphQL :

```bash
npm install @apollo/client graphql
```

L'idée derrière Apollo Client est qu'il sera utilisé dans toute votre application. Pour ce faire, vous utiliserez un composant spécial Apollo Provider pour transmettre un client Apollo créé à l'ensemble de votre arbre de composants.

Lorsque vous créez votre client Apollo, vous devez spécifier une valeur `uri`, à savoir un endpoint GraphQL. De plus, vous devez spécifier un cache.

Apollo Client est livré avec son propre cache en mémoire (in memory cache), qui est utilisé pour mettre en cache ou stocker et gérer localement vos requêtes et leurs données associées :

```js
import React from "react";
import ReactDOM from "react-dom";
import { ApolloProvider, ApolloClient, InMemoryCache } from "@apollo/client";

import App from "./App";

const client = new ApolloClient({
  uri: "https://api.spacex.land/graphql/",
  cache: new InMemoryCache()
});

const rootElement = document.getElementById("root");
ReactDOM.render(
  <ApolloProvider client={client}>
    <App />
  </ApolloProvider>,
  rootElement
);
```

Une fois que vous avez configuré le Provider et le client dans votre composant App, vous pouvez utiliser tous les différents hooks React qu'Apollo Client vous propose pour toutes les différentes opérations GraphQL. Celles-ci incluent les requêtes (queries), les mutations et les abonnements (subscriptions). Vous pouvez même utiliser le client Apollo créé directement en utilisant un hook personnalisé appelé `useApolloClient`.

Comme vous ne faites qu'interroger des données ici, vous utiliserez le hook `useQuery`.

Vous inclurez une requête GraphQL comme premier argument pour écrire votre requête. Vous utiliserez la fonction `gql`, qui fait un certain nombre de choses, comme vous donner la coloration syntaxique de l'éditeur et la fonctionnalité de formatage automatique si vous utilisez l'outil Prettier pour votre projet.

Une fois que vous exécutez cette requête, vous récupérez les valeurs `data`, `loading` et `error` :

```js
import React from "react";
import { useQuery, gql } from "@apollo/client";

const FILMS_QUERY = gql`
  {
    launchesPast(limit: 10) {
      id
      mission_name
    }
  }
`;

export default function App() {
  const { data, loading, error } = useQuery(FILMS_QUERY);

  if (loading) return "Loading...";
  if (error) return <pre>{error.message}</pre>

  return (
    <div>
      <h1>SpaceX Launches</h1>
      <ul>
        {data.launchesPast.map((launch) => (
          <li key={launch.id}>{launch.mission_name}</li>
        ))}
      </ul>
    </div>
  );
}
```

Avant d'afficher vos données, vos missions, vous voulez gérer l'état de chargement. Lorsque vous êtes dans un état de chargement, vous récupérez la requête à partir d'un endpoint distant.

Vous voulez également gérer toutes les erreurs qui surviennent. Vous pouvez simuler une erreur en faisant une erreur de syntaxe dans votre requête, comme interroger un champ qui n'existe pas. Pour gérer cette erreur, vous pouvez facilement renvoyer et afficher un message à partir de `error.message`.

## 2. Urql

Une autre bibliothèque complète qui connecte les applications React aux API GraphQL est urql.

Elle tente de vous offrir bon nombre des fonctionnalités et de la syntaxe d'Apollo tout en étant un peu plus petite en taille et en nécessitant moins de code de configuration. Elle vous offre des capacités de mise en cache si vous le souhaitez, mais elle n'inclut pas de bibliothèque de gestion d'état intégrée comme Apollo le fait.

Pour utiliser urql comme bibliothèque client GraphQL, vous devrez installer les packages urql et GraphQL.

```bash
npm install urql graphql
```

Tout comme Apollo, vous voudrez utiliser le composant Provider dédié et créer un client avec votre endpoint GraphQL. Notez que vous n'avez pas besoin de spécifier un cache par défaut.

```js
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import { createClient, Provider } from 'urql';

const client = createClient({
  url: 'https://api.spacex.land/graphql/',
});

const rootElement = document.getElementById("root");
ReactDOM.render(
  <Provider value={client}>
    <App />
  </Provider>,
  rootElement
);
```

Très similaire à Apollo, urql vous propose des hooks personnalisés qui gèrent toutes les opérations GraphQL standard, et portent donc des noms similaires.

Encore une fois, vous pouvez utiliser le hook `useQuery` du package urql. Bien qu'au lieu d'avoir besoin de la fonction `gql`, vous pouvez vous en passer et simplement utiliser un littéral de gabarit (template literal) pour écrire votre requête.

Lors de l'appel à `useQuery`, vous récupérez un tableau que vous pouvez déstructurer en tant que tableau plutôt qu'en tant qu'objet. Le premier élément de ce tableau est un objet, appelé `result`, qui vous donne un certain nombre de propriétés que vous pouvez déstructurer : `data`, `fetching` et `error`.

```js
import React from "react";
import { useQuery } from 'urql';

const FILMS_QUERY = `
  {
    launchesPast(limit: 10) {
      id
      mission_name
    }
  }
`;

export default function App() {
  const [result] = useQuery({
    query: FILMS_QUERY,
  });

  const { data, fetching, error } = result;

  if (fetching) return "Loading...";
  if (error) return <pre>{error.message}</pre>

  return (
    <div>
      <h1>SpaceX Launches</h1>
      <ul>
        {data.launchesPast.map((launch) => (
          <li key={launch.id}>{launch.mission_name}</li>
        ))}
      </ul>
    </div>
  );
}
```

De la même manière que pour l'affichage des données que vous récupérez avec Apollo, vous pouvez gérer vos états d'erreur et de chargement pendant que vous récupérez vos données distantes.

## 3. React Query + GraphQL Request

Il est important de noter à ce stade que vous n'avez pas besoin d'une bibliothèque client GraphQL sophistiquée et lourde comme urql ou Apollo pour interagir avec votre API GraphQL, comme nous le verrons plus tard.

Des bibliothèques comme Apollo et urql ont été créées non seulement pour vous aider à effectuer toutes les opérations GraphQL standard, mais aussi pour mieux gérer l'état du serveur dans votre client React grâce à un certain nombre d'outils supplémentaires. Tout cela s'ajoute au fait qu'elles sont livrées avec des hooks personnalisés qui simplifient la gestion des tâches répétitives comme la gestion du chargement, des erreurs et d'autres états connexes.

Dans cette optique, voyons comment vous pouvez utiliser une bibliothèque GraphQL très épurée pour votre récupération de données et la combiner avec un meilleur moyen de gérer et de mettre en cache cet état de serveur que vous apportez dans votre application. Vous pouvez récupérer des données très simplement à l'aide du package `graphql-request`.

GraphQL Request est une bibliothèque qui ne vous oblige pas à configurer un client ou un composant Provider. Il s'agit essentiellement d'une fonction qui accepte simplement un endpoint et une requête. Très similaire à un client HTTP, il vous suffit de passer ces deux valeurs et vous récupérez vos données.

Maintenant, si vous voulez gérer cet état dans toute votre application, vous pouvez utiliser une excellente bibliothèque normalement utilisée pour interagir avec les API REST — mais elle est tout aussi utile pour les API GraphQL — et il s'agit de React Query. Elle vous propose des hooks React aux noms très similaires, `useQuery` et `useMutation`, qui effectuent des tâches identiques à ce que font les hooks Apollo et urql.

React Query vous offre également un tas d'outils pour gérer l'état, ainsi qu'un composant Dev Tools intégré qui vous permet de voir ce qui est stocké dans le cache intégré de React Query.

> En associant votre client GraphQL très basique, GraphQL Request, à React Query, vous obtenez toute la puissance d'une bibliothèque comme urql ou Apollo.

Pour commencer avec cette association, il vous suffit d'installer React Query et GraphQL Request :

```bash
npm install react-query graphql-request
```

Vous utilisez le composant Provider de React Query et créez un client de requête où vous pouvez définir certains paramètres de récupération de données par défaut si vous le souhaitez. Ensuite, dans votre composant d'application lui-même, ou dans n'importe quel composant enfant de `App`, vous pouvez utiliser le hook `useQuery`.

```js
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import { QueryClient, QueryClientProvider } from "react-query";

const client = new QueryClient();

const rootElement = document.getElementById("root");
ReactDOM.render(
  <QueryClientProvider client={client}>
    <App />
  </QueryClientProvider>,
  rootElement
);
```

Pour stocker le résultat de votre opération dans le cache de React Query, il vous suffit de lui donner une valeur clé comme premier argument pour servir d'identifiant. Cela vous permet de référencer et d'extraire très facilement des données du cache, ainsi que de ré-exécuter ou d'invalider une requête donnée pour récupérer des données mises à jour.

Puisque vous récupérez des données de lancement, appelons cette requête « launches ».

Encore une fois, ce hook renverra le résultat de cette requête. Pour le deuxième argument de `useQuery`, vous devez spécifier comment récupérer ces données et React Query se chargera de résoudre la promesse renvoyée par GraphQL Request.

```js
import React from "react";
import { request, gql } from "graphql-request";
import { useQuery } from "react-query";

const endpoint = "https://api.spacex.land/graphql/";
const FILMS_QUERY = gql`
  {
    launchesPast(limit: 10) {
      id
      mission_name
    }
  }
`;

export default function App() {
  const { data, isLoading, error } = useQuery("launches", () => {
    return request(endpoint, FILMS_QUERY);
  });

  if (isLoading) return "Loading...";
  if (error) return <pre>{error.message}</pre>;

  return (
    <div>
      <h1>SpaceX Launches</h1>
      <ul>
        {data.launchesPast.map((launch) => (
          <li key={launch.id}>{launch.mission_name}</li>
        ))}
      </ul>
    </div>
  );
}
```

Semblable à Apollo, vous récupérez un objet que vous pouvez déstructurer pour obtenir les valeurs des données, ainsi que pour savoir si vous êtes ou non dans l'état de chargement et l'état d'erreur.

## 4. React Query + Axios

Vous pouvez utiliser des bibliothèques clientes HTTP encore plus simples qui n'ont aucun lien avec GraphQL pour récupérer vos données.

Dans ce cas, vous pouvez utiliser la bibliothèque populaire axios. Encore une fois, vous pouvez l'associer à React Query pour obtenir tous les hooks spéciaux et la gestion d'état.

```bash
npm install react-query axios
```

L'utilisation d'un client HTTP comme Axios pour effectuer une requête à partir d'une API GraphQL nécessite d'effectuer une requête POST vers votre endpoint d'API. Pour les données que vous envoyez dans la requête, vous fournirez un objet avec une propriété appelée `query`, qui sera définie sur votre requête de films.

Avec axios, vous allez devoir inclure un peu plus d'informations sur la façon de résoudre cette promesse et de récupérer vos données. Vous devez indiquer à React Query où se trouvent les données afin qu'elles puissent être placées sur la propriété `data` que `useQuery` renvoie.

En particulier, vous récupérez les données sur la propriété data de `response.data` :

```js
import React from "react";
import axios from "axios";
import { useQuery } from "react-query";

const endpoint = "https://api.spacex.land/graphql/";
const FILMS_QUERY = `
  {
    launchesPast(limit: 10) {
      id
      mission_name
    }
  }
`;

export default function App() {
  const { data, isLoading, error } = useQuery("launches", () => {
    return axios({
      url: endpoint,
      method: "POST",
      data: {
        query: FILMS_QUERY
      }
    }).then(response => response.data.data);
  });

  if (isLoading) return "Loading...";
  if (error) return <pre>{error.message}</pre>;

  return (
    <div>
      <h1>SpaceX Launches</h1>
      <ul>
        {data.launchesPast.map((launch) => (
          <li key={launch.id}>{launch.mission_name}</li>
        ))}
      </ul>
    </div>
  );
}
```

## 5. React Query + Fetch API

La plus simple de toutes ces différentes approches pour récupérer des données est d'utiliser simplement React Query plus l'API fetch.

Comme l'API fetch est incluse dans tous les navigateurs modernes, vous n'avez pas besoin d'installer une bibliothèque tierce — il vous suffit d'installer `react-query` dans votre application.

```bash
npm install react-query
```

Une fois que vous avez le client React Query fourni à l'ensemble de l'application, vous pouvez simplement remplacer votre code axios par fetch.

Ce qui est un peu différent, c'est que vous devez spécifier un en-tête (header) qui inclut le type de contenu des données que vous souhaitez recevoir en retour de votre requête. Dans ce cas, il s'agit de données JSON.

Vous devez également transformer en chaîne de caractères (stringify) l'objet que vous envoyez comme charge utile (payload) avec une propriété query qui est définie sur votre requête de films :

```js
import React from "react";
import axios from "axios";
import { useQuery } from "react-query";

const endpoint = "https://api.spacex.land/graphql/";
const FILMS_QUERY = `
  {
    launchesPast(limit: 10) {
      id
      mission_name
    }
  }
`;

export default function App() {
  const { data, isLoading, error } = useQuery("launches", () => {
    return fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: FILMS_QUERY })
    })
      .then((response) => {
        if (response.status >= 400) {
          throw new Error("Error fetching data");
        } else {
          return response.json();
        }
      })
      .then((data) => data.data);
  });

  if (isLoading) return "Loading...";
  if (error) return <pre>{error.message}</pre>;

  return (
    <div>
      <h1>SpaceX Launches</h1>
      <ul>
        {data.launchesPast.map((launch) => (
          <li key={launch.id}>{launch.mission_name}</li>
        ))}
      </ul>
    </div>
  );
}
```

L'un des avantages de l'utilisation d'axios par rapport à fetch est qu'il gère automatiquement les erreurs pour vous. Avec fetch, comme vous pouvez le voir dans le code ci-dessus, vous devez vérifier un certain code d'état, en particulier un code d'état supérieur à 400.

Cela signifie que votre requête se solde par une erreur. Si tel est le cas, vous devez lancer manuellement une erreur, qui sera capturée par votre hook `useQuery`. Sinon, s'il s'agit d'une réponse de la plage 200 ou 300, ce qui signifie que la requête a réussi, renvoyez simplement les données JSON et affichez-les.

## Conclusion

Cet article était dédié à vous montrer un certain nombre d'approches différentes pour récupérer efficacement des données à partir d'une API GraphQL avec React.

Parmi ces options, j'espère que vous pourrez évaluer celle qui est la plus appropriée pour vous et vos applications. Et maintenant, vous disposez d'un code utile qui vous permettra de commencer à utiliser ces outils et bibliothèques beaucoup plus rapidement.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre tout seul.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation de : The React Bootcamp**](https://www.thereactbootcamp.com)

**C’est le cours que j’aurais aimé avoir quand j’ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*