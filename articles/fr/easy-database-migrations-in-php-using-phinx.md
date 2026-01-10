---
title: Comment migrer une base de données en PHP avec Phinx
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2022-03-30T23:59:31.000Z'
originalURL: https://freecodecamp.org/news/easy-database-migrations-in-php-using-phinx
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/0-ddWHLcHqIojSq_GO.png
tags:
- name: data migration
  slug: data-migration
- name: database
  slug: database
- name: PHP
  slug: php
seo_title: Comment migrer une base de données en PHP avec Phinx
seo_desc: "Building modern web applications usually involves a lot of data. Managing\
  \ these data (databases) during development and production can be a lot. \nThis\
  \ is especially true if there's more than one developer, and multiple environments\
  \ where changes have..."
---

La construction d'applications web modernes implique généralement beaucoup de données. La gestion de ces données (bases de données) pendant le développement et la production peut s'avérer fastidieuse.

C'est particulièrement vrai s'il y a plus d'un développeur et plusieurs environnements où les modifications doivent être implémentées manuellement.

Les migrations de base de données aident les développeurs à gérer ces changements facilement, à travers plusieurs environnements et collaborateurs.

Cet article explique :

* Ce que sont les migrations de base de données.
* Comment débuter avec les migrations de base de données en PHP en utilisant Phinx.
* Comment gérer les tables dans votre base de données.

Cet article est destiné aux lecteurs ayant des connaissances de base en PHP. Il vous aidera à apprendre à gérer facilement (et mieux) vos bases de données.

## Qu'est-ce que les migrations de base de données ?

En termes simples, les migrations contiennent les modifications que vous souhaitez apporter à votre base de données. Ces changements peuvent être la création ou la suppression d'une table, l'ajout ou la suppression de champ(s) dans une table, le changement de types de colonnes, et bien d'autres encore.

Ces fichiers facilitent l'application de ces mêmes changements sur plusieurs systèmes, car toute personne disposant des fichiers peut simplement les exécuter et mettre à jour sa base de données.

Ainsi, dans un scénario réel, un développeur de l'équipe pourrait modifier la table _users_ pour permettre au champ _gender_ d'accepter plus que les options par défaut _male_ et _female_, peut-être une troisième option _other_.

Après avoir effectué ce changement, le développeur crée une migration. Cette migration inclut les modifications qu'il a apportées à la base de données – dans ce cas, un changement de colonne sur une table – et les autres développeurs peuvent facilement appliquer ce changement à leurs propres bases de données locales en exécutant les migrations.

