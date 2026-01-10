---
title: Apprendre les bases des bases de données relationnelles – Concepts clés pour
  débutants
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2025-01-13T16:25:34.318Z'
originalURL: https://freecodecamp.org/news/learn-relational-database-basics-key-concepts-for-beginners
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1736785487594/67bc81b6-1af8-46a0-8a7a-489896879828.png
tags:
- name: Databases
  slug: databases
- name: Relational Database
  slug: relational-database
- name: SQL
  slug: sql
- name: Beginner Developers
  slug: beginners
seo_title: Apprendre les bases des bases de données relationnelles – Concepts clés
  pour débutants
seo_desc: In today’s digital world, data is everywhere, and it’s at the heart of most
  modern applications. Databases are the unsung heroes that keep it all organised
  and accessible. Many sites use databases, from social media platforms to online
  shopping retai...
---

Dans le monde numérique d'aujourd'hui, les données sont partout et constituent le cœur de la plupart des applications modernes. Les bases de données sont les héros méconnus qui maintiennent tout organisé et accessible. De nombreux sites utilisent des bases de données, des plateformes de médias sociaux aux détaillants en ligne.  
  
Mais qu'est-ce qu'une base de données exactement et comment fonctionne-t-elle ? Cet article vous donnera une compréhension fondamentale des concepts clés des bases de données, tels que :

* Ce que sont les bases de données
    
* Les différents modèles de bases de données
    
* Les systèmes de gestion de bases de données (SGBD)
    
* Comment fonctionnent les modèles de bases de données relationnelles
    
* Les bases du langage de requête structuré (SQL)
    

Que vous soyez débutant ou que vous cherchiez simplement à rafraîchir vos connaissances, cet article vous aidera à apprendre les bases.

## Qu'est-ce qu'une base de données ?

Une base de données est une collection d'informations – des informations qui sont de préférence liées et organisées. Cela signifie qu'une base de données peut prendre n'importe quelle forme. Elle pourrait être une pile de dossiers papier dans un bureau, une grande feuille Excel, ou sur un ordinateur (ce qui est le plus probable de nos jours). Mais en termes les plus basiques, une base de données vous aide simplement à stocker des données – donc, en fin de compte, vous pouvez décider de ce qu'elle est.

Dans le monde numérique, une base de données se compose de fichiers physiques sur votre ordinateur ou dans un ordinateur cloud. Ces fichiers sont installés (ou téléchargés) lorsque vous configurez le logiciel de base de données sur votre ordinateur.

Une base de données vous permet d'enregistrer, organiser, gérer, récupérer et mettre à jour ces données de manière efficace. Une base de données est généralement structurée, organisée et contient des informations liées, sinon ce ne sera qu'un tas de données aléatoires.

La structure d'une base de données se compose de deux parties principales, les **données** et les **métadonnées**.

* Les **données** sont les informations réelles stockées dans la base de données. Par exemple, une base de données de joueurs de football contiendrait des informations sur les joueurs comme leurs noms, âges, clubs, etc.
    
* Les **métadonnées** sont la description structurelle des données dans une base de données. Elles décrivent les noms des **champs** utilisés pour stocker les données, la longueur de ces champs (le cas échéant) et leurs **types de données**. Les métadonnées donnent une structure et une organisation aux données brutes.
    

## Comment mettre à jour une base de données

Vous pouvez apporter des modifications aux différentes parties d'une base de données en utilisant diverses commandes. Il existe deux types généraux de commandes :

### **Langage de définition de données (DDL)**

Tout d'abord, nous avons le langage de définition de données, ou DDL. Il est composé de commandes qui définissent ou modifient la forme ou la structure des données dans la base de données. Ces commandes affectent la partie métadonnées d'une base de données.

Vous pourriez apporter des modifications comme la création de nouvelles tables dans une base de données relationnelle, la modification de la forme des documents dans une base de données basée sur des documents en ajoutant de nouveaux champs, ou la suppression d'un graphique entier dans une base de données de graphes. Le DDL pourrait définir un champ comme un type de données spécifique, par exemple, le type "date", garantissant que seules des dates valides peuvent être saisies.

### **Langage de manipulation de données (DML)**

Nous avons également le langage de manipulation de données, ou DML. Il est composé de commandes qui interagissent avec les données stockées dans la base de données. Ces commandes n'affectent pas la structure des données, mais plutôt les données elles-mêmes. Ces commandes n'affectent que la partie données d'une base de données.

