---
title: Comment effectuer des migrations de base de données avec Go Migrate
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-26T23:17:14.000Z'
originalURL: https://freecodecamp.org/news/database-migration-golang-migrate
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Blue-and-Pink-3D-Elements-Student-Part-Time-Graphic-Designer-Video-Resume-Talking-Presentation.png
tags:
- name: data migration
  slug: data-migration
- name: database
  slug: database
- name: golang
  slug: golang
seo_title: Comment effectuer des migrations de base de données avec Go Migrate
seo_desc: "By Rwitesh Bera\nSince its introduction, the programming language Go (also\
  \ known as Golang) has become increasingly popular. It is known for its simplicity\
  \ and efficient performance, similar to that of a lower-level language such as C++.\
  \ \nWhile workin..."
---

Par Rwitesh Bera

Depuis son introduction, le langage de programmation Go (également connu sous le nom de Golang) est devenu de plus en plus populaire. Il est connu pour sa simplicité et ses performances efficaces, similaires à celles d'un langage de bas niveau comme le C++. 

Lorsqu'on travaille avec une base de données, la migration de schéma est l'une des tâches les plus importantes que les développeurs effectuent tout au long du cycle de vie du projet. Dans cet article, je vais expliquer ce qu'est une migration de base de données et comment la gérer en utilisant [go-migrate](https://github.com/golang-migrate/migrate).

## Qu'est-ce qu'une migration de base de données ?

Une migration de base de données, également connue sous le nom de migration de schéma, est un ensemble de modifications à apporter à la structure des objets d'une base de données relationnelle. 

C'est une manière de gérer et d'implémenter des changements incrémentiels à la structure des données de manière contrôlée et programmatique. Ces changements sont souvent réversibles, ce qui signifie qu'ils peuvent être annulés ou restaurés si nécessaire. 

Le processus de migration aide à changer le schéma de la base de données de son état actuel à un nouvel état souhaité, qu'il s'agisse d'ajouter des tables et des colonnes, de supprimer des éléments, de diviser des champs ou de changer des types et des contraintes. 

En gérant ces changements de manière programmatique, il devient plus facile de maintenir la cohérence et l'exactitude de la base de données, ainsi que de suivre l'historique des modifications qui y ont été apportées.

## Installation

[migrate](https://github.com/golang-migrate/migrate) est un outil en ligne de commande que vous pouvez utiliser pour exécuter des migrations. Vous pouvez facilement l'installer sur divers systèmes d'exploitation tels que Linux, Mac et Windows en utilisant des gestionnaires de paquets comme curl, brew et scoop, respectivement. 

Pour plus d'informations sur la façon d'installer et d'utiliser l'outil, vous pouvez vous référer à la documentation officielle.

Pour installer l'outil de ligne de commande migrate en utilisant [scoop](https://scoop.sh/) sur Windows, vous pouvez suivre ces étapes :

```bash
$ scoop install migrate
```

Pour installer l'outil de ligne de commande migrate en utilisant **curl** sur Linux, vous pouvez suivre ces étapes : 

```bash
$ curl -L https://packagecloud.io/golang-migrate/migrate/gpgkey| apt-key add -
$ echo "deb https://packagecloud.io/golang-migrate/migrate/ubuntu/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/migrate.list
$ apt-get update
$ apt-get install -y migrate
```

Pour installer l'outil de ligne de commande migrate sur Mac, vous pouvez suivre ces étapes : 

```bash
$ brew install golang-migrate
```

## Comment créer une nouvelle migration

Créez un répertoire comme `database/migration` pour stocker tous les fichiers de migration.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-263.png)
_Structure des fichiers sources dans l'IDE GoLand_

Ensuite, créez des fichiers de migration en utilisant la commande suivante :

