---
title: ⚡ Comment ajouter un serveur GraphQL à une API RESTful Express.js en 2 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-22T21:34:31.000Z'
originalURL: https://freecodecamp.org/news/add-a-graphql-server-to-a-restful-express-js-api-in-2-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/ghgojj3wde2074i3n9bu.png
tags:
- name: Apollo GraphQL
  slug: apollo
- name: Express JS
  slug: express-js
- name: GraphQL
  slug: graphql
seo_title: ⚡ Comment ajouter un serveur GraphQL à une API RESTful Express.js en 2
  minutes
seo_desc: 'By Khalil Stemmler

  You can get a lot done in 2 minutes, like microwaving popcorn, sending a text message,
  eating a cupcake, and hooking up a GraphQL server.

  Yup. If you have an old Express.js RESTful API lying around or you''re interested
  in increment...'
---

Par Khalil Stemmler

On peut faire beaucoup de choses en 2 minutes, comme faire éclater du pop-corn au micro-ondes, envoyer un message texte, manger un cupcake, et **configurer un serveur GraphQL**.

Oui. Si vous avez une ancienne API RESTful Express.js qui traîne ou si vous êtes intéressé à adopter progressivement GraphQL, nous n'avons besoin que de 2 minutes pour la configurer avec un tout nouveau serveur GraphQL.

Prêt ? À vos marques. Partez !

Disons que votre serveur ressemble à quelque chose comme ceci.

```typescript
import express from 'express';
import { apiRouter } from './router';

const app = express();
const port = process.env.PORT || 5000;

// Routes existantes pour notre application Express.js
app.use('/api/v1', apiRouter);

app.listen(port, () => console.log(`[App]: Listening on port ${port}`))

```

À la racine de votre projet, `npm install` [apollo-server-express](https://github.com/apollographql/apollo-server/tree/master/packages/apollo-server-express) comme dépendance.

```
npm install apollo-server-express --save

```

Allez là où votre application Express est définie et importez `ApolloServer` et `gql` depuis `apollo-server-express`.

```typescript
import { ApolloServer, gql } from 'apollo-server-express'

```

Ensuite, créez une instance d'un `ApolloServer` avec les **définitions de types** et les **résolveurs** les plus simples possibles en GraphQL.

```typescript
const server = new ApolloServer({
  typeDefs: gql`
    type Query {
      hello: String
    }
  `,
  resolvers: {
    Query: {
      hello: () => 'Hello world!',
    },
  }
})

```

Enfin, utilisez la méthode [applyMiddleware](https://www.apollographql.com/docs/apollo-server/api/apollo-server/?utm_source=devto&utm_medium=blog_post&utm_campaign=add_graphl_server_express_2_mins#apolloserverapplymiddleware) de `ApolloServer` pour passer notre serveur Express.js.

```typescript
server.applyMiddleware({ app })

```

Boom. C'est tout !

Votre code devrait ressembler à quelque chose comme ceci.

```typescript
import express from 'express';
import { v1Router } from './api/v1';
import { ApolloServer, gql } from 'apollo-server-express'

const app = express();
const port = process.env.PORT || 5000;

const server = new ApolloServer({
  typeDefs: gql`
    type Query {
      hello: String
    }
  `,
  resolvers: {
    Query: {
      hello: () => 'Hello world!',
    },
  }
})

server.applyMiddleware({ app })

app.use('/api/v1', v1Router);

app.listen(port, () => {
  console.log(`[App]: Listening on port ${port}`)
})

```

Si vous naviguez vers `localhost:5000/graphql`, vous devriez pouvoir voir votre schéma GraphQL dans le bac à sable GraphQL.

![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/wd4tiobfydytzdtamlef.png)

Remarque : Si vous souhaitez changer l'URL où se trouve le point de terminaison GraphQL de `/graphql` à autre chose, vous pouvez passer une option `path` à `server.applyMiddleware()` avec l'URL que vous souhaitez, comme `path: '/specialUrl'`. Consultez la [documentation](https://www.apollographql.com/docs/apollo-server/api/apollo-server/?utm_source=devto&utm_medium=blog_post&utm_campaign=add_graphl_server_express_2_mins#apolloserverapplymiddleware) pour une utilisation complète de l'API.

À quel point c'était simple ? Votre pop-corn est-il prêt ? ?

## Résumé

Voici ce que nous avons fait.

1. Installer `apollo-server-express`
2. Créer un `new ApolloServer`
3. Connecter votre serveur GraphQL avec `server.applyMiddleware`

J'aime personnellement le fait que Apollo Server soit non intrusif et puisse être ajouté à n'importe quel projet comme une alternative pour communiquer entre les services et les applications.

## Où aller à partir d'ici

Si vous êtes nouveau dans Apollo et GraphQL, une excellente façon d'apprendre est de construire quelque chose en vrai. Pour cette raison, je vous recommande vivement de consulter le [Tutoriel Fullstack Apollo (vous pouvez aussi apprendre en TypeScript maintenant ?)](https://www.apollographql.com/docs/tutorial/introduction?utm_source=freecodecamp&utm_medium=blog_post&utm_campaign=add_graphl_server_express_2_mins).

Je suis [Khalil Stemmler](https://twitter.com/stemmlerjs), un Développeur Advocate chez Apollo GraphQL. J'enseigne les meilleures pratiques avancées de TypeScript, GraphQL et Node.js pour les applications à grande échelle. N'hésitez pas à me contacter sur [Twitter](https://twitter.com/stemmlerjs) si vous avez besoin d'aide pour quoi que ce soit lié à Apollo, TypeScript ou l'architecture. Santé ?