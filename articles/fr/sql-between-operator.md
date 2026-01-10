---
title: L'opérateur SQL BETWEEN - Expliqué avec des exemples de syntaxe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-01T21:16:00.000Z'
originalURL: https://freecodecamp.org/news/sql-between-operator
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9fb0740569d1a4ca4402.jpg
tags:
- name: SQL
  slug: sql
seo_title: L'opérateur SQL BETWEEN - Expliqué avec des exemples de syntaxe
seo_desc: 'The BETWEEN Operator is useful because of the SQL Query Optimizer. Although
  BETWEEN is functionally the same as: x <= element <= y, the SQL Query Optimizer
  will recognize this command faster, and has optimized code for running it.

  This operator is us...'
---

L'opérateur BETWEEN est utile grâce à l'optimiseur de requêtes SQL. Bien que BETWEEN soit fonctionnellement identique à : x <= élément <= y, l'optimiseur de requêtes SQL reconnaîtra cette commande plus rapidement et dispose d'un code optimisé pour l'exécuter.

Cet opérateur est utilisé dans une clause WHERE ou dans une clause GROUP BY HAVING.

Les lignes sont sélectionnées si elles ont une valeur supérieure à la valeur minimale et inférieure à la valeur maximale.

Il est important de garder à l'esprit que les valeurs entrées dans la commande sont **exclues** du résultat. Nous obtenons uniquement ce qui se trouve entre elles.

Voici la syntaxe pour utiliser la fonction dans une clause WHERE :

```
select field1, testField
from table1
where testField between min and max

```

Voici un exemple utilisant la table student et la clause WHERE :

```
-- pas de clause WHERE
select studentID, FullName, studentID
from student;
    
-- clause WHERE avec between
select studentID, FullName, studentID
from student
where studentID between 2 and 7;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/between01.JPG?raw=true)

Voici un exemple utilisant la table des fonds de campagne et la clause HAVING. Cela retournera les lignes où la somme des dons pour un candidat est comprise entre 3 millions et 18 millions de dollars, basée sur la clause HAVING dans la partie GROUP BY de l'instruction. Plus d'informations sur l'agrégation dans ce guide.

```
select Candidate, Office_Sought, Election_Year, format(sum(Total_$),2)
from combined_party_data
where Election_Year = 2016
group by Candidate, Office_Sought, Election_Year
having sum(Total_$) between 3000000 and 18000000
order by sum(Total_$) desc; 

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/between02.JPG?raw=true)