---
title: 'Vue SQL : Exemple de syntaxe pour l''instruction Replace View'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-14T22:53:00.000Z'
originalURL: https://freecodecamp.org/news/the-sql-replace-view-statement-example-syntax
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f4f740569d1a4ca41eb.jpg
tags:
- name: SQL
  slug: sql
seo_title: 'Vue SQL : Exemple de syntaxe pour l''instruction Replace View'
seo_desc: 'A View is a database object that presents data from in one or more tables.
  The same SQL statement used to create a view can also be used to replace an existing
  view.

  This guide will update (replace) the existing view “programming-students-v” with
  one...'
---

Une vue est un objet de base de données qui présente des données provenant d'une ou plusieurs tables. La même instruction SQL utilisée pour créer une vue peut également être utilisée pour remplacer une vue existante.

Ce guide va mettre à jour (remplacer) la vue existante « programming-students-v » par une autre légèrement différente et avec un nom différent.

Conseil de sécurité : faites toujours une sauvegarde du schéma avant de le modifier.

### Syntaxe générale

```
CREATE OR REPLACE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;

```

### SQL utilisé pour créer la vue et les données actuelles

```
create view `programming-students-v` as
select FullName, programOfStudy 
from student 
where programOfStudy = 'Programming';

```

```
select * from `programming-students-v`;

```

Données actuelles :

```
+-----------------+----------------+
| FullName        | programOfStudy |
+-----------------+----------------+
| Teri Gutierrez  | Programming    |
| Spencer Pautier | Programming    |
| Louis Ramsey    | Programming    |
| Alvin Greene    | Programming    |
| Sophie Freeman  | Programming    |
+-----------------+----------------+
5 rows in set (0.00 sec)

```

Une liste des vues existantes :

```
SHOW FULL TABLES IN fcc_sql_guides_database WHERE TABLE_TYPE LIKE 'VIEW';

```

```
+-----------------------------------+------------+
| Tables_in_fcc_sql_guides_database | Table_type |
+-----------------------------------+------------+
| programming-students-v            | VIEW       |
| students-contact-info_v           | VIEW       |
| students_dropme_v                 | VIEW       |
+-----------------------------------+------------+
3 rows in set (0.00 sec)

```

### Remplacement de la vue

```
create or replace view `programming-students-v` as
select FullName, programOfStudy, sat_score 
from student 
where programOfStudy = 'Programming';    

```

```
select * from `programming-students-v`;

```

Remarque : la vue affiche maintenant le sat_score.

```
+-----------------+----------------+-----------+
| FullName        | programOfStudy | sat_score |
+-----------------+----------------+-----------+
| Teri Gutierrez  | Programming    |       800 |
| Spencer Pautier | Programming    |      1000 |
| Louis Ramsey    | Programming    |      1200 |
| Alvin Greene    | Programming    |      1200 |
| Sophie Freeman  | Programming    |      1200 |
+-----------------+----------------+-----------+

```

Remarque : la liste des vues n'a pas changé, notre vue est remplacée.

```
mysql>  SHOW FULL TABLES IN fcc_sql_guides_database WHERE TABLE_TYPE LIKE 'VIEW';
+-----------------------------------+------------+
| Tables_in_fcc_sql_guides_database | Table_type |
+-----------------------------------+------------+
| programming-students-v            | VIEW       |
| students-contact-info_v           | VIEW       |
| students_dropme_v                 | VIEW       |
+-----------------------------------+------------+
3 rows in set (0.00 sec)

```

Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à savoir que ce qui est présenté dans ce guide d'introduction. 

J'espère que cela vous donne au moins assez pour commencer. Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options par vous-même.