Parmi les choses que vous pouvez faire avec le DML, on trouve la lecture de données à partir d'une base de données, l'ajout de nouvelles données à la base de données, l'édition de données et la suppression de données.

Des applications comme [TablePlus](https://tableplus.com) vous permettent de voir les données et les métadonnées dans une base de données. Par exemple, les parties données et métadonnées d'une application de football pourraient ressembler aux images ci-dessous, respectivement :

![données de la base de données](https://cdn.hashnode.com/res/hashnode/image/upload/v1735566678439/3f33f183-ebe5-40a3-98d1-d8462dab9dbb.png align="center")

![métadonnées de la base de données](https://cdn.hashnode.com/res/hashnode/image/upload/v1735566701148/894a87f3-3bc7-43d9-908a-dbb2e92710c3.png align="center")

Un **type de données** définit quel type d'informations peut être stocké dans un champ. Les types de données aident les ordinateurs à comprendre comment stocker, traiter et utiliser les données de manière efficace.

Ainsi, un champ dans une table avec un type de données `date` ne pourra stocker que des enregistrements de dates et générera une erreur si vous essayez de stocker autre chose, comme un nom. Il en va de même pour un champ avec un type de données `number` – il n'acceptera que des nombres et peut être configuré pour accepter des valeurs dans une plage ou jusqu'à un certain nombre de décimales.

Les types de données courants incluent `varchar` pour les données pouvant contenir différents caractères (texte + nombres), `date` pour les valeurs de date, `int` pour les nombres entiers, etc. Vous pouvez trouver d'autres types de données de base de données courants [ici](https://teachcomputerscience.com/database-data-types/).

## Qu'est-ce qu'un modèle de base de données ?

Un modèle de base de données est un concept utilisé pour décrire les informations stockées dans une base de données. Pensez-y comme au plan d'un bâtiment conçu par un architecte. Il détaille toutes les tables, colonnes et types de données de la base de données. Mais en soi, ce n'est pas une entité physique comme la base de données. Un modèle de base de données détermine comment les données sont représentées logiquement et accessibles.

Les modèles de base de données définissent si les données sont stockées dans des tables utilisant des lignes et des colonnes, ou dans des objets de type JSON. Ils définissent également comment les données sont liées, comment vous pouvez les interroger et comment vous les gérez. Les modèles de base de données sont souvent choisis (et souvent développés) pour répondre à des besoins spécifiques de données/applications.

### Modèles de bases de données populaires :

**Modèle relationnel** : Le modèle relationnel est le modèle de base de données le plus populaire. Ce modèle utilise des tables avec des lignes et des colonnes pour stocker les données. Ce modèle utilise le langage SQL pour gérer les données.

Des exemples de bases de données relationnelles incluent MySQL, PostgreSQL et SQLite. Ce modèle est couramment utilisé pour des applications généralistes nécessitant des données structurées, souvent liées, et des requêtes complexes. Le reste de l'article se concentrera sur ce modèle.

**Modèle de document** : Les données sont stockées sous forme de documents, souvent au format JSON ou XML, dans ce modèle. Des bases de données comme MongoDB et CouchDB utilisent ce modèle. Les bases de données de documents favorisent la flexibilité avec leurs structures de type JSON, et elles sont couramment utilisées dans des applications traitant des données semi-structurées ou hiérarchiques, où la flexibilité est essentielle.

**Modèle clé-valeur** : Dans ce modèle, les données sont stockées sous forme de paires clé-valeur simples, comme dans une carte en programmation. Ce modèle est utilisé par Redis et DynamoDB. En raison de la simplicité de ce modèle, il est utilisé dans des scénarios de haute performance pour des recherches simples ou la mise en cache.

**Modèle de graphe** : Ce modèle utilise des nœuds (entités) et des arêtes (relations) pour gérer les données. Neo4j et Amazon Neptune sont des exemples de bases de données utilisant ce modèle. La forme des nœuds et des arêtes dans le modèle de graphe en fait un choix courant dans les applications impliquant des relations ou des connexions entre des points de données.

Il existe de nombreux autres modèles de bases de données. Vous pouvez les trouver et les étudier [ici](https://www.lucidchart.com/pages/database-diagram/database-models) si vous souhaitez plus d'informations.

## Comment fonctionnent les bases de données relationnelles ?

> Une base de données relationnelle a la capacité d'établir des liens – ou des relations – entre des informations en joignant des tables, ce qui facilite la compréhension et l'obtention d'informations sur la relation entre divers points de données. - [Google](https://cloud.google.com/learn/what-is-a-relational-database?hl=en)

Le modèle de base de données relationnelle a été développé comme une amélioration d'un modèle de base de données plus ancien, le modèle de base de données hiérarchique. Les bases de données relationnelles s'appuient sur celui-ci et améliorent certaines de ses restrictions et relations. Les tables dans un modèle de base de données relationnelle sont souvent appelées **relations**.

Chaque ligne dans une table de base de données représente un seul **enregistrement** dans la table. La ligne raconte toute l'histoire des données. Elle contient des données pour toutes les colonnes de cette table pour une entité spécifique.

Par exemple, dans une table stockant des informations sur des joueurs de football, chaque ligne représente un joueur et inclura des détails sur le joueur comme le nom, l'âge, le pays, etc. Les lignes sont également parfois appelées **enregistrements** ou **tuples** en terminologie de base de données.

Chaque colonne liste un attribut de l'enregistrement en question, tel que le nom, l'âge ou le pays. La colonne ne raconte qu'une petite partie de l'histoire. Chaque colonne a un nom et un type de données, et elle s'applique à toutes les lignes de la table. Ces colonnes pourraient également avoir des contraintes en plus de leurs types de données. Ces contraintes pourraient être aussi simples que la contrainte ***NOT NULL*** qui indique que la colonne ne peut pas être vide sur aucune ligne, ou aussi complexes que vous le définissez.

Par exemple, dans une table de joueurs de football, les colonnes pourraient inclure "nom", "âge" et "pays". Toutes les lignes de la table auront des valeurs sous ces colonnes pour leurs attributs respectifs. Dans certains contextes, les **colonnes** sont également appelées **champs**.

La partie "relationnelle" du nom des bases de données relationnelles est souvent attribuée au fait que ce modèle se concentre sur la manière dont les données sont liées à d'autres données, et comment les tables sont liées les unes aux autres. Par exemple, les tables peuvent être liées (en relation) ensemble. Les tables peuvent également être indépendantes.

Malgré cette flexibilité avec les relations, les données dans une table peuvent être accessibles directement sans avoir connaissance des tables liées ou non liées. Vous pouvez facilement accéder aux **enregistrements** tant que vous savez ce que vous cherchez. Les clés **primaires** et **étrangères** sont utilisées dans le modèle relationnel pour gérer ces relations.

## Qu'est-ce qu'un système de gestion de base de données (SGBD) ?

Un système de gestion de base de données (SGBD) est une collection de programmes pour gérer et communiquer avec un moteur de base de données sous-jacent. En termes plus simples, un SGBD est le moteur de base de données couplé avec tous les outils supplémentaires qui l'accompagnent.

Un SGBD vous aide à créer, gérer et utiliser des bases de données. Il fournit une abstraction sur le moteur de base de données et vous permet de stocker, mettre à jour et récupérer des données de manière plus facile et sécurisée.

Les outils qui accompagnent un SGBD peuvent inclure, mais ne sont pas toujours limités à :

* Des outils frontaux (comme une interface de requête ou un panneau d'administration) qui vous aident à exécuter des requêtes et à visualiser les données résultantes dans la base de données
    
* Des outils de sauvegarde et de récupération qui fonctionnent en arrière-plan avec peu ou pas d'interaction utilisateur
    
* Des outils de sécurité pour la gestion de l'accès des utilisateurs (rôles et permissions)
    
* Et des outils d'importation ou d'exportation de données.
    

Et comme vous pouvez l'imaginer, les SGBD sont généralement spécifiques à un modèle, donc il existe des SGBD axés sur le modèle de base de données relationnelle appelés SGBDR, où le "R" signifie Relationnel. Des exemples de SGBDR populaires incluent MySQL, PostgreSQL, Oracle et Microsoft SQL Server. Les SGBDR utilisent **SQL** (Structured Query Language) pour interagir avec les données.

## Bases de SQL

> Le langage de requête structuré (SQL) est un langage de programmation pour stocker et traiter des informations dans une base de données relationnelle. Vous pouvez utiliser des instructions SQL pour stocker, mettre à jour, supprimer, rechercher et récupérer des informations à partir d'une base de données. Vous pouvez également utiliser SQL pour maintenir et optimiser les performances de la base de données. - [Amazon](https://aws.amazon.com/what-is/sql/)

Il sert d'interface principale pour interagir avec les bases de données, permettant aux utilisateurs d'effectuer diverses opérations telles que la création, la modification, l'interrogation et la suppression de données et de structures de bases de données. C'est la base sur laquelle les SGBDR comme MySQL, PostgreSQL et SQLite sont construits, avec leurs propres optimisations et extensions.

Dans cette section, nous allons examiner quelques commandes SQL de base, avec des exemples pratiques.

### Commandes DDL

#### 1\. `CREATE`

Il s'agit de la commande SQL utilisée pour créer et définir de nouveaux objets de base de données. Elle fait partie du **langage de définition de données (DDL)**, et sa fonction principale est d'établir la structure ou le schéma de la base de données.

Vous pouvez utiliser cette commande pour faire ce qui suit (entre autres utilisations) :

* Créer de nouvelles bases de données
    
* Créer de nouvelles tables
    
* Créer un nouvel index dans une table
    
* Créer des vues
    
* Créer un utilisateur avec des droits d'accès spécifiques
    

`CREATE` est le plus couramment utilisé pour créer une table dans une base de données, ou pour créer la base de données elle-même (bien que vous fassiez généralement cela en utilisant les options GUI que le SGBDR fournit).

Cette commande a la structure suivante :

```sql
CREATE OBJECT_TYPE object_name (optional_further_arguments)
```

Le `ENTITY_TYPE` est un espace réservé et pourrait être `DATABASE`, `TABLE`, `VIEW`, etc. de la liste des objets de base de données. Le `entity_name` définit le nom de l'objet créé. Et enfin, le `optional_further_arguments` est utilisé pour montrer que certains objets n'ont besoin que d'un nom pour être créés, tandis que d'autres comme les tables ont besoin de plus de contexte sur les colonnes de la table.

Ainsi, en fonction de notre exemple d'application de football, la création de la base de données `football_db` ci-dessus impliquerait d'abord de créer la base de données, comme ceci :

```sql
CREATE DATABASE football_db;
```

![CREATE DATABASE](https://cdn.hashnode.com/res/hashnode/image/upload/v1736520482758/7231e225-2dcc-407a-95b4-0684eca078d6.png align="center")

Cette commande crée une nouvelle base de données avec le nom fourni, `football_db`. Ensuite, en utilisant la commande `CREATE` suivie du type d'objet `TABLE`, vous pouvez créer une table `players`, comme ceci :

```sql
CREATE TABLE `players` (
	`id` int PRIMARY KEY AUTO_INCREMENT,
	`name` varchar(100) NOT NULL,
	`age` int NOT NULL,
	`country` varchar(100) NOT NULL,
	`level` enum('Academy', 'Amateur', 'SemiPro', 'Professional') NOT NULL,
	`position` enum('Goalkeeper', 'Defender', 'Midfielder', 'Striker') NOT NULL,
	`foot` varchar(6) NOT NULL,
	`club` varchar(100) NOT NULL,
	`scores` json NOT NULL,
	`jerseyNumber` int NOT NULL
);
```

![CREATE players TABLE](https://cdn.hashnode.com/res/hashnode/image/upload/v1736522720503/57b09674-8058-4d86-80ea-4d942276bba0.png align="center")

La commande crée une table appelée `players`, et définit les colonnes (`id`, `name`, `age`, `country`, `level`, `position`, `foot`, `club`, `scores`, `jerseyNumber`) avec leurs types de données (`int`, `varchar`, `enum`, `json`). Elle définit également leurs contraintes (`PRIMARY KEY`, `AUTO_INCREMENT`, `NOT NULL`).

#### 2\. `ALTER`

Cette commande modifie la structure d'une table existante. Cette commande est polyvalente et permet une large gamme de modifications de table. Cela inclut l'ajout, la suppression, la modification et le renommage de colonnes, ainsi que la gestion des contraintes et des index.

Pour ajouter une nouvelle colonne `height` à la table `players` nouvellement créée, vous pouvez utiliser la commande `ALTER` comme ceci :

```sql
ALTER TABLE players
ADD height INT NOT NULL;
```

![ALTER players TABLE](https://cdn.hashnode.com/res/hashnode/image/upload/v1736523536743/e45d03ec-af8c-463f-ac2c-e34e36939ea1.png align="center")

La commande s'exécute avec succès et la nouvelle colonne, définie comme une colonne entière, est ajoutée.

#### 3\. `DROP`

Cette commande supprime une table ou une base de données existante. Lorsque vous utilisez la commande `DROP`, elle supprime complètement l'objet de la base de données, et cette action est irréversible. Vous pouvez l'utiliser pour supprimer des bases de données, des tables et des index.

Si vous n'utilisez plus jamais la table `players`, vous pouvez facilement la supprimer en utilisant la commande `DROP` comme ceci :

```sql
DROP TABLE players;
```

#### 4\. `TRUNCATE`

Cette commande supprime toutes les données d'une table tout en préservant sa structure. Ce même résultat peut être obtenu en utilisant la commande DML `DELETE`.

### Commandes DML

Ces commandes DML sont fondamentales pour les **opérations CRUD**, qui signifient **Créer, Lire, Mettre à jour et Supprimer** – les actions de base que vous effectuez avec les données dans une base de données.

#### 1\. `INSERT`

Ajoute un nouvel enregistrement à la base de données. Il s'agit de la partie Créer de CRUD.

La commande a la structure suivante :

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

Le `INSERT INTO` est la première partie de la requête, il est obligatoire et suivi du nom de la table dans laquelle insérer. Le nom de la table dans laquelle insérer est représenté par l'espace réservé `table_name`. Le nom peut ensuite être suivi d'une liste de colonnes à remplir, ou du mot-clé `VALUES`. Dans le cas où les colonnes à remplir sont listées, la liste des valeurs doit avoir la même longueur que la longueur des colonnes fournies, car chaque entrée dans les deux listes sera mappée. Dans le cas où les colonnes à remplir ne sont pas listées, les éléments de la liste des valeurs sont mappés aux colonnes de la base de données, et chaque colonne devra être fournie. La commande permet également l'insertion de plusieurs enregistrements en même temps, en suivant les mêmes règles que les insertions simples, avec plusieurs listes de valeurs à insérer séparées par des virgules.

Pour ajouter quelques joueurs à la table `players` afin d'obtenir un résultat similaire à celui de la première capture d'écran, vous pouvez utiliser quelques commandes d'insertion comme ceci :

```sql
INSERT INTO
	`players` (`id`, `name`, `age`, `country`, `level`, `position`, `foot`, `club`, `scores`, `jerseyNumber`, `height`)
VALUES
	(1, 'Christiano Ronaldo', 36, 'Portugal', 'Professional', 'Striker', 'Right', 'Manchester United', '\"4, 3, 5, 2, 4\"', 7, 187),
	(2, 'Alisson Becker', 31, 'Brazil', 'Professional', 'Goalkeeper', 'Right', 'Liverpool', '\"5, 6, 7, 8, 9\"', 1, 193),
	(3, 'John Stones', 30, 'England', 'Professional', 'Defender', 'Right', 'Manchester City', '\"4, 5, 6, 7, 8\"', 5, 188),
	(4, 'Kevin DeBruyne', 33, 'Belgium', 'Professional', 'Midfielder', 'Right', 'Manchester City', '\"9, 8, 7, 6, 5\"', 17, 181),
	(5, 'Erling Haaland', 24, 'Norway', 'Professional', 'Striker', 'Right', 'Manchester City', '\"10, 9, 8, 7, 6\"', 9, 194),
	(6, 'Chris Waddle', 20, 'England', 'SemiPro', 'Midfielder', 'Left', 'Tow Law Town', '\"3, 4, 5, 6, 7\"', 11, 183),
	(7, 'Ian Wright', 25, 'England', 'SemiPro', 'Striker', 'Right', 'Greenwich Borough', '\"4, 5, 6, 7, 8\"', 8, 175),
	(8, 'Charlie Austin', 34, 'England', 'SemiPro', 'Striker', 'Right', 'Poole Town', '\"5, 6, 7, 8, 9\"', 9, 188),
	(9, 'Troy Deeney', 33, 'England', 'SemiPro', 'Striker', 'Right', 'Chelmsley Town', '\"6, 7, 8, 9, 10\"', 9, 183),
	(10, 'Rickie Lambert', 39, 'England', 'SemiPro', 'Striker', 'Right', 'Macclesfield Town', '\"7, 8, 9, 10, 11\"', 9, 187);
```

![INSERT INTO players TABLE](https://cdn.hashnode.com/res/hashnode/image/upload/v1736525270444/ce1739aa-7fef-48d0-b61a-6cee1267ab1a.png align="center")

#### 2\. `SELECT`

La commande `SELECT` a la syntaxe de base suivante :

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

La commande comprend les parties suivantes :

* `SELECT` est le mot-clé obligatoire qui commence chaque requête,
    
* `column1, column2,  0085` est un espace réservé pour la liste des colonnes à récupérer. Cela est particulièrement utile lorsque vous traitez avec de grandes tables, car vous ne souhaitez pas toujours afficher toutes les colonnes à chaque fois. Pour afficher toutes les colonnes, remplacez la liste par le caractère `*`.
    
* `FROM` est un autre mot-clé obligatoire qui est suivi du nom de la table à partir de laquelle récupérer les données,
    
* `table_name` est le nom de la table à partir de laquelle les données doivent provenir.
    
* `WHERE condition` est l'une des commandes optionnelles qui peuvent être attachées à la commande `SELECT`. Elle est utilisée pour filtrer les enregistrements selon des conditions spécifiques.
    

Il s'agit de la partie Lire de CRUD. La forme la plus simple de la commande `SELECT` est utilisée pour afficher tous les enregistrements dans une table (toutes les colonnes et lignes) :

```sql
SELECT * FROM players;
```

![SELECT ALL players](https://cdn.hashnode.com/res/hashnode/image/upload/v1736526168218/a8b4c51c-afb6-4228-885b-2620bd99cf93.png align="center")

#### 3\. `UPDATE`

La commande `UPDATE` modifie les enregistrements existants dans la base de données. Il s'agit de la partie Mettre à jour de CRUD.

Pour mettre à jour les détails de Christiano Ronaldo pour qu'ils soient plus précis, vous pouvez utiliser la commande `UPDATE` comme ceci :

```sql
UPDATE `players`
SET
	`name` = 'Cristiano Ronaldo',
	`age` = 38,
	`club` = 'Al Nassr'
WHERE
	`id` = 1;
```

![UPDATE player record](https://cdn.hashnode.com/res/hashnode/image/upload/v1736526962015/55dd1f1d-a755-40fe-90d2-9975b8df7ba1.png align="center")

Cette commande modifie légèrement son nom, son club de Manchester United à son club actuel d'Al Nassr, et met à jour son âge à 38 ans.

#### 4\. `DELETE`

La commande `DELETE` supprime les enregistrements de la base de données. Il s'agit de la partie Supprimer de CRUD.

Elle est syntaxiquement similaire à la commande `SELECT`, avec une syntaxe de base comme ceci :

```sql
DELETE FROM table_name
WHERE condition;
```

Dans cette structure,

* Le mot-clé `DELETE FROM` est le début obligatoire de toute requête de suppression,
    
* Il est suivi du nom de la table à supprimer, représenté par `table_name`.
    
* La `WHERE condition` est optionnelle lorsque toutes les lignes de la table doivent être supprimées. Sinon, elle est utilisée pour spécifier les lignes à supprimer en fonction d'une condition.
    

Pour supprimer les joueurs ne jouant pas au niveau professionnel de la table, vous pouvez utiliser une commande comme ceci :

```sql
DELETE FROM `players`
WHERE `level` != 'Professional';
```

Ce sont les commandes de base que vous utiliserez pour interagir avec les bases de données. Vous pouvez en apprendre davantage sur elles [dans cette feuille de triche des commandes SQL](https://www.freecodecamp.org/news/learn-sql-in-10-minutes/).

## **Résumé**

Les bases de données sont un pilier de la technologie moderne, et la compréhension de leurs concepts fondamentaux peut ouvrir des portes pour construire et gérer des systèmes efficaces et basés sur les données.

Cet article vous a introduit aux bases de ce qu'est une base de données et de comment fonctionnent les modèles de bases de données relationnelles. Vous devriez maintenant avoir les connaissances essentielles pour naviguer dans le monde des bases de données en toute confiance.

Pour approfondir votre compréhension, envisagez d'explorer les éléments suivants :

* **Pratique pratique** : Utilisez des outils comme [TablePlus](https://tableplus.com/) pour interagir avec des bases de données relationnelles.
    
* **Apprendre SQL** : Commencez par des tutoriels SQL adaptés aux débutants comme [ce cours sur la chaîne YouTube de freeCodeCamp](https://www.freecodecamp.org/news/learn-sql-full-course/) ou [cette feuille de triche des commandes SQL](https://www.freecodecamp.org/news/learn-sql-in-10-minutes/).
    
* **Expérimenter avec des bases de données non relationnelles** : Essayez [MongoDB](https://www.freecodecamp.org/news/how-to-start-using-mongodb/) ou [Neo4j](https://www.freecodecamp.org/news/learn-neo4j-database-course/) pour explorer comment fonctionnent d'autres modèles de bases de données.
    

Si vous êtes curieux d'en apprendre davantage, connectez-vous avec moi sur [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris), ou [GitHub](https://github.com/Zubs). Continuons ce voyage ensemble vers la maîtrise des systèmes de bases de données !