---
title: Comment masquer les clés API dans les applications frontend en utilisant les
  fonctions Netlify
subtitle: ''
author: Franklin Ohaegbulam
co_authors: []
series: null
date: '2023-02-07T23:46:43.000Z'
originalURL: https://freecodecamp.org/news/hide-api-keys-in-frontend-apps-using-netlify-functions
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/FCC-hide-API-keys-1.jpg
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: lambda
  slug: lambda
- name: Netlify
  slug: netlify
- name: netlify-functions
  slug: netlify-functions
- name: serverless
  slug: serverless
seo_title: Comment masquer les clés API dans les applications frontend en utilisant
  les fonctions Netlify
seo_desc: 'Netlify is a popular web development platform that makes it easier to build,
  deploy, and manage websites.

  You can use Netlify to host websites, and it helps you update and release new changes.
  It also provides additional features such as security, us...'
---

Netlify est une plateforme populaire de développement web qui facilite la création, le déploiement et la gestion de sites web.

Vous pouvez utiliser Netlify pour héberger des sites web, et il vous aide à mettre à jour et à publier de nouvelles modifications. Il offre également des fonctionnalités supplémentaires telles que la sécurité, les services d'authentification et d'autorisation des utilisateurs, et bien plus encore.

Ce guide se concentre sur la manière de configurer une fonction serverless Netlify pour masquer les clés d'Application Programming Interface (API) dans une application côté client.

Pour cette leçon, vous allez créer une application web de moteur de recherche de photos libres de droits, la déployer sur Netlify, et faire un appel API à l'API Pixabay en utilisant les fonctions serverless de Netlify.

Ce processus est le même pour les applications frontend construites avec ReactJS, NextJS, VueJS, Angular, ou d'autres frameworks JavaScript.

### Prérequis

Pour suivre ce tutoriel, vous devez avoir les éléments suivants :

