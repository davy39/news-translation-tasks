---
title: Une introduction étape par étape aux tests de points de terminaison
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-08-28T23:51:55.000Z'
originalURL: https://freecodecamp.org/news/end-point-testing
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca097740569d1a4ca49a0.jpg
tags:
- name: Express.js
  slug: expressjs
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Testing
  slug: testing
seo_title: Une introduction étape par étape aux tests de points de terminaison
seo_desc: 'I''ve been playing around with testing lately. One thing I tried to do
  was to test the endpoints of my Express application.

  Setting up the test was the hard part. People who write about tests don''t actually
  teach you how they set it up. I could not fi...'
---

J'ai récemment exploré les tests. L'une des choses que j'ai essayées était de tester les points de terminaison de mon application Express.

La configuration du test était la partie difficile. Les personnes qui écrivent sur les tests ne vous apprennent pas vraiment comment ils les configurent. Je n'ai pas trouvé d'informations utiles à ce sujet, et j'ai dû essayer et comprendre par moi-même.

Aujourd'hui, je veux donc partager la configuration que j'ai créée pour moi-même. Espérons que cela puisse vous aider lorsque vous créerez vos propres tests.

## Table des matières

1. [Configuration de Jest et Supertest](#heading-installation-de-jest-et-supertest)
2. [Connexion de Jest et Mongoose](#heading-connexion-de-jest-et-mongoose)
3. [Peuplement d'une base de données](#heading-peuplement-dune-base-de-donnees)

<h2 id="part1">Configuration de Jest et Supertest</h2>

Tout d'abord, parlons de la pile.

### La pile

- J'ai créé mon application avec Express.
- J'ai utilisé Mongoose pour me connecter à MongoDB
- J'ai utilisé Jest comme framework de test.

Vous auriez pu vous attendre à Express et Mongoose car tout le monde semble utiliser ces deux frameworks. Je les ai utilisés aussi.

Mais pourquoi Jest et pas d'autres frameworks de test ?

### Pourquoi Jest

Je n'aime pas Facebook, donc je ne voulais pas essayer quoi que ce soit créé par l'équipe de Facebook. Je sais que cela semble stupide, mais c'était la vérité.

Avant Jest, j'ai essayé toutes sortes de frameworks de test. J'ai essayé Tap, Tape, Mocha, Jasmine et AVA. Chaque framework de test a ses propres avantages et inconvénients. J'ai presque fini avec AVA, mais je ne suis pas allé avec AVA car j'ai trouvé difficile à configurer. Finalement, j'ai essayé Jest parce que Kent C. Dodds l'a recommandé.

Je suis tombé amoureux de Jest après l'avoir essayé. Je l'aime parce que :

1. Il est facile à configurer
2. Le [mode watch][1] est incroyable
3. Lorsque vous `console.log` quelque chose, il s'affiche réellement sans aucune difficulté (c'était un problème avec AVA).

### Configuration de Jest

Tout d'abord, vous devez installer Jest.

```js
npm install jest --save-dev
```

Ensuite, vous voulez ajouter des scripts de test à votre fichier `package.json`. Il est utile d'ajouter les scripts `test` et `test:watch` (pour les tests ponctuels et le mode watch respectivement).

```js
"scripts": {
  "test": "jest",
  "test:watch": "jest --watch"
},
```

Vous pouvez choisir d'écrire vos fichiers de test dans l'un des formats suivants. Jest les détecte automatiquement pour vous.

1. Fichiers `js` dans le dossier `__tests__`
2. Fichiers nommés avec `test.js` (comme `user.test.js`)
3. Fichiers nommés avec `spec.js` (comme `user.spec.js`)

Vous pouvez placer vos fichiers comme vous le souhaitez. Lorsque j'ai testé des points de terminaison, j'ai mis les fichiers de test avec mes points de terminaison. J'ai trouvé cela plus facile à gérer.

```bash
- routes
  |- users/
    |- index.js
    |- users.test.js
```

### Écrire votre premier test

Jest inclut `describe`, `it` et `expect` pour vous dans chaque fichier de test. Vous n'avez pas besoin de les `require`.

- `describe` vous permet de regrouper plusieurs tests sous un même parapluie. (Il est utilisé pour organiser vos tests).
- `it` vous permet d'exécuter un test.
- `expect` vous permet de faire des assertions. Le test passe si toutes les assertions passent.

Voici un exemple de test qui échoue. Dans cet exemple, je `expect` que `1` soit strictement égal à `2`. Puisque `1 !== 2`, le test échoue.

```js
// Ce test échoue car 1 !== 2
it("Test pour voir si Jest fonctionne", () => {
  expect(1).toBe(2);
});
```

Vous verrez un message d'échec de Jest si vous exécutez Jest.

```js
npm run test:watch
```

<figure><img src="https://zellwk.com/images/2019/endpoint-testing/test-fail.png" alt="Sortie du terminal. Test échoué."></figure>

Vous pouvez faire passer le test en attendant `1 === 1`.

```js
// Cela passe car 1 === 1
it("Test pour voir si Jest fonctionne", () => {
  expect(1).toBe(1);
});
```

<figure><img src="https://zellwk.com/images/2019/endpoint-testing/test-pass.png" alt="Sortie du terminal. Test réussi."></figure>

C'est le test le plus basique. Il n'est pas utile du tout car nous n'avons encore rien testé de réel.

## Tests asynchrones

Vous devez envoyer une requête pour tester un point de terminaison. Les requêtes sont asynchrones, ce qui signifie que vous devez être capable de mener des tests asynchrones.

C'est facile avec Jest. Il y a deux étapes :

1. Ajouter le mot-clé `async`
2. Appeler `done` lorsque vous avez terminé vos tests

Voici à quoi cela peut ressembler :

```js
it("Test asynchrone", async done => {
  // Faites vos tests asynchrones ici

  done();
});
```

Note : [Voici un article][2] sur Async/await en JavaScript si vous ne savez pas comment l'utiliser.

## Test des points de terminaison

Vous pouvez utiliser Supertest pour tester les points de terminaison. Tout d'abord, vous devez installer Supertest.

```bash
npm install supertest --save-dev
```

Avant de pouvoir tester les points de terminaison, vous devez configurer le serveur pour que Supertest puisse l'utiliser dans vos tests.

La plupart des tutoriels vous apprennent à `listen` l'application Express dans le fichier serveur, comme ceci :

```js
const express = require("express");
const app = express();

// Middlewares...
// Routes...

app.listen(3000);
```

Cela ne fonctionne pas car il commence à écouter sur un port. Si vous essayez d'écrire plusieurs fichiers de test, vous obtiendrez une erreur indiquant "port en cours d'utilisation".

Vous voulez permettre à chaque fichier de test de démarrer un serveur par lui-même. Pour ce faire, vous devez exporter `app` sans l'écouter.

```js
// server.js
const express = require("express");
const app = express();

// Middlewares...
// Routes...

module.exports = app;
```

Pour des fins de développement ou de production, vous pouvez écouter votre `app` normalement dans un fichier différent comme `start.js`.

```js
// start.js
const app = require("./server.js");
app.listen(3000);
```

### Utilisation de Supertest

Pour utiliser Supertest, vous avez besoin de votre application et de supertest dans le fichier de test.

```js
const app = require("./server"); // Lien vers votre fichier serveur
const supertest = require("supertest");
const request = supertest(app);
```

Une fois que vous avez fait cela, vous obtenez la possibilité d'envoyer des requêtes GET, POST, PUT, PATCH et DELETE. Avant d'envoyer une requête, nous devons avoir un point de terminaison. Supposons que nous avons un point de terminaison `/test`.

```js
app.get("/test", async (req, res) => {
  res.json({ message: "pass!" });
});
```

Pour envoyer une requête GET à `/test`, vous utilisez la méthode `.get` de Supertest.

```js
it("Obtient le point de terminaison de test", async done => {
  // Envoie une requête GET au point de terminaison /test
  const res = await request.get("/test");

  // ...
  done();
});
```

Supertest vous donne une réponse du point de terminaison. Vous pouvez tester à la fois le statut HTTP et le corps (ce que vous envoyez via `res.json`) comme ceci :

```js
it("obtient le point de terminaison de test", async done => {
  const response = await request.get("/test");

  expect(response.status).toBe(200);
  expect(response.body.message).toBe("pass!");
  done();
});
```

<figure><img src="https://zellwk.com/images/2019/endpoint-testing/test-endpoint-pass.png" alt="Premier test de point de terminaison réussi."></figure>


<h2 id="part2">Connexion de Jest et Mongoose</h2>

La partie difficile des tests d'une application backend est la configuration d'une base de données de test. Cela peut être compliqué.

Aujourd'hui, je veux partager comment j'ai configuré Jest et Mongoose.

### Configuration de Mongoose avec Jest

Jest vous donne un avertissement si vous essayez d'utiliser Mongoose avec Jest.

<figure role="figure"><img src="https://zellwk.com/images/2019/jest-and-mongoose/mongoose-jest-warning.png" alt="Avertissement si vous essayez d'utiliser Mongoose avec Jest"></figure>

Si vous ne voulez pas voir cette erreur, vous devez définir `testEnvironment` sur `node` dans votre fichier `package.json`.

```js
"jest": {
  "testEnvironment": "node"
}
```

### Configuration de Mongoose dans un fichier de test

Vous voulez vous connecter à une base de données avant de commencer les tests. Vous pouvez utiliser le hook `beforeAll` pour ce faire.

```js
beforeAll(async () => {
  // Connexion à une base de données Mongo
});
```

Pour vous connecter à une base de données MongoDB, vous pouvez utiliser la commande `connect` de Mongoose.

```js
const mongoose = require("mongoose");
const databaseName = "test";

beforeAll(async () => {
  const url = `mongodb://127.0.0.1/${databaseName}`;
  await mongoose.connect(url, { useNewUrlParser: true });
});
```

Cela crée une connexion à la base de données nommée `test`. Vous pouvez nommer votre base de données comme vous le souhaitez. Vous apprendrez plus tard comment les nettoyer.

Note : Assurez-vous d'avoir une connexion locale MongoDB active avant de tester. Vos tests échoueront si vous n'avez pas de connexion locale MongoDB active. [Lisez ceci][4] pour apprendre à créer une connexion locale MongoDB.

### Création de bases de données pour chaque fichier de test

Lorsque vous testez, vous voulez vous connecter à une base de données différente pour chaque fichier de test, car :

1. Jest exécute chaque fichier de test de manière asynchrone. Vous ne saurez pas quel fichier vient en premier.
2. Vous ne voulez pas que les tests partagent la même base de données. Vous ne voulez pas que les données d'un fichier de test se répandent dans le fichier de test suivant.

Pour vous connecter à une base de données différente, vous changez le nom de la base de données.

```js
// Se connecte à la base de données appelée avengers
beforeAll(async () => {
  const url = `mongodb://127.0.0.1/avengers`;
  await mongoose.connect(url, { useNewUrlParser: true });
});
```

```js
// Se connecte à la base de données power-rangers
beforeAll(async () => {
  const url = `mongodb://127.0.0.1/power-rangers`;
  await mongoose.connect(url, { useNewUrlParser: true });
});
```

### Envoyer une requête POST

Supposons que vous voulez créer un utilisateur pour votre application. L'utilisateur a un nom et une adresse email. Votre schéma Mongoose pourrait ressembler à ceci :

```js
const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const userSchema = new Schema({
  name: String,
  email: {
    type: String,
    require: true,
    unique: true
  }
});

