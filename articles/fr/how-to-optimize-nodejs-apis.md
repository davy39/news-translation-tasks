---
title: Comment optimiser votre API Node.js
subtitle: ''
author: Kayode Adeniyi
co_authors: []
series: null
date: '2022-08-22T17:16:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-optimize-nodejs-apis
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-ann-marie-kennon-1296000.jpg
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
- name: optimization
  slug: optimization
seo_title: Comment optimiser votre API Node.js
seo_desc: 'In this article, I will walk you through some of the best methods to optimize
  APIs written in Node.js.

  Prerequisites

  To get the most out of this article, you will need an understanding of the following
  concepts:


  Node.js setup and installation

  How to...'
---

Dans cet article, je vais vous guider à travers certaines des meilleures méthodes pour optimiser les API écrites en Node.js.

### Prérequis

Pour tirer le meilleur parti de cet article, vous aurez besoin de comprendre les concepts suivants :

* Installation et configuration de Node.js
* Comment construire des API avec Node
* Comment utiliser l'outil Postman
* Comment fonctionne JavaScript async/await
* Comment travailler avec une application Redis basique

## Que signifie réellement l'optimisation des API

L'optimisation implique l'amélioration du temps de réponse de votre API. Plus le temps de réponse est court, plus l'API sera rapide. 

Les conseils que je vais partager dans cet article vous aideront à réduire le temps de réponse, diminuer la latence, gérer les erreurs et le débit, et minimiser l'utilisation du CPU et de la mémoire.

# Comment optimiser les API Node.js

## 1. Utilisez toujours des fonctions asynchrones

Les fonctions asynchrones sont comme le cœur de JavaScript. Ainsi, la meilleure chose que nous pouvons faire pour optimiser l'utilisation du CPU est d'écrire des fonctions asynchrones pour effectuer des opérations d'I/O non bloquantes. 

Les opérations d'I/O incluent les processus qui effectuent des opérations de lecture et d'écriture de données. Cela peut être la base de données, le stockage cloud ou tout disque de stockage local sur lequel les opérations d'I/O sont effectuées.

L'utilisation de fonctions asynchrones dans une application qui utilise intensivement les opérations d'I/O l'améliorera. En effet, le CPU pourra gérer plusieurs requêtes simultanément grâce à l'I/O non bloquant, tandis que l'une de ces requêtes effectue une opération d'entrée/sortie.  
  
Voici un exemple :

```js
var fs = require('fs');
// Effectuer une I/O bloquante
var file = fs.readFileSync('/etc/passwd');
console.log(file);
// Effectuer une I/O non bloquante
fs.readFile('/etc/passwd', function(err, file) {
    if (err) return err;
    console.log(file);
});
```

* Nous utilisons le package Node **fs** pour travailler avec les fichiers.
* **readFileSync()** est synchrone et bloque l'exécution jusqu'à la fin.
* **readFile()** est asynchrone et retourne immédiatement tandis que les choses fonctionnent en arrière-plan.

## 2. Évitez les sessions et les cookies dans les API, et envoyez uniquement des données dans la réponse de l'API.

Vous utilisez des cookies et des sessions pour stocker des états temporaires sur le serveur. Ils coûtent cher pour les serveurs. 

Aujourd'hui, les API sans état sont courantes et fournissent des mécanismes d'authentification tels que JWT, OAuth, etc. Ces jetons d'authentification sont conservés côté client et protègent les serveurs de la gestion de l'état. 

JWT est un jeton de sécurité basé sur JSON pour l'authentification des API. Les JWT peuvent être vus mais ne sont pas modifiables une fois envoyés. JWT est simplement sérialisé, pas chiffré. OAuth n'est pas une API ou un service – plutôt, c'est une norme ouverte pour l'autorisation. OAuth est un ensemble standard d'étapes pour obtenir un jeton.

De plus, ne perdez pas votre temps à faire servir des fichiers statiques par votre serveur Node.js. Utilisez plutôt NGINX et Apache, car ils fonctionnent bien mieux que Node pour cet usage. 

Lors de la construction d'API en Node, n'envoyez pas la page HTML complète dans la réponse de l'API. Les serveurs Node fonctionnent mieux lorsque seules les données sont envoyées par l'API. Généralement, ce type d'application fonctionne avec des données JSON.

## 3. Optimisez les requêtes de base de données

L'optimisation des requêtes est une partie essentielle de la construction d'API optimisées en Node. Surtout dans les applications plus grandes, vous devrez interroger les bases de données de nombreuses fois. Ainsi, une mauvaise requête peut réduire les performances globales de l'application.

L'indexation est une approche pour optimiser les performances d'une base de données en minimisant le nombre d'accès au disque nécessaires lors du traitement d'une requête. C'est une technique de structure de données qui est utilisée pour localiser et accéder rapidement aux données dans une base de données. Les index sont créés en utilisant quelques colonnes de la base de données.

