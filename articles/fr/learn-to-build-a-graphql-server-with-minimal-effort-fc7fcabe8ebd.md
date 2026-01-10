---
title: Apprendre à construire un serveur GraphQL avec un effort minimal
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T21:45:22.000Z'
originalURL: https://freecodecamp.org/news/learn-to-build-a-graphql-server-with-minimal-effort-fc7fcabe8ebd
coverImage: https://cdn-media-1.freecodecamp.org/images/0*5WsW82sZj2yuVHOt
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Apprendre à construire un serveur GraphQL avec un effort minimal
seo_desc: 'By Ian Wilson

  Today in web development, we will be learning how to:


  Easily setup a GraphQL Server with NodeJS

  Mock data without a database using json-server

  Build a CRUD app that speaks GraphQL

  How Apollo saves us a lot of time and effort


  If any of...'
---

Par Ian Wilson

Aujourd'hui en développement web, nous allons apprendre comment :

* Configurer facilement un serveur GraphQL avec NodeJS
* Simuler des données sans base de données en utilisant json-server
* Construire une application CRUD qui utilise GraphQL
* Comment Apollo nous fait gagner beaucoup de temps et d'efforts

Si l'un de ces éléments vous intéresse, continuez à lire ! Assurez-vous de consulter le [code source de ce dépôt](https://github.com/iwilsonq/social-graphql) si vous souhaitez vous référer à l'exemple complet.

### Introduction en douceur

Il y a quelques années, j'ai lancé mon premier serveur HTTP Node avec Express. Cela n'a pris que 6 lignes de code de ma part.

```javascript
const express = require('express')
const app = express()

app.get('/', function(req, res) { 
  res.send({ hello: 'there' })
})

app.listen(3000, () => 'Listening at http://localhost:3000')
```

Cela a réduit considérablement l'effort nécessaire pour construire des applications côté serveur, surtout si l'on considère que nous pouvions utiliser notre JavaScript familier.

Les vannes se sont ouvertes pour d'innombrables tutoriels et vidéos sur la configuration d'un serveur Node, généralement pour construire une sorte d'API REST CRUD en un temps record.

CRUD fait référence à une application, un serveur ou un backend qui peut créer, lire, mettre à jour et supprimer — peut-être à partir d'une base de données réelle.

Mais nous sommes en 2018, nous pouvons faire des choses beaucoup plus cool.

Remplaçons REST par GraphQL.

### Entrée de GraphQL

GraphQL est une couche de manipulation et de récupération de données déclarative qui rend la consommation des API plus conviviale pour le client.

Certains avantages de la consommation de données via un serveur GraphQL sont :

