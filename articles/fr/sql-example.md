---
title: Les meilleurs exemples SQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-14T00:29:00.000Z'
originalURL: https://freecodecamp.org/news/sql-example
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/sql-image.jpeg
tags:
- name: SQL
  slug: sql
seo_title: Les meilleurs exemples SQL
seo_desc: 'SQL stands for Structured Query Language. It''s used with all kinds of
  relational databases.

  Basic SQL Syntax Example

  This guide provides a basic, high level description of the syntax for SQL statements.

  SQL is an international standard (ISO), but you...'
---

SQL signifie Structured Query Language. Il est utilisé avec tous types de bases de données relationnelles.

## Exemple de syntaxe SQL de base

Ce guide fournit une description de base et de haut niveau de la syntaxe des instructions SQL.

SQL est une norme internationale (ISO), mais vous trouverez de nombreuses différences entre les implémentations. Ce guide utilise MySQL comme exemple. Si vous utilisez l'un des nombreux autres systèmes de gestion de bases de données relationnelles (SGBDR), vous devrez consulter le manuel de ce SGBDR si nécessaire.

### Ce que nous allons couvrir

* Use (détermine quelle base de données l'instruction utilisera)
* Clauses Select et From
* Clause Where (et / ou, IN, Between, LIKE)
* Order By (ASC, DESC)
* Group by et Having

### Comment utiliser ce guide

Ceci est utilisé pour sélectionner la base de données contenant les tables pour vos instructions SQL :

```sql
use fcc_sql_guides_database; -- sélectionne la base de données d'exemple du guide

```

### Clauses Select et From

La partie Select est normalement utilisée pour déterminer quelles colonnes des données vous souhaitez afficher dans les résultats. Il existe également des options que vous pouvez utiliser pour afficher des données qui ne sont pas une colonne de table.

Cet exemple montre deux colonnes sélectionnées dans la table "student", et deux colonnes calculées. La première des colonnes calculées est un nombre sans signification, et l'autre est la date du système.

```sql
select studentID, FullName, sat_score, recordUpdated, 
3+2 as five, now() as currentDate 
from student;

```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-198.png)

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax01.JPG)

> Clause Where (et / ou, IN, Between et LIKE)

La clause WHERE est utilisée pour limiter le nombre de lignes retournées.

Dans ce cas, les cinq conditions suivantes seront utilisées dans une clause Where quelque peu ridicule.

Comparez ce résultat à l'instruction SQL ci-dessus pour suivre cette logique.

Les lignes présentées seront celles qui :

* Ont des identifiants d'étudiants entre 1 et 5 (inclus)
* ou studentID = 8
* ou ont "Maxmimo" dans le nom

L'exemple suivant est similaire, mais il précise en outre que si l'un des étudiants a certains scores SAT (1000, 1400), ils ne seront pas présentés :

```sql
select studentID, FullName, sat_score, recordUpdated
from student
where
  (
    studentID between 1 and 5
    or studentID = 8
    or FullName like '%Maximo%'
  )
and sat_score NOT in (1000, 1400);

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax02.JPG)

### Order By (ASC, DESC)

Order By nous donne un moyen de trier le jeu de résultats par un ou plusieurs des éléments de la section SELECT. Voici la même liste que ci-dessus, mais triée par le nom complet des étudiants. L'ordre de tri par défaut est ascendant (ASC), mais pour trier dans l'ordre inverse (descendant), vous utilisez DESC, comme dans l'exemple ci-dessous :

```sql
select studentID, FullName, sat_score
from student
where 
  (
    studentID between 1 
    and 5 -- inclus
    or studentID = 8 
    or FullName like '%Maximo%'
  ) 
  and sat_score NOT in (1000, 1400)
order by FullName DESC;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax03.JPG)

### Group By et Having

Group By nous donne un moyen de combiner des lignes et d'agréger des données. La clause Having est similaire à la clause Where ci-dessus, sauf qu'elle agit sur les données regroupées.

