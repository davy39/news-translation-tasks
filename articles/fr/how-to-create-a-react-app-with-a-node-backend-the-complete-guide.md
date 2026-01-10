---
title: 'Comment créer une application React avec un backend Node : Le guide complet'
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-02-03T23:10:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-react-app-with-a-node-backend-the-complete-guide
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/how-to-build-a-react-app-with-a-node-backend-alt.png
tags:
- name: full stack
  slug: full-stack
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
- name: React
  slug: react
seo_title: 'Comment créer une application React avec un backend Node : Le guide complet'
seo_desc: "A React frontend connected to a Node backend is a rock-solid combination\
  \ for any application you want to build. \nThis guide is designed to help you create\
  \ full-stack projects with React as easily as possible.\nLet's see how to set up\
  \ an entire project..."
---

Une interface React connectée à un backend Node est une combinaison solide pour toute application que vous souhaitez construire. 

Ce guide est conçu pour vous aider à créer des projets full-stack avec React aussi facilement que possible.

Voyons comment configurer un projet entier en utilisant React et Node à partir de zéro et le déployer sur le web.

## Outils dont vous aurez besoin

1. Assurez-vous que Node et NPM sont installés sur votre ordinateur. Vous pouvez télécharger les deux sur [nodejs.org](https://nodejs.org) (NPM est inclus dans votre installation de Node)
2. Utilisez un éditeur de code de votre choix. J'utilise et recommande personnellement VSCode. Vous pouvez télécharger VSCode sur [code.visualstudio.com](https://code.visualstudio.com).
3. Assurez-vous que Git est installé sur votre ordinateur. Cela est nécessaire pour déployer notre application avec Heroku. Vous pouvez l'obtenir sur [git-scm.com](https://git-scm.com)
4. Un compte sur [heroku.com](https://heroku.com). 

## Étape 1 : Créer votre backend Node (Express)

Tout d'abord, créez un dossier pour votre projet, appelé `react-node-app` (par exemple). 

Ensuite, glissez ce dossier dans votre éditeur de code.

Pour créer notre projet Node, exécutez la commande suivante dans votre terminal :

```bash
npm init -y
```

Cela créera un fichier package.json qui nous permettra de suivre tous nos scripts d'application et de gérer les dépendances dont notre application Node a besoin.

Notre code serveur résidera dans un dossier du même nom : `server`. Créons ce dossier.

Dans celui-ci, nous placerons un seul fichier à partir duquel nous exécuterons notre serveur : `index.js`.

Nous utiliserons Express pour créer un simple serveur web pour nous qui s'exécute sur le port 3001 si aucune valeur n'est donnée pour la variable d'environnement `PORT` (Heroku définira cette valeur lorsque nous déployerons notre application).

```js
// server/index.js

const express = require("express");

const PORT = process.env.PORT || 3001;

const app = express();

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});
```

Ensuite, dans notre terminal, nous installerons Express comme dépendance pour l'utiliser :

```bash
npm i express
```

Après cela, nous créerons un script dans package.json qui démarrera notre serveur web lorsque nous l'exécuterons avec `npm start` :

```json
// server/package.json

...
"scripts": {
  "start": "node server/index.js"
},
...
```

Enfin, nous pouvons exécuter notre application en utilisant ce script en exécutant npm start dans notre terminal et nous devrions voir qu'elle s'exécute sur le port 3001 :

```bash
npm start

> node server/index.js

Server listening on 3001
```

![Clip 1](https://reedbarger.nyc3.digitaloceanspaces.com/how-to-create-a-react-app-with-a-node-backend/clip-1.gif)

## Étape 2 : Créer un point de terminaison API

Nous voulons utiliser notre serveur Node et Express comme une API, afin qu'il puisse fournir des données à notre application React, modifier ces données, ou effectuer une autre opération qu'un serveur peut faire.

Dans notre cas, nous allons simplement envoyer à notre application React un message qui dit "Hello from server!" dans un objet JSON.

Le code ci-dessous crée un point de terminaison pour la route `/api`.

Si notre application React fait une requête GET à cette route, nous répondons (en utilisant `res`, qui signifie réponse) avec nos données JSON :

```js
// server/index.js
...

app.get("/api", (req, res) => {
  res.json({ message: "Hello from server!" });
});

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});
```

_Note : Assurez-vous de placer ceci au-dessus de la fonction `app.listen`._

Puisque nous avons apporté des modifications à notre code Node, nous devons redémarrer notre serveur.

Pour ce faire, terminez votre script de démarrage dans le terminal en appuyant sur Command/Ctrl + C. Ensuite, redémarrez-le en exécutant `npm start` à nouveau.

Et pour tester cela, nous pouvons simplement visiter `http://localhost:3001/api` dans notre navigateur et voir notre message :

![Clip 2](https://reedbarger.nyc3.digitaloceanspaces.com/how-to-create-a-react-app-with-a-node-backend/clip-2.gif)

## Étape 3 : Créer votre frontend React

Après avoir créé notre backend, passons au frontend. 

Ouvrez un autre onglet de terminal et utilisez create-react-app pour créer un nouveau projet React avec le nom `client` :

```bash
npx create-react-app client
```

Après cela, nous aurons une application React avec toutes ses dépendances installées.

La seule modification que nous devons apporter est d'ajouter une propriété appelée `proxy` à notre fichier package.json. 

Cela nous permettra de faire des requêtes à notre serveur Node sans avoir à fournir l'origine sur laquelle il s'exécute (http://localhost:3001) chaque fois que nous faisons une requête réseau :

```bash
// client/package.json

...
"proxy": "http://localhost:3001",
...
```

Ensuite, nous pouvons démarrer notre application React en exécutant son script de démarrage, qui est le même que notre serveur Node. Assurez-vous d'abord de vous placer dans le dossier client nouvellement créé.

Après cela, elle démarrera sur `localhost:3000` :

```bash
cd client
npm start

Compiled successfully!

You can now view client in the browser.

Local:            http://localhost:3000
```

![Clip 3](https://reedbarger.nyc3.digitaloceanspaces.com/how-to-create-a-react-app-with-a-node-backend/clip-3.gif)

## Étape 4 : Faire des requêtes HTTP de React à Node

Maintenant que nous avons une application React fonctionnelle, nous voulons l'utiliser pour interagir avec notre API.

Voyons comment récupérer des données à partir du point de terminaison `/api` que nous avons créé précédemment.

Pour ce faire, nous pouvons nous rendre dans le composant `App.js` dans notre dossier `src` et faire une requête HTTP en utilisant useEffect.

Nous allons faire une simple requête GET en utilisant l'API Fetch à notre backend et ensuite avoir nos données retournées en JSON.

Une fois que nous avons les données retournées, nous allons obtenir la propriété message (pour récupérer notre salut que nous avons envoyé depuis le serveur) et ensuite la mettre dans une variable d'état appelée `data`.

Cela nous permettra d'afficher ce message dans notre page si nous l'avons. Nous utilisons une conditionnelle dans notre JSX pour dire que si nos données ne sont pas encore là, afficher le texte "Loading...".

```js
// client/src/App.js

import React from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  const [data, setData] = React.useState(null);

  React.useEffect(() => {
    fetch("/api")
      .then((res) => res.json())
      .then((data) => setData(data.message));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>{!data ? "Loading..." : data}</p>
      </header>
    </div>
  );
}

export default App;
```

![Clip 5](https://reedbarger.nyc3.digitaloceanspaces.com/how-to-create-a-react-app-with-a-node-backend/clip-4.gif)

## Étape 5 : Déployer votre application sur le web avec Heroku

Enfin, déployons notre application sur le web. 

Tout d'abord, dans notre dossier client, assurez-vous de supprimer le dépôt Git qui est automatiquement initialisé par create-react-app. 

Cela est essentiel pour déployer notre application, car nous allons configurer un dépôt Git dans le dossier racine de notre projet (`react-node-app`), et non dans `client` :

```bash
cd client
rm -rf .git
```

Lorsque nous déployons, notre backend Node et notre frontend React vont être servis sur le même domaine (par exemple, mycoolapp.herokuapp.com).

Nous voyons comment nos requêtes sont gérées par notre API Node, donc nous devons écrire du code qui affichera notre application React lorsqu'elle sera demandée par notre utilisateur (par exemple, lorsque nous allons à la page d'accueil de notre application).

Nous pouvons faire cela en revenant à `server/index.js` en ajoutant le code suivant :

```js
// server/index.js
const path = require('path');
const express = require('express');

...

// Faire en sorte que Node serve les fichiers pour notre application React construite
app.use(express.static(path.resolve(__dirname, '../client/build')));

// Gérer les requêtes GET vers la route /api
app.get("/api", (req, res) => {
  res.json({ message: "Hello from server!" });
});

// Toutes les autres requêtes GET non gérées auparavant retourneront notre application React
app.get('*', (req, res) => {
  res.sendFile(path.resolve(__dirname, '../client/build', 'index.html'));
});
```

Ce code permettra d'abord à Node d'accéder à notre projet React construit en utilisant la fonction `express.static` pour les fichiers statiques.

Et si une requête GET arrive qui n'est pas gérée par notre route `/api`, notre serveur répondra avec notre application React.

**Ce code permet à notre application React et Node d'être déployées ensemble sur le même domaine.**

Ensuite, nous pouvons dire à notre application Node comment faire cela en ajoutant un script `build` à notre fichier package.json du serveur qui construit notre application React pour la production :

```json
// server/package.json

...
"scripts": {
    "start": "node server/index.js",
    "build": "cd client && npm install && npm run build"
  },
...
```

Je recommande également de fournir un champ appelé "engines", où vous voulez spécifier la version de Node que vous utilisez pour construire votre projet. Cela sera utilisé pour le déploiement.

Vous pouvez obtenir votre version de Node en exécutant `node -v` et vous pouvez mettre le résultat dans "engines" (par exemple, 14.15.4) :

```json
// server/package.json

"engines": {
  "node": "votre-version-node"
}
```

Après cela, nous sommes prêts à déployer en utilisant Heroku, alors assurez-vous d'avoir un compte sur [Heroku.com](https://heroku.com).

Une fois que vous êtes connecté et que vous regardez votre tableau de bord, vous sélectionnerez New > Create New App et fournirez un nom d'application unique.

Après cela, vous voudrez installer le CLI Heroku sur votre ordinateur afin de pouvoir déployer votre application chaque fois que vous apportez des modifications en utilisant Git. Nous pouvons installer le CLI en exécutant :

```bash
sudo npm i -g heroku
```

Une fois cela installé, vous vous connecterez à Heroku via le CLI en utilisant la commande `heroku login` :

```bash
heroku login

Press any key to login to Heroku
```

Une fois que vous êtes connecté, il suffit de suivre les instructions de déploiement pour notre application créée dans l'onglet "Deploy".

Les quatre commandes suivantes initialiseront un nouveau dépôt Git pour notre projet, ajouteront nos fichiers, les committeront et ajouteront un dépôt distant Git pour Heroku.

```
git init
heroku git:remote -a inserez-votre-nom-app-ici
git add .
git commit -am "Déployer l'application sur Heroku"
```

Ensuite, la toute dernière étape consiste à publier notre application en poussant le dépôt distant Heroku que nous venons d'ajouter en utilisant :

```bash
git push heroku master
```

Félicitations ! Notre application full-stack React et Node est en ligne ! 🎉

![Clip 5](https://reedbarger.nyc3.digitaloceanspaces.com/how-to-create-a-react-app-with-a-node-backend/clip-5.gif)

Lorsque vous souhaitez apporter des modifications à votre application à l'avenir (et les déployer), vous devez simplement utiliser Git pour ajouter vos fichiers, les committer et ensuite pousser vers notre dépôt distant Heroku :

```bash
git add .
git commit -m "mon message de commit"
git push heroku master
```

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*