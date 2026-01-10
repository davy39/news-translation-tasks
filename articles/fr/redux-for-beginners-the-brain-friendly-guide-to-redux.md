---
title: Redux pour Débutants – Le Guide Convivial pour Apprendre Redux
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2021-04-12T14:09:32.000Z'
originalURL: https://freecodecamp.org/news/redux-for-beginners-the-brain-friendly-guide-to-redux
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/react-redux-todo-app.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: React
  slug: react
- name: Redux
  slug: redux
seo_title: Redux pour Débutants – Le Guide Convivial pour Apprendre Redux
seo_desc: 'In this Redux for Beginners guide, we''re going to:


  Learn about the different parts of Redux and how they work together

  Learn how to fetch data from an API using Redux

  Learn how to use Redux Toolkit to setup and work with Redux using less code


  And I...'
---

Dans ce guide Redux pour Débutants, nous allons :

* Apprendre les différentes parties de Redux et comment elles fonctionnent ensemble
* Apprendre à récupérer des données depuis une API en utilisant Redux
* Apprendre à utiliser Redux Toolkit pour configurer et travailler avec Redux en utilisant moins de code

Et je vous donnerai quelques défis que vous pourrez essayer à la fin.

## Ce que nous allons construire

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-08-at-08.49.52.png)
_Oui, c'est une liste de tâches ! Mais celle-ci utilise Redux, ce qui en fait une liste de tâches sophistiquée !_

L'utilisateur peut :

* Ajouter des tâches
* Supprimer des tâches
* Marquer des tâches comme complètes
* Voir le nombre de tâches complétées

### Vidéo de Présentation

