---
title: SQL HAVING – Comment regrouper et compter avec une instruction Having
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-08-30T15:59:48.000Z'
originalURL: https://freecodecamp.org/news/sql-having-how-to-group-and-count-with-a-having-statement
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/sqlHaving.png
tags:
- name: data
  slug: data
- name: data analysis
  slug: data-analysis
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: SQL HAVING – Comment regrouper et compter avec une instruction Having
seo_desc: 'In SQL, you use the HAVING keyword right after GROUP BY to query the database
  based on a specified condition. Like other keywords, it returns the data that meet
  the condition and filters out the rest.

  The HAVING keyword was introduced because the WHE...'
---

En SQL, vous utilisez le mot-clé `HAVING` juste après `GROUP BY` pour interroger la base de données en fonction d'une condition spécifiée. Comme les autres mots-clés, il retourne les données qui répondent à la condition et filtre le reste.

Le mot-clé `HAVING` a été introduit car la clause `WHERE` échoue lorsqu'elle est utilisée avec des fonctions d'agrégation. Vous devez donc utiliser la clause `HAVING` avec des fonctions d'agrégation au lieu de `WHERE`.

Avec la clause `HAVING`, vous pouvez organiser les données de votre base de données en plusieurs groupes lorsque vous l'utilisez avec le mot-clé `GROUP BY`. Vous pouvez donc l'utiliser dans une grande base de données.

## Comment utiliser le mot-clé `HAVING`
Supposons que j'ai une table nommée `students` dans une base de données `student_scores`.
`SELECT * FROM students` retourne ce qui suit :
![ss1-6](https://www.freecodecamp.org/news/content/images/2022/08/ss1-6.png)

Vous pouvez obtenir uniquement les noms et les scores en exécutant `SELECT name, score 
FROM students`.
![ss2-6](https://www.freecodecamp.org/news/content/images/2022/08/ss2-6.png)

Vous pouvez ensuite utiliser le mot-clé `HAVING` pour filtrer certains étudiants en fonction d'une condition. Par exemple, ceux qui ont un score supérieur à 70.

Mais avant cela, vous devez utiliser la clause `GROUP BY` comme ceci :
```sql
GROUP BY name, score
```
Cela ne retournera rien pour l'instant. Vous devez donc introduire le mot-clé `HAVING` :
```sql
HAVING score > 70
```
Maintenant, je peux obtenir les étudiants qui ont obtenu un score supérieur à 70 :
![ss3-6](https://www.freecodecamp.org/news/content/images/2022/08/ss3-6.png) 

La requête complète ressemble à ceci :
```sql
SELECT name, score 
FROM students 
GROUP BY name, score
HAVING score > 70
```
Je peux également obtenir les étudiants qui ont obtenu plus de 90 de cette manière :
```sql
SELECT name, score 
FROM students 
GROUP BY name, score 
HAVING score > 90
```

La table contient également une colonne d'âge, donc je peux obtenir les étudiants qui ont plus de 14 ans de cette manière :
```sql
SELECT name, age 
FROM students 
GROUP BY name, age 
HAVING age > 14
```
![ss4-7](https://www.freecodecamp.org/news/content/images/2022/08/ss4-7.png) 

### Une erreur se produit si vous utilisez `WHERE` avec une fonction d'agrégation
```sql
SELECT name, count(*)
FROM students
GROUP BY name
WHERE COUNT(*) > 0
```
![ss5-7](https://www.freecodecamp.org/news/content/images/2022/08/ss5-7.png) 

L'erreur disparaît si vous utilisez `HAVING` :
```sql
SELECT name, count(*)
FROM students
GROUP BY name
HAVING COUNT(*) > 0
```
![ss6-6](https://www.freecodecamp.org/news/content/images/2022/08/ss6-6.png) 

### Vous pouvez utiliser n'importe quel opérateur que vous voulez !
L'opérateur n'est pas exclusif aux comparaisons. Je peux donc obtenir les étudiants qui ont 13 ans en changeant l'instruction HAVING en `HAVING age = 13` :
![ss7-5](https://www.freecodecamp.org/news/content/images/2022/08/ss7-5.png) 

J'ai obtenu les étudiants qui ont obtenu 90 de cette manière : 
```sql
SELECT name, score 
FROM students 
GROUP BY name, score 
HAVING score = 90
```
![ss8-5](https://www.freecodecamp.org/news/content/images/2022/08/ss8-5.png) 

### Si la condition dans l'instruction HAVING n'est pas remplie, aucune ligne ne sera retournée :
```sql
SELECT name, score 
FROM students 
GROUP BY name, score 
HAVING score = 100
```
![ss9-4](https://www.freecodecamp.org/news/content/images/2022/08/ss9-4.png) 

### Une erreur se produit si vous utilisez `HAVING` sans `GROUP BY`
```sql
SELECT COUNT(*)
FROM students 
HAVING score > 80
```
![ss10-4](https://www.freecodecamp.org/news/content/images/2022/08/ss10-4.png) 

Dans ce cas, vous devez utiliser la clause `WHERE` :
```sql
SELECT COUNT(*)
FROM students 
WHERE score > 80
```
![ss11-4](https://www.freecodecamp.org/news/content/images/2022/08/ss11-4.png) 

## Conclusion

Dans cet article, vous avez appris à interroger des bases de données en utilisant le mot-clé `HAVING`.

N'oubliez pas que vous devez utiliser la clause `HAVING` avec `GROUP BY` pour obtenir les données souhaitées, comme vous l'avez vu dans cet article.

Dans les situations où vous ne pouvez pas utiliser la clause `HAVING`, vous devez probablement utiliser `WHERE`.

Merci d'avoir lu.