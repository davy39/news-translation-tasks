---
title: Les instructions SQL Sum expliquées avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-20T23:06:00.000Z'
originalURL: https://freecodecamp.org/news/sql-sum-statements-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f28740569d1a4ca4114.jpg
tags:
- name: SQL
  slug: sql
seo_title: Les instructions SQL Sum expliquées avec des exemples
seo_desc: 'What is the Sum statement in SQL?

  This is one of the aggregate functions (as is count, average, max, min, etc.). They
  are used in a GROUP BY clause as it aggregates data presented by the SELECT FROM
  WHERE portion of the statement.

  Example of use

  “sum...'
---

## Qu'est-ce que l'instruction Sum en SQL ?

Il s'agit de l'une des fonctions d'agrégation (comme count, average, max, min, etc.). Elles sont utilisées dans une clause GROUP BY car elles agrègent les données présentées par la partie SELECT FROM WHERE de l'instruction.

### Exemple d'utilisation

"sum(Total_$)" dans l'instruction SELECT est agrégé dans la clause GROUP BY. "Count(*)" fournit le nombre de contributions.

Ces données proviennent des données de contributions de campagne que nous avons utilisées dans certains de ces guides.

Cette instruction SQL répond à la question : "quels candidats ont reçu le plus grand total de dollars de contributions en 2016 MAIS uniquement ceux qui avaient plus de 20 millions de dollars USD pour toutes les contributions combinées ?"

Ordonner cet ensemble de données dans un ordre décroissant (DESC) place les candidats avec les plus grandes contributions totales en haut de la liste.

```
SELECT Candidate, Election_year, sum(Total_$), count(*)
FROM combined_party_data
WHERE Election_year = 2016
GROUP BY Candidate, Election_year -- cela indique au SGBD de résumer par ces deux colonnes
HAVING sum(Total_$) > 20000000  -- limite les lignes présentées à partir du résumé de l'argent (20 millions de dollars USD)
ORDER BY sum(Total_$) DESC; -- ordonne les lignes présentées avec les plus grandes en premier.

```

```
+--------------------------------------------------+---------------+-------------------+----------+
| Candidate                                        | Election_year | sum(Total_$)      | count(*) |
+--------------------------------------------------+---------------+-------------------+----------+
| CLINTON, HILLARY RODHAM & KAINE, TIMOTHY M (TIM) |          2016 | 568135094.4400003 |      126 |
| TRUMP, DONALD J & PENCE, MICHAEL R (MIKE)        |          2016 | 366853142.7899999 |      114 |
| SANDERS, BERNARD (BERNIE)                        |          2016 |      258562022.17 |      122 |
| CRUZ, RAFAEL EDWARD (TED)                        |          2016 | 93430700.29000005 |      104 |
| CARSON, BENJAMIN S (BEN)                         |          2016 | 62202411.12999996 |       93 |
| RUBIO, MARCO ANTONIO                             |          2016 |        44384313.9 |      106 |
| BUSH, JOHN ELLIS (JEB)                           |          2016 |       34606731.78 |       97 |
+--------------------------------------------------+---------------+-------------------+----------+
7 rows in set (0.01 sec)

```

Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à savoir que ce qui est présenté dans ce guide d'introduction.

J'espère que cela vous donne au moins assez pour commencer.

Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options vous-même.