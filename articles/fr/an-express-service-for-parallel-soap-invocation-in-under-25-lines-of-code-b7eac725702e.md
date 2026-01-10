---
title: Un service Express pour l'invocation SOAP parallèle en moins de 25 lignes de
  code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-09T19:31:11.000Z'
originalURL: https://freecodecamp.org/news/an-express-service-for-parallel-soap-invocation-in-under-25-lines-of-code-b7eac725702e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gnvtnZJe9Ejl8x0oEE_Ufw.jpeg
tags:
- name: Express
  slug: express
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Un service Express pour l'invocation SOAP parallèle en moins de 25 lignes
  de code
seo_desc: 'By Felipe Ignacio Lazo Gallardo

  Overview

  Let’s suppose there is a service that has the following features:


  It exposes a REST endpoint receiving a list of requests.

  It in parallel invokes a SOAP service, once per element in the requests list.

  It retu...'
---

Par Felipe Ignacio Lazo Gallardo

### Aperçu

Supposons qu'il existe un service ayant les caractéristiques suivantes :

1. Il expose un endpoint REST recevant une liste de requêtes.
2. Il invoque en parallèle un service SOAP, une fois par élément dans la liste des requêtes.
3. Il retourne le résultat converti du XML vers le JSON.

Le code source de ce service pourrait ressembler à ceci en utilisant Node.js, Express, et le [Guide de style JavaScript d'Airbnb](https://github.com/airbnb/javascript#airbnb-javascript-style-guide-) :

```js
'use strict';

const { soap } = require('strong-soap');
const expressApp = require('express')();
const bodyParser = require('body-parser');

const url = 'http://www.dneonline.com/calculator.asmx?WSDL';
const clientPromise = new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => err ? reject(err) : resolve(client))
));

expressApp.use(bodyParser.json())
    .post('/parallel-soap-invoke', (req, res) => (clientPromise.then(client => ({ client, requests: req.body }))
        .then(invokeOperations)
        .then(results => res.status(200).send(results))
        .catch(({ message: error }) => res.status(500).send({ error }))
    ))
    .listen(3000, () => console.log('En attente des requêtes entrantes.'));

const invokeOperations = ({ client, requests }) => (Promise.all(requests.map(request => (
    new Promise((resolve, reject) => client.Add(request, (err, result) => (
        err ? reject(err) : resolve(result))
    ))
))));
```

Exemple de requête :

```
POST /parallel-soap-invoke
[
  {
    "intA": 1,
    "intB": 2
  },
  {
    "intA": 3,
    "intB": 4
  },
  {
    "intA": 5,
    "intB": 6
  }
]
```

Exemple de réponse :

```
HTTP/1.1 200
[
  {
    "AddResult": 3
  },
  {
    "AddResult": 7
  },
  {
    "AddResult": 11
  }
]
```

Les tests montrent qu'une seule requête directe au service SOAP utilisant SOAPUI prend ~430 ms (depuis l'endroit où je me trouve, au Chili). L'envoi de trois requêtes (comme montré ci-dessus) prend ~400 ms pour les appels au service Express (à l'exception du premier, qui récupère le WSDL et construit le client).

Pourquoi plus de requêtes prennent-elles moins de temps ? Principalement parce que le XML n'est pas fortement validé comme c'est le cas dans le SOAP régulier, donc si cette validation souple ne correspond pas à vos attentes, vous devriez envisager des fonctionnalités ou solutions supplémentaires.

Vous vous demandez comment cela ressemblerait en utilisant `async/await` ? Voici (les résultats sont les mêmes) :

```js
'use strict';

const { soap } = require('strong-soap');
const expressApp = require('express')();
const bodyParser = require('body-parser');

const url = 'http://www.dneonline.com/calculator.asmx?WSDL';
const clientPromise = new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => err ? reject(err) : resolve(client))
));

expressApp.use(bodyParser.json())
    .post('/parallel-soap-invoke', async (req, res) => {
        try {
            res.status(200).send(await invokeOperations(await clientPromise, req.body));
        } catch ({message: error}) {
            res.status(500).send({ error });
        }
    })
    .listen(3000, () => console.log('En attente des requêtes entrantes.'));

const invokeOperations = (client, requests) => (Promise.all(requests.map(request => (
    new Promise((resolve, reject) => client.Add(request, (err, result) => (
        err ? reject(err) : resolve(result))
    ))
))));
```

L'image suivante fournit une idée de la manière dont le code fonctionne :

