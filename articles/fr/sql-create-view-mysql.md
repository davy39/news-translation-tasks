---
title: Vue SQL Expliquée - Comment Créer une Vue en SQL et MySQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-23T21:45:00.000Z'
originalURL: https://freecodecamp.org/news/sql-create-view-mysql
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e81740569d1a4ca3d7a.jpg
tags:
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
seo_title: Vue SQL Expliquée - Comment Créer une Vue en SQL et MySQL
seo_desc: 'What is a View in SQL?

  A View is a database object that presents data existing in one or more tables. Views
  are used in a similar way to tables, but they don’t contain any data. They just
  “point” to the data that exists elsewhere (tables or views, fo...'
---

### Qu'est-ce qu'une Vue en SQL ?

Une Vue est un objet de base de données qui présente des données existant dans une ou plusieurs tables. Les Vues sont utilisées de manière similaire aux tables, mais elles ne contiennent aucune donnée. Elles "pointent" simplement vers les données qui existent ailleurs (tables ou vues, par exemple).

### Pourquoi les apprécions-nous ?

* Les Vues sont un moyen de limiter les données présentées. Par exemple, les données du département des ressources humaines filtrées pour ne présenter que les informations sensibles. Les informations sensibles dans ce cas pourraient être les numéros de sécurité sociale, le sexe de l'employé, le taux de rémunération, l'adresse domicile, etc.
* Les données complexes provenant de plus d'une table peuvent être combinées en une seule "vue". Cela peut faciliter la vie de vos analystes commerciaux et programmeurs.

### Conseils de Sécurité Importants

* Les Vues sont gérées par le système. Lorsque les données dans les tables liées sont modifiées, ajoutées ou mises à jour, la Vue est mise à jour par le système. Nous voulons les utiliser uniquement lorsque cela est nécessaire pour gérer l'utilisation des ressources système.
* Dans MySQL, les modifications de la conception de la table (c'est-à-dire, nouvelles colonnes ou colonnes supprimées) effectuées APRÈS la création d'une vue ne sont pas mises à jour dans la vue elle-même. La vue devrait être mise à jour ou recréée.
* Les Vues sont l'un des quatre types standard d'objets de base de données. Les autres sont les tables, les procédures stockées et les fonctions.
* Les Vues peuvent généralement être traitées comme une table, mais les mises à jour sont limitées ou non disponibles lorsque la vue contient plus d'une table.
* Il existe de nombreux autres détails sur les vues qui dépassent le cadre de ce guide d'introduction. Passez du temps avec le manuel de vos gestionnaires de base de données et amusez-vous avec cet objet SQL puissant.

### Syntaxe de l'Instruction Create View (MySQL)

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

```
CREATE
    VIEW view_name [(column_list)]
    AS select_statement

```

### Exemple de Création de Vue à partir des Tables Étudiants

Notes :

* Le nom de la vue se termine par un "v". Il est recommandé que le nom de la vue indique qu'il s'agit d'une vue d'une manière ou d'une autre pour faciliter la vie des programmeurs et des administrateurs de base de données. Votre service informatique devrait avoir ses propres règles de nommage des objets.
* Les colonnes dans la vue sont limitées par le SELECT et les lignes de données par la clause WHERE.
* Le caractère "`" autour des noms de vue est requis en raison du "-" dans les noms. MySQL signale une erreur sans eux.

```
create view `programming-students-v` as
select FullName, programOfStudy 
from student 
where programOfStudy = 'Programming';

select * from `programming-students-v`;

```

### Exemple d'utilisation d'une Vue pour combiner des données de plus d'une table

Une table de données démographiques des étudiants a été ajoutée à la base de données pour démontrer cette utilisation. Cette vue combinera ces tables.

Notes :

* Pour "joindre" des tables, les tables doivent avoir des champs en commun (généralement des clés primaires) qui identifient de manière unique chaque ligne. Dans ce cas, il s'agit de l'ID de l'étudiant. (Plus d'informations à ce sujet dans le guide [SQL Joins](https://guide.freecodecamp.org/sql/sql-joins/index.md).)
* Remarquez l'"alias" donné à chaque table ("s" pour student et "sc" pour student contact). C'est un outil pour raccourcir les noms de tables et faciliter l'identification de la table utilisée. C'est plus facile que de taper de longs noms de tables à plusieurs reprises. Dans cet exemple, c'était requis car studentID est le même nom de colonne dans les deux tables, et le système présenterait une "erreur de nom de colonne ambiguë" sans spécifier quelle table utiliser.