Supposons que nous avons un schéma de base de données sans indexation et que la base de données contient 1 million d'enregistrements. Une simple requête de recherche parcourra un grand nombre d'enregistrements pour trouver celui correspondant par rapport au schéma avec indexation.

* Requête sans indexation :

```js
> db.user.find({email: 'ofan@skyshi.com'}).explain("executionStats")
```

* Requête avec indexation :

```js
> db.getCollection("user").createIndex({ "email": 1 }, { "name": "email_1", "unique": true })
{
 "createdCollectionAutomatically" : false,
 "numIndexesBefore" : 1,
 "numIndexesAfter" : 2,
 "ok" : 1
}
```

Il y a une énorme différence dans le nombre de documents scannés ~ 1038 :

| Méthode           | Documents scannés |
|------------------|-------------------|
| Sans indexation   | 1,039             |
| Avec indexation   | 1                 |

## **4. Optimisez les API avec le clustering PM2**

PM2 est un gestionnaire de processus de production conçu pour les applications Node.js. Il dispose d'un équilibreur de charge intégré et permet à l'application de s'exécuter en tant que plusieurs processus sans modifications de code. 

Le temps d'arrêt de l'application est presque nul avec PM2. Dans l'ensemble, PM2 peut vraiment améliorer les performances et la concurrence de votre API. 

Déployez le code en production et exécutez la commande suivante pour voir comment le cluster PM2 a été mis à l'échelle sur tous les CPU disponibles :

```js
pm2 start  app.js -i 0
```

## **5. Réduisez le TTFB (Time to First Byte)**

Le temps jusqu'au premier octet est une mesure utilisée comme indication de la réactivité d'un serveur web ou d'une autre ressource réseau. Le TTFB mesure la durée entre la requête HTTP de l'utilisateur ou du client et la réception du premier octet de la page par le navigateur du client.

Il est peu probable que la page que tous les utilisateurs consultent sur le navigateur web se charge en moins de 100 ms. Cela est simplement dû à la distance physique entre le serveur et les utilisateurs.

Ici, nous pouvons réduire le Time to First Byte en utilisant un CDN et en mettant en cache le contenu dans des centres de données locaux à travers le monde. Cela aide les utilisateurs à accéder au contenu avec une latence minimale. Cloudflare est l'une des solutions CDN que vous pouvez utiliser pour commencer.

## **6. Utilisez des scripts d'erreur avec journalisation**

La meilleure façon de surveiller le bon fonctionnement de vos API est de suivre leur activité. C'est là que la journalisation des données entre en jeu. 

Un exemple courant de journalisation est l'impression des logs dans la console (en utilisant `console.log()`). 

Des modules de journalisation plus efficaces par rapport à console.log sont Morgan, Buyan et Winston. Ici, je vais utiliser l'exemple de Winston.

### Comment journaliser avec Winston – fonctionnalités

* Fournit 4 niveaux personnalisés que nous pouvons utiliser tels que info, error, verbose, debug, silly et warn.
* Supporte l'interrogation des logs
* Profilage simple
* Vous pouvez utiliser plusieurs transports du même type
* Capture et journalise les exceptions non capturées

Vous pouvez configurer Winston avec la commande suivante :

```js
npm install winston --save
```

Et voici une configuration de base de Winston pour la journalisation :

```js
const winston = require('winston');

let logger = new winston.Logger({
  transports: [
    new winston.transports.File({
      level: 'verbose',
      timestamp: new Date(),
      filename: 'filelog-verbose.log',
      json: false,
    }),
    new winston.transports.File({
      level: 'error',
      timestamp: new Date(),
      filename: 'filelog-error.log',
      json: false,
    })
  ]
});

logger.stream = {
  write: function(message, encoding) {
    logger.info(message);
  }
};
```

## **7. Utilisez HTTP/2 au lieu de HTTP**

En plus de ces techniques, nous pouvons également appliquer d'autres techniques comme l'utilisation de HTTP/2 au lieu de HTTP, car il présente les avantages suivants :

* Multiplexage
* Compression des en-têtes
* Push serveur
* Format binaire

Il se concentre sur les performances et les problèmes que la version précédente de HTTP avait. Il rend la navigation web plus rapide et plus facile et consomme moins de bande passante.

## **8. Exécutez les tâches en parallèle**

