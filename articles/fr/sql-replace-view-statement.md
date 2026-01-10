---
title: Instruction SQL Replace View Expliquée avec des Exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-02T00:59:00.000Z'
originalURL: https://freecodecamp.org/news/sql-replace-view-statement
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c57740569d1a4ca318e.jpg
tags:
- name: SQL
  slug: sql
- name: toothbrush
  slug: toothbrush
seo_title: Instruction SQL Replace View Expliquée avec des Exemples
seo_desc: 'Introduction

  A View is a database object that presents data from in one or more tables. The same
  SQL statement used to create a view can also be used to replace an existing view.

  This guide will update (replace) the existing view “programming-student...'
---

## **Introduction**

Une Vue est un objet de base de données qui présente des données provenant d'une ou plusieurs tables. La même instruction SQL utilisée pour créer une vue peut également être utilisée pour remplacer une vue existante.

Ce guide va mettre à jour (remplacer) la vue existante « programming-students-v » par une autre légèrement différente et avec un nom différent.

Conseil de sécurité : faites toujours une sauvegarde du schéma avant d'y apporter des modifications.

### **Syntaxe générale**

```sql
CREATE OR REPLACE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

### **SQL Utilisé pour créer la vue et les données actuelles**

```sql
create view `programming-students-v` as
select FullName, programOfStudy 
from student 
where programOfStudy = 'Programming';
```

```sql
select * from `programming-students-v`;
```

Données actuelles :

```text
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

```sql
SHOW FULL TABLES IN fcc_sql_guides_database WHERE TABLE_TYPE LIKE 'VIEW';
```

```text
+-----------------------------------+------------+
| Tables_in_fcc_sql_guides_database | Table_type |
+-----------------------------------+------------+
| programming-students-v            | VIEW       |
| students-contact-info_v           | VIEW       |
| students_dropme_v                 | VIEW       |
+-----------------------------------+------------+
3 rows in set (0.00 sec)
```

### **Remplacement de la vue**

```sql
create or replace view `programming-students-v` as
select FullName, programOfStudy, sat_score 
from student 
where programOfStudy = 'Programming';    
```

```sql
select * from `programming-students-v`;
```

Remarque : la vue affiche maintenant le sat_score.

```text
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

```text
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

*Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à savoir que ce qui est dans ce guide d'introduction. J'espère que cela vous donne au moins assez pour commencer. Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options vous-même.

## Plus sur SQL View :

* [SQL View expliqué avec des exemples](https://www.freecodecamp.org/news/sql-create-view-mysql/)

## Plus sur les commandes SQL :

* [Cours vidéo complet sur SQL et les bases de données](https://www.freecodecamp.org/news/sql-and-databases-full-course/)
* [Commandes SQL de base que vous devriez connaître](https://www.freecodecamp.org/news/basic-sql-commands/)