module.exports = mongoose.model("User", userSchema);
```

Pour créer un utilisateur, vous devez enregistrer le `name` et `email` dans MongoDB. Votre route et contrôleur pourraient ressembler à ceci :

```js
const User = require("../model/User"); // Lien vers votre modèle d'utilisateur

app.post("/signup", async (req, res) => {
  const { name, email } = req.body;
  const user = new User({ name, email });
  const ret = await user.save();
  res.json(ret);
});
```

Pour enregistrer l'utilisateur dans la base de données, vous pouvez envoyer une requête POST à `signup`. Pour envoyer une requête post, vous utilisez la méthode `post`. Pour envoyer des données avec la requête POST, vous utilisez la méthode `send`. Dans vos tests, cela ressemblera à ceci.

```js
it("Devrait enregistrer l'utilisateur dans la base de données", async done => {
  const res = await request.post("/signup").send({
    name: "Zell",
    email: "testing@gmail.com"
  });
  done();
});
```

Note : Si vous exécutez ce code deux fois, vous obtiendrez une erreur `E1100 duplicate key error`. Cette erreur s'est produite parce que :

1. Nous avons dit que l'`email` devrait être `unique` dans le schéma ci-dessus.
2. Nous avons essayé de créer un autre utilisateur avec `testing@gmail.com` même si un utilisateur existe déjà dans la base de données. (Le premier a été créé lorsque vous avez envoyé la première requête).

<figure role="figure"><img src="https://zellwk.com/images/2019/jest-and-mongoose/duplicate-error.png" alt="Erreur de clé dupliquée."></figure>

## Nettoyage de la base de données entre les tests

Vous voulez supprimer les entrées de la base de données entre chaque test. Cela garantit que vous commencez toujours avec une base de données vide.

Vous pouvez faire cela avec le hook `afterEach`.

```js
// Nettoie la base de données entre chaque test
afterEach(async () => {
  await User.deleteMany();
});
```

Dans le code ci-dessus, nous avons seulement effacé la collection `User` dans la base de données. Dans un scénario réel, vous voulez effacer toutes les collections. Vous pouvez utiliser le code suivant pour ce faire :

```js
async function removeAllCollections() {
  const collections = Object.keys(mongoose.connection.collections);
  for (const collectionName of collections) {
    const collection = mongoose.connection.collections[collectionName];
    await collection.deleteMany();
  }
}

