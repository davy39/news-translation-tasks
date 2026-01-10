---
title: Apprenez SQL avec ces 5 recettes faciles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-23T21:25:00.000Z'
originalURL: https://freecodecamp.org/news/sql-recipes
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a17740569d1a4ca236c.jpg
tags:
- name: SQL
  slug: sql
seo_title: Apprenez SQL avec ces 5 recettes faciles
seo_desc: 'By Jackson Bates

  SQL (Structured Query Language) is a powerful and expressive language for dealing
  with data from relational databases. But it can seem daunting to the uninitiated.

  The "recipes" I''m going to share with you today are some basic exampl...'
---

Par Jackson Bates

SQL (Structured Query Language) est un langage puissant et expressif pour traiter les données des bases de données relationnelles. Mais il peut sembler intimidant pour les non-initiés.

Les "recettes" que je vais partager avec vous aujourd'hui sont des exemples de base provenant d'une base de données simple. Mais les modèles que vous apprendrez ici peuvent vous aider à écrire des requêtes précises. Vous vous sentirez bientôt comme l'équivalent des données d'un MasterChef.

_Une note sur la syntaxe : La plupart des requêtes ci-dessous sont écrites dans le style utilisé pour PostgreSQL à partir de la ligne de commande psql. Différents moteurs SQL peuvent utiliser des commandes légèrement différentes._

_La plupart des requêtes ci-dessous devraient fonctionner dans la plupart des moteurs sans ajustement, bien que certains moteurs ou outils GUI puissent nécessiter l'omission des guillemets autour des noms de tables et de colonnes._

## Plat 1 : Retourner tous les utilisateurs créés dans une plage de dates particulière

### Ingrédients

* SELECT
* FROM
* WHERE
* AND

### Méthode

```sql
SELECT *
FROM "Users"
WHERE "created_at" > "2020-01-01"
AND "created_at" < "2020-02-01";
```

Ce plat simple est un aliment de base polyvalent. Ici, nous retournons les utilisateurs qui répondent à deux conditions particulières en enchaînant les conditions `WHERE` avec une instruction `AND`. Nous pouvons étendre cela davantage avec plus d'instructions `AND`.

Bien que l'exemple ici soit pour une plage de dates spécifique, la plupart des requêtes nécessitent une sorte de condition pour filtrer les données de manière utile.

## Plat 2 : Trouver tous les commentaires pour un livre, y compris l'utilisateur qui a fait le commentaire

### (Nouveaux) Ingrédients

* JOIN

### Méthode

```sql
SELECT "Comments"."comment", "Users"."username"
FROM "Comments"
JOIN "Users"
ON "Comments"."userId" = "Users"."id"
WHERE "Comments"."bookId" = 1;
```

Cette requête suppose la structure de table suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/simpleERD.png)
_Schéma ERD montrant les Utilisateurs qui peuvent avoir plusieurs Commentaires, et les Livres qui peuvent également avoir plusieurs Commentaires_

L'une des choses qui peuvent commencer à confondre les débutants avec SQL est l'utilisation des JOINs pour trouver des données dans des tables associées.

Le schéma ERD (Entity Relationship Diagram) ci-dessus montre trois tables, Utilisateurs, Livres et Commentaires, ainsi que leurs associations.

Chaque table a un `id` qui est en **gras** dans le diagramme pour montrer qu'il s'agit de la clé primaire de la table. Cette clé primaire est toujours une valeur unique et est utilisée pour distinguer les enregistrements dans les tables.

Les noms de colonnes en _italique_ `userId` et `bookId` dans la table Commentaires sont des clés étrangères, ce qui signifie qu'elles sont la clé primaire dans d'autres tables et sont utilisées ici pour référencer ces tables.

Les connecteurs dans le schéma ERD ci-dessus montrent également la nature des relations entre les 3 tables.

