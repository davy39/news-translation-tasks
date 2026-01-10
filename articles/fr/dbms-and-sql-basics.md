---
title: Systèmes de Gestion de Bases de Données et SQL – Tutoriel pour Débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-12T13:57:35.000Z'
originalURL: https://freecodecamp.org/news/dbms-and-sql-basics
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/FreeCodeCamp.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Systèmes de Gestion de Bases de Données et SQL – Tutoriel pour Débutants
seo_desc: "By Bikash Daga (Jain)\nDatabase Management Systems and SQL are two of the\
  \ most important and widely used tools on the internet today. \nYou use a Database\
  \ Management System (DBMS) to store the data you collect from various sources, and\
  \ SQL to manipulat..."
---

Par Bikash Daga (Jain)

Les Systèmes de Gestion de Bases de Données (SGBD) et SQL sont deux des outils les plus importants et largement utilisés sur Internet aujourd'hui. 

Vous utilisez un Système de Gestion de Bases de Données (SGBD) pour stocker les données que vous collectez à partir de diverses sources, et SQL pour manipuler et accéder aux données spécifiques que vous souhaitez de manière efficace.

De nombreuses entreprises utilisent ces outils pour augmenter leurs ventes et améliorer leurs produits. D'autres institutions comme les écoles et les hôpitaux les utilisent également pour améliorer leurs services administratifs.

Dans cet article, vous apprendrez :

* Les bases des SGBD et SQL
* Les fonctionnalités les plus importantes des SGBD et SQL
* Les raisons pour lesquelles vous devriez apprendre les SGBD et SQL.

## Que fait un SGBD ?

SGBD signifie Système de Gestion de Bases de Données, comme nous l'avons mentionné ci-dessus. [SQL](https://www.freecodecamp.org/news/learn-sql-free-relational-database-courses-for-beginners/) signifie Langage de Requête Structuré.

Si vous avez beaucoup de données à stocker, vous ne voulez pas simplement les garder n'importe où – sinon, il n'y aurait aucun sens à ce que cette énorme quantité de données signifie ou puisse vous dire. C'est pourquoi nous utilisons un SGBD. 

Une base de données est essentiellement l'endroit où nous stockons des données qui sont liées les unes aux autres – c'est-à-dire des données inter-reliées. Ces données inter-reliées sont faciles à manipuler. 

Un SGBD est un logiciel qui gère la base de données. Certains des SGBD (logiciels) couramment utilisés sont MS ACCESS, MySQL, Oracle, et autres. 

Supposons que vous avez des données comme différents noms, notes et numéros d'identification d'étudiants. Vous préféreriez probablement avoir ces données dans un beau tableau où une ligne particulière contient les noms, notes et numéros d'identification des étudiants. Et pour vous aider à organiser et lire ces données efficacement, vous voudrez utiliser un SGBD.

L'utilisation d'un SGBD va de pair avec SQL. Cela est dû au fait que lorsque vous stockez des données et souhaitez y accéder et les modifier, vous utiliserez SQL.

Une base de données stocke les données sous diverses formes comme des schémas, vues, tables, rapports, et plus encore.

## Types de SGBD

Il existe deux types de SGBD.

Tout d'abord, vous avez les Bases de Données Relationnelles (SGBDR). Dans ces types de bases de données, les données sont stockées sous forme de tables par le logiciel. Dans un SGBDR, chaque ligne contient des données d'une seule entité.

Certains des SGBDR couramment utilisés sont MySQL, MSSQL, Oracle, et autres.

Ensuite, vous avez les Bases de Données Non Relationnelles. Dans ces bases de données, les données sont stockées sous forme de paires clé-valeur.

Certains des SGBD Non Relationnels couramment utilisés sont MongoDB, Amazon, Redis, et autres.

### Composants d'un SGBD

Il y a principalement quatre composants d'un SGBD que vous pouvez comprendre en regardant l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-11-at-1.54.06-PM.png)

Vous avez vos Utilisateurs. Il peut y avoir plusieurs utilisateurs, comme quelqu'un qui gère la base de données (l'administrateur de la base de données), les développeurs système, et aussi ceux qui sont simplement des utilisateurs réguliers comme le client.

Vous avez également l'Application de la Base de Données. L'application d'une base de données peut être soit départementale, soit personnelle, ou peut être pour un usage interne dans une organisation.

