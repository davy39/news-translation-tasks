---
title: Qu'est-ce que Redux ? Store, Actions et Reducers expliqués pour les débutants
subtitle: ''
author: Soham De Roy
co_authors: []
series: null
date: '2022-07-27T15:48:39.000Z'
originalURL: https://freecodecamp.org/news/what-is-redux-store-actions-reducers-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Group-60.png
tags:
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'State Management '
  slug: state-management
seo_title: Qu'est-ce que Redux ? Store, Actions et Reducers expliqués pour les débutants
seo_desc: 'Redux is a predictable state container for JavaScript apps. So what does
  that really mean?

  If we dig deeper into this statement, we see that Redux is a state management library
  that you can use with any JS library or framework like React, Angular, or...'
---

Redux est un conteneur d'état prévisible pour les applications JavaScript. Alors, que signifie vraiment cette affirmation ?

Si nous approfondissons cette déclaration, nous voyons que Redux est une bibliothèque de gestion d'état que vous pouvez utiliser avec n'importe quelle bibliothèque ou framework JS comme React, Angular ou Vue.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/1-1.png)

Dans cet article, nous allons couvrir les fondamentaux de Redux. Nous allons apprendre ce qu'est Redux à sa base ainsi que ses trois principes clés.

Nous allons également voir comment certains de ses blocs de construction principaux fonctionnent, tels que le store, les actions et les reducers, et comment ils s'assemblent tous pour faire de Redux la bibliothèque de gestion d'état global qu'elle est.

En tant que prérequis, je vais supposer que vous êtes familier avec React.

## Pourquoi utiliser Redux ?

Eh bien, une application a son état, qui peut être une combinaison des états de ses composants internes.

Prenons par exemple un site web de commerce électronique. Un site web de commerce électronique aura plusieurs composants comme le composant panier, le composant profil utilisateur, le composant section précédemment consultée, et ainsi de suite.

Nous allons prendre le composant panier qui affiche le nombre d'articles dans le panier d'un utilisateur. L'état du composant panier consistera en tous les articles que l'utilisateur a ajoutés au panier et le nombre total de ces articles. À tout moment où l'application est en cours d'exécution, ce composant doit montrer le nombre mis à jour d'articles dans le panier de l'utilisateur.

Chaque fois qu'un utilisateur ajoute un article au panier, l'application doit gérer cette action en interne en ajoutant cet article à l'objet panier. Elle doit maintenir son état en interne et également montrer à l'utilisateur le nombre total d'articles dans le panier dans l'interface utilisateur.

De même, supprimer un article du panier devrait diminuer le nombre d'articles dans le panier en interne. Il devrait supprimer l'article de l'objet panier et également afficher le nombre total mis à jour d'articles dans le panier dans l'interface utilisateur.

Nous pouvons très bien maintenir l'état interne des composants à l'intérieur d'eux, mais à mesure qu'une application grandit, elle peut devoir partager certains états entre les composants. Ce n'est pas seulement pour les afficher dans la vue, mais aussi pour les gérer ou les mettre à jour ou effectuer une logique basée sur leur valeur.

Cette tâche de gestion de plusieurs états provenant de plusieurs composants efficacement peut devenir difficile lorsque l'application grandit en taille.

C'est là que Redux entre en jeu. En tant que bibliothèque de gestion d'état, Redux stockera et gérera essentiellement tous les états de l'application.

Elle nous fournit également certaines API importantes que nous pouvons utiliser pour apporter des modifications à l'état existant ainsi que pour récupérer l'état actuel de l'application.


## Qu'est-ce qui rend Redux prévisible ?

L'état est **en lecture seule** dans Redux. Ce qui rend Redux prévisible, c'est que pour apporter une modification à l'état de l'application, nous devons dispatcher une action qui décrit les modifications que nous souhaitons apporter à l'état.

