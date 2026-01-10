---
title: Comment écrire du SQL modulaire et lisible en utilisant des ensembles de résultats
  nommés et des fonctions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-07T17:47:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-modular-readable-sql-using-named-result-sets-and-functions-ac49f1ca25c1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*L6REAogd_Yiz1q5vcHuKSA.jpeg
tags:
- name: best practices
  slug: best-practices
- name: data analytics
  slug: data-analytics
- name: Data Science
  slug: data-science
- name: SQL
  slug: sql
- name: 'tech '
  slug: tech
seo_title: Comment écrire du SQL modulaire et lisible en utilisant des ensembles de
  résultats nommés et des fonctions
seo_desc: 'By Lak Lakshmanan

  My professional journey in computers has involved C++, then Java, and now Python.
  SQL remains, at best, a foreign language. For my own sanity, therefore, I’ve brought
  some of my programming best practices to SQL. In particular, the ...'
---

Par Lak Lakshmanan

Mon parcours professionnel dans le domaine de l'informatique a impliqué C++, puis Java, et maintenant Python. SQL reste, au mieux, une langue étrangère. Pour ma propre santé mentale, j'ai donc apporté certaines de mes meilleures pratiques de programmation à SQL. En particulier, l'instruction WITH a été mon amie.

![Image](https://cdn-media-1.freecodecamp.org/images/NNhuWHnTuY2hkZmbrzZY1qw1PoqpsDazq--W)
*Si vous écrivez du SQL modulaire et lisible, vous aurez le temps pour de longues balades à vélo le week-end*

Je vais utiliser un [ensemble de données public de vélos en libre-service à Londres](https://bigquery.cloud.google.com/table/bigquery-public-data:london_bicycles.cycle_hire) dans Google BigQuery pour démontrer. Supposons que nous voulons savoir si les vélos sont loués pour des durées plus longues le week-end.

#### 1. Constantes, pas de nombres codés en dur

Une bonne première étape consiste à définir des constantes que nous utiliserons tout au long de ma requête (voir [requête complète](https://bigquery.cloud.google.com/savedquery/663413318684:9b1a705e68b046cd9b44259f6198a215)) :

```
#standardsqlWITH constants AS (  SELECT  600 AS SHORT_DUR,         1800 AS LONG_DUR,         ['Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat'] AS daysofweek),
```

Ici, je définis les trajets de moins de 10 minutes comme "courts" et les trajets de plus de 30 minutes comme "longs". Remarquez comment, en définissant ces constantes à l'avance, je peux facilement essayer différents nombres. L'utilisation de constantes nommées rendra également la requête beaucoup plus lisible.

#### 2. Ensembles de résultats nommés

Une autre chose que vous voulez faire pour augmenter la lisibilité est de décomposer la requête en ensembles de résultats nommés. Au lieu d'écrire des requêtes et des sous-requêtes et de compter les parenthèses, j'ai tendance à utiliser beaucoup les instructions WITH. Comme les fonctions dans des langages comme C++ ou Python, les ensembles de résultats nommés permettent à la fois la réutilisation et la séparation logique.

Je définis d'abord une requête pour extraire les champs que je veux, et je nomme cet ensemble de résultats bikeshare ([requête complète](https://bigquery.cloud.google.com/savedquery/663413318684:9b1a705e68b046cd9b44259f6198a215)) :

```
bikeshare AS (  SELECT    IF(duration < SHORT_DUR, 1, 0) AS short_ride,    IF(duration > LONG_DUR,  1, 0) AS long_ride,    daysofweek[ORDINAL(EXTRACT(DAYOFWEEK FROM start_date))] AS dayofweek  FROM `bigquery-public-data.london_bicycles.cycle_hire`, constants)
```

Remarquez que la clause FROM doit inclure les "constants" afin d'utiliser les constantes définies.

#### 3. Fonctions SQL

Vous pouvez décomposer des requêtes complexes en utilisant le mot-clé WITH et créer des ensembles de résultats nommés. Mais qu'en est-il de l'analyse complexe ? Dans l'extrait ci-dessus, la ligne qui extrait le jour de la semaine et indexe le tableau **daysofweek** n'est pas lisible, n'est-ce pas ? Et il est assez probable que ce soit quelque chose que vous voudriez utiliser ailleurs.

Utilisez une fonction SQL afin de pouvoir réutiliser cette expression :

```
CREATE TEMPORARY FUNCTION dayOfWeek(ts TIMESTAMP,                                     days ARRAY<STRING>) AS(  days[ORDINAL(EXTRACT(DAYOFWEEK FROM ts))]);
```

Je définis une fonction **dayOfWeek** qui, étant donné un timestamp et un tableau de noms de jours, renverra le jour de la semaine auquel correspond le temps dans le timestamp. Une fois cette fonction définie, l'ensemble de résultats nommé dans la section précédente devient plus propre ([requête complète](https://bigquery.cloud.google.com/savedquery/663413318684:9b1a705e68b046cd9b44259f6198a215)) :

```
bikeshare AS (  SELECT    IF(duration < SHORT_DUR, 1, 0) AS short_ride,    IF(duration > LONG_DUR,  1, 0) AS long_ride,    dayOfWeek(start_date, daysofweek) AS dayofweek  FROM `bigquery-public-data.london_bicycles.cycle_hire`, constants)
```

#### Simplicité même

Une fois que nous avons des constantes nommées et des ensembles de résultats nommés, la requête finale est d'une simplicité même :

```
SELECT   dayofweek,  SUM(short_ride)/COUNT(short_ride) AS frac_short_rides,  SUM(long_ride)/COUNT(long_ride)  AS frac_long_rides,  COUNT(short_ride) AS num_all_ridesFROM  bikeshareGROUP BY  dayofweekORDER BY frac_long_rides DESC
```

Voici la [requête complète](https://bigquery.cloud.google.com/savedquery/663413318684:9b1a705e68b046cd9b44259f6198a215), et le résultat qui en découle :

![Image](https://cdn-media-1.freecodecamp.org/images/3IL2XIQaZ4oQV485yTgWj6QSgupIYfXsNXzT)

Les jours de semaine sont pour les trajets rapides et courts, et les week-ends sont pour les longues balades lentes. Cela a parfaitement du sens !