Ensuite, vous avez le SGBD, dont nous avons parlé. Il s'agit d'un logiciel qui aide les utilisateurs à créer la base de données et à accéder aux données qu'elle contient de manière efficace.

Enfin, vous avez la Base de Données, qui est une collection de données stockées sous la forme d'une seule unité. 

Une fonctionnalité importante d'un SGBD est qu'il aide à réduire la redondance dans les données stockées. Avoir les mêmes données stockées à plusieurs endroits dans une base de données est appelé redondance. 

Pour éliminer et réduire la redondance dans la base de données, la normalisation est utilisée.

La normalisation est le processus de structuration des données dans un SGBDR en supprimant les anomalies. Il est important de permettre une récupération facile des données de la base de données ainsi que d'ajouter ou de supprimer des données sans perdre la cohérence.   
  
Cela peut être mis en œuvre à l'aide des "Formes Normales" dans les SGBD. Ces formes normales aident à établir des relations dans une base de données relationnelle au lieu de devoir redéfinir les champs existants encore et encore. De cette manière, la normalisation réduit la redondance.

## Qu'est-ce que SQL ?

SQL est un langage de base de données. SQL est largement utilisé et presque tous les Systèmes de Gestion de Bases de Données Relationnelles peuvent le reconnaître.

SQL contient un ensemble de commandes qui vous permettent de créer une base de données. Vous pouvez également l'utiliser pour exécuter des commandes dans votre Système de Gestion de Bases de Données Relationnelles.

SQL a certains avantages qui l'ont aidé à prospérer depuis les années 1970 jusqu'à aujourd'hui. Il est largement accepté par les personnes et les plateformes, en partie grâce aux fonctionnalités suivantes :

* SQL est rapide
* SQL est un langage de très haut niveau
* SQL est un langage indépendant de la plateforme
* SQL est un langage standardisé
* SQL est un langage portable 

En plus de toutes les fonctionnalités mentionnées ci-dessus, vous avez besoin de presque aucune compétence en codage pour travailler avec SQL.

SQL effectue une variété de tâches comme la création, la modification, la maintenance et la récupération de données, la définition de propriétés, et ainsi de suite. Toutes les tâches sont effectuées en fonction des commandes que vous écrivez, et ces commandes sont regroupées en diverses catégories comme les commandes DDL, les commandes DML, les commandes DCL, et ainsi de suite. 

Discutons de certaines des commandes fréquemment utilisées et de leurs types.

### Commandes DDL

DDL signifie Langage de Définition de Données. Il inclut l'ensemble des commandes que vous utilisez pour effectuer diverses tâches liées à la définition des données. Vous utilisez ces commandes pour spécifier la structure du stockage et les méthodes par lesquelles vous pouvez accéder au système de base de données.

Vous utilisez les commandes DDL pour effectuer les fonctions suivantes :

* Pour créer, supprimer et modifier.
* Pour accorder et révoquer divers rôles et privilèges.
* Commandes de maintenance

Les exemples de commandes DDL incluent `CREATE`, `ALTER`, `DROP`, et `TRUNCATE`.

### Commandes DML

DML signifie Langage de Manipulation de Données. Comme le nom l'indique, il se compose de commandes que vous utilisez pour manipuler les données. 

Vous utilisez ces commandes pour les actions suivantes :

* Suppression
* Insertion
* Récupération
* Modification

Les exemples de commandes DML sont `SELECT`, `INSERT`, `UPDATE`, et `DELETE`.

### Commandes TCL

TCL signifie Langage de Contrôle des Transactions. Comme le nom l'indique, vous utilisez ces commandes pour contrôler et gérer les transactions.

Une unité complète de travail qui implique diverses étapes est appelée une transaction.

Vous utilisez ces commandes pour les objectifs suivants :

* Pour créer des points de sauvegarde
* Pour définir les propriétés de la transaction en cours
* Pour annuler les modifications de la base de données (permanentes)
* Pour apporter des modifications à la base de données (permanentes)

Les exemples de commandes TCL incluent `COMMIT`, `ROLLBACK`, et `SAVE TRANSACTION`.

## Comment écrire des requêtes de base en SQL