Ces données proviennent des données de contributions de campagne que nous avons utilisées dans certains de ces guides.

Cette instruction SQL répond à la question : "quels candidats ont reçu le plus grand nombre de contributions (non pas le montant en $, mais le compte (*)) en 2016, mais seulement ceux qui avaient plus de 80 contributions ?"

Le fait de trier cet ensemble de données dans un ordre décroissant (DESC) place les candidats avec le plus grand nombre de contributions en haut de la liste.

```sql
select Candidate, Election_year, sum(Total_$), count(*)
from combined_party_data
where Election_year = 2016
group by Candidate, Election_year
having count(*) > 80
order by count(*) DESC;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax04.JPG)

*Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à savoir que ce qui est dans ce guide d'introduction. J'espère que cela vous donne au moins assez pour commencer. Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options vous-même.*

## Questions courantes d'entretien SQL

### Qu'est-ce qu'une jointure interne en SQL ?

Il s'agit du type de jointure par défaut si aucune jointure n'est spécifiée. Elle retourne toutes les lignes pour lesquelles il y a au moins une correspondance dans les deux tables.

```sql
SELECT * FROM A x JOIN B y ON y.aId = x.Id

```

### Qu'est-ce qu'une jointure gauche en SQL ?

Une jointure gauche retourne toutes les lignes de la table de gauche, et les lignes correspondantes de la table de droite. Les lignes de la table de gauche seront retournées même s'il n'y avait aucune correspondance dans la table de droite. Les lignes de la table de gauche sans correspondance dans la table de droite auront `null` pour les valeurs de la table de droite.

```sql
SELECT * FROM A x LEFT JOIN B y ON y.aId = x.Id

```

### Qu'est-ce qu'une jointure droite en SQL ?

Une jointure droite retourne toutes les lignes de la table de droite, et les lignes correspondantes de la table de gauche. Opposé à une jointure gauche, cela retournera toutes les lignes de la table de droite même s'il n'y a pas de correspondance dans la table de gauche. Les lignes de la table de droite qui n'ont pas de correspondance dans la table de gauche auront des valeurs `null` pour les colonnes de la table de gauche.

```sql
SELECT * FROM A x RIGHT JOIN B y ON y.aId = x.Id

```

### Qu'est-ce qu'une jointure complète en SQL ?

Une jointure complète retourne toutes les lignes pour lesquelles il y a une correspondance dans l'une ou l'autre des tables. Ainsi, si des lignes de la table de gauche n'ont pas de correspondances dans la table de droite, elles seront incluses. De même, si des lignes de la table de droite n'ont pas de correspondances dans la table de gauche, elles seront incluses.

```sql
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders
ON Customers.CustomerID=Orders.CustomerID
ORDER BY Customers.CustomerName

```

### Quel est le résultat de la commande suivante ?

```sql
DROP VIEW view_name

```

Ici, ce sera une erreur car nous ne pouvons pas effectuer une opération DML sur une vue.

### Peut-on effectuer un rollback après avoir utilisé la commande ALTER ?

Non, car ALTER est une commande DDL et le serveur Oracle effectue un COMMIT automatique lorsque les instructions DDL sont exécutées.

### Quelle est la seule contrainte qui impose des règles au niveau des colonnes ?

NOT NULL est la seule contrainte qui fonctionne au niveau des colonnes.

### Quelles sont les pseudocolonnes en SQL ? Donnez quelques exemples ?

Une pseudocolonne est une fonction qui retourne une valeur générée par le système. La raison pour laquelle elle est connue comme telle est qu'une pseudocolonne est une valeur assignée par Oracle utilisée dans le même contexte qu'une colonne de base de données Oracle mais non stockée sur disque.

```
ROWNUM, ROWID, USER, CURRVAL, NEXTVAL etc.

