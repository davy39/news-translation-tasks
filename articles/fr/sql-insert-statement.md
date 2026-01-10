---
title: Instruction SQL INSERT – Comment insérer des données dans une table en SQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-01T18:54:21.000Z'
originalURL: https://freecodecamp.org/news/sql-insert-statement
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/SQL-Insert-Statement.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Instruction SQL INSERT – Comment insérer des données dans une table en
  SQL
seo_desc: 'By Karlgusta Annoh

  In this tutorial, you''ll learn how to use the SQL INSERT statement.

  We''ll discuss the syntax of INSERT, and then we''ll use an example to show all
  the different ways you can use INSERT. We''ll also combine it with other helpful
  claus...'
---

Par Karlgusta Annoh

Dans ce tutoriel, vous apprendrez à utiliser l'instruction SQL INSERT.

Nous discuterons de la syntaxe de INSERT, puis nous utiliserons un exemple pour montrer toutes les différentes façons dont vous pouvez utiliser INSERT. Nous le combinerons également avec d'autres clauses utiles pour effectuer des opérations plus complexes.

## Prérequis
* Compréhension de base de SQL

## Syntaxe de l'instruction SQL `INSERT`

Vous utilisez l'instruction SQL INSERT INTO pour insérer de nouveaux enregistrements dans une table. La syntaxe de l'instruction SQL INSERT INTO est :

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

## Exemple de SQL `INSERT`

Supposons que nous avons une table appelée `Persons` avec les colonnes suivantes :

* `PersonID`
* `LastName`
* `FirstName`
* `Address`
* `City`

Commençons par créer la table :