![Image](https://cdn-media-1.freecodecamp.org/images/1*WFN937ih5z83fc_gNqWVqw.png)

Cet article vise à montrer la simplicité de l'utilisation de JavaScript pour des tâches dans le monde de l'entreprise, comme l'invocation de services SOAP. Si vous êtes familier avec JavaScript, ceci est essentiellement juste un `Promise.all` sur le dessus de quelques callbacks promisifiés sous un endpoint Express. Vous pouvez aller directement à la section 4 (**Piste bonus**) si vous pensez que cela pourrait être utile pour vous.

Si vous êtes en dehors du monde JavaScript, je pense que 24 lignes de code pour les trois fonctionnalités que j'ai mentionnées au début sont une très bonne affaire. Je vais maintenant entrer dans les détails.

### 1. La section Express

Commençons par le code lié à Express, un framework d'application web minimal et flexible pour Node.js. C'est assez simple et vous pouvez le trouver partout, donc je vais donner une description résumée.

```js
'use strict';

 // Framework Express.
const express = require('express');
// Crée une application Express.
const app = express();

/**
 * Crée un endpoint GET (qui est défini par la méthode invoquée sur 'app'),
 * ayant 'parallel-soap-invoke' comme point d'entrée.
 * Chaque fois qu'une requête GET arrive à '/parallel-soap-invoke', la fonction passée
 * comme second paramètre de app.get sera invoquée.
 * La signature est fixe : les objets de requête et de réponse.
 */
app.get('/parallel-soap-invoke', (_, res) => {
    // Le statut HTTP de la réponse est d'abord défini puis le résultat à envoyer.
    res.status(200).send('Bonjour !');
});

// Démarre 'app' et envoie un message lorsqu'il est prêt.
app.listen(3000, () => console.log('En attente des requêtes entrantes.'));
```

Résultat :

```
GET /parallel-soap-invoke
HTTP/1.1 200
Bonjour !
```

Maintenant, nous aurons besoin de gérer un objet envoyé via POST. Le `body-parser` d'Express permet un accès facile au corps de la requête :

```js

'use strict';

const expressApp = require('express')(); // Compression de deux lignes en une.
const bodyParser = require('body-parser'); // Plusieurs parseurs pour les requêtes HTTP.

expressApp.use(bodyParser.json()) // Indique que 'expressApp' utilisera le parseur JSON.
    // Puisque chaque méthode Express retourne l'objet mis à jour, les méthodes peuvent être enchaînées.
    .post('/parallel-soap-invoke', (req, res) => { 
        /**
         * Par exemple, le même corps de requête sera envoyé comme réponse avec
         * un code de statut HTTP différent.
         */
        res.status(202).send(req.body); // req.body contiendra l'objet analysé 
    })
    .listen(3000, () => console.log('En attente des requêtes entrantes.'));
```

```
POST /parallel-soap-invoke
content-type: application/json

[
  {
    "intA": 1,
    "intB": 2
  },
  {
    "intA": 3,
    "intB": 4
  },
  {
    "intA": 5,
    "intB": 6
  }
]

HTTP/1.1 202

[
  {
    "intA": 1,
    "intB": 2
  },
  {
    "intA": 3,
    "intB": 4
  },
  {
    "intA": 5,
    "intB": 6
  }
]

```

Donc, en résumé : configurez l'application Express, et dès que vous avez le résultat, envoyez-le via `res` et voilà.

### 2. La section SOAP

Cela aura quelques étapes de plus que la section précédente. L'idée principale est que, pour effectuer des invocations SOAP en parallèle, j'utiliserai `Promise.all`. Pour pouvoir utiliser `Promise.all`, l'invocation des services SOAP doit être gérée dans une Promesse, ce qui n'est pas le cas pour `strong-soap`. Cette section montrera comment convertir les callbacks réguliers de `strong-soap` en Promesses et ensuite mettre un `Promise.all` par-dessus.

Le code suivant utilisera l'exemple le plus basique de la [documentation](https://github.com/strongloop/strong-soap#client) de `strong-soap`. Je vais simplement le simplifier un peu et utiliser le même WSDL que nous avons vu (je n'ai pas utilisé le même WSDL indiqué dans la documentation de `strong-soap`, puisque ce WSDL ne fonctionne plus) :

