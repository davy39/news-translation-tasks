---
title: Comment utiliser Redux pour la gestion d'état à l'échelle de l'application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-02T15:47:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-redux-for-application-wide-state-management
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/React-redux-2.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: Redux
  slug: redux
seo_title: Comment utiliser Redux pour la gestion d'état à l'échelle de l'application
seo_desc: 'By Prajwal Kulkarni

  Let''s face it – state management across multiple components isn''t easy.

  Sometimes we might set up the state or logic handling properly, but fail to consume
  the states. Or we might get everything working, but clutter up the codebas...'
---

Par Prajwal Kulkarni

Admettons-le – la gestion d'état entre plusieurs composants n'est pas facile.

Parfois, nous pouvons configurer correctement l'état ou la logique de gestion, mais échouer à consommer les états. Ou nous pouvons tout faire fonctionner, mais encombrer la base de code dans le processus, la rendant difficile à lire, adapter et étendre.  

La capacité d'avoir une seule source de vérité (un seul store) est ce qui donne à Redux un avantage sur l'API Context traditionnelle.

Alors, sans plus attendre, voyons comment nous pouvons tirer le meilleur parti de Redux pour la gestion d'état à l'échelle de l'application en écrivant un code plus propre et plus optimisé.

## Avant de commencer

Cet article examine principalement différentes façons d'améliorer un store Redux existant. Vous devrez donc connaître les bases de Redux pour le comprendre, comme la configuration des reducers, le store Redux et le dispatch d'actions.

Si vous avez besoin de vous rafraîchir la mémoire sur Redux, consultez ces guides utiles :

