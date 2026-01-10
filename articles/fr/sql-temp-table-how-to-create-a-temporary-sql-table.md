---
title: SQL Temp Table – Comment créer une table SQL temporaire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-31T17:22:54.000Z'
originalURL: https://freecodecamp.org/news/sql-temp-table-how-to-create-a-temporary-sql-table
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Shittu-Olumide-SQL-Temp-Table
seo_title: SQL Temp Table – Comment créer une table SQL temporaire
---

How-to-Create-a-Temporary-SQL-Table.png
tags:
- name: analyse de données
  slug: analyse-de-donnees
- name: base de données
  slug: base-de-donnees
- name: SQL
  slug: sql
seo_title: null
seo_desc: 'Par Shittu Olumide

  SQL, qui signifie Structured Query Language, est un langage de programmation spécialement
  conçu pour gérer et manipuler des bases de données relationnelles.

  Il fournit une manière standardisée d'interagir avec les bases de données et d'effectuer des tâches telles
  que...'
---

Par Shittu Olumide

SQL, qui signifie Structured Query Language, est un langage de programmation spécialement conçu pour gérer et manipuler des bases de données relationnelles.

Il fournit une manière standardisée d'interagir avec les bases de données et d'effectuer des tâches telles que l'interrogation de données, l'insertion, la mise à jour et la suppression d'enregistrements, la création et la modification de structures de bases de données, et plus encore.

SQL est largement utilisé dans le domaine de la gestion des données et joue un rôle crucial dans la manipulation des données dans diverses applications et systèmes. Il permet aux utilisateurs de récupérer des informations spécifiques à partir de bases de données en utilisant des requêtes, et il fournit un ensemble puissant d'outils pour la manipulation, l'analyse et la génération de rapports de données.

## Qu'est-ce qu'une table SQL temporaire ?

Une table SQL temporaire, également connue sous le nom de **table temporaire**, est une table qui est créée et utilisée dans le contexte d'une session ou d'une transaction spécifique dans un système de gestion de base de données. Elle est conçue pour stocker des données temporaires qui sont nécessaires pour une courte durée et ne nécessitent pas de solution de stockage permanente.

Les tables temporaires sont créées à la volée et sont généralement utilisées pour effectuer des calculs complexes, stocker des résultats intermédiaires ou manipuler des sous-ensembles de données pendant l'exécution d'une requête ou d'une série de requêtes.

Ces tables temporaires ont une portée et une durée de vie spécifiques associées. Elles ne sont accessibles que dans la session ou la transaction qui les a créées et sont automatiquement supprimées lorsque la session ou la transaction se termine ou lorsqu'elles sont explicitement supprimées par l'utilisateur.

Cette nature temporaire des tables les rend adaptées à la gestion de données transitoires qui n'ont pas besoin de persister au-delà de la tâche immédiate.

Les tables temporaires en SQL fournissent un moyen pratique de décomposer des problèmes complexes en étapes plus petites et plus gérables. Elles permettent la séparation des étapes de traitement des données, ce qui peut améliorer les performances, améliorer la lisibilité du code et simplifier la logique des requêtes.

Les tables temporaires peuvent être utilisées dans divers systèmes de bases de données tels que MySQL, PostgreSQL, Oracle, SQL Server, et autres, bien que la syntaxe et les fonctionnalités puissent varier légèrement entre les implémentations.

## Comment créer une table SQL temporaire

Pour créer une table SQL temporaire, nous pouvons utiliser l'instruction `CREATE TABLE` avec le mot-clé `TEMPORARY` ou `TEMP` avant le nom de la table. Voici un exemple en SQL :

```sql
CREATE TEMPORARY TABLE temp_table (
    id INT,
    name VARCHAR(50),
    age INT
);

```

**Explication du code :**

1. L'instruction `CREATE TEMPORARY TABLE` est utilisée pour créer une table temporaire.
2. `temp_table` est le nom donné à la table temporaire. Vous pouvez choisir n'importe quel nom.
3. À l'intérieur des parenthèses, nous définissons les colonnes de la table temporaire.
4. Dans cet exemple, la table temporaire `temp_table` a trois colonnes : `id` de type INT, `name` de type `VARCHAR(50)`, et `age` de type `INT`.
5. Nous pouvons ajouter plus de colonnes si nécessaire, en spécifiant le nom de la colonne suivi du type de données.
6. La table temporaire est automatiquement supprimée à la fin de la session ou lorsque la session est terminée.

## Cas d'utilisation des tables temporaires SQL

### Analyser des sous-ensembles de données à l'aide de tables temporaires

Un cas d'utilisation courant pour les tables temporaires est l'analyse de sous-ensembles spécifiques de données.

Supposons que nous avons un grand ensemble de données et que nous voulons effectuer une analyse ou des calculs complexes sur une partie plus petite de ces données. Nous pouvons créer une table temporaire contenant uniquement les lignes et colonnes nécessaires pour notre analyse. Cela nous permet de nous concentrer sur un sous-ensemble de données sans modifier l'ensemble de données original. Une fois notre analyse terminée, nous pouvons supprimer la table temporaire.

