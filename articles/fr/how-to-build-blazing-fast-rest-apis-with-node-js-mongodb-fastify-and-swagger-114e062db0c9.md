---
title: Comment créer des API REST ultra-rapides avec Node.js, MongoDB, Fastify et
  Swagger
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-05T22:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-blazing-fast-rest-apis-with-node-js-mongodb-fastify-and-swagger-114e062db0c9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*B8yGyadpWiDJtyXGVtNO-Q.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: REST API
  slug: rest-api
- name: 'tech '
  slug: tech
seo_title: Comment créer des API REST ultra-rapides avec Node.js, MongoDB, Fastify
  et Swagger
seo_desc: 'By Siegfried Grimbeek

  Presumably no web developer is a stranger to REST APIs and the challenges that architecting
  an effective and efficient API solution brings.

  These challenges include:


  Speed (API Response Times)

  Documentation (Clear concise docum...'
---

Par Siegfried Grimbeek

Présumément, aucun développeur web n'est étranger aux **API REST** et aux défis que l'architecture d'une solution **API** efficace et performante apporte.

Ces défis incluent :

* Vitesse (Temps de réponse de l'API)
* Documentation (Documents clairs et concis, décrivant l'API)
* Architecture et Durabilité (Base de code maintenable et extensible)

Dans ce tutoriel, nous allons aborder tous les points ci-dessus en utilisant une combinaison de **Node.js**, **MongoDB**, **Fastify** et **Swagger**.

Le code source du projet est disponible sur [GitHub](https://github.com/siegfriedgrimbeek/fastify-api).

### Avant de commencer…

Vous devriez avoir quelques connaissances de base/intermédiaires en **JavaScript**, avoir entendu parler de **Node.js** et **MongoDB**, et savoir ce que sont les **API REST**.

Voici quelques liens pour vous mettre à jour :

* [JavaScript](https://developer.mozilla.org/bm/docs/Web/JavaScript)
* [Node.js](https://codeburst.io/the-only-nodejs-introduction-youll-ever-need-d969a47ef219)
* [MongoDB](https://docs.mongodb.com/manual/introduction/)
* [REST APIs](https://restful.io/an-introduction-to-api-s-cee90581ca1b)

#### La technologie que nous allons utiliser :

* [Fastify](https://www.fastify.io/)
* [Mongoose](https://mongoosejs.com/)
* [Swagger](https://swagger.io/)

Il est bon d'ouvrir les pages ci-dessus dans de nouveaux onglets pour une référence facile.

#### Vous devrez avoir installé les éléments suivants :

* [NodeJS/NPM](https://nodejs.org/en/)
* [MongoDB](https://docs.mongodb.com/manual/installation/)
* [Postman](https://www.getpostman.com/)

Vous aurez également besoin d'un [**IDE**](https://ourcodeworld.com/articles/read/200/top-7-best-free-web-development-ide-for-javascript-html-and-css) et d'un **terminal**, j'utilise [iTerm2](https://www.iterm2.com/) pour Mac et [Hyper](https://hyper.is/) pour Windows.

### Commençons !

![Image](https://cdn-media-1.freecodecamp.org/images/1*Jw9V__6jYhm2amP74D_0lw.png)

Initialisez un nouveau projet en ouvrant votre **terminal** et en exécutant chacune des lignes de code suivantes :

```bash
mkdir fastify-api
cd fastify-api
mkdir src
cd src
touch index.js
npm init
```

Dans le code ci-dessus, nous avons créé deux nouveaux répertoires, nous y avons navigué, créé un fichier `index.js` et initialisé notre projet via [npm](https://www.npmjs.com/).

Vous serez invité à entrer plusieurs valeurs lors de l'initialisation d'un nouveau projet, celles-ci peuvent être laissées vides et mises à jour ultérieurement.

Une fois terminé, un fichier [package.json](https://alligator.io/nodejs/package-json/) est généré dans le répertoire `src`. Dans ce fichier, vous pouvez modifier les valeurs entrées lors de l'initialisation du projet.

Ensuite, nous installons toutes les **dépendances** dont nous aurons besoin :

```bash
npm i nodemon mongoose fastify fastify-swagger boom
```

Voici une brève description de ce que fait chaque package, citée depuis leurs sites respectifs :

[**nodemon**](https://github.com/remy/nodemon)

> nodemon est un outil qui aide à développer des applications basées sur node.js en redémarrant automatiquement l'application node lorsque des changements de fichiers dans le répertoire sont détectés.  
>   
> nodemon ne nécessite _aucun_ changement supplémentaire dans votre code ou méthode de développement. nodemon est un wrapper de remplacement pour `node`, pour utiliser `nodemon`, remplacez le mot `node` sur la ligne de commande lors de l'exécution de votre script.

Pour configurer **nodemon**, nous devons ajouter la ligne de code suivante à notre fichier `package.json`, dans l'objet scripts :

```json
"start": "./node_modules/nodemon/bin/nodemon.js ./src/index.js",
```

Notre fichier `package.json` devrait maintenant ressembler à ceci :

```json
{
  "name": "fastify-api",
  "version": "1.0.0",
  "description": "Des API REST ultra-rapides avec Node.js, MongoDB, Fastify et Swagger.",
  "main": "index.js",
  "scripts": {
  "start": "./node_modules/nodemon/bin/nodemon.js ./src/index.js",
  "test": "echo \"Error: no test specified\" && exit 1"
},
  "author": "Siegfried Grimbeek <siegfried.grimbeek@gmail.com> (www.siegfriedgrimbeek.co.za)",
  "license": "ISC",
  "dependencies": {
  "boom": "^7.2.2",
  "fastify": "^1.13.0",
  "fastify-swagger": "^0.15.3",
  "mongoose": "^5.3.14",
  "nodemon": "^1.18.7"
  }
}
```

[**mongoose**](https://mongoosejs.com/)

> Mongoose fournit une solution simple et basée sur un schéma pour modéliser les données de votre application. Il inclut la conversion de type intégrée, la validation, la construction de requêtes, les hooks de logique métier et plus encore, prêt à l'emploi.

[**fastify**](https://www.fastify.io/)

> Fastify est un framework web très axé sur la fourniture de la meilleure expérience développeur avec le moins de surcharge et une architecture de plugin puissante. Il est inspiré par Hapi et Express et, autant que nous le sachions, c'est l'un des frameworks web les plus rapides du moment.

[**fastify-swagger**](https://github.com/fastify/fastify-swagger)

> Générateur de documentation [Swagger](https://swagger.io/) pour Fastify. Il utilise les schémas que vous déclarez dans vos routes pour générer une documentation conforme à Swagger.

[**boom**](https://github.com/hapijs/boom)

> boom fournit un ensemble d'utilitaires pour retourner des erreurs HTTP.

### Configurer le serveur et créer la première route !

![Image](https://cdn-media-1.freecodecamp.org/images/1*rocnESJrNWsRGXMygLfDCQ.png)

Ajoutez le code suivant à votre fichier `index.js` :

```js
// Importer le framework et l'instancier
const fastify = require('fastify')({
  logger: true
})

// Déclarer une route
fastify.get('/', async (request, reply) => {
  return { hello: 'world' }
})

// Démarrer le serveur !
const start = async () => {
  try {
    await fastify.listen(3000)
    fastify.log.info(`server listening on ${fastify.server.address().port}`)
  } catch (err) {
    fastify.log.error(err)
    process.exit(1)
  }
}
start()
```

Nous importons le framework **Fastify**, déclarons notre première route et initialisons le serveur sur le `port 3000`. Le code est assez explicite, mais notez l'objet d'options passé lors de l'initialisation de **Fastify** :

```js
// Importer le framework fastify et l'instancier
const fastify = require('fastify')({
  logger: true
})
```

Le code ci-dessus active le logger intégré de **Fastify**, qui est désactivé par défaut.

Vous pouvez maintenant exécuter le code suivant dans votre répertoire `src` dans votre **terminal** :

```bash
npm start
```

Maintenant, lorsque vous naviguez vers [http://localhost:3000/](http://localhost:3000/), vous devriez voir l'objet `{hello:world}` retourné.

Nous reviendrons au fichier `index.js` plus tard, mais pour l'instant, passons à la configuration de notre base de données.

### Démarrer MongoDB et créer le modèle !

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ce0gUe0LbnhL7ebnDGTp5w.png)

Une fois que **MongoDB** est installé avec succès, vous pouvez ouvrir une nouvelle fenêtre de terminal et démarrer une instance **MongoDB** en exécutant ce qui suit :

```
mongod
```

Avec **MongoDB**, nous n'avons pas besoin de créer une base de données. Nous pouvons simplement spécifier un nom dans la configuration et dès que nous stockons des données, **MongoDB** créera cette base de données pour nous.

Ajoutez ce qui suit à votre fichier `index.js` :

```js
...

// Importer les modules externes
const mongoose = require('mongoose')

// Se connecter à la base de données
mongoose.connect('mongodb://localhost/mycargarage')
 .then(() => console.log('MongoDB connected…'))
 .catch(err => console.log(err))
 
...
```

Dans le code ci-dessus, nous importons **Mongoose** et nous connectons à notre base de données **MongoDB**. La base de données s'appelle `mycargarage` et si tout s'est bien passé, vous devriez maintenant voir `MongoDB connected...` dans votre terminal.

_Remarquez que vous n'avez pas eu à redémarrer l'application, grâce au package `Nodemon` que nous avons ajouté précédemment._

Maintenant que notre base de données est opérationnelle, nous pouvons créer notre premier modèle. Créez un nouveau dossier dans le répertoire `src` appelé `models`, et à l'intérieur, créez un nouveau fichier appelé `Car.js` et ajoutez le code suivant :

```js
// Dépendances externes
const mongoose = require('mongoose')

const carSchema = new mongoose.Schema({
  title: String,
  brand: String,
  price: String,
  age: Number,
  services: {
    type: Map,
    of: String
  }
})

module.exports = mongoose.model('Car', carSchema)
```

Le code ci-dessus déclare notre `carSchema` qui contient toutes les informations relatives à nos voitures. En plus des deux types de données évidents : `String` et `Number`, nous utilisons également une `Map` qui est relativement nouvelle dans **Mongoose** et vous pouvez en lire plus à ce sujet [ici](https://thecodebarbarian.com/whats-new-in-mongoose-5.1-map-support.html). Nous exportons ensuite notre `carSchema` pour qu'elle soit utilisée dans notre application.

Nous pourrions procéder à la configuration de nos routes, contrôleurs et configuration dans le fichier `index.js`, mais une partie de ce tutoriel consiste à démontrer une base de code durable. Par conséquent, chaque composant aura son propre dossier.

### Créer le contrôleur de voiture

Pour commencer à créer les contrôleurs, nous créons un dossier dans le répertoire `src` appelé `controllers`, et dans ce dossier, nous créons un fichier `carController.js` :

```js
// Dépendances externes
const boom = require('boom')

// Obtenir les modèles de données
const Car = require('../models/Car')

// Obtenir toutes les voitures
exports.getCars = async (req, reply) => {
  try {
    const cars = await Car.find()
    return cars
  } catch (err) {
    throw boom.boomify(err)
  }
}

// Obtenir une seule voiture par ID
exports.getSingleCar = async (req, reply) => {
  try {
    const id = req.params.id
    const car = await Car.findById(id)
    return car
  } catch (err) {
    throw boom.boomify(err)
  }
}

// Ajouter une nouvelle voiture
exports.addCar = async (req, reply) => {
  try {
    const car = new Car(req.body)
    return car.save()
  } catch (err) {
    throw boom.boomify(err)
  }
}

// Mettre à jour une voiture existante
exports.updateCar = async (req, reply) => {
  try {
    const id = req.params.id
    const car = req.body
    const { ...updateData } = car
    const update = await Car.findByIdAndUpdate(id, updateData, { new: true })
    return update
  } catch (err) {
    throw boom.boomify(err)
  }
}

// Supprimer une voiture
exports.deleteCar = async (req, reply) => {
  try {
    const id = req.params.id
    const car = await Car.findByIdAndRemove(id)
    return car
  } catch (err) {
    throw boom.boomify(err)
  }
}
```

Ce qui précède peut sembler un peu difficile à assimiler, mais c'est en fait très simple.

* Nous importons **boom** pour gérer nos erreurs : `boom.boomify(err)`.
* Nous exportons chacune de nos fonctions que nous utiliserons dans notre route.
* Chaque fonction est une fonction **async** qui peut contenir une expression **await** qui pause l'exécution de la fonction **async** et attend la résolution de la promesse passée, puis reprend l'exécution de la fonction **async** et retourne la valeur résolue. [En savoir plus ici.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
* Chaque fonction est enveloppée dans une instruction try / catch. [En savoir plus ici.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
* Chaque fonction prend deux paramètres : `req` (la requête) et `reply` (la réponse). Dans notre tutoriel, nous n'utilisons que le paramètre de requête. Nous l'utiliserons pour accéder au corps de la requête et aux paramètres de la requête, ce qui nous permettra de traiter les données. [En savoir plus ici.](https://www.fastify.io/docs/latest/Reply/)
* Notez le code à la ligne 31 :  
`const car = new Car({ …req.body })`   
Cela utilise l'opérateur de propagation **JavaScript**. [En savoir plus ici.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
* Notez le code à la ligne 42 :  
`const { …updateData } = car`  
Cela utilise la destructuration **JavaScript** en conjonction avec l'opérateur de propagation. [En savoir plus ici.](https://codeburst.io/use-es2015-object-rest-operator-to-omit-properties-38a3ecffe90)

Autre que cela, nous utilisons certaines fonctionnalités standard de **Mongoose** utilisées pour manipuler notre base de données.

Vous brûlez probablement d'envie de lancer votre API et de faire un test de bon sens, mais avant de le faire, nous devons simplement connecter le **contrôleur** aux **routes** et enfin connecter les **routes** à l'application.

#### Créer et importer les routes

Une fois de plus, nous pouvons commencer par créer un dossier dans le répertoire racine de notre projet, mais cette fois, il s'appelle `routes`. Dans le dossier, nous créons un fichier `index.js` avec le code suivant :

```js
// Importer nos contrôleurs
const carController = require('../controllers/carController')

const routes = [
  {
    method: 'GET',
    url: '/api/cars',
    handler: carController.getCars
  },
  {
    method: 'GET',
    url: '/api/cars/:id',
    handler: carController.getSingleCar
  },
  {
    method: 'POST',
    url: '/api/cars',
    handler: carController.addCar,
    schema: documentation.addCarSchema
  },
  {
    method: 'PUT',
    url: '/api/cars/:id',
    handler: carController.updateCar
  },
  {
    method: 'DELETE',
    url: '/api/cars/:id',
    handler: carController.deleteCar
  }
]

module.exports = routes
```

Ici, nous importons notre **contrôleur** et attribuons chacune des fonctions que nous avons créées dans notre contrôleur à nos routes.

Comme vous pouvez le voir, chaque route se compose d'une méthode, d'une URL et d'un gestionnaire, indiquant à l'application quelle fonction utiliser lorsque l'une des routes est accessible.

Le `:id` suivant certaines des routes est un moyen courant de passer des paramètres aux routes, et cela nous permettra d'accéder à l'**id** comme suit :

`[http://127.0.0.1:3000/api/cars/5bfe30b46fe410e1cfff2323](http://127.0.0.1:3000/api/cars/5bfe30b46fe410e1cfff2323)`

#### Mettre tout ensemble et tester notre API

Maintenant que nous avons construit la plupart de nos parties, nous devons simplement les connecter toutes ensemble pour commencer à servir des données via notre **API**. Tout d'abord, nous devons importer nos **routes** que nous avons créées en ajoutant la ligne de code suivante à notre fichier `index.js` principal :

```js
const routes = require('./routes')
```

Nous devons ensuite parcourir notre tableau de routes pour les initialiser avec **Fastify**. Nous pouvons faire cela avec le code suivant, qui doit également être ajouté au fichier `index.js` principal :

```js
routes.forEach((route, index) => {
 fastify.route(route)
})
```

Maintenant, nous sommes prêts à commencer les tests !

Le meilleur outil pour le travail est [Postman](https://www.getpostman.com/), que nous utiliserons pour tester toutes nos routes. Nous enverrons nos données sous forme d'objets bruts dans le corps de la requête et sous forme de paramètres.

Trouver toutes les voitures :

![Image](https://cdn-media-1.freecodecamp.org/images/1*YoxRE054Q7qgrAxaCgrzLw.png)

Trouver une seule voiture :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1T4C1-LmgWv0S5W-bgk4wQ.png)

Ajouter une nouvelle voiture :

![Image](https://cdn-media-1.freecodecamp.org/images/1*UYqA6GVUv_dcKArTRJ_NPA.png)

** Les services semblent être vides, mais les informations sont en fait persistées dans la base de données.

Mettre à jour une voiture :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BcZdrz0X3dyfDfOhkDFwFg.png)

Supprimer une voiture :

![Image](https://cdn-media-1.freecodecamp.org/images/1*9PwntcmeC1wfYMqo3raXdQ.png)

Nous avons maintenant une API entièrement fonctionnelle — mais qu'en est-il de la documentation ? C'est là que **Swagger** est vraiment pratique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7iaXjYojG6kWxLTZaW1x4Q.png)

#### Ajouter Swagger et conclure.

Maintenant, nous allons créer notre dernier dossier appelé **config**. À l'intérieur, nous créerons un fichier appelé `swagger.js` avec le code suivant :

```js
exports.options = {
  routePrefix: '/documentation',
  exposeRoute: true,
  swagger: {
    info: {
      title: 'Fastify API',
      description: 'Construire une API REST ultra-rapide avec Node.js, MongoDB, Fastify et Swagger',
      version: '1.0.0'
    },
    externalDocs: {
      url: 'https://swagger.io',
      description: 'Trouvez plus d\'infos ici'
    },
    host: 'localhost',
    schemes: ['http'],
    consumes: ['application/json'],
    produces: ['application/json']
  }
}
```

Le code ci-dessus est un objet avec les options que nous allons passer à notre plugin **fastify-swagger**. Pour ce faire, nous devons ajouter ce qui suit à notre fichier `index.js` :

```js
// Importer les options Swagger
const swagger = require('./config/swagger')

// Enregistrer Swagger
fastify.register(require('fastify-swagger'), swagger.options)
```

Ensuite, nous devons ajouter la ligne suivante après avoir initialisé notre serveur **Fastify** :

```js
...
await fastify.listen(3000)
fastify.swagger()
fastify.log.info(`listening on ${fastify.server.address().port}`)
...
```

Et c'est tout ! Si vous naviguez maintenant vers [http://localhost:3000/documentation](http://localhost:3000/documentation), vous devriez voir ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HV-5eImCMs7LtiLodTz7CQ.png)

C'est aussi simple que cela ! Vous avez maintenant une documentation API auto-mise à jour qui évoluera avec votre API. Vous pouvez facilement ajouter des informations supplémentaires à vos routes, voir plus [ici](https://github.com/fastify/fastify-swagger).

#### Qu'est-ce qui suit ?

Maintenant que nous avons une API de base en place, les possibilités sont illimitées. Elle peut être utilisée comme base pour n'importe quelle application imaginable.

Dans le prochain tutoriel, nous intégrerons **GraphQL** et intégrerons éventuellement le frontend avec **Vue.js** également !