```

Créez un utilisateur my723acct avec le mot de passe kmd26pt. Utilisez les tablespaces de données utilisateur et temporaires fournis par PO8 et attribuez à cet utilisateur 10 Mo d'espace de stockage dans user_data et 5 Mo d'espace de stockage dans temporary_data.

```sql
CREATE USER my723acct IDENTIFIED BY kmd26pt
DEFAULT TABLESPACE user_data
TEMPORARY TABLESPACE temporary_data
QUOTA 10M on user_data QUOTA 5M on temporary_data

```

### Créez le rôle role_tables_and_views.

```sql
CREATE ROLE role_tables_and_views

```

Accordez au rôle de la question précédente les privilèges de se connecter à la base de données et les privilèges de créer des tables et des vues.

Le privilège de se connecter à la base de données est CREATE SESSION. Le privilège de créer une table est CREATE TABLE. Le privilège de créer une vue est CREATE VIEW.

```sql
GRANT Create session, create table, create view TO role_tables_and_views

```

### Accordez le rôle précédent de la question aux utilisateurs anny et rita

```sql
GRANT role_tables_and_views TO anny, rita

```

Créez un utilisateur my723acct avec le mot de passe kmd26pt. Utilisez les tablespaces de données utilisateur et temporaires fournis par PO8 et attribuez à cet utilisateur 10 Mo d'espace de stockage dans user_data et 5 Mo d'espace de stockage dans temporary_data.

```sql
CREATE USER my723acct IDENTIFIED BY kmd26pt
DEFAULT TABLESPACE user_data
TEMPORARY TABLESPACE temporary_data
QUOTA 10M on user_data QUOTA 5M on temporary_data

```

### Créez le rôle role_tables_and_views.

```sql
CREATE ROLE role_tables_and_views

```

Accordez au rôle de la question précédente les privilèges de se connecter à la base de données et les privilèges de créer des tables et des vues.

Le privilège de se connecter à la base de données est CREATE SESSION. Le privilège de créer une table est CREATE TABLE. Le privilège de créer une vue est CREATE VIEW.

```sql
GRANT Create session, create table, create view TO role_tables_and_views

```

Accordez le rôle précédent de la question aux utilisateurs anny et rita

```sql
GRANT role_tables_and_views TO anny, rita

```

Écrivez une commande pour changer le mot de passe de l'utilisateur rita de abcd à dfgh

```sql
ALTER USER rita IDENTIFIED BY dfgh

```

Les utilisateurs rita et anny n'ont pas de privilèges SELECT sur la table INVENTORY qui a été créée par SCOTT. Écrivez une commande pour permettre à SCOTT d'accorder aux utilisateurs les privilèges SELECT sur ces tables.

```sql
GRANT select ON inventory TO rita, anny

```

L'utilisateur rita a été transféré et n'a plus besoin du privilège qui lui a été accordé par le rôle role_tables_and_views. Écrivez une commande pour lui retirer ses privilèges précédents, sauf qu'elle peut toujours se connecter à la base de données.

```sql
REVOKE select ON scott.inventory FROM rita
REVOKE create table, create view FROM rita

```

L'utilisateur rita, qui a été transféré, part maintenant dans une autre entreprise. Comme les objets qu'elle a créés ne sont plus utiles, écrivez une commande pour supprimer cet utilisateur et tous ses objets.

Ici, l'option CASCADE est nécessaire pour supprimer tous les objets de l'utilisateur dans la base de données.

```sql
DROP USER rita CASCADE

/* L'utilisateur rita a été transféré et n'a plus besoin du privilège
qui lui a été accordé par le rôle role_tables_and_views. Écrivez
e une commande pour lui retirer ses privilèges précédents, sauf qu'
elle peut toujours se connecter à la base de données. */
    
REVOKE select ON scott.inventory FROM rita
REVOKE create table, create view FROM rita

