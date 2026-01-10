---
title: 'L''instruction SQL Order By : Exemple de syntaxe'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-12T22:50:00.000Z'
originalURL: https://freecodecamp.org/news/sql-order-by-statement-example-syntax
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f5e740569d1a4ca423f.jpg
tags:
- name: SQL
  slug: sql
seo_title: 'L''instruction SQL Order By : Exemple de syntaxe'
seo_desc: 'Order By is a SQL command that lets you sort the resulting output from
  a SQL query.

  Order By (ASC, DESC)

  ORDER BY gives us a way to SORT the result set by one or more of the items in the
  SELECT section. Here is an SQL sorting the students by FullName...'
---

Order By est une commande SQL qui permet de trier le résultat d'une requête SQL.

### Order By (ASC, DESC)

ORDER BY nous offre un moyen de TRIER le jeu de résultats par un ou plusieurs des éléments de la section SELECT. Voici un exemple SQL triant les étudiants par FullName dans l'ordre décroissant. L'ordre de tri par défaut est ascendant (ASC), mais pour trier dans l'ordre inverse (décroissant), on utilise DESC.

Voici la requête

```
SELECT studentID, FullName, sat_score
FROM student
ORDER BY FullName DESC;

```

Et voici les données résultantes, présentées dans un joli tableau décroissant.

```
+-----------+------------------------+-----------+
| studentID | FullName               | sat_score |
+-----------+------------------------+-----------+
|         2 | Teri Gutierrez         |       800 |
|         3 | Spencer Pautier        |      1000 |
|         6 | Sophie Freeman         |      1200 |
|         9 | Raymond F. Boyce       |      2400 |
|         1 | Monique Davis          |       400 |
|         4 | Louis Ramsey           |      1200 |
|         7 | Edgar Frank "Ted" Codd |      2400 |
|         8 | Donald D. Chamberlin   |      2400 |
|         5 | Alvin Greene           |      1200 |
+-----------+------------------------+-----------+
9 rows in set (0.00 sec)

```

Voici la liste complète des étudiants NON-TRIÉE, actuelle, pour comparaison avec ce qui précède.

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

Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à découvrir que ce qui est présenté dans ce guide d'introduction.

J'espère que cela vous donne au moins assez pour commencer.

Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options par vous-même.