L'extrémité à point unique du connecteur signifie 'un' et l'extrémité divisée du connecteur signifie 'plusieurs', donc la table Utilisateur a une relation 'un-à-plusieurs' avec la table Commentaires.

Un utilisateur peut avoir plusieurs commentaires, par exemple, mais un commentaire ne peut appartenir qu'à un seul utilisateur. Les Livres et les Commentaires ont la même relation dans le diagramme ci-dessus.

La requête SQL devrait avoir du sens en fonction de ce que nous savons maintenant. Nous retournons uniquement les colonnes nommées, c'est-à-dire la colonne commentaire de la table Commentaires et le nom d'utilisateur de la table Utilisateurs associée (basée sur la clé étrangère référencée). Dans l'exemple ci-dessus, nous limitons la recherche à un seul livre, à nouveau basé sur la clé étrangère dans la table Commentaires.

## Plat 3 : Compter le nombre de commentaires ajoutés par chaque utilisateur

### (Nouveaux) Ingrédients

* COUNT
* AS
* GROUP BY

### Méthode

```sql
SELECT "Users"."username", COUNT("Comments"."id") AS "CommentCount"
FROM "Comments"
JOIN "Users"
ON "Comments"."userId" = "Users"."id"
GROUP BY "Users"."id";
```

Cette petite requête fait quelques choses intéressantes. La plus facile à comprendre est l'instruction `AS`. Cela nous permet de renommer arbitrairement, et temporairement, les colonnes dans les données qui sont retournées. Ici, nous renommons la colonne dérivée, mais c'est aussi utile lorsque vous avez plusieurs colonnes `id`, puisque vous pouvez les renommer en choses comme `userId` ou `commentId` et ainsi de suite.

L'instruction `COUNT` est une fonction SQL qui, comme vous vous en doutez, compte les choses. Ici, nous comptons le nombre de commentaires associés à un utilisateur. Comment cela fonctionne-t-il ? Eh bien, le `GROUP BY` est l'ingrédient final important.

Imaginons brièvement une requête légèrement différente :

```sql
SELECT "Users"."username", "Comments"."comment"
FROM "Comments"
JOIN "Users"
ON "Comments"."userId" = "Users"."id";
```

Remarquez, pas de comptage ou de regroupement. Nous voulons simplement chaque commentaire et qui l'a fait.

La sortie pourrait ressembler à ceci :

```
|----------|-----------------------------|
| username | comment                     |
|----------|-----------------------------|
| jackson  | c'est bien, j'ai aimé       |
| jackson  | c'était ok, pas le meilleur  |
| quincy   | excellente lecture, recommandé |
| quincy   | ne vaut pas la peine d'être lu |
| quincy   | je n'ai pas encore lu cela   |
------------------------------------------
```

Maintenant, imaginons que nous voulions compter les commentaires de Jackson et Quincy - facile à voir d'un coup d'œil ici, mais plus difficile avec un ensemble de données plus grand comme vous pouvez l'imaginer.

L'instruction `GROUP BY` indique essentiellement à la requête de traiter tous les enregistrements `jackson` comme un groupe, et tous les enregistrements `quincy` comme un autre. La fonction `COUNT` compte ensuite les enregistrements de ce groupe et retourne cette valeur :

```
|----------|--------------|
| username | CommentCount |
|----------|--------------|
| jackson  | 2            |
| quincy   | 3            |
---------------------------
```

## Plat 4 : Trouver les utilisateurs qui n'ont pas fait de commentaire

### (Nouveaux) Ingrédients

* LEFT JOIN
* IS NULL

### Méthode

```sql
SELECT "Users"."username"
FROM "Users"
LEFT JOIN "Comments"
ON "Users"."id" = "Comments"."userId"
WHERE "Comments"."id" IS NULL;
```

Les différentes jointures peuvent devenir très confuses, donc je ne vais pas les décomposer ici. Il y a une excellente explication d'entre elles ici : [Représentations visuelles des jointures SQL](https://www.codeproject.com/Articles/33052/Visual-Representation-of-SQL-Joins), qui tient également compte de certaines des différences de syntaxe entre les différentes saveurs de SQL.

