---
title: Comment construire une application de tâches améliorée par l'IA avec React
  et Appwrite
subtitle: ''
author: Fatuma Abdullahi
co_authors: []
series: null
date: '2024-03-13T09:21:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-task-app
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Group-3--20-.png
tags:
- name: AI
  slug: ai
- name: Appwrite
  slug: appwrite
- name: crud
  slug: crud
- name: projects
  slug: projects
- name: React
  slug: react
seo_title: Comment construire une application de tâches améliorée par l'IA avec React
  et Appwrite
seo_desc: "In this article, you'll build a task manager application that has some\
  \ artificial intelligence capabilities and is voice-enabled, sortable, and searchable.\
  \ \nAs an extra, the application will have dark mode support that respects the users'\
  \ system pref..."
---

Dans cet article, vous allez construire une application de gestion de tâches qui possède certaines capacités d'intelligence artificielle et est compatible avec la voix, triable et recherchable. 

En plus, l'application aura un support pour le mode sombre qui respecte les préférences système des utilisateurs.

L'application sera capable de créer, lire, mettre à jour et supprimer (CRUD) des tâches ainsi que la capacité de visualiser une tâche donnée.  

Vous allez construire cette application en utilisant Appwrite comme backend, React sur le frontend, Typescript pour la sécurité des types et Tailwind CSS pour le style.

## Table des matières

<ul>
    <li><a href="#prerequisites">Prérequis</a></li>
    <li><a href="#what-is-appwrite">Qu'est-ce qu'Appwrite ?</a></li>
    <li><a href="#heading-installation">Comment installer le backend Appwrite</a></li>
    <li><a href="#how-to-set-up-the-react-frontend">Comment installer le frontend React</a></li>
    <li><a href="#how-to-connect-to-the-appwrite-project">Comment se connecter au projet Appwrite</a></li>
    <li><a href="#how-to-build-the-task-manager-application">Comment construire l'application de gestion de tâches</a>
        <ul>
            <li><a href="#how-to-set-up-routing-with-react-router-v6">Comment configurer le routage avec React Router V6</a></li>
            <li><a href="#how-to-create-the-form-component">Comment créer le composant de formulaire</a></li>
            <li><a href="#how-to-set-up-form-to-create-task">Comment configurer le formulaire pour créer une tâche</a></li>
            <li><a href="#how-to-make-the-tasks-editable">Comment rendre les tâches modifiables</a></li>
            <li><a href="#how-to-enable-viewing-of-tasks">Comment activer la visualisation des tâches</a></li>
            <li><a href="#how-to-auto-generate-descriptions-with-vercel-s-ai-sdk">Comment générer automatiquement des descriptions avec le SDK IA de Vercel</a></li>
            <li><a href="#voice-enable-the-application-with-the-react-speech-recognition-package">Activer la voix dans l'application avec le package React Speech Recognition</a></li>
            <li><a href="#how-to-add-search-functionality-to-the-application">Comment ajouter une fonctionnalité de recherche à l'application</a></li>
            <li><a href="#how-to-add-ability-to-sort-tasks-via-due-date-and-priorityadd-ability-to-sort-tasks-via-due-date-and-priority">Comment ajouter la capacité de trier les tâches par date d'échéance et priorité</a></li>
            <li><a href="#bonus-add-dark-mode-support">Bonus : Ajouter le support du mode sombre</a></li>

        </ul>
    </li>
    <li><a href="#notes">Notes</a></li>
    <li><a href="#limitations">Limitations</a></li>
</ul>



## [Prérequis](#heading-prerequisites-1)

Vous aurez besoin des éléments suivants pour pouvoir construire cette application :