```js
'use strict';

// La bibliothèque cliente SOAP.
var { soap } = require('strong-soap');
// WSDL que nous allons utiliser dans l'article.
var url = 'http://www.dneonline.com/calculator.asmx?WSDL';

// Requête codée en dur
var requestArgs = {
    "intA": 1,
    "intB": 2,
};

// Crée le client qui est retourné dans le callback.
soap.createClient(url, {}, (_, client) => (
    // Le callback livre le résultat de l'invocation SOAP.
    client.Add(requestArgs, (_, result) => (
        console.log(`Résultat : ${"\n" + JSON.stringify(result)}`)
    ))
));
```

```
$ node index.js
Résultat :
{"AddResult":3}
```

Je vais convertir ceci en Promesses et je vais passer par tous les callbacks, un par un, pour l'exemple. De cette façon, le processus de traduction sera clair pour vous :

```js
'use strict';

var { soap } = require('strong-soap');
var url = 'http://www.dneonline.com/calculator.asmx?WSDL';

var requestArgs = {
    "intA": 1,
    "intB": 2,
};

/**
 * Une fonction qui retournera une Promesse qui retournera le client SOAP.
 * La Promesse reçoit comme paramètre une fonction ayant deux fonctions comme paramètres :
 * resolve & reject.
 * Donc, dès que vous avez un résultat, appelez resolve avec le résultat,
 * ou appelez reject avec une erreur sinon.
 */
const createClient = () => (new Promise((resolve, reject) => (
    // Même appel qu'avant, mais je nomme le paramètre d'erreur puisque je vais l'utiliser.
    soap.createClient(url, {}, (err, client) => (
        /**
         * Une erreur s'est produite ? Appelons reject et envoyons l'erreur.
         * Non ? OK, appelons resolve en envoyant le résultat. 
         */
        err ? reject(err) : resolve(client)
    ))))
);

/**
 * La fonction ci-dessus est invoquée.
 * La Promesse aurait pu être en ligne ici, mais c'est plus compréhensible de cette façon.
 */
createClient().then(
    /**
     * Si à l'exécution resolve est invoqué, la valeur envoyée via resolve
     * sera passée comme paramètre pour cette fonction.
     */
    client => (client.Add(requestArgs, (_, result) => (
        console.log(`Résultat : ${"\n" + JSON.stringify(result)}`)
    ))),
    // Même chose que ci-dessus, mais dans ce cas reject a été appelé à l'exécution.
    err => console.log(err),
);
```

L'appel à `node index.js` obtient le même résultat qu'avant. Prochain callback :

```js
'use strict';

var { soap } = require('strong-soap');
var url = 'http://www.dneonline.com/calculator.asmx?WSDL';

var requestArgs = {
    "intA": 1,
    "intB": 2,
};

const createClient = () => (new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => (
        err ? reject(err) : resolve(client)
    ))))
);

/**
 * Même chose qu'avant : faites tout ce que vous devez faire ; une fois que vous avez un résultat,
 * résolvez-le, ou rejetez une erreur sinon.
 * invokeOperation remplacera la première fonction de .then de l'exemple précédent,
 * donc les signatures doivent correspondre.
 */
const invokeOperation = client => (new Promise((resolve, reject) => (
    client.Add(requestArgs, (err, result) => (
        err ? reject(err) : resolve(result)
    ))
)));

/**
 * .then retourne également une Promesse, ayant comme résultat la valeur résolue ou rejetée
 * par les fonctions qui ont été passées comme paramètres. Dans ce cas, le second .then
 * recevra la valeur résolue/rejetée par invokeOperation.
 */
createClient().then(
    invokeOperation,
    err => console.log(err),
).then(
    result => console.log(`Résultat : ${"\n" + JSON.stringify(result)}`),
    err => console.log(err),
);
```

`node index.js` ? Toujours le même. Enveloppons ces Promesses dans une fonction, afin de préparer le code pour l'appeler à l'intérieur de l'endpoint Express. Cela simplifie également un peu la gestion des erreurs :

```js
'use strict';

var { soap } = require('strong-soap');
var url = 'http://www.dneonline.com/calculator.asmx?WSDL';

var requestArgs = {
    "intA": 1,
    "intB": 2,
};

const createClient = () => (new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => (
        err ? reject(err) : resolve(client)
    ))))
);

const invokeOperation = client => (new Promise((resolve, reject) => (
    client.Add(requestArgs, (err, result) => (
        err ? reject(err) : resolve(result)
    ))
)));

const processRequest = () => createClient().then(invokeOperation);

/**
 * .catch() gérera tout reject non géré par un .then. Dans ce cas,
 * il gérera tout reject appelé par createClient ou invokeOperation.
 */
processRequest().then(result => console.log(`Résultat : ${"\n" + JSON.stringify(result)}`))
    .catch(({ message }) => console.log(message));
```