* [Redux pour les débutants](https://www.freecodecamp.org/news/redux-for-beginners/)
* [Le guide convivial pour apprendre Redux](https://www.freecodecamp.org/news/redux-for-beginners-the-brain-friendly-guide-to-redux/)

Vous connaissez déjà les bases de Redux et avez un store Redux que vous souhaitez améliorer ? Parfait.

Voici ce que nous allons couvrir dans cet article :

* Un rapide rappel sur l'utilisation du store Redux
* Comment utiliser la bibliothèque Redux Toolkit en créant un store Redux pour une application e-commerce. Note : nous ne construirons pas l'application entière, mais seulement la partie gestion d'état
* Comment gérer le code asynchrone en dehors des reducers et des composants en utilisant des action creators

Et avec cela, commençons.

## Un rapide rappel sur le store Redux

Avant de voir comment nous pouvons améliorer notre code Redux, examinons brièvement comment nous avons utilisé Redux jusqu'à présent.

Voici un exemple de base d'un store Redux. Il s'agit d'une application de compteur simple qui peut incrémenter et décrémenter le compteur sur des clics de bouton, et l'état du compteur est géré par Redux :

```javascript
import { createStore } from 'redux'

const initialState = {
  counter: 0,
}

const reducer = (state = initialState, action) => { // Fonction reducer
  switch (action.type) {
    case 'INCREMENT':
      return { ...state, counter: state.counter + 1 }
    case 'DECREMENT':
      return { ...state, counter: state.counter - 1 }
    default:
      return state
  }
}

const store = createStore(reducer) // redux-store

export default store

```

```javascript
import { useDispatch, useSelector } from 'react-redux'

export default function Component(props) {
  const dispatch = useDispatch()
  const counter = useSelector((state) => state.counter)

  const incrementHandler = () => {
    dispatch({ type: 'INCREMENT' })
  }
  const decrementHandler = () => {
    dispatch({ type: 'DECREMENT' })
  }

  return (
    <div>
      <h1>Compteur:{counter}</h1>
      <button onClick={incrementHandler}>Incrémenter</button>
      <button onClick={decrementHandler}>Décrémenter</button>
    </div>
  )
}

```

Ceci est un exemple très simple que vous pourriez créer simplement en utilisant des hooks d'état. Mais il sert de bon aperçu de la manière dont nous utiliserions typiquement Redux.

Le store Redux ci-dessus est parfaitement bien s'il n'y a pas beaucoup de types de logique différents qui doivent être gérés ou dispatchés.

De plus, notez que j'ai utilisé `const initialState` au lieu de `var` ou `let` même si nous mettons à jour l'état en raison de la propriété d'immuabilité. C'est-à-dire que nous ne mutons pas vraiment l'état existant, mais reconstruisons plutôt un nouvel état avec les valeurs mises à jour.

C'est bien. Mais que se passe-t-il si la complexité de l'application augmente et nécessite plusieurs gestionnaires d'état et de logique ?

C'est exactement ce que nous allons couvrir dans ce guide.

## Comment créer un store Redux avec Redux Toolkit

Tout au long du reste de l'article, voyons comment gérer l'état dans une application e-commerce. Dans une application e-commerce, nous voudrions suivre et diffuser plusieurs états à travers divers composants.

En règle générale, il est toujours bon d'avoir une idée approximative de la manière dont nous allons implémenter une conception avant de se lancer.

Lorsque nous pensons à une application e-commerce, les états significatifs possibles sont probablement les suivants :

1. Authentification
2. Suivi du panier
3. Liste de surveillance

Nous pouvons diviser la logique de gestion d'état et l'état en différents modules, puis les combiner tous en un seul store.

Pour cela, nous utiliserons Redux Toolkit.

Redux Toolkit est une bibliothèque tierce comme Redux, créée et maintenue par l'équipe Redux.

Vous vous demandez peut-être pourquoi l'équipe Redux a créé Redux Toolkit en premier lieu. La réponse se trouve au début de la [documentation](https://redux-toolkit.js.org/introduction/getting-started) :

> Le package Redux Toolkit est destiné à être la manière standard d'écrire la logique Redux. Il a été créé à l'origine pour aider à résoudre trois préoccupations courantes concernant Redux :  
>   
> - "Configurer un store Redux est trop compliqué"  
> - "Je dois ajouter beaucoup de packages pour que Redux fasse quoi que ce soit d'utile"  
> - "Redux nécessite trop de code boilerplate"

En résumé, le but de l'utilisation de Redux Toolkit est de rendre l'utilisation de Redux plus facile et plus efficace.

### Comment installer Redux Toolkit

Vous pouvez installer Redux Toolkit soit avec `npm` ou `yarn` comme ceci :

* `npm install @reduxjs/toolkit`
* `yarn add @reduxjs/toolkit`

## Comment utiliser Redux Toolkit

La première étape lors de la création d'un store Redux est de configurer la gestion d'état.

Au lieu d'utiliser des reducers, nous utiliserons `createSlice` qui est fourni par Redux Toolkit.

`createSlice` accepte 3 arguments obligatoires, qui sont :

1. **name** : le nom du slice
2. **initialState** : l'état initial du slice (Ceci est comme l'état initial d'un reducer)
3. **reducers** : fonctions qui affectent les états (actions)

Un slice, en bref, est comme un bundler modulaire d'états et de leurs actions.

Commençons par créer un slice pour l'authentification et ses actions associées :

```
const authSlice = createSlice({
  name: 'Auth', // Peut être nommé n'importe quoi
  initialState: {
    isLoggedIn: false,
  },
  reducers: {
    login: (state) => {
      state.isLoggedIn = true
    },
    logout: (state) => {
      state.isLoggedIn = false
    },
  },
})

```

Comme vous pouvez le voir, le slice ci-dessus est dédié à l'authentification des utilisateurs. `initialState` est un objet qui contient différentes valeurs d'état initial, et les états sur lesquels les reducers doivent agir. Les fonctions dans les reducers sont comme des reducers réguliers qui acceptent l'état et l'action comme arguments. 

Un point notable dans l'extrait ci-dessus est la manière dont nous traitons la mise à jour de l'état avec `state.isLoggedIn = true`. Cela semble clairement muter l'état, violant la propriété d'immuabilité.

Ou, est-ce le cas ?

Comprenons ce qui se passe sous le capot avant de tirer des conclusions.

En surface, il semble que nous mutons l'état existant. Mais muter l'état existant ne déclencherait pas la diffusion des valeurs mises à jour aux abonnés.

Ainsi, lorsque nous utilisons la syntaxe de mutation dans les reducers, `createSlice` utilise une bibliothèque appelée [Immer](https://redux-toolkit.js.org/usage/immer-reducers) en interne. Cette bibliothèque établit la différence entre l'état existant et l'état mis à jour, et reconstruit un nouvel objet avec une valeur mise à jour.

Cela signifie que, lorsque nous mutons l'état, Immer s'occupe de construire un nouvel objet et de se conformer à la propriété d'immuabilité, rendant plus facile pour nous l'écriture de code.

Maintenant, écrivons les slices pour les autres états :

```javascript
const cartSlice = createSlice({
  name: 'Cart',
  initialState: {
    cart: [],
    qty: 0,
    total: 0,
  },
  reducers: {
    addItem: (state, action) => {
      state.cart.push(action.payload.cartItem)
      state.qty += action.payload.cartItem.qty
      state.total += action.payload.cartItem.price * action.payload.cartItem.qty
    },
    removeItem: (state, action) => {
      const itemIndex = state.cart.findIndex(
        (obj) => obj.id === action.payload.id
      )
      if (itemIndex !== -1 && state.cart[itemIndex].qty >= 1) {
        state.cart[itemIndex].qty -= 1
      }
    }
  }
})

```

La partie majeure ici est la logique liée à l'ajout et à la suppression d'articles du panier.

Nous suivons une logique similaire pour une liste de surveillance, mais sans la quantité totale et le coût total :

```
const watchlistSlice = createSlice({
  name: 'Watchlist',
  initialState: {
    watchlist: [],
  },
  reducers: {
    addItem: (state, action) => {
      state.watchlist.push(action.payload.watchlistItem)
    },
    removeItem: (state, action) => {
      state.watchlist.filter((item) => item.id !== action.payload.id)
    }
  }
})

```

Remarquez comment l'élément d'action est accessible via la propriété `payload`, et non directement.

C'est parce que Redux Toolkit ajoute la propriété `payload` aux actions par défaut. `payload` est un objet qui peut contenir d'autres objets imbriqués, ou des paires clé-valeur simples. Il contient essentiellement les arguments passés au dispatcher d'action.

Maintenant, vous pourriez vous demander, comment allons-nous réellement dispatcher les action(s) ?

Avant d'utiliser Redux Toolkit, nous effectuions des actions en fonction du `type` d'action. Ensuite, en fonction du `type`, nous effectuions différentes opérations.

Mais ici, nous n'utilisons pas de propriété `type`, car nous allons exporter les fonctions de reducer comme actions, qui pourraient ensuite être invoquées dans le dispatcher.

Les fonctions de reducer peuvent être exportées comme actions en appelant la propriété `actions` sur le slice créé :

`export const authActions = authSlice.actions`

`export const cartActions = cartSlice.actions`

`export const wathclistActions = watchlistSlice.actions`

Tous les slices ici ne sont pas directement liés les uns aux autres, il est donc sûr et aussi une bonne pratique de les avoir dans des fichiers séparés.

Si vous ajoutez des slices à différents fichiers, assurez-vous de les exporter également.

### Comment combiner les slices en un seul store

Un store ne peut avoir qu'un seul reducer, il est donc important de combiner tous les slices et leurs reducers en un seul reducer sans perdre son identité et sa fonctionnalité.

Pour y parvenir, nous utiliserons `configureStore` pour `createStore`.

`configureStore` est similaire à `createStore`, mais il peut fusionner les reducers de plusieurs slices en un seul reducer.

Il a un objet `reducer` qui accepte un ou plusieurs slices, comme ceci :

```js
import { authSlice } from './auth-slice'
import { cartSlice } from './cart-slice'
import { wathclistSlice } from './watchlist-slice'

const store = configureStore({
  reducer: {
    authSliceReducer: authSlice.reducer,
    cartSliceReducer: cartSlice.reducer,
    watchlistSliceReducer: watchlist.reducer,
  },
})

export default store
```

Cela configure le store pour être consommé et utilisé par plusieurs composants à travers l'application.

## Comment utiliser les états Redux dans les composants

Maintenant que nous avons notre store Redux prêt, nous pouvons consommer et dispatcher des actions depuis les composants en utilisant les hooks `useSelector` et `useDispatch`.

Voici un exemple simple :

```js
import { useDispatch, useSelector } from 'react-redux'
import { cartActions } from '...'

export default function Cart(props) {
  const dispatch = useDispatch()
  const selector = useSelector((state) => state.watchlistSliceReducer) // Puisque le store a plusieurs reducers, nous devons accéder à l'état du slice approprié.

  const addToCartHandler = () => {
    const dummyitem = {
      id: Math.random(),
      name: `Dummy Item ${Math.random()}`,
      price: 20 * Math.random(),
    }
    dispatch(cartActions.addItem(cartItem.dummyitem))
  }
  const removeFromCartHandler = (id) => {
    dispatch(cartActions.removeItem(id)) // Passage de l'id comme argument à la fonction reducer.
  }

  return (
    <div>
      {selector.cart.length &&
        selector.cart.map((item) => {
          return (
            <div>
              <p>Nom : {item.name}</p>
              <p>Prix : {item.price}</p>
              <p>Quantité : {item.qty}</p>
              <button onClick={removeFromCartHandler}>Retirer l'article</button>
            </div>
          )
        })}
      <h3>Valeur totale du panier : {selector.cart.total}</h3>
      <button onClick={addToCartHandler}>Ajouter un article factice</button>
    </div>
  )
}

```

## Comment gérer le code asynchrone en utilisant les action creators

Jusqu'à présent, tout va bien.

Mais attendez, il y a encore un sujet important que nous n'avons pas couvert – comment gérer les effets secondaires, ou le code asynchrone, avec Redux. 

Considérez un scénario où vous souhaitez dispatcher une action qui doit gérer un bloc de code produisant un effet secondaire. Mais en même temps, les reducers doivent être purs, sans effets secondaires et synchrones.

Cela signifie que l'ajout de tout code dans les reducers qui produit des effets secondaires va à l'encontre des principes fondamentaux de Redux, et est très mauvais.

Pour traiter de tels cas, nous avons deux choix : soit utiliser `useEffect`/`componentDidMount`, soit écrire des action creators.

### Comment gérer les effets secondaires avec `useEffect` ou `componentDidMount`

Une façon de gérer le code produisant des effets secondaires est d'utiliser `useEffect`. En faisant cela, nous séparons le code produisant des effets secondaires de l'action dispatchée elle-même, de sorte que les reducers restent purs et synchrones.

Mais, un inconvénient majeur de l'utilisation de `useEffect` est la redondance et la duplication du code.

S'il y a deux composants ou plus qui produisent le même effet secondaire, nous voudrions avoir la même logique s'exécuter dans les hooks `useEffect` de ces composants, ce qui est une mauvaise pratique.

Une solution rapide consiste à mettre la logique dans une fonction helper et à exécuter cette fonction au niveau du composant racine, et à faire écouter les changements par tous les autres composants via l'état Redux.

Cela serait acceptable et pas nécessairement une mauvaise pratique, mais une meilleure façon serait d'utiliser un thunk d'action creator.

## Comment gérer les effets secondaires avec les action creators

Un thunk est essentiellement une fonction qui retourne une autre fonction qui n'est pas invoquée immédiatement. En fait, nous avons utilisé des action creators tout ce temps sans le savoir lorsque nous avons dispatché des fonctions d'action.

C'est parce que Redux Toolkit abstrait tout cela pour nous. Ce qui se passe vraiment sous le capot, c'est que cette fonction retourne un objet d'action qui correspond à la fonction de reducer appropriée.

Par exemple, lorsque nous faisons ceci :

`dispatch(actions.dispatchActions(args))`

La méthode `dispatchActions(...)` retourne un objet d'action avec une propriété type et payload. En termes simples, la fonction `dispatchActions()` serait quelque chose comme ceci :

```js
function dispatchActions(args) {
  return { type: 'UNIQUE', payload: { ...args } }
}
```

`type: 'UNIQUE'` est un espace réservé, mais en interne, un identifiant unique est attribué à différents dispatchers d'action, qui sont ensuite reliés à leurs fonctions de reducer respectives. 

Ainsi, `dispatch(actions.dispatchActions(args))` signifie effectivement `dispatch({ type: 'UNIQUE_ID', args: args })`. Cela devrait également clarifier pourquoi la propriété `payload` est attachée au dispatcher d'action.

Ainsi, les thunks sont comme un action creator défini par l'utilisateur qui retourne une fonction au lieu d'un objet d'action. Les thunks d'action creator sont des fonctions autonomes, pas une fonction de reducer, donc nous pouvons écrire du code asynchrone là.

Un thunk d'action creator est une fonction qui accepte les arguments passés par l'utilisateur et retourne une fonction qui accepte davantage un argument dispatch passé par Redux Toolkit pour nous. Et c'est Redux Toolkit lui-même qui invoque plus tard cette fonction retournée.

Le code boilerplate d'un thunk d'action creator ressemblerait à ceci :

```js
export const actionCreatorThunk = async(args) => {
  return (dispatch) => {
    // code asynchrone ici
    dispatch(actions.actionDispatcher(args))
    // plus de code asynchrone
    // plus de fonctions dispatch
  }
}

```

La fonction retournée peut également être une fonction `async`, car il est clair qu'elle gère d'autres codes `async`. Les action creators peuvent avoir plusieurs fonctions dispatch dispatchant plusieurs actions dispatch.

Les thunks d'action creators peuvent ensuite être dispatchés comme suit :

```js
import {actionCreatorThunk} from '...'
import {useDispatch} from 'react-redux'
export default function Component(args){
    const dispatch = useDispatch()
    
    dispatch(actionCreatorThunk(dataToBePassed))
    ...
    ...
    ...
 }
```

Le bon côté de Redux Toolkit est qu'il n'accepte pas seulement les objets d'action retournés par les fonctions de reducer, il accepte également les fonctions retournées par les action creators. 

Lorsque Redux Toolkit identifie qu'une fonction est retournée au lieu d'un objet d'action, il appelle automatiquement la fonction retournée et passe une fonction dispatch comme argument.

Nous pouvons utiliser les action creators dans les endroits où des appels réseau sont effectués, soit pour POST ou interroger des données depuis une base de données, puis définir l'état Redux à partir des données envoyées/reçues. Cela garantit la bonne coordination entre le système backend et frontend.

## En résumé

Si vous êtes arrivé jusqu'ici, félicitations. J'apprécie vraiment que vous ayez pris le temps de lire jusqu'à la fin.

En résumé, le code synchrone et sans effets secondaires doit aller dans les reducers, tandis que le code asynchrone doit être utilisé dans les action creators ou les gestionnaires d'effets secondaires tels que `useEffect`.

C'est tout pour cet article. J'espère que cela vous a aidé à apprendre quelque chose de nouveau sur l'écriture d'un meilleur code Redux pour la gestion d'état à l'échelle de l'application.

Si vous avez des questions ou des commentaires, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/prajwalinbizz).

Vous pouvez également me connecter sur [LinkedIn](https://linkedin.com/prajwal-kulkarni).

Si vous avez trouvé cet article utile, envisagez de le partager avec vos amis qui apprennent React.

Santé !