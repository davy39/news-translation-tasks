---
title: SQL Distinct Expliqué avec des Exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-17T23:00:00.000Z'
originalURL: https://freecodecamp.org/news/sql-distinct-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f40740569d1a4ca4198.jpg
tags:
- name: SQL
  slug: sql
seo_title: SQL Distinct Expliqué avec des Exemples
seo_desc: 'What does the SQL Select Distinct command do? What does Distinct Mean?

  This keyword allows us to get lists of unique values in a column. This guide will
  demonstrate that.

  Full display of the data in the student table

  USE fcc_sql_guides_database;

  SELE...'
---

## Que fait la commande SQL Select Distinct ? Que signifie Distinct ?

Ce mot-clé nous permet d'obtenir des listes de valeurs uniques dans une colonne. Ce guide va le démontrer.

### Affichage complet des données dans la table student

```
USE fcc_sql_guides_database;
SELECT studentID, FullName, sat_score, programOfStudy, rcd_Created, rcd_Updated FROM student;

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

### Obtenir la liste des domaines d'étude

```
SELECT DISTINCT programOfStudy FROM student;

```

```
+------------------+
| programOfStudy   |
+------------------+
| Literature       |
| Programming      |
| Computer Science |
+------------------+
3 rows in set (0.00 sec)

```

Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à découvrir que ce qui est présenté dans ce guide d'introduction.

J'espère que cela vous donne au moins assez pour commencer.

Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options par vous-même.