* Un compte Netlify (vous pouvez vous inscrire [ici](http://netlify.com))

* Une compréhension de base des API RESTful, des fonctions Lambda, et des concepts async/await.

L'application de démonstration finale se trouve dans la branche principale sur GitHub : `https://netlify-func-demo.netlify.app`

## Qu'est-ce qu'une fonction Netlify ?

Les fonctions Netlify sont des fonctions serverless ou lambda fournies par Netlify. Vous les utilisez pour déployer du code côté serveur ou une logique backend sans avoir besoin d'un serveur dédié.

Le but de cette fonction Netlify est de gérer le code piloté par événements serverless et d'envoyer des requêtes HTTP qui retournent une réponse JSON.

> "Les fonctions serverless, marquées comme Netlify Functions lorsqu'elles s'exécutent sur Netlify, sont un moyen de déployer du code côté serveur en tant que points de terminaison API" - Documentation Netlify

Elle accède de manière sécurisée aux variables d'environnement en arrière-plan via la fonction lambda d'Amazon Web Services (AWS).

Les informations d'identification secrètes telles que les jetons d'accès ou les clés API, masquées uniquement à l'aide de variables d'environnement, sont moins sécurisées. Cela est dû au fait qu'elles peuvent être facilement récupérées depuis les outils de développement via la requête fetch de l'API dans le navigateur.

Les clés API, si elles sont détournées, peuvent être mal utilisées par des acteurs malveillants, ce qui pourrait affecter le seuil de construction de votre application ou vous coûter plus cher si c'est un service API payant.

D'autres fonctions serverless utilisées pour exécuter du code sans avoir à gérer des serveurs incluent les fonctions Lambda AWS, les fonctions Azure et les fonctions Google Cloud.

## Comment configurer une application côté client

### Comment cloner l'application de démonstration

Pour commencer avec ce tutoriel, vous pouvez cloner l'application **moteur de recherche de photos libres de droits** [dépôt GitHub](https://github.com/frankiefab100/netlify-serverless-functions-demo/tree/main). Voir l'aperçu en direct sur Netlify à l'adresse [https://netlify-func-demo.netlify.app](https://netlify-func-demo.netlify.app).

La première étape consiste à cloner le dépôt :

```bash
git clone https://github.com/frankiefab100/netlify-serverless-functions-demo.git
```

Ensuite, changez pour le répertoire **netlify-serverless-functions-demo**.

```bash
 cd netlify-serverless-functions-demo
```

Ensuite, vous devrez installer les dépendances.

```bash
npm install
#OU 
yarn add
```

Maintenant, lancez le serveur de développement. Exécutez la commande suivante pour démarrer l'application sur le serveur :

```bash
netlify dev
```

L'application sera prête sur `https://localhost:8888`.

Alternativement, vous pouvez sauter les étapes ci-dessus si vous souhaitez suivre en construisant l'application à partir de zéro. Dans l'étape suivante, vous allez construire une application JavaScript de moteur de recherche de photos libres de droits.

### Comment construire l'application de démonstration en utilisant JavaScript

La première étape consiste à configurer une application frontend. Ouvrez votre éditeur de code préféré, tel que VS Code.

Ensuite, créez un répertoire **dist** et à l'intérieur créez un fichier **index.html**. Remplissez-le avec le code suivant :

```xml
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>Moteur de recherche de photos libres de droits</title>
  </head>
  <body>
    <div class="container">
      <header>
        <h1>Rechercher des photos libres de droits</h1>
        <div class="search-section">
          <input
            type="text"
            name="search"
            class="search"
            placeholder="Entrez un mot-clé"
          />
          <input
            id="searchBtn"
            class="search-btn"
            type="submit"
            value="Rechercher"
          />
        </div>
      </header>

      <div class="photo-wrapper">
        <img src="" alt="" class="photo" />
      </div>
    </div>

    <script src="./script.js" type="module"></script>
  </body>
</html>
```

Dans le même répertoire `dist`, ajoutez le style suivant à style.css :

```css
/* dist/style.css */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  color: #222;
  font-family: "Roboto", sans-serif;
  font-size: 1rem;
  margin: 0 auto;
  width: 100vw;
  height: 100vh;
}

.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  min-height: 100vh;
  min-width: 100vw;
  width: 100%;
  height: 100%;
}

h1 {
  padding-bottom: 20px;
}

.search-section {
  display: inline;
  text-align: center;
  min-width: 310px;
}

.search,
.search-btn {
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  padding: 15px;
  height: 50px;
}

.search {
  background-color: #d1f3bf;
  color: #222;
  min-width: 225px;
}

.search-btn {
  background-color: #04ab04;
  color: #f6f6f6;
  cursor: pointer;
  margin-left: 5px;
  min-width: 80px;
  transition: all 0.3s ease-in-out;
}

.search-btn:hover {
  background-color: #2dc22d;
}

.photo-wrapper {
  display: flex;
  gap: 15px;
  margin: 30px;
}

.photo-wrapper img {
  width: 200px;
}
```

## Inscription à un compte gratuit sur Pixabay

La première étape pour utiliser l'[API Pixabay](https://pixabay.com/api/docs/) est de s'inscrire à un compte avec votre email.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Pixabay-API-Documentation.png align="left")

*Section de la clé API Pixabay*

Comme montré dans l'image ci-dessus, votre clé API peut être trouvée sous la section **paramètres** dans le [site de documentation de l'API Pixabay](https://pixabay.com/api/docs/).

### Créer une variable d'environnement

Les variables d'environnement (communément appelées "env") sont des combinaisons de paires clé/valeur qui peuvent affecter le comportement et les processus d'un système d'exploitation ou d'une application.

L'utilisation de variables d'environnement est recommandée pour configurer les services tiers et leurs informations d'identification pendant le développement.

### Installer dotenv

Une fois que vous avez terminé la création de compte sur Pixabay, ouvrez votre terminal et installez **dotenv** en tant que package. Cela permettra à votre application de lire les variables d'environnement enregistrées dans le fichier **.env**.

```javascript
npm install dotenv
#OU
yarn add -D dotenv
```

Dans l'étape suivante, vous enregistrerez la clé API dans un fichier **.env**.

### Créer le fichier .env

Dans le répertoire racine de votre application, créez un fichier **.env** et stockez les clés API copiées depuis votre profil Pixabay.

```plaintext
PIXABAY_API_KEY=123456-7890
```

Où `PIXABAY_API_KEY=123456-7890` représente la valeur de la clé API.

**Note :** Remplacez cette paire clé/valeur par la valeur appropriée.

### Créer un fichier .gitignore

Pour éviter de commettre des fichiers et des valeurs sensibles tels que `node_modules` et `clés secrètes` dans un dépôt public, créez un fichier **.gitignore** dans le même répertoire racine du projet et ajoutez-y ce qui suit :

```plaintext
node_modules
.env
.netlify
```

Le dossier **.netlify** qui contient les fonctions serverless compilées ainsi que les autres fichiers listés seront exclus lorsque le projet sera poussé vers GitHub ou tout autre système de contrôle de version.

### Créer une fonction de requête get

Maintenant, vous devez ajouter la logique de requête fetch dans le **script.js**. Vous ajusterez la logique de l'API plus tard en utilisant les fonctions Netlify.

```javascript
/* dist/script.js */
const dotenv = require("dotenv").config();

const searchbar = document.querySelector(".search");
const submitBtn = document.querySelector(".search-btn");
const photoWrapper = document.querySelector(".photo-wrapper");

submitBtn.addEventListener("click", () => {
  getPhoto(searchbar.value);
  searchbar.value = "";
});

window.addEventListener("keydown", (e) => {
  if (e.keyCode === 13) {
    getPhoto(searchbar.value);
    searchbar.value = "";
  }
});

async function getPhoto(keyword) {
  const apiKey = PIXABAY_API_KEY;
  let apiURL = `https://pixabay.com/api/?key=${apiKey}&q=${keyword}&image_type=photo&safesearch=true&per_page=3`;

  try {
    const response = await fetch(apiURL, {
      method: "GET",
      headers: { accept: "application/json" },
    });
    const data = await response.json();

    let imageURL = data.hits;

    imageURL.forEach((result) => {
      let imageElement = document.createElement("img");
      imageElement.setAttribute("src", `${result.webformatURL}`);
      photoWrapper.appendChild(imageElement);
    });
  } catch (error) {
    alert(error);
  }
}
```

**Note :** Comme mentionné précédemment, si le code de cette application est publié sur GitHub, la clé API sera toujours accessible depuis le côté client dans un navigateur, bien que le fichier `.env` contenant la clé secrète ait été exclu.

Pour illustrer cela, sélectionnez la branche [`testing`](https://github.com/frankiefab100/netlify-serverless-functions-demo/tree/testing) de ce dépôt d'application. L'[aperçu du site en direct](https://testing--netlify-func-demo.netlify.app/) affichera les erreurs de référence suivantes dans la console de votre navigateur :

```bash
Uncaught ReferenceError: require is not defined
Uncaught ReferenceError: require is not defined at getPhotos
Uncaught ReferenceError: process is not defined at getPhotos
```

Cela est dû au fait qu'il n'y a aucun moyen de référencer les variables d'environnement spécifiées dans le fichier **.env**, puisqu'elles n'ont pas été commises dans le dépôt public sur GitHub.

Dans l'étape suivante, sélectionnez et clonez la branche `[testing](https://github.com/frankiefab100/netlify-serverless-functions-demo/tree/testing)` sur votre machine locale avec les commandes suivantes :

```bash
git clone https://github.com/frankiefab100/netlify-serverless-functions-demo.git
cd netlify-serveless-functions-demo
npm install
netlify dev
```

L'application devrait se lancer sur votre navigateur via `localhost:8888`.

Maintenant, allez dans les **outils de développement**, faites un clic droit et sélectionnez **Inspecter**. Alternativement, appuyez sur la touche **F12**. Ensuite, naviguez vers l'onglet **Network** et cliquez sur l'URL de la requête `getPhotos.js`.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot--124----Copy.png align="left")

