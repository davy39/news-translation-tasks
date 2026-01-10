---
title: Techniques SQL avancées pour les requêtes complexes
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-21T17:01:39.000Z'
originalURL: https://freecodecamp.org/news/advanced-sql-techniques
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/GBL.JPG
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Techniques SQL avancées pour les requêtes complexes
seo_desc: 'Structured Query Language or SQL is an effective tool for managing and
  modifying data that is stored in databases.

  The SELECT, INSERT, UPDATE, and DELETE SQL commands are suitable for many common
  use cases. But sometimes, more sophisticated technique...'
---

Le Structured Query Language, ou SQL, est un outil efficace pour gérer et modifier les données stockées dans des bases de données.

Les commandes SQL SELECT, INSERT, UPDATE et DELETE conviennent à de nombreux cas d'utilisation courants. Mais parfois, des techniques plus sophistiquées peuvent vous aider à effectuer des requêtes et des analyses plus complexes avec une précision et une efficacité accrues.

Dans ce tutoriel, nous aborderons certaines des techniques SQL avancées les plus populaires et fournirons des applications concrètes pour chacune d'elles.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/tenor.gif align="left")

## Fonctions de fenêtrage

Vous pouvez utiliser les fonctions de fenêtrage (window functions) pour effectuer des calculs sur une « fenêtre » de données définie par un sous-ensemble particulier de lignes dans une table. Cela peut être utile lorsque vous effectuez des opérations telles que le calcul de totaux cumulés, le tri de lignes selon un critère particulier ou la localisation de valeurs aberrantes dans un ensemble de données.

Commençons par examiner un exemple interactif de la manière de créer des totaux cumulés à l'aide des fonctions de fenêtrage. Supposons que vous souhaitiez déterminer les ventes cumulées pour chaque mois d'une entreprise. Vous disposez d'un tableau de données de ventes qui indique les ventes totales pour chaque mois.

Voici un exemple de code que vous pouvez exécuter dans la console SQL pour effectuer ce calcul :

```sql
SELECT month, sales, SUM(sales) OVER (ORDER BY month) AS cumulative_sales
FROM sales_data;
```

Cette requête SQL est utilisée pour analyser les données de ventes au fil du temps. Elle sélectionne trois colonnes de la table `sales_data` : `month`, `sales` et `cumulative_sales`.

La colonne `month` contient le mois au cours duquel les ventes ont été réalisées, tandis que la colonne `sales` contient les ventes totales pour ce mois. La colonne `cumulative_sales` est calculée à l'aide de la fonction `SUM()` et de la clause `OVER()`, qui additionne toutes les valeurs de `sales` jusqu'au mois en cours inclusivement.

Ainsi, la colonne `cumulative_sales` montre comment les ventes s'accumulent au fil du temps. En examinant cette colonne, vous pouvez voir la progression des ventes d'un mois à l'autre et identifier les périodes de ventes élevées ou faibles.

Dans l'ensemble, cette requête SQL est utile pour identifier les tendances et les modèles de vente, ce qui peut aider les entreprises à prendre des décisions éclairées concernant leurs opérations et leurs stratégies.

## Expressions de table communes

Vous pouvez créer un ensemble de résultats nommé temporaire que vous pouvez utiliser dans des requêtes ultérieures au cours de la même session en utilisant les expressions de table communes (Common Table Expressions ou CTE). Cela peut être utile pour décomposer des requêtes compliquées en parties plus simples et plus faciles à gérer.

Essayons maintenant une démonstration interactive de l'utilisation des expressions de table communes (CTE) pour diviser une requête difficile en parties plus petites et plus maniables.

Considérez un scénario dans lequel vous souhaitez déterminer l'âge moyen des clients ayant acheté un produit particulier. Vous disposez d'un tableau de données clients comprenant leur nom, leur âge et les produits qu'ils ont achetés.

Voici un exemple de code que vous pouvez exécuter dans la console SQL pour effectuer ce calcul à l'aide d'une CTE :

```sql
WITH product_customers AS (
  SELECT name, age
  FROM customer_data
  WHERE product = 'widget'
)
SELECT AVG(age) AS avg_age
FROM product_customers;
```

