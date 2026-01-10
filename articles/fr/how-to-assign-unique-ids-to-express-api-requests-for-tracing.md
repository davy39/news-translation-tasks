---
title: Comment attribuer des identifiants uniques aux requêtes API Express pour le
  traçage
subtitle: ''
author: Orim Dominic Adah
co_authors: []
series: null
date: '2025-08-19T17:50:34.986Z'
originalURL: https://freecodecamp.org/news/how-to-assign-unique-ids-to-express-api-requests-for-tracing
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1755625819738/b5d45868-c770-4878-8c49-63011507ef56.png
tags:
- name: Node.js
  slug: nodejs
- name: Express
  slug: express
seo_title: Comment attribuer des identifiants uniques aux requêtes API Express pour
  le traçage
seo_desc: 'The ability to track what happens with API requests is an important aspect
  of monitoring, tracing and debugging back-end applications. But how do you differentiate
  between the reports of two consecutive API requests to the same API endpoint?

  This art...'
---

La capacité à suivre ce qui se passe avec les requêtes API est un aspect important de la surveillance, du traçage et du débogage des applications back-end. Mais comment différencier les rapports de deux requêtes API consécutives vers le même point de terminaison API ?

Cet article vise à vous montrer comment :

* Attribuer correctement un ID unique aux requêtes API dans vos applications Express,
    
