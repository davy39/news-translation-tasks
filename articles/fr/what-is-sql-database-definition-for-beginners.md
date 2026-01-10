---
title: Qu'est-ce que SQL ? Définition de base de données pour débutants
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-01-12T18:23:07.000Z'
originalURL: https://freecodecamp.org/news/what-is-sql-database-definition-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/cover-template--8-.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Qu'est-ce que SQL ? Définition de base de données pour débutants
seo_desc: 'Data is a powerful tool that drives everything you see and interact with
  on the internet.

  It facilitates research and powers today''s technology. It is the driving force
  behind today''s artificial intelligence and robotics. And so much more.

  Previously...'
---

Les données sont un outil puissant qui alimente tout ce que vous voyez et avec lequel vous interagissez sur Internet.

Elles facilitent la recherche et alimentent la technologie d'aujourd'hui. Elles sont la force motrice derrière l'intelligence artificielle et la robotique d'aujourd'hui. Et bien plus encore.

Auparavant, ces données étaient stockées sur papier, dans des fichiers physiques à l'intérieur de cabinets. Mais maintenant, elles sont stockées en ligne dans ce qu'on appelle une base de données.

Dans cet article, vous apprendrez ce qu'est une base de données, les deux principaux types de bases de données, puis ce qu'est SQL et pourquoi il est important.

## Qu'est-ce qu'une base de données ?

Une base de données est une collection structurée de données stockées électroniquement. Ces données peuvent être accessibles, gérées, modifiées, mises à jour, contrôlées et organisées à l'aide d'un système de gestion de base de données (SGBD).

Les données et le SGBD sont généralement liés et appelés système de base de données, souvent abrégé en base de données.

Il existe plusieurs types de bases de données, selon la manière dont les données sont stockées, récupérées et modifiées. Mais il existe deux principaux types, qui sont les bases de données relationnelles et non relationnelles.

### Qu'est-ce qu'une base de données relationnelle ?

Une base de données relationnelle, également connue sous le nom de base de données SQL, est utilisée pour stocker des données dans des tables. Cela signifie que les données sont organisées en lignes et en colonnes.

Ce type de base de données organise les données dans des relations prédéfinies et stocke ces données dans une ou plusieurs tables de colonnes et de lignes. Cela facilite la visualisation et la compréhension de la manière dont différentes structures de données sont liées les unes aux autres.

![](https://paper-attachments.dropboxusercontent.com/s_DADB35C92DE96459B45F8A24F2BA20C1018B5BA020F47C0EB9D92470905886E0_1673510261840_Untitled1.drawio.png align="left")

Ce type de base de données est appelé "relationnel" parce que deux tables ou plus peuvent être liées entre elles.

Par exemple, lorsque vous avez une table d'utilisateurs avec un identifiant unique, vous pouvez utiliser cet identifiant pour stocker chaque commande de l'utilisateur dans une table de commandes différente et les demander en utilisant l'identifiant unique de l'utilisateur.

![](https://paper-attachments.dropboxusercontent.com/s_DADB35C92DE96459B45F8A24F2BA20C1018B5BA020F47C0EB9D92470905886E0_1673510517663_Untitled1.drawio+2.png align="left")

Des exemples populaires de systèmes de gestion de bases de données relationnelles sont MySQL, PostgreSQL, MSSQL et Oracle. Pour accéder aux données des bases de données relationnelles, vous utiliserez **SQL (Structured Query Language)**.

### Qu'est-ce qu'une base de données non relationnelle ?

Les bases de données non relationnelles, également connues sous le nom de bases de données NoSQL, sont des bases de données qui stockent les données dans un format non tabulaire.

Cela signifie que les données ne sont pas modélisées en lignes et en colonnes, mais plutôt en paires clé-valeur. Par exemple, dans les paires clé-valeur, vous pouvez avoir des objets représentant chaque utilisateur :

![](https://paper-attachments.dropboxusercontent.com/s_DADB35C92DE96459B45F8A24F2BA20C1018B5BA020F47C0EB9D92470905886E0_1673543855317_Untitled11.drawio.png align="left")

Des exemples de bases de données non relationnelles sont MongoDB, Amazon DynamoDB, Redis, et bien d'autres.

## Qu'est-ce que SQL ?

Le langage de requête structuré (SQL) est un langage de requête utilisé avec les **bases de données relationnelles** telles que MySQL, Oracle, MSSQL, PostgreSQL, et bien d'autres.

C'est un langage de requête que vous pouvez utiliser pour créer et supprimer des bases de données et des tables, insérer et lire des données dans des tables, supprimer des données de tables, et bien plus encore.

![](https://paper-attachments.dropboxusercontent.com/s_DADB35C92DE96459B45F8A24F2BA20C1018B5BA020F47C0EB9D92470905886E0_1673510261840_Untitled1.drawio.png align="left")

Par exemple, disons que vous avez une table d'utilisateurs, comme vu ci-dessus, qui contient l'identifiant unique, le prénom, le nom de famille et l'âge. Vous pouvez utiliser SQL pour lire ou obtenir des données spécifiques de la table, comme les prénom et nom de famille uniquement :

```sql
SELECT first_name, last_name FROM Users;
```

Cela retournera une table avec uniquement les données interrogées :

![](https://paper-attachments.dropboxusercontent.com/s_DADB35C92DE96459B45F8A24F2BA20C1018B5BA020F47C0EB9D92470905886E0_1673544506987_Untitled1.drawio+3.png align="left")

Vous pouvez faire beaucoup plus avec SQL, mais ceci n'était qu'une introduction. Si vous souhaitez en apprendre davantage, j'ai lié quelques excellentes ressources ci-dessous.

## C'est tout !

Dans cet article, vous avez appris les différences fondamentales et majeures entre les bases de données relationnelles et non relationnelles. Vous avez également appris que SQL est un langage de requête utilisé avec les bases de données relationnelles pour interagir avec la base de données.

Il y a plus à faire avec SQL et les bases de données. Vous pouvez en apprendre davantage [sur SQL et les bases de données en regardant l'une des meilleures vidéos sur Internet, avec plus de 14 millions de vues](https://www.youtube.com/watch?v=HXV3zeQKqGY&t=1s). Vous pouvez également [consulter plus de 120 articles sur SQL publiés sur la publication freeCodeCamp](https://www.freecodecamp.org/news/tag/sql/).

Amusez-vous bien à coder !

Vous pouvez accéder à plus de 150 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.