Imaginons une version alternative de cette requête rapidement :

```sql
SELECT "Users"."username", "Comments"."id" AS "commentId"
FROM "Users"
LEFT JOIN "Comments"
ON "Users"."id" = "Comments"."userId";
```

Nous avons toujours le `LEFT JOIN` mais nous avons ajouté une colonne et supprimé la clause `WHERE`.

Les données retournées pourraient ressembler à ceci :

```
|----------|-----------|
| username | commentId |
|----------|-----------|
| jackson  | 1         |
| jackson  | 2         |
| quincy   | NULL      |
| abbey    | 3         |
------------------------
```

Donc Jackson est responsable des commentaires 1 et 2, Abbey pour 3, et Quincy n'a pas commenté.

La différence entre un `LEFT JOIN` et un `INNER JOIN` (ce que nous avons appelé simplement un `JOIN` jusqu'à présent, ce qui est valide) est que la jointure interne ne montre que les enregistrements où il y a des valeurs pour les deux tables. Une jointure gauche, en revanche, retourne tout de la première, ou gauche, table (celle du `FROM`) même s'il n'y a rien dans la table de droite. Une jointure interne ne montrerait donc que les enregistrements pour Jackson et Abbey.

Maintenant que nous pouvons visualiser ce que le `LEFT JOIN` retourne, il est plus facile de raisonner sur ce que la partie `WHERE...IS NULL` fait. Nous retournons uniquement les utilisateurs où le commentId est une valeur nulle, et nous n'avons pas réellement besoin de la colonne de valeur nulle incluse dans la sortie, d'où son omission originale.

## Plat 5 : Lister tous les commentaires ajoutés par chaque utilisateur dans un seul champ, séparés par des barres verticales

### (Nouveaux) Ingrédients

* GROUP_CONCAT ou STRING_AGG

### Méthode (MySQL)

```sql
SELECT "Users"."username", GROUP_CONCAT("Comments"."comment" SEPARATOR " | ") AS "comments"
FROM "Users"
JOIN "Comments"
ON "Users"."id" = "Comments"."userId"
GROUP BY "Users"."id";
```

### Méthode (Postgresql)

```sql
SELECT "Users"."username", STRING_AGG("Comments"."comment", " | ") AS "comments"
FROM "Users"
JOIN "Comments"
ON "Users"."id" = "Comments"."userId"
GROUP BY "Users"."id";
```

Cette dernière recette montre une différence de syntaxe pour une fonction similaire dans deux des moteurs SQL les plus populaires.

Voici un exemple de sortie que nous pourrions attendre :

```
|----------|---------------------------------------------------|
| username | comments                                          |
|----------|---------------------------------------------------|
| jackson  | c'est bien, j'ai aimé | c'était ok, pas le meilleur |
| quincy   | excellente lecture, recommandé | ne vaut pas la peine d'être lu |
----------------------------------------------------------------
```

Nous pouvons voir ici que les commentaires ont été regroupés et concaténés / agrégés, c'est-à-dire joints ensemble dans un seul champ d'enregistrement.

## **Bon Appétit**

Maintenant que vous avez quelques recettes SQL sur lesquelles vous appuyer, soyez créatif et servez vos propres plats de données !

J'aime penser à `WHERE`, `JOIN`, `COUNT`, `GROUP_CONCAT` comme le _Sel, Graisse, Acide, Chaleur_ de la cuisine des bases de données. Une fois que vous savez ce que vous faites avec ces éléments de base, vous êtes bien parti pour maîtriser.

Si cela a été une collection utile, ou si vous avez d'autres recettes préférées à partager, laissez-moi un commentaire ou suivez-moi sur Twitter : [@JacksonBates](https://twitter.com/jacksonbates).