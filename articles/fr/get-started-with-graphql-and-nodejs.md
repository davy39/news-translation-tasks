---
title: Comment commencer avec GraphQL et Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-23T18:21:36.000Z'
originalURL: https://freecodecamp.org/news/get-started-with-graphql-and-nodejs
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/getting-started-with-graphql.jpg
tags:
- name: Apollo GraphQL
  slug: apollo
- name: GraphQL
  slug: graphql
- name: Node.js
  slug: nodejs
- name: software development
  slug: software-development
- name: Tutorial
  slug: tutorial
seo_title: Comment commencer avec GraphQL et Node.js
seo_desc: "By Ramón Morcillo\nThe main purpose of this server-client Node.js project\
  \ is to help other people understand how GraphQL exposes data from the Server and\
  \ how the Client fetches it. \nI have tried to make it as simple as possible - if\
  \ you want to dive i..."
---

Par Ramón Morcillo

Le but principal de ce projet serveur-client [Node.js](https://nodejs.org/en/) est d'aider les autres à **comprendre comment GraphQL expose les données du serveur et comment le client les récupère**. 

J'ai essayé de le rendre aussi simple que possible - si vous souhaitez plonger dans le code du projet, vous pouvez le trouver [ici](https://github.com/reymon359/graphql-hello-world-server).

Maintenant, allons droit au but : [GraphQL](https://graphql.org/) est un **langage de requête pour les [API](https://en.wikipedia.org/wiki/Application_programming_interface)** développé et [open-sourcé par Facebook](https://engineering.fb.com/core-data/graphql-a-data-query-language/) pour accélérer le processus de requête.

[REST](https://en.wikipedia.org/wiki/Representational_state_transfer) a été une manière populaire d'exposer les données d'un serveur. Mais au lieu d'avoir **plusieurs endpoints** qui retournent des structures de données fixes, GraphQL n'a qu'**un seul endpoint**. Et c'est au client de spécifier les données dont il a besoin.

## Table des matières

- Installation
- Comment définir le schéma
- Comment ajouter la fonction de résolution
- Comment configurer le serveur
- Comment configurer le client
- Comment récupérer les données du serveur
- Comment afficher les données
- Conclusion
- Ressources utiles
  - Docs 📚
  - Apprendre 📝
  - Outils 🔧
  - IDE 💻
  - Extras 🍎


## Installation

La première étape est de [télécharger et installer Node.js](https://nodejs.org/en/download/) si ce n'est pas déjà fait. Une fois installé, commençons avec la structure du répertoire. 

Le projet sera composé de **deux répertoires**, un pour le client et un autre pour le serveur. J'ai choisi de garder les deux dans le répertoire racine du projet, mais vous pouvez les diviser en deux projets séparés ou de la manière que vous souhaitez.

```text
📁 projet
├── 📁 client
└── 📁 serveur
```

Maintenant, nous allons initialiser le projet dans le répertoire du serveur. Changez l'emplacement vers le dossier serveur dans votre terminal et exécutez `npm init` pour remplir les informations du projet et générer le fichier **package.json**. 

Ou vous pouvez exécuter `npm init -y` qui indique au générateur d'utiliser les valeurs par défaut (au lieu de poser des questions et de simplement générer un projet npm vide sans passer par un processus interactif).

L'étape suivante sera d'installer [GraphQL.js](https://github.com/graphql/graphql-js) et [Apollo Server](https://github.com/apollographql/apollo-server) sur notre serveur. GraphQL.js fournira deux capacités importantes :

- Construire un schéma de type, que nous ferons dans [l'étape suivante](#define-the-schema).
- Servir des requêtes contre ce schéma de type.

Pour l'installer, exécutez simplement `npm install graphql`. Je suppose que vous utilisez une version de NPM égale ou supérieure à **5.0.0**, donc vous [n'avez pas besoin](https://blog.npmjs.org/post/161081169345/v500) d'ajouter `--save` lors de l'installation d'une dépendance pour qu'elle soit enregistrée dans le `package.json`.

Apollo Server, en revanche, nous aidera à implémenter les fonctionnalités GraphQL. Il fait partie de la [plateforme Apollo Data Graph](https://www.apollographql.com/).

> Apollo est une plateforme pour construire un graphe de données, une couche de communication qui connecte de manière transparente vos clients d'application (tels que React et les applications iOS) à vos services backend. C'est une implémentation de GraphQL conçue pour les besoins des équipes d'ingénierie produit construisant des applications modernes et pilotées par les données. - [Documentation Apollo](https://www.apollographql.com/docs/)

Ce que vous devez savoir sur Apollo, au moins pour l'instant, c'est que c'est une communauté qui construit sur GraphQL et fournit différents **outils pour vous aider à construire vos projets**. Les outils fournis par Apollo sont principalement au nombre de 2 : Client et Serveur.

- **Apollo Client** aide votre Frontend à communiquer avec une API GraphQL. Il prend en charge les frameworks les plus populaires tels que React, Vue ou Angular et le développement natif sur iOS et Android.

- **Apollo Server** est la couche serveur GraphQL dans votre backend qui délivre les réponses aux requêtes des clients.

Maintenant que vous comprenez mieux Apollo et pourquoi nous allons l'utiliser, continuons à configurer GraphQL.

## Comment définir le schéma

Un schéma GraphQL est au cœur de toute implémentation de serveur GraphQL. Il **décrit la forme de vos données**, en les définissant avec une hiérarchie de **types** avec des champs qui sont remplis à partir de votre source de données. Il spécifie également les **requêtes** et **mutations** disponibles, afin que le client sache quelles informations peuvent être demandées ou envoyées.

Par exemple, si nous voulions construire une application musicale, notre schéma le plus simple, généralement défini dans un fichier `schema.graphql`, contiendrait deux **types d'objets** : `Song` et `Author`, comme ceci :

```js
type Song {
  title: String
  author: Author
}

type Author {
  name: String
  songs: [Song]
}
```

Ensuite, nous aurions un **type Query** pour définir les requêtes disponibles : `getSongs` et `getAuthors`, chacune retournant une liste du type correspondant.

```js
type Query {
  getSongs: [Song]
  getAuthors: [Author]
}
```

Pour garder cela aussi simple que possible, notre schéma n'aura qu'**un seul type Query** qui retournera une `String`.

```js
type Query {
  greeting: String
}
```

Nous pouvons utiliser **n'importe quel langage de programmation** pour créer un schéma GraphQL et **construire une interface autour**, mais comme je l'ai expliqué précédemment, nous utiliserons Apollo server pour exécuter les requêtes GraphQL. 

Nous créons donc un nouveau fichier `server.js` dans le répertoire serveur pour définir le schéma.

```text
📁 projet
├── 📁 client
└── 📁 serveur
    └── 📄 server.js
```

Maintenant, nous installons apollo-server en exécutant `npm install apollo-server`.

Nous devons importer la **fonction tag** `gql` depuis **apollo-server** pour analyser le schéma de cette manière : `const {gql} = require('apollo-server');` puis déclarer une constante `typeDefs` qui est un [arbre de syntaxe abstraite](https://en.wikipedia.org/wiki/Abstract_syntax_tree) du code Graphql.

> Lorsqu'un serveur GraphQL reçoit une requête à traiter, elle arrive généralement sous forme de chaîne. Cette chaîne doit être tokenisée et analysée en une représentation que la machine comprend. Cette représentation est appelée un arbre de syntaxe abstraite.

Si vous souhaitez en savoir plus sur les arbres de syntaxe abstraite, [AST Explorer](https://astexplorer.net/) est un outil en ligne qui vous permet d'explorer l'arbre de syntaxe créé par un langage choisi en tant qu'analyseur.

Le fichier `server.js` ressemblerait à ceci :

```js
const { gql } = require('apollo-server');

const typeDefs = gql`
  type Query {
    greeting: String
  }
`;
```


## Comment ajouter la fonction de résolution

Maintenant que nous avons défini notre schéma, nous avons besoin d'un moyen de répondre aux requêtes du client pour ces données : les **résolveurs**.

**Un résolveur est une fonction qui gère les données pour chacun des champs de votre schéma**. Vous pouvez envoyer ces données au client en **récupérant une base de données backend** ou une **API** tierce, entre autres.

Ils doivent **correspondre aux définitions de type du schéma**. Dans notre cas, nous n'avons qu'une seule définition de type, Query, qui retourne un greeting de type `String`, nous allons donc définir un résolveur pour le champ `greeting`, comme ceci :

```js
const resolvers = {
  Query: {
    greeting: () => 'Hello GraphQL world!👋',
  },
};
```

Comme je l'ai expliqué au début, nous garderons cet exemple aussi simple que possible. Mais gardez à l'esprit que dans un cas réel, **c'est ici que vous devez faire les requêtes** à la base de données, à l'API externe, ou à celle que vous avez l'intention d'utiliser pour extraire les données de la requête.


## Comment configurer le serveur

Dans le même fichier `server.js`, nous définissons et créons un nouvel objet `ApolloServer`, en passant le `Schema` (typeDefs) et les `resolvers` en tant que paramètres.

```js
const { ApolloServer, gql } = require('apollo-server');

const server = new ApolloServer({ typeDefs, resolvers });
```

Ensuite, en appelant la méthode `listen`, nous démarrons le serveur sur le `port` que nous spécifions dans les paramètres.

```js
server
  .listen({ port: 9000 })
  .then(serverInfo => console.log(`Server running at ${serverInfo.url}`));
```

Nous pouvons également **déstructurer** l'URL de ServerInfo lors de la journalisation.

```js
server
  .listen({ port: 9000 })
  .then(({ url }) => console.log(`Server running at ${url}`));
```

Le fichier `server.js` devrait ressembler à ceci pour le moment :

```js
const { ApolloServer, gql } = require('apollo-server');

const typeDefs = gql`
  type Query {
    greeting: String
  }
`;

const resolvers = {
  Query: {
    greeting: () => 'Hello GraphQL world!👋',
  },
};

const server = new ApolloServer({ typeDefs, resolvers });
server
  .listen({ port: 9000 })
  .then(({ url }) => console.log(`Server running at ${url}`));
```

Maintenant, si nous exécutons `node server/server.js`, nous aurons enfin notre serveur GraphQL opérationnel!🎉

Vous pouvez aller le vérifier sur [http://localhost:9000/](http://localhost:9000/)

```bash
~/graphql-hello-world-server
> node server/server.js
Server running at http://localhost:9000/
```

Si c'est la première fois que vous utilisez GraphQL, vous pourriez vous demander **quelle est cette application que je vois devant moi si nous n'avons pas écrit une seule ligne de code client?**.

La réponse à cette question est le **GraphQL Playground**.

![GraphQL Playground. Source: https://github.com/prisma-labs/graphql-playground](https://www.freecodecamp.org/news/content/images/2021/02/graphql-playground.png)

> [GraphQL Playground](https://github.com/prisma-labs/graphql-playground) est un IDE GraphQL graphique, interactif et intégré au navigateur, créé par [Prisma](https://www.prisma.io/) et basé sur [GraphiQL](https://github.com/graphql/graphiql). - [Docs Apollo](https://www.apollographql.com/docs/apollo-server/testing/graphql-playground/)

Mais que signifie cela ? Cela signifie que c'est un environnement où nous pouvons effectuer des requêtes, des mutations ou des abonnements sur notre schéma et interagir avec ses données.

Si vous avez déjà travaillé avec des requêtes **RESTful**, cela serait quelque chose d'équivalent à [Postman](https://www.postman.com/). C'est juste que ici vous **n'avez pas à télécharger et configurer quoi que ce soit**, cela **vient par défaut** avec Apollo !

![Awesome](https://www.freecodecamp.org/news/content/images/2021/02/awesome-chris-pratt.gif)
Alors essayons-le !

1. Dans le panneau de gauche, écrivez la requête `greeting` que nous avons définie dans notre schéma.
2. Ensuite, appuyez sur le bouton ▶ qui se trouve au milieu.
3. Et _Voilà !_ Dans le panneau de droite apparaît les données que nous avons définies dans notre résolveur pour retourner.

![Écrire une requête sur GraphQL Playground](https://www.freecodecamp.org/news/content/images/2021/02/greeting-query-on-playground.gif)

## Comment configurer le client

Maintenant que notre serveur est opérationnel, concentrons-nous sur la partie client. Nous allons commencer par créer un fichier `client.html` dans notre dossier client.

```text
📁 projet
├── 📁 client
|   └── 📄 client.html
└── 📁 serveur
    └── 📄 server.js
```

Le fichier `index.html` contiendra les bases de tout fichier `HTML` et un en-tête de chargement `<h1>Chargement...</h1>` pour montrer quelque chose à l'utilisateur pendant que nous demandons les données au serveur.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Client Hello World GraphQL</title>
  </head>

  <body>
    <h1>Chargement...</h1>

    <script src="app.js"></script>
  </body>
</html>
```

## Comment récupérer les données du serveur

Tout d'abord, dans le même dossier client, nous créons un fichier `app.js` où nous écrirons la logique du client pour récupérer les données du serveur.

```text
📁 projet
├── 📁 client
|   └── 📄 client.html
|   └── 📄 app.js
└── 📁 serveur
    └── 📄 server.js
```

À l'intérieur, nous définissons l'URL du serveur à partir de laquelle nous ferons la requête.

```js
const GRAPHQL_URL = 'http://localhost:9000/';
```

Ensuite, nous définissons notre fonction asynchrone `fetchGreeting()` pour récupérer le message de salutation du serveur. Nous utiliserons l'[API fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) pour effectuer la requête HTTP qui, par défaut, retourne une promesse à laquelle nous pouvons nous abonner et obtenir la réponse de manière asynchrone.

```js
async function fetchGreeting() {
  const response = await fetch(GRAPHQL_URL, {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
    },
    body: JSON.stringify({
      query: `
        query {
          greeting
        }
      `,
    }),
  });

  const responseBody = await response.json();
  console.log(responseBody);
}
```

Un détail à prendre en compte est que la méthode de la requête est `POST`. Cela peut nous confondre si nous avons l'habitude de travailler avec `RESTful` car cette même requête faite en `RESTful`, où nous voulons simplement lire des informations du serveur, serait généralement faite avec la méthode `GET`.

Le problème est qu'avec GraphQL, nous faisons toujours des requêtes `POST` où nous passons **la requête dans la charge utile** (body).

Enfin, nous appelons simplement notre méthode `fetchGreeting();`

```js
const GRAPHQL_URL = 'http://localhost:9000/';

async function fetchGreeting() {
  const response = await fetch(GRAPHQL_URL, {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
    },
    body: JSON.stringify({
      query: `
        query {
          greeting
        }
      `,
    }),
  });

  const responseBody = await response.json();
  console.log(responseBody);
}

fetchGreeting();
```

Si vous ouvrez le fichier dans votre navigateur et regardez la **console dans les outils de développement**, vous pouvez voir que nous avons effectivement obtenu les données de salutation de la requête 🤌!

![Récupération des données du serveur](https://www.freecodecamp.org/news/content/images/2021/02/fetching-data-from-server-3.png)

## Comment afficher les données

Maintenant que nous avons réussi à obtenir les données du serveur, **mettons à jour le titre de chargement**. La première chose que nous ferons est de déstructurer la réponse et de retourner simplement les `data` de celle-ci.

Remplacez simplement cette partie du code :

```js
const responseBody = await response.json();
console.log(responseBody);
```

Par ceci :

```js
const { data } = await response.json();
return data;
```

Ensuite, nous mettrons à jour le titre avec le `greeting` retourné **à l'intérieur des données de la réponse**

```js
fetchGreeting().then(({ greeting }) => {
  const title = document.querySelector('h1');
  title.textContent = greeting;
});
```

Ainsi, notre fichier `app.js` aura finalement cet aspect :

```js
const GRAPHQL_URL = 'http://localhost:9000/';

async function fetchGreeting() {
  const response = await fetch(GRAPHQL_URL, {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
    },
    body: JSON.stringify({
      query: `
        query {
          greeting
        }
      `,
    }),
  });

  const { data } = await response.json();
  return data;
}

fetchGreeting().then(({ greeting }) => {
  const title = document.querySelector('h1');
  title.textContent = greeting;
});
```

Notre `index.html` aura le titre de chargement mis à jour avec les données récupérées de notre serveur!🎉

![Affichage des données](https://www.freecodecamp.org/news/content/images/2021/02/displaying-the-data.png)


## Conclusion

J'espère que vous avez apprécié cet article et que ce projet vous a aidé à comprendre **comment GraphQL fonctionne en coulisses**, du moins de manière très simple. 

Je sais qu'il y a beaucoup de choses que je n'ai pas expliquées ou que j'aurais pu approfondir. Mais comme tout projet `hello world`, celui-ci était destiné aux débutants, donc je voulais le garder aussi simple que possible.

J'ai hâte d'en apprendre davantage sur GraphQL et de l'utiliser dans de futurs projets. Si vous avez des questions, des suggestions ou des commentaires en général, n'hésitez pas à me contacter sur l'un des réseaux sociaux de [mon site](https://ramonmorcillo.com) ou [par email](mailto:hey@ramonmorcillo.com).

## Ressources utiles sur GraphQL

Voici une collection de liens et de ressources qui m'ont été utiles pour améliorer et en apprendre davantage sur GraphQL.

### Docs 📚

- [Code source du projet](https://github.com/reymon359/graphql-hello-world-server) - Le dépôt Github avec tout le code du projet.
- [Site principal de GraphQL](https://graphql.org/) - Site principal de GraphQL.
- [Documentation Apollo](https://graphql.org/) - La documentation de la plateforme Apollo.

### Apprendre 📝

- [How to GraphQL](https://www.howtographql.com/) - Tutoriels gratuits et open-source pour apprendre tout sur GraphQL, de zéro à la production.
- [GraphQL par l'exemple](https://www.udemy.com/course/graphql-by-example/) - Excellent cours où vous apprenez GraphQL en écrivant des applications full-stack JavaScript avec Node.js, Express, Apollo Server, React, Apollo Client.
- [Introduction à GraphQL](https://graphql.org/learn/) - Une série d'articles pour apprendre GraphQL, comment il fonctionne et comment l'utiliser.

### Outils 🔧

- [Apollo GraphQL](https://www.apollographql.com/) - Site principal de l'implémentation Apollo GraphQL.
- [GraphQL Playground](https://github.com/prisma-labs/graphql-playground) - Dépôt de l'IDE GraphQL Playground que nous avons utilisé dans le projet.

### IDE 💻

- [JS GraphQL](https://plugins.jetbrains.com/plugin/8097-js-graphql) - Plugin pour WebStorm et autres IDE basés sur IntelliJ pour supporter le langage GraphQL, y compris les littéraux de gabarits étiquetés en JavaScript et TypeScript.
- [GraphQL](https://marketplace.visualstudio.com/items?itemName=Prisma.vscode-graphql) - Extension GraphQL pour VSCode qui ajoute la coloration syntaxique, la validation et des fonctionnalités de langage comme aller à la définition, les informations de survol et l'autocomplétion pour les projets GraphQL. Cette extension fonctionne également avec les requêtes annotées avec le tag gql.
- [GraphQL pour VSCode](https://marketplace.visualstudio.com/items?itemName=kumar-harsh.graphql-for-vscode) - Coloration syntaxique GraphQL pour VSCode, linting, auto-complétion et plus encore !

### Extras 🍎

- [APIs GraphQL](https://github.com/APIs-guru/graphql-apis) - Une liste d'APIs publiques GraphQL pour tester vos compétences ou construire quelque chose avec elles.
- [GraphQL : Le documentaire](https://www.youtube.com/watch?v=783ccP__No8) - Une vidéo de 30 minutes qui explore l'histoire de l'apparition de GraphQL et l'impact qu'il a sur les grandes entreprises technologiques mondiales, y compris Facebook, Twitter, Airbnb et Github.


J'espère que vous avez apprécié cet article. Vous pouvez également le lire [sur mon site](https://ramonmorcillo.com/getting-started-with-graphql-and-nodejs/) avec d'autres ! Si vous avez des questions, des suggestions ou des commentaires en général, n'hésitez pas à me contacter sur l'un des réseaux sociaux de [mon site](https://ramonmorcillo.com/).