*Clé API affichée dans l'onglet Network des outils de développement*

Vous devriez voir la clé API exposée publiquement dans la section **Headers** de l'onglet **Network** et retournée en tant que données de réponse dans votre navigateur.

Cela pose un problème de sécurité puisque l'onglet Network dans les outils de développement est généralement responsable de l'affichage d'informations telles que l'URL de la requête, le statut de la réponse et les données de réponse.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot--127----Copy.png align="left")

*Clé API retournée en tant que données de réponse et exposée dans l'URL de la requête*

Dans la section suivante, vous trouverez un moyen de sécuriser la clé API en utilisant les fonctions Netlify.

## Comment commencer avec les fonctions Netlify

Tout d'abord, vous devrez aller dans votre terminal et installer **Netlify CLI** et **Lambda** en tant que dépendances de développement. Vous pouvez le faire en exécutant cette commande :

```bash
npm install -g netlify-cli netlify-lambda
#OU 
yarn add -D netlify-cli netlify-lambda --save-dev
```

### Ajouter des commandes de build et de développement personnalisées dans package.json

Ces commandes construisent et démarrent l'application sur le serveur et lancent également l'application dans votre navigateur web. Voici un exemple de la manière dont vous pourriez ajouter ces commandes de script dans le fichier **package.json** :

