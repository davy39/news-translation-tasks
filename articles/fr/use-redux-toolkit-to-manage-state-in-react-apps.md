---
title: Comment utiliser Redux Toolkit pour gérer l'état dans votre application React
subtitle: ''
author: Quincy Oghenetejiri Ukumakube
co_authors: []
series: null
date: '2023-04-24T21:38:24.000Z'
originalURL: https://freecodecamp.org/news/use-redux-toolkit-to-manage-state-in-react-apps
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Freecodecamp-Banner.png
tags:
- name: React
  slug: react
- name: 'State Management '
  slug: state-management
seo_title: Comment utiliser Redux Toolkit pour gérer l'état dans votre application
  React
seo_desc: "State management is one of the most important things you'll deal with in\
  \ front end development. \nYou can manage state in React in various ways. Some examples\
  \ include using state in class components, using React hooks such as useState and\
  \ useEffect ho..."
---

La gestion d'état est l'une des choses les plus importantes que vous traiterez dans le développement front-end. 

Vous pouvez gérer l'état dans React de diverses manières. Certains exemples incluent l'utilisation de l'état dans les composants de classe, l'utilisation des hooks React tels que useState et useEffect, l'utilisation de l'API Context, ou l'utilisation de Redux. 

Dans cet article, je vais vous montrer comment utiliser Redux Toolkit pour la gestion d'état dans React. 

### Prérequis

* Une connaissance de base de React (les débutants sont les bienvenus) et de JavaScript est requise.
* Avoir Node installé afin de pouvoir télécharger le package en utilisant `npm`.

## Qu'est-ce que Redux Toolkit ?

Redux Toolkit est un ensemble d'outils que vous pouvez utiliser pour la gestion d'état dans React à la place de Redux. L'équipe Redux l'a créé. 

Redux Toolkit offre une approche standardisée pour construire du code Redux et vient avec des bibliothèques et des outils qui simplifient la création de code Redux scalable, maintenable et efficace.

### En quoi est-il différent de l'ancien Redux ?

Redux Toolkit est différent de Redux de plusieurs manières. Tout d'abord, il a moins de code boilerplate, et il a un bon support. Il fonctionne également mieux avec les composants fonctionnels (contrairement à Redux qui fonctionne mieux avec les composants de classe).

Il existe diverses raisons pour lesquelles vous devriez utiliser Redux Toolkit plutôt que Redux pour la gestion d'état : 

1. Moins de code boilerplate que Redux.
2. Vous n'avez pas à configurer thunk manuellement dans Redux Toolkit car il vient avec `createAsyncThunk`. Cela vous permet d'effectuer des opérations asynchrones.
3. Amélioration de l'expérience développeur : Redux Toolkit inclut un certain nombre d'outils et d'utilitaires qui peuvent améliorer l'expérience développeur, tels que la capacité d'utiliser Redux DevTools directement.
4. Les hooks Redux comme useSelector et useDispatch rendent votre code plus court et plus facile à lire/écrire.
5. Amélioration des performances : Redux Toolkit inclut une fonctionnalité de mémoisation intégrée qui peut aider à améliorer les performances de votre application Redux en réduisant les re-rendus inutiles.

En résumé, Redux Toolkit est un excellent choix pour les développeurs qui souhaitent simplifier leur code Redux et améliorer les performances, tout en améliorant l'expérience développeur. Il peut être particulièrement utile dans les applications plus grandes et plus complexes où la gestion de l'état peut devenir difficile.

## Comment commencer avec Redux Toolkit

Pour ce projet, vous n'utiliserez pas `create-react-app` pour créer votre application React. Au lieu de cela, vous utiliserez Vite et les plugins React. Cela est dû au fait que CRA n'est plus recommandé par la documentation React.

Pour créer votre application, exécutez le code ci-dessous dans votre terminal :

```
npm create vite@latest my-app --template react

```

Ensuite, exécutez les commandes suivantes dans le terminal :

```
cd my-app
npm install
npm run dev

```

### Comment installer Redux Toolkit

Pour utiliser Redux Toolkit dans votre projet, exécutez le code ci-dessous dans votre terminal :

```
npm install @reduxjs/toolkit react-redux
```

### Comment créer un store Redux

Après l'installation, créez un fichier nommé `src/redux/store.jsx`. Importez `configureStore` depuis Redux Toolkit, puis créez un store Redux vide qui sera exporté comme vous pouvez le voir dans le code ci-dessous :

```js
import { configureStore } from '@reduxjs/toolkit'

export const store = configureStore({
  reducer: {},
})
```

Ce code crée un store Redux et configure automatiquement l'extension Redux DevTools afin que vous puissiez inspecter le store pendant le développement.

### Comment connecter le store Redux à React

Après avoir créé le store, vous devrez envelopper votre `<App/>` avec un `<Provider/>` qui sera importé depuis react-redux. De plus, le store que vous avez créé ci-dessus sera passé en tant que prop dans le provider.

```js
//main.js
import React from 'react'
import ReactDOM from 'react-dom'
import './index.css'
import App from './App'
//Importation du store que nous avons créé ci-dessus
import { store } from "./redux/store"
//importation du provider depuis react-redux  
import { Provider } from 'react-redux'

ReactDOM.render(
    //Cela rend le store accessible à l'application qui le passe en tant que prop
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
)
```

### Comment créer une slice Redux

