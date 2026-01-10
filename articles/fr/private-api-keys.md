---
title: Comment éviter d'exposer votre clé API dans vos applications front-end publiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-23T02:50:37.000Z'
originalURL: https://freecodecamp.org/news/private-api-keys
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9fd5740569d1a4ca44e3.jpg
tags:
- name: backend
  slug: backend
seo_title: Comment éviter d'exposer votre clé API dans vos applications front-end
  publiques
seo_desc: 'By Jackson Bates

  The Problem

  All you want to do is fetch some JSON from an API endpoint for the weather, some
  book reviews, or something similarly simple.

  The fetch query in your front-end is easy enough, but you have to paste your secret
  API key rig...'
---

Par Jackson Bates

## Le Problème

Tout ce que vous voulez faire, c'est récupérer un peu de JSON depuis un point de terminaison d'API pour la météo, des critiques de livres, ou quelque chose de similaire.

La requête de récupération dans votre front-end est assez simple, mais vous devez coller votre clé API secrète directement dans le code front-end, où n'importe qui peut la trouver avec un minimum de recherche !

De plus, pousser vos clés API vers votre dépôt GitHub est un problème majeur : [Dev met les clés AWS sur Github. Ensuite, de MAUVAISES CHOSES se sont produites](https://www.theregister.co.uk/2015/01/06/dev_blunder_shows_github_crawling_with_keyslurping_bots/).

> "Pourquoi c'est si difficile ?!"  Vous, probablement il y a 15 minutes

## La Solution

Vous devriez utiliser un serveur back-end comme relais pour récupérer les résultats de l'API pour vous et ensuite les transmettre à votre front-end.

## Le Nouveau Problème

Vous essayez simplement de faire une démonstration front-end pour votre portfolio ! Vous n'avez pas encore appris les technologies back-end ! Pourquoi c'est si difficile ?!

# Démo

J'ai rencontré ce problème suffisamment souvent pour décider d'arrêter de trouver des solutions bidouillées et de mettre en place une solution qui fonctionne avec un minimum de code back-end.

Dans cette démonstration, j'ai configuré un back-end qui écoute les requêtes POST et les envoie à l'[API GoodReads](https://www.goodreads.com/api). Pour utiliser cela, vous devez implémenter **votre propre** front-end qui peut envoyer la requête POST appropriée à ce back-end. Votre front-end ne communiquera pas directement avec GoodReads, donc aucune clé API n'est exposée.

## Ce dont vous aurez besoin

* [Node](https://nodejs.org/en/download/) (ceci a été testé avec la v10.16.0, les versions ultérieures seront bien, les versions antérieures peuvent rencontrer des problèmes)
* [git](https://git-scm.com/downloads)
* Ce dépôt : https://github.com/JacksonBates/example-goodreads-api-relay

### Commencer

`git clone https://github.com/JacksonBates/example-goodreads-api-relay.git`

Le fichier README.md contient tout ce dont vous avez besoin, y compris l'installation et la configuration.

J'ai inclus les points clés ici pour votre commodité :

### README.md

Installez les dépendances :

`npm i`

Vous devez créer votre propre fichier `.env` pour votre clé :

`cp .env.example .env`

Puis ouvrez le nouveau fichier `.env` et collez vos clés au bon endroit.

Exemple :

```
GOODREADS_API_KEY=AABBCCDDEEFF00112233445566778899
```

Maintenant, lancez le serveur :

`node app.js`

Dans le navigateur, allez sur localhost:3000 pour confirmer que le serveur est en cours d'exécution. Vous devriez voir un simple `Hello World!`

### Et ensuite ?

Lisez maintenant le fichier `app.js` attentivement.

J'ai commenté le code abondamment pour vous aider à comprendre ce qui se passe si vous n'avez pas beaucoup vu node / express auparavant.

```js
// app.js

// Ces lignes importent les modules nécessaires et définissent certaines variables initiales
require("dotenv").config();
const express = require("express");
const fetch = require("node-fetch");
const convert = require("xml-js");
const rateLimit = require("express-rate-limit");
const app = express();
const port = 3000;

// Limitation de débit - Goodreads limite à 1/sec, donc nous devrions aussi

// Activez si vous êtes derrière un proxy inverse (Heroku, Bluemix, AWS ELB, Nginx, etc)
// voir https://expressjs.com/en/guide/behind-proxies.html
// app.set('trust proxy', 1);

const limiter = rateLimit({
	windowMs: 1000, // 1 seconde
	max: 1, // limite chaque IP à 1 requête par windowMs
})

// appliquer à toutes les requêtes
app.use(limiter)

// Routes

// Route de test, visitez localhost:3000 pour confirmer que cela fonctionne
// devrait afficher 'Hello World!' dans le navigateur
app.get("/", (req, res) => res.send("Hello World!"));

// Notre route de relais Goodreads !
app.get("/api/search", async (req, res) => {
	try {
		// Cela utilise l'interpolation de chaînes pour créer notre chaîne de requête de recherche
		// il récupère le paramètre de requête posté et le reformate pour goodreads
		const searchString = `q=${req.query.q}`;

		// Il utilise node-fetch pour appeler l'API goodreads, et lit la clé depuis .env
		const response = await fetch(`https://www.goodreads.com/search/index.xml?key=${process.env.GOODREADS_API_KEY}&${searchString}`);
		//plus d'info ici https://www.goodreads.com/api/index#search.books
		const xml = await response.text();

		// L'API Goodreads retourne du XML, donc pour l'utiliser facilement sur le front end, nous pouvons
		// convertir cela en JSON :
		const json = convert.xml2json(xml, { compact: true, spaces: 2 });

		// L'API retourne des choses dont nous ne nous soucions pas, donc nous pouvons aussi bien supprimer
		// tout sauf les résultats :
		const results = JSON.parse(json).GoodreadsResponse.search.results;

		return res.json({
            success: true,
            results
        })
	} catch (err) {
		return res.status(500).json({
			success: false,
			message: err.message,
		})
	}
})

// Cela lance notre serveur et génère des logs pour que nous puissions les utiliser.
// Toute instruction console.log que vous utilisez dans node pour le débogage apparaîtra dans votre
// terminal, pas dans la console du navigateur !
app.listen(port, () => console.log(`Example app listening on port ${port}!`));
```

**Mise à jour** : Un grand merci à Gouri Shankar Kumawat pour avoir contribué à une PR qui a amélioré ce code ! Vous pouvez le suivre sur Twitter à l'adresse [@dev_gskumawat](https://https://twitter.com/dev_gskumawat), ou sur GitHub : [gskumawat0](https://github.com/gskumawat0)

### Tester le relais API

Utilisez [Postman](https://www.getpostman.com/) pour tester l'API.

Configurez Postman pour GET et collez ceci dans l'URL : `localhost:3000/api/search?q=hobbit`

Postman vous montrera la réponse JSON ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/get_request.png)
_Capture d'écran de Postman montrant le JSON retourné par notre nouveau back-end_

### Comment utiliser cela dans votre front-end ?

Cette application simple écoute les requêtes post à `/api/search`, donc interagissez avec elle dans votre application front-end de la manière dont vous l'avez fait précédemment avec l'API originale.

Cela n'est configuré que pour gérer les requêtes de recherche - si vous voulez utiliser d'autres points de terminaison/méthodes de l'API Goodreads, vous devrez réfléchir à la manière de les implémenter vous-même !

### Hébergement

Vous ne pouvez pas déployer votre front-end et toujours avoir cela sur localhost - évidemment, vous devez également déployer cela.

Je recommande [Heroku](https://devcenter.heroku.com/articles/deploying-nodejs).

## Crédits supplémentaires

Si vous vouliez étendre cela, vous pourriez considérer comment rendre cela accessible uniquement depuis une plage restreinte d'adresses IP pour augmenter la sécurité - ce qui était hors du cadre de ce tutoriel/démo.

---

Cela a été rapidement mis en place en réponse à une discussion sur le [forum](https://www.freecodecamp.org/forum). Si vous repérez des problèmes dans cet article ou dans le code exemple, n'hésitez pas à répondre au [fil de forum](https://www.freecodecamp.org/forum/t/trying-to-fetch-response-from-goodreads-api/323312?u=jacksonbates) qui a tout commencé. Je garderai l'article et le dépôt à jour avec les améliorations.

N'hésitez pas à soumettre des PR si vous avez des contributions précieuses à apporter :)

Vous pouvez également me contacter via Twitter : [@JacksonBates](https://twitter.com/jacksonbates).