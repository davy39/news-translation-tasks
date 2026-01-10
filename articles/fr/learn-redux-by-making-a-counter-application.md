---
title: Apprendre Redux en créant une application de compteur
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-06-21T21:01:42.000Z'
originalURL: https://freecodecamp.org/news/learn-redux-by-making-a-counter-application
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/reduxpic.png
tags:
- name: React
  slug: react
- name: Redux
  slug: redux
seo_title: Apprendre Redux en créant une application de compteur
seo_desc: Redux is a state management library for front end applications. Developers
  commonly use it with React through the react-redux package, but it can also stand
  alone – so you can use it in any front end framework or library, including Vanilla
  JavaScript...
---

Redux est une bibliothèque de gestion d'état pour les applications front-end. Les développeurs l'utilisent couramment avec React via le package react-redux, mais elle peut également fonctionner seule – vous pouvez donc l'utiliser dans n'importe quel framework ou bibliothèque front-end, y compris Vanilla JavaScript.

Redux peut vraiment être intimidant au premier abord. Il peut vous falloir un certain temps pour vous y habituer et vous pourriez finir par consulter vos projets précédents pour comprendre comment faire les choses. 

Redux est également souvent critiqué car il nécessite beaucoup de code standardisé pour gérer l'état de l'application. Et c'est vrai – utiliser Redux dans de petites applications, c'est comme tirer sur une fourmi avec un canon. Il existe des solutions de contournement que vous pouvez utiliser dans React, par exemple, comme le prop drilling et le contexte, tandis que Vue JS a VueX et Angular a NGRX.

Dans une application React, le principal problème que Redux résout est que, au lieu de gérer l'état de l'application en passant des props (ce qui est unidirectionnel), l'état entier est enregistré dans un store globalisé. Cela vous donne la possibilité de l'utiliser partout où vous en avez besoin. C'est donc assez multidimensionnel !

Dans cet article, je vous apprendrai à créer une application de compteur avec Redux dans une application React, afin que vous ayez suffisamment de connaissances de base pour commencer à utiliser Redux dans vos projets.

## Comment installer le projet

Tout d'abord, vous devez installer les packages redux et react-redux depuis NPM en exécutant la commande ```npm i redux react-redux```. Redux est autonome et react-redux nous donne accès à plusieurs hooks qui facilitent la vie.

## Comment créer les dossiers et fichiers
Ensuite, nous devons créer les actions et les reducers. Les actions sont ce que leur nom implique – ce sont des objets qui déterminent ce qui sera fait. Les reducers, en revanche, vérifient quelle action est effectuée et mettent à jour l'état en fonction de l'action. Ils prennent l'état et l'action. 

J'aime créer les deux dans un dossier actions et un dossier reducers, puis je les mets dans un dossier que je nomme `Redux` pour plus de clarté. 

Dans le dossier reducers, je crée un fichier nommé `counterReducer.js`. Beaucoup de gens créent généralement le reducer avec une instruction switch, mais il est également possible d'utiliser une instruction if. Dans cet exemple, je vais utiliser switch. 

Donc, dans le reducer de compteur, je vais mettre le snippet de code suivant :

```js
const counterReducer = (state = 1, action) => {
  switch (action.type) {
    case "INCREMENT":
      return state + 1;
    case "DECREMENT":
      return state - 1;
    case "RESET":
      return (state = 0);
    default:
      return state;
  }
};
export default counterReducer;
```

Ici, j'ai codé en dur l'état à 1. Vous pouvez commencer à 0 si vous le souhaitez. 

Dans l'instruction switch, j'ai un cas `INCREMENT` qui augmentera le compteur de 1, `DECREMENT` pour diminuer le compteur de 1, et `RESET` pour réinitialiser le compteur à un état de 0. 

Il est conventionnel d'utiliser le type en majuscules dans les cas, mais vous n'êtes pas obligé – utilisez le cas que vous préférez. Mais vous devez exporter le reducer de compteur afin de pouvoir l'utiliser dans un autre fichier.

## Comment ajouter une authentification factice au projet
Je vais aller un peu plus loin en ajoutant une authentification factice à l'application de compteur. Là, je vais vous montrer un secret sur moi. Donc, en plus du `counterReducer`, je vais également créer un `authReducer` où je vais coller le code suivant :

```javascript
const authReducer = (state = false, action) => {
  switch (action.type) {
    case "LOG_IN":
      return true;
    case "LOG_OUT":
      return false;
    default:
      return state;
  }
};
export default authReducer;
```

Dans le `authReducer`, l'état est initialisé à false. `LOG_IN` le définira à true et `LOG_OUT` le ramènera à false pour compléter l'action de bascule.

## Comment utiliser la fonction d'assistance `combineReducer`
Puisque nous avons plus d'un reducer, nous devons importer la fonction d'assistance `combineReducer` de Redux. Cette fonction transforme nos reducers en un seul reducer que nous pouvons passer à l'API `createStore`. Ne vous inquiétez pas de ce qu'est l'API `createStore` pour l'instant – je vais l'expliquer bientôt. 

Donc, nous passons les reducers comme ceci : 
```combineReducer({reducer-a, reducer-b, reducer-c})```

