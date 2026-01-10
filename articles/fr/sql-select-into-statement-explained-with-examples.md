---
title: L'instruction SQL Select Into expliquée avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-18T23:02:00.000Z'
originalURL: https://freecodecamp.org/news/sql-select-into-statement-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f37740569d1a4ca416c.jpg
tags:
- name: SQL
  slug: sql
seo_title: L'instruction SQL Select Into expliquée avec des exemples
seo_desc: "What does the SQL Select Into statement do?\nThe  SELECT INTO  statement\
  \ is a query that allows you to create a  new  table and populate it with the result\
  \ set of a  SELECT statement. \nTo add data to an existing table, see the INSERT\
  \ INTO statement in..."
---

## Que fait l'instruction SQL Select Into ?

L'instruction `SELECT INTO` est une requête qui vous permet de créer une *nouvelle* table et de la remplir avec le jeu de résultats d'une instruction `SELECT`.

Pour ajouter des données à une table existante, voir l'instruction [INSERT INTO](https://guide.freecodecamp.org/sql/sql-select-into-statement/guides/src/pages/sql/sql-insert-into-select-statement/index.md) à la place.

`SELECT INTO` peut être utilisé lorsque vous combinez des données de plusieurs tables ou vues dans une nouvelle table. La table d'origine n'est pas affectée.

La syntaxe générale est :

```
SELECT column-names
  INTO new-table-name
  FROM table-name
 WHERE EXISTS 
      (SELECT column-name
         FROM table-name
        WHERE condition)

```

Cet exemple montre un ensemble de table qui a été "copié" de la table "Supplier" vers une nouvelle table appelée SupplierUSA qui contient l'ensemble lié à la colonne country de valeur 'USA'.

```
SELECT * INTO SupplierUSA
  FROM Supplier
 WHERE Country = 'USA';

```

**Résultats** : 4 lignes affectées

|ID|CompanyName|ContactName|City|Country|Phone|
| --- | --- | --- | --- | --- | --- |
|2|New Orleans Cajun Delights|Shelley Burke|New Orleans|USA|(100) 555-4822|
|3|Grandma Kelly's Homestead|Regina Murphy|Ann Arbor|USA|(313) 555-5735|
|16|Bigfoot Breweries|Cheryl Saylor|Bend|USA|NULL|
|19|New England Seafood Cannery|Robb Merchant|Boston|USA|(617) 555-3267|

Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options vous-même.

Pour aller plus loin :

1. (Microsoft - Inserting Rows by Using SELECT INTO)[[https://technet.microsoft.com/en-us/library/ms190750(v=sql.105).aspx](https://technet.microsoft.com/en-us/library/ms190750(v=sql.105).aspx)]
2. (dofactory - SQL SELECT INTO Statement)[[http://www.dofactory.com/sql/select-into](http://www.dofactory.com/sql/select-into)]