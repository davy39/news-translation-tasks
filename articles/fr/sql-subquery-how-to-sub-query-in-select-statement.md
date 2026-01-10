---
title: Sous-requête SQL – Comment utiliser une sous-requête dans une instruction SELECT
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-10-04T17:08:48.000Z'
originalURL: https://freecodecamp.org/news/sql-subquery-how-to-sub-query-in-select-statement
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/subqueries.png
tags:
- name: data analysis
  slug: data-analysis
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Sous-requête SQL – Comment utiliser une sous-requête dans une instruction
  SELECT
seo_desc: "A SQL subquery is a query inside a query. So, in SQL, a subquery is also\
  \ called a nested query or an inner query. The outer query in which the inner query\
  \ is inserted is the main query. \nSQL admins usually use subqueries inside the\
  \ WHERE clause to na..."
---

Une sous-requête SQL est une requête à l'intérieur d'une autre requête. Ainsi, en SQL, une sous-requête est également appelée requête imbriquée ou requête interne. La requête externe dans laquelle la sous-requête est insérée est la requête principale. 

Les administrateurs SQL utilisent généralement des sous-requêtes à l'intérieur de la clause WHERE pour affiner le résultat de la requête principale (ou requête externe). 

Vous placez généralement les sous-requêtes entre parenthèses et vous pouvez les utiliser avec des opérateurs de comparaison tels que =, <, >, <= et >=.

Un cas d'utilisation valide d'une sous-requête est de l'utiliser avec l'instruction SELECT lorsque vous ne connaissez pas la valeur exacte dans la base de données. Même si vous connaissez la valeur, vous pouvez toujours utiliser une sous-requête pour obtenir plus de données sur celle-ci.

Dans cet article, vous apprendrez à utiliser des sous-requêtes à l'intérieur de l'instruction SELECT.

## Comment utiliser les sous-requêtes SQL avec l'instruction Select
Je vais travailler avec une table `employees` dans une base de données `employees_data`. L'exécution de `SELECT * FROM employees` me donne la table suivante :

![ss1](https://www.freecodecamp.org/news/content/images/2022/10/ss1.png) 

### Exemple 1 de sous-requêtes

Pour obtenir les données de ceux qui gagnent plus que le salaire moyen, j'ai exécuté la requête et la sous-requête suivantes :

```sql
SELECT * FROM employees
WHERE wage > (SELECT AVG(wage) FROM employees)
```

Dans la requête ci-dessus :
- la requête principale a tout sélectionné dans la table employees
- la sous-requête (`SELECT AVG(wage) FROM employees`) a obtenu le salaire moyen des employés
- la clause WHERE que j'ai spécifiée (`WHERE wage >`) était responsable de l'obtention de chaque employé ayant un salaire inférieur au salaire moyen. 

La requête renvoie les données suivantes :
![ss2](https://www.freecodecamp.org/news/content/images/2022/10/ss2.png) 

Pour vous montrer le salaire moyen, en particulier, je pourrais exécuter uniquement la sous-requête :
![ss3](https://www.freecodecamp.org/news/content/images/2022/10/ss3.png) 

Vous pouvez voir que le salaire moyen est de 1250.0000. Ainsi, la requête et la sous-requête nous ont aidés à obtenir tous les employés ayant un salaire supérieur au salaire moyen de 1250.0000.

Pour ajuster la requête afin d'obtenir les données des employés gagnant moins que le salaire moyen, nous avons seulement besoin de changer le symbole supérieur à (>) par inférieur à (<) :

```sql
SELECT * FROM employees
WHERE wage < (SELECT AVG(wage) FROM employees)
```

![ss4](https://www.freecodecamp.org/news/content/images/2022/10/ss4.png) 

### Exemples de sous-requêtes SQL

Pour obtenir le salaire des employés des États-Unis, y compris leurs noms et leur pays, j'ai combiné la clause WHERE avec l'instruction IN. L'instruction IN vous permet d'utiliser plusieurs valeurs à l'intérieur d'une clause WHERE.

```sql
SELECT name, country, wage FROM employees 
WHERE country IN (SELECT country 
         FROM employees 
         WHERE country = 'USA') ;
```

![ss5](https://www.freecodecamp.org/news/content/images/2022/10/ss5.png) 

Pour vous montrer que vous pouvez réellement utiliser plusieurs valeurs à l'intérieur de la clause WHERE à l'aide de l'instruction IN, j'ai obtenu le salaire de certains employés dont les noms sont connus en exécutant cette requête :

```sql
SELECT name, wage FROM employees
WHERE name IN ('Denis Jack', 'Ola Ajayi', 'Uche Ugo');
```

Voici le résultat :

![ss6](https://www.freecodecamp.org/news/content/images/2022/10/ss6.png) 

## Conclusion
Cet article vous a montré ce que vous devez savoir sur les sous-requêtes SQL et comment les utiliser avec l'instruction SELECT.

Cependant, les sous-requêtes ne se limitent pas à l'instruction SELECT uniquement. Vous pouvez utiliser des sous-requêtes dans toutes les opérations CRUD de SQL – INSERT, SELECT, UPDATE et DELETE.

Si vous trouvez l'article utile, n'hésitez pas à le partager avec vos amis et votre famille.