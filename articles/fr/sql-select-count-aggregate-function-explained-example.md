---
title: La fonction d'agrégation SQL Select Count - Expliquée avec des exemples de
  syntaxe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-03T22:20:00.000Z'
originalURL: https://freecodecamp.org/news/sql-select-count-aggregate-function-explained-example
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9fa6740569d1a4ca43c7.jpg
tags:
- name: SQL
  slug: sql
seo_title: La fonction d'agrégation SQL Select Count - Expliquée avec des exemples
  de syntaxe
seo_desc: 'The COUNT operator is usually used in combination with a GROUP BY clause.
  It is one of the SQL “aggregate” functions, which include AVG (average) and SUM.

  This function will count the number of rows and return that count as a column in
  the result set...'
---

L'opérateur COUNT est généralement utilisé en combinaison avec une clause GROUP BY. Il fait partie des fonctions d'agrégation SQL, qui incluent AVG (moyenne) et SUM.

Cette fonction comptera le nombre de lignes et retournera ce compte comme une colonne dans l'ensemble de résultats.

Voici des exemples de ce pour quoi vous utiliseriez COUNT :

* Compter toutes les lignes d'une table (aucun group by requis)
* Compter les totaux de sous-ensembles de données (nécessite une section Group By de l'instruction)

Pour référence, voici les données actuelles pour toutes les lignes de notre base de données d'exemple d'étudiants.

```
select studentID, FullName, programOfStudy, sat_score from student; -- tous les enregistrements avec les champs d'intérêt

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/count01.JPG?raw=true)

Cette instruction SQL fournit un compte de toutes les lignes. Notez que vous pouvez donner un nom à la colonne COUNT résultante en utilisant « AS ».

```
select count(*) AS studentCount from student; -- compte de tous les enregistrements

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/count02.JPG?raw=true)

Ici, nous obtenons un compte des étudiants dans chaque domaine d'étude.

```
select studentID, FullName, count(*) AS studentCount from student group by programOfStudy;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/count03.JPG?raw=true)

Ici, nous obtenons un compte des étudiants avec les mêmes scores SAT.

```
select studentID, FullName, count(*) AS studentCount from student group by sat_score;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/count04.JPG?raw=true)

Voici un exemple utilisant la table des fonds de campagne. Il s'agit d'un total des dollars dans chaque transaction et du nombre de contributions pour chaque parti politique lors de la campagne présidentielle américaine de 2016.

```
select Specific_Party, Election_Year, format(sum(Total_$),2) AS contribution$Total, count(*) AS numberOfContributions 
from combined_party_data
group by Specific_Party,Election_Year
having Election_Year = 2016;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/count05.JPG?raw=true)

Comme pour toutes ces choses, il y a beaucoup plus à découvrir, alors veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différents tests vous-même.