Cette requête utilise une expression de table commune (CTE), qui est un ensemble de résultats nommé temporaire pouvant être référencé au sein d'une seule requête.

La CTE est nommée `product_customers`. Elle est créée à l'aide d'une instruction `SELECT` qui récupère les colonnes `name` et `age` de la table `customer_data` pour les clients ayant acheté le produit 'widget'.

La seconde partie de la requête sélectionne l'âge moyen des clients ayant acheté le produit 'widget', en utilisant la fonction `AVG()`. Le mot-clé `AS` donne à la colonne résultante le nom de `avg_age`.

Dans l'ensemble, cette requête est utile pour analyser les caractéristiques démographiques des clients ayant acheté un produit particulier, dans ce cas, le 'widget'. En calculant l'âge moyen de ces clients, les entreprises peuvent obtenir des informations sur les préférences et les comportements de leur public cible et utiliser ces informations pour orienter leurs stratégies de marketing et de développement de produits.

### Requêtes récursives

Les requêtes récursives vous permettent d'effectuer des calculs hiérarchiques ou itératifs sur des données structurées sous forme d'arbre ou de graphe. Cela peut être utile pour des tâches telles que le calcul du coût total d'une série de transactions interconnectées ou l'identification du chemin le plus court entre deux nœuds d'un réseau.

Essayons maintenant un exemple interactif de l'utilisation des requêtes récursives pour effectuer des calculs hiérarchiques sur des données.

Imaginez que vous ayez un tableau de données sur les employés qui comprend le nom de chaque employé, son titre de poste et le nom de son superviseur. Vous souhaitez trouver le nombre total d'employés dans chaque catégorie de poste.

Voici un exemple de code que vous pouvez exécuter dans la console SQL pour effectuer ce calcul à l'aide d'une CTE récursive :

```sql
WITH RECURSIVE job_categories AS (
  SELECT job_title, COUNT(*) AS employee_count
  FROM employee_data
  GROUP BY job_title
  UNION ALL
  SELECT e.job_title, COUNT(*) AS employee_count
  FROM employee_data e
  JOIN job_categories jc ON e.supervisor = jc.job_title
  GROUP BY e.job_title
)
SELECT job_title, SUM(employee_count) AS total_employees
FROM job_categories
GROUP BY job_title;
```

Cette requête utilise une expression de table commune (CTE) avec un composant récursif, ce qui lui permet de parcourir des structures de données hiérarchiques.

La CTE est nommée `job_categories` et est créée à l'aide de deux instructions `SELECT` combinées avec l'opérateur `UNION ALL`.

La première partie de la requête sélectionne la colonne `job_title` et calcule le nombre d'employés dans chaque catégorie de poste en comptant le nombre de lignes dans la table `employee_data` qui ont le même `job_title`.

La deuxième partie de la requête est l'endroit où la récursion se produit. Elle sélectionne la colonne `job_title` et calcule le nombre d'employés dans chaque catégorie de poste. Elle le fait en joignant la table `employee_data` avec la CTE `job_categories` à la condition que le superviseur de l'employé figure dans la colonne `job_title` de la CTE. Cela permet à la requête de parcourir la hiérarchie des catégories de postes pour calculer le nombre total d'employés dans chaque catégorie.

Enfin, la requête sélectionne les colonnes `job_title` et `employee_count` de la CTE `job_categories` et utilise la fonction `SUM()` pour calculer le nombre total d'employés dans chaque catégorie de poste. La clause `GROUP BY` est utilisée pour grouper les résultats par titre de poste.

Globalement, cette requête est utile pour analyser la structure hiérarchique des données des employés et calculer des statistiques agrégées pour chaque niveau de la hiérarchie. En comprenant la répartition des employés entre les catégories de postes, les entreprises peuvent identifier les domaines à améliorer et prendre des décisions fondées sur les données concernant l'embauche, les promotions et l'allocation des ressources.

## Conclusion

Les techniques SQL avancées telles que les fonctions de fenêtrage, les CTE et les requêtes récursives peuvent vous aider à effectuer des analyses et des manipulations de données complexes avec une précision et une efficacité accrues.

En comprenant ces techniques et leurs applications concrètes, vous pouvez profiter pleinement des capacités de SQL et devenir un gestionnaire de données plus efficace.