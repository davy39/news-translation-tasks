---
title: The React TypeScript Cheatsheet – How To Set Up Types on Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-05T22:27:31.000Z'
originalURL: https://freecodecamp.org/news/react-typescript-how-to-set-up-types-on-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/cover.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Ibrahima Ndaw

  TypeScript lets you type-check your code in order to make it more robust and understandable.

  In this guide, I will show you how to set up TypeScript types on React hooks (useState,
  useContext, useCallback, and so on).


  Set types on u...'
---

By Ibrahima Ndaw

TypeScript lets you type-check your code in order to make it more robust and understandable.

In this guide, I will show you how to set up TypeScript types on React hooks (useState, useContext, useCallback, and so on).

* [Set types on useState](#heading-set-types-on-usestate)
* [Set types on useRef](#heading-set-types-on-useref)
* [Set types on useContext](#heading-set-types-on-usecontext)
* [Set types on useReducer](#heading-set-types-on-usereducer)
* [Set types on useMemo](#heading-set-types-on-usememo)
* [Set types on useCallback](#heading-set-types-on-usecallback)

_Let's dive in._

## Set types on useState

The `useState` hook allows you to manage state in your React app. It's the equivalent of `this.state` in a Class component.

```tsx
import * as React from "react";

export const App: React.FC = () => {
 const [counter, setCounter] = React.useState<number>(0)
 
 return (
    <div className="App">
      <h1>Result: { counter }</h1>
      <button onClick={() => setCounter(counter + 1)}>+</button>
      <button onClick={() => setCounter(counter - 1)}>-</button>
    </div>
  );
}

```

To set types on the `useState` hook, you need to pass into `<>` the type of the state. You can also use a union type like this `<number | null>` if you don't have an initial state.

## Set types on useRef

The `useRef` hook returns a mutable ref object that allows you to access DOM elements.

```tsx
import * as React from "react";

export const App: React.FC = () => {
  const myRef = React.useRef<HTMLElement | null>(null)

  return (
    <main className="App" ref={myRef}>
      <h1>My title</h1>
    </main>
  );
}

```

As you can see, the way `useRef` receives types is the same as the `useState` hook. You just have to pass it into the `<>`. And, if you have multiple type annotations, just use union type as I do here.

## Set types on useContext

`useContext` is a hook that allows you to access and consume a given Context in a React app.

```tsx
import * as React from "react";

interface IArticle {
  id: number
  title: string
}

const ArticleContext = React.createContext<IArticle[] | []>([]);

const ArticleProvider: React.FC<React.ReactNode> = ({ children }) => {
  const [articles, setArticles] = React.useState<IArticle[] | []>([
    { id: 1, title: "post 1" },
    { id: 2, title: "post 2" }
  ]);

  return (
    <ArticleContext.Provider value={{ articles }}>
      {children}
    </ArticleContext.Provider>
  );
}

const ShowArticles: React.FC = () => {
  const { articles } = React.useContext<IArticle[]>(ArticleContext);

  return (
    <div>
      {articles.map((article: IArticle) => (
        <p key={article.id}>{article.title}</p>
      ))}
    </div>
  );
};

export const App: React.FC = () => {
  return (
    <ArticleProvider>
      <h1>My title</h1>
      <ShowArticles />
    </ArticleProvider>
  );
}

```

Here, we start by creating the `IArticle` interface that is the type of our context.  
Next, we use it on the `createContext()` method to create a new context, and then initialize it with `[]`. You can also use `null` as an initial state if you want.

With that in place, we can now handle the state of the context and set the type on `useContext` in order to expect an array of type `IArticle` as a value.

## Set types on useReducer

The `useReducer` hook helps you manage more complex states. It's an alternative to `useState` - but keep in mind that they are different.

```tsx
import * as React from "react";

enum ActionType {
  INCREMENT_COUNTER = "INCREMENT_COUNTER",
  DECREMENT_COUNTER = "DECREMENT_COUNTER"
}

interface IReducer {
  type: ActionType;
  count: number;
}

interface ICounter {
  result: number;
}

const initialState: ICounter = {
  result: 0
};

const countValue: number = 1;

const reducer: React.Reducer<ICounter, IReducer> = (state, action) => {
  switch (action.type) {
    case ActionType.INCREMENT_COUNTER:
      return { result: state.result + action.count };
    case ActionType.DECREMENT_COUNTER:
      return { result: state.result - action.count };
    default:
      return state;
  }
};

export default function App() {
  const [state, dispatch] = React.useReducer<React.Reducer<ICounter, IReducer>>(
    reducer,
    initialState
  );

  return (
    <div className="App">
      <h1>Result: {state.result}</h1>
      <button
        onClick={() =>
          dispatch({ type: ActionType.INCREMENT_COUNTER, count: countValue })
        }> +
      </button>
      <button
        onClick={() =>
          dispatch({ type: ActionType.DECREMENT_COUNTER, count: countValue })
        }> -
      </button>
    </div>
  );
}

```

Here, we start by declaring the action types that allow handling the counter. Next, we set two types for the reducer function and the counter state, respectively.

The reducer expects a `state` of type `ICounter` and an `action` of type `IReducer`. With that, the counter can now be handled.

The `useReducer` hook receives the reducer function and an initial state as arguments and returns two elements: the `state` of the counter and the `dispatch` action.

To set the type for the values returned by `ueReducer`, just pass into the `<>` the type of your data.

With that in place, the counter can now be incremented or decremented through `useReducer`.

### Set types on useMemo

The `useMemo` hook allows you to memoize the output of a given function. It returns a memoized value.

```tsx
const memoizedValue = React.useMemo<string>(() => {
  computeExpensiveValue(a, b)
}, [a, b])

```

To set types on `useMemo`, just pass into the `<>` the type of data you want to memoize. Here, the hook expects a `string` as a returned value.

## Set types on useCallback

The `useCallback` hook allows you to memoize a function to prevent unnecessary re-renders. It returns a memoized callback.

```tsx
type CallbackType = (...args: string[]) => void

const memoizedCallback = React.useCallback<CallbackType>(() => {
    doSomething(a, b);
  }, [a, b]);

```

Here, we declare the `CallbackType` type that is using as type on the callback we want to memoize.

It expects to receive parameters of type `string` and should return a value of type `void`.

Next, we set that type on `useCallback` - and if you pass a wrong type to the callback or the array of dependencies, TypeScript will yell at you.

You can find other great content like this on [my blog](https://www.ibrahima-ndaw.com) or follow me [on Twitter](https://twitter.com/ibrahima92_) to get notified.

Thanks for reading.

