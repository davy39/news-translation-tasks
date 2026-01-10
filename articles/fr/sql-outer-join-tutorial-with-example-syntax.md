---
title: Tutoriel SQL Outer Join – Avec Exemple de Syntaxe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-02T20:06:07.000Z'
originalURL: https://freecodecamp.org/news/sql-outer-join-tutorial-with-example-syntax
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60651b659618b008528aadab.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Tutoriel SQL Outer Join – Avec Exemple de Syntaxe
seo_desc: "By Veronica Stork\nWhat are SQL JOINs?\nIn SQL, JOINs are used to unite\
  \ the rows of two or more tables, based on a column that is shared between them.\
  \ \nThere are four different types of JOINs: INNER JOIN, LEFT JOIN, RIGHT JOIN,\
  \ and FULL OUTER JOIN. In ..."
---

Par Veronica Stork

## Qu'est-ce que les JOINs en SQL ?

En SQL, les JOINs sont utilisés pour unir les lignes de deux tables ou plus, sur la base d'une colonne qui est partagée entre elles.

Il existe quatre types différents de JOINs : `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN` et `FULL OUTER JOIN`. Dans cet article, nous allons discuter du `FULL OUTER JOIN`.

## Qu'est-ce qu'un Full Outer Join en SQL ?

Le `FULL OUTER JOIN` (aka `OUTER JOIN`) est utilisé pour retourner tous les enregistrements qui ont des valeurs dans la table de gauche _ou_ dans celle de droite.

Par exemple, un full outer join d'une table de clients et d'une table de commandes pourrait retourner tous les clients, y compris ceux qui n'ont pas passé de commandes, ainsi que toutes les commandes. Les clients ayant passé des commandes seraient unis à leurs commandes en utilisant leur numéro d'identification de client.

Un full outer join peut retourner beaucoup de données, alors avant de l'utiliser, réfléchissez à savoir si une méthode plus conservative pourrait répondre à vos besoins.

## Ensemble de Données Exemple

Imaginez que vous enseignez un cours de littérature américaine. Vous avez dix étudiants, et vous voulez que chacun d'eux lise un livre différent d'une liste de classiques américains pré-approuvés. Certains étudiants ont choisi le livre qu'ils liront, tandis que d'autres ne l'ont pas encore fait.

Vous avez créé une table qui liste les étudiants avec leurs numéros d'identification, et une autre table qui liste les livres avec leur titre, auteur, ISBN, et l'ID de l'étudiant qui lira le livre, si quelqu'un l'a choisi.

![Tableau avec les noms des étudiants et leurs numéros d'identification](https://www.freecodecamp.org/news/content/images/2021/04/students-1.png)
_Tableau des étudiants_

![Tableau des livres avec ISBN, ID de l'étudiant qui le lira, titre et auteur](https://www.freecodecamp.org/news/content/images/2021/04/books.png)
_Tableau des livres_

## Comment Faire un Outer Join en SQL

Pour faire un outer join sur nos données d'exemple, nous pourrions utiliser la requête suivante :

```sql
SELECT students.name, books.title
FROM students
FULL OUTER JOIN books ON students.student_id=books.student_id;
```

Dans cet exemple, nous sélectionnons les noms de la table `students` et les titres des livres de la table `books`. Les enregistrements sont appariés en utilisant la colonne `student_id` dans les deux tables.

Les résultats ressemblent à ceci :

![noms des étudiants appariés avec les livres qu'ils lisent](https://www.freecodecamp.org/news/content/images/2021/04/result.png)

Avec le full outer join, nous pouvons voir tous les étudiants, y compris ceux qui n'ont pas encore choisi de livre. Nous pouvons également voir tous les livres, y compris ceux qui n'ont pas encore été choisis.

Dans notre exemple, vous pourriez utiliser ces données pour voir qui doit encore décider d'un livre, et quels livres sont encore disponibles pour qu'ils choisissent.

## Conclusion

L'utilisation d'un full outer join en SQL peut vous aider à obtenir une vue complète des données de plusieurs tables liées.

Gardez à l'esprit, cependant, qu'avec un grand ensemble de données, cette requête peut retourner une quantité ingérable d'informations, alors utilisez ce pouvoir avec sagesse !