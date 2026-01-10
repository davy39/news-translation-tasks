---
title: How to work with FaunaDB + GraphQL
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
seo_title: null
seo_desc: 'By Jeff M Lowery

  I have one or two projects I maintain on Netlify, in addition to hosting my blog
  there. It’s an easy platform to deploy to, and has features for content management
  (CMS) and lambda functions (by way of AWS).

  What I needed for my late...'
---

By Jeff M Lowery

I have one or two projects I maintain on [Netlify](https://www.netlify.com/), in addition to hosting my blog there. It’s an easy platform to deploy to, and has features for content management (CMS) and lambda functions (by way of AWS).

What I needed for my latest project, though, was a database. Netlify has integrated [FaunaDB](https://fauna.com/): a NoSQL, document-oriented database. Fauna has recently [boasted support for GraphQL](https://fauna.com/blog/the-worlds-best-serverless-database-now-with-native-graphql), which is a big plus. At no charge and with a simplified setup, why not try it?

## The database

Fauna has a unique approach to managing [transactions across globally distributed data stores](https://fauna.com/blog/consistency-without-clocks-faunadb-transaction-protocol), so that that database records don’t get out of sync when they’re updated from points far and wide. This is a problem for global enterprises with high transaction volumes, but irrelevant for my small project.

## The application

I’m a chess player of middling ability and I want to set up data to do analysis of master-level chess games. SQL or NoSQL didn’t matter—I’ve worked with both and either would support my application’s modest needs.

I love GraphQL, and have been using it since 2016. I don’t want my GraphQL schema exposed on the client side, though. The way around this is to have lambda functions to do the GraphQL requests, then have the client use those functions as a sort of proxy.

## The implementation

I started with [netlify-fauna-example](https://github.com/netlify/netlify-faunadb-example)*. This doesn’t use GraphQL; instead the example’s [Netlify Functions](https://www.netlify.com/docs/functions/) use FQL: [Fauna Query Language](https://docs.fauna.com/fauna/current/api/fql/). You can execute queries via [fauna shell](https://github.com/fauna/fauna-shell), or by [using a NodeJS client module](https://github.com/fauna/faunadb-js). The following uses the client to insert a **todoItem** into the **todos** collection:

todos-create.js

```js
  ...
  /* construct the fauna query */
  return client.query(q.Create(q.Ref('classes/todos'), todoItem))
    .then((response) => {
      console.log('success', response)
      /* Success! return the response with statusCode 200 */
      return callback(null, {
        statusCode: 200,
        body: JSON.stringify(response)
      })
    }).catch((error) => {
      console.log('error', error)
      /* Error! return the error with statusCode 400 */
      return callback(null, {
        statusCode: 400,
        body: JSON.stringify(error)
      })
    })
```

To use GraphQL, I need to create a database on Fauna, and then import a GraphQL schema. Once you’ve created an account on Fauna, you can do all this through their dashboard.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-29-at-11.27.05-AM---Edited.png)
_My new Fauna database_

Once done, a set of collections (akin to tables in SQL) are created based on my imported GraphQL type definitions. Interestingly, new types and fields are also added to handle stuff like identifying instances and managing relations between types. For instance, my type for Opening was:

```gql
type Opening {
  desc: String!
  fen: String!
  SCID: String!
}
```

and when I go to the dashboard, open GraphQL Playground, and look at the schema, I see:

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-28-at-1.05.59-PM.png)

OpeningInput and OpeningPage were added by Fauna, in addition to the _id and _ts fields in Opening.

### Queries and Mutations

There are certain queries and mutations that will be automatically implemented for you by Fauna _if_ you define them in the schema you created. When I define the type to hold chess opening information, I _may_ then include the following Query and Mutation definitions in my schema:

```text
type Query {
 allOpenings: [Opening]
}
```

And FaunaDB will provide an implementation.

### lambda functions

The original lambdas in [netlify-fauna-example](https://github.com/netlify/netlify-faunadb-example) speak FQL. To convert these to GraphQL requests, use a fetch library such as node-fetch, and make HTTPS requests to the Fauna GraphQL endpoint using an client like the one included with [apollo-boost](https://levelup.gitconnected.com/giving-react-a-lift-with-apollo-boost-74c6ff32894d):

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

The code above requests the FEN strings for all the openings in the Opening collection.

## Are we done now? No.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-217.png)
_Photo by [Unsplash](https://unsplash.com/@sarti46?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Massimo Sartirana</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Fauna’s GraphQL support is in a functional but still formative stage. One of the things I wanted to do was have batch insert ability so I wouldn’t have to insert once opening at a time into the Opening collection. This mutation isn’t created by Fauna automatically (though it is ticketed feature request), so I had to define a resolver for it.

Fauna has a [@resolver](https://docs.fauna.com/fauna/current/api/graphql/directives/d_resolver) directive that can be used on mutation definitions. It will direct Fauna to use a user-defined function written in FQL; these can be written directly in the shell. For a collection of simple types like Opening, the resolver FQL is pretty straightforward.

First, I go to the FaunaDB Console Shell, and create the function `add_openings`:

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

Openings is an array, and the Map method executes Create call on each element. I then add a @resolver directive to my mutation definition in the schema I will import (referred to as a **custom resolver**):

```text
type Mutation {
   addOpenings(openings: [OpeningInput]) : [Opening]! @resolver(name: "add_openings" paginated:false)
}
```

Now when the mutation is executed via the GraphQL client, `add_openings` is called and will insert all games passed in as a parameter to the mutation. From the GraphQL client it looks like this:

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

## The old chicken and egg problem

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-218.png)
_Photo by [Unsplash](https://unsplash.com/@chromatograph?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Chromatograph</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

You’ll notice in the mutation above that I refer to the OpeningInput type. In order for me to import my schema into Fauna, that type has to be defined. But… when I imported Opening, Fauna auto-generated that type for me. When I define it in my schema later (for the mutation), I essentially override that type. Since that generated type is used in generated mutations (ie., createOpening, singular), by overriding that type definition in my own schema I could possibly break one of the generated mutations.

The solution suggested is to not override the OpeningInput type, but to rename my input type to something like MyOpeningInput. That ensures that my import schema validates, and doesn’t mess with what the generated mutations expect.

The problem gets messier, though, when you use the [@relation](https://fauna.com/blog/getting-started-with-graphql-part-2-relations) directive. That directive generates types used to relate two other type instances.

Here’s the relation in my import schema. Note the directive:

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

To store a Game, I need to have also a required Header (Opening is not required). The relation is maintained by a Fauna-generated **ref** field on the Header. It's defined for the mutation through the use of a GameHeaderRelation type that allows the creation of both Game and Header in a single mutation. Here are the relevant generated types:

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

Now to add a game with the required header info, I can call the mutation like so, from within the Playground:

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

Let' say I now want to create a mutation to batch upload multiple games. Unfortunately I don’t have access to the generated **GameHeaderRelation** type, or any of the other input types. My import schema won’t validate without those defined if I try to use them in my bulk mutation definition. Again, bulk mutations are a ticketed feature request, so they should be available soon. Yet this type of issue will arise regarding any custom resolver’s use of types.

I though for a minute that the solution would be to download the generate schema (from Playground), then modify it with my bulk mutations. However, I am _overriding_ **__**the otherwise-generated types on import, which is not what I want to happen.

### The workaround: write a custom resolver in FQL

As stated, I need to ensure that when I create a function for my addGames resolver to call, there has to be a Header created first for each game.

The GraphQL Schema resolver attribute calls the FQL add_games function:

```text
addGames(games: [GameInput]) : [Game]! @resolver(name: "add_games", paginated: false)
```

And here’s the function definition for add_games:

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

I’m not an FQL expert (see acknowledgments), but this code is readable (from innermost outward):

1. creates a header instance
2. selects its generated reference field “ref”
3. merges that reference as field “header” into the a data object “X”
4. “X” represents one element of the input array parameter “games” (GameInput)

I should note that one of Fauna’s engineers stated that maintaining references _by hand_ is “tricky”. It requires understanding of what is going on beneath the covers. The [@embedded](https://docs.fauna.com/fauna/current/api/graphql/directives/d_embedded) type of relation may be easier to implement in FQL if the relation is one-to-one, as in this case.

## Where to go from here…

Fauna’s support team and Slack community forum members have been exceedingly helpful with questions and have even offered help with implementing FQL functions. They’re also forthcoming when onsite documentation is incomplete or wrong.

Performance wasn’t great: the bulk insert of a 1000 small documents executed in matters of seconds, which is slow. However I didn’t use pagination in my resolvers, and that may make a significant difference. It is also possible that the GraphQL features are in a slower debuggable configuration as Fauna ramps up the feature set.

To write custom resolvers, it is necessary to master [FQL](https://docs.fauna.com/fauna/current/api/fql/). Its [LISPish](https://www.tutorialspoint.com/lisp/lisp_basic_syntax.htm) syntax will appeal to some, but I find it verbose and “nesty”. For simple CRUD operations it is fine. You may not find yourself writing many custom resolvers, either.

I chose to try Fauna not for its strengths, but for convenience. I may come back to it in a few months and see how it has progressed.

**Acknowledgements**

I’d like to thank Summer Schrader, Chris Biscardi, and Leo Regnier for their patience and insight.

---

* I guess my life isn’t interesting enough: when I clone a project like netlify-fauna-example, I will usually then run `npm update outdated` and `npm audit fix`. I can expect to encounter issues when I do this, but in practice I usually resolve them in an hour or two.

**Not this time.** I deleted node_modules, package-lock.json, and even did a forced clean of the cache before reinstalling everything. Didn’t work. I eventually switched over to **yarn**, deleted the above (but left the updated version info in package.json alone) and installed. After a few hiccups, success! Here are the dependency versions I would up with:

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

  

