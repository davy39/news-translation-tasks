---
title: L'opérateur SQL LIKE expliqué avec la syntaxe d'exemple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-10T22:44:00.000Z'
originalURL: https://freecodecamp.org/news/sql-like-statements-explained-with-example-syntax
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f72740569d1a4ca42a2.jpg
tags:
- name: SQL
  slug: sql
seo_title: L'opérateur SQL LIKE expliqué avec la syntaxe d'exemple
seo_desc: 'You may have encountered the LIKE operator before. In this article we''ll
  explain how you can use it.

  LIKE Operator defined

  The  LIKE  operator is used in a  WHERE  or  HAVING  (as part of the  GROUP BY )
  to limit the selected rows to the items when a...'
---

Vous avez peut-être déjà rencontré l'opérateur LIKE. Dans cet article, nous allons expliquer comment vous pouvez l'utiliser.

### Opérateur LIKE défini

L'opérateur `LIKE` est utilisé dans une clause `WHERE` ou `HAVING` (dans le cadre d'un `GROUP BY`) pour limiter les lignes sélectionnées aux éléments où une colonne contient un certain motif de caractères.

### Ce guide démontrera :

* Déterminer si une chaîne commence ou se termine par un motif de chaîne donné
* Déterminer si un motif existe au milieu de la chaîne
* Déterminer si une chaîne n'est pas contenue dans la chaîne

### Une colonne commence ou se termine par un motif de chaîne donné

Ce SQL sélectionnera les étudiants dont le `FullName` commence par « Monique » ou se termine par « Greene ».

```
SELECT studentID, FullName, sat_score, rcd_updated
FROM student 
WHERE 
FullName LIKE 'Monique%' OR -- notez le % à la fin mais pas au début
FullName LIKE '%Greene'; -- notez le % au début mais pas à la fin

```

```
+-----------+---------------+-----------+---------------------+
| studentID | FullName      | sat_score | rcd_updated         |
+-----------+---------------+-----------+---------------------+
|         1 | Monique Davis |       400 | 2017-08-16 15:34:50 |
|         5 | Alvin Greene  |      1200 | 2017-08-16 15:34:50 |
+-----------+---------------+-----------+---------------------+
2 rows in set (0.00 sec)

```

### Un motif de chaîne est au milieu de la colonne

Ce SQL sélectionnera les étudiants dont le nom contient « ree » n'importe où.

```
SELECT studentID, FullName, sat_score, rcd_updated
FROM student 
WHERE FullName LIKE '%ree%'; -- notez le % au début ET à la fin

```

```
+-----------+----------------+-----------+---------------------+
| studentID | FullName       | sat_score | rcd_updated         |
+-----------+----------------+-----------+---------------------+
|         5 | Alvin Greene   |      1200 | 2017-08-16 15:34:50 |
|         6 | Sophie Freeman |      1200 | 2017-08-16 15:34:50 |
+-----------+----------------+-----------+---------------------+
2 rows in set (0.00 sec)

```

### Une chaîne n'est PAS dans la colonne

Vous pouvez placer « NOT » avant LIKE pour exclure les lignes avec le motif de chaîne au lieu de les sélectionner. Ce SQL exclut les enregistrements qui contiennent « cer Pau » et « Ted » dans la colonne FullName.

```
SELECT studentID, FullName, sat_score, rcd_updated
FROM student 
WHERE FullName NOT LIKE '%cer Pau%' AND FullName NOT LIKE '%"Ted"%';

```

```
+-----------+----------------------+-----------+---------------------+
| studentID | FullName             | sat_score | rcd_updated         |
+-----------+----------------------+-----------+---------------------+
|         1 | Monique Davis        |       400 | 2017-08-16 15:34:50 |
|         2 | Teri Gutierrez       |       800 | 2017-08-16 15:34:50 |
|         4 | Louis Ramsey         |      1200 | 2017-08-16 15:34:50 |
|         5 | Alvin Greene         |      1200 | 2017-08-16 15:34:50 |
|         6 | Sophie Freeman       |      1200 | 2017-08-16 15:34:50 |
|         8 | Donald D. Chamberlin |      2400 | 2017-08-16 15:35:33 |
|         9 | Raymond F. Boyce     |      2400 | 2017-08-16 15:35:33 |
+-----------+----------------------+-----------+---------------------+
7 rows in set (0.00 sec)

```

_Voici la liste complète actuelle des étudiants pour comparer avec les résultats des clauses WHERE ci-dessus._

```
SELECT studentID, FullName, sat_score, rcd_updated FROM student;

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