Je parie que vous pouvez deviner le résultat de `node index.js`.

Que se passe-t-il si plusieurs appels consécutifs sont effectués ? Nous allons le découvrir avec le code suivant :

```js
'use strict';

var { soap } = require('strong-soap');
var url = 'http://www.dneonline.com/calculator.asmx?WSDL';

var requestArgs = {
    "intA": 1,
    "intB": 2,
};

const createClient = () => (new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => {
        if (err) {
            reject(err);
        } else {
            // Un message est affiché chaque fois qu'un client est créé.
            console.log('Un nouveau client est en cours de création.');
            resolve(client);
        }
    })))
);

const invokeOperation = client => (new Promise((resolve, reject) => (
    client.Add(requestArgs, (err, result) => (
        err ? reject(err) : resolve(result)
    ))
)));

const processRequest = () => createClient().then(invokeOperation)

processRequest().then(result => console.log(`Résultat : ${"\n" + JSON.stringify(result)}`))
    .catch(({ message }) => console.log(message));
processRequest().then(result => console.log(`Résultat : ${"\n" + JSON.stringify(result)}`))
    .catch(({ message }) => console.log(message));
processRequest().then(result => console.log(`Résultat : ${"\n" + JSON.stringify(result)}`))
    .catch(({ message }) => console.log(message));
```

```
$ node index.js
Un nouveau client est en cours de création.
Un nouveau client est en cours de création.
Résultat :
{"AddResult":3}
Un nouveau client est en cours de création.
Résultat :
{"AddResult":3}
Résultat :
{"AddResult":3}
```

Pas bon, car plusieurs clients sont créés. Idéalement, le client devrait être mis en cache et réutilisé. Il y a deux principales façons d'y parvenir :

1. Vous pouvez créer une variable en dehors de la Promesse et mettre en cache le client dès que vous l'avez (juste avant de le résoudre). Appelons cela `cachedClient`. Mais, dans ce cas, vous devriez gérer manuellement les appels à `createClient()` faits entre la première fois où il est appelé et avant que le premier client ne soit résolu. Vous devriez inspecter si `cachedClient` est la valeur attendue, ou vous devriez vérifier si la Promesse est résolue ou non, ou vous devriez mettre une sorte d'émetteur d'événements pour savoir quand le `cachedClient` est prêt. La première fois que j'ai écrit du code pour cela, j'ai utilisé cette approche et j'ai fini par vivre avec le fait que chaque appel fait avant le premier `createClient().resolve` écrasait `cachedClient`. Si le problème n'est pas clair, faites-le moi savoir et j'écrirai le code et les exemples.
2. Les Promesses ont une fonctionnalité très cool ([voir la documentation MDN, section « Return value »](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)) : si vous appelez `.then()` sur une Promesse résolue/rejetée, elle retournera la même valeur qui a été résolue/rejetée, sans la traiter à nouveau. En fait, très techniquement, ce sera la même référence d'objet.

La deuxième approche est beaucoup plus simple à implémenter, donc le code lié est le suivant :

```js
'use strict';

var { soap } = require('strong-soap');
var url = 'http://www.dneonline.com/calculator.asmx?WSDL';

var requestArgs = {
    "intA": 1,
    "intB": 2,
};

// La fonction createClient est supprimée.
const clientPromise = (new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => {
        if (err) {
            reject(err);
        } else {
            console.log('Un nouveau client est en cours de création.');
            resolve(client);
        }
    })))
);

const invokeOperation = client => (new Promise((resolve, reject) => (
    client.Add(requestArgs, (err, result) => (
        err ? reject(err) : resolve(result)
    ))
)));

// clientPromise est appelé au lieu de getClient().
clientPromise.then(invokeOperation)
    .then(result => console.log(`Résultat : ${"\n" + JSON.stringify(result)}`))
    .catch(({ message }) => console.log(message));
clientPromise.then(invokeOperation)
    .then(result => console.log(`Résultat : ${"\n" + JSON.stringify(result)}`))
    .catch(({ message }) => console.log(message));
clientPromise.then(invokeOperation)
    .then(result => console.log(`Résultat : ${"\n" + JSON.stringify(result)}`))
    .catch(({ message }) => console.log(message));
```

