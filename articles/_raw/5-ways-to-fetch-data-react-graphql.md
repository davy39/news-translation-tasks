---
title: How to Fetch Data in React from a GraphQL API
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-05-03T17:20:56.000Z'
originalURL: https://freecodecamp.org/news/5-ways-to-fetch-data-react-graphql
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/5-ways-to-fetch-data-in-react-with-graphql-2.png
tags:
- name: apollo client
  slug: apollo-client
- name: axios
  slug: axios
- name: GraphQL
  slug: graphql
- name: React
  slug: react
seo_title: null
seo_desc: 'Let''s go through the five best ways that you can fetch data with React
  from a GraphQL API.

  While there are a couple of popular libraries which are made to interact with GraphQL
  APIs from a React application, there are many different ways to fetch dat...'
---

Let's go through the five best ways that you can fetch data with React from a GraphQL API.

While there are a couple of popular libraries which are made to interact with GraphQL APIs from a React application, there are many different ways to fetch data with GraphQL.

I've included code samples that show you how to fetch or "query" data in the shortest code possible and how to get up and running with each of these different methods of connecting React with GraphQL. 

## Getting Started

In these examples, we'll be using the SpaceX GraphQL API to fetch and display the past 10 missions that SpaceX has made. 

Feel free to use the code below if you are attempting to connect your React app with a GraphQL API. In these examples, we're going to go from the most advanced GraphQL client library for React to the simplest approach to querying a GraphQL endpoint. 

## 1. Apollo Client

The most popular and comprehensive GraphQL library is Apollo Client. 

Not only can you use it to fetch remote data with GraphQL, which we're doing here, but it allows us to manage data locally, both through an internal cache as well as an entire state management API. 

To get started with Apollo Client, you need to install both the main Apollo Client dependency, as well as GraphQL:

```bash
npm install @apollo/client graphql
```

The idea behind the Apollo Client is that it will be used across your entire application. To do this, you'll use a special Apollo Provider component to pass a created Apollo client down your entire component tree.

When you create your Apollo Client, you need to specify a `uri` value, namely a GraphQL endpoint. Additionally, you need to specify a cache. 

Apollo Client comes with its own in memory cache, which is used to cache or locally store and manage your queries and their related data:

```js
import React from "react";
import ReactDOM from "react-dom";
import { ApolloProvider, ApolloClient, InMemoryCache } from "@apollo/client";

import App from "./App";

const client = new ApolloClient({
  uri: "https://api.spacex.land/graphql/",
  cache: new InMemoryCache()
});

const rootElement = document.getElementById("root");
ReactDOM.render(
  <ApolloProvider client={client}>
    <App />
  </ApolloProvider>,
  rootElement
);
```

Once you've set up the Provider and client within your App component, you can use all of the different React hooks that Apollo Client gives you for all the different GraphQL operations. These include queries, mutations, and subscriptions. You can even use the created Apollo Client directly using a custom hook called `useApolloClient`. 

Since you're just querying data here, you will use the `useQuery` hook. 

You will include a GraphQL query as its first argument to write your query. You'll use the function `gql`, which does a number of things, such as giving you editor syntax highlighting and the auto formatting functionality if you use the tool Prettier for your project. 

Once you execute this query, you get back the values `data`, `loading`, and `error`:

```js
import React from "react";
import { useQuery, gql } from "@apollo/client";

const FILMS_QUERY = gql`
  {
    launchesPast(limit: 10) {
      id
      mission_name
    }
  }
`;

export default function App() {
  const { data, loading, error } = useQuery(FILMS_QUERY);

  if (loading) return "Loading...";
  if (error) return <pre>{error.message}</pre>

  return (
    <div>
      <h1>SpaceX Launches</h1>
      <ul>
        {data.launchesPast.map((launch) => (
          <li key={launch.id}>{launch.mission_name}</li>
        ))}
      </ul>
    </div>
  );
}
```

 Before you display your data, your missions, you want to handle the loading state. When you are in a loading state, you are fetching the query from a remote endpoint. 

You also want to handle any errors that occur. You can simulate an error by making a syntax error in your query, such as querying for a field that doesn't exist. To handle that error, you can conveniently return and display a message from `error.message`.

## 2. Urql

Another fully-featured library that connects React apps with GraphQL APIs is urql.

