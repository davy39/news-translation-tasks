---
title: Comment utiliser Redux et Redux Toolkit – Tutoriel pour débutants
subtitle: ''
author: Boateng Dickson
co_authors: []
series: null
date: '2023-05-04T14:20:56.000Z'
originalURL: https://freecodecamp.org/news/redux-and-redux-toolkit-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/redux-for-beginners1.jpg
tags:
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'State Management '
  slug: state-management
seo_title: Comment utiliser Redux et Redux Toolkit – Tutoriel pour débutants
seo_desc: "When I started learning Redux, I found it challenging to wrap my head around\
  \ the concepts. Despite reading many online resources, I struggled to grasp the\
  \ core ideas. \nWhile the online tutorials and guides provided helpful information,\
  \ I needed more ..."
---

Lorsque j'ai commencé à apprendre Redux, j'ai trouvé difficile de comprendre les concepts. Malgré la lecture de nombreuses ressources en ligne, j'ai eu du mal à saisir les idées principales. 

Bien que les tutoriels et guides en ligne fournissaient des informations utiles, j'avais besoin de plus de clarté pour vraiment comprendre Redux.

Mais avec de la persévérance et de la pratique, j'ai finalement mieux compris les concepts clés de Redux et je les ai implémentés avec succès dans mes projets.

Dans cet article, je vais expliquer Redux de la manière la plus simple possible. En tant que personne ayant initialement eu du mal à comprendre Redux, je sais à quel point cela peut être frustrant d'apprendre un nouveau concept. Mais j'espère que cet article aidera à rendre les concepts de Redux plus accessibles aux débutants.

Nous allons également explorer Redux Toolkit, une collection d'outils qui simplifient l'utilisation de Redux. Ces outils aident à rendre Redux moins intimidant et plus facile à utiliser.

## Qu'est-ce que Redux ?

Redux est une bibliothèque de gestion d'état qui vous permet de gérer l'état de vos applications JavaScript de manière plus efficace et prévisible.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-165.png)

Imaginez que vous construisez une maison et que vous devez garder une trace de tous les matériaux que vous utilisez et de l'argent que vous dépensez. Au lieu de tout garder en tête ou sur un morceau de papier, vous pourriez utiliser un registre pour garder une trace de chaque transaction. Redux fonctionne de manière similaire en gardant une trace de l'état de votre application dans un seul endroit appelé le "store".

Disons que vous construisez un site de commerce électronique. Vous devrez peut-être garder une trace des articles dans le panier d'un utilisateur, de ses informations de paiement et de ses détails de livraison. 

Au lieu de passer ces informations de composant en composant en utilisant des props, Redux vous permet de les stocker dans un emplacement central où elles peuvent être facilement accessibles et mises à jour. Cela facilite la gestion des états complexes et maintient votre application organisée.

Il est important de noter que Redux n'est pas limité à React et que vous pouvez l'utiliser avec d'autres frameworks ou même avec JavaScript vanilla.

## Pourquoi devrais-je utiliser Redux ?

Redux peut aider à simplifier le processus de gestion d'état, surtout lorsque vous traitez avec des composants complexes et interconnectés. Voici quelques raisons pour lesquelles vous pourriez vouloir utiliser Redux dans votre application :

1. **Gestion d'état centralisée :** Avec Redux, vous pouvez maintenir l'état de votre application entière dans un seul store, ce qui facilite la gestion et l'accès aux données entre les composants.
2. **Mises à jour d'état prévisibles :** Redux a un flux de données clair, ce qui signifie que les changements d'état ne peuvent se produire que lorsque vous créez une action et l'envoyez via Redux. Cela facilite la compréhension de la manière dont les données de votre application changeront en réponse aux actions de l'utilisateur.
3. **Débogage plus facile :** Avec Redux DevTools, vous avez un enregistrement clair de tous les changements apportés à l'état de votre application. Cela facilite la localisation et la correction des problèmes dans votre code, vous faisant gagner du temps et des efforts dans le processus de débogage.
4. **Meilleures performances :** En minimisant le nombre de mises à jour d'état et en réduisant le besoin de prop drilling, Redux aide à améliorer les performances de votre application.

## Comment fonctionne Redux ?

Comme mentionné précédemment, Redux vous permet de maintenir un seul store centralisé qui gère l'état de votre application entière. Tous les composants de votre application peuvent accéder à ce store et mettre à jour ou récupérer des données selon les besoins. 

