---
title: Comment gérer les migrations MongoDB avec ts-migrate-mongoose
subtitle: ''
author: Orim Dominic Adah
co_authors: []
series: null
date: '2024-11-27T14:06:04.270Z'
originalURL: https://freecodecamp.org/news/handle-mongodb-migrations-with-ts-migrate-mongoose
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1732615343335/0a1b3e5e-bfa7-4f57-81a7-7f4bac9e8b0a.png
tags:
- name: MongoDB
  slug: mongodb
- name: database
  slug: database
seo_title: Comment gérer les migrations MongoDB avec ts-migrate-mongoose
seo_desc: 'Database migrations are modifications made to a database. These modifications
  may include changing the schema of a table, updating the data in a set of records,
  seeding data or deleting a range of records.

  Database migrations are usually run before a...'
---

Les migrations de base de données sont des modifications apportées à une base de données. Ces modifications peuvent inclure la modification du schéma d'une table, la mise à jour des données dans un ensemble d'enregistrements, le peuplement de données ou la suppression d'une plage d'enregistrements.

Les migrations de base de données sont généralement exécutées avant qu'une application ne démarre et ne s'exécutent pas avec succès plus d'une fois pour la même base de données. Les outils de migration de base de données enregistrent un historique des migrations qui ont été exécutées dans une base de données afin qu'elles puissent être suivies pour des besoins futurs.

