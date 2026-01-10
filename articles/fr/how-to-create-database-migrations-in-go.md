---
title: Comment créer des migrations de base de données en Go avec Docker et Postgres
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-06-26T11:40:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-database-migrations-in-go
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/fotis-fotopoulos-DuHKoV44prg-unsplash.jpg
tags:
- name: Docker
  slug: docker
- name: Go Language
  slug: go
- name: postgres
  slug: postgres
seo_title: Comment créer des migrations de base de données en Go avec Docker et Postgres
seo_desc: 'By Okure U. Edet

  Go is a fast programming language with a relatively simple syntax. While learning
  Go, it is important to learn how to build APIs and how to use them to communicate
  with databases. In the process of learning, I decided to take on a pr...'
---

Par Okure U. Edet

Go est un langage de programmation rapide avec une syntaxe relativement simple. En apprenant Go, il est important d'apprendre à construire des API et à les utiliser pour communiquer avec des bases de données. Dans le cadre de mon apprentissage, j'ai décidé de me lancer dans un projet qui m'a aidé à cet égard : une API simple de suivi d'inventaire.

En travaillant avec une base de données SQL comme Postgres, j'ai appris qu'il est important d'apporter des modifications à la base de données de manière opportune. Ainsi, si vous avez un schéma que vous pourriez modifier à l'avenir, la meilleure façon de procéder est d'utiliser des migrations de base de données. Cela garantit que les modifications apportées à la base de données sont effectuées avec précision sans affecter les données existantes.

Dans cet article, vous apprendrez à effectuer des migrations de base de données en utilisant Docker et Postgres.

