---
title: Le manuel SQL – Un cours gratuit pour les développeurs web
subtitle: ''
author: Lane Wagner
co_authors: []
series: null
date: '2023-09-05T13:57:37.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-sql
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/The-SQL-Handbook-Cover.png
tags:
- name: database
  slug: database
- name: handbook
  slug: handbook
- name: SQL
  slug: sql
seo_title: Le manuel SQL – Un cours gratuit pour les développeurs web
seo_desc: 'SQL is everywhere these days. Whether you''re learning backend development,
  data engineering, DevOps, or data science, SQL is a skill you''ll want in your toolbelt.

  This a free and open text-based handbook. If you want to get started, just scroll
  down ...'
---

SQL est partout de nos jours. Que vous appreniez le développement backend, l'ingénierie des données, DevOps ou la science des données, SQL est une compétence que vous voudrez avoir dans votre boîte à outils.

Ceci est un manuel texte gratuit et ouvert. Si vous voulez commencer, il vous suffit de faire défiler vers le bas et de commencer à lire. Cela dit, il existe deux autres options pour suivre le cours :

1. Essayez la version interactive de ce [cours SQL](https://boot.dev/learn/learn-gsql) sur [Boot.dev](https://boot.dev/), avec des défis de codage et des projets
2. Regardez la vidéo de ce cours sur la chaîne YouTube de FreeCodeCamp (intégrée ci-dessous) :

%[https://www.youtube.com/watch?v=KBDSJU3cGkc]

## Table des matières

* [Chapitre 1 : Introduction](#heading-chapitre-1-introduction)
* [Chapitre 2 : Tables SQL](#heading-chapitre-2-tables-sql)
* [Chapitre 3 : Contraintes](#heading-chapitre-3-contraintes)
* [Chapitre 4 : Opérations CRUD](#heading-chapitre-4-operations-crud-en-sql)
* [Chapitre 5 : Requêtes SQL de base](#heading-chapitre-5-requetes-sql-de-base)
* [Chapitre 6 : Comment structurer les données retournées en SQL](#heading-chapitre-6-comment-structurer-les-donnees-retournees-en-sql)
* [Chapitre 7 : Comment effectuer des agrégations en SQL](#heading-chapitre-7-comment-effectuer-des-aggregations-en-sql)
* [Chapitre 8 : Sous-requêtes SQL](#heading-chapitre-8-sous-requetes-sql)
* [Chapitre 9 : Normalisation de la base de données](#heading-chapitre-9-normalisation-de-la-base-de-donnees)
* [Chapitre 10 : Comment joindre des tables en SQL](#heading-chapitre-10-comment-joindre-des-tables-en-sql)
* [Chapitre 11 : Performance de la base de données](#heading-chapitre-11-performance-de-la-base-de-donnees)

## Chapitre 1 : Introduction

Structured Query Language, ou [SQL](https://www.freecodecamp.org/news/what-is-sql-database-definition-for-beginners/), est le principal langage de programmation utilisé pour gérer et interagir avec les [bases de données relationnelles](https://cloud.google.com/learn/what-is-a-relational-database). SQL peut effectuer diverses opérations telles que la création, la mise à jour, la lecture et la suppression d'enregistrements dans une base de données.

%[https://www.youtube.com/watch?v=pYKirBUnr-8]

### Qu'est-ce qu'une instruction SELECT en SQL ?

Écrivons notre propre instruction SQL à partir de zéro. Une instruction `SELECT` est l'opération la plus courante en SQL – souvent appelée "requête". `SELECT` récupère des données d'une ou plusieurs tables. Les instructions `SELECT` standard ne modifient *pas* l'état de la base de données.

```SQL
SELECT id from users;
```

#### Comment sélectionner un seul champ

Une instruction `SELECT` commence par le mot-clé `SELECT` suivi des champs que vous souhaitez récupérer.

```SQL
SELECT id from users;
```

#### Comment sélectionner plusieurs champs

Si vous souhaitez sélectionner plus d'un champ, vous pouvez spécifier plusieurs champs séparés par des virgules comme ceci :

```SQL
SELECT id, name from users;
```

#### Comment sélectionner tous les champs

Si vous souhaitez sélectionner *tous* les champs d'un enregistrement, vous pouvez utiliser la syntaxe raccourcie `*`.

```SQL
SELECT * from users;
```

Après avoir spécifié les champs, vous devez indiquer de quelle table vous souhaitez extraire les enregistrements en utilisant l'instruction `from` suivie du nom de la table. 

Nous parlerons plus des tables plus tard, mais pour l'instant, vous pouvez les considérer comme des structs ou des objets. Par exemple, la table `users` pourrait avoir 3 champs :

* `id`
* `name`
* `balance`

Et enfin, *toutes* les instructions se terminent par un point-virgule `;`.

### Quelles bases de données utilisent SQL ?

SQL est juste un langage de requête. Vous l'utilisez généralement pour interagir avec une technologie de base de données spécifique. Par exemple : 

* [SQLite](https://www.sqlite.org/index.html)
* [PostgreSQL](https://www.postgresql.org/)
* [MySQL](https://www.mysql.com/)
* [CockroachDB](https://www.cockroachlabs.com/)
* [Oracle](https://www.oracle.com/database/)

Et d'autres.

Bien que de nombreuses bases de données différentes utilisent le langage SQL, la plupart d'entre elles auront leur propre *dialecte*. Il est crucial de comprendre que toutes les bases de données ne sont pas créées égales. Le fait qu'une base de données compatible SQL fasse les choses d'une certaine manière ne signifie pas que toutes les bases de données compatibles SQL suivront ces mêmes schémas.

#### Nous utilisons SQLite

Dans ce cours, nous utiliserons spécifiquement [SQLite](https://www.sqlite.org/index.html). SQLite est idéal pour les projets embarqués, les navigateurs web et les projets jouets. Il est léger, mais a des fonctionnalités limitées par rapport à des technologies SQL de production plus courantes comme PostgreSQL ou MySQL.

Et je m'assurerai de vous indiquer chaque fois que certaines fonctionnalités avec lesquelles nous travaillons sont uniques à SQLite.

## NoSQL vs SQL

Lorsque nous parlons des bases de données SQL, nous devons également mentionner l'éléphant dans la pièce : [NoSQL](https://en.wikipedia.org/wiki/NoSQL).

Pour faire simple, une base de données NoSQL est une base de données qui n'utilise pas SQL (Structured Query Language). Chaque NoSQL a généralement sa propre façon d'écrire et d'exécuter des requêtes. Par exemple, [MongoDB](https://www.mongodb.com/) utilise MQL (MongoDB Query Language) et [ElasticSearch](https://www.elastic.co/) a simplement une API JSON.

Alors que la plupart des bases de données relationnelles sont assez similaires, les bases de données NoSQL tendent à être assez uniques et sont utilisées pour des fins plus spécifiques. Certaines des principales différences entre une base de données SQL et NoSQL sont :

1. Les bases de données NoSQL sont généralement non relationnelles, les bases de données SQL sont généralement [relationnelles](https://cloud.google.com/learn/what-is-a-relational-database) (nous parlerons plus de ce que cela signifie plus tard).
2. Les bases de données SQL ont généralement un schéma défini, les bases de données NoSQL ont généralement un schéma dynamique.
3. Les bases de données SQL sont basées sur des tables, les bases de données NoSQL ont une variété de différentes méthodes de stockage, telles que document, clé-valeur, graphe, colonne large, et plus.

### Types de bases de données NoSQL

* [Base de données documentaire](https://en.wikipedia.org/wiki/Document-oriented_database)
* [Magasin clé-valeur](https://en.wikipedia.org/wiki/Key%E2%80%93value_database)
* [Colonne large](https://en.wikipedia.org/wiki/Wide-column_store)
* [Graphe](https://en.wikipedia.org/wiki/Graph_database)

Quelques-unes des bases de données NoSQL les plus populaires sont :

* [MongoDB](https://en.wikipedia.org/wiki/MongoDB)
* [Cassandra](https://en.wikipedia.org/wiki/Apache_Cassandra)
* [CouchDB](https://en.wikipedia.org/wiki/Apache_CouchDB)
* [DynamoDB](https://en.wikipedia.org/wiki/Amazon_DynamoDB)
* [ElasticSearch](https://www.elastic.co/)

%[https://www.youtube.com/watch?v=NovjCrDFlXk]

### Comparaison des bases de données SQL

Plongeons plus profondément et parlons de certaines des bases de données SQL populaires et de ce qui les distingue les unes des autres. Certaines des bases de données SQL les plus populaires en ce moment sont :

* [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL)
* [MySQL](https://en.wikipedia.org/wiki/MySQL)
* [Microsoft SQL Server](https://db-engines.com/en/system/Microsoft+SQL+Server)
* [SQLite](https://en.wikipedia.org/wiki/SQLite)
* [Et beaucoup d'autres](https://en.wikipedia.org/wiki/List_of_relational_database_management_systems)

Source : [db-engines.com](https://db-engines.com/en/ranking)

Bien que toutes ces bases de données utilisent SQL, chaque base de données définit des règles, des pratiques et des stratégies spécifiques qui les distinguent de leurs concurrents. 

#### SQLite vs PostgreSQL

Personnellement, SQLite et PostgreSQL sont mes préférés de la liste ci-dessus. Postgres est une base de données SQL très puissante, open-source et prête pour la production. SQLite est une base de données légère, embarquable et open-source. Je choisis généralement l'une de ces technologies si je travaille avec SQL.

SQLite est un système de gestion de base de données sans serveur (DBMS) qui peut fonctionner au sein d'applications, tandis que PostgreSQL utilise un modèle Client-Serveur et nécessite qu'un serveur soit installé et écoute sur un réseau, similaire à un serveur HTTP.

Voir une comparaison complète [ici](https://db-engines.com/en/system/PostgreSQL%3BSQLite).

Encore une fois, dans ce cours, nous travaillerons avec SQLite, une base de données légère et simple. Pour la plupart des serveurs web backend, PostgreSQL est une option plus adaptée à la production, mais SQLite est idéal pour l'apprentissage et pour les petits systèmes.

## Chapitre 2 : Tables SQL

L'instruction `CREATE TABLE` est utilisée pour créer une nouvelle table dans une base de données.

### Comment utiliser l'instruction `CREATE TABLE`

Pour créer une table, utilisez l'instruction `CREATE TABLE` suivie du nom de la table et des champs que vous souhaitez dans la table.

```SQL
CREATE TABLE employees (id INTEGER, name TEXT, age INTEGER, is_manager BOOLEAN, salary INTEGER);
```

Chaque nom de champ est suivi de son type de données. Nous aborderons les types de données dans un instant.

Il est également acceptable et courant de diviser l'instruction `CREATE TABLE` avec un peu d'espace blanc comme ceci :

```SQL
CREATE TABLE employees(
    id INTEGER,
    name TEXT,
    age INTEGER,
    is_manager BOOLEAN,
    salary INTEGER
);
```

### Comment modifier les tables

Nous devons souvent modifier notre schéma de base de données sans le supprimer et le recréer. Imaginez si Twitter supprimait sa base de données chaque fois qu'il devait ajouter une fonctionnalité, ce serait un désastre ! Votre compte et tous vos tweets seraient effacés quotidiennement.

Au lieu de cela, nous pouvons utiliser l'instruction `ALTER TABLE` pour apporter des modifications sans supprimer de données.

#### Comment utiliser `ALTER TABLE`

Avec SQLite, une instruction `ALTER TABLE` vous permet de :

1. Renommer une table ou une colonne, que vous pouvez faire comme ceci :

```SQL
ALTER TABLE employees
RENAME TO contractors;

ALTER TABLE contractors
RENAME COLUMN salary TO invoice;
```

2. AJOUTER ou SUPPRIMER une colonne, que vous pouvez faire comme ceci :

```SQL
ALTER TABLE contractors
ADD COLUMN job_title TEXT;

ALTER TABLE contractors
DROP COLUMN is_manager;
```


### Introduction aux migrations

Une migration de base de données est un ensemble de modifications apportées à une base de données relationnelle. En fait, les instructions `ALTER TABLE` que nous avons effectuées dans le dernier exercice étaient des exemples de migrations.

Les migrations sont utiles lors de la transition d'un état à un autre, de la correction d'erreurs ou de l'adaptation d'une base de données aux changements. 

Les bonnes migrations sont petites, incrémentielles et idéalement réversibles. Comme vous pouvez l'imaginer, lorsque vous travaillez avec de grandes bases de données, apporter des modifications peut être effrayant. Nous devons être prudents lors de l'écriture des migrations de base de données afin de ne pas casser les systèmes qui dépendent de l'ancien schéma de base de données.

#### Exemple d'une mauvaise migration

Si un serveur backend exécute périodiquement une requête comme `SELECT * FROM people`, et que nous exécutons une migration de base de données qui modifie le nom de la table de `people` à `users` *sans mettre à jour le code*, l'application se cassera. Elle essaiera de récupérer des données d'une table qui n'existe plus.

Une solution simple à ce problème serait de déployer un nouveau code qui utilise une nouvelle requête :

```sql
SELECT * FROM users;
```

Et nous déployons ce code en production immédiatement après la migration.

%[https://www.youtube.com/watch?v=iHIGUpEVN6Y]

### Types de données SQL

SQL en tant que langage peut supporter de nombreux types de données différents. Mais les types de données que votre système de gestion de base de données ([DBMS](https://en.wikipedia.org/wiki/Database#:~:text=A%20database%20management%20system%20(DBMS))) supporte varieront en fonction de la base de données spécifique que vous utilisez.

SQLite ne supporte que les types les plus basiques, et nous utilisons SQLite dans ce cours.

#### Types de données SQLite

Passons en revue les [types de données supportés par SQLite](https://www.sqlite.org/datatype3.html) et comment ils sont stockés.

1. `NULL` - Valeur nulle.
2. `INTEGER` - Un entier signé stocké en 0,1,2,3,4,6, ou 8 octets.
3. `REAL` - Valeur à virgule flottante stockée sous forme de nombre à virgule flottante [IEEE 64 bits](https://en.wikipedia.org/wiki/IEEE_754).
4. `TEXT` - Chaîne de texte stockée en utilisant l'encodage de la base de données tel que [UTF-8](https://en.wikipedia.org/wiki/UTF-8)
5. `BLOB` - Abréviation de [Binary large object](https://en.wikipedia.org/wiki/Binary_large_object) et généralement utilisé pour les images, l'audio ou d'autres multimédias.

Par exemple :

```sql
CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    age INTEGER,
    is_manager BOOLEAN,
    salary INTEGER
);
```

#### Valeurs booléennes

Il est important de noter que SQLite n'a pas de classe de stockage `BOOLEAN` séparée. Au lieu de cela, les valeurs booléennes sont stockées sous forme d'entiers :

* `0` = `false`
* `1` = `true`

Ce n'est pas vraiment si étrange – les valeurs booléennes ne sont que des bits binaires après tout !

SQLite vous permettra toujours d'écrire vos requêtes en utilisant des expressions `boolean` et les mots-clés `true`/`false`, mais il convertira les booléens en entiers sous le capot.

## Chapitre 3 : Contraintes

Une `contrainte` est une règle que nous créons sur une base de données qui impose un comportement spécifique. Par exemple, définir une contrainte `NOT NULL` sur une colonne garantit que la colonne n'acceptera pas de valeurs `NULL`.

Si nous essayons d'insérer une valeur `NULL` dans une colonne avec la contrainte `NOT NULL`, l'insertion échouera avec un message d'erreur. Les contraintes sont extrêmement utiles lorsque nous devons nous assurer que certains types de données existent dans notre base de données. 

#### Contrainte NOT NULL

La contrainte `NOT NULL` peut être ajoutée directement à l'instruction `CREATE TABLE`.

```SQL
CREATE TABLE employees(
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    title TEXT NOT NULL
);
```

#### Limitation de SQLite

Dans d'autres dialectes de SQL, vous pouvez `ADD CONSTRAINT` dans une instruction `ALTER TABLE`. SQLite ne supporte pas cette fonctionnalité, donc lorsque nous créons nos tables, nous devons nous assurer de spécifier toutes les contraintes que nous voulons. 

Voici une [liste des fonctionnalités SQL](https://www.sqlite.org/omitted.html) que SQLite n'implémente pas au cas où vous seriez curieux.

### Contraintes de clé primaire

Une *clé* définit et protège les relations entre les tables. Une [`clé primaire`](https://en.wikipedia.org/wiki/Primary_key) est une colonne spéciale qui identifie de manière unique les enregistrements dans une table. Chaque table peut avoir une, et une seule clé primaire.

#### Votre clé primaire sera presque toujours la colonne "id"

Il est très courant d'avoir une colonne nommée `id` sur chaque table dans une base de données, et cet `id` est la clé primaire pour cette table. Aucune des deux lignes de cette table ne peut partager un `id`.

Une contrainte `PRIMARY KEY` peut être explicitement spécifiée sur une colonne pour garantir l'unicité, rejetant toute insertion où vous tentez de créer un ID en double.

### Contraintes de clé étrangère

Les clés étrangères sont ce qui rend les bases de données relationnelles relationnelles ! Les clés étrangères définissent les relations *entre* les tables. En termes simples, une `FOREIGN KEY` est un champ dans une table qui référence la `PRIMARY KEY` d'une autre table.

#### Création d'une clé étrangère dans SQLite

La création d'une `FOREIGN KEY` dans SQLite se fait lors de la création de la table ! Après avoir défini les champs et les contraintes de la table, nous ajoutons une contrainte `CONSTRAINT` supplémentaire où nous définissons la `FOREIGN KEY` et ses `REFERENCES`.

Voici un exemple :

```SQL
CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL
);

CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department_id INTEGER,
    CONSTRAINT fk_departments
    FOREIGN KEY (department_id)
    REFERENCES departments(id)
);
```

Dans cet exemple, un `employee` a un `department_id`. Le `department_id` doit être le même que le champ `id` d'un enregistrement de la table `departments`.

### Schéma

Nous avons utilisé le mot *schéma* plusieurs fois maintenant, parlons de ce que signifie ce mot. Le [schéma](https://www.ibm.com/cloud/learn/database-schema) d'une base de données décrit comment les données y sont organisées.

Les types de données, les noms de tables, les noms de champs, les contraintes et les relations entre toutes ces entités font partie du *schéma* d'une base de données.

#### Il n'y a pas de manière parfaite d'architecturer un schéma de base de données

Lors de la conception d'un schéma de base de données, il n'y a généralement pas de solution "correcte". Nous faisons de notre mieux pour choisir un ensemble cohérent de tables, de champs, de contraintes, etc. qui accomplira les objectifs de notre projet. Comme beaucoup de choses en programmation, différentes conceptions de schéma présentent différents compromis.

#### Comment décider d'une architecture de schéma cohérente ?

Une décision très importante qui doit être prise est de décider quelle table stockera le solde d'un utilisateur ! Comme vous pouvez l'imaginer, garantir l'exactitude de nos données lorsqu'il s'agit d'argent est *super* important. Nous voulons pouvoir :

* Suivre le solde actuel d'un utilisateur
* Voir le solde historique à tout moment dans le passé
* Voir un journal des transactions qui ont modifié le solde au fil du temps

Il existe de nombreuses façons d'aborder ce problème. Pour notre première tentative, essayons le schéma le plus simple qui répond aux besoins de notre projet. 

## Chapitre 4 : Opérations CRUD en SQL

### Qu'est-ce que CRUD ?

CRUD est un acronyme qui signifie `CREATE`, `READ`, `UPDATE` et `DELETE`. Ces quatre opérations sont le pain et le beurre de presque toutes les bases de données que vous créerez. 

#### HTTP et CRUD

Les opérations CRUD correspondent bien aux méthodes HTTP que vous avez peut-être déjà apprises :

* `HTTP POST` - `CREATE`
* `HTTP GET` - `READ`
* `HTTP PUT` - `UPDATE`
* `HTTP DELETE` - `DELETE`

### Instruction INSERT en SQL

Les tables sont assez inutiles sans données. En SQL, nous pouvons ajouter des enregistrements à une table en utilisant une instruction `INSERT INTO`. Lorsque nous utilisons une instruction `INSERT`, nous devons d'abord spécifier la `table` dans laquelle nous insérons l'enregistrement, suivie des `champs` dans cette table auxquels nous voulons ajouter des `VALUES`.

Voici un exemple d'instruction `INSERT INTO` :

```SQL
INSERT INTO employees(id, name, title)
VALUES (1, 'Allan', 'Engineer');
```


### Cycle de vie de la base de données HTTP CRUD

Il est important de comprendre comment les données *circulent* dans une application web typique.

![database flow](https://i.imgur.com/hli3crD.png)

1. Le front-end traite certaines données à partir de l'entrée de l'utilisateur - peut-être qu'un formulaire est soumis.
2. Le front-end envoie ces données au serveur via une requête HTTP - peut-être un `POST`.
3. Le serveur effectue une requête SQL à sa base de données pour créer un enregistrement associé - Probablement en utilisant une instruction `INSERT`.
4. Une fois que le serveur a traité que la requête de la base de données a réussi, il répond au front-end avec un code de statut ! Espérons un code de niveau 200 (succès) !

### Saisie manuelle

Insérer manuellement *chaque* enregistrement dans une base de données serait une tâche *extêmement* chronophage ! Travailler avec du SQL brut comme nous le faisons maintenant n'est pas très courant lors de la conception de [systèmes backend](https://blog.boot.dev/backend/do-backend-devs-need-sql/).

Lorsque vous travaillez avec SQL dans un système logiciel, comme une application web backend, vous aurez généralement accès à un langage de programmation tel que [Go](https://boot.dev/learn/learn-golang) ou [Python](https://boot.dev/learn/learn-python). 

Par exemple, un serveur backend écrit en Go peut utiliser la concaténation de chaînes pour créer dynamiquement des instructions SQL, et c'est généralement ainsi que cela se fait.

```go
sqlQuery := fmt.Sprintf(`
INSERT INTO users(name, age, country_code)
VALUES ('%s', %v, %s);
`, user.Name, user.Age, user.CountryCode)
```

#### Injection SQL

L'exemple ci-dessus est une simplification excessive de ce qui se passe *réellement* lorsque vous accédez à une base de données en utilisant du code Go. En essence, c'est correct. L'interpolation de chaînes est la manière dont les systèmes de production accèdent aux bases de données. Cela dit, cela doit être fait *prudemment* pour ne pas être une [vulnérabilité de sécurité](https://en.wikipedia.org/wiki/SQL_injection). Nous en parlerons plus tard !

### Compter

Nous pouvons utiliser une instruction `SELECT` pour obtenir un compte des enregistrements dans une table. Cela peut être très utile lorsque nous devons savoir combien d'enregistrements il y a, mais que nous ne nous soucions pas particulièrement de ce qu'ils contiennent.

Voici un exemple dans SQLite :

```SQL
SELECT count(*) from employees;
```

Le `*` dans ce cas fait référence à un nom de colonne. Nous ne nous soucions pas du compte d'une colonne spécifique - nous voulons connaître le nombre total d'enregistrements, donc nous pouvons utiliser le caractère générique (*).

### Cycle de vie de la base de données HTTP CRUD

Nous avons parlé de la manière dont une opération "create" circule dans une application web. Parlons d'une "lecture".

![read lifecycle](https://i.imgur.com/KTDQGy1.png)

Prenons un exemple. Notre chef de produit veut afficher les données de profil sur la page des paramètres de l'utilisateur. Voici comment nous pourrions concevoir cette demande de fonctionnalité :

1. Tout d'abord, la page web du front-end se charge.
2. Le front-end envoie une requête HTTP `GET` à un point de terminaison `/users` sur le serveur backend.
3. Le serveur reçoit la requête.
4. Le serveur utilise une instruction `SELECT` pour récupérer l'enregistrement de l'utilisateur de la table `users` dans la base de données.
5. Le serveur convertit la ligne de données SQL en un objet `JSON` et l'envoie au front-end.

### Clause WHERE

Afin de continuer à apprendre les opérations CRUD en SQL, nous devons apprendre à rendre les instructions que nous envoyons à la base de données plus spécifiques. SQL accepte une clause `WHERE` dans une requête qui nous permet d'être très spécifiques avec nos instructions.

Si nous ne pouvions pas spécifier l'enregistrement spécifique que nous voulions `LIRE`, `METTRE À JOUR` ou `SUPPRIMER`, faire des requêtes à une base de données serait très frustrant et très inefficace.

#### Utilisation d'une clause WHERE

Supposons que nous avons plus de 9000 enregistrements dans notre table `users`. Nous voulons souvent regarder des données utilisateur spécifiques dans cette table sans récupérer *tous* les autres enregistrements de la table. Nous pouvons utiliser une instruction `SELECT` suivie d'une clause `WHERE` pour spécifier quels enregistrements récupérer. L'instruction `SELECT` reste la même, nous ajoutons simplement la clause `WHERE` à la fin du `SELECT`. 

Voici un exemple :

```SQL
SELECT name FROM users WHERE power_level >= 9000;
```

Cela sélectionnera uniquement le champ `name` de tout utilisateur dans la table `users` `WHERE` le champ `power_level` est supérieur ou égal à `9000`.

### Trouver des valeurs NULL

Vous pouvez utiliser une clause `WHERE` pour filtrer les valeurs selon qu'elles sont `NULL` ou non.

#### IS NULL

```SQL
SELECT name FROM users WHERE first_name IS NULL;
```

#### IS NOT NULL

```SQL
SELECT name FROM users WHERE first_name IS NOT NULL;
```


### DELETE

Lorsque qu'un utilisateur supprime son compte sur Twitter, ou supprime un commentaire sur une vidéo YouTube, ces données doivent être supprimées de leur base de données respective.

#### Instruction DELETE

Une instruction `DELETE` supprime un enregistrement d'une table qui correspond à la clause `WHERE`. Par exemple :

```SQL
DELETE from employees
    WHERE id = 251;
```

Cette instruction `DELETE` supprime tous les enregistrements de la table `employees` qui ont un id de `251` !

### Le danger de supprimer des données

Supprimer des données peut être une opération dangereuse. Une fois supprimées, les données peuvent être très difficiles, voire impossibles à restaurer ! Parlons de quelques méthodes courantes que les ingénieurs backend utilisent pour protéger contre la perte de données client précieuses.

#### Stratégie 1 - Sauvegardes

Si vous utilisez un service cloud comme [Cloud SQL](https://cloud.google.com/sql) de GCP ou [RDS](https://aws.amazon.com/rds/) d'AWS, vous devez *toujours* activer les sauvegardes automatisées. Elles prennent un instantané automatique de votre base de données entière à intervalles réguliers et le conservent pendant une certaine période.

Par exemple, la base de données Boot.dev a un instantané de sauvegarde pris quotidiennement et nous conservons ces sauvegardes pendant 30 jours. Si j'exécute accidentellement une requête qui supprime des données précieuses, je peux les restaurer à partir de la sauvegarde.

**Vous devriez avoir une stratégie de sauvegarde pour les bases de données de production.**

#### Stratégie 2 - Suppressions logiques

Une "suppression logique" est lorsque vous ne supprimez pas réellement les données de votre base de données, mais que vous "marquez" simplement les données comme supprimées. 

Par exemple, vous pourriez définir une date `deleted_at` sur la ligne que vous souhaitez supprimer. Ensuite, dans vos requêtes, vous ignorez tout ce qui a une date `deleted_at` définie. L'idée est que cela permet à votre application de se comporter comme si elle supprimait des données, mais vous pouvez toujours revenir en arrière et restaurer toutes les données qui ont été supprimées.

Vous ne devriez probablement effectuer une suppression logique que si vous avez une raison spécifique de le faire. Les sauvegardes automatisées devraient être "suffisantes" pour la plupart des applications qui ne cherchent qu'à se protéger contre les erreurs des développeurs.

%[https://www.youtube.com/watch?v=kCWHniEnQDM]

### Requête de mise à jour en SQL

Chaque fois que vous mettez à jour votre photo de profil ou changez votre mot de passe en ligne, vous modifiez les données d'un champ dans une table d'une base de données. Imaginez si chaque fois que vous faisiez une erreur dans un tweet sur Twitter, vous deviez supprimer tout le tweet et en poster un nouveau au lieu de simplement l'éditer...

...Eh bien, c'est un mauvais exemple.

#### Instruction de mise à jour

L'instruction `UPDATE` en SQL nous permet de mettre à jour les champs d'un enregistrement. Nous pouvons même mettre à jour de nombreux enregistrements en fonction de la manière dont nous écrivons l'instruction.

Une instruction `UPDATE` spécifie la table qui doit être mise à jour, suivie des champs et de leurs nouvelles valeurs en utilisant le mot-clé `SET`. Enfin, une clause `WHERE` indique les enregistrements à mettre à jour.

```SQL
UPDATE employees
SET job_title = 'Backend Engineer', salary = 150000
WHERE id = 251;
```


### Mappage objet-relationnel (ORM)

Un [mappage objet-relationnel](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) ou un *ORM* en abrégé, est un outil qui permet d'effectuer des opérations CRUD sur une base de données en utilisant un langage de programmation traditionnel. Ceux-ci se présentent généralement sous la forme d'une bibliothèque ou d'un framework que vous utiliseriez dans votre code backend.

Le principal avantage qu'un ORM offre est qu'il mappe vos enregistrements de base de données à des objets en mémoire. Par exemple, en Go, nous pourrions avoir une struct que nous utilisons dans notre code :

```go
type User struct {
    ID int
    Name string
    IsAdmin bool
}
```

Cette définition de struct représente commodément une table de base de données appelée `users`, et une instance de la struct représente une ligne dans la table.

#### Exemple : Utilisation d'un ORM

En utilisant un ORM, nous pourrions être en mesure d'écrire un code simple comme ceci :

```go
user := User{
    ID: 10,
    Name: "Lane",
    IsAdmin: false,
}

// génère une instruction SQL et l'exécute,
// créant un nouvel enregistrement dans la table users
db.Create(user)
```

#### Exemple : Utilisation de SQL pur

En utilisant SQL pur, nous pourrions devoir faire quelque chose de plus manuel :

```go
user := User{
    ID: 10,
    Name: "Lane",
    IsAdmin: false,
}

db.Exec("INSERT INTO users (id, name, is_admin) VALUES (?, ?, ?);",
    user.ID, user.Name, user.IsAdmin)
```

#### Devriez-vous utiliser un ORM ?

Cela dépend – un ORM échange généralement la simplicité contre le contrôle.

En utilisant SQL pur, vous pouvez tirer pleinement parti de la puissance du langage SQL. En utilisant un ORM, vous êtes limité par les fonctionnalités que l'ORM offre. 

Si vous rencontrez des problèmes avec une requête spécifique, il peut être plus difficile de la déboguer avec un ORM car vous devez creuser dans le code et la documentation du framework pour comprendre comment les requêtes sous-jacentes sont générées.

Je recommande de faire des projets des deux manières afin que vous puissiez apprendre les compromis. À la fin de la journée, lorsque vous travaillez au sein d'une équipe de développeurs, ce sera une décision d'équipe.

## Chapitre 5 : Requêtes SQL de base

### Comment utiliser la clause `AS` en SQL

Parfois, nous devons structurer les données que nous retournons de nos requêtes d'une manière spécifique. Une clause `AS` nous permet de "renommer" une donnée dans notre requête. L'alias n'existe que pour la durée de la requête. 

#### Mot-clé `AS`

Les requêtes suivantes retournent les mêmes données :

```SQL
SELECT employee_id AS id, employee_name AS name
FROM employees;
```

et :

```SQL
SELECT employee_id, employee_name
FROM employees;
```

La différence est que les résultats de la requête aliasée auraient des noms de colonnes `id` et `name` au lieu de `employee_id` et `employee_name`.

### Fonctions SQL

À la fin de la journée, SQL est un langage de programmation, et c'est un langage qui supporte les fonctions. Nous pouvons utiliser des fonctions et des alias pour *calculer* de nouvelles colonnes dans une requête. Cela est similaire à la manière dont vous pourriez utiliser des formules dans Excel.

#### Fonction IIF

Dans SQLite, la fonction `IIF` fonctionne comme un [ternaire](https://book.pythontips.com/en/latest/ternary_operators.html). Par exemple :

```SQL
IIF(carA > carB, "Car a is bigger", "Car b is bigger")
```

Si `a` est supérieur à `b`, cette instruction évalue la chaîne `"Car a is bigger"`. Sinon, elle évalue `"Car b is bigger"`.

Voici comment nous pouvons utiliser `IIF()` et un alias `directive` pour ajouter une nouvelle colonne calculée à notre ensemble de résultats :

```SQL
SELECT quantity,
    IIF(quantity < 10, "Order more", "In Stock") AS directive
    from products
```

### Comment utiliser `BETWEEN` avec `WHERE`

Nous pouvons vérifier si certaines valeurs sont `between` deux nombres en utilisant la clause `WHERE` de manière intuitive. La clause `WHERE` n'a pas toujours besoin d'être utilisée pour spécifier des identifiants ou des valeurs spécifiques. Nous pouvons également l'utiliser pour aider à réduire notre ensemble de résultats. Voici un exemple :

```SQL
SELECT employee_name, salary
FROM employees
WHERE salary BETWEEN 30000 and 60000;
```

Cette requête retourne tous les champs `name` et `salary` des employés pour toutes les lignes où le `salary` est `BETWEEN` 30 000 et 60 000. Nous pouvons également interroger les résultats qui ne sont pas `BETWEEN` deux valeurs spécifiées. 

```SQL
SELECT product_name, quantity
FROM products
WHERE quantity NOT BETWEEN 20 and 100;
```

Cette requête retourne tous les noms de produits où la quantité n'était pas entre `20` et `100`. Nous pouvons utiliser des conditionnelles pour rendre les résultats de notre requête aussi spécifiques que nous en avons besoin.

### Comment retourner des valeurs distinctes

Parfois, nous voulons récupérer des enregistrements d'une table sans obtenir de doublons.

Par exemple, nous pouvons vouloir connaître toutes les différentes entreprises pour lesquelles nos employés ont travaillé précédemment, mais nous ne voulons pas voir la même entreprise plusieurs fois dans le rapport.

#### `SELECT DISTINCT`

SQL nous offre le mot-clé `DISTINCT` qui supprime les enregistrements en double de la requête résultante.

```SQL
SELECT DISTINCT previous_company
    FROM employees;
```

Cela ne retourne qu'une seule ligne pour chaque valeur unique de `previous_company`.

### Opérateurs logiques

Nous devons souvent utiliser plusieurs conditions pour récupérer les informations exactes que nous voulons. Nous pouvons commencer à structurer des requêtes beaucoup plus complexes en utilisant plusieurs conditions ensemble pour réduire les résultats de recherche de notre requête.

L'opérateur logique `AND` peut être utilisé pour réduire encore plus nos ensembles de résultats.

#### Opérateur `AND`

```SQL
SELECT product_name, quantity, shipment_status
    FROM products
    WHERE shipment_status = 'pending'
    AND quantity BETWEEN 0 and 10;
```

Cela ne récupère que les enregistrements où à la fois le `shipment_status` est "pending" ET la `quantity` est entre `0` et `10`.

#### Opérateurs d'égalité

Tous les opérateurs suivants sont supportés en SQL. Le `=` est le principal à surveiller, ce n'est pas `==` comme dans de nombreux autres langages.

* `=`
* `<`
* `>`
* `<=`
* `>=`

Par exemple, en Python, vous pourriez comparer deux valeurs comme ceci :

```py
if name == "age"
```

Alors qu'en SQL, vous feriez :

```sql
WHERE name = "age"
```

#### Opérateur `OR`

Comme vous l'avez probablement deviné, si l'opérateur logique `AND` est supporté, l'opérateur `OR` est probablement également supporté.

```SQL
SELECT product_name, quantity, shipment_status
    FROM products
    WHERE shipment_status = 'out of stock'
    OR quantity BETWEEN 10 and 100;
```

Cette requête récupère les enregistrements où soit la condition `shipment_status` OU la condition `quantity` sont remplies.

L'ordre des opérations compte lorsque vous utilisez ces opérateurs.

Vous pouvez regrouper les opérations logiques avec des parenthèses pour spécifier l'[ordre des opérations](https://www.mathsisfun.com/operation-order-pemdas.html).

```sql
(this AND that) OR the_other
```

#### L'opérateur `IN`

Une autre variation de la clause `WHERE` que nous pouvons utiliser est l'opérateur `IN`. `IN` retourne `true` ou `false` si le premier opérande correspond à l'une des valeurs du deuxième opérande. L'opérateur `IN` est un raccourci pour plusieurs conditions `OR`.

Ces deux requêtes sont équivalentes :

```SQL
SELECT product_name, shipment_status
    FROM products
    WHERE shipment_status IN ('shipped', 'preparing', 'out of stock');
```

```SQL
SELECT product_name, shipment_status
    FROM products
    WHERE shipment_status = 'shipped'
        OR shipment_status = 'preparing'
        OR shipment_status = 'out of stock';
```

Espérons que vous commencez à voir comment l'interrogation de données spécifiques à l'aide de clauses SQL finement réglées aide à révéler des informations importantes. Plus une table devient grande, plus il devient difficile de l'analyser sans requêtes appropriées.

#### Le mot-clé `LIKE`

Parfois, nous n'avons pas le luxe de savoir exactement ce que nous devons interroger. Avez-vous déjà voulu chercher une chanson ou une vidéo mais vous ne vous souvenez que d'une partie du nom ? SQL nous offre une option pour les situations `LIKE` celle-ci.

Le mot-clé `LIKE` permet l'utilisation des opérateurs génériques `%` et `_`. Concentrons-nous d'abord sur `%`.

#### Opérateur `%`

L'opérateur `%` correspondra à zéro ou plusieurs caractères. Nous pouvons utiliser cet opérateur dans notre chaîne de requête pour trouver plus que des correspondances exactes en fonction de l'endroit où nous le plaçons.

Voici quelques exemples qui montrent comment cela fonctionne :

Produit commençant par "banana" :

```SQL
SELECT * FROM products
WHERE product_name LIKE 'banana%';
```

Produit se terminant par "banana" :
 
```SQL
SELECT * from products
WHERE product_name LIKE '%banana';
```

Produit contenant "banana" :

```SQL
SELECT * from products
WHERE product_name LIKE '%banana%';
```

### Opérateur de soulignement

Comme discuté, l'opérateur générique `%` correspond à zéro ou plusieurs caractères. Pendant ce temps, l'opérateur générique `_` ne correspond qu'à un seul caractère.

```SQL
SELECT * FROM products
    WHERE product_name LIKE '_oot';
```

La requête ci-dessus correspond à des produits comme :

* boot
* root
* foot

```SQL
SELECT * FROM products
    WHERE product_name LIKE '__oot';
```

La requête ci-dessus correspond à des produits comme :

* shoot
* groot

## Chapitre 6 : Comment structurer les données retournées en SQL

### Le mot-clé `LIMIT`

Parfois, nous ne voulons pas récupérer chaque enregistrement d'une table. Par exemple, il est courant qu'une table de base de données de production ait des millions de lignes, et `SELECT`er toutes pourrait planter votre système. C'est là que le mot-clé `LIMIT` entre en jeu.

Le mot-clé `LIMIT` peut être utilisé à la fin d'une instruction select pour réduire le nombre d'enregistrements retournés.

```SQL
SELECT * FROM products
    WHERE product_name LIKE '%berry%'
    LIMIT 50;
```

La requête ci-dessus récupère tous les enregistrements de la table `products` où le nom contient le mot berry. Si nous exécutions cette requête sur la base de données Facebook, elle retournerait presque certainement beaucoup d'enregistrements. 

L'instruction `LIMIT` ne permet à la base de données de retourner que jusqu'à 50 enregistrements correspondant à la requête. Cela signifie que si ce n'est pas autant d'enregistrements qui correspondent à la requête, l'instruction `LIMIT` n'aura pas d'effet.

### Le mot-clé `ORDER BY` en SQL

SQL nous offre également la possibilité de trier les résultats d'une requête en utilisant `ORDER BY`. Par défaut, le mot-clé `ORDER BY` trie les enregistrements par le champ donné dans l'ordre croissant, ou `ASC` pour faire court. Cependant, `ORDER BY` supporte également l'ordre décroissant avec le mot-clé `DESC`.

#### Exemples

Cette requête retourne les champs `name`, `price` et `quantity` de la table `products` triés par `price` dans l'ordre croissant :

```SQL
SELECT name, price, quantity FROM products
    ORDER BY price;
```

Cette requête retourne le `name`, `price` et `quantity` des produits commandés par la quantité dans l'ordre décroissant :

```SQL
SELECT name, price, quantity FROM products
    ORDER BY quantity desc;
```

### Order By et Limit

Lorsque vous utilisez à la fois `ORDER BY` et `LIMIT`, la clause `ORDER BY` doit venir en premier.



## Chapitre 7 : Comment effectuer des agrégations en SQL

Une "agrégation" est une valeur unique dérivée en combinant plusieurs autres valeurs. Nous avons effectué une agrégation plus tôt lorsque nous avons utilisé l'instruction `count` pour compter le nombre d'enregistrements dans une table.

### Pourquoi utiliser des agrégations ?

Les données stockées dans une base de données doivent généralement être stockées [brutes](https://wagslane.dev/posts/keep-your-data-raw-at-rest/). Lorsque nous devons calculer certaines données supplémentaires à partir des données brutes, nous pouvons utiliser une agrégation.

Prenons l'exemple de l'agrégation `count` suivante :

```SQL
SELECT COUNT(*)
FROM products
WHERE quantity = 0;
```

Cette requête retourne le nombre de produits qui ont une `quantity` de `0`. Nous pourrions stocker un compte des produits dans une table de base de données séparée, et l'incrémenter/décrémenter chaque fois que nous apportons des modifications à la table `products` - mais cela serait redondant. 

Il est beaucoup plus simple de stocker les produits en un seul endroit (nous appelons cela une [source unique de vérité](https://en.wikipedia.org/wiki/Single_source_of_truth)) et d'exécuter une agrégation lorsque nous devons dériver des informations supplémentaires à partir des données brutes.

### La fonction `SUM`

La fonction d'agrégation `sum` retourne la somme d'un ensemble de valeurs.

Par exemple, la requête ci-dessous retourne un seul enregistrement contenant un seul champ. La valeur retournée est égale au salaire total perçu par tous les `employees` de la table `employees`.

```SQL
SELECT sum(salary)
FROM employees;
```

Ce qui retourne :

| SUM(SALARY) |
| ----------- |
| 2483        |

### La fonction `MAX`

Comme vous pouvez vous y attendre, la fonction `max` récupère la *plus grande* valeur d'un ensemble de valeurs. Par exemple :

```SQL
SELECT max(price)
FROM products
```

Cette requête parcourt tous les prix de la table `products` et retourne le prix avec la valeur de prix la plus élevée. N'oubliez pas qu'elle ne retourne que le `price`, et non le reste de l'enregistrement. Vous devez toujours spécifier chaque champ que vous souhaitez qu'une requête retourne.


#### Une note sur le schéma

* Le `sender_id` sera présent pour toute transaction où l'utilisateur en question (`user_id`) reçoit de l'argent (de l'expéditeur).
* Le `recipient_id` sera présent pour toute transaction où l'utilisateur en question (`user_id`) envoie de l'argent (au destinataire).

En d'autres termes, une transaction ne peut avoir qu'un `sender_id` ou un `recipient_id` - pas les deux. La présence de l'un ou de l'autre indique si l'argent entre ou sort du compte de l'utilisateur.

Ce schéma `user_id`, `recipient_id`, `sender_id` que nous avons conçu n'est qu'une façon de concevoir une base de données de transactions - il existe d'autres façons valides de le faire. C'est celle que nous utilisons, et plus tard nous parlerons davantage des compromis dans les différentes options de conception de base de données.

### La fonction `MIN`

La fonction `min` fonctionne de la même manière que la fonction `max` mais trouve la valeur la plus basse au lieu de la valeur la plus élevée.

```SQL
SELECT product_name, min(price)
from products;
```

Cette requête retourne les champs `product_name` et `price` de l'enregistrement avec le `price` le plus bas.

### La clause `GROUP BY`

Il arrive que nous devions regrouper des données en fonction de valeurs spécifiques.

SQL offre la clause `GROUP BY` qui peut regrouper des lignes ayant des valeurs similaires en lignes "résumé". Elle retourne une ligne pour chaque groupe. La partie intéressante est que chaque groupe peut avoir une fonction d'agrégation appliquée qui opère uniquement sur les données regroupées.

#### Exemple de `GROUP BY`

Imaginez que nous avons une base de données avec des chansons et des albums, et que nous voulons voir combien de chansons il y a sur chaque album. Nous pouvons utiliser une requête comme celle-ci :

```SQL
SELECT album_id, count(song_id)
FROM songs
GROUP BY album_id;
```

Cette requête récupère un compte de toutes les chansons sur chaque album. Un enregistrement est retourné par album, et chacun a son propre `count`.

### La fonction `AVG()`

Tout comme nous pouvons vouloir trouver les valeurs minimales ou maximales dans un ensemble de données, parfois nous devons connaître la [moyenne](https://en.wikipedia.org/wiki/Arithmetic_mean) !

SQL nous offre la fonction `AVG()`. Similaire à `MAX()`, `AVG()` calcule la moyenne de toutes les valeurs non-NULL. 

```SQL
select song_name, avg(song_length)
from songs
```

Cette requête retourne la longueur moyenne des `song_length` dans la table `songs`.

### La clause `HAVING`

Lorsque nous devons filtrer les résultats d'une requête `GROUP BY` encore plus, nous pouvons utiliser la clause `HAVING`. La clause `HAVING` spécifie une condition de recherche pour un groupe.

La clause `HAVING` est similaire à la clause `WHERE`, mais elle opère sur des groupes après qu'ils aient été regroupés, plutôt que sur des lignes avant qu'elles aient été regroupées.

```SQL
SELECT album_id, count(id) as count
FROM songs
GROUP BY album_id
HAVING count > 5;
```

Cette requête retourne l'`album_id` et le compte de ses chansons, mais uniquement pour les albums avec plus de `5` chansons.

### `HAVING` vs `WHERE` en SQL

Il est assez courant que les développeurs soient confus sur la différence entre les clauses `HAVING` et `WHERE` - elles sont assez similaires après tout.

La différence est assez simple en réalité :

* Une condition `WHERE` est appliquée à toutes les données d'une requête avant qu'elles ne soient regroupées par une clause `GROUP BY`.
* Une condition `HAVING` n'est appliquée qu'aux lignes regroupées qui sont retournées après qu'un `GROUP BY` soit appliqué.

Cela signifie que si vous voulez filtrer sur le résultat d'une agrégation, vous devez utiliser `HAVING`. Si vous voulez filtrer sur une valeur présente dans les données brutes, vous devriez utiliser une simple clause `WHERE`.

### La fonction `ROUND`

Parfois, nous devons [arrondir](https://en.wikipedia.org/wiki/Rounding) certains nombres, en particulier lorsque nous travaillons avec les résultats d'une agrégation. Nous pouvons utiliser la fonction `ROUND()` pour faire le travail.

La fonction SQL `round()` vous permet de spécifier à la fois la valeur que vous souhaitez arrondir et la précision à laquelle vous souhaitez l'arrondir :

```SQL
round(value, precision)
```

Si aucune précision n'est donnée, SQL arrondira la valeur à la valeur entière la plus proche :

```SQL
select song_name, round(avg(song_length), 1)
from songs
```

Cette requête retourne la longueur moyenne des `song_length` de la table `songs`, arrondie à un seul chiffre décimal.

## Chapitre 8 : Sous-requêtes SQL

### Sous-requêtes

Parfois, une seule requête ne suffit pas pour récupérer les enregistrements spécifiques dont nous avons besoin.

Il est possible d'exécuter une requête sur le jeu de résultats d'une autre requête - une requête dans une requête ! Cela s'appelle "query-ception"... euh... je veux dire une "sous-requête".

Les sous-requêtes peuvent être très utiles dans un certain nombre de situations lorsque l'on essaie de récupérer des données spécifiques qui ne seraient pas accessibles en interrogeant simplement une seule table.

#### Comment récupérer des données à partir de plusieurs tables

Voici un exemple de sous-requête :

```SQL
SELECT id, song_name, artist_id
FROM songs
WHERE artist_id IN (
    SELECT id
    FROM artists
    WHERE artist_name LIKE 'Rick%'
);
```

Dans cette base de données hypothétique, la requête ci-dessus sélectionne tous les `song_id`, `song_name` et `artist_id` de la table `songs` qui sont écrits par des artistes dont le nom commence par "Rick". Remarquez que la sous-requête nous permet d'utiliser des informations d'une table différente - dans ce cas, la table `artists`.

#### Syntaxe des sous-requêtes

La seule syntaxe unique à une sous-requête est les parenthèses entourant la requête imbriquée. L'opérateur `IN` pourrait être différent, par exemple, nous pourrions utiliser l'opérateur `=` si nous attendons une seule valeur à retourner.

Voici un exemple :

```SQL
SELECT id, song_name, artist_id
FROM songs
WHERE artist_id IN (
    SELECT id
    FROM artists
    WHERE artist_name LIKE 'Rick%'
);
```

### Aucune table nécessaire

Lorsque vous travaillez sur une application backend, cela n'arrive pas souvent, mais il est important de se rappeler que **SQL est un langage de programmation complet**. Nous l'utilisons généralement pour interagir avec des données stockées dans des tables, mais il est assez flexible et puissant.

Par exemple, vous pouvez `SELECT` des informations qui sont simplement calculées, sans avoir besoin de tables.

```SQL
SELECT 5 + 10 as sum;
```

## Chapitre 9 : Normalisation de la base de données


### Relations entre les tables

Les bases de données relationnelles sont puissantes grâce aux relations entre les tables. Ces relations nous aident à garder nos bases de données propres et efficaces. 

Une relation entre les tables suppose que l'une de ces tables a une `clé étrangère` qui référence la `clé primaire` d'une autre table.

@[youtube](https://www.youtube.com/watch?v=WJTdg1AsSz0)

#### Types de relations

Il existe 3 types principaux de relations dans une base de données relationnelle :

1. Un à un
2. Un à plusieurs
3. Plusieurs à plusieurs

![relationships](https://i.imgur.com/u4i6XdL.png)

### Un à un

Une relation `un à un` se manifeste le plus souvent sous la forme d'un champ ou d'un ensemble de champs sur une ligne dans une table. Par exemple, un `user` aura exactement un `password`.

Les champs de paramètres pourraient être un autre exemple de relation un à un. Un utilisateur aura exactement une `email_preference` et exactement une `birthday`.

### Un à plusieurs

Lorsque l'on parle des relations entre les tables, une relation un à plusieurs est probablement la relation la plus couramment utilisée. 

Une relation un à plusieurs se produit lorsqu'un seul enregistrement dans une table est lié à potentiellement plusieurs enregistrements dans une autre table. 

Notez que la relation un->plusieurs ne fonctionne que dans un sens, un enregistrement dans la deuxième table ne peut pas être lié à plusieurs enregistrements dans la première table !

#### Exemples de relations un à plusieurs

* Une table `customers` et une table `orders`. Chaque client a `0`, `1`, ou plusieurs commandes qu'il a passées.
* Une table `users` et une table `transactions`. Chaque `user` a `0`, `1`, ou plusieurs transactions auxquelles il a participé.

### Plusieurs à plusieurs

Une relation plusieurs à plusieurs se produit lorsque plusieurs enregistrements dans une table peuvent être liés à plusieurs enregistrements dans une autre table.

#### Exemples de relations plusieurs à plusieurs

* Une table `products` et une table `suppliers` - Les produits peuvent avoir `0` à plusieurs fournisseurs, et les fournisseurs peuvent fournir `0` à plusieurs produits.
* Une table `classes` et une table `students` - Les étudiants peuvent suivre potentiellement plusieurs cours et les cours peuvent avoir plusieurs étudiants inscrits.

#### Joindre des tables

Joindre des tables aide à définir des relations plusieurs à plusieurs entre les données dans une base de données. Par exemple, lors de la définition de la relation ci-dessus entre les produits et les fournisseurs, nous définirions une table de jointure appelée `products_suppliers` qui contient les clés primaires des tables à joindre.

Ensuite, lorsque nous voulons voir si un fournisseur fournit un produit spécifique, nous pouvons regarder dans la table de jointure pour voir si les identifiants partagent une ligne.

#### Contraintes uniques sur 2 champs

Lors de l'application de contraintes de schéma spécifiques, nous pouvons avoir besoin d'appliquer la contrainte `UNIQUE` sur deux champs différents.

```SQL
CREATE TABLE product_suppliers (
  product_id INTEGER,
  supplier_id INTEGER,
  UNIQUE(product_id, supplier_id)
);
```

Cela garantit que nous pouvons avoir plusieurs lignes avec le même `product_id` ou `supplier_id`, mais nous ne pouvons pas avoir deux lignes où à la fois le `product_id` et le `supplier_id` sont les mêmes.

### Normalisation de la base de données

La normalisation de la base de données est une méthode pour structurer votre schéma de base de données de manière à aider :

* Améliorer l'intégrité des données
* Réduire la redondance des données

#### Qu'est-ce que l'intégrité des données ?

"L'intégrité des données" fait référence à l'exactitude et à la cohérence des données. Par exemple, si l'âge d'un utilisateur est stocké dans une base de données, plutôt que sa date de naissance, cette donnée devient incorrecte automatiquement avec le passage du temps.

Il serait préférable de stocker une date de naissance et de calculer l'âge au besoin.

#### Qu'est-ce que la redondance des données ?

La "redondance des données" se produit lorsque la même donnée est stockée à plusieurs endroits. Par exemple : enregistrer le même fichier plusieurs fois sur différents disques durs.

La redondance des données peut être problématique, surtout lorsque les données à un endroit sont modifiées de telle sorte que les données ne sont plus cohérentes sur toutes les copies de ces données.

%[https://www.youtube.com/watch?v=U3L4NYNwb6k]

### Formes normales

Le créateur de la "normalisation des bases de données", [Edgar F. Codd](https://en.wikipedia.org/wiki/Edgar_F._Codd), a décrit différentes "formes normales" qu'une base de données peut respecter. Nous parlerons des plus courantes.

* Première forme normale (1NF)
* Deuxième forme normale (2NF)
* Troisième forme normale (3NF)
* Forme normale de Boyce-Codd (BCNF)

![normal forms](https://i.imgur.com/CpDOeej.png)

En bref, la 1ère forme normale est la forme la moins "normalisée", et la forme normale de Boyce-Codd est la plus "normalisée".

Plus une base de données est normalisée, meilleure est son intégrité des données, et moins vous aurez de données en double.

#### Dans le contexte des formes normales, "clé primaire" signifie quelque chose de légèrement différent

Dans le contexte de la normalisation des bases de données, nous allons utiliser le terme "clé primaire" légèrement différemment. Lorsque nous parlons de SQLite, une "clé primaire" est une colonne unique qui identifie de manière unique une ligne.

Lorsque nous parlons plus généralement de la normalisation des données, le terme "clé primaire" signifie la collection de colonnes qui identifient de manière unique une ligne. Cela peut être une seule colonne, mais cela peut en fait être n'importe quel nombre de colonnes. Une clé primaire est le nombre minimum de colonnes nécessaires pour identifier de manière unique une ligne dans une table. 

Si vous pensez à la table de jointure plusieurs-à-plusieurs `product_suppliers`, la "clé primaire" de cette table était en fait une combinaison des 2 identifiants, `product_id` et `supplier_id` :

```SQL
CREATE TABLE product_suppliers (
    product_id INTEGER,
    supplier_id INTEGER,
    UNIQUE(product_id, supplier_id)
);
```

### 1ère Forme Normale (1NF)

Pour être conforme à la [première forme normale](https://en.wikipedia.org/wiki/First_normal_form), une table de base de données doit simplement suivre 2 règles :

* Elle doit avoir une clé primaire unique.
* Une cellule ne peut pas avoir une table imbriquée comme valeur (selon la base de données que vous utilisez, cela peut ne pas être possible)

#### Exemple de NON 1ère forme normale

| name  | age | email          |
| ----- | --- | -------------- |
| Lane  | 27  | lane@boot.dev  |
| Lane  | 27  | lane@boot.dev  |
| Allan | 27  | allan@boot.dev |

Cette table ne respecte pas la 1NF. Elle a deux lignes identiques, donc il n'y a pas de clé primaire unique pour chaque ligne.

#### Exemple de 1ère forme normale

La manière la plus simple (mais pas la seule) de se conformer à la première forme normale est d'ajouter une colonne `id` unique.

| id  | name  | age | email          |
| --- | ----- | --- | -------------- |
| 1   | Lane  | 27  | lane@boot.dev  |
| 2   | Lane  | 27  | lane@boot.dev  |
| 3   | Allan | 27  | allan@boot.dev |

Il est intéressant de noter que si vous créez une "clé primaire" en vous assurant que deux colonnes sont toujours "uniques ensemble", cela fonctionne aussi.

#### Vous ne devriez *presque* jamais concevoir une table qui ne respecte pas la 1NF

La première forme normale est simplement une bonne idée. Je n'ai jamais construit un schéma de base de données où chaque table n'est pas au moins en première forme normale.

### 2ème Forme Normale (2NF)

Une table en [deuxième forme normale](https://en.wikipedia.org/wiki/Second_normal_form) suit toutes les règles de la 1ère forme normale, et une règle supplémentaire :

* Toutes les colonnes qui ne font pas partie de la clé primaire dépendent de la clé primaire entière, et pas seulement d'une des colonnes de la clé primaire.

#### Exemple de 1ère NF, mais pas de 2ème NF

Dans cette table, la clé primaire est une combinaison de `first_name` + `last_name`.

| first_name | last_name | first_initial |
| ---------- | --------- | ------------- |
| Lane       | Wagner    | l             |
| Lane       | Small     | l             |
| Allan      | Wagner    | a             |

Cette table ne respecte pas la 2NF. La colonne `first_initial` dépend entièrement de la colonne `first_name`, la rendant redondante.

#### Exemple de 2ème forme normale

Une façon de convertir la table ci-dessus en 2NF est d'ajouter une nouvelle table qui mappe un `first_name` directement à son `first_initial`. Cela supprime tous les doublons :

| first_name | last_name |
| ---------- | --------- |
| Lane       | Wagner    |
| Lane       | Small     |
| Allan      | Wagner    |

| first_name | first_initial |
| ---------- | ------------- |
| Lane       | l             |
| Allan      | a             |

#### La 2NF est *généralement* une bonne idée

Vous devriez probablement par défaut garder vos tables en deuxième forme normale. Cela dit, il y a de bonnes raisons de s'en écarter, en particulier pour des raisons de performance. La raison étant que lorsque vous devez interroger une deuxième table pour obtenir des données supplémentaires, cela peut prendre un peu plus de temps.

Ma règle de base est :

> Optimisez pour l'intégrité des données et la dé-duplication des données en premier. Si vous avez des problèmes de vitesse, dé-normalisez en conséquence.

### 3ème Forme Normale (3NF)

Une table en [3ème forme normale](https://en.wikipedia.org/wiki/Third_normal_form) suit toutes les règles de la 2ème forme normale, et une règle supplémentaire :

* Toutes les colonnes qui ne font pas partie de la clé primaire dépendent uniquement de la clé primaire.

Remarquez que cela n'est que légèrement différent de la deuxième forme normale. Dans la deuxième forme normale, nous ne pouvons pas avoir une colonne complètement dépendante d'une partie de la clé primaire, et dans la troisième forme normale, nous ne pouvons pas avoir une colonne qui est entièrement dépendante de quoi que ce soit qui n'est pas la clé primaire entière.

#### Exemple de 2ème NF, mais pas de 3ème NF

Dans cette table, la clé primaire est simplement la colonne `id`.

| id  | name    | first_initial | email                  |
| --- | ------- | ------------- | ---------------------- |
| 1   | Lane    | l             | lane.works@example.com |
| 2   | Breanna | b             | breanna@example.com    |
| 3   | Lane    | l             | lane.right@example.com |

Cette table est en 2ème forme normale car `first_initial` ne dépend pas d'une partie de la clé primaire. Cependant, parce qu'elle dépend de la colonne `name`, elle ne respecte pas la 3ème forme normale.

#### Exemple de 3ème forme normale

La manière de convertir la table ci-dessus en 3NF est d'ajouter une nouvelle table qui mappe un `name` directement à son `first_initial`. Remarquez à quel point cette solution est similaire à la 2NF.

| id  | name    | email                  |
| --- | ------- | ---------------------- |
| 1   | Lane    | lane.works@example.com |
| 2   | Breanna | breanna@example.com    |
| 3   | Lane    | lane.right@example.com |

| name    | first_initial |
| ------- | ------------- |
| Lane    | l             |
| Breanna | b             |

#### La 3NF est *généralement* une bonne idée

La même règle de base s'applique aux deuxième et troisième formes normales.

> Optimisez pour l'intégrité des données et la dé-duplication des données en premier en respectant la 3NF. Si vous avez des problèmes de vitesse, dé-normalisez en conséquence.

Rappelez-vous la [fonction IIF](https://www.sqlitetutorial.net/sqlite-functions/sqlite-iif/) et la clause `AS`.

### Forme Normale de Boyce-Codd (BCNF)

Une table en [forme normale de Boyce-Codd](https://en.wikipedia.org/wiki/Boyce%E2%80%93Codd_normal_form) (créée par [Raymond F Boyce](https://en.wikipedia.org/wiki/Raymond_F._Boyce) et [Edgar F Codd](https://en.wikipedia.org/wiki/Edgar_F._Codd)) suit toutes les règles de la 3ème forme normale, plus une règle supplémentaire :

* Une colonne qui fait partie d'une clé primaire ne peut pas être entièrement dépendante d'une colonne qui ne fait pas partie de cette clé primaire.

Cela n'entre en jeu que lorsqu'il existe plusieurs combinaisons possibles de clés primaires qui se chevauchent. Un autre nom pour cela est "clés candidates chevauchantes".

Seulement dans de rares cas, une table en troisième forme normale ne répond pas aux exigences de la forme normale de Boyce-Codd.

#### Exemple de 3ème NF, mais pas de Boyce-Codd NF

| release_year | release_date | sales | name            |
| ------------ | ------------ | ----- | --------------- |
| 2001         | 2001-01-02   | 100   | Kiss me tender  |
| 2001         | 2001-02-04   | 200   | Bloody Mary     |
| 2002         | 2002-04-14   | 100   | I wanna be them |
| 2002         | 2002-06-24   | 200   | He got me       |

La chose intéressante ici est qu'il y a 3 clés primaires possibles :

* `release_year` + `sales`
* `release_date` + `sales`
* `name`

Cela signifie que par définition, cette table est en 2ème et 3ème forme normale car ces formes ne restreignent que la dépendance d'une colonne qui ne fait pas partie d'une clé primaire.

Cette table n'est pas en forme normale de Boyce-Codd car `release_year` dépend entièrement de `release_date`.

#### Exemple de forme normale de Boyce-Codd

La manière la plus simple de corriger la table dans notre exemple est de simplement supprimer les données en double de `release_date`. Renommons cette colonne `release_day_and_month`.

| release_year | release_day_and_month | sales | name            |
| ------------ | --------------------- | ----- | --------------- |
| 2001         | 01-02                 | 100   | Kiss me tender  |
| 2001         | 02-04                 | 200   | Bloody Mary     |
| 2002         | 04-14                 | 100   | I wanna be them |
| 2002         | 06-24                 | 200   | He got me       |

#### BCNF est *généralement* une bonne idée

La même règle de base s'applique aux 2ème, 3ème et formes normales de Boyce-Codd. Cela dit, il est peu probable que vous rencontriez des problèmes spécifiques à BCNF en pratique.

> Optimisez pour l'intégrité des données et la dé-duplication des données en premier en respectant la forme normale de Boyce-Codd. Si vous avez des problèmes de vitesse, dé-normalisez en conséquence.

### Révision de la normalisation

À mon avis, les définitions exactes des 1ère, 2ème, 3ème et formes normales de Boyce-Codd ne sont pas si importantes dans votre travail en tant que développeur backend.

Cependant, ce qui est important, c'est de comprendre les principes de base de l'intégrité des données et de la redondance des données que les formes normales nous enseignent. 

Passons en revue quelques règles de base que vous devriez mémoriser - elles vous serviront bien lorsque vous concevrez des bases de données et même simplement lors des entretiens de codage.

#### Règles de base pour la conception de bases de données

1. Chaque table doit toujours avoir un identifiant unique (clé primaire)
2. 90% du temps, cet identifiant unique sera une seule colonne nommée `id`
3. Évitez les données en double
4. Évitez de stocker des données qui dépendent complètement d'autres données. Au lieu de cela, calculez-les à la volée lorsque vous en avez besoin.
5. Gardez votre schéma aussi simple que possible. Optimisez pour une base de données normalisée en premier. Ne dénormalisez pour la vitesse que lorsque vous commencez à rencontrer des problèmes de performance.

Nous parlerons plus de l'optimisation de la vitesse dans un chapitre ultérieur.

## Chapitre 10 : Comment joindre des tables en SQL


Les jointures sont l'une des fonctionnalités les plus importantes que SQL offre. Les jointures nous permettent de tirer parti des relations que nous avons établies entre nos tables. En bref, les jointures nous permettent d'interroger plusieurs tables en même temps.

### `INNER JOIN`

Le type de jointure le plus simple et le plus courant en SQL est le `INNER JOIN`. Par défaut, une commande `JOIN` est un `INNER JOIN`. 

Un `INNER JOIN` retourne tous les enregistrements de `table_a` qui ont des enregistrements correspondants dans `table_b`, comme le démontre le diagramme de Venn suivant.

![inner join](https://i.imgur.com/wgxAmhA.png)

#### La clause `ON`

Pour effectuer une jointure, nous devons indiquer à la base de données quels champs doivent être "appariés". La clause `ON` est utilisée pour spécifier ces colonnes à joindre.

```SQL
SELECT *
FROM employees
INNER JOIN departments 
ON employees.department_id = departments.id;
```

La requête ci-dessus retourne tous les champs des deux tables. Le mot-clé `INNER` n'a rien à voir avec le nombre de colonnes retournées - il n'affecte que le nombre de lignes retournées.

### Espace de noms sur les tables

Lorsque vous travaillez avec plusieurs tables, vous pouvez spécifier à quelle table appartient un champ en utilisant un `.`. Par exemple :

`table_name.column_name`

```SQL
SELECT students.name, classes.name
FROM students
INNER JOIN classes on classes.class_id = students.class_id;
```

La requête ci-dessus retourne le champ `name` de la table `students` et le champ `name` de la table `classes`. 

### `LEFT JOIN`

Un `LEFT JOIN` retournera chaque enregistrement de `table_a` indépendamment du fait que l'un de ces enregistrements ait une correspondance dans `table_b`. Une jointure gauche retournera également tous les enregistrements correspondants de `table_b`. 

Voici un diagramme de Venn pour aider à visualiser l'effet d'un `LEFT JOIN`.

![left-join](https://i.imgur.com/mNbhWfM.png)

Un petit truc que vous pouvez faire pour faciliter l'écriture de la requête SQL est de définir un [alias](https://en.wikipedia.org/wiki/Alias_(SQL)) pour chaque table. Voici un exemple :

```SQL
SELECT e.name, d.name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.id;
```

Remarquez les déclarations d'alias simples `e` et `d` pour `employees` et `departments` respectivement.

Certains développeurs font cela pour rendre leurs requêtes moins verbeuses. Cela dit, je déteste personnellement cela car les variables à une seule lettre sont plus difficiles à comprendre.

### `RIGHT JOIN`

Un `RIGHT JOIN` est, comme vous pouvez vous y attendre, l'inverse d'un `LEFT JOIN`. Il retourne tous les enregistrements de `table_b` indépendamment des correspondances, et tous les enregistrements correspondants entre les deux tables.

![right-join](https://i.imgur.com/LG6Y43j.png)

#### Restriction de SQLite

SQLite ne supporte pas les jointures à droite, mais de nombreux dialectes de SQL le font. Si vous y réfléchissez, un `RIGHT JOIN` est simplement un `LEFT JOIN` avec l'ordre des tables inversé, donc ce n'est pas un gros problème que SQLite ne supporte pas la syntaxe.

### `FULL JOIN`

Un `FULL JOIN` combine le jeu de résultats des commandes `LEFT JOIN` et `RIGHT JOIN`. Il retourne tous les enregistrements des deux tables `table_a` et `table_b` indépendamment du fait qu'ils aient des correspondances ou non.

![Full-join](https://i.imgur.com/Kk3k1Ub.png)

#### SQLite

Comme les `RIGHT JOIN`, SQLite ne supporte pas les `FULL JOIN` mais ils sont toujours importants à connaître.

## Chapitre 11 : Performance de la base de données

### Index SQL

Un index est une structure en mémoire qui garantit que les requêtes que nous exécutons sur une base de données sont performantes, c'est-à-dire qu'elles s'exécutent rapidement. 

Si vous avez appris les structures de données, la plupart des index de base de données sont simplement des [arbres binaires](https://en.wikipedia.org/wiki/Binary_tree). L'arbre binaire peut être stocké en [ram](https://en.wikipedia.org/wiki/Random-access_memory) ainsi que sur [disque](https://en.wikipedia.org/wiki/Computer_data_storage), et il facilite la recherche de l'emplacement d'une ligne entière.

Les colonnes `PRIMARY KEY` sont indexées par défaut, garantissant que vous pouvez rechercher une ligne par son `id` très rapidement. Mais si vous avez d'autres colonnes sur lesquelles vous souhaitez effectuer des recherches rapides, vous devrez les indexer.

#### `CREATE INDEX`

```sql
CREATE INDEX index_name on table_name (column_name);
```

Il est assez courant de nommer un index d'après la colonne sur laquelle il est créé avec un suffixe de `_idx`.

### Révision des index

Comme nous l'avons discuté, un index est une structure de données qui peut effectuer des recherches rapides. En indexant une colonne, nous créons une nouvelle structure en mémoire, généralement un arbre binaire, où les valeurs de la colonne indexée sont triées dans l'arbre pour garder les recherches rapides. 

En termes de complexité Big-O, un index d'arbre binaire garantit que les recherches sont [O(log(n))](https://en.wikipedia.org/wiki/Big_O_notation).

#### Ne devrions-nous pas indexer tout ? Nous pouvons rendre la base de données ultra-rapide !

Bien que les index rendent certains types de recherches beaucoup plus rapides, ils ajoutent également une surcharge de performance - ils peuvent ralentir une base de données de différentes manières. 

Réfléchissez-y : si vous indexez chaque colonne, vous pourriez avoir des centaines d'arbres binaires en mémoire. Cela gonfle inutilement l'utilisation de la mémoire de votre base de données. Cela signifie également que chaque fois que vous insérez un enregistrement, cet enregistrement doit être ajouté à de nombreux arbres - ralentissant votre vitesse d'insertion.

La règle de base est simple :

> Ajoutez un index aux colonnes sur lesquelles vous savez que vous effectuerez des recherches fréquentes. Laissez le reste non indexé. Vous pouvez toujours ajouter des index plus tard.

### Index multi-colonnes

Les index multi-colonnes sont utiles pour la raison exacte que vous pourriez penser - ils accélèrent les recherches qui dépendent de plusieurs colonnes. 

#### `CREATE INDEX`

```sql
CREATE INDEX first_name_last_name_age_idx
ON users (first_name, last_name, age);
```

Un index multi-colonnes est trié par la première colonne en premier, la deuxième colonne ensuite, et ainsi de suite. Une recherche sur seulement la première colonne dans un index multi-colonnes obtient presque toutes les améliorations de performance qu'elle obtiendrait de son propre index à colonne unique. Mais les recherches sur seulement la deuxième ou troisième colonne auront des performances très dégradées.

#### Règle de base

Sauf si vous avez des raisons spécifiques de faire quelque chose de spécial, ajoutez uniquement des index multi-colonnes si vous effectuez des recherches fréquentes sur une combinaison spécifique de colonnes.

### Dénormalisation pour la vitesse

Je vous ai laissé avec un suspense dans le chapitre "normalisation". Il s'avère que l'intégrité des données et la dé-duplication ont un coût, et ce coût est généralement la vitesse.

Joindre des tables ensemble, utiliser des sous-requêtes, effectuer des agrégations et exécuter des calculs post-hoc prennent du temps. À très grande échelle, ces techniques avancées peuvent en fait avoir un énorme impact sur les performances d'une application - parfois en bloquant le serveur de base de données.

Stocker des informations en double peut considérablement accélérer une application qui doit les rechercher de différentes manières. Par exemple, si vous stockez les informations de pays d'un utilisateur directement sur son enregistrement utilisateur, aucune jointure coûteuse n'est requise pour charger sa page de profil.

Cela dit, la dénormalisation se fait à vos propres risques. La dénormalisation d'une base de données entraîne un grand risque de données inexactes et boguées.

À mon avis, elle devrait être utilisée comme une sorte de "dernier recours" au nom de la vitesse.

### Injection SQL

SQL est une méthode très courante utilisée par les pirates pour causer des dommages ou violer une base de données. L'une de mes bandes dessinées [XKCD](https://xkcd.com/327/) préférées de tous les temps illustre le problème :

![bobby tables](https://bobby-tables.com/img/xkcd.png)

La blague ici est que si quelqu'un utilisait cette requête :

```SQL
INSERT INTO students(name) VALUES (?);
```

Et que le "nom" d'un étudiant était `'Robert'); DROP TABLE students;--` alors la requête SQL résultante ressemblerait à ceci :

```sql
INSERT INTO students(name) VALUES ('Robert'); DROP TABLE students;--)
```

Comme vous pouvez le voir, ceci est en fait 2 requêtes ! La première insère "Robert" dans la base de données, et la seconde supprime la table des étudiants !

#### Comment se protéger contre l'injection SQL ?

Vous devez être conscient des attaques par injection SQL, mais pour être honnête, la solution de nos jours est simplement d'utiliser une bibliothèque SQL moderne qui nettoie les entrées SQL. Nous n'avons plus souvent besoin de nettoyer les entrées manuellement au niveau de l'application.

Par exemple, les packages SQL de la bibliothèque standard de Go protègent automatiquement vos entrées contre les attaques SQL si vous [les utilisez correctement](https://go.dev/doc/database/sql-injection). En bref, ne faites pas d'interpolation d'entrée utilisateur dans des chaînes brutes vous-même - assurez-vous que votre bibliothèque de base de données a un moyen de nettoyer les entrées, et passez-lui ces valeurs brutes.

## Félicitations pour être arrivé à la fin !
Si vous êtes intéressé par les devoirs de codage interactifs et les quiz de ce cours, vous pouvez consulter le cours [Learn SQL Course](https://www.boot.dev/learn/learn-sql) sur [Boot.dev](https://www.boot.dev/)

Ce cours fait partie de mon parcours complet de carrière de développeur backend, composé d'autres cours et projets si vous êtes intéressé à les consulter.

Si vous voulez voir les autres contenus que je crée liés au développement web, consultez certains de mes liens ci-dessous :

[Podcast de Lane : Backend Banter](https://www.backendbanter.fm/)
[Lane sur Twitter](https://twitter.com/wagslane)
[Lane sur YouTube](https://www.youtube.com/@bootdotdev)