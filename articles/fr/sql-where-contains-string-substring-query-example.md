---
title: SQL Where Contains String – Exemple de requête de sous-chaîne
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-23T22:36:06.000Z'
originalURL: https://freecodecamp.org/news/sql-where-contains-string-substring-query-example
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/sqlSubstring.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: SQL Where Contains String – Exemple de requête de sous-chaîne
seo_desc: "If you’re working with a database, whether large or small, there might\
  \ be occasions when you need to search for some entries containing strings. \nIn\
  \ this article, I’ll show you how to locate strings and substrings in MySQL and\
  \ SQL Server.\nI‘ll be usi..."
---

Si vous travaillez avec une base de données, qu'elle soit grande ou petite, il peut arriver que vous ayez besoin de rechercher des entrées contenant des chaînes de caractères. 

Dans cet article, je vais vous montrer comment localiser des chaînes et des sous-chaînes dans MySQL et SQL Server.

J'utiliserai une table nommée `products_data` dans une base de données `products_schema`. L'exécution de `SELECT * FROM products_data` affiche toutes les entrées de la table :

![Screenshot-2023-03-23-at-10.39.24](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-10.39.24.png)

Comme je vais également vous montrer comment rechercher une chaîne dans SQL Server, j'ai la table `products_data` dans une base de données `products` :

![Screenshot-2023-03-23-at-10.42.05](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-10.42.05.png)


