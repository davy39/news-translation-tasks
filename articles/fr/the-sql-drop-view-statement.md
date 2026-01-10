---
title: L'instruction SQL DROP VIEW pour supprimer des données d'une table
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-10T21:34:00.000Z'
originalURL: https://freecodecamp.org/news/the-sql-drop-view-statement
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ec9740569d1a4ca3f1c.jpg
tags:
- name: SQL
  slug: sql
seo_title: L'instruction SQL DROP VIEW pour supprimer des données d'une table
seo_desc: 'Introduction

  This guide covers the SQL statement for dropping (deleting) one or more view objects.

  A View is an object that presents data from one or more tables.

  Note: before deleting or changing data or objects, remember to have a fresh backup.

  We ...'
---

### Introduction

Ce guide couvre l'instruction SQL pour supprimer (effacer) un ou plusieurs objets de vue.

Une Vue est un objet qui présente des données provenant d'une ou plusieurs tables.

Note : avant de supprimer ou de modifier des données ou des objets, pensez à faire une sauvegarde fraîche.

Nous allons couvrir :

* Utiliser SQL pour supprimer une table
* Utiliser le workbench pour supprimer une vue

Nous utiliserons MySQL pour la démonstration. Consultez le manuel pour cette fonction dans d'autres gestionnaires de bases de données.

Nous allons supprimer la vue appelée `students_dropMe_v`, qui a été créée spécialement pour cet usage.

### Syntaxe de base

```
DROP VIEW [IF EXISTS]
    view_name [, view_name] ...
```

### Supprimer une Vue avec SQL

La partie "if exists" permettra de "capturer" les erreurs, au cas où la vue n'existerait pas.

```
drop view if exists students_dropMe_v;
```

La vue après sa création :

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/drop-view01.JPG)

### Utiliser le Workbench

Depuis le workbench :

1. Faites un clic droit sur la vue à supprimer
2. Sélectionnez "drop view" dans le menu
3. Choisissez soit a) exécuter SQL pour revoir l'instruction SQL à exécuter, soit b) supprimer maintenant

*Comme pour toutes ces choses SQL, il y a BEAUCOUP PLUS à savoir que ce qui est présenté dans ce guide d'introduction. J'espère que cela vous donne au moins assez pour commencer.*

*Veuillez consulter le manuel de votre gestionnaire de base de données et amusez-vous à essayer différentes options par vous-même.*

### Supplément

Voici le SQL que j'ai utilisé pour créer la table que nous venons de supprimer :

```
create view `students_dropMe_v` as
select FullName, programOfStudy 
from student 
where programOfStudy = 'Programming';
```