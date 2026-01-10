---
title: Les meilleurs tutoriels sur les bases de données SQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-24T00:47:00.000Z'
originalURL: https://freecodecamp.org/news/best-sql-database-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f16740569d1a4ca40bd.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Les meilleurs tutoriels sur les bases de données SQL
seo_desc: 'SQL stands for Structured Query Language. It is the most common tool used
  to manipulate and manage data in a relational database (often referred to as a “SQL
  database”).

  SQL is commonly pronounced “sequel.” Its most popular variants are MySQL, Postgr...'
---

SQL signifie Structured Query Language. C'est l'outil le plus courant utilisé pour manipuler et gérer des données dans une base de données relationnelle (souvent appelée « base de données SQL »).

SQL est communément prononcé « sequel ». Ses variantes les plus populaires sont MySQL, PostgreSQL et SQLite - une version de SQL qui est couramment utilisée pour le prototypage. Il a introduit le concept d'accès à de nombreux enregistrements avec une seule commande, en utilisant des requêtes SQL.

Nous recommandons de commencer par le tutoriel de 4 heures sur les bases de données SQL de freeCodeCamp [4 hour SQL database tutorial](https://www.youtube.com/watch?v=HXV3zeQKqGY).

![Image](https://img.youtube.com/vi/HXV3zeQKqGY/maxresdefault.jpg)

Nous recommandons également le [cours CS50 de Harvard sur les bases de données et SQL](https://www.youtube.com/watch?v=TplT4jz1RQ).

Et si vous vous en sentez capable, voici un tutoriel complet de [9 heures sur la conception de bases de données relationnelles](https://www.youtube.com/watch?v=ztHopE5Wnpc) afin que vous puissiez construire votre propre système RDBMS en utilisant SQL.

![Image](https://img.youtube.com/vi/ztHopE5Wnpc/maxresdefault.jpg)

# Quelques instructions et requêtes SQL courantes

## L'instruction SQL Select

### Clauses Select et From

La partie SELECT d'une requête est normalement utilisée pour déterminer quelles colonnes des données doivent être affichées dans les résultats. Il existe également des options que vous pouvez appliquer pour afficher des données qui ne sont pas une colonne de table.

Cet exemple montre trois colonnes sélectionnées dans la table « student » et une colonne calculée. La base de données stocke le studentID, FirstName et LastName de l'étudiant. Nous pouvons combiner les colonnes First et Last name pour créer la colonne FullName calculée.

```sql
select studentID, FirstName, LastName, FirstName + ' ' + LastName as FullName
from student;
```

```text
+-----------+-------------------+------------+------------------------+
| studentID | FirstName         | LastName   | FullName               |
+-----------+-------------------+------------+------------------------+
|         1 | Monique           | Davis      | Monique Davis          |
|         2 | Teri              | Gutierrez  | Teri Gutierrez         |
|         3 | Spencer           | Pautier    | Spencer Pautier        |
|         4 | Louis             | Ramsey     | Louis Ramsey           |
|         5 | Alvin             | Greene     | Alvin Greene           |
|         6 | Sophie            | Freeman    | Sophie Freeman         |
|         7 | Edgar Frank "Ted" | Codd       | Edgar Frank "Ted" Codd |
|         8 | Donald D.         | Chamberlin | Donald D. Chamberlin   |
|         9 | Raymond F.        | Boyce      | Raymond F. Boyce       |
+-----------+-------------------+------------+------------------------+
9 rows in set (0.00 sec)
```

La contrainte CHECK est utilisée pour limiter la plage de valeurs qui peuvent être placées dans une colonne.

Si vous définissez une contrainte CHECK sur une seule colonne, elle permet uniquement certaines valeurs pour cette colonne.

Si vous définissez une contrainte CHECK sur une table, elle peut limiter les valeurs de certaines colonnes en fonction des valeurs d'autres colonnes dans la ligne.

### **SQL CHECK sur CREATE TABLE**

Le SQL suivant crée une contrainte CHECK sur la colonne « Age » lorsque la table « Persons » est créée. La contrainte CHECK garantit que vous ne pouvez pas avoir de personne de moins de 18 ans :

**MySQL :**

```sql
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CHECK (Age>=18)
);
```

**SQL Server / Oracle / MS Access :**

```sql
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int CHECK (Age>=18)
);
```

Pour permettre la nomination d'une contrainte CHECK et pour définir une contrainte CHECK sur plusieurs colonnes, utilisez la syntaxe SQL suivante :

**MySQL / SQL Server / Oracle / MS Access :**

```sql
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    City varchar(255),
    CONSTRAINT CHK_Person CHECK (Age>=18 AND City='Sandnes')
);
```

### **SQL CHECK sur ALTER TABLE**

Pour créer une contrainte CHECK sur la colonne « Age » lorsque la table est déjà créée, utilisez le SQL suivant :

**MySQL / SQL Server / Oracle / MS Access :**

```sql
ALTER TABLE Persons
ADD CHECK (Age>=18);
```

Pour permettre la nomination d'une contrainte CHECK et pour définir une contrainte CHECK sur plusieurs colonnes, utilisez la syntaxe SQL suivante :

**MySQL / SQL Server / Oracle / MS Access :**

```sql
ALTER TABLE Persons
ADD CONSTRAINT CHK_PersonAge CHECK (Age>=18 AND City='Sandnes');
```

### **Supprimer une contrainte CHECK**

Pour supprimer une contrainte CHECK, utilisez le SQL suivant :

**SQL Server / Oracle / MS Access :**

```sql
ALTER TABLE Persons
DROP CONSTRAINT CHK_PersonAge;
```

**MySQL :**

```sql
ALTER TABLE Persons
DROP CHECK CHK_PersonAge; 
```

## **Clause SQL Where**

### **Clause `WHERE` (et/ou, `IN`, `BETWEEN`, et `LIKE`)**

La clause `WHERE` est utilisée pour limiter le nombre de lignes retournées.

Dans ce cas, les cinq conditions suivantes seront utilisées dans une clause `WHERE` quelque peu ridicule.

Voici la liste complète actuelle des étudiants à comparer avec le jeu de résultats de la clause `WHERE` :

```sql
select studentID, FullName, sat_score, rcd_updated from student;
```

```text
+-----------+------------------------+-----------+---------------------+
| studentID | FullName               | sat_score | rcd_updated         |
+-----------+------------------------+-----------+---------------------+
|         1 | Monique Davis          |       400 | 2017-08-16 15:34:50 |
|         2 | Teri Gutierrez         |       800 | 2017-08-16 15:34:50 |
|         3 | Spencer Pautier        |      1000 | 2017-08-16 15:34:50 |
|         4 | Louis Ramsey           |      1200 | 2017-08-16 15:34:50 |
|         5 | Alvin Greene           |      1200 | 2017-08-16 15:34:50 |
|         6 | Sophie Freeman         |      1200 | 2017-08-16 15:34:50 |
|         7 | Edgar Frank "Ted" Codd |      2400 | 2017-08-16 15:35:33 |
|         8 | Donald D. Chamberlin   |      2400 | 2017-08-16 15:35:33 |
|         9 | Raymond F. Boyce       |      2400 | 2017-08-16 15:35:33 |
+-----------+------------------------+-----------+---------------------+
9 rows in set (0.00 sec)
```

Les lignes seront présentées si...

* `WHERE` les identifiants des étudiants sont entre 1 et 5 (inclus)
* `OR` studentID = 8

Voici une requête mise à jour, où tout enregistrement ayant un score SAT dans cette liste (1000, 1400) ne sera pas présenté :

```sql
select  studentID, FullName, sat_score, recordUpdated
from    student
where   (studentID between 1 and 5 or studentID = 8)
        and
        sat_score NOT in (1000, 1400);
```

```text
+-----------+----------------------+-----------+---------------------+
| studentID | FullName             | sat_score | rcd_updated         |
+-----------+----------------------+-----------+---------------------+
|         1 | Monique Davis        |       400 | 2017-08-16 15:34:50 |
|         2 | Teri Gutierrez       |       800 | 2017-08-16 15:34:50 |
|         4 | Louis Ramsey         |      1200 | 2017-08-16 15:34:50 |
|         5 | Alvin Greene         |      1200 | 2017-08-16 15:34:50 |
|         8 | Donald D. Chamberlin |      2400 | 2017-08-16 15:35:33 |
+-----------+----------------------+-----------+---------------------+
5 rows in set (0.00 sec)
```

*Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à elles que ce qui est dans ce guide d'introduction.

J'espère que cela vous donne au moins assez pour commencer.

Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options vous-même.

## **Instruction SQL Update**

Pour mettre à jour un enregistrement dans une table, vous utilisez l'instruction `UPDATE`.

Faites attention. Vous pouvez mettre à jour tous les enregistrements de la table ou seulement quelques-uns. Utilisez la condition `WHERE` pour spécifier quels enregistrements vous souhaitez mettre à jour. Il est possible de mettre à jour une ou plusieurs colonnes à la fois. La syntaxe est :

```sql
UPDATE table_name
SET column1 = value1, 
    column2 = value2, ...
WHERE condition;
```

Voici un exemple de mise à jour du nom de l'enregistrement avec l'identifiant 4 :

```sql
UPDATE Person
SET Name = "Elton John"
WHERE Id = 4;
```

Vous pouvez également mettre à jour des colonnes dans une table en utilisant des valeurs d'autres tables. Utilisez la clause `JOIN` pour obtenir des données de plusieurs tables. La syntaxe est :

```sql
UPDATE table_name1
SET table_name1.column1 = table_name2.columnA
    table_name1.column2 = table_name2.columnB
FROM table_name1
JOIN table_name2 ON table_name1.ForeignKey = table_name2.Key
```

Voici un exemple de mise à jour du Manager de tous les enregistrements :

```sql
UPDATE Person
SET Person.Manager = Department.Manager
FROM Person
JOIN Department ON Person.DepartmentID = Department.ID
```

### **Ce qu'une requête Update peut faire**

Une requête de mise à jour donne à l'administrateur de base de données ou au programmeur utilisant SQL la possibilité de mettre à jour de nombreux enregistrements avec une seule commande.

Conseil de sécurité important ! Ayez toujours une copie de sauvegarde de ce que vous allez modifier AVANT de le modifier !

Cette section va :

* ajouter un nouveau champ à la table des étudiants
* tester la logique pour mettre à jour ce champ avec une adresse e-mail attribuée par l'école
* mettre à jour le nouveau champ.

Voici la table des étudiants au début de ce processus :

```sql
SELECT * FROM student;
```

```text
+-----------+------------------------+-----------+------------------+---------------------+---------------------+
| studentID | FullName               | sat_score | programOfStudy   | rcd_Created         | rcd_Updated         |
+-----------+------------------------+-----------+------------------+---------------------+---------------------+
|         1 | Monique Davis          |       400 | Literature       | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         2 | Teri Gutierrez         |       800 | Programming      | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         3 | Spencer Pautier        |      1000 | Programming      | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         4 | Louis Ramsey           |      1200 | Programming      | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         5 | Alvin Greene           |      1200 | Programming      | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         6 | Sophie Freeman         |      1200 | Programming      | 2017-08-16 15:34:50 | 2017-08-16 15:34:50 |
|         7 | Edgar Frank "Ted" Codd |      2400 | Computer Science | 2017-08-16 15:35:33 | 2017-08-16 15:35:33 |
|         8 | Donald D. Chamberlin   |      2400 | Computer Science | 2017-08-16 15:35:33 | 2017-08-16 15:35:33 |
|         9 | Raymond F. Boyce       |      2400 | Computer Science | 2017-08-16 15:35:33 | 2017-08-16 15:35:33 |
+-----------+------------------------+-----------+------------------+---------------------+---------------------+
9 rows in set (0.00 sec)
```

### **Modifier la table et ajouter un nouveau champ**

```sql
    ALTER TABLE `fcc_sql_guides_database`.`student` 
	ADD COLUMN `schoolEmailAdr` VARCHAR(125) NULL AFTER `programOfStudy`;
```

La table des étudiants après l'exécution de l'alter.

```text
mysql> SELECT FullName, sat_score, programOfStudy, schoolEmailAdr FROM student;
+------------------------+-----------+------------------+----------------+
| FullName               | sat_score | programOfStudy   | schoolEmailAdr |
+------------------------+-----------+------------------+----------------+
| Monique Davis          |       400 | Literature       | NULL           |
| Teri Gutierrez         |       800 | Programming      | NULL           |
| Spencer Pautier        |      1000 | Programming      | NULL           |
| Louis Ramsey           |      1200 | Programming      | NULL           |
| Alvin Greene           |      1200 | Programming      | NULL           |
| Sophie Freeman         |      1200 | Programming      | NULL           |
| Edgar Frank "Ted" Codd |      2400 | Computer Science | NULL           |
| Donald D. Chamberlin   |      2400 | Computer Science | NULL           |
| Raymond F. Boyce       |      2400 | Computer Science | NULL           |
+------------------------+-----------+------------------+----------------+
9 rows in set (0.00 sec)
```

### **TESTER la logique (Étape TRÈS importante !)**

```sql
SELECT FullName, instr(FullName," ") AS firstSpacePosition, 
concat(substring(FullName,1,instr(FullName," ")-1),"@someSchool.edu") AS schoolEmail
FROM student;
```

```text
+------------------------+--------------------+------------------------+
| FullName               | firstSpacePosition | schoolEmail            |
+------------------------+--------------------+------------------------+
| Monique Davis          |                  8 | Monique@someSchool.edu |
| Teri Gutierrez         |                  5 | Teri@someSchool.edu    |
| Spencer Pautier        |                  8 | Spencer@someSchool.edu |
| Louis Ramsey           |                  6 | Louis@someSchool.edu   |
| Alvin Greene           |                  6 | Alvin@someSchool.edu   |
| Sophie Freeman         |                  7 | Sophie@someSchool.edu  |
| Edgar Frank "Ted" Codd |                  6 | Edgar@someSchool.edu   |
| Donald D. Chamberlin   |                  7 | Donald@someSchool.edu  |
| Raymond F. Boyce       |                  8 | Raymond@someSchool.edu |
+------------------------+--------------------+------------------------+
9 rows in set (0.00 sec)
```

_Une note sur concat() : dans MySQL, cette commande est utilisée pour combiner des chaînes, ce n'est pas le cas dans d'autres versions SQL (consultez votre manuel). Dans cette utilisation, elle fonctionne comme suit : La sous-chaîne du champ FullName jusqu'à mais non incluant le premier espace est combinée avec « @someSchool.edu ». Dans le monde réel, cela devrait être beaucoup plus complexe et vous devriez vous assurer que l'adresse e-mail est unique._

### **Effectuer la mise à jour**

Nous allons prétendre que c'est ce que nous voulons et mettre à jour la table avec ces informations :

```sql
UPDATE student SET schoolEmailAdr = concat(substring(FullName,1,instr(FullName," ")-1),"@someSchool.edu")
WHERE schoolEmailAdr is NULL;
```

Succès !

```text
mysql> SELECT FullName, sat_score, programOfStudy, schoolEmailAdr FROM student;
+------------------------+-----------+------------------+------------------------+
| FullName               | sat_score | programOfStudy   | schoolEmailAdr         |
+------------------------+-----------+------------------+------------------------+
| Monique Davis          |       400 | Literature       | Monique@someSchool.edu |
| Teri Gutierrez         |       800 | Programming      | Teri@someSchool.edu    |
| Spencer Pautier        |      1000 | Programming      | Spencer@someSchool.edu |
| Louis Ramsey           |      1200 | Programming      | Louis@someSchool.edu   |
| Alvin Greene           |      1200 | Programming      | Alvin@someSchool.edu   |
| Sophie Freeman         |      1200 | Programming      | Sophie@someSchool.edu  |
| Edgar Frank "Ted" Codd |      2400 | Computer Science | Edgar@someSchool.edu   |
| Donald D. Chamberlin   |      2400 | Computer Science | Donald@someSchool.edu  |
| Raymond F. Boyce       |      2400 | Computer Science | Raymond@someSchool.edu |
+------------------------+-----------+------------------+------------------------+
9 rows in set (0.00 sec)
```