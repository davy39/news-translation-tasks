---
title: Comment travailler avec FaunaDB + GraphQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-30T17:01:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-faunadb
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/vincent-van-zalinge-WHrwb43vH9E-unsplash.jpg
tags:
- name: FaunaDB
  slug: faunadb
- name: GraphQL
  slug: graphql
- name: Netlify
  slug: netlify
- name: netlify-functions
  slug: netlify-functions
seo_title: Comment travailler avec FaunaDB + GraphQL
seo_desc: 'By Jeff M Lowery

  I have one or two projects I maintain on Netlify, in addition to hosting my blog
  there. It’s an easy platform to deploy to, and has features for content management
  (CMS) and lambda functions (by way of AWS).

  What I needed for my late...'
---

Par Jeff M Lowery

J'ai un ou deux projets que je maintiens sur [Netlify](https://www.netlify.com/), en plus d'héberger mon blog là-bas. C'est une plateforme facile à déployer, et elle dispose de fonctionnalités pour la gestion de contenu (CMS) et les fonctions lambda (via AWS).

Ce dont j'avais besoin pour mon dernier projet, cependant, était une base de données. Netlify a intégré [FaunaDB](https://fauna.com/) : une base de données NoSQL, orientée documents. Fauna a récemment [annoncé la prise en charge de GraphQL](https://fauna.com/blog/the-worlds-best-serverless-database-now-with-native-graphql), ce qui est un gros plus. Sans frais et avec une configuration simplifiée, pourquoi ne pas l'essayer ?

## La base de données

