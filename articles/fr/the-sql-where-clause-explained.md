---
title: 'La clause SQL Where expliquée : In, Between, Like et autres exemples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-22T23:16:00.000Z'
originalURL: https://freecodecamp.org/news/the-sql-where-clause-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f1d740569d1a4ca40e1.jpg
tags:
- name: SQL
  slug: sql
seo_title: 'La clause SQL Where expliquée : In, Between, Like et autres exemples'
seo_desc: 'What is a SQL Where Clause?

  The WHERE  Clause (and/or,  IN ,  BETWEEN , and  LIKE )

  The  WHERE  clause is used to limit the number of rows returned.

  In this case all five of these will be used is a some what ridiculous  WHERE  clause.

  Here is the cur...'
---

## Qu'est-ce qu'une clause SQL Where ?

### La clause `WHERE` (et/ou, `IN`, `BETWEEN`, et `LIKE`)

La clause `WHERE` est utilisée pour limiter le nombre de lignes retournées.

Dans ce cas, les cinq conditions suivantes seront utilisées dans une clause `WHERE` quelque peu ridicule.

Voici la liste complète actuelle des étudiants à comparer avec le jeu de résultats de la clause `WHERE` :

```
select studentID, FullName, sat_score, rcd_updated from student;

```

```
+-----------+------------------------+-----------+---------------------+
| studentID | FullName               | sat_score | rcd_updated         |
+-----------+------------------------+-----------+---------------------+
|         1 | Monique Davis          |       400 | 2017-08-16 15:34:50 |
|         2 | Teri Gutierrez         |       800 | 2017-08-16 15:34:50 |
|         3 | Spencer Pautier        |      1000 | 2017-08-16 15:34:50 |
|         4 | Louis Ramsey           |      1200 | 2017-08-16 15:34:50 |
|         5 | Alvin Greene           |      1200 | 2017-08-16 15:34:50 |
|         6 | Sophie Freeman         |      1200 | 2017-08-16 15:34:50 |
|         7 | Edgar Frank "Ted" Codd |      2400 | 2017-08-16 15:35:33 |
|         8 | Donald D. Chamberlin   |      2400 | 2017-08-16 15:35:33 |
|         9 | Raymond F. Boyce       |      2400 | 2017-08-16 15:35:33 |
+-----------+------------------------+-----------+---------------------+
9 rows in set (0.00 sec)

```

Les lignes présentées seront celles où :

* `WHERE` les identifiants des étudiants sont entre 1 et 5 (inclus)
* `OR` studentID = 8

Voici une requête mise à jour, où tout enregistrement ayant un score SAT dans cette liste (1000, 1400) ne sera pas présenté :

```
select  studentID, FullName, sat_score, recordUpdated
from    student
where   (studentID between 1 and 5 or studentID = 8)
        and
        sat_score NOT in (1000, 1400);

```

```
+-----------+----------------------+-----------+---------------------+
| studentID | FullName             | sat_score | rcd_updated         |
+-----------+----------------------+-----------+---------------------+
|         1 | Monique Davis        |       400 | 2017-08-16 15:34:50 |
|         2 | Teri Gutierrez       |       800 | 2017-08-16 15:34:50 |
|         4 | Louis Ramsey         |      1200 | 2017-08-16 15:34:50 |
|         5 | Alvin Greene         |      1200 | 2017-08-16 15:34:50 |
|         8 | Donald D. Chamberlin |      2400 | 2017-08-16 15:35:33 |
+-----------+----------------------+-----------+---------------------+
5 rows in set (0.00 sec)

```

*Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à découvrir que ce qui est présenté dans ce guide d'introduction.

J'espère que cela vous donne au moins assez pour commencer.

Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options par vous-même.