---
title: 'Instructions SQL Select : Exemples de Select Distinct, Select Into, Insert
  into, et plus'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-11T01:07:00.000Z'
originalURL: https://freecodecamp.org/news/sql-select-statements
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ca3740569d1a4ca3358.jpg
tags:
- name: SQL
  slug: sql
- name: toothbrush
  slug: toothbrush
seo_title: 'Instructions SQL Select : Exemples de Select Distinct, Select Into, Insert
  into, et plus'
seo_desc: 'Select and From clauses

  The SELECT part of a query is normally to determine which columns of the data to
  show in the results. There are also options you can apply to show data that is not
  a table column.

  This example shows three columns selected from...'
---

## Clauses Select et From

La partie SELECT d'une requête est normalement utilisée pour déterminer quelles colonnes des données afficher dans les résultats. Il existe également des options que vous pouvez appliquer pour afficher des données qui ne sont pas une colonne de table.

Cet exemple montre trois colonnes sélectionnées dans la table "student" et une colonne calculée. La base de données stocke le studentID, FirstName et LastName de l'étudiant. Nous pouvons combiner les colonnes First et Last name pour créer la colonne calculée FullName.

```sql
select studentID, FirstName, LastName, FirstName + ' ' + LastName as FullName
from student;
```

```text
+-----------+-------------------+------------+------------------------+
| studentID | FirstName         | LastName   | FullName               |
+-----------+-------------------+------------+------------------------+
|         1 | Monique           | Davis      | Monique Davis          |
|         2 | Teri              | Gutierrez  | Teri Gutierrez         |
|         3 | Spencer           | Pautier    | Spencer Pautier        |
|         4 | Louis             | Ramsey     | Louis Ramsey           |
|         5 | Alvin             | Greene     | Alvin Greene           |
|         6 | Sophie            | Freeman    | Sophie Freeman         |
|         7 | Edgar Frank "Ted" | Codd       | Edgar Frank "Ted" Codd |
|         8 | Donald D.         | Chamberlin | Donald D. Chamberlin   |
|         9 | Raymond F.        | Boyce      | Raymond F. Boyce       |
+-----------+-------------------+------------+------------------------+
9 rows in set (0.00 sec)
```

*Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à elles que ce qui est dans ce guide d'introduction.

J'espère que cela vous donne au moins assez pour commencer.

Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options vous-même.

## **Instruction SQL Select Distinct**

### **Introduction**

Ce mot-clé nous permet d'obtenir des listes de valeurs uniques dans une colonne. Ce guide va démontrer cela.

### **Affichage complet des données dans la table student**

```sql
USE fcc_sql_guides_database;
SELECT studentID, FullName, sat_score, programOfStudy, rcd_Created, rcd_Updated FROM student;
```

```text
+-----------+------------------------+-----------+------------------+---------------------+---------------------+
| studentID | FullName               | sat_score | programOfStudy   | rcd_Created         | rcd_Updated         |
+-----------+------------------------+-----------+------------------+---------------------+---------------------+
|         1 | Monique Davis          |       400 | Literature       | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         2 | Teri Gutierrez         |       800 | Programming      | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         3 | Spencer Pautier        |      1000 | Programming      | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         4 | Louis Ramsey           |      1200 | Programming      | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         5 | Alvin Greene           |      1200 | Programming      | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         6 | Sophie Freeman         |      1200 | Programming      | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         7 | Edgar Frank "Ted" Codd |      2400 | Computer Science | 2017-08-16 15:35:33 | 2017-08-16 15:35:33 |
|         8 | Donald D. Chamberlin   |      2400 | Computer Science | 2017-08-16 15:35:33 | 2017-08-16 15:35:33 |
|         9 | Raymond F. Boyce       |      2400 | Computer Science | 2017-08-16 15:35:33 | 2017-08-16 15:35:33 |
+-----------+------------------------+-----------+------------------+---------------------+---------------------+
9 rows in set (0.00 sec)
```

### **Obtenir la liste des domaines d'étude**

```sql
SELECT DISTINCT programOfStudy FROM student;
```

```text
+------------------+
| programOfStudy   |
+------------------+
| Literature       |
| Programming      |
| Computer Science |
+------------------+
3 rows in set (0.00 sec)
```

Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à elles que ce qui est dans ce guide d'introduction.

