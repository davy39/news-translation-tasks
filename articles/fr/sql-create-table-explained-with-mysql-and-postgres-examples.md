---
title: SQL Create Table Expliqué avec des Exemples de Syntaxe pour MySQL et Postgres
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-04T22:21:00.000Z'
originalURL: https://freecodecamp.org/news/sql-create-table-explained-with-mysql-and-postgres-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f9e740569d1a4ca4392.jpg
tags:
- name: SQL
  slug: sql
seo_title: SQL Create Table Expliqué avec des Exemples de Syntaxe pour MySQL et Postgres
seo_desc: 'A table is a group of data stored in a database.

  To create a table in a database you use the  CREATE TABLE  statement. You give a
  name to the table and a list of columns with its datatypes.

  CREATE TABLE TABLENAME(Attribute1 Datatype, Attribute2 Datat...'
---

Une table est un groupe de données stockées dans une base de données.

Pour créer une table dans une base de données, vous utilisez l'instruction `CREATE TABLE`. Vous donnez un nom à la table et une liste de colonnes avec leurs types de données.

```
CREATE TABLE TABLENAME(Attribute1 Datatype, Attribute2 Datatype,........);

```

Voici un exemple de création d'une table nommée Person :

```
CREATE TABLE Person(
  Id int not null,
  Name varchar not null,
  DateOfBirth date not null,
  Gender bit not null,
  PRIMARY KEY( Id )
);

```

Dans l'exemple ci-dessus, chaque Person a un Name, une Date of Birth et un Gender. La colonne Id est la clé qui identifie une personne dans la table. Vous utilisez le mot-clé `PRIMARY KEY` pour configurer une ou plusieurs colonnes comme clé primaire.

Une colonne peut être `not null` ou `null`, indiquant si elle est obligatoire ou non.

## Un Guide Plus Approfondi sur le Guide SQL de la Commande CREATE TABLE

Ce guide est un aperçu des bases des fonctions SQL `CREATE TABLE`.

Nous utiliserons MySQL pour tous les exemples tout au long de ces guides SQL de freeCodeCamp. MySQL est fréquemment utilisé sur les sites web pour la base de données backend, 2) il est gratuit, et il est amusant et facile à utiliser.

## Couvert dans ce Guide

* Création d'un schéma, le conteneur pour tous nos objets de base de données.
* Créer une table pour avoir quelque chose à modifier.
* Création d'une table en important un fichier CSV et modification de cette table
* Création d'une table en utilisant l'outil MySQL Workbench

Nous faisons la plupart de ce travail avec des instructions SQL dans l'outil de script MySQL Workbench. Nous verrons également comment créer une table en utilisant l'interface Workbench au lieu d'utiliser des instructions SQL.

## Structure de Haut Niveau d'une Base de Données Relationnelle

1. Niveau le plus élevé ; La Base de Données ; l'installation du système de base de données. Dans ce cas, c'est MySQL. Appelé « Local instance MySQL Router » dans les captures d'écran ci-dessus.
2. Ensuite, un Schéma ; un conteneur pour les objets nécessaires à la gestion des données dans un système de base de données relationnelle.
3. Objets que nous créons (tables, index, procédures stockées, fonctions) pour gérer le système et ses données

## Création d'un Schéma MySQL

Le schéma est un conteneur pour les objets nécessaires à la gestion des données pour un sujet ou un processus donné. Nous montrons des exemples au fur et à mesure que nous progressons dans ce guide.

Nous créerons le schéma pour notre apprentissage et nos tests en utilisant la commande SQL ;

```
create database fCC_alterTableGuide;

```

Structure du schéma de cette instance avant l'exécution de cette commande

![Image](https://www.freecodecamp.org/news/content/images/2020/03/create_table02.JPG)

## Création d'une table, ajout de données de test avec « insert », renommage de la table (alter)

Nous créerons une table Student.

Les étapes seront :

1. s'assurer que nous n'avons pas déjà la table
2. créer la table
3. insérer les données de test.
4. Types de données : le nom de l'étudiant est un champ de caractères limité à 90 caractères
5. L'ID de l'étudiant est un nombre (entier) (plage de -2147483648 à 2147483647). Ce sera la clé primaire de la table et s'incrémentera automatiquement lorsqu'un enregistrement sera ajouté.
6. Il y aura également deux champs « time-stamp » à utiliser

Instruction de création et affichage des résultats de l'exécution.

En utilisant une instruction Select, nous verrons que la table est là mais qu'aucun enregistrement n'a été ajouté.

![image-5](https://freecodecamp.s3.amazonaws.com/guide-sql-images/create_table05.JPG)

Maintenant, insérons quelques données et voyons à quoi ressemble notre nouvelle table avec des enregistrements (et comprenons les timestamps de création et de mise à jour) ;

Le premier timestamp est la date et l'heure de création et le deuxième est la date et l'heure de mise à jour. La modification d'un enregistrement devrait mettre à jour ts2 mais pas ts1. Jetons un coup d'œil.

![image-7](https://freecodecamp.s3.amazonaws.com/guide-sql-images/create_table07.JPG)

## Créer une table avec MySQL Workbench

Faites un clic droit sur « Tables » sous le schéma où vous souhaitez placer le nouveau fichier. Sélectionnez Create Table. Ensuite, complétez le formulaire comme souhaité et cliquez sur Apply.

## Créer une Table en tant que Sélection (CTAS)

Un moyen rapide de créer une copie d'une table, y compris les données, est de créer une table en tant que sélection.

CREATE TABLE my_table as (SELECT * FROM orig_tbl);

## Créer et peupler une table en important un fichier CSV

Faites un clic droit sur « Tables » sous le schéma où vous souhaitez placer le nouveau fichier. Sélectionnez Table Data Import.

Sélectionnez le fichier CSV à importer et cliquez sur NEXT. Habituellement, vous créez une nouvelle table à partir des données, sélectionnez les options souhaitées et cliquez sur NEXT.

![image-11](https://freecodecamp.s3.amazonaws.com/guide-sql-images/create_table11.JPG)

Ajustez les types de données si nécessaire et cliquez sur NEXT.

Cliquez sur NEXT (sur cet écran et le suivant qui s'affiche) pour importer les données dans la table. Vous verrez l'état de la complétion, passez en revue et cliquez sur FINISH.

![image-13](https://freecodecamp.s3.amazonaws.com/guide-sql-images/create_table13.JPG)

## Autres Matériaux

Il y a beaucoup plus de détails à couvrir sur ce sujet, alors installez MySQL et amusez-vous !