---
title: Fonctions d'agrégation SQL – Avec des exemples de requêtes de données pour
  débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-15T15:48:09.000Z'
originalURL: https://freecodecamp.org/news/sql-aggregate-functions-with-example-data-queries-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/sql-aggregate-functions.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Fonctions d'agrégation SQL – Avec des exemples de requêtes de données pour
  débutants
seo_desc: "By Veronica Stork\nWhat is an Aggregate Function?\nSQL aggregate functions\
  \ will seem very familiar if you have worked with spreadsheets. \nHave you ever\
  \ used SUM in Google Sheets or Excel? The SUM function exists in SQL as well, and\
  \ is called an aggrega..."
---

Par Veronica Stork

## Qu'est-ce qu'une fonction d'agrégation ?

Les fonctions d'agrégation SQL vous sembleront très familières si vous avez travaillé avec des tableurs. 

Avez-vous déjà utilisé `SUM` dans Google Sheets ou Excel ? La fonction `SUM` existe également en SQL et est appelée une _fonction d'agrégation_. 

Les fonctions d'agrégation effectuent une tâche particulière sur les lignes d'une base de données. Par exemple, supposons que vous organisez une collecte de fonds annuelle. Vous disposez d'une base de données de donateurs ainsi que du montant qu'ils ont donné chaque année. 

Vous pourriez utiliser la fonction `COUNT` pour déterminer combien de dons ont été reçus, ou la fonction `SUM` pour savoir combien vous avez récolté au total cette année. 

Nous utiliserons le petit ensemble de données suivant à des fins d'illustration.

| name | email | donation_2020 | donation_2021
| ---- | ------ | -------- | ----------- |
| Andrew Jones | ajones@someemail.com | 400 | 500 |
| Maria Rodriguez | maria77@someemail.com | 1000 | 350 |
| Gerry Ford | NULL | 25 | 25 |
| Isabella Munn | isamun91@someemail.com | 250 | NULL |
| Jennifer Ward | jjw1972@someemail.com | 2000 | 2300 |
| Rowan Parker | NULL | 5000 | 4000 |

Dans cet article, nous aborderons les fonctions d'agrégation suivantes : `COUNT`, `SUM`, `MIN/MAX` et `AVG`.

## La fonction COUNT

La fonction `COUNT` retourne un compte des lignes. Dans sa forme la plus simple, `COUNT` compte le nombre total de lignes dans votre table. 

Pour obtenir cette valeur à partir de notre table de donateurs, vous exécuteriez la requête suivante : `SELECT COUNT(*) FROM donors`. Cela retournera le nombre total de donateurs, qui dans ce cas est de 6. Ici, bien sûr, vous pourriez simplement compter les lignes dans cet exemple, mais imaginons qu'il y ait beaucoup plus de lignes.

Vous pourriez vouloir compter seulement certaines lignes, cependant. Dans notre exemple de base de données de donateurs, disons que vous voulez compter le nombre de donateurs qui ont une adresse email listée. 

Si vous exécutez la requête `SELECT COUNT(email) FROM donors`, vous obtiendrez 4, qui est le nombre total de donateurs avec des valeurs non nulles dans la colonne email. 

Gardez à l'esprit que, sauf si vous utilisez un alias, la colonne retournée sera simplement étiquetée "count". Si vous voulez un nom plus descriptif, exécutez une requête en utilisant `AS` pour créer un alias, par exemple `SELECT COUNT(email) FROM donors AS email_count`.

## La fonction SUM

SUM est une fonction d'agrégation très pratique que vous pouvez utiliser pour additionner des valeurs numériques provenant de différentes lignes. 

Dans notre base de données de donateurs, vous pourriez utiliser `SUM` pour additionner tous les dons de 2021 en exécutant la requête `SELECT SUM(donation_2021) FROM donors`. Notez que `SUM` ignore les valeurs `NULL`, donc le résultat de cette requête sera 7175.

Rappelez-vous que `SUM`, comme les autres fonctions d'agrégation, fonctionne sur les lignes, et non sur les colonnes. 

Ainsi, dans notre exemple, vous pourriez l'utiliser pour additionner tous les dons de 2021 (représentés par la colonne `donation_2021`), mais pas pour additionner tous les dons d'une seule personne provenant de la colonne `donation_2020` et de la colonne `donation_2021`.

## Les fonctions MIN et MAX

Comme vous pouvez le deviner, vous pouvez utiliser MIN et MAX pour trouver les valeurs minimales et maximales dans une colonne particulière d'une base de données. 

Dans nos données d'exemple, imaginez que vous voulez trouver les montants de dons minimaux et maximaux pour 2021. Vous pourriez le faire en exécutant la requête : `SELECT MIN(donation_2021) AS "Minimum donation 2021", MAX(donation_2021) AS "Maximum donation 2021" FROM donors`. 

Notez que dans cet exemple, nous attribuons des alias aux colonnes retournées en utilisant des guillemets. Les guillemets ne sont pas nécessaires si votre alias ne contient pas d'espaces, mais nous utilisons des guillemets ici pour pouvoir utiliser des espaces.

Une note intéressante : vous pouvez utiliser `MIN` et `MAX` sur des valeurs non numériques. `MIN` trouvera le plus petit nombre, la lettre la plus proche de A, ou la date la plus ancienne. `MAX` trouvera le plus grand nombre, la lettre la plus proche de Z, ou la date la plus récente. Très pratique !

## La fonction AVG

Enfin, la fonction `AVG` calcule la moyenne des valeurs numériques d'une colonne particulière. Comme avec `SUM`, elle ignore les valeurs `NULL`. 

Pour obtenir une moyenne de tous les dons de 2020, vous pouvez exécuter la requête suivante : `SELECT AVG(donation_2020) FROM donors`. Le résultat de cette requête serait 1435.

## Conclusion

Comme vous l'avez vu, les fonctions d'agrégation sont des outils faciles et utiles pour analyser des données en SQL. `AVG`, `MIN/MAX`, `SUM` et `COUNT` sont une addition importante à votre ensemble de compétences SQL.