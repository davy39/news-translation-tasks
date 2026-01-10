---
title: Une introduction complète à Apollo, la boîte à outils GraphQL
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-03-24T10:57:58.000Z'
originalURL: https://freecodecamp.org/news/a-complete-introduction-to-apollo-the-graphql-toolkit-83acab4b8143
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3crww-zqngVHMJ-3xhnq5w.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Une introduction complète à Apollo, la boîte à outils GraphQL
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  Introduction to Apollo

  In the last few years, GraphQL has gotten hugely popular as an alternative approach
  to building an API over REST.

  GraphQL is a great way to let the client decid...'
---

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)

### Introduction à Apollo

Au cours des dernières années, [GraphQL](https://flaviocopes.com/graphql/) est devenu extrêmement populaire comme approche alternative pour construire une API sur REST.

GraphQL est un excellent moyen de laisser le client décider quelles données il souhaite transmettre sur le réseau, plutôt que de laisser le serveur envoyer un ensemble fixe de données.

De plus, il permet de spécifier des ressources imbriquées, réduisant les allers-retours parfois nécessaires lors de la gestion des API REST.

Apollo est une équipe et une communauté qui construit sur GraphQL et fournit différents outils pour aider à construire vos projets.

![Image](https://cdn-media-1.freecodecamp.org/images/cZlluTAwxSbZXNG6wNJXed2IjdlURME1gg0r)
_Logo Apollo gracieuseté de apollographql.com_

Les outils fournis par Apollo sont principalement au nombre de trois : **Client**, **Server**, **Engine**.

**Apollo Client** aide à consommer une API GraphQL, avec support pour les technologies web frontend les plus populaires comme React, Vue, Angular, Ember et Meteor. Il supporte également le développement natif sur iOS et Android.

**Apollo Server** est la partie serveur de GraphQL, qui interface avec votre backend et envoie des réponses aux requêtes du client.

**Apollo Engine** est une infrastructure hébergée (SaaS) qui sert d'intermédiaire entre le client et votre serveur, fournissant un cache, des rapports de performance, des mesures de charge, un suivi des erreurs, des statistiques d'utilisation des champs de schéma, des statistiques historiques et bien plus encore. Il est actuellement gratuit jusqu'à 1 million de requêtes par mois, et c'est la seule partie d'Apollo qui n'est pas open source et gratuite. Il fournit un financement pour la partie open source du projet.

Il est important de noter que ces trois outils ne sont pas liés ensemble de quelque manière que ce soit, et vous pouvez utiliser uniquement Apollo Client pour interfacer avec une API tierce, ou servir une API en utilisant Apollo Server sans avoir de client du tout, par exemple.

#### Certains avantages de l'utilisation d'Apollo

Tout est **compatible avec la spécification standard GraphQL**, donc il n'y a pas de technologie propriétaire ou incompatible dans Apollo.

Mais il est très pratique d'avoir tous ces outils ensemble sous un même toit comme une suite complète pour tous vos besoins liés à GraphQL.

Apollo s'efforce d'être facile à utiliser et facile à contribuer.

Apollo Client et Apollo Server sont tous deux des projets communautaires, construits par la communauté, pour la communauté. Apollo est soutenu par le [Meteor Development Group](https://www.meteor.io/) (la société derrière [Meteor](https://flaviocopes.com/meteor-hello-world/)), un framework JavaScript très populaire.

Apollo se concentre sur **le maintien des choses simples**. C'est quelque chose de clé pour le succès d'une technologie qui veut devenir populaire. Beaucoup de technologies, frameworks ou bibliothèques peuvent être excessifs pour 99% des petites ou moyennes entreprises, et sont vraiment adaptés aux grandes entreprises avec des besoins très complexes.

### Apollo Client

[Apollo Client](https://www.apollographql.com/client) est le principal client JavaScript pour GraphQL. Puisqu'il est piloté par la communauté, il est conçu pour vous permettre de construire des composants d'interface utilisateur qui interfacent avec les données GraphQL — soit en affichant ces données, soit en effectuant des mutations lorsque certaines actions se produisent.

Vous n'avez pas besoin de tout changer dans votre application pour utiliser Apollo Client. Vous pouvez commencer avec juste une petite couche et une requête, et développer à partir de là.

Surtout, Apollo Client est construit pour être simple, petit et flexible dès le départ.

Dans cet article, je vais détailler le processus d'utilisation d'Apollo Client dans une application React.

J'utiliserai l'[API GraphQL de GitHub](https://developer.github.com/v4/) comme serveur.

### Démarrer une application React

J'utilise `[create-react-app](https://github.com/facebook/create-react-app)` pour configurer l'application React, ce qui est très pratique et ajoute simplement les bases de ce dont nous avons besoin :

```
npx create-react-app myapp
```

> `_npx_` _est une commande disponible dans les dernières versions de npm. Mettez à jour npm si vous n'avez pas cette commande._

Démarrez le serveur local de l'application avec

```
yarn start
```

Ouvrez `src/index.js` :

```
import React from 'react'import ReactDOM from 'react-dom'import './index.css'import App from './App'import registerServiceWorker from './registerServiceWorker'ReactDOM.render(<App />, document.getElementById('root'))registerServiceWorker()
```

et supprimez tout ce contenu.

### Commencer avec Apollo Boost

Apollo Boost est le moyen le plus simple de commencer à utiliser Apollo Client sur un nouveau projet. Nous allons l'installer en plus de `react-apollo` et `graphql`.

Dans la console, exécutez

```
yarn add apollo-boost react-apollo graphql
```

ou avec npm :

```
npm install apollo-boost react-apollo graphql --save
```

### Créer un objet ApolloClient

Vous commencez par importer ApolloClient depuis `apollo-client` dans `index.js` :

```
import { ApolloClient } from 'apollo-client'const client = new ApolloClient()
```

Par défaut, Apollo Client utilise le point de terminaison `/graphql` sur l'hôte actuel, alors utilisons un **Apollo Link** pour spécifier les détails de la connexion au serveur GraphQL en définissant l'URI du point de terminaison GraphQL.

### Apollo Links

Un Apollo Link est représenté par un objet `HttpLink`, que nous importons depuis `apollo-link-http`.

Apollo Link nous fournit un moyen de décrire comment nous voulons obtenir le résultat d'une opération GraphQL, et ce que nous voulons faire avec la réponse.

En bref, vous créez plusieurs instances d'Apollo Link qui agissent toutes sur une requête GraphQL les unes après les autres, fournissant le résultat final que vous souhaitez. Certains Links peuvent vous donner l'option de réessayer une requête si elle n'est pas réussie, de regrouper les requêtes, et bien plus encore.

Nous allons ajouter un Apollo Link à notre instance Apollo Client pour utiliser l'URI du point de terminaison GraphQL de GitHub `[https://api.github.com/graphql](https://api.github.com/graphql)`

```
import { ApolloClient } from 'apollo-client'import { HttpLink } from 'apollo-link-http'const client = new ApolloClient({  link: new HttpLink({ uri: 'https://api.github.com/graphql' })})
```

### Mise en cache

Nous n'avons pas encore terminé. Avant d'avoir un exemple fonctionnel, nous devons également indiquer à `ApolloClient` quelle [stratégie de mise en cache](https://www.apollographql.com/docs/react/basics/caching.html) utiliser : `InMemoryCache` est la stratégie par défaut et c'est une bonne stratégie pour commencer.

```
import { ApolloClient } from 'apollo-client'import { HttpLink } from 'apollo-link-http'import { InMemoryCache } from 'apollo-cache-inmemory'const client = new ApolloClient({  link: new HttpLink({ uri: 'https://api.github.com/graphql' }),  cache: new InMemoryCache()})
```

### Utiliser `ApolloProvider`

Maintenant, nous devons connecter Apollo Client à notre arbre de composants. Nous le faisons en utilisant `ApolloProvider`, en enveloppant notre composant d'application dans le fichier principal React :

```
import React from 'react'import ReactDOM from 'react-dom'import { ApolloClient } from 'apollo-client'import { HttpLink } from 'apollo-link-http'import { InMemoryCache } from 'apollo-cache-inmemory'import { ApolloProvider } from 'react-apollo'import App from './App'const client = new ApolloClient({  link: new HttpLink({ uri: 'https://api.github.com/graphql' }),  cache: new InMemoryCache()})ReactDOM.render(  <ApolloProvider client={client}>    <App />  </ApolloProvider>,  document.getElementById('root'))
```

Cela est suffisant pour rendre l'écran par défaut de `create-react-app`, avec Apollo Client initialisé :

![Image](https://cdn-media-1.freecodecamp.org/images/He9moRbQxqfLHpSuSiBHDMXppwRq2CDhytKz)

### La balise de modèle `gql`

Nous sommes maintenant prêts à faire quelque chose avec Apollo Client, et nous allons récupérer des données depuis l'API GitHub et les rendre.

Pour ce faire, nous devons importer la balise de modèle `gql` :

```
import gql from 'graphql-tag'
```

Toute requête GraphQL sera construite en utilisant cette balise de modèle, comme ceci :

```
const query = gql`  query {    ...  }`
```

### Effectuer une requête GraphQL

`gql` était le dernier élément dont nous avions besoin dans notre boîte à outils.

Nous sommes maintenant prêts à faire quelque chose avec Apollo Client, et nous allons récupérer des données depuis l'API GitHub et les rendre.

#### Obtenir un jeton d'accès pour l'API

La première chose à faire est d'[obtenir un jeton d'accès personnel](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) depuis GitHub.

GitHub facilite cela en fournissant une interface à partir de laquelle vous pouvez sélectionner toutes les permissions dont vous pourriez avoir besoin :

![Image](https://cdn-media-1.freecodecamp.org/images/cZXXNubCl6sKWtoZRt90VupyIIEptCWfI2OD)

Pour les besoins de ce tutoriel, vous n'avez besoin d'aucune de ces permissions. Elles sont destinées à l'accès aux données privées de l'utilisateur, mais nous allons simplement interroger les données des dépôts publics.

Le jeton que vous obtenez est un **jeton Bearer OAuth 2.0**.

Vous pouvez facilement le tester en exécutant depuis la ligne de commande :

```
$ curl -H "Authorization: bearer ***_VOTRE_JETON_ICI_***" -X POST -d " \ { \   \"query\": \"query { viewer { login }}\" \ } \" https://api.github.com/graphql
```

ce qui devrait vous donner le résultat

```
{"data":{"viewer":{"login":"***_VOTRE_NOM_DE_CONNEXION_***"}}}
```

ou

```
{  "message": "Bad credentials",  "documentation_url": "https://developer.github.com/v4"}
```

si quelque chose s'est mal passé.

#### Utiliser un Apollo Link pour s'authentifier

Donc, nous devons envoyer l'en-tête **Authorization** avec notre requête GraphQL, tout comme nous l'avons fait dans la requête `curl` ci-dessus.

Nous pouvons faire cela avec Apollo Client en créant un middleware Apollo Link. Commencez par installer `[apollo-link-context](https://www.npmjs.com/package/apollo-link-context)` :

```
npm install apollo-link-context
```

Ce package nous permet d'ajouter un mécanisme d'authentification en définissant le contexte de nos requêtes.

Nous pouvons l'utiliser dans ce code en référençant la fonction `setContext` de cette manière :

```
const authLink = setContext((_, { headers }) => {  const token = '***VOTRE_JETON**'  return {    headers: {      ...headers,      authorization: `Bearer ${token}`    }  }})
```

et une fois que nous avons ce nouveau Apollo Link, nous pouvons le [composer](https://www.apollographql.com/docs/link/composition.html) avec le `HttpLink` que nous avions déjà en utilisant la méthode `concat()` sur un lien :

```
const link = authLink.concat(httpLink)
```

Voici le code complet pour le fichier `src/index.js` avec le code que nous avons actuellement :

```
import React from 'react'import ReactDOM from 'react-dom'import { ApolloClient } from 'apollo-client'import { HttpLink } from 'apollo-link-http'import { InMemoryCache } from 'apollo-cache-inmemory'import { ApolloProvider } from 'react-apollo'import { setContext } from 'apollo-link-context'import gql from 'graphql-tag'import App from './App'const httpLink = new HttpLink({ uri: 'https://api.github.com/graphql' })const authLink = setContext((_, { headers }) => {  const token = '***VOTRE_JETON**'  return {    headers: {      ...headers,      authorization: `Bearer ${token}`    }  }})const link = authLink.concat(httpLink)const client = new ApolloClient({  link: link,  cache: new InMemoryCache()})ReactDOM.render(  <ApolloProvider client={client}>    <App />  </ApolloProvider>,  document.getElementById('root'))
```

> _AVERTISSEMENT ⚠️ ? Gardez à l'esprit que ce code est un **exemple** à des fins éducatives. Il expose votre API GraphQL GitHub pour que le monde entier puisse la voir dans votre code frontal. Le code de production doit garder ce jeton privé._

Nous pouvons maintenant faire la première requête GraphQL en bas de ce fichier, et cette requête exemple demande les noms et les propriétaires des 10 dépôts les plus populaires avec plus de 50k étoiles :

```
const POPULAR_REPOSITORIES_LIST = gql`{  search(query: "stars:>50000", type: REPOSITORY, first: 10) {    repositoryCount    edges {      node {        ... on Repository {          name          owner {            login          }          stargazers {            totalCount          }        }      }    }  }}`client.query({ query: POPULAR_REPOSITORIES_LIST }).then(console.log)
```

L'exécution de ce code retourne avec succès le résultat de notre requête dans la console du navigateur :

![Image](https://cdn-media-1.freecodecamp.org/images/DPyIddPqoBytsvccGzq1K4n4PPGDaOOuwEtP)

### Afficher un ensemble de résultats de requête GraphQL dans un composant

Ce que nous avons vu jusqu'à présent est déjà cool. Ce qui est encore plus cool, c'est d'utiliser l'ensemble de résultats GraphQL pour rendre vos composants.

Nous laissons Apollo Client supporter le fardeau (ou la joie) de récupérer les données et de gérer toutes les choses de bas niveau. Cela nous permet de nous concentrer sur l'affichage des données en utilisant l'améliorateur de composant `graphql` offert par `react-apollo` :

```
import React from 'react'import { graphql } from 'react-apollo'import { gql } from 'apollo-boost'const POPULAR_REPOSITORIES_LIST = gql`{  search(query: "stars:>50000", type: REPOSITORY, first: 10) {    repositoryCount    edges {      node {        ... on Repository {          name          owner {            login          }          stargazers {            totalCount          }        }      }    }  }}`const App = graphql(POPULAR_REPOSITORIES_LIST)(props =>  <ul>    {props.data.loading ? '' : props.data.search.edges.map((row, i) =>      <li key={row.node.owner.login + '-' + row.node.name}>        {row.node.owner.login} / {row.node.name}: {' '}        <strong>          {row.node.stargazers.totalCount}        </strong>      </li>    )}  </ul>)export default App
```

Voici le résultat de notre requête rendu dans le composant ?

![Image](https://cdn-media-1.freecodecamp.org/images/bGd9-rLBDlC0LElJiyHIfPFsh206T5OXj3p0)

### Apollo Server

Un serveur GraphQL a pour tâche d'accepter les requêtes entrantes sur un point de terminaison, d'interpréter la requête et de rechercher toutes les données nécessaires pour répondre aux besoins du client.

Il existe de nombreuses implémentations différentes de serveurs GraphQL pour chaque langage possible.

**Apollo Server est une implémentation de serveur GraphQL pour JavaScript, en particulier pour la plateforme Node.js**.

Il supporte de nombreux frameworks Node.js populaires, notamment :

* [Express](https://expressjs.com/)
* [Hapi](https://hapijs.com/)
* [Koa](http://koajs.com/)
* [Restify](http://restify.com/)

Apollo Server nous donne essentiellement trois choses :

* Un moyen de décrire nos données avec un **schéma**.
* Le framework pour les **résolveurs**, qui sont des fonctions que nous écrivons pour récupérer les données nécessaires pour répondre à une requête.
* Il facilite la gestion de l'**authentification** pour notre API.

Pour les besoins de l'apprentissage des bases d'Apollo Server, nous n'allons utiliser aucun des frameworks Node.js supportés. Au lieu de cela, nous allons utiliser quelque chose qui a été construit par l'équipe Apollo, quelque chose de vraiment génial qui sera la base de notre apprentissage : Launchpad.

### Launchpad

[Launchpad](https://launchpad.graphql.com/) est un projet qui fait partie de l'ombrelle des produits Apollo, et c'est un outil assez incroyable qui permet d'écrire du code dans le cloud et de créer un serveur Apollo en ligne, tout comme nous exécuterions un extrait de code sur Codepen, JSFiddle ou JSBin.

Sauf qu'au lieu de construire un outil visuel qui sera isolé là-bas, et destiné uniquement à être une vitrine ou un outil d'apprentissage, avec Launchpad nous créons une API GraphQL. Elle sera accessible publiquement.

Chaque projet sur Launchpad est appelé **pad** et a son URL de point de terminaison GraphQL, comme :

```
https://1jzxrj129.lp.gql.zone/graphql
```

Une fois que vous avez construit un pad, Launchpad vous donne la possibilité de télécharger le code complet de l'application Node.js qui l'exécute, et vous devez simplement exécuter `npm install` et `npm start` pour avoir une copie locale de votre serveur Apollo GraphQL.

Pour résumer, c'est un **excellent outil pour apprendre, partager et prototyper**.

### Le Hello World d'Apollo Server

Chaque fois que vous créez un nouveau _pad_ Launchpad, vous êtes présenté avec le Hello, World! d'Apollo Server. Plongeons-nous dedans.

Tout d'abord, vous importez la fonction `makeExecutableSchema` depuis `graphql-tools`.

```
import { makeExecutableSchema } from 'graphql-tools'
```

Cette fonction est utilisée pour créer un objet `GraphQLSchema`, en lui fournissant une définition de schéma (écrite dans le [langage de schéma GraphQL](http://graphql.org/learn/schema/)) et un ensemble de **résolveurs**.

Une définition de schéma est une chaîne de littéral de modèle contenant la description de notre requête et les types associés à chaque champ :

```
const typeDefs = `  type Query {    hello: String  }`
```

Un **résolveur** est un objet qui mappe les champs dans le schéma aux fonctions de résolution. Il est capable de rechercher des données pour répondre à une requête.

Voici un résolveur simple contenant la fonction de résolution pour le champ `hello`, qui retourne simplement la chaîne `Hello world!` :

```
const resolvers = {  Query: {    hello: (root, args, context) => {      return 'Hello world!'    }  }}
```

Étant donné ces deux éléments, la définition du schéma et le résolveur, nous utilisons la fonction `makeExecutableSchema` que nous avons importée précédemment pour obtenir un objet `GraphQLSchema`, que nous assignons à la constante `schema`.

```
export const schema = makeExecutableSchema({ typeDefs, resolvers })
```

C'est **tout** ce dont vous avez besoin pour servir une API simple en lecture seule. Launchpad s'occupe des petits détails.

Voici le code complet pour l'exemple simple Hello World :

```
import { makeExecutableSchema } from 'graphql-tools'const typeDefs = `  type Query {    hello: String  }`const resolvers = {  Query: {    hello: (root, args, context) => {      return 'Hello world!'    }  }}export const schema = makeExecutableSchema({  typeDefs,  resolvers})
```

Launchpad fournit un outil intégré génial pour consommer l'API :

![Image](https://cdn-media-1.freecodecamp.org/images/QFNQVQsPIXbZX3leOK84JiPVPV0o228Z-pDh)

Et comme je l'ai dit précédemment, l'API est accessible publiquement, donc vous devez simplement vous connecter et sauvegarder votre pad.

J'ai créé un pad qui expose son point de terminaison à `https://kqwwkp0pr7.lp.gql.zone/graphql`, alors essayons-le en utilisant `curl` depuis la ligne de commande :

```
$ curl \  -X POST \  -H "Content-Type: application/json" \  --data '{ "query": "{ hello }" }' \  https://kqwwkp0pr7.lp.gql.zone/graphql
```

ce qui nous donne avec succès le résultat que nous attendons :

```
{  "data": {    "hello": "Hello world!"  }}
```

### Exécuter le serveur GraphQL localement

Nous avons mentionné que tout ce que vous créez sur Launchpad est téléchargeable, alors continuons.

Le package est composé de deux fichiers. Le premier, `schema.js` est ce que nous avons ci-dessus.

Le second, `server.js`, était invisible dans Launchpad et c'est ce qui fournit la fonctionnalité sous-jacente du serveur Apollo, alimenté par [Express](https://expressjs.com/), le framework Node.js populaire.

Ce n'est pas l'exemple le plus simple d'une configuration de serveur Apollo, donc pour les besoins de l'explication, je vais le remplacer par un exemple plus simple (mais n'hésitez pas à étudier cela après avoir compris les bases).

### Votre premier code Apollo Server

Tout d'abord, exécutez `npm install` et `npm start` sur le code Launchpad que vous avez téléchargé.

Le serveur node que nous avons initialisé précédemment utilise [nodemon](https://nodemon.io/) pour redémarrer le serveur lorsque les fichiers changent, donc lorsque vous changez le code, le serveur est redémarré avec vos modifications appliquées.

Ajoutez ce code dans `server.js` :

```
const express = require('express')const bodyParser = require('body-parser')const { graphqlExpress } = require('apollo-server-express')const { schema } = require('./schema')const server = express()server.use('/graphql', bodyParser.json(), graphqlExpress({ schema }))server.listen(3000, () => {  console.log('GraphQL listening at http://localhost:3000/graphql')})
```

Avec seulement 11 lignes, ceci est **beaucoup plus simple** que le serveur configuré par Launchpad, car nous avons supprimé toutes les choses qui rendaient ce code plus flexible pour leurs besoins.

Coder vous oblige à prendre des décisions difficiles : combien de flexibilité avez-vous besoin maintenant ? À quel point est-il important d'avoir un code propre et compréhensible que vous pouvez reprendre six mois plus tard et modifier facilement, ou transmettre à d'autres développeurs et membres de l'équipe afin qu'ils puissent être productifs en aussi peu de temps que nécessaire ?

Voici ce que fait le code :

Nous importons d'abord quelques bibliothèques que nous allons utiliser.

* `**express**` qui alimentera la fonctionnalité réseau sous-jacente pour exposer le point de terminaison
* `**bodyParser**` est le middleware de parsing du corps de Node
* `**graphqlExpress**` est l'objet Apollo Server pour Express

```
const express = require('express')const bodyParser = require('body-parser')const { graphqlExpress } = require('apollo-server-express')
```

Ensuite, nous importons l'objet `GraphQLSchema` que nous avons créé dans le fichier schema.js ci-dessus en tant que `Schema` :

```
const { schema } = require('./schema')
```

Voici une configuration standard d'Express, et nous initialisons simplement un serveur sur le port `3000`

```
const server = express()
```

Nous sommes maintenant prêts à initialiser Apollo Server :

```
graphqlExpress({ schema })
```

et nous passons cela comme un callback à notre point de terminaison pour les requêtes HTTP JSON :

```
server.use('/graphql', bodyParser.json(), graphqlExpress({ schema }))
```

Tout ce dont nous avons besoin maintenant est de démarrer Express :

```
server.listen(3000, () => {  console.log('GraphQL listening at http://localhost:3000/graphql')})
```

### Ajouter un point de terminaison GraphiQL

Si vous utilisez GraphiQL, vous pouvez facilement ajouter un point de terminaison `/graphiql`, pour consommer avec l'[IDE interactif GraphiQL dans le navigateur](https://github.com/graphql/graphiql) :

```
server.use('/graphiql', graphiqlExpress({  endpointURL: '/graphql',  query: ``}))
```

Nous devons maintenant simplement démarrer le serveur Express :

```
server.listen(PORT, () => {  console.log('GraphQL listening at http://localhost:3000/graphql')  console.log('GraphiQL listening at http://localhost:3000/graphiql')})
```

Vous pouvez le tester en utilisant `curl` à nouveau :

```
$ curl \  -X POST \  -H "Content-Type: application/json" \  --data '{ "query": "{ hello }" }' \  http://localhost:3000/graphql
```

Cela vous donnera le même résultat que ci-dessus, où vous avez appelé les serveurs Launchpad :

```
{  "data": {    "hello": "Hello world!"  }}
```

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)