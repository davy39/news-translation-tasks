---
title: Comment utiliser Redux dans votre application React TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-08T23:33:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-redux-in-your-react-typescript-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/cover.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: TypeScript
  slug: typescript
seo_title: Comment utiliser Redux dans votre application React TypeScript
seo_desc: "By Ibrahima Ndaw\nRedux is a predictable state container for JavaScript\
  \ apps. It's a popular library for managing state in React apps. \nRedux can offer\
  \ a better developer experience when you use it along with TypeScript. TypeScript\
  \ is a superset of Ja..."
---

Par Ibrahima Ndaw

Redux est un conteneur d'état prévisible pour les applications JavaScript. C'est une bibliothèque populaire pour gérer l'état dans les applications React. 

Redux peut offrir une meilleure expérience de développement lorsque vous l'utilisez avec TypeScript. TypeScript est un sur-ensemble de JavaScript qui vérifie les types de code pour le rendre robuste et compréhensible.

Dans ce guide, je vais vous montrer comment utiliser Redux dans votre projet React TypeScript en construisant une application qui vous permet d'ajouter, de supprimer et d'afficher des articles.

_Commençons._

* [Prérequis](#heading-prerequis)
* [Installation](#heading-installation)
* [Créer les types](#heading-creer-les-types)
* [Créer les types d'actions](#heading-creer-les-types-d-actions)
* [Créer les créateurs d'actions](#heading-creer-les-createurs-d-actions)
* [Créer un réducteur](#heading-creer-un-reducteur)
* [Créer un store](#heading-creer-un-store)
* [Créer les composants](#heading-creer-les-composants)

## Prérequis

Ce tutoriel suppose que vous avez au moins une compréhension de base de React, Redux et TypeScript. 

Donc, si vous n'êtes pas familier avec ces technologies, essayez d'abord de lire ce [guide pratique de TypeScript](https://www.ibrahima-ndaw.com/blog/a-practical-guide-to-typescript/) ou [ce tutoriel React Redux](https://www.ibrahima-ndaw.com/blog/7-steps-to-understand-react-redux/). Sinon, commençons.

## Installation du projet

Pour utiliser Redux et TypeScript, nous devons créer une nouvelle application React.

Pour ce faire, ouvrons le CLI (interface de ligne de commande) et exécutons cette commande :

```shell
  npx create-react-app my-app --template typescript

```

Ensuite, structurons le projet comme suit :

```
├── src
│   ├── components
│   │   ├── AddArticle.tsx
│   │   └── Article.tsx
│   ├── store
│   │   ├── actionCreators.ts
│   │   ├── actionTypes.ts
│   │   └── reducer.ts
│   ├── type.d.ts
│   ├── App.test.tsx
│   ├── App.tsx
│   ├── index.css
│   ├── index.tsx
│   ├── react-app-env.d.ts
│   └── setupTests.ts
├── tsconfig.json
├── package.json
└── yarn.lock

```

La structure de fichiers du projet est assez simple. Cependant, il y a deux choses à noter :

* Le dossier `store` qui contient les fichiers liés à React Redux.
* Le fichier `type.d.ts` qui contient les types TypeScript, qui peuvent être utilisés maintenant dans d'autres fichiers sans importation.

Cela dit, nous pouvons maintenant installer Redux et créer notre premier store.

Donc, ouvrons le projet et exécutons la commande suivante :

```shell
  yarn add redux react-redux redux-thunk

```

Ou lorsque vous utilisez `npm`

```shell
  npm install redux react-redux redux-thunk

```

Nous devons également installer leurs types en tant que dépendances de développement pour aider TypeScript à comprendre les bibliothèques.

Donc, exécutons à nouveau cette commande sur le CLI.

```shell
  yarn add -D @types/redux @types/react-redux @types/redux-thunk

```

Ou pour `npm` :

```shell
  npm install -D @types/redux @types/react-redux @types/redux-thunk

```

Super ! Avec cette étape franchie, nous pouvons maintenant créer les types TypeScript pour le projet dans la section suivante.

## Créer les types

Les types TypeScript vous permettent de définir des types pour vos variables, paramètres de fonction, etc.

* type.d.ts

```ts
interface IArticle {
  id: number
  title: string
  body: string
}

type ArticleState = {
  articles: IArticle[]
}

type ArticleAction = {
  type: string
  article: IArticle
}

type DispatchType = (args: ArticleAction) => ArticleAction

```

Ici, nous commençons par déclarer l'interface `IArticle` qui reflète la forme d'un article donné. 

Ensuite, nous avons `ArticleState`, `ArticleAction` et `DispatchType` qui serviront de types pour, respectivement, l'objet d'état, les créateurs d'actions et la fonction de dispatch fournie par Redux.

Cela dit, nous avons maintenant les types nécessaires pour commencer à utiliser React Redux. Créons les types d'actions.

## Créer les types d'actions

* store/actionTypes.ts

```ts
export const ADD_ARTICLE = "ADD_ARTICLE"
export const REMOVE_ARTICLE = "REMOVE_ARTICLE"

```

Nous avons besoin de deux types d'actions pour le store Redux. Un pour ajouter des articles et un autre pour les supprimer.

## Créer les créateurs d'actions

* store/actionCreators.ts

```ts
import * as actionTypes from "./actionTypes"

export function addArticle(article: IArticle) {
  const action: ArticleAction = {
    type: actionTypes.ADD_ARTICLE,
    article,
  }

  return simulateHttpRequest(action)
}

export function removeArticle(article: IArticle) {
  const action: ArticleAction = {
    type: actionTypes.REMOVE_ARTICLE,
    article,
  }
  return simulateHttpRequest(action)
}

export function simulateHttpRequest(action: ArticleAction) {
  return (dispatch: DispatchType) => {
    setTimeout(() => {
      dispatch(action)
    }, 500)
  }
}

```

Dans ce tutoriel, je vais simuler la requête HTTP en la retardant de 0,5 seconde. Mais, n'hésitez pas à utiliser un vrai serveur si vous le souhaitez.

Ici, la fonction `addArticle` va dispatcher une action pour ajouter un nouvel article, et la méthode `removeArticle` fera l'inverse. Donc, supprimez l'objet passé en argument.

## Créer un réducteur

Un réducteur est une fonction pure qui reçoit l'état du store et une action en paramètres, puis retourne l'état mis à jour.

* store/reducer.ts

```ts
import * as actionTypes from "./actionTypes"

const initialState: ArticleState = {
  articles: [
    {
      id: 1,
      title: "post 1",
      body:
        "Quisque cursus, metus vitae pharetra Nam libero tempore, cum soluta nobis est eligendi",
    },
    {
      id: 2,
      title: "post 2",
      body:
        "Harum quidem rerum facilis est et expedita distinctio quas molestias excepturi sint",
    },
  ],
}

```

Comme vous pouvez le voir ici, nous déclarons un état initial pour avoir quelques articles à afficher lorsque la page se charge. L'objet d'état doit correspondre au type `ArticleState` - sinon, TypeScript générera une erreur.

* store/reducer.ts

```ts
const reducer = (
  state: ArticleState = initialState,
  action: ArticleAction
): ArticleState => {
  switch (action.type) {
    case actionTypes.ADD_ARTICLE:
      const newArticle: IArticle = {
        id: Math.random(), // pas vraiment unique
        title: action.article.title,
        body: action.article.body,
      }
      return {
        ...state,
        articles: state.articles.concat(newArticle),
      }
    case actionTypes.REMOVE_ARTICLE:
      const updatedArticles: IArticle[] = state.articles.filter(
        article => article.id !== action.article.id
      )
      return {
        ...state,
        articles: updatedArticles,
      }
  }
  return state
}

export default reducer

```

Ensuite, nous avons la fonction `reducer` qui attend l'état précédent et une action pour pouvoir mettre à jour le store. Ici, nous avons deux actions : une pour ajouter et une autre pour supprimer.

Avec cela en place, nous pouvons maintenant gérer l'état avec le réducteur. Créons maintenant un store pour le projet.

## Créer un store

Un store Redux est l'endroit où vit l'état de votre application.

* index.tsx

```tsx
import * as React from "react"
import { render } from "react-dom"
import { createStore, applyMiddleware, Store } from "redux"
import { Provider } from "react-redux"
import thunk from "redux-thunk"

import App from "./App"
import reducer from "./store/reducer"

const store: Store<ArticleState, ArticleAction> & {
  dispatch: DispatchType
} = createStore(reducer, applyMiddleware(thunk))

const rootElement = document.getElementById("root")
render(
  <Provider store={store}>
    <App />
  </Provider>,
  rootElement
)

```

Comme vous pouvez le voir, nous importons la fonction de réducteur puis la passons en argument à la méthode `createStore` afin de créer un nouveau store Redux. Le middleware `redux-thunk` doit également être traité comme un deuxième paramètre de la méthode pour pouvoir gérer le code asynchrone.

Ensuite, nous connectons React à Redux en fournissant l'objet `store` comme props au composant `Provider`.

Nous pouvons maintenant utiliser Redux dans ce projet et accéder au store. Donc, créons les composants pour obtenir et manipuler les données.

## Créer les composants

* components/AddArticle.tsx

```tsx
import * as React from "react"

type Props = {
  saveArticle: (article: IArticle | any) => void
}

export const AddArticle: React.FC<Props> = ({ saveArticle }) => {
  const [article, setArticle] = React.useState<IArticle | {}>()

  const handleArticleData = (e: React.FormEvent<HTMLInputElement>) => {
    setArticle({
      ...article,
      [e.currentTarget.id]: e.currentTarget.value,
    })
  }

  const addNewArticle = (e: React.FormEvent) => {
    e.preventDefault()
    saveArticle(article)
  }

  return (
    <form onSubmit={addNewArticle} className="Add-article">
      <input
        type="text"
        id="title"
        placeholder="Titre"
        onChange={handleArticleData}
      />
      <input
        type="text"
        id="body"
        placeholder="Description"
        onChange={handleArticleData}
      />
      <button disabled={article === undefined ? true : false}>
        Ajouter un article
      </button>
    </form>
  )
}

```

Pour ajouter un nouvel article, nous allons utiliser ce composant de formulaire. Il reçoit la fonction `saveArticle` comme paramètre, ce qui permet d'ajouter un nouvel article au store. 

L'objet article doit suivre le type `IArticle` pour rendre TypeScript heureux.

* components/Article.tsx

```tsx
import * as React from "react"
import { Dispatch } from "redux"
import { useDispatch } from "react-redux"

type Props = {
  article: IArticle
  removeArticle: (article: IArticle) => void
}

export const Article: React.FC<Props> = ({ article, removeArticle }) => {
  const dispatch: Dispatch<any> = useDispatch()

  const deleteArticle = React.useCallback(
    (article: IArticle) => dispatch(removeArticle(article)),
    [dispatch, removeArticle]
  )

  return (
    <div className="Article">
      <div>
        <h1>{article.title}</h1>
        <p>{article.body}</p>
      </div>
      <button onClick={() => deleteArticle(article)}>Supprimer</button>
    </div>
  )
}

```

Le composant `Article` affiche un objet article.

La fonction `removeArticle` doit dispatcher pour accéder au store et ainsi supprimer un article donné. C'est la raison pour laquelle nous utilisons le hook `useDispatch` ici, qui permet à Redux de compléter l'action de suppression.

Ensuite, l'utilisation de `useCallback` aide à éviter les re-rendus inutiles en mémorisant les valeurs en tant que dépendances.

Nous avons enfin les composants dont nous avons besoin pour ajouter et afficher les articles. Ajoutons maintenant la dernière pièce au puzzle en les utilisant dans le fichier `App.tsx`.

* App.tsx

```tsx
import * as React from "react"
import { useSelector, shallowEqual, useDispatch } from "react-redux"
import "./styles.css"

import { Article } from "./components/Article"
import { AddArticle } from "./components/AddArticle"
import { addArticle, removeArticle } from "./store/actionCreators"
import { Dispatch } from "redux"

const App: React.FC = () => {
  const articles: readonly IArticle[] = useSelector(
    (state: ArticleState) => state.articles,
    shallowEqual
  )

  const dispatch: Dispatch<any> = useDispatch()

  const saveArticle = React.useCallback(
    (article: IArticle) => dispatch(addArticle(article)),
    [dispatch]
  )

  return (
    <main>
      <h1>Mes Articles</h1>
      <AddArticle saveArticle={saveArticle} />
      {articles.map((article: IArticle) => (
        <Article
          key={article.id}
          article={article}
          removeArticle={removeArticle}
        />
      ))}
    </main>
  )
}

export default App

```

Le hook `useSelector` permet d'accéder à l'état du store. Ici, nous passons `shallowEqual` comme deuxième argument à la méthode pour indiquer à Redux d'utiliser l'égalité superficielle lors de la vérification des changements.

Ensuite, nous nous appuyons sur `useDispatch` pour dispatcher une action pour ajouter des articles dans le store. Enfin, nous parcourons le tableau des articles et passons chacun au composant `Article` pour l'afficher.

Avec cela, nous pouvons maintenant naviguer jusqu'à la racine du projet et exécuter cette commande :

```shell
  yarn start

```

Ou pour `npm` :

```shell
  npm start

```

Si vous ouvrez `http://localhost:3000/` dans le navigateur, vous devriez voir ceci :

![Aperçu de l'application](https://www.freecodecamp.org/news/content/images/2021/10/mxuc7kv9gtkiuuxdf4hx.png)

Super ! Notre application a l'air bien. Avec cela, nous avons maintenant terminé l'utilisation de Redux dans une application React TypeScript.

Vous pouvez trouver le projet terminé [dans ce CodeSandbox](https://codesandbox.io/s/react-redux-typescript-oc4hi).

Vous pouvez trouver d'autres excellents contenus comme celui-ci sur [mon blog](https://www.ibrahima-ndaw.com) ou me suivre [sur Twitter](https://twitter.com/ibrahima92_) pour être notifié.

Merci d'avoir lu.