* Connaissances de base en programmation
* Compréhension de base de React, Typescript et Tailwind
* [Un compte Appwrite](https://appwrite.io/)
* Et un éditeur de texte pour coder

## Qu'est-ce qu'Appwrite ?

Appwrite est une plateforme [open source](https://opensource.com/resources/what-open-source) Backend-as-a-Service (BaaS). Un BaaS est un service cloud qui regroupe les tâches backend généralement nécessaires pour la plupart des applications. 

Appwrite offre à la fois une base de données gérée, une authentification, des fonctions et des services de stockage, ainsi que la possibilité d'auto-héberger l'ensemble de la plateforme sur votre propre infrastructure. 

Appwrite a récemment annoncé une série de nouvelles fonctionnalités qui simplifient la vie des développeurs construisant sur leur plateforme. Vous pouvez en lire plus sur cela [ici](https://appwrite.io/init). 

## Comment installer le backend Appwrite

Avant de commencer à construire l'application et à interagir avec Appwrite, vous aurez besoin d'un compte Appwrite et de configurer le projet.

Une fois que vous avez le compte prêt, vous devrez créer une organisation, puis créer un projet au sein de cette organisation. Vous pouvez nommer le projet "Tasks App" ou tout autre nom qui vous semble approprié. 

**Note :** Appwrite cloud vous limite à une organisation par compte sur le plan hobby/gratuit. Si vous aviez déjà une organisation, vous pouvez passer directement à la création d'un projet au sein de votre organisation existante.

Dans votre projet Tasks App, ajoutez une plateforme web et suivez les invites. Pour le nom d'hôte, ajoutez "localhost" pour l'instant. Cela permet au frontend de contourner [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) lors de l'interaction avec le backend Appwrite.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-08-at-14.44.11.png)
_Une image de la console Appwrite montrant la section "Add a platform"_

Copiez les instructions d'installation au fur et à mesure que vous terminez la configuration de la plateforme web pour le projet. Conservez-les en sécurité, vous en aurez besoin lors de la configuration du frontend. 

Vous devriez maintenant être dans la console cloud Appwrite. Cliquez sur "Databases" dans la barre latérale de gauche. Ensuite, cliquez sur le bouton rose "Create database". Nommez votre base de données et laissez l'ID autogénéré tel quel.  

Maintenant, cliquez sur le bouton "Create collection", nommez votre collection "tasks" et laissez l'ID autogénéré tel quel. Maintenant, cliquez sur le bouton gris "Create attribute" comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-08-at-15.00.42.png)
_Une image de la console Appwrite montrant le bouton "Create attribute"_

Ajoutez les attributs suivants : 

* title de type String, donnez-lui une taille de 49 et rendez-le requis
* description de type String, donnez-lui une taille de 200
* due_date de type Datetime, rendez-le requis
* done de type Boolean, donnez-lui une valeur par défaut de False
* priority de type String, donnez-lui une taille de 10

Enfin, vous devez définir les permissions afin que votre frontend React puisse interagir avec les services Appwrite. Dans ce cas, autorisez n'importe qui à avoir accès. Ce n'est pas idéal pour la production et vous pouvez en lire plus sur les permissions Appwrite [ici](https://appwrite.io/docs/advanced/platform/permissions).

Allez dans la console, cliquez sur databases, puis sur votre base de données de tâches et ensuite sur votre collection de tâches, puis cliquez sur settings et faites défiler vers le bas jusqu'aux permissions. Ajoutez des permissions pour le rôle "Any" et donnez-leur un accès CRUD complet.

Vous êtes maintenant prêt à commencer à configurer le frontend et à le connecter au projet Appwrite que vous venez de terminer de préparer.

## Comment installer le frontend React

Ouvrez votre éditeur de texte à l'emplacement de votre choix. Ensuite, ouvrez le terminal intégré et exécutez la commande suivante pour créer une application basée sur Vite : 

```terminal
 
//taskwrite est le nom de l'application
npm create vite@latest taskwrite 
```

Choisissez React puis Typescript simple lorsque vous y êtes invité. Cela créera une application React avec Typescript déjà configuré pour vous. 

Changez de dossier dans le nouveau dossier "taskwrite" en exécutant `cd taskwrite` depuis le terminal. Exécutez la commande suivante dans la même fenêtre de terminal pour ajouter Tailwind à l'application :

```terminal

npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Ensuite, dans votre fichier **tailwind.config.js** qui se trouve à la racine de l'application Taskwrite, remplacez la clé "content" par `content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],`. Le fichier devrait ressembler à ceci :

```javascript

/** @type {import('tailwindcss').Config} */
export default {
	content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
	theme: {
		extend: {},
	},
	plugins: [],
};    
```

Cela indique à Tailwind qu'il doit rechercher ses classes dans le fichier index.html à la racine et dans les fichiers du dossier **src** qui se terminent par les extensions `.js`, `.ts`, `.jsx` ou `.tsx`.

Ouvrez ensuite le dossier **src** et supprimez le fichier "App.css". Ouvrez le fichier **index.css** et remplacez son contenu par ce qui suit : 

```css

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@100..900&family=Quicksand:wght@300..700&display=swap');
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
    :root{
        --base-bg: #ffffff;
        --btn-bg-primary: #be185d;
        --btn-bg-primary-hover: #9d174d;
        --btn-icon-main: #1e293b;
        --btn-bg-ok: #4ade80;
        --btn-bg-light-ok: #bbf7d0;
        --btn-bg-light: #e5e7eb;
        --low-priority: #facc15;
        --medium-priority: #fb923c;
        --high-priority: #f87171;
        --text-error: #dc2626;
        --text-ok: #16a34a;
        --text-main: #262626;
        --border-container: #9ca3af;
        --border-input: #1e293b;
        --border-error: #dc2626;
    }

    body{
        background-color: var(--base-bg);
        color: var(--text-main);    
    }

    #date::-webkit-calendar-picker-indicator {
        background-color: var(--btn-bg-light); 
    }
}




```

Cela ajoute quelques variables CSS personnalisées à l'application. Les variables mappent aux couleurs Tailwind. 

Ensuite, collez ce qui suit dans le fichier **tailwind.config.js** à la racine de l'application :

```typescript

/** @type {import('tailwindcss').Config} */
export default {
	content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
	theme: {
		extend: {
			textColor: {
				error: "var(--text-error)",
				ok: "var(--text-ok)",
				main: "var(--text-main)",
				iconColor: "var(--btn-icon-main)",
			},
			backgroundColor: {
				base: "var(--base-bg)",
				primary: "var(--btn-bg-primary)",
				primaryHover: "var(--btn-bg-primary-hover)",
				ok: "var(--btn-bg-ok)",
				lightOk: "var(--btn-bg-light-ok)",
				light: "var(--btn-bg-light)",
				lowPriority: "var(--low-priority)",
				mediumPriority: "var(--medium-priority)",
				highPriority: "var(--high-priority)",
			},
			borderColor: {
				container: "var(--border-container)",
				input: "var(--border-input)",
				error: "var(--border-error)",
			},
		},
	},
	plugins: [],
};

```

Cela lie les variables CSS à la configuration tailwind et les rend disponibles pour une utilisation dans notre application.

Maintenant, Taskwrite est configuré avec React, Typescript et Tailwind.

## Comment se connecter au projet Appwrite

Tout d'abord, vous devez ajouter la dépendance Appwrite à l'application React. Exécutez la commande suivante dans la fenêtre du terminal pour cela : `npm i appwrite`.

La prochaine chose à faire est de configurer les clés Appwrite dont nous avons besoin en tant que variables d'environnement. Dans le fichier **.gitignore** à la racine de l'application, ajoutez `*.env` en haut du fichier puis enregistrez. Cela garantira que le fichier **.env** que vous allez créer ne sera pas ajouté au contrôle de version. 

Maintenant, créez un fichier **.env** à la racine de l'application React et collez les variables suivantes dedans :

```env

//remplacez le côté droit du signe égal par les valeurs correctes de votre projet Appwrite.
VITE_APPWRITE_URL=YOUR-APPWRITE-API-ENDPOINT
VITE_APPWRITE_PROJ_ID=YOUR-APPWRITE-PROJECT-ID
```

Vous pouvez obtenir les valeurs nécessaires dans votre console Appwrite. Cliquez sur l'onglet des paramètres en bas de la barre latérale de gauche et copiez les informations d'identification de l'API. 

Ensuite, créez un dossier utils dans le dossier **src** de l'application React. Ajoutez un fichier appelé **appwrite.ts** à l'intérieur et collez les informations de configuration suivantes :

```typescript

import { Client, Databases } from "appwrite";

export const client = new Client();

client
	.setEndpoint(import.meta.env.VITE_APPWRITE_URL)
	.setProject(import.meta.env.VITE_APPWRITE_PROJ_ID);

export const databases = new Databases(client);

export { ID } from "appwrite";
```

Vous êtes prêt à tester que l'application React est connectée au projet Appwrite. Remplacez tout dans le fichier **App.tsx** dans le dossier **src** par le code suivant :

```typescript

import { client } from "./utils/appwrite";

const App = () => {
	console.log("Appwrite", client);
	return <div className="text-purple-500 text-center font-bold text-	  5xl">App</div>;
};

export default App;
```

Ensuite, ouvrez une fenêtre de terminal intégré et exécutez la commande suivante : `npm run dev`. Cela exécutera votre application React à cette URL : [http://localhost:5173/](http://localhost:5173/). Ouvrez l'URL dans une fenêtre de navigateur et ouvrez la console du navigateur. 

Vous devriez voir un grand texte violet "App" au centre de l'écran et le client Appwrite enregistré dans la console comme suit : 

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-08-at-16.36.36.png)
_L'application web s'exécutant dans le navigateur_

Maintenant, vous devez récupérer l'ID de la base de données et l'ID de la collection depuis la console Appwrite. Cliquez sur l'onglet des bases de données dans la barre latérale de gauche, survolez la valeur de l'ID de la base de données et cliquez pour la copier. 

Retournez à votre fichier **.env** et ajoutez une entrée comme suit :

```env

//remplacez le côté droit du signe égal par les valeurs correctes de votre projet Appwrite.
VITE_APPWRITE_URL=YOUR-APPWRITE-API-ENDPOINT
VITE_APPWRITE_PROJ_ID=YOUR-APPWRITE-PROJECT-ID
//nouvelle entrée ci-dessous
VITE_APPWRITE_DB_ID=YOUR-APPWRITE-DB-ID
```

Enfin, retournez à la console et cliquez à travers la base de données pour accéder aux collections. Survolez et copiez l'ID de la collection comme avant, puis ajoutez-le juste en dessous de l'ID de la base de données dans votre fichier env comme suit : 

```env

VITE_APPWRITE_DB_ID=YOUR-APPWRITE-DB-ID
VITE_APPWRITE_COLLECTION_ID=YOUR-APPWRITE-COLLECTION-ID
```

Avec cela, la partie installation de la construction de Taskwrite est terminée.

## Comment construire l'application de gestion de tâches

Pour faciliter le travail avec Typescript, vous devrez ajouter des interfaces qui correspondent à la forme de la réponse de la base de données Appwrite. 

Dans votre dossier **src**, créez un dossier appelé **models** et à l'intérieur, créez un fichier appelé **interface.ts**. Collez ce qui suit dans le fichier :

```typescript

import { Models } from "appwrite";

export interface IPayload {
	title: string;
	description: string;
	due_date: Date;
	priority?: string;
	done?: boolean;
}

export interface ITask extends Models.Document {
	title: string;
	description: string;
	due_date: Date;
	priority?: string;
	done: boolean;
}

```

Ici, vous définissez une interface appelée "IPayload" avec les mêmes attributs que la tâche que nous avons définie dans le projet Appwrite. Ensuite, vous définissez une autre interface appelée "ITask" qui étend le modèle de base intégré de Appwrite. 

Cela signifie que ITask possède à la fois les attributs de la tâche que nous avons définie précédemment et les attributs de base intégrés que les collections Appwrite comportent.

Ensuite, dans votre dossier **utils**, ajoutez un fichier appelé **db.ts** et collez ce qui suit dedans :

```typescript

import { ID, databases } from "./appwrite";
import { IPayload } from "../models/interface";

const dbID: string = import.meta.env.VITE_APPWRITE_DB_ID;
const collectionID: string = import.meta.env.VITE_APPWRITE_COLLECTION_ID;

const createDocument = async (payload: IPayload) => {
	const res = await databases.createDocument(dbID, collectionID, ID.unique(), {
		...payload,
	});

	return res;
};

const readDocuments = async () => {
	const res = await databases.listDocuments(dbID, collectionID);

	return res;
};

const updateDocument = async (payload: IPayload, id: string) => {
	const res = await databases.updateDocument(dbID, collectionID, id, {
		...payload,
	});

	return res;
};
const deleteDocument = async (id: string) => {
	const res = await databases.deleteDocument(dbID, collectionID, id);

	return res;
};

export { createDocument, readDocuments, updateDocument, deleteDocument };
```

Ce fichier définit quatre fonctions correspondant aux opérations CRUD. Le nom des fonctions correspond à l'opération qu'elles effectuent. Pour toutes les fonctions, vous passez les ID de la collection et de la base de données afin qu'Appwrite sache quelles ressources utiliser.

Pour créer une tâche dans la base de données Appwrite, vous passez un objet avec la forme d'une tâche à la fonction et lui demandez de créer un ID unique pour chaque nouvelle tâche qu'elle crée. 

Pour mettre à jour une tâche, vous lui passez un objet de tâche similaire à la création, mais vous lui passons également l'ID unique de la tâche à mettre à jour.

Pour lire toutes les tâches depuis Appwrite, vous appelez la fonction "listDocuments" et pour supprimer une tâche, vous passez l'ID correspondant à la tâche à supprimer.

### Comment configurer le routage avec React Router V6

L'application Taskwrite aura deux routes et un menu de navigation pour faciliter cela. Pour ajouter la navigation, ouvrez un terminal intégré et exécutez la commande suivante pour installer la bibliothèque React Router : `npm i react-router-dom`.

Maintenant, allez dans le fichier **main.tsx** dans le dossier **src** et collez ce qui suit dedans : 

```typescript

import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App.tsx";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")!).render(
	<React.StrictMode>
		<BrowserRouter>
			<App />
		</BrowserRouter>
	</React.StrictMode>
);
```

Ensuite, allez dans le fichier **App.tsx** dans le dossier **src** et collez ce qui suit dedans :

```typescript

import "./index.css";
import { Route, Routes } from "react-router-dom";
import Task from "./routes/Task";
import Index from "./routes/Index";
import Navbar from "./components/Navbar";

function App() {
	return (
		<>
			<Navbar/>
			<Routes>
				<Route path="/" element={<Index />} />
				<Route path="/tasks" element={<Task />} />
			</Routes>
		</>
	);
}

export default App;

```

Vous devez maintenant créer le composant référencé ci-dessus. Dans le dossier **src**, créez un dossier appelé **routes** et à l'intérieur, créez deux fichiers appelés **Index.tsx** et **Task.tsx**.  

Dans **Index.tsx**, collez ce qui suit : 

```typescript

const Index = () => {
	return (
		<main className="container mx-auto">
			<section className="max-w-5xl mx-auto m-12 p-16">
				<h1 className="text-4xl md:text-7xl font-bold text-center py-3 mb-16">
					Gestionnaire de tâches amélioré par l'IA, compatible voix, recherchable
				</h1>
			</section>
		</main>
	);
};

export default Index;
```

Et dans **Task.tsx**, collez ce qui suit :

```typescript

const Task = () => {
	return (
		<main className="container mx-auto">
			<section className="max-w-5xl mx-auto m-12 p-16">
				<h1 className="text-4xl md:text-7xl font-bold text-center py-3 mb-16">
					Vos tâches
				</h1>
			</section>
		</main>
	);
};

export default Task;
```

Maintenant, créez un dossier components dans le dossier **src** et ajoutez un fichier à l'intérieur appelé **Navbar.tsx**. Collez ce qui suit dans ce fichier : 

```typescript

import { Link, useNavigate } from "react-router-dom";
import { PencilIcon } from "@heroicons/react/24/solid";
import Button from "./Button";

const Navbar = () => {
	const navigate = useNavigate();

	return (
		<nav className="py-4 border-b-2 border-container shadow-md shadow-gray-400 w-full fixed top-0 bg-base">
			<ul className="flex items-center justify-between  w-11/12 mx-auto">
				<Link to="/">
					<Button
						content={{
							text: "Taskwrite",
							icon: PencilIcon,
						}}
						textClasses="font-semibold text-main"
						iconClasses="text-main"
					/>
				</Link>
				</Link>
				<div className="flex items-center justify-between gap-6">
					<Link
						to="/tasks"
						className="font-semibold hover:scale-105 transition duration-300 ease-in-out"
					>
						Voir les tâches
					</Link>
				</div>
			</ul>
		</nav>
	);
};

