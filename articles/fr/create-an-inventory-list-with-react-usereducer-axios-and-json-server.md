---
title: Comment créer une liste d'inventaire avec React useReducer, Axios et JSON Server
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2024-03-07T15:33:49.000Z'
originalURL: https://freecodecamp.org/news/create-an-inventory-list-with-react-usereducer-axios-and-json-server
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/inventory-list.png
tags:
- name: axios
  slug: axios
- name: hooks
  slug: hooks
- name: React
  slug: react
seo_title: Comment créer une liste d'inventaire avec React useReducer, Axios et JSON
  Server
seo_desc: 'When it comes to web development, it''s hard to ignore React.js. It has
  been one of the leading user interface libraries for a decade, and it supports a
  lot of popular frameworks like Next.js in the background.

  If you are a React developer, you likely...'
---

En matière de développement web, il est difficile d'ignorer React.js. Il est l'une des principales bibliothèques d'interface utilisateur depuis une décennie et il supporte de nombreux frameworks populaires comme Next.js en arrière-plan.

Si vous êtes un développeur React, vous appréciez probablement son architecture basée sur les composants, la liaison de données unidirectionnelle, le grand soutien de la communauté et la passion de l'équipe React pour apporter des fonctionnalités aux développeurs.

Si vous débutez avec React ou si vous êtes un débutant, c'est génial – il y a une [feuille de route complète React.js publiée ici](https://www.freecodecamp.org/news/react-fundamentals-for-beginners/) sur freeCodeCamp que vous pouvez consulter. Et je pense que vous trouverez la bibliothèque beaucoup plus facile à apprendre si vous avez une bonne maîtrise des bases de JavaScript.

Quelle que soit votre expérience avec React, le vrai plaisir réside dans la construction de choses avec, n'est-ce pas ? J'ai donc pensé à créer une simple `liste d'inventaire` pour expliquer quelques concepts puissants comme la gestion d'état complexe avec useReducer.

Et pendant que nous faisons cela, nous allons également créer un serveur API mock en utilisant `JSON Server`, nous allons utiliser `axios` pour appeler l'API, et enfin nous allons utiliser le hook `useReducer` pour gérer l'état.

Cela semble intéressant ? Commençons. Si vous souhaitez également consulter la version vidéo de ce projet, la voici : 😊

