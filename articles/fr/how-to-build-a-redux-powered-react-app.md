---
title: Comment créer une application React alimentée par Redux
subtitle: ''
author: Soham De Roy
co_authors: []
series: null
date: '2022-08-03T21:51:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-redux-powered-react-app
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Group-58.png
tags:
- name: React
  slug: react
- name: Redux
  slug: redux
seo_title: Comment créer une application React alimentée par Redux
seo_desc: "The Problem We're Solving\nIn many cases when we want to create a small\
  \ application, we might have some components that declare and use their own state.\
  \ And in a few cases, a component might want to share the state with its immediate\
  \ children. \nWe can..."
---

## Le problème que nous résolvons
Dans de nombreux cas, lorsque nous voulons créer une petite application, nous pouvons avoir certains composants qui déclarent et utilisent leur propre état. Et dans quelques cas, un composant peut vouloir partager l'état avec ses enfants immédiats. 

Nous pouvons gérer ces situations simplement en déclarant des états localement dans un composant – et peut-être en passant l'état à ses enfants sous forme de props si nécessaire (ce qui est également connu sous le nom de prop drilling). 

Mais si votre application grandit en taille, vous pourriez avoir besoin de passer l'état à un enfant qui pourrait être plusieurs étapes plus bas dans la hiérarchie. Vous pourriez également avoir besoin d'utiliser un état commun entre des composants frères. 

Bien sûr, dans le cas du partage d'état entre des composants frères, nous pouvons déclarer l'état dans leurs parents et ensuite passer l'état à leurs enfants par prop drilling. Mais cela n'est pas toujours réalisable et présente ses propres inconvénients que nous verrons dans un instant. 

Considérez simplement le diagramme suivant :