It attempts to give you many of the features and syntax Apollo has while being a little bit smaller in size and requiring less setup code. It gives you caching capabilities if you choose, but it does not include an integrated state management library like Apollo does.

To use urql as your GraphQL client library, you'll need to install the packages urql and GraphQL. 

```bash
npm install urql graphql
```

Just like Apollo, you'll want to use the dedicated Provider component, and create a client with your GraphQL endpoint. Note that you do not need to specify a cache out of the box.

```js
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import { createClient, Provider } from 'urql';

const client = createClient({
  url: 'https://api.spacex.land/graphql/',
});

const rootElement = document.getElementById("root");
ReactDOM.render(
  <Provider value={client}>
    <App />
  </Provider>,
  rootElement
);
```

Very similar to Apollo, urql gives you custom hooks that handle all the standard GraphQL operations, and therefore have similar names.

Again, you can use the `useQuery` hook from the urql package. Although instead of needing the function `gql`, you can drop it and just use a template literal to write your query. 

When calling `useQuery`, you get back an array which you can destructure as an array instead of as an object. The first element in this array is an object, called `result`, which gives you a number of properties that you can destructure: `data`, `fetching`, and `error`.

```js
import React from "react";
import { useQuery } from 'urql';

const FILMS_QUERY = `
  {
    launchesPast(limit: 10) {
      id
      mission_name
    }
  }
`;

export default function App() {
  const [result] = useQuery({
    query: FILMS_QUERY,
  });

  const { data, fetching, error } = result;

  if (fetching) return "Loading...";
  if (error) return <pre>{error.message}</pre>

  return (
    <div>
      <h1>SpaceX Launches</h1>
      <ul>
        {data.launchesPast.map((launch) => (
          <li key={launch.id}>{launch.mission_name}</li>
        ))}
      </ul>
    </div>
  );
}
```

In an identical fashion to displaying the data that you fetch with Apollo, you can handle both your error and loading states while you're fetching your remote data.

## 3. React Query + GraphQL Request

It's important to note at this point that you don't need a sophisticated, heavyweight GraphQL client library like urql or Apollo to interact with your GraphQL API, as we will see later. 

Libraries like Apollo and urql were created not only to help you perform all the standard GraphQL operations, but to better manage the server state in your React client through a number of additional tools. All this along with the fact that they come with custom hooks that make managing repetitive tasks like handling loading, error, and other related states simple. 

With that in mind, let's take a look at how you can use a very pared-down GraphQL library for your data fetching and combine that with a better means of managing and caching that server state that you're bringing into your application. You can fetch data very simply with the help of the package `graphql-request`. 

GraphQL Request is a library that doesn't require you to set up a client or a Provider component. It is essentially a function that just accepts an endpoint and a query. Very similar to an HTTP client, you just have to pass in those two values and you get back your data. 

Now if you want to manage that state across your app, you can use a great library normally used for interacting with Rest APIs – but it's equally helpful for GraphQL APIs – and that is React Query. It gives you some very similarly named React Hooks, `useQuery` and `useMutation`, that perform identical tasks to what the Apollo and urql hooks perform. 

React Query also gives you a bunch of tools for managing state, along with an integrated Dev Tools component that allows you to see what's being stored in React Query's built-in cache. 

> By pairing your very basic GraphQL client, GraphQL request, with React Query you get all the power of a library like urql or Apollo. 

To get started with this pairing, you just need to install React Query and GraphQL Request: 

```bash
npm install react-query graphql-request
```

You use React Query's Provider component and create a query client where you can set some default data fetching settings if you like. Then within your app component itself, or any child components of `App`, you can use the `useQuery` hook. 

```js
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import { QueryClient, QueryClientProvider } from "react-query";

const client = new QueryClient();

const rootElement = document.getElementById("root");
ReactDOM.render(
  <QueryClientProvider client={client}>
    <App />
  </QueryClientProvider>,
  rootElement
);
```

To store the result of your operation in the React Query cache, you just need to give it a key value as the first argument to serve as an identifier. This allows you to very easily reference and pull data from the cache, as well as to refetch or invalidate a given query to fetch updated data.

Since you're fetching launch data, let's call this query "launches". 

Once again, this hook will return the result of making that request. For the second argument to `useQuery`, you need to specify how to fetch that data and React Query will take care of resolving the promise that GraphQL request returns. 

