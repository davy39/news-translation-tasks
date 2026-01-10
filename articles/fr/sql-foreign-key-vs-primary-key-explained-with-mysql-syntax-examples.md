---
title: Clé étrangère SQL VS Clé primaire expliquée avec des exemples de syntaxe MySQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-26T19:49:00.000Z'
originalURL: https://freecodecamp.org/news/sql-foreign-key-vs-primary-key-explained-with-mysql-syntax-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e78740569d1a4ca3d46.jpg
tags:
- name: SQL
  slug: sql
seo_title: Clé étrangère SQL VS Clé primaire expliquée avec des exemples de syntaxe
  MySQL
seo_desc: A Foreign Key is a key used to link two tables. The table with the Foreign
  Key Constraint (aka “child table”) is connected to another table (aka, the “parent
  table”). The connection is between the child table’s Foreign Key Constraint and
  the parent t...
---

Une clé étrangère est une clé utilisée pour lier deux tables. La table avec la contrainte de clé étrangère (aka « table enfant ») est connectée à une autre table (aka, la « table parente »). La connexion est entre la contrainte de clé étrangère de la table enfant et la clé primaire de la table parente.

Les contraintes de clé étrangère sont utilisées pour aider à maintenir la cohérence entre les tables. Par exemple, si un enregistrement de la table parente est supprimé et que la table enfant contient des enregistrements, le système pourrait également supprimer les enregistrements enfants.

Elles aident également à prévenir l'entrée de données inexactes dans la table enfant en exigeant qu'un enregistrement de la table parente existe pour chaque enregistrement qui est entré dans la table enfant.

### Exemple d'utilisation

Pour ce guide, nous allons examiner de plus près les tables student (parente) et student contact (enfant).

### La clé primaire de la table parente

Notez que la table student a une clé primaire d'une colonne, studentID.

```
SHOW index FROM student;

```

```
+---------+------------+----------+--------------+-------------+
| Table   | Non_unique | Key_name | Seq_in_index | Column_name |
+---------+------------+----------+--------------+-------------+
| student |          0 | PRIMARY  |            1 | studentID   |
+---------+------------+----------+--------------+-------------+
1 row in set (0.00 sec) (certaines colonnes supprimées à droite pour plus de clarté)

```

### Les clés primaires et étrangères de la table enfant

La table d'informations de contact des étudiants a une clé primaire qui est également studentID. Cela est dû à une relation un-à-un entre les deux tables. En d'autres termes, nous attendons un seul étudiant et un seul enregistrement de contact d'étudiant par étudiant.

```
SHOW index FROM `student-contact-info`;

```

```
+----------------------+------------+----------+--------------+-------------+
| Table                | Non_unique | Key_name | Seq_in_index | Column_name |
+----------------------+------------+----------+--------------+-------------+
| student-contact-info |          0 | PRIMARY  |            1 | studentID   |
+----------------------+------------+----------+--------------+-------------+
1 row in set (0.00 sec) (certaines colonnes supprimées à droite pour plus de clarté)

```

```
SELECT concat(table_name, '.', column_name) AS 'foreign key',
concat(referenced_table_name, '.', referenced_column_name) AS 'references'
FROM information_schema.key_column_usage
WHERE referenced_table_name IS NOT NULL
AND table_schema = 'fcc_sql_guides_database' 
AND table_name = 'student-contact-info';

```

```
+--------------------------------+-------------------+
| foreign key                    | references        |
+--------------------------------+-------------------+
| student-contact-info.studentID | student.studentID |
+--------------------------------+-------------------+
1 row in set (0.00 sec)

```

### Exemple de rapport utilisant la table parente student et la table enfant contact

```
SELECT a.studentID, a.FullName, a.programOfStudy,
b.`student-phone-cell`, b.`student-US-zipcode`
FROM student AS a
JOIN `student-contact-info` AS b ON a.studentID = b.studentID;

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
+-----------+------------------------+------------------+--------------------+--------------------+

```

### Conclusion

Les contraintes de clé étrangère sont un excellent outil d'intégrité des données. Prenez le temps de bien les apprendre.

Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à elles que ce qui est dans ce guide d'introduction.

J'espère que cela vous donne au moins assez pour commencer.

Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options vous-même.