export default Navbar;
```

Ce fichier contient un menu de navigation qui bascule entre les deux pages. Vous devrez créer le composant `Button` référencé ci-dessus et ajouter le package Hero icons.   
  
Dans un terminal intégré, exécutez ce qui suit pour ajouter Hero icons : `npm i @heroicons/react` . Ensuite, ajoutez un nouveau fichier appelé **Button.tsx** dans le dossier components. Collez ce qui suit dans ce fichier :

```typescript
import { ReactNode } from "react";

interface ButtonProps {
	extraBtnClasses?: string;
	textColor?: string;
	handleClick?: (e: React.MouseEvent<HTMLButtonElement>) => void;
	title?: string;
	disable?: boolean;
	type?: "button" | "submit" | "reset";
	children: ReactNode;
}

function Button({
	extraBtnClasses,
	textColor,
	handleClick,
	title,
	disable,
	type = "button",
	children,
}: ButtonProps) {
	const handleClickProp = type === "submit" ? undefined : handleClick;

	return (
		<button
			type={type}
			title={title ?? ""}
			onClick={handleClickProp}
			disabled={disable}
			className={`flex gap-2 items-center text-iconColor ${extraBtnClasses} ${
				textColor ?? ""
			} rounded-md px-2 py-1 hover:scale-105 transition duration-300 ease-in-out`}
		>
			{children}
		</button>
	);
}

export default Button;

```

Ce fichier décrit un composant de bouton partagé et définit les props qu'il acceptera.

Retournez et corrigez les erreurs d'importation et relancez l'application en exécutant `npm run dev`, vous devriez voir quelque chose comme ceci : 

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-08-at-18.23.45.png)
_application en cours d'exécution avec la commande npm run dev_

### Comment créer le composant de formulaire

Ajoutez un nouveau fichier appelé **AddTask.tsx** dans le dossier components et collez ce qui suit dedans :

```typescript

import { useState } from "react";
import Select from "./Select";
import Button from "./Button";

const AddTask = () => {
	const [titleVal, setTitleVal] = useState("");
	const [textAreaVal, setTextAreaVal] = useState("");
	const [dueDate, setDueDate] = useState(new Date());

	const priorityArray = ["low", "medium", "high"];

	const [priority, setPriority] = useState(priorityArray[0]);

	return (
		<form id="form" className="m-8">
			<div className="flex flex-col mb-6">
				<label htmlFor="title">Titre de la tâche</label>
				<input
					type="text"
					id="title"
					placeholder="Titre de votre tâche"
					value={titleVal}
					onChange={(e) => setTitleVal(e.target.value)}
					className="bg-inherit border rounded-sm p-2 focus:outline-none focus:ring-1 border-input focus:ring-slate-900"
				/>
			</div>
			<div className="flex flex-col mb-6">
				<label htmlFor="description" className="mb-1">
					Description de la tâche
				</label>
				<textarea
					id="description"
					placeholder="Décrivez votre tâche"
					maxLength={200}
					value={textAreaVal}
					onChange={(e) => setTextAreaVal(e.target.value)}
					className="bg-inherit border rounded-sm p-2 h-32 resize-none focus:outline-none focus:ring-1 border-input focus:ring-slate-900"
				/>
			</div>
			<div className="flex flex-col mb-6">
				<label htmlFor="description" className="mb-1">
					Priorité de la tâche
				</label>
				<Select
					defaultSelectValue={priority}
					selectOptions={priorityArray}
					handleSelectChange={(e) => setPriority(e.target.value)}
				/>
			</div>
			<div className="flex flex-col mb-6">
				<label htmlFor="description" className="mb-1">
					Date d'échéance de la tâche
				</label>
				<input
					type="date"
					id="date"
					value={dueDate!.toISOString().split("T")[0]}
					min={new Date().toISOString().split("T")[0]}
					onChange={(e) => setDueDate(new Date(e.target.value))}
					className="bg-inherit border rounded-sm border-input p-2 focus:outline-none focus:ring-1 focus:ring-slate-900 invalid:focus:ring-red-600"
				/>
			</div>
			<Button
				type="submit"
				content={{
					text: "Ajouter une tâche",
				}}
				extraBtnClasses="bg-pink-700 justify-center text-white font-semibold px-4 py-2 outline-1 hover:bg-pink-800 focus:ring-1 focus:ring-pink-800 w-full"
			/>
		</form>
	);
};

export default AddTask;
```

Maintenant, créez un nouveau fichier dans les composants appelé **Select.tsx**, collez ce qui suit dedans :

```typescript

import { useState } from "react";

interface SelectProps {
	defaultSelectValue: string;
	selectOptions: string[];
	handleSelectChange: (e: React.ChangeEvent<HTMLSelectElement>) => void;
}

const Select = ({
	defaultSelectValue,
	handleSelectChange,
	selectOptions,
}: SelectProps) => {
	const [selectVal, setSelectVal] = useState(defaultSelectValue);
	return (
		<select
			value={selectVal}
			onChange={(e) => {
				setSelectVal(e.target.value);
				handleSelectChange(e);
			}}
			className="bg-inherit border rounded-sm border-input p-2 focus:outline-none focus:ring-1 focus:ring-slate-900 cursor-pointer"
		>
			{selectOptions.map((option) => (
				<option key={option} value={option}>
					{option.charAt(0).toUpperCase() + option.slice(1)}
				</option>
			))}
		</select>
	);
};

export default Select;

```

Cela définit un composant `Select` et ses props. Les props du composant `Select` sont une fonction pour gérer le changement, un tableau d'options et la valeur par défaut qu'il doit afficher. 

Maintenant, importez le composant `AddTask` dans le fichier **Index.tsx** entre les balises `h1` comme suit : 

```typescript

import AddTask from "../components/AddTask";

const Index = () => {
	return (
		<main className="container mx-auto">
			<section className="max-w-5xl mx-auto m-12 p-16">
				<h1 className="text-4xl md:text-7xl font-bold text-center py-3 mb-16">
					Gestionnaire de tâches amélioré par l'IA, compatible voix, recherchable
				</h1>
				<AddTask />
			</section>
		</main>
	);
};

export default Index;
```

Votre application devrait maintenant afficher le formulaire :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-08-at-18.57.25.png)
_formulaire de l'application de tâches_

### Comment configurer le formulaire pour créer une tâche

Pour rendre le formulaire fonctionnel, vous devez le connecter à une fonction de soumission qui appellera la fonction de création définie dans le fichier **db.ts**. 

De plus, vous devrez valider le formulaire pour éviter d'envoyer des données incorrectes et d'avoir Appwrite renvoyer des erreurs à l'application React.

Dans le fichier du composant `AddTask`, collez le code suivant au-dessus de l'instruction `return` et en dessous de `setPriority` useState :

```typescript

const [priority, setPriority] = useState(priorityArray[0]);

//coller ici
const navigate = useNavigate();
    
