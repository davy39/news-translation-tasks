---
title: Redux pour les débutants – Apprenez les bases de Redux avec des exemples de
  code
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-05-18T16:18:18.000Z'
originalURL: https://freecodecamp.org/news/redux-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/pexels-philipp-birmes-830891.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
seo_title: Redux pour les débutants – Apprenez les bases de Redux avec des exemples
  de code
seo_desc: 'Redux can be confusing for beginner React developers to understand. There
  are a lot of concepts you need to know to use it properly, like reducers, actions,
  store, pure functions, immutability, and much more.

  But every React developer should know the...'
---

Redux peut être déroutant à comprendre pour les développeurs React débutants. Il y a beaucoup de concepts que vous devez connaître pour l'utiliser correctement, comme les reducers, les actions, le store, les fonctions pures, l'immutabilité, et bien plus encore.

Mais chaque développeur React devrait connaître les bases du fonctionnement de Redux, car les projets industriels utilisent souvent Redux pour gérer des projets de plus grande envergure.

Ainsi, dans cet article, nous explorerons les bases de Redux et comment l'utiliser.

Voici un aperçu de l'application que nous allons construire dans cet article. C'est un excellent projet que vous pouvez ajouter à votre portfolio et à votre CV.

<iframe width="800" height="500" src="https://www.youtube.com/embed/izSw74H08Bc?mute=1"></iframe>

## Qu'est-ce que Redux ?

Redux est une bibliothèque de gestion d'état (state management) qui vous aide à mieux gérer l'état dans vos applications.

La bibliothèque Redux n'est pas spécifique à React. C'est une bibliothèque que vous pouvez utiliser dans n'importe quelle autre bibliothèque ou Framework comme Angular, Vue, et même en vanilla JavaScript.

Mais les développeurs utilisent principalement Redux lorsqu'ils travaillent avec React.

Redux fournit un store unique que vous pouvez utiliser pour gérer une grande quantité de données.

## Comment débuter avec Redux

Créons un nouveau projet React afin d'apprendre les bases de Redux.

Exécutez la commande suivante dans le terminal/invite de commande pour créer un nouveau projet React en utilisant create-react-app :

```js
npx create-react-app redux-demo

```

> `npx` dans ce cas nous permet d'utiliser le package npm `create-react-app` pour créer un nouveau projet React sans l'installer sur notre machine locale.

Une fois le projet créé, supprimez tous les fichiers du dossier `src` et créez un nouveau fichier `index.js` à l'intérieur du dossier `src`.

Maintenant, ouvrez à nouveau le terminal et exécutez la commande suivante depuis le dossier `redux-demo` :

```js
npm install redux@4.1.0

```

La commande ci-dessus installera la bibliothèque Redux avec la version `4.1.0` pour l'utiliser dans votre projet (qui est la dernière version au moment de la rédaction de cet article).

## Comment créer le store Redux

Dans Redux, vous utilisez le store pour gérer et suivre les données qui changent dans l'application.

Pour créer un store, nous devons importer la fonction `createStore` comme ceci :

```js
import { createStore } from 'redux';

```

La fonction `createStore` accepte trois arguments :

* le premier argument est une fonction qui est normalement connue sous le nom de reducer (obligatoire)
* le deuxième argument est la valeur initiale de l'état (optionnel)
* le troisième argument est un enhancer où nous pouvons passer un middleware, le cas échéant (optionnel)

Jetez un œil au code ci-dessous :

```js
import { createStore } from 'redux';

const reducer = (state, action) => {
  console.log('reducer called');
  return state;
};

const store = createStore(reducer, 0);

```

Ici, nous avons d'abord défini une fonction reducer en utilisant la syntaxe des fonctions fléchées ES6. Vous pouvez utiliser une fonction normale au lieu de la fonction fléchée si vous le souhaitez.

À l'intérieur de la fonction reducer, nous logguons du texte dans la console, puis nous retournons la valeur de l'état depuis la fonction.

Ensuite, nous passons cette fonction reducer à la fonction `createStore` comme premier argument et `0` comme valeur initiale de l'état comme deuxième argument.

La fonction `createStore` retourne un store que nous pouvons utiliser pour gérer les données de l'application.

La fonction reducer reçoit state et action comme paramètres.

La valeur initiale de l'état que nous avons passée comme `0` pour la fonction `createStore` est automatiquement passée comme valeur du paramètre `state`.

Mais il est bien plus courant d'initialiser l'état à l'intérieur du reducer lui-même plutôt que de le passer comme second argument à la fonction `createStore` comme ceci :

```js
import { createStore } from 'redux';

const reducer = (state = 0, action) => {
  console.log('reducer called');
  return state;
};

const store = createStore(reducer);

```