%[https://www.youtube.com/watch?v=jKyAEj0EvAA]

## Table des matières

* [Configuration du projet avec React et TailwindCSS](#heading-installation-du-projet-avec-react-et-tailwindcss)
* [Comment configurer un serveur avec JSON Server](#heading-comment-configurer-un-serveur-avec-json-server)
* [Comment configurer et utiliser Axios](#heading-comment-configurer-et-utiliser-axios)
* [Comment utiliser le hook useReducer de React](#heading-comment-utiliser-le-hook-usereducer-de-react)
* [Comment créer des actions](#heading-comment-creer-des-actions)
* [Comment créer un réducteur d'inventaire](#heading-comment-creer-un-reducteur-dinventaire)
* [Comment construire le composant de liste d'inventaire](#heading-comment-construire-le-composant-de-liste-dinventaire)
* [Comment utiliser Axios pour récupérer des données et les transmettre au réducteur](#heading-comment-utiliser-axios-pour-recuperer-des-donnees-et-les-transmettre-au-reducteur)
* [Complétons la partie JSX](#heading-completons-la-partie-jsx)
* [Comment utiliser la liste d'inventaire dans le composant App](#heading-comment-utiliser-la-liste-dinventaire-dans-le-composant-app)
* [Conclusion](#heading-conclusion)

## Installation du projet avec React et TailwindCSS

Avant de faire quoi que ce soit d'autre, commençons par configurer le projet. Vous pouvez également suivre le [code source](https://github.com/atapas/youtube/tree/main/react/27-inventory-useReducer-jsonserver-axios) tout en lisant.

Pour construire cette application, nous utiliserons React avec `Vite` et `TailwindCSS`. Vous pouvez configurer ces outils en suivant quelques étapes de la documentation [Vite](https://vitejs.dev/guide/) et [TailwindCSS](https://tailwindcss.com/docs/guides/vite).

Mais pourquoi ne pas utiliser quelque chose qui fournit tout intégré ? Cela vous fera gagner du temps pour les futurs projets React, car vous pourrez utiliser la même infrastructure pour créer des projets React à chaque fois.

Rendez-vous sur ce [dépôt](https://github.com/atapas/vite-tailwind-react) et cliquez sur le bouton `Use this template` comme indiqué dans l'image ci-dessous. Cela vous aidera à créer un tout nouveau dépôt à partir d'un dépôt de modèle avec Vite, React et TailwindCSS configurés.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-12-at-5.25.29-PM.png)
_Créer un dépôt de projet React avec TailwindCSS et Vite à partir d'un modèle existant_

Maintenant, donnez un nom approprié à votre dépôt (appelons-le `inventory-list` dans cet article) ainsi qu'une description. Vous pouvez choisir de garder le dépôt privé si vous le souhaitez, sinon allez-y et créez le dépôt en cliquant sur le bouton en bas.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-12-at-5.30.34-PM.png)
_Fournir les détails du nouveau dépôt_

C'est tout. Vous avez un dépôt avec tous les ingrédients de base pour commencer. Maintenant, allez à l'invite de commande/terminal et clonez le dépôt nouvellement créé :

```bash
git clone <URL DE VOTRE NOUVEAU DÉPÔT>
```

Changez de répertoire pour le répertoire du projet et installez les dépendances du projet en utilisant les commandes suivantes :

```bash
## Changer pour le répertoire du projet
cd inventory-list

## Installer les dépendances

## En utilisant NPM
npm install

## En utilisant Yarn
yarn install

## En utilisant PNPM
pnpm install 
```

Après l'installation réussie des dépendances, exécutez la commande suivante pour exécuter le projet sur un serveur local :

```bash
## Exécuter le projet localement

## En utilisant NPM
npm run dev

## En utilisant Yarn
yarn dev

## En utilisant PNPM
pnpm dev
```

Maintenant, le projet devrait s'exécuter localement et devrait être accessible sur l'URL par défaut, `http://localhost:5173`. Vous pouvez accéder à l'URL sur votre navigateur et importer le code source du projet dans votre éditeur de code préféré (j'utilise VS Code). Nous sommes prêts à commencer le codage.

## Comment configurer un serveur avec JSON Server

`JSON Server` est l'option privilégiée lorsque vous souhaitez travailler avec des API factices/mock pour servir des données de votre choix. Il est facile à configurer et à personnaliser selon votre cas d'utilisation.

Configurons le JSON Server pour notre projet. La première chose à faire est de l'installer.

Ouvrez un terminal à la racine du dossier du projet et tapez la commande suivante pour installer JSON Server :

```shell
## En utilisant NPM
npm install json-server

## En utilisant Yarn
yarn add json-server

## En utilisant PNPM
pnpm install json-server
```

JSON Server utilise des fichiers JSON comme sources de données pour effectuer des opérations HTTP comme GET/POST/PUT/PATCH/DELETE. Créez un répertoire `server/database` sous le répertoire `src/`. Maintenant, créez un fichier appelé `data.json` sous `src/server/database/` avec le contenu suivant :

```json
{
  "edibles": [
    {
      "id": 1,
      "picture": "🍌",
      "name": "Banane",
      "price": 32,
      "quantity": 200,
      "type": "fruits"
    },
    {
      "id": 2,
      "picture": "🍓",
      "name": "Fraise",
      "price": 52,
      "quantity": 100,
      "type": "fruits"
    },
    {
      "id": 3,
      "picture": "🍗",
      "name": "Poulet",
      "price": 110,
      "quantity": 190,
      "type": "aliments",
      "sub-type": "Non-Végétarien"
    },
    {
      "id": 4,
      "picture": "🥬",
      "name": "Laitue",
      "price": 12,
      "quantity": 50,
      "type": "Légumes"
    },
    {
      "id": 5,
      "picture": "🍅",
      "name": "Tomate",
      "price": 31,
      "quantity": 157,
      "type": "Légumes"
    },
    {
      "id": 6,
      "picture": "🥩",
      "name": "Mouton",
      "price": 325,
      "quantity": 90,
      "type": "Non-Végétarien"
    },
    {
      "id": 7,
      "picture": "🥕",
      "name": "Carotte",
      "price": 42,
      "quantity": 190,
      "type": "Légumes"
    }
  ]
}
```

Le fichier `data.json` contient un tableau d'articles comestibles. Chacun des articles du tableau possède des propriétés comme picture, name, price, quantity et type à afficher dans la liste d'inventaire.

La dernière chose à faire est d'ajouter un script dans le fichier `package.json` afin de pouvoir démarrer le JSON Server facilement à chaque fois. Ouvrez le fichier package.json et ajoutez cette ligne à l'intérieur de l'objet `scripts` comme ceci :

```json
"start-server": "json-server --watch ./src/server/database/data.json"
```

Ensuite, allez dans le terminal et utilisez la commande suivante pour démarrer le JSON Server afin de servir l'API :

```shell
## En utilisant NPM
npm run start-server

## En utilisant Yarn
yarn start-server

## En utilisant PNPM
pnpm run start-server
```

Vous devriez voir un message comme celui-ci dans votre terminal :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-07-at-8.46.32-AM-1.png)
_La sortie_

Cela indique que le JSON Server est en cours d'exécution localement sur `localhost:3000` et qu'il existe un point de terminaison d'API appelé `edibles` qui sert les données. Vous pouvez maintenant accéder à l'URL `http://localhost:3000/edibles` depuis votre navigateur pour voir les données (récupérées par un appel de méthode GET) :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-32.png)
_La sortie de l'API_

Super ! Maintenant, nous avons le point de terminaison d'API `/edibles` prêt à être consommé dans le composant React.

## Comment configurer et utiliser Axios

`Axios` est un client HTTP qui nous aide à effectuer des appels asynchrones basés sur les promesses depuis le navigateur et l'environnement Node.js. Il possède un certain nombre de [fonctionnalités utiles](https://www.npmjs.com/package/axios#features) qui en font l'une des bibliothèques les plus utilisées pour les requêtes-réponses asynchrones.

Notez que nous aurions pu utiliser le `fetch Web API` de JavaScript au lieu d'`Axios` dans ce projet. La seule raison d'utiliser Axios ici est de l'introduire progressivement. Dans les futurs articles, vous apprendrez ses usages dans la gestion des jetons JWT depuis une application React. Restez à l'écoute !

Ouvrez le terminal à la racine du dossier du projet et utilisez la commande suivante pour installer Axios :

```shell
## En utilisant NPM
npm install axios

## En utilisant Yarn
yarn add axios

## En utilisant PNPM
pnpm install axios
```

C'est tout. Nous utiliserons Axios dans un instant après avoir disposé les composants de base nécessaires pour la liste d'inventaire.

## Comment utiliser le hook useReducer de React

React est une bibliothèque d'interface utilisateur qui supporte l'architecture basée sur les composants au cœur. Un composant est une entité unique qui est censée effectuer une tâche bien. Plusieurs composants se réunissent pour composer l'interface utilisateur finale.

Souvent, un composant aura ses propres données privées. Nous appelons cela les `états` d'un composant. La valeur d'un état détermine le comportement et l'apparence d'un composant. Lorsque l'état change, le composant se réaffiche pour se tenir à jour avec la dernière valeur de l'état.

La manière traditionnelle de gérer l'état dans React est avec le hook `useState`. Il fonctionne très bien tant que vos changements d'état sont triviaux. Lorsque la logique de changement d'état devient plus complexe et si vous devez gérer plusieurs scénarios autour, `useState` peut rendre les choses maladroites. C'est là que vous devriez penser à utiliser le hook `useReducer`.

`useReducer` est un hook standard de la bibliothèque React. Il accepte deux paramètres principaux :

* `initState` : la valeur initiale de l'état
* `reducer` : une fonction JavaScript qui contient la logique de changement d'état basée sur une action (ou un déclencheur).

Le hook retourne les éléments suivants :

* Un `state` : la valeur actuelle de l'état.
* Une fonction `dispatch` : une fonction qui indique au réducteur respectif quoi faire ensuite, et sur quelles données agir.

L'image ci-dessous explique chacune des entités du hook `useReducer`. Si vous souhaitez en apprendre davantage sur ce hook, n'hésitez pas à [consulter cela](https://www.youtube.com/watch?v=PMyPyT8N4m8).

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-27.png)
_L'anatomie du hook useReducer_

## Comment créer des actions

La fonction de réduction est le cœur du hook useReducer. Elle effectue toute la logique nécessaire pour maintenir l'état de votre application à jour et valide.

Mais comment la fonction de réduction serait-elle consciente de sa tâche ? Qui dirait à la fonction de réduction quoi faire et quel type de données traiter ? Voici les `actions`, un objet qui contient tous les détails pour le réducteur.

Nous définissons des actions avec des types qui indiquent les étapes où un changement d'état se produira dans la fonction de réduction. Le même objet d'action peut également transporter les données de l'application (parfois nous l'appelons payload) à passer à la fonction de réduction lorsqu'un composant effectue un dispatch.

Nous allons maintenant commencer par créer quelques actions. Nous définirons les types ici. Comme notre réducteur doit gérer l'état de l'inventaire lors d'une récupération de données, d'un succès de récupération de données et d'une erreur de récupération de données, nous définirons des actions pour chacune de ces étapes.

Créez un répertoire appelé `actions/` sous le répertoire `src/`. Maintenant, créez un fichier appelé `index.js` sous le répertoire `src/actions/` avec le contenu suivant :

```js
const FETCH_ACTIONS = {
  PROGRESS: 'progress',
  SUCCESS: 'success',
  ERROR: 'error',
}

export { FETCH_ACTIONS };
```

Nous avons défini trois actions, PROGRESS, SUCCESS et ERROR. Ensuite, créons le réducteur.

## Comment créer un réducteur d'inventaire

Nous avons besoin d'un réducteur où nous garderons toute la logique de changement d'état. Le même réducteur sera passé au hook `useReducer` plus tard pour obtenir la valeur actuelle de l'état et dispatcher la fonction au composant.

Créez un répertoire appelé `reducers/` sous `src/`. Maintenant, créez un fichier appelé `inventoryReducers.js` sous le répertoire `src/reducers/`.

Notre réducteur aura besoin des actions car il doit travailler sur les changements d'état basés sur les actions. Donc, importons les actions dans le fichier `inventoryReducers.js` :

```js
import { FETCH_ACTIONS } from "../actions"
```

Vous pouvez définir un état initial dans le fichier du réducteur. Le hook `useReducer` a besoin d'un réducteur et d'un état initial pour nous donner la valeur actuelle de l'état, vous vous souvenez ? Définissons un état initial.

Nous devons afficher une liste d'articles d'inventaire après avoir obtenu une réponse API réussie. Pendant que nous récupérons la liste des articles en faisant un appel API, nous devons gérer un état de chargement des données.

Au cas où il y aurait un problème dans la récupération des données, nous devons signaler l'erreur en utilisant l'état d'erreur. Nous pouvons donc créer un état initial avec toutes ces valeurs comme propriétés d'objet.

Maintenant, créez une variable initialState avec la valeur de l'objet d'état suivante qui lui est assignée :

```js
const initialState = {
  items: [],
  loading: false,
  error: null,
}
```

Ensuite, créons la fonction de réduction. Créez une fonction appelée `inventoryReducer` avec le fragment de code suivant :

```js
const inventoryReducer = (state, action) => {

  switch (action.type) {
    case FETCH_ACTIONS.PROGRESS: {
      return {
        ...state,
        loading: true,
      }
    }

    case FETCH_ACTIONS.SUCCESS: {
      return {
        ...state,
        loading: false,
        items: action.data,
      }
    }

    case FETCH_ACTIONS.ERROR: {
      return {
        ...state,
        loading: false,
        error: action.error,
      }
    }
    
    default: {
      return state;
    }      
  }

}
```

Comprenons le fragment de code ci-dessus. La fonction `inventoryReducer` prend deux arguments, `state` et `action`. La fonction de réduction travaille sur l'état en fonction du type d'action. Par exemple,

* Lorsqu'il s'agit d'une action `PROGRESS`, nous voulons que la valeur `loading` soit vraie.
* Pour une action `SUCCESS`, nous voulons remplir les `items` avec les données reçues de la réponse de l'API tout en mettant la valeur `loading` à false.
* Pour une action `ERROR`, nous fournirons une valeur à la propriété `error` de l'état.

Dans l'un des cas ci-dessus, nous ne mutons pas directement l'état. Plutôt, nous créons un clone (une nouvelle référence de celui-ci en utilisant l'opérateur `...`) de l'état, puis nous mettons à jour ses propriétés en conséquence. Enfin, nous retournons l'état mis à jour pour chacune des actions. Si les actions passées ne correspondent à aucun des types donnés, nous retournons l'état tel quel.

Enfin, exportez la fonction `inventoryReducer` et l'objet `initialState` :

```js
export {inventoryReducer, initialState};
```

Voici le code complet du fichier `inventoryReducers.js` :

```js
import { FETCH_ACTIONS } from "../actions"

const initialState = {
  items: [],
  loading: false,
  error: null,
}

const inventoryReducer = (state, action) => {

  switch (action.type) {
    case FETCH_ACTIONS.PROGRESS: {
      return {
        ...state,
        loading: true,
      }
    }

    case FETCH_ACTIONS.SUCCESS: {
      return {
        ...state,
        loading: false,
        items: action.data,
      }
    }

    case FETCH_ACTIONS.ERROR: {
      return {
        ...state,
        loading: false,
        error: action.error,
      }
    }
    
    default: {
      return state;
    } 
  }

}

export {inventoryReducer, initialState};
```

## Comment construire le composant de liste d'inventaire

Nous allons maintenant créer le composant de liste d'inventaire où nous utiliserons le réducteur que nous avons créé ci-dessus.

Créez un répertoire appelé `components/` sous le répertoire `src/`. Maintenant, créez un fichier appelé `InventoryList.jsx` sous le répertoire `stc/components/`.

Tout d'abord, importez les éléments nécessaires comme :

* Le hook `useReducer` où nous utiliserons le réducteur d'inventaire.
* Le hook `useEffect` pour gérer l'appel asynchrone avec Axios.
* Le `inventory reducer` et l'`initial state` que nous avons créés il y a quelques minutes.
* Les `actions`, car nous en avons besoin pour dispatcher.
* L'`axios` pour effectuer des appels asynchrones.

```js
import { useReducer, useEffect } from "react";

import { inventoryReducer, initialState } from "../reducers/inventoryReducer";

import { FETCH_ACTIONS } from "../actions";

import axios from "axios";
```

Maintenant, créez une fonction pour définir le composant :

```js
const InventoryList = () => {

  const [state, dispatch] = useReducer(inventoryReducer, initialState);

  const { items, loading, error} = state;

  return(
    <div className="flex flex-col m-8 w-2/5">
      
    </div>
  );
};
```

Ici,

* Nous avons utilisé le hook `useReducer`. Nous lui avons passé le `inventoryReducer` et l'`initialState` en tant qu'arguments pour obtenir la valeur actuelle de l'`state` et la fonction `dispatch`.
* Comme nous savons que l'objet state a les propriétés `items`, `loading` et `error`, nous les `destructurons` dans notre composant. Nous les utiliserons bientôt.
* Le composant retourne une div vide que nous modifierons au fur et à mesure.

Enfin, exportez le composant comme une exportation par défaut comme ceci :

```js
export default InventoryList;
```

## Comment utiliser Axios pour récupérer des données et les transmettre au réducteur

C'est l'heure de la récupération des données ! La récupération des données en effectuant un appel asynchrone est un effet secondaire que vous devez gérer dans votre composant. Copiez et collez le bloc de code `useEffect` à l'intérieur de la fonction `InventoryList`.

```js
// -- Le code ci-dessus tel quel

const InventoryList = () => {

  // --- Le code ci-dessus tel quel
    
    
  useEffect(() => {
    dispatch({type: FETCH_ACTIONS.PROGRESS});

    const getItems = async () => {
      try{
        let response = await axios.get("http://localhost:3000/edibles");
        if (response.status === 200) {
          dispatch({type: FETCH_ACTIONS.SUCCESS, data: response.data});
        }
      } catch(err){
        console.error(err);
        dispatch({type: FETCH_ACTIONS.ERROR, error: err.message})
      }
    }

    getItems();

  }, []);
    
  // --- L'instruction de retour JSX ci-dessous telle quelle  

```

Comprenons le flux de code :

* Au début du rappel `useEffect`, nous avons dispatché une action `PROGRESS`. Cela invoque la fonction de réduction avec le type d'action de progression pour mettre la valeur de la propriété `loading` à true. Nous pouvons utiliser la valeur de la propriété loading dans le JSX plus tard pour afficher un indicateur de chargement.
* Ensuite, nous utilisons Axios pour effectuer un appel asynchrone en utilisant l'URL de l'API. En recevant la réponse, nous vérifions si c'est un succès, et dans ce cas, nous dispatchons une action `SUCCESS` avec les données `items` (vous vous souvenez, payload ?) de la réponse. Cette fois, le dispatcher invoquera le réducteur avec l'action de succès pour changer les propriétés `items` et `loading` en conséquence.
* Si une erreur se produit, nous dispatchons une action d'erreur avec le message d'erreur pour mettre à jour l'état avec les informations d'erreur dans le réducteur.

Chaque fois que nous dispatchons une action et mettons à jour l'état, nous obtenons également la dernière valeur de l'état dans notre composant. Il est temps d'utiliser la valeur de l'état dans le JSX pour rendre la liste des articles d'inventaire.

## Complétons la partie JSX

La partie JSX est assez simple :

```js

// -- Le code ci-dessus tel quel

const InventoryList = () => {

  // -- Le code ci-dessus tel quel

  return (
    <div className="flex flex-col m-8 w-2/5">
      {
        loading ? (
          <p>Chargement...</p>
        ) : error ? (
          <p>{error}</p>
        ) : (
          <ul className="flex flex-col">
            <h2 className="text-3xl my-4">Liste des articles</h2>
            {
              items.map((item) => (
                <li
                  className="flex flex-col p-2 my-2 bg-gray-200 border rounded-md" 
                  key={item.id}>
                  <p className='my-2 text-xl'>
                    <strong>{item.name}</strong> {' '} {item.picture} de type <strong>{item.type}</strong>
                    {' '} coûte <strong>{item.price}</strong> INR/KG.
                  </p>
                  <p className='mb-2 text-lg'>
                    Disponible en stock : <strong>{item.quantity}</strong>
                  </p>

                </li>
              ))
            }
            
          </ul>
        )
      }

    </div>
  )
}

export default InventoryList;
```

Voici ce qui se passe dans le code :

* Nous affichons un message `Chargement...` si la propriété loading de l'état est vraie.
* Nous affichons le message d'erreur en cas d'erreur.
* Dans aucun des cas, nous parcourons les articles d'inventaire en utilisant la fonction map. Chacun des articles dans le tableau `items` a des informations comme picture, name, price, et plus encore. Nous affichons ces informations de manière significative.

Voici le code complet du composant `InventoryList` :

```js

import { useReducer, useEffect } from "react";
import { inventoryReducer, initialState } from "../reducers/inventoryReducer";
import { FETCH_ACTIONS } from "../actions";

import axios from "axios";

const InventoryList = () => {

  const [state, dispatch] = useReducer(inventoryReducer, initialState);

  const { items, loading, error} = state;

  console.log(items, loading, error);

  useEffect(() => {
    dispatch({type: FETCH_ACTIONS.PROGRESS});

    const getItems = async () => {
      try{
        let response = await axios.get("http://localhost:3000/edibles");
        if (response.status === 200) {
          dispatch({type: FETCH_ACTIONS.SUCCESS, data: response.data});
        }
      } catch(err){
        console.error(err);
        dispatch({type: FETCH_ACTIONS.ERROR, error: err.message})
      }
    }

    getItems();

  }, []);


  return (
    <div className="flex flex-col m-8 w-2/5">
      {
        loading ? (
          <p>Chargement...</p>
        ) : error ? (
          <p>{error}</p>
        ) : (
          <ul className="flex flex-col">
            <h2 className="text-3xl my-4">Liste des articles</h2>
            {
              items.map((item) => (
                <li
                  className="flex flex-col p-2 my-2 bg-gray-200 border rounded-md" 
                  key={item.id}>
                  <p className='my-2 text-xl'>
                    <strong>{item.name}</strong> {' '} {item.picture} de type <strong>{item.type}</strong>
                    {' '} coûte <strong>{item.price}</strong> INR/KG.
                  </p>
                  <p className='mb-2 text-lg'>
                    Disponible en stock : <strong>{item.quantity}</strong>
                  </p>

                </li>
              ))
            }
            
          </ul>
        )
      }

    </div>
  )
}

export default InventoryList
```

## Comment utiliser la liste d'inventaire dans le composant App

Maintenant, nous devons faire connaître le composant `App` du composant `InventoryList` afin de pouvoir le rendre. Ouvrez le fichier `App.jsx` et remplacez son contenu par le fragment de code suivant :

```js
import InventoryList from "./components/InventoryList"

function App() {

  return (
    <>
      <InventoryList />
    </>
  )
}

export default App
```

C'est tout. Assurez-vous que votre serveur d'application est en cours d'exécution. Maintenant, accédez à l'application sur votre navigateur en utilisant l'URL [`http://localhost:5173/`](http://localhost:5173/).

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-28.png)
_La sortie finale - Liste d'inventaire_

## Conclusion

J'espère que vous avez apprécié la construction de ce projet et en apprendre davantage sur React. [Voici le code source](https://github.com/atapas/youtube/tree/main/react/27-inventory-useReducer-jsonserver-axios) sur mon GitHub. N'hésitez pas à étendre le projet en ajoutant des fonctionnalités comme :

* Ajouter un article à l'inventaire
* Modifier un article de l'inventaire
* Supprimer un article de l'inventaire

Indice : Vous devez créer des actions pour chacune de ces étapes et améliorer la fonction de réduction pour écrire la logique de mise à jour de l'état afin de prendre en charge ces fonctionnalités. J'espère que vous essayerez et si vous le faites, faites-le moi savoir (mes coordonnées sont mentionnées ci-dessous).

C'est tout pour l'instant. Je publie également des articles significatifs sur mon [blog GreenRoots](https://blog.greenroots.info/), et je pense que vous les trouverez utiles également.

Restez en contact.

* Je suis un éducateur sur ma chaîne YouTube, `tapaScript`. Veuillez [vous ABONNER](https://www.youtube.com/tapasadhikary?sub_confirmation=1) à la chaîne si vous souhaitez apprendre JavaScript, ReactJS, Next.js, Node.js, Git et tout sur le développement web de manière fondamentale.
* [Suivez-moi sur X (Twitter)](https://twitter.com/tapasadhikary) ou [LinkedIn](https://www.linkedin.com/in/tapasadhikary/) si vous ne voulez pas manquer la dose quotidienne de conseils sur le développement web et la programmation.
* Retrouvez toutes mes conférences publiques [ici](https://www.tapasadhikary.com/talks).
* Consultez et suivez mon travail Open Source sur [GitHub](https://github.com/atapas).

À bientôt avec mon prochain article. En attendant, prenez soin de vous et restez heureux.