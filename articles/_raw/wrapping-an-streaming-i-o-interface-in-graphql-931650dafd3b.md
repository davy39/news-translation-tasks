---
title: How to Wrap a Streaming I/O Interface in GraphQL
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
seo_title: null
seo_desc: 'By Jeff M Lowery


  _Photo by [Unsplash](https://unsplash.com/@emcomeau?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Ezra
  Comeau-Jeffrey / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utmcampaign=api-credit)

  This...'
---

By Jeff M Lowery

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-252.png)
_Photo by [Unsplash](https://unsplash.com/@emcomeau?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Ezra Comeau-Jeffrey</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

This post will be about using GraphQL to handle a service that uses an I/O stream for interaction between client and server. In a previous post, I mocked up a GraphQL API to the [Universal Chess Interface](http://wbec-ridderkerk.nl/html/UCIProtocol.html) (UCI). The UCI uses [stdio](https://www.urbandictionary.com/define.php?term=stdio) to communicate, accepting commands from an input stream and sending responses via an output stream. I’ll be using UCI as an illustration, but I won’t be describing UCI in great detail.

### Stockfish

Stockfish is as well-known chess engine that supports UCI. Using NodeJS and the module stockfish.js (a JavaScript transpilation of the original), it is easy to setup a running engine that implements UCI via stdio:

* create and cd into a folder
* `npm init`
* `npm install stockfish`
* `node node_modules/stockfish/src/stockfish.js`

And from there you can type in UCI commands in terminal window and see the results.

### A review of [Query vs Mutation](http://graphql.org/learn/schema/#the-query-and-mutation-types)

Queries are executed in parallel. That is not a problem for a stateless API where each query will return the same result regardless of the order in which results are returned. **UCI is not stateless**, so commands and results have to operate in sequence. Here’s an example of interaction between the command line ‘client’ and chess engine:

```
GUI     engine

// tell the engine to switch to UCI mode
uci

// engine identify  
    id name Shredder
		id author Stefan MK

// engine sends the options it can change
		option name Hash type spin default 1 min 1 max 128
		option name NalimovPath type string default 
		option name NalimovCache type spin default 1 min 1 max 32
// the engine has sent all parameters and is ready
		uciok

// now the GUI sets some values in the engine
// set hash to 32 MB
setoption name Hash value 32
setoption name NalimovCache value 1
setoption name NalimovPath value d:\tb;c\tb

// this command and the answer is required here!
isready

// engine has finished setting up the internal values
		readyok

// now we are ready to go
```

Engine responses to client commands are indented. The first state transition is to initiate the UCI protocol, where the engine responds with default option settings and a **uciok** signal indicating it is finished. At this point, the client can configure options. These will only take effect when the command **isready** is issued. The engine responds with **readyok** when all options are set. Later state transitions will occur during game set up and analysis (not shown).

Running several queries in parallel may issue commands prematurely, since no query waits for the response of another query. The problem can be illustrated with a simple GraphQL API to an mock asynchronous service:

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

The results are:

![Image](https://cdn-media-1.freecodecamp.org/images/1*rqOQsfsW6HNp2ovNmvTSWQ.png)
_Order of resolution differs from response._

In the console windows (bottom half), you can see when responses were returned. Now execute the same requests via Mutation:

![Image](https://cdn-media-1.freecodecamp.org/images/1*6blqj1VzTMOohRjRHBG2zQ.png)
_Order of resolution matches order of response_

Getting a response takes longer because each operation must finish before the next is invoked.

#### What this means for a GraphQL UCI wrapper

[In a previous post](https://medium.freecodecamp.org/mocking-a-graphql-wrapper-around-the-universal-chess-interface-1c5bb1acd821), I gave arguments for why GraphQL might be used to wrap UCI. Perhaps the easiest way to do this is to use GraphQL’s subscription service. This will send events back to the client via a web socket. Commands are sent via Queries or Mutations, and the responses come back as subscribed-to events.

In the case of UCI interaction, mutations would be used to ensure that commands are executed in the expected sequence. Before executing a command, you would first set up a subscription to receive the response. By using GraphQL, subscription responses are type-safe, much like return values of a Query or Mutation request.

The client calls GraphQL Mutations to send requests via HTTP, then receives responses (if any) via web socket. Though simple to implement on the server, **a socket-based interface is awkward for the client** because it is multi-stepped:

1. subscribe to the expected response event
2. send a command via HTTP
3. receive an HTTP response (an acknowledgment that the request was received, not the actual result)
4. await the real response to arrive via the web socket.
5. act on the response

#### Simplifying the client-server interaction

Let’s categorize the types of responses UCI sends:

1. single line response
2. no response
3. multi-line, multi-value response, with terminator

_(Aside: It is possible to start analysis without a definite time limit (“infinite **go**”). This would fall under category 2 because analysis will arrive at a best move termination point, either by exhaustion or by the **stop** command.)_

**Category 1** is simple call and response, and these can be handled as plain old GraphQL HTTP requests. No need to subscribe for a response: the resolver can just return it when it arrives.

**Category 2** receives no response from the engine, but a response is required by HTTP. All that is needed in this case is to acknowledge the request.

**Category 3** has two subtypes: requests with multi-line but fixed responses (e.g. **option**), and requests with streaming, intermediate responses (**go**). The former can again be handled through HTTP because the response will be predictable and timely. The latter has a varying (possibly long) completion time, and may be sending a series of intermediate responses of interest to the client, which it would like to receive in real time**_._** Since we can’t send back multiple responses to an HTTP request, this latter case cannot be handled by HTTP alone, so the subscription interface as described above is still appropriate.

Despite UCI being a streaming interface, it turns out that for most cases, an HTTP response/request can be used for interaction via GraphQL.

### Conclusions

1. The GraphQL schema should consist of Mutations because UCI is stateful and commands must execute in sequence
2. For Category 1 & 2 commands, HTTP request/response is simplest. There is still streaming going on in the back end, but GraphQL resolvers will instantiate a UCI stream listener specific to the expected UCI command response before sending the command to the engine. That listener will resolve the GraphQL request via HTTP when the response arrives from the engine. This makes lighter work for the client.
3. The server will also track UCI state to ensure that commands are executed in the proper context. If the client tries to execute a command before the engine can handle it, an HTTP status error will be returned
4. For those cases where there is no expected response from UCI, the GraphQL resolver will just acknowledge the command was received.
5. The determinate case for Category 3 (where there’s a sure and quick response) can be handled by HTTP.
6. The indeterminate case, where there are intermediate responses before termination, can be handled via web socket. This, in turn, can be wrapped in a GraphpQL subscription service.

The [mock implementation](https://github.com/JeffML/chessQ/tree/chessQ-mock) pretty much covered the essentials, but this short analysis provides a blueprint for going forward with an implementation.

_Code for this article can be found [here](https://github.com/JeffML/query_async)._

