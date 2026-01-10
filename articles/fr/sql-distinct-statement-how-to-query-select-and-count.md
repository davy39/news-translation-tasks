---
title: Instruction SQL DISTINCT – Comment interroger, sélectionner et compter
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-30T16:24:19.000Z'
originalURL: https://freecodecamp.org/news/sql-distinct-statement-how-to-query-select-and-count
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/anthony-riera-kylWNDQFd5A-unsplash.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Instruction SQL DISTINCT – Comment interroger, sélectionner et compter
seo_desc: "In SQL, you can make a database query and use the COUNT function to get\
  \ the number of rows for a particular group in the table. \nIn this article, I will\
  \ show you how to use the COUNT function with a few code examples. \nWhat is the\
  \ COUNT function in S..."
---

En SQL, vous pouvez effectuer une requête de base de données et utiliser la fonction `COUNT` pour obtenir le nombre de lignes pour un groupe particulier dans la table. 

Dans cet article, je vais vous montrer comment utiliser la fonction `COUNT` avec quelques exemples de code. 

## Qu'est-ce que la fonction COUNT en SQL ?

Cette fonction SQL retournera le nombre de lignes pour un groupe donné.

Voici la syntaxe de base :

```sql
SELECT COUNT(column_name) FROM table_name;
```

L'instruction `SELECT` en SQL indique à l'ordinateur de récupérer des données de la table. 

`COUNT(column_name)` n'inclura pas les valeurs `NULL` dans le compte. 

Une valeur `NULL` en SQL fait référence aux valeurs qui ne sont pas présentes dans la table. 

Parfois, vous pouvez utiliser un `*` à l'intérieur des parenthèses pour la fonction `COUNT`.

```sql
SELECT COUNT(*) FROM table_name;
```

La fonction `COUNT(*)` retournera le nombre total d'éléments dans ce groupe, y compris les valeurs `NULL`. 

La clause `FROM` en SQL spécifie quelle table nous voulons lister.

Vous pouvez également utiliser le mot-clé `ALL` dans la fonction `COUNT`. 

```sql
SELECT COUNT(ALL column_name) FROM table_name;
```

Le mot-clé `ALL` comptera toutes les valeurs de la table, y compris les doublons. Vous pouvez omettre ce mot-clé car la fonction `COUNT` utilise le mot-clé `ALL` par défaut, que vous l'écriviez ou non. 

Parfois, vous verrez le mot-clé `DISTINCT` utilisé avec la fonction `COUNT`.

```sql
SELECT COUNT(DISTINCT column_name) FROM table_name;
```

Le mot-clé `DISTINCT` ne comptera que les valeurs uniques qui ne sont pas `NULL`. L'ordinateur ignorera toute valeur en double. 

## Comment utiliser la fonction COUNT en SQL

Dans cet exemple, nous avons une table pour jeunes campeurs avec les colonnes `id`, `name`, `age` et `counselor`.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-1.35.37-AM.png)

Si nous voulons sélectionner toutes les lignes de notre table, nous pouvons utiliser la syntaxe suivante :

```sql
SELECT COUNT(*) FROM campers;
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-1.37.18-AM.png)

Comme vous pouvez le voir, la requête a retourné le nombre 12 qui représente le nombre total de lignes dans notre table `campers`. 

### Utilisation de la clause `WHERE`

Nous pouvons utiliser la clause `WHERE` pour spécifier le nombre de lignes pour le nom d'un conseiller de camp particulier. 

Dans cet exemple, nous voulons compter le nombre de lignes pour le conseiller de camp nommé Ashley. 

Dans la clause `WHERE`, nous devons spécifier `counselor` avec une valeur de `"Ashley"`.

```sql
 WHERE counselor="Ashley";