Voici une [vidéo de présentation](https://www.youtube.com/watch?v=fiesH6WU63I) si vous souhaitez compléter votre lecture (sur YouTube).

### Code Source

Enfin, vous pouvez récupérer le [code final ici](https://github.com/chrisblakely01/react-redux-todo-app) (sur GitHub).

## Obtenez le Code de Démarrage

J'ai fourni un code de démarrage qui nous donne une interface utilisateur React basique avec tous les composants en place. Cela nous permet de nous concentrer davantage sur l'aspect Redux, qui est la raison pour laquelle nous sommes tous ici !

Commençons par ouvrir un terminal et exécuter les commandes suivantes :

```
git clone https://github.com/chrisblakely01/react-redux-todo-app.git
cd react-redux-todo-app/starter
npm install
npm start 
```

Cela devrait lancer un navigateur avec l'application démarrée. 

Ensuite, ouvrez le dossier `react-redux-todo-app` dans votre IDE (j'utiliserai VS Code). L'arborescence du projet devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-08-at-09.13.17.png)

Vous remarquerez quelques dossiers ici :

* **API** : Il s'agit de l'API que nous utiliserons plus tard dans le projet lorsque nous apprendrons à travailler avec les API dans Redux (quel excitement !) 
* **Final** : Il s'agit du code final. Notez que si vous exécutez cela, l'API doit également être démarrée. Voir le **readme** dans le dépôt GitHub pour savoir comment faire cela
* **Starter** : Il s'agit du dossier dans lequel nous travaillerons si vous décidez de suivre le tutoriel 

## Aperçu de Redux 

Avant de nous plonger dans le code, examinons les différentes parties de Redux et comment elles fonctionnent ensemble.

Redux est composé d'**actions**, de **réducteurs**, d'**état** et du **store**. Chaque élément effectue une tâche spécifique. Prenons un exemple :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/ReduxDataFlowDiagram-49fa8c3968371d9ef6f2a1486bd40a26-1.gif)
_[image de redux.js.org](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)_

Disons que nous avons un composant qui nous permet de déposer de l'argent avec un clic sur un bouton (la boîte "UI" dans le diagramme ci-dessus).

Lorsque nous cliquons sur un bouton, nous appelons généralement une fonction qui gère cet événement. C'est là que nous enverrions une action.

**Dispatch** est une fonction donnée par Redux, et nous permet de **déclencher des actions**.

L'**action** contient un **type**, et une **charge utile**. Le type est généralement juste une chaîne avec le nom de l'action. La charge utile contient les données que nous devons connaître. Par exemple, nous ne pouvons pas déposer d'argent sans connaître le montant

Le **store** reçoit l'action, et est responsable de la gestion de l'état. Pensez-y comme à une base de données, dans le sens où il contient toutes nos données en un seul endroit

Le store est également responsable de la mise à jour de l'état en fonction de l'action et de l'état actuel, ce qu'il fait en utilisant des **réducteurs**.

Un **réducteur** semble sophistiqué mais ce n'est qu'une fonction qui prend l'état actuel du store, et l'action. Il combine les choses ensemble et retourne le nouvel état.

Pensez-y comme à une chaîne de montage – il prend l'ancien état et l'action, fait un peu de travail, et produit le nouvel état.

Le store enregistre ensuite ce nouvel état qui est retourné par le réducteur et passe l'état aux composants. Cela les fait se re-rendre, affichant les nouvelles données.

### Pourquoi avons-nous besoin de tout cela ?

Imaginez une application avec des centaines, voire des milliers de composants. Il deviendrait ingérable de passer l'état autour et de se souvenir quel composant change l'état, comment il change l'état, et ainsi de suite.

En décomposant les choses comme cela, nous donnons différentes responsabilités à différentes choses, et nous gardons tout notre état en un seul endroit.

Cela rend les choses plus faciles à comprendre et à tester. Par exemple, vous pouvez tester les réducteurs en isolation puisqu'ils ne sont que des fonctions pures. Nous pouvons tester que nos actions sont correctement envoyées, et que notre store enregistre correctement l'état.

## Comment Configurer Notre Store 

Nous allons utiliser Redux toolkit pour configurer tout ce dont nous avons besoin pour faire fonctionner Redux, en commençant par le store.

Créez un nouveau dossier dans le dossier **src** appelé **redux.** Dans ce dossier, créez un fichier appelé **store.js,** et ajoutez le code suivant :

```jsx
import { configureStore } from '@reduxjs/toolkit';

export default configureStore({
	reducer: {},
});

```

La fonction configure store fait tout le travail difficile pour nous. Elle crée le store qui contient notre état, combine nos réducteurs, et a un joli middleware intégré que nous utiliserons plus tard.

La fonction configureStore nous retourne un store, que nous pouvons exporter (ligne 3). Cela nous permet de lier le store à notre application, ce que nous ferons dans un instant.

Nous devons passer nos réducteurs à la fonction configureStore, ce que nous faisons en passant un objet.

Nous n'avons pas encore créé de réducteurs, mais nous pourrions avoir autant de réducteurs que nous voulons ici.

### Comment Connecter le Store à l'Application

Nous avons un store, et nous avons une application, alors joignons ces deux choses !

Ouvrez **index.js** et mettez-le à jour avec ce qui suit :

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import store from './redux/store';
import { Provider } from 'react-redux';

ReactDOM.render(
	<React.StrictMode>
		<Provider store={store}>
			<App />
		</Provider>
	</React.StrictMode>,
	document.getElementById('root')
);

```

Nous importons le **store** et le **Provider** (en haut), puis nous enveloppons notre composant **App** dans le composant **Provider**. Le Provider doit recevoir un store à utiliser, donc nous passons le store que nous venons de créer. Cela donne à nos composants l'accès à l'état qui vit dans le store.

## Comment Créer un Slice 

Un **slice** nous donne un moyen de stocker une partie, ou une tranche, de données, et nous donne tout ce dont nous avons besoin pour changer et récupérer ces données. 

Vous pouvez le considérer comme un regroupement de données, similaire aux tables de base de données.

Dans le dossier **src/redux**, créez un nouveau fichier appelé **todoSlice.js** :

```jsx
import { createSlice } from '@reduxjs/toolkit';

export const todoSlice = createSlice({
	name: 'todos',
	initialState: [
		{ id: 1, title: 'todo1', completed: false },
		{ id: 2, title: 'todo2', completed: false },
		{ id: 3, title: 'todo3', completed: true },
		{ id: 4, title: 'todo4', completed: false },
		{ id: 5, title: 'todo5', completed: false },
	],
	reducers: {
		addTodo: (state, action) => {
			const todo = {
				id: new Date(),
				title: action.payload.title,
				completed: false,
			};
			state.push(todo);
		},

	},
});


export const { addTodo } = todoSlice.actions;

export default todoSlice.reducer;
```

La fonction **createSlice** nous retournera certaines choses et les assignera à la variable todoSlice (ligne 3)

C'est ici que nous obtenons nos actions et réducteurs que nous pouvons exporter.

Nous devons passer certaines propriétés à cette fonction afin qu'elle nous retourne les bonnes choses. Nous le faisons avec un objet.

Tout d'abord, nous donnons un nom au slice. Nous sommes dans le slice des todos, donc nous l'appellerons todos. C'est aussi ce que nous verrons dans les outils de développement Redux (ligne 4).

Ensuite, nous ajoutons l'état initial. Nous allons ajouter quelques données factices pour l'instant. Cela peut être vide, mais nous allons ajouter des choses pour que nous puissions voir ce qui se passe (ligne 5)

Maintenant, nous ajoutons les réducteurs. Le réducteur répond à l'action, prend l'état actuel, et crée un nouvel état basé sur la charge utile de l'action. Le premier que nous ajoutons est le réducteur **addTodo** (ligne 13)

Ce n'est qu'une fonction simple. Redux passe le **state** et **action** en arrière-plan. Le state est l'état actuel de ce slice, et l'action contient le type et la charge utile.

Donc, lorsque nous envoyons l'action **addTodo**, c'est le **réducteur** qui gère cette action.

Dans le réducteur, c'est ici que nous voulons effectuer la logique pour mettre à jour l'état (ligne 14). 

Puisque nous ajoutons un todo, la première chose que nous voulons faire est de créer un nouvel objet todo. Cet objet va avoir les mêmes propriétés que nos autres todos. Nous générerons un nouvel ID basé sur la date pour nous assurer qu'il est unique, prendrons le titre de la charge utile, et mettrons par défaut completed à false.

Maintenant, nous ajoutons simplement cela à l'objet state. À ce stade, redux prendra ce nouvel état et mettra à jour le store

C'est le premier dont nous avons besoin, mais nous ajouterons plus de réducteurs au fur et à mesure que nous avancerons dans le tutoriel

Lorsque nous ajoutons un objet réducteur comme celui-ci, la fonction createSlice crée des actions basées sur les noms des réducteurs.

### Comment exporter nos actions et réducteurs

Nous utilisons la déstructuration pour obtenir les actions et les exporter, afin que nos composants puissent y accéder.

Donc, le todoSlice a créé un ensemble d'actions pour nous basées sur nos noms de réducteurs, et nous utilisons simplement la déstructuration pour obtenir l'action addTodo et l'exporter (ligne 26).

Et nous exportons le réducteur afin de pouvoir l'ajouter à notre store (ligne 28).

## Comment Ajouter les Réducteurs au Store 

Maintenant, nous devons ajouter notre réducteur au store. Dans **store.js**, ajoutez ce qui suit :

```jsx
import { configureStore } from '@reduxjs/toolkit';
import todoReducer from './todoSlice';

export default configureStore({
	reducer: {
		todos: todoReducer,
	},
});

```

Rappelez-vous que le store contient tous nos réducteurs et les gère pour nous.

Par exemple, nous pourrions avoir un autre réducteur appelé userReducer ici et le store gérera tout pour nous. Cela rend simplement notre code plus facile à maintenir.

## Comment Ajouter une Nouvelle Tâche 

Nous avons créé le réducteur et l'action pour ajouter une tâche. Cela ne fait rien pour l'instant car nous n'avons pas encore envoyé l'action.

### Envoyer l'action addTodo 

Ce que nous voulons faire, c'est que lorsque l'utilisateur clique sur soumettre, nous voulons envoyer l'action addTodo.

Dans **AddTodoForm.js**, lorsque l'utilisateur clique sur soumettre, nous voulons envoyer l'action addTodo. 

Mettez à jour le code dans **AddTodoForm.js** avec ce qui suit :

```jsx
import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { addTodo } from '../redux/todoSlice';

const AddTodoForm = () => {
	const [value, setValue] = useState('');
	const dispatch = useDispatch();

	const onSubmit = (event) => {
		event.preventDefault();
		if (value) {
			dispatch(
				addTodo({
					title: value,
				})
			);
		}
	};

	return (
		<form onSubmit={onSubmit} className='form-inline mt-3 mb-3'>
			<label className='sr-only'>Name</label>
			<input
				type='text'
				className='form-control mb-2 mr-sm-2'
				placeholder='Add todo...'
				value={value}
				onChange={(event) => setValue(event.target.value)}
			></input>

			<button type='submit' className='btn btn-primary mb-2'>
				Submit
			</button>
		</form>
	);
};

export default AddTodoForm;

```

* Nous importons le hook useDispatch et l'action addTodo (ligne 2/ligne 3)
* Maintenant, dans notre fonction qui est appelée lorsque le formulaire est soumis, nous ajouterons un appel pour envoyer l'action addTodo (ligne 12)
* Pour chaque todo, nous devons connaître le titre, donc nous ajouterons un nouvel objet et passerons le titre. Cet objet sera mappé à la charge utile de l'action (ligne 13)

Maintenant, si nous essayons cela, rien ne se passe dans notre interface utilisateur car nous n'avons pas mis à jour le TodoList pour récupérer les données de Redux, ce que nous ferons dans un instant.

Si nous ouvrons les outils de développement Redux, vous pouvez voir sous l'onglet des actions que notre action a été envoyée, et la charge utile contient notre titre :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-09-at-07.18.47.png)
_L'action est envoyée avec la charge utile correcte_

Vous pouvez également voir que l'état a été mis à jour avec le nouveau todo en cliquant sur l'onglet **state**.

## Comment Afficher la Liste des Tâches

Maintenant que nous avons vu comment envoyer des actions et mettre à jour l'état, nous allons voir comment récupérer des données de Redux

Dans notre composant TodoList, nous voulons prendre les TODOS de Redux, plutôt que d'utiliser la liste factice

Pour cela, nous utilisons ce qu'on appelle le hook **useSelector**. Ouvrez TodoList.js et mettez-le à jour avec ce qui suit :

```jsx
import React, { useEffect } from 'react';
import TodoItem from './TodoItem';
import { useSelector } from 'react-redux';

const TodoList = () => {
	const todos = useSelector((state) => state.todos);

	return (
		<ul className='list-group'>
			{todos.map((todo) => (
				<TodoItem id={todo.id} title={todo.title} completed={todo.completed} />
			))}
		</ul>
	);
};

export default TodoList;

```

Le hook **useSelector** accepte une fonction, et nous retourne les données basées sur cette fonction.

Nous allons donc passer notre fonction – dans ce cas, nous allons faire une fonction fléchée. Celle-ci accepte l'état qui est passé par Redux. Dans ce cas, nous voulons faire state.todos pour obtenir tous les todos.

Maintenant, cela va aller dans le store, sélectionner tous les todos de l'état, et assigner cela à la variable todos que nous avons définie nous-mêmes

Puisque nous avons déjà fait le travail difficile pour afficher la liste dans notre JSX, nous devons simplement remplacer la liste factice par ce que nous avons reçu de Redux.

Si nous essayons cela, vous pouvez voir que les todos sont maintenant récupérés depuis notre todosSlice !

La valeur d'état qui est passée dans la fonction du hook useSelector est l'arbre d'état entier qui est stocké dans Redux.

Donc, si vous avez plusieurs tranches d'état, cela retournera le tout. Cela nous permet de faire des choses assez cool – par exemple, si nous voulons obtenir un todo spécifique, ou filtrer la liste, nous pouvons le faire ici dans cette fonction.

## Comment Marquer une Tâche comme Complète

### Créer le réducteur/action

Ensuite, nous allons voir comment marquer une tâche comme complète. C'est intéressant car cela implique la mise à jour de l'état existant. Mettez à jour todoSlice.js avec ce qui suit :

```jsx
import { createSlice } from '@reduxjs/toolkit';

export const todoSlice = createSlice({
	name: 'todos',
	initialState: [
		{ id: 1, title: 'todo1', completed: false },
		{ id: 2, title: 'todo2', completed: false },
		{ id: 3, title: 'todo3', completed: true },
		{ id: 4, title: 'todo4', completed: false },
		{ id: 5, title: 'todo5', completed: false },
	],
	reducers: {
		addTodo: (state, action) => {
			const todo = {
				id: new Date(),
				title: action.payload.title,
				completed: false,
			};
			state.push(todo);
		},
		toggleComplete: (state, action) => {
			const index = state.findIndex((todo) => todo.id === action.payload.id);
			state[index].completed = action.payload.completed;
		},
	},
});

export const { addTodo, toggleComplete } = todoSlice.actions;

export default todoSlice.reducer;

```

Nous ajoutons notre nouveau réducteur (ligne 21). Rappelez-vous que chaque réducteur accepte l'état actuel et une action qui est passée par Redux.

Lorsque notre composant envoie l'action **toggleComplete**, ce réducteur gérera cette action.

Maintenant que nous avons notre réducteur, nous devons implémenter la logique pour mettre à jour l'état (ligne 22).

Donc, rappelez-vous que chaque todo dans la liste a un **ID**. Notre composant passera cet ID dans la charge utile de l'action et nous utiliserons l'ID pour déterminer quel todo dans le tableau nous devons mettre à jour.

Nous utiliserons l'ID pour trouver l'index du todo dans le tableau, donc si l'ID est 1, il retournera l'index 0.

Maintenant que nous connaissons l'index, nous pouvons mettre à jour la propriété "completed" pour le todo donné.

Nous définirons la propriété completed pour ce todo à ce qu'elle est dans la **charge utile**.

Enfin, nous exportons l'action afin que les composants puissent l'envoyer (ligne 30). Rappelez-vous que la fonction createSlice crée automatiquement des actions basées sur nos noms de réducteurs, donc puisque nous avons un réducteur toggleComplete, cela signifie que nous avons une action toggleComplete.

### Envoyer l'action

Maintenant, lorsque notre case est cochée, nous voulons déclencher l'action toggleComplete. Mettez à jour **TodoItem.js** avec ce qui suit :

```jsx
import React from 'react';
import { useDispatch } from 'react-redux';
import { toggleComplete } from '../redux/todoSlice';

const TodoItem = ({ id, title, completed }) => {
	const dispatch = useDispatch();

	const handleCheckboxClick = () => {
		dispatch(toggleComplete({ id, completed: !completed }));
	};

	return (
		<li className={`list-group-item ${completed && 'list-group-item-success'}`}>
			<div className='d-flex justify-content-between'>
				<span className='d-flex align-items-center'>
					<input
						type='checkbox'
						className='mr-3'
						onClick={handleCheckboxClick}
						checked={completed}
					></input>
					{title}
				</span>
				<button className='btn btn-danger'>Delete</button>
			</div>
		</li>
	);
};

export default TodoItem;

```

Maintenant, lorsque notre case est cochée, nous voulons déclencher l'action toggleComplete.

Dans notre composant TodoItem, nous créerons une fonction de gestion de clic qui envoie une action.

Tout d'abord, nous importons toggleComplete/useDispatch (ligne 2/ ligne 3)

Ensuite, nous créons une fonction de gestion de clic appelée handleCompleteClick (ligne 8). Ce sera une fonction fléchée qui envoie notre action. 

Nous appellerons la fonction dispatch, et passerons l'action que nous voulons envoyer (ligne 9).

Rappelez-vous, notre réducteur doit connaître l'ID de l'élément todo que nous modifions, et quelle est la nouvelle valeur de completed, donc nous passerons cela dans notre objet de charge utile. 

Nous passerons l'ID et une valeur de completed, qui sera l'inverse de ce qu'est la valeur actuelle de completed. Donc si la valeur actuelle est true, la nouvelle valeur sera false, et vice versa.

Maintenant, nous appelons simplement cette fonction depuis notre input (ligne 19).

## Comment Supprimer une Tâche

Nous allons voir un autre exemple de l'utilisation de ce modèle dans notre application avec la suppression d'une tâche.

### Créer le réducteur 

Allez dans TodoSlice.js et mettez-le à jour avec ce qui suit :

```jsx
import { createSlice } from '@reduxjs/toolkit';

export const todoSlice = createSlice({
	name: 'todos',
	initialState: [
		{ id: 1, title: 'todo1', completed: false },
		{ id: 2, title: 'todo2', completed: false },
		{ id: 3, title: 'todo3', completed: true },
		{ id: 4, title: 'todo4', completed: false },
		{ id: 5, title: 'todo5', completed: false },
	],
	reducers: {
		addTodo: (state, action) => {
			const todo = {
				id: new Date(),
				title: action.payload.title,
				completed: false,
			};
			state.push(todo);
		},
		toggleComplete: (state, action) => {
			const index = state.findIndex((todo) => todo.id === action.payload.id);
			state[index].completed = action.payload.completed;
		},
		deleteTodo: (state, action) => {
			return state.filter((todo) => todo.id !== action.payload.id);
		},
	},
});

export const { addTodo, toggleComplete, deleteTodo } = todoSlice.actions;

export default todoSlice.reducer;

```

Nous allons créer notre réducteur (ligne 25).

Lorsque notre action est envoyée, nous enverrons l'ID de la tâche qui a été cliquée, puis nous filtrerons cette tâche de la liste actuelle dans l'état.

Utilisez la fonction filter pour obtenir toutes les tâches qui ne sont pas égales à l'ID dans la charge utile (ligne 26). Nous devons retourner cela puisque la fonction filter nous donne un nouveau tableau.

Enfin, nous exporterons notre action qui a été créée pour nous (ligne 31).

### Envoyer l'action 

Maintenant, nous devons envoyer notre action deleteTodo lorsque le bouton de suppression est cliqué. Allez dans **TodoItem.js** et mettez-le à jour avec ce qui suit :

```jsx
import React from 'react';
import { useDispatch } from 'react-redux';
import { toggleComplete, deleteTodo } from '../redux/todoSlice';

const TodoItem = ({ id, title, completed }) => {
	const dispatch = useDispatch();

	const handleCheckboxClick = () => {
		dispatch(toggleComplete({ id, completed: !completed }));
	};

	const handleDeleteClick = () => {
		dispatch(deleteTodo({ id }));
	};

	return (
		<li className={`list-group-item ${completed && 'list-group-item-success'}`}>
			<div className='d-flex justify-content-between'>
				<span className='d-flex align-items-center'>
					<input
						type='checkbox'
						className='mr-3'
						onClick={handleCheckboxClick}
						checked={completed}
					></input>
					{title}
				</span>
				<button onClick={handleDeleteClick} className='btn btn-danger'>
					Delete
				</button>
			</div>
		</li>
	);
};

export default TodoItem;

```

Nous allons créer la fonction handleDeleteClick (ligne 12) qui enverra l'action de suppression, en passant l'ID comme objet dans la charge utile. Rappelez-vous, le réducteur doit connaître l'ID de la tâche à supprimer.

## Comment Afficher le Nombre Total d'Éléments Complétés

Ensuite, nous allons voir comment afficher le nombre d'éléments complétés. Ouvrez **TotalCompleteItems.js** et ajoutez ce qui suit :

```jsx
import React from 'react';
import { useSelector } from 'react-redux';

const TotalCompleteItems = () => {
	const todos = useSelector((state) =>
		state.todos.filter((todo) => todo.completed === true)
	);

	return <h4 className='mt-3'>Total des éléments complétés : {todos.length}</h4>;
};

export default TotalCompleteItems;

```

Tout d'abord, nous importons le hook useSelector (ligne 2) et l'assignons à une variable pour pouvoir l'utiliser (ligne 5).

Maintenant, nous pouvons passer une fonction pour dire à Redux ce que nous voulons retourner. Nous utiliserons la fonction filter pour retourner tous les todos qui ont une valeur completed de true (ligne 6).

Rappelez-vous que la valeur d'état qui est passée au sélecteur est l'arbre d'état TOTAL, c'est pourquoi nous devons spécifier les todos ici.

Maintenant, le résultat de notre fonction est passé à la variable todos. Puisque nous avons utilisé la fonction filter, le résultat est un tableau.

Maintenant, nous pouvons utiliser cette variable comme nous le souhaitons, donc nous afficherons la longueur dans notre JSX (ligne 9).

Ainsi, chaque fois que ce composant est monté, il va chercher les todos qui sont complétés, et afficher la longueur dans le JSX. 

Maintenant, si vous enregistrez et exécutez le code, vous verrez que chaque fois que nous cocherons une tâche, le compteur en bas sera mis à jour !

## Comment Travailler avec une API dans Redux

Pour effectuer des appels API dans Redux, nous avons besoin de ce qu'on appelle un middleware.

Au lieu d'envoyer une action qui va directement au réducteur, nous envoyons une action qui appelle un thunk, qui effectue l'appel API.

Cela crée ensuite une action normale, et l'envoie sur son chemin vers le réducteur. Regardons un diagramme :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/ReduxAsyncDataFlowDiagram-d97ff38a0f4da0f327163170ccc13e80.gif)
_Image de redux.js.org_

Au lieu d'envoyer une action simple, notre composant envoie une action qui appelle un **thunk.**

Cette action est interceptée par le middleware, qui effectue l'appel API.

Une fois que l'API a fait son travail et que nous avons reçu la réponse, le middleware prend les données et envoie une action normale.

Ainsi, la charge utile ici pourrait être ce qui a été retourné par l'API.

À partir de là, les choses se passent comme nous en avons l'habitude – un réducteur gère l'action, accepte l'état actuel et l'action, et retourne un nouvel état.

Le flux est le même que ce que nous avons appris jusqu'à présent – nous ajoutons simplement une étape supplémentaire entre les deux qui gère l'appel API.

C'est l'endroit logique pour le faire, car nous ne pouvons pas faire l'appel API dans nos composants puisque cela rendrait difficile la réutilisation du code, et nous ne pouvons pas faire l'appel API dans le réducteur car le réducteur est une fonction pure qui crée uniquement un nouvel état.

### Configurer l'API

Maintenant, nous allons connecter notre application à une API, afin que nous puissions pratiquer le travail avec les API dans Redux.

J'ai inclus une API préconstruite que nous utiliserons pour cela.

Si vous n'avez pas encore cloné le code source, vous pouvez le faire en ouvrant un terminal et en tapant :

```
Git clone https://github.com/chrisblakely01/react-redux-todo-app.git
```

Une fois que vous avez le code cloné, exécutez ce qui suit :

```
cd react-redux-todo-app/api
npm install
npm run server
```

Testez-le en allant sur **localhost:7000/todos** dans le navigateur, et vous devriez voir un tableau de todos retourné :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-09-at-08.08.31.png)

Notez que si vous arrêtez/démarrez le serveur, toutes les données que vous avez modifiées seront perdues car elles ne sont pas connectées à une base de données !

## Comment Obtenir les Todos depuis l'API

Commençons par obtenir les todos depuis l'API. Allez dans **todoSlice.js** et mettez-le à jour avec ce qui suit :

```
import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';

export const getTodosAsync = createAsyncThunk(
	'todos/getTodosAsync',
	async () => {
		const resp = await fetch('http://localhost:7000/todos');
		if (resp.ok) {
			const todos = await resp.json();
			return { todos };
		}
	}
);

export const todoSlice = createSlice({
	name: 'todos',
	initialState: [
		{ id: 1, title: 'todo1', completed: false },
		{ id: 2, title: 'todo2', completed: false },
		{ id: 3, title: 'todo3', completed: true },
		{ id: 4, title: 'todo4', completed: false },
		{ id: 5, title: 'todo5', completed: false },
	],
	reducers: {
		addTodo: (state, action) => {
			const todo = {
				id: new Date(),
				title: action.payload.title,
				completed: false,
			};
			state.push(todo);
		},
		toggleComplete: (state, action) => {
			const index = state.findIndex((todo) => todo.id === action.payload.id);
			state[index].completed = action.payload.completed;
		},
		deleteTodo: (state, action) => {
			return state.filter((todo) => todo.id !== action.payload.id);
		},
	},
    extraReducers: {
		[getTodosAsync.fulfilled]: (state, action) => {
			return action.payload.todos;
		},
	},
});

export const { addTodo, toggleComplete, deleteTodo } = todoSlice.actions;

export default todoSlice.reducer;

```

### Créer l'appel API/Thunk

La première chose que nous allons faire est d'importer la fonction createAsyncThunk et de créer notre thunk (ligne 3). Un thunk est une fonction qui retourne une autre fonction.

Ce thunk est la nouvelle action que nous envoyons depuis nos composants.

Cela va à son tour envoyer sa propre action lorsque la réponse est complète, avec les données de la réponse comme charge utile.

Nous devons passer certaines choses à la fonction createAsyncThunk, donc nous allons lui donner un nom, et passer une fonction qui utilise l'API fetch pour obtenir les données (ligne 4 / ligne 5).

Si la réponse est bonne, nous convertirons la réponse en JSON. La réponse revient sous forme de chaîne, donc nous devons la convertir en objet (ligne 8).

Enfin, nous retournerons un objet contenant nos todos. Rappelez-vous que l'API retourne un tableau de todos.

Une fois que la fonction retourne, elle enverra une action. Ce que nous retournons, dans ce cas un objet contenant le tableau de todo, sera la charge utile de l'action (ligne 9). Tout cela est fait en arrière-plan.

### Créer le Réducteur

Maintenant, nous devons implémenter la logique du réducteur qui gère cette action.

Nous le faisons dans l'objet extraReducers (ligne 39 dans l'extrait de code ci-dessus). C'est ici que nous spécifions des réducteurs supplémentaires que notre todoSlice peut utiliser.

La syntaxe est un peu différente, car notre thunk va envoyer un certain nombre d'actions.

L'action qui nous intéresse pour l'instant est l'action fulfilled. Lorsque le thunk envoie cette action, cela signifie que l'appel API dans notre thunk est terminé.

Ces réducteurs fonctionnent de la même manière que nos réducteurs simples – ils sont simplement une fonction qui accepte l'état actuel et la charge utile.

Maintenant, nous allons retourner les todos qui sont arrivés dans la charge utile, moment auquel Redux mettra à jour l'état pour nous.

Nous avons maintenant notre nouvelle action, et notre réducteur, nous devons simplement exporter notre thunk (ligne 3).

### Envoyer l'Action

Maintenant, nous devons déclencher l'action qui récupère le todo. Le meilleur endroit pour le faire est lorsque le composant TodoList est chargé pour la première fois.

Ouvrez TodoList.js et mettez-le à jour avec ce qui suit :

```jsx
import React, { useEffect } from 'react';
import TodoItem from './TodoItem';
import { useSelector, useDispatch } from 'react-redux';
import { getTodosAsync } from '../redux/todoSlice';

const TodoList = () => {
	const dispatch = useDispatch();
	const todos = useSelector((state) => state.todos);

	useEffect(() => {
		dispatch(getTodosAsync());
	}, [dispatch]);

	return (
		<ul className='list-group'>
			{todos.map((todo) => (
				<TodoItem id={todo.id} title={todo.title} completed={todo.completed} />
			))}
		</ul>
	);
};

export default TodoList;

```

Tout d'abord, nous allons importer le hook useDispatch, et l'assigner à une variable (ligne 7). 

Ensuite, nous importons l'action que nous voulons envoyer (ligne 4).

Nous voulons obtenir les Todos dès que le composant se charge, donc nous ajouterons le **hook useEffect** (ligne 10).

À partir de là, nous envoyons notre action (ligne 11).

Lorsque l'état dans le store est mis à jour, le hook useSelector est notifié et met à jour la variable todos avec les nouveaux todos pris de l'état.

Essayez cela et voyez-le en action !

## Comment Ajouter un Todo via l'API

Ensuite, nous allons voir comment créer un Todo et le persister sur l'API. Cela sera similaire à ce que nous avions avant, donc ouvrez **TodoSlice.js** et mettez-le à jour avec ce qui suit :

```jsx
import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';

export const getTodosAsync = createAsyncThunk(
	'todos/getTodosAsync',
	async () => {
		const resp = await fetch('http://localhost:7000/todos');
		if (resp.ok) {
			const todos = await resp.json();
			return { todos };
		}
	}
);

export const addTodoAsync = createAsyncThunk(
	'todos/addTodoAsync',
	async (payload) => {
		const resp = await fetch('http://localhost:7000/todos', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({ title: payload.title }),
		});

		if (resp.ok) {
			const todo = await resp.json();
			return { todo };
		}
	}
);

