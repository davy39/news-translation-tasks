---
title: Guide des alias SQL - Comment utiliser des alias pour les tables avec le mot-clé
  AS - avec syntaxe d'exemple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-17T21:53:00.000Z'
originalURL: https://freecodecamp.org/news/sql-alias-guide-as-keyword
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/jamie-street-Zqy-x7K5Qcg-unsplash.jpg
tags:
- name: SQL
  slug: sql
seo_title: Guide des alias SQL - Comment utiliser des alias pour les tables avec le
  mot-clé AS - avec syntaxe d'exemple
seo_desc: 'Using AS to assign meaningful or simpler names

  You can use AS to assign a name to a column of data you are selecting or that has
  been calculated.

  SELECT user_only_num1 AS AgeOfServer, (user_only_num1 - warranty_period) AS NonWarrantyPeriod
  FROM serve...'
---

## Utilisation de AS pour attribuer des noms significatifs ou plus simples

Vous pouvez utiliser AS pour attribuer un nom à une colonne de données que vous sélectionnez ou qui a été calculée.

```
SELECT user_only_num1 AS AgeOfServer, (user_only_num1 - warranty_period) AS NonWarrantyPeriod FROM server_table

```

Cela produit le résultat suivant.

```
+-------------+------------------------+
| AgeOfServer | NonWarrantyPeriod      | 
+-------------+------------------------+
|         36  |                     24 |
|         24  |                     12 | 
|         61  |                     49 |
|         12  |                      0 | 
|          6  |                     -6 |
|          0  |                    -12 | 
|         36  |                     24 |
|         36  |                     24 | 
|         24  |                     12 | 
+-------------+------------------------+

```

Vous pouvez également utiliser AS pour attribuer un nom à une table afin de faciliter les références dans les jointures.

```
SELECT ord.product, ord.ord_number, ord.price, cust.cust_name, cust.cust_number FROM customer_table AS cust

JOIN order_table AS ord ON cust.cust_number = ord.cust_number

```

Cela produit le résultat suivant.

```
+-------------+------------+-----------+-----------------+--------------+
| product     | ord_number | price     | cust_name       | cust_number  |
+-------------+------------+-----------+-----------------+--------------+
|     RAM     |   12345    |       124 | John Smith      |  20          |
|     CPU     |   12346    |       212 | Mia X           |  22          |
|     USB     |   12347    |        49 | Elise Beth      |  21          |
|     Cable   |   12348    |         0 | Paul Fort       |  19          |
|     Mouse   |   12349    |        66 | Nats Back       |  15          |
|     Laptop  |   12350    |       612 | Mel S           |  36          |
|     Keyboard|   12351    |        24 | George Z        |  95          |
|     Keyboard|   12352    |        24 | Ally B          |  55          |
|     Air     |   12353    |        12 | Maria Trust     |  11          |
+-------------+------------+-----------+-----------------+--------------+

```