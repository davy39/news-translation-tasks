---
title: 'Commandes SQL : Une introduction à la syntaxe de base, aux instructions et
  aux requêtes avec des exemples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-21T23:07:00.000Z'
originalURL: https://freecodecamp.org/news/sql-commands-syntax-statements-queries
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f22740569d1a4ca40f7.jpg
tags:
- name: SQL
  slug: sql
seo_title: 'Commandes SQL : Une introduction à la syntaxe de base, aux instructions
  et aux requêtes avec des exemples'
seo_desc: 'This guide provides a basic, high level description of the syntax for SQL
  statements.

  SQL is an international standard (ISO), but you will find many differences between
  implementations. This guide uses MySQL as an example. If you use one of the many
  ...'
---

Ce guide fournit une description de base, de haut niveau, de la syntaxe des instructions SQL.

SQL est une norme internationale (ISO), mais vous trouverez de nombreuses différences entre les implémentations. Ce guide utilise MySQL comme exemple. Si vous utilisez l'un des nombreux autres gestionnaires de bases de données relationnelles (SGBD), vous devrez consulter le manuel de ce SGBD si nécessaire.

### Ce que nous allons couvrir

* Use (détermine quelle base de données l'instruction utilisera)
* Clauses Select et From
* Clause Where (et / ou, IN, Between, LIKE)
* Order By (ASC, DESC)
* Group by et Having

### Comment utiliser ce guide

Ceci est utilisé pour sélectionner la base de données contenant les tables pour vos instructions SQL :

```
use fcc_sql_guides_database; -- sélectionne la base de données d'exemple du guide

```

### Clauses Select et From

La partie Select est normalement utilisée pour déterminer quelles colonnes des données vous souhaitez afficher dans les résultats. Il existe également des options que vous pouvez utiliser pour afficher des données qui ne sont pas une colonne de table.

Cet exemple montre deux colonnes sélectionnées dans la table « student », et deux colonnes calculées. La première des colonnes calculées est un nombre sans signification, et l'autre est la date du système.

```
	select studentID, FullName, 3+2 as five, now() as currentDate
    from student;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax01.JPG)

### Clause Where (et / ou, IN, Between et LIKE)

La clause WHERE est utilisée pour limiter le nombre de lignes retournées.

Dans ce cas, les cinq conditions suivantes seront utilisées dans une clause Where quelque peu ridicule.

Comparez ce résultat à l'instruction SQL ci-dessus pour suivre cette logique.

Les lignes présentées seront celles qui :

* Ont des identifiants d'étudiants entre 1 et 5 (inclus)
* ou studentID = 8
* ou ont « Maxmimo » dans le nom

L'exemple suivant est similaire, mais il précise en outre que si l'un des étudiants a certains scores SAT (1000, 1400), ils ne seront pas présentés :

```
    select studentID, FullName, sat_score, recordUpdated
    from student
    where (
		studentID between 1 and 5
		or studentID = 8
        or FullName like '%Maximo%'
		)
		and sat_score NOT in (1000, 1400);

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax02.JPG)

### Order By (ASC, DESC)

Order By nous donne un moyen de trier le jeu de résultats par un ou plusieurs des éléments de la section SELECT. Voici la même liste que ci-dessus, mais triée par le nom complet des étudiants. L'ordre de tri par défaut est ascendant (ASC), mais pour trier dans l'ordre inverse (descendant), vous utilisez DESC, comme dans l'exemple ci-dessous :

```
    select studentID, FullName, sat_score
    from student
    where (studentID between 1 and 5 -- inclus
		or studentID = 8
        or FullName like '%Maximo%')
		and sat_score NOT in (1000, 1400)
	order by FullName DESC;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax03.JPG)

### Group By et Having

Group By nous donne un moyen de combiner des lignes et d'agréger des données. La clause Having est similaire à la clause Where ci-dessus, sauf qu'elle agit sur les données groupées.

Ces données proviennent des données de contributions de campagne que nous avons utilisées dans certains de ces guides.

Cette instruction SQL répond à la question : « Quels candidats ont reçu le plus grand nombre de contributions (non pas le montant en $, mais le compte (*)) en 2016, mais seulement ceux qui avaient plus de 80 contributions ? »

Le fait de trier cet ensemble de données dans un ordre décroissant (DESC) place les candidats ayant le plus grand nombre de contributions en haut de la liste.

```
    select Candidate, Election_year, sum(Total_$), count(*)
    from combined_party_data
    where Election_year = 2016
    group by Candidate, Election_year
    having count(*) > 80
    order by count(*) DESC;

```

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/syntax04.JPG)

Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à découvrir que ce qui est présenté dans ce guide d'introduction. J'espère que cela vous donne au moins assez pour commencer. Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options par vous-même.