```

L'utilisateur rita, qui a été transféré, part maintenant dans une autre entreprise. Comme les objets qu'elle a créés ne sont plus utiles, écrivez une commande pour supprimer cet utilisateur et tous ses objets.

Ici, l'option CASCADE est nécessaire pour supprimer tous les objets de l'utilisateur dans la base de données.

```sql
DROP USER rita CASCADE

```

### Écrivez une requête SQL pour trouver le n-ième salaire le plus élevé dans une table.

```sql
SELECT TOP 1 Salary
FROM
  (
    SELECT DISTINCT TOP N Salary
    FROM Employee
    ORDER BY Salary DESC
  )
ORDER BY Salary ASC
```

## Instruction SQL Create View

### Qu'est-ce qu'une Vue ?

Une Vue est un objet de base de données qui présente des données existant dans une ou plusieurs tables. Les Vues sont utilisées de manière similaire aux tables, mais elles ne contiennent aucune donnée. Elles "pointent" simplement vers les données qui existent ailleurs (tables ou vues, par exemple).

### Pourquoi les aimons-nous ?

* Les Vues sont un moyen de limiter les données présentées. Par exemple, les données du département des ressources humaines filtrées pour ne présenter que les informations non sensibles. Les informations sensibles dans ce cas pourraient être les numéros de sécurité sociale, le sexe de l'employé, le taux de rémunération, l'adresse domicile, etc.
* Les données complexes provenant de plus d'une table peuvent être combinées en une seule "vue". Cela peut faciliter la vie de vos analystes commerciaux et programmeurs.

### Conseils de sécurité importants

* Les Vues sont gérées par le système. Lorsque les données des tables liées sont modifiées, ajoutées ou mises à jour, la Vue est mise à jour par le système. Nous voulons les utiliser uniquement lorsque cela est nécessaire pour gérer l'utilisation des ressources système.
* Dans MySQL, les modifications de la conception de la table (c'est-à-dire, les nouvelles colonnes ou les colonnes supprimées) effectuées APRÈS la création d'une vue ne sont pas mises à jour dans la vue elle-même. La vue devrait être mise à jour ou recréée.
* Les Vues sont l'un des quatre types standard d'objets de base de données. Les autres sont les tables, les procédures stockées et les fonctions.
* Les Vues peuvent généralement être traitées comme une table, mais les mises à jour sont limitées ou non disponibles lorsque la vue contient plus d'une table.
* Il existe de nombreux autres détails sur les vues qui dépassent le cadre de ce guide d'introduction. Passez du temps avec le manuel de votre gestionnaire de base de données et amusez-vous avec cet objet SQL puissant.

### Syntaxe de l'instruction Create View (MySQL)

```
CREATE
    [OR REPLACE]
    [ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}]
    [DEFINER = { user | CURRENT_USER }]
    [SQL SECURITY { DEFINER | INVOKER }]
    VIEW view_name [(column_list)]
    AS select_statement
	[WITH [CASCADED | LOCAL] CHECK OPTION]

```

_Ce guide couvrira cette partie de l'instruction…_

```sql
CREATE VIEW view_name [(column_list) ] AS select_statement

```

### Exemple de création de Vue à partir des tables étudiantes

Notes :

* Le nom de la vue se termine par un "v". Il est recommandé que le nom de la vue indique qu'il s'agit d'une vue d'une manière ou d'une autre pour faciliter la vie des programmeurs et des administrateurs de bases de données. Votre service informatique devrait avoir ses propres règles de nommage des objets.
* Les colonnes de la vue sont limitées par le SELECT et les lignes de données par la clause WHERE.
* Le caractère "`" autour des noms de vues est requis en raison du "-" dans les noms. MySQL signale une erreur sans eux.

```sql
create view `programming-students-v` as
select FullName, programOfStudy 
from student 
where programOfStudy = 'Programming';

select * from `programming-students-v`;

```

### Exemple d'utilisation d'une Vue pour combiner des données de plus d'une table

Une table de données démographiques des étudiants a été ajoutée à la base de données pour démontrer cette utilisation. Cette vue combinera ces tables.