* Vous obtenez exactement les données que vous demandez en spécifiant les champs dont vous avez besoin.
* Moins de requêtes et moins de sur-récupération. Les requêtes GraphQL sont généralement suffisamment spécifiques pour éviter de récupérer des enregistrements ou des champs inutiles.
* Schémas fortement typés, par opposition aux champs JSON bruts qui n'ont pas d'opinion sur le type de données retournées.
* GraphQL playground pour l'exploration de données qui vient avec l'autocomplétion et une documentation intégrée. Si vous aimez travailler avec [Postman](https://www.getpostman.com/), vous vous sentirez chez vous avec cette interface.

Ce dernier point en particulier facilite grandement l'intégration de nouveaux développeurs.

Ils n'ont plus à étudier vos centaines de points de terminaison sur swagger, car ils peuvent explorer les types et les relations entre eux dans cette interface.

Plus sur cela bientôt, passons au codage.

### Commencer et installer les dépendances

Commençons par créer un répertoire et initialiser un fichier `package.json`.

```
mkdir social-graphql && cd social-graphql && npm init -y
```

Notre stack technologique ressemblera à ceci :

* JavaScript fonctionnant avec Node (pas de code côté client aujourd'hui)
* Babel pour écrire du ES6 moderne
* Express pour configurer rapidement un serveur HTTP
* Apollo Server pour toutes les utilités GraphQL utiles qui nous aident à configurer le serveur et à construire des schémas
* json-server pour tester sur un ensemble de données fictif (beaucoup plus facile que d'interroger une base de données réelle)

```
npm install -S express apollo-server-express graphql json-server axios
```

En outre, nous aurons quelques dépendances de développement qui nous aideront.

```
npm install -D babel-cli babel-preset-env nodemon npm-run-all
```

Avec les dépendances installées, nous pouvons commencer à coder.

#### Commencer avec un serveur HTTP de base

Créons un serveur HTTP qui gère la route d'index. C'est-à-dire, si je lance le serveur et navigue vers [http://localhost:3500](http://localhost:3500), je devrais voir le message JSON, au lieu de "Cannot GET "/".

Créez un fichier `index.js` :

```javascript
import express from 'express'

const PORT = process.env.PORT || 3500
const app = express()

app.get('/', function(req, res) {
  res.send({ hello: 'there!' })
})

app.listen(PORT, () => `Listening at http://localhost:${PORT}`)
```

Cela est très similaire au code au début de l'article, à l'exception de la syntaxe d'importation et du port qui est configurable via des variables d'environnement.

Pour faire fonctionner la syntaxe d'importation ici, nous allons devoir tirer parti de notre présélection babel. Créez un fichier appelé `.babelrc` et :

```
{
  "presets": ["env"]
}
```

Enfin, pour exécuter le serveur, mettez à jour le script de démarrage dans `package.json` comme suit :

```
"scripts": {
  "dev:api": "nodemon --exec 'babel-node index.js'"
}
```

Puis entrez `npm run dev:api` dans votre terminal. En naviguant vers [http://localhost:3500](http://localhost:3500), vous pourrez voir une réponse qui dit "hello: there!".

Contrairement au `node index.js` plus typique dans un script `npm start`, nous utilisons une commande dev avec nodemon exécutant babel-node.

Nodemon redémarre votre serveur de développement chaque fois que vous enregistrez des fichiers afin que vous n'ayez pas à le faire. Habituellement, il s'exécute avec `node`, mais nous lui disons de s'exécuter avec `babel-node` pour qu'il gère nos imports ES6.

#### Mise à niveau vers Apollo

D'accord, nous avons assemblé un serveur HTTP de base qui peut servir des points de terminaison REST. Mettons-le à jour afin de servir GraphQL.

```js
import express from 'express'
import { ApolloServer } from 'apollo-server-express'
import { resolvers, typeDefs } from './schema'

const PORT = process.env.PORT || 3500
const app = express()

const server = new ApolloServer({
  typeDefs,
  resolvers,
  playground: true
})

server.applyMiddleware({ app })

app.get('/', (req, res) => {
  res.send({ hello: 'there!' })
})

app.listen(PORT, () =>
  console.log(`Listening at http://localhost:${PORT}/graphql`)
)
```

Ensuite, dans un nouveau fichier que j'appellerai `schema.js`, insérez :

```js
import { gql } from 'apollo-server-express'

export const typeDefs = gql`
  type Query {
    users: String
  }
`

export const resolvers = {
  Query: {
    users() {
      return "This will soon return users!"
    }
  }
}
```

#### Les Résolveurs et le Schéma (définitions de type)

Ici, si vous êtes nouveau dans le travail avec GraphQL, vous verrez cette syntaxe amusante que nous attribuons à `typeDefs`.

En JavaScript ES6, nous pouvons invoquer une fonction en utilisant des backticks comme nous le faisons avec `gql`. En termes de JavaScript vanilla, vous pouvez le lire comme ceci :

```
gql.apply(null, ["type Query {\n users: String \n }"])
```

Essentiellement, cela appelle `gql` avec un tableau d'arguments. Il se trouve que l'écriture de chaînes multilignes est pratique lors de l'expression d'une requête de type JSON.

Si vous exécutez toujours le serveur, rendez-vous sur [http://localhost:3500/graphql](http://localhost:3500/graphql). Ici, vous pourrez voir une interface fantastique pour tester nos requêtes.

![Image](https://cdn-media-1.freecodecamp.org/images/Ta632PscgIFxlBanWZNUfTyGQ28n5qdWnkrt)

C'est exact, plus besoin de lancer des cURLs vers un point de terminaison obscur, nous pouvons tester nos requêtes avec autocomplétion, mise en forme et documentation intégrée. C'est aussi prêt à l'emploi avec Apollo, donc vous n'avez pas besoin d'installer des packages ou des applications supplémentaires.

Maintenant, rendons cette requête un peu plus intéressante.

#### Implémentation d'une requête GraphQL du monde réel : Lister les utilisateurs

Avant de plonger trop profondément dans cette section, assurez-vous de copier `db.json` depuis [ce dépôt](https://github.com/iwilsonq/social-graphql) dans votre répertoire de travail aux côtés de index.js et schema.js.

Ensuite, mettez à jour les scripts dans `package.json` :

```js
"scripts": {
  "dev": "npm-run-all --parallel dev:*",
  "dev:api": "nodemon --exec 'babel-node index.js' --ignore db.json",
  "dev:json": "json-server --watch db.json"
}
```

Relancez le serveur avec `npm run dev` et continuez.

Dans un serveur GraphQL, il y a un concept de **requête racine**. Ce type de requête est le point d'entrée pour toute demande de récupération de données vers notre schéma GraphQL. Pour nous, cela ressemble à ceci :

```js
type Query {
  users: String
}
```

Si nous servons des utilisateurs, des posts ou des avions, le client qui demande des données doit le faire en passant par la requête racine.

```js
type Query {
  users: [User] # ici les "[]" signifient que ceux-ci retournent des listes
  posts: [Post]
  airplanes: [Airplane]
}
```

Par exemple, si nous voulions définir une nouvelle requête sur notre serveur, nous devrions mettre à jour au moins deux endroits.

1. Ajouter la requête sous le type Query dans nos définitions de type.
2. Ajouter une fonction de résolveur sous l'objet Query dans notre objet de résolveurs.

Nous devrions ensuite nous assurer que nous avons le type correct des données de retour. Pour une liste d'utilisateurs, cela signifie retourner un tableau d'objets, chacun avec un nom, un email, un âge, des amis et un ID.

Notre schéma actuel a notre requête users qui retourne une simple chaîne. Ce n'est pas bon, car nous attendons des données **utilisateur** à revenir de cette route.

Mettez à jour `schema.js` comme suit :

```js
export const typeDefs = gql`
  type User {
    id: ID
    name: String
    age: Int
    email: String
    friends: [User]
  }

  type Query {
    users: [User]
  }
`
```

Super, nous avons le type utilisateur, et la requête racine qui retourne une liste d'utilisateurs.

Mettons à jour le résolveur :

```js
export const resolvers = {
  Query: {
    users() {
      return userModel.list()
    }
  }
}
```

À l'intérieur de notre résolveur, nous appelons list depuis `userModel`, que nous n'avons pas encore défini.

À l'intérieur d'un nouveau fichier appelé `models.js`, ajoutez ce qui suit :

```js
import axios from 'axios'

class User {
  constructor() {
    this.api = axios.create({
      baseURL: 'http://localhost:3000' // point de terminaison json-server
    })
  }

  list() {
    return this.api.get('/users').then(res => res.data)
  }
}

export default new User()
```

Cette classe forme une couche d'abstraction sur la logique qui gère directement nos données.

Enfin, en haut de `schema.js`, ajoutez cette importation :

```
import userModel from './models'
```

Retournez à [http://localhost:3500/graphql](http://localhost:3500/graphql), collez et exécutez cette requête :

```js
query Users {
  users {
    id
    name
    email
  }
}
```

La requête utilisateur semble maintenant un peu plus excitante ! Pour chaque utilisateur dans notre fichier `db.json`, nous avons retourné leur id, nom et email.

![Image](https://cdn-media-1.freecodecamp.org/images/2lOr6slP47Ck6PE88U2umwsm4iACvKyG5NoO)

Puisque nous utilisons json-server hébergé sur un port local, nous utilisons le modèle comme s'il récupérait des données depuis une API distante.

Dans de nombreux cas, notre modèle ferait des appels de base de données ou récupérerait des données depuis un magasin clé-valeur comme firebase.

Cependant, du point de vue d'un client, ils n'ont aucune idée de la manière dont le modèle récupère les données — ils ne connaissent que la forme des données.

Cette abstraction fait de GraphQL un outil idéal pour résoudre les données provenant de plusieurs sources en une seule requête.

#### Amis d'amis : Une requête plus intense

Obtenir une liste d'utilisateurs est sympa, et le GraphQL playground aussi. Mais jusqu'à présent, vous pourriez facilement faire le même travail avec un point de terminaison REST.

Et si vous vouliez récupérer les utilisateurs, ainsi que tous les amis d'un utilisateur particulier ? Nous voulons exécuter une requête comme celle-ci :

```js
query UsersAndFriends {
  users {
    id
    name
    friends {
      id
      name
    }
  }
}
```

Pour ce faire, notez la forme des données dans notre fichier `db.json` : chaque utilisateur a un champ friends qui est un tableau d'objets indexés par ID.

En gros, nous allons faire une sorte de requête pour chaque ID que nous trouvons, pour chaque utilisateur.

Cela semble-t-il être un calcul intense ?

Oui, nous exécuterions une nouvelle requête vers notre magasin de données pour chaque ami de chaque utilisateur que nous récupérons.

La mise en œuvre d'une sorte de cache aiderait énormément à réduire la quantité de travail nécessaire pour compléter la requête — mais ne nous inquiétons pas de l'optimiser pour l'instant.

Dans `models.js`, ajoutez cette méthode `find` à la classe User :

```js
class User {
  constructor() {
    this.api = axios.create({
      baseURL: 'http://localhost:3000' // point de terminaison json-server
    })
  }

  list() {
    return this.api.get('/users').then(res => res.data)
  }

  find(id) {
    return this.api.get(`/users/${id}`).then(res => res.data)
  }
}
```

Maintenant, nous pouvons utiliser cette méthode dans un nouveau résolveur User. La différence dans ce résolveur est qu'il est utilisé lorsqu'il essaie de résoudre les connexions à un type particulier, `friends` ici.

Sinon, la requête ne saurait pas comment résoudre une liste d'utilisateurs lorsqu'elle voit `friends`.

```js
export const resolvers = {
  Query: {
    users() {
      return userModel.list()
    }
  },
  User: {
    friends(source) {
      if (!source.friends || !source.friends.length) {
        return
      }

      return Promise.all(
        source.friends.map(({ id }) => userModel.find(id))
      )
    }
  },
}
```

Dans la méthode friends, source est la valeur parente que la fonction de résolveur est appelée avec. C'est-à-dire, pour l'utilisateur avec l'id 0, Peck Montoya, la valeur de source est l'objet entier avec la liste des ids d'amis.

Pour les requêtes racines, source est le plus souvent indéfini, car la requête racine n'est pas résolue à partir d'une source particulière.

La méthode friends retourne lorsque toutes les requêtes pour trouver des utilisateurs individuels ont été résolues.

Essayez maintenant d'exécuter cette requête si vous ne l'avez pas fait plus tôt :

```js
query UsersAndFriends {
  users {
    id
    name
    friends {
      id
      name
    }
  }
}
```

#### Mutations : Créer un utilisateur

Jusqu'à présent, nous n'avons fait que récupérer des données. Et si nous voulions mutuer des données ?

Commençons par créer un utilisateur avec un nom et un âge.

Jetez un coup d'œil à cette mutation :

```js
mutation CreateUser($name: String!, $email: String, $age: Int) {
  createUser(name: $name, email: $email, age: $age) {
    name
    email
    age
  }
}
```

Quelques différences à première vue :

* nous désignons ce code avec "mutation" plutôt que "query"
* nous passons deux ensembles d'arguments similaires

Les arguments sont essentiellement des déclarations de type pour les variables attendues par notre requête.

S'il y a une incompatibilité entre ces types et ceux passés par un client tel qu'une application web ou mobile, le serveur GraphQL générera une erreur.

Pour faire fonctionner cette requête maintenant, mettons d'abord à jour la classe User dans `model.js` :

```js
create(data) {
  data.friends = data.friends 
    ? data.friends.map(id => ({ id })) 
    : []

  return this.api.post('/users', data).then(res => res.data)
}
```

Lorsque nous lançons cette requête, json-server ajoutera un nouvel utilisateur avec les données que nous avons passées.

Maintenant, mettez à jour `schema.js` comme suit :

```js
export const typeDefs = gql`

  # other types...

  type Mutation {
    createUser(name: String!, email: String, age: Int): User
  }
`

export const resolvers = {
  // other resolvers...
  Mutation: {
    createUser(source, args) {
      return userModel.create(args)
    }
  }
}
```

À ce stade, la requête devrait fonctionner. Mais nous pouvons faire un peu mieux.

#### Simplification des arguments de requête et de mutation

Plutôt que d'écrire chaque argument pour la mutation, nous pouvons définir des **types d'entrée**. Cela rendra les mutations et requêtes que nous écrivons plus tard plus composables.

```javascript
export const typeDefs = gql`

  # other types...

  input CreateUserInput {
    id: Int
    name: String
    age: Int
    email: String
    friends: [Int]
  }

  type Mutation {
    createUser(input: CreateUserInput!): User
  }
`

export const resolvers = {
  // other resolvers...
  Mutation: {
    createUser(source, args) {
      return userModel.create(args.input)
    }
  }
}

```

Voyez-vous que si nous voulions implémenter une mutation UpdateUser, nous pourrions probablement tirer parti de ce nouveau type d'entrée.

Essayez maintenant cette mutation :

```javascript
mutation CreateUser($input: CreateUserInput!) {
  createUser(input: $input) {
    name
    email
    age
    friends {
      id
      name
    }
  }
}
```

Pour remplir les variables qui entrent dans la requête, cliquez et développez l'onglet intitulé "Query Variables" en bas à gauche du GraphQL playground.

Ensuite, entrez ce JSON :

```js
{
  "input": {
    "name": "Indigo Montoya",
    "email": "indigomontoya@gmail.com",
    "age": 29,
    "id": 13,
    "friends": [1,2]
  }
}
```

En supposant que tout s'est bien passé, vous devriez voir une réponse avec l'utilisateur que nous venons de créer. Vous devriez également voir les deux utilisateurs avec les ids 1 et 2.

![Image](https://cdn-media-1.freecodecamp.org/images/hpPAUpQXSGfpBcYwg5e56yDMKj1eXFMsfIN0)

Maintenant, notre méthode create n'est pas totalement complète — les amis de notre nouvel utilisateur ne savent pas que notre nouvel utilisateur est leur ami.

Pour créer un utilisateur avec des références à ses amis, nous devrions également mettre à jour la liste d'amis des utilisateurs qui ont été référencés.

Je vais opter pour laisser cela comme exercice au lecteur s'il est enclin à le faire.

### Relier les points (Conclusion)

Assurez-vous de consulter le [code source de ce dépôt](https://github.com/iwilsonq/social-graphql) si vous souhaitez voir comment j'ai implémenté les mutations `deleteUser` et `updateUser`.

Utiliser GraphQL avec Apollo dans mes propres projets a été un plaisir. Je peux honnêtement dire qu'il est plus amusant de développer des schémas et des résolveurs GraphQL que d'implémenter des gestionnaires de routes HTTP.

Si vous souhaitez en savoir plus sur GraphQL, consultez ces publications sur Medium :

* [Publication Open GraphQL](https://medium.com/open-graphql)
* [Blog Apollo](https://blog.apollographql.com/)
* [Formation React Native](https://medium.com/react-native-training)

Si vous avez aimé cet article et souhaitez en voir plus à l'avenir, faites-le moi savoir dans les commentaires et suivez-moi sur [Twitter](https://twitter.com/iwilsonq) et [Medium](https://medium.com/@iwilsonq) !