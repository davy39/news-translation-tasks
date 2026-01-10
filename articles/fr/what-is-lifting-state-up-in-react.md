---
title: Qu'est-ce que la "remontée d'état" (Lifting State Up) dans React ?
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-05-06T21:41:34.000Z'
originalURL: https://freecodecamp.org/news/what-is-lifting-state-up-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/what-is-lifting-state-up-in-react.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Qu'est-ce que la "remontée d'état" (Lifting State Up) dans React ?
seo_desc: 'Here is a simple and practical example what it means to "lift state up"
  in React, and how it can help you build your applications.

  Lifting state up is a common pattern that is essential for React developers to know.
  It helps you avoid more complex (a...'
---

Voici un exemple simple et pratique de ce que signifie « faire remonter l'état » (lift state up) dans React, et comment cela peut vous aider à construire vos applications.

La remontée d'état est un modèle courant qu'il est essentiel pour les développeurs React de connaître. Cela vous aide à éviter des modèles plus complexes (et souvent inutiles) pour gérer votre état.

Comment fait-elle cela ? Voyons cela à travers un exemple simple.

%[https://www.youtube.com/watch?v=rdwc4JmX_fU]

## Analyse de notre application Todo

Commençons par une application de liste de tâches (todo) basique, qui se compose de trois composants : `TodoCount`, `TodoList`, et `AddTodo`. 

Tous ces composants, comme leur nom l'indique, vont avoir besoin de partager un état commun. 

Si vous regardez `TodoCount`, c'est là que vous allez afficher, tout en haut de votre application, le nombre total de tâches que vous avez dans votre application. 

`TodoList` sera l'endroit où vous afficherez toutes vos tâches. Il possède un état initial avec ces trois éléments (« élément 1 », « élément 2 », « élément 3 ») que vous afficherez dans une liste non ordonnée. 

Et enfin, vous avez `AddTodo`. Il s'agit d'un formulaire où vous voulez pouvoir ajouter un nouvel élément à cette liste. Pour l'instant, vous vous contentez de consigner dans la console la tâche que vous saisissez dans le champ de saisie :

```js
// src/App.js

import React from "react";

export default function App() {
  return (
    <>
      <TodoCount />
      <TodoList />
      <AddTodo />
    </>
  );
}

function TodoCount() {
  return <div>Total des tâches : </div>;
}

function TodoList() {
  const [todos, setTodos] = React.useState(["élément 1", "élément 2", "élément 3"]);

  return (
    <ul>
      {todos.map((todo) => (
        <li key={todo}>{todo}</li>
      ))}
    </ul>
  );
}

function AddTodo() {
  function handleSubmit(event) {
    event.preventDefault();
    const todo = event.target.elements.todo.value;
    console.log(todo);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" id="todo" />
      <button type="submit">Ajouter une tâche</button>
    </form>
  );
}
```

## Pourquoi devriez-vous vous soucier de la remontée d'état ?

Comment pouvez-vous utiliser le concept de remontée d'état pour aider à terminer votre application ?

Ces composants ont besoin de partager un certain état, l'état des tâches (todos). Vous devez partager cet état afin d'afficher le nombre de tâches ainsi que pour mettre à jour votre liste de tâches.

C'est là qu'intervient le concept de remontée d'état. 

> Nous faisons remonter l'état vers un ancêtre commun aux composants qui en ont besoin, afin qu'ils puissent tous partager cet état. Cela nous permet de partager plus facilement l'état entre tous ces composants qui en dépendent. 

Vers quel ancêtre commun devriez-vous faire remonter votre état pour que tous les composants puissent lire et mettre à jour cet état ? Le composant `App`.

Voici à quoi devrait maintenant ressembler votre application :

```js
// src/App.js

import React from "react";

export default function App() {
  const [todos, setTodos] = React.useState(["élément 1", "élément 2", "élément 3"]);    
    
  return (
    <>
      <TodoCount />
      <TodoList />
      <AddTodo />
    </>
  );
}

function TodoCount() {
  return <div>Total des tâches : </div>;
}

function TodoList() {
  return (
    <ul>
      {todos.map((todo) => (
        <li key={todo}>{todo}</li>
      ))}
    </ul>
  );
}

function AddTodo() {
  function handleSubmit(event) {
    event.preventDefault();
    const todo = event.target.elements.todo.value;
    console.log(todo);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" id="todo" />
      <button type="submit">Ajouter une tâche</button>
    </form>
  );
}
```

## Comment transmettre l'état vers le bas

Cependant, il y a un petit problème. 

`TodoList` n'a pas accès à la variable d'état `todos`, vous devez donc la transmettre depuis `App` :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screen-Shot-2021-05-05-at-12.29.41-AM.png)

Vous pouvez le faire avec les composants dans React en utilisant les props. 

Sur `TodoList`, ajoutons une prop nommée `todos`. Vous pouvez déstructurer `todos` à partir de l'objet props. Cela vous permet de voir à nouveau vos éléments de tâche.

Maintenant, qu'en est-il de l'affichage du nombre total de tâches dans le composant `TodoCount` ? 

C'est un autre cas où vous pouvez transmettre les données en tant que prop, puisque `TodoCount` dépend de cet état. Une fois de plus, nous fournirons la même prop, `todos`, nous la déstructurerons de l'objet props et nous afficherons le nombre total de tâches en utilisant `todos.length` :

```js
import React from "react";

export default function App() {
  const [todos, setTodos] = React.useState(["élément 1", "élément 2", "élément 3"]);

  return (
    <>
      <TodoCount todos={todos} />
      <TodoList todos={todos} />
      <AddTodo />
    </>
  );
}

function TodoCount({ todos }) {
  return <div>Total des tâches : {todos.length}</div>;
}

function TodoList({ todos }) {
  return (
    <ul>
      {todos.map((todo) => (
        <li key={todo}>{todo}</li>
      ))}
    </ul>
  );
}
```

## Comment transmettre des fonctions de rappel (callbacks) vers le bas

Maintenant, la dernière étape consiste à pouvoir ajouter une nouvelle tâche. 

C'est ici qu'intervient votre fonction de mise à jour, `setTodos`. Pour mettre à jour l'état de vos tâches, vous n'avez pas besoin de transmettre les deux valeurs, la variable et la fonction de mise à jour – tout ce que vous avez à faire est de transmettre `setTodos`. 

Vous la transmettrez à `AddTodo` en tant que prop du même nom (`setTodos`) et vous la déstructurerez à partir des props. 

Comme vous pouvez le voir, vous utilisez l'événement `onSubmit` de votre formulaire pour accéder à la valeur du champ de saisie – ce qui a été tapé, que vous placez dans une variable locale nommée `todo`.

Au lieu de devoir transmettre le tableau `todos` actuel, vous pouvez simplement utiliser une fonction interne pour obtenir la valeur précédente des tâches. Cela vous permet d'obtenir les tâches précédentes et de simplement renvoyer ce que vous voulez que le nouvel état soit. 

Ce nouvel état sera un tableau, dans lequel vous décomposerez (spread) toutes les tâches précédentes et ajouterez votre nouvelle tâche comme dernier élément de ce tableau :

```js
import React from "react";

export default function App() {
  const [todos, setTodos] = React.useState(["élément 1", "élément 2", "élément 3"]);

  return (
    <>
      <TodoCount todos={todos} />
      <TodoList todos={todos} />
      <AddTodo setTodos={setTodos} />
    </>
  );
}

function AddTodo({ setTodos }) {
  function handleSubmit(event) {
    event.preventDefault();
    const todo = event.target.elements.todo.value;
    setTodos(prevTodos => [...prevTodos, todo]);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" id="todo" />
      <button type="submit">Ajouter une tâche</button>
    </form>
  );
}
```

> Non seulement nous pouvons utiliser ce modèle en faisant remonter l'état et en transmettant sa variable d'état aux composants qui ont besoin de la lire, mais nous pouvons également l'utiliser pour les fonctions de rappel (callbacks) afin de pouvoir mettre à jour l'état.

Une fois que vous ajoutez un nouvel élément à votre liste de tâches, il est immédiatement ajouté à l'état. Ensuite, vous voyez votre composant `TodoList` se re-rendre pour afficher ce nouvel élément, ainsi que `TodoCount` pour montrer le nombre total de tâches qui est maintenant de 4 :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/lifting-state-2.gif)

## Conclusion

La remontée d'état est un modèle important pour les développeurs React car nous avons parfois un état situé dans un composant particulier qui doit également être partagé avec des composants frères. 

Au lieu d'utiliser une bibliothèque de gestion d'état complète comme Redux ou React Context, nous pouvons simplement faire remonter l'état jusqu'à l'ancêtre commun le plus proche et transmettre à la fois les variables d'état (les valeurs d'état) ainsi que toutes les fonctions de rappel pour mettre à jour cet état. 

## Devenir un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre tout seul.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir quand j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*