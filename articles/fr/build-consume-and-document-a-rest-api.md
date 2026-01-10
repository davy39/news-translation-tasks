---
title: Le manuel de l'API REST – Comment construire, tester, consommer et documenter
  les API REST
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2023-04-27T13:55:17.000Z'
originalURL: https://freecodecamp.org/news/build-consume-and-document-a-rest-api
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pavan-trikutam-71CjSSB83Wo-unsplash.jpg
tags:
- name: REST API
  slug: rest-api
seo_title: Le manuel de l'API REST – Comment construire, tester, consommer et documenter
  les API REST
seo_desc: 'Hi everyone! In this tutorial we''re going to take a deep dive into REST
  APIs.

  I recently wrote this article where I explained the main differences between common
  API types nowadays. And this tutorial aims to show you an example of how you can
  fully i...'
---

Bonjour à tous ! Dans ce tutoriel, nous allons plonger en profondeur dans les API REST.

J'ai récemment écrit [cet article](https://www.freecodecamp.org/news/rest-vs-graphql-apis/) où j'ai expliqué les principales différences entre les types d'API courants de nos jours. Et ce tutoriel vise à vous montrer un exemple de la manière dont vous pouvez implémenter pleinement une API REST.

Nous aborderons la configuration de base et l'architecture avec Node et Express, les tests unitaires avec Supertest, en voyant comment nous pouvons consommer l'API à partir d'une application front-end React et enfin documenter l'API en utilisant des outils tels que Swagger.

Gardez à l'esprit que nous n'irons pas trop en profondeur dans le fonctionnement de chaque technologie. L'objectif ici est de vous donner un aperçu général du fonctionnement d'une API REST, de la manière dont ses éléments interagissent et de ce à quoi une implémentation complète pourrait ressembler.

C'est parti !

# Table des matières

