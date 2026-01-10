---
title: Comment construire une API REST CRUD avec NestJS, Docker, Swagger et Prisma
subtitle: ''
author: Isaiah Clifford Opoku
co_authors: []
series: null
date: '2024-01-23T00:17:33.000Z'
originalURL: https://freecodecamp.org/news/build-a-crud-rest-api-with-nestjs-docker-swagger-prisma
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Nestjs_Free_code.png
tags:
- name: crud
  slug: crud
- name: Docker
  slug: docker
- name: handbook
  slug: handbook
- name: nestjs
  slug: nestjs
- name: REST API
  slug: rest-api
seo_title: Comment construire une API REST CRUD avec NestJS, Docker, Swagger et Prisma
seo_desc: Welcome to this in-depth guide on crafting a RESTful API with NestJS, Docker,
  Swagger, and Prisma. My goal here is to teach you how to build robust and efficient
  backends, regardless of whether you're a seasoned developer or a beginner just dipping
  y...
---

Bienvenue dans ce guide approfondi sur la création d'une API RESTful avec NestJS, Docker, Swagger et Prisma. Mon objectif ici est de vous apprendre à construire des backends robustes et efficaces, que vous soyez un développeur expérimenté ou un débutant qui commence à explorer le monde de la programmation.

Dans ce guide, nous allons créer un système de gestion de recettes. Nous explorerons la puissance de NestJS, Docker, Swagger et Prisma, et utiliserons ces technologies de pointe pour implémenter les opérations CRUD (Create, Read, Update, Delete) pour gérer les recettes.

Mais ce tutoriel n'est pas seulement pour les passionnés de cuisine ou les collectionneurs de recettes. Il s'adresse à toute personne passionnée par l'apprentissage et le développement de ses compétences en développement.

Alors, attachez vos ceintures et préparez-vous pour une aventure passionnante de codage alors que nous plongeons et commençons à construire votre propre système de gestion de recettes ensemble.

Voici ce que nous allons construire :

