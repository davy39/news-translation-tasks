---
title: How to use React hooks with the GraphQL API to manage state
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2019-11-04T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/hooks-and-graphql
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9fa3740569d1a4ca43bf.jpg
tags:
- name: GraphQL
  slug: graphql
- name: react hooks
  slug: react-hooks
- name: React
  slug: reactjs
- name: 'State Management '
  slug: state-management
seo_title: null
seo_desc: 'In this blog post, we are going to learn -


  What React hooks are

  How to use hooks for state management


  Before we start working with hooks, let us take a brief moment to talk about state
  management.

  State management is managing data that flows betwee...'
---

In this blog post, we are going to learn -

1. What React hooks are
2. How to use hooks for state management

Before we start working with hooks, let us take a brief moment to talk about state management.

**State management** is managing data that flows between our application components. It could be data flowing inside one component (local state) or data flowing between multiple components (shared state). We need to manage state because sometimes components need to talk to each other through a reliable source of information. In Redux, this reliable source of information is called the store.

## Part 1: React hooks - the what and why

### What are hooks?

Hooks are functions that lets you access state without using a class component. Hooks are a more natural way of thinking about React. Instead of thinking of what lifecycle methods to use, you can now write components thinking about how and when your data needs to be used.

React hooks were introduced in October 2018 and released in February 2019. It is now available with React 16.8 and higher. React hooks became highly popular as soon as they were introduced.

### Why are React hooks so popular?

1. No boilerplate: To use hooks, you don't need to import any new libraries or write any boilerplate code. You can simply start using hooks out of the box in React 16.8 and up. 
2. No need to use class components to use state: Traditionally, if you were using a functional component and decided that this component needs React state, you would have to convert it into a React class component. With the addition of hooks, you can use React state inside a functional component.
3. More logical way of thinking of React: You no longer have to think about when React mounts a component and what you should do in `componentDidMount` and remember to clean it up in `componentWillUnmount`. Now you can think more directly about how data is consumed by your component. React takes care of handling the mounting and cleanup functions for you. 

### What are some common hooks?

#### 1. useState

useState is used to set and update state like `this.state` in a class component.

```javascript
const [ state, setState] = useState(initialState); 

```

#### 2. useEffect

useEffect is used to carry out a function that does side effects. Side effects could include things like DOM manipulation, subscriptions, and API calls.

```javascript
useEffect(() => {
  document.title = 'New Title' 
});


```

#### 3. useReducer

useReducer works similar to how a reducer works in Redux. useReducer is used when state is more complex. You can actually use useReducer for everything you do with useState. It gives a dispatch function in addition to a state variable. 

```javascript
const [ state, dispatch ] = useReducer(reducer, initialArg, init);

```

#### 4. useContext

useContext is similar to the context API. In the context API, there is a Provider method and Consumer method. Similarly, with useContext, the closest Provider method is used to read data.

```javascript
const value = useContext(MyContext);

```

For more detailed explanation of how each of these work, read [the official docs](https://reactjs.org/docs/hooks-reference.html#usestate).

## Part 2: How to use hooks for state management

With React 16.8, you can use hooks out of the box.

We are going to build an application to make a list of songs. Here is what it will do -

1. Fetch a GraphQL API for a list of a songs and render it on the UI.
2. Have the ability to add a song to the list.
3. When the song gets added to the list, update the list on the frontend and store data on the backend.

By the way, all the code is available on [my GitHub](https://github.com/shrutikapoor08/hooks-graphql). To see this in action, you can go to [this CodeSandbox](https://codesandbox.io/embed/github/shrutikapoor08/hooks-graphql/tree/master/). 

We are going to use the GraphQL API with this app, but you can do the following steps with a REST API as well. 

### Step 0: Main gist

The main idea here is that we are going to use `context` to pass data down to our components. We will be using hooks, `useContext` and `useReducer`, to read and update this state. We will be using `useState` to store any local state. For doing side effects such as calling an API, we are going to use `useEffect`. 

Let's get started! 

###  Step 1: Set up context

```javascript
import { createContext } from 'react';

const Context = createContext({
  songs: []
});

export default Context
```

### Step 2: Initialize your state. Call this initialState

We are going to use this context from to initialize our state:

```javascript
 const initialState = useContext(Context);   

```

### Step 3: Setup reducers using useReducer

Now we are going to set up reducers with an initialState with `useReducer` in App.js:

```javascript
   const [ state, dispatch ] = useReducer(reducer, initialState);

```

### Step 4: Figure out which is the top level component.

We will need to set up a Context Provider here. For our example, it will be `App.js`. Also, pass in the dispatch returned from useReducer here so that children can have access to dispatch:

```javascript
  <Context.Provider value={state,dispatch}>
    // children components
      <App />
  <Context.Provider value={state,dispatch}>

```

### Step 5: Now hook up the APIs using the useEffect hook

```javascript
  const {state, dispatch} = useContext(Context);

  useEffect(() => {
      if(songs) {
          dispatch({type: "ADD_CONTENT", payload: songs});
      }
  }, [songs]);

```

### Step 6: Update state

You can use `useContext` and `useReducer` to receive and update global application state. For local state like form components, you can use `useState`.

```javascript
  const [artist, setArtist] = useState("");
  
  const [lyrics, setLyrics] = useState("");

```

And that's it! State management is now set up.

Did you learn anything new? Have something to share? Tweet me on Twitter.

%[https://twitter.com/shrutikapoor08/status/1189975126705504256?s=20]


