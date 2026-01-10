---
title: Fonctions d'agrégation SQL – Comment utiliser GROUP BY dans MySQL et PostgreSQL
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-09-01T15:57:13.000Z'
originalURL: https://freecodecamp.org/news/sql-aggregate-functions-how-to-group-by-in-mysql-and-postgresql
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/agg.png
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: postgres
  slug: postgres
- name: SQL
  slug: sql
seo_title: Fonctions d'agrégation SQL – Comment utiliser GROUP BY dans MySQL et PostgreSQL
seo_desc: "In SQL, aggregate functions let you perform a calculation on multiple data\
  \ and return a single value. That’s why they are called “aggregate” functions. \n\
  Those aggregate functions are AVG(), COUNT(), SUM(), MIN(), and MAX(). \nWhile making\
  \ queries with..."
---

En SQL, les fonctions d'agrégation vous permettent d'effectuer un calcul sur plusieurs données et de retourner une seule valeur. C'est pourquoi elles sont appelées fonctions "agrégées".

Ces fonctions d'agrégation sont `AVG()`, `COUNT()`, `SUM()`, `MIN()` et `MAX()`.

Lors de la création de requêtes avec les fonctions d'agrégation, vous pouvez également les utiliser en combinaison avec la clause `GROUP BY` et l'instruction `HAVING` dans n'importe quelle base de données relationnelle – MySQL, PostgreSQL, et autres.

Dans cet article, vous apprendrez comment utiliser les fonctions d'agrégation seules et avec la clause `GROUP BY` et l'instruction `HAVING`.

