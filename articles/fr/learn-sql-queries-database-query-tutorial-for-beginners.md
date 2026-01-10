---
title: Apprendre les requêtes SQL – Tutoriel sur les requêtes de base de données pour
  débutants
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-08-10T00:05:46.000Z'
originalURL: https://freecodecamp.org/news/learn-sql-queries-database-query-tutorial-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/jan-antonin-kolar-lRoX0shwjUQ-unsplash--1-.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Apprendre les requêtes SQL – Tutoriel sur les requêtes de base de données
  pour débutants
seo_desc: 'SQL stands for Structured Query Language and is a language that you use
  to manage data in databases. SQL consists of commands and declarative statements
  that act as instructions to the database so it can perform tasks.

  You can use SQL commands to cre...'
---

SQL signifie Structured Query Language et est un langage que vous utilisez pour gérer les données dans les bases de données. SQL se compose de commandes et d'instructions déclaratives qui agissent comme des instructions pour la base de données afin qu'elle puisse effectuer des tâches.

Vous pouvez utiliser des commandes SQL pour créer une table dans une base de données, ajouter et apporter des modifications à de grandes quantités de données, rechercher des informations spécifiques rapidement, ou supprimer une table entièrement.

Dans cet article, nous examinerons certaines des commandes SQL les plus courantes pour les débutants et comment vous pouvez les utiliser pour interroger efficacement une base de données – c'est-à-dire faire une demande d'informations spécifiques.

## La structure de base d'une base de données

Avant de commencer, vous devez comprendre la hiérarchie d'une base de données.

Une base de données SQL est une collection d'informations liées stockées dans des tables. Chaque table a des colonnes qui décrivent les données qu'elles contiennent, et des lignes qui contiennent les données réelles. Un champ est une seule pièce de données dans une ligne. Donc, pour récupérer les données souhaitées, nous devons être spécifiques.

Par exemple, une entreprise à distance peut avoir plusieurs bases de données. Pour voir une liste complète de leurs bases de données, nous pouvons taper `SHOW DATABASES;` et nous pouvons nous concentrer sur la base de données `Employees`.

La sortie ressemblera à quelque chose comme ceci :

```
+--------------------+
|     Databases      |
+--------------------+
| mysql              |
| information_schema |
| employees          |
| test               |
| sys                |
+--------------------+
```

Une seule base de données peut avoir plusieurs tables. En prenant l'exemple ci-dessus, pour voir les différentes tables dans la base de données `employees`, nous pouvons faire `SHOW TABLES in employees;`. Les tables peuvent être `Engineering`, `Product`, `Marketing`, et `Sales` pour les différentes équipes de l'entreprise.

```
+----------------------+
| Tables_in_employees  |
+----------------------+
| engineering          |
| product              |
| marketing            |
| sales                |
+----------------------+
```

Toutes les tables se composent ensuite de différentes colonnes qui décrivent les données.

Pour voir les différentes colonnes, utilisez `Describe Engineering;`. Par exemple, la table Engineering peut avoir des colonnes qui définissent un seul attribut comme `employee_id`, `first_name`, `last_name`, `email`, `country`, et `salary`.

Voici la sortie :

```
+-----------+-------------------+--------------+
| Name      |         Null      |      Type    |  
+-----------+-------------------+--------------+
|EMPLOYEE_ID| NOT NULL          | INT(6)       |  
|FIRST_NAME | NOT NULL          |VARCHAR2(20)  |
|LAST_NAME  | NOT NULL          |VARCHAR2(25)  | 
|EMAIL      | NOT NULL          |VARCHAR2(255) |
|COUNTRY    | NOT NULL          |VARCHAR2(30)  |
|SALARY     | NOT NULL          |DECIMAL(10,2) |
+-----------+-------------------+--------------+
```

Les tables se composent également de lignes, qui sont des entrées individuelles dans la table. Par exemple, une ligne inclurait des entrées sous `employee_id`, `first_name`, `last_name`, `email`, `salary`, et `country`. Ces lignes définiraient et fourniraient des informations sur une personne de l'équipe Engineering.

## Requêtes SQL de base

Toutes les opérations que vous pouvez effectuer avec des données suivent l'acronyme CRUD.

CRUD signifie les 4 principales opérations que nous effectuons lorsque nous interrogeons une base de données : Create, Read, Update, et Delete.