```
$ node index.js
Un nouveau client est en cours de création.
Résultat :
{"AddResult":3}
Résultat :
{"AddResult":3}
Résultat :
{"AddResult":3}
```

Enfin pour cette section, faisons en sorte que le code gère plusieurs appels parallèles. Ce sera facile :

1. Pour gérer plusieurs appels parallèles, nous aurons besoin de `Promise.all`.
2. `Promise.all` a un seul paramètre : un tableau de Promesses. Donc nous allons convertir la liste de requêtes en une liste de Promesses. Le code convertit actuellement une seule requête en une seule Promesse (`invokeOperation`), donc le code a juste besoin d'un `.map` pour y parvenir.

```js
'use strict';

var { soap } = require('strong-soap');
var url = 'http://www.dneonline.com/calculator.asmx?WSDL';

// Liste codée en dur des requêtes.
var requestsArgs = [
    {
        "intA": 1,
        "intB": 2,
    },
    {
        "intA": 3,
        "intB": 4,
    },
    {
        "intA": 5,
        "intB": 6,
    },
];

const clientPromise = (new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => err ? reject(error) : resolve(client))
)));

// Promise.all par-dessus tout.
const invokeOperation = client => (Promise.all(
    // Pour chaque requête, une Promesse est retournée.
    requestsArgs.map(requestArgs => new Promise((resolve, reject) => (
        // Tout reste le même ici.
        client.Add(requestArgs, (err, result) => (
            err ? reject(err) : resolve(result)
        ))
    )))
));

clientPromise.then(invokeOperation)
    .then(result => console.log(`Résultat : ${"\n" + JSON.stringify(result)}`))
    .catch(({ message }) => console.log(message));
```

```
$ node index.js
Résultat :
[{"AddResult":3},{"AddResult":7},{"AddResult":11}]
```

### 3. Mettre le tout ensemble

C'est assez facile — il s'agit simplement d'assembler le dernier code de chaque section précédente :

```js
'use strict';

const { soap } = require('strong-soap');
const expressApp = require('express')();
const bodyParser = require('body-parser');

const url = 'http://www.dneonline.com/calculator.asmx?WSDL';
const clientPromise = new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => err ? reject(err) : resolve(client))
));

expressApp.use(bodyParser.json())
    .post('/parallel-soap-invoke', (req, res) => (clientPromise.then(invokeOperations)
        .then(results => res.status(200).send(results))
        .catch(({ message: error }) => res.status(500).send({ error }))
    ))
    .listen(3000, () => console.log('En attente des requêtes entrantes.'));

// Ajout de req.body au lieu des requêtes codées en dur.
const invokeOperations = client => Promise.all(req.body.map(request => (
    new Promise((resolve, reject) => client.Add(request, (err, result) => (
        err ? reject(err) : resolve(result))
    ))
)));
```

```
POST /parallel-soap-invoke

[
  {
    "intA": 1,
    "intB": 2
  },
  {
    "intA": 3,
    "intB": 4
  },
  {
    "intA": 5,
    "intB": 6
  }
]
 
HTTP/1.1 500

{
  "error": "req is not defined"
}
```

Hmmm… Pas un bon résultat, car je ne m'attendais pas du tout à une erreur. Le problème est que `invokeOperations` n'a pas `req` dans sa portée. La première pensée pourrait être « Ajoutez-le simplement à la signature. » Mais ce n'est pas possible, car cette signature correspond au résultat de la Promesse précédente, et cette promesse ne retourne pas `req`, elle ne retourne que `client`. Mais, que se passe-t-il si nous ajoutons une Promesse intermédiaire dont le seul but est d'injecter cette valeur ?

```js
'use strict';

const { soap } = require('strong-soap');
const expressApp = require('express')();
const bodyParser = require('body-parser');

const url = 'http://www.dneonline.com/calculator.asmx?WSDL';
const clientPromise = new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => err ? reject(err) : resolve(client))
));

expressApp.use(bodyParser.json())
    .post('/parallel-soap-invoke', (req, res) => (
        /**
         * Après clientPromise.then, où le client est reçu, une nouvelle Promesse est
         * créée, et cette Promesse résoudra un objet ayant deux propriétés :
         * client et requests.
         */
        clientPromise.then(client => ({ client, requests: req.body }))
            .then(invokeOperations)
            .then(results => res.status(200).send(results))
            .catch(({ message: error }) => res.status(500).send({ error }))
    ))
    .listen(3000, () => console.log('En attente des requêtes entrantes.'));

/**
 * Puisque la forme de l'objet passé à invokeOperations a changé, la signature doit
 * changer pour refléter la forme du nouvel objet.
 */
const invokeOperations = ({ client, requests }) => Promise.all(requests.map(request => (
    new Promise((resolve, reject) => client.Add(request, (err, result) => (
        err ? reject(err) : resolve(result)
    ))
)));
```

