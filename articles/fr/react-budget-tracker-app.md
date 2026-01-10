---
title: Créer une application de suivi de budget avec React – Apprendre React et l'API
  Context avec ce projet amusant
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2021-03-12T19:24:55.000Z'
originalURL: https://freecodecamp.org/news/react-budget-tracker-app
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/react-budget-app-1.png
tags:
- name: app development
  slug: app-development
- name: JavaScript
  slug: javascript
- name: projects
  slug: projects
- name: React
  slug: react
- name: React context
  slug: react-context
seo_title: Créer une application de suivi de budget avec React – Apprendre React et
  l'API Context avec ce projet amusant
seo_desc: "In this React Budget Tracker App tutorial we're going to:\n\nWe’ll learn\
  \ how break down a UI into React components\nLearn how to work with state using\
  \ the Context API\nLearn about actions, reducers, and the dispatch function \n\n\
  And I’ll give you some chal..."
---

Dans ce tutoriel sur l'application de suivi de budget avec React, nous allons :

* Apprendre à décomposer une interface utilisateur en composants React
* Apprendre à travailler avec l'état en utilisant l'API Context
* Découvrir les actions, les réducteurs et la fonction dispatch

Et je vous donnerai quelques défis que vous pourrez essayer à la fin !

## Voici ce que nous allons construire :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-07-at-09.20.33.png)

L'utilisateur peut :

* Ajouter des dépenses qui ont un nom et un coût
* Supprimer des dépenses
* Voir combien il reste de leur budget
* Voir combien ils ont dépensé jusqu'à présent
* (Défi) Modifier le budget
* (Défi) Rechercher des dépenses

## Présentation vidéo

