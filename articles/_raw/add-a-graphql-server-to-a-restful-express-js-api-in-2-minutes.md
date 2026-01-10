---
title: ⚡ How to Add a GraphQL Server to a RESTful Express.js API in 2 Minutes
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
seo_title: null
seo_desc: 'By Khalil Stemmler

  You can get a lot done in 2 minutes, like microwaving popcorn, sending a text message,
  eating a cupcake, and hooking up a GraphQL server.

  Yup. If you have an old Express.js RESTful API lying around or you''re interested
  in increment...'
---

By Khalil Stemmler

You can get a lot done in 2 minutes, like microwaving popcorn, sending a text message, eating a cupcake, and **hooking up a GraphQL server**.

Yup. If you have an old Express.js RESTful API lying around or you're interested in incrementally adopting GraphQL, we only need 2 minutes to hook it up with a fresh new GraphQL Server.

Ready? Set. Go!

Let's say that your server looked something like the following.

```typescript
import express from 'express';
import { apiRouter } from './router';

const app = express();
const port = process.env.PORT || 5000;

// Existing routes for our Express.js app
app.use('/api/v1', apiRouter);

app.listen(port, () => console.log(`[App]: Listening on port ${port}`))

```

At the root of your project, `npm install` [apollo-server-express](https://github.com/apollographql/apollo-server/tree/master/packages/apollo-server-express) as a dependency.

```
npm install apollo-server-express --save

```

Go to where your Express app is defined and import `ApolloServer` and `gql` from `apollo-server-express`.

```typescript
import { ApolloServer, gql } from 'apollo-server-express'

```

Next, create an instance of an `ApolloServer` with the _simplest possible_ GraphQL **type definitions** and **resolvers**.

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

Lastly, use `ApolloServer`'s [applyMiddleware](https://www.apollographql.com/docs/apollo-server/api/apollo-server/?utm_source=devto&utm_medium=blog_post&utm_campaign=add_graphl_server_express_2_mins#apolloserverapplymiddleware) method to pass in our Express.js server.

```typescript
server.applyMiddleware({ app })

```

Boom. That's it!

Your code should look something like this.

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

If you navigate to `localhost:5000/graphql`, you should be able to see your GraphQL schema in the GraphQL playground.

![Alt Text](https://thepracticaldev.s3.amazonaws.com/i/wd4tiobfydytzdtamlef.png)

Note: If you want to change the URL that the GraphQL endpoint sits at from `/graphql` to something else, you can pass in a `path` option to `server.applyMiddleware()` with the URL you want, like `path: '/specialUrl'`. Check out the [docs](https://www.apollographql.com/docs/apollo-server/api/apollo-server/?utm_source=devto&utm_medium=blog_post&utm_campaign=add_graphl_server_express_2_mins#apolloserverapplymiddleware) for full API usage.

How simple was that? Is your popcorn finished? ?

## Summary

Here's what we did.

1. Install `apollo-server-express`
2. Create a `new ApolloServer`
3. Connect your GraphQL Server with `server.applyMiddleware`

I personally really love the fact that Apollo Server is non-intrusive and can be tacked on any project as an alternative way to communicate between services and applications.

## Where to go from here

If you're new to Apollo and GraphQL, a great way to learn is to actually build something in real life. For that reason, I highly recommend checking out the [Apollo Fullstack Tutorial (you can also learn in TypeScript now ?)](https://www.apollographql.com/docs/tutorial/introduction?utm_source=freecodecamp&utm_medium=blog_post&utm_campaign=add_graphl_server_express_2_mins).

I'm [Khalil Stemmler](https://twitter.com/stemmlerjs), a Developer Advocate at Apollo GraphQL. I teach advanced TypeScript, GraphQL, and Node.js best practices for large-scale applications. Feel free to ping me on [Twitter](https://twitter.com/stemmlerjs) if you need help with anything Apollo, TypeScript, or architecture-related. Cheers ?

