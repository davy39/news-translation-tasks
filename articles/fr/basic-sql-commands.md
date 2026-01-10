---
title: Commandes SQL de base - La liste des requêtes et instructions de base de données
  que vous devez connaître
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2020-01-01T22:17:00.000Z'
originalURL: https://freecodecamp.org/news/basic-sql-commands
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e55740569d1a4ca3c8e.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Commandes SQL de base - La liste des requêtes et instructions de base de
  données que vous devez connaître
seo_desc: 'SQL stands for Structured Query Language. SQL commands are the instructions
  used to communicate with a database to perform tasks, functions, and queries with
  data.

  SQL commands can be used to search the database and to do other functions like creatin...'
---

SQL signifie Structured Query Language. Les commandes SQL sont les instructions utilisées pour communiquer avec une base de données afin d'effectuer des tâches, des fonctions et des requêtes avec des données.

Les commandes SQL peuvent être utilisées pour rechercher dans la base de données et pour effectuer d'autres fonctions comme la création de tables, l'ajout de données à des tables, la modification de données et la suppression de tables.

Voici une liste des commandes SQL de base (parfois appelées clauses) que vous devez connaître si vous allez travailler avec SQL.

### **SELECT et FROM**

La partie `SELECT` d'une requête détermine quelles colonnes des données afficher dans les résultats. Il existe également des options que vous pouvez appliquer pour afficher des données qui ne sont pas une colonne de table.

L'exemple ci-dessous montre trois colonnes `SELECT`ionnées `FROM` la table "student" et une colonne calculée. La base de données stocke le studentID, FirstName et LastName de l'étudiant. Nous pouvons combiner les colonnes First et Last name pour créer la colonne FullName calculée.

```sql
SELECT studentID, FirstName, LastName, FirstName + ' ' + LastName AS FullName
FROM student;
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

### **CREATE TABLE**

`CREATE TABLE` fait exactement ce à quoi cela ressemble : cela crée une table dans la base de données. Vous pouvez spécifier le nom de la table et les colonnes qui doivent être dans la table.

```sql
CREATE TABLE table_name (
    column_1 datatype,
    column_2 datatype,
    column_3 datatype
);
```

### ALTER TABLE

[`ALTER TABLE`](https://dev.mysql.com/doc/refman/5.7/en/alter-table.html) modifie la structure d'une table. Voici comment ajouter une colonne à une base de données :

```sql
ALTER TABLE table_name
ADD column_name datatype;
```

### CHECK

La contrainte `CHECK` est utilisée pour limiter la plage de valeurs qui peuvent être placées dans une colonne.

Si vous définissez une contrainte `CHECK` sur une seule colonne, elle permet uniquement certaines valeurs pour cette colonne. Si vous définissez une contrainte `CHECK` sur une table, elle peut limiter les valeurs de certaines colonnes en fonction des valeurs d'autres colonnes dans la ligne.

Le SQL suivant crée une contrainte `CHECK` sur la colonne "Age" lorsque la table "Persons" est créée. La contrainte `CHECK` garantit que vous ne pouvez pas avoir de personne de moins de 18 ans.

```sql
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CHECK (Age>=18)
);
```

Pour permettre la nomination d'une contrainte `CHECK` et pour définir une contrainte `CHECK` sur plusieurs colonnes, utilisez la syntaxe SQL suivante :

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

### WHERE

**(**`AND`, `OR`**, `IN`, `BETWEEN`, et `LIKE`)**

La clause `WHERE` est utilisée pour limiter le nombre de lignes retournées.

Par exemple, nous allons d'abord vous montrer une instruction `SELECT` et les résultats _sans_ instruction `WHERE`. Ensuite, nous ajouterons une instruction `WHERE` qui utilise les cinq qualificateurs ci-dessus.

```sql
SELECT studentID, FullName, sat_score, rcd_updated FROM student;
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

Maintenant, nous allons répéter la requête `SELECT` mais nous allons limiter les lignes retournées en utilisant une instruction `WHERE`.

