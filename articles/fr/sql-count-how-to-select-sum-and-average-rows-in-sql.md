---
title: SQL Count – Comment sélectionner, additionner et calculer la moyenne des lignes
  en SQL
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-29T20:04:04.000Z'
originalURL: https://freecodecamp.org/news/sql-count-how-to-select-sum-and-average-rows-in-sql
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/safar-safarov-koOdUvfGr4c-unsplash.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: SQL Count – Comment sélectionner, additionner et calculer la moyenne des
  lignes en SQL
seo_desc: "In SQL, there are two built-in functions to sum or average the data in\
  \ your table. \nIn this article I will show you how to use the SUM and AVG functions\
  \ in SQL using code examples. \nHow to use the SUM function in SQL\nIf you need\
  \ to add a group of num..."
---

En SQL, il existe deux fonctions intégrées pour additionner ou calculer la moyenne des données de votre table. 

Dans cet article, je vais vous montrer comment utiliser les fonctions **`SUM`** et **`AVG`** en SQL à l'aide d'exemples de code. 

## Comment utiliser la fonction SUM en SQL

Si vous devez additionner un groupe de nombres dans votre table, vous pouvez utiliser la fonction `SUM` en SQL. 

Voici la syntaxe de base :

```sql
SELECT SUM(column_name) FROM table_name;
```

L'instruction `SELECT` en SQL indique à l'ordinateur d'obtenir des données à partir de la table.

La clause `FROM` en SQL spécifie quelle table nous voulons lister.

Dans cet exemple, nous avons une table appelée `students` avec les colonnes `id`, `name`, `date` et `total`. Nous voulons additionner le nombre total de barres chocolatées vendues par tous les étudiants. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-5.42.26-AM.png)

Nous pouvons utiliser cette syntaxe pour obtenir le nombre total de barres chocolatées vendues :

```sql
SELECT SUM(total) FROM students;
```

Le résultat serait 41.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-5.44.54-AM.png)

Nous pouvons également obtenir la somme pour chaque étudiant en utilisant la clause `GROUP BY`. 

La première partie consiste à sélectionner le nom et la somme du nombre total de barres chocolatées vendues, comme ceci :

```sql
SELECT name, SUM(total)
```

La deuxième partie consiste à regrouper la somme par nom :

```sql
FROM students GROUP BY name;
```

Voici le code complet pour regrouper le nombre total de barres chocolatées vendues par nom d'étudiant. 

```sql
SELECT name, SUM(total) FROM students GROUP BY name;
```

Voici à quoi ressemblerait le résultat dans notre table :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-5.54.14-AM.png)

Pour l'instant, les résultats sont regroupés par ordre alphabétique selon le nom de l'étudiant. 

Nous pouvons modifier le code pour trier la liste des résultats du total le plus grand au plus petit en utilisant la clause `ORDER BY`. 

```sql
SELECT name, SUM(total) FROM students GROUP BY name ORDER BY total DESC;
```

Le mot-clé `DESC` indique à l'ordinateur de trier du total le plus grand au plus petit. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-6.05.02-AM.png)

Si nous voulions trier le total du plus petit au plus grand, nous omettions alors le mot-clé `DESC`.

```sql
SELECT name, SUM(total) FROM students GROUP BY name ORDER BY total;
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-6.07.10-AM.png)

## Comment utiliser la fonction AVG en SQL

La fonction `AVG` trouve la moyenne arithmétique pour un groupe d'enregistrements dans une table SQL. Une moyenne, ou moyenne arithmétique, est la somme d'un groupe de nombres divisée par le nombre d'éléments de ce groupe. 

Par exemple, 2+4+4+6+6+8 est 30 divisé par 6, ce qui donne une moyenne de 5. 

Voici la syntaxe de base pour la fonction `AVG` :

```sql
SELECT AVG(column_name) FROM table_name;
```

Dans cet exemple, nous avons une table appelée `students`, avec les colonnes `id`, `name`, `date` et `scores`. Nous voulons trouver la moyenne de tous les résultats des tests des étudiants dans notre table.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-4.10.47-AM.png)

Nous devons utiliser cette syntaxe pour obtenir la moyenne des résultats des tests :

```sql
SELECT AVG(scores) FROM students; 
```

La moyenne serait 85,333. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-4.21.21-AM.png)

Nous pouvons également utiliser la fonction `ROUND` pour arrondir notre résultat à l'entier le plus proche. 

```sql
SELECT ROUND(AVG(scores)) FROM students; 
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-4.32.05-AM.png)

Nous pouvons également obtenir la moyenne pour chaque étudiant en utilisant la clause `GROUP BY`. 

La première partie consiste à sélectionner le nom et la moyenne des scores, comme ceci :

```sql
SELECT name, ROUND(AVG(scores))
```

La deuxième partie consiste à regrouper les scores moyens par nom :

```sql
FROM students GROUP BY name;
```

Voici à quoi ressemble le code complet :

```sql
SELECT name, ROUND(AVG(scores)) FROM students GROUP BY name;
```

Voici à quoi ressemble le résultat dans la table :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-29-at-5.17.28-AM.png)

## Conclusion

Il peut y avoir des moments où vous devez trouver la somme ou la moyenne des enregistrements de votre table.

Si vous devez additionner un groupe de nombres dans votre table, vous pouvez utiliser la fonction `SUM` en SQL.

Voici la syntaxe de base :

```sql
SELECT SUM(column_name) FROM table_name;
```

Si vous devez organiser les données en groupes, vous pouvez utiliser la clause `GROUP BY`.

La fonction `AVG` trouve la moyenne arithmétique pour un groupe d'enregistrements dans une table SQL. Une moyenne, ou moyenne arithmétique, est la somme d'un groupe de nombres divisée par le nombre d'éléments de ce groupe.

Voici la syntaxe de base.

```sql
SELECT AVG(column_name) FROM table_name;
```

J'espère que vous avez apprécié ce tutoriel et je vous souhaite bonne chance dans votre apprentissage de SQL.