Les composants clés qui permettent cette approche centralisée de la gestion d'état sont :

1. Store
2. Actions
3. Dispatch
4. Reducers

Explorons le rôle de chacun :

### Le Store

Le store Redux est comme un grand conteneur qui contient toutes les données de votre application.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-167.png)

Imaginez le store comme une boîte avec différents compartiments pour différents types de données. Vous pouvez stocker n'importe quelle donnée que vous voulez dans ces compartiments, et il peut contenir divers types de données, tels que des chaînes de caractères, des nombres, des tableaux, des objets, et même des fonctions.

De plus, le store est la seule source de vérité pour l'état de votre application. Cela signifie que n'importe quel composant de votre application peut y accéder pour récupérer et mettre à jour des données.

### Actions

Une action est un objet qui décrit les changements qui doivent être apportés à l'état de votre application. Elle envoie des données de votre application au store Redux et sert de seule manière de mettre à jour le store.

Une action doit avoir une propriété "type" décrivant l'action en cours d'exécution. Cette propriété "type" est généralement définie comme une constante de chaîne de caractères pour assurer la cohérence et éviter les fautes de frappe.

En plus de la propriété "type", une action peut avoir une propriété "payload". La propriété "payload" représente les données qui fournissent des informations supplémentaires sur l'action en cours d'exécution. Par exemple, si un type d'action est `ADD_TASK`, le payload pourrait être un objet contenant l'"id", le "texte" et le "statut de complétion" d'un nouvel élément de tâche.

Voici un exemple d'action :

```javascript
{
  type: 'ADD_TASK',
  payload: {
    id: 1,
    text: 'Acheter des courses',
    completed: false
  }
}

```

Notez que pour créer des actions, nous utilisons des créateurs d'actions. Les créateurs d'actions sont des fonctions qui créent et retournent des objets d'action.

Voici un exemple de créateur d'action qui prend le texte d'une tâche et retourne un objet d'action pour ajouter la tâche au store Redux :

```javascript
function addTask(taskText) {
  return {
    type: 'ADD_TASK',
    payload: {
      id: 1,
      text: taskText,
      completed: false
    }
  }
}

```

Une analogie appropriée pour les actions et les créateurs d'actions serait un chef utilisant une recette. La recette décrit les ingrédients nécessaires et les instructions pour préparer un plat, similaire à la manière dont une action dans Redux spécifie les détails nécessaires pour modifier l'état d'une application. 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-171.png)

Dans ce scénario, le chef représente le créateur d'action, qui suit la recette pour créer le plat, similaire à la manière dont un créateur d'action crée une action basée sur des propriétés prédéfinies.

### Dispatch

Dans Redux, dispatch est une fonction fournie par le store qui vous permet d'envoyer une action pour mettre à jour l'état de votre application. Lorsque vous appelez `dispatch`, le store exécute une action à travers tous les reducers disponibles, qui à leur tour mettent à jour l'état en conséquence.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-185.png)

Vous pouvez penser à `dispatch` comme un facteur qui livre le courrier à différents départements dans une grande entreprise. Tout comme le facteur livre le courrier à différents départements, `dispatch` livre des actions à divers reducers dans votre store Redux. Chaque reducer est comme un département dans l'entreprise qui traite le courrier et met à jour sa propre partie des données de l'entreprise.

### Reducers

Dans Redux, un reducer est une fonction qui prend l'état actuel d'une application et une action comme arguments, et retourne un nouvel état basé sur l'action.

Voici un exemple de reducer simple :

```javascript
const initialState = {
  count: 0
};

function counterReducer(state = initialState, action) {
  switch(action.type) {
    case 'INCREMENT':
      return { ...state, count: state.count + 1 };
    case 'DECREMENT':
      return { ...state, count: state.count - 1 };
    default:
      return state;
  }
}

```

Dans le code ci-dessus, nous avons un reducer simple appelé "counterReducer" qui gère l'état d'une variable de compte. Il prend deux arguments : `state` et `action`. L'argument `state` représente l'état actuel de votre application, tandis que l'argument `action` représente l'action dispatchée pour modifier l'état.

Le reducer utilise ensuite une instruction switch pour vérifier le "type" de l'action, et en fonction de ce type, il met à jour l'état en conséquence. 

Par exemple, si le type d'action est "INCREMENT", le reducer retourne un nouvel objet d'état avec le compte incrémenté de 1. De même, si le type d'action est "DECREMENT", le reducer retourne un nouvel objet d'état avec le compte décrémenté de 1.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-172.png)