Notes :

* Pour "joindre" des tables, les tables doivent avoir des champs en commun (généralement des clés primaires) qui identifient de manière unique chaque ligne. Dans ce cas, il s'agit de l'identifiant de l'étudiant. (Plus d'informations à ce sujet dans le guide [SQL Joins](https://guide.freecodecamp.org/sql/sql-joins/index.md).)
* Remarquez l'"alias" donné à chaque table ("s" pour student et "sc" pour student contact). C'est un outil pour raccourcir les noms des tables et faciliter l'identification de la table utilisée. C'est plus facile que de taper de longs noms de tables à plusieurs reprises. Dans cet exemple, cela était requis car studentID est le même nom de colonne dans les deux tables, et le système présenterait une "erreur de nom de colonne ambiguë" sans spécifier quelle table utiliser.

## Guide de l'opérateur SQL Between

L'opérateur BETWEEN est utile en raison de l'optimiseur de requêtes SQL. Bien que BETWEEN soit fonctionnellement identique à : x <= élément <= y, l'optimiseur de requêtes SQL reconnaîtra cette commande plus rapidement et dispose d'un code optimisé pour l'exécuter.

Cet opérateur est utilisé dans une clause WHERE ou dans une clause GROUP BY HAVING.

Les lignes sélectionnées ont une valeur supérieure à la valeur minimale et inférieure à la valeur maximale.

Il est important de garder à l'esprit que les valeurs saisies dans la commande sont **exclues** du résultat. Nous obtenons uniquement ce qui se trouve entre elles.

Voici la syntaxe pour utiliser la fonction dans une clause WHERE :

```sql
select field1, testField
from table1
where testField between min and max

```

Voici un exemple utilisant la table étudiant et la clause WHERE :

```sql
-- pas de clause WHERE
select studentID, FullName, studentID
from student;
    
-- clause WHERE avec between
select studentID, FullName, studentID
from student
where studentID between 2 and 7;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/between01.JPG?raw=true)

Voici un exemple utilisant la table des fonds de campagne et la clause having. Cela retournera les lignes où la somme des dons pour un candidat est comprise entre 3 millions et 18 millions de dollars, en fonction de la clause HAVING dans la partie GROUP BY de l'instruction. Plus d'informations sur l'agrégation dans ce guide.

```sql
select Candidate, Office_Sought, Election_Year, format(sum(Total_$),2)
from combined_party_data
where Election_Year = 2016
group by Candidate, Office_Sought, Election_Year
having sum(Total_$) between 3000000 and 18000000
order by sum(Total_$) desc; 

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/between02.JPG?raw=true)

# Exemple d'instruction SQL Create Table

Une table est un groupe de données stockées dans une base de données.

Pour créer une table dans une base de données, vous utilisez l'instruction `CREATE TABLE`. Vous donnez un nom à la table et une liste de colonnes avec leurs types de données.

```sql
CREATE TABLE TABLENAME(Attribute1 Datatype, Attribute2 Datatype, ...);

```

Voici un exemple de création d'une table nommée Person :

```sql
CREATE TABLE Person(
  Id int not null, 
  Name varchar not null, 
  DateOfBirth date not null, 
  Gender bit not null, 
  PRIMARY KEY(Id)
);

```

Dans l'exemple ci-dessus, chaque Person a un Name, une Date de naissance et un Gender. La colonne Id est la clé qui identifie une personne dans la table. Vous utilisez le mot-clé `PRIMARY KEY` pour configurer une ou plusieurs colonnes comme clé primaire.

Une colonne peut être `not null` ou `null` indiquant si elle est obligatoire ou non.

# Guide de la requête SQL Insert

Les requêtes Insert sont un moyen d'insérer des données dans une table. Supposons que nous avons créé une table en utilisant

```sql
CREATE TABLE example_table (
  name varchar(255), 
  age int
)

```

**example_table**

```
Name|Age
--- | --- 
```