## Ce que nous allons couvrir
- [Comment utiliser les fonctions d'agrégation](#heading-comment-utiliser-les-fonctions-dagregation)
- [Syntaxe des fonctions d'agrégation](#heading-syntaxe-des-fonctions-dagregation)
- [Comment utiliser la fonction d'agrégation `AVG()`](#heading-comment-utiliser-la-fonction-dagregation-avg)
  - [Comment utiliser la fonction `AVG()` avec `GROUP BY` et `HAVING`](#heading-comment-utiliser-la-fonction-avg-avec-group-by-et-having)
- [Comment utiliser la fonction d'agrégation `COUNT()`](#heading-comment-utiliser-la-fonction-dagregation-count)
  - [Comment utiliser `COUNT()` avec `GROUP BY` et `HAVING`](#heading-comment-utiliser-count-avec-group-by-et-having)
- [Comment utiliser la fonction d'agrégation `MAX()`](#heading-comment-utiliser-la-fonction-dagregation-max)
  - [Comment utiliser `MAX()` avec `GROUP BY` et `HAVING`](#heading-comment-utiliser-max-avec-group-by-et-having)
- [Comment utiliser la fonction d'agrégation `MIN()`](#heading-comment-utiliser-la-fonction-dagregation-min)
  - [Comment utiliser `MIN()` avec `GROUP BY` et `HAVING`](#heading-comment-utiliser-min-avec-group-by-et-having)
- [Comment utiliser la fonction d'agrégation `SUM()`](#heading-comment-utiliser-la-fonction-dagregation-sum)
  - [Comment utiliser `SUM()` avec `GROUP BY` et `HAVING`](#heading-comment-utiliser-sum-avec-group-by-et-having)
- [Conclusion](#heading-conclusion)

## Comment utiliser les fonctions d'agrégation

Pour vous montrer comment fonctionnent les fonctions d'agrégation, je vais travailler avec une table `employees` dans une base de données `employees_data`.

L'exécution de `SELECT * FROM employees` m'a donné ce qui suit :
![ss1](https://www.freecodecamp.org/news/content/images/2022/09/ss1.png)

## Syntaxe des fonctions d'agrégation
La syntaxe pour travailler avec les fonctions d'agrégation ressemble à ceci :
```sql
aggregate_function(MODIFIER | expression)
```
- la fonction d'agrégation peut être `AVG`, `COUNT`, `MAX`, `MIN` ou `SUM`
- le modificateur peut être toutes les valeurs ou les valeurs dans une colonne particulière

Cette syntaxe sera plus claire en pratique, alors utilisons-la avec les fonctions d'agrégation.

## Comment utiliser la fonction d'agrégation `AVG()`
La fonction d'agrégation `AVG()` obtient le nombre total de données et calcule leur moyenne.

J'ai pu obtenir le salaire moyen payé aux employés de cette manière :
```sql
SELECT AVG(wage) 
FROM employees
```
![ss2](https://www.freecodecamp.org/news/content/images/2022/09/ss2.png)

La requête suivante obtient le salaire moyen des développeurs juniors :
```sql
SELECT AVG(wage) 
FROM employees
WHERE role = "Junior dev"
```
![ss3](https://www.freecodecamp.org/news/content/images/2022/09/ss3.png)

### Comment utiliser la fonction `AVG()` avec `GROUP BY` et `HAVING`
Vous pouvez obtenir le nombre moyen d'entrées (lignes) dans une colonne particulière avec la clause `GROUP BY` et l'instruction `HAVING`. Cela signifie que vous devez combiner ces deux éléments avec `AVG()`.

Par exemple, j'ai pu obtenir le salaire moyen payé aux employés dans chaque ligne avec cette requête :
```sql
SELECT role, AVG(wage) 
FROM employees
GROUP BY role
```
![ss4](https://www.freecodecamp.org/news/content/images/2022/09/ss4.png)

J'ai également pu obtenir le salaire moyen des développeurs seniors en utilisant l'instruction HAVING :
```sql
SELECT role, AVG(wage) 
FROM employees
GROUP BY role
HAVING role = "Senior dev"
```
![ss5](https://www.freecodecamp.org/news/content/images/2022/09/ss5.png)

## Comment utiliser la fonction d'agrégation `COUNT()`

`COUNT()` retourne le nombre de lignes dans une table en fonction de la condition (ou filtre) que vous appliquez.

Par exemple, pour obtenir le nombre total de lignes, j'ai exécuté la requête suivante :
```sql
SELECT COUNT(*) 
FROM employees
```
Et j'ai obtenu 20 :
![ss6](https://www.freecodecamp.org/news/content/images/2022/09/ss6.png)

Pour obtenir le nombre total d'employés des États-Unis, j'ai exécuté la requête suivante :
```sql
SELECT COUNT(*) 
FROM employees
WHERE country = "USA"
```
![ss7](https://www.freecodecamp.org/news/content/images/2022/09/ss7.png)

Et pour obtenir les employés qui sont rédacteurs techniques, j'ai fait ceci :
```sql
SELECT COUNT(*) 
FROM employees
WHERE role = "Tech Writer"
```
![ss8](https://www.freecodecamp.org/news/content/images/2022/09/ss8.png)

### Comment utiliser `COUNT()` avec `GROUP BY` et `HAVING`
Dans une grande base de données, vous pouvez utiliser la clause `GROUP BY` et l'instruction `HAVING` en combinaison avec COUNT() pour obtenir le nombre total d'entrées (lignes) dans une colonne particulière.

Dans la base de données que j'utilise dans cet article, j'ai pu obtenir le nombre total d'employés dans chaque ligne avec la clause GROUP BY :
```sql
SELECT role, COUNT(*) 
FROM employees
GROUP BY role
```
![ss9](https://www.freecodecamp.org/news/content/images/2022/09/ss9.png)

Pour obtenir le nombre uniquement des employés qui sont développeurs seniors, j'ai ajouté `HAVING role = "Senior dev"` à la requête :
```sql
SELECT role, COUNT(*) 
FROM employees
GROUP BY role
HAVING role = "Senior dev"
```
![ss10](https://www.freecodecamp.org/news/content/images/2022/09/ss10.png)

## Comment utiliser la fonction d'agrégation `MAX()`
La fonction `MAX()` retourne la valeur maximale parmi les valeurs non-NULL. Cela signifie qu'elle ignorera les champs qui sont vides et retournera la valeur la plus élevée parmi ceux qui ne sont pas vides.

Par exemple, pour obtenir le salaire le plus élevé dans la table `employees`, j'ai utilisé la fonction `MAX()` comme ceci :
```sql
SELECT MAX(wage) 
FROM employees
```
![ss11](https://www.freecodecamp.org/news/content/images/2022/09/ss11.png)

Pour obtenir le salaire maximum des développeurs de niveau intermédiaire, j'ai utilisé l'instruction `WHERE` :
```sql
SELECT MAX(wage) 
FROM employees
WHERE role = "Mid level dev"
```
![ss12](https://www.freecodecamp.org/news/content/images/2022/09/ss12.png)

### Comment utiliser `MAX()` avec `GROUP BY` et `HAVING`
Pour obtenir le salaire maximum dans chaque rôle, la clause `GROUP BY` est utile :
```sql
SELECT role, MAX(wage) 
FROM employees
GROUP BY role
```
![ss13](https://www.freecodecamp.org/news/content/images/2022/09/ss13.png)

Et pour obtenir le salaire maximum dans un rôle particulier, la combinaison de l'instruction HAVING avec la clause `GROUP BY` permet de le faire :

```sql
SELECT role, MAX(wage) 
FROM employees
GROUP BY role
HAVING role = "Tech writer"
```
![ss14](https://www.freecodecamp.org/news/content/images/2022/09/ss14.png)

## Comment utiliser la fonction d'agrégation `MIN()`
La fonction `MIN()` est l'opposé de la fonction `MAX()` – elle retourne la valeur minimale parmi les valeurs non-NULL.

Par exemple, j'ai obtenu le salaire le plus bas dans la table `employees` de cette manière :
```sql
SELECT MIN(wage) 
FROM employees
```
![ss15](https://www.freecodecamp.org/news/content/images/2022/09/ss15.png)

### Comment utiliser `MIN()` avec `GROUP BY` et `HAVING`
Encore une fois, pour obtenir le salaire minimum dans chaque rôle, la clause `GROUP BY` peut le faire :
```sql
SELECT role, MIN(wage) 
FROM employees
GROUP BY role
```
![ss16](https://www.freecodecamp.org/news/content/images/2022/09/ss16.png)

Et pour obtenir le salaire minimum d'un rôle particulier, l'instruction `HAVING` et la clause `GROUP BY` sont ce qu'il faut utiliser :
```sql
SELECT role, MIN(wage) 
FROM employees
GROUP BY role
HAVING role = "Junior dev"
```
![ss17](https://www.freecodecamp.org/news/content/images/2022/09/ss17.png)

## Comment utiliser la fonction d'agrégation `SUM()`
La fonction d'agrégation SUM() additionne le nombre d'entrées dans une colonne en fonction du filtre appliqué.

La requête suivante obtient le nombre total de salaires payés aux employés :
```sql
SELECT SUM(wage) 
FROM employees
```
![ss18](https://www.freecodecamp.org/news/content/images/2022/09/ss18.png)

### Comment utiliser SUM() avec `GROUP BY` et `HAVING`

Pour obtenir la somme des salaires totaux payés pour les employés dans chaque rôle, j'ai sélectionné le rôle, utilisé `SUM()` sur les salaires et les ai groupés par rôle :
```sql
SELECT role, SUM(wage) 
FROM employees
GROUP BY role
```
![ss19](https://www.freecodecamp.org/news/content/images/2022/09/ss19.png)

Pour obtenir les salaires totaux payés uniquement aux rédacteurs techniques, j'ai utilisé l'instruction `HAVING` :
```sql
SELECT role, SUM(wage) 
FROM employees
GROUP BY role
HAVING role = "Tech Writer"
```
![ss20](https://www.freecodecamp.org/news/content/images/2022/09/ss20.png)

## Conclusion
Cet article vous a guidé à travers ce que sont les fonctions d'agrégation en SQL, leur syntaxe et comment les utiliser.

De plus, vous avez également appris comment utiliser les fonctions d'agrégation avec la clause `GROUP BY`, `HAVING` et les instructions `WHERE`.

Si vous voulez apprendre comment fonctionne l'instruction `HAVING`, vous devriez lire [cet article](https://www.freecodecamp.org/news/sql-having-how-to-group-and-count-with-a-having-statement/) que j'ai écrit à ce sujet.

Merci d'avoir lu.