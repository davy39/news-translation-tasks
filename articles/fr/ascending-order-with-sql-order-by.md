---
title: Ordre croissant avec SQL Order By
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-20T14:29:04.000Z'
originalURL: https://freecodecamp.org/news/ascending-order-with-sql-order-by
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/brett-jordan-M3cxjDNiLlQ-unsplash.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Ordre croissant avec SQL Order By
seo_desc: "In this article, I will show you a few code examples on how you can sort\
  \ your data in ascending order using the ORDER BY clause in SQL. \nORDER BY syntax\n\
  This is the basic syntax to sort your data in ascending order:\nSELECT columns FROM\
  \ table\nORDER BY..."
---

Dans cet article, je vais vous montrer quelques exemples de code sur la façon de trier vos données par ordre croissant en utilisant la clause `ORDER BY` en SQL. 

## Syntaxe ORDER BY

Voici la syntaxe de base pour trier vos données par ordre croissant :

```sql
SELECT columns FROM table
ORDER BY column;
```

Si vous souhaitez trier par ordre décroissant, vous devez utiliser le mot-clé `DESC`.

```sql
SELECT columns FROM table
ORDER BY column DESC;
```

L'instruction `SELECT` en SQL indique à l'ordinateur de récupérer des données de la table. 

La clause `FROM` en SQL spécifie quelle table nous voulons lister. 

Dans cet exemple, nous avons une table de musiciens avec les colonnes `id`, `name`, `age`, `instrument` et `city` :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-20-at-2.57.23-AM.png)

Actuellement, cette table est triée automatiquement par `id` dans l'ordre croissant. 

Si nous voulions trier la colonne `name` dans l'ordre croissant, nous devrions utiliser cette syntaxe :

```sql
SELECT * FROM musicians
ORDER BY name;
```

Le caractère `*` indique à l'ordinateur de sélectionner toutes les colonnes de la table. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-20-at-3.03.11-AM.png)

Vous pouvez voir que les `names` sont maintenant triés par ordre alphabétique et que les `id` ne sont plus dans le bon ordre croissant. 

Si nous voulions trier les données par `city`, nous pourrions utiliser cette syntaxe.

```sql
SELECT * FROM musicians
ORDER BY city;
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-20-at-3.22.34-AM.png)

Vous pouvez également trier plusieurs colonnes dans l'ordre croissant dans la même commande.

Dans cet nouvel exemple de musiciens, nous pouvons trier les colonnes `age` et `city` dans l'ordre croissant. 

```sql
SELECT * FROM musicians
ORDER BY age, city;
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-20-at-3.13.46-AM.png)

Nous pouvons voir qu'il y a trois musiciens de 19 ans avec leurs villes respectives triées par ordre alphabétique dans la table. Nous pouvons également voir les deux musiciens de 38 ans avec leurs villes correctement triées par ordre alphabétique. 

Si nous voulions trier certaines des données dans l'ordre croissant et d'autres données dans l'ordre décroissant, nous devrions utiliser les mots-clés `ASC` et `DESC`. 

Dans cet nouvel exemple de musiciens, nous voulons trier la colonne `age` dans l'ordre décroissant et la colonne `instrument` dans l'ordre croissant. 

Voici la syntaxe :

```sql
SELECT * FROM musicians
ORDER BY age DESC, instrument ASC;
```

Nous devons utiliser les mots-clés `ASC` et `DESC` à côté des noms de colonnes pour indiquer à l'ordinateur comment trier les données. 

Le résultat serait le suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-20-at-3.33.26-AM.png)

Nous pouvons voir dans notre table qu'Oscar et Jenny sont les plus âgés. Mais Oscar est le premier résultat car la batterie vient avant le trombone dans l'ordre alphabétique. 

Nous voyons la même situation avec Jess et Dave. Bien qu'ils aient le même âge, Jess est plus haut dans la table car la flûte vient avant la trompette dans l'ordre alphabétique. 

## Conclusion

Vous pouvez trier les données de votre table dans l'ordre croissant en utilisant la clause `ORDER BY` en SQL.

```sql
SELECT columns FROM table
ORDER BY column;
```

Si vous souhaitez trier par ordre décroissant, vous devez également utiliser le mot-clé `DESC`.

```sql
SELECT columns FROM table
ORDER BY column DESC;
```

Le caractère `*` indique à l'ordinateur de sélectionner toutes les colonnes de la table. 

```sql
SELECT * FROM table
ORDER BY column;
```

Si vous souhaitez trier plusieurs colonnes dans l'ordre croissant, vous devez lister les colonnes que vous souhaitez trier à côté de la clause `ORDER BY`.

```sql
SELECT * FROM table
ORDER BY column1, column2;
```

Si vous souhaitez trier certaines des données dans l'ordre croissant et d'autres données dans l'ordre décroissant, vous devez utiliser les mots-clés `ASC` et `DESC`. 

```sql
SELECT * FROM table
ORDER BY column1 ASC, column2 DESC;
```

C'est ainsi que vous utilisez la clause `ORDER BY` en SQL pour trier les données dans l'ordre croissant.