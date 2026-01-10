---
title: Comment créer une application Pokemon avec GraphQL et Apollo
subtitle: ''
author: Segun Ajibola
co_authors: []
series: null
date: '2024-04-03T12:28:07.000Z'
originalURL: https://freecodecamp.org/news/build-a-pokemon-app-with-graphql-and-apollo
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Parameters-vs-Arguments--2-.png
tags:
- name: Apollo GraphQL
  slug: apollo
- name: GraphQL
  slug: graphql
- name: projects
  slug: projects
- name: React
  slug: react
seo_title: Comment créer une application Pokemon avec GraphQL et Apollo
seo_desc: 'Pokemon is a Japanese media franchise consisting of video games, animated
  series and films, a trading card game, and other related media.

  In this blog, we will be building with a Pokemon GraphQL API that gives us data
  about different Pokemons.

  We wil...'
---

Pokemon est une franchise médiatique japonaise composée de jeux vidéo, de séries et films animés, d'un jeu de cartes à collectionner et d'autres médias associés.

Dans cet article, nous allons construire une application avec une API Pokemon GraphQL qui nous fournit des données sur différents Pokemons.

Nous allons utiliser Apollo et GraphQL pour gérer la récupération des données, et React pour construire notre application front-end.

Pas d'inquiétude si vous ne connaissez pas ces technologies, je vais vous guider à travers les bases au fur et à mesure de votre lecture.

### Prérequis

Vous devez avoir ces éléments sur votre ordinateur pour suivre le tutoriel :

* Nodejs v18+
* Un éditeur de code
* Un navigateur web

Créons notre application React.

### Installation de l'application React

Pour créer votre application React, naviguez vers votre terminal et utilisez l'invite de commande. Ouvrez votre invite de commande et choisissez l'emplacement préféré pour créer votre projet React. Allons avec le Bureau.

```bash
cd Bureau
```

La commande ci-dessus vous amènera à votre Bureau.

```bash
npm create vite@latest pokemon-app -- --template react
```

`npm create vite@latest` va commencer à construire un nouveau projet en utilisant Vite. Mais nous avons attaché le nom de notre projet (`pokemon-app`) et la technologie ou le framework que notre application utilisera (`-- --template react`).

Vous pouvez définir un autre template comme `svelte`, `vanilla` ou `vue` et le projet sera créé en utilisant ce framework. Lisez plus sur Vite sur [son site officiel](https://vitejs.dev/guide/).

Après l'installation de Vite, exécutez les commandes suivantes :

```bash
cd pokemon-app
npm install
npm run dev
```

Nous utiliserons les commandes ci-dessus pour terminer l'installation de React.

Exécutez la première commande, `cd pokemon-app`, pour naviguer vers le dossier **pokemon-app**.

Exécutez `code .` pour ouvrir le dossier dans votre éditeur de code.

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1711666709423/593e293d-af0b-4cbd-b4ac-83d0c8213446.png)
_modal s'affichant sur VSCode pour accepter que vous faites confiance aux auteurs des fichiers ouverts dans VSCode_

Cochez la case de confiance à l'auteur si cela apparaît.