## Table des matières
- [Qu'est-ce que la migration de base de données ?](#quest-ce-que-la-migration-de-base-de-donnees)
- [Comment démarrer et exécuter un conteneur Docker](#comment-demarrer-et-executer-un-conteneur-docker)
- [Comment créer et exécuter un schéma avec TablePlus](#comment-creer-et-executer-un-schema-avec-tableplus)
- [Comment installer golang-migrate](#comment-installer-golang-migrate)
- [Comment créer une nouvelle migration](#comment-creer-une-nouvelle-migration)
- [Comment créer et supprimer la base de données à l'intérieur et à l'extérieur d'un conteneur Docker Postgres](#comment-creer-et-supprimer-la-base-de-donnees-a-linterieur-et-a-lextérieur-dun-conteneur-docker-postgres)
- [Comment visualiser la base de données dans TablePlus](#comment-visualiser-la-base-de-donnees-dans-tableplus)
- [Comment exécuter les migrations](#comment-executer-les-migrations)
- [Conclusion](#heading-conclusion)

## Qu'est-ce que la migration de base de données ?

Qu'est-ce que la migration de base de données et pourquoi devriez-vous l'utiliser ? Eh bien, en tant que développeur backend, lorsque vous travaillez sur un projet qui nécessite de stocker des données dans une base de données, vous devrez développer un schéma pour les données que vous souhaitez stocker.

Les migrations de base de données vous aident à gérer la structure des données au sein d'une base de données et, dans ce cas, d'une base de données relationnelle. Les migrations aident à modifier les schémas d'un état actuel à un état spécifique/souhaité. Cela peut impliquer l'ajout de tables et de colonnes, la suppression d'éléments ou la modification de types et de contraintes.

L'un des avantages de la migration de base de données est de rendre les changements dans une base de données répétables et fluides sans craindre la perte de données.

Il est conseillé d'utiliser les migrations si vous n'êtes pas sûr de l'apparence de votre schéma de données final. Dans ce sens, vous pouvez implémenter progressivement des changements.

## Comment démarrer et exécuter un conteneur Docker

Ouvrez votre terminal et créez un nouveau répertoire `mkdir tracking-inventory-app`.

Ensuite, téléchargez une image postgres depuis [Docker Hub](https://hub.docker.com/). J'ai utilisé le tag `postgres:14-alpine`. Vous pouvez utiliser n'importe quel tag que vous souhaitez.

Dans votre terminal, collez ce qui suit et appuyez sur entrée :

```
$ docker pull postgres:14-alpine
```

Après l'avoir installé, démarrez le conteneur en utilisant la commande `docker run` :

```
$ docker run --name postgres14 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=passwordd -p 5432:5432 -d postgres:14-alpine
```

Le drapeau `--name` fait référence au nom du conteneur. Le drapeau `-e` fait référence aux variables d'environnement. Le drapeau `-p` signifie publier. Vous devez exécuter votre conteneur sur un port spécifié. Le drapeau `-d` signifie que vous souhaitez l'exécuter en mode détaché.

Après avoir appuyé sur entrée, ouvrez votre Docker Desktop si vous l'avez installé. Si ce n'est pas le cas, vous pouvez le télécharger depuis le [site web de docker](https://www.docker.com/products/docker-desktop).

Dans votre Docker Desktop, vous devriez voir que le conteneur a été démarré :

![docker-postgres14](https://www.freecodecamp.org/news/content/images/2024/06/docker-postgres14.png)

Vous pouvez établir une connexion avec la base de données en utilisant TablePlus :

![connectionok](https://www.freecodecamp.org/news/content/images/2024/06/connectionok.png)

Testez la connexion. Si elle indique ok, alors connectez-vous. Si vous êtes sur Windows et qu'elle affiche une erreur d'authentification, accédez à votre bouton démarrer et cliquez sur `Exécuter`. Dans la fenêtre contextuelle, tapez `services.msc` et appuyez sur entrée. Recherchez postgres et cliquez sur arrêter le service. Ensuite, essayez de vous connecter à nouveau.

## Comment créer et exécuter un schéma avec TablePlus

J'ai créé un schéma/modèle prédéfinis pour le projet de suivi d'inventaire avec [db diagram](https://www.dbdiagram.io/d). Ce suivi d'inventaire devrait vous permettre d'ajouter un article, un numéro de série et une valeur. Ainsi, le schéma aura des champs `item`, `serial_number`, `id` et `created_at`.

```
CREATE TABLE "inventory" (
  "id" uuid PRIMARY KEY,
  "item" varchar NOT NULL,
  "serial_number" varchar NOT NULL,
  "user" uuid NOT NULL,
  "created_at" timestamptz NOT NULL DEFAULT 'now()'
);

CREATE TABLE "user" (
  "id" uuid PRIMARY KEY,
  "name" varchar NOT NULL,
  "email" varchar UNIQUE NOT NULL,
  "password" varchar NOT NULL,
  "created_at" timestamptz NOT NULL DEFAULT 'now()'
);

CREATE INDEX ON "inventory" ("item");

ALTER TABLE "inventory" ADD FOREIGN KEY ("user") REFERENCES "user" ("id");

```
Voici à quoi ressemble le mien. Vous pouvez ouvrir votre TablePlus et ajouter le code PostgreSQL généré et l'exécuter.

## Comment installer golang-migrate

L'étape suivante consiste à installer `golang-migrate` sur votre système. J'utilise Linux sur Windows pour ce tutoriel.

Pour l'installer, visitez cette [documentation](https://github.com/golang-migrate/migrate/tree/master/cmd/migrate).

J'utilise Linux, donc j'utiliserai `curl` :

```
$ curl -L https://github.com/golang-migrate/migrate/releases/download/v4.12.2/migrate.linux-amd64.tar.gz | tar xvz
```
Une fois qu'il est installé avec succès, dans votre terminal, exécutez la commande `migrate -help` pour voir ses différentes commandes.

![migrate-help](https://www.freecodecamp.org/news/content/images/2024/06/migrate-help.png)

## Comment créer une nouvelle migration
Après avoir installé `golang-migrate`, vous pouvez créer un nouveau script de migration.

Tout d'abord, dans votre terminal et dans le répertoire tracking-app, ouvrez VS code avec la commande `code`.

Une fois cela fait, créez un nouveau dossier nommé `db` et un autre dossier à l'intérieur du dossier db nommé `migrations`.

Ensuite, dans votre terminal, exécutez la commande suivante :
```
 $ migrate create -ext sql -dir db/migration -seq tracking_inventory_schema
```

Le drapeau `-ext` fait référence à l'extension avec laquelle vous souhaitez créer la migration. Dans ce cas, il s'agit de sql. Le drapeau `-dir` fait référence au répertoire dans lequel vous souhaitez créer les fichiers. Le drapeau `-seq` fait référence au numéro séquentiel pour les fichiers de migration.

Dans votre VS code, il devrait y avoir deux fichiers : un pour `up` et un autre pour `down`. Le premier est utilisé pour apporter des modifications vers l'avant au répertoire tandis que le second est utilisé pour inverser les modifications.

Dans le fichier `up`, vous allez coller votre schéma dans le fichier.

Mon schéma ressemble à ceci :

```
CREATE TABLE "inventory" (
  "id" uuid PRIMARY KEY,
  "item" varchar NOT NULL,
  "serial_number" varchar NOT NULL,
  "user" uuid NOT NULL,
  "created_at" timestamptz NOT NULL DEFAULT 'now()'
);

CREATE TABLE "user" (
  "id" uuid PRIMARY KEY,
  "name" varchar NOT NULL,
  "email" varchar UNIQUE NOT NULL,
  "password" varchar NOT NULL,
  "created_at" timestamptz NOT NULL DEFAULT 'now()'
);

CREATE INDEX ON "inventory" ("item");

ALTER TABLE "inventory" ADD FOREIGN KEY ("user") REFERENCES "user" ("id");

```

Le vôtre peut être différent selon le projet que vous construisez.

Pour le fichier `down`, collez simplement ceci :
```
DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS user; 
```

La table d'inventaire doit être supprimée en premier car elle référence la table utilisateur.

## Comment créer et supprimer la base de données à l'intérieur et à l'extérieur d'un conteneur Docker Postgres

Vérifiez si votre conteneur docker est en cours d'exécution en utilisant la commande :

```
$ docker ps
```

S'il ne l'est pas, utilisez la commande `docker start ${container name}` pour le démarrer.

L'étape suivante consiste à accéder au shell postgres en utilisant la commande suivante puisque je suis sur Linux :

```
$ docker exec -it postgres14 bin/bash
```

Le drapeau `-it` signifie shell/terminal interactif. À l'intérieur de ce shell, vous pouvez exécuter la commande `createdb` :

```
/# createdb --username=root --owner=root tracking_inventory
```

Une fois créé, vous pouvez exécuter la commande `psql` pour interagir avec la base de données :

```
/# psql tracking-inventory
psql (14.12)
Type "help" for help.

tracking_inventory=#
```

Vous pouvez également supprimer la base de données avec la commande `dropdb`.

Pour quitter le shell, utilisez la commande `exit`.

Pour créer la base de données à l'extérieur du conteneur postgres, collez la commande suivante :

```
$ docker exec -it postgres14 createdb --username=root --owner=root tracking_inventory
```


## Comment visualiser la base de données dans TablePlus

Pour visualiser la base de données que vous avez créée, connectez-vous en utilisant la connexion précédente que nous avons établie plus tôt. Cela vous mènera à la base de données racine, puis cliquez sur l'icône de la base de données en haut.

![root-db](https://www.freecodecamp.org/news/content/images/2024/06/root-db.png)
 
La base de données créée apparaîtra, puis cliquez simplement sur `open` pour l'ouvrir
 
![tracking-inventory-db](https://www.freecodecamp.org/news/content/images/2024/06/tracking-inventory-db.png)

## Comment exécuter les migrations

Pour exécuter les migrations, exécutez cette commande dans votre terminal :

```
$ migrate -path db/migration -database "postgresql://root:passwordd@localhost:5432/tracking_inventory?sslmode=disable" -verbose up
```

Le drapeau `-path` spécifie le chemin contenant les fichiers de migration. L'option `-database` spécifie l'URL de la base de données.

À l'intérieur de l'URL, le pilote est `postgresql`. Le nom d'utilisateur et le mot de passe sont `root` et `passwordd` respectivement. Il est également important d'ajouter l'option `sslmode=disable` car Postgres n'active pas SSL par défaut.

Maintenant, exécutez les migrations :

```
$ migrate -path db/migration -database "postgresql://root:passwordd@localhost:5432/tracking_inventory?sslmode=disable" -verbose up
calhost:5432/tracking_inventory?sslmode=disable" -verbose up
2024/06/25 00:13:25 Start buffering 1/u tracking_inventory_schema
2024/06/25 00:13:25 Read and execute 1/u tracking_inventory_schema
2024/06/25 00:13:26 Finished 1/u tracking_inventory_schema (read 43.186044ms, ran 255.501635ms)
2024/06/25 00:13:26 Finished after 312.928488ms
2024/06/25 00:13:26 Closing source and database
```
La migration est réussie !

Actualisez la base de données et voyez les nouvelles tables :

![schema-migrations](https://www.freecodecamp.org/news/content/images/2024/06/schema-migrations.png)


## Conclusion

Tout au long de ce tutoriel, vous avez appris à écrire et exécuter des migrations de base de données en Go en utilisant Docker et Postgres. J'espère que vous avez beaucoup appris de cet article.

Vous pouvez me contacter sur [twitter](https://x.com/itzz_okure) ou sur [linkedin](https://www.linkedin.com/in/okure/).