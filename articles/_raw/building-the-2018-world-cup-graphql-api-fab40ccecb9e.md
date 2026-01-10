---
title: How we built the 2018 World Cup GraphQL API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-20T14:35:46.000Z'
originalURL: https://freecodecamp.org/news/building-the-2018-world-cup-graphql-api-fab40ccecb9e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*y_uooSFcpVZy14uv
tags:
- name: Grandstack
  slug: grandstack
- name: api
  slug: api
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: World Cup
  slug: world-cup
seo_title: null
seo_desc: 'By Michael Hunger

  After the second round of matches at World Cup 2018 got underway, we wanted to create
  an easy way for people to answer all their questions about the teams involved.


  TL;DR

  We’ve created a Neo4j backed GraphQL API for World Cup 2018....'
---

By Michael Hunger

After the second round of matches at World Cup 2018 got underway, we wanted to create an **easy way** for people to answer all their questions about the teams involved.

![Image](https://cdn-media-1.freecodecamp.org/images/0*y_uooSFcpVZy14uv)

### TL;DR

We’ve created a Neo4j backed GraphQL API for World Cup 2018. You can play with it [here](https://worldcup-2018.now.sh/).

### Building a GraphQL API backed by Neo4j

We’d already created a [database with _all the World Cup Data_](https://medium.com/neo4j/world-cup-2018-graph-19fbac0a75db) for people to use and query with, but we wanted to make the data accessible to people who don’t know Neo4j’s query language, Cypher.

**GraphQL to the rescue!**

Before we get to that, let’s first take a look at the Neo4j graph model that we’ve created.

![Image](https://cdn-media-1.freecodecamp.org/images/0*zfRcG-bR_cMXR8cF)

The **WorldCup** node sits in the middle of our graph, and all other parts of the model revolve around that. We have one WorldCup node for each tournament.

Next up we have the host **Country** which is connected to the WorldCup node by a **HOSTED_BY** relationship. **Matches** also belong to a WorldCup**,** and each **Country** names a **Squad of Players** that will represent them in a WorldCup tournament_._

A player is connected to an **Appearance** node for each match that they participate in either as a starter or substitute. If they score a **Goal,** the Appearance node will connect to that Goal node.

### The GRANDstack Starter Kit

Ok that’s enough Neo4j, let’s get back to GraphQL.

The GRANDstack combines **G**raphQL, **R**eact, **A**pollo and **N**eo4j **D**atabase into an easy to use bundle for quickly building APIs and apps. It uses the GraphQL schema to automatically transpile GraphQL queries to **single** Neo4j queries and is able to auto-generate all queries, mutations, and fields from the annotated schema.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HqKavloPXkMx3dNIkvK8Vw.png)
_GRANDstack Logo_

We used the [GRANDstack.io starter kit](https://github.com/grand-stack/grand-stack-starter/tree/master/api) to create a GraphQL API on top of our existing Neo4j database.

It consist of two parts: a backend `api` and a front-end `ui`. The backend serves the GraphQL API and also a GraphQL Playground (a really neat browser and editor for GraphQL queries), which also provides the data schema, docs, and auto-completion.

We forked it to our own repository and then merged it back to a [branch `worldcup`](https://github.com/grand-stack/grand-stack-starter/tree/worldcup) for you to use.

The first step is to create a **GraphQL schema**. You can see what we came up with below, which closely matches what we have above in our Graph Model.

A minimal schema looks like this:

We extended it quite a bit with some GRANDstack specific Neo4j extensions to have some alternative mappings and so on.

[**grand-stack/grand-stack-starter**](https://github.com/grand-stack/grand-stack-starter/blob/worldcup/api/src/graphql-schema.js)  
[_grand-stack-starter - Simple starter project for GRANDstack full stack apps_github.com](https://github.com/grand-stack/grand-stack-starter/blob/worldcup/api/src/graphql-schema.js)

Once we’d defined the schema, we updated our .env file to point to our Neo4j Cloud (https://neo4j.com/cloud/) hosted database.

```
NEO4J_URI=bolt://c27d992b.databases.neo4j.ioNEO4J_USER=worldcupNEO4J_PASSWORD=worldcup
```

You can run this locally by executing `yarn && yarn start`. That will launch the Playground at [http://localhost:4000,](http://localhost:4000,) where you can start to play around with some queries.

We can write some queries to find the world’s best player.

![Image](https://cdn-media-1.freecodecamp.org/images/0*A5TZARxOgWIqVRc4)
_GraphQL Playground_

Of course we can find out much more about him.

![Image](https://cdn-media-1.freecodecamp.org/images/0*2Q2NxAJRiibIYumb)
_Result for details on Messi_

### Deploy to zeit.now

Now we’re ready to deploy. We could deploy our service to anywhere that hosts Node.js apps, but @Will.Lyon recommended [Zeit Now](https://zeit.co/now) — a great and easy to use service for hosting your app that has an easy to use free plan for small projects.

We just install the service and then run the `now` command in our directory to deploy. For stable URLs, you can alias the project to a fixed name.

The GraphQL server is deployed at [https://worldcup-2018.now.sh/](https://worldcup-2018.now.sh/) and is ready for use now. Let’s have a look at the types of queries we can run against the dataset.

#### Portugal vs. Morocco

As I’m writing this post, **Portugal** is playing **Morocco.** We can check for the latest score by executing this GraphQL query in the playground defined above.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ZQMuxQj0WEr0yiKC)
_Portugal vs. Morocco results_

Portugal are 1–0 up at the moment, and it’s no surprise to learn that Cristiano Ronaldo was the scorer.

#### Who is Cristiano?

If we want to learn more about Cristiano, we can query for players as well. For example, the following query will show us his date of birth and how many goals he’s ever scored in the World Cup, as well as how many goals he has scored this time around:

So he’s got 4 goals in World Cup 2018 and 7 in total, which means he’s got more goals in this tournament than the previous ones combined!

#### Germany’s score in 1990

Although Germany didn’t get off to a great start in this World Cup, we can write a nostalgic query to find out the score of the 1990 World Cup final:

#### Bad times in 1966 :(

Or we could look back to 1966, as my colleague Mark forced me to do:

### Keeping the data fresh

The database is being updated via a Lambda job every few minutes while matches are being played, so the data should be reasonably fresh whenever you query it.

![Image](https://cdn-media-1.freecodecamp.org/images/0*y1MqPFFZjGLJb6Mt)

### The React UI

The front-end `ui` is basically just a React app that uses Apollo Client to query our API and render the results in components.

Please note that the current React code is really ugly and horrible. We leave that as challenge to you to build beautiful web and/or mobile apps using the **World Cup GraphQL API**. :)

![Image](https://cdn-media-1.freecodecamp.org/images/1*1dH26XFHo70f9Ns1CEgkyA.png)
_my (ugly) world cup screen_

Of course you can also use Vue or Angular or other ui-frameworks you love.

It connects to the URL provided in the `.env` file, where we just put either our local `http://localhost:4000` or our now.sh URI.

```
REACT_APP_GRAPHQL_URI=https://worldcup-2018.now.sh/
```

Again, a single `now` command deploys our UI as well. In our case we don’t need it, but Zeit now has support if you have any secret credentials.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SA6pQOO4Bb50zPeu0dO4oQ.jpeg)

### GRANDstack Hackathon

Luckily, the [GRANDstack Hackathon](https://blog.grandstack.io/announcing-the-grandstack-online-hackathon-for-graphql-europe-2018-7d256ebf68e1) is **still ongoing to gather great ideas** and there are some really cool prizes for your submissions.

> Thanks a lot to my colleague [Mark Needham](https://www.freecodecamp.org/news/building-the-2018-world-cup-graphql-api-fab40ccecb9e/undefined) for doing all the hard work of putting the data and model together.

