---
title: Coalesce SQL – Exemple de fonctions PostgreSQL et SQL Server
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-01-13T18:14:20.000Z'
originalURL: https://freecodecamp.org/news/coalesce-sql-example-postgresql-and-sql-server-functions
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/coalesce.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Coalesce SQL – Exemple de fonctions PostgreSQL et SQL Server
seo_desc: "In SQL, the COALESCE() function returns the first non-null value in an\
  \ entry. \nIt evaluates the values of the entries one by one, ignores the null values,\
  \ then returns the first value that is not null. It works in PostgreSQL, SQL server,\
  \ and MySQL.\nI..."
---

En SQL, la fonction `COALESCE()` retourne la première valeur non nulle dans une entrée. 

Elle évalue les valeurs des entrées une par une, ignore les valeurs nulles, puis retourne la première valeur qui n'est pas nulle. Elle fonctionne dans PostgreSQL, SQL Server et MySQL.

Dans cet article, je vais vous montrer comment utiliser la fonction `COALESCE()` pour gérer les valeurs nulles. Mais d'abord, qu'est-ce qu'une valeur nulle ? C'est ce que nous allons voir ensuite.

## Ce que nous allons couvrir
- [Qu'est-ce qu'une valeur NULL ?](#heading-quest-ce-quune-valeur-null)
- [Syntaxe de la fonction `COALESCE()`](#heading-syntaxe-de-la-fonction-coalesce)
- [Comment gérer les valeurs NULL avec la fonction `COALESCE()` dans PostgreSQL](#heading-comment-gerer-les-valeurs-null-avec-la-fonction-coalesce-dans-postgresql)
  - [Exemple de gestion des valeurs NULL avec la fonction `COALESCE()` dans PostgreSQL](#heading-exemple-de-gestion-des-valeurs-null-avec-la-fonction-coalesce-dans-postgresql) 

## Qu'est-ce qu'une valeur NULL ?

Null signifie rien. Donc lorsque vous voyez `NULL` dans un serveur SQL, PostgreSQL ou MySQL, cela signifie qu'il n'y a pas d'entrée pour cet attribut.

Une valeur non nulle est l'opposé d'une valeur nulle. Tout entier, chaîne ou autre valeur autre que null est une valeur non nulle.

## Syntaxe de la fonction `COALESCE()`

La fonction `COALESCE()` accepte toutes les valeurs courantes, y compris null. Voici la syntaxe de base :

```sql
COALESCE(valeur1, valeur2, valeur3, …)
```

Après exécution, `COALESCE()` supprime toutes les valeurs `NULL` tant qu'il n'y a pas d'erreur dans vos entrées.

Voici comment cela fonctionne :

```sql
SELECT COALESCE(NULL, 'freeCodeCamp', 'freeCodeCamp Blog', NULL);
```

![ss1-1](https://www.freecodecamp.org/news/content/images/2023/01/ss1-1.png) 

La fonction `COALESCE()` fonctionne parfaitement pour ce qu'elle fait. Même si la valeur non nulle est la dernière entrée et qu'il y a beaucoup d'entrées NULL derrière elle, elle fonctionne toujours :

```sql
SELECT COALESCE(NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'freeCodeCamp Blog', 12, 'JavaScript');
```

![ss2-1](https://www.freecodecamp.org/news/content/images/2023/01/ss2-1.png) 

Et s'il n'y a qu'une seule valeur non nulle dans l'entrée, elle fonctionne toujours :

```sql
SELECT COALESCE(NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'JavaScript', NULL, NULL, NULL);
```

![ss3-1](https://www.freecodecamp.org/news/content/images/2023/01/ss3-1.png) 

## Comment gérer les valeurs NULL avec la fonction `COALESCE()` dans PostgreSQL

Vous pouvez utiliser la fonction `COALESCE()` pour gérer les valeurs NULL dans PostgreSQL en substituant ces valeurs NULL par une valeur par défaut. 

Voici la syntaxe :

```sql
SELECT COALESCE(colonne, valeurParDefaut) FROM table;
```

Si la valeur NULL est de type entier, la valeur par défaut doit être un entier. Et si cette valeur NULL est de type chaîne, la valeur par défaut doit être une chaîne. 

### Exemple de gestion des valeurs NULL avec la fonction `COALESCE()` dans PostgreSQL

J'ai une table `langs` avec 6 entrées créées de cette manière :

```sql
create table langs (yob integer, name varchar(100), purpose varchar(100));
		insert into langs (yob, name, purpose) values (NULL, 'JavaScript', 'frontend');
		insert into langs (yob, name, purpose) values (NULL, 'PHP', 'backend');
		insert into langs (yob, name, purpose) values (NULL, 'Python', 'everything');
   
        insert into langs (yob, name, purpose) values (2009, 'Golang', 'everything');
        insert into langs (yob, name, purpose) values (2010, 'Rust', 'Systems Programming');
        insert into langs (yob, name, purpose) values (NULL, 'MQL4', 'Trading Bots');
```

Voici la table lorsque j'exécute `SELECT * FROM langs;` :

![ss4-1](https://www.freecodecamp.org/news/content/images/2023/01/ss4-1.png) 

Voici ce que j'ai obtenu lorsque j'ai sélectionné uniquement la colonne `yob` (SELECT yob FROM langs;) :

![ss5-1](https://www.freecodecamp.org/news/content/images/2023/01/ss5-1.png)

J'ai besoin d'une valeur par défaut pour ces valeurs NULL, donc je vais le faire avec la syntaxe pour gérer les valeurs NULL dans PostgreSQL :

```sql
SELECT COALESCE(yob, 0) FROM langs;
```

Voici le résultat :

![ss6-1](https://www.freecodecamp.org/news/content/images/2023/01/ss6-1.png) 

## Conclusion
Cet article vous a montré ce que fait la fonction `COALESCE()` en SQL. Vous pouvez supprimer les valeurs NULL dans n'importe quelle colonne avec elle. Nous avons également vu comment vous pouvez utiliser la fonction `COALESCE()` pour gérer les valeurs NULL dans PostgreSQL. 

Si vous trouvez cet article utile, partagez-le sur les réseaux sociaux avec vos amis et votre famille.