Ouvrez le terminal de votre éditeur de code. Si vous utilisez VSCode sur Windows, le raccourci est `Ctrl + \`.

Exécutez les deux autres commandes dans le terminal l'une après l'autre.

```bash
npm install
```

```bash
npm run dev
```

Votre projet devrait maintenant s'exécuter dans le navigateur.

Nous allons gérer la récupération de nos données en utilisant GraphQL et Apollo.

## Comment utiliser GraphQL et Apollo

GraphQL est un langage de requête pour les API et un runtime pour exécuter des requêtes avec vos données existantes. Il vous permet de demander uniquement les données dont vous avez besoin dans votre application et rien de plus, ce qui le rend très efficace et flexible.

Apollo est une bibliothèque de gestion d'état qui vous permet de gérer les données locales et distantes avec GraphQL. Il peut être utilisé pour récupérer, mettre en cache et modifier les données de l'application, tout en mettant automatiquement à jour votre interface utilisateur.

Installons les packages dont vous avez besoin.

### Installation des packages

Exécutez la commande suivante dans votre terminal pour installer le client Apollo.

```bash
npm install @apollo/client
```

Naviguez vers votre fichier **main.jsx** et importez ces éléments :

```javascript
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import {
  ApolloProvider,
  ApolloClient,
  InMemoryCache,
} from "@apollo/client";
import "./index.css";
```

Vous avez importé React et ReactDOM pour la manipulation du DOM.

`ApolloClient` est responsable de la gestion de la récupération des données et de la gestion d'état de votre application. Il gère l'envoi de requêtes et de mutations GraphQL à votre serveur GraphQL et la mise en cache des résultats.

`ApolloProvider` sera utilisé pour envelopper votre application React afin de fournir l'instance Apollo Client à tous vos composants, de sorte que votre application puisse accéder aux données récupérées via Apollo Client.

`InMemoryCache` est une implémentation de cache pour stocker les résultats des requêtes GraphQL en mémoire pour un accès et une récupération efficaces.

Vous avez également importé **index.css** pour styliser votre application.

### Comment créer un client Apollo

```javascript
const client = new ApolloClient({
  uri: "https://graphql-pokemon2.vercel.app/",
  cache: new InMemoryCache(),
});
```

Le code ci-dessus crée une nouvelle instance de `ApolloClient` avec certaines configurations :

1. `uri` : Cela spécifie l'URL de votre point de terminaison de l'API GraphQL. C'est le point de terminaison où votre Apollo Client enverra les requêtes et mutations GraphQL.
2. `cache` : Cela configure l'implémentation du cache pour Apollo Client afin d'utiliser un cache en mémoire pour accéder aux données et stocker le résultat des requêtes GraphQL, réduisant ainsi le besoin de récupérer à nouveau les données du serveur.

Vous pouvez maintenant envelopper votre composant `<App />` avec `ApolloProvider` :

```javascript
ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <ApolloProvider client={client}>
      <App />
    </ApolloProvider>
  </React.StrictMode>
);
```

Notez que la prop `client` a également été passée pour fournir à votre application la configuration `ApolloClient`.

Allez dans votre composant **App.jsx** et entrez ceci :

```javascript
import React from "react";
import { PokemonsContainer } from "./components/PokemonsContainer";

export default function App() {
  return (
    <main>
      <PokemonsContainer />
    </main>
  );
}
```

Vous avez importé React et `PokemonsContainer` sera créé. Le composant `PokemonsContainer` a été enveloppé dans une balise main et sera rendu lorsque le composant sera collé dans le DOM.

Créons le composant `PokemonsContainer` dans un fichier situé dans le dossier **components**. C'est-à-dire :

📂 src/components/PokemonsContainer.jsx

### Composant Pokemons Container

```javascript
import React from "react";
import { useQuery } from "@apollo/client";
import { Pokemon } from "../components/Pokemon";
import { GET_POKEMONS } from "../graphql/get-pokemons";
```

Le `useQuery` de `@apollo/client` est utilisé pour exécuter des requêtes dans une application Apollo. Pour ce faire, `useQuery()` est appelé et une chaîne de requête GraphQL est passée en argument. Lorsque votre composant est rendu, `useQuery` retourne un objet d'Apollo Client qui contient les propriétés `loading`, `error` et `data` que vous pouvez utiliser pour rendre votre interface utilisateur.

Le composant `Pokemon` a été importé pour rendre une interface utilisateur pour un Pokemon, cela sera construit sous peu.

`GET_POKEMONS` a également été importé. Cela contiendra une requête GraphQL.

Après avoir importé les fonctions ci-dessus, continuez à construire votre page.

```javascript
export function PokemonsContainer() {
  const { loading, error, data } = useQuery(GET_POKEMONS, {
    variables: { first: 5 },
  });

  if (loading) return <p>Chargement...</p>;
  if (error) return <p>Erreur : {error.message}</p>;

  const pokemons = data?.pokemons || [];
  return (
    <div className="container">
      {pokemons &&
        pokemons.map((pokemon) => (
          <Pokemon key={pokemon.id} pokemon={pokemon} />
        ))}
    </div>
  );
}
```

Comme mentionné précédemment, `useQuery` retourne un objet d'Apollo Client qui contient les propriétés `loading`, `error` et `data`. Elles sont déstructurées ici pour que vous puissiez y accéder dans la page.

Remarquez que nous fournissons une option de configuration (`variables`) au hook `useQuery`. `{ variables: { first: 5 } }` a également été passé en tant que deuxième argument. L'option `variables` est un objet qui contient toutes les variables que nous voulons passer à notre requête GraphQL. Dans ce cas, nous avons passé un objet `{ first: 5 }` pour spécifier que nous voulons les cinq premiers Pokemons.

Si la requête est toujours en cours de chargement, `<p>Chargement...</p>` est retourné pour informer l'utilisateur tandis que `<p>Erreur : {error.message}</p>` sera retourné en cas d'erreur.

La constante `pokemons` a été créée pour contenir la valeur de la propriété Pokemons de l'objet data. Si `data.pokemons` n'est pas disponible, la constante `pokemons` sera un tableau vide.

Une div est retournée avec un `className` de `container` qui vérifie si `pokemons` est disponible et mappe le tableau sur le composant `Pokemon`.

Créons le composant `Pokemon` :

📂 src/components/Pokemon.jsx

## Composant Pokemon

```javascript
import React from "react";