Maintenant, pour ajouter des données à cette table, nous utiliserons **INSERT** de la manière suivante :

`INSERT INTO example_table (column1,column2) VALUES ("Andrew",23)`

```sql
INSERT INTO example_table (column1, column2) 
VALUES ("Andrew", 23)

```

**example_table**

```
Name|Age
--- | --- 
Andrew|23
```

Même ce qui suit fonctionnera, mais il est toujours bon de spécifier quelles données vont dans quelle colonne.

`INSERT INTO table_name VALUES ("John", 28)`

```sql
INSERT INTO table_name 
VALUES ("John", 28)

```

**example_table**

```
Name|Age
--- | --- 
Andrew|23
John|28
```

# Guide de l'opérateur SQL AND

AND est utilisé dans une clause WHERE ou une clause GROUP BY HAVING pour limiter les lignes retournées par l'instruction exécutée. Utilisez AND lorsqu'il est nécessaire d'avoir plus d'une condition remplie.

Nous utiliserons la table étudiant pour présenter des exemples.

Voici la table étudiant sans clause WHERE :

```sql
select * from student;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/and_operator01.JPG?raw=true)

Maintenant, la clause WHERE est ajoutée pour afficher uniquement les étudiants en programmation :

```sql
select * from student 
where programOfStudy = 'Programming';

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/and_operator02.JPG?raw=true)

Maintenant, la clause WHERE est mise à jour avec AND pour montrer les résultats pour les étudiants en programmation qui ont également un score SAT supérieur à 800 :

```sql
select * from student 
where programOfStudy = 'Programming' 
and sat_score > 800;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/and_operator03.JPG?raw=true)

Voici un exemple plus complexe à partir de la table des contributions de campagne. Cet exemple comporte une clause GROUP BY avec une clause HAVING utilisant un AND pour restreindre les enregistrements retournés aux candidats de 2016 avec des contributions comprises entre 3 millions et 18 millions de dollars au total.

```sql
select Candidate, Office_Sought, Election_Year, FORMAT(sum(Total_$),2) from combined_party_data
where Office_Sought = 'PRESIDENT / VICE PRESIDENT'
group by Candidate, Office_Sought, Election_Year
having Election_Year = 2016 and sum(Total_$) between 3000000 and 18000000
order by sum(Total_$) desc;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/and_operator06.JPG?raw=true)

## Comment utiliser le mot-clé SQL Order By

### Order By (ASC, DESC)

ORDER BY nous donne un moyen de TRIER le jeu de résultats par un ou plusieurs des éléments de la section SELECT. Voici un SQL triant les étudiants par FullName dans l'ordre décroissant. L'ordre de tri par défaut est ascendant (ASC), mais pour trier dans l'ordre inverse (descendant), vous utilisez DESC.

```sql
SELECT studentID, FullName, sat_score
FROM student
ORDER BY FullName DESC;

```

```
+-----------+------------------------+-----------+
| studentID | FullName               | sat_score |
+-----------+------------------------+-----------+
|         2 | Teri Gutierrez         |       800 |
|         3 | Spencer Pautier        |      1000 |
|         6 | Sophie Freeman         |      1200 |
|         9 | Raymond F. Boyce       |      2400 |
|         1 | Monique Davis          |       400 |
|         4 | Louis Ramsey           |      1200 |
|         7 | Edgar Frank "Ted" Codd |      2400 |
|         8 | Donald D. Chamberlin   |      2400 |
|         5 | Alvin Greene           |      1200 |
+-----------+------------------------+-----------+
9 rows in set (0.00 sec)

```

_Voici la liste complète des étudiants NON-TRIÉE, actuelle, à comparer avec celle ci-dessus._

```sql
SELECT studentID, FullName, sat_score, rcd_updated FROM student;

```

```
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

Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à savoir que ce qui est dans ce guide d'introduction.

J'espère que cela vous donne au moins assez pour commencer.

Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options vous-même.