J'espère que cela vous donne au moins assez pour commencer.

Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options vous-même.

## **Instruction SQL Select into**

L'instruction `SELECT INTO` est une requête qui vous permet de créer une _nouvelle_ table et de la remplir avec le jeu de résultats d'une `instruction SELECT`. Pour ajouter des données à une table existante, voir plutôt l'instruction [INSERT INTO](https://guide.freecodecamp.org/sql/sql-select-into-statement/guides/src/pages/sql/sql-insert-into-select-statement/index.md).

`SELECT INTO` peut être utilisé lorsque vous combinez des données de plusieurs tables ou vues dans une nouvelle table.<sup>1</sup> La table d'origine n'est pas affectée.

La syntaxe générale est :

```sql
SELECT column-names
  INTO new-table-name
  FROM table-name
 WHERE EXISTS 
      (SELECT column-name
         FROM table-name
        WHERE condition)
```

Cet exemple montre un ensemble d'une table qui a été "copié" de la table "Supplier" vers une nouvelle table appelée SupplierUSA qui contient l'ensemble lié à la colonne country de valeur 'USA'.

```sql
SELECT * INTO SupplierUSA
  FROM Supplier
 WHERE Country = 'USA';
```

**Résultats** : 4 lignes affectées <sup>2</sup>

IDCompanyNameContactNameCityCountryPhone2New Orleans Cajun DelightsShelley BurkeNew OrleansUSA(100) 555-48223Grandma Kelly's HomesteadRegina MurphyAnn ArborUSA(313) 555-573516Bigfoot BreweriesCheryl SaylorBendUSANULL19New England Seafood CanneryRobb MerchantBostonUSA(617) 555-3267

Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options vous-même.

## **Instruction SQL Insert into**

Pour insérer un enregistrement dans une table, vous utilisez l'instruction `INSERT INTO`.

Vous pouvez le faire de deux manières. Si vous souhaitez insérer des valeurs uniquement dans certaines colonnes, vous devez lister leurs noms, y compris toutes les colonnes obligatoires. La syntaxe est :

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

L'autre manière consiste à insérer des valeurs dans toutes les colonnes de la table, il n'est pas nécessaire de spécifier les noms des colonnes. La syntaxe est :

```sql
INSERT INTO table_name 
VALUES (value1, value2, value3, ...);
```

Voici un exemple d'insertion d'un enregistrement dans la table Person de deux manières :

```sql
INSERT INTO Person
VALUES (1, 'John Lennon', '1940-10-09', 'M');
```

Et

```sql
INSERT INTO Person(Id, Name, DateOfBirth, Gender)
VALUES (1, 'John Lennon', '1940-10-09', 'M');
```

Certaines versions de SQL (par exemple, MySQL) supportent l'insertion de plusieurs lignes à la fois. Par exemple :

```sql
INSERT INTO Person(Id, Name, DateOfBirth, Gender)
VALUES (1, 'John Lennon', '1940-10-09', 'M'), (2, 'Paul McCartney', '1942-06-18', 'M'),
(3, 'George Harrison', '1943-02-25', 'M'), (4, 'Ringo Starr', '1940-07-07', 'M')
```

Notez que la requête originale entière reste intacte - nous ajoutons simplement des lignes de données encodées par des parenthèses et séparées par des virgules.

## **Instruction SQL Insert into Select**

Vous pouvez insérer des enregistrements dans une table en utilisant des données déjà stockées dans la base de données. Ce n'est qu'une copie des données et cela n'affecte pas la table d'origine.

L'instruction `INSERT INTO SELECT` combine les instructions `INSERT INTO` et `SELECT`, et vous pouvez utiliser n'importe quelles conditions que vous souhaitez. La syntaxe est :

```sql
INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table1
WHERE condition;
```

Voici un exemple qui insère dans la table Person tous les étudiants masculins de la table Students.

```sql
INSERT INTO Person(Id, Name, DateOfBirth, Gender)
SELECT Id, Name, DateOfBirth, Gender
FROM Students
WHERE Gender = 'M'
```

## Autres ressources SQL :

* [Cours vidéo complet sur SQL et les bases de données](https://www.freecodecamp.org/news/sql-and-databases-full-course/)
* [Commandes SQL de base que vous devriez connaître](https://www.freecodecamp.org/news/basic-sql-commands/)