afterEach(async () => {
  await removeAllCollections();
});
```

### Test du point de terminaison

Commençons nos tests. Dans ce test, nous allons envoyer une requête POST au point de terminaison `/signup`. Nous voulons nous assurer que :

1. L'utilisateur est enregistré dans la base de données
2. L'objet retourné contient des informations sur l'utilisateur

### Vérification si l'utilisateur a été enregistré dans la base de données

Pour vérifier si l'utilisateur est enregistré dans la base de données, vous recherchez l'utilisateur dans la base de données.

```js
const User = require("../model/User"); // Lien vers votre modèle d'utilisateur

it("Devrait enregistrer l'utilisateur dans la base de données", async done => {
  const res = await request.post("/signup").send({
    name: "Zell",
    email: "testing@gmail.com"
  });

  // Recherche l'utilisateur dans la base de données
  const user = await User.findOne({ email: "testing@gmail.com" });

  done();
});
```

Si vous `console.log` l'utilisateur, vous devriez voir quelque chose comme ceci :

<figure role="figure"><img src="https://zellwk.com/images/2019/jest-and-mongoose/user.png" alt="Objet utilisateur de MongoDB."></figure>

Cela signifie que notre utilisateur a été enregistré dans la base de données. Si nous voulons confirmer que l'utilisateur a un nom et un email, nous pouvons faire `expect` qu'ils soient vrais.

```js
it("Devrait enregistrer l'utilisateur dans la base de données", async done => {
  // Envoie la requête...

  // Recherche l'utilisateur dans la base de données
  const user = await User.findOne({ email: "testing@gmail.com" });
  expect(user.name).toBeTruthy();
  expect(user.email).toBeTruthy();

  done();
});
```

#### Vérification si l'objet retourné contient les informations sur l'utilisateur

Nous voulons nous assurer que l'objet retourné contient le nom et l'adresse email de l'utilisateur. Pour ce faire, nous vérifions la réponse de la requête post.

```js
it("Devrait enregistrer l'utilisateur dans la base de données", async done => {
  // Envoie la requête...

  // Recherche l'utilisateur dans la base de données...

  // Assure que la réponse contient le nom et l'email
  expect(res.body.name).toBeTruthy();
  expect(res.body.email).toBeTruthy();
  done();
});
```

Nous avons terminé nos tests maintenant. Nous voulons supprimer la base de données de MongoDB.

### Suppression de la base de données

Pour supprimer la base de données, vous devez vous assurer qu'il y a 0 collections dans la base de données. Nous pouvons faire cela en supprimant chaque collection que nous avons utilisée.

Nous le ferons après que tous nos tests ont été exécutés, dans le hook `afterAll`.

```js
afterAll(async () => {
  // Supprime la collection User
  await User.drop();
});
```

Pour supprimer toutes vos collections, vous pouvez utiliser ceci :

```js
async function dropAllCollections() {
  const collections = Object.keys(mongoose.connection.collections);
  for (const collectionName of collections) {
    const collection = mongoose.connection.collections[collectionName];
    try {
      await collection.drop();
    } catch (error) {
      // Cette erreur se produit lorsque vous essayez de supprimer une collection qui est déjà supprimée. Cela arrive rarement.
      // Sans danger à ignorer.
      if (error.message === "ns not found") return;

      // Cette erreur se produit lorsque vous utilisez it.todo.
      // Sans danger à ignorer.
      if (error.message.includes("a background operation is currently running"))
        return;

      console.log(error.message);
    }
  }
}