Nous `CRÉONS` des informations dans la base de données, nous `LISONS`/Récupérons ces informations de la base de données, nous les `METTONS À JOUR`/manipulons, et si nous le souhaitons, nous pouvons les `SUPPRIMER`.

Ci-dessous, nous examinerons quelques requêtes SQL de base ainsi que leur syntaxe pour commencer.

### Instruction SQL `CREATE DATABASE`

Pour créer une base de données nommée `engineering`, nous pouvons utiliser le code suivant :

```sql
CREATE DATABASE engineering;
```

### Instruction SQL `CREATE TABLE`

```SQL
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype
);
```

Cette requête crée une nouvelle table dans la base de données.

Elle donne un nom à la table, et les différentes colonnes que nous voulons que notre table ait sont également passées.

Il existe une variété de types de données que nous pouvons utiliser. Certains des plus courants sont : `INT`, `DECIMAL`, `DATETIME`, `VARCHAR`, `NVARCHAR`, `FLOAT`, et `BIT`.

À partir de notre exemple ci-dessus, cela pourrait ressembler au code suivant :

```sql
CREATE TABLE engineering (
employee_id  int(6) NOT NULL,
first_name   varchar(20) NOT NULL,
last_name  varchar(25) NOT NULL,
email  varchar(255) NOT NULL,
country varchar(30),
salary  decimal(10,2) NOT NULL
);
```

La table que nous créons à partir de ces données ressemblerait à quelque chose comme ceci :

|employee_id | first_name | last_name | email |country |salary |
| ---         | :--        | --:       | :-:   |:-:   | :-:   |
|​ |


### Instruction SQL `ALTER TABLE`

Après avoir créé la table, nous pouvons la modifier en ajoutant une autre colonne.

```sql
ALTER TABLE table_name 
ADD column_name datatype;
```

Par exemple, si nous le souhaitons, nous pourrions ajouter une colonne `birthday` à notre table existante en tapant :

```sql
ALTER TABLE engineering
ADD  birthday date;
```

Maintenant, notre table ressemblerait à ceci :

|employee_id | first_name | last_name | email |country |salary |birthday |
| ---         | :--        | --:       | :-:   |:-:   | :-:   |:-:   |
|​ |


### Instruction SQL `INSERT`

C'est ainsi que nous insérons des données dans les tables et créons de nouvelles lignes. C'est la partie `C` de CRUD.

```sql
INSERT INTO table_name(column1, column2, column3,..) 
VALUES(value1, 'value2', value3,..);
```

Dans la partie `INSERT INTO`, nous pouvons spécifier les colonnes que nous voulons remplir avec des informations.

À l'intérieur de `VALUES` se trouvent les informations que nous voulons stocker. Cela crée un nouvel enregistrement dans la table qui est une nouvelle ligne.

Chaque fois que nous insérons des valeurs de chaîne, elles sont enfermées dans des guillemets simples, `''`.


Par exemple :

```sql
INSERT INTO table_name(employee_id,first_name,last_name,email,country,salary) 
VALUES
(1,'Timmy','Jones','timmy@gmail.com','USA',2500.00);
(2,'Kelly','Smith','ksmith@gmail.com','UK',1300.00);
```

La table ressemblerait maintenant à ceci :

|employee_id | first_name | last_name | email |country |salary |
| ---        | :--        | --:       | :-:   |:-:   | :-:   |
|1           |Timmy       |Jones       |timmy@gmail.com|USA|2500.00
|2           |Kelly      |Smith       |ksmith@gmail.com|UK|1300.00


### Instruction SQL `SELECT`

Cette instruction récupère des données de la base de données. C'est la partie `R` de CRUD.

```sql
SELECT  column1,column2
FROM    table_name;
```

À partir de notre exemple précédent, cela ressemblerait à ce qui suit :

```sql
SELECT first_name,last_name
FROM   engineering;
```

Sortie :

```
+-----------+----------+
|FirstName  | LastName |
+-----------+----------+
| Timmy     | Jones    |
| Kelly     | Smith    |
+-----------+----------+
```


L'instruction `SELECT` pointe vers la colonne spécifique dont nous voulons récupérer les données à afficher dans les résultats.

La partie `FROM` détermine la table elle-même.

Voici un autre exemple de `SELECT` :

```sql
SELECT * FROM table_name;
```

L'astérisque `*` récupérera toutes les informations de la table que nous spécifions.

### Instruction SQL `WHERE`

`WHERE` nous permet d'être plus spécifiques avec nos requêtes.

