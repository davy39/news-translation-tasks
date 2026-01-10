---
title: Comment créer une table en SQL – Exemple de requête Postgres et MySQL
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-10-25T22:53:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-table-in-sql-postgres-and-mysql-example-query
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/xavier-foucrier-UYHhyLwM1Wk-unsplash.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: postgres
  slug: postgres
- name: SQL
  slug: sql
seo_title: Comment créer une table en SQL – Exemple de requête Postgres et MySQL
seo_desc: "Knowing how to create tables in SQL is an important and fundamental concept.\
  \ \nIn this tutorial, I will walk you through the SQL syntax for the CREATE TABLE\
  \ statement using code examples for both PostgreSQL and MySQL.  \nBasic CREATE TABLE\
  \ Syntax\nHere ..."
---

Savoir comment créer des tables en `SQL` est un concept important et fondamental.

Dans ce tutoriel, je vais vous guider à travers la syntaxe `SQL` pour l'instruction `CREATE TABLE` en utilisant des exemples de code pour PostgreSQL et MySQL.

## Syntaxe de base de `CREATE TABLE`

Voici la syntaxe de base pour l'instruction `CREATE TABLE` :

```sql
CREATE TABLE nom_table(
	colonne1 type_donnee contrainte_colonne,
    colonne2 type_donnee contrainte_colonne,
    colonne3 type_donnee contrainte_colonne,
    colonne4 type_donnee contrainte_colonne,
    ... etc
);
```

Pour la première partie, vous devez commencer par l'instruction `CREATE TABLE` suivie du nom de la table que vous souhaitez créer.

Si je voulais créer une table d'informations sur les enseignants, j'écrirais quelque chose comme ceci :

```sql
CREATE TABLE enseignants();
```

À l'intérieur des parenthèses, vous ajouterez les informations pour créer les colonnes de la table. Si vous oubliez les parenthèses, vous obtiendrez un message d'erreur.

```sql
CREATE TABLE enseignants;
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-19-at-5.54.40-PM.png)

Le point-virgule à la fin des parenthèses indique à l'ordinateur qu'il s'agit de la fin de l'instruction `SQL`. Vous entendrez parfois cela appelé terminateur d'instruction.

### Qu'est-ce que les moteurs de stockage `MySQL` ?

Selon la [documentation](https://dev.mysql.com/doc/refman/8.0/en/storage-engines.html) de `MySQL` :

> Les moteurs de stockage sont des composants MySQL qui gèrent les opérations SQL pour différents types de tables.

`MySQL` utilise ces moteurs de stockage pour effectuer des opérations CRUD (create, read, update et delete) sur la base de données.

Dans `MySQL`, vous avez la possibilité de spécifier le type de moteur de stockage que vous souhaitez utiliser pour votre table. Si vous omettez la clause `ENGINE`, le moteur par défaut sera InnoDB.

```sql
CREATE TABLE nom_table(
	colonne1 type_donnee contrainte_colonne,
    colonne2 type_donnee contrainte_colonne,
    colonne3 type_donnee contrainte_colonne,
    colonne4 type_donnee contrainte_colonne,
    ... etc
)ENGINE=moteur_stockage;
```

### Qu'est-ce que la clause `IF NOT EXISTS` ?

Il existe une clause optionnelle appelée `IF NOT EXISTS` qui vérifie si la table que vous souhaitez créer existe déjà dans la base de données. Vous pouvez placer cette clause juste avant le nom de la table.

```sql
CREATE TABLE IF NOT EXISTS enseignants();
```

Si la table existe déjà, alors l'ordinateur ne créera pas de nouvelle table.

Si vous omettez la clause `IF NOT EXISTS` et essayez de créer une table qui existe déjà dans la base de données, vous obtiendrez un message d'erreur.

Dans cet exemple, j'ai d'abord créé une table appelée enseignants. Mais si j'essaie de créer cette même table dans la commande suivante, je rencontrerai une erreur.

```sql
CREATE TABLE IF NOT EXISTS enseignants();
CREATE TABLE enseignants();
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-19-at-5.27.02-PM.png)