![Group-49](https://www.freecodecamp.org/news/content/images/2022/08/Group-49.png)

Il s'agit d'une représentation schématique d'une structure de fichiers de composants dans une application React typique. 

Disons que nous devons partager un état commun entre l'Enfant 5 et l'Enfant 6. Dans ce cas, nous pouvons très bien déclarer un état dans leur parent (c'est-à-dire, l'Enfant 2) et passer l'état aux deux enfants (5 et 6). 

Tout va bien pour l'instant. Mais que faire si nous devons avoir le même morceau d'état dans l'Enfant 3 ? Dans ce cas, nous devrions déclarer l'état dans le parent/grand-parent commun des Enfants 5, 6 et 3 – c'est-à-dire, le composant App. 

De même, que faire si nous voulons partager un état entre les Enfants 4, 11 et 10 qui sont éloignés les uns des autres dans l'arbre ? Nous devrions à nouveau créer l'état dans le composant App et ensuite faire plusieurs niveaux de prop drilling pour passer l'état de App à ces composants. 

Et avec le temps, lorsque notre application grandit en taille, elle commencera à encombrer notre composant App ou tout autre composant parent commun avec des déclarations d'état inutiles. Ces déclarations ne sont pas utilisées directement par ces composants mais sont utilisées par certains de leurs enfants éloignés.

## Inconvénients du Prop Drilling Multi-Niveaux
Il y a principalement deux inconvénients avec le prop drilling multi-niveaux. Ils sont :

- **Encombrement inutile des composants** : Comme discuté ci-dessus, à mesure que notre application grandit en taille, certains composants parents communs peuvent être encombrés de déclarations d'état inutiles. Et ces composants peuvent ne pas utiliser directement ces déclarations, mais elles peuvent être utilisées par certains de leurs enfants éloignés. Certains autres composants peuvent également être encombrés qui ne font que passer des props à un composant enfant. Cela affectera également négativement la lisibilité du code.
- **Re-rendu inutile** : Le re-rendu inutile est un grand non pour une application côté client. Les re-rendus inutiles peuvent rendre une application lente, laggy, non réactive et donner une mauvaise expérience utilisateur. Dans React, les re-rendus sont causés par des changements d'état ou de props, entre autres raisons. Donc si un composant n'utilise pas réellement un état et ne fait que servir de passage de parent à enfant pour les props, alors il peut également être re-rendu inutilement lorsque l'état/les props changent. Voir l'image ci-dessous pour mieux comprendre

![Group-52-1](https://www.freecodecamp.org/news/content/images/2022/08/Group-52-1.png)

## La solution à ce problème
C'est pourquoi nous utilisons une application de gestion d'état comme Redux ou MobX pour gérer les scénarios ci-dessus de gestion d'état de manière plus uniforme et efficace. 

Dans ces types de solutions de gestion d'état comme Redux, nous pouvons créer un état global et le mettre dans un store. Tout composant nécessitant un état de ce store peut facilement l'obtenir en s'y abonnant. De cette manière, nous pouvons nous débarrasser des deux inconvénients ci-dessus.

- **Désencombrement des composants** : Obtenir l'état à la demande depuis le composant qui l'utilise "réellement" peut désencombrer beaucoup de nos composants dans une large mesure en supprimant tout prop drilling inutile.
- **Plus de re-rendus inutiles** : Comme nous n'avons pas de composants qui ne font que passer des props, nous évitons également les re-rendus inutiles de ces composants. Seuls les composants qui utilisent une partie de l'état global se re-rendent lorsque l'état change, ce qui est un comportement souhaité.

## Ce que vous apprendrez ici

Dans ce tutoriel, vous apprendrez comment configurer votre propre application React alimentée par Redux. Nous créerons une application React et configurerons Redux pour pouvoir gérer l'état globalement afin que n'importe quel composant puisse accéder à n'importe quelle partie de l'état (d'où le nom d'application React alimentée par Redux). Certaines des autres alternatives à Redux que l'on peut essayer sont MobX, Zustand, etc., mais pour cet article, nous utiliserons Redux.

Nous verrons comment créer le store et le connecter à l'application. Nous verrons également comment écrire des actions et les dispatcher lors des interactions utilisateur. Ensuite, nous verrons comment créer des reducers et mettre à jour le store, lire le store depuis d'autres composants qui sont des enfants de App, et bien plus encore. 

Je fournirai également tous les extraits de code importants en cours de route afin que vous puissiez rapidement lancer l'application pendant que vous lisez et codez.

Pour vous donner un aperçu dès le début, voici ce que nous construirons à la fin :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/finalAppDemo.gif)

Nous créerons une application de base où nous pourrons ajouter et supprimer des articles dans un panier. Nous gérerons les changements d'état dans le store Redux et afficherons les informations dans l'interface utilisateur.

## Avant de commencer

Avant de procéder à ce tutoriel, vous devriez être familier avec le store Redux, les actions et les reducers.

Si ce n'est pas le cas, vous pouvez consulter mon dernier article que j'ai écrit sur Redux (si vous ne l'avez pas encore fait) : **[Qu'est-ce que Redux ? Store, Actions et Reducers expliqués pour les débutants](https://www.freecodecamp.org/news/what-is-redux-store-actions-reducers-explained/).** 

Cela vous aidera à comprendre l'article actuel. Dans ce tutoriel précédent, j'ai essayé d'expliquer les principes/concepts fondamentaux de Redux. J'ai couvert ce qu'est le store, ce que sont les actions et comment fonctionnent les reducers. Je discute également de ce qui rend Redux prévisible avec un exemple.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/despicable-me-minions.gif)

## Configuration initiale du code

Mettons en place tout ce dont nous avons besoin pour notre projet. Suivez simplement ces étapes et vous serez opérationnel en un rien de temps.

### 1. Créer une application React avec la commande create-react-app

```node
npx create-react-app react-app-with-redux
```

### 2. Aller dans le dossier nouvellement créé

Tapez simplement cette commande pour naviguer vers le nouveau dossier :

```shell
cd react-app-with-redux
```

### 3. Installer Redux et les bibliothèques react-redux 

Vous pouvez installer Redux et react-redux comme ceci :

```node
npm install redux react-redux
``` 

### 4. Exécuter l'application

Vous pouvez exécuter votre nouvelle application avec la commande suivante :

```node
npm start
```

## Comment construire l'application principale

### 5. Comment créer le Reducer

Pour créer un reducer, créez d'abord un dossier à l'intérieur de `src` nommé `actionTypes`. Ensuite, créez un fichier à l'intérieur nommé `actionTypes.js`. Ce fichier contiendra toutes les **actions** que l'application traitera.

Ajoutez les lignes suivantes dans `actionTypes.js` :

```js
export const ADD_ITEM = "ADD_ITEM";
export const DELETE_ITEM = "DELETE_ITEM";
```

Puisque notre application aura la fonctionnalité d'ajouter et de supprimer des articles, nous avons besoin des deux types d'actions ci-dessus.

Ensuite, créez un dossier à l'intérieur de `src` appelé `reducers` et créez un nouveau fichier nommé `cartReducer.js`. Ce fichier contiendra toute la logique du reducer liée au composant **cart**. 

**Note** : Nous créerons la vue/UI à l'étape 8, alors restez à l'écoute pour cela.

Ajoutez les lignes suivantes dans `cartReducer.js` :

```js
import { ADD_ITEM, DELETE_ITEM } from "../actionTypes/actionTypes";

const initialState = {
  numOfItems: 0,
};

export default const cartReducer = (state = initialState, action) => {
  switch (action.type) {
    case ADD_ITEM:
      return {
        ...state,
        numOfItems: state.numOfItems + 1,
      };

    case DELETE_ITEM:
      return {
        ...state,
        numOfItems: state.numOfItems - 1,
      };
    default:
      return state;
  }
};

```

Comme nous l'avons discuté dans [mon tutoriel précédent](https://www.freecodecamp.org/news/what-is-redux-store-actions-reducers-explained/), nous avons créé un **état initial** pour l'application et l'avons assigné au paramètre par défaut de `state` dans la fonction `cartReducer`. 

Cette fonction bascule sur le **type d'action** dispatché. Ensuite, en fonction du cas qui correspond au type d'action, elle apporte les modifications nécessaires à l'état et retourne une nouvelle instance fraîche de l'état mis à jour. 

Si aucun des types d'action ne correspond, alors l'état est retourné tel quel. 

Enfin, nous faisons une **exportation par défaut** de la fonction `cakeReducer` pour l'utiliser dans le processus de création du store.

### 6. Comment créer le store et le fournir à l'application

Créez un fichier à l'intérieur de `src` avec le nom `store.js` et créez le store en utilisant cette commande :

```js
const store = createStore()
```

Ajoutez les lignes suivantes dans `store.js` :

```js
import { createStore } from "redux";
import { cartReducer } from "./reducers/cartReducer";

const store = createStore(cartReducer);

export default store;
```

Il est maintenant temps de fournir ce `store` au composant `App`. Pour cela, nous utiliserons la balise `<Provider>` que nous obtenons de la bibliothèque `react-redux`. 

Nous enveloppons tout le composant `App` à l'intérieur de la balise `<Provider>` en utilisant la syntaxe suivante :

```jsx
// reste du code ...

<Provider store={store}>
        <div>Composant App</div>
        // composants enfants de App/ autre logique
</Provider>

// reste du code ...
```

En enveloppant le composant `App` à l'intérieur de la balise `<Provider>`, tous les composants enfants de `App` auront accès au `store`. Vous pouvez lire mon article précédent sur [Qu'est-ce que Redux ? Store, Actions et Reducers expliqués pour les débutants](https://www.freecodecamp.org/news/what-is-redux-store-actions-reducers-explained/) pour en savoir plus.

En continuant avec `App.js`, ajoutez les lignes suivantes au fichier :

```jsx
import "./App.css";
import { Provider } from "react-redux";
import store from "./store";

function App() {
  return (
    <Provider store={store}>
      <div>Composant App</div>
    </Provider>
  );
}

export default App;
```

### 7. Créer les Actions

Maintenant, créez un dossier à l'intérieur de `src` appelé `actions` et créez un fichier à l'intérieur appelé `cartAction.js`. Ici, nous ajouterons toutes les actions à **dispatch** sur certaines interactions utilisateur. 

Ajoutez les lignes suivantes dans le fichier `cartAction.js` :

```js
import { ADD_ITEM, DELETE_ITEM } from "../actionTypes/actionTypes";

const addItem = () => {
  return {
    type: ADD_ITEM,
  };
};

const deleteItem = () => {
  return {
    type: DELETE_ITEM,
  };
};

export { addItem, deleteItem };
```

Dans le code ci-dessus, nous avons créé deux créateurs d'actions (fonctions JS pures qui retournent un objet `action`) appelés `addItem()` et `deleteItem()`. Les deux créateurs d'actions retournent des objets `action` avec un `type` spécifique. 

**Note** : Chaque objet `action` doit avoir une valeur `type` unique. Avec cela, toute donnée supplémentaire passée avec l'objet action est optionnelle et dépendra de la logique utilisée pour mettre à jour l'`état`.

### 8. Comment créer la vue/UI

Maintenant que nous avons créé toutes les entités requises telles que le store, les actions et les Reducers, il est temps de créer les éléments UI. 

Créez un dossier `component` à l'intérieur de `src` et un fichier `Cart.js` à l'intérieur. Ajoutez les lignes suivantes à l'intérieur de `Cart.js` :

```jsx
import React from "react";

const Cart = () => {
  return (
    <div className="cart">
      <h2>Nombre d'articles dans le panier :</h2>
      <button className="green">Ajouter un article au panier</button>
      <button className="red">Retirer un article du panier</button>
    </div>
  );
};

export default Cart;
```

Ajoutez ce composant `Cart` dans le fichier `App.js` :

```jsx
import "./App.css";
import { Provider } from "react-redux";
import store from "./store";
import Cart from "./component/Cart";

function App() {
  return (
    <Provider store={store}>
      <Cart />
    </Provider>
  );
}

export default App;
```

Juste pour le rendre un peu plus présentable, j'ai ajouté un peu de style de base dans `App.css` comme suit :

```css
button {
  margin: 10px;
  font-size: 16px;
  letter-spacing: 2px;
  font-weight: 400;
  color: #fff;
  padding: 23px 50px;
  text-align: center;
  display: inline-block;
  text-decoration: none;
  border: 0px;
  cursor: pointer;
}
.green {
  background-color: rgb(6, 172, 0);
}
.red {
  background-color: rgb(221, 52, 66);
}
.red:disabled {
  background-color: rgb(193, 191, 191);
  cursor: not-allowed;
}
.cart {
  text-align: center;
}
```

Voici à quoi ressemble l'interface utilisateur pour l'instant :


![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot-2022-05-20-at-20.01.01.png)

### 9. Comment lire et accéder au store en utilisant le hook `useSelector`

`useSelector` est un hook fourni par la bibliothèque **react-redux** qui nous aide à lire le `store` et son contenu. 

Importez le hook depuis `react-redux` et utilisez la syntaxe suivante pour lire le store avec le hook `useSelector` :

```jsx
import { useSelector } from "react-redux";
// reste du code
const state = useSelector((state) => state);

// reste du code
```

Après avoir ajouté le hook `useSelector`, votre fichier `Cart.js` ressemblera à quelque chose comme ceci :

```jsx
import React from "react";
import { useSelector } from "react-redux";

const Cart = () => {
  const state = useSelector((state) => state);
  console.log("store", state);
  return (
    <div className="cart">
      <h2>Nombre d'articles dans le panier :</h2>
      <button className="green">Ajouter un article au panier</button>
      <button className="red">Retirer un article du panier</button>
    </div>
  );
};

export default Cart;
```

Le journal de la console de l'état nous donnera l'état initial que nous avons défini dans le fichier reducer à l'étape 5.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot-2022-05-21-at-01.10.28.png)

### 10. Comment dispatcher une action au clic sur un bouton avec le hook `useDispatch`

La bibliothèque react-redux nous donne un autre hook appelé le hook `useDispatch`. Il nous aide à dispatcher les actions ou les créateurs d'actions qui, à leur tour, retournent des actions. La syntaxe est la suivante :

```jsx
const dispatch = useDispatch();

dispatch(actionObject ou appel du créateur d'action);
```

Ainsi, l'ajout d'un dispatcher dans notre `Cart.js` fera finalement ressembler le fichier à quelque chose comme ceci :

```jsx
import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { addItem, deleteItem } from "../actions/cartAction";

const Cart = () => {
  const state = useSelector((state) => state);
  const dispatch = useDispatch();
  return (
    <div className="cart">
      <h2>Nombre d'articles dans le panier : {state.numOfItems}</h2>
      <button
        onClick={() => {
          dispatch(addItem());
        }}
      >
        Ajouter un article au panier
      </button>
      <button
        disabled={state.numOfItems > 0 ? false : true}
        onClick={() => {
          dispatch(deleteItem());
        }}
      >
        Retirer un article du panier
      </button>
    </div>
  );
};

export default Cart;
```

Remarquez comment, au clic sur le bouton **Ajouter un article au panier**, nous `dispatchons` le créateur d'action `addItem()` que nous avons créé à l'étape n° 7. 

De même, au clic sur le bouton **Retirer un article du panier**, nous dispatchons le créateur d'action avec `deleteItem()`. 

La variable `state` stocke l'état de l'application, qui est essentiellement un objet avec une clé `numOfItems`. Donc `state.numOfItems` nous donne la valeur actuelle du nombre d'articles dans le store. 

Nous affichons cette information dans la vue dans la ligne `<h2>Nombre d'articles dans le panier : {state.numOfItems}</h2>`. 

Pour approfondir un peu, lorsqu'un utilisateur clique sur le bouton Ajouter un article au panier, il dispache le créateur d'action `addItem()`. Cela, à son tour, retourne un objet `action` avec le type `type: ADD_ITEM`. 

Comme mentionné dans [mon tutoriel précédent](https://www.freecodecamp.org/news/what-is-redux-store-actions-reducers-explained/), lorsqu'une action est dispatchée, tous les reducers deviennent actifs. 

Actuellement dans cet exemple, nous n'avons qu'un seul reducer – `cartReducer`. Il devient donc actif et écoute l'`action` dispatchée. 

Comme montré à l'étape 5, le reducer prend l'état et l'action en entrée, bascule sur le `type d'action` et **retourne la nouvelle instance fraîche de l'état mis à jour**. 

Dans cet exemple, lorsque l'action avec `type: ADD_ITEM` correspond au premier cas de commutation, elle fait d'abord une copie de tout l'état en utilisant l'opérateur de propagation `...state`. Ensuite, elle fait la mise à jour nécessaire – qui, dans le cas de l'ajout d'articles, est `numOfItems: state.numOfItems + 1` (c'est-à-dire augmenter le `numOfItems` de 1). 

De même, en utilisant la même logique, en cliquant sur le bouton Retirer un article du panier, une action avec le type `type: DELETE_ITEM` est dispatchée, ce qui diminue le `numOfItems` de 1. 

Voici la démonstration de l'application fonctionnelle :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/finalAppDemo-1.gif)

Remarquez comment nous avons pu contrôler le comportement du bouton Retirer un article du panier en fonction de la valeur de `numOfItems` dans le store Redux. Comme un nombre négatif d'articles n'a pas de sens, nous avons désactivé le bouton Retirer un article du panier si `state.numOfItems <= 0`. 

De cette manière, nous sommes en mesure d'empêcher l'utilisateur de diminuer le nombre d'articles dans le panier s'il est déjà à 0. 

C'était un exemple de base pour vous montrer comment nous pouvons **contrôler le comportement de divers éléments DOM** en fonction de l'état interne de l'application. 

Et voilà ! Nous venons de terminer la configuration de notre première application React alimentée par Redux. Vous pouvez maintenant créer divers autres composants en fonction de vos besoins et partager un état global commun entre eux.

## Dépôt GitHub

Voici le dépôt GitHub du projet afin que vous puissiez examiner le code source complet si vous le souhaitez : [Dépôt GitHub](https://github.com/sohamderoy/blog-setup-react-app-with-redux/tree/master)


## Résumé

Dans cet article, nous avons appris comment rapidement configurer une application React alimentée par Redux. 

En cours de route, nous avons appris comment :

- Créer des actions, des créateurs d'actions, des reducers et le store
- Fournir le store à l'application en utilisant `<Provider>`
- Lire/accéder au store depuis les composants en utilisant le hook `useSelector` et afficher les informations d'état dans l'UI
- Dispatcher les actions sur des événements utilisateur tels que des clics sur des boutons, en utilisant le hook `useDispatch`
- Contrôler le comportement des éléments DOM avec une logique basée sur l'état de l'application
- Nous avons appris quels sont les inconvénients d'une gestion d'état inefficace et de multiples niveaux de prop drilling

## Ressources supplémentaires

Voici quelques ressources supplémentaires que vous pouvez consulter pour en savoir plus sur Redux

- [Qu'est-ce que Redux ? Store, Actions et Reducers expliqués pour les débutants](https://www.freecodecamp.org/news/what-is-redux-store-actions-reducers-explained/)
- [Documentation officielle de Redux](https://redux.js.org/introduction/getting-started)


## Conclusion

Merci d'avoir lu ! J'espère vraiment que vous avez apprécié lire comment configurer une application React alimentée par Redux et que vous avez trouvé ce tutoriel utile.

N'hésitez pas à le partager avec vos amis, car j'apprécierais vraiment cela. Suivez-moi sur LinkedIn et Twitter et restez à l'écoute pour plus de contenu incroyable ! Paix ! 🖖

### Liens sociaux

- [LinkedIn](https://www.linkedin.com/feed/)
- [Site Web](https://www.sohamderoy.dev/)
- [Autres blogs de moi](https://blogs.sohamderoy.dev)
- [Twitter](https://twitter.com/_sohamderoy)