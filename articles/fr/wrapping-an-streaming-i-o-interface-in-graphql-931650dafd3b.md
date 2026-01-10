---
title: Comment envelopper une interface I/O de streaming dans GraphQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-08T18:31:53.000Z'
originalURL: https://freecodecamp.org/news/wrapping-an-streaming-i-o-interface-in-graphql-931650dafd3b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q_D9nZAIvlL8Sj9wSwluJQ.jpeg
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comment envelopper une interface I/O de streaming dans GraphQL
seo_desc: 'By Jeff M Lowery


  _Photo by [Unsplash](https://unsplash.com/@emcomeau?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Ezra
  Comeau-Jeffrey / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utmcampaign=api-credit)

  This...'
---

Par Jeff M Lowery

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-252.png)
_Photo par [Unsplash](https://unsplash.com/@emcomeau?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Ezra Comeau-Jeffrey</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Cet article traitera de l'utilisation de GraphQL pour gérer un service qui utilise un flux I/O pour l'interaction entre le client et le serveur. Dans un article précédent, j'ai simulé une API GraphQL pour l'[Universal Chess Interface](http://wbec-ridderkerk.nl/html/UCIProtocol.html) (UCI). L'UCI utilise [stdio](https://www.urbandictionary.com/define.php?term=stdio) pour communiquer, acceptant des commandes à partir d'un flux d'entrée et envoyant des réponses via un flux de sortie. J'utiliserai UCI comme illustration, mais je ne décrirai pas UCI en détail.

### Stockfish

Stockfish est un moteur d'échecs bien connu qui supporte UCI. En utilisant NodeJS et le module stockfish.js (une transpilation JavaScript de l'original), il est facile de configurer un moteur en cours d'exécution qui implémente UCI via stdio :

* créer et se déplacer dans un dossier
* `npm init`
* `npm install stockfish`
* `node node_modules/stockfish/src/stockfish.js`

Et à partir de là, vous pouvez taper des commandes UCI dans la fenêtre du terminal et voir les résultats.

### Un rappel sur [Query vs Mutation](http://graphql.org/learn/schema/#the-query-and-mutation-types)

Les requêtes sont exécutées en parallèle. Ce n'est pas un problème pour une API sans état où chaque requête retournera le même résultat indépendamment de l'ordre dans lequel les résultats sont retournés. **UCI n'est pas sans état**, donc les commandes et les résultats doivent fonctionner en séquence. Voici un exemple d'interaction entre le client en ligne de commande et le moteur d'échecs :

```
GUI     engine

// dire au moteur de passer en mode UCI
uci

// identification du moteur  
    id name Shredder
		id author Stefan MK

// le moteur envoie les options qu'il peut changer
		option name Hash type spin default 1 min 1 max 128
		option name NalimovPath type string default 
		option name NalimovCache type spin default 1 min 1 max 32
// le moteur a envoyé tous les paramètres et est prêt
		uciok

// maintenant le GUI définit quelques valeurs dans le moteur
// définir le hash à 32 Mo
setoption name Hash value 32
setoption name NalimovCache value 1
setoption name NalimovPath value d:\tb;c\tb

// cette commande et la réponse sont requises ici !
isready

// le moteur a fini de configurer les valeurs internes
		readyok

// maintenant nous sommes prêts à commencer
```

Les réponses du moteur aux commandes du client sont indentées. La première transition d'état consiste à initier le protocole UCI, où le moteur répond avec les paramètres d'option par défaut et un signal **uciok** indiquant qu'il a terminé. À ce stade, le client peut configurer les options. Celles-ci ne prendront effet que lorsque la commande **isready** est émise. Le moteur répond avec **readyok** lorsque toutes les options sont définies. D'autres transitions d'état se produiront lors de la configuration du jeu et de l'analyse (non montré).

L'exécution de plusieurs requêtes en parallèle peut émettre des commandes prématurément, car aucune requête n'attend la réponse d'une autre requête. Le problème peut être illustré avec une simple API GraphQL vers un service asynchrone simulé :

```js
import {makeExecutableSchema} from 'graphql-tools';

const typeDefs = `
type Query {
  message(id: ID!): String!
}
type Mutation {
  message(id: ID!): String!
}
`

const resolvers = {
  Query: {
    message: (_, {id}) => new Promise(resolve => {
      setTimeout(function() {
        let message = `response to message ${id}`;
        console.log(message)
        resolve(message);
      }, Math.random() * 10000)
    })
  },
  Mutation: {
    message: (_, {id}) => new Promise(resolve => {
      setTimeout(function() {
        let message = `response to message ${id}`;
        console.log(message)
        resolve(message);
      }, Math.random() * 10000)
    })
  }
}

const schema = makeExecutableSchema({typeDefs, resolvers});
export {
  schema
};
```

Les résultats sont :