Fauna a une approche unique pour gérer [les transactions à travers des magasins de données distribués mondialement](https://fauna.com/blog/consistency-without-clocks-faunadb-transaction-protocol), de sorte que les enregistrements de la base de données ne se désynchronisent pas lorsqu'ils sont mis à jour à partir de points éloignés. C'est un problème pour les entreprises mondiales avec des volumes de transactions élevés, mais sans importance pour mon petit projet.

## L'application

Je suis un joueur d'échecs de niveau moyen et je veux mettre en place des données pour analyser des parties d'échecs de niveau maître. SQL ou NoSQL n'avait pas d'importance—j'ai travaillé avec les deux et l'un ou l'autre supporterait les besoins modestes de mon application.

J'adore GraphQL, et je l'utilise depuis 2016. Je ne veux pas que mon schéma GraphQL soit exposé côté client, cependant. La solution est d'avoir des fonctions lambda pour effectuer les requêtes GraphQL, puis de faire en sorte que le client utilise ces fonctions comme une sorte de proxy.

## L'implémentation

J'ai commencé avec [netlify-fauna-example](https://github.com/netlify/netlify-faunadb-example)*. Cela n'utilise pas GraphQL ; au lieu de cela, les [Netlify Functions](https://www.netlify.com/docs/functions/) de l'exemple utilisent FQL : [Fauna Query Language](https://docs.fauna.com/fauna/current/api/fql/). Vous pouvez exécuter des requêtes via [fauna shell](https://github.com/fauna/fauna-shell), ou en [utilisant un module client NodeJS](https://github.com/fauna/faunadb-js). Ce qui suit utilise le client pour insérer un **todoItem** dans la collection **todos** :

todos-create.js

```js
  ...
  /* construire la requête fauna */
  return client.query(q.Create(q.Ref('classes/todos'), todoItem))
    .then((response) => {
      console.log('succès', response)
      /* Succès ! retourner la réponse avec statusCode 200 */
      return callback(null, {
        statusCode: 200,
        body: JSON.stringify(response)
      })
    }).catch((error) => {
      console.log('erreur', error)
      /* Erreur ! retourner l'erreur avec statusCode 400 */
      return callback(null, {
        statusCode: 400,
        body: JSON.stringify(error)
      })
    })
```

Pour utiliser GraphQL, je dois créer une base de données sur Fauna, puis importer un schéma GraphQL. Une fois que vous avez créé un compte sur Fauna, vous pouvez faire tout cela via leur tableau de bord.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-29-at-11.27.05-AM---Edited.png)
_Ma nouvelle base de données Fauna_

Une fois terminé, un ensemble de collections (similaires à des tables en SQL) sont créées en fonction de mes définitions de types GraphQL importées. Intéressamment, de nouveaux types et champs sont également ajoutés pour gérer des choses comme l'identification des instances et la gestion des relations entre les types. Par exemple, mon type pour Opening était :

```gql
type Opening {
  desc: String!
  fen: String!
  SCID: String!
}
```

et lorsque je vais dans le tableau de bord, j'ouvre GraphQL Playground, et je regarde le schéma, je vois :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-28-at-1.05.59-PM.png)

OpeningInput et OpeningPage ont été ajoutés par Fauna, en plus des champs _id et _ts dans Opening.

### Requêtes et Mutations

Il y a certaines requêtes et mutations qui seront automatiquement implémentées pour vous par Fauna _si_ vous les définissez dans le schéma que vous avez créé. Lorsque je définis le type pour contenir les informations d'ouverture d'échecs, je _peux_ alors inclure les définitions de requête et de mutation suivantes dans mon schéma :

```text
type Query {
 allOpenings: [Opening]
}
```

Et FaunaDB fournira une implémentation.

### Fonctions lambda

Les lambdas originales dans [netlify-fauna-example](https://github.com/netlify/netlify-faunadb-example) parlent FQL. Pour les convertir en requêtes GraphQL, utilisez une bibliothèque de fetch telle que node-fetch, et faites des requêtes HTTPS à l'endpoint GraphQL de Fauna en utilisant un client comme celui inclus avec [apollo-boost](https://levelup.gitconnected.com/giving-react-a-lift-with-apollo-boost-74c6ff32894d) :

```js
import ApolloClient from 'apollo-boost';
import gql from 'graphql-tag'
import fetch from 'node-fetch'
import authorization from './authorization'

const URL = 'https://graphql.fauna.com/graphql'

const client = new ApolloClient({
  uri: URL,
  fetch,
  request: operation => {
    operation.setContext({
      headers: {
        authorization
      },
    });
  },
})


exports.handler = (event, context, callback) => {
  const allOpeningFens = gql`    
  query openings {
      allOpenings {
        data {fen}
      }
    }
  `;


  client.query({ query: allOpeningFens })
    .then(results => {
      callback(null, {
        statusCode: 200,
        body: JSON.stringify(results),
      })
    })
    .catch(e => callback(e))
}
```

Le code ci-dessus demande les chaînes FEN pour toutes les ouvertures dans la collection Opening.

## Avons-nous terminé maintenant ? Non.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-217.png)
_Photo par [Unsplash](https://unsplash.com/@sarti46?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Massimo Sartirana</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Le support GraphQL de Fauna est dans un état fonctionnel mais encore en formation. L'une des choses que je voulais faire était d'avoir une capacité d'insertion par lots afin de ne pas avoir à insérer une ouverture à la fois dans la collection Opening. Cette mutation n'est pas créée automatiquement par Fauna (bien qu'elle soit une demande de fonctionnalité ticketée), donc j'ai dû définir un resolver pour celle-ci.

Fauna a une directive [@resolver](https://docs.fauna.com/fauna/current/api/graphql/directives/d_resolver) qui peut être utilisée sur les définitions de mutation. Elle dirigera Fauna pour utiliser une fonction définie par l'utilisateur écrite en FQL ; celles-ci peuvent être écrites directement dans le shell. Pour une collection de types simples comme Opening, le resolver FQL est assez simple.

Tout d'abord, je vais dans le FaunaDB Console Shell, et je crée la fonction `add_openings` :

```text
CreateFunction({
  name: "add_openings",
  body: Query(
    Lambda(
      ["openings"],
      Map(
        Var("openings"),
        Lambda("X", Create(Collection("Opening"), { data: Var("X") }))
      )
    )
  )
```

Openings est un tableau, et la méthode Map exécute l'appel Create sur chaque élément. J'ajoute ensuite une directive @resolver à ma définition de mutation dans le schéma que je vais importer (appelé **custom resolver**) :

```text
type Mutation {
   addOpenings(openings: [OpeningInput]) : [Opening]! @resolver(name: "add_openings" paginated:false)
}
```

Maintenant, lorsque la mutation est exécutée via le client GraphQL, `add_openings` est appelée et insérera toutes les parties passées en tant que paramètre à la mutation. Depuis le client GraphQL, cela ressemble à ceci :

```text
import ApolloClient from 'apollo-boost';
import gql from 'graphql-tag'
import fetch from 'node-fetch'
import authorization from './authorization'

const URL = 'https://graphql.fauna.com/graphql'

const client = new ApolloClient({
  uri: URL,
  fetch,
  request: operation => {
    operation.setContext({
      headers: {
        authorization
      },
    });
  },
})


exports.handler = (event, context, callback) => {

  const addScidDocs = gql`
  mutation($scid: [OpeningInput]) {
    addOpenings(openings: $scid) {desc}
  }
  `

  const json = JSON.parse(event.body)

  client.mutate({
    mutation: addScidDocs,
    variables: { scid: json },
  })
    .then(results => {
      console.log({ results })
      callback(null, {
        statusCode: 200,
        body: JSON.stringify(results),
      })
    })
    .catch(e => callback(e.toString()))

  // callback(null, { statusCode: 200, body: event.body })
}
```

## Le vieux problème de la poule et de l'œuf

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-218.png)
_Photo par [Unsplash](https://unsplash.com/@chromatograph?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Chromatograph</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Vous remarquerez dans la mutation ci-dessus que je fais référence au type OpeningInput. Pour que je puisse importer mon schéma dans Fauna, ce type doit être défini. Mais... lorsque j'ai importé Opening, Fauna a auto-généré ce type pour moi. Lorsque je le définis dans mon schéma plus tard (pour la mutation), j'écrase essentiellement ce type. Puisque ce type généré est utilisé dans les mutations générées (c'est-à-dire, createOpening, singulier), en écrasant cette définition de type dans mon propre schéma, je pourrais éventuellement casser l'une des mutations générées.

La solution suggérée est de ne pas écraser le type OpeningInput, mais de renommer mon type d'entrée en quelque chose comme MyOpeningInput. Cela garantit que mon schéma d'importation est valide, et ne perturbe pas ce que les mutations générées attendent.

Le problème devient plus compliqué, cependant, lorsque vous utilisez la directive [@relation](https://fauna.com/blog/getting-started-with-graphql-part-2-relations). Cette directive génère des types utilisés pour relier deux autres instances de types.

Voici la relation dans mon schéma d'importation. Notez la directive :

```text
type Game {
  header: Header! @relation
  fens: [String!]!
  opening: Opening @relation
}

type Header {
    Event: String
    Date: String!
    White: String!
    WhiteElo: String
    Black: String!
    BlackElo: String
    ECO: String
    Result: String
}
```

Pour stocker un Game, je dois également avoir un Header requis (Opening n'est pas requis). La relation est maintenue par un champ **ref** généré par Fauna sur le Header. Il est défini pour la mutation par l'utilisation d'un type GameHeaderRelation qui permet la création à la fois de Game et de Header dans une seule mutation. Voici les types générés pertinents :

```text
input GameHeaderRelation {
  create: HeaderInput
  connect: ID
}

input GameInput {
  header: GameHeaderRelation
  fens: [String!]!
  opening: GameOpeningRelation
}

type Mutation {
  createGame(data: GameInput!): Game!
}
```

Maintenant, pour ajouter un jeu avec les informations d'en-tête requises, je peux appeler la mutation comme suit, depuis le Playground :

```text
mutation CreateGameWithHeader {
    createGame(data: {
        fens: [],
        header: { 
           create: {
           date: "2004.10.16", 
           white: "Morozevich, Alexander", 
           ...} ) {
        _id
        fens
        header {
          data {
            date
            white
          }
        }
    }
}
```

Disons que je veux maintenant créer une mutation pour télécharger par lots plusieurs jeux. Malheureusement, je n'ai pas accès au type **GameHeaderRelation** généré, ni à aucun des autres types d'entrée. Mon schéma d'importation ne se validera pas sans ceux définis si j'essaie de les utiliser dans ma définition de mutation en masse. Encore une fois, les mutations en masse sont une demande de fonctionnalité ticketée, donc elles devraient être disponibles bientôt. Pourtant, ce type de problème surgira concernant l'utilisation de types par n'importe quel resolver personnalisé.

J'ai pensé pendant une minute que la solution serait de télécharger le schéma généré (à partir de Playground), puis de le modifier avec mes mutations en masse. Cependant, je suis en train de _remplacer_ les types autrement générés à l'importation, ce qui n'est pas ce que je veux qu'il se produise.

### La solution de contournement : écrire un resolver personnalisé en FQL

Comme indiqué, je dois m'assurer que lorsque je crée une fonction pour que mon resolver addGames appelle, il doit y avoir un Header créé en premier pour chaque jeu.

L'attribut resolver du schéma GraphQL appelle la fonction FQL add_games :

```text
addGames(games: [GameInput]) : [Game]! @resolver(name: "add_games", paginated: false)
```

Et voici la définition de la fonction pour add_games :

```text
CreateFunction({
  name: "add_games",
  body: Query(
    Lambda(
      ["games"],
      Map(
        Var("games"),
        Lambda("X", [
          Create(Collection("Game"), {
            data: Merge(Var("X"), {
              header: Select(
                ["ref"],
                Create(Collection("Header"), {
                  data: Select(["header"], Var("X"))
                })
              )
            })
          })
        ])
      )
    )
  )
}
```

Je ne suis pas un expert FQL (voir les remerciements), mais ce code est lisible (de l'intérieur vers l'extérieur) :

1. crée une instance d'en-tête
2. sélectionne son champ de référence généré "ref"
3. fusionne cette référence en tant que champ "header" dans un objet de données "X"
4. "X" représente un élément du paramètre de tableau d'entrée "games" (GameInput)

Je devrais noter que l'un des ingénieurs de Fauna a déclaré que le maintien des références _à la main_ est "tricky". Cela nécessite une compréhension de ce qui se passe sous le capot. Le type de relation [@embedded](https://docs.fauna.com/fauna/current/api/graphql/directives/d_embedded) peut être plus facile à implémenter en FQL si la relation est de un à un, comme dans ce cas.

## Où aller à partir d'ici...

L'équipe de support de Fauna et les membres du forum de la communauté Slack ont été extrêmement utiles avec les questions et ont même offert de l'aide pour la mise en œuvre des fonctions FQL. Ils sont également francs lorsque la documentation sur site est incomplète ou erronée.

Les performances n'étaient pas géniales : l'insertion en masse de 1000 petits documents s'est exécutée en quelques secondes, ce qui est lent. Cependant, je n'ai pas utilisé la pagination dans mes resolvers, et cela peut faire une différence significative. Il est également possible que les fonctionnalités GraphQL soient dans une configuration plus lente et débogable alors que Fauna développe l'ensemble des fonctionnalités.

Pour écrire des resolvers personnalisés, il est nécessaire de maîtriser [FQL](https://docs.fauna.com/fauna/current/api/fql/). Sa syntaxe [LISPish](https://www.tutorialspoint.com/lisp/lisp_basic_syntax.htm) plaira à certains, mais je la trouve verbeuse et "nested". Pour les opérations CRUD simples, c'est bien. Vous ne vous trouverez peut-être pas à écrire beaucoup de resolvers personnalisés, non plus.

J'ai choisi d'essayer Fauna non pour ses forces, mais pour sa commodité. Je pourrais revenir dans quelques mois et voir comment il a progressé.

**Remerciements**

Je voudrais remercier Summer Schrader, Chris Biscardi et Leo Regnier pour leur patience et leur perspicacité.

---

* Je suppose que ma vie n'est pas assez intéressante : lorsque je clone un projet comme netlify-fauna-example, je vais généralement exécuter `npm update outdated` et `npm audit fix`. Je peux m'attendre à rencontrer des problèmes lorsque je le fais, mais en pratique, je les résous généralement en une heure ou deux.

**Pas cette fois.** J'ai supprimé node_modules, package-lock.json, et même fait un nettoyage forcé du cache avant de tout réinstaller. Cela n'a pas fonctionné. J'ai finalement passé à **yarn**, supprimé les éléments ci-dessus (mais laissé les informations de version mises à jour dans package.json intactes) et installé. Après quelques hoquets, succès ! Voici les versions des dépendances avec lesquelles j'ai terminé :

```text
  "dependencies": {
    "apollo-boost": "^0.4.4",
    "chess.js": "^0.10.2",
    "encoding": "^0.1.12",
    "faunadb": "^2.8.0",
    "graphql": "^14.5.7",
    "graphql-tag": "^2.10.1",
    "node-fetch": "^2.6.0",
    "react": "^16.9.0",
    "react-dom": "^16.9.0",
    "react-scripts": "^3.1.1"
  },
  "devDependencies": {
    "http-proxy-middleware": "^0.20.0",
    "markdown-magic": "^1.0.0",
    "netlify-lambda": "^1.6.3",
    "npm-run-all": "^4.1.5"
  },
```