---
title: Instruction SQL SELECT – Comment sélectionner des données dans une base de
  données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-20T16:56:43.000Z'
originalURL: https://freecodecamp.org/news/sql-select-statement-how-to-select-data-from-a-database
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/SQL-SELECT-Statement.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Instruction SQL SELECT – Comment sélectionner des données dans une base
  de données
seo_desc: "By Karlgusta Annoh\nIn this article, you will learn about the SQL SELECT\
  \ statement. We'll discuss its syntax, how to use it, and how to use the SELECT\
  \ statement with the WHERE clause. You will also learn how to use it with the ORDER\
  \ BY clause. \nIntrod..."
---

Par Karlgusta Annoh

Dans cet article, vous apprendrez à utiliser l'instruction SQL SELECT. Nous discuterons de sa syntaxe, de son utilisation et de la manière d'utiliser l'instruction SELECT avec la clause WHERE. Vous apprendrez également à l'utiliser avec la clause ORDER BY.

## Introduction à l'instruction SQL SELECT

L'instruction SQL SELECT est une instruction que vous utilisez pour sélectionner des données dans une base de données.

Le résultat de l'instruction SELECT est stocké dans une table de résultats, également appelée résultat. Le résultat est une table virtuelle qui n'a pas d'existence physique. Vous utilisez le résultat pour afficher les données dans un format tabulaire.

## Syntaxe de l'instruction SQL SELECT

La syntaxe de l'instruction SQL SELECT est la suivante :

```sql
    SELECT column_name(s)
    FROM table_name;
```

Un exemple de l'instruction SQL SELECT est le suivant :

```sql
    SELECT * FROM Customers;
```

## Comment utiliser l'instruction SQL SELECT dans MySQL Workbench

Nous allons utiliser un outil de conception de base de données visuel appelé MySQL Workbench.

MySQL Workbench nous permet de créer une base de données, de créer une table, d'insérer des données dans la table et d'exécuter l'instruction SQL SELECT.

Pour utiliser l'instruction SQL SELECT dans MySQL Workbench, nous devons suivre les étapes suivantes :

1. Ouvrez MySQL Workbench.
2. Connectez-vous au serveur MySQL.
3. Créez une base de données.
4. Créez une table.
5. Insérez des données dans la table.
6. Exécutez l'instruction SQL SELECT.
7. Affichez le résultat.

## Ouvrir MySQL Workbench

Pour ouvrir MySQL Workbench, nous devons suivre ces étapes :

Tout d'abord, installez MySQL Workbench sur votre ordinateur, si vous ne l'avez pas déjà installé. Vous pouvez télécharger MySQL Workbench à partir du lien suivant : https://dev.mysql.com/downloads/workbench/