Ces actions sont ensuite consommées par quelque chose appelé reducers, dont le seul travail est d'accepter deux choses (l'action et l'état actuel de l'application) et de retourner une nouvelle instance mise à jour de l'état.

Nous parlerons davantage des actions et des reducers dans les sections suivantes.

Notez que les reducers ne modifient aucune partie de l'état. Plutôt, un reducer produit une nouvelle instance de l'état avec toutes les mises à jour nécessaires.

Selon @[Dan Abramov](@gaearon) (le créateur de Redux) lui-même,

>"Les actions peuvent être enregistrées et rejouées plus tard, ce qui rend la gestion d'état prévisible. Avec les mêmes actions dans le même ordre, vous allez vous retrouver dans le même état."

Ainsi, en continuant avec notre exemple précédent d'un site web de commerce électronique, si l'état initial du panier est qu'il a 0 article, alors une action d'**ajout d'un article** au panier augmentera le nombre d'articles dans le panier de 1. Et déclencher l'action d'**ajout d'un article** au panier à nouveau augmentera le nombre d'articles dans le panier à 2.

Étant donné un état initial, avec une liste spécifique d'**actions** dans un ordre spécifique, cela nous fournira toujours exactement le même état final de l'entité. C'est ainsi que Redux rend la gestion d'état prévisible.

Dans la section suivante, nous allons plonger profondément dans les concepts clés de Redux – le store, les actions et les reducers.

## Principes de base de Redux