Dans le dossier reducer, nous devons créer un autre fichier nommé `index` afin que nous puissions importer la fonction d'assistance `combineReducer`, ainsi que les reducers, et les combiner à l'intérieur. 

Dans le fichier index, j'ai le code suivant :

```js
import counter from "./counter";
import auth from "./auth";
import { combineReducers } from "redux";

const allReducers = combineReducers({
  counter,
  auth,
});
export default allReducers;
```

## Comment créer le store global
La prochaine chose à faire est de créer un store. J'aime le créer dans le fichier `index` de React. 

Pour ce faire, vous devez importer l'API `createStore` de Redux comme ceci : ```import { createStore } from "redux";```. 

Nous devons également importer nos reducers qui ont déjà été combinés, puis créer le store dans leur instance. 

Pour donner vie à la fonctionnalité de notre application de compteur, nous devons connecter tout ce que nous avons fait avec Redux à l'application. 

Tout d'abord, nous devons importer `Provider` depuis react-redux et l'envelopper autour de l'application entière dans notre fichier index. Le provider connecte l'état global à l'application. `Provider` prend un argument appelé store dans lequel nous devons passer le store créé. 

Dans le fichier index, j'ai maintenant les snippets de code suivants :

```js
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import { createStore } from "redux";
import allReducers from "./redux/reducers";
import { Provider } from "react-redux";

//Le store créé
const store = createStore(
  allReducers,
);
ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById("root")
);
```

## Comment extraire les reducers et configurer les actions
La prochaine étape consiste à extraire le `counterReducer` en important `useSelector` depuis `react-redux` afin que nous puissions accéder à l'état entier. 

Pour voir le secret que j'ai dit que je vais vous montrer sur moi, nous devons également extraire `authReducer`. Je vais faire cela dans le fichier app.js :

```
import { useSelector } from "react-redux";
```

Pour commencer à incrémenter et décrémenter, et également se connecter et se déconnecter, nous devons retourner dans le dossier des actions, configurer les actions à dispatcher dans l'application, et les exporter également. Dispatch est la fonction qui aide à rendre nos actions réelles. 

Donc, dans le fichier index du dossier des actions, j'ai le code ci-dessous :

```js
export const increment = () => {
  return {
    type: "INCREMENT",
  };
};

export const decrement = () => {
  return {
    type: "DECREMENT",
  };
};

export const reset = () => {
  return {
    type: "RESET",
  };
};

export const logIn = () => {
  return {
    type: "LOG_IN",
  };
};

export const logOut = () => {
  return {
    type: "LOG_OUT",
  };
};

```

## Comment importer et dispatcher les actions
Rappelons que j'ai défini les actions `INCREMENT`, `DECREMENT`, `RESET`, `LOG_IN` et `LOG_OUT` dans les fichiers des reducers. Nous devons les importer dans les actions de la même manière. L'identifiant de l'objet peut être dans n'importe quel cas.

Cela signifie que nous devons importer les actions que nous avons configurées, ainsi que le hook `useDispatch` depuis react-redux, afin que nous puissions dispatcher n'importe quelle action que nous voulons.

```
import { useDispatch } from "react-redux";

```

Puisque nous pouvons utiliser le hook `useDispatch` et tout le reste maintenant, nous devons configurer les boutons d'incrémentation, de décrémentation, de réinitialisation, et de connexion/déconnexion.

À l'intérieur de nos boutons, nous devons configurer un gestionnaire d'événements de clic pour mettre le dispatch. Le code complet dans le fichier ap.js ressemble maintenant à ceci :

```js
import "./App.css";
import { useSelector, useDispatch } from "react-redux";
import {
  decrement,
  increment,
  reset,
  logIn,
  logOut,
} from "./redux/actions/index";

function App() {
  const counter = useSelector((state) => state.counter);
  const auth = useSelector((state) => state.auth);
  const dispatch = useDispatch();

  return (
    <div className="App">
      <h1>
         Bonjour le monde <br /> Un petit projet Redux. YaaY!
      </h1>
      <h3>Compteur</h3>
      <h3>{counter}</h3>
      <button onClick={() => dispatch(increment())}>Augmenter</button>
      <button onClick={() => dispatch(reset())}>Réinitialiser</button>
      <button onClick={() => dispatch(decrement())}>Diminuer</button>

      <h2>Pour les utilisateurs connectés uniquement</h2>
      <p>Connectez-vous pour voir un secret sur moi</p>
      <button onClick={() => dispatch(logIn())}>Connexion</button>
      <button onClick={() => dispatch(logOut())}>Déconnexion</button>
      {auth ? (
        <div>
          <p>
            Je ne connais pas plus de 50% de redux. Mais si vous en connaissez 50%, vous êtes comme un Superman.
          </p>
        </div>
      ) : (
        ""
      )}
    </div>
  );
}

export default App;
```

À la fin, voici ce que vous aurez :
![redux](https://www.freecodecamp.org/news/content/images/2021/06/redux.gif)

J'espère que vous pourrez trouver le secret sur moi.

## Conclusion

Merci d'avoir lu ce tutoriel. J'espère qu'il vous donne une compréhension de base de Redux afin que vous puissiez commencer à créer quelque chose avec par vous-même. 

Pour me contacter, suivez-moi sur [Twitter](http://twitter.com/koladechris), où je passe la plupart de mon temps à discuter de codage et de développement web.