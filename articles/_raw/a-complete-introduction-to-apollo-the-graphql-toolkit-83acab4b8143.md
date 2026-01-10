---
title: A complete introduction to Apollo, the GraphQL toolkit
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-03-24T10:57:58.000Z'
originalURL: https://freecodecamp.org/news/a-complete-introduction-to-apollo-the-graphql-toolkit-83acab4b8143
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3crww-zqngVHMJ-3xhnq5w.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  Introduction to Apollo

  In the last few years, GraphQL has gotten hugely popular as an alternative approach
  to building an API over REST.

  GraphQL is a great way to let the client decid...'
---

> Interested in learning JavaScript? Get my ebook at [jshandbook.com](https://jshandbook.com/)

### Introduction to Apollo

In the last few years, [GraphQL](https://flaviocopes.com/graphql/) has gotten hugely popular as an alternative approach to building an API over REST.

GraphQL is a great way to let the client decide which data they want to be transmitted over the network, rather than having the server send a fixed set of data.

Also, it allows you to specify nested resources, reducing the back and forth sometimes required when dealing with REST APIs.

Apollo is a team and community that builds on top of GraphQL, and provides different tools that help you build your projects.

![Image](https://cdn-media-1.freecodecamp.org/images/cZlluTAwxSbZXNG6wNJXed2IjdlURME1gg0r)
_Apollo Logo courtesy of apollographql.com_

The tools provided by Apollo are mainly three: **Client**, **Server**, **Engine**.

**Apollo Client** helps you consume a GraphQL API, with support for the most popular frontend web technologies like React, Vue, Angular, Ember, and Meteor. It also supports native development on iOS and Android.

**Apollo Server** is the server part of GraphQL, which interfaces with your backend and sends responses back to the client requests.

**Apollo Engine** is a hosted infrastructure (SaaS) that serves as a middle man between the client and your server, providing caching, performance reporting, load measurement, error tracking, schema field usage statistics, historical stats and many more goodies. It’s currently free up to 1 million requests per month, and it’s the only part of Apollo that’s not open source and free. It provides funding for the open source part of the project.

It’s worth noting that those three tools are not linked together in any way, and you can use just Apollo Client to interface with a 3rd part API, or serve an API using Apollo Server without having a client at all, for example.

#### Some benefits of using Apollo

It’s all **compatible with the GraphQL standard specification**, so there is no proprietary or incompatible tech in Apollo.

But it’s very convenient to have all those tools together under a single roof as a complete suite for all your GraphQL-related needs.

Apollo strives to be easy to use and easy to contribute to.

Apollo Client and Apollo Server are all community projects, built by the community, for the community. Apollo is backed by the [Meteor Development Group](https://www.meteor.io/) (the company behind [Meteor](https://flaviocopes.com/meteor-hello-world/)), a very popular JavaScript framework.

Apollo is focused on **keeping things simple**. This is something key to the success of a technology that wants to become popular. Much of the tech or frameworks or libraries out there might be overkill for 99% of small or medium companies, and is really suited for the big companies with very complex needs.

### Apollo Client

[Apollo Client](https://www.apollographql.com/client) is the leading JavaScript client for GraphQL. Since it’s community-driven, it’s designed to let you build UI components that interface with GraphQL data — either in displaying that data, or in performing mutations when certain actions happen.

You don’t need to change everything in your application to make use of Apollo Client. You can start with just one tiny layer and one request, and expand from there.

Most of all, Apollo Client is built to be simple, small, and flexible from the ground up.

In this post I’m going to detail the process of using Apollo Client within a React application.

I’ll use the [GitHub GraphQL API](https://developer.github.com/v4/) as a server.

### Start a React app

I use `[create-react-app](https://github.com/facebook/create-react-app)` to setup the React app, which is very convenient and just adds the bare bones of what we need:

```
npx create-react-app myapp
```

> `_npx_` _is a command available in the latest npm versions. Update npm if you do not have this command._

Start the app local server with

```
yarn start
```

Open `src/index.js`:

```
import React from 'react'import ReactDOM from 'react-dom'import './index.css'import App from './App'import registerServiceWorker from './registerServiceWorker'ReactDOM.render(<App />, document.getElementById('root'))registerServiceWorker()
```

and remove all this content.

### Get started with Apollo Boost

Apollo Boost is the easiest way to start using Apollo Client on a new project. We’ll install that in addition to `react-apollo` and `graphql`.

In the console, run

```
yarn add apollo-boost react-apollo graphql
```

or with npm:

```
npm install apollo-boost react-apollo graphql --save
```

### Create an ApolloClient object

You start by importing ApolloClient from `apollo-client` in `index.js`:

```
import { ApolloClient } from 'apollo-client'const client = new ApolloClient()
```

By default Apollo Client uses the `/graphql` endpoint on the current host, so let’s use an **Apollo Link** to specify the details of the connection to the GraphQL server by setting the GraphQL endpoint URI.

### Apollo Links

An Apollo Link is represented by an `HttpLink` object, which we import from `apollo-link-http`.

Apollo Link provides us a way to describe how we want to get the result of a GraphQL operation, and what we want to do with the response.

In short, you create multiple Apollo Link instances that all act on a GraphQL request one after another, providing the final result you want. Some Links can give you the option of retrying a request if not successful, batching, and much more.

We’ll add an Apollo Link to our Apollo Client instance to use the GitHub GraphQL endpoint URI `[https://api.github.com/graphql](https://api.github.com/graphql)`

```
import { ApolloClient } from 'apollo-client'import { HttpLink } from 'apollo-link-http'const client = new ApolloClient({  link: new HttpLink({ uri: 'https://api.github.com/graphql' })})
```

### Caching

We’re not done yet. Before having a working example we must also tell `ApolloClient` which [caching strategy](https://www.apollographql.com/docs/react/basics/caching.html) to use: `InMemoryCache` is the default and it’s a good one with which to start.

```
import { ApolloClient } from 'apollo-client'import { HttpLink } from 'apollo-link-http'import { InMemoryCache } from 'apollo-cache-inmemory'const client = new ApolloClient({  link: new HttpLink({ uri: 'https://api.github.com/graphql' }),  cache: new InMemoryCache()})
```

### Use `ApolloProvider`

Now we need to connect the Apollo Client to our component tree. We do so using `ApolloProvider`, by wrapping our application component in the main React file:

```
import React from 'react'import ReactDOM from 'react-dom'import { ApolloClient } from 'apollo-client'import { HttpLink } from 'apollo-link-http'import { InMemoryCache } from 'apollo-cache-inmemory'import { ApolloProvider } from 'react-apollo'import App from './App'const client = new ApolloClient({  link: new HttpLink({ uri: 'https://api.github.com/graphql' }),  cache: new InMemoryCache()})ReactDOM.render(  <ApolloProvider client={client}>    <App />  </ApolloProvider>,  document.getElementById('root'))
```

This is enough to render the default `create-react-app` screen, with Apollo Client initialized:

![Image](https://cdn-media-1.freecodecamp.org/images/He9moRbQxqfLHpSuSiBHDMXppwRq2CDhytKz)

### The `gql` template tag

We’re now ready to do something with Apollo Client, and we’re going to fetch some data from the GitHub API and render it.

To do so, we need to import the `gql` template tag:

```
import gql from 'graphql-tag'
```

Any GraphQL query will be built using this template tag, like this:

```
const query = gql`  query {    ...  }`
```

### Perform a GraphQL request

`gql` was the last item we needed in our toolset.

We’re now ready to do something with Apollo Client, and we’re going to fetch some data from the GitHub API and render it.

#### Obtain an access token for the API

The first thing to do is to [obtain a personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) from GitHub.

GitHub makes it easy by providing an interface from which you select any permission you might need:

![Image](https://cdn-media-1.freecodecamp.org/images/cZXXNubCl6sKWtoZRt90VupyIIEptCWfI2OD)

For the sake of this example tutorial, you don’t need any of those permissions. They are meant for access to private user data, but we will just query the public repositories data.

The token you get is an **OAuth 2.0 Bearer token**.

You can easily test it by running from the command line:

```
$ curl -H "Authorization: bearer ***_YOUR_TOKEN_HERE_***" -X POST -d " \ { \   \"query\": \"query { viewer { login }}\" \ } \" https://api.github.com/graphql
```

which should give you the result

```
{"data":{"viewer":{"login":"***_YOUR_LOGIN_NAME_***"}}}
```

or

```
{  "message": "Bad credentials",  "documentation_url": "https://developer.github.com/v4"}
```

if something went wrong.

#### Use an Apollo Link to authenticate

So, we need to send the **Authorization** header along with our GraphQL request, just like we did in the `curl` request above.

We can do this with Apollo Client by creating an Apollo Link middleware. Start with installing `[apollo-link-context](https://www.npmjs.com/package/apollo-link-context)`:

```
npm install apollo-link-context
```

This package allows us to add an authentication mechanism by setting the context of our requests.

We can use it in this code by referencing the `setContext` function in this way:

```
const authLink = setContext((_, { headers }) => {  const token = '***YOUR_TOKEN**'  return {    headers: {      ...headers,      authorization: `Bearer ${token}`    }  }})
```

and once we have this new Apollo Link, we can [compose](https://www.apollographql.com/docs/link/composition.html) it with the `HttpLink` we already had by using the `concat()` method on a link:

```
const link = authLink.concat(httpLink)
```

Here is the full code for the `src/index.js` file with the code we have right now:

```
import React from 'react'import ReactDOM from 'react-dom'import { ApolloClient } from 'apollo-client'import { HttpLink } from 'apollo-link-http'import { InMemoryCache } from 'apollo-cache-inmemory'import { ApolloProvider } from 'react-apollo'import { setContext } from 'apollo-link-context'import gql from 'graphql-tag'import App from './App'const httpLink = new HttpLink({ uri: 'https://api.github.com/graphql' })const authLink = setContext((_, { headers }) => {  const token = '***YOUR_TOKEN**'  return {    headers: {      ...headers,      authorization: `Bearer ${token}`    }  }})const link = authLink.concat(httpLink)const client = new ApolloClient({  link: link,  cache: new InMemoryCache()})ReactDOM.render(  <ApolloProvider client={client}>    <App />  </ApolloProvider>,  document.getElementById('root'))
```

> _WARNING ⚠️ ? Keep in mind that this code is an e**xample** for educational purposes. It exposes your GitHub GraphQL API for the world to see in your frontend-facing code. Production code needs to keep this token private._

We can now make the first GraphQL request at the bottom of this file, and this sample query asks for the names and the owners of the 10 most popular repositories with more than 50k stars:

```
const POPULAR_REPOSITORIES_LIST = gql`{  search(query: "stars:>50000", type: REPOSITORY, first: 10) {    repositoryCount    edges {      node {        ... on Repository {          name          owner {            login          }          stargazers {            totalCount          }        }      }    }  }}`client.query({ query: POPULAR_REPOSITORIES_LIST }).then(console.log)
```

Running this code successfully returns the result of our query in the browser console:

![Image](https://cdn-media-1.freecodecamp.org/images/DPyIddPqoBytsvccGzq1K4n4PPGDaOOuwEtP)

### Render a GraphQL query result set in a component

What we’ve seen up to now is already cool. What’s even cooler is using the GraphQL result set to render your components.

We let Apollo Client have the burden (or joy) or fetching the data and handling all the low-level stuff. This lets us focus on showing the data by using the `graphql` component enhancer offered by `react-apollo`:

```
import React from 'react'import { graphql } from 'react-apollo'import { gql } from 'apollo-boost'const POPULAR_REPOSITORIES_LIST = gql`{  search(query: "stars:>50000", type: REPOSITORY, first: 10) {    repositoryCount    edges {      node {        ... on Repository {          name          owner {            login          }          stargazers {            totalCount          }        }      }    }  }}`const App = graphql(POPULAR_REPOSITORIES_LIST)(props =>  <ul>    {props.data.loading ? '' : props.data.search.edges.map((row, i) =>      <li key={row.node.owner.login + '-' + row.node.name}>        {row.node.owner.login} / {row.node.name}: {' '}        <strong>          {row.node.stargazers.totalCount}        </strong>      </li&gt;    )}  </ul>)export default App
```

Here is the result of our query rendered in the component ?

![Image](https://cdn-media-1.freecodecamp.org/images/bGd9-rLBDlC0LElJiyHIfPFsh206T5OXj3p0)

### Apollo Server

A GraphQL server has the job of accepting incoming requests on an endpoint, interpreting the request and looking up any data that’s necessary to fulfill the client’s needs.

There are tons of different GraphQL server implementations for every possible language.

**Apollo Server is a GraphQL server implementation for JavaScript, in particular for the Node.js platform**.

It supports many popular Node.js frameworks, including:

* [Express](https://expressjs.com/)
* [Hapi](https://hapijs.com/)
* [Koa](http://koajs.com/)
* [Restify](http://restify.com/)

The Apollo Server basically gives us three things:

* A way to describe our data with a **schema**.
* The framework for **resolvers**, which are functions we write to fetch the data needed to fulfill a request.
* It facilitates handling **authentication** for our API.

For the sake of learning the basics of Apollo Server, we’re not going to use any of the supported Node.js frameworks. Instead, we’ll be using something that was built by the Apollo team, something really great which will be the base of our learning: Launchpad.

### Launchpad

[Launchpad](https://launchpad.graphql.com/) is a project that’s part of the Apollo umbrella of products, and it’s a pretty amazing tool that allows us to write code on the cloud and create a an Apollo Server online, just like we’d run a snippet of code on Codepen, JSFiddle or JSBin.

Except that instead of building a visual tool that’s going to be isolated there, and meant just as a showcase or as a learning tool, with Launchpad we create a GraphQL API. It’s going to be publicly accessible.

Every project on Launchpad is called **pad** and has its GraphQL endpoint URL, like:

```
https://1jzxrj129.lp.gql.zone/graphql
```

Once you build a pad, Launchpad gives you the option to download the full code of the Node.js app that’s running it, and you just need to run `npm install` and `npm start` to have a local copy of your Apollo GraphQL Server.

To summarize, it’s a **great tool to learn, share, and prototype**.

### The Apollo Server Hello World

Every time you create a new Launchpad _pad_, you are presented with the Hello, World! of Apollo Server. Let’s dive into it.

First you import the `makeExecutableSchema` function from `graphql-tools`.

```
import { makeExecutableSchema } from 'graphql-tools'
```

This function is used to create a `GraphQLSchema` object, by providing it a schema definition (written in the [GraphQL schema language](http://graphql.org/learn/schema/)) and a set of **resolvers**.

A schema definition is an template literal string containing the description of our query and the types associated with each field:

```
const typeDefs = `  type Query {    hello: String  }`
```

A **resolver** is an object that maps fields in the schema to resolver functions. It’s able to lookup data to respond to a query.

Here is a simple resolver containing the resolver function for the `hello` field, which simply returns the `Hello world!` string:

```
const resolvers = {  Query: {    hello: (root, args, context) => {      return 'Hello world!'    }  }}
```

Given those two elements, the schema definition and the resolver, we use the `makeExecutableSchema` function we imported previously to get a `GraphQLSchema` object, which we assign to the `schema` const.

```
export const schema = makeExecutableSchema({ typeDefs, resolvers })
```

This is **all** you need to serve a simple read-only API. Launchpad takes care of the tiny details.

Here is the full code for the simple Hello World example:

```
import { makeExecutableSchema } from 'graphql-tools'const typeDefs = `  type Query {    hello: String  }`const resolvers = {  Query: {    hello: (root, args, context) => {      return 'Hello world!'    }  }}export const schema = makeExecutableSchema({  typeDefs,  resolvers})
```

Launchpad provides a great built-in tool to consume the API:

![Image](https://cdn-media-1.freecodecamp.org/images/QFNQVQsPIXbZX3leOK84JiPVPV0o228Z-pDh)

And as I said previously, the API is publicly accessible so you just need to login and save your pad.

I made a pad that exposes its endpoint at `https://kqwwkp0pr7.lp.gql.zone/graphql`, so let’s try it using `curl` from the command line:

```
$ curl \  -X POST \  -H "Content-Type: application/json" \  --data '{ "query": "{ hello }" }' \  https://kqwwkp0pr7.lp.gql.zone/graphql
```

which successfully gives us the result we expect:

```
{  "data": {    "hello": "Hello world!"  }}
```

### Run the GraphQL Server locally

We mentioned that anything you create on Launchpad is downloadable, so let’s go on.

The package is composed of two files. The first, `schema.js` is what we have above.

The second, `server.js`, was invisible in Launchpad and that is what provides the underlying Apollo Server functionality, powered by [Express](https://expressjs.com/), the popular Node.js framework.

It is not the simplest example of an Apollo Server setup, so for the sake of explaining, I’m going to replace it with a simpler example (but feel free to study that after you’ve understood the basics).

### Your first Apollo Server code

First, run `npm install` and `npm start` on the Launchpad code you downloaded.

The node server we initialized previusly uses [nodemon](https://nodemon.io/) to restart the server when the files change, so when you change the code, the server is restarted with your changes applied.

Add this code in `server.js`:

```
const express = require('express')const bodyParser = require('body-parser')const { graphqlExpress } = require('apollo-server-express')const { schema } = require('./schema')const server = express()server.use('/graphql', bodyParser.json(), graphqlExpress({ schema }))server.listen(3000, () => {  console.log('GraphQL listening at http://localhost:3000/graphql')})
```

With just 11 lines, this is **much simpler** than the server set up by Launchpad, because we removed all the things that made that code more flexible for their needs.

Coding forces you to make tough decisions: how much flexibility do you need now? How important is it to have clean, understandable code that you can pick up six months from now and easily tweak, or pass to other developers and team members so they can be productive in as little time as needed?

Here’s what the code does:

We first import a few libraries we’re going to use.

* `**express**` which will power the underlying network functionality to expose the endpoint
* `**bodyParser**` is the Node body parsing middleware
* `**graphqlExpress**` is the Apollo Server object for Express

```
const express = require('express')const bodyParser = require('body-parser')const { graphqlExpress } = require('apollo-server-express')
```

Next we import the `GraphQLSchema` object we created in the schema.js file above as `Schema`:

```
const { schema } = require('./schema')
```

Here is some standard Express set, and we just initialize a server on port `3000`

```
const server = express()
```

Now we are ready to initialize Apollo Server:

```
graphqlExpress({ schema })
```

and we pass that as a callback to our endpoint to HTTP JSON requests:

```
server.use('/graphql', bodyParser.json(), graphqlExpress({ schema }))
```

All we need now is to start Express:

```
server.listen(3000, () => {  console.log('GraphQL listening at http://localhost:3000/graphql')})
```

### Add a GraphiQL endpoint

If you use GraphiQL, you can easily add a `/graphiql` endpoint, to consume with the [GraphiQL interactive in-browser IDE](https://github.com/graphql/graphiql):

```
server.use('/graphiql', graphiqlExpress({  endpointURL: '/graphql',  query: ``}))
```

We now just need to start up the Express server:

```
server.listen(PORT, () => {  console.log('GraphQL listening at http://localhost:3000/graphql')  console.log('GraphiQL listening at http://localhost:3000/graphiql')})
```

You can test it by using `curl` again:

```
$ curl \  -X POST \  -H "Content-Type: application/json" \  --data '{ "query": "{ hello }" }' \  http://localhost:3000/graphql
```

This will give you the same result as above, where you called the Launchpad servers:

```
{  "data": {    "hello": "Hello world!"  }}
```

> Interested in learning JavaScript? Get my ebook at [jshandbook.com](https://jshandbook.com/)