export const todoSlice = createSlice({
	name: 'todos',
	initialState: [],
	reducers: {
		addTodo: (state, action) => {
			const todo = {
				id: new Date(),
				title: action.payload.title,
				completed: false,
			};
			state.push(todo);
		},
		toggleComplete: (state, action) => {
			const index = state.findIndex((todo) => todo.id === action.payload.id);
			state[index].completed = action.payload.completed;
		},
		deleteTodo: (state, action) => {
			return state.filter((todo) => todo.id !== action.payload.id);
		},
	},
	extraReducers: {
		[getTodosAsync.fulfilled]: (state, action) => {
			return action.payload.todos;
		},
		[addTodoAsync.fulfilled]: (state, action) => {
			state.push(action.payload.todo);
		},
	},
});

export const { addTodo, toggleComplete, deleteTodo } = todoSlice.actions;

export default todoSlice.reducer;

```

### Créer l'appel API/Thunk

Nous créons un autre thunk, lui donnons un nom, et créons notre fonction asynchrone. Cette fois, nous passons le paramètre payload, car nous devons connaître le titre du Todo. Ce payload contient ce que le composant nous a envoyé lorsqu'il a envoyé l'action.

Utilisez l'API fetch, cette fois nous devons passer un objet avec une configuration pour indiquer que la requête fetch est un POST. Nous passerons le type de contenu et convertirons le corps en chaîne (ligne 17).

Maintenant, si la réponse est OK, l'API nous donnera un objet Todo avec un titre, un ID, et une valeur complétée.

Similaire à avant, si la réponse est ok, nous retournerons les données, qui dans ce cas est un seul objet todo. 

### Créer le Réducteur

Similaire à avant, ajoutez une fonction fulfilled, mettez à jour l'état en ajoutant ce todo au tableau des todos (ligne 56).

### Envoyer l'Action

Maintenant, ouvrez **AddTodoForm.js** et ajoutez ce qui suit :

```jsx
import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { addTodoAsync } from '../redux/todoSlice';

