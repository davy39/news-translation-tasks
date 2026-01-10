---
title: Comment tester vos applications Express.js et Mongoose avec Jest et SuperTest
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-27T23:26:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-test-in-express-and-mongoose-apps
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/how-to-write-tests.png
tags:
- name: Express JS
  slug: express-js
- name: Jest
  slug: jest
- name: mongoose
  slug: mongoose
- name: Software Testing
  slug: software-testing
- name: Testing
  slug: testing
seo_title: Comment tester vos applications Express.js et Mongoose avec Jest et SuperTest
seo_desc: "By Rakesh Potnuru\nTesting is a vital part of software development. The\
  \ sooner you start testing, the better. \nIn this article, I'll show you how to\
  \ write tests for your NodeJs/ExpressJS and MongoDB/Mongoose applications with Jest\
  \ and Supertest.\nLet's..."
---

Par Rakesh Potnuru

Le test est une partie vitale du développement logiciel. Plus tôt vous commencez à tester, mieux c'est.

Dans cet article, je vais vous montrer comment écrire des tests pour vos applications NodeJs/ExpressJS et MongoDB/Mongoose avec **Jest** et **Supertest**.

## Commençons

Tout d'abord, configurons une application Express.js de démonstration.

Supposons que nous construisons une API REST backend pour une application d'e-commerce.

Cette application devrait :

* Récupérer tous les produits
* Récupérer un produit par identifiant
* Ajouter des produits à la base de données
* Supprimer des produits de la base de données
* Mettre à jour les informations sur le produit

## Configuration de l'application Express.js

### Étape 1 : Configuration du projet

Tout d'abord, créez un dossier et démarrez une application vide avec `npm`.

```bash
npm init
```

Remplissez tous les détails demandés.

Ensuite, installez `express`, `mongoose`, `axios` et `dotenv` avec la commande suivante :

```bash
npm i express mongoose axios dotenv
```

