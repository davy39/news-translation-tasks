---
title: Comment implémenter le fulfillment local pour les actions Google Assistant
  en utilisant Dialogflow
subtitle: ''
author: Zubin Pratap
co_authors: []
series: null
date: '2019-03-05T15:04:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-local-fulfillment-for-google-assistant-actions-using-dialogflow-1b3b3a13075f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*7jmZNu-Wbc7Z4Ulo.png
tags:
- name: coding
  slug: coding
- name: Google Assistant
  slug: google-assistant
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment implémenter le fulfillment local pour les actions Google Assistant
  en utilisant Dialogflow
seo_desc: 'NB: this blog covers Actions on Google node.js deployments only, and presumes
  some basic prior knowledge of Actions on Google/ Dialogflow


  Google Home Devices that run the Google Assistant

  Hello, world!

  Problem statement

  I’ve been getting into Action...'
---

NB : ce blog couvre uniquement les déploiements node.js d'Actions on Google et présume une connaissance de base d'Actions on Google/Dialogflow

![Image](https://cdn-media-1.freecodecamp.org/images/VFFY4IHPLQMJDw0QkHQf5XQL0au4uIdLTjOI align="left")

*Appareils Google Home qui exécutent Google Assistant*

Bonjour, le monde !

#### **Énoncé du problème**

Je me suis récemment beaucoup intéressé à [Actions on Google](https://developers.google.com/actions/) — je m'amuse énormément — Mon apprentissage a principalement consisté à concevoir de petits "tours de magie" avec lesquels je peux divertir les visiteurs. J'ai fait de même avec Alexa, mais comme je suis beaucoup plus familier avec la [Google Cloud Platform](https://cloud.google.com/) et [Firebase](https://firebase.google.com/) en particulier, j'ai plus prototypé sur Google.

Les Actions et le travail avec Google Assistant nécessitent souvent une logique côté serveur pour gérer l'interaction avec le niveau de personnalisation ou de personnalisation souhaité. Cela s'appelle le "fulfillment".

Le cycle de développement pour le fulfillment peut être un peu fastidieux car vous devez pousser votre code serveur dans le cloud à chaque fois pour voir s'il fonctionne. Chaque fois que nous apportons des modifications que nous voulons tester, nous devons pousser le code vers Firebase et lui donner 30 à 60 secondes pour se propager. C'est comme le développement web avant les rechargements à chaud — ouah ! Donc 2011.

#### **Résumé de l'architecture**

Je ne vais pas entrer dans les détails de la création d'Actions pour l'Assistant, car il y a beaucoup de ressources pour vous aider avec cela. Mais un aperçu de haut niveau du système vous aidera à comprendre l'énoncé du problème qui a inspiré ce blog.

Voici un diagramme de Google qui explique comment les interactions Actions/Assistant sont traitées.

L'interaction d'un utilisateur est captée par l'appareil, convertie en texte qui est analysé par l'appareil, et transmise à un agent [DialogFlow](http://dialogflow.com/) qui est un moteur [NLU](https://en.wikipedia.org/wiki/Natural-language_understanding). Celui-ci détermine ensuite l'« intention » de la déclaration de l'utilisateur (« phrase » ou « énoncé »). Cette intention est ensuite associée à un code qui « satisfait » l'intention de l'utilisateur, puis renvoie une réponse qui est (espérons-le) appropriée et acceptable.

![Image](https://cdn-media-1.freecodecamp.org/images/0*7jmZNu-Wbc7Z4Ulo.png align="left")

Si vous avez étudié l'image, vous verrez qu'une requête est faite dans la dernière colonne, qui désigne [Firebase](https://firebase.google.com/). Ce qu'elle désigne vraiment, c'est un serveur back-end qui possède un webhook HTTP qui reçoit des « requêtes » de fulfillment et détermine ensuite comment répondre de manière appropriée. Architecturalement, l'agent NLU Dialogflow envoie une requête **POST** au webhook du serveur, qui est ensuite traitée par le serveur à l'aide de SDK.

Le serveur back-end qui traite les requêtes et les réponses est facilement hébergé sur [Firebase Cloud Functions](https://firebase.google.com/) (bien sûr, Google facilite l'utilisation de leur stack — c'est juste du bon business !).

De plus, un serveur exécuté localement générera un point de terminaison de webhook comme [http://localhost:3000,](http://localhost:3000,/) qui n'est pas accessible aux requêtes POST de Google Assistant.

#### **Solution — serveur de développement de fulfillment local !**

Il y a trois étapes à cette solution :

1. Créer le serveur de fulfillment back-end en tant que serveur [Express](https://expressjs.com/).

2. Gérer les requêtes et réponses Dialogflow en tant que point de terminaison Express. Le serveur par défaut Firebase Cloud Functions utilise la [Actions on Google Nodejs Client Library](https://github.com/actions-on-google/actions-on-google-nodejs) qui possède une fonctionnalité intégrée pour recevoir les requêtes HTTP POST de l'agent Dialogflow. Mais cela ne fonctionne pas en dehors de l'environnement Firebase (c'est-à-dire sur notre serveur de développement local). Nous devons donc déployer notre serveur de fulfillment en tant qu'application Express.

3. Utiliser le [package Ngrok Node](https://www.npmjs.com/package/ngrok) pour créer un point de terminaison HTTP temporaire qui tunnelise les requêtes HTTP vers notre serveur local:3000 (ou tout autre port que vous utilisez).

Je ne vais pas entrer dans les étapes de configuration de votre code de base pour un serveur de fulfillment nodejs simple — la documentation Dialogflow/Actions on Google vous aide avec tout cela. Mais je fournis ici les extraits qui vous montrent comment convertir cette application Dialogflow en une application Express, et à quoi votre `package.json` doit ressembler.

Commençons par la configuration de base pour le client Dialogflow node.js. Nous l'appellerons l'application Dialogflow.

```js
const {
  dialogflow,
  BasicCard
} = require("actions-on-google");


// Instancier le client Dialogflow.
const app = dialogflow({ debug: true });


// Les gestionnaires vont ici..
app.intent("Default Welcome Intent", conv => {
   // gestionnaire pour cette intention
});

app.intent("Say_Something_Silly", conv => {
   // gestionnaire pour cette intention
});


module.exports = app;
```

C'est l'application qui « gère » les intentions. Le code ci-dessus est juste une structure. Exportez l'application et importez-la dans `functions/index.js`.

`index.js` est le point d'entrée dans notre dossier `functions`, qui contient les fonctions cloud que nous poussons vers Firebase Cloud Functions. Dans ce fichier, nous créons l'application Express, importons l'objet DialogflowApp, puis le passons dans la route Express qui recevra les requêtes HTTP POST de Dialogflow. **Notez** que nous avons besoin du package npm body-parser car les requêtes HTTP sont en JSON.

```js
"use strict";

const express = require("express");
const bodyParser = require("body-parser");
const functions = require("firebase-functions");


// clients
const dialogFlowApp = require("./DialogflowApp");
const expressApp = express().use(bodyParser.json());

// Route de fulfillment de l'application EXPRESS (POST). L'objet dialogFlowApp entier (y compris ses gestionnaires) est le gestionnaire de rappel pour cette route.
expressApp.post("/", dialogFlowApp);


// Route de test de l'application EXPRESS (GET)
expressApp.get("/", (req, res) => {
  res.send("CONFIRMATION DE RÉCEPTION DE GET.");
});



/*
 *   LOGIQUE DU SERVEUR NGROK LOCAL. ASSUREZ-VOUS d'exporter "IS_LOCAL_DEV=true" dans le terminal avant de démarrer
 */
if (process.env.IS_LOCAL_DEV) {
  const PORT = 8000;
  expressApp.listen(PORT, () =>
    console.log(`*** SERVEUR EN COURS D'EXÉCUTION LOCALMENT SUR LE PORT ${PORT} ***`)
  );
} else {
  console.log("*** NON SERVI LOCALMENT - OU - VARIABLE D'ENVIRONNEMENT LOCAL NON DÉFINIE ****");
}

// EXPORTER l'une des deux points de terminaison suivants : une application express, une application dialogflow
exports.fulfillmentExpressServer = functions.https.onRequest(expressApp);
exports.dialogflowFirebaseFulfillment = functions.https.onRequest(dialogFlowApp);
```

Les parties clés de ce code sont que nous créons une route POST qui prend, en tant que rappel de gestionnaire, notre objet DialogflowApp. J'ai créé une route GET juste pour faire des requêtes GET rapides dans le navigateur pour tester si le point de terminaison fonctionne. Mais Dialogflow n'utilise que la route POST.

**Notez** que j'ai fait deux exports ici. L'un est l'application Express et l'autre est l'application Dialogflow elle-même. Cela crée deux fonctions Firebase avec deux points de terminaison qui sont identifiés par la propriété attachée à l'objet `exports`. Un point de terminaison sera &lt;.../fulfillmentExpressServer&gt; et l'autre sera &lt;.../dialogflowFirebaseFulfillment&gt;.

Je peux utiliser l'un de ces points de terminaison HTTP pour le fulfillment, une fois que j'ai terminé le développement local et que j'ai poussé le code final vers Firebase Cloud Functions.

#### **NGROK pour le tunneling du serveur de développement local**

Il y a un code qui semble étrange à la ligne 26. Sur mon terminal Mac, j'utilise `export IS_LOCAL_DEV=true` avant de démarrer le serveur localement. Ce bloc de code à la ligne 26 démarre essentiellement le serveur en écoute locale, ce qui **n'est pas** nécessaire lorsque nous poussons le code vers Cloud Functions — il est uniquement pour le serveur local.

```js
"dependencies": {
    "actions-on-google": "^2.0.0",
    "body-parser": "^1.18.3",
    "express": "^4.16.4",
    "firebase-functions": "^2.2.0"
  },
"devDependencies": {
    "ngrok": "^3.1.1"
  },
"scripts": {
    "lint": "eslint .",
    "serve": "firebase serve --only functions",
    "shell": "firebase experimental:functions:shell",
    "start": "npm run shell",
    "deploy": "firebase deploy --only functions",
    "logs": "firebase functions:log",
    "tunnel": "ngrok http 8000",
    "dev": "nodemon index.js"
  },
```

Ce qui m'amène à la configuration ci-dessus dans package.json. Dans la propriété `scripts`, vous pouvez voir celle appelée `tunnel`. Notez le numéro de port 8000. Il peut être défini à n'importe quelle valeur, mais assurez-vous que le code dans `index.js` qui définit la constante `PORT` (ligne 27 dans le Gist) est le même numéro de port.

Avant d'exécuter le code, vérifiez les points suivants :

1. Vous avez défini votre variable d'environnement et le code correspond — dans mon cas, j'ai utilisé `IS_LOCAL_DEV=true`

2. Vos numéros de port correspondent dans `index.js` et le script `tunnel`

Ensuite, vous ouvrez deux fenêtres de terminal et exécutez les commandes suivantes :

`npm run dev` et `npm run tunnel`

Dans le terminal qui a exécuté le tunnel (ngrok), vous verrez quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*N7SNAkcHzlVyWFoPTVk2eg.png align="left")

Notez les deux adresses de "redirection". Elles sont identiques, sauf qu'une est en https. Les deux fonctionnent. C'est votre point de terminaison, en supposant que votre route POST est `/` et non `/<un chemin>`. Si vous avez ajouté un chemin au gestionnaire POST, vous devez ajouter ce chemin à l'adresse de redirection.

**Notez** que chaque fois que vous exécutez ngrok, il génère une nouvelle URL temporaire pour vous. Par conséquent, vous devez mettre à jour votre webhook de fulfillment Dialogflow chaque fois que vous exécutez `npm run tunnel`.

Et voilà. Plus besoin de pousser chaque petit changement de code vers Firebase Cloud Functions et d'attendre une minute ou deux avant de tester. Développez à la volée, et avec nodemon, votre serveur redémarre et vous pouvez continuer à tester pendant que vous codez !

Et si vous êtes un novice en code et que cela vous semble écrasant, c'est naturel. Vous allez trop loin. J'ai fait la même erreur et cela m'a coûté trop cher.

Si vous souhaitez en savoir plus sur mon parcours dans le code, écoutez l'[épisode 53](http://podcast.freecodecamp.org/53-zubin-pratap-from-lawyer-to-developer) du [podcast freeCodeCamp](http://podcast.freecodecamp.org/), où Quincy (fondateur de freeCodeCamp) et moi partageons nos expériences en tant que reconvertis professionnels, ce qui pourrait vous aider dans votre parcours. Vous pouvez également accéder au podcast sur [iTunes](https://itunes.apple.com/au/podcast/ep-53-zubin-pratap-from-lawyer-to-developer/id1313660749?i=1000431046274&mt=2), [Stitcher](https://www.stitcher.com/podcast/freecodecamp-podcast/e/59201373?autoplay=true) et [Spotify](https://open.spotify.com/episode/4lG0RGpzriG5vXRMgza05C).

Je vais également organiser quelques AMAs et webinaires dans les mois à venir. Si cela vous intéresse, faites-le moi savoir en allant [ici](http://www.matchfitmastery.com/). Et bien sûr, vous pouvez également me tweeter à [@ZubinPratap](https://twitter.com/zubinpratap).