![Où télécharger MySQL Workbench](https://user-images.githubusercontent.com/33565767/206399335-81d0642c-4d9a-4f0d-a949-90a1836b6280.png 'Où télécharger MySQL Workbench')

Ensuite, installez le serveur MySQL sur votre ordinateur, si vous ne l'avez pas déjà installé. Vous pouvez télécharger le serveur MySQL à partir du lien suivant : https://dev.mysql.com/downloads/mysql/

![Où télécharger le serveur MySQL](https://user-images.githubusercontent.com/33565767/206399804-7db0adb6-190a-44ce-8ad8-5380b1a74db2.png 'Où télécharger le serveur MySQL')

Maintenant, vous allez ouvrir MySQL Workbench. Pour ce faire, cliquez sur le bouton Démarrer, puis cliquez sur l'icône MySQL Workbench.

![Ouvrir MySQL Workbench](https://user-images.githubusercontent.com/33565767/206399997-e991c3ab-89aa-489a-ab9a-20be8aafe55d.png 'Ouvrir MySQL Workbench')

Connectez-vous au serveur MySQL en cliquant sur l'icône Connexions MySQL, puis cliquez sur l'icône Instance locale 3306.

![Se connecter au serveur MySQL](https://user-images.githubusercontent.com/33565767/206400391-f4dc143e-06e7-4aac-9e7b-32f1e5138d40.png 'Se connecter au serveur MySQL')

Entrez le mot de passe du serveur MySQL dans le champ Mot de passe, puis cliquez sur le bouton OK.

![Entrez le mot de passe pour le serveur MySQL](https://user-images.githubusercontent.com/33565767/206400694-eba711dc-79b2-48df-a8d5-9cbb6ca6bb86.png 'Entrez le mot de passe pour le serveur MySQL')

Ensuite, vous devrez créer la base de données en cliquant sur l'icône Nouveau Schéma, puis en entrant le nom de la base de données dans le champ Nom.

![Créer une base de données dans MySQL Workbench](https://user-images.githubusercontent.com/33565767/206401624-b98fdf11-cc19-4dd5-8ef0-487c38d23fb1.png 'Créer une base de données dans MySQL Workbench')

Ensuite, cliquez sur le bouton Appliquer et cliquez sur le bouton Fermer.

![Voici la base de données créée](https://user-images.githubusercontent.com/33565767/206402352-a24a4e80-3770-4c63-a011-48896f455169.png 'Voici la base de données créée')

Maintenant, vous allez créer une table. Pour ce faire, entrez l'instruction SQL suivante dans l'éditeur SQL, puis cliquez sur le bouton Exécuter :

```sql
   CREATE TABLE Customers (
    CustomerID int NOT NULL,
    CustomerName varchar(255) NOT NULL,
    ContactName varchar(255) NOT NULL,
    Address varchar(255) NOT NULL,
    City varchar(255) NOT NULL,
    PostalCode varchar(255) NOT NULL,
    Country varchar(255) NOT NULL
   );
```

Assurez-vous d'avoir sélectionné la base de données dans le navigateur de base de données. Pour accéder à l'éditeur SQL, cliquez sur l'icône Éditeur SQL.

![Onglet Éditeur SQL](https://user-images.githubusercontent.com/33565767/206403845-8ca3f459-cda2-4292-8f71-57eecd09bc23.png 'Onglet Éditeur SQL')


Créons maintenant la table Customers. Pour ce faire, entrez l'instruction SQL suivante dans l'éditeur SQL, puis cliquez sur le bouton Exécuter :

```sql
   CREATE TABLE Customers (
    CustomerID int NOT NULL,
    CustomerName varchar(255) NOT NULL,
    ContactName varchar(255) NOT NULL,
    Address varchar(255) NOT NULL,
    City varchar(255) NOT NULL,
    PostalCode varchar(255) NOT NULL,
    Country varchar(255) NOT NULL
   );
```

![Créer la table Customers](https://user-images.githubusercontent.com/33565767/206403200-94b39cc3-a785-455d-b72d-236d0f876af7.png 'Créer la table Customers')

Maintenant, vous allez exécuter l'instruction SQL. Après avoir entré l'instruction SQL, cliquez sur le bouton Exécuter.

![image](https://user-images.githubusercontent.com/33565767/206404552-87efc906-ac16-457e-acaf-d4261c8fff88.png)


Pour insérer des données dans la table, entrez l'instruction SQL suivante dans l'éditeur SQL, puis cliquez sur le bouton Exécuter :

```sql
   INSERT INTO Customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country) VALUES (1, 'Alfreds Futterkiste', 'Maria Anders', 'Obere Str. 57', 'Berlin', '12209', 'Germany');
```

![Insérer dans la table Customers](https://user-images.githubusercontent.com/33565767/206649495-65f45f7e-9b4b-4b12-961f-fb5200fc2ddf.png 'Insérer dans la table Customers')


Maintenant, exécutez l'instruction SQL SELECT en entrant l'instruction SQL suivante dans l'éditeur SQL, puis cliquez sur le bouton Exécuter :

```sql
   SELECT * FROM Customers;
```

![Sélectionner depuis Customers](https://user-images.githubusercontent.com/33565767/206650409-71ebd314-8c97-4b4b-83c1-9ec3fa37992f.png 'Sélectionner depuis Customers')

## Comment utiliser l'instruction SQL SELECT avec la clause WHERE

Vous pouvez utiliser l'instruction SQL SELECT avec la clause WHERE. Vous utilisez la clause WHERE pour filtrer les enregistrements. La clause WHERE extrait uniquement les enregistrements qui remplissent une condition spécifiée.

La syntaxe de l'instruction SQL SELECT avec la clause WHERE est la suivante :

```sql
   SELECT column_name(s)
   FROM table_name
   WHERE condition;
```

Un exemple d'utilisation de l'instruction SQL SELECT avec la clause WHERE est le suivant :

```sql
   SELECT * FROM Customers
   WHERE Country='Germany';
```

Insérons un autre enregistrement avec un pays différent et testons l'instruction SQL SELECT avec la clause WHERE.

Pour insérer un autre enregistrement, entrez l'instruction SQL suivante dans l'éditeur SQL, puis cliquez sur le bouton Exécuter :

```sql
   INSERT INTO Customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country) VALUES (2, 'Ana Trujillo Emparedados y helados', 'Ana Trujillo', 'Avda. de la Constitucion 2222', 'Mexico D.F.', '05021', 'Mexico');
```

![Insérer dans Customers dans MySQL Workbench](https://user-images.githubusercontent.com/33565767/206651983-753b9b6d-ec67-4070-ba85-855fec07fedb.png 'Insérer dans Customers dans MySQL Workbench')

Maintenant, exécutons l'instruction SQL SELECT avec la clause WHERE. Entrez l'instruction SQL suivante dans l'éditeur SQL, puis cliquez sur le bouton Exécuter :

```sql
   SELECT * FROM Customers
   WHERE Country='Germany';
```

![Sélectionner depuis Customers dans MySQL Workbench](https://user-images.githubusercontent.com/33565767/206653156-c6f4a814-6ff7-4414-9217-b94b1d83f442.png 'Sélectionner depuis Customers dans MySQL Workbench')

## Comment utiliser l'instruction SQL SELECT avec la clause ORDER BY

Vous pouvez également utiliser l'instruction SQL SELECT avec la clause ORDER BY. La clause ORDER BY trie le résultat dans l'ordre croissant ou décroissant. Elle trie les enregistrements dans l'ordre croissant par défaut. Si vous souhaitez trier les enregistrements dans l'ordre décroissant, vous pouvez utiliser le mot-clé DESC.

La syntaxe de l'instruction SQL SELECT avec la clause ORDER BY est la suivante :

```sql
   SELECT column_name(s)
   FROM table_name
   ORDER BY column_name(s) ASC/DESC;
```

Un exemple d'utilisation de l'instruction SQL SELECT avec la clause ORDER BY est le suivant :

```sql
   SELECT * FROM Customers
   ORDER BY Country DESC;
```

![Sélectionner depuis Customers, trier par ordre décroissant par nom de pays](https://user-images.githubusercontent.com/33565767/206653974-affc64b0-5f01-4700-9f81-7609588e95f0.png 'Sélectionner depuis Customers, trier par ordre décroissant par nom de pays')

## Conclusion

Dans cet article, nous avons appris à utiliser l'instruction SQL SELECT. Nous avons appris la syntaxe de l'instruction SELECT, comment l'utiliser et comment elle fonctionne avec la clause WHERE. Nous avons également appris à utiliser l'instruction SQL SELECT avec la clause ORDER BY.