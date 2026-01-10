---
title: Simuler un wrapper GraphQL autour de l'Interface Universelle des Échecs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-26T00:18:20.000Z'
originalURL: https://freecodecamp.org/news/mocking-a-graphql-wrapper-around-the-universal-chess-interface-1c5bb1acd821
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9caff0740569d1a4cab0de.jpg
tags:
- name: Universal Chess Interface
  slug: universal-chess-interface
- name: chess
  slug: chess
- name: GraphQL
  slug: graphql
- name: 'tech '
  slug: tech
- name: websocket
  slug: websocket
seo_title: Simuler un wrapper GraphQL autour de l'Interface Universelle des Échecs
seo_desc: 'By Jeff M Lowery


  _Photo by [Unsplash](https://unsplash.com/@samuelzeller?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Samuel
  Zeller / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utmcampaign=api-credit)

  The Un...'
---

Par Jeff M Lowery

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-253.png)
_Photo par [Unsplash](https://unsplash.com/@samuelzeller?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Samuel Zeller</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

L'Interface Universelle des Échecs (UCI) existe depuis longtemps et est utilisée par de nombreux moteurs d'échecs. Qu'apporte GraphQL à ce mélange ?

J'ai eu des échanges de courriels avec un propriétaire d'un site web d'échecs récemment, et il m'a demandé ce que je savais sur UCI et les websockets. Cela m'a amené à examiner de plus près UCI et à réfléchir sur la manière et la raison pour laquelle on pourrait envelopper un schéma GraphQL autour de celui-ci.

### L'Interface Universelle des Échecs

L'UCI [existe depuis plus d'une décennie](http://wbec-ridderkerk.nl/html/UCIProtocol.html), et est basée sur la messagerie I/O standard entre un moteur d'échecs et son client (généralement une interface graphique). Le client soumet un message au moteur d'échecs, et le moteur **peut** renvoyer une réponse. Je dis **peut** parce que l'UCI ne nécessite pas de réponse pour certains messages entrants vers le moteur d'échecs.

Le moteur **peut** également renvoyer plus d'une réponse. Pendant l'analyse du jeu, le moteur enverra des paquets **info** détaillant sa réflexion. Le client indique quelle est la position de départ, lui dit « Go », et le moteur continue jusqu'à ce qu'il arrive à un **meilleur coup**. Pendant le processus, le moteur diffuse des messages sur ce qu'il pense.

La spécification UCI est courte, et vous n'avez pas besoin d'une compréhension approfondie pour voir les bases de son fonctionnement — et cela a bien fonctionné jusqu'à présent, alors pourquoi y toucher ?

Si le moteur réside sur un serveur distant, alors ouvrez simplement une websocket et faites comme vous le feriez normalement. Cela fonctionne, bien sûr, mais il ne fait pas de mal de regarder les avantages et les inconvénients de faire les choses légèrement différemment.

### Moteur d'échecs versus Serveur d'échecs

Je veux commencer par simuler un service UCI. Une prochaine étape sera de construire un prototype fonctionnel et, comme toujours semble être le cas, il n'est pas difficile de trouver un package Node.js qui aide pour la plupart du travail.

L'un des moteurs les plus populaires s'appelle [Stockfish](https://stockfishchess.org/). Quelqu'un a pris la peine de le transpiler de C++ en JavaScript afin que le moteur puisse être exécuté entièrement en Node.js.

C'est aussi simple que cela :

* créer et se déplacer dans un dossier
* `npm init`
* `npm install stockfish`
* `node node_modules/stockfish/src/stockfish.js`

Et maintenant vous êtes dans un shell de commande Stockfish, et pouvez commencer à taper des commandes.

La première chose à faire est de lancer l'interface UCI en tapant `uci`. Vous devriez obtenir une réponse comme celle-ci :

```
id name Stockfish.js 8
id author T. Romstad, M. Costalba, J. Kiiski, G. Linscott

option name Contempt type spin default 0 min -100 max 100
option name Threads type spin default 1 min 1 max 1
option name Hash type spin default 16 min 1 max 2048
option name Clear Hash type button
option name Ponder type check default false
option name MultiPV type spin default 1 min 1 max 500
option name Skill Level type spin default 20 min 0 max 20
option name Move Overhead type spin default 30 min 0 max 5000
option name Minimum Thinking Time type spin default 20 min 0 max 5000
option name Slow Mover type spin default 89 min 10 max 1000
option name nodestime type spin default 0 min 0 max 10000
option name UCI_Chess960 type check default false
option name UCI_Variant type combo default chess var chess var giveaway var atomic var crazyhouse var horde var kingofthehill var racingkings var relay var threecheck
option name Skill Level Maximum Error type spin default 200 min 0 max 5000
option name Skill Level Probability type spin default 128 min 1 max 1000
uciok
```

Il montre les paramètres des options et retourne ensuite `**uciok**`, ce qui signifie que l'interface est prête. L'étape suivante consiste à définir les options puis à appeler `**isready**`, et lorsque le moteur répond `**readyok**`, il peut commencer à analyser une position d'échecs.

Je n'utiliserai pas réellement ce moteur pour mon implémentation simulée, mais il est utile si je veux examiner ce que fait une commande en utilisant un vrai moteur.

Dans une implémentation réelle de serveur, je lancerais un moteur par client (ou peut-être plus). [GraphQL](http://graphql.org/) m'aide à définir une API qui supporterait plusieurs clients exécutant plusieurs moteurs.

### GraphQL

Pour cette simulation, j'ai divisé le composant UCI en requêtes HTTP de type appel/réponse, et en abonnements websocket pour gérer les réponses en streaming. Cela signifie qu'une socket n'est ouverte que si l'utilisateur souhaite s'abonner à des informations détaillées sur ce que le moteur pense. De plus, je peux affiner le nombre et les types de messages **info** que je reçois sur le client, afin que le trafic de la socket soit minimisé.

#### **Chaque commande reçoit une réponse**

Parce que l'interaction client-serveur se fait (dans la plupart des cas) via HTTP non fiable, il est important que le client (s'exécutant sur le navigateur) sache que son message est parvenu au serveur. La commande UCI `**setoption**`, par exemple, n'envoie pas de réponse selon la spécification.

C'est bien pour une interface basée sur des sockets fiables, mais pas si bon pour les requêtes HTTP. GraphQL garantit qu'une réponse est envoyée pour chaque requête reçue, ne serait-ce que pour accuser réception de la requête.

#### **Chaque commande et ses arguments sont typés de manière sécurisée**

Les interfaces GraphQL sont basées sur un schéma, les interfaces UCI ne le sont pas (elles sont basées sur du texte descriptif dans la spécification). Si un client envoie une commande invalide, le serveur du moteur d'échecs ne devrait jamais avoir à la traiter. En définissant UCI en termes de types dans GraphQL, je peux intercepter une commande erronée au niveau de l'API — dans GraphQL — avant qu'elle n'atteigne le moteur.

#### **Les résolveurs GraphQL peuvent décomposer les réponses en structures JSON**

JavaScript est le langage de l'internet, et GraphQL retourne des réponses JSON. En faisant en sorte que les résolveurs GraphQL prennent une réponse UCI et la décomposent de manière fine et structurée, le client est soulagé de la tâche d'analyse de la réponse UCI.

#### **Je peux facilement simuler mon API en utilisant Apollo GraphQL Tools**

Après avoir conçu une API, mais avant de passer à l'implémentation, il est utile de vérifier d'abord l'apparence et la convivialité de l'API en utilisant des simulations. Le package [graphql-tools](https://github.com/apollographql/graphql-tools) rend [cela facile et sans douleur](https://medium.freecodecamp.org/mocking-graphql-with-graphql-tools-42c2dd9d0364). Vous pouvez même mélanger des simulations avec de vrais résolveurs, ce qui vous donne l'option d'une implémentation itérative de votre API.

#### Je peux interagir avec l'API via le service GraphiQL

[Graph**i**QL](https://github.com/graphql/graphiql) est le service interactif qui peut être exécuté sur un serveur GraphQL. Cela est pratique pour effectuer des tests ad hoc de l'API, basés sur une simulation ou une implémentation.

### Passons à la simulation !

Examinons d'abord les dépendances :

```json
"dependencies": {
    "apollo-server-express": "^1.3.2",
    "babel-cli": "^6.26.0",
    "babel-preset-env": "^1.6.1",
    "express": "^4.16.2",
    "graphql": "^0.12.3",
    "graphql-subscriptions": "^0.5.7",
    "graphql-tag": "^2.7.3",
    "graphql-tools": "^2.21.0",
    "stockfish": "^8.0.0",
    "subscriptions-transport-ws": "^0.9.5"
  },
  "devDependencies": {
    "casual": "^1.5.19",
    "randexp": "^0.4.8"
  },
```

J'appelle ce serveur **chessQ**, et le serveur lui-même sera basé sur `**apollo-server-express**`, l'implémentation du serveur GraphQL du groupe Apollo. Le package `**stockfish.js**`, mentionné précédemment, est inclus en tant que moteur intégré. Bien que cette simulation ne l'utilise pas, il est là pour référence. Dans une implémentation réelle, on utiliserait probablement [un moteur externe en cours d'exécution](https://www.npmjs.com/package/node-uci).

Inclus sont `casual` et `randexp` pour aider avec les simulations. Enfin, `**graphql-subscriptions**` et `**subscriptions-transport-ws**` géreront les messages en streaming provenant de notre simulation pendant qu'elle prétend analyser.

### Le schéma chessQ

Je tiens d'abord à dire que je n'ai pas passé de temps à polir le schéma, alors considérez-le comme un premier jet. Il est fonctionnel, mais il changera probablement à mesure que je continuerai à le développer. À la fin de cet article, je lierai une branche stable qui correspond à ce qui est décrit ici. Je n'entrerai pas dans les détails fastidieux du code, mais je lierai les sources pertinentes sur GitHub lorsque cela sera approprié. Surveillez cela.

La première chose est de définir [les requêtes de haut niveau](https://github.com/JeffML/chessQ/blob/chessQ-mock/schema.js). Ce sont les points d'entrée pour le client :

```js
type Query {
    createEngine: EngineResponse
    uci(engineId: String!): UciResponse!
    register(engineId: String!, name: String, code: String): String
    registerLater(engineId: String!): String
    setSpinOption(engineId: String!, name: String!, value: Int!): String!
    setButtonOption(engineId: String!, name: String!): String!
    setCheckOption(engineId: String!, name: String!, value: Boolean!): String!
    setComboOption(engineId: String!, name: String!, value: String!): String!
    quit(engineId: String!): String!
    isready(engineId: String!): String!
  }
```

La requête `createEngine` retournera une [EngineResponse](https://github.com/JeffML/chessQ/blob/chessQ-mock/readySchema.js), à l'intérieur de laquelle se trouve un identifiant d'instance de moteur qui est utilisé pour les requêtes suivantes :

```json
{
  "data": {
    "createEngine": {
      "engineId": "46d89031-03c3-4851-ae97-34e4b5d1d7c6"
    }
  }
}
```

La requête `**uci**` retournera une [UciResponse](https://github.com/JeffML/chessQ/blob/chessQ-mock/optionsSchema.js) détaillant les paramètres des options actuels. Dans le schéma GraphQL, chaque type d'option (spin, check, button, et combo) a ses propres champs spécifiques :

```graphql
interface Option {
    name: String!
    type: String!
  }
    
type SpinOption implements Option {
    name: String!
    type: String!
    value: Int!
    min: Int!
    max: Int!
  }
    
type ButtonOption implements Option {
    name: String!
    type: String!
  }
    
type CheckOption implements Option {
    name: String!
    type: String!
    value: Boolean!
  }
    
type ComboOption implements Option {
    name: String!
    type: String!
    value: String!
    options: [String!]!
  }
```

Une requête `uci` simulée pourrait être :

```graphql
query uci {
  uci(engineId: "46d89031-03c3-4851-ae97-34e4b5d1d7c6") {
    uciokay
    options {
      name
      type
      ... on SpinOption {
        value
        min
        max
      }
    }
  }
}
```

et la réponse :

```json
{
  "data": {
    "uci": {
      "uciokay": true,
      "options": [
        {
          "name": "Porro tempora minus",
          "type": "check"
        },
        {
          "name": "Id ducimus",
          "type": "combo"
        },
        {
          "name": "Aliquam voluptates",
          "type": "button"
        },
        {
          "name": "Voluptatibus illo ullam",
          "type": "spin",
          "value": 109,
          "min": 0,
          "max": 126
        },
        {
          "name": "Temporibus et nisi",
          "type": "check"
        }
      ]
    }
  }
}
```

Techniquement, certaines de ces commandes pourraient être considérées comme des Mutations, et non des Requêtes, puisqu'elles changent l'état du moteur. Mais les Mutations dans GraphQL concernent principalement l'ordre séquentiel d'exécution, et cela ne s'applique pas dans ce cas : toute option peut être définie dans n'importe quel ordre.

En fin de compte, chaque instance de moteur devra maintenir une certaine indication de son [état](https://github.com/JeffML/chessQ/blob/chessQ-mock/readySchema.js) (non implémenté dans cette simulation). Ceux-ci pourraient être :

```js
enum eEngineState {
    CREATED
    INITIALIZED
    READY
    RUNNING
    STOPPED
  }
```

Si, par exemple, une commande `**go**` est envoyée avant que l'état du moteur ne soit `**READY**`, alors ce serait une erreur.

#### Le schéma Ready

Lorsque le moteur est READY, trois nouvelles commandes sont possibles :

* `ucinewgame` : dire au moteur qu'une nouvelle partie a commencé
* `position` : dire au moteur quelle est la position de départ (ainsi que les coups éventuels à partir de cette position)
* `go` : démarrer le moteur !

Avant d'émettre la commande `**go**`, le client a la possibilité de s'abonner à tout message [**info**](https://github.com/JeffML/chessQ/blob/chessQ-mock/schema.js) diffusés via la websocket (sinon, il n'y aura qu'une réponse HTTP `BestMove` lorsque le moteur aura terminé).

Les détails sur la manière de configurer un service d'abonnement en utilisant [graphql-subscriptions](https://github.com/apollographql/graphql-subscriptions) peuvent être trouvés ailleurs, donc ici je me concentrerai sur l'implémentation du schéma et du résolveur.

Le schéma définit les types d'`Subscriptions` disponibles. Pour cette simulation, il n'y en a qu'un :

```graphql
type Subscription {
    info: Info
  }
```

Le type `Info`, comme le type `Option`, est une union de plusieurs structures d'info spécifiques :

```graphql
type Score {
    cp: Int!
    depth: Int!
    nodes: Int!
    time: Int!
    pv: [Move!]!
  }
  
type Depth {
    depth: Int!
    seldepth: Int!
    nodes: Int
  }
  
type Nps {
    value: Int!
  }
  
type BestMove {
    value: Move!,
    ponder: Move
  }
  
union Info = Score | Depth | Nps | BestMove
```

La signification précise de ces messages `Info` est sans importance pour cette discussion. L'important est de savoir qu'ils arrivent dans n'importe quel ordre, sauf pour le message `BestMove`, qui est le dernier.

Le client s'abonne aux messages d'info en utilisant une requête `subscription` comme suit :

```
subscription sub {
  info {
    ... on Score {
      pv
    }
    ... on BestMove {
      value
    }
  }
}
```

Il y a un résolveur pour gérer la requête `Subscription`, qui utilise des méthodes du package `**graphql-subscriptions**` :

```js
import {PubSub, withFilter} from 'graphql-subscriptions';
...

resolvers: 
...
Subscription: {
      info: {
        subscribe: withFilter(() => pubsub.asyncIterator(TOPIC), (payload, variables) => {
          return true
        })
      }
    }...
```

Dans ce résolveur d'abonnement, la fonction passée à `withFilter` transmet chaque message. Mais un vrai résolveur d'abonnement pourrait être plus discriminant en fonction des paramètres passés par le client.

#### Voir cela en action

Vous pouvez interroger, muter et vous abonner dans GraphiQL, donc il n'est pas nécessaire d'écrire un client à des fins de test. Le seul piège est que GraphiQL passera en mode « abonnement » une fois qu'un abonnement est demandé, et ne répondra pas volontiers aux commandes supplémentaires.

La solution est d'avoir deux onglets GraphiQL ouverts dans votre navigateur, l'un pour émettre des requêtes et des mutations, et l'autre pour écouter les messages abonnés.

Téléchargez le package [chessQ](https://github.com/JeffML/chessQ/tree/chessQ-mock), exécutez `npm install` puis `npm run dev`. L'application de simulation chessQ devrait maintenant être en cours d'exécution.

Ouvrez deux onglets vers [http://localhost:3001/graphiql](http://localhost:3001/graphiql).

Dans un onglet, entrez :

```
subscription sub {
  info {
    __typename
    ... on Score {
      pv
    }
    ... on BestMove {
      value
    }
  }
}
```

Vous verrez un message qui dit :

```
"Vos données d'abonnement apparaîtront ici après la publication du serveur !"
```

![Image](https://cdn-media-1.freecodecamp.org/images/E2xSU2QP22UL1MvOuIqnnlc1ixS6zEU3nSLw)
_Prêt à recevoir !_

Pour générer des messages, il y a un résolveur `**go**` (montré ci-dessous) qui parcourt un [ensemble statique de messages d'info](https://github.com/JeffML/chessQ/blob/chessQ-mock/InfoGenerator.js) et les publie un par un. Parce que le panneau de l'abonné **ne montrera qu'un seul message** à la fois, il y a une implémentation simple de `sleep` qui ralentit la messagerie afin que vous puissiez les voir défiler :

```js
function sleep(ms) {
  return new Promise(resolve => {
    setTimeout(resolve, ms)
  })
}
...

resolvers: {...

Mutation: {
      go: async () => {
        let info;
        for (info of InfoGenerator()) {
          pubsub.publish(TOPIC, {info})
          await sleep(1000)
        }
        return info;
      }
    },...
```

Enfin, dans l'onglet non-abonnement, commencez l'analyse avec `**go**` :

```graphql
mutation go {
  go {
    __typename
    value
  }
}
```

Pendant que cet onglet attend la réponse `go` montrant le `BestMove`, l'onglet `subscription` attrapera les messages d'info et les affichera un par un.

![Image](https://cdn-media-1.freecodecamp.org/images/Sead--yLEPWQIqOBgZlLM9czMcSB61AgRMxQ)
_Messages d'info en cours de réception…_

![Image](https://cdn-media-1.freecodecamp.org/images/Ag3amWB0PTUL--3UjwwK-96bpH7vEUN5pUAY)
_Analyse terminée !_

### Réflexions supplémentaires

Avant de passer de la simulation à l'implémentation, quelques notes :

Le mécanisme simple de pub/sub utilisé dans cet exemple n'est ni robuste ni scalable. Ce n'est pas grave, car il existe des implémentations [Redis](https://redis.io/) et [RabbitMQ](https://github.com/cdmbase/graphql-rabbitmq-subscriptions) de graphql-subscription qui le sont. Une spécification d'abonnement plus raffinée pourrait également être définie et donner un contrôle fin à l'abonné quant aux messages reçus.

Peu de réflexion a été accordée à la gestion de la durée de vie des websockets dans cette simulation, ce qui est quelque chose qui doit être considéré si l'on sert un grand nombre d'utilisateurs.

Tout le code source de cet article peut être trouvé [ici](https://github.com/JeffML/chessQ/tree/chessQ-mock).