---
title: L'opérateur SQL AND expliqué avec des exemples de syntaxe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-18T17:52:00.000Z'
originalURL: https://freecodecamp.org/news/the-sql-and-operator-explained-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/and-operator.jpeg
tags:
- name: SQL
  slug: sql
seo_title: L'opérateur SQL AND expliqué avec des exemples de syntaxe
seo_desc: 'AND is used in a WHERE clause or a GROUP BY HAVING clause to limit the
  rows returned from the executed statement. Use AND when it’s required to have more
  than one condition met.

  We’ll use the student table to present examples.

  Here’s the student tabl...'
---

AND est utilisé dans une clause WHERE ou une clause GROUP BY HAVING pour limiter les lignes retournées par la requête exécutée. Utilisez AND lorsqu'il est nécessaire de satisfaire plus d'une condition.

Nous utiliserons la table student pour présenter des exemples.

Voici la table student sans clause WHERE :

```
select * from student;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/and_operator01.JPG?raw=true)

Maintenant, la clause WHERE est ajoutée pour afficher uniquement les étudiants en programmation :

```
select * from student 
where programOfStudy = 'Programming';

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/and_operator02.JPG?raw=true)

Maintenant, la clause WHERE est mise à jour avec AND pour afficher les résultats des étudiants en programmation qui ont également un score SAT supérieur à 800 :

```
select * from student 
where programOfStudy = 'Programming' 
and sat_score > 800;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/and_operator03.JPG?raw=true)

Voici un exemple plus complexe à partir de la table des contributions de campagne. Cet exemple contient une clause GROUP BY avec une clause HAVING utilisant un AND pour restreindre les enregistrements retournés aux candidats de 2016 avec des contributions totales comprises entre 3 millions et 18 millions de dollars.

```
select Candidate, Office_Sought, Election_Year, FORMAT(sum(Total_$),2) from combined_party_data
where Office_Sought = 'PRESIDENT / VICE PRESIDENT'
group by Candidate, Office_Sought, Election_Year
 having Election_Year = 2016 and sum(Total_$) between 3000000 and 18000000
order by sum(Total_$) desc;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/and_operator06.JPG?raw=true)