Voici un lien vers le [package.json](https://github.com/itsrakeshhq/jest-tests-demo/blob/a1725cb3379f78a03cf8d3d4cfa22127469e8b50/package.json) sur mon GitHub.

### Étape 2 : Créer le boilerplate

Créons tous les dossiers et fichiers, puis remplissons-les avec du code boilerplate.

Voici à quoi devrait ressembler la hiérarchie de vos dossiers :

```bash
.
├── controllers
│   └── product.controller.js
├── models
│   └── product.model.js
├── routes
│   └── product.route.js
├── package-lock.json
├── package.json
├── .env
├── app.js
└── server.js
```

Utilisez le code de ces fichiers en faisant un copier-coller. Analysez le code et le flux du mieux que vous pouvez.

* `[product.controller.js](https://github.com/itsrakeshhq/jest-tests-demo/blob/main/controllers/product.controller.js)`
* `[product.model.js](https://github.com/itsrakeshhq/jest-tests-demo/blob/main/models/product.model.js)`
* `[product.route.js](https://github.com/itsrakeshhq/jest-tests-demo/blob/main/routes/product.route.js)`
* `[app.js](https://github.com/itsrakeshhq/jest-tests-demo/blob/main/app.js)` 
* `[server.js](https://github.com/itsrakeshhq/jest-tests-demo/blob/main/server.js)`

### Étape 3 : Configuration de la base de données

Je conseille d'utiliser deux bases de données pour un projet — une pour les tests, l'autre pour le développement. Mais une seule base de données suffira pour l'apprentissage.

Tout d'abord, créez un compte [MongoDB](https://mongodb.com) ou connectez-vous.

Ensuite, créez un nouveau projet. Donnez-lui un nom et appuyez sur le bouton **Next**.

![Nommer le projet](https://www.freecodecamp.org/news/content/images/2022/09/Screenshot-2022-09-26-205148.png)
_Nommer le projet_

Cliquez ensuite sur **Create Project** après cela.

Nous devons créer une base de données dans la fenêtre suivante en sélectionnant un fournisseur cloud, un emplacement et des spécifications. Appuyez donc sur **Build a Database** pour commencer.

![Construire une base de données](https://www.freecodecamp.org/news/content/images/2022/09/Screenshot-2022-09-26-205911.png)
_Construire une base de données_

Choisissez « Shared » car c'est suffisant pour l'apprentissage. Cliquez ensuite sur **Create**.

![Choisir une option de déploiement](https://www.freecodecamp.org/news/content/images/2022/09/Screenshot-2022-09-26-211701.png)
_Choisir une option de déploiement_

Ensuite, sélectionnez « aws » comme fournisseur cloud et la région la plus proche de chez vous. Après votre sélection, cliquez sur **Create Cluster**.

La formation du cluster prendra un certain temps. Créez un utilisateur pour accéder à votre base de données en attendant.

![Créer un super-utilisateur](https://www.freecodecamp.org/news/content/images/2022/09/Screenshot-2022-09-26-212537.png)
_Créer un super-utilisateur_

Choisissez « My Local Environment » car nous développons notre application. Vous pouvez ensuite ajouter des adresses IP. Pour conclure, cliquez sur **Close**.

![Ajouter des adresses IP](https://www.freecodecamp.org/news/content/images/2022/09/Screenshot-2022-09-26-213347.png)
_Ajouter des adresses IP_

Vous recevrez une chaîne URI une fois la base de données configurée, que nous utiliserons pour nous connecter à la base de données. La chaîne se présente comme suit :

```bash
mongodb+srv://<VOTRE_NOM_UTILISATEUR>:<VOTRE_MOT_DE_PASSE>@<VOTRE_URL_CLUSTER>/<NOM_BASE_DE_DONNEES>?retryWrites=true&w=majority
```

Mettez cette chaîne dans le fichier `.env`.

```bash
MONGODB_URI=votre chaîne de base de données
```

Nous sommes maintenant prêts à commencer à tester notre application.

## Comment écrire des tests avec Jest et SuperTest

### Étape 1 : Installer les packages

Vous avez besoin de trois packages npm pour commencer à écrire des tests : `jest`, `supertest` et `cross-env`. Vous pouvez les installer comme ceci :

```bash
npm i jest supertest cross-env
```

* `jest` : Jest est un Framework pour tester le code JavaScript. Les tests unitaires en sont l'utilisation principale.
* `supertest` : En utilisant Supertest, nous pouvons tester les points de terminaison et les routes sur les serveurs HTTP.
* `cross-env` : Vous pouvez définir des variables d'environnement en ligne dans une commande à l'aide de cross-env.

### Étape 2 : Ajouter le script de test

Ouvrez votre fichier `package.json` et ajoutez le script de test aux scripts.

```json
"scripts": {
    "test": "cross-env NODE_ENV=test jest --testTimeout=5000",
    "start": "node server.js",
    "dev": "nodemon server.js"
},
```

Dans ce cas, nous utilisons `cross-env` pour définir les variables d'environnement, `jest` pour exécuter les suites de tests, et `testTimeout` est défini sur `5000` car certaines requêtes peuvent prendre un certain temps à se terminer.

### Étape 3 : Commencer à écrire des tests

Tout d'abord, créez un dossier nommé `tests` à la racine de l'application, puis créez-y un fichier nommé `product.test.js`. Jest recherche le dossier `tests` à la racine du projet lorsque vous exécutez `npm run test`. Par conséquent, vous devez placer vos fichiers de test dans le dossier `tests`.

Ensuite, importez les packages `supertest` et `mongoose` dans le fichier de test.

```javascript
const mongoose = require("mongoose");
const request = require("supertest");
```

Importez `dotenv` pour charger les variables d'environnement, et importez `app.js` car c'est là que notre application démarre.

```javascript
const mongoose = require("mongoose");
const request = require("supertest");
const app = require("../app");

require("dotenv").config();

```

Vous devrez connecter et déconnecter la base de données avant et après chaque test (car nous n'avons plus besoin de la base de données une fois les tests terminés).

```javascript
/* Connexion à la base de données avant chaque test. */
beforeEach(async () => {
  await mongoose.connect(process.env.MONGODB_URI);
});

/* Fermeture de la connexion à la base de données après chaque test. */
afterEach(async () => {
  await mongoose.connection.close();
});

```

Vous pouvez maintenant écrire votre premier test unitaire.

```javascript
describe("GET /api/products", () => {
  it("should return all products", async () => {
    const res = await request(app).get("/api/products");
    expect(res.statusCode).toBe(200);
    expect(res.body.length).toBeGreaterThan(0);
  });
});

```

Dans le code ci-dessus, 

* Nous utilisons `describe` pour décrire le test unitaire. Même si ce n'est pas obligatoire, cela sera utile pour identifier les tests dans les résultats de test.
* Dans `it`, nous écrivons le code de test réel. Indiquez ce que le test effectue dans le premier argument, puis dans le second argument, écrivez une fonction de rappel qui contient le code de test.
* Dans la fonction de rappel, la requête est d'abord envoyée au point de terminaison, puis les réponses attendues et réelles sont comparées. Le test réussit si les deux réponses correspondent, sinon, il échoue. ✨ C'est aussi simple que ça ✨.

Vous pouvez écrire des tests pour tous les points de terminaison de la même manière.

```javascript
describe("GET /api/products/:id", () => {
  it("should return a product", async () => {
    const res = await request(app).get(
      "/api/products/6331abc9e9ececcc2d449e44"
    );
    expect(res.statusCode).toBe(200);
    expect(res.body.name).toBe("Product 1");
  });
});

describe("POST /api/products", () => {
  it("should create a product", async () => {
    const res = await request(app).post("/api/products").send({
      name: "Product 2",
      price: 1009,
      description: "Description 2",
    });
    expect(res.statusCode).toBe(201);
    expect(res.body.name).toBe("Product 2");
  });
});

describe("PUT /api/products/:id", () => {
  it("should update a product", async () => {
    const res = await request(app)
      .patch("/api/products/6331abc9e9ececcc2d449e44")
      .send({
        name: "Product 4",
        price: 104,
        description: "Description 4",
      });
    expect(res.statusCode).toBe(200);
    expect(res.body.price).toBe(104);
  });
});

describe("DELETE /api/products/:id", () => {
  it("should delete a product", async () => {
    const res = await request(app).delete(
      "/api/products/6331abc9e9ececcc2d449e44"
    );
    expect(res.statusCode).toBe(200);
  });
});

```

Ensuite, exécutez `npm run test` pour lancer les suites de tests (suite - fichier de test).

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-428.png)
_Résultats des tests_

Et voilà ! Vous savez maintenant comment tester vos applications Express/Mongoose avec Jest et SuperTest.

Maintenant, lancez-vous et créez de nouveaux tests pour vos applications. :)

Si vous avez des questions, n'hésitez pas à m'envoyer un message sur [Twitter](https://twitter.com/rakesh_at_tweet).