* [Qu'est-ce que REST ?](#heading-quest-ce-que-rest)
    
* [Comment construire une API REST avec Node et Express](#heading-comment-construire-une-api-rest-avec-node-et-express)
    
* [Comment tester une API REST avec Supertest](#heading-comment-tester-une-api-rest-avec-supertest)
    
* [Comment consommer une API REST sur une application front-end React](#heading-comment-consommer-une-api-rest-sur-une-application-front-end-react)
    
* [Comment documenter une API REST avec Swagger](#heading-comment-documenter-une-api-rest-avec-swagger)
    
* [Conclusion](#heading-conclusion)
    

# Qu'est-ce que REST ?

Le transfert d'état représentationnel (REST) est un style architectural largement utilisé pour construire des services web et des API.

Les API RESTful sont conçues pour être simples, évolutives et flexibles. Elles sont souvent utilisées dans les applications web et mobiles, ainsi que dans les architectures d'Internet des objets (IoT) et de microservices.

**Caractéristiques principales :**

1. **Sans état :** Les API REST sont sans état, ce qui signifie que chaque requête contient toutes les informations nécessaires pour la traiter. Cela facilite la mise à l'échelle de l'API et améliore les performances en réduisant le besoin de stocker et de gérer les données de session sur le serveur.
    
2. **Basé sur les ressources :** Les API REST sont basées sur les ressources, ce qui signifie que chaque ressource est identifiée par un URI (Uniform Resource Identifier) unique et peut être accessible en utilisant des méthodes HTTP standard telles que GET, POST, PUT et DELETE.
    
3. **Interface uniforme :** Les API REST ont une interface uniforme qui permet aux clients d'interagir avec les ressources en utilisant un ensemble standardisé de méthodes et de formats de réponse. Cela facilite le développement et la maintenance des API pour les développeurs, et leur consommation pour les clients.
    
4. **Mise en cache :** Les API REST sont mises en cache, ce qui signifie que les réponses peuvent être mises en cache pour améliorer les performances et réduire le trafic réseau.
    
5. **Système en couches :** Les API REST sont conçues pour être en couches, ce qui signifie que des intermédiaires tels que des proxys et des passerelles peuvent être ajoutés entre le client et le serveur sans affecter le système global.
    

**Avantages** des API REST\*\*:\*\*

* **Facile à apprendre et à utiliser :** Les API REST sont relativement simples et faciles à apprendre par rapport à d'autres API.
    
* **Évolutivité :** La nature sans état des API REST les rend hautement évolutives et efficaces.
    
* **Flexibilité :** Les API REST sont flexibles et peuvent être utilisées pour construire une large gamme d'applications et de systèmes.
    
* **Large support :** Les API REST sont largement supportées par les outils et frameworks de développement, ce qui facilite leur intégration dans les systèmes existants.
    

**Inconvénients** des API REST\*\*:\*\*

* **Manque de standards :** Le manque de standards stricts pour les API REST peut conduire à des incohérences et à des problèmes d'interopérabilité.
    
* **Fonctionnalités limitées :** Les API REST sont conçues pour gérer des requêtes et des réponses simples et peuvent ne pas être adaptées à des cas d'utilisation plus complexes.
    
* **Problèmes de sécurité :** Les API REST peuvent être vulnérables aux attaques de sécurité telles que le cross-site scripting (XSS) et la contrefaçon de requête inter-sites (CSRF) si elles ne sont pas implémentées correctement.
    

**Les API REST sont les meilleures pour :**\*\*\*\*

* Les API REST sont bien adaptées pour construire des applications web et mobiles, ainsi que des architectures de microservices et des systèmes IoT.
    
* Elles sont particulièrement utiles dans les situations où l'évolutivité et la flexibilité sont importantes, et où les développeurs doivent s'intégrer avec des systèmes et des technologies existants.
    

En résumé, les API REST sont un style architectural populaire et largement utilisé pour construire des services web et des API. Elles sont simples, évolutives et flexibles, et peuvent être utilisées pour construire une large gamme d'applications et de systèmes.

Bien qu'il y ait certaines limitations et préoccupations avec les API REST, elles restent une option populaire et efficace pour construire des API dans de nombreuses industries et secteurs différents.

# Comment construire une API REST avec Node et Express

## Nos outils

[**Node.js**](https://nodejs.org/) est un environnement d'exécution JavaScript open-source, multiplateforme, côté serveur qui permet aux développeurs d'exécuter du code JavaScript en dehors d'un navigateur web. Il a été créé par Ryan Dahl en 2009 et est depuis devenu un choix populaire pour construire des applications web, des API et des serveurs.

Node.js fournit un modèle d'E/S piloté par événements et non bloquant qui le rend léger et efficace, lui permettant de gérer de grandes quantités de données avec des performances élevées. Il dispose également d'une grande et active communauté, avec de nombreuses bibliothèques et modules disponibles pour aider les développeurs à construire leurs applications plus rapidement et plus facilement.

[**Express.js**](https://expressjs.com/) est un framework populaire d'application web pour Node.js, qui est utilisé pour construire des applications web et des API. Il fournit un ensemble de fonctionnalités et d'outils pour construire des serveurs web, gérer les requêtes et réponses HTTP, router les requêtes vers des gestionnaires spécifiques, gérer les middlewares, et bien plus encore.

Express est connu pour sa simplicité, sa flexibilité et son évolutivité, ce qui en fait un choix populaire pour les développeurs construisant des applications web avec Node.js.

Certaines des fonctionnalités et avantages clés d'Express.js incluent :

* **Minimaliste et flexible :** Express.js fournit une structure minimaliste et flexible qui permet aux développeurs de construire des applications comme ils le souhaitent.
    
* **Routing :** Express.js facilite la définition de routes pour gérer les requêtes HTTP et les mapper à des fonctions ou gestionnaires spécifiques.
    
* **Middleware :** Express.js permet aux développeurs de définir des fonctions middleware qui peuvent être utilisées pour gérer des tâches courantes telles que l'authentification, la journalisation, la gestion des erreurs, et plus encore.
    
* **API robuste :** Express.js fournit une API robuste pour gérer les requêtes et réponses HTTP, permettant aux développeurs de construire des applications web haute performance.
    

## Notre architecture

Pour ce projet, nous suivrons une architecture en couches dans notre base de code. L'architecture en couches consiste à diviser les préoccupations et les responsabilités en différents dossiers et fichiers, et à permettre une communication directe uniquement entre certains dossiers et fichiers.

La question de savoir combien de couches votre projet doit avoir, quels noms chaque couche doit avoir, et quelles actions elle doit gérer est une question de discussion. Alors voyons ce que je pense être une bonne approche pour notre exemple.

Notre application aura cinq couches différentes, qui seront ordonnées de cette manière :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-110.png align="left")

*Couches de l'application*

* La couche application aura la configuration de base de notre serveur et la connexion à nos routes (la couche suivante).
    
* La couche routes aura la définition de toutes nos routes et la connexion aux contrôleurs (la couche suivante).
    
* La couche contrôleurs aura la logique réelle que nous voulons effectuer dans chacun de nos endpoints et la connexion à la couche modèle (la couche suivante, vous comprenez l'idée...)
    
* La couche modèle contiendra la logique pour interagir avec notre base de données simulée.
    
* Enfin, la couche persistance est l'endroit où se trouvera notre base de données.
    

Une chose importante à garder à l'esprit est que dans ces types d'architectures, **il y a un flux de communication défini** entre les couches qui doit être suivi pour que cela ait du sens.

Cela signifie qu'une requête doit d'abord passer par la première couche, puis la deuxième, puis la troisième et ainsi de suite. Aucune requête ne doit sauter des couches car cela perturberait la logique de l'architecture et les avantages d'organisation et de modularité qu'elle nous offre.

> Si vous souhaitez connaître d'autres options d'architecture d'API, je vous recommande [cet article sur l'architecture logicielle](https://www.freecodecamp.org/news/an-introduction-to-software-architecture-patterns/) que j'ai écrit il y a quelque temps.

## Le code

Avant de passer au code, mentionnons ce que nous allons réellement construire. Nous allons construire une API pour une entreprise de refuge pour animaux. Ce refuge pour animaux doit enregistrer les animaux qui séjournent dans le refuge, et pour cela nous effectuerons des opérations CRUD de base (créer, lire, mettre à jour et supprimer).

Maintenant, oui, commençons. Créez un nouveau répertoire, allez-y et démarrez un nouveau projet Node en exécutant `npm init -y`.

Ensuite, installez Express en exécutant `npm i express` et installez nodemon comme dépendance de développement en exécutant `npm i -D nodemon` ([Nodemon](https://nodemon.io/) est un outil que nous utiliserons pour faire fonctionner notre serveur et le tester). Enfin, exécutez également `npm i cors`, que nous utiliserons pour pouvoir tester notre serveur localement.

### App.js

Super, maintenant créez un fichier `app.js` et déposez ce code dedans :

```javascript

import express from 'express'
import cors from 'cors'

import petRoutes from './pets/routes/pets.routes.js'

const app = express()
const port = 3000

/* Global middlewares */
app.use(cors())
app.use(express.json())

/* Routes */
app.use('/pets', petRoutes)

/* Server setup */
if (process.env.NODE_ENV !== 'test') {
    app.listen(port, () => console.log(`\u26a1\ufe0f[server]: Server is running at https://localhost:${port}`))
}

export default app
```

Ceci serait la **couche application** de notre projet.

Ici, nous configurons essentiellement notre serveur et déclarons que toute requête qui atteint la direction `/pets` doit utiliser les routes (endpoints) que nous avons déclarées dans le répertoire `./pets/routes/pets.routes.js`.

Ensuite, allez-y et créez cette structure de dossiers dans votre projet :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-246.png align="left")

*Structure des dossiers*

### Routes

Allez dans le dossier des routes, créez un fichier appelé `pets.routes.js`, et déposez ce code dedans :

```javascript
import express from "express";
import {
  listPets,
  getPet,
  editPet,
  addPet,
  deletePet,
} from "../controllers/pets.controllers.js";

const router = express.Router();

router.get("/", listPets);

router.get("/:id", getPet);

router.put("/:id", editPet);

router.post("/", addPet);

router.delete("/:id", deletePet);

export default router;
```

Dans ce fichier, nous initialisons un routeur (la chose qui traite notre requête et les dirige en conséquence selon l'URL de l'endpoint) et configurons chacun de nos endpoints.

Voyez que pour chaque endpoint, nous déclarons la méthode HTTP correspondante (`get`, `put`, etc.) et la fonction correspondante que cet endpoint déclenchera (`listPets`, `getPet`, etc.). Chaque nom de fonction est assez explicite, donc nous pouvons facilement savoir ce que fait chaque endpoint sans avoir besoin de voir plus de code. ;)

Enfin, nous déclarons également quel endpoint recevra les paramètres d'URL dans les requêtes comme ceci : `router.get("/:id", getPet);` Ici, nous disons que nous recevrons l'`id` de l'animal comme paramètre d'URL.

### Contrôleurs

Maintenant, allez dans le dossier des contrôleurs, créez un fichier `pets.controllers.js` et mettez ce code dedans :

```javascript
import { getItem, listItems, editItem, addItem, deleteItem } from '../models/pets.models.js'

export const getPet = (req, res) => {
    try {
        const resp = getItem(parseInt(req.params.id))
        res.status(200).json(resp)

    } catch (err) {
        res.status(500).send(err)
    }
}

export const listPets = (req, res) => {
    try {
        const resp = listItems()
        res.status(200).json(resp)

    } catch (err) {
        res.status(500).send(err)
    }
}

export const editPet = (req, res) => {
    try {
        const resp = editItem(parseInt(req.params.id), req.body)
        res.status(200).json(resp)

    } catch (err) {
        res.status(500).send(err)
    }
}

export const addPet = (req, res) => {
    try {
        const resp = addItem(req.body)
        res.status(200).json(resp)

    } catch (err) {
        res.status(500).send(err)
    }
}

export const deletePet = (req, res) => {
    try {
        const resp = deleteItem(parseInt(req.params.id))
        res.status(200).json(resp)

    } catch (err) {
        res.status(500).send(err)
    }
}
```

Les contrôleurs sont les fonctions que chaque requête d'endpoint déclenchera. Comme vous pouvez le voir, ils reçoivent en paramètres les objets de requête et de réponse. Dans l'objet de requête, nous pouvons lire des choses telles que les paramètres d'URL ou de corps, et nous utiliserons l'objet de réponse pour envoyer notre réponse après avoir effectué le calcul correspondant.

Chaque contrôleur appelle une fonction spécifique définie dans nos modèles.

### Modèles

Maintenant, allez dans le dossier des modèles et créez un fichier `pets.models.js` avec ce code dedans :

```javascript
import db from '../../db/db.js'

export const getItem = id => {
    try {
        const pet = db?.pets?.filter(pet => pet?.id === id)[0]
        return pet
    } catch (err) {
        console.log('Error', err)
    }
}

export const listItems = () => {
    try {
        return db?.pets
    } catch (err) {
        console.log('Error', err)
    }
}

export const editItem = (id, data) => {
    try {
        const index = db.pets.findIndex(pet => pet.id === id)

        if (index === -1) throw new Error('Pet not found')
        else {
            db.pets[index] = data
            return db.pets[index]
        }        
    } catch (err) {
        console.log('Error', err)
    }
}

export const addItem = data => {
    try {  
        const newPet = { id: db.pets.length + 1, ...data }
        db.pets.push(newPet)
        return newPet

    } catch (err) {
        console.log('Error', err)
    }
}

export const deleteItem = id => {
    try {
        // delete item from db
        const index = db.pets.findIndex(pet => pet.id === id)

        if (index === -1) throw new Error('Pet not found')
        else {
            db.pets.splice(index, 1)
            return db.pets
        }
    } catch (error) {
        
    }
}
```

Ce sont les fonctions responsables de l'interaction avec notre couche de données (base de données) et du retour des informations correspondantes à nos contrôleurs.

### Base de données

Nous n'utiliserons pas de base de données réelle pour cet exemple. Au lieu de cela, nous utiliserons simplement un tableau simple qui fonctionnera très bien pour les besoins de l'exemple, bien que nos données seront bien sûr réinitialisées chaque fois que notre serveur le fera.

À la racine de notre projet, créez un dossier `db` et un fichier `db.js` avec ce code dedans :

```javascript
const db = {
    pets: [
        {
            id: 1,
            name: 'Rex',
            type: 'dog',
            age: 3,
            breed: 'labrador',
        },
        {
            id: 2,
            name: 'Fido',
            type: 'dog',
            age: 1,
            breed: 'poodle',
        },
        {
            id: 3,
            name: 'Mittens',
            type: 'cat',
            age: 2,
            breed: 'tabby',
        },
    ]
}

export default db
```

Comme vous pouvez le voir, notre objet `db` contient une propriété `pets` dont la valeur est un tableau d'objets, chaque objet étant un animal. Pour chaque animal, nous stockons un id, un nom, un type, un âge et une race.

Maintenant, allez dans votre terminal et exécutez `nodemon app.js`. Vous devriez voir ce message confirmant que votre serveur est en vie : `\u26a1\ufe0f[server]: Server is running at [https://localhost:3000](https://localhost:3000)`.

# Comment tester une API REST avec Supertest

Maintenant que notre serveur est en marche, implémentons une simple suite de tests pour vérifier si chacun de nos endpoints se comporte comme prévu.

Si vous n'êtes pas familier avec les tests automatisés, je vous recommande de lire [cet article d'introduction que j'ai écrit il y a quelque temps](https://www.freecodecamp.org/news/test-a-react-app-with-jest-testing-library-and-cypress/).

## Nos outils

[**SuperTest**](https://www.npmjs.com/package/supertest) est une bibliothèque JavaScript utilisée pour tester les serveurs HTTP ou les applications web qui font des requêtes HTTP. Elle fournit une abstraction de haut niveau pour tester le HTTP, permettant aux développeurs d'envoyer des requêtes HTTP et de faire des assertions sur les réponses reçues, ce qui facilite l'écriture de tests automatisés pour les applications web.

SuperTest fonctionne avec n'importe quel framework de test JavaScript, tel que [Mocha](https://mochajs.org/) ou [Jest](https://jestjs.io/), et peut être utilisé avec n'importe quel serveur HTTP ou framework d'application web, tel qu'Express.

SuperTest est construit sur la bibliothèque de test populaire Mocha, et utilise la bibliothèque d'assertion [Chai](https://www.chaijs.com/) pour faire des assertions sur les réponses reçues. Il fournit une API facile à utiliser pour faire des requêtes HTTP, y compris le support pour l'authentification, les en-têtes et les corps de requête.

SuperTest permet également aux développeurs de tester l'ensemble du cycle requête/réponse, y compris le middleware et la gestion des erreurs, ce qui en fait un outil puissant pour tester les applications web.

Dans l'ensemble, SuperTest est un outil précieux pour les développeurs qui souhaitent écrire des tests automatisés pour leurs applications web. Il aide à garantir que leurs applications fonctionnent correctement et que les modifications qu'ils apportent à la base de code n'introduisent pas de nouveaux bugs ou problèmes.

## Le code

Tout d'abord, nous devrons installer quelques dépendances. Pour économiser les commandes du terminal, allez dans votre fichier `package.json` et remplacez votre section `devDependencies` par celle-ci. Ensuite, exécutez `npm install`

```javascript
  "devDependencies": {
    "@babel/core": "^7.21.4",
    "@babel/preset-env": "^7.21.4",
    "babel-jest": "^29.5.0",
    "jest": "^29.5.0",
    "jest-babel": "^1.0.1",
    "nodemon": "^2.0.22",
    "supertest": "^6.3.3"
  }
```

Ici, nous installons les bibliothèques `supertest` et `jest`, dont nous avons besoin pour exécuter nos tests, ainsi que quelques éléments `babel` dont nous avons besoin pour que notre projet identifie correctement les fichiers de test.

Toujours dans votre `package.json`, ajoutez ce script :

```javascript
  "scripts": {
    "test": "jest"
  },
```

Pour terminer avec le code standard, à la racine de votre projet, créez un fichier `babel.config.cjs` et déposez ce code dedans :

```javascript
//babel.config.cjs
module.exports = {
    presets: [
      [
        '@babel/preset-env',
        {
          targets: {
            node: 'current',
          },
        },
      ],
    ],
  };
```

Maintenant, écrivons quelques tests réels ! Dans votre dossier de routes, créez un fichier `pets.test.js` avec ce code dedans :

```javascript
import supertest from 'supertest' // Import supertest
import server from '../../app' // Import the server object
const requestWithSupertest = supertest(server) // We will use this function to mock HTTP requests

describe('GET "/"', () => {
    test('GET "/" returns all pets', async () => {
        const res = await requestWithSupertest.get('/pets')
        expect(res.status).toEqual(200)
        expect(res.type).toEqual(expect.stringContaining('json'))
        expect(res.body).toEqual([
            {
                id: 1,
                name: 'Rex',
                type: 'dog',
                age: 3,
                breed: 'labrador',
            },
            {
                id: 2,
                name: 'Fido',
                type: 'dog',
                age: 1,
                breed: 'poodle',
            },
            {
                id: 3,
                name: 'Mittens',
                type: 'cat',
                age: 2,
                breed: 'tabby',
            },
        ])
    })
})

describe('GET "/:id"', () => {
    test('GET "/:id" returns given pet', async () => {
        const res = await requestWithSupertest.get('/pets/1')
        expect(res.status).toEqual(200)
        expect(res.type).toEqual(expect.stringContaining('json'))
        expect(res.body).toEqual(
            {
                id: 1,
                name: 'Rex',
                type: 'dog',
                age: 3,
                breed: 'labrador',
            }
        )
    })
})

describe('PUT "/:id"', () => {
    test('PUT "/:id" updates pet and returns it', async () => {
        const res = await requestWithSupertest.put('/pets/1').send({
            id: 1,
            name: 'Rexo',
            type: 'dogo',
            age: 4,
            breed: 'doberman'
        })
        expect(res.status).toEqual(200)
        expect(res.type).toEqual(expect.stringContaining('json'))
        expect(res.body).toEqual({
            id: 1,
            name: 'Rexo',
            type: 'dogo',
            age: 4,
            breed: 'doberman'
        })
    })
})

describe('POST "/"', () => {
    test('POST "/" adds new pet and returns the added item', async () => {
        const res = await requestWithSupertest.post('/pets').send({
            name: 'Salame',
            type: 'cat',
            age: 6,
            breed: 'pinky'
        })
        expect(res.status).toEqual(200)
        expect(res.type).toEqual(expect.stringContaining('json'))
        expect(res.body).toEqual({
            id: 4,
            name: 'Salame',
            type: 'cat',
            age: 6,
            breed: 'pinky'
        })
    })
})

describe('DELETE "/:id"', () => {
    test('DELETE "/:id" deletes given pet and returns updated list', async () => {
        const res = await requestWithSupertest.delete('/pets/2')
        expect(res.status).toEqual(200)
        expect(res.type).toEqual(expect.stringContaining('json'))
        expect(res.body).toEqual([
            {
                id: 1,
                name: 'Rexo',
                type: 'dogo',
                age: 4,
                breed: 'doberman'
            },
            {
                id: 3,
                name: 'Mittens',
                type: 'cat',
                age: 2,
                breed: 'tabby',
            },
            {
                id: 4,
                name: 'Salame',
                type: 'cat',
                age: 6,
                breed: 'pinky'
            }
        ])
    })
})
```

Pour chaque endpoint, les tests envoient des requêtes HTTP et vérifient les réponses pour trois choses : le code de statut HTTP, le type de réponse (qui doit être JSON), et le corps de la réponse (qui doit correspondre au format JSON attendu).

* Le premier test envoie une requête GET à l'endpoint /pets et s'attend à ce que l'API retourne un tableau d'animaux au format JSON.
    
* Le deuxième test envoie une requête GET à l'endpoint /pets/:id et s'attend à ce que l'API retourne l'animal avec l'ID spécifié au format JSON.
    
* Le troisième test envoie une requête PUT à l'endpoint /pets/:id et s'attend à ce que l'API mette à jour l'animal avec l'ID spécifié et retourne l'animal mis à jour au format JSON.
    
* Le quatrième test envoie une requête POST à l'endpoint /pets et s'attend à ce que l'API ajoute un nouvel animal et retourne l'animal ajouté au format JSON.
    
* Enfin, le cinquième test envoie une requête DELETE à l'endpoint /pets/:id et s'attend à ce que l'API supprime l'animal avec l'ID spécifié et retourne la liste mise à jour des animaux au format JSON.
    

Chaque test vérifie si le code de statut HTTP attendu, le type de réponse et le corps de la réponse sont retournés. Si l'une de ces attentes n'est pas remplie, le test échoue et fournit un message d'erreur.

Ces tests sont importants pour garantir que l'API fonctionne correctement et de manière cohérente sur différentes requêtes HTTP et endpoints. Les tests peuvent être exécutés automatiquement, ce qui facilite la détection de tout problème ou régression dans la fonctionnalité de l'API.

Maintenant, allez dans votre terminal, exécutez `npm test`, et vous devriez voir tous vos tests réussir :

```javascript
> restapi@1.0.0 test
> jest

 PASS  pets/routes/pets.test.js
  GET "/"
    \u2713 GET "/" returns all pets (25 ms)
  GET "/:id"
    \u2713 GET "/:id" returns given pet (4 ms)
  PUT "/:id"
    \u2713 PUT "/:id" updates pet and returns it (15 ms)
  POST "/"
    \u2713 POST "/" adds new pet and returns the added item (3 ms)
  DELETE "/:id"
    \u2713 DELETE "/:id" deletes given pet and returns updated list (3 ms)

Test Suites: 1 passed, 1 total
Tests:       5 passed, 5 total
Snapshots:   0 total
Time:        1.611 s
Ran all test suites.
```

# Comment consommer une API REST sur une application front-end React

Maintenant, nous savons que notre serveur est en marche et que nos endpoints se comportent comme prévu. Voyons un exemple plus réaliste de la manière dont notre API pourrait être consommée par une application front-end.

Pour cet exemple, nous utiliserons une application React, et deux outils différents pour envoyer et traiter nos requêtes : l'API Fetch et la bibliothèque Axios.

## Nos outils

[**React**](https://react.dev/) est une bibliothèque JavaScript populaire pour construire des interfaces utilisateur. Elle permet aux développeurs de créer des composants d'interface utilisateur réutilisables et de les mettre à jour et de les rendre efficacement en réponse aux changements d'état de l'application.

L'**API Fetch** est une API de navigateur moderne qui permet aux développeurs de faire des requêtes HTTP asynchrones à partir de code JavaScript côté client. Elle fournit une interface simple pour récupérer des ressources à travers le réseau, et supporte une variété de types de requêtes et de réponses.

[**Axios**](https://axios-http.com/docs/intro) est une bibliothèque cliente HTTP populaire pour JavaScript. Elle fournit une API simple et intuitive pour faire des requêtes HTTP, et supporte une large gamme de fonctionnalités, y compris l'interception des requêtes et des réponses, les transformations automatiques pour les données de requête et de réponse, et la capacité d'annuler les requêtes. Elle peut être utilisée à la fois dans le navigateur et sur le serveur, et est souvent utilisée en conjonction avec des applications React.

## Le code

Créons notre application React en exécutant `yarn create vite` et en suivant les invites du terminal. Une fois cela fait, exécutez `yarn add axios` et `yarn add react-router-dom` (que nous utiliserons pour configurer le routage de base dans notre application).

### App.jsx

Mettez ce code dans votre fichier `App.jsx` :

```javascript
import { Suspense, lazy, useState } from 'react'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import './App.css'

const PetList = lazy(() => import ('./pages/PetList'))
const PetDetail = lazy(() => import ('./pages/PetDetail'))
const EditPet = lazy(() => import ('./pages/EditPet'))
const AddPet = lazy(() => import ('./pages/AddPet'))

function App() {

  const [petToEdit, setPetToEdit] = useState(null)

  return (
    <div className="App">
      <Router>
        <h1>Pet shelter</h1>

        <Link to='/add'>
          <button>Add new pet</button>
      </Link>

        <Routes>
          <Route path='/' element={<Suspense fallback={<></>}><PetList /></Suspense>}/>

          <Route path='/:petId' element={<Suspense fallback={<></>}><PetDetail setPetToEdit={setPetToEdit} /></Suspense>}/>

          <Route path='/:petId/edit' element={<Suspense fallback={<></>}><EditPet petToEdit={petToEdit} /></Suspense>}/>

          <Route path='/add' element={<Suspense fallback={<></>}><AddPet /></Suspense>}/>
        </Routes>

      </Router>
    </div>
  )
}

export default App
```

Ici, nous définissons simplement nos routes. Nous aurons 4 routes principales dans notre application, chacune correspondant à une vue différente :

* Une pour voir la liste complète des animaux.
    
* Une pour voir le détail d'un seul animal.
    
* Une pour modifier un seul animal.
    
* Une pour ajouter un nouvel animal à la liste.
    

En outre, nous avons un bouton pour ajouter un nouvel animal et un état qui stockera les informations de l'animal que nous voulons modifier.

Ensuite, créez un répertoire `pages` avec ces fichiers dedans :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-281.png align="left")

*Structure des dossiers*

### PetList.jsx

Commençons par le fichier responsable du rendu de la liste complète des animaux :

```javascript
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'

function PetList() {
    const [pets, setPets] = useState([])

    const getPets = async () => {
        try {
            /* FETCH */
            // const response = await fetch('http://localhost:3000/pets')
            // const data = await response.json()
            // if (response.status === 200) setPets(data)

            /* AXIOS */
            const response = await axios.get('http://localhost:3000/pets')
            if (response.status === 200) setPets(response.data)
            
        } catch (error) {
            console.error('error', error)
        }
    }
  
    useEffect(() => { getPets() }, [])

    return (
        <>
            <h2>Pet List</h2>

            {pets?.map((pet) => {
                return (
                    <div key={pet?.id}>
                        <p>{pet?.name} - {pet?.type} - {pet?.breed}</p>

                        <Link to={`/${pet?.id}`}>
                            <button>Pet detail</button>
                        </Link>
                    </div>
                )
            })}
        </>
    )
}

export default PetList
```

Comme vous pouvez le voir, en termes de logique, nous avons 3 choses principales ici :

* Un état qui stocke la liste des animaux à rendre.
    
* Une fonction qui exécute la requête correspondante à notre API.
    
* Un useEffect qui exécute cette fonction lorsque le composant se rend.
    

Vous pouvez voir que la syntaxe pour faire la requête HTTP avec fetch et Axios est plutôt similaire, mais Axios est un peu plus succinct. Une fois que nous faisons la requête, nous vérifions si le statut est 200 (ce qui signifie qu'elle a réussi), et stockons la réponse dans notre état.

Une fois que notre état est mis à jour, le composant rendra les données fournies par notre API.

> N'oubliez pas que pour faire des appels à notre serveur, nous devons l'avoir en marche en exécutant `nodemon app.js` dans le terminal de notre projet serveur.

### PetDetail.jsx

Maintenant, allons dans le fichier `PetDetail.jsx` :

```javascript
import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import axios from 'axios'

function PetDetail({ setPetToEdit }) {

    const [pet, setPet] = useState([])

    const { petId } = useParams()

    const getPet = async () => {
        try {
            /* FETCH */
            // const response = await fetch(`http://localhost:3000/pets/${petId}`)
            // const data = await response.json()
            // if (response.status === 200) {
            //     setPet(data)
            //     setPetToEdit(data)
            // }

            /* AXIOS */
            const response = await axios.get(`http://localhost:3000/pets/${petId}`)
            if (response.status === 200) {
                setPet(response.data)
                setPetToEdit(response.data)
            }
            
        } catch (error) {
            console.error('error', error)
        }
    }
  
    useEffect(() => { getPet() }, [])

    const deletePet = async () => {
        try {
            /* FETCH */
            // const response = await fetch(`http://localhost:3000/pets/${petId}`, {
            //     method: 'DELETE'
            // })
            
            /* AXIOS */
            const response = await axios.delete(`http://localhost:3000/pets/${petId}`)

            if (response.status === 200) window.location.href = '/'
        } catch (error) {
            console.error('error', error)
        }
    }

    return (
        <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', aligniItems: 'center' }}>
            <h2>Pet Detail</h2>

            {pet && (
                <>
                    <p>Pet name: {pet.name}</p>
                    <p>Pet type: {pet.type}</p>
                    <p>Pet age: {pet.age}</p>
                    <p>Pet breed: {pet.breed}</p>

                    <div style={{ display: 'flex', justifyContent: 'center', aligniItems: 'center' }}>
                        
                        <Link to={`/${pet?.id}/edit`}>
                            <button style={{ marginRight: 10 }}>Edit pet</button>
                        </Link>

                        <button
                            style={{ marginLeft: 10 }}
                            onClick={() => deletePet()}
                        >
                            Delete pet
                        </button>
                    </div>
                </>
            )}
        </div>
    )
}

export default PetDetail
```

Ici, nous avons deux types de requêtes différents :

* Une qui obtient les informations de l'animal donné (qui se comporte très similaire à la requête précédente que nous avons vue). La seule différence ici est que nous passons un paramètre d'URL à notre endpoint, que nous lisons en même temps de l'URL dans notre application front-end.
    
* L'autre requête est pour supprimer l'animal donné de notre registre. La différence ici est qu'une fois que nous confirmons que la requête a réussi, nous redirigeons l'utilisateur vers la racine de notre application.
    

### AddPet.jsx

Ce fichier est responsable de l'ajout d'un nouvel animal à notre registre :

```javascript
import React, { useState } from 'react'
import axios from 'axios'

function AddPet() {

    const [petName, setPetName] = useState()
    const [petType, setPetType] = useState()
    const [petAge, setPetAge] = useState()
    const [petBreed, setPetBreed] = useState()

    const addPet = async () => {
        try {
            const petData = {
                name: petName,
                type: petType,
                age: petAge,
                breed: petBreed
            }

            /* FETCH */
            // const response = await fetch('http://localhost:3000/pets/', {
            //     method: 'POST',
            //     headers: {
            //         'Content-Type': 'application/json'
            //     },
            //     body: JSON.stringify(petData)
            // })

            // if (response.status === 200) {
            //     const data = await response.json()
            //     window.location.href = `/${data.id}`
            // }

            /* AXIOS */
            const response = await axios.post(
                'http://localhost:3000/pets/',
                petData,
                { headers: { 'Content-Type': 'application/json' } }
            )
                
            if (response.status === 200) window.location.href = `/${response.data.id}`

        } catch (error) {
            console.error('error', error)
        }
    }

    return (
        <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', aligniItems: 'center' }}>
            <h2>Add Pet</h2>
            
            <div style={{ display: 'flex', flexDirection: 'column', margin: 20 }}>
                <label>Pet name</label>
                <input type='text' value={petName} onChange={e => setPetName(e.target.value)} />
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', margin: 20 }}>
                <label>Pet type</label>
                <input type='text' value={petType} onChange={e => setPetType(e.target.value)} />
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', margin: 20 }}>
                <label>Pet age</label>
                <input type='text' value={petAge} onChange={e => setPetAge(e.target.value)} />
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', margin: 20 }}>
                <label>Pet breed</label>
                <input type='text' value={petBreed} onChange={e => setPetBreed(e.target.value)} />
            </div>

            <button
                style={{ marginTop: 30 }}
                onClick={() => addPet()}
            >
                Add pet
            </button>
        </div>
    )
}

export default AddPet
```

Ici, nous rendons un formulaire dans lequel l'utilisateur doit entrer les nouvelles informations sur l'animal.

Nous avons un état pour chaque morceau d'information à entrer, et dans notre requête, nous construisons un objet avec chaque état. Cet objet sera le corps de notre requête.

Dans notre requête, nous vérifions si la réponse est réussie. Si c'est le cas, nous redirigeons vers la page de détail de l'animal nouvellement ajouté. Pour rediriger, nous utilisons l'`id` retourné dans la réponse HTTP. ;)

### EditPet.jsx

Enfin, le fichier responsable de la modification d'un enregistrement d'animal :

```javascript
import React, { useState } from 'react'
import axios from 'axios'

function EditPet({ petToEdit }) {

    const [petName, setPetName] = useState(petToEdit?.name)
    const [petType, setPetType] = useState(petToEdit?.type)
    const [petAge, setPetAge] = useState(petToEdit?.age)
    const [petBreed, setPetBreed] = useState(petToEdit?.breed)

    const editPet = async () => {
        try {
            const petData = {
                id: petToEdit.id,
                name: petName,
                type: petType,
                age: petAge,
                breed: petBreed
            }

            /* FETCH */
            // const response = await fetch(`http://localhost:3000/pets/${petToEdit.id}`, {
            //     method: 'PUT',
            //     headers: {
            //         'Content-Type': 'application/json'
            //     },
            //     body: JSON.stringify(petData)
            // })

            /* AXIOS */
            const response = await axios.put(
                `http://localhost:3000/pets/${petToEdit.id}`,
                petData,
                { headers: { 'Content-Type': 'application/json' } }
            )
            
            if (response.status === 200) {
                window.location.href = `/${petToEdit.id}`
            }
        } catch (error) {
            console.error('error', error)
        }
    }

    return (
        <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', aligniItems: 'center' }}>
            <h2>Edit Pet</h2>
            
            <div style={{ display: 'flex', flexDirection: 'column', margin: 20 }}>
                <label>Pet name</label>
                <input type='text' value={petName} onChange={e => setPetName(e.target.value)} />
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', margin: 20 }}>
                <label>Pet type</label>
                <input type='text' value={petType} onChange={e => setPetType(e.target.value)} />
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', margin: 20 }}>
                <label>Pet age</label>
                <input type='text' value={petAge} onChange={e => setPetAge(e.target.value)} />
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', margin: 20 }}>
                <label>Pet breed</label>
                <input type='text' value={petBreed} onChange={e => setPetBreed(e.target.value)} />
            </div>

            <button
                style={{ marginTop: 30 }}
                onClick={() => editPet()}
            >
                Save changes
            </button>
        </div>
    )
}

export default EditPet
```

Cela se comporte très similaire au fichier `AddPet.jsx`. La seule différence est que nos états d'informations sur les animaux sont initialisés avec les valeurs de l'animal que nous voulons modifier. Lorsque ces valeurs sont mises à jour par l'utilisateur, nous construisons un objet qui sera le corps de notre requête et envoyons la requête avec les informations mises à jour. Assez simple. ;)

Et c'est tout ! Nous utilisons tous nos endpoints d'API dans notre application front-end. =)

# Comment documenter une API REST avec Swagger

Maintenant que nous avons notre serveur en marche, testé et connecté à notre application front-end, la dernière étape de notre implémentation sera de documenter notre API.

Documenter une API signifie généralement déclarer quels endpoints sont disponibles, quelles actions sont effectuées par chaque endpoint, et les paramètres et valeurs de retour pour chacun d'eux.

Cela est utile non seulement pour se souvenir de la manière dont notre serveur fonctionne, mais aussi pour les personnes qui veulent interagir avec notre API.

Par exemple, dans les entreprises, il est très courant d'avoir des équipes back-end et des équipes front-end. Lorsqu'une API est en cours de développement et doit être intégrée à une application front-end, il serait très fastidieux de demander quel endpoint fait quoi, et quels paramètres doivent être passés. Si vous avez toutes ces informations à un seul endroit, vous pouvez simplement y aller et les lire vous-même. C'est à cela que sert la documentation.

## Nos outils

[**Swagger**](https://swagger.io/) est un ensemble d'outils open-source qui aident les développeurs à construire, documenter et consommer des services web RESTful. Il fournit une interface graphique conviviale pour que les utilisateurs interagissent avec une API et génère également du code client pour divers langages de programmation afin de faciliter l'intégration de l'API.

Swagger fournit un ensemble complet de fonctionnalités pour le développement d'API, y compris la conception, la documentation, les tests et la génération de code. Il permet aux développeurs de définir les endpoints de l'API, les paramètres d'entrée, la sortie attendue et les exigences d'authentification de manière standardisée en utilisant la spécification OpenAPI.

Swagger UI est un outil populaire qui rend les spécifications OpenAPI sous forme de documentation API interactive qui permet aux développeurs d'explorer et de tester les API via un navigateur web. Il fournit une interface conviviale qui permet aux développeurs de visualiser et d'interagir facilement avec les endpoints de l'API.

## Comment implémenter Swagger

De retour dans notre application serveur, pour implémenter Swagger, nous aurons besoin de deux nouvelles dépendances. Donc exécutez `npm i swagger-jsdoc` et `npm i swagger-ui-express`.

Ensuite, modifiez le fichier `app.js` pour qu'il ressemble à ceci :

```javascript
import express from 'express'
import cors from 'cors'
import swaggerUI from 'swagger-ui-express'
import swaggerJSdoc from 'swagger-jsdoc'

import petRoutes from './pets/routes/pets.routes.js'

const app = express()
const port = 3000

// swagger definition
const swaggerSpec = {
    definition: {
        openapi: '3.0.0',
        info: {
            title: 'Pets API',
            version: '1.0.0',
        },
        servers: [
            {
                url: `http://localhost:${port}`,
            }
        ]
    },
    apis: ['./pets/routes/*.js'],
}

/* Global middlewares */
app.use(cors())
app.use(express.json())
app.use(
    '/api-docs',
    swaggerUI.serve,
    swaggerUI.setup(swaggerJSdoc(swaggerSpec))
)

/* Routes */
app.use('/pets', petRoutes)

/* Server setup */
if (process.env.NODE_ENV !== 'test') {
    app.listen(port, () => console.log(`\u26a1\ufe0f[server]: Server is running at https://localhost:${port}`))
}

export default app
```

Comme vous pouvez le voir, nous importons les nouvelles dépendances, nous créons un objet `swaggerSpec` qui contient des options de configuration pour notre implémentation, et nous définissons un middleware pour rendre notre documentation dans le répertoire `/api-docs` de notre application.

Maintenant, si vous ouvrez votre navigateur et allez sur [`http://localhost:3000/api-docs/`](http://localhost:3000/api-docs/), vous devriez voir ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-325.png align="left")

*Interface utilisateur de la documentation*

Le truc cool avec Swagger est qu'il fournit une interface utilisateur prête à l'emploi pour nos docs, et vous pouvez y accéder facilement dans le chemin d'URL déclaré dans la configuration.

Maintenant, écrivons une vraie documentation !

Allez dans le fichier `pets.routes.js` et remplacez son code par ceci :

```javascript
import express from "express";
import {
  listPets,
  getPet,
  editPet,
  addPet,
  deletePet,
} from "../controllers/pets.controllers.js";

const router = express.Router();

/**
 * @swagger
 * components:
 *  schemas:
 *     Pet:
 *      type: object
 *      properties:
 *          id:
 *              type: integer
 *              description: Pet id
 *          name:
 *              type: string
 *              description: Pet name
 *          age:
 *              type: integer
 *              description: Pet age
 *          type:
 *              type: string
 *              description: Pet type
 *          breed:
 *              type: string
 *              description: Pet breed
 *     example:
 *          id: 1
 *          name: Rexaurus
 *          age: 3
 *          breed: labrador
 *          type: dog
 */

/**
 * @swagger
 * /pets:
 *  get:
 *     summary: Get all pets
 *     description: Get all pets
 *     responses:
 *      200:
 *         description: Success
 *      500:
 *         description: Internal Server Error
 */
router.get("/", listPets);

/**
 * @swagger
 * /pets/{id}:
 *  get:
 *     summary: Get pet detail
 *     description: Get pet detail
 *     parameters:
 *       - in: path
 *         name: id
 *         schema:
 *           type: integer
 *         required: true
 *         description: Pet id
 *     responses:
 *      200:
 *         description: Success
 *      500:
 *         description: Internal Server Error
 */
router.get("/:id", getPet);

/**
 * @swagger
 * /pets/{id}:
 *  put:
 *     summary: Edit pet
 *     description: Edit pet
 *     parameters:
 *       - in: path
 *         name: id
 *         schema:
 *           type: integer
 *         required: true
 *         description: Pet id
 *     requestBody:
 *       description: A JSON object containing pet information
 *       content:
 *         application/json:
 *           schema:
 *              $ref: '#/components/schemas/Pet'
 *           example:
 *              name: Rexaurus
 *              age: 12
 *              breed: labrador
 *              type: dog
 *     responses:
 *     200:
 *        description: Success
 *     500:
 *       description: Internal Server Error
 *
 */
router.put("/:id", editPet);

/**
 * @swagger
 * /pets:
 *  post:
 *      summary: Add pet
 *      description: Add pet
 *      requestBody:
 *          description: A JSON object containing pet information
 *          content:
 *             application/json:
 *                 schema:
 *                    $ref: '#/components/schemas/Pet'
 *                 example:
 *                    name: Rexaurus
 *                    age: 12
 *                    breed: labrador
 *                    type: dog
 *      responses:
 *      200:
 *          description: Success
 *      500:
 *          description: Internal Server Error
 */
router.post("/", addPet);

/**
 * @swagger
 * /pets/{id}:
 *  delete:
 *     summary: Delete pet
 *     description: Delete pet
 *     parameters:
 *       - in: path
 *         name: id
 *         schema:
 *           type: integer
 *         required: true
 *         description: Pet id
 *     responses:
 *     200:
 *        description: Success
 *     500:
 *       description: Internal Server Error
 */
router.delete("/:id", deletePet);

export default router;
```

Comme vous pouvez le voir, nous ajoutons un type spécial de commentaire pour chacun de nos endpoints. C'est ainsi que Swagger UI identifie la documentation dans notre code. Nous les avons placés dans ce fichier car il est logique d'avoir les docs aussi proches que possible des endpoints, mais vous pourriez les placer où vous voulez.

Si nous analysons les commentaires en détail, vous pouvez voir qu'ils sont écrits dans une syntaxe de type YAML, et pour chacun d'eux, nous spécifions la route de l'endpoint, la méthode HTTP, une description, les paramètres qu'il reçoit et les réponses possibles.

Tous les commentaires sont plus ou moins les mêmes sauf le premier. Dans celui-ci, nous définissons un "schéma" qui est comme un typage pour un type d'objet que nous pouvons réutiliser plus tard dans d'autres commentaires. Dans notre cas, nous définissons le schéma "Pet" que nous utilisons ensuite pour les endpoints `put` et `post`.

Si vous entrez à nouveau sur [`http://localhost:3000/api-docs/`](http://localhost:3000/api-docs/), vous devriez maintenant voir ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-327.png align="left")

*Interface utilisateur de la documentation*

Chacun des endpoints peut être développé, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-328.png align="left")

*Interface utilisateur de la documentation*

Et si nous cliquons sur le bouton "Try it out", nous pouvons exécuter une requête HTTP et voir à quoi ressemble la réponse :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-329.png align="left")

*Interface utilisateur de la documentation*

Cela est vraiment utile pour les développeurs en général et les personnes qui veulent travailler avec notre API, et très facile à configurer comme vous pouvez le voir.

Avoir une interface utilisateur prête à l'emploi simplifie l'interaction avec la documentation. Et l'avoir également dans notre base de code est un grand bonus, car nous pouvons la modifier et la mettre à jour sans avoir besoin de toucher autre chose que notre propre code.

# Conclusion

Comme toujours, j'espère que vous avez apprécié le manuel et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman).

À la prochaine !

![Image](https://www.freecodecamp.org/news/content/images/2023/04/5325cccb7a8a7ba25e7780d03c348b2f.gif align="left")