Une analogie parfaite pour un reducer serait un mixeur de cuisine. Tout comme un mixeur prend différents ingrédients, les mélange et produit un mélange lisse, un reducer prend l'état actuel d'une application et une action, les traite ensemble et produit un nouvel état.

## Projet d'exemple – Implémentation d'une application réelle

Maintenant que vous comprenez les bases de Redux et son fonctionnement, créons un projet simple du monde réel. Pour cet exemple, nous allons créer une application de liste de tâches de base où vous pouvez ajouter et supprimer des tâches.

### Étape 1 : Comment configurer le projet

Créez un nouveau projet React en exécutant la commande suivante dans votre terminal. Remplacez _"nom-de-votre-projet"_ par le nom de votre projet.

```
npm create vite@latest nom-de-votre-projet -- --template react

cd nom-de-votre-projet

npm install
```

La séquence de commandes ci-dessus créera un nouveau projet React en utilisant l'outil de construction Vite et installera toutes les dépendances nécessaires.

### Étape 2 : Comment installer Redux

Redux nécessite quelques dépendances pour ses opérations, notamment :

* **Redux :** La bibliothèque principale qui permet l'architecture redux.
* **React Redux :** Simplifie la connexion de vos composants React au store Redux.
* **Redux Thunk :** Vous permet d'écrire une logique asynchrone dans vos actions Redux.
* **Redux DevTools Extension :** Connecte votre application Redux à Redux DevTools

Vous pouvez les installer en utilisant npm, comme montré ci-dessous :

```
npm install \

redux \

react-redux \

redux-thunk \

redux-devtools-extension
```

### Étape 3 : Comment configurer les reducers

Maintenant, créons le reducer pour notre application. 

Dans le répertoire `src`, créez un nouveau dossier appelé `reducers`, et à l'intérieur de ce dossier, créez deux nouveaux fichiers : `index.js` et `taskReducer.js`.

Le fichier `index.js` représente le reducer racine, qui combine tous les reducers individuels de l'application. En revanche, le fichier `taskReducer.js` est l'un des reducers individuels qui sera combiné dans le reducer racine.

```javascript
import taskReducer from "./taskReducer";
import { combineReducers } from "redux";

const rootReducer = combineReducers({
  tasks: taskReducer,
});

export default rootReducer;

```

Dans le fichier `index.js` ci-dessus, nous utilisons la fonction `combineReducers` pour combiner tous les reducers individuels en un seul reducer racine. Dans ce cas, nous n'avons qu'un seul reducer (`taskReducer`), nous le passons donc en argument à `combineReducers`.

Le reducer combiné résultant est ensuite exporté afin que d'autres fichiers de l'application puissent l'importer et l'utiliser pour créer le store.

Voici le code pour `taskReducer` :

```jsx
const initialState = {
  tasks: []
};

const taskReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'ADD_TASK':
      return {
        ...state,
        tasks: [...state.tasks, action.payload]
      };
    case 'DELETE_TASK':
      return {
        ...state,
        tasks: state.tasks.filter(task => task.id !== action.payload)
      };
    default:
      return state;
  }
};

export default rootReducer;

```

Dans le fichier `taskReducer.js` ci-dessus, nous définissons une fonction de reducer qui prend deux arguments : `state` et `action`. L'argument `state` représente l'état actuel de l'application, tandis que l'argument `action` représente l'action dispatchée pour mettre à jour l'état.

L'instruction `switch` à l'intérieur du reducer gère différents cas en fonction du "type" de l'action. Par exemple, si le type d'action est `ADD_TASK`, le reducer retourne un nouvel objet d'état avec une nouvelle tâche ajoutée au tableau `tasks`. Et si le type d'action est `DELETE_TASK`, le reducer retourne un nouvel objet d'état avec les tâches actuelles filtrées pour supprimer la tâche avec l'`id` spécifié.

### Étape 4 : Comment créer le store Redux

Maintenant que nous avons notre configuration de base prête, créons un nouveau fichier appelé `store.js` dans le répertoire `src`. C'est là que vous définirez votre store Redux :

```javascript
import { createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { composeWithDevTools } from "redux-devtools-extension";

import taskReducer from "./reducers/taskReducer";

const store = createStore(
  taskReducer,
  composeWithDevTools(applyMiddleware(thunk))
);

export default store;

```

