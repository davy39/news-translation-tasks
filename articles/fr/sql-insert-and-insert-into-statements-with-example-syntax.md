---
title: 'SQL Insert Into et Insert : Avec Exemple de Syntaxe MySQL'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-11T22:46:00.000Z'
originalURL: https://freecodecamp.org/news/sql-insert-and-insert-into-statements-with-example-syntax
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f67740569d1a4ca4277.jpg
tags:
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
seo_title: 'SQL Insert Into et Insert : Avec Exemple de Syntaxe MySQL'
seo_desc: 'This article will walk you through how to use both Insert and Insert Into
  statements in SQL.

  How to use Insert in SQL

  Insert queries are a way to insert data into a table. Let’s say we have created
  a table using

  CREATE TABLE example_table ( name varc...'
---

Cet article vous guidera sur l'utilisation des instructions Insert et Insert Into en SQL.

## Comment utiliser Insert en SQL

Les requêtes Insert sont un moyen d'insérer des données dans une table. Supposons que nous avons créé une table en utilisant

`CREATE TABLE example_table ( name varchar(255), age int)`

**example_table**

Nom Âge

Pour ajouter des données à cette table, nous utiliserons **INSERT** de la manière suivante :

`INSERT INTO example_table (column1,column2) VALUES ("Andrew",23)`

**example_table**

NomÂgeAndrew23

Même la syntaxe suivante fonctionnera, mais il est toujours bon de spécifier quelles données vont dans quelle colonne.

`INSERT INTO table_name VALUES ("John", 28)`

**example_table**

NomÂgeAndrew23John28

## Comment utiliser Insert Into en SQL

Pour insérer un enregistrement dans une table, vous utilisez l'instruction `INSERT INTO`.

Vous pouvez le faire de deux manières. Si vous souhaitez insérer des valeurs uniquement dans certaines colonnes, vous devez lister leurs noms, y compris toutes les colonnes obligatoires. La syntaxe est :

```
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

```

L'autre méthode consiste à insérer des valeurs dans toutes les colonnes de la table, il n'est pas nécessaire de spécifier les noms des colonnes. La syntaxe est :

```
INSERT INTO table_name 
VALUES (value1, value2, value3, ...);

```

Voici un exemple d'insertion d'un enregistrement dans la table Person de deux manières :

```
INSERT INTO Person
VALUES (1, 'John Lennon', '1940-10-09', 'M');

```

Et

```
INSERT INTO Person(Id, Name, DateOfBirth, Gender)
VALUES (1, 'John Lennon', '1940-10-09', 'M');

```

Certaines versions de SQL (par exemple, MySQL) supportent l'insertion de plusieurs lignes à la fois. Par exemple :

```
INSERT INTO Person(Id, Name, DateOfBirth, Gender)
VALUES (1, 'John Lennon', '1940-10-09', 'M'), (2, 'Paul McCartney', '1942-06-18', 'M'),
(3, 'George Harrison', '1943-02-25', 'M'), (4, 'Ringo Starr', '1940-07-07', 'M')

```

Notez que la requête originale entière reste intacte - nous ajoutons simplement des lignes de données enfermées dans des parenthèses et séparées par des virgules.

## Vous pouvez même utiliser Insert Into dans une instruction Select.

Vous pouvez insérer des enregistrements dans une table en utilisant des données déjà stockées dans la base de données. Cela n'est qu'une copie des données et n'affecte pas la table d'origine.

L'instruction `INSERT INTO SELECT` combine les instructions `INSERT INTO` et `SELECT`, et vous pouvez utiliser n'importe quelles conditions que vous souhaitez. La syntaxe est :

```
INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table1
WHERE condition;

```

Voici un exemple qui insère dans la table Person tous les étudiants masculins de la table Students.

```
INSERT INTO Person(Id, Name, DateOfBirth, Gender)
SELECT Id, Name, DateOfBirth, Gender
FROM Students
WHERE Gender = 'M'

```