* Stocker et accéder à l'ID en utilisant l'API [AsyncLocalStorage](https://nodejs.org/docs/latest-v18.x/api/async_context.html#class-asynclocalstorage) de Node.js, et
    
* L'utiliser dans la journalisation des requêtes.
    

Une expérience dans la création de points de terminaison API et l'utilisation de middlewares dans Express sera utile pour suivre ce guide. Vous pouvez également appliquer les idées de cet article à des Frameworks comme NestJS et Koa.

## Table des matières

* [Mise en route avec le dépôt de démarrage](#heading-mise-en-route-avec-le-depot-de-demarrage)
    
* [Configuration des utilitaires de journalisation](#heading-configuration-des-utilitaires-de-journalisation)
    
* [Qu'est-ce que AsyncLocalStorage et pourquoi est-ce important ?](#heading-qu-est-ce-que-asynclocalstorage-et-pourquoi-est-ce-important)
    
* [Stocker l'ID de la requête dans AsyncLocalStorage](#heading-stocker-l-id-de-la-requete-dans-asynclocalstorage)
    
* [Utiliser l'ID de la requête dans les utilitaires de journalisation](#heading-utiliser-l-id-de-la-requete-dans-les-utilitaires-de-journalisation)
    
* [Définir l'en-tête pour avoir X-Request-Id (Défi optionnel)](#heading-definir-l-en-tete-pour-avoir-x-request-id-defi-optionnel)
    
* [Conclusion](#heading-conclusion)
    

## Mise en route avec le dépôt de démarrage

Pour faciliter le suivi, j'ai créé un projet de démarrage et l'ai hébergé sur GitHub. Vous pouvez le [cloner ici](https://github.com/orimdominic/freecodecamp-express-request-ids). Pour le mettre en service sur votre ordinateur local, installez ses dépendances en utilisant votre gestionnaire de paquets JavaScript préféré (npm, yarn, pnpm, bun). Ensuite, lancez l'application en exécutant la commande `npm start` dans le terminal du projet.

Si l'application démarre avec succès, elle devrait afficher l'extrait ci-dessous sur le terminal :

```bash
Listening on port 3333
```

L'application n'a actuellement qu'un seul point de terminaison API – un `GET /`. Lorsque vous effectuez une requête API vers le point de terminaison en utilisant `curl` ou un navigateur en visitant http://localhost:3333, vous recevrez une chaîne "OK" comme réponse :

```bash
$ curl -i http://localhost:3333

OK%
```

Si l'extrait ci-dessus est ce que vous voyez, alors félicitations ! Vous avez configuré le projet correctement.

## Configuration des utilitaires de journalisation

La première étape consiste à configurer des loggers personnalisés pour enregistrer les messages sur le terminal. Les loggers enregistreront les événements qui se produisent pendant le processus de traitement d'une requête API et consigneront le résumé de la requête.

Pour y parvenir, vous devrez installer deux middlewares Express – [morgan](https://www.npmjs.com/package/morgan) et [winston](https://www.npmjs.com/package/winston) – en utilisant votre gestionnaire de paquets préféré. Si vous utilisez `npm`, vous pouvez exécuter la commande ci-dessous dans le terminal du dossier du projet :

```bash
$ npm install morgan winston 
```

Si la commande ci-dessus réussit, morgan et winston seront ajoutés à l'objet `dependencies` dans `package.json`. Créez un fichier nommé `logger.js` dans le dossier racine du projet. `logger.js` contiendra le code pour les utilitaires de journalisation personnalisés.

Le premier utilitaire de journalisation que vous créerez est `logger`, créé à partir du package winston que vous avez installé précédemment. `logger` est un objet avec deux méthodes :

* `info` pour enregistrer les messages non liés à une erreur sur le terminal
    
* `error` pour enregistrer les messages d'erreur sur le terminal
    

```javascript
// logger.js

const winston = require("winston");

const { combine, errors, json, timestamp, colorize } = winston.format;

const logHandler = winston.createLogger({
  level: "debug",
  levels: winston.config.npm.levels,
  format: combine(
    timestamp({ format: "YYYY-MM-DD hh:mm:ss.SSS A" }), // définit le format des horodatages enregistrés
    errors({ stack: true }),
    json({ space: 2 }),
    colorize({
      all: true,
      colors: {
        info: "gray", // tous les journaux d'info doivent être de couleur grise
        error: "red", // tous les journaux d'erreur doivent être de couleur rouge     
        },
    })
  ),
  transports: [new winston.transports.Console()],
});

exports.logger = {
  info: function (message) {
    logHandler.child({}).info(message);
  },

  error: function (message) {
    logHandler.child({}).error(message);
  },
};
```

Dans l'extrait de code ci-dessus, `winston.createLogger` est utilisé pour créer `logHandler`. `logger` est exporté du module `logger.js` et `logger.info` et `logger.error` sont des fonctions qui utilisent `logHandler` pour enregistrer des messages sur le terminal.

Le deuxième utilitaire de journalisation sera un middleware qui enregistrera des informations sur la requête juste avant que la réponse ne soit envoyée au client. Il enregistrera des informations telles que le temps d'exécution de la requête et le code de statut de la requête. Il sera appelé `logRequestSummary` et utilisera le package morgan et la méthode `http` de `logHandler`.

```javascript
// logger.js

const winston = require("winston");
const morgan = require("morgan");

const { combine, errors, json, timestamp, colorize } = winston.format;

const logHandler = winston.createLogger({
  // ...
  format: combine(
    // ...
    colorize({
      all: true,
      colors: {
        // ...
        http: "blue", // 👈🏾 (nouvelle ligne) les journaux de logRequestSummary seront de couleur bleue
      },
    })
  ),
  // ...
});

exports.logger = {
    // ...
};

exports.logRequestSummary = morgan(
  function (tokens, req, res) {
    return JSON.stringify({
      url: tokens.url(req, res),
      method: tokens.method(req, res),
      status_code: Number(tokens.status(req, res) || "500"),
      content_length: tokens.res(req, res, "content-length") + " bytes",
      response_time: Number(tokens["response-time"](req, res) || "0") + " ms",
    });
  },
  {
    stream: {
      // utiliser logHandler avec la sévérité http
      write: (message) => {
        const httpLog = JSON.parse(message);
        logHandler.http(httpLog);
      },
    },
  }
);
```

La chaîne JSON renvoyée par la première fonction lors de l'exécution de la fonction `morgan` est reçue par la fonction `write` de l'objet `stream` dans le deuxième argument passé à la fonction morgan. Elle est ensuite analysée en JSON et transmise à `logHandler.http` pour être enregistrée avec le niveau de sévérité `http` de `winston.npm`.

À ce stade, deux objets sont exportés de `logger.js` : `logger` et `logRequestSummary`.

Dans `index.js`, créez un nouveau contrôleur pour gérer les requêtes `GET` vers le chemin `/hello`. Importez et utilisez également les objets exportés de `logger.js`. Utilisez `logger` pour enregistrer des informations lorsque des événements se produisent dans les contrôleurs et incluez `logRequestSummary` comme middleware pour l'application.

```javascript
// index.js
const express = require("express");
const { logRequestSummary, logger } = require("./logger");

const app = express();

app.use(
  express.json(),
  express.urlencoded({ extended: true }),
  logRequestSummary // utilitaire middleware de journalisation
);

app.get("/", function (req, res) {
  logger.info(`${req.method} request to ${req.url}`); // utilitaire logger pour les événements
  return res.json({ method: req.method, url: req.url });
});

app.get("/hello", function (req, res) {
  logger.info(`${req.method} request to ${req.url}`); // utilitaire logger pour les événements
  return res.json({ method: req.method, url: req.url });
});

// ...
```

Arrêtez l'application (avec `CTRL` + `C` ou `OPTION` + `C`), et redémarrez-la avec `npm start`. Faites des requêtes API vers les deux points de terminaison, vous verrez une sortie similaire à l'extrait ci-dessous dans le terminal – un journal d'événement d'abord et un journal du résumé de la requête après.

```bash
{
  "level": "info",
  "message": "GET request to /",
  "timestamp": "2025-08-16 10:35:06.831 PM"
}
{
  "level": "http",
  "message": {
    "content_length": "26 bytes",
    "method": "GET",
    "response_time": "9.034 ms",
    "status_code": 200,
    "url": "/"
  },
  "timestamp": "2025-08-16 10:35:06.844 PM"
}
```

Vous pouvez consulter le dernier état du code en basculant vers la branche `2-custom-logger-middleware` en utilisant `git checkout 2-custom-logger-middleware` ou en visitant la branche [2-custom-logger-middleware](https://github.com/orimdominic/freecodecamp-express-request-ids/tree/2-custom-logger-middleware) du dépôt.

Maintenant que vous pouvez enregistrer et visualiser les événements qui se produisent pour chaque requête API, comment différencier deux requêtes consécutives vers le même point de terminaison ? Comment savoir quelle requête API a enregistré un message spécifique ? Comment spécifier la requête API à tracer lors de la communication avec vos coéquipiers ? En attachant un ID unique à chaque requête, vous pourrez répondre à toutes ces questions.

## Qu'est-ce que AsyncLocalStorage et pourquoi est-ce important ?

Avant [AsyncLocalStorage](https://nodejs.org/docs/latest-v18.x/api/async_context.html#class-asynclocalstorage), les utilisateurs d'Express stockaient les informations de contexte de requête dans l'objet `res.locals`. Avec AsyncLocalStorage, Node.js fournit un moyen natif de stocker les informations nécessaires à l'exécution de fonctions asynchrones. Selon sa documentation, il s'agit d'une implémentation performante et sûre du point de vue de la mémoire qui implique des optimisations significatives qu'il serait difficile d'implémenter soi-même.

Lorsque vous utilisez AsyncLocalStorage, vous pouvez stocker et accéder aux informations d'une manière similaire à [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) dans le navigateur. Vous passez la valeur du store (généralement un objet, mais cela peut aussi être une valeur primitive) comme premier argument et la fonction asynchrone qui doit accéder à la valeur du store comme deuxième argument lorsque vous exécutez la méthode `run`.

James Snell, l'un des principaux contributeurs de Node.js, l'explique plus en détail dans cette vidéo [Async Context Tracking in Node with Async Local Storage API](https://www.youtube.com/watch?v=ukefzxZ_G9U).

## Stocker l'ID de la requête dans AsyncLocalStorage

Dans le projet, créez un fichier portant le nom `context-storage.js`. Dans ce fichier, vous créerez une instance d'AsyncLocalStorage (si elle n'a pas encore été créée) et l'exporterez. Cette instance d'AsyncLocalStorage sera utilisée pour stocker et récupérer les ID de requête pour le logger et tout autre contexte nécessitant l'ID de requête.

```javascript
// context-storage.js
const { AsyncLocalStorage } = require("node:async_hooks");

let store;

module.exports.contextStorage = function () {
  if (!store) {
    store = new AsyncLocalStorage();
  }

  return store;
};
```

Vous créerez un autre fichier appelé `set-request-id.js` qui créera et exportera un middleware. Le middleware interceptera les requêtes API, générera un ID de requête et le stockera dans l'instance d'AsyncLocalStorage de `context-storage.js` s'il n'y figure pas déjà.

Vous pouvez utiliser n'importe quelle bibliothèque de génération d'ID de votre choix, mais ici nous utiliserons `randomUUID` du package `crypto` de Node.js.

```javascript
// set-request-id.js
const { randomUUID } = require("node:crypto");
const { contextStorage } = require("./context-storage");

/**
 * De préférence votre premier middleware.
 *
 * Il génère un ID unique et le stocke dans l'instance AsyncLocalStorage
 * pour le contexte de la requête.
 */
module.exports.setRequestId = function () {
  return function (_req, _res, next) {
    requestId = randomUUID();
    const store = contextStorage().getStore();

    if (!store) {
      return contextStorage().run({ requestId }, next);
    }

    if (store && !store.requestId) {
      store.requestId = requestId;
      return next();
    }

    return next();
  };
};
```

Dans la fonction `setRequestId` de l'extrait ci-dessus, l'instance d'AsyncLocalStorage créée dans `context-storage.js` est récupérée à partir de la valeur de retour de l'exécution de `contextStorage` sous le nom `store`. Si `store` est faux, la méthode `run` exécute le rappel Express `next`, en fournissant `requestId` dans un objet pour un accès n'importe où dans `next` via `contextStorage`.

Si `store` a une valeur mais n'a pas la propriété `requestId`, définissez la propriété `requestId` et sa valeur sur celui-ci et renvoyez la fonction `next` exécutée.

Enfin, placez `setRequestId` comme premier middleware de l'application Express dans `index.js` afin que chaque requête puisse avoir un ID avant d'effectuer d'autres opérations.

```javascript
// index.js
const express = require("express");
const { logRequestSummary, logger } = require("./logger");
const { setRequestId } = require("./set-request-id");

const app = express();

app.use(
  setRequestId(), // 👈🏾 défini comme premier middleware
  express.json(),
  express.urlencoded({ extended: true }),
  logRequestSummary
);

// ...
```

Vous pouvez vérifier l'état actuel de ce projet si vous exécutez la commande `git checkout 3-async-local-storage-req-id` sur votre terminal ou en visitant [3-async-local-storage-req-id](https://github.com/orimdominic/freecodecamp-express-request-ids/tree/3-async-local-storage-req-id) du dépôt GitHub.

## Utiliser l'ID de la requête dans les utilitaires de journalisation

Maintenant que la propriété `requestId` a été définie dans le store, vous pouvez y accéder de n'importe où dans `next` en utilisant `contextStorage`. Vous y accéderez dans les fonctions de `logger.js` et l'attacherez aux journaux afin que, lorsque des messages sont enregistrés sur le terminal pour une requête, l'ID de la requête apparaisse avec le message enregistré.

```javascript
// logger.js
const winston = require("winston");
const morgan = require("morgan");
const { contextStorage } = require("./context-storage");

const { combine, errors, json, timestamp, colorize } = winston.format;

const logHandler = winston.createLogger({
  level: "debug",
  levels: winston.config.npm.levels,
  format: combine(

    // 👇🏽 récupérer requestId de contextStorage et l'attacher au message journalisé
    winston.format((info) => {
      info.request_id = contextStorage().getStore()?.requestId;
      return info;
    })(),
    // 👆🏽 récupérer requestId de contextStorage et l'attacher au message journalisé

    timestamp({ format: "YYYY-MM-DD hh:mm:ss.SSS A" }),
    errors({ stack: true }),
    // ...
  ),
  transports: [new winston.transports.Console()],
});

// ...
```

Dans la fonction `combine` de winston, vous inclurez un argument de fonction qui accepte le message à enregistrer – `info` – comme argument et lui attacherez la propriété `request_id`. Sa valeur est la valeur de `requestId` récupérée de `contextStorage`. Avec cette modification, tout message enregistré pour une requête aura l'ID de cette requête qui lui sera attaché.

Une fois cela terminé, arrêtez le projet s'il est déjà en cours d'exécution et relancez-le avec la commande `npm start`. Faites des requêtes API vers les deux points de terminaison et vous verrez une sortie similaire à l'extrait ci-dessous sur le terminal :

```bash
{
  "level": "info",
  "message": "GET request to /hello",
  "request_id": "c80e92d0-eafe-42c7-b093-e5ffce014819",
  "timestamp": "2025-08-17 07:58:13.571 PM"
}
{
  "level": "http",
  "message": {
    "content_length": "31 bytes",
    "method": "GET",
    "response_time": "9.397 ms",
    "status_code": 200,
    "url": "/hello"
  },
  "request_id": "c80e92d0-eafe-42c7-b093-e5ffce014819",
  "timestamp": "2025-08-17 07:58:13.584 PM"
}
```

Contrairement à la sortie de journal précédente, celle-ci contient l'ID de chaque requête. En utilisant `AsyncLocalStorage` pour stocker efficacement la valeur de l'ID de requête et y accéder pour l'utiliser dans les loggers, vous pouvez tracer avec précision les messages enregistrés vers leurs requêtes API.

Vous pouvez accéder à l'état actuel du projet si vous exécutez la commande `git checkout 4-use-context-in-logger` sur le terminal ou en visitant [4-use-context-in-logger](https://github.com/orimdominic/freecodecamp-express-request-ids/tree/4-use-context-in-logger) du dépôt GitHub.

## Définir l'en-tête pour avoir X-Request-Id (Défi optionnel)

Vous avez réussi à stocker, accéder et attacher l'ID d'une requête à son message journalisé. Pouvez-vous définir l'ID de la requête comme un en-tête sur la réponse ? Le défi consiste à définir un en-tête, `X-Request-Id`, sur la réponse afin que chaque réponse de requête ait la valeur de l'ID de la requête comme valeur de l'en-tête de réponse `X-Request-Id`.

Ceci est utile pour communiquer avec le frontend lors de tentatives de débogage de requêtes.

## Conclusion

Lorsque les requêtes API peuvent être surveillées, vous pouvez suivre les mesures de performance pour découvrir les domaines qui nécessitent une amélioration et une attention particulière, identifier les problèmes tels que les requêtes échouées et les erreurs de serveur et pourquoi ils se sont produits, et étudier les modèles dans les mesures de volume de requêtes pour la planification et l'évolutivité.

Lorsque vous attachez un identifiant unique à une requête API, vous pouvez l'utiliser pour tracer les événements qui se sont produits pendant la durée de vie de la requête et la différencier des autres requêtes du même type.

En plus d'utiliser AsyncLocalStorage pour stocker les ID de requête, vous pouvez également l'utiliser pour stocker d'autres informations de contexte de requête telles que les détails de l'utilisateur authentifié. L'utilisation d'AsyncLocalStorage pour stocker les informations de contexte de requête est considérée comme une bonne pratique.