// Déconnecter Mongoose
afterAll(async () => {
  await dropAllCollections();
});
```

Enfin, vous voulez fermer la connexion Mongoose pour terminer le test. Voici comment vous pouvez le faire :

```js
afterAll(async () => {
  await dropAllCollections();
  // Ferme la connexion Mongoose
  await mongoose.connection.close();
});
```

C'est tout ce que vous devez faire pour configurer Mongoose avec Jest !

### Refactoring

Il y a beaucoup de code qui va dans les hooks `beforeEach`, `afterEach` et `afterAll`. Nous allons les utiliser pour chaque fichier de test. Il est logique de créer un fichier de configuration pour ces hooks.

```js
// test-setup.js
const mongoose = require("mongoose");
mongoose.set("useCreateIndex", true);
mongoose.promise = global.Promise;

async function removeAllCollections() {
  const collections = Object.keys(mongoose.connection.collections);
  for (const collectionName of collections) {
    const collection = mongoose.connection.collections[collectionName];
    await collection.deleteMany();
  }
}

async function dropAllCollections() {
  const collections = Object.keys(mongoose.connection.collections);
  for (const collectionName of collections) {
    const collection = mongoose.connection.collections[collectionName];
    try {
      await collection.drop();
    } catch (error) {
      // Parfois cette erreur se produit, mais vous pouvez l'ignorer en toute sécurité
      if (error.message === "ns not found") return;
      // Cette erreur se produit lorsque vous utilisez it.todo. Vous pouvez
      // ignorer cette erreur également
      if (error.message.includes("a background operation is currently running"))
        return;
      console.log(error.message);
    }
  }
}