```js
import React from "react";
import { request, gql } from "graphql-request";
import { useQuery } from "react-query";

const endpoint = "https://api.spacex.land/graphql/";
const FILMS_QUERY = gql`
  {
    launchesPast(limit: 10) {
      id
      mission_name
    }
  }
`;

export default function App() {
  const { data, isLoading, error } = useQuery("launches", () => {
    return request(endpoint, FILMS_QUERY);
  });

  if (isLoading) return "Loading...";
  if (error) return <pre>{error.message}</pre>;

  return (
    <div>
      <h1>SpaceX Launches</h1>
      <ul>
        {data.launchesPast.map((launch) => (
          <li key={launch.id}>{launch.mission_name}</li>
        ))}
      </ul>
    </div>
  );
}
```

Similar to Apollo, you get back an object that you can destructure to get the values for the data, as well as whether or not you're in the loading state, and the error state.

## 4. React Query + Axios

You can use even simpler HTTP client libraries that have no relationship to GraphQL to fetch your data. 

In this case, you can use the popular library axios. Once again you can pair it with React Query to get all the special hooks and state management.

```bash
npm install react-query axios
```

Using an HTTP client like Axios to perform a query from a GraphQL API requires performing a POST request to your API endpoint. For the data that you send along in the request, you will provide an object with a property called `query`, which will be set to your films query. 

With axios, you're going to need to include a little bit more information about how to resolve this promise and get back your data. You need to tell React Query where the data is so it can be put on the `data` property that `useQuery` returns.

In particular, you get the data back on the data property of `response.data`:

```js
import React from "react";
import axios from "axios";
import { useQuery } from "react-query";

const endpoint = "https://api.spacex.land/graphql/";
const FILMS_QUERY = `
  {
    launchesPast(limit: 10) {
      id
      mission_name
    }
  }
`;

export default function App() {
  const { data, isLoading, error } = useQuery("launches", () => {
    return axios({
      url: endpoint,
      method: "POST",
      data: {
        query: FILMS_QUERY
      }
    }).then(response => response.data.data);
  });

  if (isLoading) return "Loading...";
  if (error) return <pre>{error.message}</pre>;

  return (
    <div>
      <h1>SpaceX Launches</h1>
      <ul>
        {data.launchesPast.map((launch) => (
          <li key={launch.id}>{launch.mission_name}</li>
        ))}
      </ul>
    </div>
  );
}
```

## 5. React Query + Fetch API

The easiest way of all these different approaches to fetch data is to just use React query plus the fetch API. 

Since the fetch API is included in all modern browsers, you do not need to install a third-party library – you only need to install `react-query` within your application. 

```bash
npm install react-query
```

Once you have the React Query client provided to the entire app, you can just swap out your axios code with fetch. 

What's a little bit different is that you need to specify a header that includes the content type of the data that you want back from your request. In this case, it is JSON data. 

You also need to stringify the object that you're sending as your payload with a query property that is set to your films query:

```js
import React from "react";
import axios from "axios";
import { useQuery } from "react-query";

const endpoint = "https://api.spacex.land/graphql/";
const FILMS_QUERY = `
  {
    launchesPast(limit: 10) {
      id
      mission_name
    }
  }
`;

export default function App() {
  const { data, isLoading, error } = useQuery("launches", () => {
    return fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: FILMS_QUERY })
    })
      .then((response) => {
        if (response.status >= 400) {
          throw new Error("Error fetching data");
        } else {
          return response.json();
        }
      })
      .then((data) => data.data);
  });

  if (isLoading) return "Loading...";
  if (error) return <pre>{error.message}</pre>;

  return (
    <div>
      <h1>SpaceX Launches</h1>
      <ul>
        {data.launchesPast.map((launch) => (
          <li key={launch.id}>{launch.mission_name}</li>
        ))}
      </ul>
    </div>
  );
}
```

One benefit of using axios over fetch is that it automatically handles errors for you. With fetch, as you can see in the code above, you need to check for a certain status code, in particular a status code above 400. 

This means that your request resolves to an error. If that's the case, you need to manually throw an error, which will be caught by your `useQuery` hook. Otherwise, if it's a 200 or 300 range response, meaning the request was successful, simply return the JSON data and display it.

## Conclusion

This article was dedicated to showing you a number of different approaches to effectively fetching data from a GraphQL API with React.  

From these options, hopefully you can evaluate which is most appropriate for you and your applications. And now you have some helpful code that will enable you to start using these tools and libraries much faster.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*