![Image](https://www.freecodecamp.org/news/content/images/2022/06/2.png)

### 1. Qu'est-ce que le Redux Store ?

> L'état global d'une application est stocké dans un arbre d'objets au sein d'un seul store – [Redux docs](https://redux.js.org/understanding/thinking-in-redux/three-principles)

Le Redux store est le principal conteneur central qui stocke tous les états d'une application. Il doit être considéré et maintenu comme une **source unique de vérité** pour l'état de l'application.

Si le `store` est fourni à **App.js** (en enveloppant le composant `App` dans les balises `<Provider>` `</Provider>`) comme montré dans l'extrait de code ci-dessous, alors tous ses enfants (composants enfants de `App.js`) peuvent également accéder à l'état de l'application à partir du store. Cela en fait un état global.

```js
// src/index.js

import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'

import { App } from './App'
import createStore from './createReduxStore'

const store = createStore()

// À partir de React 18
const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
  <Provider store={store}>
    <App />
  </Provider>
)

```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/4.png)

L'état de toute l'application est stocké sous la forme d'un **arbre d'objets JS** dans un **seul store** comme montré ci-dessous.

```js
// voici à quoi ressemble la structure de l'objet store
{
    noOfItemInCart: 2,
    cart: [
        {
            bookName: "Harry Potter et la Chambre des Secrets",
            noOfItem: 1,
        },
        {
            bookName: "Harry Potter et le Prisonnier d'Azkaban",
            noOfItem: 1
        }
    ]
}

```

### 2. Que sont les Actions dans Redux ?

> La seule façon de changer l'état est d'émettre une action, qui est un objet décrivant ce qui s'est passé – [Redux Docs](https://redux.js.org/understanding/thinking-in-redux/three-principles)

Comme mentionné ci-dessus, l'état dans Redux est en lecture seule. Cela vous aide à restreindre toute partie de la vue ou tout appel réseau à écrire/mettre à jour l'état directement.

Au lieu de cela, si quelqu'un veut changer l'état de l'application, il devra exprimer son intention de le faire en **émettant ou en dispatchant une action**.

Prenons l'exemple du store ci-dessus où nous avons 2 livres dans le store : *"Harry Potter et la Chambre des Secrets"* et *"Harry Potter et le Prisonnier d'Azkaban"*. Il n'y a qu'une seule copie de chaque.

Maintenant, si l'utilisateur veut ajouter un autre article au panier, il devra cliquer sur le bouton **"Ajouter au panier"** à côté de l'article.

Au clic sur le bouton **"Ajouter au panier"**, une action sera dispatchée. Cette action n'est rien d'autre qu'un objet JS décrivant les modifications à apporter dans le store. Quelque chose comme ceci :

```js
// Reste du code

const dispatch = useDispatch()

const addItemToCart = () => {
return {
    type: "ADD_ITEM_TO_CART"
    payload: {
        bookName: "Harry Potter et la Coupe de Feu",
        noOfItem: 1,
        }
    }
}

<button onClick = {() => dispatch(addItemToCart())}>Ajouter au panier</button>

// Reste du code
```

Notez comment dans l'exemple ci-dessus, nous dispatchons une action au clic sur le bouton. Ou plutôt, pour être plus précis, nous dispatchons quelque chose appelé un **créateur d'action** – c'est-à-dire, la fonction `addItemToCart()`. Cela retourne à son tour une `action` qui est un objet JS simple décrivant le but de l'action désigné par la clé `type` ainsi que toute autre donnée requise pour le changement d'état. Dans ce cas, il s'agit du nom du livre à ajouter au panier désigné par la clé `payload`.

**Chaque action doit avoir au moins** un `type` associé. Tout autre détail à passer est optionnel et dépendra du type d'action que nous dispatchons.

Par exemple, l'extrait de code ci-dessus dispatches l'action suivante :

```js
// Action créée par le créateur d'action addItemToCart()

{
    type: "ADD_ITEM_TO_CART" // Note : Chaque action doit avoir une clé type
    payload: {
        bookName: "Harry Potter et la Coupe de Feu",
        noOfItem: 1,
    }
}
```

### 3. Que sont les Reducers dans Redux ?

> Pour spécifier comment l'arbre d'état est transformé par les actions, nous écrivons des reducers purs – [Redux docs](https://redux.js.org/understanding/thinking-in-redux/three-principles)

![Image](https://www.freecodecamp.org/news/content/images/2022/06/3.png)

Les reducers, comme leur nom l'indique, prennent deux choses : **l'état précédent** et **une action**. Ensuite, ils les réduisent (lisez, retournent) à une seule entité : la **nouvelle instance mise à jour de l'état**.

Ainsi, les reducers sont essentiellement des fonctions JS pures qui prennent l'état précédent et une action et retournent le nouvel état mis à jour.

Il peut y avoir un seul reducer si c'est une application simple ou plusieurs reducers prenant en charge différentes parties ou tranches de l'état global dans une application plus grande.

Par exemple, il peut y avoir un reducer gérant l'état du panier dans une application d'achat, puis il peut y avoir un reducer gérant la partie détails de l'utilisateur de l'application, et ainsi de suite.

Chaque fois qu'une action est dispatchée, **tous les reducers sont activés**. Chaque reducer filtre l'action en utilisant une instruction switch basculant sur le **type d'action**. Chaque fois que l'instruction switch correspond à l'action passée, les reducers correspondants prennent les mesures nécessaires pour effectuer la mise à jour et retournent une nouvelle instance fraîche de l'état global.

En continuant avec notre exemple précédent, nous pouvons avoir un reducer comme suit :

```js

const initialCartState = {    
    noOfItemInCart: 0,          
    cart: []                              
}

// NOTE :
// Il est important de passer un état initial comme valeur par défaut au
// paramètre state pour gérer le cas de l'appel
// des reducers pour la première fois lorsque le
// state peut être indéfini

const cartReducer = (state = initialCartState, action) => {
    switch (action.type) {
        case "ADD_ITEM_TO_CART": 
            return {
                ...state,
                noOfItemInCart: state.noOfItemInCart + 1,
                cart : [
                    ...state.cart,
                    action.payload
                ]
            }
        case "DELETE_ITEM_FROM_CART":
            return {
                // Logique restante
            }
        default: 
            return state  
    }       // Important de gérer le comportement par défaut
}           // soit en retournant tout l'état tel quel
            // soit en effectuant une logique requise

```

Dans l'extrait de code ci-dessus, nous avons créé un reducer appelé `cartReducer` qui est une fonction JS pure. Cette fonction accepte deux paramètres : `state` et `action`.

Notez que le paramètre `state` est un paramètre par défaut qui accepte un état initial. Cela est pour gérer le scénario lorsque **le reducer est appelé pour la première fois** lorsque la valeur `state` est `undefined`.

Notez également que chaque reducer doit gérer le cas `default` où, si aucun des cas du switch ne correspond à l'action passée, alors le reducer doit retourner `state` tel quel ou effectuer une logique requise avant de passer l'état.

Chaque fois que nous dispatchons une action avec un certain type, nous devons nous assurer d'avoir des reducers appropriés pour gérer cette action.

Dans l'exemple ci-dessus, en cliquant sur le bouton, nous avons dispatché une **action** avec un **créateur d'action** appelé `addItemToCart()`. Ce créateur d'action a dispatché une action avec le `type` `ADD_ITEM_TO_CART`.

Ensuite, nous avons créé un **reducer** appelé `cartReducer` qui prend l'état (avec l'état initial par défaut) et l'action comme paramètres. Il bascule sur le **type d'action**, puis, quel que soit le cas qui correspond au type d'action dispatché, il effectue la mise à jour nécessaire et retourne la nouvelle version fraîche de l'état mis à jour.

Notez ici que **l'état dans redux est immutable**. Ainsi, les reducers font une copie de tout l'état actuel d'abord, apportent les modifications nécessaires, puis retournent une nouvelle instance fraîche de l'état – avec toutes les modifications/updates nécessaires.

Ainsi, dans l'exemple ci-dessus, nous faisons d'abord une copie de tout l'état en utilisant l'opérateur de propagation `...state`. Ensuite, nous incrémentons le `noOfItemInCart` de 1, mettons à jour le tableau cart en ajoutant le nouvel objet passé dans le `action.payload` montré ci-dessous, puis retournons enfin l'objet mis à jour.

```js
{
    bookName: "Harry Potter et la Coupe de Feu",
    noOfItem: 1,
}

```

Après que les reducers ont mis à jour l'état, si nous allons et `console.log` l'`state`, alors nous verrions le résultat suivant :

```js
// Store mis à jour

{
    noOfItemInCart: 3, // Incrémenté de 1
    cart: [
        {
            bookName: "Harry Potter et la Chambre des Secrets",
            noOfItem: 1,
        },
        {
            bookName: "Harry Potter et le Prisonnier d'Azkaban",
            noOfItem: 1
        },
        { // Objet nouvellement ajouté
            bookName: "Harry Potter et la Coupe de Feu",
            noOfItem: 1,
        }
    ]
}

```
## Résumé

En bref, les trois principes suivants gouvernent complètement le fonctionnement de Redux :

- L'état global d'une application est stocké dans un arbre d'objets au sein d'un seul **store**
- La seule façon de changer l'état est d'émettre une **action**, qui est un objet décrivant ce qui s'est passé
- Pour spécifier comment l'arbre d'état est transformé par les actions, nous écrivons des **reducers purs**

## Conclusion

Merci d'avoir lu ! J'espère vraiment que vous avez apprécié apprendre Redux et ses principes de base et que vous avez trouvé ce tutoriel utile.

N'hésitez pas à le partager avec vos amis, j'apprécierais vraiment cela. Restez à l'écoute pour plus de contenu incroyable. Peace out ! 🖖

### Liens sociaux

- [LinkedIn](https://www.linkedin.com/feed/)
- [Site Web](https://www.sohamderoy.dev/)
- [Autres Blogs](https://www.freecodecamp.org/news/author/sohamderoy)
- [Twitter](https://twitter.com/_sohamderoy)