module.exports = {
  setupDB(databaseName) {
    // Connexion à Mongoose
    beforeAll(async () => {
      const url = `mongodb://127.0.0.1/${databaseName}`;
      await mongoose.connect(url, { useNewUrlParser: true });
    });

    // Nettoie la base de données entre chaque test
    afterEach(async () => {
      await removeAllCollections();
    });

    // Déconnecter Mongoose
    afterAll(async () => {
      await dropAllCollections();
      await mongoose.connection.close();
    });
  }
};
```

Vous pouvez importer le fichier de configuration pour chaque test comme ceci :

```js
const { setupDB } = require("../test-setup");

// Configuration d'une base de données de test
setupDB("endpoint-testing");

// Continuer avec vos tests...
```

Il y a une autre chose que je veux vous montrer.

Lorsque vous créez des tests, vous voulez peupler la base de données avec des données factices.



<h3 id="part3">Peuplement d'une base de données</h3>

Lorsque vous écrivez des tests pour le backend, vous devez tester quatre types d'opérations différents :

1. Créer (pour ajouter des choses à la base de données)
2. Lire (pour obtenir des choses de la base de données)
3. Mettre à jour (pour changer la base de données)
4. Supprimer (pour supprimer des choses de la base de données)

Le type le plus facile à tester est les opérations de création. Vous mettez quelque chose dans la base de données et testez s'il y est.

Pour les trois autres types d'opérations, vous devez mettre quelque chose dans la base de données _avant_ d'écrire le test.

### Mettre des choses dans la base de données

Le processus où vous ajoutez des choses à une base de données est appelé **peuplement d'une base de données**.

Supposons que vous voulez ajouter trois utilisateurs à la base de données. Ces utilisateurs contiennent un nom et une adresse email.

```js
const users = [
  {
    name: "Zell",
    email: "testing1@gmail.com"
  },
  {
    name: "Vincy",
    email: "testing2@gmail.com"
  },
  {
    name: "Shion",
    email: "testing3@gmail.com"
  }
];
```

Vous pouvez utiliser vos modèles pour peupler la base de données au début du test.

```js
const User = require("../model/User"); // Lien vers le modèle User

