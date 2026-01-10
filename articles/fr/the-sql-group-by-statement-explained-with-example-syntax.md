---
title: L'instruction SQL GROUP BY expliquée avec la syntaxe d'exemple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-06T22:29:00.000Z'
originalURL: https://freecodecamp.org/news/the-sql-group-by-statement-explained-with-example-syntax
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f87740569d1a4ca4312.jpg
tags:
- name: SQL
  slug: sql
seo_title: L'instruction SQL GROUP BY expliquée avec la syntaxe d'exemple
seo_desc: 'GROUP BY gives us a way to combine rows and aggregate data.

  The data used is from the campaign contributions data we’ve been using in some of
  these guides.

  The following SQL statement is answering the question: “which candidates received
  the largest ...'
---

GROUP BY nous donne un moyen de combiner des lignes et d'agréger des données.

Les données utilisées proviennent des données de contributions de campagne que nous avons utilisées dans certains de ces guides.

L'instruction SQL suivante répond à la question : "Quels candidats ont reçu les plus grandes contributions totales en 2016, mais uniquement ceux qui ont reçu plus de 20 millions de dollars USD ?"

Ordonner cet ensemble de données dans un ordre décroissant (DESC) place les candidats avec les plus grandes contributions totales en haut de la liste.

```
SELECT Candidate, Election_year, sum(Total_$), count(*)
FROM combined_party_data
WHERE Election_year = 2016
GROUP BY Candidate, Election_year -- cela indique au DBMS de résumer par ces deux colonnes
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