---
title: Tutoriel de projet Full Stack – Créer une application de recettes avec React,
  Node.js et PostgreSQL
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2023-10-19T20:31:03.000Z'
originalURL: https://freecodecamp.org/news/full-stack-project-create-a-recipe-app-using-react-node-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/react-note-photo-gallery-app--1-.png
tags:
- name: full stack
  slug: full-stack
- name: node
  slug: node
- name: postgres
  slug: postgres
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Tutoriel de projet Full Stack – Créer une application de recettes avec
  React, Node.js et PostgreSQL
seo_desc: 'In this in-depth tutorial, we''ll build a full stack recipe app from scratch,
  using React, Node.js, Postgres and the Spoonacular API. We''ll cover features such
  as:


  Building an API server in Node

  Integrating securely with a 3rd party API

  Interacting w...'
---

Dans ce tutoriel approfondi, nous allons construire une application de recettes full stack à partir de zéro, en utilisant React, Node.js, Postgres et l'API Spoonacular. Nous aborderons des fonctionnalités telles que :

* Construire un serveur API en Node
* Intégration sécurisée avec une API tierce
* Interagir avec une base de données Postgres en utilisant Prisma
* Faire des requêtes API depuis React
* Créer des composants réutilisables
* Travailler avec la pagination
* Travailler avec des éléments d'interface utilisateur tels que des onglets, des grilles d'images, des modales et le style

Plongeons-nous.

## Table des matières

