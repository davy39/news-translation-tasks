---
title: Fonctions de date SQL et GETDATE expliquées avec des exemples de syntaxe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-21T21:41:00.000Z'
originalURL: https://freecodecamp.org/news/sql-date-functions-getdate
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e92740569d1a4ca3dd3.jpg
tags:
- name: SQL
  slug: sql
seo_title: Fonctions de date SQL et GETDATE expliquées avec des exemples de syntaxe
seo_desc: 'There are 61 Date Functions defined in MySQL. Don’t worry, we won’t review
  them all here. This guide will give you an introduction to some of the common ones,
  and enough exposure for you to comfortably to explore on your own.

  We will cover:


  Getting ...'
---

Il existe 61 fonctions de date définies dans MySQL. Ne vous inquiétez pas, nous ne les passerons pas toutes en revue ici. Ce guide vous donnera une introduction à certaines des plus courantes, et suffisamment d'exposition pour que vous puissiez explorer confortablement par vous-même.

Nous allons couvrir :

* Obtenir la date actuelle
* Calculs de date
* Dates dans une clause where ou having

### Obtenir la date actuelle

Obtenir la date du système peut être très utile pour traiter des données avec SQL.

```
-- date actuelle
select now(), sysdate(), current_date(), current_time(), -- date et heure du système à l'exécution
dayofyear(now()) as NumDaysSoFarThisYr,
EXTRACT(YEAR FROM now()) as theYearPart,
EXTRACT(YEAR_MONTH FROM now()) as theYrMonPart, 
date_format(now(), '%W %M %Y') as oneOfManyFormats; 
;

```

Dans la requête SQL, nous voyons ce qui suit :

* Les deux premières colonnes du résultat sont deux façons d'obtenir les mêmes informations : la date du système au moment où le SQL est exécuté.
* Les deux colonnes suivantes extraient uniquement les parties Date et Heure de la date du système.
* La suivante présente le « numéro du jour » de la date du système cette année. Vous remarquerez que cela correspond à un jour de plus que le calcul montré dans l'exemple suivant.
* Les deux suivantes extraient uniquement l'année, puis à la fois l'année et le mois.
* Enfin, mais non des moindres, il y a un exemple unique de l'une des nombreuses façons de formater ces dates.

Vous pouvez également utiliser GETDATE() pour obtenir la date actuelle.

### Calculs de date

```
select now(), current_date(), 
datediff(now(),'2017-01-01') as daysThisYear, 
subdate(current_date(), interval 150 day) as '150DaysAgo', 
adddate(now(), interval 7 day) as dateInA_Week -- date dans une semaine
;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/date-functions02.jpg)

Ici, nous voyons :

* Les deux premières colonnes sont simplement la date et l'heure du système pour référence.
* La deuxième colonne est la différence de date (datediff) entre le 1er janvier 2017 et la date du système.
* Les deux dernières colonnes sont des exemples de soustraction et d'addition de dates.

### Dans une clause where ou having

Voici deux exemples d'utilisation des calculs de date dans une clause where :

```
select * from student; - pour montrer les données actuelles utilisées pour l'exemple
select * from student where recordCreated < '2017-01-01';
select * from student where recordCreated < subdate(current_date(), interval 225 day);

```

En ce qui concerne la partie HAVING : Gardez à l'esprit que la plupart de la logique de la clause WHERE fonctionnera également dans la clause HAVING d'un GROUP BY. La différence entre les deux est que la clause WHERE s'exécute sur l'ensemble des données, tandis que la clause HAVING s'exécute sur les données agrégées par la clause GROUP BY.

Comme pour toutes ces choses, il y a BEAUCOUP PLUS à découvrir que ce qui est présenté dans ce guide d'introduction. J'espère que cela vous donne au moins suffisamment pour commencer. Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options par vous-même.