Ici, nous utilisons la syntaxe des paramètres par défaut ES6 pour initialiser le paramètre state à la valeur `0`.

Une fois le store créé, nous pouvons utiliser la méthode `subscribe` fournie par le store pour nous abonner aux changements du store comme indiqué ci-dessous :

```js
store.subscribe(() => {
  console.log('current state', store.getState());
});

```

Ici, en utilisant la fonction `subscribe`, nous enregistrons une fonction de rappel (callback) qui sera appelée une fois que le store aura changé.

Et à l'intérieur de la fonction de rappel, nous appelons la méthode `store.getState` pour obtenir la valeur actuelle de l'état.

Maintenant, ouvrez le fichier `src/index.js` et ajoutez-y le contenu suivant :

```js
import { createStore } from 'redux';

const reducer = (state = 0, action) => {
  console.log('reducer called');
  return state;
};

const store = createStore(reducer);

store.subscribe(() => {
  console.log('current state', store.getState());
});

```

Maintenant, si vous lancez l'application en exécutant la commande `npm start` depuis le terminal et que vous accédez à [http://localhost:3000/](http://localhost:3000/), vous verrez le message `reducer called` affiché dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/reducer_log.png)

C'est parce que le reducer est appelé immédiatement une fois que nous le passons à la fonction `createStore`.

## Comment modifier le store

Nous avons maintenant terminé la création du store. Mais le store ne nous est pas d'une grande utilité pour le moment. En effet, le store est connecté via la fonction reducer, mais nous n'avons ajouté aucun code à l'intérieur du reducer pour gérer le store. Faisons donc cela.

**La seule façon de modifier le store est de dispatcher des actions.**

Une action est un objet envoyé au store comme ceci :

```js
store.dispatch({
  type: 'INCREMENT'
})

```

Ici, nous appelons la fonction dispatch disponible sur le `store` pour envoyer une action avec le type `INCREMENT` au store.

La fonction dispatch prend un objet en paramètre qui est connu sous le nom d'action.

L'action doit avoir une propriété `type` comme indiqué ci-dessus. Si vous ne passez pas la propriété `type`, vous obtiendrez une erreur.

> Il est courant et recommandé de spécifier la valeur `type` en majuscules.

Le type peut être n'importe quelle opération que vous souhaitez effectuer, comme `ADD_USER`, `DELETE_RECORD`, `GET_USERS`, etc.

Si vous avez plusieurs mots, vous pouvez les séparer par des underscores comme ceci : `{ type: 'INCREMENT_NUMBER' }`.

Maintenant, ouvrez le fichier `index.js` et remplacez son contenu par le code suivant :

```js
import { createStore } from 'redux';

const reducer = (state = 0, action) => {
  if (action.type === 'INCREMENT') {
    return state + 1;
  } else if (action.type === 'DECREMENT') {
    return state - 1;
  }

  return state;
};

const store = createStore(reducer);

store.subscribe(() => {
  console.log('current state', store.getState());
});

store.dispatch({
  type: 'INCREMENT'
});

store.dispatch({
  type: 'INCREMENT'
});

store.dispatch({
  type: 'DECREMENT'
});

```

Maintenant, si vous lancez l'application en exécutant la commande `npm start` depuis le terminal, vous verrez les logs suivants affichés dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/changing_store-1.png)

Comme vous pouvez le voir, pour chaque action dispatchée vers le store, le store est modifié. Nous sommes donc en mesure de voir les différentes valeurs de l'état dans la console.

Dans le code ci-dessus, notre fonction reducer ressemble à ceci :

```js
const reducer = (state = 0, action) => {
  if (action.type === 'INCREMENT') {
    return state + 1;
  } else if (action.type === 'DECREMENT') {
    return state - 1;
  }

  return state;
};

```

Chaque fois que nous appelons la fonction `store.dispatch`, la fonction reducer sera appelée. Tout ce qui est retourné par le reducer deviendra la nouvelle valeur du store.

Ainsi, la première fois que nous dispatchons une action vers le store comme ceci :

```js
store.dispatch({
  type: 'INCREMENT'
});

```

la première condition if à l'intérieur de la fonction reducer sera exécutée. Elle incrémentera la valeur de `state` à `1`, qui était initialement initialisée à `0` en utilisant la syntaxe des paramètres par défaut ES6. Ensuite, elle sera retournée par la fonction reducer.

**Notez que nous utilisons la valeur de `state` pour calculer la nouvelle valeur et que nous ne modifions pas la valeur originale de `state` comme ceci :**

```js
if (action.type === 'INCREMENT') {
   state = state + 1;
   return state;
} 

```

Le code ci-dessus n'est donc pas correct, car dans le reducer, nous ne devrions pas modifier l'état original. Cela créerait des problèmes dans votre application et n'est donc pas recommandé.