it("fait quelque chose", async done => {
  // Ajoute des utilisateurs à la base de données
  for (const u of users) {
    const user = new User(u);
    await user.save();
  }

  // Créez le reste de votre test ici
});
```

Si vous avez besoin de ces utilisateurs pour chaque test, la meilleure façon est de les ajouter via le hook `beforeEach`. Le hook `beforeEach` s'exécute avant chaque déclaration `it`.

```js
// Peupler la base de données avec des utilisateurs
beforeEach(async () => {
  for (u of users) {
    const user = new User(u);
    await user.save();
  }
});
```

Vous pouvez également utiliser la fonction `create` de Mongoose pour faire la même chose. Elle exécute `new Model()` et `save()`, donc le code ci-dessous et celui ci-dessus font la même chose.

```js
// Peupler la base de données avec des utilisateurs
beforeEach(async () => {
  await User.create(users);
});
```

### create vs insertMany

Mongoose a une deuxième méthode pour vous aider à peupler la base de données. Cette méthode s'appelle `insertMany`. `insertMany` est plus rapide que `create`, car :

- `insertMany` envoie une opération au serveur
- `create` envoie une opération pour chaque document

Cependant, `insertMany` n'exécute pas le middleware `save`.

#### Est-il important de déclencher le middleware save ?

Cela dépend de vos données de peuplement. Si vos données de peuplement doivent passer par le middleware `save`, vous devez utiliser `create`. Par exemple, supposons que vous voulez enregistrer le mot de passe d'un utilisateur dans la base de données. Vous avez ces données :

```js
const users = [
  {
    name: "Zell",
    email: "testing1@gmail.com",
    password: "12345678"
  },
  {
    name: "Vincy",
    email: "testing2@gmail.com",
    password: "12345678"
  },
  {
    name: "Shion",
    email: "testing3@gmail.com",
    password: "12345678"
  }
];
```

Lorsque nous enregistrons le mot de passe d'un utilisateur dans la base de données, nous voulons hacher le mot de passe pour des raisons de sécurité. Nous hachons généralement le mot de passe via le middleware `save`.

```js
// Hache le mot de passe automatiquement
userSchema.pre("save", async function(next) {
  if (!this.isModified("password")) return next();
  const salt = bcrypt.genSaltSync(10);
  const hashedPassword = bcrypt.hashSync(password, salt);
  this.password = hashedPassword;
});
```

Si vous utilisez `create`, vous obtiendrez des utilisateurs avec des mots de passe hachés :

<figure role="figure"><img src="https://zellwk.com/images/2019/seed-database/create.png" alt="Create exécute le middleware save."></figure>

Si vous utilisez `insertMany`, vous obtiendrez des utilisateurs sans mots de passe hachés :

<figure role="figure"><img src="https://zellwk.com/images/2019/seed-database/insert-many.png" alt="InsertMany n'exécute pas le middleware save."></figure>

### Quand utiliser create, quand utiliser insertMany

Puisque `insertMany` est plus rapide que `create`, vous voulez utiliser `insertMany` chaque fois que vous le pouvez.

Voici comment je le fais :

1. Si les données de peuplement ne nécessitent pas le middleware `save`, utilisez `insertMany`.
2. Si les données de peuplement nécessitent le middleware `save`, utilisez `create`. Ensuite, écrasez les données de peuplement pour qu'elles ne nécessitent plus le middleware `save`.

Pour l'exemple de mot de passe ci-dessus, j'exécuterais d'abord `create`. Ensuite, je copierais-collerais les données de peuplement de mot de passe haché. Ensuite, j'utiliserais `insertMany` à partir de ce point.

Si vous voulez écraser des données de peuplement compliquées, vous pourriez vouloir obtenir du JSON directement de MongoDB. Pour ce faire, vous pouvez utiliser `mongoexport` :

```js
mongoexport --db <databaseName> --collection <collectionName> --jsonArray --pretty --out output.json
```

Cela signifie :

1. Exporter `<collection>` de `<databaseName>`
2. Crée une sortie sous forme de tableau JSON, joliment formaté, dans un fichier appelé `output.json`. Ce fichier sera placé dans le dossier où vous exécutez la commande.

### Peuplement de plusieurs fichiers de test et collections

Vous voulez un endroit pour stocker vos données de peuplement afin de pouvoir les utiliser dans tous vos tests et collections. Voici un système que j'utilise :

1. Je nomme mes fichiers de peuplement selon leurs modèles. Je peuple un modèle `User` avec le fichier `user.seed.js`.
2. Je mets mes fichiers de peuplement dans le dossier `seeds`
3. Je parcours chaque fichier de peuplement pour peupler la base de données.

Pour parcourir chaque fichier de peuplement, vous devez utiliser le module `fs`. `fs` signifie filesystem.

La manière la plus simple de parcourir les fichiers est de créer un fichier `index.js` dans le même dossier `seeds`. Une fois que vous avez le fichier `index.js`, vous pouvez utiliser le code suivant pour rechercher tous les fichiers avec `*.seed.js`

```js
const fs = require("fs");
const util = require("util");