const [isSubmitting, setIsSubmitting] = useState(false);
const [titleValidationError, setTitleValidationError] = useState("");

	const handleTitleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
		setTitleVal(e.target.value);

		if (e.target.value.trim() !== "") {
			setTitleValidationError("");
		}
	};

	const handleSubmitTask = async (e: React.FormEvent<HTMLFormElement>) => {
		e.preventDefault();
		setIsSubmitting(true);

		try {
			if (!titleVal) {
				setTitleValidationError("Veuillez fournir au moins un titre pour la tâche");
				setTimeout(() => setTitleValidationError(""), 2000);
				setIsSubmitting(false);
				return;
			}

			if (titleVal.length > 49) {
				setTitleValidationError(
					"Titre trop long. Il ne peut être que de 49 caractères de long"
				);
				setTimeout(() => setTitleValidationError(""), 2000);
				setIsSubmitting(false);
				return;
			}

			const payload: IPayload = {
				title: titleVal,
				description: textAreaVal,
				due_date: dueDate,
				priority: priority,
			};

			await createDocument(payload);

			// réinitialiser le formulaire
			setTitleVal("");
			setTextAreaVal("");
			setDueDate(new Date());
			setPriority(priorityArray[0]);
			setTitleValidationError("");
			setIsSubmitting(false);
			navigate("/tasks");
		} catch (error) {
			console.error("Erreur dans handleSubmitTask :", error);
			setIsSubmitting(false);
		}
	};
    
    return (
    //reste du code inchangé ci-dessous
    

```

Ensuite, remplacez l'instruction `return` par le code suivant :

```

return (
<form id="form" onSubmit={handleSubmitTask} className="m-8">
    <div className="flex flex-col mb-6">
        <label htmlFor="title">Titre de la tâche</label>
        <input
            type="text"
            id="title"
            placeholder="Titre de votre tâche"
            value={titleVal}
            onChange={handleTitleChange}
            className={`bg-inherit border rounded-sm p-2 focus:outline-none 						focus:ring-1 ${
                    titleValidationError
                    ? "border-error focus:ring-red-500 invalid:focus:ring-red-						 600"
                    : "border-input focus:ring-slate-900"
            }`}
        />
        {titleValidationError && (
        <span className="text-error mt-1">{titleValidationError}</span>
        )}
    </div>
    <div className="flex flex-col mb-6">
        <label htmlFor="description" className="mb-1">
        	Description de la tâche
        </label>
        <textarea
            id="description"
            placeholder="Décrivez votre tâche"
            maxLength={200}
            value={textAreaVal}
            onChange={(e) => setTextAreaVal(e.target.value)}
            className={`bg-inherit border rounded-sm p-2 h-32 resize-none 							focus:outline-none focus:ring-1 ${
                        textAreaVal.length > 197
                        ? "border-error focus:ring-red-500 invalid:focus:ring-							 red-600"
                        : "border-input focus:ring-slate-900"
       		 }`}
        />
        {textAreaVal.length > 197 && (
        <span className="text-error mt-1">
        	Avertissement, la description devient trop longue. Peut seulement être de 200 caractères
        </span>
        )}
    </div>
    <div className="flex flex-col mb-6">
        <label htmlFor="description" className="mb-1">
            Priorité de la tâche
        </label>
        <Select
            defaultSelectValue={priority}
            selectOptions={priorityArray}
            handleSelectChange={(e) => setPriority(e.target.value)}
        />
    </div>
    <div className="flex flex-col mb-6">
        <label htmlFor="description" className="mb-1">
        	Date d'échéance de la tâche
        </label>
        <input
            type="date"
            id="date"
            value={dueDate!.toISOString().split("T")[0]}
            min={new Date().toISOString().split("T")[0]}
            onChange={(e) => setDueDate(new Date(e.target.value))}
                className="bg-inherit border rounded-sm border-input p-2 	   							  focus:outline-none focus:ring-1 focus:ring-slate-							   900 invalid:focus:ring-red-600"
        />
    </div>
    <Button
        type="submit"
        disable={isSubmitting}
        extraBtnClasses="bg-primary justify-center text-white font-semibold px-4 py-2 outline-1 hover:bg-primaryHover focus:ring-1 focus:ring-pink-800 w-full"
    >
        <span>
        	Ajouter une tâche
        </span>
	</Button>
</form>
);
```

Corrigez les erreurs d'importation et votre application devrait maintenant valider le titre et la description ainsi que créer la tâche puis vous envoyer vers la route "/tasks". Vous pouvez vérifier la console Appwrite pour confirmer que la tâche a été créée. 

### Comment configurer la lecture et la suppression des tâches

Ouvrez le fichier **Task.jsx** dans le dossier routes dans le dossier **src**, et ajoutez le code suivant au-dessus du `return` comme suit :

```typescript

const [tasks, setTasks] = useState<ITask[]>([]);
const [tasksError, setTasksError] = useState("");

useEffect(() => {
        getTasks()
        .then((res) => {
        setTasks(res.reverse());
        })
        .catch((err) => {
        console.error(err);
        setTasksError("Erreur lors de la récupération des tâches, veuillez réessayer");
        });
	}, []);
    
return (
//reste du code
```

Ici, le fichier définit un état local en utilisant useState pour contenir les tâches et définir les erreurs potentielles liées aux tâches.

Maintenant, remplacez le code dans le `return` par le code suivant :

```typescript


<main className="container mx-auto">
    <section className="max-w-5xl mx-auto m-12 p-16">
        <h1 className="text-4xl md:text-7xl font-bold text-center py-3 mb-16">
        Vos tâches
        </h1>
        {tasksError ? (
        	<span className="m-8 text-error">{tasksError}</span>
        ) : (
            <div className="flex flex-col md:flex-row justify-between">
            	<div className="flex-1">
                    <h3 className="text-2xl font-bold m-8">Tâches en attente</h3>
                    <div>
                         {tasks
                             .filter((task) => !task.done)
                             .map((task) => (
                                <TaskItem key={task.$id} task={task} />
                         ))}
            		</div>
            	</div>
            	<div className="flex-1">
                    <h3 className="text-2xl font-bold m-8">Tâches terminées</h3>
                    <div>
                        {tasks
                            .filter((task) => task.done)
                            .map((task) => (
                            	<TaskItem key={task.$id} task={task} />
                        ))}
                    </div>
            	</div>
            </div>
        )}
    </section>
</main>
```

Vous devez maintenant créer la fonction `getTasks()` et le composant `TaskItem`. Dans le dossier components, créez un fichier appelé **TaskItem.tsx** et collez le code suivant dedans :

```typescript

interface TaskItemProps {
	task: ITask;
}
function TaskItem({ task }: TaskItemProps) {
    return (
    <>
        <div className="m-8 cursor-pointer border border-container rounded-md p-4 hover:shadow-lg transition duration-300 ease-in-out max-h-96">
            <section
            key={task.$id}
            className="flex flex-col justify-between gap-2 my-4 h-full"
            >
            <section className="flex gap-4 items-center justify-between flex-wrap">
                {task.priority && (
                <span>
                    <span className="font-medium">Priorité : </span>
                        <span
                            className={`${
                            task.priority === "low"
                            ? "bg-lowPriority text-iconColor"
                            : task.priority === "medium"
                            ? "bg-mediumPriority text-iconColor"
                            : "bg-highPriority text-iconColor"
                            } py-1 px-2 rounded-md`}
                        >
                        	{task.priority}
                        </span>
                </span>
                )}
                <div className="flex gap-2 py-1 ml-auto">
                    <Button
                        handleClick={() => handleEdit(task)}
                        extraBtnClasses="bg-ok"
                    >
                        <span className="font-medium">Modifier</span>
                        <PencilSquareIcon height={25} className="hidden lg:flex" />
                    </Button>
                    <Button
                        handleClick={(e) => handleDelete(e, task.$id)}
                        extraBtnClasses="bg-highPriority"
                    >
                        <span className="font-medium">Supprimer</span>
                        <TrashIcon height={25} className="hidden lg:flex" />
                    </Button>
                </div>
            </section>
            <section className="">
                <h2 className="text-xl font-medium py-2 break-words">
                	{task.title}
                </h2>
                <p className="py-1 mb-4 min-h-16 break-words">
                    {task.description.length > 70
                    	? task.description.substring(0, 70) + "..."
                    	: task.description}
                </p>
                <span className="font-extralight mt-2">
                    <span className="font-medium">Échéance : </span>
                        <span className="underline">{`${new Date(
                        	task.due_date
                        ).toLocaleDateString()}`}
                    </span>
                </span>
                </section>
                <section className="flex justify-between">
                    {task.done ? (
                        <span className="items-center text-ok font-bol ml-auto">
                        	Terminé
                        </span>
                    ) : (
                    <div className="flex items-center ml-auto hover:scale-105 transition duration-300 ease-in-out">
                        <label htmlFor="done" className="mr-2 font-light">
                        	Marquer comme terminé
                        </label>
                        <input
                            type="checkbox"
                            checked={isDone}
                            onClick={(e) => e.stopPropagation()}
                            onChange={(e) => {
                            setIsDone(e.target.checked);
                            handleCheckbox(task, task.$id, e);
                        }}
                    		className="size-5 accent-pink-600 rounded-sm"
                    />
                </div>
                )}
                </section>
            </section>
        </div>
    </>
    );
}
export default TaskItem;
```

Cela donne au fichier une mise en page pour l'affichage. Il divise la page en deux colonnes, une pour les tâches en attente et une pour les tâches terminées, et il gère la réactivité de la page.

Afin de se débarrasser des erreurs, collez le code suivant juste avant l'instruction `return` comme suit : 

```typescript

function TaskItem({ task }: TaskItemProps) {

//coller ici
const [isDone, setIsDone] = useState(false);

const handleDelete = async (
        currentTaskId: string
    ) => {
        try {
            await deleteDocument(currentTaskId);
        } catch (error) {
            console.error(error);
        }
};

const handleCheckbox = async (
        currentTask: IPayload,
        id: string,
        checkedVal: boolean
    ) => {
        if (!checkedVal) return;

        const payload: IPayload = {
        title: currentTask.title,
        description: currentTask.description,
        due_date: currentTask.due_date,
        priority: currentTask.priority,
        done: checkedVal,
        };

        try {
        	await updateDocument(payload, id);
        } catch (error) {
        	console.error(error);
        }
};

//reste du code ci-dessous inchangé
return (
......
```

Cela ajoute la capacité de supprimer un élément de tâche et la capacité de le marquer comme terminé. 

Créez un nouveau fichier dans le dossier **utils** et appelez-le **shared.ts**. Ce fichier abritera toute fonction qui sera appelée dans plus de deux endroits de l'application. 

La fonction `getTasks` est une telle fonction répétitive, donc elle sera placée dans le fichier **shared.ts**. Collez le code suivant dedans :

```typescript

import { readDocuments } from "./db";
import { ITask } from "../models/interface";

export const getTasks = async () => {
	const { documents } = await readDocuments();

	return documents as ITask[];
};
```

Cela définit la fonction et retourne un tableau de `ITasks`. Retournez au fichier **Task.tsx** et corrigez les erreurs d'importation. 

Exécutez l'application et vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-09-at-00.10.56.png)
_vos tâches en attente et terminées affichées dans le navigateur_

La tâche peut être supprimée ou marquée comme terminée, mais vous ne verrez pas de mise à jour sur l'interface utilisateur tant que la page n'est pas actualisée. Pour corriger cela, retournez au fichier **TaskItem** et collez le code suivant en dessous de l'état `isDone` useState et au-dessus de la fonction `handleDelete` :

```typescript

const [isDone, setIsDone] = useState(false);

//coller ici
const updateTasks = async () => {
    try {
        const allTasks = await getTasks();
        if (setTasks) setTasks(allTasks.reverse());
    } catch (error) {
    	console.error(error);
    }
};

//le reste du code ci-dessous reste tel quel
const handleDelete = async (
```

Mettez à jour l'interface des props de `TaskItem` et la fonction `TaskItem` comme suit :

```typescript

interface TaskItemProps {
	task: ITask;
	setTasks?: (tasks: ITask[]) => void;
}

function TaskItem({ task, setTasks }: TaskItemProps) {
//reste du code ci-dessous
	const [isDone, setIsDone] = useState(false);
```

Cela donne une fonction de setter qui réinitialise le tableau des tâches en tant que prop au composant `TaskItem`. 

Ajustez les fonctions `handleDelete` et `handleCheckbox` dans le composant `TaskItem` pour inclure la fonction `updateTasks` que vous avez ajoutée ci-dessus. Cela devrait se lire comme suit :

```typescript

const handleDelete = async (
    e: React.MouseEvent<HTMLButtonElement>,
    currentTaskId: string
) => {
    try {
        await deleteDocument(currentTaskId);
        updateTasks();
    } catch (error) {
    	console.error(error);
    }
};

const handleCheckbox = async (
    currentTask: IPayload,
    id: string,
    e: React.ChangeEvent<HTMLInputElement>
	) => {
    
    const payload: IPayload = {
        title: currentTask.title,
        description: currentTask.description,
        due_date: currentTask.due_date,
        priority: currentTask.priority,
        done: e.target.checked,
    };

    try {
    	await updateDocument(payload, id);
    	updateTasks();
    } catch (error) {
    	console.error(error);
    }
};

```

Retournez au fichier **Task.tsx** et passez `setTasks` au composant `TaskItem` comme suit : `<TaskItem key={task.$id} task={task} setTasks={setTasks} />`. Maintenant, l'interface utilisateur se met à jour sans avoir besoin d'actualiser manuellement la page.

### Comment rendre les tâches modifiables

Pour modifier une tâche, vous devrez passer une fonction au bouton de modification dans le composant `TaskItem`. 

Collez le code suivant dans le fichier **TaskItem.tsx** entre les fonctions `updateTasks` et `handleDelete` comme suit :

```typescript

//coller en dessous de updateTasks
const handleEdit = async (
    currentTask: ITask
) => {
    navigate("/", { state: { task: currentTask } });
};

//reste du code inchangé ci-dessous
```

Ajoutez cette ligne juste au-dessus de l'état `isDone` useState : `const navigate = useNavigate();`. 

Dans le même fichier, trouvez le bouton de modification et passez-lui la fonction `handleEdit`. Enveloppez-le également dans une condition qui vérifie si la tâche est terminée de sorte que le bouton ne soit affiché que dans le cas où la tâche n'est pas marquée comme terminée. Comme suit :

```typescript
{!task.done && (
    <Button
        handleClick={() => handleEdit(task)}
        extraBtnClasses="bg-ok"
    >
    	<span className="font-medium">Modifier</span>
    	<PencilSquareIcon height={25} className="hidden lg:flex" />
    </Button>
)
```

Le composant `AddTask` doit être ajusté pour gérer la modification d'une tâche et le fichier **Index.tsx** doit être mis à jour pour gérer la tâche à modifier qui lui est passée via la fonction de navigation `handleEdit`.

Tout d'abord, allez dans le fichier **AddTask** et ajoutez quelques définitions de props directement en dessous des instructions d'importation, puis passez les nouvelles props au composant comme suit :

```typescript
import....

// passer une tâche et un booléen isEdit
// si isEdit est vrai, alors le formulaire sera rempli avec les données de la tâche
interface ITaskFormProps {
	task: ITask | null;
	isEdit?: boolean;
	setTasks?: (tasks: ITask[]) => void;
}

//passer les props du composant
const AddTask = ({ task, isEdit, setTasks }: ITaskFormProps) => {
//code inchangé ci-dessous

```

Ajustez les états useStates de la date d'échéance et de la priorité pour qu'ils se lisent comme suit :

```typescript

const [dueDate, setDueDate] = useState(
	isEdit && task?.due_date ? new Date(task.due_date) : new Date()
);

const [priority, setPriority] = useState(
	isEdit && task?.priority ? task?.priority : priorityArray[0]
);
```

Ajoutez un useEffect en dessous des useStates comme suit :

```typescript

const [titleValidationError, setTitleValidationError] = useState("");

//coller en dessous des instructions useState
useEffect(() => {
    if (isEdit && task) {
        setTitleVal(task.title);
        setTextAreaVal(task.description);
    } else {
    	setTitleVal("");
    }
}, [isEdit, task]);
```

Dans la fonction `handleSubmit` dans le même fichier **AddTask**, supprimez cette ligne : `await createDocument(payload);` et remplacez-la par ce qui suit :

```typescript

if (isEdit && task) {
    await updateDocument(payload, task!.$id);
    const allTasks = await getTasks();
	if (setTasks) return setTasks(allTasks.reverse());
} else {
	await createDocument(payload);
}
```

Maintenant, remplacez le composant `Button` en bas du fichier juste au-dessus de la balise de fermeture du formulaire par ceci :

```typescript

<Button
    type="submit"
    disable={isSubmitting}
    extraBtnClasses="bg-primary justify-center text-white font-semibold px-4 py-2 outline-1 hover:bg-primaryHover focus:ring-1 focus:ring-pink-800 w-full"
>
    <span>
    	{isSubmitting ? "Soumission..." : task ? "Modifier la tâche" : "Ajouter une tâche"}
    </span>
</Button>
//code inchangé ci-dessous
</form>
	);
};

export default AddTask;
```

Cela définit le texte sur le bouton en fonction de si le formulaire est en train de soumettre, de créer une nouvelle tâche ou de mettre à jour une tâche existante.

Allez dans le fichier **Index.tsx** dans le dossier **routes** et collez ce qui suit au-dessus de l'instruction `return` :

```typescript
const Index = () => {
	//coller ici
	const location = useLocation();
	const navigate = useNavigate();

	const taskFromState: ITask = location.state?.task;

	const [taskToEdit] = useState<ITask | null>(taskFromState ?? null);

	useEffect(() => {
		if (taskFromState) {
			navigate(location.pathname, {});
		}
	}, [taskFromState, location.pathname, navigate]);
    
    //le code ci-dessous reste inchangé
    return (....
```

Ici, le fichier récupère la tâche qui lui est passée depuis la route "/tasks" et la définit dans l'état local. Ensuite, le useEffect annule la tâche passée afin que le formulaire soit réinitialisé lors du rafraîchissement.

Dans le fichier **Index.tsx**, remplacez le composant `AddTask` par cette ligne : `<AddTask task={taskToEdit} isEdit={taskToEdit ? true : false} />`.

Exécutez votre application et vous devriez pouvoir cliquer sur le bouton de modification, être redirigé vers la route "/", avoir le formulaire pré-rempli avec les détails de la tâche, pouvoir modifier certains des champs et être redirigé vers "/tasks" une fois que vous cliquez sur le bouton "Modifier la tâche". 

### Comment activer la visualisation des tâches

L'application crée, lit, met à jour et supprime désormais les tâches. Il ne reste plus qu'à pouvoir visualiser une tâche particulière. 

Allez dans le fichier **TaskItem**, ajoutez ce qui suit à l'interface `TaskItemProps` : `isViewTask: boolean;    handleViewTask?: (e: React.MouseEvent<HTMLDivElement>) => void;`.

Ajoutez-les en tant que props au composant `TaskItem` et définissez `isViewTask` à une valeur par défaut de `false` comme suit :

```typescript

function TaskItem({
	task,
	setTasks,
	isViewTask = false,
	handleViewTask,
}: TaskItemProps) {	
	//reste du code ci-dessous inchangé
	const navigate = useNavigate();
```

Remplacez la balise de paragraphe qui affiche la description de la tâche dans le `return` du composant par cette mise en page :

```typescript

<p className="py-1 mb-4 min-h-16 break-words">
    {task.description.length > 70 && !isViewTask
        ? task.description.substring(0, 70) + "..."
        : task.description
    }
</p>
```

Le changement introduit garantira que la description complète est visible si `isViewTask` est défini sur `true`.

Sur la balise `div` juste en dessous du `return` dans le même composant, ajoutez un gestionnaire `onClick` comme suit :

```typescript

return (
<>
    <div
        className="m-8 cursor-pointer border border-container rounded-md p-4 					   hover:shadow-lg transition duration-300 ease-in-out max-h-					   96"
        onClick={handleViewTask}
    >
//reste du code inchangé
...
```

Retournez dans le fichier **Task.tsx** et collez ce qui suit juste au-dessus du useEffect :

```typescript

const handleViewTask = (
    e: React.MouseEvent<HTMLDivElement>,
    activeTask: ITask
) => {
    setIsViewTask(true);
    setSelectedTask(activeTask);
};

//code inchangé ci-dessous
useEffect(...
```

Ajoutez les fonctions useState suivantes au-dessus de la fonction `handleViewTask`, en dessous des autres useStates :

```typescript

const [tasksError, setTasksError] = useState("");
//coller ici
const [isViewTask, setIsViewTask] = useState(false);
const [selectedTask, setSelectedTask] = useState<ITask>();

//code ci-dessous inchangé
const handleViewTask = (...
```

Maintenant, collez le code suivant dans l'instruction `return` du même fichier, juste au-dessus de la balise `h1` affichant le texte "Vos tâches" :

```typescript

return (
<main className="container mx-auto">
    <section className="max-w-5xl mx-auto m-12 p-16">
        //coller ici
        {isViewTask && selectedTask && (
            <Dialog key={selectedTask.$id} setIsViewTask={setIsViewTask}>
                <TaskItem
                    task={selectedTask}
                    handleViewTask={() => handleViewTask(selectedTask!)}
                    isViewTask={isViewTask}
                />
            </Dialog>
        )}
        <h1 className="text-4xl md:text-7xl font-bold text-center py-3 mb-16">
        Vos tâches
        </h1>
    	//reste du code ci-dessous reste inchangé
```

Vous devrez créer le composant Dialog. Créez un nouveau fichier dans le dossier components et appelez-le **Dialog.tsx**, puis collez ce qui suit dedans :

```typescript

import { XMarkIcon } from "@heroicons/react/24/solid";
import { ReactNode, useState } from "react";
import { ITask } from "../models/interface";
import Button from "./Button";

interface DialogProps {
    setIsViewTask?: (isViewTask: boolean) => void;
    children: ReactNode;
}

function Dialog({ setIsViewTask, children }: DialogProps) {
    const [isOpen, setIsOpen] = useState(true);

    const closeModal = () => {
        if (setIsViewTask) setIsViewTask(false);
        setIsOpen(false);
    };
	return (
        <dialog
            open={isOpen}
            id="modal"
            style={{
            backgroundColor: "var(--base-bg)",
            color: "var(--text-main)",
            }}
            className={`${
				isOpen ? "opacity-100" : "opacity-0 pointer-events-none"
                } transition-opacity duration-300 ease-in-out fixed inset-0      				backdrop-filter backdrop-blur-md backdrop-brightness-50 w-4/6  					border border-container rounded-md max-h-[80vh] overflow-y-auto 				text-main`}
        >
        <Button
            handleClick={closeModal}
            content={{ text: "Fermer", icon: XMarkIcon }}
            extraBtnClasses="ml-auto text-main font-medium hover:text-error"
        />
        <div className="max-h-[80vh] overflow-y-auto">{children}</div>
        </dialog>
    );
    }

export default Dialog;
```

Ici, le fichier définit un composant `Dialog` qui prend certaines props, affiche un bouton et les enfants qu'il reçoit des props. 

Enfin, remplacez les deux composants `TaskItem` dans la fonction `tasks.filter...` dans l'instruction return du fichier **Task.tsx** par ce qui suit :

```typescript

{tasks
    .filter((task) => !task.done)
    .map((task) => (
        <TaskItem
            key={task.$id}
            task={task}
            setTasks={setTasks}
            handleViewTask={() => handleViewTask(task)}
            isViewTask={isViewTask}
        />
))}
```

Vous devriez pouvoir cliquer sur les éléments de tâche et voir la boîte de dialogue s'ouvrir avec les détails de la tâche. 

Cependant, si vous essayez de supprimer l'élément, vous remarquerez qu'il ouvre la boîte de dialogue tout en le supprimant. Pour corriger cela, ajustez la fonction `handleDelete` dans le fichier **TaskItem.tsx** pour qu'elle se lise comme suit : 

```typescript

const handleDelete = async (
    e: React.MouseEvent<HTMLButtonElement>,
    currentTaskId: string
) => {
    e.stopPropagation();
    try {
    	await deleteDocument(currentTaskId);
        if (isViewTask) {
        	navigate(0);
        } else {
        	updateTasks();
        }
    } catch (error) {
    	console.error(error);
    }
};
```

Vous avez ajouté `e.stopPropagation()` pour empêcher l'événement de remonter à l'élément parent et d'interférer potentiellement avec le clic pour ouvrir la boîte de dialogue. 

Vous avez également ajouté une vérification après la suppression de la tâche pour voir si la tâche est en cours de visualisation, auquel cas nous actualisons la page via `navigate(0)` pour forcer la mise à jour de l'interface utilisateur à l'état approprié. Sinon, il procède à l'appel de `updateTasks()` pour actualiser l'état.

Vous remarquerez le même problème lorsque vous essayez de marquer la tâche comme terminée, ce qui fait apparaître la boîte de dialogue. Pour corriger cela, ajustez l'entrée de la case à cocher pour inclure cette ligne : `onClick={(e) => e.stopPropagation()}`. 

La nouvelle ligne empêche l'événement de remonter à l'élément parent `div`. Elle est ajoutée à `onClick` au lieu de `onChange` car l'événement qu'elle tente d'intercepter est de type `onClick`. L'entrée devrait se lire comme suit :

```typescript

<label htmlFor="done" className="mr-2 font-light">
	Marquer comme terminé
</label>
<input
    type="checkbox"
    checked={isDone}
    onClick={(e) => e.stopPropagation()}
    onChange={(e) => {
    setIsDone(e.target.checked);
    handleCheckbox(task, task.$id, e);
    }}
    className="size-5 accent-pink-600 rounded-sm"
/>
```

À ce stade, l'application React est réactive, peut effectuer des opérations CRUD sur la base de données Appwrite et l'utilisateur peut visualiser des tâches individuelles. 

### Comment générer automatiquement des descriptions avec le SDK IA de Vercel

Pour améliorer l'application et son expérience utilisateur, vous pouvez ajouter la capacité de générer automatiquement des descriptions pour les tâches en utilisant l'IA. 

Pour commencer, ouvrez un terminal intégré et exécutez la commande suivante : `npm i ai`. Cela ajoute le [SDK IA de Vercel](https://vercel.com/blog/introducing-the-vercel-ai-sdk) à l'application React. 

Ensuite, exécutez cette commande dans le terminal : `npm i @huggingface/inference` pour ajouter la prise en charge de Hugging Face. L'application utilisera [Hugging Face](https://sdk.vercel.ai/docs/guides/providers/huggingface) car vous devez payer pour obtenir un accès programmatique à OpenAI.

Créez un nouveau fichier dans le dossier utils, appelez-le **ai.ts** et collez ce qui suit dedans :

```typescript

import { HfInference } from "@huggingface/inference";
import { HuggingFaceStream, StreamingTextResponse } from "ai";

// Créer une nouvelle instance d'inférence HuggingFace
const Hf = new HfInference(import.meta.env.VITE_HUGGINGFACE_KEY);

// IMPORTANT! Définir le runtime sur edge
export const runtime = "edge";

export const callAI = async (prompt: string) => {
	const response = Hf.textGenerationStream({
		model: "OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5",
		inputs: `<|prompter|>${prompt}<|endoftext|><|assistant|>`,
		parameters: {
			max_new_tokens: 150,
			// @ts-ignore
			typical_p: 0.2,
			repetition_penalty: 1,
			truncate: 1000,
			return_full_text: false,
		},
	});

	// Convertir la réponse en un flux de texte convivial
	const stream = HuggingFaceStream(response);

	// Répondre avec le flux
	return new StreamingTextResponse(stream);
};

```

Ce code générique crée une instance de Hugging Face, crée une fonction qui prend une invite, passe cette invite à la fonction `textGenerationStream`. Ensuite, il convertit la réponse en un flux et en un flux de texte. 

Vous devrez ajouter un jeton d'accès Hugging Face. Vous pouvez en générer un à cette [adresse](https://huggingface.co/settings/tokens). Vous aurez besoin d'un compte avant de pouvoir y accéder. 

Une fois que vous avez le jeton, ouvrez le fichier env et ajoutez-y la ligne suivante

```env

//remplacez par votre jeton réel
VITE_HUGGINGFACE_KEY=YOUR-HF-ACCESS-TOKEN
```

Ouvrez le fichier **AddTask.tsx** et collez le bouton suivant juste au-dessus de la balise de fermeture div de la div contenant l'entrée de la zone de texte :

```typescript

{textAreaVal.length > 197 && (
    <span className="text-error mt-1">
    	Avertissement, la description devient trop longue. Peut seulement être de 200 caractères
    </span>
)}
//coller ici
<Button
    handleClick={generateDesc}
    disable={isGenerating}
    extraBtnClasses="bg-light mt-2 w-fit ml-auto"
>
    <span>Générer une description</span>
    <SparklesIcon height={20} />
</Button>
//reste du code ci-dessous inchangé
</div>
```

Définissez la fonction `generateDesc` juste au-dessus de l'instruction `return` dans le fichier **AddTask** comme suit :

```

const generateDesc = async () => {
    setTextAreaVal("");

    if (!titleVal) {
    alert("Veuillez fournir un titre pour la tâche");
    return;
    }
    
    setIsGenerating(true);

    const prompt = `Fournissez une description pour cette tâche : ${titleVal}. Gardez la description à un maximum de 30 mots`;

    try {
        const res = await callAI(prompt);
        const responseText = await res.text();

        setIsGenerating(false);
		
        //créer un effet de frappe
        responseText.split("").forEach((char, index) => {
        setTimeout(() => {
        setTextAreaVal((prevText) => prevText + char);
        }, index * 32);
        });
    } catch (error) {
    	console.log("ERREUR API HUGGING FACE : " + error);
    }
};
```

La fonction vérifie que le titre n'est pas vide et utilise le titre pour créer une invite à transmettre à l'assistant Hugging Face. La réponse de l'appel est enregistrée dans l'état local. Un simple effet de frappe est créé lorsque la zone de texte est remplie avec la réponse. 

Ensuite, ajoutez cet état useState : `const [isGenerating, setIsGenerating] = useState(false);` aux autres états useState dans le composant `AddTask`.

Remplacez l'entrée de la zone de texte dans le même composant par ce qui suit :

```typescript

<textarea
    id="description"
    placeholder="Décrivez votre tâche"
    maxLength={200}
    value={isGenerating ? "génération..." : textAreaVal}
    onChange={(e) => setTextAreaVal(e.target.value)}
    className={`bg-inherit border rounded-sm p-2 h-32 resize-none 		 focus:outline-none focus:ring-1 ${
    textAreaVal.length > 197
    ? "border-error focus:ring-red-500 invalid:focus:ring-red-600"
    : "border-input focus:ring-slate-900"
    }`}
/>
```

En vérifiant l'application, vous devriez voir le bouton et pouvoir générer une description pour le titre d'une tâche comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-09-at-04.57.05.png)
_description de tâche améliorée par l'IA_

### Activer la voix dans l'application avec le package React Speech Recognition

Tout d'abord, vous devez ajouter la dépendance et son helper Typescript en exécutant les commandes suivantes dans une fenêtre de terminal intégré : `npm i react-speech-recognition` et `npm i @types/react-speech-recognition`. 

De plus, exécutez la commande suivante pour que la dépendance fonctionne correctement : `npm i regenerator-runtime`.

Créez un dossier **hooks** dans le dossier **src**. Créez un fichier à l'intérieur appelé **useSpeechToTextHelper.ts** et collez ce qui suit dedans :

```typeacript

import "regenerator-runtime/runtime";
import { useState } from "react";
import { useSpeechRecognition } from "react-speech-recognition";

export function useSpeechToTextHelper() {
	const [error, setError] = useState("");

	const {
		transcript,
		listening,
		resetTranscript,
		browserSupportsSpeechRecognition,
	} = useSpeechRecognition();

	if (!browserSupportsSpeechRecognition) {
		setError("Le navigateur ne supporte pas la reconnaissance vocale.");
	}

	return {
		error,
		listening,
		transcript,
		resetTranscript,
	};
}

```

Ce hook expose certaines fonctions d'assistance intégrées de React Speech Recognition, gère le cas où le navigateur ne supporte pas les [API web pertinentes](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition) et retourne certaines de ces données.

Créez un nouveau fichier dans le dossier components appelé **Speaker.tsx**. Collez le code suivant dedans :

```typescript

import { useSpeechToTextHelper } from "../hooks/useSpeechToTextHelper";
import { MicrophoneIcon, XCircleIcon } from "@heroicons/react/24/solid";
import Button from "./Button";
import SpeechRecognition from "react-speech-recognition";

interface SpeakerProps {
handleClear: (e: React.MouseEvent<HTMLButtonElement>) => void;
}

function Speaker({ handleClear }: SpeakerProps) {
    const { listening, error } = useSpeechToTextHelper();

    const handleSpeech = () => {
        SpeechRecognition.startListening();
    };

    return (
    <div>
        {error && <div>{error}</div>}
        <div className="flex gap-2 py-1 items-center text-center justify-center">
            <span className="font-medium">{listening ? "Microphone allumé" : "Microphone éteint"}</span>
            <Button
                handleClick={handleSpeech}
                extraBtnClasses="bg-lightOk"
                title="Démarrer"
            >
            	<MicrophoneIcon height={25} />
            </Button>
            <Button
                handleClick={handleClear}
                extraBtnClasses="bg-light"
                type="reset"
                title="Réinitialiser"
            >
            	<XCircleIcon height={25} />
            </Button>
        </div>
    </div>
    );
}

export default Speaker;
```

Ce composant accepte une fonction pour effacer l'entrée vocale en tant que prop, utilise le hook d'assistance, définit une fonction pour gérer la parole réelle, gère l'état d'erreur potentiel et affiche un bouton pour gérer la parole et un autre pour effacer la transcription vocale.

Dans le fichier **AddTask**, supprimez l'étiquette du titre et remplacez-la par la mise en page suivante :

```typescript

<div className="flex flex-row justify-between items-center">
    <label htmlFor="title">Titre de la tâche</label>
    <Speaker handleClear={clearTranscript} />
</div>
```

Cela ajoute le composant `Speaker` et enveloppe à la fois l'étiquette et le composant `Speaker` dans une div représentative afin de maintenir la disposition du formulaire. 

Ajoutez la fonction `clearTranscript` juste au-dessus de la fonction `handleSubmit` comme suit :

```typescript

const handleTitleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
	setTitleVal(e.target.value);

    if (e.target.value.trim() !== "") {
    	setTitleValidationError("");
    }
};
    
//coller ici
const clearTranscript = () => {
    resetTranscript();
};
//le code ci-dessous reste inchangé
const handleSubmitTask = asyc....

```

Ensuite, dans le même composant `AddTask`, ajoutez ce qui suit :

```

const AddTask = ({ task, isEdit, setTasks }: ITaskFormProps) => {
	const navigate = useNavigate();
    //coller ici
	const { transcript, resetTranscript } = useSpeechToTextHelper();
    //le reste reste inchangé
```

Remplacez le useEffect dans le fichier par ce nouveau :

```typescript

useEffect(() => {
    if (isEdit && task && !transcript) {
        setTitleVal(task.title);
        setTextAreaVal(task.description);
    } else {
    	setTitleVal(transcript || "");
    }
}, [isEdit, task, transcript]);
```

Votre application devrait maintenant supporter la création de titres pour les tâches via des entrées vocales. Et devrait ressembler à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-09-at-05.36.51.png)
_fonctionnalité d'entrée vocale ajoutée au formulaire_

 

### Comment ajouter une fonctionnalité de recherche à l'application

Pour augmenter la facilité d'utilisation, il est utile d'avoir une fonctionnalité de recherche dans l'application. 

Pour commencer, ouvrez la console Appwrite. Cliquez sur vos collections, cliquez sur l'onglet Indexes puis cliquez sur le bouton "Create index". 

Laissez la clé d'index telle quelle, sélectionnez FullText dans le menu déroulant du type d'index. Ajoutez l'attribut title et créez l'index. Répétez le processus pour l'attribut description.

Dans votre application, ouvrez le fichier **db.ts** dans le dossier **utils** et collez la fonction suivante juste au-dessus du mot-clé `export`, puis ajoutez-la à la liste des exports :

```typescript

const searchTasks = async (searchTerm: string) => {
    const resTitle = await databases.listDocuments(dbID, collectionID, [
                        Query.search("title", searchTerm),
                    ]);
    const resDesc = await databases.listDocuments(dbID, collectionID, [
                        Query.search("description", searchTerm),
                     ]);
    const res = [...resTitle.documents, ...resDesc.documents];

    return res;
};

export {
	createDocument,
	readDocuments,
	updateDocument,
	deleteDocument,
	searchTasks,
};
```

Créez un nouveau fichier dans le dossier components, appelez-le **Search.tsx**. Collez ce qui suit dedans :

```typescript
import { FormEvent, useState } from "react";
import { ITask } from "../models/interface";
import Dialog from "./Dialog";
import TaskItem from "./TaskItem";
import Button from "./Button";
import { searchTasks } from "../utils/db";

const Search = () => {
const [searchTerm, setSearchTerm] = useState("");
const [isSearching, setIsSearching] = useState(false);
const [searchedTasks, setSearchedTasks] = useState<ITask[]>([]);
const [error, setError] = useState("");

    return (
        <div className="flex flex-col w-full md:w-1/2">
            <form
                className="flex flex-col md:flex-row items-start md:items-center gap-2"
                onSubmit={handleSubmit}
            >
                {searchedTasks.length > 0 && (
                    <Dialog setSearchedTasks={setSearchedTasks}>
                        {searchedTasks.map((task: ITask) => (
                        	<TaskItem key={task.$id} task={task} isViewTask={true} />
                        ))}
                    </Dialog>
                )}
            <input
                aria-roledescription="search"
                type="text"
                id="search"
                placeholder="rechercher vos tâches..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className={`bg-inherit w-5/6 border rounded-md p-2 focus:outline-none focus:ring-1 ${
                error
                ? "border-error focus:ring-red-500 invalid:focus:ring-red-600"
                : "border-input focus:ring-slate-900"
                }`}
            />
            <Button
            type="submit"
            extraBtnClasses="bg-primary text-white hover:bg-primaryHover font-medium text-main py-2"
            >
            	<span>{isSearching ? "Recherche..." : "Rechercher"}</span>
            </Button>
            </form>
        	<span className="text-error font-medium mt-1">{error}</span>
        </div>
    );
};

export default Search;

```

Le nouveau composant `Search` crée un état local et retourne un formulaire avec une entrée et un bouton de recherche. Il ouvre également la boîte de dialogue lorsqu'il a des résultats de recherche.

Ajoutez cette fonction `handleSubmit` au-dessus de l'instruction `return` comme suit :

```typescript

const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
	e.preventDefault();
    if (!searchTerm) {
        setError("Aucun terme de recherche saisi");
        setTimeout(() => {
        setError("");
        }, 3000);
        return;
    }

	setIsSearching(true);

    const res = await searchTasks(searchTerm);
    console.log("res search: ", res);
    if (res.length === 0) {
        setIsSearching(false);
        setError("Aucune tâche trouvée");
        setTimeout(() => {
        setSearchTerm("");
        setError("");
        }, 3000);
        return;
    }
    setIsSearching(false);
	setSearchedTasks(res as ITask[]);
};
```

Cette fonction définit une erreur si aucun terme de recherche n'est reçu, puis elle tente d'appeler la fonction de recherche de la base de données en lui passant le terme de recherche. Si elle réussit, elle définit les tâches dans l'état local et si ce n'est pas le cas, elle attrape l'erreur.

Cliquez dans le composant de dialogue et remplacez ses props par ce qui suit, puis passez-lui `setSearchedTasks` comme suit :

```typescript

interface DialogProps {
    setIsViewTask?: (isViewTask: boolean) => void;
    setSearchedTasks?: (tasks: ITask[]) => void;
    children: ReactNode;
}

function Dialog({ setIsViewTask, setSearchedTasks, children }: DialogProps) {...
```

Remplacez la fonction `closeModal` dans le composant de dialogue par ce snippet :

```typescript

const closeModal = () => {
    if (setIsViewTask) setIsViewTask(false);
    //c'est la nouvelle ligne
    if (setSearchedTasks) setSearchedTasks([]);
    setIsOpen(false);
};
```

Retournez dans le fichier **Task.tsx** et collez ceci en dessous de la balise `h1` qui affiche le texte "Vos tâches" :

```typescript

<h1 className="text-4xl md:text-7xl font-bold text-center py-3 mb-16">
Vos tâches
</h1>
//coller ici
<div className="m-8 flex flex-col-reverse md:flex-row gap-8 items-start 					md:items-center md:justify-between">
    <Search />
    <Button
        handleClick={() => navigate("/")}
        extraBtnClasses="bg-primary text-white font-medium py-2 hover:bg-	primaryHover ml-auto"
    >
        <span>Ajouter une tâche</span>
        <PlusIcon height={25} className="hidden md:flex" />
    </Button>
</div>
//le reste du code reste inchangé
```

Cela ajoute le composant de recherche et un bouton qui vous ramène à la page d'index lorsque vous cliquez dessus.

Ajoutez ce qui suit dans le composant Task juste en dessous des useStates :

```typescript

const [selectedTask, setSelectedTask] = useState<ITask>();
//coller ici
const navigate = useNavigate();
//tout ce qui suit reste inchangé
const handleSelectChange = (e: React.ChangeEvent<HTMLSelectElement>) 
```

Vous pouvez maintenant tester votre fonctionnalité de recherche. Elle fonctionne mais a un bug : si le terme de recherche est présent à la fois dans le titre et la description, nous obtenons deux résultats de recherche. 

Pour corriger cela, modifiez la fonction `searchTasks` dans **db.ts** pour filtrer les tâches en double par ID comme suit : 

```typescript

const searchTasks = async (searchTerm: string) => {
    const resTitle = await databases.listDocuments(dbID, collectionID, [
    	Query.search("title", searchTerm),
    ]);
    const resDesc = await databases.listDocuments(dbID, collectionID, [
    	Query.search("description", searchTerm),
    ]);

    const res = [...resTitle.documents, ...resDesc.documents];

    // supprimer les tâches en double
    const uniqueRes = res.filter(
    	(task, index, self) => index === self.findIndex((t) => t.$id ===  				task.$id)
    );

    return uniqueRes;
};

```

Maintenant, votre recherche devrait fonctionner comme prévu et devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-09-at-08.00.40.png)
_vos tâches en attente et terminées affichées dans le navigateur_

### Comment ajouter la capacité de trier les tâches par date d'échéance et priorité

L'application ne triera que les tâches en attente car cela a le plus de sens. Elle triera par date d'échéance de la date la plus proche à la plus éloignée et vice versa. Elle triera également par priorité de la plus faible à la plus élevée et vice versa.

Pour commencer, collez ce qui suit dans le fichier **Tasks.tsx** juste en dessous de la balise `h3` avec le texte "Tâches en attente" comme suit :

```typescript

<h3 className="text-2xl font-bold m-8">Tâches en attente</h3>
//coller ici
<div className="m-8 flex items-start lg:items-center gap-1 justify-between flex-col lg:flex-row">
    <span className="font-medium">Trier les tâches par : </span>
    <Select
        defaultSelectValue={selectArray[0]}
        handleSelectChange={handleSelectChange}
        selectOptions={selectArray}
    />
</div>
```

Ensuite, collez le tableau suivant qui contiendra les options pour le composant select ci-dessus. Collez-le juste au-dessus de la fonction `handleViewTask` comme suit :

```typescript

const navigate = useNavigate();
//coller ici
const selectArray = [
    "priorité - (faible - élevée)",
    "priorité - (élevée - faible)",
    "date d'échéance - (la plus proche - la plus éloignée)",
    "date d'échéance - (la plus éloignée - la plus proche)",
];
//le reste reste inchangé
const handleViewTask = (...
```

Ajoutez les fonctions `handleSelectChange` et de tri au-dessus de `selectArray`, comme suit :

```typescript

const sortByPriority = (tasksList: ITask[], isAsc: boolean): ITask[] => {
    const priorityOrder: { [key: string]: number } = {
    low: 1,
    medium: 2,
    high: 3,
    };

    return [...tasksList].sort((a, b) => {
    const priorityA = priorityOrder[a.priority!.toLowerCase()];
    const priorityB = priorityOrder[b.priority!.toLowerCase()];
    return isAsc ? priorityA - priorityB : priorityB - priorityA;
    });
};

const handleSelectChange = async (
	e: React.ChangeEvent<HTMLSelectElement>
) => {
    const selectedOption = e.target.value;
    const doneTasks = tasks.filter((task) => task.done);

    switch (selectedOption) {
        case "priorité - (faible - élevée)":
        case "priorité - (élevée - faible)": {
            const isAsc = selectedOption === "priorité - (faible - élevée)";
            const sortedTasks = sortByPriority(tasks, isAsc);
            setTasks([...doneTasks, ...sortedTasks.filter((task) =>  		 				!task.done)]);
        	break;
        }
        case "date d'échéance - (la plus proche - la plus éloignée)":
        case "date d'échéance - (la plus éloignée - la plus proche)": {
            const isEarliestToLatest =
            selectedOption === "date d'échéance - (la plus proche - la plus éloignée)";
            const dueDateResult = await sortByDueDate(isEarliestToLatest);
            const sortedTasks = dueDateResult.documents as ITask[];
            setTasks([...doneTasks, ...sortedTasks.filter((task) => 	   					!task.done)]);
            break;
        }
        default:
        	break;
        }
};

//ci-dessous reste inchangé
const selectArray = .....
```

La fonction sortByPriority crée un objet dont les clés mappent au tableau de priorité et leur donne des valeurs numériques. Cela facilite le tri car il est difficile de dire quelle chaîne est de priorité plus élevée sans cela.

La fonction `handleSelectChange` sélectionne l'option choisie et filtre les tâches pour obtenir celles qui sont terminées. Elle effectue une logique de correspondance dans les instructions switch, appelant `sortByPriority` pour les cas où l'utilisateur essaie de faire cela et elle appelle `sortByDueDate` pour le reste des cas. 

`sortByDueDate` est défini dans le fichier **db.ts**. Ouvrez-le et collez ce qui suit en bas du fichier au-dessus des exports. Ensuite, ajoutez-le à la liste des exports comme suit :

```typescript

const sortByDueDate = async (isEarliestToLatest: boolean) => {
	const orderQuery = isEarliestToLatest
		? Query.orderAsc("due_date")
		: Query.orderDesc("due_date");
	const res = await databases.listDocuments(dbID, collectionID, 		 	[orderQuery]);
	return res;
};

export {
	createDocument,
	readDocuments,
	updateDocument,
	deleteDocument,
	searchTasks,
	sortByDueDate,
};

```

Cette fonction utilise les méthodes Query d'Appwrite pour trier la chaîne de date selon le booléen qui lui est passé.

Retournez à votre application, exécutez-la pour tester la fonctionnalité de tri. L'application devrait être triée et le tri ne devrait s'appliquer qu'aux tâches en attente.

### Bonus : Comment ajouter le support du mode sombre

La dernière chose à faire est d'ajouter le support du mode sombre qui respecte les paramètres système des utilisateurs. 

Pour cela, ouvrez le fichier **tailwind.config.ts** et remplacez son contenu par ce qui suit :

```typescript

/** @type {import('tailwindcss').Config} */
export default {
	content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
	darkMode: "selector",
	theme: {
		extend: {
			textColor: {
				error: "var(--text-error)",
				ok: "var(--text-ok)",
				main: "var(--text-main)",
				iconColor: "var(--btn-icon-main)",
			},
			backgroundColor: {
				base: "var(--base-bg)",
				primary: "var(--btn-bg-primary)",
				primaryHover: "var(--btn-bg-primary-hover)",
				ok: "var(--btn-bg-ok)",
				lightOk: "var(--btn-bg-light-ok)",
				light: "var(--btn-bg-light)",
				lowPriority: "var(--low-priority)",
				mediumPriority: "var(--medium-priority)",
				highPriority: "var(--high-priority)",
			},
			borderColor: {
				container: "var(--border-container)",
				input: "var(--border-input)",
				error: "var(--border-error)",
			},
		},
	},
	plugins: [],
};

```

Cela étend les couleurs préréglées de tailwind et lie les variables CSS qui ont été définies dans le fichier **index.css** à la configuration Tailwind. 

Dans le fichier **index.css**, ajoutez cette classe dark en dessous de la classe date comme suit :

```css

#date::-webkit-calendar-picker-indicator {
    background-color: var(--btn-bg-light); 
}
//coller ici
.dark{
    --base-bg: #262626;
    --text-main: #ffffff;
    --text-error: #fca5a5;
    --text-ok: #86efac;
    --border-input: #e2e8f0;
    --border-error: #fca5a5;
}
```

Cela change certaines des valeurs des variables CSS lorsque la classe dark est appliquée.

Maintenant, ouvrez le fichier navbar dans le dossier components et remplacez son contenu par ce qui suit :

```typescript

const Navbar = () => {
    const navigate = useNavigate();

    const themeArray = ["light", "dark", "system"];
    const [theme, setTheme] = useState(() => {
    	return localStorage.getItem("theme") || themeArray[2];
    });

    const applyTheme = (selectedTheme: string) => {
        const isDarkModePreferred = window.matchMedia(
            "(prefers-color-scheme: dark)"
            ).matches;

        document.documentElement.classList.remove("light", "dark");
        document.documentElement.classList.add(selectedTheme);

        if (selectedTheme === "system") {
        document.documentElement.classList.toggle("dark", isDarkModePreferred);
        document.documentElement.classList.toggle("light", 		 		!isDarkModePreferred);
        }
    };

    const handleSelectTheme = (e: React.ChangeEvent<HTMLSelectElement>) => {
        const selectedTheme = e.target.value;
        setTheme(selectedTheme);

        // Stocker le thème sélectionné dans localStorage
        localStorage.setItem("theme", selectedTheme);
    };

    useEffect(() => {
    	applyTheme(theme);
    }, [theme]);

    return (
        <nav className="py-4 border-b-2 border-container shadow-md shadow-gray-400 w-full fixed top-0 bg-base">
            <ul className="flex items-center justify-between  w-11/12 mx-auto">
                <Link to="/">
                    <Button>
                        <span className="font-semibold text-main">Taskwrite</span>
                        <PencilIcon height={20} className="text-main" />
                    </Button>
                </Link>
                <div className="flex items-center justify-between gap-6">
                <Link
                    to="/tasks"
                    className="font-semibold hover:scale-105 transition duration-300 ease-in-out"
                >
                	Voir les tâches
                </Link>
                <div className="flex gap-2 items-center">
                    <span className="font-semibold"> Thème : </span>
                    <Select
                        defaultSelectValue={theme}
                        selectOptions={themeArray}
                        handleSelectChange={handleSelectTheme}
                    />
                </div>
                </div>
            </ul>
        </nav>
    );
};

export default Navbar;

```

Votre application devrait maintenant avoir un sélecteur dans le menu de navigation qui bascule avec succès entre les thèmes sombre et clair tout en utilisant les préférences système par défaut lorsqu'il est défini sur "Système". 

Cela devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-09-at-13.21.38.png)
_Interface et fonctionnalités complètes de Taskwrite_

Et Taskwrite est complet ! Vous avez réussi à construire une application de gestion de tâches qui est améliorée par l'IA, compatible voix, recherchable et triable en utilisant React et Appwrite.

## Notes

Appwrite a récemment annoncé de nouvelles fonctionnalités qui simplifieraient grandement la fonctionnalité de recherche ci-dessus, mais au moment de la rédaction, ces changements n'avaient pas été déployés dans leur offre cloud. 

L'application pourrait être encore simplifiée en utilisant des solutions de gestion d'état, et cela sera ajouté dans des articles ultérieurs.

L'application est en ligne [ici](https://taskwrite.netlify.app/).

## Limitations

Voici quelques limitations et problèmes connus avec cette application :

* Le menu de navigation n'est pas réactif
* L'application n'a pas de tests écrits
* Les permissions définies pour Appwrite sont permissives et non recommandées pour les environnements de production
* L'application pourrait tirer parti des [capacités Realtime d'Appwrite](https://appwrite.io/docs/apis/realtime) pour une expérience plus fluide
* L'application pourrait bénéficier de notifications push pour rappeler à l'utilisateur lorsque la date d'échéance de la tâche approche

Cela dit, l'application continuera à être améliorée et travaillée. Vous pouvez suivre cela sur [GitHub](https://github.com/FatumaA/taskwrite). Toutes les contributions et améliorations du code sont les bienvenues. Veuillez mettre une étoile au dépôt pendant que vous y êtes.