---
title: Qu'est-ce qu'une base de données relationnelle ? Définition du SGBDR
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-08-25T22:51:46.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-relational-database-rdbms-definition
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/guerrillabuzz-crypto-pr-IlUq1ruyv0Q-unsplash.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Qu'est-ce qu'une base de données relationnelle ? Définition du SGBDR
seo_desc: "A relational database is a type of database that stores data in tables\
  \ made up of rows and columns. Each table represents a specific object in the database\
  \ like users, products, orders, and so on. \nThe term \"relational\" is the main\
  \ characteristic fea..."
---

Une base de données relationnelle est un type de base de données qui stocke les données dans des tables composées de lignes et de colonnes. Chaque table représente un objet spécifique dans la base de données comme les utilisateurs, les produits, les commandes, et ainsi de suite. 

Le terme "relationnelle" est la caractéristique principale qui rend les bases de données relationnelles uniques. Cela est dû au fait que chaque entité (table) dans une base de données relationnelle peut être "en relation" avec une autre pour créer plus de tables, ce qui rend le flux de données flexible. 

Les colonnes désignent le type spécifique de données qui peut être stocké sous chaque colonne respective. Un exemple serait une table d'utilisateurs avec les colonnes suivantes : Nom, Date de naissance, Téléphone et Pays. 

Vous utilisez des lignes pour remplir les données dans une table de base de données. En utilisant les noms de colonnes ci-dessus comme exemples, nous pouvons remplir les lignes avec des données comme ceci : John Doe, 02-04-1970, 555-777-999, Terre. 

Cela donne :

| Nom   |      Date de naissance      |  Téléphone | Pays |
|----------|:-------------:|------:|-------:|
| John Doe |  02-04-1970 | 555-777-999 |Terre |
| Jane Does |    03-05-1980   |444-222-444 |Nigeria |
| Jade Do | 05-03-1990 |565-784-437 |Angleterre |

Comme vous pouvez le voir ci-dessus, chaque ligne contient des données qui correspondent à son nom de colonne. 

## Qu'est-ce que les clés primaires et les clés étrangères dans une base de données relationnelle ?

La table de la dernière section manque l'un des attributs les plus importants dans une base de données relationnelle — un identifiant/ID unique. 

Les tables sont capables de se relier les unes aux autres en utilisant des identifiants uniques. 

Un bon exemple de l'importance des identifiants est une situation où vous avez deux utilisateurs ou plus avec le même nom effectuant la même action, comme acheter un produit. La seule façon de faire la différence entre ces utilisateurs est d'utiliser leur ID unique. 

Ces identifiants uniques sont généralement appelés **clés** dans une base de données relationnelle.

Dans une base de données relationnelle, vous pouvez avoir soit une clé primaire, soit une clé étrangère. Expliquons ce qu'elles signifient. 

### Qu'est-ce qu'une clé primaire dans une base de données relationnelle ?

Une clé primaire est une colonne dans une colonne de base de données utilisée pour identifier des enregistrements/lignes spécifiques. Chaque ligne doit avoir sa propre clé unique. 

La clé primaire peut être n'importe quel attribut dans la table, comme le numéro de téléphone de l'utilisateur ou toute autre information que l'utilisateur fournit. 

À long terme, l'utilisation d'informations fournies par les utilisateurs comme clé primaire peut devenir préjudiciable car vous pouvez avoir des valeurs en double. Cela rendrait difficile la différenciation des enregistrements.

Dans la plupart des cas, les clés primaires sont générées automatiquement par le système de gestion de base de données lors de la création des enregistrements. Aucune clé primaire particulière ne peut être générée deux fois — cela rend chaque ligne unique. 

Voici un exemple de table avec une clé primaire :

| ID Utilisateur| Nom   |      Date de naissance      |  Téléphone | Pays |
|---:|----------|:-------------:|------:|-------:|
| 1 | John Doe |  02-04-1970 | 555-777-999 |Nigeria |
| 2 | John Doe |    03-05-1980   |444-222-444 |Nigeria |
| 3 | John Doe | 05-03-1990 |565-784-437 |Nigeria |

Dans la table ci-dessus, nous avons trois utilisateurs avec le même nom et le même pays.  

Si ces utilisateurs passent commande et achètent des produits, les différencier par leur nom devient un problème. 

Notez qu'une clé primaire ne doit jamais avoir de valeur nulle.

En utilisant la clé primaire (ID UTILISATEUR), nous rendons chaque utilisateur unique. Cela éliminerait également l'option de faire d'un autre attribut fourni par les utilisateurs — DATE DE NAISSANCE, TÉLÉPHONE — une clé primaire. 

### Qu'est-ce qu'une clé étrangère dans une base de données relationnelle ?

Une clé étrangère est une colonne/groupe de colonnes utilisée pour faire référence/lier à la clé primaire d'une autre table. 

En d'autres termes, c'est la représentation de la clé primaire d'une autre table. 

Voici un exemple pour montrer l'importance des clés étrangères :

| ID Client| Nom   |      Date de naissance      |  Téléphone | Pays |
|---:|----------|:-------------:|------:|-------:|
| 1 | John Doe |  02-04-1970 | 555-777-999 |Nigeria |
| 2 | John Doe |    03-05-1980   |444-222-444 |Nigeria |
| 3 | John Doe | 05-03-1990 |565-784-437 |Nigeria |

