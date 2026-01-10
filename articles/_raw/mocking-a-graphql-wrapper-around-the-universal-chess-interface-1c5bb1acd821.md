---
title: Mocking a GraphQL Wrapper around the Universal Chess Interface
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
seo_title: null
seo_desc: 'By Jeff M Lowery


  _Photo by [Unsplash](https://unsplash.com/@samuelzeller?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Samuel
  Zeller / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utmcampaign=api-credit)

  The Un...'
---

By Jeff M Lowery

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-253.png)
_Photo by [Unsplash](https://unsplash.com/@samuelzeller?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Samuel Zeller</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

The Universal Chess Interface (UCI) has been around a long time and used by many chess engines. What does GraphQL bring to the mix?

I had some email exchanges with an owner of a chess website recently, and he asked me what I knew about UCI and websockets. That got me looking closer at UCI and thinking about how and why one would wrap a GraphQL schema around it.

### The Universal Chess Interface

The UCI has [been around for over a decade](http://wbec-ridderkerk.nl/html/UCIProtocol.html), and is based on standard I/O messaging between a chess engine and its client (usually a graphical UI). The client submits a message to the chess engine, and the engine **may** send back a response. I say **may** because UCI doesn’t require a response for some incoming messages to the chess engine.

The engine also **might** send back more than one response. During game analysis, the engine will be sending back **info** packets detailing it’s thinking. The client says what the start position is, tells it “Go”, and the engine keeps going until it arrives at a **best move.** During the process, the engine streams back messages about what it’s thinking.

The UCI specification is short, and you don’t need a deep understanding of it to see the basics of how it works — and it has worked well so far, so why monkey with it?

If the engine resides on a remote server, then just open a websocket and do as you would normally do. That works, of course, but it doesn’t hurt to look at the pros and cons of doing things slightly differently.

### Chess Engine versus Chess Server

I want to start by mocking up a UCI service. A next step will be to build a functional prototype and, as always seems to be the case, its not hard to find a Node.js package that helps with most of the work.

One of the more popular engines is called [Stockfish](https://stockfishchess.org/). Someone has taken the trouble of transpiling it from C++ to JavaScript so that the engine can be run wholly in Node.js.

It’s this simple:

* create and cd into a folder
* `npm init`
* `npm install stockfish`
* `node node_modules/stockfish/src/stockfish.js`

And now you are in a Stockfish command shell, and can start typing in commands.

The first thing to do is to fire up the UCI interface by typing `uci`. You should get a response like this:

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

It shows what the option settings are set to and then returns `**uciok**`, meaning the interface is ready. The next step is to set options and then call `**isready**`, and when the engine responds `**readyok**`, it can start analyzing a chess position.

I won’t actually be using this engine for my mock implementation, but it does come in handy if I want to examine what a command does using a real engine.

In a real server implementation, I would be firing up one engine per client (or perhaps more). [GraphQL](http://graphql.org/) helps me define an API that would support multiple clients running multiple engines.

### GraphQL

For this mock, I’ve divide up the UCI component into HTTP requests of a call/response nature, and websocket subscriptions for handling streaming responses. This means that a socket is only open if the user wants to subscribe to detailed information about what the engine is thinking. Furthermore, I can refine the number and types of **info** messages I receive on the client, so that socket traffic is minimized.

#### **Each command gets a response**

Because client-server interaction is happening (in most cases) over unreliable HTTP, it’s important that the client (running on the browser) knows that its message got through to the server. The UCI command `**setoption**`, for instance, doesn’t send a response back according to the specification.

That’s fine for an interface based on reliable sockets, not so good for HTTP requests. GraphQL ensures that there is a response sent back to every received request, if only to acknowledge that the request was received.

#### **Each command and its arguments are type-safe**

GraphQL interfaces are schema-based, UCI interfaces are not (they’re based on descriptive text in the specification). If a client to sends an invalid command, the chess engine server should never have to deal with it. By defining UCI in terms of types in GraphQL, I can waylay an errant command at the API level — in GraphQL — before it gets to the engine.

#### **GraphQL resolvers can decompose responses into JSON structures**

JavaScript is the language of the internet, and GraphQL returns JSON responses. By having the GraphQL resolvers take a UCI response and break it down in a fine-grained and structured way, the client is alleviated of the UCI response parsing task.

#### **I can easily mock my API using Apollo GraphQL Tools**

After designing an API, but before heading off to implementation land, it’s useful to first check the API look and feel of using mocks. The [graphql-tools](https://github.com/apollographql/graphql-tools) package makes [this easy and painless](https://medium.freecodecamp.org/mocking-graphql-with-graphql-tools-42c2dd9d0364). You can even mix mocks with real resolvers, giving you the option of iterative implementation of your API.

#### I can interact with the API through the GraphiQL service

[Graph**i**QL](https://github.com/graphql/graphiql) is the interactive service that can be run atop a GraphQL server. This is convenient for doing ad hoc testing of the API, based on either a mock or implementation.

### On to the Mocking!

Let’s take a look at the dependencies first:

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

I’m calling this server **chessQ**, and the server itself will be based on `**apollo-server-express**`, the Apollo Group’s GraphQL server implementation. The `**stockfish.js**` package, mentioned earlier, is included as an embedded engine. Though this mock doesn’t use it, it’s there for reference. In a real implementation, one would probably [access an externally running engine](https://www.npmjs.com/package/node-uci).

Included is `casual` and `randexp` for helping with the mocks. Finally, `**graphql-subscriptions**` and `**subscriptions-transport-ws**` will handle the streaming messages coming back from our mock while it is pretending to analyze.

### The chessQ schema

Let me first say that I haven’t spent time polishing up the schema, so consider it a first draft. It’s functional, but it will probably change as I continue to develop it. At the end of this article, I’ll link to a stable branch that corresponds to what is described here. I won’t be going into painstaking detail on the code, but will link to relevant source in GitHub where appropriate. Watch for those.

First thing is to define [the top-level queries](https://github.com/JeffML/chessQ/blob/chessQ-mock/schema.js). These are the entry points for the client:

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

The `createEngine` request will return an [EngineResponse](https://github.com/JeffML/chessQ/blob/chessQ-mock/readySchema.js), inside of which is an engine instance identifier that is used for subsequent requests:

```json
{
  "data": {
    "createEngine": {
      "engineId": "46d89031-03c3-4851-ae97-34e4b5d1d7c6"
    }
  }
}
```

The `**uci**` request will return a [UciResponse](https://github.com/JeffML/chessQ/blob/chessQ-mock/optionsSchema.js) detailing the current option settings. In the GraphQL schema, each type of option (spin, check, button, and combo) has its own specific fields:

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

A mock `uci query` might be:

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

and the response:

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

Technically, some of these commands could be thought of as Mutations, not Queries, since they change the state of the engine. But Mutations in GraphQL are primarily about sequential order-of-execution and that does not apply in this case: any option can be set in any order.

Ultimately, each engine instance will need to maintain some indication of its [state](https://github.com/JeffML/chessQ/blob/chessQ-mock/readySchema.js) (not implemented in this mock). These might be:

```js
enum eEngineState {
    CREATED
    INITIALIZED
    READY
    RUNNING
    STOPPED
  }
```

If for instance, a `**go**` command is sent before the engine state is `**READY**`, then that would be an error.

#### The Ready Schema

When the engine is READY, three new commands are possible:

* `ucinewgame`: tell the engine a new game has started
* `position`: tell the engine what the starting position is (along with any moves from that position)
* `go`: start the engine!

Before issuing the `**go**` command, the client has the option to subscribe to any [**info** messages](https://github.com/JeffML/chessQ/blob/chessQ-mock/schema.js) streaming in through the websocket (otherwise, there will be just a `BestMove` HTTP response when the engine is finished).

Details on how to set up a subscription service using [graphql-subscriptions](https://github.com/apollographql/graphql-subscriptions) can be found elsewhere, so here I will focus on the schema and resolver implementation.

The schema defines the types of `Subscriptions` available. For this mock, there is just one:

```graphql
type Subscription {
    info: Info
  }
```

The `Info` type, like the `Option` type, is a union of several specific info structures:

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

The precise meaning of these `Info` messages is irrelevant to this discussion. The important thing is to know that they come in any order, except for the `BestMove` message, which is last.

The client subscribes to info messages using a `subscription` request like the following:

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

There’s a resolver to handle the `Subscription` request, which uses methods in the `**graphql-subscriptions**` package:

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

In this subscription resolver, the the function passed to `withFilter` passes every message back. But a real subscribe resolver could be more discriminating based on parameters passed in by the client.

#### Seeing it in action

You can query, mutate, and subscribe in GraphiQL, so there’s no need to write a client for testing purposes. The one gotcha is that GraphiQL will enter “subscription” mode once a subscription is requested, and won’t happily respond to further commands.

The solution is to have two GraphiQL tabs open in your browser, one for issuing queries and mutations, and the other for listening to subscribed messages.

Download the [chessQ](https://github.com/JeffML/chessQ/tree/chessQ-mock) package, run `npm install` and then `npm run dev` . The chessQ mock application should now be running.

Open two tabs to [http://localhost:3001/graphiql](http://localhost:3001/graphiql).

In one tab, enter:

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

You’ll see a message that says:

```
"Your subscription data will appear here after server publication!"
```

![Image](https://cdn-media-1.freecodecamp.org/images/E2xSU2QP22UL1MvOuIqnnlc1ixS6zEU3nSLw)
_Ready to receive!_

To generate messages, there is a `**go**` resolver (shown below) that iterates through a [static set of info messages](https://github.com/JeffML/chessQ/blob/chessQ-mock/InfoGenerator.js) and publishes them one by one. Because the subscriber pane **will only show one message** at a time, there’s a simple `sleep` implementation that slows down the messaging so that you can see them fly by:

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

Finally, in the non-subscription tab, start the analysis with `**go**`:

```graphql
mutation go {
  go {
    __typename
    value
  }
}
```

While this tab is awaiting the `go` response showing the `BestMove`, the `subscription` tab will be catching info messages and displaying them one-by-one.

![Image](https://cdn-media-1.freecodecamp.org/images/Sead--yLEPWQIqOBgZlLM9czMcSB61AgRMxQ)
_Info messages coming in…_

![Image](https://cdn-media-1.freecodecamp.org/images/Ag3amWB0PTUL--3UjwwK-96bpH7vEUN5pUAY)
_Analysis complete!_

### Further Thoughts

Before rolling forth from mock to implementation, a couple of notes:

The simple pub/sub mechanism used in this example is neither robust or scalable. That’s okay, because there are [Redis](https://redis.io/) and [RabbitMQ](https://github.com/cdmbase/graphql-rabbitmq-subscriptions) implementations of graphql-subscription that are. A more refined subscription specification could also be defined and give fine-grained control to the subscriber as to which messages are received.

Not a lot of thought was given to managing websocket lifetime in this mock, which is something that needs to be considered if serving a large number of users.

All source code for this article can be found [here](https://github.com/JeffML/chessQ/tree/chessQ-mock).