```bash
"scripts": {
   "build": "npm run-script",
   "dev": "netlify dev"
 }
```

### Installer Axios

Vous utiliserez la méthode `axios.get`, car c'est une fonction node contrairement à la méthode `fetch` qui est destinée à l'exécution dans le navigateur.

Pour installer Axios, ouvrez votre terminal et entrez la commande :

```bash
npm install axios
#OU
yarn add -D axios
```

Dans ce cas, vous travaillez avec une application JavaScript vanilla, vous devez donc importer Axios dans le fichier `getPhotos.js` comme suit :

```javascript
const axios = require("axios");
```

Pour les bibliothèques JavaScript, comme React, importez-le comme suit :

```javascript
import axios from "axios";
```

### Créer une fonction serverless

À la racine du projet, créez un dossier nommé `netlify`, et à l'intérieur créez un autre dossier `functions`. Dans ce répertoire `functions`, créez un fichier nommé `getPhotos.js`.

Vous allez créer une fonction serverless dans `getPhotos`. Cela masquera complètement les clés API lors de la récupération d'images depuis l'[API Pixabay](https://pixabay.com/api).

```javascript
//netlify/functions/getPhotos.js 
require("dotenv").config();

const axios = require("axios");

exports.handler = async (event, context) => {
  try {
    const { keyword } = event.queryStringParameters;
    let response = await axios.get(
      `https://pixabay.com/api/?key=${process.env.PIXABAY_API_KEY}&q=${keyword}&image_type=photo&safesearch=true&per_page=3`,
      {
        headers: { Accept: "application/json", "Accept-Encoding": "identity" },
        params: { trophies: true },
      }
    );

    let imageURL = response.data.hits;

    return {
      statusCode: 200,
      body: JSON.stringify({ imageURL }),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error }),
    };
  }
};
```

Ici, `process.env.PIXABAY_API_KEY` fait référence à la configuration de l'environnement de la clé API spécifiée dans le fichier `.env` pour le mode développement.

Le paramètre `keyword` accepte une chaîne accessible dans la propriété `queryStringParameters` et retourne des données de réponse stockées dans la variable `imageURL`. Cela sera transmis à `script.js` en tant que réponse de requête (nous en discuterons plus tard).

Si la requête GET est réussie, elle retourne une réponse avec un `statusCode` 200 et la réponse correspondante sous forme d'objet JSON. En cas d'erreurs, nous recevrons une alerte avec le message d'erreur et le code de statut.

En raison des changements de version, Axios peut retourner Buffer en tant que réponse dans votre fenêtre de terminal, ce qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/netlify-data.JPG align="left")

*Réponse Buffer d'Axios dans le Terminal*

Pour éviter cela, vous devez attacher ce qui suit à la requête GET :

```javascript
 let response = await axios.get(
      `https://pixabay.com/api/?key=${process.env.PIXABAY_API_KEY}&q=${keyword}&image_type=photo&safesearch=true&per_page=3`,
      {
        headers: { Accept: "application/json", "Accept-Encoding": "identity" },
        params: { trophies: true },
      }
    );