![Créer une table en SQL](https://user-images.githubusercontent.com/33565767/204135303-4ce17e6e-9ed9-4083-80e7-32a644cbacd9.png 'Créer une table en SQL')

J'utilise cette requête pour créer la table :

```sql
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
```

En exécutant la requête, la table sera créée.

![Table vide que nous avons créée](https://user-images.githubusercontent.com/33565767/204135389-e4c47686-0232-4d7b-89cd-d94a10a9b7af.png 'Table vide que nous avons créée')


Nous pouvons insérer un nouvel enregistrement dans la table `Persons` en utilisant l'instruction SQL suivante :

```sql
INSERT INTO Persons (PersonID, LastName, FirstName, Address, City) 
VALUES (1, 'Wilson', 'John', '123 Main St.', 'Anytown');
```

![Insertion de données dans la table persons](https://user-images.githubusercontent.com/33565767/204135468-a58b036f-eb22-4da0-9fb8-a42a2ffd31b2.png 'Insertion de données dans la table persons')

Voici la table avec les données insérées :

![Table après insertion des données](https://user-images.githubusercontent.com/33565767/204135554-ffab65c8-5c0b-465c-a5b4-c1913a343eb1.png 'Table après insertion des données')

## Comment insérer plusieurs enregistrements avec l'instruction `INSERT`

Nous pouvons insérer plusieurs enregistrements dans une table en utilisant une seule instruction SQL. L'instruction SQL suivante insère trois nouveaux enregistrements dans la table `Persons` :

```sql
INSERT INTO Persons (PersonID, LastName, FirstName, Address, City)
VALUES (1, 'Wilson', 'John', '123 Main St.', 'Anytown'),
       (2, 'Smith', 'Mary', '456 Maple St.', 'Anytown'),
       (3, 'Jones', 'David', '789 Elm St.', 'Anytown'),
       (4, 'John', 'David', '789 Elm St.', 'Meru');
```

Lors de l'exécution de la requête sur TablePlus, cela ressemblera à ceci :

![Insérer plusieurs enregistrements](https://user-images.githubusercontent.com/33565767/204137155-1b131742-5765-46e6-8f34-44dd9accd55d.png 'Insérer plusieurs enregistrements')

Voici la table avec les données insérées :

![La table avec les enregistrements insérés](https://user-images.githubusercontent.com/33565767/204135891-0868ec8d-6278-43b3-95e2-f143be29b919.png 'La table avec les enregistrements insérés')


## Comment insérer des enregistrements à partir d'une autre table

Nous pouvons insérer des enregistrements dans une table à partir d'une autre table en utilisant l'instruction SQL INSERT INTO SELECT.

L'instruction SQL suivante insère tous les enregistrements de la table `Persons` dans la table `PersonsBackup` :

```sql
INSERT INTO PersonsBackup
SELECT * FROM Persons;
```

Pour exécuter cette requête, nous devons créer une nouvelle table appelée `PersonsBackup` :

```sql
CREATE TABLE PersonsBackup (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255),
    PRIMARY KEY (PersonID)
);
```

![Créer la table PersonsBackup](https://user-images.githubusercontent.com/33565767/204136076-03bc5e9b-dc54-4e07-92b5-16ed695f6d58.png 'Créer la table PersonsBackup')

Maintenant, nous pouvons exécuter la requête pour insérer les enregistrements de la table `Persons` dans la table `PersonsBackup` :

```sql
INSERT INTO PersonsBackup
SELECT * FROM Persons;
```

![Insertion dans PersonsBackup à partir de la table Persons](https://user-images.githubusercontent.com/33565767/204136180-97a0266a-c753-4f68-8f62-c418906a487a.png 'Insertion dans PersonsBackup à partir de la table Persons')

Voici la table avec les données insérées :

![Enregistrements insérés dans PersonsBackup à partir de la table Persons](https://user-images.githubusercontent.com/33565767/204136259-7abff786-659a-4b78-9077-2d3462496dcd.png 'Enregistrements insérés dans PersonsBackup à partir de la table Persons')


## Comment insérer des enregistrements à partir d'une instruction SELECT

Nous pouvons insérer des enregistrements à partir d'une instruction SELECT dans une table en utilisant l'instruction SQL INSERT INTO SELECT. L'instruction SQL suivante insère tous les enregistrements de la table `Persons` dans la table `PersonsBackup` :

```sql
INSERT INTO PersonsBackup
SELECT * FROM Persons;
```

![Insertion dans PersonsBackup à partir de la table Persons](https://user-images.githubusercontent.com/33565767/204136180-97a0266a-c753-4f68-8f62-c418906a487a.png 'Insertion dans PersonsBackup à partir de la table Persons')

Voici la table avec les données insérées :

![Enregistrements insérés dans PersonsBackup à partir de la table Persons](https://user-images.githubusercontent.com/33565767/204136259-7abff786-659a-4b78-9077-2d3462496dcd.png 'Enregistrements insérés dans PersonsBackup à partir de la table Persons')

## Comment insérer des enregistrements à partir d'une instruction SELECT avec une clause WHERE

Nous pouvons insérer des enregistrements dans une table à partir d'une instruction SELECT avec une clause WHERE en utilisant l'instruction SQL INSERT INTO SELECT.

L'instruction SQL suivante insère tous les enregistrements de la table `Persons` dans la table `PersonsBackup` où la `City` est `Anytown` :

Commençons par supprimer les enregistrements de la table `PersonsBackup` :

```sql
DELETE FROM PersonsBackup;
```

![Suppression des enregistrements de PersonsBackup](https://user-images.githubusercontent.com/33565767/204136584-667bcd37-f9b6-4103-a0a8-e140b11bd11a.png 'Suppression des enregistrements de PersonsBackup')

Maintenant que les enregistrements ont été supprimés, nous pouvons insérer les enregistrements de la table `Persons` dans la table `PersonsBackup` où la `City` est `Anytown` :

```sql
INSERT INTO PersonsBackup
SELECT * FROM Persons WHERE City = 'Anytown';
```

Insertion des enregistrements de la table `Persons` dans la table `PersonsBackup` où la `City` est `Anytown` :

![Enregistrement inséré de la table Persons dans la table PersonsBackup où la City est Anytown](https://user-images.githubusercontent.com/33565767/204136655-7a104a0b-088a-4b15-8c39-0f735d706a67.png 'Enregistrement inséré de la table Persons dans la table PersonsBackup où la City est Anytown')


Voici la table avec les données insérées :

![Table où les données ont été insérées](https://user-images.githubusercontent.com/33565767/204136695-b7bad680-5620-4558-8846-94b057ddb14d.png 'Table où les données ont été insérées')


## Comment insérer des enregistrements à partir d'une instruction SELECT avec une clause WHERE et une clause LIMIT

Nous pouvons insérer des enregistrements dans une table à partir d'une instruction SELECT avec une clause WHERE et une clause LIMIT en utilisant l'instruction SQL INSERT INTO SELECT.

L'instruction SQL suivante insère les 10 premiers enregistrements de la table `Persons` dans la table `PersonsBackup` où la `City` est `Anytown` :

Commençons par créer au moins 10 enregistrements dans la table `Persons` où la `City` est `Anytown` :

```sql
INSERT INTO Persons(PersonID, LastName, FirstName, Address, City) 
VALUES (5, 'Wilson', 'John', '123 Main St.', 'Anytown'),
       (6, 'Smith', 'Mary', '456 Maple St.', 'Anytown'),
       (7, 'Jones', 'David', '789 Elm St.', 'Anytown'),
       (8, 'John', 'David', '789 Elm St.', 'Anytown'),
       (9, 'Wilson', 'John', '123 Main St.', 'Anytown'),
       (10, 'Smith', 'Mary', '456 Maple St.', 'Anytown'),
       (11, 'Jones', 'David', '789 Elm St.', 'Anytown'),
       (12, 'John', 'David', '789 Elm St.', 'Anytown'),
       (13, 'Wilson', 'John', '123 Main St.', 'Anytown'),
       (14, 'Smith', 'Mary', '456 Maple St.', 'Anytown');
```

Les valeurs ont été insérées dans la table `Persons` :

![Insertion dans la table Persons](https://user-images.githubusercontent.com/33565767/204225226-f1a52566-78bd-46fb-af84-8b8e5e5ce49e.png 'Insertion dans la table Persons')

La table contient maintenant 14 enregistrements :

![Les données insérées dans la table Persons](https://user-images.githubusercontent.com/33565767/204225456-754695bb-68de-4194-93d1-3c1a5a6c9732.png 'Les données insérées dans la table Persons')

Nous pouvons également ajouter des enregistrements avec un nom de ville autre que `Anytown` :

```sql
INSERT INTO Persons(PersonID, LastName, FirstName, Address, City)
VALUES (15, 'Jones', 'David', '789 Elm St.', 'New York'),
       (16, 'John', 'David', '789 Elm St.', 'New York'),
       (17, 'Wilson', 'John', '123 Main St.', 'New York'),
       (18, 'Smith', 'Mary', '456 Maple St.', 'New York');
```

Les valeurs ont été insérées dans la table `Persons` :

![Les valeurs insérées dans la table Persons](https://user-images.githubusercontent.com/33565767/204225867-02987894-f103-45be-a6b6-2ce8d0adcc81.png 'Les valeurs insérées dans la table Persons')

Les données avec différentes villes ont été insérées dans la table `Persons` :

![Les enregistrements avec différentes villes ont été insérés dans la table Persons](https://user-images.githubusercontent.com/33565767/204226482-49f01867-b989-4234-8669-401dc99d820f.png 'Les enregistrements avec différentes villes ont été insérés dans la table Persons')


Maintenant que nous avons au moins 10 enregistrements dans la table `Persons` où la `City` est `Anytown`, nous pouvons insérer les 10 premiers enregistrements de la table `Persons` dans la table `PersonsBackup` où la `City` est `Anytown` :

Nous allons d'abord supprimer les enregistrements de la table `PersonsBackup` :

```sql
DELETE FROM PersonsBackup;
```

![Suppression de la table PersonsBackup](https://user-images.githubusercontent.com/33565767/204227157-4c2a54c2-8f5c-4dd5-a917-e7bb2aeb4878.png 'Suppression de la table PersonsBackup')

La table `PersonsBackup` est maintenant vide :

![La table PersonsBackup est maintenant vide](https://user-images.githubusercontent.com/33565767/204227440-a776129c-ee5a-4eed-8c52-c16642d149c8.png 'La table PersonsBackup est maintenant vide')

Nous pouvons maintenant insérer les 10 premiers enregistrements de la table `Persons` dans la table `PersonsBackup` où la `City` est `Anytown` :

```sql
INSERT INTO PersonsBackup
SELECT * FROM Persons WHERE City = 'Anytown' LIMIT 10;
```

Vous utilisez la clause limit pour limiter le nombre d'enregistrements à insérer dans la table `PersonsBackup`. Dans ce cas, nous insérons les 10 premiers enregistrements de la table `Persons` dans la table `PersonsBackup` où la `City` est `Anytown`.

Vous utilisez la clause where pour spécifier la condition qui doit être remplie pour que les enregistrements soient insérés dans la table `PersonsBackup`. Dans ce cas, la `City` doit être `Anytown` pour que les enregistrements soient insérés dans la table `PersonsBackup`.

Lorsque nous exécutons la requête ci-dessus, les 10 premiers enregistrements de la table `Persons` où la `City` est `Anytown` seront insérés dans la table `PersonsBackup` :

Exécution de la requête ci-dessus :

![Exécution de la requête ci-dessus, les 10 premiers enregistrements de la table Persons où la City est Anytown seront insérés dans la table PersonsBackup](https://user-images.githubusercontent.com/33565767/204228608-464fb97f-1c24-452b-ae9e-17d02ffaa912.png 'Exécution de la requête ci-dessus, les 10 premiers enregistrements de la table Persons où la City est Anytown seront insérés dans la table PersonsBackup')


Les enregistrements ont été insérés dans la table `PersonsBackup` :

![Les 10 enregistrements insérés de la table Persons](https://user-images.githubusercontent.com/33565767/204228789-407882d8-9e6e-4b47-a08b-bfe0da268204.png)


## Comment insérer des enregistrements à partir d'une instruction SELECT avec une clause WHERE et une clause ORDER BY

Nous pouvons insérer des enregistrements à partir d'une instruction SELECT avec une clause WHERE et une clause ORDER BY dans une table en utilisant l'instruction SQL INSERT INTO SELECT.

L'instruction SQL suivante insère tous les enregistrements de la table `Persons` dans la table `PersonsBackup` où la `City` est `Anytown` et trie les enregistrements par `LastName`.

Commençons par supprimer les enregistrements de la table `PersonsBackup` :

```sql
DELETE FROM PersonsBackup;
```

![Suppression de PersonsBackup](https://user-images.githubusercontent.com/33565767/204490301-d3a4a651-8b0b-4ace-8ddc-6c049a5170bd.png 'Suppression de PersonsBackup')

La table `PersonsBackup` est maintenant vide.

Maintenant, nous pouvons insérer tous les enregistrements de la table `Persons` dans la table `PersonsBackup` où la `City` est `Anytown` et trier les enregistrements par `LastName` :

```sql
INSERT INTO PersonsBackup
SELECT * FROM Persons WHERE City = 'Anytown' ORDER BY LastName;
```

![Insertion dans la table PersonsBackup à partir de la table Persons où la ville est Anytown et tri par nom](https://user-images.githubusercontent.com/33565767/204491737-1ca6933c-6f09-4085-908c-b54f34440aa4.png 'Insertion dans la table PersonsBackup à partir de la table Persons où la ville est Anytown et tri par nom')

Voici la table `Persons` avant l'exécution de la requête :

![La table Persons avant l'exécution de la requête](https://user-images.githubusercontent.com/33565767/204492282-fb2e2e81-ccf6-44df-94f5-15291fbce90c.png 'La table Persons avant l'exécution de la requête')

Voici la table `PersonsBackup` après l'insertion des enregistrements :

![La table PersonsBackup après l'insertion des enregistrements](https://user-images.githubusercontent.com/33565767/204492653-6a893c30-2446-4a06-b1ca-e2a44ded0f0a.png 'La table PersonsBackup après l'insertion des enregistrements')


## Comment insérer des enregistrements à partir d'une instruction SELECT avec une clause WHERE, une clause ORDER BY et une clause LIMIT

Nous pouvons insérer des enregistrements dans une table à partir d'une instruction SELECT avec une clause WHERE, une clause ORDER BY et une clause LIMIT en utilisant l'instruction SQL INSERT INTO SELECT.

L'instruction SQL suivante insère les 10 premiers enregistrements de la table `Persons` dans la table `PersonsBackup` où la `City` est `Anytown` et trie les enregistrements par `LastName`.

Commençons par supprimer les enregistrements de la table `PersonsBackup` :

```sql
DELETE FROM PersonsBackup;
```

Exécutez la requête ci-dessus sur votre outil de gestion de base de données. J'utilise TablePlus.

Après avoir exécuté la requête de suppression, voici le résultat :

![Suppression de la table PersonsBackup](https://user-images.githubusercontent.com/33565767/204725197-abb4114e-d4bf-44dd-9931-f8e91e4f8b17.png 'Suppression de la table PersonsBackup')

La table `PersonsBackup` est maintenant vide.

```sql
INSERT INTO PersonsBackup
SELECT * FROM Persons WHERE City = 'Anytown' ORDER BY LastName LIMIT 10;
```

Exécution de la requête ci-dessus sur TablePlus :

![image](https://user-images.githubusercontent.com/33565767/204727587-e6bde08d-e2a4-4ea5-8496-a30ac3fc9341.png)

Voici la table `PersonsBackup` après l'insertion des enregistrements :

![Insertion dans la table PersonsBackup après sélection de la table Persons où la ville est Anytown, triée par nom et limitée à 10](https://user-images.githubusercontent.com/33565767/204727939-a4519f59-b30e-45ed-b95c-f6840effb87e.png 'Insertion dans la table PersonsBackup après sélection de la table Persons où la ville est Anytown, triée par nom et limitée à 10')


## Comment insérer des enregistrements à partir d'une instruction SELECT avec une clause WHERE, une clause ORDER BY, une clause LIMIT et une clause OFFSET

Nous pouvons insérer des enregistrements à partir d'une instruction SELECT avec une clause WHERE, une clause ORDER BY, une clause LIMIT et une clause OFFSET en utilisant l'instruction SQL INSERT INTO SELECT.

L'instruction SQL suivante insère les enregistrements de la table `Persons` dans la table `PersonsBackup` où la `City` est `Anytown`. Elle trie les enregistrements par `LastName`, limite les enregistrements à 10 et saute les 5 premiers enregistrements.

Nous commencerons par la clause `OFFSET`. La clause `OFFSET` est utilisée pour sauter les `n` premiers enregistrements. Dans ce cas, nous sautons les 5 premiers enregistrements.

Commençons par supprimer les enregistrements de la table `PersonsBackup` :

```sql
DELETE FROM PersonsBackup;
```

Exécutez la requête ci-dessus sur votre outil de gestion de base de données.

Après avoir exécuté la requête de suppression, voici le résultat.

![Suppression de la table PersonsBackup](https://user-images.githubusercontent.com/33565767/204725197-abb4114e-d4bf-44dd-9931-f8e91e4f8b17.png 'Suppression de la table PersonsBackup')


```sql
INSERT INTO PersonsBackup
SELECT * FROM Persons WHERE City = 'Anytown' ORDER BY LastName LIMIT 10 OFFSET 5;
```

![Insertion dans la table PersonsBackup, sélection de la table Persons où la ville est Anytown et tri par nom, tout en limitant à 10 et en sautant les 5 premiers éléments](https://user-images.githubusercontent.com/33565767/204733392-3a08eb1d-6d42-45e2-8372-1ccd02eddcc3.png 'Insertion dans la table PersonsBackup, sélection de la table Persons où la ville est Anytown et tri par nom, tout en limitant à 10 et en sautant les 5 premiers éléments')

Puisque nous avons sauté les 5 premiers enregistrements, les 5 premiers enregistrements de la table `Persons` ne sont pas insérés dans la table `PersonsBackup`. Cela signifie que seuls 8 enregistrements sur 13 sont insérés dans la table `PersonsBackup`, où la ville est égale à Anytown.

## Conclusion

Dans ce tutoriel, vous avez appris à insérer des enregistrements dans une table en utilisant l'instruction SQL INSERT INTO.

Vous avez également appris à insérer des enregistrements dans une table avec une instruction SELECT en utilisant l'instruction SQL INSERT INTO SELECT.

Si vous souhaitez en savoir plus sur SQL, consultez ce cours : [SQL Tutorial - Full Database Course for Beginners](https://www.youtube.com/watch?v=HXV3zeQKqGY&t=5s). Il est gratuit sur la chaîne YouTube de freeCodeCamp.