const AddTodoForm = () => {
	const [value, setValue] = useState('');
	const dispatch = useDispatch();

	const onSubmit = (event) => {
		event.preventDefault();
		if (value) {
			dispatch(
				addTodoAsync({
					title: value,
				})
			);
		}
	};

	return (
		<form onSubmit={onSubmit} className='form-inline mt-3 mb-3'>
			<label className='sr-only'>Name</label>
			<input
				type='text'
				className='form-control mb-2 mr-sm-2'
				placeholder='Add todo...'
				value={value}
				onChange={(event) => setValue(event.target.value)}
			></input>

			<button type='submit' className='btn btn-primary mb-2'>
				Submit
			</button>
		</form>
	);
};

export default AddTodoForm;

```

  
Notez que tout ce que nous faisons ici, c'est changer notre fonction onSubmit pour envoyer l'action **addTodoAsync** plutôt que l'action **addTodo** (ligne 13).

Maintenant, si vous essayez cela dans le navigateur en ajoutant un todo, vous remarquerez que le todo persiste – même après avoir actualisé la page !

## Comment Marquer un Todo comme Complété via l'API

J'espère que vous commencez à comprendre comment tout cela fonctionne, mais nous allons passer par un dernier exemple juste pour être sûr.

Nous devons appeler l'API pour mettre à jour la propriété "completed" lorsque l'utilisateur clique sur la case à cocher.

Allez dans **TodoSlice.js** et ajoutez ce qui suit :

```jsx
import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';