[Voici une présentation vidéo si vous souhaitez compléter votre lecture (sur YouTube)](https://youtu.be/aeYxBd1it7I)

## Code source

Enfin, au cas où vous vous perdriez en suivant, [vous pouvez récupérer le code final ici (sur GitHub)](https://github.com/chrisblakely01/react-budget-app).

C'est parti !

## Comment configurer un projet React

La première chose que nous devons faire est de configurer un projet React. Pour cela, nous utiliserons `create-react-app`.

Ouvrez un terminal et tapez :

`npx create-react-app budget-tracker`

Lorsque cela aura fini de faire son travail, nous allons installer Bootstrap. Cela nous donnera des styles prêts à l'emploi que nous pourrons utiliser au lieu de devoir créer les nôtres en CSS.

Dans le même terminal, changez de répertoire de travail et installez Bootstrap :

```
cd budget-tracker
npm i bootstrap
```

Ensuite, nous allons installer un package qui nous permet de générer des ID. Nous utiliserons des ID pour identifier chaque dépense dans la liste, donc c'est important.

Exécutez la commande suivante dans votre répertoire de projet :

```
npm i uuid
```

Le dernier package que nous devons installer nous donne quelques icônes à utiliser, ce qui nous évite de devoir les créer nous-mêmes.

Exécutez la commande suivante dans votre répertoire de projet :

```
npm i react-icons
```

Ouvrez maintenant le projet dans VS Code (ou l'IDE que vous utilisez). Vous devriez voir certaines choses apparaître dans l'arborescence du projet (c'est notre projet React vide).

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-07-at-09.37.55-1.png)

Vous pouvez ignorer la plupart de ces éléments, car nous allons créer nos propres composants. Ouvrez App.js, supprimez tout et ajoutez ce qui suit :

```jsx
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const App = () => {
	return <p>Bonjour React !</p>;
};

export default App;
```

Ce que cela fait :

* Importe le CSS de Bootstrap dans notre projet
* Crée un composant qui affiche "Bonjour React !" avec des balises de paragraphe
* Exporte ce composant afin que d'autres composants puissent l'utiliser

Ensuite, nous allons lancer l'application et nous assurer que tout fonctionne comme il se doit. Ouvrez un terminal (soit dans VS Code, soit autre) et démarrez l'application en tapant ce qui suit :

```
npm start
```

Si tout se passe bien, l'application devrait démarrer et s'ouvrir dans un navigateur :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-07-at-09.45.18.png)

*Le texte "Bonjour React" devrait apparaître sur la page. Cela signifie que votre application fonctionne !*

Succès ! Maintenant, nous sommes prêts à commencer à construire nos composants React.

## Comment mettre en place les composants de l'interface utilisateur

Une approche pour construire des applications consiste à commencer par mettre en place les composants de l'interface utilisateur avec quelques données factices. Cela aide généralement à visualiser les objets d'état nécessaires et signifie généralement moins de retravail plus tard.

Avec cela en tête, nous allons mettre en place nos composants d'interface utilisateur en commençant par le haut et en descendant.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-07-at-10.04.55.png)

*Nous allons ajouter un titre, puis ajouter un nouveau composant pour chacune des "boîtes" affichées. Nous allons ajouter quelques données factices juste pour que les choses s'affichent correctement*

### Comment créer le composant Budget

Plongez dans le code, dans le dossier **src**, créez un nouveau dossier appelé **components**. À l'intérieur de celui-ci, créez un fichier appelé **Budget.js**. Votre structure de projet devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-07-at-10.13.37.png)

Ouvrez **Budget.js** et ajoutez ce qui suit :

```jsx
import React from 'react';

const Budget = () => {
	return (
		<div className='alert alert-secondary'>
			<span>Budget : £2000</span>
		</div>
	);
};

export default Budget;
```

Ce que nous faisons :

* Créer un nouveau composant appelé **Budget** (ligne 3)
* Utiliser les classes **Bootstrap Alert** pour nous donner un bel arrière-plan gris (ligne 5)
* Ajouter du texte et coder en dur une valeur (ligne 6)

### Comment créer le composant `Remaining`

Ensuite, nous allons créer le composant **`Remaining`**, qui montre combien de budget il reste à l'utilisateur.

Créez un nouveau fichier sous **src/components** appelé **Remaining.js**. Ouvrez-le et ajoutez ce qui suit :

```jsx
import React from 'react';

const Remaining = () => {
	return (
		<div className='alert alert-success'>
			<span>Restant : £1000</span>
		</div>
	);
};

export default Remaining;
```

Ce que nous faisons :

* Créer un nouveau composant appelé **Remaining** (ligne 3)
* Utiliser les classes **Bootstrap Alert** pour nous donner un arrière-plan vert (ligne 5)
* Ajouter du texte et coder en dur une valeur (ligne 6)
* Ajouter Dépensé jusqu'à présent

Enfin, nous allons créer le composant **Dépensé jusqu'à présent**, qui montre combien l'utilisateur a dépensé jusqu'à présent.

Créez un nouveau fichier sous **src/components** appelé **ExpenseTotal.js**. Ouvrez-le et ajoutez ce qui suit :

```jsx
import React from 'react';

const ExpenseTotal = () => {
	return (
		<div className='alert alert-primary'>
			<span>Dépensé jusqu'à présent : £1000</span>
		</div>
	);
};

export default ExpenseTotal;
```

Ce que nous faisons :

* Créer un nouveau composant appelé **ExpenseTotal** (ligne 3)
* Utiliser les classes **Bootstrap Alert** pour nous donner un arrière-plan bleu (ligne 5)
* Ajouter du texte et coder en dur une valeur (ligne 6)

### Comment ajouter un titre et rendre nos composants

À ce stade, vous pourriez penser : "Tous ces composants se ressemblent, qu'est-ce qui se passe ?!". C'est vrai, bien que rappelez-vous que nous ajoutons simplement quelques données codées en dur pour l'instant. Plus tard, chaque composant fera des choses différentes pour afficher les données dynamiquement.

Maintenant que nous avons créé nos composants, nous devons les rendre dans **App.js**. Ouvrez App.js et ajoutez ce qui suit :

```jsx
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Budget from './components/Budget';
import Remaining from './components/Remaining';
import ExpenseTotal from './components/ExpenseTotal';

const App = () => {
	return (
			<div className='container'>
				<h1 className='mt-3'>Mon Planificateur de Budget</h1>
				<div className='row mt-3'>
					<div className='col-sm'>
						<Budget />
					</div>
					<div className='col-sm'>
						<Remaining />
					</div>
					<div className='col-sm'>
						<ExpenseTotal />
					</div>
				</div>
			</div>
	);
};

export default App;
```

Ce que nous faisons :

* Importer nos différents composants (lignes 3-5)
* Ajouter un conteneur bootstrap qui nous aide à centrer notre application sur la page (ligne 9)
* Ajouter un titre (ligne 9)
* Ajouter une ligne Bootstrap (ligne 10)
* Ajouter une colonne dans la ligne pour chacun de nos composants jusqu'à présent (lignes 12-20)

Maintenant, si vous exécutez l'application, vous devriez voir le titre et nos composants rendus sur la page !

### Comment créer le composant Liste des dépenses

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-07-at-10.31.44.png)

*La liste des dépenses montre les dépenses que l'utilisateur a ajoutées jusqu'à présent, affichant le nom, le coût et un bouton de suppression pour chacune*

Ensuite, nous allons construire le composant **ExpenseList**. Ce composant sera responsable de prendre une liste de dépenses et de rendre un composant **ExpenseItem** pour chaque élément.

Nous allons ajouter quelques données factices, pour nous assurer que notre interface utilisateur a l'air bien et que les choses fonctionnent comme prévu. Plus tard, ces éléments proviendront du contexte.

Commencez par créer un nouveau fichier sous **src/components** appelé **ExpenseList.js**. Ouvrez ExpenseList.js et ajoutez ce qui suit :

```jsx
import React from 'react'
import ExpenseItem from './ExpenseItem';

const ExpenseList = () => {
    const expenses = [
		{ id: 12, name: 'shopping', cost: 40 },
		{ id: 13, name: 'holiday', cost: 400 },
		{ id: 14, name: 'car service', cost: 50 },
	];

    return (
		<ul className='list-group'>
			{expenses.map((expense) => (
				<ExpenseItem id={expense.id} name={expense.name} cost={expense.cost} />
			))}
		</ul>
    )
}

export default ExpenseList
```

Ce que nous faisons :

* Ajouter une liste factice de dépenses. Pour chaque dépense, nous avons besoin d'un ID, d'un nom et d'un coût. Plus tard, nous prendrons cette liste à partir du contexte (ligne 4)
* Créer une liste (ligne 11)
* Utiliser la fonction map pour itérer sur les dépenses et afficher un composant ExpenseItem (nous ne l'avons pas encore créé ! Ligne 12)
* Passer l'ID, le nom et le coût au composant ExpenseItem en tant que props

### Comment créer le composant Éléments de dépenses

Maintenant que nous avons créé un composant pour contenir notre liste, nous avons besoin d'un composant pour rendre chaque élément. Créez un nouveau fichier dans le dossier **src/components** appelé **ExpenseItem.js**. Ouvrez-le et ajoutez ce qui suit :

```jsx
import React from 'react';
import { TiDelete } from 'react-icons/ti';

const ExpenseItem = (props) => {
	return (
		<li className='list-group-item d-flex justify-content-between align-items-center'>
			{props.name}
			<div>
				<span className='badge badge-primary badge-pill mr-3'>
					£{props.cost}
				</span>
				<TiDelete size='1.5em'></TiDelete>
			</div>
		</li>
	);
};

export default ExpenseItem;
```

Ce que nous faisons :

* Créer un élément de liste (ligne 6)
* Rendre le nom de la dépense, que nous obtenons des props (ligne 7)
* Rendre le coût de la dépense, que nous obtenons également des props
* Nous affichons une DeleteIcon (ligne 12) que nous obtenons du package react-icons (ligne 2)

### Comment rendre le composant ExpenseList

Maintenant que nous avons créé nos composants, nous devons simplement rendre ExpenseList dans App.js. Ouvrez App.js et mettez-le à jour avec ce qui suit :

```jsx
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Budget from './components/Budget';
import Remaining from './components/Remaining';
import ExpenseTotal from './components/ExpenseTotal';
import ExpenseList from './components/ExpenseList';

const App = () => {
	return (
		<div className='container'>
			<h1 className='mt-3'>Mon Planificateur de Budget</h1>
			<div className='row mt-3'>
				<div className='col-sm'>
					<Budget />
				</div>
				<div className='col-sm'>
					<Remaining />
				</div>
				<div className='col-sm'>
					<ExpenseTotal />
				</div>
			</div>
			<h3 className='mt-3'>Dépenses</h3>
			<div className='row mt-3'>
				<div className='col-sm'>
					<ExpenseList />
				</div>
			</div>
		</div>
	);
};

export default App;
```

Ce qui est nouveau :

* Nous avons importé notre ExpenseList (ligne 6)
* Ajouté une nouvelle ligne Bootstrap (ligne 24)
* Rendu notre ExpenseList (ligne 26)

Maintenant, si vous enregistrez/exécutez l'application, vous verrez que la liste des dépenses est apparue !

### Comment créer le composant de formulaire "Ajouter une dépense"

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-08-at-07.28.29.png)

Nos composants d'interface utilisateur sont presque complets ! Le dernier composant dont nous avons besoin est le composant de formulaire "Ajouter une dépense", qui permet aux utilisateurs d'ajouter de nouvelles dépenses. Nous mettrons d'abord en place les composants d'interface utilisateur pour le formulaire, puis nous reviendrons plus tard pour ajouter les fonctionnalités avancées.

Créez un nouveau fichier dans **src/components** appelé **AddExpenseForm.js**. Ouvrez-le et ajoutez ce qui suit :

```jsx
import React from 'react';

const AddExpenseForm = () => {

	return (
		<form>
			<div className='row'>
				<div className='col-sm'>
					<label for='name'>Nom</label>
					<input
						required='required'
						type='text'
						className='form-control'
						id='name'
					></input>
				</div>
				<div className='col-sm'>
					<label for='cost'>Coût</label>
					<input
						required='required'
						type='text'
						className='form-control'
						id='cost'
					></input>
				</div>

			</div>
            <div className='row'>
            	<div className='col-sm'>
					<button type='submit' className='btn btn-primary mt-3'>
						Enregistrer
					</button>
				</div>
            </div>
		</form>
	);
};

export default AddExpenseForm;
```

Ce que nous faisons :

* Ajouter nos balises de formulaire (ligne 6)
* Ajouter une étiquette/entrée pour notre champ **nom** (ligne 9)
* Ajouter une étiquette/entrée pour notre champ **coût** (ligne 18)
* Ajouter un bouton pour soumettre le formulaire (ligne 30)

### Comment rendre le composant AddExpenseForm

Enfin, dans App.js, nous devons rendre notre nouveau composant. Mettez à jour App.js avec ce qui suit :

```
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Budget from './components/Budget';
import Remaining from './components/Remaining';
import ExpenseTotal from './components/ExpenseTotal';
import ExpenseList from './components/ExpenseList';
import AddExpenseForm from './components/AddExpenseForm';

const App = () => {
	return (
		<div className='container'>
			<h1 className='mt-3'>Mon Planificateur de Budget</h1>
			<div className='row mt-3'>
				<div className='col-sm'>
					<Budget />
				</div>
				<div className='col-sm'>
					<Remaining />
				</div>
				<div className='col-sm'>
					<ExpenseTotal />
				</div>
			</div>
			<h3 className='mt-3'>Dépenses</h3>
			<div className='row mt-3'>
				<div className='col-sm'>
					<ExpenseList />
				</div>
			</div>
			<h3 className='mt-3'>Ajouter une dépense</h3>
			<div className='row mt-3'>
				<div className='col-sm'>
					<AddExpenseForm />
				</div>
			</div>
		</div>
	);
};

export default App;
```

Ce qui a changé :

* Importé le AddExpenseForm (ligne 7)
* Rendu le AddExpenseForm (ligne 33)

## Comment ajouter l'API Context

L'API Context est ce que nous allons utiliser pour stocker notre état global. Elle fait déjà partie de la bibliothèque React, donc pas besoin d'importer/installer autre chose.

Commencez par créer un nouveau dossier dans le dossier **src** appelé **context**. À l'intérieur de ce dossier, créez un nouveau fichier appelé **AppContext.js**.

### Comment créer l'état initial

La première chose dont notre contexte a besoin pour fonctionner est un état initial. Cela indique la "forme" de notre état (en d'autres termes, quelles propriétés et données nous avons) et peut être utilisé pour initialiser l'application avec des données provenant d'un appel d'API, par exemple.

Pour l'instant, nous allons simplement ajouter quelques valeurs initiales. Dans AppContext.js, ajoutez ce qui suit :

```jsx
const initialState = {
	budget: 2000,
	expenses: [
		{ id: 12, name: 'shopping', cost: 40 },
		{ id: 13, name: 'holiday', cost: 400 },
		{ id: 14, name: 'car service', cost: 50 },
	],
};
```

* Nous ajoutons un budget initial
* Nous ajoutons une liste factice de dépenses

> REMARQUE : les propriétés de initialState n'ont pas besoin d'avoir des valeurs, elles peuvent être définies sur des chaînes vides, des tableaux vides, etc. Nous ajoutons des données à des fins visuelles

### Comment créer l'AppContext

Ensuite, nous allons créer l'AppContext. C'est la chose que nos composants importent et utilisent pour obtenir l'état.

Mettez à jour AppContext.js avec ce qui suit :

```jsx
const initialState = {
	budget: 2000,
	expenses: [
		{ id: 12, name: 'shopping', cost: 40 },
		{ id: 13, name: 'holiday', cost: 400 },
		{ id: 14, name: 'car service', cost: 50 },
	],
};

export const AppContext = createContext();
```

Tout ce que nous avons fait, c'est ajouter un appel à createContext à la ligne (11) - c'est notre objet de contexte créé !

### Comment créer l'AppProvider

Le fournisseur est un composant qui enveloppe les composants auxquels nous voulons passer l'état. Nous l'utilisons en conjonction avec le hook useReducer pour stocker réellement l'état global.

Mettez à jour le fichier AppContext.js comme suit :

```jsx
const initialState = {
	budget: 2000,
	expenses: [
		{ id: 12, name: 'shopping', cost: 40 },
		{ id: 13, name: 'holiday', cost: 400 },
		{ id: 14, name: 'car service', cost: 50 },
	],
};

export const AppContext = createContext();

export const AppProvider = (props) => {
	const [state, dispatch] = useReducer(AppReducer, initialState);

	return (
		<AppContext.Provider
			value={{
				budget: state.budget,
				expenses: state.expenses,
				dispatch,
			}}
		>
			{props.children}
		</AppContext.Provider>
	);
};
```

Ce que nous faisons :

* Créer notre composant Provider (ligne 12)
* Configurer le hook useReducer qui contiendra notre état et nous permettra de mettre à jour l'état via dispatch (REMARQUE : nous n'avons pas encore créé AppReducer ! Ligne 13)
* Nous retournons **AppContext.Provider**. Celui-ci a une prop **value** qui contient les données que nous permettons à nos composants de voir et d'avoir accès, ainsi que la fonction dispatch qui nous permet de mettre à jour l'état en dispatchant des actions (ligne 16)

### Comment créer l'AppReducer

Ensuite, nous allons créer l'AppReducer. Le réducteur est responsable de la création du nouvel objet d'état global, basé sur un type d'action et une charge utile.

Mettez à jour AppContext.js avec ce qui suit :

```jsx
const AppReducer = (state, action) => {
	switch (action.type) {
		default:
			return state;
	}
};

const initialState = {
	budget: 2000,
	expenses: [
		{ id: 12, name: 'shopping', cost: 40 },
		{ id: 13, name: 'holiday', cost: 400 },
		{ id: 14, name: 'car service', cost: 50 },
	],
};

export const AppContext = createContext();

export const AppProvider = (props) => {
	const [state, dispatch] = useReducer(AppReducer, initialState);

	return (
		<AppContext.Provider
			value={{
				budget: state.budget,
				expenses: state.expenses,
				dispatch,
			}}
		>
			{props.children}
		</AppContext.Provider>
	);
};
```

Ce que nous faisons :

* Créer une fonction qui accepte l'état actuel et une action (ligne 1)
* Nous utilisons un switch basé sur le type d'action pour décider comment mettre à jour l'état (ligne 2)
* Pour l'instant, puisque nous configurons simplement les choses, nous allons simplement retourner l'état par défaut et ajouter des actions plus tard au fur et à mesure que nous en avons besoin (ligne 3)

Et c'est tout ! Notre état global est maintenant configuré et prêt à l'emploi.

## Comment lier AppContext à notre App

L'étape suivante consiste à lier notre AppContext à notre composant App. Nous faisons cela en enveloppant les composants auxquels nous voulons passer l'état avec le AppProvider.

Retournez dans App.js et mettez à jour ce qui suit :

```jsx
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Budget from './components/Budget';
import Remaining from './components/Remaining';
import ExpenseTotal from './components/ExpenseTotal';
import ExpenseList from './components/ExpenseList';
import AddExpenseForm from './components/AddExpenseForm';
import { AppProvider } from './context/AppContext';

const App = () => {
	return (
		<AppProvider>
			<div className='container'>
				<h1 className='mt-3'>Mon Planificateur de Budget</h1>
				<div className='row mt-3'>
					<div className='col-sm'>
						<Budget />
					</div>
					<div className='col-sm'>
						<Remaining />
					</div>
					<div className='col-sm'>
						<ExpenseTotal />
					</div>
				</div>
				<h3 className='mt-3'>Dépenses</h3>
				<div className='row mt-3'>
					<div className='col-sm'>
						<ExpenseList />
					</div>
				</div>
				<h3 className='mt-3'>Ajouter une dépense</h3>
				<div className='row mt-3'>
					<div className='col-sm'>
						<AddExpenseForm />
					</div>
				</div>
			</div>
		</AppProvider>
	);
};

export default App;
```

Ce qui a changé :

* Importé notre **AppProvider** (ligne 8)
* Imbriqué nos composants dans l'élément AppProvider (lignes 12 / lignes 39)

Maintenant que nos composants sont imbriqués dans le AppProvider, ils ont accès à l'objet **value** que le AppProvider expose.

## Comment connecter nos composants à AppContext

### Comment rendre le budget à partir du contexte

Maintenant, nous pouvons commencer à extraire les valeurs de l'état global dans nos composants. Nous commencerons par le budget, alors plongez dans **Budget.js** et ajoutez ce qui suit :

```jsx
import React, { useContext } from 'react';
import { AppContext } from '../context/AppContext';

const Budget = () => {
	const { budget } = useContext(AppContext);

	return (
		<div className='alert alert-secondary'>
			<span>Budget : £{budget}</span>
		</div>
	);
};

export default Budget;
```

Ce que nous faisons :

* Nous devons importer **AppContext** de notre Contexte (ligne 2)
* Nous importons le hook **useContext** et passons notre AppContext - c'est ainsi qu'un composant se connecte au contexte afin d'obtenir des valeurs de l'état global
* Nous utilisons la **destructuration** pour obtenir le **budget** du contexte (ligne 5)
* Nous rendons le budget dans notre JSX (ligne 9)

Maintenant, si vous changez le budget dans AppContext et rechargez votre navigateur, vous verrez que le budget se met à jour sur l'interface utilisateur. Cela signifie que notre composant extrait avec succès les données de notre contexte. Succès !

### Comment rendre les dépenses à partir du contexte

Maintenant, nous pouvons faire quelque chose de similaire avec la liste des dépenses. Ouvrez **ExpenseList.js** et mettez-le à jour avec ce qui suit :

```jsx
import React, { useContext } from 'react';
import ExpenseItem from './ExpenseItem';
import { AppContext } from '../context/AppContext';

const ExpenseList = () => {
	const { expenses } = useContext(AppContext);

	return (
		<ul className='list-group'>
			{expenses.map((expense) => (
				<ExpenseItem id={expense.id} name={expense.name} cost={expense.cost} />
			))}
		</ul>
	);
};

export default ExpenseList;
```

Ce que nous faisons :

* Importer notre AppContext et le hook useContext comme avant
* Nous avons supprimé la liste factice des dépenses
* Nous avons remplacé la liste factice par la liste des dépenses que nous stockons dans le contexte

Puisque nous avons déjà fait le travail pour rendre la liste des dépenses, nous n'avons pas à faire autre chose ! Actualisez le navigateur et vous verrez que la liste provient maintenant du contexte plutôt que de la liste factice.

Rappelez-vous que nous avons exporté les dépenses dans le cadre de l'objet value dans le fournisseur. Tout composant enveloppé dans le fournisseur peut accéder à cet objet value et utiliser la destructuration pour obtenir la valeur spécifique dont il a besoin.

### Comment ajouter une nouvelle dépense - Capturer les valeurs du formulaire

Jusqu'à présent, nous avons vu comment obtenir des valeurs de l'état, ensuite nous verrons comment nous pouvons dispatcher des actions et mettre à jour l'état.

Avant de faire cela, nous devons connaître le **nom** et le **coût** de la nouvelle dépense que l'utilisateur a saisie. Plongez dans AddExpenseForm.js et ajoutez ce qui suit :

```jsx
import React, { useState } from 'react';

const AddExpenseForm = () => {
	const [name, setName] = useState('');
	const [cost, setCost] = useState('');

	const onSubmit = (event) => {

	};

	return (
		<form onSubmit={onSubmit}>
			<div className='row'>
				<div className='col-sm'>
					<label for='name'>Nom</label>
					<input
						required='required'
						type='text'
						className='form-control'
						id='name'
						value={name}
						onChange={(event) => setName(event.target.value)}
					></input>
				</div>
				<div className='col-sm'>
					<label for='cost'>Coût</label>
					<input
						required='required'
						type='text'
						className='form-control'
						id='cost'
						value={cost}
						onChange={(event) => setCost(event.target.value)}
					></input>
				</div>
				<div className='col-sm'>
					<button type='submit' className='btn btn-primary mt-3'>
						Enregistrer
					</button>
				</div>
			</div>
		</form>
	);
};

export default AddExpenseForm;
```

Ce que nous faisons :

* Utiliser React pour contrôler les **valeurs d'entrée**. Pour chaque champ d'entrée, nous avons un objet d'état (lignes 7 et 8)
* Lorsque l'utilisateur tape dans les entrées, les valeurs d'état correspondantes seront mises à jour (lignes 25 et 36)
* Lorsque l'utilisateur clique sur le bouton, il appellera une fonction **onSubmit**. Cette fonction ne fait rien pour l'instant, mais c'est ici que nous dispatcherons l'action

Maintenant que nous avons les valeurs du formulaire stockées dans l'état, nous pouvons dispatcher une action pour mettre à jour l'état.

### Comment ajouter une nouvelle dépense - Dispatcher une action

Mettez à jour le AddExpenseForm avec ce qui suit :

```jsx
import React, { useContext, useState } from 'react';
import { AppContext } from '../context/AppContext';
import { v4 as uuidv4 } from 'uuid';

const AddExpenseForm = () => {
	const { dispatch } = useContext(AppContext);

	const [name, setName] = useState('');
	const [cost, setCost] = useState('');

	const onSubmit = (event) => {
		event.preventDefault();

		const expense = {
			id: uuidv4(),
			name: name,
			cost: parseInt(cost),
		};

		dispatch({
			type: 'ADD_EXPENSE',
			payload: expense,
		});
	};

	return (
		<form onSubmit={onSubmit}>
			<div className='row'>
				<div className='col-sm'>
					<label for='name'>Nom</label>
					<input
						required='required'
						type='text'
						className='form-control'
						id='name'
						value={name}
						onChange={(event) => setName(event.target.value)}
					></input>
				</div>
				<div className='col-sm'>
					<label for='cost'>Coût</label>
					<input
						required='required'
						type='text'
						className='form-control'
						id='cost'
						value={cost}
						onChange={(event) => setCost(event.target.value)}
					></input>
				</div>
				<div className='col-sm'>
					<button type='submit' className='btn btn-primary mt-3'>
						Enregistrer
					</button>
				</div>
			</div>
		</form>
	);
};

export default AddExpenseForm;
```

Ce que nous faisons :

* Importer AppContext et useContext comme d'habitude
* Obtenir **dispatch** de notre état global (ligne 6)
* Créer un **objet de dépense**, contenant le nom et le coût. C'est ce qui sera dispatché comme charge utile et ce que nous utiliserons pour mettre à jour l'état. Nous utilisons également le package uuid que nous avons importé précédemment pour créer un ID. Cela est utilisé pour identifier une dépense donnée (ligne 14).
* Nous dispatchons une **action**, avec un type et notre charge utile. Le type indique au réducteur comment mettre à jour l'état, ce que nous verrons dans une minute (ligne 20)

### Comment ajouter une nouvelle dépense - Mettre à jour le réducteur

C'est tout du côté du composant. Vous remarquerez que si vous exécutez cela dans le navigateur, rien ne se passe. C'est parce que nous n'avons pas mis à jour notre réducteur pour gérer l'action et mettre à jour l'état.

Plongez dans **AppContext.js** et mettez à jour la fonction **reducer** avec ce qui suit :

```jsx
const AppReducer = (state, action) => {
	switch (action.type) {
		case 'ADD_EXPENSE':
			return {
				...state,
				expenses: [...state.expenses, action.payload],
			};
		default:
			return state;
	}
};
```

Ce que nous faisons :

* Nous vérifions le type de l'action (que nous obtenons de la variable action) (ligne 2)
* Ajouter un nouveau cas à l'instruction switch appelé "ADD_EXPENSE" (ligne 3)
* Retourner un nouvel objet d'état avec la nouvelle dépense prise de la charge utile (que nous obtenons de la variable action) (ligne 4)

> Lorsque nous retournons quelque chose d'une instruction de cas, le réducteur met automatiquement à jour l'état et réaffiche les composants, presque comme par magie.

Maintenant, si vous exécutez le code et ajoutez une nouvelle dépense, vous pouvez voir qu'elle est ajoutée à la liste des dépenses !

### Comment calculer `dépensé jusqu'à présent`

La prochaine chose que nous allons voir est comment calculer combien l'utilisateur a dépensé jusqu'à présent. Pour cela, nous allons prendre un total de toutes les dépenses que l'utilisateur a engagées et l'afficher sur l'interface utilisateur.

Ouvrez **ExpenseTotal.js** et mettez-le à jour avec ce qui suit :

```jsx
import React, { useContext } from 'react';
import { AppContext } from '../context/AppContext';

const ExpenseTotal = () => {
	const { expenses } = useContext(AppContext);

	const totalExpenses = expenses.reduce((total, item) => {
		return (total += item.cost);
	}, 0);

	return (
		<div className='alert alert-primary'>
			<span>Dépensé jusqu'à présent : £{totalExpenses}</span>
		</div>
	);
};

export default ExpenseTotal;
```

Ce que nous faisons :

* Importer notre useContext et AppContext comme d'habitude
* Prendre les dépenses de l'état (ligne 5)
* Utiliser la fonction reduce pour obtenir un total de tous les coûts et assigner cela à une variable (ligne 7)
* Afficher la variable dans notre JSX (ligne 13)

Maintenant, chaque fois que l'utilisateur ajoute une dépense, cela provoque la mise à jour de l'état, ce qui provoquera le réaffichage de tous les composants connectés au contexte et leur mise à jour avec de nouvelles valeurs.

Allez-y et essayez cela dans le navigateur.

### Comment calculer `Restant`

Maintenant, nous allons voir comment calculer combien de budget il reste à l'utilisateur pour dépenser.

Pour cela, nous allons obtenir les coûts totaux des dépenses et les soustraire du budget. Si l'utilisateur dépasse le budget, c'est-à-dire que les dépenses sont supérieures au budget, nous voulons afficher un fond rouge (par opposition à un fond vert). Heureusement, Bootstrap nous donne déjà ces belles choses.

Ouvrez Remaining.js et mettez-le à jour avec ce qui suit :

```jsx
import React, { useContext } from 'react';
import { AppContext } from '../context/AppContext';

const Remaining = () => {
	const { expenses, budget } = useContext(AppContext);

	const totalExpenses = expenses.reduce((total, item) => {
		return (total = total + item.cost);
	}, 0);

	const alertType = totalExpenses > budget ? 'alert-danger' : 'alert-success';

	return (
		<div className={`alert ${alertType}`}>
			<span>Restant : £{budget - totalExpenses}</span>
		</div>
	);
};

export default Remaining;
```

Ce que nous faisons

* Importer les dépenses et le budget du Contexte (ligne 5)
* Obtenir le coût total des dépenses en utilisant la fonction reduce (ligne 7)
* Créer une variable pour stocker le nom de la classe CSS que nous voulons afficher (selon si l'utilisateur a dépassé le budget ou non, ligne 11)
* Utiliser une chaîne de modèle pour créer nos classes (ligne 14)
* Afficher le budget restant en utilisant une soustraction (ligne 15)

Maintenant, si vous exécutez le code dans le navigateur et ajoutez un tas de dépenses jusqu'à ce que le total dépasse 2000, vous verrez que l'arrière-plan du composant "Restant" devient rouge !

### Comment supprimer une dépense

La dernière chose que nous verrons avant de passer aux défis est de supprimer une dépense.

Lorsque l'utilisateur clique sur la petite croix à côté d'une dépense, nous voulons dispatcher une action pour la supprimer de l'état. Lorsque cela se produit, notre ExpenseList se réaffichera avec la dépense supprimée.

Plongez dans ExpenseItem.js et mettez-le à jour avec ce qui suit :

```jsx
import React, { useContext } from 'react';
import { TiDelete } from 'react-icons/ti';
import { AppContext } from '../context/AppContext';

const ExpenseItem = (props) => {
	const { dispatch } = useContext(AppContext);

	const handleDeleteExpense = () => {
		dispatch({
			type: 'DELETE_EXPENSE',
			payload: props.id,
		});
	};

	return (
		<li className='list-group-item d-flex justify-content-between align-items-center'>
			{props.name}
			<div>
				<span className='badge badge-primary badge-pill mr-3'>
					£{props.cost}
				</span>
				<TiDelete size='1.5em' onClick={handleDeleteExpense}></TiDelete>
			</div>
		</li>
	);
};

export default ExpenseItem;
```

Ce que nous faisons :

* Importer dispatch du Contexte, ce qui nous permet de dispatcher une action de suppression (ligne 6)
* Créer une fonction qui est appelée lorsque l'icône de suppression est cliquée (ligne 8)
* Dispatcher une action. Notre action contient le type (afin que le réducteur sache comment mettre à jour l'état) et la charge utile. Dans ce cas, nous passons l'ID de cette dépense (que nous obtenons des props lorsque nous avons rendu ExpenseList) (ligne 9)

Si vous essayez cela dans le navigateur, vous verrez que rien ne se passe. Même si nous dispatchons une action, nous n'avons pas implémenté la logique du réducteur pour ce type d'action, donc il ne sait pas comment mettre à jour l'état.

Plongez dans AppContext.js et mettez à jour la fonction du réducteur avec ce qui suit :

```jsx
const AppReducer = (state, action) => {
	switch (action.type) {
		case 'ADD_EXPENSE':
			return {
				...state,
				expenses: [...state.expenses, action.payload],
			};
		case 'DELETE_EXPENSE':
			return {
				...state,
				expenses: state.expenses.filter(
					(expense) => expense.id !== action.payload
				),
			};
		default:
			return state;
	}
};
```

Tout ce que nous faisons vraiment ici, c'est ajouter une nouvelle instruction de cas, pour gérer notre action **DELETE_EXPENSE**. Nous utilisons la méthode de filtrage de tableau pour supprimer la dépense qui a l'ID que nous avons reçu de la charge utile.

Maintenant, si vous essayez cela, vous pouvez supprimer une dépense en cliquant sur l'icône de suppression. Remarquez comment tous les autres composants se mettent également à jour. Bien !

## Défis à essayer

Félicitations pour être arrivé jusqu'ici ! Maintenant, c'est à vous d'essayer quelques défis. N'oubliez pas que vous pouvez voir comment je l'ai fait dans le code source GitHub.

### Permettre à l'utilisateur de modifier le budget

Vous remarquerez que jusqu'à présent, nous avons utilisé une valeur codée en dur pour le budget. Votre première tâche consiste à ajouter une fonctionnalité qui permet à l'utilisateur de modifier le budget. Voici quelques conseils pour commencer :

* Vous devrez ajouter une entrée de texte qui permet à l'utilisateur de saisir une valeur pour leur budget souhaité.
* Nous stockons le budget dans l'état, vous devrez donc dispatcher une action avec un nouveau TYPE et une CHARGE UTILE qui mettra à jour l'état.

### Permettre à l'utilisateur de rechercher une dépense

Si l'utilisateur a de nombreuses dépenses, il sera difficile de trouver celle qu'il recherche. Ajoutez un moyen pour l'utilisateur de rechercher la dépense par nom. Voici quelques conseils pour commencer :

* Vous devrez ajouter un champ d'entrée qui permet à l'utilisateur de saisir une valeur à rechercher.
* Vous devrez ajouter quelque chose au composant ExpenseList qui filtre la liste du contexte en fonction de cette valeur de recherche.

### Merci d'avoir lu !

[![](https://www.freecodecamp.org/news/content/images/size/w1000/2021/03/Screenshot-2021-03-10-at-08.33.56.png)](https://reactbeginnerprojects.com)