```sql
SELECT studentID, FullName, sat_score, rcd_updated
FROM student
WHERE (studentID BETWEEN 1 AND 5 OR studentID = 8)
        AND
        sat_score NOT IN (1000, 1400);
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

### UPDATE

Pour mettre à jour un enregistrement dans une table, vous utilisez l'instruction `UPDATE`.

Utilisez la condition `WHERE` pour spécifier les enregistrements que vous souhaitez mettre à jour. Il est possible de mettre à jour une ou plusieurs colonnes à la fois. La syntaxe est :

```sql
UPDATE table_name
SET column1 = value1, 
    column2 = value2, ...
WHERE condition;
```

Voici un exemple de mise à jour du nom de l'enregistrement avec l'Id 4 :

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

### **GROUP BY**

`GROUP BY` vous permet de combiner des lignes et d'agréger des données.

Voici la syntaxe de `GROUP BY` :

```sql
SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name;
```

### HAVING

`HAVING` vous permet de filtrer les données agrégées par la clause `GROUP BY` afin que l'utilisateur obtienne un ensemble limité d'enregistrements à afficher.

Voici la syntaxe de `HAVING` :

```sql
SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name
HAVING COUNT(*) > value;
```

### AVG()

"Average" est utilisé pour calculer la moyenne d'une colonne numérique à partir de l'ensemble de lignes retournées par une instruction SQL.

Voici la syntaxe pour utiliser la fonction :

```sql
SELECT groupingField, AVG(num_field)
FROM table1
GROUP BY groupingField
```

Voici un exemple utilisant la table student :

```sql
SELECT studentID, FullName, AVG(sat_score) 
FROM student 
GROUP BY studentID, FullName;
```

### AS

`AS` vous permet de renommer une colonne ou une table en utilisant un alias.

```sql
SELECT user_only_num1 AS AgeOfServer, (user_only_num1 - warranty_period) AS NonWarrantyPeriod FROM server_table
```

Cela donne un résultat comme ci-dessous.

```text
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

Vous pouvez également utiliser AS pour attribuer un nom à une table afin de faciliter sa référence dans les jointures.

```sql
SELECT ord.product, ord.ord_number, ord.price, cust.cust_name, cust.cust_number FROM customer_table AS cust

JOIN order_table AS ord ON cust.cust_number = ord.cust_number
```

Cela donne un résultat comme ci-dessous.

```text
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

### ORDER BY

`ORDER BY` nous donne un moyen de trier l'ensemble des résultats par un ou plusieurs des éléments de la section `SELECT`. Voici un SQL triant les étudiants par FullName dans l'ordre décroissant. L'ordre de tri par défaut est croissant (`ASC`) mais pour trier dans l'ordre inverse (décroissant), vous utilisez `DESC`.

```sql
SELECT studentID, FullName, sat_score
FROM student
ORDER BY FullName DESC;
```

### COUNT

`COUNT` comptera le nombre de lignes et retournera ce compte comme une colonne dans l'ensemble des résultats.

Voici des exemples de ce pour quoi vous utiliseriez COUNT :

* Compter toutes les lignes d'une table (aucun group by requis)
* Compter les totaux de sous-ensembles de données (nécessite une section Group By de l'instruction)

Cette instruction SQL fournit un compte de toutes les lignes. Notez que vous pouvez donner un nom à la colonne COUNT résultante en utilisant "AS".

```sql
SELECT count(*) AS studentCount FROM student; 
```

### DELETE

`DELETE` est utilisé pour supprimer un enregistrement dans une table.

Faites attention. Vous pouvez supprimer tous les enregistrements de la table ou seulement quelques-uns. Utilisez la condition `WHERE` pour spécifier les enregistrements que vous souhaitez supprimer. La syntaxe est :

```sql
DELETE FROM table_name
WHERE condition;
```

Voici un exemple de suppression de la table Person de l'enregistrement avec Id 3 :

```sql
DELETE FROM Person
WHERE Id = 3;
```

### INNER JOIN

`JOIN`, également appelé Inner Join, sélectionne les enregistrements qui ont des valeurs correspondantes dans deux tables.

```sql
SELECT * FROM A x JOIN B y ON y.aId = x.Id
```

### **LEFT JOIN**

Un `LEFT JOIN` retourne toutes les lignes de la table de gauche et les lignes correspondantes de la table de droite. Les lignes de la table de gauche seront retournées même s'il n'y avait pas de correspondance dans la table de droite. Les lignes de la table de gauche sans correspondance dans la table de droite auront `null` pour les valeurs de la table de droite.

```sql
SELECT * FROM A x LEFT JOIN B y ON y.aId = x.Id
```

### **RIGHT JOIN**

Un `RIGHT JOIN` retourne toutes les lignes de la table de droite et les lignes correspondantes de la table de gauche. Opposé à un left join, cela retournera toutes les lignes de la table de droite même s'il n'y a pas de correspondance dans la table de gauche. Les lignes de la table de droite qui n'ont pas de correspondance dans la table de gauche auront des valeurs `null` pour les colonnes de la table de gauche.

```sql
SELECT * FROM A x RIGHT JOIN B y ON y.aId = x.Id

