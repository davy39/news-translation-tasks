---
title: 'Apollo GraphQL : Comment construire une application full-stack avec React
  et Node Js'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-29T17:03:39.000Z'
originalURL: https://freecodecamp.org/news/apollo-graphql-how-to-build-a-full-stack-app-with-react-and-node-js
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/cover-3.png
tags:
- name: Apollo GraphQL
  slug: apollo
- name: GraphQL
  slug: graphql
- name: node
  slug: node
- name: React
  slug: react
seo_title: 'Apollo GraphQL : Comment construire une application full-stack avec React
  et Node Js'
seo_desc: 'By Ibrahima Ndaw

  Apollo Client is a complete state management library for JavaScript apps. It''s
  a powerful tool since it can be used on both the back end and front end side.

  In this tutorial, we will use it on the front end and back end by building a...'
---

Par Ibrahima Ndaw

Apollo Client est une bibliothèque complète de gestion d'état pour les applications JavaScript. C'est un outil puissant puisqu'il peut être utilisé à la fois côté back-end et front-end.

Dans ce tutoriel, nous allons l'utiliser côté front-end et back-end en construisant un serveur Apollo GraphQL avec Node JS. Ensuite, nous allons consommer les données côté client en utilisant React JS.

Si vous êtes nouveau dans GraphQL, [ce tutoriel](https://www.ibrahima-ndaw.com/blog/graphql-api-express-mongodb/) pourrait vous aider. Sinon, commençons.

* [Construction du serveur avec Apollo, Node et GraphQL](#heading-construction-du-serveur-avec-apollo-node-et-graphql)
* [Schéma GraphQL](#heading-schema-graphql)
* [Résolveurs GraphQL](#heading-resolveurs-graphql)
* [Création du serveur Apollo](#heading-creation-du-serveur-apollo)
* [Construction du côté client avec React](#heading-construction-du-cote-client-avec-react)
* [Connexion de React à Apollo](#heading-connexion-de-react-a-apollo)
* [Récupération des données](#heading-recuperation-des-donnees)
* [Affichage des données](#heading-affichage-des-donnees)

## Construction du serveur avec Apollo, Node et GraphQL

Dans ce guide, j'utiliserai l'API Github pour avoir des données à afficher, et cette opération sera effectuée par le serveur GraphQL construit avec Apollo et Node JS.

Pour que cela se produise, nous devons exécuter la commande suivante dans le terminal pour configurer un nouveau projet Node JS :

```shell
  yarn init

```

Une fois la configuration terminée, nous pouvons maintenant installer les packages nécessaires en exécutant cette commande :

```shell
  yarn add apollo-server graphql axios

```

Super, nous avons maintenant tout ce dont nous avons besoin pour construire un serveur. Donc, commençons par créer un nouveau fichier `app.js` à la racine qui sera le point d'entrée de notre serveur.

Ensuite, nous devons définir un schéma GraphQL qui reflète la manière dont nos données doivent apparaître.

### Schéma GraphQL

Un schéma décrit la forme de votre graphe de données. Il définit un ensemble de types avec des champs qui sont remplis à partir de vos magasins de données back-end. Donc, ajoutons un nouveau schéma dans le fichier `app.js`.

* `app.js`

```js
const { ApolloServer, gql } = require("apollo-server")
const axios = require("axios")

const typeDefs = gql`
  type User {
    id: ID
    login: String
    avatar_url: String
  }

  type Query {
    users: [User]
  }
`

```

Comme vous pouvez le voir, nous n'utilisons pas toutes les données fournies par l'API Github. Nous avons juste besoin de l'id qui sera utilisé comme clé de référence dans l'application React, du login et de l'avatar_url. Nous avons également une requête `users` qui retourne un tableau d'utilisateurs.

Maintenant que nous avons un schéma GraphQL, il est temps de construire les résolveurs correspondants pour compléter l'opération de requête.

### Résolveurs GraphQL

Un résolveur est une collection de fonctions qui aident à générer une réponse à partir d'une requête GraphQL. Donc, ajoutons un nouveau résolveur dans le fichier `app.js`.

* `app.js`

```js
const resolvers = {
  Query: {
    users: async () => {
      try {
        const users = await axios.get("https://api.github.com/users")
        return users.data.map(({ id, login, avatar_url }) => ({
          id,
          login,
          avatar_url,
        }))
      } catch (error) {
        throw error
      }
    },
  },
}

```

Un résolveur doit correspondre au schéma approprié par nom. Par conséquent, ici `users` fait référence à la requête `users` définie dans notre schéma. C'est une fonction qui récupère les données de l'API avec l'aide d'`axios` et retourne comme prévu l'id, le login et l'avatar_url.

Et cette opération peut prendre du temps à se compléter. C'est pourquoi async/await est utilisé ici pour la gérer.

Avec cela, nous pouvons maintenant créer le serveur Apollo dans la section suivante.

### Création du serveur Apollo

Si vous vous souvenez, dans le fichier `app.js`, nous avions importé `ApolloServer` du package `apollo-server`. C'est un constructeur qui reçoit un objet comme argument. Et cet objet doit contenir le schéma et le résolveur pour pouvoir créer le serveur.

Donc, modifions un peu `app.js` avec `ApolloServer`.

* `app.js`

```js
const server = new ApolloServer({
  typeDefs,
  resolvers,
})
//  typeDefs: typeDefs,
//  resolvers: resolvers
server.listen().then(({ url }) => console.log(`Server ready at ${url}`))

```

Ici, nous passons en paramètre un objet qui contient le schéma et le résolveur à `ApolloServer` pour créer le serveur et ensuite l'écouter. Avec cela en place, nous avons maintenant un serveur fonctionnel avec lequel travailler.

Vous pouvez déjà jouer avec et envoyer des requêtes avec l'aide de GraphQL playground en exécutant cette commande :

```shell
  yarn start

```

Vous pouvez maintenant le prévisualiser sur `http://localhost:400`

* Le fichier `app.js` complet

```js
const { ApolloServer, gql } = require("apollo-server")
const axios = require("axios")

const typeDefs = gql`
  type User {
    id: ID
    login: String
    avatar_url: String
  }

  type Query {
    users: [User]
  }
`

const resolvers = {
  Query: {
    users: async () => {
      try {
        const users = await axios.get("https://api.github.com/users")
        return users.data.map(({ id, login, avatar_url }) => ({
          id,
          login,
          avatar_url,
        }))
      } catch (error) {
        throw error
      }
    },
  },
}

const server = new ApolloServer({
  typeDefs,
  resolvers,
})

server.listen().then(({ url }) => console.log(`Server ready at ${url}`))

```

Un serveur seul ne fait pas grand-chose. Nous devons ajouter un script de démarrage dans le fichier `package.json` pour, comme vous l'avez deviné, démarrer le serveur.

* `package.json`

```js
  // d'abord ajouter nodemon : yarn add nodemon --dev
  "scripts": {
    "start": "nodemon src/index.js"
  }

```

Avec cela, nous avons un serveur pour récupérer des données de l'API Github. Il est donc temps de passer côté client et de consommer les données.

_Faisons-le._

![yaay](https://media.giphy.com/media/huJxyJPiPk1jwQWPAN/source.gif)

## Construction du côté client avec React

La première chose que nous devons faire est de créer une nouvelle application React en exécutant la commande suivante dans le terminal :

```shell
npx create-react-app client-react-apollo

```

Ensuite, nous devons installer les packages Apollo et GraphQL :

```shell
  yarn add apollo-boost @apollo/react-hooks graphql

```

Maintenant, nous pouvons connecter Apollo à notre application React en mettant à jour le fichier `index.js`.

### Connexion de React à Apollo

* `index.js`

```shell
import React from 'react';
import ReactDOM from 'react-dom';
import ApolloClient from 'apollo-boost'
import { ApolloProvider } from '@apollo/react-hooks';

import App from './App';
import './index.css';
import * as serviceWorker from './serviceWorker';

const client = new ApolloClient({
  uri: 'https://7sgx4.sse.codesandbox.io'
})


ReactDOM.render(
  <React.StrictMode>
    <ApolloProvider client={client}>
      <App />
    </ApolloProvider>
  </React.StrictMode>,
  document.getElementById('root')
);

serviceWorker.unregister();

```

Comme vous pouvez le voir, nous commençons par importer `ApolloClient` et `ApolloProvider`. Le premier nous aide à informer Apollo de l'URL à utiliser lors de la récupération des données. Et si aucun `uri` n'est passé à `ApolloClient`, il prendra le nom de domaine actuel plus `/graphql`.

Le second est le Provider qui s'attend à recevoir l'objet client pour pouvoir connecter Apollo à React.

Cela dit, nous pouvons maintenant créer un composant qui affiche les données.

### Récupération des données

* `App.js`

```jsx
import React from "react"
import { useQuery } from "@apollo/react-hooks"
import gql from "graphql-tag"
import "./App.css"

const GET_USERS = gql`
  {
    users {
      id
      login
      avatar_url
    }
  }
`

```

Ici, nous avons une simple requête GraphQL qui récupère les données. Cette requête sera passée plus tard à `useQuery` pour dire à Apollo quelles données récupérer.

* `App.js`

```jsx
const User = ({ user: { login, avatar_url } }) => (
  <div className="Card">
    <div>
      <img alt="avatar" className="Card--avatar" src={avatar_url} />
      <h1 className="Card--name">{login}</h1>
    </div>
    <a href={`https://github.com/${login}`} className="Card--link">
      Voir le profil
    </a>
  </div>
)

```

Ce composant de présentation sera utilisé pour afficher un utilisateur. Il reçoit les données du composant App et les affiche.

### Affichage des données

* `App.js`

```jsx
function App() {
  const { loading, error, data } = useQuery(GET_USERS)

  if (error) return <h1>Something went wrong!</h1>
  if (loading) return <h1>Loading...</h1>

  return (
    <main className="App">
      <h1>Github | Users</h1>
      {data.users.map(user => (
        <User key={user.id} user={user} />
      ))}
    </main>
  )
}

export default App

```

Le hook `useQuery` fourni par Apollo reçoit la requête GraphQL et retourne trois états : le chargement, l'erreur et les données.

Si les données sont récupérées avec succès, nous les passons au composant User. Sinon, nous affichons une erreur.

* Le fichier `App.js` complet

```jsx
import React from "react"
import { useQuery } from "@apollo/react-hooks"
import gql from "graphql-tag"
import "./App.css"

const GET_USERS = gql`
  {
    users {
      id
      login
      avatar_url
    }
  }
`

const User = ({ user: { login, avatar_url } }) => (
  <div className="Card">
    <div>
      <img alt="avatar" className="Card--avatar" src={avatar_url} />
      <h1 className="Card--name">{login}</h1>
    </div>
    <a href={`https://github.com/${login}`} className="Card--link">
      Voir le profil
    </a>
  </div>
)

function App() {
  const { loading, error, data } = useQuery(GET_USERS)

  if (error) return <h1>Something went wrong!</h1>
  if (loading) return <h1>Loading...</h1>

  return (
    <main className="App">
      <h1>Github | Users</h1>
      {data.users.map(user => (
        <User key={user.id} user={user} />
      ))}
    </main>
  )
}

export default App

```

Super ! Avec cela, nous avons maintenant terminé la construction d'une application full-stack Apollo GraphQL en utilisant React et Node JS.

Prévisualisez le serveur Apollo GraphQL [ici](https://codesandbox.io/s/node-apollo-graphql-7sgx4?file=/package.json:139-193)

Prévisualisez l'application React [ici](https://codesandbox.io/s/react-apollo-graphql-1qu75)

Trouvez le code source [ici](https://github.com/ibrahima92/apollo-graphql-full-stack)

Vous pouvez trouver d'autres contenus intéressants comme celui-ci sur [mon blog](https://www.ibrahima-ndaw.com/blog/apollo-graphql-fullstack-app-with-react-and-nodejs/)

Merci d'avoir lu !

![congrats](https://media.giphy.com/media/OcZp0maz6ALok/source.gif)