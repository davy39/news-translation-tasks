---
title: Comment supprimer une ligne en SQL – Exemple de requête
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-23T17:56:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-delete-a-row-in-sql-example-query
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/ujesh-krishnan-7ySd00IGyx4-unsplash.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Comment supprimer une ligne en SQL – Exemple de requête
seo_desc: "In SQL, you can delete a row in a table by using the DELETE query and the\
  \ WHERE clause. \nIn the article, I will walk you through how to use the DELETE\
  \ query and WHERE clause to delete rows. I will also show you how to delete multiple\
  \ rows from a tabl..."
---

En SQL, vous pouvez supprimer une ligne dans une table en utilisant la requête `DELETE` et la clause `WHERE`.

Dans cet article, je vais vous expliquer comment utiliser la requête `DELETE` et la clause `WHERE` pour supprimer des lignes. Je vais également vous montrer comment supprimer plusieurs lignes d'une table en une seule fois.

## Comment utiliser la requête DELETE en SQL

Voici la syntaxe de base pour utiliser la requête `DELETE` :

```sql
DELETE FROM nom_de_la_table
WHERE condition des lignes à supprimer;
```

Dans cet exemple, nous avons une table appelée `cats` qui contient actuellement dix lignes. Les colonnes seraient `id`, `name` et `gender`.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-23-at-2.28.51-AM.png)

Nous voulons supprimer la ligne avec l'`id` 8 qui est la ligne de Loki.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-23-at-2.30.10-AM.png)

La première ligne de la requête `DELETE` ressemblerait à ceci :

```sql
DELETE FROM cats
```

Dans la deuxième ligne, nous allons spécifier quelle ligne en utilisant `id=8` après la clause `WHERE`.

```sql
WHERE id=8;
```

Voici la syntaxe complète pour supprimer la ligne de Loki :

```sql
DELETE FROM cats
WHERE id=8;
```

Voici à quoi ressemble la nouvelle table `cats` :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-23-at-2.31.22-AM.png)

Nous pouvons voir que notre requête `DELETE` a fonctionné car les informations de Loki ne sont plus là.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-23-at-2.31.40-AM.png)

## Comment supprimer plusieurs lignes d'une table en SQL

Une façon de supprimer plusieurs lignes de notre table `cats` est de changer la condition de `id` à `gender`.

Si nous voulions supprimer les lignes avec seulement les chats mâles, alors nous pouvons utiliser la condition `gender="M"`.

```sql
DELETE FROM cats
WHERE gender="M";
```

Notre nouvelle table `cats` ressemblerait à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-23-at-2.32.55-AM.png)

Maintenant, la table `cats` n'affiche que les chats femelles.

## Comment supprimer plusieurs lignes en utilisant l'opérateur BETWEEN avec l'opérateur AND en SQL

Si nous voulions supprimer un certain nombre de lignes dans une plage, nous pouvons utiliser l'opérateur `AND` avec l'opérateur `BETWEEN`.

Dans cet exemple, nous voulons supprimer les lignes avec les `id` de 4 à 7 inclus.

Voici la syntaxe pour cela :

```sql
DELETE FROM cats
WHERE id BETWEEN 4 AND 7;
```

Voici le résultat de cette requête `DELETE` :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-23-at-2.41.48-AM.png)

Nous pouvons voir que les lignes 1-3 et 8-10 sont restantes dans notre table. Les `id` de 4-7 ont été supprimés avec succès.

## Comment supprimer plusieurs lignes en utilisant l'opérateur IN en SQL

Nous pouvons spécifier quels noms supprimer de la table `cats` en utilisant l'opérateur `IN`.

Dans cet exemple, je veux supprimer les noms de Lucy, Stella, Max et Tiger de notre table `cats` originale ici :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-23-at-2.48.48-AM.png)

Nous devons spécifier la colonne et utiliser l'opérateur `IN` pour lister les noms que nous voulons supprimer.

```sql
DELETE FROM cats
WHERE name IN ("Lucy","Stella","Max","Tiger");
```

Voici à quoi ressemblerait le nouveau résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-23-at-2.55.29-AM.png)

Notre requête `DELETE` a réussi, car ces quatre chats ne sont plus présents dans la table.

## Comment supprimer tous les enregistrements de la table en SQL

Si vous voulez supprimer toutes les informations de votre table, alors vous utiliseriez cette syntaxe :

```sql
DELETE FROM nom_de_la_table;
```

Afin de supprimer tous les chats de notre table `cats`, nous utiliserions ce code.

```sql
DELETE FROM cats;
```

## Conclusion

Dans cet article, nous avons appris les différentes façons de supprimer des informations d'une table SQL.

Voici la syntaxe de base pour utiliser la requête `DELETE` :

```sql
DELETE FROM nom_de_la_table
WHERE condition des lignes à supprimer;
```

Si vous voulez supprimer une ligne de la table, alors vous devez spécifier une condition.

```sql
WHERE id=8;
```

Il existe plusieurs façons de supprimer plusieurs lignes dans une table.

Si vous voulez supprimer un certain nombre de lignes dans une plage, vous pouvez utiliser l'opérateur `AND` avec l'opérateur `BETWEEN`.

```sql
DELETE FROM nom_de_la_table
WHERE nom_de_la_colonne BETWEEN valeur1 AND valeur2;
```

Une autre façon de supprimer plusieurs lignes est d'utiliser l'opérateur `IN`.

```sql
DELETE FROM nom_de_la_table
WHERE nom_de_la_colonne IN (valeur1, valeur2, valeur3, etc...);
```

Si vous voulez supprimer tous les enregistrements de la table, vous pouvez utiliser cette syntaxe.

```sql
DELETE FROM nom_de_la_table;
```

J'espère que vous avez apprécié cet article et bonne chance dans votre apprentissage de SQL.