Les résultats sont exactement les mêmes que ceux du résumé.

### 4. Piste bonus

Un convertisseur SOAP vers JSON générique pour l'invocation SOAP parallèle. Le code est familier, basé sur ce que vous avez vu dans les sections précédentes. Qu'en pensez-vous ?

```js
'use strict';

const { soap } = require('strong-soap');
const expressApp = require('express')();
const bodyParser = require('body-parser');

const clientPromises = new Map();

expressApp.use(bodyParser.json())
    .post('/parallel-soap-invoke', ({ body: { wsdlUrl, operation, requests } }, res) => (
        getClient(wsdlUrl).then(client => ({ client, operation, requests }))
            .then(invokeOperations)
            .then(results => res.status(200).send(results))
            .catch(({ message: error }) => res.status(500).send({ error }))
    ))
    .listen(3000, () => console.log('En attente des requêtes entrantes.'));

const getClient = wsdlUrl => clientPromises.get(wsdlUrl)
    || (clientPromises.set(wsdlUrl, new Promise((resolve, reject) => (
        soap.createClient(wsdlUrl, {}, (err, client) => err ? reject(err) : resolve(client))
    ))).get(wsdlUrl));

const invokeOperations = ({ client, operation, requests }) => (Promise.all(requests.map(request => (
    new Promise((resolve, reject) => client[operation](request, (err, result) => (
        err ? reject(err) : resolve(result)
    ))
))));
```

Premier exemple d'utilisation :

```
POST /parallel-soap-invoke
content-type: application/json

{
  "wsdlUrl": "http://www.dneonline.com/calculator.asmx?WSDL",
  "operation": "Add",
  "requests": [
    {
      "intA": 1,
      "intB": 2
    },
    {
      "intA": 3,
      "intB": 4
    },
    {
      "intA": 5,
      "intB": 6
    }
  ]
}

HTTP/1.1 200

[
  {
    "AddResult": 3
  },
  {
    "AddResult": 7
  },
  {
    "AddResult": 11
  }
]

```

Deuxième exemple d'utilisation :

```
POST /parallel-soap-invoke
content-type: application/json

{
  "wsdlUrl": "http://ws.cdyne.com/ip2geo/ip2geo.asmx?wsdl",
  "operation": "ResolveIP",
  "requests": [
    {
      "ipAddress": "8.8.8.8",
      "licenseKey": ""
    },
    {
    	"ipAddress": "8.8.4.4",
    	"licenseKey": ""
    }
  ]
}

HTTP/1.1 200

[
  {
    "ResolveIPResult": {
      "Country": "États-Unis",
      "Latitude": 37.75101,
      "Longitude": -97.822,
      "AreaCode": "0",
      "HasDaylightSavings": false,
      "Certainty": 90,
      "CountryCode": "US"
    }
  },
  {
    "ResolveIPResult": {
      "Country": "États-Unis",
      "Latitude": 37.75101,
      "Longitude": -97.822,
      "AreaCode": "0",
      "HasDaylightSavings": false,
      "Certainty": 90,
      "CountryCode": "US"
    }
  }
]
```

Passez-vous par le [Découplage Numérique](https://www.accenture.com/t00010101T000000__w__/nz-en/_acnmedia/Accenture/Conversion-Assets/DotCom/Documents/Global/PDF/Digital_2/Accenture-Digital-Decoupling.pdf) ? Dans une architecture full-stack JavaScript au-dessus des anciens services, cet artefact pourrait vous aider à encapsuler tous les services SOAP, à les étendre et à exposer uniquement du JSON. Vous pourriez même modifier ce code un peu pour appeler plusieurs services SOAP différents en même temps (ce qui devrait être juste un `.map` et un `.reduce` supplémentaires, comme je le vois maintenant). Ou vous pourriez encapsuler les WSDL de votre entreprise dans une base de données et les invoquer en fonction d'un code ou d'un identifiant. Cela ne serait qu'une ou deux promesses supplémentaires dans la chaîne.