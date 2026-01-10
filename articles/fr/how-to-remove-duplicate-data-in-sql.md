---
title: Comment supprimer les données en double en SQL
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-10T21:22:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-duplicate-data-in-sql
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Remove.JPG
tags:
- name: data analysis
  slug: data-analysis
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Comment supprimer les données en double en SQL
seo_desc: 'Duplicates can be a big problem in SQL databases as they can slow down
  query performance and waste valuable storage space.

  Fortunately, there are several ways to remove duplicate data in SQL.

  In this article, we will explore some of the most effectiv...'
---

Les doublons peuvent être un problème majeur dans les bases de données SQL, car ils peuvent ralentir les performances des requêtes et gaspiller un espace de stockage précieux.

Heureusement, il existe plusieurs façons de supprimer les données en double en SQL.

Dans cet article, nous explorerons certaines des méthodes les plus efficaces pour supprimer les données en double en SQL, notamment l'utilisation du mot-clé DISTINCT, de la clause GROUP BY et de l'instruction INNER JOIN.

## Comment supprimer les doublons en SQL à l'aide du mot-clé `DISTINCT` 

L'un des moyens les plus simples de supprimer les données en double en SQL consiste à utiliser le mot-clé DISTINCT. Vous pouvez utiliser le mot-clé DISTINCT dans une instruction SELECT pour récupérer uniquement les valeurs uniques d'une colonne particulière.

Voici un exemple de la façon d'utiliser le mot-clé DISTINCT pour supprimer les doublons d'une table :

```sql
SELECT DISTINCT column_name
FROM table_name;
```

Par exemple, si nous avons une table appelée "customers" avec les colonnes "customer\_id" et "customer\_name", nous pouvons utiliser la requête SQL suivante pour supprimer les doublons de la colonne "customer\_name" :

```sql
SELECT DISTINCT customer_name
FROM customers;
```

## Comment supprimer les doublons en SQL à l'aide de la clause `GROUP BY` 

Une autre façon de supprimer les doublons en SQL consiste à utiliser la clause GROUP BY. La clause GROUP BY regroupe les lignes en fonction des valeurs d'une colonne spécifique et ne renvoie qu'une seule ligne pour chaque valeur unique.

Voici un exemple de la façon d'utiliser la clause GROUP BY pour supprimer les doublons d'une table :

```sql
SELECT column_name
FROM table_name
GROUP BY column_name;
```

Par exemple, si nous avons une table appelée "orders" avec les colonnes "order\_id", "customer\_id" et "order\_date", nous pouvons utiliser la requête SQL suivante pour supprimer les doublons de la colonne "customer\_id" :

```sql
SELECT customer_id
FROM orders
GROUP BY customer_id;
```

## Comment supprimer les doublons en SQL à l'aide de l'instruction `INNER JOIN` 

Une autre façon de supprimer les doublons en SQL consiste à utiliser l'instruction INNER JOIN. L'instruction INNER JOIN combine les lignes de deux tables ou plus sur la base d'une colonne liée entre elles. En joignant une table avec elle-même, nous pouvons comparer les lignes et supprimer les doublons.

Voici un exemple de la façon d'utiliser l'instruction INNER JOIN pour supprimer les doublons d'une table :

```sql
SELECT a.column_name
FROM table_name a
INNER JOIN table_name b ON a.column_name = b.column_name
WHERE a.primary_key > b.primary_key;
```

Par exemple, si nous avons une table appelée "employees" avec les colonnes "employee\_id", "employee\_name" et "department\_id", nous pouvons utiliser la requête SQL suivante pour supprimer les doublons de la colonne "department\_id" :

```sql
SELECT a.department_id
FROM employees a
INNER JOIN employees b ON a.department_id = b.department_id
WHERE a.employee_id > b.employee_id;
```

## Conclusion

La suppression des données en double dans SQL peut aider à améliorer les performances des requêtes et à économiser de l'espace de stockage.

En utilisant le mot-clé `DISTINCT`, la clause `GROUP BY` et l'instruction `INNER JOIN`, nous pouvons supprimer les doublons d'une table en SQL.

N'oubliez pas de toujours faire une sauvegarde de vos données avant de les modifier afin d'éviter toute perte de données potentielle.

Connectons-nous sur [Twitter](https://twitter.com/Olujerry19) et [LinkedIn](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/).