// fs.readdir est écrit avec des callbacks.
// Cette ligne convertit fs.readdir en une promesse
const readDir = util.promisify(fs.readdir);

async function seedDatabase() {
  // Obtient la liste des fichiers dans le répertoire
  // `__dirname` pointe vers le dossier `seeds/`
  const dir = await readDir(__dirname);

  // Obtient une liste de fichiers qui correspondent à *.seed.js
  const seedFiles = dir.filter(f => f.endsWith(".seed.js"));
}
```

Une fois que vous avez une liste de fichiers de peuplement, vous pouvez parcourir chaque fichier de peuplement pour peupler la base de données. Ici, j'utilise une boucle `for...of` pour garder les choses simples.

```js
async function seedDatabase() {
  for (const file of seedFiles) {
    // Peupler la base de données
  }
}
```

Pour peupler la base de données, nous devons trouver le modèle Mongoose correct à partir du nom du fichier de peuplement. Un fichier appelé `user.seed.js` devrait peupler le modèle `User`. Cela signifie :

1. Nous devons trouver `user` à partir de `user.seed.js`
2. Nous devons capitaliser `user` en `User`

Voici une version brute qui fait ce qui est requis. (Si vous le souhaitez, vous pouvez rendre le code plus robuste avec regex au lieu de `split`).

```js
for (const file of seedFiles) {
  const fileName = file.split(".seed.js")[0];
  const modelName = toTitleCase(fileName);
  const model = mongoose.models[modelName];
}
```

Ensuite, nous voulons nous assurer que chaque fichier a un modèle qui lui correspond. Si le modèle ne peut pas être trouvé, nous voulons lancer une erreur.

```js
for (const file of seedFiles) {
  //...
  if (!model) throw new Error(`Impossible de trouver le modèle '${modelName}'`);
}
```

S'il y a un modèle correspondant, nous voulons peupler la base de données avec le contenu du fichier de peuplement. Pour ce faire, nous devons d'abord lire le fichier de peuplement. Ici, puisque j'ai utilisé l'extension `.js`, je peux simplement importer le fichier.

```js
for (const file of seedFiles) {
  //...
  const fileContents = require(path.join(__dirname, file));
}
```

Pour que cela fonctionne, mes fichiers de peuplement doivent exporter un tableau de données.

```js
module.exports = [
  {
    name: "Zell",
    email: "testing1@gmail.com",
    password: "12345678"
  },
  {
    name: "Vincy",
    email: "testing2@gmail.com",
    password: "12345678"
  },
  {
    name: "Shion",
    email: "testing3@gmail.com",
    password: "12345678"
  }
];
```

Une fois que j'ai le contenu du fichier de peuplement, je peux exécuter `create` ou `insertMany`.

```js
async function seedDatabase(runSaveMiddleware = false) {
  // ...
  for (const file of seedFiles) {
    // ...

    runSaveMiddleware
      ? model.create(fileContents)
      : model.insertMany(fileContents);
  }
}
```

Voici le code complet de `seedDatabase` :

```js
const fs = require("fs");
const util = require("util");
const readDir = util.promisify(fs.readdir).bind(fs);
const path = require("path");
const mongoose = require("mongoose");