```

### **FULL OUTER JOIN**

Un `FULL OUTER JOIN` retourne toutes les lignes pour lesquelles il y a une correspondance dans l'une ou l'autre des tables. Ainsi, si des lignes de la table de gauche n'ont pas de correspondances dans la table de droite, celles-ci seront incluses. De même, si des lignes de la table de droite n'ont pas de correspondances dans la table de gauche, celles-ci seront incluses.

```sql
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders
ON Customers.CustomerID=Orders.CustomerID
ORDER BY Customers.CustomerName
```

### INSERT

`INSERT` est un moyen d'insérer des données dans une table.

```sql
INSERT INTO table_name (column_1, column_2, column_3) 
VALUES (value_1, 'value_2', value_3);
```

### LIKE

`LIKE` est utilisé dans une clause `WHERE` ou `HAVING` (dans le cadre du `GROUP BY`) pour limiter les lignes sélectionnées aux éléments lorsqu'une colonne contient un certain motif de caractères.

Ce SQL sélectionnera les étudiants dont le `FullName` commence par "Monique" ou se termine par "Greene".

```sql
SELECT studentID, FullName, sat_score, rcd_updated
FROM student 
WHERE 
    FullName LIKE 'Monique%' OR 
    FullName LIKE '%Greene'; 
```

```text
+-----------+---------------+-----------+---------------------+
| studentID | FullName      | sat_score | rcd_updated         |
+-----------+---------------+-----------+---------------------+
|         1 | Monique Davis |       400 | 2017-08-16 15:34:50 |
|         5 | Alvin Greene  |      1200 | 2017-08-16 15:34:50 |
+-----------+---------------+-----------+---------------------+
2 rows in set (0.00 sec)
```

Vous pouvez placer `NOT` avant `LIKE` pour exclure les lignes avec le motif de chaîne au lieu de les sélectionner. Ce SQL exclut les enregistrements qui contiennent "cer Pau" et "Ted" dans la colonne FullName.

```sql
SELECT studentID, FullName, sat_score, rcd_updated
FROM student 
WHERE FullName NOT LIKE '%cer Pau%' AND FullName NOT LIKE '%"Ted"%';
```

```text
+-----------+----------------------+-----------+---------------------+
| studentID | FullName             | sat_score | rcd_updated         |
+-----------+----------------------+-----------+---------------------+
|         1 | Monique Davis        |       400 | 2017-08-16 15:34:50 |
|         2 | Teri Gutierrez       |       800 | 2017-08-16 15:34:50 |
|         4 | Louis Ramsey         |      1200 | 2017-08-16 15:34:50 |
|         5 | Alvin Greene         |      1200 | 2017-08-16 15:34:50 |
|         6 | Sophie Freeman       |      1200 | 2017-08-16 15:34:50 |
|         8 | Donald D. Chamberlin |      2400 | 2017-08-16 15:35:33 |
|         9 | Raymond F. Boyce     |      2400 | 2017-08-16 15:35:33 |
+-----------+----------------------+-----------+---------------------+
7 rows in set (0.00 sec)
```