---
title: 'Le guide ultime des instructions SQL Join : Left, Right, Inner, Outer'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-10T21:28:00.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-sql-join-statements
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eca740569d1a4ca3f21.jpg
tags:
- name: SQL
  slug: sql
seo_title: 'Le guide ultime des instructions SQL Join : Left, Right, Inner, Outer'
seo_desc: 'What is a SQL Join Statement?

  For this guide we’ll discuss the JOIN section of the SQL statement. We will cover
  its syntax and the different types of joins that SQL enables.

  SQL syntax with focus on Join

  SELECT col1, col2, col3, etc....

  FROM  tableNa...'
---

## Qu'est-ce qu'une instruction SQL Join ?

Dans ce guide, nous discuterons de la section JOIN de l'instruction SQL. Nous aborderons sa syntaxe et les différents types de jointures que SQL permet.

### Syntaxe SQL avec un focus sur Join

```
SELECT col1, col2, col3, etc....
FROM  tableNameOne AS a
JOIN tableNameTwo AS b ON a.primeKey = b.primeKey 
etc...

```

L'instruction JOIN peut être simplement JOIN ou INNER JOIN, qui sont identiques, ou LEFT JOIN (décrit ci-dessous).

### Différents types de JOINs

* (INNER) JOIN
* Retourne les enregistrements qui ont des valeurs correspondantes dans les deux tables
* LEFT (OUTER) JOIN
* Retourne tous les enregistrements de la table de gauche, et les enregistrements correspondants de la table de droite
* RIGHT (OUTER) JOIN
* Retourne tous les enregistrements de la table de droite, et les enregistrements correspondants de la table de gauche
* FULL (OUTER) JOIN
* Retourne tous les enregistrements lorsqu'il y a une correspondance dans la table de gauche ou de droite

### Join

La table des étudiants sera dans la clause FROM, elle sera donc une table de départ ou de GAUCHE.

Nous allons JOINdre cela à la table des contacts des étudiants ou à la table de DROITE.

Vous verrez que tous les étudiants apparaissent également dans la table des contacts.

Comme le montrent les tables ci-dessous, l'étudiantID 9 est dans la table des étudiants mais PAS dans la table des contacts, donc il n'apparaîtra pas dans une jointure.

Instruction SQL

```
SELECT a.studentID, a.FullName, a.programOfStudy,
b.`student-phone-cell`, b.`student-US-zipcode`
FROM student AS a
JOIN `student-contact-info` AS b ON a.studentID = b.studentID;

```

Données "jointes" :

```
+-----------+------------------------+------------------+--------------------+--------------------+
| studentID | FullName               | programOfStudy   | student-phone-cell | student-US-zipcode |
+-----------+------------------------+------------------+--------------------+--------------------+
|         1 | Monique Davis          | Literature       | 555-555-5551       |              97111 |
|         2 | Teri Gutierrez         | Programming      | 555-555-5552       |              97112 |
|         3 | Spencer Pautier        | Programming      | 555-555-5553       |              97113 |
|         4 | Louis Ramsey           | Programming      | 555-555-5554       |              97114 |
|         5 | Alvin Greene           | Programming      | 555-555-5555       |              97115 |
|         6 | Sophie Freeman         | Programming      | 555-555-5556       |              97116 |
|         7 | Edgar Frank "Ted" Codd | Computer Science | 555-555-5557       |              97117 |
|         8 | Donald D. Chamberlin   | Computer Science | 555-555-5558       |              97118 |
+-----------+------------------------+------------------+--------------------+--------------------+

```

### Left Join

L'utilisation du mot-clé LEFT avant JOIN amène le système à commencer avec la table des étudiants (GAUCHE) mais retournera NULL de la table de DROITE s'il n'y a pas de lignes pour l'étudiant de la table de GAUCHE.

Notez que l'étudiantID 9 apparaît ici mais les données de la table des contacts sont simplement affichées comme NULL.

```
SELECT a.studentID, a.FullName, a.programOfStudy,
b.`student-phone-cell`, b.`student-US-zipcode`
FROM student AS a
LEFT JOIN `student-contact-info` AS b ON a.studentID = b.studentID;

```

