---
title: L'opérateur SQL Union et Union All expliqué avec des exemples de syntaxe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-10T22:40:00.000Z'
originalURL: https://freecodecamp.org/news/sql-union-and-union-all-operators-explained-with-syntax-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f73740569d1a4ca42a7.jpg
tags:
- name: SQL
  slug: sql
seo_title: L'opérateur SQL Union et Union All expliqué avec des exemples de syntaxe
seo_desc: 'For this guide we’ll discuss the UNION Operator section of the SQL statement.

  The UNION Operator is used to combine the results of multiple select statements
  into one result set.

  The SQL statements must have the same number of columns in their Select...'
---

Pour ce guide, nous allons discuter de la section de l'opérateur UNION de l'instruction SQL.

L'opérateur UNION est utilisé pour combiner les résultats de plusieurs instructions select en un seul ensemble de résultats.

Les instructions SQL doivent avoir le même nombre de colonnes dans leur instruction Select.

### Exemple de base

Instruction SQL

```
SELECT 'aaaaa'
UNION
SELECT 'bbbbbbbbb';

```

Sortie

```
+-----------+
| aaaaa     |
+-----------+
| aaaaa     |
| bbbbbbbbb |
+-----------+
2 rows in set (0.00 sec)

```

### Exemple utilisant les tables student

Instruction SQL

```
SELECT StudentID, FullName FROM student WHERE studentID BETWEEN 1 AND 5
UNION
SELECT studentID, studentEmailAddr FROM `student-contact-info` WHERE studentID BETWEEN 7 AND 8;

```

Sortie

```
+-----------+--------------------------------+
| StudentID | FullName                       |
+-----------+--------------------------------+
|         1 | Monique Davis                  |
|         2 | Teri Gutierrez                 |
|         3 | Spencer Pautier                |
|         4 | Louis Ramsey                   |
|         5 | Alvin Greene                   |
|         7 | Maximo.Smith@freeCodeCamp.org  |
|         8 | Michael.Roach@freeCodeCamp.ort |
+-----------+--------------------------------+
7 rows in set (0.00 sec)

```

## Opérateur SQL UNION ALL

L'opérateur UNION ALL est une extension de l'opérateur UNION où il doit vous donner un résultat de A+B de lignes dans la sortie en supposant que A et B sont vos entrées, en termes simples, UNION ALL ne supprime pas les doublons.

### Syntaxe de base

Instruction SQL

```
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions]
UNION ALL
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions];

```

Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à elles que ce qui est dans ce guide d'introduction.

J'espère que cela vous donne au moins assez pour commencer.

Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options vous-même.