export function Pokemon({ pokemon }) {
  return (
    <div className="pokemon">
      <div className="pokemon__name">
        <p>{pokemon.name}</p>
      </div>
      <div className="pokemon__meta">
        <span>{pokemon.maxHP}</span>
        <span>{pokemon.maxCP}</span>
      </div>
      <div className="pokemon__image">
        <img src={pokemon.image} alt={pokemon.name} />
      </div>
      <div className="pokemon__attacks">
        {pokemon.attacks.special.slice(0, 3).map((attack) => (
          <span key={`${attack.name}-${attack.damage}`}>{attack.name}</span>
        ))}
      </div>
    </div>
  );
}
```

La structure d'une instance d'un Pokemon est définie ici avec le className pour le style. Le `name`, `maxHP`, `maxCP`, `image` et le tableau `attacks` seront rendus.

Créons la requête GraphQL `GET_POKEMONS`.

📂 src/graphql/get-pokemons

## Requête GraphQL

```javascript
import gql from "graphql-tag";

export const GET_POKEMONS = gql`
  query pokemons($first: Int!) {
    pokemons(first: $first) {
      id
      name
      image
      maxHP
      maxCP
      attacks {
        special {
          name
          damage
        }
      }
    }
  }
`;
```

Vous avez importé `gql` de `graphql-tag` et créé une requête GraphQL nommée `GET_POKEMONS`.

La fonction de requête `pokemons` a été enveloppée dans des chaînes pour que la fonction `gql` les analyse en documents de requête.

`$first: Int!` signifie que votre requête attend une variable appelée `first`, qui est un entier, et le symbole `!` après `Int` signifie que la variable est requise.

Rappelons que nous avons créé l'objet `variables` dans le composant `PokemonsContainer`, il est ici ci-dessous.

```javascript
 const { loading, error, data } = useQuery(GET_POKEMONS, {
   variables: { first: 5 },
 });
