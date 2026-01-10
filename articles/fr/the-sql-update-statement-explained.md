---
title: 'L''instruction SQL Update expliquée : Requêtes pour mettre à jour des tables
  (y compris des exemples MySQL)'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-21T23:10:00.000Z'
originalURL: https://freecodecamp.org/news/the-sql-update-statement-explained
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/sql-update.jpeg
tags:
- name: SQL
  slug: sql
seo_title: 'L''instruction SQL Update expliquée : Requêtes pour mettre à jour des
  tables (y compris des exemples MySQL)'
seo_desc: 'What an Update query can do

  An update query gives the DBA or SQL-using programmer the ability to update many
  records with one command.

  Important Safety Tip: always have a backup copy of what you are about to change
  BEFORE you change it.

  This guide wi...'
---

## Ce qu'une requête Update peut faire

Une requête Update donne à l'administrateur de base de données ou au programmeur utilisant SQL la capacité de mettre à jour de nombreux enregistrements avec une seule commande.

Conseil de sécurité important : toujours avoir une copie de sauvegarde de ce que vous allez modifier AVANT de le modifier.

Ce guide va :

* ajouter un nouveau champ à la table student
* tester la logique pour mettre à jour ce champ avec une adresse email attribuée par l'école
* mettre à jour le nouveau champ.

Voici la table student au début de ce processus

```
SELECT * FROM student;

```

```
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

### Modifier la table et ajouter un nouveau champ

```
    ALTER TABLE `fcc_sql_guides_database`.`student` 
	ADD COLUMN `schoolEmailAdr` VARCHAR(125) NULL AFTER `programOfStudy`;

```

La table student après l'exécution de l'alter.

```
mysql> SELECT FullName, sat_score, programOfStudy, schoolEmailAdr FROM student;
+------------------------+-----------+------------------+----------------+
| FullName               | sat_score | programOfStudy   | schoolEmailAdr |
+------------------------+-----------+------------------+----------------+
| Monique Davis          |       400 | Literature       | NULL           |
| Teri Gutierrez         |       800 | Programming      | NULL           |
| Spencer Pautier        |      1000 | Programming      | NULL           |
| Louis Ramsey           |      1200 | Programming      | NULL           |
| Alvin Greene           |      1200 | Programming      | NULL           |
| Sophie Freeman         |      1200 | Programming      | NULL           |
| Edgar Frank "Ted" Codd |      2400 | Computer Science | NULL           |
| Donald D. Chamberlin   |      2400 | Computer Science | NULL           |
| Raymond F. Boyce       |      2400 | Computer Science | NULL           |
+------------------------+-----------+------------------+----------------+
9 rows in set (0.00 sec)

```

### TESTER la logique (Étape TRÈS importante !)

```
SELECT FullName, instr(FullName," ") AS firstSpacePosition, 
concat(substring(FullName,1,instr(FullName," ")-1),"@someSchool.edu") AS schoolEmail
FROM student;

```

```
+------------------------+--------------------+------------------------+
| FullName               | firstSpacePosition | schoolEmail            |
+------------------------+--------------------+------------------------+
| Monique Davis          |                  8 | Monique@someSchool.edu |
| Teri Gutierrez         |                  5 | Teri@someSchool.edu    |
| Spencer Pautier        |                  8 | Spencer@someSchool.edu |
| Louis Ramsey           |                  6 | Louis@someSchool.edu   |
| Alvin Greene           |                  6 | Alvin@someSchool.edu   |
| Sophie Freeman         |                  7 | Sophie@someSchool.edu  |
| Edgar Frank "Ted" Codd |                  6 | Edgar@someSchool.edu   |
| Donald D. Chamberlin   |                  7 | Donald@someSchool.edu  |
| Raymond F. Boyce       |                  8 | Raymond@someSchool.edu |
+------------------------+--------------------+------------------------+
9 rows in set (0.00 sec)

```

_Une note sur concat() : dans MySQL, cette commande est utilisée pour combiner des chaînes, ce qui n'est pas le cas dans d'autres versions de SQL (consultez votre manuel). Dans cette utilisation, cela fonctionne comme suit : La sous-chaîne du champ FullName jusqu'à mais non incluant le premier espace est combinée avec "@someSchool.edu". Dans le monde réel, cela devrait être beaucoup plus complexe et vous devriez vous assurer que l'adresse email est unique._

### Effectuer la mise à jour

Nous allons prétendre que c'est ce que nous voulons et mettre à jour la table avec ces informations :

```
UPDATE student SET schoolEmailAdr = concat(substring(FullName,1,instr(FullName," ")-1),"@someSchool.edu")
WHERE schoolEmailAdr is NULL;

```

Succès !

```
mysql> SELECT FullName, sat_score, programOfStudy, schoolEmailAdr FROM student;
+------------------------+-----------+------------------+------------------------+
| FullName               | sat_score | programOfStudy   | schoolEmailAdr         |
+------------------------+-----------+------------------+------------------------+
| Monique Davis          |       400 | Literature       | Monique@someSchool.edu |
| Teri Gutierrez         |       800 | Programming      | Teri@someSchool.edu    |
| Spencer Pautier        |      1000 | Programming      | Spencer@someSchool.edu |
| Louis Ramsey           |      1200 | Programming      | Louis@someSchool.edu   |
| Alvin Greene           |      1200 | Programming      | Alvin@someSchool.edu   |
| Sophie Freeman         |      1200 | Programming      | Sophie@someSchool.edu  |
| Edgar Frank "Ted" Codd |      2400 | Computer Science | Edgar@someSchool.edu   |
| Donald D. Chamberlin   |      2400 | Computer Science | Donald@someSchool.edu  |
| Raymond F. Boyce       |      2400 | Computer Science | Raymond@someSchool.edu |
+------------------------+-----------+------------------+------------------------+
9 rows in set (0.00 sec)

```

Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à elles que ce qui est dans ce guide d'introduction.

J'espère que cela vous donne au moins assez pour commencer.

Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options vous-même.

## Comment utiliser une instruction Update ?

Pour mettre à jour un enregistrement dans une table, vous utilisez l'instruction `UPDATE`.

Faites attention. Vous pouvez mettre à jour tous les enregistrements de la table ou seulement quelques-uns. Utilisez la condition `WHERE` pour spécifier quels enregistrements vous souhaitez mettre à jour. Il est possible de mettre à jour une ou plusieurs colonnes à la fois. La syntaxe est :

```
UPDATE table_name
SET column1 = value1, 
    column2 = value2, ...
WHERE condition;

```

Voici un exemple de mise à jour du Nom de l'enregistrement avec l'Id 4 :

```
UPDATE Person
SET Name = "Elton John"
WHERE Id = 4;

```

Vous pouvez également mettre à jour des colonnes dans une table en utilisant des valeurs provenant d'autres tables. Utilisez la clause `JOIN` pour obtenir des données à partir de plusieurs tables. La syntaxe est :

```
UPDATE table_name1
SET table_name1.column1 = table_name2.columnA
    table_name1.column2 = table_name2.columnB
FROM table_name1
JOIN table_name2 ON table_name1.ForeignKey = table_name2.Key

```

Voici un exemple de mise à jour du Manager de tous les enregistrements :

```
UPDATE Person
SET Person.Manager = Department.Manager
FROM Person
JOIN Department ON Person.DepartmentID = Department.ID

```