Le code ci-dessus configure un store Redux en créant une nouvelle instance du store en utilisant la fonction `createStore`. Ensuite, le rootReducer – qui combine tous les reducers de l'application en un seul reducer – est passé en argument à `createStore`. 

De plus, le code utilise également deux autres bibliothèques : `redux-thunk` et `redux-devtools-extension`. 

La bibliothèque `redux-thunk` vous permet d'écrire des actions asynchrones, tandis que la bibliothèque `redux-devtools-extension` vous permet d'utiliser l'extension de navigateur Redux DevTools pour déboguer et inspecter l'état et les actions dans le store. 

Enfin, nous exportons le store afin de pouvoir l'utiliser dans notre application. Nous utilisons la fonction `composeWithDevTools` pour améliorer le store avec la capacité d'utiliser l'extension Redux DevTools, et la fonction `applyMiddleware` pour appliquer le middleware thunk au store."

### Étape 5 : Comment connecter le store Redux à l'application

Pour connecter le store Redux à l'application ToDo, nous devons utiliser le composant `Provider` de la bibliothèque `react-redux`.

Tout d'abord, nous importons la fonction `Provider` et le store Redux que nous avons créé dans notre `main.jsx`. Ensuite, nous enveloppons notre composant `App` avec la fonction `Provider` et passons le `store` comme prop. Cela rend le store Redux disponible pour tous les composants à l'intérieur de `App`.

```jsx
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";

import { Provider } from "react-redux";
import store from "./store";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>
);

```

### Étape 6 : Comment utiliser Redux DevTools

Une fois que vous avez configuré le `<Provider>` Redux dans votre application, vous pouvez commencer à utiliser l'extension Redux DevTools. Pour commencer à l'utiliser, vous devrez télécharger l'extension Redux DevTools pour votre navigateur. 

Après l'installation, les DevTools ajouteront un nouvel onglet aux outils de développement de votre navigateur spécifiquement pour Redux.

<img src="https://i.imgur.com/QPPsZDT.gif" style="box-shadow: 3px 3px 10px rgba(0,0,0,0.3); border-radius: 5px;"/>

En cliquant sur l'onglet "State" dans les Redux DevTools, vous verrez l'état entier de votre store Redux et toutes les actions qui ont été dispatchées ainsi que leurs payloads. 

Cela peut être incroyablement utile lors du débogage de votre application, car vous pouvez inspecter l'état et les actions en temps réel.

### Étape 7 : Comment configurer les actions Redux

Maintenant que nous avons tout configuré, créons nos actions. Comme je l'ai mentionné précédemment, les actions représentent quelque chose qui s'est produit dans l'application. Par exemple, lorsqu'un utilisateur ajoute une nouvelle tâche, cela déclenche une action "ajouter une tâche". De même, lorsqu'un utilisateur supprime une tâche, cela déclenche une action "supprimer une tâche".

Pour créer les actions, créez un nouveau dossier appelé "actions" dans le répertoire `src`, puis créez un nouveau fichier appelé `index.js`. Ce fichier contiendra tous les créateurs d'actions pour notre application.

```jsx
export const addTodo = (text) => {
  return {
    type: "ADD_TASK",
    payload: {
      id: new Date().getTime(),
      text: text,
    },
  };
};

export const deleteTodo = (id) => {
  return {
    type: "DELETE_TASK",
    payload: id,
  };
};

```

Le code ci-dessus exporte deux créateurs d'actions : `addTodo` et `deleteTodo`. Ces fonctions retournent un objet avec une propriété `type` qui décrit l'action qui s'est produite.

Dans le cas de `addTodo`, la propriété `type` est définie sur `"ADD_TASK"`, indiquant qu'une nouvelle tâche a été ajoutée. La propriété `payload` contient un objet avec les valeurs `id` et `text` de la nouvelle tâche. L'`id` est généré en utilisant la méthode `new Date().getTime()` qui crée un identifiant unique basé sur le timestamp actuel.

Dans le cas de `deleteTodo`, la propriété `type` est définie sur `"DELETE_TASK"`, indiquant qu'une tâche a été supprimée. La propriété `payload` contient l'`id` de la tâche à supprimer.

Ces créateurs d'actions peuvent être dispatchés au store Redux en utilisant la méthode `dispatch()`, ce qui déclenchera la fonction de reducer correspondante pour mettre à jour l'état de l'application en conséquence.

### Étape 8 : Comment dispatcher des actions