## Sommaire
- [Comment rechercher des chaînes en SQL avec la clause `WHERE` et l'opérateur `LIKE`](#heading-comment-rechercher-des-chaines-en-sql-avec-la-clause-where-et-loperateur-like)
- [Comment rechercher des chaînes dans SQL Server avec la fonction `CHARINDEX`](#heading-comment-rechercher-des-chaines-dans-sql-server-avec-la-fonction-charindex)
- [Comment rechercher des chaînes dans SQL Server avec la fonction `PATINDEX`](#heading-comment-rechercher-des-chaines-dans-sql-server-avec-la-fonction-patindex)
- [Comment rechercher des chaînes dans MySQL avec la fonction `SUBSTRING_INDEX()`](#heading-comment-rechercher-des-chaines-dans-mysql-avec-la-fonction-substringindex)
- [Conclusion](#heading-conclusion)


## Comment rechercher des chaînes en SQL avec la clause `WHERE` et l'opérateur `LIKE` 
La clause `WHERE` vous permet d'obtenir uniquement les enregistrements qui répondent à une condition particulière. L'opérateur `LIKE`, quant à lui, permet de trouver un motif particulier dans une colonne. Vous pouvez combiner ces deux éléments pour rechercher une chaîne ou une sous-chaîne d'une chaîne.

J'ai pu obtenir tous les produits contenant le mot « computer » en combinant la clause `WHERE` et l'opérateur `LIKE` en exécutant la requête ci-dessous :

```sql
SELECT * FROM products_data
WHERE product_name LIKE '%computer%'
```

![Screenshot-2023-03-23-at-11.01.49](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-11.01.49.png)

Le signe de pourcentage avant et après le mot « computer » signifie : **trouver le mot « computer », qu'il soit à la fin, au milieu ou au début**.

Ainsi, si vous placez le signe de pourcentage au début d'une sous-chaîne que vous recherchez, cela signifie : **trouver cette sous-chaîne à la fin d'une chaîne**. Par exemple, j'ai obtenu tous les produits se terminant par « er » en exécutant cette requête :

```sql
SELECT * FROM products_data
WHERE product_name LIKE '%er'
```

![Screenshot-2023-03-23-at-11.07.53](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-11.07.53.png)

Et s'il est à la fin d'une chaîne, cela signifie : **trouver cette sous-chaîne au début d'une chaîne**. Par exemple, j'ai pu obtenir le produit commençant par « lap » avec cette requête :

```sql
SELECT * FROM products_data
WHERE product_name LIKE 'lap%'
```

![Screenshot-2023-03-23-at-11.09.59](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-11.09.59.png)

Cette méthode fonctionne également très bien dans SQL Server :

![Screenshot-2023-03-23-at-11.19.51](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-11.19.51.png)


## Comment rechercher des chaînes dans SQL Server avec la fonction `CHARINDEX` 
CHARINDEX() est une fonction SQL Server permettant de trouver l'index d'une sous-chaîne dans une chaîne.

La fonction `CHARINDEX()` prend 3 arguments – la sous-chaîne, la chaîne et la position de départ. La syntaxe ressemble à ceci :

```sql
CHARINDEX(substring, string, start_position)
```

S'il trouve une correspondance, il renvoie l'index où il trouve la correspondance, mais s'il ne trouve pas de correspondance, il renvoie 0. Contrairement à de nombreux autres langages, le comptage en SQL commence à 1.

Voici un exemple :

```sql
SELECT CHARINDEX('free', 'free is the watchword of freeCodeCamp') position;
```

![Screenshot-2023-03-23-at-12.33.03](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-12.33.03.png)

Vous pouvez voir que le mot « free » a été trouvé à la position 1. C'est parce que le « f » lui-même est à la position 1 :

![Screenshot-2023-03-23-at-12.36.22](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-12.36.22.png)

Si je spécifie 25 comme position, SQL Server trouvera une correspondance à partir du texte « freeCodeCamp » :

```sql
SELECT CHARINDEX('free', 'free is the watchword of freeCodeCamp', 25);
```

![Screenshot-2023-03-23-at-12.39.10](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-12.39.10.png)

J'ai pu utiliser la fonction `CHARINDEX` pour rechercher tous les produits contenant le mot « computer » en exécutant cette requête :

```sql
SELECT * FROM products_data WHERE CHARINDEX('computer', product_name, 0) > 0
```

Cette requête dit : **commence à l'index 0, tant qu'ils sont supérieurs à 0, donne-moi chaque produit qui contient le mot « computer » dans la colonne `product_name`**. Voici le résultat :

![Screenshot-2023-03-23-at-12.43.31](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-12.43.31.png) 


## Comment rechercher des chaînes dans SQL Server avec la fonction `PATINDEX` 
`PATINDEX` signifie « pattern index » (index de motif). Ainsi, avec cette fonction, vous pouvez rechercher une sous-chaîne avec des expressions régulières.

`PATINDEX` prend deux arguments – le motif et la chaîne. La syntaxe ressemble à ceci :

```sql
PATINDEX(pattern, string)
``` 

Si `PATINDEX` trouve une correspondance, il renvoie la position de cette correspondance. S'il ne trouve pas de correspondance, il renvoie 0. Voici un exemple :

```sql
SELECT PATINDEX('%ava%', 'JavaScript is a Jack of all trades');
```

![Screenshot-2023-03-23-at-12.52.54](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-12.52.54.png)

Pour appliquer `PATINDEX` à la table d'exemple, j'ai exécuté cette requête :

```sql
SELECT product_name, PATINDEX('%ann%', product_name) position
FROM products_data
```

Mais elle a seulement listé chaque produit et renvoyé l'index où elle a trouvé la correspondance :

![Screenshot-2023-03-23-at-13.08.46](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-13.08.46.png)

Vous pouvez voir qu'elle a trouvé le mot « ann » à l'index 3 du produit « Scanner ». Dans de nombreux cas, vous ne voudrez peut-être pas de ce comportement car vous voudriez qu'il n'affiche que l'élément correspondant.

Je l'ai fait renvoyer uniquement ce qui correspond en utilisant la clause `WHERE` et l'opérateur `LIKE` :

```sql
SELECT product_name, PATINDEX('%ann%', product_name) position
FROM products_data
WHERE product_name LIKE '%ann%'
```

![Screenshot-2023-03-23-at-13.11.28](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-13.11.28.png)

Maintenant, il se comporte comme vous le souhaitez.


## Comment rechercher des chaînes dans MySQL avec la fonction `SUBSTRING_INDEX()` 
En plus des solutions que je vous ai déjà montrées, MySQL possède une fonction intégrée `SUBSTRING_INDEX()` avec laquelle vous pouvez trouver une partie d'une chaîne.

La fonction `SUBSTRING_INDEX()` prend 3 arguments obligatoires – la chaîne, la sous-chaîne à rechercher et un délimiteur. Le délimiteur doit être un nombre.

Lorsque vous spécifiez les arguments obligatoires, la fonction `SUBSTRING_INDEX()` vous donnera chaque partie de la chaîne qui se trouve avant le délimiteur que vous spécifiez. Voici un exemple :

```sql
SELECT SUBSTRING_INDEX("Learn on freeCodeCamp with me", "with", 1);
```

![Screenshot-2023-03-23-at-14.14.14](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-14.14.14.png)

Dans la requête ci-dessus, "Learn on freeCodeCamp with me" est la chaîne, "with" est la sous-chaîne et 1 est le délimiteur. Dans ce cas, la requête vous donnera « Learn on freeCodeCamp » :

Le délimiteur peut également être un nombre négatif. S'il s'agit d'un nombre négatif, il vous donne chaque partie de la chaîne qui se trouve après le délimiteur que vous spécifiez. Voici un exemple :

```sql
SELECT SUBSTRING_INDEX("Learn on freeCodeCamp with me", "with", -1);
```

![Screenshot-2023-03-23-at-14.16.09](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-23-at-14.16.09.png)


## Conclusion
Cet article vous a montré comment localiser une sous-chaîne dans une chaîne en SQL en utilisant à la fois MySQL et SQL Server.

`CHARINDEX()` et `PATINDEX()` sont les fonctions avec lesquelles vous pouvez rechercher une sous-chaîne dans une chaîne à l'intérieur de SQL Server. `PATINDEX()` est plus puissante car elle vous permet d'utiliser des expressions régulières.

Comme `CHARINDEX()` et `PATINDEX()` n'existent pas dans MySQL, le premier exemple vous a montré comment trouver une sous-chaîne dans une chaîne avec la clause `WHERE` et l'opérateur `LIKE`.

Merci de votre lecture !