Si nous voulions filtrer notre table `Engineering` pour rechercher des employés ayant un salaire spécifique, nous utiliserions `WHERE`.

```sql
SELECT employee_id,first_name,last_name,email,country
FROM engineering
WHERE salary > 1500
```

La table de l'exemple précédent :

|employee_id | first_name | last_name | email |country |salary |
| ---        | :--        | --:       | :-:   |:-:   | :-:   |
|1           |Timmy       |Jones       |timmy@gmail.com|USA|2500.00
|2           |Kelly      |Smith       |ksmith@gmail.com|UK|1300.00


Aurait maintenant la sortie suivante :

```
+-----------+----------+----------+----------------+------------+
|employee_id|first_name|last_name |email           |country     |
+-----------+----------+----------+----------------+------------+
|          1| Timmy    |Jones     |timmy@gmail.com | USA        |
+-----------+----------+----------+----------------+------------+
```


Cela filtre et affiche les résultats qui satisfont la condition – c'est-à-dire qu'il affiche *uniquement* les lignes des personnes dont le salaire est « supérieur à 1500 ».

### Opérateurs SQL `AND`, `OR`, et `BETWEEN`

Ces opérateurs vous permettent de rendre la requête encore plus spécifique en ajoutant plus de critères à l'instruction `WHERE`.

L'opérateur `AND` prend deux conditions et elles doivent toutes deux être `vraies` pour que la ligne soit affichée dans le résultat.

```sql
SELECT column_name
FROM table_name
WHERE column1 =value1
    AND column2 = value2;
```

L'opérateur `OR` prend deux conditions, et l'une ou l'autre doit être vraie pour que la ligne soit affichée dans le résultat.

```sql
SELECT column_name
FROM table_name
WHERE column_name = value1
    OR column_name = value2;
```

L'opérateur `BETWEEN` filtre dans une plage spécifique de nombres ou de texte.

```sql
SELECT column1,column2
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

Nous pouvons également utiliser ces opérateurs en combinaison les uns avec les autres.

Supposons que notre table ressemble maintenant à ceci :

|employee_id | first_name | last_name | email |country |salary |
| ---        | :--        | --:       | :-:   |:-:   | :-:   |
|1           |Timmy       |Jones       |timmy@gmail.com|USA|2500.00
|2           |Kelly       |Smith       |ksmith@gmail.com|UK|1300.00
|3           |Jim         |White       |jwhite@gmail.com|UK|1200.76
|4           |José Luis   |Martínez    |jmart@gmail.com|Mexico| 1275.87
|5           |Emilia      |Fischer     |emfis@gmail.com | Germany| 2365.90
|6           |Delphine    |Lavigne     |lavigned@gmail.com| France| 2108.00
|7           |Louis      |Meyer     |lmey@gmail.com | Germany| 2145.70

Si nous utilisions une instruction comme celle ci-dessous :

```sql
SELECT * FROM engineering
WHERE  employee_id BETWEEN 3 AND 7
        AND 
        country = 'Germany';
```

Nous obtiendrions cette sortie :

```
+------------+-----------+-----------+----------------+--------+--------+
|employee_id | first_name| last_name | email          |country |salary  |
+------------+-----------+-----------+----------------+--------+--------+
|5           |Emilia     |Fischer    |emfis@gmail.com | Germany| 2365.90|
|7           |Louis      |Meyer      |lmey@gmail.com  | Germany| 2145.70|
+------------+-----------+-----------+----------------+--------+--------+
```

Cela sélectionne *toutes* les colonnes qui ont un `employee_id` entre `3 et 7` `ET` ont un pays d'Allemagne.


### Instruction SQL `ORDER BY`

`ORDER BY` trie par les colonnes que nous avons mentionnées dans l'instruction `SELECT`.

Il trie les résultats et les présente dans l'ordre alphabétique ou numérique décroissant ou croissant (l'ordre par défaut étant croissant).

Nous pouvons spécifier cela avec la commande : `ORDER BY column_name DESC | ASC`.

```sql
SELECT employee_id, first_name, last_name,salary
FROM engineering
ORDER BY salary DESC;
```

Dans l'exemple ci-dessus, nous trions les salaires des employés de l'équipe engineering et les présentons dans l'ordre numérique décroissant.


### Instruction SQL `GROUP BY`

`GROUP BY` nous permet de combiner des lignes avec des données identiques et des similitudes.

C'est utile pour organiser les données en double et les entrées qui apparaissent plusieurs fois dans la table.

```sql
SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name;
```

Ici, `COUNT(*)` compte chaque ligne séparément et retourne le nombre de lignes dans la table spécifiée tout en préservant les lignes en double.

### Instruction SQL `LIMIT`

`LIMIT` vous permet de spécifier le nombre *maximum* de lignes qui doivent être retournées dans les résultats.

C'est utile lorsque vous travaillez avec un grand ensemble de données qui peut faire que les requêtes prennent beaucoup de temps à s'exécuter. En limitant les résultats que vous obtenez, cela peut vous faire gagner du temps.

```sql
SELECT column1,column2
FROM table_name
LIMIT number;
```


### Instruction SQL `UPDATE`

C'est ainsi que nous mettons à jour une ligne dans une table. C'est la partie `U` de CRUD.

```sql
UPDATE table_name 
SET column1 = value1, 
    column2 = value2 