export const getTodosAsync = createAsyncThunk(
	'todos/getTodosAsync',
	async () => {
		const resp = await fetch('http://localhost:7000/todos');
		if (resp.ok) {
			const todos = await resp.json();
			return { todos };
		}
	}
);

export const addTodoAsync = createAsyncThunk(
	'todos/addTodoAsync',
	async (payload) => {
		const resp = await fetch('http://localhost:7000/todos', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({ title: payload.title }),
		});

		if (resp.ok) {
			const todo = await resp.json();
			return { todo };
		}
	}
);

export const toggleCompleteAsync = createAsyncThunk(
	'todos/completeTodoAsync',
	async (payload) => {
		const resp = await fetch(`http://localhost:7000/todos/${payload.id}`, {
			method: 'PATCH',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({ completed: payload.completed }),
		});

		if (resp.ok) {
			const todo = await resp.json();
			return { todo };
		}
	}
);

export const todoSlice = createSlice({
	name: 'todos',
	initialState: [],
	reducers: {
		addTodo: (state, action) => {
			const todo = {
				id: new Date(),
				title: action.payload.title,
				completed: false,
			};
			state.push(todo);
		},
		toggleComplete: (state, action) => {
			const index = state.findIndex((todo) => todo.id === action.payload.id);
			state[index].completed = action.payload.completed;
		},
		deleteTodo: (state, action) => {
			return state.filter((todo) => todo.id !== action.payload.id);
		},
	},
	extraReducers: {
		[getTodosAsync.fulfilled]: (state, action) => {
			return action.payload.todos;
		},
		[addTodoAsync.fulfilled]: (state, action) => {
			state.push(action.payload.todo);
		},
		[toggleCompleteAsync.fulfilled]: (state, action) => {
			const index = state.findIndex(
				(todo) => todo.id === action.payload.todo.id
			);
			state[index].completed = action.payload.todo.completed;
		},
	},
});