Après la création du store, créez un fichier `src/redux/countslice.jsx`. Ensuite, importez `createSlice` depuis `@redux/toolkit`.

Une slice Redux est un concept introduit par Redux Toolkit qui représente une partie autonome du store Redux qui inclut une fonction de réducteur, un état initial et des créateurs d'actions.

Les slices fournissent un moyen d'organiser et de modulariser le code Redux, ce qui facilite la gestion et la maintenance à mesure que votre application grandit. Vous pouvez considérer les slices comme des mini-stores Redux qui gèrent une partie spécifique de l'état dans votre application.

La création d'une slice nécessite trois choses :

* Nom, qui est généralement défini comme une chaîne de caractères. 
* Valeur d'état initial.
* Réducteur, qui contient des actions qui définissent comment l'état peut être mis à jour.

La création d'une slice d'état crée une architecture plus modulaire et maintenable pour votre application, ce qui facilite le raisonnement et la mise à jour à mesure que votre application grandit.

En organisant votre code Redux en slices, vous pouvez créer une architecture plus modulaire et maintenable pour votre application, ce qui facilite le raisonnement et la mise à jour à mesure que votre application grandit.

Après avoir créé la slice, les réducteurs et les actions Redux à l'intérieur des réducteurs sont exportés différemment. Cela est dû au fait que la slice créée devra être exportée avant de pouvoir être utilisée à l'intérieur du store. 

En exportant le réducteur depuis la slice, vous pouvez facilement l'utiliser pour configurer votre store Redux. Cela facilite également le test du réducteur en isolation, sans avoir besoin de configurer un store Redux complet. Cela peut être utile pour les tests unitaires et pour s'assurer que le réducteur se comporte comme prévu pour chaque action qu'il gère.

```js
import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  count: 0,
}

export const counterSlice = createSlice({
  name: 'counter',
  initialState,
  reducers: {
    increment: (state) => {
      state.count += 1
    },
    decrement: (state) => {
      state.count -= 1
    },
    incrementByAmount: (state, action) => {
      state.count += action.payload
    },
  },
})

// Les créateurs d'actions sont générés pour chaque fonction de réducteur de cas
export const { increment, decrement, incrementByAmount } = counterSlice.actions

export default counterSlice.reducer
```

### Comment ajouter la slice au store 

Le `Reducer` exporté depuis la slice est importé et ajouté au store que vous avez créé précédemment. Cela vous permet de compléter la configuration du store.

```javascript
//store.jsx
import { configureStore } from '@reduxjs/toolkit'
//Importation du réducteur depuis countSlice
import counterReducer from "./countslice"

export const store = configureStore({
  reducer: {
    counter: counterReducer,
  },
})
```

### Comment utiliser l'état et les actions dans vos composants React.

Jusqu'à présent, vous avez simplement parcouru la configuration initiale pour Redux Toolkit, configuré le store et créé le réducteur. Maintenant, vous devez commencer à utiliser l'état et les actions dans votre application pour obtenir la fonctionnalité souhaitée.

Vous utiliserez deux hooks : `useDispatch` et `useSelector`. Les données sont lues depuis le store via le hook `useSelector` tandis que les actions sont dispatchées en utilisant le hook `useDispatch`. 

Les actions correspondantes (increment, decrement, et incrementByAmount) sont importées depuis le fichier `countSlice.jsx` pour être utilisées par le `dispatch`.

Jetez un coup d'œil au code ci-dessous où l'état est défini dans une variable `count` en utilisant le hook `useSelector` et les actions sont définies dans une variable `dispatch` en utilisant le `useDispatch`. Il y a trois boutons : le bouton `increase`, le bouton `decrease`, et le bouton `increaseByAmount`. Un événement `onClick` a été placé sur chaque bouton qui exécute les différentes actions.

Lorsque ces boutons sont cliqués, deux choses se produisent :

* L'action Redux est dispatchée vers le store.
* Le réducteur de slice verra l'action et mettra ensuite à jour l'état.

Voici le code qui fait tout cela :

```js
//App.jsx
import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { decrement, increment, incrementByAmount } from "./redux/countslice"

export default function App() {
  const count = useSelector((state) => state.counter.count)
  const dispatch = useDispatch()

  return (
    
      <div className='App'>
        <h1>The count is {count}</h1>
        <div className="button">
        <button
          onClick={() => dispatch(increment())}
        >
          Increase
        </button>
        <button
          onClick={() => dispatch(decrement())}
        >
          Decrease
        </button>
        <button onClick={()=>dispatch(incrementByAmount(10))} > Increase by 10</button>

        </div>
        
      </div>
    
  )
} 
```

### Le Résultat

C'est exactement ce que vous devriez obtenir lorsque vous exécutez votre code :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Redux-toolkit-GIF.gif)
_Application montrant la fonction de Redux Toolkit_

## Conclusion

Ce tutoriel vous a guidé à travers l'utilisation de Redux Toolkit pour gérer l'état dans votre application React. Vous avez appris comment créer un store en utilisant divers hooks tels que les hooks useSelector et useDispatch pour lire les données depuis le store. 

À ce stade, vous devriez être suffisamment confiant pour utiliser Redux Toolkit pour gérer l'état dans votre application React. 

Connectons-nous sur [Twitter](https://twitter.com/Quincyoghenex) et [LinkedIn](https://www.linkedin.com/in/quincy-oghenetejiri).