```

Voici le code complet :

```sql
SELECT COUNT(*) FROM campers WHERE counselor="Ashley";
```

Voici ce que le résultat retournerait :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-1.47.03-AM.png)

Si nous regardons notre table de tout à l'heure, nous pouvons voir que `"Ashley"` n'apparaît que 4 fois. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-1.35.37-AM.png)

Nous pouvons modifier notre résultat pour compter combien de lignes il y a pour les campeurs qui ont 11 ans.

Dans la clause `WHERE`, nous devons spécifier `age` avec une valeur de `11`.

```sql
WHERE age=11;
```

Voici le code complet :

```sql
SELECT COUNT(*) FROM campers WHERE age=11;
```

Voici ce que le résultat retournerait :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-1.50.46-AM.png)

Si nous regardons notre table de tout à l'heure, nous pouvons voir qu'il n'y a que trois campeurs de 11 ans.

### Comment utiliser la clause `GROUP BY`

Nous pouvons utiliser la clause `GROUP BY` et la fonction `COUNT` pour voir le nombre de campeurs de 11, 12 et 13 ans dans notre table.

Nous devons d'abord sélectionner la colonne `age` et utiliser la fonction `COUNT` :

```sql
SELECT age, COUNT(*)
```

Nous devons ensuite spécifier la table `campers` et regrouper les résultats par `age` :

```sql
FROM campers GROUP BY age;
```

Voici à quoi ressemble le code dans son ensemble :

```sql
SELECT age, COUNT(*) FROM campers GROUP BY age;
```

Voici à quoi ressemblent les résultats :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-2.23.35-AM.png)

### Comment utiliser la clause `ORDER BY`

Nous pouvons modifier notre exemple pour la liste des âges et utiliser la clause `ORDER BY` pour lister les résultats du plus petit au plus grand.

Voici le code pour la clause `ORDER BY` :

```sql
ORDER BY COUNT(*);
```

Nous ajoutons cette clause à la fin de l'instruction `SELECT` comme ceci :

```sql
SELECT age, COUNT(*) FROM campers GROUP BY age ORDER BY COUNT(*);
```

Voici à quoi ressemble l'exemple modifié :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-2.28.18-AM.png)

Si nous voulions que les résultats du compte soient triés du plus grand au plus petit, nous pourrions utiliser le mot-clé `DESC`.

Voici le code pour la clause `ORDER BY` utilisant le mot-clé `DESC` :

```sql
ORDER BY COUNT(*) DESC;
```

Voici le code complet :

```sql
SELECT age, COUNT(*) FROM campers GROUP BY age ORDER BY COUNT(*) DESC;
```

Voici à quoi ressemblerait le nouveau résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-2.31.52-AM.png)

### Comment utiliser la clause `HAVING`

Nous pouvons utiliser la clause `HAVING` pour spécifier une condition pour la fonction `COUNT`. 

Nous pouvons modifier le code pour n'afficher que les résultats pour les âges où le compte est inférieur à 5. 

Voici à quoi ressemble le code pour la clause `HAVING` :

```sql
HAVING COUNT(*)<5;

```

Voici à quoi ressemble le code complet :

```sql
SELECT age, COUNT(*) FROM campers GROUP BY age HAVING COUNT(*)<5;

```

Voici à quoi ressemblent les résultats modifiés :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-30-at-2.48.28-AM.png)

Nous pouvons voir que les 12 ans ont été retirés de ce résultat car le compte était supérieur à 5. 

## Conclusion

En SQL, vous pouvez effectuer une requête de base de données et utiliser la fonction `COUNT` pour obtenir le nombre de lignes pour un groupe particulier dans la table. 

Voici la syntaxe de base :

```sql
SELECT COUNT(column_name) FROM table_name;
```

`COUNT(column_name)` n'inclura pas les valeurs `NULL` dans le compte.

Une valeur `NULL` en SQL fait référence aux valeurs qui ne sont pas présentes dans la table.

Parfois, vous pouvez utiliser un `*` à l'intérieur des parenthèses pour la fonction `COUNT`.

```sql
SELECT COUNT(*) FROM table_name;
```

La fonction `COUNT(*)` retournera le nombre total d'éléments dans ce groupe, y compris les valeurs `NULL`.

J'espère que vous avez apprécié cet article et bonne chance dans votre apprentissage de SQL.