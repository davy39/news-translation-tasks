---
title: SQL Inner Join – Comment joindre 3 tables en SQL et MySQL
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2022-04-01T18:19:05.000Z'
originalURL: https://freecodecamp.org/news/sql-inner-join-how-to-join-3-tables-in-sql-and-mysql
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-pixabay-269399--1-.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
seo_title: SQL Inner Join – Comment joindre 3 tables en SQL et MySQL
seo_desc: 'When you''re working with your database, you might need to put together
  data from a few different tables. This article will show you how.

  I have already written about SQL joins here and here, but let''s take a moment to
  review how a join works first, a...'
---

Lorsque vous travaillez avec votre base de données, vous pourriez avoir besoin de regrouper des données provenant de plusieurs tables différentes. Cet article vous montrera comment faire.

J'ai déjà écrit sur les jointures SQL [ici](https://www.freecodecamp.org/news/sql-join-types-inner-join-vs-outer-join-example/) et [ici](https://www.freecodecamp.org/news/sql-left-join-example-join-statement-syntax/), mais prenons un moment pour revoir comment fonctionne une jointure d'abord, et particulièrement la syntaxe spécifique à MySQL.

## L'instruction SQL Join

Join est une instruction qui vous permet de regrouper deux tables, en faisant correspondre les lignes qui sont liées les unes aux autres, et en ne conservant que les lignes qui peuvent être appariées, sans garder les lignes isolées.

```sql
SELECT * FROM table1 
  INNER JOIN table2
  ON table1.id = table2.id;
```

L'instruction `SELECT ... FROM` indique quelle est la première table, puis le nom de la deuxième table est écrit juste après les mots-clés `INNER JOIN`. 

La manière dont les deux tables doivent être jointes est écrite dans l'instruction `ON`. Dans ce cas, les deux tables sont jointes à l'aide de la relation `table1.id = table2.id`.

Il est possible d'utiliser plusieurs instructions de jointure ensemble pour joindre plus d'une table en même temps.

```sql
SELECT *
  FROM table1
  INNER JOIN table2
  ON table1.id = table2.id
  INNER JOIN table3
  ON table2.id = table3.id;
```

Pour ce faire, vous ajoutez une deuxième instruction `INNER JOIN` et une deuxième instruction `ON` pour indiquer la troisième table et la deuxième relation.

Parlons un instant des relations que vous pouvez avoir entre les tables et pourquoi vous pourriez vouloir joindre trois tables ensemble.

## Relations entre les tables en SQL

Lorsque vous avez des tables qui sont liées entre elles, leurs relations peuvent être de plusieurs types.

### un-à-plusieurs (one-to-many)

Dans une relation de type un-à-plusieurs, une ligne de la première table peut être liée à plusieurs lignes de la seconde table.

Dans une base de données relationnelle, cela peut être implémenté avec la seconde table ayant une colonne `first_table_id` qui indique à quelle ligne de la première table cette ligne est liée.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-11.png)

### plusieurs-à-un (many-to-one)

Dans une relation de type plusieurs-à-un, une ligne de la première table ne peut être liée qu'à une seule ligne de la seconde table, et une ligne de la seconde table peut être liée à plusieurs lignes de la première table.

Dans une base de données relationnelle, cela peut être implémenté avec la première table ayant une colonne `second_table_id` qui indique à quelle ligne de la seconde table cette ligne est liée.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-10.png)
_Plusieurs-à-un_

### plusieurs-à-plusieurs (many-to-many)

Dans ce cas, plusieurs lignes sont liées à plusieurs lignes.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-9.png)
_Plusieurs-à-plusieurs_

Ce type de relation ne peut pas être représenté tel quel avec des tables SQL – vous devez ajouter une table de liaison entre les deux tables afin que seules des relations plusieurs-à-un et un-à-plusieurs soient présentes entre les tables. 

Chaque ligne de la table du milieu représente une relation entre les lignes de la table de gauche et les lignes de la table de droite.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-12.png)

En pratique dans MySQL, cette table intermédiaire aura une colonne pour `first_table_id` et une colonne pour `second_table_id`, chaque combinaison étant unique.

## Joindre des tables SQL en pratique

Imaginons que nous ayons la base de données d'une organisation, où nous avons une table avec des équipes (leur nom et d'autres informations d'identification), et une table avec des projets (nom, avancement, etc.).

| id | team_name | specialty |
| --- | --- | --- | --- |
| 1 | Lanceurs de bananes | Bananes |
| 2 | Rongeurs de bois | Ronger du bois |
| 3 | Les éléphants roses | Trépigner sur le sol |
| 4 | Patates duveteuses | Travailler et dormir |

| id | project_name | progress |
| --- | --- | --- |
| 1 | Construction de barrage | Encore un peu de rongeage de bois et de piétinement au sol nécessaires |
| 2 | Gâteau à la banane | Quelqu'un mange toutes les bananes |
| 3 | Recherche sur le sommeil | Trop de sommeil, pas assez de recherche |

Comme une équipe peut travailler sur plusieurs projets, et qu'un projet peut être travaillé par plusieurs équipes, il existe également une troisième table qui assure le suivi des correspondances équipe-projet.

| project_id | group_id |
| --- | --- |
| 1 | 2 |
| 1 | 3 |
| 2 | 1 |
| 3 | 1 |
| 3 | 2 |
| 3 | 3 |
| 3 | 4 |

Nous pouvons utiliser une instruction `JOIN` pour tout regrouper lorsque nous avons besoin de visualiser les informations des tables d'une manière lisible par l'homme, comme ceci :

```mysql
SELECT
  teams.team_name AS team_name,
  projects.project_name AS project_name
FROM TABLE teams
INNER JOIN matches
  ON teams.id = matches.team_id
INNER JOIN matches
  ON matches.project_id = projects.id
ORDER BY teams.id;
```

Nous choisissons les colonnes à afficher de chaque table avec une instruction `SELECT`.

Nous spécifions comment les lignes des tables doivent être combinées avec une instruction `ON`.

Et nous trions les lignes de la manière que nous préférons avec une instruction `ORDER BY`.

Les instructions `ON` `teams.id = matches.team_id` et `matches.projects_id = projects.id` signifient que les lignes sont combinées en utilisant les lignes de la table `matches`. Chaque ligne de la table de sortie contient le nom du projet et le nom de l'équipe combinés en utilisant les paires d'identifiants de projet et d'équipe dans la table `matches`.

La table de sortie ressemblera à celle ci-dessous.

| Team_name | Project_name |
| --- | --- |
| Lanceurs de bananes | Gâteau à la banane |
| Lanceurs de bananes | Recherche sur le sommeil |
| Rongeurs de bois | Construction de barrage |
| Rongeurs de bois | Recherche sur le sommeil |
| Les éléphants roses | Construction de barrage |
| Les éléphants roses | Construction de barrage |
| Patates duveteuses | Recherche sur le sommeil |

Il n'y a aucune colonne provenant directement de la table `matches`. La table `matches` n'est pas affichée dans la sortie mais elle est utilisée comme instructions sur la manière de combiner les lignes des tables `teams` et `projects`.

## Conclusion

L'instruction `JOIN` vous permet de joindre une ou plusieurs tables. Elle doit être utilisée conjointement avec l'instruction `ON` pour déterminer la relation entre les lignes d'une table et les lignes d'une table différente. 

Dans cet article, vous avez appris à utiliser l'instruction `JOIN` pour joindre trois tables différentes.