```
+-----------+------------------------+------------------+--------------------+--------------------+
| studentID | FullName               | programOfStudy   | student-phone-cell | student-US-zipcode |
+-----------+------------------------+------------------+--------------------+--------------------+
|         1 | Monique Davis          | Literature       | 555-555-5551       |              97111 |
|         2 | Teri Gutierrez         | Programming      | 555-555-5552       |              97112 |
|         3 | Spencer Pautier        | Programming      | 555-555-5553       |              97113 |
|         4 | Louis Ramsey           | Programming      | 555-555-5554       |              97114 |
|         5 | Alvin Greene           | Programming      | 555-555-5555       |              97115 |
|         6 | Sophie Freeman         | Programming      | 555-555-5556       |              97116 |
|         7 | Edgar Frank "Ted" Codd | Computer Science | 555-555-5557       |              97117 |
|         8 | Donald D. Chamberlin   | Computer Science | 555-555-5558       |              97118 |
|         9 | Raymond F. Boyce       | Computer Science | NULL               |               NULL |
+-----------+------------------------+------------------+--------------------+--------------------+
9 rows in set (0.00 sec)

```

### Listes complètes des tables pour référence

Listes des tables des étudiants

```
SELECT a.studentID, a.FullName, sat_score, a.programOfStudy, schoolEmailAdr 
FROM student AS a;

```

Table des étudiants ou table de GAUCHE

```
+-----------+------------------------+-----------+------------------+------------------------+
| studentID | FullName               | sat_score | programOfStudy   | schoolEmailAdr         |
+-----------+------------------------+-----------+------------------+------------------------+
|         1 | Monique Davis          |       400 | Literature       | Monique@someSchool.edu |
|         2 | Teri Gutierrez         |       800 | Programming      | Teri@someSchool.edu    |
|         3 | Spencer Pautier        |      1000 | Programming      | Spencer@someSchool.edu |
|         4 | Louis Ramsey           |      1200 | Programming      | Louis@someSchool.edu   |
|         5 | Alvin Greene           |      1200 | Programming      | Alvin@someSchool.edu   |
|         6 | Sophie Freeman         |      1200 | Programming      | Sophie@someSchool.edu  |
|         7 | Edgar Frank "Ted" Codd |      2400 | Computer Science | Edgar@someSchool.edu   |
|         8 | Donald D. Chamberlin   |      2400 | Computer Science | Donald@someSchool.edu  |
|         9 | Raymond F. Boyce       |      2400 | Computer Science | Raymond@someSchool.edu |
+-----------+------------------------+-----------+------------------+------------------------+
9 rows in set (0.00 sec)
```sql
SELECT * from `student-contact-info` AS b;

```

Table des contacts des étudiants ou table de DROITE

```
+-----------+----------------------------------+--------------------+--------------------+
| studentID | studentEmailAddr                 | student-phone-cell | student-US-zipcode |
+-----------+----------------------------------+--------------------+--------------------+
|         1 | Monique.Davis@freeCodeCamp.org   | 555-555-5551       |              97111 |
|         2 | Teri.Gutierrez@freeCodeCamp.org  | 555-555-5552       |              97112 |
|         3 | Spencer.Pautier@freeCodeCamp.org | 555-555-5553       |              97113 |
|         4 | Louis.Ramsey@freeCodeCamp.org    | 555-555-5554       |              97114 |
|         5 | Alvin.Green@freeCodeCamp.org     | 555-555-5555       |              97115 |
|         6 | Sophie.Freeman@freeCodeCamp.org  | 555-555-5556       |              97116 |
|         7 | Maximo.Smith@freeCodeCamp.org    | 555-555-5557       |              97117 |
|         8 | Michael.Roach@freeCodeCamp.ort   | 555-555-5558       |              97118 |
+-----------+----------------------------------+--------------------+--------------------+
8 rows in set (0.00 sec)

```

Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à elles que ce qui est dans ce guide d'introduction.

J'espère que cela vous donne au moins assez pour commencer.

Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options vous-même.

### Exemple d'utilisation

Dans ce guide, nous discuterons du SQL RIGHT JOIN.

### Right Join

Le mot-clé RIGHT JOIN retourne tous les enregistrements de la table de droite (table2), et les enregistrements correspondants de la table de gauche (table1). Le résultat est NULL du côté gauche, lorsqu'il n'y a pas de correspondance.

```
SELECT *
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;

```

### Listes complètes des tables pour référence

Données de la table des aliments ou table de GAUCHE

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



Données de la table des entreprises ou table de DROITE
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

Pour obtenir le nom de l'entreprise à partir de la table des entreprises et l'ID de l'entreprise, le nom de l'article à partir de la table des aliments, l'instruction SQL suivante peut être utilisée :

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