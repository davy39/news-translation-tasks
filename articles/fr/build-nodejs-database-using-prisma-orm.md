---
title: Comment construire une base de données Node.js avec Prisma et SQLite
subtitle: ''
author: Gaël Thomas
co_authors: []
series: null
date: '2021-08-11T15:24:42.000Z'
originalURL: https://freecodecamp.org/news/build-nodejs-database-using-prisma-orm
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/manage-node-js-database-prisma-orm.png
tags:
- name: database
  slug: database
- name: node js
  slug: node-js
- name: SQLite
  slug: sqlite
seo_title: Comment construire une base de données Node.js avec Prisma et SQLite
seo_desc: 'Lately I''ve been seeing many tweets and articles about Prisma. It''s a
  modern ORM (Object-Relational-Mapping tool) that works with Node.jsand TypeScript.

  Yes, this library will help you build and manage your Node.js database – and it''s
  compatible with...'
---

Récemment, j'ai vu de nombreux tweets et articles sur [Prisma](https://www.prisma.io/). C'est un ORM (Outil de Mappage Objet-Relationnel) moderne qui fonctionne avec Node.js et TypeScript.

Oui, cette bibliothèque vous aidera à construire et gérer votre base de données Node.js – et elle est compatible avec TypeScript ! Elle générera automatiquement tous les types de vos entités.

La définition du schéma est facile à lire pour les humains – plus de maux de tête là-dessus. Vous verrez comment cela fonctionne dans les sections à venir.

De plus, l'ORM fonctionne bien avec Next.js, GraphQL, Nest.Js, Express.js, Apollo et Hapi.

Pour résumer, Prisma est un ORM moderne qui s'intègre bien avec toutes les piles technologiques tendances.

C'est pourquoi j'ai décidé de l'essayer et de remplacer ma précédente bibliothèque de gestion de base de données : [TypeORM](https://typeorm.io/).