WHERE condition;
```

La condition `WHERE` spécifie l'enregistrement que vous souhaitez modifier.

```sql
UPDATE engineering
SET    country = 'Spain'
WHERE   employee_id = 1
```

Notre table d'avant :

|employee_id | first_name | last_name | email |country |salary |
| ---        | :--        | --:       | :-:   |:-:   | :-:   |
|1           |Timmy       |Jones       |timmy@gmail.com|USA|2500.00
|2           |Kelly       |Smith       |ksmith@gmail.com|UK|1300.00
|3           |Jim         |White       |jwhite@gmail.com|UK|1200.76
|4           |José Luis   |Martínez    |jmart@gmail.com|Mexico| 1275.87
|5           |Emilia      |Fischer     |emfis@gmail.com | Germany| 2365.90
|6           |Delphine    |Lavigne     |lavigned@gmail.com| France| 2108.00
|7           |Louis      |Meyer     |lmey@gmail.com | Germany| 2145.70

Ressemblerait maintenant à ceci :

|employee_id | first_name | last_name | email |country |salary |
| ---        | :--        | --:       | :-:   |:-:   | :-:   |
|1           |Timmy       |Jones       |timmy@gmail.com|Spain|2500.00
|2           |Kelly       |Smith       |ksmith@gmail.com|UK|1300.00
|3           |Jim         |White       |jwhite@gmail.com|UK|1200.76
|4           |José Luis   |Martínez    |jmart@gmail.com|Mexico| 1275.87
|5           |Emilia      |Fischer     |emfis@gmail.com | Germany| 2365.90
|6           |Delphine    |Lavigne     |lavigned@gmail.com| France| 2108.00
|7           |Louis      |Meyer     |lmey@gmail.com | Germany| 2145.70


Cela met à jour la colonne du pays de résidence d'un employé avec un id de 1.

Nous pouvons également mettre à jour des informations dans une table avec des valeurs d'une autre table avec `JOIN`.

```sql
UPDATE table_name
SET table_name1.column_name1 = table_name2.column_name1
    table_name1.column_name2 = table_name2.column2
FROM table_name1
JOIN table_name2 
    ON table_name1.column_name = table_2.column_name;
```

  
### Instruction SQL `DELETE`

`DELETE` est la partie `D` de CRUD. C'est ainsi que nous supprimons un enregistrement d'une table.

La syntaxe de base ressemble à ceci :

```sql
DELETE FROM table_name 
WHERE condition;
```

Par exemple, dans notre exemple `engineering`, cela pourrait ressembler à ceci :

```sql
DELETE FROM engineering
WHERE employee_id = 2;
```

Cela supprime l'enregistrement d'un employé dans l'équipe engineering avec un id de 2.

### Instruction SQL `DROP COLUMN`

Pour supprimer une colonne spécifique de la table, nous ferions ceci :

```sql
ALTER TABLE table_name 
DROP COLUMN column_name;
```


### Instruction SQL `DROP TABLE`

Pour supprimer toute la table, nous pouvons faire ceci :

```sql
DROP TABLE table_name;
```

## Conclusion

Dans cet article, nous avons passé en revue certaines des requêtes de base que vous utiliserez en tant que débutant en SQL.

Nous avons appris à créer des tables et des lignes, à collecter et mettre à jour des informations, et enfin à supprimer des données. Nous avons également mappé les requêtes SQL à leurs actions CRUD correspondantes.

Merci d'avoir lu et bon codage !