```

### Créer un fichier de configuration Netlify

Dans le répertoire racine du projet, créez un fichier `netlify.toml`. Ce fichier spécifie comment Netlify construit et déploie votre application.

Maintenant, ajoutez les configurations de build suivantes dans `netlify.toml` :

```bash
[build]
  command = "npm run build"
  functions = "netlify/functions"
  publish = "dist"
```

**Note :**

* `command = "npm run build"` déclenche le CLI Netlify pour construire l'application à partir des fonctions.

* `functions = "netlify/functions"` indique que les fonctions `getPhotos` existent dans le répertoire `netlify/functions`.

* `publish = "dist"` identifie `dist` comme le répertoire à partir duquel le fichier sera servi.

### Mettre à jour le fichier script.js avec l'URL de requête des fonctions Netlify

Ensuite, mettez à jour l'`apiURL` de ceci :

```javascript
let apiURL = `https://pixabay.com/api/?key=${apiKey}&q=${keyword}&image_type=photo&safesearch=true&per_page=3`;
```

vers le point de terminaison de la requête HTTP des fonctions :

```javascript
  let apiURL = `/.netlify/functions/getPhotos?keyword=${keyword}`;
```

Cette fonction serverless sera interrogée côté client de votre application via le point de terminaison : `/.netlify/functions/getPhotos`. Une fois une requête fetch envoyée, la fonction `getphotos` sera invoquée et accessible dans le `script.js`.

La réponse `imageURL` des fonctions Netlify `getPhotos` sera transmise et les données accessibles en tant que valeur du paramètre `keyword` dans la chaîne de requête de la fonction. Elle sera parcourue pour retourner trois images de l'API Pixabay vers le côté client.

Le fichier **script.js** devrait ressembler à ceci :

```javascript
/* dist/script.js */
const searchbar = document.querySelector(".search");
const submitBtn = document.querySelector(".search-btn");
const photoWrapper = document.querySelector(".photo-wrapper");

submitBtn.addEventListener("click", () => {
  getPhoto(searchbar.value);
  searchbar.value = "";
  photoWrapper.innerHTML = "";
});

window.addEventListener("keydown", (e) => {
  if (e.keyCode === 13) {
    getPhoto(searchbar.value);
    searchbar.value = "";
    photoWrapper.innerHTML = "";
  }
});

async function getPhoto(keyword) {
  let apiURL = `/.netlify/functions/getPhotos?keyword=${keyword}`;

  try {
    const response = await fetch(apiURL, {
      method: "GET",
      headers: { accept: "application/json" },
    });
    const data = await response.json();

    for (let i = 0; i < data.imageURL.length; i++) {
      let imageElement = document.createElement("img");
      imageElement.setAttribute("src", `${data.imageURL[i].webformatURL}`);
      photoWrapper.appendChild(imageElement);
    }
  } catch (error) {
    alert(error);
  }
}
```

**Note :** À partir du code ci-dessus, votre variable d'environnement est sécurisée puisqu'elle est accessible depuis la fonction serverless.

### Exécuter le serveur de développement

Maintenant, exécutez votre application en lançant la commande :

```bash
netlify dev
```

Cela chargera la fonction **getPhotos** via `https://localhost:8888/.netlify/functions/getPhotos`.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/netlify-dev-terminal.JPG align="left")

*Sortie du terminal de build netlify*

Ensuite, démarrez le serveur de développement et lancez l'application dans votre navigateur web par défaut sur `localhost:8888`.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/netlify-success2.JPG align="left")

*Fonction netlify prête sur https://localhost:8888*

À ce stade, la fonction Netlify est entièrement configurée, et vous pouvez maintenant procéder à l'envoi de requêtes HTTP `GET`.

### Comment envoyer des requêtes Fetch

Maintenant que vous avez déjà l'application web servie, allez-y et envoyez une requête fetch. Entrez du texte dans le champ de recherche et appuyez sur **Entrée** ou cliquez sur le bouton pour récupérer des images de l'API Pixabay.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Stock-Photos-Search-Engine--1-.png align="left")

*Images de fleurs récupérées depuis l'API Pixabay*

Pour plus d'informations sur l'API Pixabay, consultez la [documentation Pixabay](https://pixabay.com/api/docs).

La commande précédente enverra une requête à la fonction serverless et retournera six réponses. Voici à quoi ressemble la réponse dans vos fenêtres de terminal :

> Requête de ::1: GET /.netlify/functions/getPhotos?keyword=flower  
> Réponse avec le statut 200 en 4895 ms.

Vous pouvez également utiliser les **outils de développement** via l'onglet **Network** pour valider la requête.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot--118----Copy.png align="left")

*Données de réponse de l'API de la fonction serverless*

La requête fetch retourne l'URL de notre application, la fonction **getPhotos** de Netlify, script.js et les images de Pixabay.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot--120-.png align="left")

*Réponse de la fonction Netlify fetch depuis la section d'en-tête de l'onglet Network dans le navigateur*

## Comment héberger l'application sur le dépôt distant

Maintenant, vous devriez pousser votre projet vers le contrôle de version GitHub.

```javascript
git add .
git commit -m"initial commit"
git push origin -u main
```

## Comment déployer l'application et la fonction serverless sur Netlify

Une fois que vous avez publié le projet sur GitHub, connectez-vous à [Netlify](https://app.netlify.com) et connectez votre compte GitHub en accordant l'autorisation.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot--130-.png align="left")

*Importer le projet pour le déploiement sur Netlify*

Comme montré dans l'image ci-dessus, cliquez sur `Add A New Project` puis recherchez le dépôt de l'application dans la liste. Ensuite, cliquez sur `Build Your Site`. Cela prendra quelques minutes pour se terminer.

Vous venez de déployer l'application depuis l'interface utilisateur de Netlify. Votre application est maintenant prête à l'adresse : `https://netlify-func-demo.netlify.app`.

L'URL de la requête fetch devrait ressembler à ceci : `https://netlify-func-demo.netlify.app/.netlify/functions/getPhotos`.

## Optionnel - Comment configurer l'application Netlify depuis le tableau de bord

Alternativement, vous pouvez configurer la commande Netlify depuis le tableau de bord Netlify. Si ces paramètres sont déjà spécifiés dans **netlify.toml**, ils remplaceront toute configuration correspondante.

Tout d'abord, sélectionnez les paramètres du site du répertoire du projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Site-overview-netlify-func-demo1.png align="left")

*Paramètres du site pour le répertoire du projet sur Netlify*

### Définir la commande de build et le répertoire de publication

Accédez à `Site settings` > `Deploy` > `Build & deploy` et modifiez les commandes suivantes puis sauvegardez les modifications :

* Commande de build : **npm run build**

* Répertoire de publication : **dist**

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot--132-.png align="left")

*Section Build and deploy sur Netlify*

### Définir le répertoire des fonctions

Par défaut, Netlify utilise `netlify/functions` comme répertoire pour trouver les fonctions à déployer. Dans notre cas, notre fonction serverless `getPhotos` peut être trouvée dans le répertoire `netlify/functions`.

Maintenant, nous allons définir un répertoire de fonctions personnalisé afin que Netlify puisse trouver vos fonctions compilées. Allez dans `Site settings` > `Functions` et entrez le chemin du répertoire où les fonctions sont stockées dans votre dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot--131-.png align="left")

*Section du répertoire des fonctions sur Netlify*

### Comment définir les variables d'environnement pour la production

Dans le tableau de bord Netlify, cliquez sur `Site settings` > `Build & deploy` > `Environment` > `Environment variables` puis configurez les paires CLÉ/VALEUR comme suit :

```plaintext
PIXABAY_API_KEY=votre-clé-api-ici
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot--133-.png align="left")

*Section des variables d'environnement sur Netlify*

Cliquez sur Enregistrer, puis redéployez votre application afin que les modifications soient ajoutées.

Pour redéployer l'application sur Netlify, accédez à `Deploys` > `Trigger deploy`. Ensuite, sélectionnez `Clear cache and redeploy site`.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot--134-.png align="left")

*Onglet de redéploiement déclenché sur Netlify*

**Note :** Le nom de la variable d'environnement (PIXABAY\_API\_KEY) doit correspondre à celui mentionné dans le code de la fonction `getPhotos`.

Pour une application React, préfixez la variable d'environnement de l'API avec le préfixe `REACT_APP` afin qu'elles puissent être lues depuis le fichier `.env`.

```plaintext
 REACT_APP_PIXABAY_API_KEY=votre-clé-api-ici
```

## Comment initialiser la fonction serverless à l'application distante

Pour connecter votre répertoire de projet à l'application web existante déployée sur Netlify, connectez-vous à votre compte Netlify depuis le terminal :

```bash
netlify login
```

Ensuite, initialisez l'application sur Netlify en exécutant la commande dans votre terminal :

```bash
netlify init
```

Votre application est maintenant configurée pour un déploiement continu via Netlify.

## Comment construire la fonction serverless Netlify

Vous devez lier votre application à l'ID du site sur Netlify avant d'exécuter la commande de build sur votre terminal. Pour connecter votre dossier de projet local à son ID de site sur Netlify, entrez la commande dans votre terminal :

```bash
netlify link
```

Cela vous invitera à lier le dossier à un site via l'une des options suivantes :

* Rechercher par nom de site complet ou partiel

* Choisir parmi une liste de vos sites récemment mis à jour

* Entrer un ID de site

Une fois que vous avez sélectionné votre option préférée, cela connectera le dossier du projet au site hébergé sur Netlify. Cela vous permet d'exécuter des commandes **Netlify CLI** et également de déployer automatiquement le dépôt du projet dès qu'il y a des changements dans le code.

Dans l'étape suivante, vous allez construire une fonction serverless tout en l'exécutant sur le serveur. Pour activer la commande de build définie dans le fichier `netlify.toml`, exécutez la commande suivante :

```bash
netlify build
```

Cela exécute la commande `npm run-script` sous le capot comme spécifié dans le `package.json`. Maintenant, votre fonction serverless dans le répertoire `netlify/functions` est emballée et regroupée avec succès !

## Comment tester l'application

Pour tester et confirmer que la fonction Netlify fonctionne correctement, exécutez cette commande sur votre terminal :

```bash
netlify functions:serve
```

Cela injecte vos variables d'environnement de projet depuis le fichier **.env** et exécute la fonction serverless.

### Comment confirmer la sécurité des clés API

Pour inspecter votre application et confirmer que les clés API sont masquées du public, suivez les étapes ci-dessous :

Cliquez sur l'URL de votre application hébergée, et accédez aux **outils de développement** en appuyant sur la touche **F12** ou en faisant un clic droit et en sélectionnant **Inspecter**. Accédez à l'onglet **Network**, où vous devriez voir les données récupérées de l'API Pixabay.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot--128-.png align="left")

*Clé API masquée du public et des parties non autorisées après inspection via les outils de développement*

Maintenant, vous avez confirmé que vous avez configuré avec succès une fonction serverless et l'avez déployée sur Netlify.

## **Conclusion**

Ce tutoriel a introduit les fonctions serverless, JavaScript asynchrone et les concepts d'API RESTful.

Espérons que vous savez maintenant comment créer une fonction serverless/lambda et sécuriser toute valeur sensible telle que les clés API dans votre application JavaScript frontend.

Si vous êtes bloqué avec quelque chose, vous pouvez accéder au code source complet dans ce [dépôt GitHub](https://github.com/frankiefab100/netlify-serverless-functions-demo/tree/main).

Merci d'avoir lu ! Si vous avez des questions, n'hésitez pas à me contacter via [Twitter](https://twitter.com/frankiefab100).

## **Liens pertinents**

* [Fonctions Netlify](https://docs.netlify.com/functions/overview/)

* [Introduction aux fonctions serverless par Netlify](https://www.netlify.com/blog/intro-to-serverless-functions/)

* [Exemple de fonctions Netlify](https://github.com/sdras/netlify-functions-example)