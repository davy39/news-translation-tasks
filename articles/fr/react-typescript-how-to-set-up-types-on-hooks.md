---
title: Le React TypeScript Cheatsheet – Comment Configurer les Types sur les Hooks
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
seo_title: Le React TypeScript Cheatsheet – Comment Configurer les Types sur les Hooks
seo_desc: 'By Ibrahima Ndaw

  TypeScript lets you type-check your code in order to make it more robust and understandable.

  In this guide, I will show you how to set up TypeScript types on React hooks (useState,
  useContext, useCallback, and so on).


  Set types on u...'
---

Par Ibrahima Ndaw

TypeScript vous permet de vérifier les types de votre code afin de le rendre plus robuste et compréhensible.

Dans ce guide, je vais vous montrer comment configurer les types TypeScript sur les hooks React (useState, useContext, useCallback, et ainsi de suite).

* [Configurer les types sur useState](#heading-configurer-les-types-sur-usestate)
* [Configurer les types sur useRef](#heading-configurer-les-types-sur-useref)
* [Configurer les types sur useContext](#heading-configurer-les-types-sur-usecontext)
* [Configurer les types sur useReducer](#heading-configurer-les-types-sur-usereducer)
* [Configurer les types sur useMemo](#heading-configurer-les-types-sur-usememo)
* [Configurer les types sur useCallback](#heading-configurer-les-types-sur-usecallback)

_Commençons._

## Configurer les types sur useState

Le hook `useState` vous permet de gérer l'état dans votre application React. C'est l'équivalent de `this.state` dans un composant de classe.

```tsx
import * as React from "react";

export const App: React.FC = () => {
 const [counter, setCounter] = React.useState<number>(0)
 
 return (
    <div className="App">
      <h1>Résultat: { counter }</h1>
      <button onClick={() => setCounter(counter + 1)}>+</button>
      <button onClick={() => setCounter(counter - 1)}>-</button>
    </div>
  );
}

```

Pour configurer les types sur le hook `useState`, vous devez passer dans `<>` le type de l'état. Vous pouvez également utiliser un type union comme ceci `<number | null>` si vous n'avez pas d'état initial.

## Configurer les types sur useRef

Le hook `useRef` retourne un objet ref mutable qui vous permet d'accéder aux éléments du DOM.

```tsx
import * as React from "react";

export const App: React.FC = () => {
  const myRef = React.useRef<HTMLElement | null>(null)

  return (
    <main className="App" ref={myRef}>
      <h1>Mon titre</h1>
    </main>
  );
}

```

Comme vous pouvez le voir, la manière dont `useRef` reçoit les types est la même que celle du hook `useState`. Vous devez simplement les passer dans `<>`. Et, si vous avez plusieurs annotations de type, utilisez simplement un type union comme je le fais ici.

## Configurer les types sur useContext

`useContext` est un hook qui vous permet d'accéder et de consommer un contexte donné dans une application React.

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
      <h1>Mon titre</h1>
      <ShowArticles />
    </ArticleProvider>
  );
}

```

Ici, nous commençons par créer l'interface `IArticle` qui est le type de notre contexte. Ensuite, nous l'utilisons sur la méthode `createContext()` pour créer un nouveau contexte, puis nous l'initialisons avec `[]`. Vous pouvez également utiliser `null` comme état initial si vous le souhaitez.

Avec cela en place, nous pouvons maintenant gérer l'état du contexte et configurer le type sur `useContext` afin d'attendre un tableau de type `IArticle` comme valeur.

## Configurer les types sur useReducer

Le hook `useReducer` vous aide à gérer des états plus complexes. C'est une alternative à `useState` - mais gardez à l'esprit qu'ils sont différents.

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
      <h1>Résultat: {state.result}</h1>
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

Ici, nous commençons par déclarer les types d'action qui permettent de gérer le compteur. Ensuite, nous définissons deux types pour la fonction de réduction et l'état du compteur, respectivement.

Le réducteur attend un `state` de type `ICounter` et une `action` de type `IReducer`. Avec cela, le compteur peut maintenant être géré.

Le hook `useReducer` reçoit la fonction de réduction et un état initial comme arguments et retourne deux éléments : le `state` du compteur et l'action `dispatch`.

Pour configurer le type pour les valeurs retournées par `useReducer`, il suffit de passer dans `<>` le type de vos données.

Avec cela en place, le compteur peut maintenant être incrémenté ou décrémenté via `useReducer`.

### Configurer les types sur useMemo

Le hook `useMemo` vous permet de mémoriser la sortie d'une fonction donnée. Il retourne une valeur mémorisée.

```tsx
const memoizedValue = React.useMemo<string>(() => {
  computeExpensiveValue(a, b)
}, [a, b])

```

Pour configurer les types sur `useMemo`, il suffit de passer dans `<>` le type de données que vous souhaitez mémoriser. Ici, le hook attend une `string` comme valeur retournée.

## Configurer les types sur useCallback

Le hook `useCallback` vous permet de mémoriser une fonction pour éviter les re-rendus inutiles. Il retourne un callback mémorisé.

```tsx
type CallbackType = (...args: string[]) => void

const memoizedCallback = React.useCallback<CallbackType>(() => {
    doSomething(a, b);
  }, [a, b]);

```

Ici, nous déclarons le type `CallbackType` qui est utilisé comme type sur le callback que nous voulons mémoriser.

Il s'attend à recevoir des paramètres de type `string` et doit retourner une valeur de type `void`.

Ensuite, nous définissons ce type sur `useCallback` - et si vous passez un mauvais type au callback ou au tableau des dépendances, TypeScript vous le fera savoir.

Vous pouvez trouver d'autres contenus intéressants comme celui-ci sur [mon blog](https://www.ibrahima-ndaw.com) ou me suivre [sur Twitter](https://twitter.com/ibrahima92_) pour être informé.

Merci d'avoir lu.