```bash
$ migrate create -ext sql -dir database/migration/ -seq init_mg
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-267.png)
_Sortie du terminal affichant la création réussie de la migration_

Vous utilisez `-seq` pour générer une version séquentielle et `init_mg` est le nom de la migration.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-269.png)
_Structure des fichiers sources dans l'IDE GoLand_

Une migration se compose généralement de deux fichiers distincts, l'un pour faire passer la base de données à un nouvel état (appelé "up") et l'autre pour revenir aux changements apportés à l'état précédent (appelé "down"). 

Le fichier "up" est utilisé pour implémenter les changements souhaités dans la base de données, tandis que le fichier "down" est utilisé pour annuler ces changements et restaurer la base de données à son état précédent.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Database-migration.jpg)
_Flux de migration de base de données_

Le format de ces fichiers pour SQL est :

```bash
{version}_{title}.down.sql
{version}_{title}.up.sql
```

Lorsque vous créez des fichiers de migration, ils seront vides par défaut. Pour implémenter les changements que vous souhaitez, vous devrez les remplir avec les requêtes SQL appropriées.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-282.png)
_Requêtes SQL pour migrer les données_

### Comment exécuter une migration Up

Pour exécuter les instructions SQL dans les fichiers de migration, migrate nécessite une connexion valide à une base de données Postgres. 

Pour ce faire, vous devrez fournir une chaîne de connexion au format approprié.

```bash
$ migrate -path database/migration/ -database "postgresql://username:secretkey@localhost:5432/database_name?sslmode=disable" -verbose up
```

Maintenant, dans votre shell Postgres, vous pouvez vérifier les tables nouvellement créées en utilisant les commandes suivantes :

```bash
\d+

\d+ table_name DESCRIBE TABLE
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-286.png)
_Affichage des données de la table dans Postgres_

### Comment annuler les migrations

Si vous souhaitez revenir en arrière sur la migration, vous pouvez le faire en utilisant le tag `down` suivant :

```bash
$ migrate -path database/migration/ -database "postgresql://username:secretkey@localhost:5432/database_name?sslmode=disable" -verbose down
```

Cela supprimera la colonne `email` des deux tables comme mentionné dans le fichier `000002_init_mg.up.sql`.

Maintenant, vérifions la base de données pour voir si `email` a été supprimé ou non :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot_20230126_102731.png)
_Affichage des données de la table mises à jour dans Postgres_

### Comment résoudre les erreurs de migration

Si une migration contient une erreur et est exécutée, migrate empêchera toute autre migration d'être exécutée sur la même base de données. 

Un message d'erreur comme `Dirty database version 1. Fix and force version` sera affiché, même après que l'erreur dans la migration soit corrigée. Cela indique que la base de données est "sale" et doit être investiguée. 

Il est nécessaire de déterminer si la migration a été appliquée partiellement ou pas du tout. Une fois que vous avez déterminé cela, la version de la base de données doit être forcée à refléter son état réel en utilisant la commande force.

```bash
$ migrate -path database/migration/ -database "postgresql://username:secretkey@localhost:5432/database_name?sslmode=disable" force <VERSION>
```

### Comment ajouter des commandes dans un Makefile

```makefile
migration_up: migrate -path database/migration/ -database "postgresql://username:secretkey@localhost:5432/database_name?sslmode=disable" -verbose up

migration_down: migrate -path database/migration/ -database "postgresql://username:secretkey@localhost:5432/database_name?sslmode=disable" -verbose down

migration_fix: migrate -path database/migration/ -database "postgresql://username:secretkey@localhost:5432/database_name?sslmode=disable" force VERSION
```

Maintenant, vous pouvez exécuter `$ make migration_up` pour 'up', `$ make migration_down` pour 'down', et `$ make migration_fix` pour corriger le problème de migration. 

Avant d'exécuter le makefile, assurez-vous que le numéro de version correct est inclus dans la commande `migration_fix`.

## Conclusion

Les systèmes de migration génèrent généralement des fichiers qui peuvent être partagés entre les développeurs et plusieurs équipes. Ils peuvent également être appliqués à plusieurs bases de données et maintenus dans le contrôle de version. 

Garder une trace des changements apportés à la base de données permet de suivre l'historique des modifications qui y ont été apportées. De cette manière, le schéma de la base de données et la compréhension de cette structure par l'application peuvent évoluer ensemble.

Cela conclut notre discussion sur la migration de base de données. J'espère que vous avez trouvé les informations utiles et instructives. 

Si vous avez aimé lire cet article, veuillez envisager de le partager avec vos collègues et amis sur les réseaux sociaux. De plus, veuillez me suivre sur [Twitter](https://twitter.com/RwiteshBera/) pour plus de mises à jour sur la technologie et la programmation. Merci pour votre lecture !