function toTitleCase(str) {
  return str.replace(/\w\S*/g, txt => {
    return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
  });
}

async function seedDatabase(runSaveMiddleware = false) {
  const dir = await readDir(__dirname);
  const seedFiles = dir.filter(f => f.endsWith(".seed.js"));

  for (const file of seedFiles) {
    const fileName = file.split(".seed.js")[0];
    const modelName = toTitleCase(fileName);
    const model = mongoose.models[modelName];

    if (!model) throw new Error(`Impossible de trouver le modèle '${modelName}'`);
    const fileContents = require(path.join(__dirname, file));

    runSaveMiddleware
      ? await model.create(fileContents)
      : await model.insertMany(fileContents);
  }
}
```

### Pourquoi JS, pas JSON ?

C'est la norme de l'industrie d'utiliser JSON pour stocker des données. Dans ce cas, je trouve plus facile d'utiliser des objets JavaScript car :

1. Je n'ai pas à écrire des guillemets doubles d'ouverture et de fermeture pour chaque propriété.
2. Je n'ai pas à utiliser de guillemets doubles du tout ! (Il est plus facile d'écrire des guillemets simples car il n'est pas nécessaire de presser la touche shift).

```js
// Qu'est-ce qui est plus facile à écrire. Les objets JavaScript ou JSON ?

// Objets JavaScript
module.exports = [
  {
    objectName: "property"
  }
][
  // JSON
  {
    objectName: "property"
  }
];
```

Si vous voulez utiliser JSON, assurez-vous de modifier `seedDatabase` pour qu'il fonctionne avec JSON. (Je vous laisse travailler le code vous-même).

## Ajustement de la fonction setupDB

Plus tôt, j'ai créé une fonction `setupDB` pour aider à configurer les bases de données pour mes tests. `seedDatabase` va dans la fonction `setupDB` puisque le peuplement fait partie du processus de configuration.

```js
async function seedDatabase(runSaveMiddleware = false) {
  // ...
}

module.exports = {
  setupDB(databaseName, runSaveMiddleware = false) {
    // Connexion à Mongoose
    beforeAll(/*...*/);

    // Peupler les données
    beforeEach(async () => {
      await seedDatabase(runSaveMiddleware);
    });

    // Nettoie la base de données entre chaque test
    afterEach(/*...*/);

    // Déconnecter Mongoose
    afterAll(/*...*/);
  }
};
```

### Un dépôt Github

J'ai créé un [dépôt Github][5] pour accompagner cet article. J'espère que ce code de démonstration vous aidera à commencer à tester vos applications.

[1]: https://egghead.io/lessons/javascript-use-jest-s-interactive-watch-mode "Utiliser le mode watch interactif de Jest"
[2]: https://zellwk.com/blog/async-await
[3]: https://github.com/visionmedia/supertest "Supertest"
[4]: https://zellwk.com/blog/local-mongodb
[5]: https://github.com/zellwk/endpoint-testing-example "Exemple de test de point de terminaison"

<hr>

Merci d'avoir lu. Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/endpoint-testing). Inscrivez-vous à [ma newsletter](https://zellwk.com) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.