Il existe divers mots-clés que vous utilisez en SQL comme SELECT, FROM, WHERE, et autres. Ces mots-clés SQL ne sont pas sensibles à la casse.

Pour créer une table appelée Student qui contient un nom, des numéros de rôle et des notes, vous pouvez écrire : 

```sql
CREATE TABLE student
(Name char(20)  NOT NULL,
Rollno int,
Marks int );
```

Ici, CREATE, TABLE et NOT NULL sont des mots-clés. Vous utilisez CREATE et TABLE pour créer une table et NOT NULL pour spécifier que la colonne ne peut pas être laissée vide lors de la création d'un enregistrement.

Pour faire une requête à partir d'une table, vous écrirez :  

```sql
SELECT what_to_select FROM table_name WHERE condition_to_satisfy.
```

Vous utilisez le mot-clé 'select' pour extraire les informations d'une table. Le mot-clé 'From' sélectionne la table à partir de laquelle les informations doivent être extraites. Le mot-clé 'where' spécifie la condition à remplir.

Par exemple, supposons que nous voulons récupérer les notes de la table student qui contient des données pour les notes, les numéros de rôle et les noms. La commande serait la suivante :

```sql
SELECT Name FROM student WHERE marks>95
```

Si vous voulez en savoir plus sur SQL pour les débutants, vous pouvez [consulter cette feuille de triche](https://www.freecodecamp.org/news/learn-sql-in-10-minutes/) qui vous apprendra les bases assez rapidement.

Vous pouvez également suivre ce [Cours sur les Bases de Données Relationnelles pour Débutants](https://www.freecodecamp.org/news/learn-sql-free-relational-database-courses-for-beginners/) pour obtenir une compréhension plus solide du langage de requête.

## Pourquoi les SGBD et SQL sont-ils importants ?

Savoir travailler avec les SGBD et SQL sont deux des compétences les plus critiques dans le monde d'aujourd'hui. Après tout, vous savez ce qu'ils disent - "Les données sont le nouveau pétrole." Vous devriez donc savoir comment travailler avec efficacement.

Voici quelques raisons pour lesquelles vous devriez apprendre à utiliser au moins un SGBD et SQL.

## Raisons d'apprendre à utiliser un SGBD

### Si vous stockez une quantité extrêmement grande de données

Si votre organisation doit stocker une énorme quantité de données, vous voudrez utiliser un SGBD pour les garder organisées et pouvoir y accéder facilement. 

Les SGBD stockent les données de manière très logique, ce qui facilite grandement le travail avec une quantité énorme de données. Vous pouvez en savoir plus sur les systèmes de gestion de bases de données dans [ce tutoriel de freeCodeCamp](https://www.freecodecamp.org/news/sql-and-databases-full-course/), [dans ce Wiki](https://en.wikipedia.org/wiki/SQL), [et sur Scaler](https://www.scaler.com/topics/dbms/) pour une meilleure compréhension du stockage des données dans les SGBD.

### Si vous faites de l'extraction de données

L'extraction de données est le processus d'extraction de données utilisables qui incluent uniquement des informations pertinentes à partir d'un très grand ensemble de données. En utilisant un SGBD, vous pouvez effectuer l'extraction de données très efficacement.   
  
Pour gérer les données, vous utilisez [les opérations CRUD](https://www.freecodecamp.org/news/learn-crud-operations-in-javascript-by-building-todo-app/) qui signifient Créer, Lire, Mettre à jour et Supprimer. Vous pouvez effectuer ces opérations avec un SGBD facilement et efficacement.

### Contrainte d'intégrité et évolutivité

Les données que vous stockez dans votre base de données satisfont les contraintes d'intégrité. Les contraintes d'intégrité sont l'ensemble des règles qui sont déjà définies et qui sont responsables du maintien de la qualité et de la cohérence des données dans cette base de données. Le SGBD s'assure que les données sont cohérentes.   
  
L'évolutivité est une autre fonctionnalité importante d'un SGBD. Vous pouvez insérer beaucoup de données dans une base de données très facilement et elles seront accessibles à l'utilisateur rapidement et avec quelques requêtes de base.   
  
Vous n'avez pas besoin d'écrire un nouveau code et de passer beaucoup de temps et d'argent à étendre la même base de données.

### Lorsque vous avez plusieurs interfaces utilisateur

Lorsque vous utilisez un SGBD, vous pouvez avoir plusieurs utilisateurs accéder au système en même temps. Tout comme dans un système d'exploitation UNIX, deux utilisateurs peuvent se connecter à un seul compte en même temps. 

### Sécurité

Les SGBD rendent le stockage des données simple. Vous pouvez également ajouter des permissions de sécurité sur l'accès aux données pour vous assurer que l'accès est restreint et que la confidentialité des données reste intacte.   
  
Les SGBD protègent la confidentialité, la disponibilité, l'intégrité et la cohérence des données qui y sont stockées.   
  
En plus de rendre les données sécurisées, ils réduisent le temps nécessaire pour développer une application et rendent le processus efficace.

### Apprendre un SGBD est une compétence recherchée : 

La plupart des entreprises – grandes ou petites – ont beaucoup de données à traiter. Et elles auront donc besoin de personnes pour les analyser. 

Si vous savez comment utiliser un SGBD, vous pouvez utiliser ces compétences dans presque toutes les technologies orientées données. Donc, une fois que vous avez appris les SGBD, il sera facile de travailler sur n'importe quelle technologie basée sur les données.

## Raisons d'apprendre SQL

Puisque SQL est un langage utilisé pour la gestion des bases de données, certains des points ci-dessus s'appliquent également à son apprentissage (comme le stockage des données, l'extraction de données, etc.). 

Voici quelques raisons supplémentaires pour lesquelles vous devriez apprendre SQL.

### SQL est relativement facile à apprendre

SQL est assez facile à apprendre dans le contexte de la gestion des bases de données. Les requêtes SQL ressemblent à l'anglais simple que nous utilisons dans notre vie quotidienne. Par exemple, si nous voulons créer une table nommée Topics, nous devons simplement utiliser la commande : 

```sql
CREATE TABLE Topics;
```

Comprendre comment fonctionne un ordinateur vous aide à apprendre d'autres compétences liées aux ordinateurs comme n'importe quel langage de programmation, les logiciels de tableur comme MS Excel, et les logiciels de traitement de texte comme MS Word. 

Vous utilisez également SQL pour gérer les données sur diverses plateformes comme [SQLite](https://www.sqlite.org/). 

### SQL est standardisé

SQL a été développé dans les années 1970 et a été largement utilisé pendant plus de 50 ans sans changements significatifs.  
  
Cela en fait une compétence standard pour travailler avec les données, donc généralement lorsque vous postulez à un emploi, ils utiliseront SQL pour le stockage et la gestion des données.   
  
Cette standardisation générale le rend également plus facile à apprendre car vous n'avez pas besoin de mettre à jour constamment vos connaissances pour le maîtriser.

### SQL est facile à dépanner

Toute erreur que vous obtenez en utilisant SQL affichera un message clair sur ce qui se passe en anglais très simple. 

Par exemple, si vous essayez d'utiliser une table ou une base de données qui n'existe pas, elle affichera l'erreur que la table ou la base de données que vous essayez d'accéder n'existe pas. 

Il y a le concept de gestion des exceptions en SQL également, comme dans n'importe quel autre langage de programmation. 

La gestion des exceptions est utilisée pour gérer les erreurs d'exécution des requêtes avec la structure TRY CATCH. Le bloc TRY est utilisé pour spécifier l'ensemble des instructions qui doivent être vérifiées pour une erreur, tandis que le bloc CATCH exécute certaines instructions en cas d'erreur. La gestion des exceptions est cruciale pour écrire un code sans bogues.

### Facile à manipuler les données 

La manipulation des données fait référence à l'ajout (ou insertion), à la suppression et à la modification (mise à jour) des données dans une base de données.  
  
Les données que vous stockez dans SQL sont dynamiques par nature, ce qui vous permet de manipuler les données à tout moment. 

Vous pouvez également récupérer des données facilement en utilisant une commande SQL en une seule ligne. Et si vous voulez présenter les données sous forme de graphiques ou de tableaux, alors SQL joue un rôle clé dans cela et facilite la visualisation des données pour vous. 

### Partage de données entre client et serveur

Lorsque vous utilisez une application, les données stockées dans le système de gestion de base de données sont récupérées en fonction de l'option sélectionnée par l'utilisateur.   
  
Pour créer et gérer les serveurs, SQL est utilisé. SQL est utilisé pour naviguer à travers la grande quantité de données stockées dans le système de gestion de base de données.   


### Facile à synchroniser les données de plusieurs sources

Vous rencontrerez de nombreux cas où vous devrez obtenir des données de plusieurs sources et les combiner pour obtenir le résultat souhaité. Cela signifie que vous traiterez avec des résultats de plusieurs sources en même temps, ce qui peut être chronophage et fastidieux.

Mais lorsque vous utilisez SQL, il est beaucoup plus facile de gérer les données de plusieurs sources en même temps et de les combiner pour obtenir le résultat souhaité. 

En SQL, vous pouvez utiliser l'opération UNION pour combiner les données, comme ceci :

```sql
SELECT name FROM customers
UNION
SELECT order_id FROM orders;
```

L'utilisation de cela combine les colonnes "name" et "order_id" des tables "customers" et "orders", respectivement, et rend la table combinée.

### Flexibilité, polyvalence et analyse de données

SQL est un langage de programmation, mais la portée de ce langage n'est pas limitée aux seules tâches de programmation.   
  
Vous pouvez l'utiliser à diverses fins comme dans le secteur financier et dans les ventes et le marketing, également. En exécutant quelques requêtes, vous pouvez obtenir les données dont vous avez besoin et les analyser pour vos besoins. 

Il existe divers rôles spécifiques à SQL comme développeur SQL, administrateur de base de données SQL, testeur de base de données, analyste de données SQL DBA, modélisateur de données, et plus encore. Vous pouvez en savoir plus sur les insights salariaux [ici](https://www.glassdoor.co.in/Salaries/sql-developer-salary-SRCH_KO0,13.htm).

Un autre rôle important est celui d'analyste de données. Le processus de nettoyage, de modélisation et de transformation des données pour en tirer des conclusions basées sur certaines informations est appelé analyse de données. 

Le rôle d'un analyste de données est important dans toute organisation car il aide à analyser les tendances et à prendre des décisions rapides et flexibles sur la base des données disponibles. 

SQL et SGBD sont deux des compétences les plus demandées pour l'analyse de données.

## Comment les SGBD et SQL fonctionnent ensemble

Les SGBD et SQL sont interdépendants et coopèrent pour organiser les données et les rendre accessibles. Maintenant, comprenons comment SQL fonctionne en synchronisation avec un Système de Gestion de Bases de Données.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/How-Does-SQL-Work.png)
_Comment SQL + SGBD fonctionnent_

  
SQL est la manière dont vous interagissez avec le système de gestion de base de données. Vous l'utilisez pour récupérer, insérer, mettre à jour ou supprimer des données (opérations CRUD), entre autres.

Lorsque vous exécutez une commande SQL, le SGBD détermine le moyen le plus efficace d'exécuter cette commande. L'interprétation de la tâche à effectuer est déterminée par le moteur SQL.

Le moteur de requête classique est utilisé pour gérer toutes les requêtes non-SQL, mais il ne gérera aucun fichier logique.

Le processeur de requêtes interprète les requêtes de l'utilisateur et les traduit dans un format compréhensible par la base de données.

L'analyseur est utilisé à des fins de traduction (dans le traitement des requêtes). Il vérifie également la syntaxe de la requête et recherche les erreurs, si présentes.

Le moteur d'optimisation, comme son nom l'indique, optimise les performances de la base de données à l'aide d'informations utiles.

Le moteur SGBD est le composant logiciel sous-jacent pour effectuer les opérations CRUD sur la base de données.

Le gestionnaire de fichiers est utilisé pour gérer les fichiers dans la base de données, un à la fois.

Et le gestionnaire de transactions est utilisé pour gérer les transactions afin de maintenir la concurrence lors de l'accès aux données.

## Conclusion

Dans cet article, nous avons discuté des bases des SGBD et SQL et des raisons pour lesquelles vous devriez apprendre ces compétences. 

Nous avons discuté du but et de l'importance des SGBD et SQL, de ce pour quoi ils sont utilisés, et de ce que font les professionnels qui travaillent avec les bases de données et SQL.

Après avoir lu cet article, vous avez une bonne compréhension de ce que la connaissance des SGBD et SQL peut vous apporter.  
  
Bon apprentissage !