Utilisez [async.js](https://caolan.github.io/async/v3/) pour vous aider à exécuter des tâches. L'exécution parallèle des tâches a un grand impact sur les performances de votre API. Elle réduit la latence et minimise les opérations bloquantes.   
  
Parallèle signifie exécuter plusieurs choses en même temps. Cependant, lorsque vous exécutez des choses en parallèle, vous n'avez pas besoin de contrôler la séquence d'exécution du programme.

Voici un exemple simple utilisant async parallel avec un tableau :

```js
const async = require("async");
// un exemple utilisant un objet au lieu d'un tableau
async.parallel({
  task1: function(callback) {
    setTimeout(function() {
      console.log('Task One');
      callback(null, 1);
    }, 200);
  },
  task2: function(callback) {
    setTimeout(function() {
      console.log('Task Two');
      callback(null, 2);
    }, 100);
    }
}, function(err, results) {
  console.log(results);
  // results est maintenant égal à : {task2: 2, task1: 1}
});
```

Dans cet exemple, nous avons utilisé [async.js](https://caolan.github.io/async/v3/) pour exécuter les deux tâches en mode asynchrone. La tâche 1 nécessite 200 ms pour se compléter, mais la tâche 2 n'attend pas sa complétion – elle s'exécute à son délai spécifié de 100 ms. 

L'exécution parallèle des tâches a un grand impact sur les performances de l'API. Elle réduit la latence et minimise les opérations bloquantes.

## **9. Utilisez Redis pour mettre en cache l'application**

Redis est la version avancée de Memcached. Il optimise le temps de réponse des API en stockant et en récupérant les données depuis la mémoire principale du serveur. Il améliore les performances des requêtes de base de données, ce qui réduit également la latence d'accès. 

Dans les extraits de code suivants, nous avons appelé les API sans et avec Redis, respectivement, et comparé le temps de réponse. 

Il y a une énorme différence dans le temps de réponse ~ 899.37 ms :

| Méthode        | Temps de réponse |
|---------------|---------------|
| Sans Redis    | 900 ms         |
| Avec Redis    | 0.621 ms       |

Voici Node sans Redis :

```js
'use strict';

// Définir toutes les dépendances nécessaires
const express = require('express');
const responseTime = require('response-time')
const axios = require('axios');

// Charger le Framework Express
var app = express();

// Créer un middleware qui ajoute un en-tête X-Response-Time aux réponses.
app.use(responseTime());

const getBook = (req, res) => {
  let isbn = req.query.isbn;
  let url = `https://www.googleapis.com/books/v1/volumes?q=isbn:${isbn}`;
  axios.get(url)
    .then(response => {
      let book = response.data.items
      res.send(book);
    })
    .catch(err => {
      res.send('Le livre que vous cherchez est introuvable !!!');
    });
};

app.get('/book', getBook);

app.listen(3000, function() {
  console.log('Votre node est en cours d'exécution sur le port 3000 !!!')
});
```

Et voici Node avec Redis :

```js
'use strict';

// Définir toutes les dépendances nécessaires
const express = require('express');
const responseTime = require('response-time')
const axios = require('axios');
const redis = require('redis');
const client = redis.createClient();

// Charger le Framework Express
var app = express();

// Créer un middleware qui ajoute un en-tête X-Response-Time aux réponses.
app.use(responseTime());

const getBook = (req, res) => {
  let isbn = req.query.isbn;
  let url = `https://www.googleapis.com/books/v1/volumes?q=isbn:${isbn}`;
  return axios.get(url)
    .then(response => {
      let book = response.data.items;
      // Définir la clé de chaîne :isbn dans notre cache. Avec le contenu du cache : titre
      // Définir l'expiration du cache à 1 heure (60 minutes)
      client.setex(isbn, 3600, JSON.stringify(book));

      res.send(book);
    })
    .catch(err => {
      res.send('Le livre que vous cherchez est introuvable !!!');
    });
};

const getCache = (req, res) => {
  let isbn = req.query.isbn;
  // Vérifier les données du cache depuis le serveur redis
  client.get(isbn, (err, result) => {
    if (result) {
      res.send(result);
    } else {
      getBook(req, res);
    }
  });
}
app.get('/book', getCache);

app.listen(3000, function() {
  console.log('Votre node est en cours d'exécution sur le port 3000 !!!')
)};
```

## Conclusion

Dans ce guide, nous avons appris comment optimiser le temps de réponse des API Node.js. 

JavaScript dépend fortement des fonctions. Ainsi, l'utilisation de fonctions asynchrones peut rendre le script plus rapide et non bloquant. 

En plus de cela, nous avons utilisé la mémoire cache (Redis), l'indexation de base de données, le TTFB et le clustering PM2 pour améliorer les temps de réponse.

Enfin, gardez à l'esprit qu'il est important de prêter attention à la sécurité des routes et de vous assurer qu'elles sont aussi optimisées que possible. Nous ne pouvons pas compromettre une réponse rapide de l'API au détriment d'une faille de sécurité. Ainsi, vous devez maintenir toutes vos vérifications de sécurité standard lors de la construction d'API optimisées en Node.

Connectez-vous avec moi sur [LinkedIn](https://www.linkedin.com/in/kadeniyi/). 

À bientôt !