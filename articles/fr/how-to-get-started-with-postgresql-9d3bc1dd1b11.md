---
title: Comment commencer avec PostgreSQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-02T16:22:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-postgresql-9d3bc1dd1b11
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IJ3HI44YdLzTkMOQpibNGw.png
tags:
- name: learning
  slug: learning
- name: postgres
  slug: postgres
- name: General Programming
  slug: programming
- name: SQL
  slug: sql
- name: technology
  slug: technology
seo_title: Comment commencer avec PostgreSQL
seo_desc: 'By Akul Tomar

  PostgreSQL is an open source Relational Database Management System (RDBMS). In this
  article, I’ll provide an introduction to getting started with PostgreSQL. Here is
  what we’ll cover:


  Installation

  Administration

  Basic Database Operatio...'
---

Par Akul Tomar

PostgreSQL est un système de gestion de base de données relationnelle (SGBDR) open source. Dans cet article, je vais fournir une introduction pour commencer avec PostgreSQL. Voici ce que nous allons couvrir :

* [Installation](https://medium.com/p/9d3bc1dd1b11#d220)
* [Administration](https://medium.com/p/9d3bc1dd1b11#d003)
* Opérations de base sur les bases de données

### Installation

Si vous avez homebrew installé sur votre système, vous pouvez exécuter la commande suivante dans votre terminal pour installer rapidement PostgreSQL :

```
brew install postgresql
```

Les autres peuvent télécharger la dernière version de PostgreSQL [ici](https://www.postgresql.org/download/) et suivre les étapes d'installation.

Une fois téléchargé, pour vérifier que vous avez bien installé PostgreSQL, exécutez la commande suivante pour vérifier votre version de PostgreSQL :

```
postgres --version
```

### Administration

PostgreSQL peut être administré depuis la ligne de commande en utilisant l'utilitaire `psql`, en exécutant la commande suivante :

```
psql postgres
```

Cela devrait lancer votre utilitaire psql. psql est l'outil en ligne de commande de PostgreSQL. Bien qu'il existe de nombreux outils tiers disponibles pour administrer les bases de données PostgreSQL, je n'ai pas encore ressenti le besoin d'installer un autre outil. psql est assez pratique et fonctionne très bien.

> Pour quitter l'interface psql, vous pouvez taper `\q` et vous êtes sorti.

Si vous avez besoin d'aide, tapez `\help` sur votre terminal psql. Cela listera toutes les options d'aide disponibles. Vous pouvez taper `\help [Nom de la Commande]`, au cas où vous auriez besoin d'aide avec une commande particulière. Par exemple, taper `\help UPDATE` depuis `psql` vous montrera la syntaxe de l'option de mise à jour.

```
Description: mettre à jour les lignes d'une table[ WITH [ RECURSIVE ] with_query [, ...] ]UPDATE [ ONLY ] table_name [ * ] [ [ AS ] alias ]    SET { column_name = { expression | DEFAULT } |          ( column_name [, ...] ) = ( { expression | DEFAULT } [, ...] ) |          ( column_name [, ...] ) = ( sub-SELECT )        } [, ...]    [ FROM from_list ]    [ WHERE condition | WHERE CURRENT OF cursor_name ]    [ RETURNING * | output_expression [ [ AS ] output_name ] [, ...] ]
```

Si vous êtes débutant, vous ne comprendrez peut-être pas encore. Une rapide recherche sur Google vous fournira des exemples de son utilisation ou vous pouvez toujours consulter la documentation officielle de [psql](https://www.postgresql.org/docs/current/static/sql-update.html) qui fournira de nombreux exemples.

Lorsque vous installez PostgreSQL pour la première fois, il y a quelques tâches administratives courantes que vous effectuerez fréquemment.

La première chose à faire serait de vérifier les utilisateurs et les bases de données existants. Exécutez la commande suivante pour lister toutes les bases de données :

```
\list ou \l
```

![Image](https://cdn-media-1.freecodecamp.org/images/X7JXfDeBJE4FwB8VpGyzcQQeScyrXbkbi0MR)

Sur la figure ci-dessus, vous pouvez voir **trois** bases de données par défaut et un superutilisateur `akultomar` qui sont créés lorsque vous installez PostgreSQL.

Pour lister tous les utilisateurs, utilisez la commande `\du`. Les attributs de l'utilisateur nous indiquent qu'ils sont un Superutilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/ufNwqrWDxIpZPbuVWl73LbCHehsjT3Hp5Tab)

### Opérations de base sur les bases de données

Pour effectuer des opérations de base sur les bases de données, vous utilisez le langage de requête structuré (communément appelé SQL).

#### **Créer une base de données**

Pour créer une base de données, vous utilisez la commande `create database`. Dans l'exemple ci-dessous, nous allons créer une base de données nommée `riskzone`.

![Image](https://cdn-media-1.freecodecamp.org/images/cDE-hPhNlkyAacTptApc62hoZrDTczpurCPy)

Si vous oubliez le point-virgule à la fin, le signe `=` à l'invite de postgres est remplacé par un `-` comme sur la figure ci-dessous. Cela indique simplement que vous devez terminer votre requête. Vous comprendrez son importance lorsque vous commencerez à écrire des requêtes plus longues. Pour l'instant, mettez simplement un point-virgule pour compléter l'instruction SQL et appuyez sur retour.

![Image](https://cdn-media-1.freecodecamp.org/images/yLCabIGAb-rU5IrgEr-ziVy9ynjkkcclgG2U)

#### **Créer un utilisateur**

Pour créer un utilisateur, vous utilisez la commande `create user`. Dans l'exemple ci-dessous, nous allons créer un utilisateur nommé `no_one`.

![Image](https://cdn-media-1.freecodecamp.org/images/Zo-ux1MpucuEes7-fNdgt1z5jwIoAswSj08n)

Lorsque vous créez un utilisateur, le message affiché est **CREATE ROLE**. Les utilisateurs sont des rôles avec des droits de connexion. Je les ai utilisés de manière interchangeable. Vous remarquerez également que la colonne Attributs est vide pour l'utilisateur `no_one`. Cela signifie que l'utilisateur `no_one` n'a pas de permissions administratives. Il ne peut que lire des données et ne peut pas créer un autre utilisateur ou une autre base de données.

Vous pouvez définir un mot de passe pour votre utilisateur. Pour définir un mot de passe pour un utilisateur existant, vous devez utiliser la commande `\password` suivante :

```
postgres=#\password no_one 
```

Pour définir un mot de passe lors de la création d'un utilisateur, la commande suivante peut être utilisée :

```
postgres=#create user no_two with login password 'qwerty';
```

#### **Supprimer un utilisateur ou une base de données**

La commande `drop` peut être utilisée pour supprimer une base de données ou un utilisateur, comme dans les commandes suivantes.

```
drop database <database_name>drop user <user_name>
```

> Cette commande doit être utilisée avec beaucoup de précaution. Les éléments supprimés ne reviennent pas sauf si vous avez une sauvegarde en place.

Si nous exécutons `\du` et `\l` que nous avons appris précédemment pour afficher la liste des utilisateurs et des bases de données respectivement, nous pouvons voir que notre nouvel utilisateur `no_one` et la base de données `riskzone`.

![Image](https://cdn-media-1.freecodecamp.org/images/RHPB-ZGQ4e8vqVY9mmlN-w1Qkieg44phby9Q)

Lorsque vous spécifiez `psql postgres` (sans nom d'utilisateur), il se connecte à la base de données postgres en utilisant le superutilisateur par défaut (`akultomar` dans mon cas). Pour se connecter à une base de données en utilisant un utilisateur spécifique, vous pouvez utiliser la commande suivante :

```
psql [database_name] [user_name]
```

Connectons-nous à la base de données `riskzone` avec l'utilisateur `no_one`. Appuyez sur `\q` pour quitter la base de données postgres précédente, puis exécutez la commande suivante pour vous connecter à `riskzone` avec l'utilisateur `no_one`.

![Image](https://cdn-media-1.freecodecamp.org/images/MsaHxCUlBMaQ0VEnGj7bNcH9rVjH9XuxGg3v)

J'espère que vous avez apprécié cette courte introduction à PostgreSQL. Je vais écrire un autre article pour vous aider à mieux comprendre les rôles. Si vous êtes nouveau dans SQL, mon conseil serait de pratiquer autant que possible. Mettez les mains dans le cambouis et créez vos propres petites tables et pratiquez.