---
title: 'Apollo GraphQL: How to Build a Full-stack App with React and Node Js'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-29T17:03:39.000Z'
originalURL: https://freecodecamp.org/news/apollo-graphql-how-to-build-a-full-stack-app-with-react-and-node-js
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/cover-3.png
tags:
- name: Apollo GraphQL
  slug: apollo
- name: GraphQL
  slug: graphql
- name: node
  slug: node
- name: React
  slug: react
seo_title: null
seo_desc: 'By Ibrahima Ndaw

  Apollo Client is a complete state management library for JavaScript apps. It''s
  a powerful tool since it can be used on both the back end and front end side.

  In this tutorial, we will use it on the front end and back end by building a...'
---

By Ibrahima Ndaw

Apollo Client is a complete state management library for JavaScript apps. It's a powerful tool since it can be used on both the back end and front end side.

In this tutorial, we will use it on the front end and back end by building an Apollo GraphQL Server with Node JS. Then we will consume the data on the client-side using React JS.

If you're new to GraphQl, [this tutorial](https://www.ibrahima-ndaw.com/blog/graphql-api-express-mongodb/) might help you. Otherwise, let's get started.

* [Building the server with Apollo, Node, and GraphQl](#heading-building-the-server-with-apollo-node-and-graphql)
* [GraphQl Schema](#heading-graphql-schema)
* [GraphQl resolvers](#heading-graphql-resolvers)
* [Creating the Apollo Server](#heading-creating-the-apollo-server)
* [Building the Client-side with React](#heading-building-the-client-side-with-react)
* [Connecting React to Apollo](#heading-connecting-react-to-apollo)
* [Fetching the data](#heading-fetching-the-data)
* [Showing the data](#heading-showing-the-data)

## Building the server with Apollo, Node, and GraphQl

In this guide, I will use the Github API to have data to show, and that operation will be done by the GraphQl server built with Apollo and Node JS.

To make this happen, we need to run the following command on the terminal to set up a new Node JS project:

```shell
  yarn init

```

Once the set up is done, we can now install the necessary packages by running this command:

```shell
  yarn add apollo-server graphql axios

```

Great, we now have all we need to build a server. So first let's create a new file `app.js` in the root which will be the entry point of our server.

Next, we need to define a Graphql schema that mirrors the way our data should look.

### GraphQl Schema

A schema describes the shape of your data graph. It defines a set of types with fields that are populated from your back-end data stores. So, let's add a new schema in the `app.js` file.

* `app.js`

```js
const { ApolloServer, gql } = require("apollo-server")
const axios = require("axios")

const typeDefs = gql`
  type User {
    id: ID
    login: String
    avatar_url: String
  }

  type Query {
    users: [User]
  }
`

```

As you can see we don't use all data provided by the Github API. We just need the id that will be used as a reference key on the React App, the login, and the avatar_url. We also have a query `users` that returns an array of users.

Now that we have a GraphQL schema, it's time to build the corresponding resolvers to complete the query operation.

### GraphQl resolvers

A resolver is a collection of functions that helps generate a response from a GraphQL query. So, let's add a new resolver in the `app.js` file.

* `app.js`

```js
const resolvers = {
  Query: {
    users: async () => {
      try {
        const users = await axios.get("https://api.github.com/users")
        return users.data.map(({ id, login, avatar_url }) => ({
          id,
          login,
          avatar_url,
        }))
      } catch (error) {
        throw error
      }
    },
  },
}

```

A resolver has to match the appropriate schema by name. Therefore, here `users` refers to the `users` query defined in our schema. It's a function that fetches the data from the API with the help of `axios` and returns as expected the id, the login, and the avatar_url.

And that operation can take time to complete. That's why async/await is used here to handle it.

With that, we can now create the Apollo Server in the next section.

### Creating the Apollo Server

If you remember, in the `app.js` file, we had imported `ApolloServer` from the `apollo-server` package. It's a constructor that receives an object as an argument. And that object must contain the schema and the resolver to be able to create the server.

So, let's tweak `app.js` a bit with `ApolloServer`.

* `app.js`

```js
const server = new ApolloServer({
  typeDefs,
  resolvers,
})
//  typeDefs: typeDefs,
//  resolvers: resolvers
server.listen().then(({ url }) => console.log(`Server ready at ${url}`))

```

Here, we pass as a parameter an object that holds the schema and the resolver to `ApolloServer` to create the server and then listens to it. With that in place, we now have a functional server to work with.

You can already play with it and send queries with the help of GraphQL playground by running this command:

```shell
  yarn start

```

You can now preview it on `http://localhost:400`

* The complete `app.js` file

```js
const { ApolloServer, gql } = require("apollo-server")
const axios = require("axios")

const typeDefs = gql`
  type User {
    id: ID
    login: String
    avatar_url: String
  }

  type Query {
    users: [User]
  }
`

const resolvers = {
  Query: {
    users: async () => {
      try {
        const users = await axios.get("https://api.github.com/users")
        return users.data.map(({ id, login, avatar_url }) => ({
          id,
          login,
          avatar_url,
        }))
      } catch (error) {
        throw error
      }
    },
  },
}

const server = new ApolloServer({
  typeDefs,
  resolvers,
})

server.listen().then(({ url }) => console.log(`Server ready at ${url}`))

```

A server alone does not do much. We need to add a start script in the `package.json` file to, as you guessed, start the server.

* `package.json`

```js
  // first add nodemon: yarn add nodemon --dev
  "scripts": {
    "start": "nodemon src/index.js"
  }

```

With that, we have a server to fetch data from the Github API. So now it's time to move to the client-side and consume the data.

_Let's do it._

![yaay](https://media.giphy.com/media/huJxyJPiPk1jwQWPAN/source.gif)

## Building the Client-side with React

The first thing we have to do is create a fresh React App by running the following command in the terminal:

```shell
npx create-react-app client-react-apollo

```

Next, we need to install the Apollo and GraphQl packages:

```shell
  yarn add apollo-boost @apollo/react-hooks graphql

```

Now, we can connect Apollo with our React App by updating the `index.js` file.

### Connecting React to Apollo

* `index.js`

```shell
import React from 'react';
import ReactDOM from 'react-dom';
import ApolloClient from 'apollo-boost'
import { ApolloProvider } from '@apollo/react-hooks';

import App from './App';
import './index.css';
import * as serviceWorker from './serviceWorker';

const client = new ApolloClient({
  uri: 'https://7sgx4.sse.codesandbox.io'
})


ReactDOM.render(
  <React.StrictMode>
    <ApolloProvider client={client}>
      <App />
    </ApolloProvider>
  </React.StrictMode>,
  document.getElementById('root')
);

serviceWorker.unregister();

```

As you can see, we start by importing `ApolloClient` and `ApolloProvider`. The first helps us inform Apollo about which URL to use when fetching data. And if no `uri` is passed to `ApolloClient`, it will take the current domain name plus `/graphql`.

The second is the Provider which expects to receive the client object to be able to connect Apollo to React.

That said, we can now create a component that shows the data.

### Fetching the data

* `App.js`

```jsx
import React from "react"
import { useQuery } from "@apollo/react-hooks"
import gql from "graphql-tag"
import "./App.css"

const GET_USERS = gql`
  {
    users {
      id
      login
      avatar_url
    }
  }
`

```

Here, we have a simple GraphQL query that fetches the data. That query will be passed later to `useQuery` to tell Apollo which data to fetch.

* `App.js`

```jsx
const User = ({ user: { login, avatar_url } }) => (
  <div className="Card">
    <div>
      <img alt="avatar" className="Card--avatar" src={avatar_url} />
      <h1 className="Card--name">{login}</h1>
    </div>
    <a href={`https://github.com/${login}`} className="Card--link">
      See profile
    </a>
  </div>
)

```

This presentational component will be used to display a user. It receives the data from the App component and displays it.

### Showing the data

* `App.js`

```jsx
function App() {
  const { loading, error, data } = useQuery(GET_USERS)

  if (error) return <h1>Something went wrong!</h1>
  if (loading) return <h1>Loading...</h1>

  return (
    <main className="App">
      <h1>Github | Users</h1>
      {data.users.map(user => (
        <User key={user.id} user={user} />
      ))}
    </main>
  )
}

export default App

```

The `useQuery` hook provided by Apollo receives the GraphQL query and returns three states: the loading, the error, and the data.

If the data are successfully fetched, we pass it to the User component. Otherwise we throw an error.

* The complete `App.js` file

```jsx
import React from "react"
import { useQuery } from "@apollo/react-hooks"
import gql from "graphql-tag"
import "./App.css"

const GET_USERS = gql`
  {
    users {
      id
      login
      avatar_url
    }
  }
`

const User = ({ user: { login, avatar_url } }) => (
  <div className="Card">
    <div>
      <img alt="avatar" className="Card--avatar" src={avatar_url} />
      <h1 className="Card--name">{login}</h1>
    </div>
    <a href={`https://github.com/${login}`} className="Card--link">
      See profile
    </a>
  </div>
)

function App() {
  const { loading, error, data } = useQuery(GET_USERS)

  if (error) return <h1>Something went wrong!</h1>
  if (loading) return <h1>Loading...</h1>

  return (
    <main className="App">
      <h1>Github | Users</h1>
      {data.users.map(user => (
        <User key={user.id} user={user} />
      ))}
    </main>
  )
}

export default App

```

Great! With that, we are now done building a full-stack Apollo GraphQL app using React and Node JS.

Preview the Apollo GraphQL Server [here](https://codesandbox.io/s/node-apollo-graphql-7sgx4?file=/package.json:139-193)

Preview the React App [here](https://codesandbox.io/s/react-apollo-graphql-1qu75)

Find the source code [here](https://github.com/ibrahima92/apollo-graphql-full-stack)

You can find other great content like this on [my blog](https://www.ibrahima-ndaw.com/blog/apollo-graphql-fullstack-app-with-react-and-nodejs/)

Thanks for reading!

![congrats](https://media.giphy.com/media/OcZp0maz6ALok/source.gif)

