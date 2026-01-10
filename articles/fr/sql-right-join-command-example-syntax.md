---
title: 'La commande SQL Right Join : Exemple de syntaxe'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-16T22:59:00.000Z'
originalURL: https://freecodecamp.org/news/sql-right-join-command-example-syntax
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f47740569d1a4ca41bf.jpg
tags:
- name: SQL
  slug: sql
seo_title: 'La commande SQL Right Join : Exemple de syntaxe'
seo_desc: 'For this guide we’ll discuss the SQL RIGHT JOIN.

  Right Join

  The RIGHT JOIN keyword returns all records from the right table (table2), and the
  matched records from the left table(table1) . The result is NULL from the left side,
  when there is no match....'
---

Dans ce guide, nous allons discuter de la commande SQL RIGHT JOIN.

### Jointure à droite

Le mot-clé RIGHT JOIN retourne tous les enregistrements de la table de droite (table2), et les enregistrements correspondants de la table de gauche (table1). Le résultat est NULL du côté gauche, lorsqu'il n'y a pas de correspondance.

```
SELECT *
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;

```

### Listes complètes des tables pour référence

Données de la table food ou LEFT

```
+---------+--------------+-----------+------------+
| ITEM_ID | ITEM_NAME    | ITEM_UNIT | COMPANY_ID |
+---------+--------------+-----------+------------+
| 1       | Chex Mix     | Pcs       | 16         |
| 6       | Cheez-It     | Pcs       | 15         |
| 2       | BN Biscuit   | Pcs       | 15         |
| 3       | Mighty Munch | Pcs       | 17         |
| 4       | Pot Rice     | Pcs       | 15         |
| 5       | Jaffa Cakes  | Pcs       | 18         |
| 7       | Salt n Shake | Pcs       |            |
+---------+--------------+-----------+------------+



Données de la table company ou RIGHT
``` text
+------------+---------------+--------------+
| COMPANY_ID | COMPANY_NAME  | COMPANY_CITY |
+------------+---------------+--------------+
| 18         | Order All     | Boston       |
| 15         | Jack Hill Ltd | London       |
| 16         | Akas Foods    | Delhi        |
| 17         | Foodies.      | London       |
| 19         | sip-n-Bite.   | New York     |
+------------+---------------+--------------+

```

Pour obtenir le nom de la société à partir de la table company et l'ID de la société, le nom de l'article à partir de la table foods, l'instruction SQL suivante peut être utilisée :

```
SELECT company.company_id,company.company_name,
company.company_city,foods.company_id,foods.item_name
FROM   company
RIGHT JOIN foods
ON company.company_id = foods.company_id;

```

SORTIE

```
COMPANY_ID COMPANY_NAME              COMPANY_CITY              COMPANY_ID ITEM_NAME
---------- ------------------------- ------------------------- ---------- --------------
18         Order All                 Boston                    18         Jaffa Cakes
15         Jack Hill Ltd             London                    15         Pot Rice
15         Jack Hill Ltd             London                    15         BN Biscuit
15         Jack Hill Ltd             London                    15         Cheez-It
16         Akas Foods                Delhi                     16         Chex Mix
17         Foodies.                  London                    17         Mighty Munch
NULL       NULL                      NULL                      NULL       Salt n Shake

```