Maintenant que nous avons créé les actions nécessaires, nous pouvons passer à la création des composants qui dispatcheront ces actions. 

Créons un nouveau dossier nommé "components" à l'intérieur du répertoire _src_. À l'intérieur de ce dossier, nous créerons deux nouveaux fichiers : `Task.jsx` et `TaskList.jsx`.

Le composant `Task.jsx` sera responsable de l'ajout de tâches. Mais avant de continuer, nous devons importer les éléments suivants dans le fichier :

* _addTodo action_ : Pour ajouter de nouvelles tâches à l'état.
* _useDispatch hook_ : Pour dispatcher l'action `addTodo`.
* _useRef_ : Permet d'obtenir une référence aux éléments HTML.

```javascript
import { useRef } from "react";
import { useDispatch } from "react-redux";
import { addTodo } from "../actions";

```

Une fois que nous avons importé ces composants nécessaires, nous pouvons procéder à l'écriture du code pour `Task.jsx`. 

```javascript
const Task = () => {
  const dispatch = useDispatch();
  const inputRef = useRef(null);

  function addNewTask() {
    const task = inputRef.current.value.trim();
    if (task !== "") {
      dispatch(addTodo(task));
      inputRef.current.value = "";
    }
  }

  return (
    <div className="task-component">
      <div className="add-task">
        <input
          type="text"
          placeholder="Ajouter une tâche ici..."
          ref={inputRef}
          className="taskInput"
        />
        <button onClick={addNewTask}>Ajouter une tâche</button>
      </div>
    </div>
  );
};

export default Task;

```

Dans le code ci-dessus, nous avons créé un composant composé d'un champ de saisie et d'un bouton. Lorsque l'utilisateur clique sur le bouton "Ajouter une tâche", la fonction `addNewTask` est exécutée. Cette fonction utilise le hook `useRef` pour obtenir la valeur du champ de saisie, supprime les espaces de début ou de fin, puis dispatch l'action `addTodo` avec la nouvelle tâche comme payload.

Passons maintenant au composant `TaskList.jsx`, responsable de l'affichage de la liste des tâches et de la gestion des suppressions de tâches. Pour ce faire, nous devons importer les éléments suivants :

* Le **hook useSelector** qui fournit l'accès à l'état du store Redux.
* L'**action deleteTodo**, responsable de la suppression d'une tâche de la liste des tâches dans le store Redux.

```javascript
import { useSelector, useDispatch } from "react-redux";
import { deleteTodo } from "../actions";

```

Nous allons maintenant écrire le code pour `TaskList.jsx` qui parcourt le tableau des tâches et affiche chaque tâche :

```javascript
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { deleteTodo } from '../actions';

const TaskList = () => {
  const tasks = useSelector((state) => state.tasks);
  const dispatch = useDispatch();

  const handleDelete = (id) => {
    dispatch(deleteTodo(id));
  };

  return (
    <div className="tasklist">
      <div className="display-tasks">
        <h3>Vos tâches :</h3>
        <ul className="tasks">
          {tasks.map((task) => (
            <li className="task" key={task.id}>
              {task.text}
              <button
                className="delete-btn"
                onClick={() => handleDelete(task.id)}
              >
                supprimer
              </button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default TaskList;

```

Ici, le composant parcourt chaque tâche dans le tableau des tâches et affiche le texte et un bouton de suppression. Lorsque l'utilisateur clique sur le bouton de suppression, la fonction `handleDelete` est appelée, dispatchant l'action `deleteTodo` avec l'`id` de la tâche comme payload.

Enfin, importez les composants dans votre fichier `App.jsx` et affichez-les.

```javascript
import Task from "./components/Task";
import TaskList from "./components/TaskList";

function App() {
  return (
    <div className="App">
      <Task />
      <TaskList />
    </div>
  );
}

export default App;

```

### Étape 9 : Styling