Par exemple :

```sql
-- Créer une table temporaire avec un sous-ensemble de données
CREATE TEMPORARY TABLE subset_data AS
SELECT column1, column2, column3
FROM original_table
WHERE condition;

-- Effectuer une analyse sur le sous-ensemble de données
SELECT column1, AVG(column2) AS average_value
FROM subset_data
GROUP BY column1;

-- Supprimer la table temporaire
DROP TABLE subset_data;

```

### Améliorer les performances des requêtes avec des tables temporaires

Vous pouvez utiliser des tables temporaires pour optimiser des requêtes complexes ou intensives en ressources. En décomposant une requête complexe en plusieurs étapes à l'aide de tables temporaires, nous pouvons améliorer les performances des requêtes en réduisant la quantité de données traitées à chaque étape ou en pré-calculant des résultats intermédiaires.

Les tables temporaires nous permettent de stocker et de réutiliser les résultats intermédiaires des requêtes, évitant ainsi des calculs redondants. Voici un exemple :

```sql
-- Créer une table temporaire pour stocker les résultats intermédiaires
CREATE TEMPORARY TABLE temp_results AS
SELECT column1, COUNT(*) AS count_value
FROM large_table
WHERE condition1
GROUP BY column1;

-- Utiliser la table temporaire pour optimiser la requête finale
SELECT column1, column2
FROM temp_results
WHERE count_value > 10
ORDER BY column1;

-- Supprimer la table temporaire
DROP TABLE temp_results;

```

### Préparer et transformer des données à l'aide de tables temporaires

Les tables temporaires sont également utiles pour préparer et transformer des données avant de les charger dans des tables permanentes. Nous pouvons créer une table temporaire, importer des données de différentes sources, effectuer un nettoyage des données, appliquer des transformations et valider les données avant de les insérer dans la destination finale.

Les tables temporaires fournissent un moyen flexible et efficace de traiter et de manipuler des données sans affecter la source originale. Voici un exemple :

```sql
-- Créer une table temporaire pour préparer les données
CREATE TEMPORARY TABLE staging_table (
    id INT,
    name VARCHAR(50),
    quantity INT
);

-- Importer et transformer des données dans la table de préparation
INSERT INTO staging_table (id, name, quantity)
SELECT id, UPPER(name), quantity * 2
FROM external_source;

-- Valider et manipuler les données dans la table de préparation
UPDATE staging_table
SET quantity = 0
WHERE quantity < 0;

-- Insérer les données transformées dans la table finale
INSERT INTO final_table (id, name, quantity)
SELECT id, name, quantity
FROM staging_table;

-- Supprimer la table temporaire
DROP TABLE staging_table;

```

## Différences entre les tables temporaires et permanentes en SQL

|  Critères         | Tables temporaires     |     Tables permanentes        |
|------------------|--------------------------------------------------------|----------------------------|
|**Durée de vie**      | 	Existent uniquement pour la session ou la connexion actuelle	  | Persistent même après la fermeture de la session ou de la connexion. | 	
|**Persistance des données**      | Les données ne sont pas conservées au-delà de la session actuelle	  | Les données sont conservées de manière permanente | 	
|**Allocation de stockage**      | 		Le stockage temporaire est généralement	alloué en mémoire ou dans un espace de stockage temporaire	  | Le stockage permanent est alloué sur disque ou dans une base de données. | 	
|**Accessibilité**      | 		Accessibles uniquement par la session ou la connexion qui les a créées			  | Accessibles à tous les utilisateurs et connexions avec les privilèges appropriés. | 	
|**Convention de nommage**      | 		Les noms des tables temporaires sont souvent précédés d'un	caractère ou mot-clé spécial		  | Les noms des tables permanentes ne sont pas précédés d'un caractère ou mot-clé spécial. | 	
|**Conservation des données**      | 		Les données sont automatiquement supprimées à la fin de la session ou	de la connexion			  | Les données restent dans la table jusqu'à ce qu'elles soient explicitement supprimées ou modifiées. | 	
|**Index et contraintes**      | 		Les tables temporaires peuvent avoir		des index et des contraintes, mais ils sont généralement temporaires et sont supprimés lorsque la	table est supprimée			  | Les tables permanentes peuvent avoir des index, des contraintes et des déclencheurs. | 	
|**Propriétés transactionnelles**      | 		Les tables temporaires ne sont souvent		pas transactionnelles par défaut, mais cela peut varier en fonction du système de base de données	  | Les tables permanentes participent aux transactions et supportent les propriétés ACID. | 	

## Conclusion

Les tables SQL temporaires sont un outil précieux dans le monde de la gestion de bases de données et de l'optimisation des requêtes. Elles offrent divers avantages et peuvent considérablement améliorer votre expérience SQL.

Grâce à la pratique et à l'expérimentation, vous pouvez découvrir des moyens innovants d'exploiter les tables temporaires et d'améliorer vos compétences SQL.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !