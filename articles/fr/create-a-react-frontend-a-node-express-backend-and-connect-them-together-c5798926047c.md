---
title: Comment créer un frontend React et un backend Node/Express et les connecter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-07T09:46:26.000Z'
originalURL: https://freecodecamp.org/news/create-a-react-frontend-a-node-express-backend-and-connect-them-together-c5798926047c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*IlQX1QCLarsRIFl7
tags:
- name: Express
  slug: express
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment créer un frontend React et un backend Node/Express et les connecter
seo_desc: 'By João Henrique

  In this article, I’ll walk you through the process of creating a simple React app
  and connecting it to a simple Node/Express API that we will also be creating.

  I won''t go into much detail about how to work with any of the technologie...'
---

Par João Henrique

Dans cet article, je vais vous guider à travers le processus de création d'une application React simple et de sa connexion à une API Node/Express simple que nous allons également créer.

Je ne vais pas entrer dans les détails sur la façon de travailler avec les technologies mentionnées dans ce tutoriel, mais je vais laisser des liens au cas où vous voudriez en savoir plus.

Vous pouvez trouver tout le code dans [**ce dépôt**](https://github.com/Joao-Henrique/React_Express_App_Medium_Tutorial) que j'ai créé pour le tutoriel.

L'objectif ici est de vous donner un guide pratique sur la façon de configurer et de connecter le **client frontend** et l'**API backend**.

Avant de mettre les mains dans le cambouis, assurez-vous d'avoir [Node.js](https://nodejs.org/en/) installé sur votre machine.

#### Créer le répertoire principal du projet

Dans votre terminal, naviguez vers un répertoire où vous souhaitez enregistrer votre projet. Créez un nouveau répertoire pour votre projet et naviguez dedans :

```bash
mkdir mon_projet_genial
cd mon_projet_genial
```

#### Créer une application [React](https://reactjs.org/)

Ce processus est vraiment simple.

J'utiliserai [create-react-app](https://github.com/facebook/create-react-app) de Facebook pour... vous l'avez deviné, créer facilement une application React nommée **client** :

```bash
npx create-react-app client
cd client
npm start
```

_Voyons ce que j'ai fait :_

1. _Utilisé [npx](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b) de npm pour créer une application React et l'ai nommée client._
2. _cd (changer de répertoire) dans le répertoire client._
3. _Démarré l'application._

Dans votre navigateur, accédez à [http://localhost:3000/](http://localhost:3000/).

Si tout est correct, vous verrez la page de bienvenue de React. Félicitations ! Cela signifie que vous avez maintenant une application [**React**](https://reactjs.org/) de base en cours d'exécution sur votre machine locale. Facile, non ?

Pour arrêter votre application React, appuyez simplement sur `**Ctrl + c**` dans votre terminal.

#### Créer une application [Express](https://expressjs.com/)

D'accord, cela sera aussi simple que l'exemple précédent. N'oubliez pas de naviguer vers le dossier principal de votre projet.

J'utiliserai le [Générateur d'applications Express](https://expressjs.com/en/starter/generator.html) pour créer rapidement un squelette d'application et le nommer **api** :

```bash
npx express-generator api
cd api
npm install
npm start
```

_Voyons ce que j'ai fait :_

1. _Utilisé npx de npm pour installer express-generator globalement._
2. _Utilisé express-generator pour créer une application express et l'ai nommée api._
3. _cd dans le répertoire API._
4. Installé toutes les dépendances.
5. Démarré l'application.

Dans votre navigateur, accédez à [http://localhost:3000/](http://localhost:3000/).

Si tout est correct, vous verrez la page de bienvenue d'Express. Félicitations ! Cela signifie que vous avez maintenant une application [**Express**](https://expressjs.com/) de base en cours d'exécution sur votre machine locale. Facile, non ?

Pour arrêter votre application React, appuyez simplement sur `**Ctrl + c**` dans votre terminal.

#### Configurer une nouvelle [route](https://expressjs.com/en/guide/routing.html) dans l'API Express

D'accord, mettons les mains dans le cambouis. Il est temps d'ouvrir votre éditeur de code préféré _(j'utilise [VS Code](https://code.visualstudio.com/))_ et de naviguer vers votre dossier de projet.

_Si vous avez nommé l'application React **client** et l'application Express **api**, vous trouverez deux dossiers principaux : **client** et **api**._

1. Dans le répertoire **API**, allez dans **bin/www** et changez le numéro de port à la ligne 15 de 3000 à 9000. Nous allons exécuter les deux applications en même temps plus tard, donc cela évitera les problèmes. Le résultat devrait être quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/m7e3LsFolz6988HgYjgdDuP3DPY1Ix3F8u5u)
_mon_projet_genial/api/bin/www_

2. Dans **api/routes**, créez un fichier **testAPI.js** et collez ce code :

```js
var express = require("express");
var router = express.Router();

router.get("/", function(req, res, next) {
    res.send("API fonctionne correctement");
});

module.exports = router;
```

3. Dans le fichier **api/app.js**, insérez une nouvelle route à la ligne 24 :

```js
app.use("/testAPI", testAPIRouter);
```

4. D'accord, vous "dites" à express d'utiliser cette route, mais vous devez encore l'importer. Faisons cela à la ligne 9 :

```js
var testAPIRouter = require("./routes/testAPI");
```

Les seules modifications sont aux lignes 9 et 25. Cela devrait ressembler à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/hG-IcH7kyM8nj1VO43Mgo1nZGI0hsVhvAfFi)
_mon_projet_genial/api/app.js_

5. Félicitations ! Vous avez créé une nouvelle [route](https://expressjs.com/en/guide/routing.html).

Si vous démarrez votre application API (dans votre terminal, naviguez vers le répertoire API et tapez "**npm start**"), et allez à [http://localhost:9000/testAPI](http://localhost:9000/testAPI) dans votre navigateur, vous verrez le message : **_API fonctionne correctement._**

#### Connecter le client React à l'API Express

1. Dans votre éditeur de code, travaillons dans le répertoire **client**. Ouvrez le fichier **app.js** situé dans **mon_projet_genial/client/app.js**.
2. Ici, j'utiliserai l'[**API Fetch**](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) pour récupérer des données de l'**API**. Collez simplement ce code après la déclaration de la classe et avant la méthode render :

```jsx
constructor(props) {
    super(props);
    this.state = { apiResponse: "" };
}

callAPI() {
    fetch("http://localhost:9000/testAPI")
        .then(res => res.text())
        .then(res => this.setState({ apiResponse: res }));
}

componentWillMount() {
    this.callAPI();
}
```

3. À l'intérieur de la méthode render, vous trouverez une balise **<**;p>. Changeons-la pour qu'elle affiche la **apiResponse** :

```jsx
<p className="App-intro">;{this.state.apiResponse}</p>
```

À la fin, ce fichier devrait ressembler à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/dswag4EEuA3vcVmZ9cs7rxJwOayb-SW6HiI8)

Je sais !!! C'était un peu trop. Le copier-coller est votre ami, mais vous devez comprendre ce que vous faites. Voyons ce que j'ai fait ici :

1. _Aux lignes 6 à 9, nous avons inséré un constructeur, qui initialise l'état par défaut._
2. _Aux lignes 11 à 16, nous avons inséré la méthode **callAPI()** qui récupérera les données de l'API et stockera la réponse dans **this.state.apiResponse.**_
3. _Aux lignes 18 à 20, nous avons inséré une méthode de cycle de vie React appelée **componentDidMount(),** qui exécutera la méthode **callAPI()** après le montage du composant._
4. Enfin, à la ligne 29, j'ai utilisé la balise **<**;p> pour afficher un paragraphe sur notre page client, avec le texte que nous avons récupéré de l'API.

#### Qu'est-ce que c'est que ça !! [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) ?

Oh oui, mon ami ! Nous avons presque terminé. Mais si nous démarrons nos deux applications (client et API) et naviguons vers [http://localhost:3000/](http://localhost:3000/), vous ne trouverez toujours pas le résultat attendu affiché sur la page. Si vous ouvrez les outils de développement de Chrome, vous trouverez pourquoi. Dans la console, vous verrez cette erreur :

> Échec du chargement de [http://localhost:9000/testAPI](http://localhost:9000/testAPI) : Aucun en-tête 'Access-Control-Allow-Origin' n'est présent sur la ressource demandée. L'origine '[http://localhost:3000'](http://localhost:3000') n'est donc pas autorisée à accéder. Si une réponse opaque répond à vos besoins, définissez le mode de la requête sur 'no-cors' pour récupérer la ressource avec CORS désactivé.

C'est simple à résoudre. Nous devons simplement ajouter CORS à notre API pour permettre les requêtes cross-origin. Faisons cela. Vous devriez [vérifier ici](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) pour en savoir plus sur [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

1. Dans votre terminal, naviguez vers le répertoire API et installez le package **CORS** :

```bash
npm install --save cors
```

2. Dans votre éditeur de code, allez dans le répertoire API et ouvrez le fichier **mon_projet_genial/api/app.js**.

3. À la ligne 6, importez **CORS** :

```js
var cors = require("cors");
```

4. Maintenant, à la ligne 18, "dites" à express d'utiliser **CORS** :

```js
app.use(cors());
```

Le fichier **app.js** de l'API devrait ressembler à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/NOuexIhM99Tn-eKYJ0wJjRJUCbIwww8Lyr61)
_mon_projet_genial/api/app.js_

#### Excellent travail. C'est tout fait !!

D'accord ! Nous sommes prêts !

Maintenant, démarrez vos deux applications (client et API) dans deux terminaux différents, en utilisant la commande **npm start**.

Si vous naviguez vers [http://localhost:3000/](http://localhost:3000/) dans votre navigateur, vous devriez trouver quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Fwq4HE7hMM2Z5Um3U9xuwCVzlZSAeSvr9U1c)

Bien sûr, ce projet tel quel ne fera pas grand-chose, mais c'est le début d'une application Full Stack. Vous pouvez trouver tout le code dans [**ce dépôt**](https://github.com/Joao-Henrique/React_Express_App_Medium_Tutorial) que j'ai créé pour le tutoriel.

Ensuite, je travaillerai sur quelques tutoriels complémentaires, comme comment connecter cela à une base de données MongoDB et même comment tout exécuter dans des conteneurs Docker.

Comme le dit un bon ami à moi :

> Soyez fort et continuez à coder !!!

...et n'oubliez pas d'être génial aujourd'hui ;)