![Image](https://cdn-media-1.freecodecamp.org/images/1*rqOQsfsW6HNp2ovNmvTSWQ.png)
_L'ordre de résolution diffère de l'ordre de réponse._

Dans les fenêtres de la console (moitié inférieure), vous pouvez voir quand les réponses ont été retournées. Exécutez maintenant les mêmes requêtes via Mutation :

![Image](https://cdn-media-1.freecodecamp.org/images/1*6blqj1VzTMOohRjRHBG2zQ.png)
_L'ordre de résolution correspond à l'ordre de réponse_

Obtenir une réponse prend plus de temps car chaque opération doit se terminer avant que la suivante ne soit invoquée.

#### Ce que cela signifie pour un wrapper GraphQL UCI

[Dans un article précédent](https://medium.freecodecamp.org/mocking-a-graphql-wrapper-around-the-universal-chess-interface-1c5bb1acd821), j'ai donné des arguments sur les raisons pour lesquelles GraphQL pourrait être utilisé pour envelopper UCI. Peut-être que le moyen le plus simple de le faire est d'utiliser le service de subscription de GraphQL. Cela enverra des événements au client via une socket web. Les commandes sont envoyées via des Queries ou des Mutations, et les réponses reviennent sous forme d'événements abonnés.

Dans le cas de l'interaction UCI, les mutations seraient utilisées pour garantir que les commandes sont exécutées dans la séquence attendue. Avant d'exécuter une commande, vous configureriez d'abord une subscription pour recevoir la réponse. En utilisant GraphQL, les réponses de subscription sont typées, tout comme les valeurs de retour d'une requête Query ou Mutation.

Le client appelle les Mutations GraphQL pour envoyer des requêtes via HTTP, puis reçoit des réponses (le cas échéant) via une socket web. Bien que simple à implémenter sur le serveur, **une interface basée sur des sockets est maladroite pour le client** car elle est multi-étapes :

1. s'abonner à l'événement de réponse attendu
2. envoyer une commande via HTTP
3. recevoir une réponse HTTP (un accusé de réception que la requête a été reçue, pas le résultat réel)
4. attendre que la vraie réponse arrive via la socket web.
5. agir sur la réponse

#### Simplifier l'interaction client-serveur

Catégorisons les types de réponses que UCI envoie :

1. réponse en une seule ligne
2. pas de réponse
3. réponse multi-ligne, multi-valeur, avec terminateur

_(À part : Il est possible de démarrer une analyse sans limite de temps définie (« infinite **go** »). Cela entrerait dans la catégorie 2 car l'analyse aboutira à un point de terminaison du meilleur coup, soit par épuisement, soit par la commande **stop**.)_

**Catégorie 1** est un simple appel et réponse, et ceux-ci peuvent être gérés comme de simples requêtes HTTP GraphQL. Pas besoin de s'abonner pour une réponse : le resolver peut simplement la retourner lorsqu'elle arrive.

**Catégorie 2** ne reçoit pas de réponse du moteur, mais une réponse est requise par HTTP. Tout ce qui est nécessaire dans ce cas est d'accuser réception de la requête.

**Catégorie 3** a deux sous-types : les requêtes avec des réponses multi-lignes mais fixes (par exemple, **option**), et les requêtes avec des réponses intermédiaires en streaming (**go**). Le premier peut à nouveau être géré via HTTP car la réponse sera prévisible et rapide. Le second a un temps d'achèvement variable (éventuellement long), et peut envoyer une série de réponses intermédiaires d'intérêt pour le client, qu'il souhaiterait recevoir en temps réel. Comme nous ne pouvons pas envoyer plusieurs réponses à une requête HTTP, ce dernier cas ne peut pas être géré par HTTP seul, donc l'interface de subscription décrite ci-dessus est toujours appropriée.

Malgré le fait que UCI soit une interface de streaming, il s'avère que dans la plupart des cas, une réponse/requête HTTP peut être utilisée pour l'interaction via GraphQL.

### Conclusions

1. Le schéma GraphQL doit être constitué de Mutations car UCI est stateful et les commandes doivent être exécutées en séquence
2. Pour les commandes de Catégorie 1 & 2, la requête/réponse HTTP est la plus simple. Il y a toujours du streaming en cours dans le back-end, mais les resolvers GraphQL instaureront un écouteur de flux UCI spécifique à la réponse de commande UCI attendue avant d'envoyer la commande au moteur. Cet écouteur résoudra la requête GraphQL via HTTP lorsque la réponse arrivera du moteur. Cela facilite le travail pour le client.

3. Le serveur suivra également l'état UCI pour s'assurer que les commandes sont exécutées dans le bon contexte. Si le client tente d'exécuter une commande avant que le moteur ne puisse la gérer, une erreur de statut HTTP sera retournée
4. Pour les cas où il n'y a pas de réponse attendue de UCI, le resolver GraphQL accusera simplement réception de la commande
5. Le cas déterminé pour la Catégorie 3 (où il y a une réponse sûre et rapide) peut être géré par HTTP.
6. Le cas indéterminé, où il y a des réponses intermédiaires avant la terminaison, peut être géré via une socket web. Cela, à son tour, peut être enveloppé dans un service de subscription GraphQL.

La [mock implementation](https://github.com/JeffML/chessQ/tree/chessQ-mock) a couvert l'essentiel, mais cette courte analyse fournit un plan pour avancer avec une implémentation.

_Le code pour cet article peut être trouvé [ici](https://github.com/JeffML/query_async)._