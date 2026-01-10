---
title: 'La commande SQL Inner Join : Exemple de syntaxe'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-14T22:58:00.000Z'
originalURL: https://freecodecamp.org/news/the-sql-inner-join-command-example-syntax
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f4c740569d1a4ca41e1.jpg
tags:
- name: SQL
  slug: sql
seo_title: 'La commande SQL Inner Join : Exemple de syntaxe'
seo_desc: 'For this guide we’ll discuss the SQL (INNER) Joins

  Join Commands Explained (the same as Inner Join)

  The student table will be in the FROM clause so it will be a starting or LEFT table.

  We’ll JOIN this to the student contact table or RIGHT table. You’...'
---

Pour ce guide, nous allons discuter des jointures SQL (INNER).

### Commandes de jointure expliquées (identiques à Inner Join)

La table des étudiants sera dans la clause FROM, ce qui en fera une table de départ ou de GAUCHE.

Nous allons JOINdre cela à la table des contacts des étudiants ou table de DROITE. Vous verrez que tous les étudiants apparaissent qui sont ÉGALEMENT dans la table des contacts. Comme le montrent les tables ci-dessous, l'étudiantID 9 est dans la table des étudiants mais PAS dans la table des contacts, donc il n'apparaîtra pas dans une jointure.

Instruction SQL

```
SELECT a.studentID, a.FullName, a.programOfStudy,
b.`student-phone-cell`, b.`student-US-zipcode`
FROM student AS a
INNER JOIN `student-contact-info` AS b ON a.studentID = b.studentID;

```

Données "jointes"

```
+-----------+------------------------+------------------+--------------------+--------------------+
| studentID | FullName               | programOfStudy   | student-phone-cell | student-US-zipcode |
+-----------+------------------------+------------------+--------------------+--------------------+
|         1 | Monique Davis          | Literature       | 555-555-5551       |              97111 |
|         2 | Teri Gutierrez         | Programming      | 555-555-5552       |              97112 |
|         3 | Spencer Pautier        | Programming      | 555-555-5553       |              97113 |
|         4 | Louis Ramsey           | Programming      | 555-555-5554       |              97114 |
|         5 | Alvin Greene           | Programming      | 555-555-5555       |              97115 |
|         6 | Sophie Freeman         | Programming      | 555-555-5556       |              97116 |
|         7 | Edgar Frank "Ted" Codd | Computer Science | 555-555-5557       |              97117 |
|         8 | Donald D. Chamberlin   | Computer Science | 555-555-5558       |              97118 |
+-----------+------------------------+------------------+--------------------+--------------------+

```

### Listes complètes des tables pour référence

Table des étudiants SQL

```
SELECT a.studentID, a.FullName, sat_score, a.programOfStudy, schoolEmailAdr 
FROM student AS a;

```

table des étudiants ou table de GAUCHE

```
+-----------+------------------------+-----------+------------------+------------------------+
| studentID | FullName               | sat_score | programOfStudy   | schoolEmailAdr         |
+-----------+------------------------+-----------+------------------+------------------------+
|         1 | Monique Davis          |       400 | Literature       | Monique@someSchool.edu |
|         2 | Teri Gutierrez         |       800 | Programming      | Teri@someSchool.edu    |
|         3 | Spencer Pautier        |      1000 | Programming      | Spencer@someSchool.edu |
|         4 | Louis Ramsey           |      1200 | Programming      | Louis@someSchool.edu   |
|         5 | Alvin Greene           |      1200 | Programming      | Alvin@someSchool.edu   |
|         6 | Sophie Freeman         |      1200 | Programming      | Sophie@someSchool.edu  |
|         7 | Edgar Frank "Ted" Codd |      2400 | Computer Science | Edgar@someSchool.edu   |
|         8 | Donald D. Chamberlin   |      2400 | Computer Science | Donald@someSchool.edu  |
|         9 | Raymond F. Boyce       |      2400 | Computer Science | Raymond@someSchool.edu |
+-----------+------------------------+-----------+------------------+------------------------+
9 rows in set (0.00 sec)


```sql
SELECT * FROM `student-contact-info` AS b;

```

table des contacts des étudiants ou table de DROITE

```
+-----------+----------------------------------+--------------------+--------------------+
| studentID | studentEmailAddr                 | student-phone-cell | student-US-zipcode |
+-----------+----------------------------------+--------------------+--------------------+
|         1 | Monique.Davis@freeCodeCamp.org   | 555-555-5551       |              97111 |
|         2 | Teri.Gutierrez@freeCodeCamp.org  | 555-555-5552       |              97112 |
|         3 | Spencer.Pautier@freeCodeCamp.org | 555-555-5553       |              97113 |
|         4 | Louis.Ramsey@freeCodeCamp.org    | 555-555-5554       |              97114 |
|         5 | Alvin.Green@freeCodeCamp.org     | 555-555-5555       |              97115 |
|         6 | Sophie.Freeman@freeCodeCamp.org  | 555-555-5556       |              97116 |
|         7 | Maximo.Smith@freeCodeCamp.org    | 555-555-5557       |              97117 |
|         8 | Michael.Roach@freeCodeCamp.ort   | 555-555-5558       |              97118 |
+-----------+----------------------------------+--------------------+--------------------+
8 rows in set (0.00 sec)

```

### Conclusion

Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à elles que ce qui est dans ce guide d'introduction.

J'espère que cela vous donne au moins assez pour commencer.

Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options vous-même.