Dans la table ci-dessus, nous avons une table d'utilisateurs avec une clé primaire appelée ID CLIENT. 

La table ci-dessous montre les différents produits que les clients peuvent commander : 

| ID Produit| Nom du Produit|
|---:|----------|
| 10 | Pizza |
| 20 | Café |
| 30 | John Doe |

Ensuite, nous allons créer une table pour montrer les commandes passées par les clients. 

| ID Commande | ID Client| Nom du Produit |
|----:|---:|----------|
| 1 | 3 | Pizza |
| 2 | 2 | Pizza |
| 3 | 3 | Café |
| 2 | 1 | Café |

Dans la table ci-dessus, ID CLIENT est une clé étrangère. Elle sert de référence à la clé primaire dans la table des clients.

La table des commandes est plus facile à comprendre car nous pouvons identifier chaque client en utilisant son identifiant unique au lieu de leurs noms similaires. 

Une table peut avoir plus d'une clé étrangère. 

## Exemples de bases de données relationnelles

Voici des exemples de quelques bases de données relationnelles populaires :

* MySQL.
* PostgreSQL.
* Oracle Database.
* Microsoft SQL Server.
* IBM Db2. 
* MariaDB.

Il existe également des bases de données relationnelles basées sur le cloud comme :

* Oracle Cloud.
* Google Cloud SQL.
* IBM Db2 sur Cloud.
* AWS Databases.

## Avantages d'une base de données relationnelle

Dans cette section, nous allons lister et expliquer certaines des caractéristiques d'une base de données relationnelle. 

### Facilité d'utilisation

Interagir avec les données dans une base de données relationnelle est facile et direct. Vous le faites en utilisant SQL (**Structured Query Language**).

### Flexibilité

Vous pouvez facilement mettre à l'échelle une base de données relationnelle à mesure que les données grandissent. Il est également facile d'ajouter, de mettre à jour et de supprimer des données stockées dans la base de données. 

Lorsque des données spécifiques sont stockées dans plusieurs tables, les modifier dans une table met à jour leur valeur pour toutes les autres tables partageant les données.

### Sécurité

Vous pouvez facilement restreindre l'accès à certaines tables dans une base de données relationnelle, la rendant inaccessible aux utilisateurs non autorisés. Vous le faites en utilisant un système de gestion de base de données relationnelle (SGBDR).

Les SGBDR sont principalement utilisés pour créer, lire, mettre à jour et supprimer des données dans une base de données relationnelle. 

### Précision

Avec l'utilisation de clés (primaires et étrangères), chaque morceau de données stocké dans une base de données relationnelle peut être accessible lorsque cela est nécessaire sans le confondre avec un autre.

### Simplicité

La structure des bases de données relationnelles facilite la compréhension du type et du flux de données qui y sont stockées. Vous pouvez également [représenter graphiquement les données stockées dans une base de données](https://www.freecodecamp.org/news/crows-foot-notation-relationship-symbols-and-how-to-read-diagrams/). Cela vous aide à comprendre la relation entre les tables.

## Qu'est-ce qu'un SGBDR ?

SGBDR est l'acronyme de Système de Gestion de Base de Données Relationnelle. Il s'agit d'un programme utilisé pour gérer une base de données relationnelle. 

Il vous permet de créer, lire, mettre à jour et supprimer (opérations CRUD) des données dans une base de données. 

La plupart des SGBDR utilisent SQL pour interagir avec la base de données. SQL est un langage de programmation utilisé pour gérer et effectuer des opérations dans une base de données relationnelle. Il est quelque peu facile à apprendre car sa syntaxe est similaire à la langue anglaise. 

```sql
SELECT * FROM Users;
```

Le code SQL ci-dessus sélectionne toutes les colonnes dans une table appelée `Users`. 

Voici quelques-uns des systèmes de gestion de base de données relationnelle populaires :

* MySQL.
* Microsoft SQL Server.
* SQLite.
* PostgreSQL.

## Résumé

Dans cet article, nous avons parlé des bases de données relationnelles. 

Nous avons vu certaines des caractéristiques d'une base de données relationnelle comme la représentation des données dans des tables avec des lignes et des colonnes, et l'utilisation de clés pour rendre chaque morceau de données unique par rapport aux autres. 

Nous avons également parlé des clés primaires et étrangères avec des exemples pour démontrer comment utiliser chacune. 

Enfin, nous avons parlé de certains des avantages de l'utilisation d'une base de données relationnelle. 

Pour en savoir plus sur les bases de données relationnelles, consultez [la certification en bases de données relationnelles de freeCodeCamp](https://www.freecodecamp.org/learn/relational-database/).

Vous commencerez par apprendre les commandes Bash de base et comment utiliser le terminal pour naviguer et manipuler un système de fichiers.

Vous apprendrez également comment créer et utiliser une base de données relationnelle, et l'utilisation de Git pour le contrôle de version. 

Au fur et à mesure que vous progresserez dans le cours, vous construirez des projets formidables pour vous aider à approfondir vos connaissances sur les bases de données relationnelles. 

Bon codage !