Dans cet article, vous apprendrez comment configurer et exécuter des migrations de base de données dans une application API Node.js minimale. Nous utiliserons [ts-migrate-mongoose](https://www.npmjs.com/package/ts-migrate-mongoose) et un script npm pour créer une migration et peupler des données dans une base de données MongoDB. ts-migrate-mongoose prend en charge l'exécution de scripts de migration à partir de code TypeScript ainsi que de code CommonJS.

ts-migrate-mongoose est un framework de migration pour les projets Node.js qui utilisent [mongoose](https://www.npmjs.com/package/mongoose) comme mappeur objet-données. Il fournit un modèle pour écrire des scripts de migration. Il fournit également une configuration pour exécuter les scripts de manière programmatique et à partir de la CLI.

## Table des matières

* [Comment configurer le projet](#heading-comment-configurer-le-projet)
  
* [Comment configurer ts-migrate-mongoose pour le projet](#heading-comment-configurer-ts-migrate-mongoose-pour-le-projet)
  
* [Comment peupler les données utilisateur avec ts-migrate-mongoose](#heading-comment-peupler-les-donnees-utilisateur-avec-ts-migrate-mongoose)
  
* [Comment construire un endpoint API pour récupérer les données peuplées](#heading-comment-construire-un-endpoint-api-pour-recuperer-les-donnees-peuplees)
  
* [Conclusion](#heading-conclusion)
  

## Comment configurer le projet

Pour utiliser ts-migrate-mongoose pour les migrations de base de données, vous devez avoir les éléments suivants :

1. Un projet Node.js avec mongoose installé comme dépendance.
  
2. Une base de données MongoDB connectée au projet.
  
3. MongoDB Compass (Optionnel – pour nous permettre de visualiser les changements dans la base de données).
  

Un dépôt de démarrage qui peut être cloné depuis [ts-migrate-mongoose-starter-repo](https://github.com/orimdominic/ts-migrate-mongoose-starter-repo) a été créé pour faciliter les choses. Clonez le dépôt, remplissez les variables d'environnement et démarrez l'application en exécutant la commande `npm start`.

Visitez [http://localhost:8000](http://localhost:8000) avec un navigateur ou un client API tel que Postman et le serveur retournera un texte "Hello there!" pour montrer que l'application de démarrage fonctionne comme prévu.

## Comment configurer ts-migrate-mongoose pour le projet

Pour configurer ts-migrate-mongoose pour le projet, installez ts-migrate-mongoose avec cette commande :

```bash
npm install ts-migrate-mongoose
```

ts-migrate-mongoose permet la configuration avec un fichier JSON, un fichier TypeScript, un fichier `.env` ou via la CLI. Il est conseillé d'utiliser un fichier `.env` car le contenu de la configuration peut contenir un mot de passe de base de données et il n'est pas approprié d'exposer cela au public. Les fichiers `.env` sont généralement masqués via des fichiers `.gitignore` et sont donc plus sécurisés à utiliser. Ce projet utilisera un fichier `.env` pour la configuration de ts-migrate-mongoose.

Le fichier doit contenir les clés suivantes et leurs valeurs :

* `MIGRATE_MONGO_URI` - l'URI de la base de données Mongo. Il est identique à l'URL de la base de données.
  
* `MIGRATE_MONGO_COLLECTION` - le nom de la collection (ou table) dans laquelle les migrations doivent être enregistrées. La valeur par défaut est migrations, ce qui est utilisé dans ce projet. ts-migrate-mongoose enregistre les migrations dans MongoDB.
  
* `MIGRATE_MIGRATIONS_PATH` - le chemin vers le dossier pour stocker et lire les scripts de migration. La valeur par défaut est `./migrations`, ce qui est utilisé dans ce projet.
  

## Comment peupler les données utilisateur avec ts-migrate-mongoose

Nous avons réussi à créer un projet et à le connecter avec succès à une base de données Mongo. À ce stade, nous voulons peupler des données utilisateur dans la base de données. Nous devons :

1. Créer une collection (ou table) d'utilisateurs
  
2. Utiliser ts-migrate-mongoose pour créer un script de migration pour peupler les données
  
3. Utiliser ts-migrate-mongoose pour exécuter la migration afin de peupler les données utilisateur dans la base de données avant que l'application ne démarre
  

### 1. Créer une collection d'utilisateurs avec Mongoose

Le schéma Mongoose peut être utilisé pour créer une collection (ou table) d'utilisateurs. Les documents utilisateur (ou enregistrements) auront les champs (ou colonnes) suivants : `email`, `favouriteEmoji` et `yearOfBirth`.

Pour créer un schéma Mongoose pour la collection d'utilisateurs, créez un fichier `user.model.js` à la racine du projet contenant le code suivant :

```javascript
const mongoose = require("mongoose");

const userSchema = new mongoose.Schema(
  {
    email: {
      type: String,
      lowercase: true,
      required: true,
    },
    favouriteEmoji: {
      type: String,
      required: true,
    },
    yearOfBirth: {
      type: Number,
      required: true,
    },
  },
  {
    timestamps: true,
  }
);

module.exports.UserModel = mongoose.model("User", userSchema);
```

### 2. Créer un script de migration avec ts-migrate-mongoose

ts-migrate-mongoose fournit des commandes CLI qui peuvent être utilisées pour créer des scripts de migration.

L'exécution de `npx migrate create <nom-du-script>` dans le dossier racine du projet créera un script dans le dossier `MIGRATE_MIGRATIONS_PATH` (`./migrations` dans notre cas). `<nom-du-script>` est le nom que nous voulons donner au fichier de script de migration lorsqu'il est créé.

Pour créer un script de migration pour peupler les données utilisateur, exécutez :

```bash
npx migrate create seed-users
```

La commande créera un fichier dans le dossier `./migrations` avec un nom de la forme `-<timestamp>-seed-users.ts`. Le fichier contiendra le code suivant :

```ts
// Importez vos modèles ici

export async function up (): Promise<void> {
  // Écrivez la migration ici
}

export async function down (): Promise<void> {
  // Écrivez la migration ici
}
```

La fonction `up` est utilisée pour exécuter la migration. La fonction `down` est utilisée pour inverser ce que la fonction `up` exécute, si nécessaire. Dans notre cas, nous essayons de peupler des utilisateurs dans la base de données. La fonction `up` contiendra le code pour peupler les utilisateurs dans la base de données et la fonction `down` contiendra le code pour supprimer les utilisateurs créés dans la fonction `up`.

Si la base de données est inspectée avec MongoDB Compass, la collection migrations aura un document qui ressemble à ceci :

```json
{
  "_id": ObjectId("6744740465519c3bd9c1a7d1"),
  "name": "seed-users",
  "state": "down",
  "createdAt": 2024-11-25T12:56:36.316+00:00,
  "updatedAt": 2024-11-25T12:56:36.316+00:00,
  "__v": 0
}
```

Le champ `state` du document de migration est défini sur `down`. Après son exécution réussie, il passe à `up`.

Vous pouvez mettre à jour le code dans `./migrations/<timestamp>-seed-users.ts` avec celui du snippet ci-dessous :

```typescript
require("dotenv").config() // charge les variables d'environnement
const db = require("../db.js")
const { UserModel } = require("../user.model.js");

const seedUsers = [
  { email: "john@email.com", favouriteEmoji: "\ud83c\udfc3", yearOfBirth: 1997 },
  { email: "jane@email.com", favouriteEmoji: "\ud83c\udf4f", yearOfBirth: 1998 },
];

export async function up (): Promise<void> {
  await db.connect(process.env.MONGO_URI)
  await UserModel.create(seedUsers);}

export async function down (): Promise<void> {
  await db.connect(process.env.MONGO_URI)
  await UserModel.delete({
    email: {
      $in: seedUsers.map((u) => u.email),
    },
  });
}
```

### 3. Exécuter la migration avant que l'application ne démarre

ts-migrate-mongoose nous fournit des commandes CLI pour exécuter les fonctions `up` et `down` des scripts de migration.

Avec `npx migrate up <nom-du-script>` nous pouvons exécuter la fonction `up` d'un script spécifique. Avec `npx migrate up` nous pouvons exécuter la fonction `up` de tous les scripts dans le dossier `./migrations` avec un `state` de `down` dans la base de données.

Pour exécuter la migration avant que l'application ne démarre, nous utilisons des scripts npm. Les scripts npm avec un préfixe `pre` s'exécuteront avant un script sans le préfixe `pre`. Par exemple, s'il y a un script `dev` et un script `predev`, chaque fois que le script `dev` est exécuté avec `npm run dev`, le script `predev` s'exécutera automatiquement avant le script `dev`.

Nous utiliserons cette fonctionnalité des scripts npm pour placer la commande ts-migrate-mongoose dans un script `prestart` afin que la migration s'exécute avant le script `start`.

Mettez à jour le fichier `package.json` pour avoir un script `prestart` qui exécute la commande ts-migrate-mongoose pour exécuter la fonction `up` des scripts de migration dans le projet.

```json
  "scripts": {
    "prestart": "npx migrate up",
    "start": "node index.js"
  },
```

Avec cette configuration, lorsque `npm run start` est exécuté pour démarrer l'application, le script `prestart` s'exécutera pour exécuter la migration en utilisant ts-migrate-mongoose et peupler la base de données avant que l'application ne démarre.

Vous devriez avoir quelque chose de similaire au snippet ci-dessous après avoir exécuté `npm run start` :

```bash
Synchronizing database with file system migrations...
MongoDB connection successful
up: 1732543529744-seed-users.ts 
All migrations finished successfully

> ts-migrate-mongoose-starter-repo@1.0.0 start
> node index.js

MongoDB connection successful                      
Server listening on port 8000
```

Consultez la branche [seed-users](https://github.com/orimdominic/ts-migrate-mongoose-starter-repo/tree/seed-users) du dépôt pour voir l'état actuel de la base de code à ce stade de l'article.

## Comment construire un endpoint API pour récupérer les données peuplées

Nous pouvons construire un endpoint API pour récupérer les données des utilisateurs peuplées dans notre base de données. Dans le fichier `server.js`, mettez à jour le code avec celui du snippet ci-dessous :

```javascript
const { UserModel } = require("./user.model.js")

module.exports = async function (req, res) {
  const users = await UserModel.find({}) // récupère tous les utilisateurs dans la base de données

  res.writeHead(200, { "Content-Type": "application/json" });
  return res.end(JSON.stringify({ // retourne une représentation JSON des données des utilisateurs récupérées
    users: users.map((u) => ({
      email: u.email,
      favouriteEmoji: u.favouriteEmoji,
      yearOfBirth: u.yearOfBirth,
      createdAt: u.createdAt
    }))
  }, null, 2));
};
```

Si nous démarrons l'application et visitons [http://localhost:8000](http://localhost:8000) en utilisant Postman ou un navigateur, nous obtenons une réponse JSON similaire à celle ci-dessous :

```json
{
  "users": [
    {
      "email": "john@email.com",
      "favouriteEmoji": "\ud83c\udfc3",
      "yearOfBirth": 1997,
      "createdAt": "2024-11-25T14:18:55.416Z"
    },
    {
      "email": "jane@email.com",
      "favouriteEmoji": "\ud83c\udf4f",
      "yearOfBirth": 1998,
      "createdAt": "2024-11-25T14:18:55.416Z"
    }
  ]
}
```

Remarquez que si l'application est exécutée à nouveau, le script de migration ne s'exécute plus car l'état de la migration sera maintenant `up` après son exécution réussie.

Consultez la branche [fetch-users](https://github.com/orimdominic/ts-migrate-mongoose-starter-repo/tree/fetch-users) du dépôt pour voir l'état actuel de la base de code à ce stade de l'article.

## Conclusion

Les migrations sont utiles lors de la construction d'applications et il est nécessaire de peupler des données initiales pour les tests, de peupler des utilisateurs administratifs, de mettre à jour le schéma de la base de données en ajoutant ou en supprimant des colonnes et de mettre à jour les valeurs des colonnes dans de nombreux enregistrements à la fois.

ts-migrate-mongoose peut aider à fournir un framework pour exécuter des migrations pour vos applications Node.js si vous utilisez Mongoose avec MongoDB.