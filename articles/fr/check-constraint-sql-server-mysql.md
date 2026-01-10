---
title: Contrainte CHECK en SQL - Expliquée avec des exemples de syntaxe MySQL et SQL
  Server
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-02T21:18:00.000Z'
originalURL: https://freecodecamp.org/news/check-constraint-sql-server-mysql
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9fac740569d1a4ca43ea.jpg
tags:
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
seo_title: Contrainte CHECK en SQL - Expliquée avec des exemples de syntaxe MySQL
  et SQL Server
seo_desc: 'The CHECK constraint is used to limit the value range that can be placed
  in a column.

  If you define a CHECK constraint on a single column it allows only certain values
  for this column.

  If you define a CHECK constraint on a table it can limit the valu...'
---

La contrainte CHECK est utilisée pour limiter la plage de valeurs qui peuvent être placées dans une colonne.

Si vous définissez une contrainte CHECK sur une seule colonne, elle n'autorise que certaines valeurs pour cette colonne.

Si vous définissez une contrainte CHECK sur une table, elle peut limiter les valeurs de certaines colonnes en fonction des valeurs d'autres colonnes dans la ligne.

### CHECK SQL sur CREATE TABLE

Le SQL suivant crée une contrainte CHECK sur la colonne "Age" lors de la création de la table "Persons". La contrainte CHECK garantit que vous ne pouvez pas avoir de personne de moins de 18 ans :

**MySQL :**

```
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CHECK (Age>=18)
);
```

**SQL Server / Oracle / MS Access :**

```
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int CHECK (Age>=18)
);
```

Pour permettre le nommage d'une contrainte CHECK et pour définir une contrainte CHECK sur plusieurs colonnes, utilisez la syntaxe SQL suivante :

**MySQL / SQL Server / Oracle / MS Access :**

```
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    City varchar(255),
    CONSTRAINT CHK_Person CHECK (Age>=18 AND City='Sandnes')
);
```

### CHECK SQL sur ALTER TABLE

Pour créer une contrainte CHECK sur la colonne "Age" lorsque la table est déjà créée, utilisez le SQL suivant :

**MySQL / SQL Server / Oracle / MS Access :**

```
ALTER TABLE Persons
ADD CHECK (Age>=18);
```

Pour permettre le nommage d'une contrainte CHECK et pour définir une contrainte CHECK sur plusieurs colonnes, utilisez la syntaxe SQL suivante :

**MySQL / SQL Server / Oracle / MS Access :**

```
ALTER TABLE Persons
ADD CONSTRAINT CHK_PersonAge CHECK (Age>=18 AND City='Sandnes');
```

### Supprimer une contrainte CHECK

Pour supprimer une contrainte CHECK, utilisez le SQL suivant :

**SQL Server / Oracle / MS Access :**

```
ALTER TABLE Persons
DROP CONSTRAINT CHK_PersonAge;
```

**MySQL :**

```
ALTER TABLE Persons
DROP CHECK CHK_PersonAge;
```