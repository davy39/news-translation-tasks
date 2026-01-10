---
title: SQL Alter Table - Comment ajouter une colonne, la renommer ou la supprimer
  - Expliqué avec des exemples de syntaxe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-05T22:23:00.000Z'
originalURL: https://freecodecamp.org/news/sql-alter-table-add-column-rename-drop
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f93740569d1a4ca4356.jpg
tags:
- name: SQL
  slug: sql
seo_title: SQL Alter Table - Comment ajouter une colonne, la renommer ou la supprimer
  - Expliqué avec des exemples de syntaxe
seo_desc: 'This is a guide to SQL ALTER TABLE

  This guide will introduce you to and attempt to explain some of the basics of the
  SQL alter table functions within a relational database.  IMPORTANT Safety Tip: ALWAYS
  backup your data before making changes!

  We will...'
---

## Ce guide explique SQL ALTER TABLE

Ce guide vous présentera et tentera d'expliquer certaines des bases des fonctions SQL alter table dans une base de données relationnelle. **Conseil de sécurité important : TOUJOURS sauvegardez vos données avant de faire des modifications !**

Nous utiliserons MySQL pour tous les exemples de ce guide SQL freeCodeCamp. Les raisons de choisir MySQL sont 1) il est très couramment utilisé sur les sites web pour la base de données backend, 2) il est gratuit, et il est amusant et facile à utiliser.

## Ce qui est couvert dans ce guide

Nous utiliserons les tables créées dans le guide « CREATE TABLE ». N'hésitez pas à consulter ce guide si vous n'êtes pas familier avec la création d'une table.

* La modification de la table créée la modifiera de plusieurs manières différentes.
* Nous changerons son nom et modifierons les colonnes.
* Ajouter des colonnes (en ajoutant des colonnes, nous passerons également en revue plusieurs des types de colonnes les plus importants et leur utilisation).
* Supprimer des colonnes (c'est-à-dire supprimer la colonne).
* Créer une table en important un fichier CSV et modifier cette table.
* Créer et modifier des tables avec les outils MySQL Workbench.

La plupart de cela sera fait en utilisant des instructions SQL dans l'outil de script MySQL Workbench, mais nous passerons également en revue comment modifier une table en utilisant l'interface Workbench au lieu d'utiliser des instructions SQL.

## La table avant les modifications

Ajouter des colonnes de date et d'adresse email (une date et une colonne de caractères) :

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/alter_table01.JPG)

Ajouter une colonne numérique (notez qu'elle a été ajoutée à un emplacement spécifique dans la table) :

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/alter_table02.JPG)

Renommer certaines colonnes :

![image-1](https://freecodecamp.s3.amazonaws.com/guide-sql-images/alter_table03.JPG)

Vous pouvez également utiliser l'outil ALTER TABLE de Workbench. Il suffit de cliquer avec le bouton droit sur la table que vous souhaitez modifier et de la changer comme vous le souhaitez.

Il y a beaucoup plus à faire, consultez le manuel de votre logiciel de gestion de base de données pour en savoir plus.