export const { addTodo, toggleComplete, deleteTodo } = todoSlice.actions;

export default todoSlice.reducer;

```

### Créer l'appel API/Thunk

Nous créons notre Async thunk comme d'habitude (ligne 32).

Cette fois, ce sera un PATCH, car nous mettons à jour une partie d'un objet. Nous passerons l'ID via l'URL, et nous passerons la valeur complétée prise de la charge utile.

La réponse nous donnera l'objet Todo mis à jour, donc nous retournerons cela qui sera passé au réducteur dans le cadre de l'action.

### Créer le Réducteur 

Maintenant, nous allons gérer l'action **toggleCompleteAsync.fulfilled**. 

Nous utilisons l'ID de la charge utile pour obtenir l'index, et mettons à jour le todo à cette position avec la nouvelle valeur complétée (ligne 77).

### Envoyer l'Action

Enfin, nous devons simplement envoyer notre nouvelle action. Allez dans TodoItem.js et mettez-le à jour avec ce qui suit :

```
import React from 'react';
import { useDispatch } from 'react-redux';
import { toggleCompleteAsync, deleteTodo } from '../redux/todoSlice';

const TodoItem = ({ id, title, completed }) => {
	const dispatch = useDispatch();

	const handleCheckboxClick = () => {
		dispatch(toggleCompleteAsync({ id, completed: !completed }));
	};

	const handleDeleteClick = () => {
		dispatch(deleteTodo({ id }));
	};

	return (
		<li className={`list-group-item ${completed && 'list-group-item-success'}`}>
			<div className='d-flex justify-content-between'>
				<span className='d-flex align-items-center'>
					<input
						type='checkbox'
						className='mr-3'
						onClick={handleCheckboxClick}
						checked={completed}
					></input>
					{title}
				</span>
				<button onClick={handleDeleteClick} className='btn btn-danger'>
					Delete
				</button>
			</div>
		</li>
	);
};

