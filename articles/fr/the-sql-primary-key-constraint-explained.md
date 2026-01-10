---
title: La contrainte de clé primaire SQL expliquée avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-13T22:52:00.000Z'
originalURL: https://freecodecamp.org/news/the-sql-primary-key-constraint-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f53740569d1a4ca4205.jpg
tags:
- name: SQL
  slug: sql
seo_title: La contrainte de clé primaire SQL expliquée avec des exemples
seo_desc: 'A primary key is a column or a set of columns that uniquely identifies
  each row in a table.

  It’s called a “constraint” because it causes the system to restrict the data allowed
  in these column(s). In this case…


  to contain data (NOT NULL)

  be UNIQUE f...'
---

Une clé primaire est une colonne ou un ensemble de colonnes qui identifie de manière unique chaque ligne dans une table.

Elle est appelée une "contrainte" car elle oblige le système à restreindre les données autorisées dans ces colonne(s). Dans ce cas...

* contenir des données (NOT NULL)
* être UNIQUE par rapport à toutes les autres lignes de la table.
* Chaque table ne peut avoir qu'une seule clé primaire

Les clés primaires sont principalement utilisées pour maintenir l'intégrité des données de chaque ligne.

Cela permet également au système et aux applications d'être sûrs qu'ils lisent, mettent à jour et joignent les données correctement.

### Exemple avec create table

Voici une commande create table qui créera également une clé primaire en utilisant deux champs.

```
CREATE TABLE priKeyExample(
rcdKey_id_a INT NOT NULL,
rcdKeySeq_id INT NOT NULL,
someData varchar(256) NOT NULL,
PRIMARY KEY(rcdKey_id_a,rcdKeySeq_id));
```

### Exemple avec alter table

La clé primaire existante doit d'abord être supprimée

```
DROP INDEX `primary` ON priKeyExample;
```

Maintenant, nous allons ajouter la nouvelle clé primaire.

```
ALTER TABLE priKeyExample 
ADD CONSTRAINT myPriKey PRIMARY KEY(rcdKey_id_a,rcdKeySeq_id);
```

Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à savoir que ce qui est présenté dans ce guide d'introduction.

J'espère que cela vous donne au moins assez pour commencer.

Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options par vous-même.