> Les migrations sont comme un contrôle de version pour votre base de données, permettant à votre équipe de définir et de partager la définition du schéma de la base de données de l'application. Si vous avez déjà dû demander à un coéquipier d'ajouter manuellement une colonne à son schéma de base de données local après avoir récupéré vos modifications depuis le contrôle de source, vous avez été confronté au problème que les migrations de base de données résolvent. - [Laravel](https://laravel.com/docs/9.x/)

De nombreux Frameworks web populaires intègrent déjà le support des migrations. Mais dans cet article, nous explorons l'utilisation des migrations en PHP pur.

Apprenez-en plus sur les migrations de base de données [ici](https://www.cloudbees.com/blog/database-migration).

## Qu'est-ce que Phinx ?

> Phinx est une bibliothèque PHP qui rend ridiculement facile la gestion des migrations de base de données pour votre application PHP. - Phinx

Phinx permet de gérer les migrations facilement, que vous utilisiez un Framework PHP ou non. Il est également très facile à installer (comme nous le verrons plus loin).

Il est livré avec quelques commandes pour faciliter les opérations. Il est entièrement personnalisable (vous pouvez en faire ce que vous voulez 🙃). Il fonctionne également dans plusieurs environnements, ce qui signifie que vous pouvez avoir des migrations de production, des migrations de test et des migrations de développement.

## Installation de Phinx

Vous pouvez ajouter Phinx à n'importe quel projet PHP en utilisant composer.

```bash
$ mkdir php-migrations
$ cd php-migrations
$ composer init
```

La première commande crée un dossier dans votre répertoire actuel, `php-migrations`, et la deuxième commande s'y déplace. La dernière commande lance un shell interactif.

Suivez les instructions en remplissant les détails requis (les valeurs par défaut conviennent). Vous pouvez définir la description du projet, le nom de l'auteur (ou des contributeurs), la stabilité minimale des dépendances, le type de projet, la licence et définir vos dépendances.

Lorsque vous arrivez à la partie des dépendances, installez le paquet _phinx_ `robmorgan/phinx` comme dépendance.

Acceptez les autres valeurs par défaut et procédez à la génération du fichier `composer.json`. Le fichier généré devrait ressembler à ceci actuellement :

```php
{
    "name": "zubair/php-migrations",
    "description": "A simple tutorial on how to use and manage migrations in PHP applications.",
    "type": "project",
    "require": {
        "robmorgan/phinx": "^0.12.10"
    },
    "license": "ISC",
    "autoload": {
        "psr-4": {
            "Zubs\\": "src/"
        }
    },
    "authors": [
        {
            "name": "Zubs",
            "email": "zubairidrisaweda@gmail.com"
        }
    ]
}

```

## Initialisation de Phinx

Après avoir installé Phinx, vous devez l'initialiser. Vous pouvez le faire très facilement en utilisant son binaire installé dans le dossier `vendor`.

```bash
$ ./vendor/bin/phinx init
```

Ceci crée le fichier de configuration de Phinx sous forme de fichier PHP. Il pourrait également être créé en tant que fichier JSON. Je préfère le JSON pour les configurations, je vais donc utiliser le format JSON.

```bash
$ ./vendor/bin/phinx init --format=json
```

Voici à quoi ressemble le fichier de configuration par défaut :

```json
{
    "paths": {
        "migrations": "%%PHINX_CONFIG_DIR%%/db/migrations",
        "seeds": "%%PHINX_CONFIG_DIR%%/db/seeds"
    },
    "environments": {
        "default_migration_table": "phinxlog",
        "default_environment": "development",
        "production": {
            "adapter": "mysql",
            "host": "localhost",
            "name": "production_db",
            "user": "root",
            "pass": "",
            "port": 3306,
            "charset": "utf8"
        },
        "development": {
            "adapter": "mysql",
            "host": "localhost",
            "name": "development_db",
            "user": "root",
            "pass": "",
            "port": 3306,
            "charset": "utf8"
        },
        "testing": {
            "adapter": "mysql",
            "host": "localhost",
            "name": "testing_db",
            "user": "root",
            "pass": "",
            "port": 3306,
            "charset": "utf8"
        }
    },
    "version_order": "creation"
}

```

Dans ce fichier de configuration, remarquez comment Phinx s'attend par défaut à ce que vous ayez un chemin `db/migrations` (pour vos migrations). Vous pouvez changer cela si vous le souhaitez, mais je pense que c'est correct et je vais le garder.

```bash
$ mkdir db && db/migrations
```

Vous pouvez en savoir plus sur ces configurations dans la [documentation officielle](https://book.cakephp.org/phinx/0/en/configuration.html).

Phinx est également livré avec des commandes pour différentes actions afin de faciliter son utilisation dans nos projets.

## Comment créer une migration

Phinx utilise des classes pour ses migrations. Pour créer une nouvelle migration (par exemple, une pour créer une table _posts_), utilisez la commande `create` avec le nom de la migration.

```bash
$ ./vendor/bin/phinx create PostsTableMigration
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-28-at-13.22.17.png)
_Création d'une migration_

Ceci crée un fichier `20220328122134_posts_table_migration.php` dans le répertoire `db/migrations` créé précédemment. Ce fichier est nommé selon le format `YYYYMMDDHHMMSS_ma_nouvelle_migration.php`. Dans ce format, les 14 premiers caractères, _YYYYMMDDHHMMSS_, sont des représentations de l'horodatage actuel.

Le fichier `20220328122134_posts_table_migration.php` ressemble actuellement à ceci :

```php
<?php
declare(strict_types=1);

use Phinx\Migration\AbstractMigration;

final class PostsTableMigration extends AbstractMigration
{
    /**
     * Méthode Change.
     *
     * Écrivez vos migrations réversibles en utilisant cette méthode.
     *
     * Plus d'informations sur l'écriture de migrations sont disponibles ici :
     * https://book.cakephp.org/phinx/0/en/migrations.html#the-change-method
     *
     * N'oubliez pas d'appeler "create()" ou "update()" et NON "save()" lors de l'utilisation
     * de la classe Table.
     */
    public function change(): void
    {

    }
}

```

Ce fichier (et toutes les autres migrations créées avec Phinx) étend la classe `Phinx\Migration\AbstractMigration`. Cette classe possède toutes les méthodes dont vous avez besoin pour interagir avec votre base de données.

Ce fichier de migration inclut également une méthode `change`. Cette méthode a été introduite récemment dans Phinx à la version 0.2.0 pour implémenter l'idée de migrations réversibles de Phinx.

Il s'agit de fichiers de migration avec une seule méthode, _change_, qui contient la logique pour effectuer une action, laissant Phinx comprendre comment l'annuler. Plutôt que l'utilisation traditionnelle de deux méthodes, _up_ et _down_, pour créer et annuler des actions.

> Phinx vous permet toujours d'utiliser les méthodes _up_ et _down_. Mais il donne la préférence à la méthode _change_ sur celles-ci lorsqu'elles sont utilisées ensemble. Il les ignore.

## Comment gérer les tables

Les tables sont la base sur laquelle les bases de données structurées sont construites et constituent la partie la plus importante de ce que Phinx propose.

Vous pouvez facilement gérer les tables de base de données en utilisant du code PHP avec Phinx. Phinx propose une méthode puissante `table()`. Cette méthode récupère une instance de l'objet _Table_.

### Comment créer une table

Créer une table est très facile avec Phinx. Vous créez une nouvelle instance de l'objet _Table_ en utilisant la méthode `table()` avec le nom de la table.

```php
$table = $this->table('posts');
```

Ensuite, vous pouvez ajouter des colonnes avec leurs paramètres.

```php
$table->addColumn('title', 'string', ['limit' => 20])
	->addColumn('body', 'text')
    ->addColumn('cover_image', 'string')
    ->addTimestamps()
    ->addIndex(['title'], ['unique' => true]);
```

Ici, j'ai créé les colonnes `title`, `body`, `cover_image`, `created_at` et `updated_at`. J'ai également défini le type de `title` comme étant une chaîne (_string_) de 20 caractères ou moins.

J'ai défini `body` comme un champ de texte (_text_), afin qu'il puisse contenir de longs articles. Le `cover_image` est également un champ _string_ qui utilise la taille par défaut d'une chaîne (255).

Les champs `created_at` et `updated_at` sont des horodatages générés automatiquement dans la méthode `addTimestamps()`.

Enfin, j'ai défini le champ `title` comme étant unique (comme ce serait le cas dans un vrai blog).

Vous pouvez obtenir tous les types de colonnes disponibles en consultant les [Types de Colonnes Valides](https://book.cakephp.org/phinx/0/en/migrations.html#valid-column-types). Vous pouvez également obtenir toutes les options de colonnes disponibles en consultant les [Options de Colonnes Valides](https://book.cakephp.org/phinx/0/en/migrations.html#valid-column-options).

Enfin, vous pouvez indiquer que la base de données doit être créée en utilisant la méthode `create`.

```php
$table->create();
```

Au final, la méthode _change_ de votre fichier de migration devrait ressembler à ceci :

```php
public function change(): void
{
    $table = $this->table('posts');

    $table->addColumn('title', 'string', ['limit' => 20])
        ->addColumn('body', 'text')
        ->addColumn('cover_image', 'string')
        ->addTimestamps()
        ->addIndex(['title'], ['unique' => true]);

     $table->create();
}
```

Nous pouvons maintenant exécuter cette migration pour créer notre table.

## Comment exécuter les migrations

Après avoir créé les migrations, l'étape suivante consiste à appliquer ces changements souhaités dans la base de données. L'exécution des migrations applique réellement ces changements.

```php
$ ./vendor/bin/phinx migrate
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-29-at-18.54.56.png)
_Exécution d'une migration_

Cette image montre le résultat de la migration. Vous pouvez voir le temps mis pour exécuter la migration.

Maintenant, si vous vérifiez votre outil d'interface graphique de base de données, vous remarquerez que la table _posts_ a été créée avec un champ supplémentaire, le champ _id_. Ce champ est également le champ primaire par défaut. Et il s'auto-incrémente également.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-29-at-19.00.27.png)
_table posts._

Vous pouvez changer la clé primaire pour une autre clé en spécifiant un autre champ comme champ primaire, ou en mappant le champ _id_ au champ primaire souhaité. Cette dernière option inclut la capacité d'auto-incrémentation du champ _id_ normal.

```php
$table = $this->table('posts', [
    'id' => false,
    'primary_key' => ['posts_key']
]);

$table = $this->table('posts', [
    'id' => 'posts_key',
]);
```

Dans la première méthode, la clé primaire à utiliser doit être une colonne de la table (elle n'est pas auto-créée).

Vous pouvez également définir dans quel environnement vous souhaitez exécuter les migrations.

```bash
$ ./vendor/bin/phinx migrate -e testing
```

### Comment annuler les migrations

Les migrations peuvent être annulées en étant exécutées vers le bas (_run down_). C'est l'inverse de la migration vers le haut (_migrating up_). La table précédemment créée sera supprimée, les colonnes ajoutées seront retirées et la base de données sera ramenée à son état initial pré-migration.

```bash
$ ./vendor/bin/phinx rollback
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-29-at-18.56.46.png)
_Annulation d'une migration_

### Comment vérifier le statut des migrations

À mesure que la taille de votre application augmente, il est normal que vos migrations de base de données augmentent. Pour cette raison, à un moment donné, vous souhaiterez peut-être vérifier le statut de vos migrations, pour savoir lesquelles ont été exécutées et lesquelles ne l'ont pas été.

```bash
$ ./vendor/bin/phinx status
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-29-at-18.58.07.png)
_Vérification du statut de la migration_

### Comment supprimer une table

Vous pouvez facilement utiliser la méthode `drop`, suivie de la méthode `save` pour persister le changement, sur l'objet _Table_.

```php
$this->table('posts')->drop()->save();
```

### Comment renommer une table

```php
$table = $this->table('posts');

$table->rename('articles')
    ->update();
```

Pour renommer une table, récupérez la table. Utilisez ensuite la méthode `rename` avec le nouveau nom, suivie de la méthode `update` pour persister ce changement.

### Comment changer la clé primaire d'une table

Vous pouvez également changer très facilement la clé primaire d'une table.

```php
$table = $this->table('posts');

$table->changePrimaryKey('new_primary_key');

$table->update();
```

## Conclusion

Vous savez maintenant comment configurer des migrations dans vos applications PHP.

Si vous avez des questions ou des conseils pertinents, n'hésitez pas à me contacter pour les partager.

Pour lire davantage de mes articles ou suivre mon travail, vous pouvez me retrouver sur [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris) et [Github](https://github.com/Zubs). C'est rapide, facile et gratuit !