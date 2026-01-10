---
title: Instruction SQL LIKE – Comment interroger SQL avec des caractères génériques
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-11-22T15:01:50.000Z'
originalURL: https://freecodecamp.org/news/sql-like-statement-how-to-query-sql-with-wildcard
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/firos-nv-1wBmbnvv4TE-unsplash.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Instruction SQL LIKE – Comment interroger SQL avec des caractères génériques
seo_desc: "You can use the % and _ wildcards with the SQL LIKE statement to compare\
  \ values from an SQL table. But how does that work exactly? \nIn this article, I\
  \ will show you how to use the SQL LIKE statement through code examples. \nBasic\
  \ syntax of SQL LIKE st..."
---

Vous pouvez utiliser les caractères génériques `%` et `_` avec l'instruction SQL LIKE pour comparer des valeurs d'une table SQL. Mais comment cela fonctionne-t-il exactement ?

Dans cet article, je vais vous montrer comment utiliser l'instruction SQL LIKE à travers des exemples de code.

## Syntaxe de base de l'instruction SQL LIKE

Voici la syntaxe de base pour l'instruction SQL Like :

```sql
SELECT FROM table_name
WHERE column LIKE 'string pattern'
```

[En SQL](https://dev.mysql.com/doc/mysql-tutorial-excerpt/5.7/en/pattern-matching.html),

> la correspondance de motifs vous permet d'utiliser `_` pour correspondre à n'importe quel caractère unique et `%` pour correspondre à un nombre arbitraire de caractères (y compris zéro caractère)

Par exemple, si nous voulions trouver tous les noms de la table qui commencent par la lettre "T", nous pourrions utiliser cette syntaxe :

```sql
WHERE name LIKE 'T%'
```

Ou si nous voulions trouver tous les noms de la table qui contiennent les lettres "on", nous pourrions utiliser cette syntaxe :

```sql
WHERE name LIKE '%on%'
```

Nous pouvons utiliser le caractère générique `_` pour trouver une correspondance de caractère unique. Par exemple, voici la syntaxe pour trouver tous les nombres dans la catégorie `quantity` qui ont 2 chiffres et se terminent par '9' :

```sql
WHERE quantity LIKE '_9';

```

Pour mieux comprendre comment ces caractères génériques fonctionnent avec l'instruction SQL Like, examinons un exemple de table de données.

## Comment utiliser l'instruction SQL LIKE – exemple avec une table de voitures

Dans cet exemple, nous avons une table `cars` avec les colonnes `id`, `model`, `make` et `price`.

```sql
id|make|model|price
1|Honda|Civic|21000
2|Ford|Fusion|23000
3|Toyota|Camry|24000
4|Dodge|Challenger|29000
5|Tesla|Model X|104000
6|Chevrolet|Tahoe|49000
```

### Comment utiliser le caractère générique `%` avec l'instruction SQL LIKE

Dans ce premier exemple, nous voulons trouver tous les modèles de voitures qui commencent par la lettre "C".

```sql
SELECT * FROM cars
WHERE model LIKE 'C%';
```

Ce code retournerait les résultats suivants de la table `cars` :

```sql
id|make|model|price
1|Honda|Civic|21000
3|Toyota|Camry|24000
4|Dodge|Challenger|29000
```

Nous pouvons voir que 3 des 6 entrées de notre table `cars` ont des noms de modèles qui commencent par la lettre "C".

L'instruction SQL LIKE n'est pas sensible à la casse, ce qui signifie que `'C%'` et `'c%'` retourneraient des résultats identiques.

Nous pouvons également utiliser le caractère générique `%` et l'instruction SQL LIKE pour trouver des entrées qui se terminent par un ou plusieurs caractères.

Dans cet exemple, nous voulons trouver tous les fabricants de voitures dont le nom se termine par un "a".

```sql
SELECT * FROM cars
WHERE make LIKE '%a';
```

Ce code retournerait les résultats suivants de la table `cars` :

```sql
id|make|model|price
1|Honda|Civic|21000
3|Toyota|Camry|24000
5|Tesla|Model X|104000
```

Nous pouvons voir que 3 des 6 fabricants de voitures ont un nom qui se termine par la lettre "a".

### Comment utiliser plusieurs caractères génériques `%` avec l'instruction SQL LIKE

Dans cet exemple, nous voulons trouver tous les prix de voitures qui incluent le chiffre 9.

```sql
SELECT * FROM cars
WHERE price LIKE '%9%';
```

Ce code retournerait les résultats suivants de la table `cars` :

```sql
id|make|model|price
4|Dodge|Challenger|29000
6|Chevrolet|Tahoe|49000
```

Nous pouvons voir que 2 des 6 prix de voitures incluent le chiffre 9.

### Comment utiliser le caractère générique `_` avec l'instruction SQL LIKE

Nous pouvons utiliser le caractère générique `_` pour trouver une correspondance de caractère unique.

Modifions notre table `cars` :

```sql
id|make|model|price
30|Honda|Civic|21000
35|Ford|Fusion|23000
40|Toyota|Camry|24000
45|Dodge|Challenger|29000
50|Tesla|Model X|104000
55|Chevrolet|Tahoe|49000
```

Dans cet exemple, nous voulons trouver tous les identifiants qui ont deux chiffres et se terminent par le chiffre 0.

```sql
SELECT * FROM cars
WHERE id LIKE '_0';
```

Ce code retournerait les résultats suivants de la table `cars` :

```sql
id|make|model|price
30|Honda|Civic|21000
40|Toyota|Camry|24000
50|Tesla|Model X|104000
```

Nous pouvons voir que 3 des 6 identifiants de voitures à deux chiffres se terminent par le chiffre 0.

### Comment utiliser plusieurs caractères génériques `_` avec l'instruction SQL LIKE

Modifions à nouveau notre table `cars`.

```sql
id|make|model|price
130|Honda|Civic|21000
135|Ford|Fusion|23000
140|Toyota|Camry|24000
145|Dodge|Challenger|29000
150|Tesla|Model X|104000
155|Chevrolet|Tahoe|49000
```

Dans cet exemple, nous voulons trouver tous les identifiants qui ont trois chiffres et se terminent par le chiffre 0.

```sql
SELECT * FROM cars
WHERE id LIKE '__0';
```

Ce code retournerait les résultats suivants de la table `cars` :

```sql
id|make|model|price
130|Honda|Civic|21000
140|Toyota|Camry|24000
150|Tesla|Model X|104000
```

Nous avons dû utiliser deux underscores `_` avec l'instruction SQL LIKE pour trouver tous les identifiants qui ont trois chiffres et se terminent par le chiffre 0.

```sql
Utilisation de deux underscores
'__0'

au lieu d'un seul
'_0'
```

### Comment utiliser l'opérateur NOT avec l'instruction SQL LIKE

Nous pouvons utiliser l'opérateur NOT en SQL pour trouver tous les résultats qui ne correspondent pas au motif de chaîne dans l'instruction LIKE.

Nous pouvons modifier notre dernier exemple pour trouver tous les identifiants à trois chiffres qui ne se terminent pas par le chiffre 0.

```sql
SELECT * FROM cars
WHERE id NOT LIKE '__0';
```

Ce code retournerait les résultats suivants de la table `cars` :

```sql
id|make|model|price
135|Ford|Fusion|23000
145|Dodge|Challenger|29000
155|Chevrolet|Tahoe|49000
```

### Comment utiliser les caractères génériques `%` et `_` avec l'instruction SQL LIKE

Dans cet exemple, nous voulons trouver tous les fabricants de voitures dont la deuxième lettre est un "o" et le nom se termine par un "a".

```sql
SELECT * FROM cars
WHERE make LIKE '_o%a';
```

Le `_o` est utilisé pour trouver tous les fabricants de voitures dont la deuxième lettre est "o". Le `%a` est utilisé pour trouver tous les fabricants de voitures qui se terminent par la lettre "a".

Ce code retournerait les résultats suivants de la table `cars` :

```sql
id|make|model|price
130|Honda|Civic|21000
140|Toyota|Camry|24000
```

## Conclusion

Vous pouvez utiliser les caractères génériques `%` et `_` avec l'instruction SQL LIKE pour comparer des valeurs d'une table SQL.

Voici la syntaxe de base pour l'instruction SQL Like.

```sql
SELECT FROM table_name
WHERE column LIKE 'string pattern'
```

Le `%` correspond à zéro, un ou plusieurs caractères tandis que le `_` correspond à un seul caractère.

Dans cet article, nous avons appris comment utiliser ces deux caractères génériques avec l'instruction SQL LIKE en utilisant l'exemple de la table `cars`.

J'espère que vous avez apprécié cet article et je vous souhaite bonne chance dans votre apprentissage de SQL.