## Comment créer des colonnes dans la table

À l'intérieur des parenthèses pour l'instruction `CREATE TABLE`, vous allez lister les noms des colonnes que vous souhaitez créer ainsi que leurs types de données et contraintes.

Voici un exemple de la façon dont nous pouvons ajouter quatre colonnes de `school_id`, `name`, `email` et `age` à notre table enseignants. Chaque nom de colonne doit être séparé par des virgules.

```sql
CREATE TABLE enseignants(
	school_id type_donnee contrainte_colonne, 
	name type_donnee contrainte_colonne,
    email type_donnee contrainte_colonne, 
	age type_donnee contrainte_colonne
);

```

Selon la [documentation](https://dev.mysql.com/doc/refman/8.0/en/create-table.html#create-table-types-attributes) de `MySQL` :

> MySQL a une limite stricte de 4096 colonnes par table, mais le maximum effectif peut être inférieur pour une table donnée. La limite exacte de colonnes dépend de plusieurs facteurs.

Si vous travaillez sur des projets personnels plus petits en `MySQL`, vous n'aurez probablement pas à vous soucier de dépasser le nombre de colonnes pour vos tables.

Selon la [documentation PostgreSQL](https://www.postgresql.org/docs/current/limits.html), il y a une limite de 1600 colonnes par table. Similaire à `MySQL`, une limite exacte peut varier en fonction de l'espace disque ou des restrictions de performance.

### Types de données en `SQL`

Lorsque vous créez des colonnes dans la table, vous devez leur assigner un type de données. Les types de données décrivent le type de valeur à l'intérieur des colonnes.

Voici six catégories populaires de types de données en `SQL` :

1. Numérique (int, float, serial, decimal, etc)
2. Date et heure (timestamp, data, time, etc)
3. Caractère et chaîne (char, varchar, text, etc)
4. Unicode (ntext, nvarchar, etc.)
5. Binaire (binary, etc.)
6. Divers (xml, table, etc.)

Cet article ne passera pas en revue chaque type de données, mais couvrira certains des plus populaires.

Voici la liste complète des [types de données `PostgreSQL`](https://www.postgresql.org/docs/8.1/datatype.html) et des [types de données `MySQL`](https://dev.mysql.com/doc/refman/8.0/en/data-types.html).

### Qu'est-ce que `SERIAL` et `AUTO_INCREMENT` ?

Dans `PostgreSQL`, un type de données `SERIAL` est un entier qui s'incrémentera automatiquement de un pour chaque nouvelle ligne créée.

Nous pouvons ajouter `SERIAL` juste après la colonne `school_id` dans notre table enseignants.

```sql
school_id SERIAL

```

Dans `MySQL`, vous utiliseriez `AUTO_INCREMENT` au lieu de `SERIAL`. Dans cet exemple, le type de données `INT` est utilisé, ce qui représente un entier.

```sql
school_id INT AUTO_INCREMENT
```

Si nous ajoutions cinq lignes à notre table enseignants, le résultat montrerait les nombres 1, 2, 3, 4, 5 pour la colonne `school_id` car l'entier s'incrémente automatiquement de un pour chaque nouvelle ligne.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-23-at-6.09.13-PM.png)

### Qu'est-ce que le type de données `VARCHAR` ?

Un type de données `VARCHAR` est une chaîne de longueur variable où vous pouvez définir une longueur maximale de caractères.

Voici un exemple d'utilisation du type de données `VARCHAR` pour les colonnes `name` et `email` dans notre table enseignants. Le nombre 30 est la longueur maximale de caractères.

```sql
name VARCHAR(30) contrainte_colonne,
email VARCHAR(30) contrainte_colonne,
```

### Contraintes de colonne en SQL

Ce sont des règles qui sont appliquées aux données à l'intérieur des colonnes de la table.

Voici une liste de certaines des contraintes de colonne les plus courantes :

* PRIMARY KEY - cette clé sert d'identifiant unique pour la table
* FOREIGN KEY - cette clé garantit que les valeurs d'une colonne sont également présentes dans une autre table. Cela sert de lien entre les tables.
* UNIQUE - toutes les valeurs de la colonne doivent être uniques
* NOT NULL - les valeurs ne peuvent pas être NULL. NULL est l'absence de valeur
* CHECK - teste une valeur contre une expression booléenne

### Exemples de clés `PRIMARY` et `FOREIGN`

Dans notre table enseignants, nous pouvons ajouter une `PRIMARY KEY` à la colonne `school_id`.

Voici à quoi ressemblerait le code dans PostgreSQL :

```sql
 school_id SERIAL PRIMARY KEY
```

Voici à quoi ressemblerait le code dans MySQL :

```sql
school_id INT AUTO_INCREMENT PRIMARY KEY
```

Si vous souhaitez avoir plus d'une colonne pour la `PRIMARY KEY`, vous l'ajouteriez juste après vos créations de colonnes.

```sql
CREATE TABLE nom_table(
	colonne1 type_donnee contrainte_colonne,
    colonne2 type_donnee contrainte_colonne,
    colonne3 type_donnee contrainte_colonne,
    colonne4 type_donnee contrainte_colonne,
    ... etc
    PRIMARY KEY (colonne1, colonne2)
);
```

Si vous souhaitez lier une table à une autre, vous pouvez utiliser une `FOREIGN KEY`.

Supposons que nous ayons une table appelée district_employees avec une clé primaire de `district_id`. Voici à quoi ressemblerait le code dans PostgreSQL :

```sql
CREATE TABLE district_employees(
   district_id SERIAL PRIMARY KEY,
   employee_name VARCHAR(30) NOT NULL,
   PRIMARY KEY(district_id)
);
```

Dans notre table enseignants, nous pouvons utiliser une clé étrangère et référencer la table district_employees.

```sql
district_id INT REFERENCES district_employees(district_id),

```

```sql
CREATE TABLE enseignants(
    school_id SERIAL PRIMARY KEY,
    district_id INT REFERENCES district_employees(district_id),
    colonne1 type_donnee contrainte_colonne,
    colonne2 type_donnee contrainte_colonne,
    colonne3 type_donnee contrainte_colonne,
    colonne4 type_donnee contrainte_colonne,
    ... etc 
);
```

### Exemples de `NOT NULL`, `CHECK` et `UNIQUE`

Si nous voulons nous assurer que nous n'avons aucune valeur nulle, nous pouvons utiliser la contrainte `NOT NULL`.

```sql
name VARCHAR(30) NOT NULL
```

Nous pouvons utiliser la contrainte `CHECK` pour nous assurer que tous nos enseignants ont 18 ans et plus. La contrainte `CHECK` teste une valeur contre une expression booléenne.

```sql
age INT CHECK(age >= 18)
```

Si l'une de nos valeurs ne répond pas à cette condition, nous obtiendrons un message d'erreur.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-19-at-10.47.07-PM.png)

Nous pouvons utiliser la contrainte `UNIQUE` pour nous assurer que tous les emails sont uniques.

```sql
email VARCHAR(30) UNIQUE

```

Voici le résultat final pour la table enseignants :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-23-at-8.09.36-PM.png)

Voici à quoi ressemblerait le code dans PostgreSQL :

```sql
CREATE TABLE enseignants(
	school_id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
    email VARCHAR(30) UNIQUE,
	age INT CHECK(age >= 18)      
);
```

Voici à quoi ressemblerait le code dans MySQL :

```sql
CREATE TABLE enseignants(
	school_id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
    email VARCHAR(30) UNIQUE,
	age INT CHECK(age >= 18)      
);
```

J'espère que vous avez apprécié cet article et bonne chance dans votre parcours SQL.