> "Prisma aide les développeurs d'applications à construire plus rapidement et à faire moins d'erreurs avec un ORM open source pour PostgreSQL, MySQL et SQLite." – [Page d'accueil de Prisma](https://www.prisma.io/)

## Construisons une base de données Twitter simple en utilisant Node, Prisma et SQLite

Il est temps de pratiquer. Je vais vous montrer comment construire votre première base de données Node.js en utilisant Prisma. Pour garder cette introduction accessible, nous utiliserons Node avec SQLite.

SQLite est un moteur de base de données autonome. Cela signifie que vous n'avez pas besoin de configurer une base de données sur votre ordinateur. Le projet fonctionnera par lui-même si vous suivez les étapes de ce tutoriel.

Si, à l'avenir, vous souhaitez utiliser Prisma avec une base de données PostgreSQL, voici un [tutoriel sur la création d'une base de données PostgreSQL en utilisant Docker-Compose](https://herewecode.io/blog/create-a-postgresql-database-using-docker-compose/).

### Prérequis

* **Node.js (12.2 ou supérieur)**

Avant de commencer, prenez le temps de vérifier si vous avez la version 12.2 ou supérieure de [Node.js](https://nodejs.org/en/). Si ce n'est pas le cas, mettez simplement à jour votre Node avant de commencer la section suivante.

> **Note :** Si vous voulez vérifier votre version de Node.js, vous pouvez taper : `node -v` dans un terminal. La sortie sera la version.

* **Connaissances de base en SQL**

Bien que j'adopte une approche simple pour cette nouvelle bibliothèque, je recommande d'avoir des connaissances de base en SQL pour comprendre pleinement le tutoriel.

> **Note :** Vous n'avez pas besoin d'être un expert ! Seules les bases comme la création d'une table et l'exécution de quelques requêtes sont essentielles ici.

## Comment configurer un projet Twitter de base

Tout d'abord, vous devez créer un nouveau dossier pour ce projet et vous y déplacer :

```shell
$ mkdir minimalistic-twitter
$ cd minimalistic-twitter
```

Ensuite, nous installerons toutes les dépendances obligatoires telles que TypeScript et Prisma.

```shell
$ npm init -y
$ npm install prisma typescript ts-node @types/node --save-dev
$ npm install @prisma/client
```

Désormais, vous devriez voir un dossier `node_modules` et un fichier `package.json` dans votre dépôt.

Avant de passer à l'initialisation de Prisma, la dernière étape de configuration consiste à créer une configuration pour TypeScript à la racine du dépôt.

Pour ce faire, vous pouvez créer un fichier `tsconfig.json` et coller la configuration suivante :

```json
{
  "compilerOptions": {
    "sourceMap": true,
    "outDir": "dist",
    "strict": true,
    "lib": ["esnext"],
    "esModuleInterop": true
  }
}
```

Nous y voilà ! Il est temps d'utiliser Prisma dans notre projet. Dans le dossier `minimalistic-twitter`, vous pouvez utiliser la commande suivante pour afficher l'aide de Prisma.

```shell
$ npx prisma
```

Maintenant, la dernière étape avant de construire notre application Twitter minimaliste est d'initialiser la configuration de la base de données.

Nous utiliserons la commande `init` mais avec un paramètre `--datasource-provider` pour définir le type de base de données. Sinon, par défaut, `init` créera une base de données PostgreSQL.

```shell
$ npx prisma init --datasource-provider sqlite
```

Lorsque la commande aura fini de s'exécuter, vous devriez trouver dans votre dépôt un fichier `.env` et un dossier `prisma` avec un fichier `schema.prisma` à l'intérieur.

Le fichier `schema.prisma` contient toutes les instructions pour se connecter à votre base de données. Plus tard, il inclura également les instructions pour générer vos tables de base de données.

Le fichier `.env` contient toutes les variables d'environnement dont votre projet a besoin pour fonctionner. Pour Prisma, la seule variable est `DATABASE_URL`. Sa valeur est définie sur `./dev.db`.

Le fichier `dev.db` sera le fichier de base de données autonome.

![Arborescence du projet après l'initialisation du projet](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-at-23.56.14.png)
_Arborescence du projet après l'initialisation du projet_

Si vous avez la même sortie, félicitations, cela signifie que votre projet est prêt ! 🎉

## Comment construire notre premier modèle – Utilisateur

Notre base de données Twitter de base se composera de deux entités principales :

* Une entité utilisateur avec les informations de l'utilisateur et ses tweets
* Une entité tweet avec le contenu du tweet et son auteur

Tout d'abord, nous nous concentrerons sur la création de l'entité utilisateur. Chacun d'eux a :

* un id
* un email unique (deux utilisateurs ne peuvent pas avoir le même email)
* un nom d'utilisateur
* une liste de tweets

Avec Prisma, si nous voulons définir un nouveau schéma (modèle), nous devons le faire dans le fichier `schema.prisma`.

Pour définir une entité, nous utiliserons l'instruction `model` comme ci-dessous. Vous pouvez la reproduire après l'instruction de connexion à la base de données dans votre fichier `schema.prisma`.

```typescript
// Après la connexion à la base de données

model User {
  // Nous définissons une variable `id`
  // Avec un type `Int` (nombre)
  // Ensuite, nous définissons les décorateurs Prisma :
  // - @id (parce que c'est un ID)
  // - @default(autoincrement()) (valeur par défaut est auto-incrémentée)
  id Int @id @default(autoincrement())

  // Nous définissons une variable `email`
  // Avec un type `String`
  // Ensuite, nous définissons le décorateur Prisma :
  // - @unique (parce que nous voulons que l'utilisateur soit unique
  // basé sur l'email - deux utilisateurs ne peuvent pas avoir le même)
  email String @unique

  // Nous définissons une variable `username`
  // Avec un type `String`
  username String

  // Nous définissons une variable `tweets`
  // Avec un type `Tweet[]` (relation un-à-plusieurs)
  // Parce que chaque utilisateur peut avoir entre
  // 0 et un nombre infini de tweets
  tweets Tweet[]
}
```

Comme vous l'avez peut-être remarqué, nous n'avons pas encore le modèle `Tweet`. Ce sera notre prochaine étape.

## Comment construire notre deuxième modèle – Tweet

Maintenant que nous avons des utilisateurs, nous avons besoin de tweets. Suivons le même processus que précédemment, mais cette fois pour l'entité `Tweet`.

Chacun d'eux a :

* un id
* une date de création
* un texte
* un userId (auteur du tweet)

Ci-dessous, vous trouverez l'entité. Vous pouvez la reproduire après la déclaration du modèle `User` dans votre fichier `schema.prisma`.

```typescript
// Après la connexion à la base de données

// Après le modèle User

model Tweet {
  // Nous définissons une variable `id`
  // Avec un type `Int` (nombre)
  // Ensuite, nous définissons les décorateurs Prisma :
  // - @id (parce que c'est un ID)
  // - @default(autoincrement()) (valeur par défaut est auto-incrémentée)
  id Int @id @default(autoincrement())

  // Enregistre l'heure de création du tweet
  createdAt DateTime @default(now())

  // Nous définissons une variable `text`
  // Avec un type `String`
  text String

  // Nous définissons une variable `userId`
  // Avec un type `Int` (nombre)
  // Il reliera l'`id` du modèle `User`
  userId Int

  // Nous définissons une variable `user`
  // Avec un type `User` (relation plusieurs-à-un)
  // Parce que chaque tweet a un auteur
  // Cet auteur est un `User`
  // Nous relions le `User` à un `Tweet` basé sur :
  // - le `userId` dans le modèle `Tweet`
  // - l'`id` dans le modèle `User`
  user User @relation(fields: [userId], references: [id])
}

```

## Comment générer notre première migration de base de données

La première chose que nous devons faire avant d'utiliser notre base de données est de la générer. Pour ce faire, nous utiliserons une autre commande de l'interface de ligne de commande de Prisma. Cette commande nous permettra de créer des migrations.

Si nous regardons la documentation sur la commande `migrate`, nous verrons ce qui suit :

> "Prisma Migrate est un outil de migration de schéma de base de données impératif qui vous permet de : **Garder votre schéma de base de données synchronisé avec votre schéma Prisma au fur et à mesure qu'il évolue et maintenir les données existantes dans votre base de données**." – [Documentation de Prisma migrate](https://www.prisma.io/docs/concepts/components/prisma-schema/)

L'idée ici est de sauvegarder notre première implémentation de base de données. Vous pouvez le faire en tapant la commande ci-dessous dans votre terminal :

```shell
npx prisma migrate dev --name initialize
```

**Note :** Vous pouvez entrer le nom de votre choix après le paramètre `--name`. Gardez à l'esprit que le nom de la migration est utile pour se souvenir des changements que vous avez apportés.

Si votre commande de migration est réussie, cela signifie que toutes les instructions dans `schema.prisma` sont correctes. ✅

Votre arborescence de projet devrait maintenant être similaire à l'image ci-dessous (à l'exception du hash de migration).

![Arborescence du projet après la génération de la migration](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-08-at-00.41.22.png)
_Arborescence du projet après la génération de la migration_

**Note :** Dans le fichier `migration.sql`, vous trouverez les requêtes SQL pour générer votre base de données.

Votre base de données est prête ! 🚀 Il est temps de l'essayer, d'ajouter des utilisateurs et de les laisser tweeter.

## Comment tester notre projet Node JS SQLite

Alors, les utilisateurs pourront-ils maintenant tweeter ? Essayons d'exécuter quelques requêtes sur notre base de données. Nous créerons un fichier `index.ts` à la racine du dépôt et nous y écrirons quelques instructions.

Tout d'abord, nous devons importer et initialiser la connexion à la base de données. Basé sur la [documentation de démarrage rapide de Prisma](https://www.prisma.io/docs/getting-started/quickstart/), nous créons une variable `prisma` pour interagir avec la base de données et une fonction pour écrire notre code de test :

```typescript
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

async function main() {}

main()
  .catch((e) => {
    throw e;
  })
  .finally(async () => {
    await prisma.$disconnect();
  });

```

Nous sommes prêts à remplir la fonction `main` avec quelques instructions.

```typescript
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

async function main() {
  // Nous créons un nouvel utilisateur
  const newUser = await prisma.user.create({
    data: {
      email: "hello@herewecode.io",
      username: "gaelgthomas", // <- c'est aussi mon nom d'utilisateur Twitter 😄
    },
  });

  console.log("Nouvel utilisateur :");
  console.log(newUser);

  // Nous créons un nouveau tweet et nous le lions à notre nouvel utilisateur
  const firstTweet = await prisma.tweet.create({
    data: {
      text: "Bonjour le monde !",
      userId: newUser.id,
    },
  });

  console.log("Premier tweet :");
  console.log(firstTweet);

  // Nous récupérons le nouvel utilisateur à nouveau (par son adresse email unique)
  // et nous demandons à récupérer ses tweets en même temps
  const newUserWithTweets = await prisma.user.findUnique({
    where: {
      email: "hello@herewecode.io",
    },
    include: { tweets: true },
  });

  console.log("Objet utilisateur avec Tweets :");
  console.dir(newUserWithTweets);
}

main()
  .catch((e) => {
    throw e;
  })
  .finally(async () => {
    await prisma.$disconnect();
  });

```

**Note :** Si vous voulez découvrir les différentes instructions que vous pouvez utiliser, une bonne page de documentation Prisma est [celle sur les opérations CRUD](https://www.prisma.io/docs/concepts/components/prisma-client/crud).

Il est temps d'exécuter le fichier `index.ts`.

Avant de le faire, ouvrez votre fichier `package.json` et cherchez la section `scripts`. Vous devrez ajouter une commande pour démarrer le projet en utilisant `ts-node`.

Si vous le souhaitez, vous pouvez remplacer votre section `scripts` par le code suivant :

```json
"scripts": {
  "dev": "ts-node ./index.ts",
  "test": "echo \"Error: no test specified\" && exit 1"
},
```

Ensuite, dans votre terminal, vous pouvez taper la commande ci-dessous et lire la sortie pour voir si tout fonctionne bien :

```shell
$ npm run dev
```

**Note :** Dans la commande ci-dessus, nous exécutons le script dev de notre package.json.

![Sortie du test NPM utilisant Prisma](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-08-at-01.04.59.png)
_Sortie du test NPM utilisant Prisma_

Cela fonctionne ! Vous avez obtenu votre premier utilisateur et tweet. 👍 Maintenant que vous avez configuré votre première base de données en utilisant Prisma, vous pouvez y ajouter des fonctionnalités. Voici quelques idées :

* ajouter plus d'informations dans l'entité Utilisateur (date de naissance, adresse, biographie, etc.)
* ajouter un système de likes (chaque tweet peut avoir des likes, chaque utilisateur peut avoir une liste de tweets aimés)

### **Le code est disponible sur GitHub – Node JS avec Prisma et SQLite**

Si vous voulez obtenir le code complet, vous pouvez le trouver sur mon GitHub.

**->** [GitHub : Exemple Prisma SQLite](https://github.com/gaelgthomas/prisma-sqlite-example)

**Merci d'avoir lu jusqu'à la fin !**

J'espère que vous utiliserez Prisma dans l'un de vos prochains projets. 🎉

Je commence à tweeter plus régulièrement. Si vous voulez obtenir plus de conseils et de ressources sur la programmation web -> [Retrouvez-moi sur mon Twitter 🐦](https://twitter.com/gaelgthomas)