Et parce que nous avons ajouté la fonction `store.subscribe` dans le fichier `index.js`, nous sommes informés du changement du store comme nous pouvons le voir dans les logs de la console.

Ainsi, lorsque nous appelons à nouveau le dispatch avec le type `INCREMENT`, la première condition if sera à nouveau exécutée. Elle ajoutera donc 1 à la valeur de l'état précédent qui était 1, et la valeur finale de l'état deviendra 2.

Ensuite, nous dispatchons l'action `DECREMENT` vers le store comme ceci :

```js
store.dispatch({
  type: 'DECREMENT'
});

```

ce qui exécutera la condition else à l'intérieur du reducer et décrémentera la valeur de l'état de 1 (ainsi 2 - 1 deviendra 1).

Notez que, à l'intérieur du reducer, nous retournons également l'état à la fin. Ainsi, si aucune des conditions ne correspond, l'état précédent par défaut sera retourné par la fonction.

Il est courant d'utiliser une instruction switch à l'intérieur du reducer au lieu de la condition if-else comme ceci :

```js
const reducer = (state = 0, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return state + 1;
    case 'DECREMENT':
      return state - 1;
    default:
      return state;
  }
};

```

En plus du type, nous pouvons également passer des informations supplémentaires dans le cadre de l'action.

Remplacez le contenu du fichier `index.js` par le code suivant :

```js
import { createStore } from 'redux';

const reducer = (state = 0, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return state + action.payload;
    case 'DECREMENT':
      return state - action.payload;
    default:
      return state;
  }
};

const store = createStore(reducer);

store.subscribe(() => {
  console.log('current state', store.getState());
});

store.dispatch({
  type: 'INCREMENT',
  payload: 1
});

store.dispatch({
  type: 'INCREMENT',
  payload: 5
});

store.dispatch({
  type: 'DECREMENT',
  payload: 2
});

```

Maintenant, si vous lancez l'application en exécutant la commande `npm start` depuis le terminal, vous verrez les logs suivants affichés dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/with_payload-1.png)

Ici, tout en dispatchant une action vers le store, nous passons un `payload` avec une certaine valeur que nous utilisons à l'intérieur du reducer pour incrémenter ou décrémenter la valeur du store.

Ici, nous avons utilisé `payload` comme nom de propriété, mais vous pouvez le nommer comme vous le souhaitez.

Notre fonction reducer ressemble maintenant à ceci :

```js
const reducer = (state = 0, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return state + action.payload;
    case 'DECREMENT':
      return state - action.payload;
    default:
      return state;
  }
};

```

Ainsi, lorsque nous dispatchons des actions avec le type `INCREMENT` comme ceci :

```js
store.dispatch({
  type: 'INCREMENT',
  payload: 1
});

store.dispatch({
  type: 'INCREMENT',
  payload: 5
});

```

le code suivant du reducer sera exécuté :

```js
return state + action.payload;

```

Cela ajoutera d'abord 1 puis 5 à la valeur précédente de l'état, nous passons donc de 1 à 6. Et à cause du type d'action `DECREMENT` :

```js
store.dispatch({
  type: 'DECREMENT',
  payload: 2
});

```

nous passons de 6 à 4. La valeur finale du store deviendra donc 4.

Voici une [démo Code Sandbox](https://codesandbox.io/s/goofy-hooks-y1w9s?file=/src/index.js).

## Merci de m'avoir lu !

C'était une introduction rapide à Redux tirée de mon cours [Mastering Redux](https://master-redux.yogeshchavan.dev/). Si vous voulez apprendre Redux en détail et construire une application complète de commande de nourriture, vous pouvez y jeter un œil.

Dans ce cours, vous apprendrez :

* Redux de base et avancé
* Comment gérer l'état complexe des tableaux et des objets
* Comment utiliser plusieurs reducers pour gérer un état Redux complexe
* Comment déboguer une application Redux
* Comment utiliser Redux dans React en utilisant la bibliothèque react-redux pour rendre votre application réactive.
* Comment utiliser la bibliothèque redux-thunk pour gérer les appels API asynchrones 

et bien plus encore.

Enfin, nous construirons une [application complète de commande de nourriture](https://www.youtube.com/watch?v=izSw74H08Bc) à partir de zéro avec l'intégration Stripe pour accepter les paiements et nous la déploierons en production.

Vous pouvez obtenir le cours pour seulement 12 $ au lieu du prix original de 19 $, accompagné d'un exemplaire gratuit de mon livre populaire [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/) si vous l'achetez avant le 19 mai 2021.

Vous voulez rester à jour avec du contenu régulier concernant JavaScript, React, Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).