Pour le style, copiez le contenu de ce [gist](https://gist.githubusercontent.com/dboatengg/ea07e95167aec1af97084651128ea8e9/raw/d5b0e5611c4a82e46ad4bc2f33defefd4ce9937a/index.css) et collez-le dans votre fichier `index.css`. L'accent de ce guide est uniquement sur la fonctionnalité et non sur le style. Par conséquent, seuls des styles de base ont été inclus pour garantir que l'application ait une apparence présentable.

### Résultat final

Après avoir implémenté tout, le résultat final de notre application de liste de tâches devrait ressembler à ceci :

<img src="https://i.imgur.com/AACNPOW.gif" style="border-radius:5px;box-shadow: 3px 3px 12px rgba(0,0,0,0.3);"/>

Comme montré ci-dessus, nous pouvons ajouter des tâches en entrant du texte dans le champ de saisie et en cliquant sur le bouton "Ajouter une tâche". Nous pouvons également supprimer des tâches en cliquant sur le bouton "supprimer" à côté de chaque tâche.

L'état et les actions de l'application peuvent également être facilement suivis et inspectés en utilisant Redux DevTools. Cette fonctionnalité aide à déboguer et à comprendre comment l'application fonctionne sous le capot.

Avec cela, vous avez maintenant une application ToDo entièrement fonctionnelle alimentée par Redux ! Le code source de l'application est disponible sur ce [dépôt GitHub](https://github.com/dboatengg/redux-tutorial).

Enfin, il est important de noter que l'état d'une application est stocké en mémoire lors de l'utilisation de Redux. Par conséquent, l'état sera perdu si un utilisateur actualise la page ou navigue loin de l'application.

Ainsi, pour conserver les informations même après qu'un utilisateur quitte ou ferme la page, vous devez stocker ces informations ailleurs en dehors de la mémoire de l'application. Diverses techniques, telles que le stockage local ou côté serveur, peuvent être utilisées pour accomplir cela.

Félicitations ! Vous avez maintenant une bonne compréhension de la manière d'intégrer Redux dans vos applications React. Dans la section suivante, nous explorerons Redux Toolkit et découvrirons comment il peut simplifier le processus d'écriture de code Redux avec moins d'efforts.

## Comment utiliser Redux Toolkit

L'écriture de code Redux peut devenir complexe et verbeuse, en particulier à mesure que la taille d'une application grandit. À mesure que le nombre de reducers et d'actions augmente, il peut devenir difficile de gérer les différentes parties et de tout suivre.

Heureusement, Redux Toolkit offre une solution à ce problème. Il fournit une manière plus rationalisée et efficace de gérer l'état de votre application en abstraisant certains des aspects plus complexes et répétitifs de Redux, tels que la création de reducers et d'actions.

### Avantages de Redux Toolkit

Redux Toolkit offre plusieurs avantages par rapport à Redux traditionnel :

* Il est plus facile à configurer et nécessite moins de dépendances.
* Réduit le code répétitif en permettant la création d'un seul fichier connu sous le nom de "slice" qui combine les actions et les reducers.
* Fournit des valeurs par défaut sensées pour les fonctionnalités couramment utilisées, telles que Redux Thunk et Redux DevTools. Cela signifie que vous n'avez pas à passer du temps à configurer ces fonctionnalités vous-même, car elles sont déjà intégrées dans Redux Toolkit.
* Il utilise la bibliothèque immer sous le capot, ce qui permet une mutation directe de l'état et élimine le besoin de copier manuellement l'état `{...state}` avec chaque reducer.

Dans les sections suivantes, nous explorerons comment utiliser Redux Toolkit pour simplifier le code Redux de l'application ToDo que nous avons construite précédemment.

### Comment configurer Redux Toolkit

Pour utiliser Redux Toolkit dans votre application React, vous devez installer deux dépendances : `@reduxjs/toolkit` et `react-redux`. 

Le package `@reduxjs/toolkit` fournit les outils nécessaires pour simplifier le développement Redux, tandis que `react-redux` est nécessaire pour connecter votre store Redux à vos composants React. 

```
npm install @reduxjs/toolkit react-redux
```

### Comment créer une slice

Une fois que vous avez installé les dépendances nécessaires, créez une nouvelle "slice" en utilisant la fonction `createSlice`. Une slice est une portion du store Redux qui est responsable de la gestion d'une partie spécifique de l'état.

Imaginez le store Redux comme un gâteau, où chaque slice représente une partie spécifique des données dans le store. En créant une slice, vous pouvez définir le comportement de l'état en réponse à des actions particulières en utilisant des fonctions de reducer.

Pour créer une slice pour gérer notre application ToDo, créez un nouveau fichier nommé `src/features/todo/todoSlice.js` et ajoutez le code suivant.

```javascript
import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  tasks: [],
};

const todoSlice = createSlice({
  name: "todo",
  initialState,
  reducers: {
    addTodo: (state, action) => {
      state.tasks.push({ id: Date.now(), text: action.payload });
    },
    deleteTodo: (state, action) => {
      state.tasks = state.tasks.filter((task) => task.id !== action.payload);
    },
  },
});

export const { addTodo, deleteTodo } = todoSlice.actions;

export default todoSlice.reducer;
```

Le code ci-dessus définit une slice nommée `todoSlice`, avec un objet `initialState` qui contient un tableau vide de tâches. 

L'objet `reducers` définit deux fonctions de reducer : `addTask` et `deleteTask`. `addTask` ajoute un nouvel objet de tâche au tableau `tasks`, et `deleteTask` supprime une tâche du tableau `tasks` en fonction de sa propriété `id`.

La fonction `createSlice` génère automatiquement des créateurs d'actions et des types d'actions basés sur les noms des fonctions de reducer que vous fournissez. Ainsi, vous n'avez pas à définir les créateurs d'actions vous-même manuellement.

L'instruction `export` exporte les créateurs d'actions générés, qui peuvent être utilisés dans d'autres parties de votre application pour dispatcher des actions à la slice.

Et enfin, la fonction `todoSlice.reducer` gère toutes les actions générées automatiquement basées sur les objets de reducer fournis à la fonction `createSlice`. En l'exportant par défaut, vous pouvez le combiner avec d'autres reducers dans votre application pour créer un store Redux complet.

### Comment configurer le store Redux

La création d'un store Redux est beaucoup plus simple avec Redux Toolkit. 

La manière la plus basique de créer un store est d'utiliser la fonction `configureStore()`, qui génère automatiquement un reducer racine pour vous en combinant tous les reducers définis dans votre application. 

Pour créer un store pour l'application, ajoutez un fichier nommé `src/store.js` et ajoutez le code suivant :

```javascript
import { configureStore } from "@reduxjs/toolkit";
import todoReducer from "./features/todo/todoSlice";

const store = configureStore({
  reducer: {
    todo: todoReducer,
  },
});

export default store;

```

Dans cet exemple, nous importons d'abord la fonction `configureStore` du package `@reduxjs/toolkit`, et la fonction `todoReducer` d'un fichier séparé.

Ensuite, nous créons un objet `store` en appelant `configureStore` et en lui passant un objet avec une propriété `reducer`. La propriété `reducer` est un objet qui mappe les noms des slices de reducer à leurs fonctions de reducer correspondantes. Dans ce cas, nous avons une slice de reducer appelée `todo`, et sa fonction de reducer correspondante est `todoReducer`.

Enfin, nous exportons l'objet `store` afin qu'il puisse être importé et utilisé dans d'autres parties de l'application.

### Comment fournir le store Redux à React

Pour rendre votre store Redux disponible pour les composants React dans votre application, importez le composant Provider de la bibliothèque `react-redux` et enveloppez votre composant racine (généralement `<App>`) avec lui. 

Le composant Provider prend le store comme prop et le transmet à tous les composants enfants qui ont besoin d'y accéder.

```jsx
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";

import store from "./store.js";
import { Provider } from "react-redux";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>
);

```

### Créer des composants

Vous pouvez maintenant créer des composants React tels que `Task.jsx` et `TaskList.jsx` qui utilisent le hook `useSelector` pour accéder à l'état actuel du store. De même, vous pouvez utiliser le hook `useDispatch` pour dispatcher des actions afin de mettre à jour le store, tout comme vous l'avez fait avec Redux simple. 

Vous devriez maintenant avoir la même application qu'auparavant avec quelques mises à jour de Redux Toolkit et beaucoup moins de code à maintenir.

## Conclusion

Si vous avez suivi ce tutoriel, vous devriez maintenant avoir une solide compréhension de Redux, à la fois l'approche traditionnelle et la version simplifiée utilisant Redux Toolkit. 

J'espère que vous avez trouvé cet article utile et informatif. Je sais que c'était beaucoup de matériel à couvrir, mais j'espère qu'il servira de ressource complète pour les débutants et les apprenants intermédiaires cherchant à apprendre Redux. 

Si vous souhaitez expérimenter avec le code que nous avons couvert dans cet article, vous pouvez y accéder dans le [dépôt GitHub](https://github.com/dboatengg/redux-tutorial) fourni. N'hésitez pas à l'utiliser comme point de départ pour vos propres applications ou comme référence alors que vous continuez à apprendre et à explorer le monde de Redux.

Merci d'avoir lu, et bon codage !