---
title: Build Better React Apps with These Simple Tricks
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-06-16T20:55:03.000Z'
originalURL: https://freecodecamp.org/news/build-better-react-apps-with-these-tricks
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/amazing-react-tricks.png
tags:
- name: React
  slug: react
- name: tips
  slug: tips
- name: Web Applications
  slug: web-applications
seo_title: null
seo_desc: 'Here''s a list of amazing tricks that you can use to improve your React
  applications instantly.

  These tips will not only make your code cleaner and more reliable, but they also
  aim to make your development experience easier and overall more enjoyable....'
---

Here's a list of amazing tricks that you can use to improve your React applications instantly.

These tips will not only make your code cleaner and more reliable, but they also aim to make your development experience easier and overall more enjoyable. 

Give these techniques a try in your React projects today!

## Replace Redux with React Query

As your application gets larger it becomes harder to manage state across your components. So you may reach for a state management library like Redux.

If your application relies on data that you get from an API, you often use Redux to fetch that server state and then update your application state.

This can be a challenging process – not only do you have to fetch data, but you also need to handle the different states, depending on whether you have the data or are in a loading or error state.

Instead of using Redux to manage data you get from a server, **use a library like React Query.**

First of all, React Query gives you greater control over making HTTP requests in your React apps through helpful hooks, along with the ability to easily refetch data. And it also enables you to seamlessly manage state across your app components, often without having to manually update state yourself.

Here's how you set up React Query in your index.js file:

```js
import { QueryClient, QueryClientProvider } from 'react-query'
import ReactDOM from "react-dom";

import App from "./App";

const queryClient = new QueryClient()

const rootElement = document.getElementById("root");
ReactDOM.render(
  <QueryClientProvider client={queryClient}>
    <App />
  </QueryClientProvider>,
  rootElement
);
```

Here, we are setting up a query client which will set up a cache for us to effortlessly manage any requests that we have made in the past. We also set up a query client provider component to pass it down the entire component tree.

### How to make requests with React Query

You can make requests with the useQuery hook, which takes an identifier for your query (in this case, since we are fetching user data, we will call it 'user'), plus a function that is used to fetch that data.

```js
import { useQuery } from "react-query";

export default function App() {
  const { isLoading, isError, data } = useQuery("user", () =>
    fetch("https://randomuser.me/api").then((res) => res.json())
  );

  if (isLoading) return "Loading...";
  if (isError) return "Error!";

  const user = data.results[0];
  return user.email;
}
```

As you can see, React Query takes care of managing these various states that can take place when we fetch our data. We no longer need to manage these states ourselves, we can just destructure them from what is returned from `useQuery`.

Where does the state management part of useQuery come into play?

Now that we have fetched the user data and have it stored in our internal cache, all we need to do to be able to use it across any other component is to call `useQuery()` with the 'user' key that we associated with it:

```js
import { useQuery } from "react-query";

export default function OtherComponent() {
  const { data } = useQuery('user');
    
  console.log(data);
}
```

## Make React Context Easier with a Custom Hook

React Context is a great way to pass data across our component tree. It allows us to pass data into whatever component we like without having to use props. 

To consume context in a React function component, we use the `useContext` hook.

However, there is a slight downside to doing so. In every component that we want to consume data that has been passed down on context, we have to import both the created context object and import React to grab the useContext hook.

Instead of having to write multiple import statements every time we want to read from context, we can simply create a custom React hook.

```js
import React from "react";

const UserContext = React.createContext();

function UserProvider({ children }) {
  const user = { name: "Reed" };
  return <UserContext.Provider value={user}>{children}</UserContext.Provider>;
}

function useUser() {
  const context = React.useContext(UserContext);
  if (context === undefined) {
    throw new Error("useUser in not within UserProvider");
  }
  return context;
}

export default function App() {
  return (
    <UserProvider>
      <Main />
    </UserProvider>
  );
}

function Main() {
  const user = useUser();

  return <h1>{user.name}</h1>; // displays "Reed"
}
```

In this example, we are passing down user data on our custom UserProvider component, which takes a user object and is wrapped around the Main component.

We have a `useUser` hook to more easily consume that context. We only need to import that hook itself to consume our User Context in any component we like, such as our Main component.

## Manage Context Providers in a Custom Component

In almost any React application that you create, you will need a number of Context providers.

We not only need context providers for React Context that we are creating, but also from third party libraries that rely upon it (like React Query) in order to pass their tools down to our to the components that need them.

Once you've started working on your React project for a while, here's what it tends to look like:

```js
ReactDOM.render(
  <Provider3>
    <Provider2>
      <Provider1>
        <App />
      </Provider1>
    </Provider2>
  </Provider3>,
  rootElement
);
```

What can we do about this clutter?

Instead of putting all of our context providers within our App.js file or index.js file, we can create a component called ContextProviders. 

This allows us to use the children prop, then all we have to do is put all these providers into this one component:

```js
src/context/ContextProviders.js

export default function ContextProviders({ children }) {
  return (
    <Provider3>
      <Provider2>
        <Provider1>
          {children}
        </Provider1>
      </Provider2>
    </Provider3>
  );
}
```

Then, wrap the ContextProviders component around App:

```js
src/index.js

import ReactDOM from "react-dom";
import ContextProviders from './context/ContextProviders'
import App from "./App";

const rootElement = document.getElementById("root");
ReactDOM.render(
  <ContextProviders>
    <App />
  </ContextProviders>,
  rootElement
);
```

## Pass props more easily using the object spread operator

When it comes to working with components, we normally pass down data with the help of props. We create a prop name and set it equal to its appropriate value.

However, if we have a lot of props that we need to pass down to a component, do we need to list them all individually?

No, we don't.

A very easy way to be able to pass down all the props that we like without having to write all of the prop names and their corresponding values is to use the `{...props}` pattern. 

This involves putting all of our prop data in an object and spreading all of those props individually to the component we want to pass it to:

```js
export default function App() {
  const data = {
    title: "My awesome app",
    greeting: "Hi!",
    showButton: true
  };

  return <Header {...data} />;
}

function Header(props) {
  return (
    <nav>
      <h1>{props.title}</h1>
      <h2>{props.greeting}</h2>
      {props.showButton && <button>Logout</button>}
    </nav>
  );
}
```

## Map over fragments with React fragment

The `.map()` function in React allows us to take an array and iterate over it, then display each element's data within some JSX. 

However, in some cases, we want to iterate over that data but we do not want to return it within a closing JSX element. Maybe using an enclosing JSX element would modify our applied or we simply don't want to add another element to the DOM. 

A little known tip to be able to iterate over a set of data, and not have the parent element as an HTML element, is to use `React.Fragment`. 

To use the longhand form of React fragments can provide it the `key` prop which is required for any element over which we are iterating.

```js
import React from 'react'

export default function App() {
  const users = [
    {
      id: 1,
      name: "Reed"
    },
    {
      id: 2,
      name: "John"
    },
    {
      id: 3,
      name: "Jane"
    }
  ];

  return users.map((user) => (
    <React.Fragment key={user.id}>{user.name}</React.Fragment>
  ));
}
```

Note that we cannot use the required `key` prop for the shorthand fragment's alternative: `<></>`.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