* [Prérequis](#heading-prerequisites)
* [Dépôts GitHub](#try-it-yourself-first)
* [Tutoriel vidéo](#heading-video-tutorial)
* [Architecture du projet](#heading-project-architecture)
* [Comment configurer le backend](#heading-how-to-setup-the-backend)
* [Comment configurer la base de données et Prisma](#heading-how-to-setup-the-database-and-prisma)
* [Comment obtenir et sécuriser une clé API Spoonacular](#heading-how-to-get-and-secure-a-spoonacular-api-key)
* [Comment créer le point de terminaison de recherche](#heading-how-to-create-the-search-endpoint)
* [Comment configurer le frontend](#heading-how-to-setup-the-frontend)
* [Comment appeler l'API de recherche et afficher les résultats sur le frontend](#heading-how-to-call-the-search-api-and-display-results-on-the-frontend)
* [Comment créer le composant de saisie de recherche et de carte de recette](#heading-how-to-create-the-search-input-and-recipe-card-component)
* [Comment construire la fonctionnalité de pagination et de voir plus](#heading-how-to-build-the-pagination-and-view-more-functionality)
* [Comment construire le composant modal de résumé de recette](#how-to-build-the-recipe-summary-and-build-more-component)
* [Comment créer des points de terminaison pour obtenir/créer/supprimer des recettes favorites](#heading-how-to-create-endpoints-to-getcreatedelete-favorite-recipes)
* [Comment ajouter la fonctionnalité des favoris au frontend](#heading-how-to-add-favorites-functionality-to-the-frontend)
* [Comment ajouter du CSS/du style](#heading-how-to-add-cssstyling)
* [Conclusion](#heading-conclusion)

## Prérequis

Puisque nous allons nous concentrer sur la construction d'un projet, il y a quelques prérequis qui seront nécessaires pour tirer le meilleur parti de ce tutoriel :

* Certaines connaissances sur les concepts de développement web (frontend, backend, bases de données, API, REST).
* Certaines connaissances en JavaScript (variables, fonctions, objets, tableaux, etc.).
* Compréhension de base de React (comment créer des composants, ajouter des styles, travailler avec l'état).
* Compréhension de base de Node.js/Express (travailler avec des API).

## Dépôts GitHub 

### Code terminé 

[Vous pouvez trouver le code terminé sur GitHub en cliquant ici,](https://github.com/chrisblakely01/react-node-recipe-app) ou clonez le dépôt :

```
git clone git@github.com:chrisblakely01/react-node-recipe-app.git
```

### Code de démarrage

Si vous voulez gagner du temps et sauter la configuration initiale, [vous pouvez trouver le code de démarrage ici.](https://github.com/chrisblakely01/react-node-recipe-app-starter) Cela inclut un projet frontend/backend squelette déjà configuré, ainsi que la mise en page de base et le CSS. Ou clonez le dépôt :

```
git clone git@github.com:chrisblakely01/react-node-recipe-app-starter.git
```

## Tutoriel vidéo

Si vous souhaitez également apprendre à partir de la version vidéo, la voici :

%[https://www.youtube.com/watch?v=5wwaQ4GiSNU]

## Architecture du projet

Voici un diagramme qui illustre comment les différents composants de notre application interagiront les uns avec les autres :

![recipe-app-architecture](https://www.freecodecamp.org/news/content/images/2023/10/recipe-app-architecture.png)
_Diagramme illustrant les différents composants de l'application_

Nous aurons un frontend React et un backend Node. Ces deux éléments communiqueront via des points de terminaison spécifiques. Nous établirons cinq points de terminaison, tous hébergés dans notre backend.

Nous pouvons catégoriser ces points de terminaison en deux groupes distincts. Le premier groupe concernera les recherches de recettes. Il invoquera l'API de recettes et retournera les résultats en fonction d'une requête de recherche donnée. Notre frontend initiéra un appel à notre backend, qui relayera ensuite la demande de recherche à l'API de recettes. 

Nous choisissons de ne pas appeler directement l'API de recettes depuis notre frontend car cela nécessite une clé API—une forme d'authentification similaire à un mot de passe. Exposer cette clé dans notre code frontend pourrait entraîner un accès non autorisé si quelqu'un explore le code via son navigateur pour récupérer la clé API.

Il est plus sécurisé de stocker la clé API sur notre backend dans des variables d'environnement. À partir de là, nous pouvons appeler l'API de recettes puis transmettre la réponse à notre frontend. 

Cette approche est conforme aux pratiques courantes dans les environnements de production. Elle offre également la flexibilité de modifier les données sur le backend, si nécessaire, avant de les renvoyer au frontend. Et elle améliore les performances, car l'interface utilisateur n'aura pas à gérer plusieurs requêtes API vers et depuis l'API de recettes.

C'est l'essence de la manière dont notre fonctionnalité de recherche fonctionnera. Nous aurons également plusieurs points de terminaison pour ajouter, créer et supprimer des favoris. Ces favoris seront stockés dans notre propre base de données, ce qui donnera une image claire de ce que nous visons à construire.

## Comment configurer le backend

Dans ce tutoriel, nous allons passer par le processus de construction d'une application de recettes full-stack. Nous allons configurer le backend, créer le frontend et le lier à une base de données. Nous allons également nous connecter à une API de recettes en utilisant une clé API. 

Si vous préférez sauter la configuration, un code de démarrage est disponible sur CodeCoyotes, qui inclut une configuration de base et du CSS. Mais vous devrez toujours créer une base de données et obtenir une clé API.

Commençons par configurer notre espace de travail :

### Étape 1 : Configurer votre espace de travail

Commencez par ouvrir Visual Studio Code (ou votre éditeur de code préféré). Créez un nouveau dossier nommé `recipe-app` sur votre bureau ou un autre emplacement. Ensuite, faites glisser ce dossier dans la fenêtre de Visual Studio Code pour l'ouvrir.

Votre structure de dossier devrait maintenant ressembler à ceci :

```plaintext
recipe-app

```

### Étape 2 : Configurer le backend

Dans le dossier `recipe-app`, créez un autre dossier nommé `backend`.

Accédez à `Affichage -> Terminal` dans Visual Studio Code pour ouvrir un terminal. Changez votre répertoire pour le dossier `backend` en utilisant la commande `cd backend`.

Tapez `npm init` pour initialiser un nouveau package npm, puis appuyez sur Entrée pour passer par les invites. Pour le point d'entrée, tapez `./src/index.ts` et appuyez sur Entrée.

Votre structure de dossier devrait maintenant ressembler à ceci :

```plaintext
recipe-app
|-- backend
    |-- package.json

```

### Étape 3 : Installer les dépendances

Tout d'abord, installez les dépendances nécessaires en utilisant la commande suivante :

```bash
npm install express prisma @prisma/client cors

```

Maintenant, installez les dépendances de développement :

```bash
npm install --save-dev ts-node typescript nodemon @types/cors @types/express @types/node

```

Votre structure de dossier devrait maintenant ressembler à ceci :

```plaintext
recipe-app
|-- backend
    |-- node_modules
    |-- package.json
    |-- package-lock.json

```

### Étape 4 : Configurer votre code backend

Dans le dossier `backend`, créez un nouveau dossier nommé `src`. À l'intérieur de `src`, créez un fichier nommé `index.ts`.

Ajoutez le code suivant à `index.ts` :

```javascript
import express from "express";
import cors from "cors";

const app = express();

app.use(express.json());
app.use(cors());

app.get("/api/recipe/search", async (req, res) => {
  res.json({ message: "success" });
});

app.listen(5000, () => {
  console.log("Server running on localhost:5000");
});

```

### Étape 5 : Ajouter le script de démarrage

Tout d'abord, ouvrez `package.json` dans le dossier `backend`. Dans la section `scripts`, remplacez le script `test` par un script `start` comme suit :

```json
"scripts": {
    "start": "npx nodemon ./src/index.ts"
}

```

### Étape 6 : Exécuter votre backend

Dans le terminal, assurez-vous d'être dans le dossier `backend`, puis tapez `npm start` pour exécuter votre serveur backend.

Ouvrez ensuite un navigateur et allez à `http://localhost:5000/api/recipe/search`. Vous devriez voir une réponse avec le message `success`.

Félicitations ! Vous avez configuré et exécuté votre serveur backend avec succès. Dans la prochaine partie de ce tutoriel, nous nous concentrerons sur la configuration du frontend et la connexion à une base de données.

## Comment configurer la base de données et Prisma

Dans cette section, nous allons nous concentrer sur la configuration d'une base de données Postgres en utilisant ElephantSQL et l'intégration de Prisma pour interagir avec notre base de données sans effort. Plongeons-nous directement !

### Étape 1 : Configurer la base de données ElephantSQL

Commencez par naviguer vers [ElephantSQL](https://www.elephantsql.com/). Cliquez sur "Obtenez une base de données gérée dès aujourd'hui", suivi de la sélection du plan "Tiny Turtle" pour une instance gratuite.

Connectez-vous ou créez un compte pour accéder à la page "Créer une nouvelle instance".

Ensuite, entrez un nom pour votre base de données (par exemple, `recipe-app-db`), gardez le plan sur le niveau gratuit et choisissez une région proche de vous.

Cliquez sur "Revoir", vérifiez les détails, puis cliquez sur "Créer une instance".

### Étape 2 : Récupérer les identifiants de la base de données

Une fois votre instance créée, cliquez dessus pour voir les détails.

Localisez et copiez l'URL sous la section "Détails". Cette URL contient les identifiants nécessaires pour se connecter à votre base de données.

### Étape 3 : Créer un fichier d'environnement

Maintenant, retournez à votre éditeur de code et ouvrez le dossier `backend`.

Créez un nouveau fichier nommé `.env`. À l'intérieur du fichier `.env`, ajoutez la ligne suivante :

```plaintext
DATABASE_URL=<Votre-URL-de-base-de-données-copiée>

```

Remplacez `<Votre-URL-de-base-de-données-copiée>` par l'URL que vous avez copiée depuis ElephantSQL.

### Étape 4 : Intégrer Prisma

Arrêtez votre serveur s'il est en cours d'exécution en appuyant sur `Ctrl + C` (ou `Cmd + C` sur Mac) dans le terminal.

Dans le terminal, assurez-vous d'être dans le répertoire `backend`, et tapez la commande suivante pour initialiser Prisma :

```bash
npx prisma init

```

Cette commande créera un nouveau dossier nommé `prisma` avec un fichier nommé `schema.prisma`.

### Étape 5 : Vérifier l'intégration de Prisma

Maintenant, ouvrez `prisma/schema.prisma` pour vous assurer que votre `DATABASE_URL` a été détecté correctement.

Redémarrez votre serveur avec la commande `npm start`. Naviguez ensuite vers `http://localhost:5000/api/recipe/search` dans votre navigateur pour vous assurer que votre API fonctionne toujours et retourne le message de succès.

Votre structure de dossier devrait maintenant inclure le dossier Prisma et ressembler à ceci :

```plaintext
recipe-app
|-- backend
    |-- prisma
        |-- schema.prisma
    |-- .env
    |-- ...

```

## Comment obtenir et sécuriser une clé API Spoonacular

### Étape 1 : Obtenir une clé API de Spoonacular

Pour ce faire, naviguez vers [Spoonacular](https://spoonacular.com/) et cliquez sur "Start Now." Inscrivez-vous pour un compte et accédez au tableau de bord.

Dans le tableau de bord, cliquez sur "Profile" sur le côté gauche, et trouvez la section liée aux clés API. Générez une nouvelle clé API, et copiez-la dans votre presse-papiers.

### Étape 2 : Stocker la clé API en toute sécurité

Maintenant, retournez à votre éditeur de code et ouvrez le fichier `.env` dans le dossier `backend`.

Ajoutez une nouvelle variable d'environnement pour stocker votre clé API comme suit :

```plaintext
API_KEY=<Votre-clé-API-copiée>

```

Remplacez `<Votre-clé-API-copiée>` par la clé API que vous avez copiée de Spoonacular.

### Étape 3 : Installer et configurer Thunder Client

Dans Visual Studio Code, naviguez vers l'onglet des extensions (icône carrée sur la barre latérale), et recherchez Thunder Client.

Installez Thunder Client en cliquant sur le bouton Installer. Une fois installé, vous verrez une nouvelle icône (un éclair violet) sur la barre latérale.

### Étape 4 : Tester la clé API avec Thunder Client

Maintenant, cliquez sur l'icône Thunder Client, puis cliquez sur "Nouvelle requête".

Copiez l'URL du point de terminaison pour rechercher des recettes à partir de la documentation de Spoonacular. Elle devrait ressembler à ceci : `https://api.spoonacular.com/recipes/complexSearch`.

Collez cette URL dans la barre d'URL dans Thunder Client.

Sous l'onglet de requête, ajoutez deux nouveaux paramètres :

* `apiKey` avec la valeur de votre clé API.
* `query` avec une valeur de `burgers` ou tout autre terme que vous souhaitez rechercher.

Ensuite, cliquez sur "Envoyer" pour émettre la requête et observer la réponse. Vous devriez voir une liste de recettes liées au terme que vous avez recherché, indiquant que votre clé API et votre point de terminaison fonctionnent correctement.

## Comment créer le point de terminaison de recherche

### Étape 1 : Configurer un nouveau fichier pour la logique de l'API de recettes

Tout d'abord, naviguez vers votre dossier `backend/src` et créez un nouveau fichier nommé `recipe-api.ts`.

Dans `recipe-api.ts`, initiez une constante pour stocker votre clé API à partir des variables d'environnement :

```typescript
const API_KEY = process.env.API_KEY;

```

### Étape 2 : Créer la fonction searchRecipes

Dans `recipe-api.ts`, définissez une nouvelle fonction asynchrone `searchRecipes` qui prend en paramètres un `searchTerm` et un `page` :

```typescript
export const searchRecipes = async (searchTerm: string, page: number) => {
  if (!API_KEY) {
    throw new Error("API key not found");
  }

  const baseURL = "https://api.spoonacular.com/recipes/complexSearch";
  const url = new URL(baseURL);

  const queryParams = {
    apiKey: API_KEY,
    query: searchTerm,
    number: 10,
    offset: (page - 1) * 10,
  };

  url.search = new URLSearchParams(queryParams).toString();

  try {
    const searchResponse = await fetch(url.toString());
    const resultsJson = await searchResponse.json();
    return resultsJson;
  } catch (error) {
    console.error(error);
  }
};

```

### Étape 3 : Importer et utiliser `searchRecipes` dans index.ts

Maintenant, naviguez vers `index.ts` dans le dossier `backend/src`.

Importez la fonction `searchRecipes` depuis `recipe-api.ts` en haut de votre fichier :

```typescript
import * as RecipeAPI from "./recipe-api";

```

Localisez le point de terminaison où vous souhaitez utiliser la fonction `searchRecipes`, et modifiez-le pour appeler `searchRecipes` avec les arguments appropriés, puis retournez les résultats :

```typescript
app.get("/api/recipe/search", async (req, res) => {
  const searchTerm = req.query.searchTerm as string;
  const page = parseInt(req.query.page as string);

  const results = await recipeAPI.searchRecipes(searchTerm, page);
  return res.json(results);
});

```

### Étape 4 : Tester votre point de terminaison

Maintenant, vous pouvez redémarrer votre serveur en l'arrêtant (`Ctrl + C` ou `Cmd + C` sur Mac) puis en exécutant `npm start`.

Testez votre point de terminaison en envoyant une requête GET avec les paramètres de requête appropriés. Par exemple, naviguez vers `http://localhost:5000/api/recipe/search?searchTerm=burgers&page=1` dans votre navigateur ou utilisez un client REST comme Postman ou Thunder Client.

Vous devriez maintenant voir une liste de recettes retournées en réponse à votre requête, indiquant que votre logique backend pour appeler l'API de recettes et retourner les résultats fonctionne comme prévu.

## Comment configurer le frontend

Avant de commencer cette section, assurez-vous d'être dans le répertoire de premier niveau de votre projet, qui dans ce cas est nommé `recipe-app`.

### Étape 1 : Créer une application React avec Vite

Commencez par ouvrir un terminal et assurez-vous d'être dans le dossier de premier niveau (`recipe-app`).

Exécutez ensuite la commande suivante pour installer la dernière version de Vite :

```bash
npm install vite@latest --save-dev

```

Maintenant, initiez un nouveau projet React avec Vite en exécutant :

```bash
npx create-vite frontend --template react-ts

```

Cette commande crée un nouveau dossier nommé `frontend`, le configure comme un projet React et spécifie TypeScript comme langage.

### Étape 2 : Naviguer vers votre nouvelle application React

Changez votre répertoire pour le dossier `frontend` :

```bash
cd frontend

```

Installez ensuite les dépendances nécessaires :

```bash
npm install

```

### Étape 3 : Démarrer le serveur de développement

Vous pouvez démarrer le serveur de développement avec la commande suivante :

```bash
npm run dev

```

Votre navigateur web par défaut devrait maintenant s'ouvrir en affichant la configuration initiale de votre application React, qui inclut un exemple de compteur.

### Étape 4 : Nettoyer et personnaliser votre application React

Maintenant, vous pouvez retourner à votre éditeur de code et naviguer vers `frontend/src`. Supprimez le fichier `index.css` car il ne sera pas nécessaire.

Dans `main.tsx`, supprimez l'instruction d'importation pour `index.css`.

Maintenant, ouvrez `App.tsx`. Ici, vous verrez le code pour un compteur. Supprimez tout le contenu à l'intérieur de `App.tsx`.

Commençons frais en ajoutant le code suivant à `App.tsx` :

```jsx
// src/App.tsx
const App = () => {
  return <div>Hello from Recipe App</div>;
};

export default App;

```

Enregistrez `App.tsx` et vérifiez votre navigateur pour voir le texte mis à jour : "Hello from Recipe App".

### Étape 5 : Configurer votre feuille de style

Allez dans `src` et ouvrez `App.css`. Supprimez tous les styles pré-remplis mais gardez la définition de la classe `.root` vide pour l'instant.

Ajoutez une propriété `font-family` à la classe `.root` :

```css
/* src/App.css */
.root {
  font-family: Helvetica, Arial, sans-serif;
}

```

Ensuite, retournez à `App.tsx` et importez votre feuille de style :

```jsx
// src/App.tsx
import "./App.css";

const App = () => {
  // ...
};

```

Ensuite, enregistrez `App.tsx` et vérifiez votre navigateur pour voir la police mise à jour.

Maintenant, vous avez une ardoise propre pour commencer à construire le frontend de votre application de recettes avec React et TypeScript, en utilisant Vite comme outil de construction. Au fur et à mesure que vous progressez, vous pouvez maintenant commencer à ajouter des composants, du routage et de la gestion d'état pour construire l'interface utilisateur et la fonctionnalité de votre application.

## Comment appeler l'API de recherche et afficher les résultats sur le frontend

Maintenant, nous allons récupérer des données à partir d'une API et afficher les résultats sur l'interface utilisateur. La réponse de l'API est structurée comme suit :

```json
{
  "results": [
    {
      "id": 650235,
      "title": "Loaded Turkey Burgers",
      "image": "https://spoonacular.com/recipeImages/650235-312x231.jpg",
      "imageType": "jpg"
    }
    // ... autres recettes
  ],
  "offset": 10,
  "number": 10,
  "totalResults": 50
}

```

Chaque objet de recette contient un `id`, `title`, `image` et `imageType`. Nous allons parcourir le tableau `results` et afficher chaque recette sur notre interface utilisateur.

### Étape 1 : Configurer l'état

Dans votre `App.tsx`, configurez l'état pour stocker le `searchTerm` et les `recipes`.

```jsx
import React, { useState } from "react";

const App = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const [recipes, setRecipes] = useState([]);

  // ... reste de votre composant
};

```

### Étape 2 : Récupérer les données de l'API

Créez un nouveau fichier `API.ts` et configurez une fonction pour effectuer l'appel API.

```typescript
// src/API.ts
const searchRecipes = async (searchTerm: string, page: number) => {
  const baseURL = new URL("http://localhost:5000/api/recipes/search");
  baseURL.searchParams.append("searchTerm", searchTerm);
  baseURL.searchParams.append("page", page.toString());

  const response = await fetch(baseURL.toString());

  if (!response.ok) {
    throw new Error(`HTTP Error: ${response.status}`);
  }

  return response.json();
};

export { searchRecipes };

```

### Étape 3 : Créer une fonction de gestion

De retour dans `App.tsx`, importez la fonction `searchRecipes` et créez une fonction de gestion à appeler lorsque le formulaire est soumis.

```jsx
import React, { useState, FormEvent } from "react";
import { searchRecipes } from "./API";

const App = () => {
  // ... configuration d'état précédente

  const handleSearchSubmit = async (event: FormEvent) => {
    event.preventDefault();

    try {
      const { results } = await searchRecipes(searchTerm, 1);
      setRecipes(results);
    } catch (error) {
      console.error(error);
    }
  };

  // ... reste de votre composant
};

```

### Étape 4 : Afficher les données

Affichez les données des recettes dans l'instruction de retour de votre composant.

```jsx
const App = () => {
  // ... code précédent

  return (
    <div>
      <form onSubmit={handleSearchSubmit}>
        <button type="submit">Submit</button>
      </form>
      {recipes.map((recipe) => (
        <div key={recipe.id}>
          Recipe Image Location: {recipe.image}
          <br />
          Recipe Title: {recipe.title}
        </div>
      ))}
    </div>
  );
};

export default App;

```

### Étape 5 : Définir le type de recette

Définissez une interface `Recipe` dans un nouveau fichier nommé `types.ts`.

```typescript
// src/types.ts
export interface Recipe {
  id: number;
  title: string;
  image: string;
  imageType: string;
}

```

De retour dans `App.tsx`, importez l'interface `Recipe` et utilisez-la pour typer votre état et la fonction map.

```jsx
import React, { useState, FormEvent } from 'react';
import { searchRecipes } from './API';
import { Recipe } from './types';

const App = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [recipes, setRecipes] = useState<Recipe[]>([]);

  // ... reste de votre code

  return (
    <div>
      {/* ... reste de votre instruction de retour */}
      {recipes.map((recipe: Recipe) => (
        {/* ... reste de votre fonction map */}
      ))}
    </div>
  );
};

export default App;

```

### Étape 6 : Tester votre configuration

Maintenant, démarrez à la fois vos serveurs frontend et backend. Ouvrez votre navigateur, naviguez vers votre application et essayez de soumettre une recherche. Vous devriez voir les données des recettes affichées à l'écran.

```bash
# Dans un terminal
cd frontend
npm run dev

# Dans un autre terminal
cd backend
npm start

```

Cette configuration devrait maintenant récupérer et afficher les données des recettes en fonction du `searchTerm` codé en dur "burgers". Dans un scénario réel, vous remplaceriez le `searchTerm` codé en dur par une valeur dynamique provenant d'un champ de saisie utilisateur.

## Comment créer l'entrée de recherche et le composant de carte de recette

### Étape 1 : Configurer votre projet

Commencez par configurer un nouveau projet React ou naviguez vers le répertoire de votre projet existant.

```bash
npx create-react-app recipe-search-ui
cd recipe-search-ui

```

### Étape 2 : Créer des hooks d'état pour l'entrée utilisateur et les données

Dans votre dossier `src`, créez un nouveau fichier nommé `App.tsx` et importez les dépendances nécessaires :

```jsx
import React, { useState, FormEvent } from "react";

function App() {
  const [searchTerm, setSearchTerm] = useState < string > "";
  const [recipes, setRecipes] = useState < Array < any >> [];

  // ... reste du code
}

export default App;

```

Ici, nous avons configuré deux hooks d'état : un pour capturer le terme de recherche de l'utilisateur et un autre pour contenir les données de recette retournées par le backend.

### Étape 3 : Construire un formulaire pour capturer l'entrée utilisateur

Dans le composant `App`, construisez un formulaire avec un champ de saisie et un bouton de soumission. Nous allons également créer une fonction pour gérer la soumission du formulaire, qui déclenchera l'appel API.

```jsx
function App() {
  // ... reste du code

  const handleSearchSubmit = async (event: FormEvent) => {
    event.preventDefault();
    // ... logique de l'appel API
  };

  return (
    <div>
      <form onSubmit={handleSearchSubmit}>
        <input
          type="text"
          required
          placeholder="Enter a search term"
          value={searchTerm}
          onChange={(event) => setSearchTerm(event.target.value)}
        />
        <button type="submit">Submit</button>
      </form>
      {/* ... reste du code */}
    </div>
  );
}

```

Maintenant, les utilisateurs peuvent entrer leur terme de recherche, et lors de la soumission du formulaire, `handleSearchSubmit` sera déclenché.

### Étape 4 : Récupérer les données de recette depuis le backend

Dans la fonction `handleSearchSubmit`, utilisez l'API `fetch` pour envoyer une requête à votre backend, capturer les données retournées et mettre à jour l'état `recipes`.

```jsx
const handleSearchSubmit = async (event: FormEvent) => {
  event.preventDefault();
  try {
    const response = await fetch(
      `http://localhost:5000/api/recipes/search?searchTerm=${searchTerm}`
    );
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    setRecipes(data.results);
  } catch (error) {
    console.error(error);
  }
};

```

### Étape 5 : Afficher les données de recette

Créez un nouveau dossier nommé `components` dans votre répertoire `src`. À l'intérieur de ce dossier, créez un fichier nommé `RecipeCard.tsx`. Ce composant affichera les données de recette individuelles.

```jsx
import { Recipe } from "../types";

interface Props {
  recipe: Recipe;
}

const RecipeCard = ({ recipe }: Props) => {
  return (
    <div className="recipe-card">
      <img src={recipe.image}></img>
      <div className="recipe-card-title">
        <h3>{recipe.title}</h3>
      </div>
    </div>
  );
};

export default RecipeCard;

```

Maintenant, retournez à `App.tsx` et importez `RecipeCard`. Mappez sur l'état `recipes` pour afficher chaque recette en utilisant le composant `RecipeCard`.

```jsx
import RecipeCard from "./components/RecipeCard";

// ... reste du code

return (
  <div>
    {/* ... reste du code */}
    {recipes.map((recipe) => (
      <RecipeCard key={recipe.id} recipe={recipe} />
    ))}
  </div>
);

```

Maintenant, lorsque vous soumettez un terme de recherche, l'interface utilisateur affichera une liste de cartes de recettes contenant les images et les titres des recettes retournées par le backend.

### Étape 6 : Tester votre interface utilisateur

Exécutez votre application React, entrez un terme de recherche tel que "pasta" ou "burgers", et soumettez le formulaire. Vous devriez voir une liste de cartes de recettes affichant les recettes pertinentes du backend.

```bash
npm start

```

Naviguez vers `http://localhost:3000` dans votre navigateur et essayez votre nouvelle interface utilisateur de recherche de recettes !

## Comment construire la pagination et la fonctionnalité "Voir plus"

### Étape 1 : Pagination du backend

Nous avons ajouté un paramètre de requête `page` dans le point de terminaison de recherche. La valeur `page` est utilisée pour calculer le décalage des données de recette récupérées depuis la base de données ou l'API externe.

### Étape 2 : Ajouter le bouton "Voir plus" à l'interface utilisateur

Naviguez vers votre fichier `App.tsx`. Faites défiler vers le bas jusqu'au code JSX où vous mappez le tableau `recipes` et ajoutez un bouton "Voir plus" en dessous.

```jsx
// ... autre code
{
  recipes.map((recipe) => <RecipeCard key={recipe.id} recipe={recipe} />);
}
<button className="view-more" onClick={handleViewMoreClick}>
  View More
</button>;
// ... autre code

```

### Étape 3 : Créer un hook `useRef` pour stocker le numéro de page actuel

Au-dessus de l'instruction de retour de votre composant, créez un hook `useRef` pour suivre le numéro de page actuel sans provoquer de re-rendus.

```jsx
// ... autre code
const pageNumber = useRef(1);
// ... autre code

```

### Étape 4 : Implémenter la fonction `handleViewMoreClick`

Définissez une fonction appelée `handleViewMoreClick` pour gérer la logique de chargement de plus de recettes.

```jsx
// ... autre code
const handleViewMoreClick = async () => {
  try {
    const nextPage = pageNumber.current + 1;
    const nextRecipes = await api.searchRecipes(searchTerm, nextPage);
    setRecipes((prevRecipes) => [...prevRecipes, ...nextRecipes.results]);
    pageNumber.current = nextPage;
  } catch (error) {
    console.error(error);
  }
};
// ... autre code

```

### Étape 5 : Réinitialiser le numéro de page lors d'une nouvelle recherche

Modifiez votre fonction `handleSearchSubmit` pour réinitialiser le numéro de page à 1 chaque fois qu'un nouveau terme de recherche est entré.

```jsx
// ... autre code
const handleSearchSubmit = async (event: FormEvent) => {
  // ... autre code
  setRecipes(recipes.results);
  pageNumber.current = 1;
};
// ... autre code

```

### Étape 6 : Tester votre implémentation

Exécutez votre application et effectuez une recherche. Cliquez sur le bouton "Voir plus" pour charger plus de résultats. Changez le terme de recherche et assurez-vous que le numéro de page est réinitialisé et que vous obtenez une nouvelle liste de recettes.

```bash
npm start

```

Maintenant, lorsque vous recherchez des recettes et cliquez sur "Voir plus", vous devriez voir des recettes supplémentaires être chargées et affichées dans l'interface utilisateur.

## Comment construire le composant modal de résumé de recette

Je vais vous guider à travers ce processus étape par étape. Nous allons créer un modèle qui affiche un résumé de recette en utilisant un point de terminaison spécifique de l'API fournie.

### Étape 1 : Comprendre le point de terminaison du résumé de recette

Vous pouvez comprendre d'où proviennent les données de résumé en consultant la documentation de votre API. Le point de terminaison dont vous avez besoin s'appelle `Summarize Recipe`. Ce point de terminaison nécessite un ID de recette pour générer un résumé.

### Étape 2 : Configurer le point de terminaison du backend

Créez un point de terminaison backend qui interface avec le point de terminaison `Summarize Recipe`.

```typescript
// Dans votre backend, créez un point de terminaison pour récupérer le résumé de la recette
// Fichier : recipe-api.ts
export const getRecipeSummary = async (recipeId: string) => {
  if (!apiKey) {
    throw new Error("API key not found");
  }

  const url = new URL(
    `https://api.spoonacular.com/recipes/${recipeId}/summary`
  );
  const params = { apiKey: apiKey };
  url.search = new URLSearchParams(params).toString();

  const response = await fetch(url.toString());
  const json = await response.json();
  return json;
};

```

### Étape 3 : Créer une route backend

Créez une route dans votre backend pour gérer les requêtes vers votre nouveau point de terminaison.

```typescript
// Fichier : index.ts
app.get("/api/recipe/:recipeId/summary", async (req, res) => {
  const recipeId = req.params.recipeId;
  const result = await recipeSummary(recipeId);
  res.json(result);
});

```

### Étape 4 : Créer le composant modal de recette

Créez un composant React pour le modal de recette. Nous utiliserons le hook useEffect pour appeler le point de terminaison backend que nous venons de créer, et stocker les données de résumé de recette dans l'état.

Tout d'abord, ajoutez un type pour `RecipeSummary` à `types.ts`

```ts
export interface RecipeSummary {
  id: number;
  title: string;
  summary: string;
}

```

```jsx
// Fichier : RecipeModal.tsx
import React, { useState, useEffect } from "react";
import { RecipeSummary } from "../types";

interface Props {
  recipeId: string;
  onClose: () => void;
}

const RecipeModal: React.FC<Props> = ({ recipeId, onClose }) => {
  const [recipeSummary, setRecipeSummary] =
    (useState < RecipeSummary) | (null > null);

  useEffect(() => {
    const fetchRecipeSummary = async () => {
      try {
        const summary = await getRecipeSummary(recipeId);
        setRecipeSummary(summary);
      } catch (error) {
        console.error(error);
      }
    };
    fetchRecipeSummary();
  }, [recipeId]);

  return (
    <div className="overlay">
      <div className="modal">
        <div className="modal-content">
          <div className="modal-header">
            <h2>{recipeSummary?.title}</h2>
            <span className="close-button" onClick={onClose}>
              &times;
            </span>
          </div>
          <p dangerouslySetInnerHTML={{ __html: recipeSummary?.summary }} />
        </div>
      </div>
    </div>
  );
};

export default RecipeModal;

```

### Étape 5 : Styliser le modal

Ajoutez le CSS suivant pour styliser le modal :

```css
/* Fichier : app.css */
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  z-index: 1;
}

.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
  background-color: white;
  padding: 2em;
  border-radius: 4px;
  max-width: 500px;
}

.modal-header {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}

```

### Étape 6 : Rendre et gérer les interactions du modal

Modifiez votre composant principal pour gérer le rendu et les interactions avec le modal.

```jsx
// Fichier : App.tsx
const App: React.FC = () => {
  const [selectedRecipe, setSelectedRecipe] =
    (useState < Recipe) | (undefined > undefined);

  return (
    <div className="App">
      {/* Autres composants et logique */}
      {selectedRecipe && (
        <RecipeModal
          recipeId={selectedRecipe.id.toString()}
          onClose={() => setSelectedRecipe(undefined)}
        />
      )}
    </div>
  );
};

export default App;

```

Maintenant, lorsqu'un utilisateur clique sur une recette, le modal apparaîtra en affichant le résumé de la recette sélectionnée. Le modal peut être fermé en cliquant sur le bouton de fermeture, ce qui définira `selectedRecipe` à undefined, masquant ainsi le modal.

## Comment créer des points de terminaison pour obtenir/créer/supprimer des recettes favorites

### Étape 1 : Configurer la base de données

Tout d'abord, nous devons étendre notre schéma de base de données pour inclure une table de stockage des recettes favorites par leurs identifiants.

Tout d'abord, naviguez vers le dossier `Prisma` dans le répertoire `backend` de votre projet. Ensuite, ouvrez le fichier `schema.prisma`.

Définissez un nouveau modèle pour les recettes favorites comme suit :

```prisma
model FavoriteRecipe {
  id        Int    @id @default(autoincrement())
  recipeId  Int    @unique
}

```

### Étape 2 : Synchroniser le schéma de la base de données

Maintenant, synchronisons le schéma mis à jour avec notre base de données.

```bash
cd backend
npx prisma db push

```

### Étape 3 : Configurer les points de terminaison

Nous devons configurer des points de terminaison dans notre backend Node pour gérer la création, la visualisation et la suppression des favoris. Nous utiliserons le prismaClient pour nous aider à effectuer des opérations crud sur la base de données.

Tout d'abord, nous allons créer un nouveau point de terminaison post comme ceci :

```javascript
// Dans backend/index.ts
import { PrismaClient } from "@prisma/client";

const prismaClient = new PrismaClient();

app.post("/api/recipes/favorite", async (req, res) => {
  const { recipeId } = req.body;
  try {
    const favoriteRecipe = await prismaClient.favoriteRecipe.create({
      data: { recipeId },
    });
    res.status(201).json(favoriteRecipe);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Oops, something went wrong." });
  }
});

```

Ensuite, nous allons créer le point de terminaison de visualisation. Pour cela, créez une fonction utilitaire pour récupérer les détails des recettes par leurs identifiants :

```javascript
// Dans backend/src/recipe-api.ts
export const getFavoriteRecipesByIds = async (ids: string[]) => {
  if (!apiKey) {
    throw new Error("API Key not found");
  }
  const url = new URL("https://api.spoonacular.com/recipes/informationBulk");
  url.search = new URLSearchParams({
    apiKey: apiKey,
    ids: ids.join(","),
  }).toString();

  const response = await fetch(url);
  const json = await response.json();
  return { results: json };
};

```

Maintenant, créez le point de terminaison pour récupérer toutes les recettes favorites :

```javascript
// Dans backend/index.ts
import { getFavoriteRecipesByIds } from "./src/recipe-api";

app.get("/api/recipes/favorite", async (req, res) => {
  try {
    const favoriteRecipes = await prismaClient.favoriteRecipe.findMany();
    const recipeIds = favoriteRecipes.map((recipe) =>
      recipe.recipeId.toString()
    );
    const favorites = await getFavoriteRecipesByIds(recipeIds);
    res.json(favorites);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Oops, something went wrong." });
  }
});

```

Ensuite, le point de terminaison de suppression :

```javascript
// Dans backend/index.ts
app.delete("/api/recipes/favorite", async (req, res) => {
  const { recipeId } = req.body;
  try {
    await prismaClient.favoriteRecipe.delete({
      where: { recipeId },
    });
    res.status(204).send();
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Oops, something went wrong." });
  }
});

```

### Étape 4 : Tester les points de terminaison

Vous pouvez utiliser des outils comme Postman ou Thunder Client pour tester les points de terminaison. Assurez-vous d'ajuster la méthode de requête et l'URL en conséquence, et fournissez le corps ou les paramètres de requête nécessaires.

* **Créer un favori** : requête POST à `/api/recipes/favorite` avec `recipeId` dans le corps.
* **Voir les favoris** : requête GET à `/api/recipes/favorite`.
* **Supprimer un favori** : requête DELETE à `/api/recipes/favorite` avec `recipeId` dans le corps.

### Étape 5 : Vérifier la base de données

Vérifiez la table `favoriteRecipes` dans votre base de données ElephantSQL pour vérifier les actions effectuées via les points de terminaison.

## Comment ajouter la fonctionnalité des favoris au frontend

### Étape 1 : Configurer la fonctionnalité des onglets

Ensuite, nous allons voir comment intégrer ces points de terminaison sur le frontend. Nous allons commencer par configurer des onglets pour 'Recherche' et 'Favoris' dans notre application.

Tout d'abord, définissez un nouvel état pour suivre l'onglet sélectionné.

```javascript
import React, { useState } from "react";

type Tabs = "search" | "favorites";

function App() {
  const [selectedTab, setSelectedTab] = useState < Tabs > "search";

  // Reste de votre code...
}

```

### Étape 2 : Rendre les onglets

Maintenant, vous allez rendre les onglets dans votre JSX, et gérer le changement d'onglet avec l'événement `onClick`. Cela rend chaque élément `<h1>` cliquable, et enregistre l'onglet sur lequel l'utilisateur a cliqué dans l'état. Cela aide à rendre conditionnellement différents éléments de l'interface utilisateur en fonction de leur sélection.

```jsx
// À l'intérieur de votre JSX...
<div className="tabs">
  <h1 onClick={() => setSelectedTab("search")}>Recipe Search</h1>
  <h1 onClick={() => setSelectedTab("favorites")}>Favorites</h1>
</div>

```

### Étape 3 : Rendu conditionnel

En fonction de l'onglet sélectionné, vous souhaitez rendre conditionnellement soit le composant de recherche, soit le composant des favoris. Cela affichera/masquera soit la "section de recherche", soit la "section des favoris" en fonction de la variable d'état `selectedTab`.

```jsx
{selectedTab === 'search' && (
  // code du composant de recherche...
)}
{selectedTab === 'favorites' && (
  // code du composant des favoris...
)}

```

### Étape 4 : Récupérer les recettes favorites

Ensuite, nous devons remplir l'onglet des recettes favorites avec nos recettes favorites. Nous voulons le faire lorsque l'application se charge, pour une expérience utilisateur rapide.

Pour ce faire, récupérez les recettes favorites depuis le backend lorsque l'application se charge en utilisant le hook `useEffect`, et stockez les recettes favorites récupérées dans un nouvel état.

```javascript
// api.ts
export const getFavouriteRecipes = async () => {
  const url = new URL("http://localhost:5000/api/recipes/favourite");
  const response = await fetch(url);

  if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.status}`);
  }
  return response.json();
};

```

```javascript
//App.tsx
import React, { useEffect, useState } from "react";

// ... Reste de vos imports et code

function App() {
  // ... Reste de vos déclarations d'état

  const [favoriteRecipes, setFavoriteRecipes] = useState([]);

  useEffect(() => {
    const fetchFavoriteRecipes = async () => {
      try {
        const favouriteRecipes = await api.getFavouriteRecipes();
        setFavouriteRecipes(favouriteRecipes.results);
      } catch (error) {
        console.error(error);
      }
    };

    fetchFavoriteRecipes();
  }, []);

  // ... Reste de votre code
}

```

### Étape 5 : Rendre les recettes favorites

Maintenant, vous devez rendre les recettes favorites dans l'onglet 'Favoris'.

```jsx
{selectedTab === 'favorites' && (
  <div>
    {favoriteRecipes.map(recipe => (
      // Rendre chaque carte de recette favorite...
    ))}
  </div>
)}

```

### Étape 6 : Ajouter une icône de cœur

Ensuite, nous allons ajouter un moyen pour l'utilisateur d'ajouter et de supprimer des favoris. Nous allons le faire en ajoutant une icône "cœur" à chaque carte. 

Avant de plonger dans le code, assurez-vous d'être dans le bon répertoire en naviguant vers le répertoire front-end de votre projet dans votre terminal. Installez le package nécessaire pour les icônes en exécutant :

```bash
npm install react-icons

```

### Étape 7 : Importer l'icône

Ouvrez le composant `RecipeCard`, et importez l'icône de cœur en haut de votre fichier :

```javascript
import { AiOutlineHeart } from "react-icons/ai";

```

### Étape 8 : Insérer l'icône

Dans le composant `RecipeCard`, ajoutez l'icône de cœur dans un élément `span` juste au-dessus de la balise `h3` :

```javascript
<span onClick={handleFavoriteClick}>
  <AiOutlineHeart size={25} />
</span>

```

### Étape 9 : Ajouter le style CSS

Dans votre fichier `App.css`, ajoutez le CSS suivant pour styliser l'icône et vous assurer qu'elle apparaît sur la même ligne que le titre. En utilisant `flex` et `align-items`, l'icône et le titre seront bien alignés sous l'image :

```css
.recipe-card-title {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

```

### Étape 10 : Créer un gestionnaire d'événements pour ajouter aux favoris

Dans `App.tsx`, créez un gestionnaire d'événements pour ajouter une recette aux favoris. C'est ce qui sera appelé lorsque l'utilisateur clique sur l'icône de cœur d'une recette qui n'a pas encore été ajoutée aux favoris :

```javascript
const addfavoriteRecipe = async (recipe) => {
  try {
    await API.addFavoriteRecipe(recipe);
    setFavoriteRecipes([...favoriteRecipes, recipe]);
  } catch (error) {
    console.log(error);
  }
};

```

### Étape 11 : Logique de l'API

Dans un nouveau fichier appelé `API.ts`, créez une fonction pour gérer l'appel API pour sauvegarder une recette favorite. Cela appellera notre point de terminaison que nous avons créé précédemment dans le backend :

```javascript
export const addFavoriteRecipe = async (recipe) => {
  const body = {
    recipeId: recipe.id,
  };
  const response = await fetch("http://localhost:5000/api/recipes/favourite", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });
  if (!response.ok) {
    throw new Error("Failed to save favorite");
  }
};

```

### Étape 12 : Relier le gestionnaire d'événements

Passez le gestionnaire d'événements au composant `RecipeCard` :

```javascript
<RecipeCard
  //.. autres props
  onFavoriteButtonClick={favoriteRecipe}
/>

```

### Étape 13 : Créer le gestionnaire d'événements pour supprimer des favoris

De même, créez un gestionnaire d'événements pour supprimer une recette des favoris dans `App.tsx` :

```javascript
const removeFavoriteRecipe = async (recipe) => {
  try {
    await API.removeFavoriteRecipe(recipe);
    const updatedRecipes = favoriteRecipes.filter(
      (favRecipe) => favRecipe.id !== recipe.id
    );
    setFavoriteRecipes(updatedRecipes);
  } catch (error) {
    console.log(error);
  }
};

```

### Étape 14 : Logique de l'API

Dans `API.ts`, créez une fonction pour gérer l'appel API pour supprimer une recette des favoris. Encore une fois, cela appellera l'API backend pour supprimer une recette que nous avons créée précédemment :

```javascript
export const removeFavoriteRecipe = async (recipe) => {
  const body = {
    recipeID: recipe.id,
  };
  const response = await fetch("http://localhost:5000/api/recipes/favourite", {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });
  if (!response.ok) {
    throw new Error("Failed to remove favorite");
  }
};

```

### Étape 15 : Gestionnaire d'événements conditionnel

Selon que l'utilisateur "ajoute aux favoris" ou "supprime des favoris" une recette, nous voulons appeler conditionnellement soit `addFavoriteRecipe` soit `removeFavoriteRecipe` en fonction de l'état des favoris :

```javascript
<RecipeCard
  //.. autres props
  onFavoriteButtonClick={isFavorite ? removeFavoriteRecipe : favoriteRecipe}
/>

```

### Étape 16 : Déterminer l'état des favoris

Avant de pouvoir afficher l'icône de cœur dans un état de favori/non favori, nous devons savoir si la recette est déjà un favori ou non.   
  
Pour ce faire, nous déterminons si une recette est un favori en vérifiant si elle existe dans le tableau d'état `favoriteRecipes`. Passez cette information à `RecipeCard` :

```javascript
const isFavorite = favoriteRecipes.some(
  (favRecipe) => favRecipe.id === recipe.id
);
<RecipeCard
  // ...autres props
  isFavorite={isFavorite}
/>;

```

### Étape 17 : Afficher l'état des favoris

Dans `RecipeCard`, affichez conditionnellement une icône de cœur remplie ou en contour en fonction de la prop `isFavorite` :

```javascript
{
  isFavorite ? (
    <AiFillHeart size={25} color="red" />
  ) : (
    <AiOutlineHeart size={25} />
  );
}

```

## Comment ajouter du CSS/du style

### Étape 1 : Préparer l'image héroïque

Nous avons ajouté un style de base jusqu'à présent, alors complétons le CSS pour que notre application ait l'air polie !

Tout d'abord, obtenez une image à partir d'une source comme [Pexels](https://www.pexels.com) ou tout autre dépôt d'images. Cela sera utilisé dans la section Hero de notre application en haut, et aura notre titre superposé dessus. Assurez-vous que l'image a une orientation horizontale pour une meilleure gestion des ratios d'aspect.

Placez l'image dans le dossier `public` de votre projet.

```plaintext
project-folder

public
       hero-image.jpeg

```

### Étape 2 : Structurer l'en-tête

Ouvrez `app.tsx` et localisez le balisage JSX. Ajoutez une `className` de `app-container` à l'élément `div` du haut.

À l'intérieur de la div `app-container`, ajoutez une nouvelle `div` avec une `className` de `header`. À l'intérieur de la div `header`, ajoutez un élément `img` avec un attribut `src` pointant vers votre image, et un élément `div` avec une `className` de `title` contenant le titre de l'application.

```jsx
<div className="app-container">
  <div className="header">
    <img src="/hero-image.jpeg" alt="Hero" />
    <div className="title">My Recipe App</div>
  </div>
  {/* ...reste de votre code */}
</div>

```

### Étape 3 : Styliser l'en-tête

Ouvrez `app.css` et faites défiler vers le haut. Ajoutez le CSS suivant pour styliser les éléments `app-container`, `header`, `img` et `title`. Cela fait apparaître le `title` au-dessus de l'image, avec un fond translucide :

```css
.app-container {
  display: flex;
  flex-direction: column;
  gap: 2em;
}

.header {
  position: relative;
}

.header img {
  width: 100%;
  height: 500px;
  object-fit: cover;
  object-position: center;
  opacity: 0.5;
  border-radius: 1em;
}

.title {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 2em;
  text-align: center;
  background-color: black;
  opacity: 0.8;
  padding: 0.5em 1.5em 0.5em 1.5em;
}

```

### Étape 4 : Ajuster la mise en page

Ajoutez un remplissage à l'élément `body` et utilisez une requête média pour ajouter des marges sur les grands écrans. Nous faisons cela pour que notre application n'apparaisse pas trop étroite sur les appareils mobiles. Lorsque la taille de l'écran atteint `768px`, la requête média se déclenchera et ajoutera une marge à gauche et à droite de notre application, de sorte que l'application n'apparaisse pas trop large.

```css
body {
  padding: 5em 0;
  height: 100vh;
  background-color: #f0f0f0; /* ou toute couleur que vous préférez */
}

@media (min-width: 768px) {
  body {
    margin-left: 10em;
    margin-right: 10em;
  }
}

```

### Étape 5 : Styliser le soulignement des onglets

Actuellement, il n'est pas clair quel onglet l'utilisateur a sélectionné. Ce que nous voulons faire, c'est ajouter un soulignement orange à l'onglet sélectionné. Pour ce faire, nous pouvons utiliser une combinaison de classes CSS et de rendu conditionnel.

Dans `app.tsx`, localisez vos éléments `h1` représentant les onglets, et appliquez dynamiquement une `className` de `tab-active` en fonction de l'onglet sélectionné.

```jsx
<h1 className={selectedTab === 'search' ? 'tab-active' : ''}>Search</h1>
<h1 className={selectedTab === 'favorites' ? 'tab-active' : ''}>Favorites</h1>

```

Dans `app.css`, définissez la classe `tab-active` :

```css
.tab-active {
  border-bottom: 4px solid orange; /* ou toute couleur que vous préférez */
  padding-bottom: 0.5em;
}

```

### Étape 6 : Styliser la barre de recherche

Nous voulons que notre barre de recherche prenne toute la largeur du conteneur, et nous voulons ajouter une icône au lieu du bouton de recherche, ce qui rend notre interface utilisateur plus intéressante. 

Dans `app.tsx`, localisez l'élément `form` dans l'onglet `Search`. Remplacez le texte "Submit" dans l'élément `button` par une icône d'une bibliothèque comme React Icons.

```jsx
<button>
  <AiOutlineSearch size={40} />
</button>

```

Dans `app.css`, stylisez les éléments `form`, `input` et `button` :

```css
form {
  display: flex;
  background-color: white;
  align-items: center;
}

input {
  padding: 0.5em;
  font-size: 2em;
  flex: 1;
  border: none;
}

input:focus {
  outline: none;
}

button {
  background-color: white;
  border: none;
  cursor: pointer;
}

```

### Étape 7 : Implémenter une grille de cartes de recettes réactive

Actuellement, nos cartes de recettes sont empilées horizontalement. Nous allons utiliser la grille CSS pour faire apparaître les cartes de recettes dans une mise en page de grille, ce qui rendra également les choses plus réactives. 

Dans `app.tsx`, créez une nouvelle `div` avec une `className` de `recipe-grid` juste au-dessus de l'endroit où vous mappez vos recettes, et placez la logique de rendu des recettes à l'intérieur de cette `div`.

```jsx
<div className="recipe-grid">
  {recipes.map((recipe) => {
    const isFavourite = favouriteRecipes.some((favRecipe) => favRecipe.id === recipe.id);

    return (
      <RecipeCard
        key={recipe.id}
        recipe={recipe}
        onFavouriteButtonClick={isFavourite ? removeFavouriteRecipe : addFavouriteRecipe}
        onClick={() => setSelectedRecipe(recipe)}
        isFavourite={isFavourite}
      />
    );
  })}
</div>
```

Dans `app.css`, stylisez les éléments `recipe-grid` et `recipe-card` :

```css
.recipe-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  gap: 2em;
}

.recipe-card {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  background-color: white;
  padding: 1em;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  position: relative;
  cursor: pointer;
  gap: 1.5em;
}

.recipe-card h3 {
  font-size: 1.5em;
  margin: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

```

### Étape 8 : Dernières touches

Stylisez le bouton "Voir plus" pour vous assurer qu'il correspond au style de notre application et qu'il est centré sous notre grille de recettes :

```css
.view-more-button {
  font-size: 1.5em;
  padding: 1em;
  font-weight: bold;
  margin: auto;
}

```

## Conclusion

Félicitations pour être arrivé à la fin ! Espérons que vous avez appris quelques choses sur le développement full stack en utilisant React et Node. 

Si vous avez apprécié ce projet, vous pouvez en trouver d'autres sur [CodeCoyotes.com](https://www.codecoyotes.com/), où vous pouvez également m'envoyer un message si vous avez besoin de me contacter.   
  
Merci d'avoir lu, à la prochaine !