---
title: La clause SQL HAVING expliquée avec la syntaxe d'exemple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-07T22:31:00.000Z'
originalURL: https://freecodecamp.org/news/the-sql-having-clause-explained-with-example-syntax
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f83740569d1a4ca4302.jpg
tags:
- name: SQL
  slug: sql
seo_title: La clause SQL HAVING expliquée avec la syntaxe d'exemple
seo_desc: 'HAVING gives the DBA or SQL-using programmer a way to filter the data aggregated
  by the GROUP BY clause so that the user gets a limited set of records to view.

  Example of use

  The HAVING clause is like the WHERE clause, except it acts on the grouped d...'
---

HAVING offre à l'administrateur de base de données ou au programmeur utilisant SQL un moyen de filtrer les données agrégées par la clause GROUP BY afin que l'utilisateur obtienne un ensemble limité d'enregistrements à afficher.

### Exemple d'utilisation

La clause HAVING est similaire à la clause WHERE, sauf qu'elle agit sur les données groupées. Dans ce cas, l'utilisateur ne verra que les montants les plus élevés.

Ces données proviennent des données de contributions de campagne que nous avons utilisées dans certains de ces guides.

Cette instruction SQL répond à la question : « quels candidats ont reçu les contributions totales les plus élevées en 2016 MAIS uniquement ceux qui ont reçu plus de 20 millions de dollars USD ? »

Le fait de classer cet ensemble de données dans un ordre décroissant (DESC) place les candidats avec les contributions totales les plus élevées en haut de la liste.

```
SELECT Candidate, Election_year, sum(Total_$), count(*)
FROM combined_party_data
WHERE Election_year = 2016
GROUP BY Candidate, Election_year -- cela indique au SGBD de résumer par ces deux colonnes
HAVING sum(Total_$) > 20000000  -- limite les lignes présentées à partir du résumé de l'argent (20 millions de dollars USD)
ORDER BY sum(Total_$) DESC; -- classe les lignes présentées avec les plus grandes en premier.

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