export default TodoItem;

```

Encore une fois, tout ce que nous faisons ici, c'est envoyer l'action **toggleCompleteAsync** depuis notre fonction de gestion d'événement (ligne 8).

Maintenant, si vous ouvrez cela dans le navigateur et cochez quelques todos comme complétés, vous remarquerez que l'état est sauvegardé même après avoir actualisé la page.

## Défi - Comment Supprimer un Todo via l'API

Un défi à pratiquer vous-même est de supprimer le todo via l'API ! L'API que j'ai fournie prend en charge la suppression des todos en passant un ID. Voici quelques conseils pour commencer.

Tout d'abord, vous devrez créer un async thunk/appel API similaire à ce que nous avons fait avant. La requête pour supprimer un Todo ressemblera à ceci :

```
const resp = await fetch(`http://localhost:7000/todos/${payload.id}`, {
	method: 'DELETE',
});
```

Ensuite, vous devrez ajouter un **réducteur** qui met à jour l'état lorsque la réponse est complète

Et vous devrez **envoyer une action** lorsque le bouton est cliqué, ce qui déclenchera le thunk que vous avez créé à l'étape 1.

Vous pouvez trouver la solution dans le code **final** sur GitHub !

## Merci d'avoir lu ! 

<a href="https://www.reactheroes.com">
<img src="https://i.ibb.co/rs79F7Z/Screenshot-2021-04-12-at-10-44-16.png" alt="Screenshot-2021-04-12-at-10-44-16" border="0">
</a>

##