![API REST ALL](https://www.freecodecamp.org/news/content/images/2024/01/all-for-swagger-end-product.png)
_Un aperçu de l'interface utilisateur Swagger montrant tous les endpoints implémentés._

Et voici ce que nous allons couvrir :

## Table des matières

* [Technologies](#heading-technologies)
* [Prérequis](#heading-prerequisites)
* [Environnement de développement](#heading-development-environment)
* [Comment configurer le projet NestJS](#heading-how-to-set-up-the-nestjs-project)
* [Comment créer une instance PostgreSQL avec Docker](#heading-how-to-create-a-postgresql-instance-with-docker)
* [Comment configurer Prisma](#heading-how-to-set-up-prisma)
* [Comment initialiser Prisma](#heading-how-to-initialize-prisma)
* [Comment définir votre variable d'environnement](#heading-how-to-set-your-environment-variable)
* [Comprendre le schéma Prisma](#heading-understanding-the-prisma-schema)
* [Comment modéliser les données](#heading-how-to-model-the-data)
* [Comment migrer la base de données](#heading-how-to-migrate-the-database)
* [Comment ensemencer la base de données](#heading-how-to-seed-the-database)
* [Comment créer un service Prisma](#heading-how-to-create-a-prisma-service)
* [Comment configurer Swagger](#heading-how-to-set-up-swagger)
* [Comment implémenter les opérations CRUD pour le modèle Recipe](#heading-how-to-implement-crud-operations-for-the-recipe-model)
* [Comment générer des ressources REST avec NestJS CLI](#heading-how-to-generate-rest-resources-with-nestjs-cli)
* [Comment ajouter PrismaClient au module Recipe](#heading-how-to-add-prismaclient-to-the-recipe-module)
* [Comment définir l'endpoint GET /recipes](#heading-how-to-define-the-get-recipes-endpoint)
* [Comment définir l'endpoint GET /recipes/:id](#heading-how-to-define-the-get-recipesid-endpoint)
* [Comment définir l'endpoint POST /recipes](#heading-how-to-define-the-post-recipes-endpoint)
* [Comment définir l'endpoint PATCH /recipes/:id](#heading-how-to-define-the-patch-recipesid-endpoint)
* [Comment définir l'endpoint DELETE /recipes/:id](#heading-how-to-define-the-delete-recipesid-endpoint)
* [Résumé et remarques finales](#heading-summary-and-final-remarks)

## Technologies

Pour construire cette application, nous allons utiliser les outils suivants :

* **[NestJS](https://nestjs.com/)** : Un framework Node.js progressif pour construire des applications côté serveur efficaces, fiables et évolutives.
* **[Prisma](https://www.prisma.io/)** : Une boîte à outils de base de données open-source qui facilite la gestion de vos données et de vos interactions avec elles.
* **[PostgreSQL](https://www.postgresql.org/)** : Un système de gestion de base de données relationnelle objet puissant et open-source.
* **[Docker](https://www.docker.com/)** : Une plateforme ouverte pour développer, expédier et exécuter des applications. Docker vous permet de séparer vos applications de votre infrastructure afin que vous puissiez livrer des logiciels rapidement.
* **[Swagger](https://swagger.io/)** : Un outil pour concevoir, construire et documenter des API RESTful.
* **[TypeScript](https://www.typescriptlang.org/)** : Un sur-ensemble de JavaScript typé statiquement qui ajoute des types optionnels, des classes et des modules au langage.

Chacune de ces technologies joue un rôle crucial dans la création d'une application robuste, évolutive et maintenable. Nous approfondirons chacune d'elles au fur et à mesure.

## Prérequis

### Connaissances supposées

Ce tutoriel est conçu pour être accessible aux débutants, mais je fais quelques hypothèses sur ce que vous savez déjà :

* Les bases de TypeScript
* Les bases de NestJS
* Docker

Si vous n'êtes pas familier avec ces technologies, ne vous inquiétez pas ! Je vous ai couvert. Ce tutoriel vous guidera à travers tout ce que vous devez savoir.

Mais voici quelques ressources supplémentaires si vous souhaitez en apprendre davantage :

* Pour une plongée plus profonde dans NestJS, n'hésitez pas à explorer la [documentation officielle de NestJS](https://docs.nestjs.com/).
* Pour en savoir plus sur Docker, voici un [manuel complet pour les débutants](https://www.freecodecamp.org/news/the-docker-handbook/).
* Et pour plus d'informations sur TypeScript, voici un [cours intensif utile](https://www.freecodecamp.org/news/learn-typescript-with-this-crash-course/).

## Environnement de développement

### Outils et technologies

Dans ce tutoriel, nous utiliserons les outils suivants :

* [Node.js](https://nodejs.org/en/download/) – Notre environnement d'exécution
* [Docker](https://www.docker.com/get-started/) – Pour conteneuriser notre base de données
* [Visual Studio Code](https://code.visualstudio.com/Download) – Notre éditeur de code
* [PostgreSQL](https://www.postgresql.org/download/) – Notre base de données
* [NestJS](https://docs.nestjs.com/) – Notre framework Node.js

**Note :** N'oubliez pas d'installer l'extension Prisma pour Visual Studio Code. Elle améliore votre expérience de codage en mettant en évidence la syntaxe et les mots-clés spécifiques à Prisma.

## Comment configurer le projet NestJS

NestJS est un framework Node.js progressif qui offre de nombreux avantages, notamment une interface de ligne de commande (CLI) puissante. Cette CLI simplifie le processus de création d'une nouvelle application NestJS, rendant facile le démarrage d'un nouveau projet à tout moment et n'importe où.

L'un des principaux avantages de NestJS est son ensemble riche de fonctionnalités intégrées qui simplifient considérablement le processus de développement, rendant votre vie de développeur beaucoup plus facile.

Commençons par installer la CLI NestJS sur votre système :

```bash
npm i -g @nestjs/cli
```

Avec la CLI NestJS installée, vous êtes prêt à créer notre projet de recettes. La CLI simplifie la création d'une nouvelle application NestJS, rendant simple le démarrage.

Pour créer un nouveau projet, exécutez la commande suivante :

```bash
nest new recipe
```

Après avoir exécuté cette commande, vous rencontrerez une invite comme celle que vous voyez ci-dessous :

![Invite du gestionnaire de paquets Nest CLI](https://www.freecodecamp.org/news/content/images/2024/01/Settting-nest.png)
_L'invite de la CLI Nest pour la sélection d'un gestionnaire de paquets lors de la configuration du projet._

Comme illustré dans l'image, la CLI Nest vous demandera de sélectionner un gestionnaire de paquets. Pour ce projet, nous opterons pour `npm`. Une fois que vous avez fait votre sélection, la CLI procédera à la configuration du projet, et vous verrez une série d'opérations s'effectuer dans votre terminal.

Vous pouvez maintenant ouvrir votre projet dans VSCode (ou l'éditeur de votre choix). Vous devriez voir les fichiers suivants :

![Invite du gestionnaire de paquets Nest CLI](https://www.freecodecamp.org/news/content/images/2024/01/After-setting-up-nejst.png)
_La structure des dossiers du projet après sa création à l'aide de la CLI Nest._

Décortiquons la structure du projet :

<table>
<thead>
<tr>
<th>Répertoire/Fichier</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>recipe/</code></td>
<td>Répertoire racine du projet.</td>
</tr>
<tr>
<td><code>├── node_modules/</code></td>
<td>Contient tous les paquets npm requis pour le projet.</td>
</tr>
<tr>
<td><code>├── src/</code></td>
<td>Contient le code source de l'application.</td>
</tr>
<tr>
<td><code>│ ├── app.controller.spec.ts</code></td>
<td>Contient les tests pour <code>app.controller.ts</code>.</td>
</tr>
<tr>
<td><code>│ ├── app.controller.ts</code></td>
<td>Contient un contrôleur de base avec une seule route.</td>
</tr>
<tr>
<td><code>│ ├── app.module.ts</code></td>
<td>Le module racine de l'application.</td>
</tr>
<tr>
<td><code>│ ├── app.service.ts</code></td>
<td>Contient les services utilisés par <code>app.controller.ts</code>.</td>
</tr>
<tr>
<td><code>│ └── main.ts</code></td>
<td>Le point d'entrée de l'application.</td>
</tr>
<tr>
<td><code>├── test/</code></td>
<td>Contient les tests de bout en bout pour l'application.</td>
</tr>
<tr>
<td><code>│ ├── app.e2e-spec.ts</code></td>
<td>Contient les tests de bout en bout pour <code>app.controller.ts</code>.</td>
</tr>
<tr>
<td><code>│ └── jest-e2e.json</code></td>
<td>Contient la configuration pour les tests de bout en bout.</td>
</tr>
<tr>
<td><code>├── README.md</code></td>
<td>Le fichier readme du projet.</td>
</tr>
<tr>
<td><code>├── nest-cli.json</code></td>
<td>Contient la configuration pour la CLI NestJS.</td>
</tr>
<tr>
<td><code>├── package-lock.json</code></td>
<td>Contient les versions exactes des paquets npm utilisés dans le projet.</td>
</tr>
<tr>
<td><code>├── package.json</code></td>
<td>Liste les paquets npm requis pour le projet.</td>
</tr>
<tr>
<td><code>└── tsconfig.build.json</code></td>
<td>Contient les options du compilateur TypeScript pour la construction.</td>
</tr>
</tbody>
</table>

Le répertoire `src` est le centre névralgique de notre application, hébergeant la majeure partie de notre base de code. La CLI NestJS a déjà préparé le terrain pour nous avec plusieurs fichiers clés :

* `src/app.module.ts` : Il s'agit du module racine de notre application, servant de jonction principale pour tous les autres modules.
* `src/app.controller.ts` : Ce fichier contient un contrôleur de base avec une seule route : `/`. Lorsqu'elle est accédée, cette route renvoie un simple message 'Hello World!'.
* `src/main.ts` : Il s'agit de la passerelle vers notre application. Elle est chargée de démarrer et de lancer l'application NestJS.

Pour démarrer votre projet et voir le message 'Hello World!' en action, exécutez la commande suivante :

```bash
npm run start:dev
```

Cette commande déclenche un serveur de développement avec rechargement automatique. Il surveille vigilamment vos fichiers, et s'il détecte des modifications, il recompile automatiquement votre code et rafraîchit le serveur. Cela garantit que vous pouvez voir vos modifications en temps réel, éliminant le besoin de redémarrages manuels.

Pour vérifier que votre serveur est opérationnel, rendez-vous sur `http://localhost:3000/` dans votre navigateur web ou Postman. Vous devriez être accueilli par une page minimaliste affichant le message `Hello World`. Il s'agit de la page d'accueil par défaut de votre application, une toile vierge attendant votre touche créative.

## Comment créer une instance PostgreSQL avec Docker

Pour stocker notre API REST de recettes, nous utiliserons une base de données PostgreSQL. Docker nous aidera à conteneuriser cette base de données, garantissant une configuration et une exécution fluides, quel que soit l'environnement.

Tout d'abord, assurez-vous que Docker est installé sur votre système. Si ce n'est pas le cas, suivez les instructions [ici](https://www.docker.com/get-started).

Ensuite, vous devrez créer un fichier `docker-compose.yml`.

Ouvrez le terminal et exécutez la commande suivante :

```bash
touch docker-compose.yml
```

Cette commande crée un nouveau fichier `docker-compose.yml` dans le répertoire racine de votre projet.

Ouvrez le fichier `docker-compose.yml` et ajoutez le code suivant :

```bash
# docker-compose.yml

version: '3.8'
services:
  postgres:
    image: postgres:13.5
    restart: always
    environment:
      - POSTGRES_USER=recipe
      - POSTGRES_PASSWORD=RecipePassword
    volumes:
      - postgres:/var/lib/postgresql/data
    ports:
      - '5432:5432'
volumes:
  postgres:
```

Voici un bref aperçu de cette configuration :

* `image: postgres:13.5` : Spécifie l'image Docker pour la base de données PostgreSQL.
* `restart: always` : Assure que le conteneur redémarre s'il s'arrête.
* `environment` : Définit le nom d'utilisateur et le mot de passe pour la base de données.
* `volumes` : Monte un volume pour persister les données de la base de données, même si le conteneur est arrêté ou supprimé.
* `ports` : Expose le port `5432` sur la machine hôte et le conteneur pour l'accès à la base de données.

Note : Si vous souhaitez utiliser un port différent, changez simplement le port de la machine hôte. Par exemple, pour utiliser le port `5433`, modifiez la section `ports` comme suit :

```bash
ports:
  - '5444:5432'
```

Note : Avant de continuer, assurez-vous que le port `5432` est libre sur votre machine. Pour démarrer le conteneur PostgreSQL, exécutez la commande suivante dans le répertoire racine de votre projet (et assurez-vous également d'avoir ouvert l'application Docker Desktop et qu'elle est en cours d'exécution) :

```bash
docker-compose up
```

Cette commande lance le conteneur PostgreSQL et le rend accessible sur le port `5432` de votre machine. Si tout se passe comme prévu, vous devriez voir une sortie similaire à celle-ci :

```bash
...
 | PostgreSQL init process complete; ready for start up.
postgres-1  |
postgres-1  | 2024-01-12 14:59:33.519 UTC [1] LOG:  starting PostgreSQL 13.5 (Debian 13.5-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
postgres-1  | 2024-01-12 14:59:33.520 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
postgres-1  | 2024-01-12 14:59:33.520 UTC [1] LOG:  listening on IPv6 address "::", port 5432
postgres-1  | 2024-01-12 14:59:33.526 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
postgres-1  | 2024-01-12 14:59:33.533 UTC [62] LOG:  database system was shut down at 2024-01-12 14:59:33 UTC
postgres-1  | 2024-01-12 14:59:33.550 UTC [1] LOG:  database system is ready to accept connections
```

Rappelez-vous, si vous avez changé le numéro de port, la sortie reflétera le port que vous avez choisi.

Si le port est déjà utilisé, vous rencontrerez un message d'erreur comme celui-ci :

```bash
Error starting userland proxy: listen tcp 0.0.0.0:5432: bind: address already in use
```

Dans un tel cas, libérez le port ou choisissez un autre dans votre fichier `docker-compose.yml`.

Note : si vous fermez la fenêtre du terminal, cela arrêtera également le conteneur. Pour éviter cela, vous pouvez exécuter le conteneur en mode détaché. Ce mode permet au conteneur de s'exécuter indéfiniment en arrière-plan.

Pour ce faire, ajoutez une option `-d` à la fin de la commande, comme suit :

```bash
docker-compose up -d
```

Pour arrêter le conteneur, utilisez la commande suivante :

```bash
docker-compose down
```

Félicitations 🎉. Vous avez maintenant votre propre base de données PostgreSQL avec laquelle jouer.

## Comment configurer Prisma

Maintenant que nous avons notre base de données PostgreSQL en cours d'exécution, nous sommes prêts à configurer Prisma. Prisma est une boîte à outils de base de données open-source qui facilite la gestion de vos données et de vos interactions avec elles.

Prisma est un outil puissant qui offre une large gamme de fonctionnalités, notamment :

* **Migrations de base de données** : Prisma facilite l'évolution de votre schéma de base de données au fil du temps, sans perdre de données.
* **Ensemencement de base de données** : Prisma vous permet d'ensemencer votre base de données avec des données de test.
* **Accès à la base de données** : Prisma fournit une API puissante pour accéder à votre base de données.
* **Gestion du schéma de base de données** : Prisma vous permet de définir votre schéma de base de données en utilisant le langage de schéma Prisma.
* **Requêtes de base de données** : Prisma fournit une API puissante pour interroger votre base de données.
* **Relations de base de données** : Prisma vous permet de définir des relations entre vos tables de base de données.

Vous pouvez en apprendre plus sur Prisma [ici](https://www.prisma.io/).

### Comment initialiser Prisma

Pour commencer avec Prisma, nous devons installer la CLI Prisma. Cette CLI nous permet d'interagir avec notre base de données, facilitant l'exécution des migrations de base de données, l'ensemencement, et plus encore.

Pour installer la CLI Prisma, exécutez la commande suivante :

```bash
npm install prisma -D
```

Cette commande installe la CLI Prisma comme une dépendance de développement dans votre projet. Le drapeau `-D` indique à npm d'installer le package comme une dépendance de développement.

Ensuite, initialisez Prisma dans votre projet en exécutant la commande suivante :

```bash
npx prisma init
```

Cela créera un nouveau répertoire `prisma` avec un fichier `schema.prisma`. Il s'agit du fichier de configuration principal qui contient votre schéma de base de données. Cette commande crée également un fichier `.env` à l'intérieur de votre projet.

### Comment définir votre variable d'environnement

Le fichier `.env` contient les variables d'environnement nécessaires pour se connecter à votre base de données. Ouvrez ce fichier et remplacez le contenu par ce qui suit :

```bash
DATABASE_URL="postgres://recipe:RecipePassword@localhost:5444/recipe"
```

Note : Si vous avez changé le numéro de port dans votre fichier `docker-compose.yml`, assurez-vous de mettre à jour le numéro de port dans la variable d'environnement `DATABASE_URL` avec le numéro de port que vous avez utilisé.

Cette variable d'environnement contient la chaîne de connexion à votre base de données. Elle est utilisée par Prisma pour se connecter à votre base de données dans le conteneur Docker.

### Comprendre le schéma Prisma

Le fichier `schema.prisma` contient le schéma de votre base de données. Il est écrit dans le langage de schéma Prisma, un langage déclaratif pour définir votre schéma de base de données. Le fichier `prisma/schema.prisma` est le fichier de configuration principal pour votre configuration Prisma. Il définit votre connexion de base de données et le générateur de client Prisma.

```ts
// prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}
```

Ce fichier est écrit dans le langage de schéma Prisma, qui est un langage que Prisma utilise pour définir votre schéma de base de données. Le fichier `schema.prisma` a trois composants principaux :

* **Générateur** : Cette section définit le générateur de client Prisma. Le générateur de client Prisma est responsable de la génération du client Prisma, une API puissante pour accéder à votre base de données.
* **Source de données** : Cette section définit la connexion à la base de données. Elle spécifie le fournisseur de base de données et la chaîne de connexion. Elle utilise la variable d'environnement `DATABASE_URL` pour se connecter à votre base de données.
* **Modèle** : Cette section définit le schéma de la base de données. Elle spécifie les tables de la base de données et leurs champs.

## Comment modéliser les données

Maintenant que nous avons configuré notre Prisma, nous sommes prêts à modéliser nos données. Nous allons construire un système de gestion de recettes, donc nous devrons définir un modèle `Recipe`. Ce modèle aura divers champs.

Ouvrez le fichier `schema.prisma` et ajoutez le code suivant :

```ts
// prisma/schema.prisma
// ...
model Recipe {
  id           Int      @id @default(autoincrement())
  title        String   @unique
  description  String?
  ingredients  String
  instructions String
  createdAt    DateTime @default(now())
  updatedAt    DateTime @updatedAt
}
```

Voici un bref aperçu de ce modèle :

* `id` : Il s'agit de la clé primaire du modèle `Recipe`. C'est un entier auto-incrémenté qui identifie de manière unique chaque recette. Il a l'attribut `@id`, qui indique à Prisma que ce champ est la clé primaire. Il a également l'attribut `@default(autoincrement())`, qui indique à Prisma d'auto-incrémenter ce champ.
* `title` : Il s'agit du titre de la recette. C'est une chaîne unique utilisée pour identifier la recette.
* `description` : Il s'agit de la description de la recette. C'est une chaîne optionnelle qui décrit la recette.
* `ingredients` : Il s'agit de la liste des ingrédients utilisés dans la recette. C'est une chaîne qui contient une liste d'ingrédients séparés par des virgules.
* `instructions` : Il s'agit de la liste des instructions pour préparer la recette. C'est une chaîne qui contient une liste d'instructions séparées par des virgules.
* `createdAt` : Il s'agit de la date et de l'heure de création de la recette. Elle est définie à la date et à l'heure actuelles par défaut. Elle a l'attribut `@default(now())`, qui indique à Prisma de définir ce champ à la date et à l'heure actuelles par défaut.
* `updatedAt` : Il s'agit de la date et de l'heure de la dernière mise à jour de la recette. Elle est définie à la date et à l'heure actuelles par défaut.

## Comment migrer la base de données

Maintenant que nous avons défini notre schéma de base de données, nous sommes prêts à migrer notre base de données. Cela créera les tables et les champs de la base de données définis dans notre fichier `schema.prisma`.

Pour migrer votre base de données, exécutez la commande suivante :

```bash
npx prisma migrate dev --name init
```

Cette commande fera trois choses :

**Enregistrer la migration** : Prisma Migrate prendra un instantané de votre schéma et déterminera les commandes SQL nécessaires pour effectuer la migration. Prisma enregistrera le fichier de migration contenant les commandes SQL dans le dossier `prisma/migrations` nouvellement créé.

**Exécuter la migration** : Prisma Migrate exécutera les commandes SQL dans le fichier de migration, créant les tables et les champs de la base de données définis dans votre fichier `schema.prisma`.

**Générer Prisma Client** : Prisma générera Prisma Client basé sur votre dernier schéma. Comme vous n'aviez pas la bibliothèque Client installée, la CLI l'installera également pour vous. Vous devriez voir le package `@prisma/client` dans les dépendances de votre fichier package.json.

Prisma Client est un générateur de requêtes TypeScript généré automatiquement à partir de votre schéma Prisma. Il est adapté à votre schéma Prisma et sera utilisé pour envoyer des requêtes à la base de données.

Si tout se passe comme prévu, vous devriez voir une sortie similaire à celle-ci :

```bash
The following migration(s) have been created and applied from new schema changes:
migrations/
  └─ 20220528101323_init/
    └─ migration.sql
Your database is now in sync with your schema.
...
✓ Generated Prisma Client (3.14.0 | library) to ./node_modules/@prisma/client in 31ms
```

Vérifiez le fichier de migration généré pour avoir une idée de ce que Prisma Migrate fait en arrière-plan :

```bash
-- prisma/migrations/20220528101323_init/migration.sql
CREATE TABLE "Recipe" (
    "id" SERIAL NOT NULL,
    "title" TEXT NOT NULL,
    "description" TEXT,
    "ingredients" TEXT NOT NULL,
    "instructions" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,
    CONSTRAINT "Recipe_pkey" PRIMARY KEY ("id")
);
-- CreateIndex
CREATE UNIQUE INDEX "Recipe_title_key" ON "Recipe"("title");
```

Ce fichier de migration contient les commandes SQL nécessaires pour créer la table `Recipe`. Il contient également les commandes SQL nécessaires pour créer le champ `title`, qui est un champ unique. Cela garantit que le champ `title` est unique, empêchant la création de recettes en double.

## Comment ensemencer la base de données

Maintenant que nous avons migré notre base de données, nous sommes prêts à l'ensemencer avec des données de test. Cela nous permettra de tester notre application sans avoir à créer manuellement des recettes.

Tout d'abord, créez un fichier de seed appelé `prisma/seed.ts`. Ce fichier contiendra les données factices et les requêtes nécessaires pour ensemencer votre base de données.

Ouvrez le terminal et exécutez la commande suivante :

```bash
touch prisma/seed.ts
```

Cette commande crée un nouveau fichier `prisma/seed.ts` dans le répertoire racine de votre projet.

Ensuite, remplissez ce fichier avec le code suivant :

```ts
// prisma/seed.ts
import { PrismaClient } from '@prisma/client';

// initialiser Prisma Client
const prisma = new PrismaClient();

async function main() {
  // créer deux recettes factices
  const recipe1 = await prisma.recipe.upsert({
    where: { title: 'Spaghetti Bolognese' },
    update: {},
    create: {
      title: 'Spaghetti Bolognese',
      description: 'Un plat italien classique',
      ingredients:
        'Spaghetti, viande hachée, 
        sauce tomate, oignons, ail, huile d\'olive, sel, poivre',
      instructions:
        '1. Cuire les spaghetti. 2. Faire revenir la viande hachée. 3.
        Ajouter la sauce tomate à la viande.
        4. Servir les spaghetti avec la sauce.'
    }
  });

  const recipe2 = await prisma.recipe.upsert({
    where: { title: 'Chicken Curry' },
    update: {},
    create: {
      title: 'Chicken Curry',
      description: 'Un plat indien épicé',
      ingredients:
        'Poulet, poudre de curry, oignons, ail, 
        lait de coco, huile d\'olive, sel, poivre',
      instructions:
        '1. Faire revenir le poulet. 2. Ajouter la poudre de curry au
        poulet. 3. Ajouter le lait de coco.
        4. Servir le curry avec du riz.'
    }
  });

  console.log({ recipe1, recipe2 });
}

// exécuter la fonction principale
main()
  .catch(e => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    // fermer Prisma Client à la fin
    await prisma.$disconnect();
  });
```

Ce fichier contient les données factices et les requêtes nécessaires pour ensemencer votre base de données. Décomposons-le :

* `import { PrismaClient } from '@prisma/client';` : Cela importe le Prisma Client, qui est utilisé pour envoyer des requêtes à la base de données.
* `const prisma = new PrismaClient();` : Cela initialise le Prisma Client, nous permettant d'envoyer des requêtes à la base de données.
* `async function main() { ... }` : Il s'agit de la fonction principale qui contient les données factices et les requêtes nécessaires pour ensemencer votre base de données.
* `const recipe1 = await prisma.recipe.upsert({ ... });` : Cela crée une nouvelle recette. Il utilise la méthode `upsert`, qui crée une nouvelle recette si elle n'existe pas, ou met à jour la recette existante si elle existe.
* `const recipe2 = await prisma.recipe.upsert({ ... });` : Cela crée une nouvelle recette. Il utilise la méthode `upsert`, qui crée une nouvelle recette si elle n'existe pas, ou met à jour la recette existante si elle existe.
* `console.log({ recipe1, recipe2 });` : Cela journalise les recettes nouvellement créées dans la console.
* `main().catch((e) => { ... });` : Cela exécute la fonction principale et capture les erreurs qui se produisent.
* `await prisma.$disconnect();` : Cela ferme le Prisma Client à la fin.

Maintenant, avant de pouvoir ensemencer notre base de données, nous devons ajouter un script à notre fichier `package.json`. Ouvrez le fichier `package.json` et ajoutez le script suivant :

```json
// package.json
// ...
  "scripts": {
    // ...
  },
  "dependencies": {
    // ...
  },
  "devDependencies": {
    // ...
  },
  "jest": {
    // ...
  },
  // coller le script prisma ici
  "prisma": {
    "seed": "ts-node prisma/seed.ts"
  }
```

La commande seed exécutera le script `prisma/seed.ts` que vous avez précédemment défini. Cette commande devrait fonctionner automatiquement car ts-node est déjà installé comme dépendance de développement dans votre `package.json`.

Maintenant que nous avons défini notre script de seed, nous sommes prêts à ensemencer la base de données. Pour ensemencer votre base de données, exécutez la commande suivante :

```bash
npx prisma db seed
```

Cette commande ensemencera votre base de données avec les données factices définies dans votre fichier `prisma/seed.ts`. Si tout se passe comme prévu, vous devriez voir une sortie similaire à celle-ci :

```ts
Running seed command `ts-node prisma/seed.ts` ...
{
  recipe1: {
    id: 1,
    title: 'Spaghetti Bolognese',
    description: 'Un plat italien classique',
    ingredients: 'Spaghetti, viande hachée, sauce tomate, oignons, ail, huile d\'olive, sel, poivre',
    instructions: '1. Cuire les spaghetti. 2. Faire revenir la viande hachée. 3. Ajouter la sauce tomate à la viande. 4. Servir les spaghetti avec la sauce.',
    createdAt: 2024-01-12T16:21:09.133Z,
    updatedAt: 2024-01-12T16:21:09.133Z
  },
  recipe2: {
    id: 2,
    title: 'Chicken Curry',
    description: 'Un plat indien épicé',
    ingredients: 'Poulet, poudre de curry, oignons, ail, lait de coco, huile d\'olive, sel, poivre',
    instructions: '1. Faire revenir le poulet. 2. Ajouter la poudre de curry au poulet. 3. Ajouter le lait de coco. 4. Servir le curry avec du riz.',
    createdAt: 2024-01-12T16:21:09.155Z,
    updatedAt: 2024-01-12T16:21:09.155Z
  }
}

The seed command has been executed.
```

Félicitations 🎉. Vous avez maintenant une base de données entièrement fonctionnelle avec des données factices.

## Comment créer un service Prisma

Maintenant que nous avons configuré Prisma, nous sommes prêts à créer un service Prisma. Ce service servira de wrapper autour du Prisma Client, facilitant l'envoi de requêtes à la base de données.

La CLI Nest vous offre un moyen facile de générer des modules et des services directement depuis la CLI. Exécutez la commande suivante dans votre terminal :

```bash
npx nest generate module prisma
npx nest generate service prisma
```

Notez que la commande `generate` peut être raccourcie en `g`. Vous pouvez donc également exécuter la commande suivante :

```bash
npx nest g module prisma
npx nest g service prisma
```

Cette commande génère un nouveau module appelé `prisma` et un nouveau service appelé `prisma`. Elle importe également le `PrismaModule` dans le `AppModule`.

Vous devriez donc voir quelque chose comme ceci :

```bash
src/prisma/prisma.service.spec.ts
src/prisma/prisma.service.ts
src/prisma/prisma.module.ts
```

Note : Dans certains cas, vous devrez peut-être redémarrer votre serveur pour que les modifications prennent effet.

Ensuite, ouvrez le fichier `prisma.service.ts` et remplacez le contenu par ce qui suit :

```ts
// src/prisma/prisma.service.ts
import { Injectable } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class PrismaService extends PrismaClient {}
```

Ce service est un wrapper autour du Prisma Client, facilitant l'envoi de requêtes à la base de données. C'est également un fournisseur NestJS, ce qui signifie qu'il peut être injecté dans d'autres modules.

Ensuite, ouvrez le fichier `prisma.module.ts` et remplacez le contenu par ce qui suit :

```ts
// src/prisma/prisma.module.ts
import { Module } from '@nestjs/common';
import { PrismaService } from './prisma.service';

@Module({
  providers: [PrismaService],
  exports: [PrismaService]
})
export class PrismaModule {}
```

**Note :** Le `PrismaModule` est un module NestJS qui importe le `PrismaService`, le rendant facilement disponible pour une utilisation dans d'autres modules de votre application. Cette configuration permet une intégration transparente du service Prisma dans votre projet.

Félicitations 🎉 ! Vous avez réussi à configurer votre service Prisma.

Avant de plonger dans l'écriture de la logique de notre application, configurons Swagger. Swagger est un outil standard de l'industrie pour concevoir, construire et documenter des API RESTful. Il permet aux développeurs de créer une documentation API élégante et complète sans effort.

## Comment configurer Swagger

Pour configurer Swagger, nous allons utiliser le package `@nestjs/swagger`. Ce package offre une suite de décorateurs et de méthodes spécialement conçus pour générer la documentation Swagger.

Pour installer ce package, exécutez la commande suivante :

```bash
npm install --save @nestjs/swagger swagger-ui-express
```

Cette commande ajoute le package `@nestjs/swagger` comme dépendance dans votre projet. Elle installe également le package `swagger-ui-express`, qui sert l'interface utilisateur Swagger.

Ensuite, accédez au fichier `main.ts` et ajoutez le code suivant :

```ts
// src/main.ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';

// Définir la fonction bootstrap
async function bootstrap() {
  // Créer une instance d'application NestJS en passant le AppModule à NestFactory
  const app = await NestFactory.create(AppModule);

  // Utiliser DocumentBuilder pour créer une nouvelle configuration de document Swagger
  const config = new DocumentBuilder()
    .setTitle('Recipes API') // Définir le titre de l'API
    .setDescription('Recipes API description') // Définir la description de l'API
    .setVersion('0.1') // Définir la version de l'API
    .build(); // Construire le document

  // Créer un document Swagger en utilisant l'instance d'application et la configuration du document
  const document = SwaggerModule.createDocument(app, config);

  // Configurer le module Swagger avec l'instance d'application et le document Swagger
  SwaggerModule.setup('api', app, document);

  // Démarrer l'application et écouter les requêtes sur le port 3000
  await app.listen(3000);
}

// Appeler la fonction bootstrap pour démarrer l'application
bootstrap();
```

Ce code initialise Swagger et génère la documentation Swagger. Décomposons-le :

* `const config = new DocumentBuilder() ... .build();` : Cela crée un nouveau générateur de document Swagger. Il définit le titre, la description et la version du document Swagger. Il construit également le document Swagger.
* `const document = SwaggerModule.createDocument(app, config);` : Cela crée un nouveau document Swagger. Il utilise le générateur de document Swagger pour générer le document Swagger.
* `SwaggerModule.setup('api', app, document);` : Cela configure l'interface utilisateur Swagger. Il utilise le document Swagger pour générer l'interface utilisateur Swagger.

Pendant que l'application est en cours d'exécution, ouvrez votre navigateur et accédez à `http://localhost:3000/api`. Vous devriez voir l'interface utilisateur Swagger.

![Swagger UI](https://www.freecodecamp.org/news/content/images/2024/01/Swager-first-look.png)
_La vue initiale de l'interface utilisateur Swagger après une configuration réussie._

Maintenant que nous avons configuré Swagger, nous sommes prêts à commencer à construire notre API REST.

## Comment implémenter les opérations CRUD pour le modèle Recipe

Dans cette section, nous allons implémenter les opérations CRUD pour le modèle `Recipe`. Nous commencerons par générer les ressources REST pour le modèle `Recipe`. Ensuite, nous ajouterons le client Prisma au module `Recipe`. Enfin, nous implémenterons les opérations CRUD pour le modèle `Recipe`.

### Comment générer des ressources REST avec NestJS CLI

Avant de pouvoir implémenter les opérations CRUD pour le modèle `Recipe`, nous devons générer les ressources REST pour le modèle `Recipe`. Cela créera le code de base pour le module `Recipe`, le contrôleur, le service et les DTO.

Pour générer les ressources REST pour le modèle `Recipe`, exécutez la commande suivante :

```bash
npx nest generate resource recipe
```

Et il vous demandera quel type d'API vous souhaitez générer. Nous allons donc sélectionner `REST API`.

Consultez l'image ci-dessous pour référence :

![REST API](https://www.freecodecamp.org/news/content/images/2024/01/Generating-CRUD.png)
_Sélection de REST API lors de la création des opérations CRUD à l'aide de la CLI Nest_

Cette commande générera les fichiers suivants :

```bash
CREATE src/recipe/recipe.controller.ts (959 bytes)
CREATE src/recipe/recipe.controller.spec.ts (596 bytes)
CREATE src/recipe/recipe.module.ts (264 bytes)
CREATE src/recipe/recipe.service.ts (661 bytes)
CREATE src/recipe/recipe.service.spec.ts (478 bytes)
CREATE src/recipe/dto/create-recipe.dto.ts (33 bytes)
CREATE src/recipe/dto/update-recipe.dto.ts (176 bytes)
CREATE src/recipe/entities/recipe.entity.ts (24 bytes)
UPDATE src/app.module.ts (385 bytes)
```

Si vous ouvrez à nouveau la page de l'API Swagger, vous devriez voir quelque chose comme ceci :

![SWagger UI](https://www.freecodecamp.org/news/content/images/2024/01/swagger-pplo--after-crating-crud.png)
_L'interface utilisateur Swagger affichant les nouvelles opérations CRUD créées._

La page Swagger a maintenant une nouvelle section appelée `Recipe API`. Cette section contient les ressources REST pour le modèle `Recipe`.

Maintenant, lorsque vous ouvrez Swagger, vous verrez quelque chose comme ceci :

* `POST /recipes` : Créer une nouvelle recette.
* `GET /recipes` : Récupérer toutes les recettes.
* `GET /recipes/{id}` : Récupérer une recette spécifique par son ID.
* `PATCH /recipes/{id}` : Mettre à jour une recette spécifique par son ID.
* `DELETE /recipes/{id}` : Supprimer une recette spécifique par son ID.

### Comment ajouter `PrismaClient` au module Recipe

Maintenant que nous avons généré les ressources REST pour le modèle `Recipe`, nous sommes prêts à ajouter le client Prisma au module `Recipe`. Cela nous permettra d'envoyer des requêtes à la base de données.

Tout d'abord, ouvrez le fichier `recipe.module.ts` et ajoutez le code suivant :

```ts
// src/recipes/recipes.module.ts
import { Module } from '@nestjs/common';
import { RecipeService } from './recipe.service';
import { RecipeController } from './recipe.controller';
import { PrismaModule } from '../prisma/prisma.module';

@Module({
  imports: [PrismaModule],
  controllers: [RecipeController],
  providers: [RecipeService]
})
export class RecipeModule {}
```

Nous avons donc importé le `PrismaModule` et l'avons ajouté au tableau `imports`. Cela rendra le `PrismaService` disponible pour le `RecipeService`.

Ensuite, ouvrez le fichier `recipe.service.ts` et ajoutez le code suivant :

```ts
// src/recipes/recipes.service.ts
import { Body, Injectable, Post } from '@nestjs/common';
import { CreateRecipeDto } from './dto/create--recipe.dto';
import { UpdateRecipeDto } from './dto/update--recipe.dto';
import { PrismaService } from 'src/prisma/prisma.service';

@Injectable()
export class RecipesService {
  constructor(private readonly prisma: PrismaService) {}

  //  reste du code
}
```

Nous avons donc défini le service `prisma` comme une propriété privée de la classe `RecipeService`. Cela nous permettra d'accéder au `PrismaService` depuis la classe `RecipeService`. Nous utilisons donc le service `prisma` pour effectuer les opérations CRUD.

Puisque nous avons défini le service pour le modèle Recipe, nous sommes prêts à implémenter les opérations CRUD pour le modèle Recipe.

### Comment définir l'endpoint `GET /recipes`

Commençons notre voyage dans la création d'endpoints API en définissant l'endpoint `GET /recipes`. Cet endpoint servira de passerelle pour récupérer toutes les recettes stockées dans notre base de données.

Dans votre fichier `recipes.controller.ts`, vous trouverez une méthode nommée `findAll`. Cette méthode, comme son nom l'indique, est responsable de la récupération de toutes les recettes. Voici comment nous allons la définir :

```ts
// src/recipes/recipes.controller.ts

// Autre code...

@Get()
async findAll() {
  return await this.recipeService.findAll();
}

// Autre code...
```

Dans le code ci-dessus :

* Le décorateur `@Get()` mappe la méthode `findAll` à l'endpoint `GET /recipes`.
* La méthode `findAll` appelle la méthode `findAll` du `recipeService`, qui récupère toutes les recettes de la base de données.

Comme nous l'avons vu précédemment, le `Controller` est le cœur de la logique de notre application. Dans ce contexte, nous visons à implémenter une méthode `findAll` qui récupère toutes les recettes de notre base de données. Pour y parvenir, nous allons exploiter la puissance des services Prisma dans notre fichier `recipe.service.ts`.

Lorsque vous ouvrez le fichier `recipe.service.ts`, vous verrez quelque chose comme ceci :

```ts
// Autre code...
// src/recipes/recipes.service.ts
 findAll() {
    return `This action returns all recipe`;
  }
// Autre code...
```

Nous allons maintenant remplacer la méthode `findAll` par le code suivant :

```ts
// src/recipes/recipes.service.ts
// Autre code...

async findAll() {
    return this.prisma.recipe.findMany();
}
// Autre code...
```

Dans l'extrait ci-dessus :

* La méthode `findAll` utilise la fonction `findMany` de Prisma pour récupérer toutes les recettes de la base de données.
* Le mot-clé `await` n'est pas nécessaire ici car la fonction `async` enveloppe implicitement la valeur retournée dans une promesse.

Nous avons maintenant implémenté avec succès la méthode de service que notre contrôleur `findAll` utilisera pour récupérer toutes les recettes.

Étant donné que nous avons déjà des données de seed dans notre base de données, l'ouverture de Swagger devrait nous permettre de récupérer toutes les recettes. Voici ce à quoi vous pouvez vous attendre :

![Fetch All Recipes](https://www.freecodecamp.org/news/content/images/2024/01/get-all-recipe-swagger.png)
_L'interface utilisateur Swagger affichant le résultat de l'opération 'Fetch All Recipes'._

Comme illustré dans l'image ci-dessus, notre endpoint `GET /recipes` fonctionne comme prévu, récupérant avec succès toutes les recettes de notre base de données.

Cela marque une étape significative dans notre voyage de construction d'un système de gestion de recettes robuste. Continuons et ajoutons quelques fonctionnalités supplémentaires.

### Comment définir l'endpoint `GET /recipes/{id}`

Concentrons-nous maintenant sur l'endpoint `GET /recipes/{id}`, qui récupère une recette spécifique en fonction de son ID. Pour implémenter cela, nous devrons modifier à la fois le `controller` et le `service`.

Tout d'abord, accédez au fichier `recipes.controller.ts`. Vous y trouverez la méthode `findOne`, qui est définie comme suit :

```ts
// src/recipes/recipes.controller.ts

// autre code ...
@Get(':id')
async findOne(@Param('id') id: string) {
  return await this.recipeService.findOne(+id);
}
// autre code ...
```

Dans ce code :

* Le décorateur `@Get(':id')` mappe à l'endpoint `GET /recipes/{id}`.
* La méthode `findOne` accepte un paramètre `id`, qui est extrait des paramètres de la route.

Ensuite, tournons notre attention vers le fichier `recipes.service.ts`. Vous y trouverez une méthode `findOne` de remplacement :

```ts
// src/recipes/recipes.service.ts
// autre code ...
  findOne(id: number) {
    return `This action returns a #${id} recipe`;
  }

// autre code ...
```

Nous allons remplacer ce remplacement par une méthode qui récupère une recette en fonction de son `id` :

```ts
// src/recipes/recipes.service.ts

findOne(id: number) {
  return this.prisma.recipe.findUnique({
    where: { id },
  });
}
```

Dans ce code :

* La méthode `findOne` prend un `id` comme argument et utilise la fonction `findUnique` de Prisma pour récupérer la recette avec l'`id` correspondant.

Avec les modifications récentes, vous avez débloqué la capacité de récupérer des recettes individuelles par leur ID.

Pour voir cette fonctionnalité en action, accédez à votre page Swagger. Voici un aperçu de ce à quoi vous pouvez vous attendre :

![GET BY ID](https://www.freecodecamp.org/news/content/images/2024/01/Get-by-id.png)
_L'interface utilisateur Swagger affichant le résultat de l'opération 'GET BY ID'._

Ayant atteint cette étape, nous sommes prêts à nous aventurer dans la création de nos propres recettes, en ajoutant à celles existantes dans notre base de données.

### Comment définir l'endpoint `POST /recipes`

La CLI NestJS a commodément généré une méthode `create` pour nous lorsque nous avons créé la ressource pour le modèle `Recipe`. Maintenant, nous devons implémenter la logique de cette méthode dans le fichier `recipe.service.ts`.

Tout d'abord, regardons la méthode `create` dans le fichier `recipe.controller.ts` :
Nous verrons quelque chose comme ceci :

```ts
// src/recipes/recipes.controller.ts

// autre code ...
@Post()
create(@Body() createRecipeDto: CreateRecipeDto) {
  return this.recipesService.create(createRecipeDto);
}
// autre code ...
```

Dans ce code :

* Le décorateur `@Post()` mappe la méthode à l'endpoint `POST /recipes`.
* La méthode `create` accepte un paramètre `createRecipeDto`, qui est extrait du corps de la requête.

La CLI NestJS nous a fourni des fichiers DTO (Data Transfer Object) dans le dossier `recipe`. L'un d'eux, `CreateRecipeDto`, sera notre outil de choix pour valider les données entrantes du client.

**Un rapide rappel sur les DTO** : Si vous êtes nouveau dans le concept des DTO, ce sont essentiellement des objets qui transportent des données entre des processus. Dans le contexte de notre application, nous utiliserons les DTO pour nous assurer que les données que nous recevons sont conformes à nos attentes. Si vous êtes intéressé à approfondir les DTO, consultez ce guide complet [guide](https://docs.nestjs.com/controllers#request-payloads).

Maintenant, implémentons la méthode `create` dans le fichier `recipe.service.ts` pour interagir avec notre base de données.

Mais avant de continuer, utilisons la puissance du dossier DTO (Data Transfer Object), généré par la CLI Nest, pour modéliser nos données.

La classe `CreateRecipeDto`, comme montré ci-dessous, est un exemple typique de DTO. Elle est conçue pour valider les données entrantes du client, en s'assurant qu'elles sont conformes à nos attentes.

```ts
// src/recipes/dto/create-recipe.dto.ts
import { IsString, IsOptional } from 'class-validator';

export class CreateRecipeDto {
  @IsString()
  title: string;

  @IsOptional()
  @IsString()
  description?: string;

  @IsString()
  ingredients: string;

  @IsString()
  instructions: string;
}
```

Dans cette classe, nous utilisons le package `class-validator` pour appliquer la validation des données. Ce package offre une suite de décorateurs, tels que `IsString` et `IsOptional`, que nous avons utilisés pour valider les champs `title`, `description`, `ingredients` et `instructions`.

Avec cette configuration, nous pouvons être confiants que ces champs seront toujours des chaînes de caractères, avec `description` étant optionnel.

Maintenant, implémentons la méthode `create` dans le fichier `recipe.service.ts` pour interagir avec notre base de données. Lorsque vous ouvrez le fichier `recipe.service.ts`, vous verrez quelque chose comme ceci :

```ts
// src/recipes/recipes.service.ts

// autre code ...
  create(createRecipeDto: CreateRecipeDto) {
    return 'This action adds a new recipe';
  }

// autre code ...
```

Remplacez la méthode `create` par le code suivant :

```ts
// src/recipes/recipes.service.ts

// autre code ...
create(createRecipeDto: CreateRecipeDto) {
  return this.prisma.recipe.create({
    data: createRecipeDto,
  });
}
// autre code ...
```

Dans ce code :

* La méthode `create` utilise la fonction `create` de Prisma pour ajouter une nouvelle recette à la base de données. Les données pour la nouvelle recette sont fournies par le `createRecipeDto`.

Avec ces changements, vous pouvez maintenant créer de nouvelles recettes dans votre page Swagger. Voici à quoi vous pouvez vous attendre :

![Creating a Recipe](https://www.freecodecamp.org/news/content/images/2024/01/Creating-POST.png)
_L'interface utilisateur Swagger affichant le processus de création d'une nouvelle recette._

Comme illustré dans l'image ci-dessus, nous avons ajouté avec succès une troisième recette à notre collection. Cela démontre l'efficacité de notre méthode POST dans la création de nouvelles recettes.

### Comment définir l'endpoint `PATCH /recipes/{id}`

Ayant implémenté les endpoints pour créer et récupérer des recettes, concentrons-nous maintenant sur la mise à jour d'une recette. Nous allons implémenter l'endpoint `PATCH /recipes/{id}`, qui met à jour une recette spécifique en fonction de son ID. Cela nécessite des modifications dans le `controller` et le `service`.

Dans le fichier `recipes.controller.ts`, localisez la méthode `update`. Cette méthode est mappée à l'endpoint `PATCH /recipes/{id}` :

```ts
// src/recipes/recipes.controller.ts

// autre code ...
@Patch(':id')
update(@Param('id') id: string, @Body() updateRecipeDto: UpdateRecipeDto) {
  return this.recipesService.update(+id, updateRecipeDto);
}
// autre code ...
```

Dans ce code :

* Le décorateur `@Patch(':id')` mappe la méthode à l'endpoint `PATCH /recipes/{id}`.
* La méthode `update` accepte deux paramètres : `id` (extrait des paramètres de la route) et `updateRecipeDto` (extrait du corps de la requête).

Ensuite, implémentons la méthode `update` dans le fichier `recipe.service.ts`. Lorsque vous ouvrez le fichier `recipe.service.ts`, vous verrez quelque chose comme ceci :

```ts
// src/recipes/recipes.service.ts

// autre code ...
  update(id: number, updateRecipeDto: UpdateRecipeDto) {
    return `This action updates a #${id} recipe`;
  }

// autre code ...
```

Remplacez la méthode `update` par le code suivant :

```ts
// src/recipes/recipes.service.ts

update(id: number, updateRecipeDto: UpdateRecipeDto) {
  return this.prisma.recipe.update({
    where: { id },
    data: updateRecipeDto,
  });
}
```

Dans ce code :

* La méthode `update` utilise la fonction `update` de Prisma pour mettre à jour la recette dans la base de données. La clause `where` spécifie la recette à mettre à jour (en fonction de `id`), et la clause `data` spécifie les nouvelles données pour la recette (fournies par `updateRecipeDto`).

Avec les modifications récentes, nous avons débloqué la capacité de mettre à jour des recettes individuelles par leur ID.

Testons cette nouvelle fonctionnalité en mettant à jour la recette avec un ID de 3.

Voici un aperçu de l'état actuel de la recette :

![Current Recipe Data](https://www.freecodecamp.org/news/content/images/2024/01/by-id3.png)
_Affichage des données actuelles d'une recette spécifique._

Comme illustré ci-dessus, voici les données existantes pour la recette que nous allons mettre à jour.

Après avoir exécuté l'opération de mise à jour, voici comment notre recette se transforme :

![Updated Recipe Data](https://www.freecodecamp.org/news/content/images/2024/01/after-updating-id-3-response.png)
_Affichage des données mises à jour d'une recette spécifique après modification._

Comme vous pouvez le voir, notre opération de mise à jour a modifié avec succès la recette, démontrant l'efficacité de notre nouvelle fonctionnalité implémentée.

Tournez maintenant notre attention vers la suppression des recettes.

### Comment définir l'endpoint `DELETE /recipes/{id}`

Ayant défini avec succès les endpoints `GET`, `POST` et `PATCH`, notre prochaine tâche est d'implémenter l'endpoint `DELETE /recipes/{id}`. Cet endpoint nous permettra de supprimer une recette spécifique en utilisant son ID. Comme pour les endpoints précédents, nous devrons apporter des modifications à la fois dans le `controller` et le `service`.

Dans le fichier `recipes.controller.ts`, nous avons une méthode `remove`. Cette méthode est mappée à l'endpoint `DELETE /recipes/{id}` :

```ts
// src/recipes/recipes.controller.ts

@Delete(':id')
async remove(@Param('id', ParseIntPipe) id: number) {
  return await this.recipesService.remove(id);
}
```

Dans ce code mis à jour :

* Le décorateur `@Delete(':id')` mappe la méthode à l'endpoint `DELETE /recipes/{id}`.
* La méthode `remove` accepte un paramètre `id`, qui est extrait des paramètres de la route et analysé en un nombre à l'aide de `ParseIntPipe`.

Ensuite, implémentons la méthode `remove` dans le fichier `recipe.service.ts`. Maintenant, avec la méthode `remove`, vous voyez ceci :

```ts
// src/recipes/recipes.service.ts
// autre code ...
 @Delete(':id')
  remove(@Param('id') id: string) {
    return this.recipeService.remove(+id);
  }

  // autre code ... 
```

Remplacez la méthode `remove` par ce code :

```ts
// src/recipes/recipes.service.ts


// autre code 
async remove(id: number) {
  return await this.prisma.recipe.delete({
    where: { id },
  });
}

// autre code .. 
```

Dans ce code, la méthode `remove` utilise la fonction `delete` de Prisma pour supprimer la recette avec l'`id` spécifié de la base de données.

Dans ce code :

* La méthode `remove` utilise la fonction `delete` de Prisma pour supprimer la recette avec l'`id` correspondant de la base de données.

Avec ces changements, vous pouvez maintenant supprimer des recettes individuelles par leur ID. Consultez la page Swagger pour voir la documentation de l'API mise à jour.

![Delete Recipe Data](https://www.freecodecamp.org/news/content/images/2024/01/delet-by-id.png)
_Affichage du processus de suppression d'une recette spécifique._

## Résumé et remarques finales

Dans ce manuel, nous avons parcouru le processus de construction d'une API REST en utilisant NestJS et Prisma.

Nous avons commencé par configurer un projet NestJS, configurer une base de données PostgreSQL en utilisant Docker, et intégrer Prisma.

Nous avons ensuite plongé au cœur de notre application, créant un modèle `Recipe` et implémentant les opérations CRUD pour celui-ci. Cela a impliqué la génération de routes RESTful, l'intégration du client Prisma dans notre service `Recipe`, et la création de la logique pour chaque opération.

Ce guide sert de base solide pour vos futurs projets. N'hésitez pas à l'étendre, en ajoutant plus de fonctionnalités pour répondre à vos besoins. Merci de nous avoir suivis, et bon codage !