```

`pokemons(first: $first)` a également été déclaré. `$first` sera assigné à 5 ici (nous avons passé 9 dans l'extrait de code ci-dessus). Ainsi, le tableau contiendra seulement 5 objets. Chaque objet contiendra `id`, `name`, `image`, `maxHP`, `maxCP`, et l'objet attacks qui contiendra l'objet special contenant name et damage.

Le serveur GraphQL peut contenir plus de propriétés mais ne retournera que les propriétés listées ci-dessus. C'est l'une des fonctionnalités intéressantes de GraphQL – il vous donne uniquement les données que vous demandez.

## Stylisation de notre application

Votre fichier **index.css** devrait contenir ceci :

```css
/* RESETS
=========================================== */
html {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

*,
*:before,
*:after {
  -webkit-box-sizing: inherit;
  box-sizing: inherit;
}

body {
  margin: 20px 0;
  padding: 0 20px;
  line-height: 1;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  color: #202020;
  background-color: #fbfbfb;
  font-smooth: always;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* APPLICATION POKEMON
=========================================== */
.container {
  display: flex;
  max-width: 80%;
  margin: auto;
  height: 100vh;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
}

.container p {
  margin: 0;
}

.container .pokemon {
  width: 20%;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(0, 0, 0, 0.125);
  border-radius: 0.25rem;
  box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
  overflow: hidden;
  /* margin: 5px; */
}

.container .pokemon__name {
  background-color: #ecd018;
  text-align: center;
  padding: 10px;
}

.container .pokemon__name p {
  text-transform: uppercase;
  font-weight: bold;
  color: white;
  letter-spacing: 4px;
  text-shadow: 0px 1px 2px rgba(0, 0, 0, 0.4);
}

.container .pokemon__image {
  padding: 20px;
  min-height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.container .pokemon__image img {
  max-width: 100%;
  height: auto;
}

.container .pokemon__attacks {
  display: flex;
  padding-left: 10px;
  padding-right: 10px;
  justify-content: space-between;
}

.container .pokemon__attacks span {
  width: 32%;
  background-color: #f16820;
  border-radius: 3px;
  padding: 7px;
  font-weight: 700;
  color: #fff;
  padding-left: 10px;
  padding-right: 10px;
  font-size: 12px;
  margin-bottom: 10px;
  word-wrap: break-word;
  text-align: center;
  line-height: 15px;
}

.container .pokemon__meta {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
  padding: 0 10px;
}

.container .pokemon__meta span {
  color: white;
  text-shadow: 0px 1px 2px rgba(0, 0, 0, 0.4);
  background-color: #7bb7b7;
  font-weight: bold;
  margin: 0;
  padding: 5px 20px;
  border-radius: 5px;
}
```

Si tout est bien fait, vous devriez avoir ceci dans votre navigateur :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1712103327205/94a0fc27-6e6e-4441-b7e7-c3e3df005383.png)
_une image montrant les données des cinq pokemons dans le navigateur_

Vous pouvez obtenir le code GitHub ici : [https://github.com/segunajibola/pokemon-graphql](https://github.com/segunajibola/pokemon-graphql)

Vous pouvez également voir le site en direct hébergé sur Vercel ici : [**pokemonsapp.vercel.app**](http://pokemonsapp.vercel.app)

Consultez mon portfolio de projets : [segunajibola.com](https://segunajibola.com)

## [Conclusion](https://pokemonsapp.vercel.app/)

C'est tout. J'espère que vous avez trouvé de la valeur ici en apprenant davantage sur le web.

Si vous avez aimé cet article et souhaitez voir plus de contenu lié à JavaScript et au développement web, alors suivez-moi ici, sur [Twitter (X)](https://x.com/intent/follow?screen_name=iamsegunajibola) ou connectez-vous sur [LinkedIn](https://www.linkedin.com/mwlite/in/segun-ajibola-511502175). Je serais ravi de vous compter parmi mon groupe toujours croissant d'amis géniaux sur Internet.

Vous pouvez également rejoindre ma [communauté de développeurs WhatsApp](https://chat.whatsapp.com/E57KqFYQK9B1woySXTaqKr) et ma [communauté OpenSource](https://chat.whatsapp.com/KH7r2EA6kMgHuHwVfM4VFB) de 330+ développeurs apprenant et construisant des projets cool.

Si vous souhaitez également me soutenir, vous pouvez également [m'offrir un café](https://www.buymeacoffee.com/segunajibola).

Merci et au revoir. 👋