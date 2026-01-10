---
title: Instruction CASE en SQL – Exemple de requête
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-16T13:57:32.000Z'
originalURL: https://freecodecamp.org/news/case-statement-in-sql-example-query
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-anete-lusina-4792286.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: SQL
  slug: sql
seo_title: Instruction CASE en SQL – Exemple de requête
seo_desc: 'If you need to add a value to a cell conditionally based on other cells,
  SQL''s case statement is what you''ll use.

  If you know other languages, the case statement in SQL is similar to an if statement,
  or a switch statement. It allows you to conditiona...'
---

Si vous devez ajouter une valeur à une cellule conditionnellement en fonction d'autres cellules, l'instruction CASE de SQL est ce que vous utiliserez.

Si vous connaissez d'autres langages, l'instruction CASE en SQL est similaire à une instruction if ou à une instruction switch. Elle vous permet de spécifier une valeur conditionnellement, de sorte que, selon la condition satisfaite, vous obtenez une valeur différente dans la cellule.

Cela peut être vraiment important en analyse de données, donc après avoir introduit l'instruction CASE, nous verrons quelques exemples de la manière dont vous pouvez l'utiliser pour analyser des données de manière simple.

# Syntaxe de l'instruction CASE en SQL

La syntaxe contient beaucoup d'éléments, mais elle reste plutôt intuitive : le mot-clé `CASE` signale le début d'une instruction CASE, et le mot-clé `END` signale sa fin.

Ensuite, pour une seule condition, vous pouvez écrire le mot-clé `WHEN` suivi de la condition qui doit être satisfaite. Après cela vient le mot-clé `THEN` et la valeur pour cette condition, comme `WHEN <condition> THEN <valeur>`.

Cela peut ensuite être suivi par d'autres instructions `WHEN`/`THEN`.

À la fin, vous pouvez ajouter une valeur à utiliser par défaut si aucune des conditions n'est vraie avec le mot-clé `ELSE`, comme montré ci-dessous.

```sql
CASE
   WHEN condition1 THEN valeur1
   WHEN condition2 THEN autre_valeur
   ...
   ELSE valeur_par_defaut
END
```

Mettons cela en pratique pour mieux le comprendre.

# Exemples d'instruction CASE en SQL

Utilisons l'instruction `CASE` dans un exemple. Nous avons une table avec une liste d'étudiants et leurs scores à un examen. Nous devons attribuer une note à chaque étudiant, et nous pouvons utiliser l'instruction CASE pour le faire automatiquement.

| id | name | score |
| -- | -- | -- |
| 1 | Simisola | 60|
| 2 | Ivan | 80 |
| 3 | Metodija | 52 |
| 4 | Callum | 98 |
| 5 | Leia | 84 |
| 6 | Aparecida | 82 |
| 7 | Ursula | 69 |
| 8 | Ramazan | 78 |
| 9 | Corona | 87 |
| 10 | Alise | 57 |
| 11 | Galadriel | 89 |
| 12 | Merel | 99 |
| 13 | Cherice | 55 |
| 14 | Nithya | 81 |
| 15 | Elşad | 71 |
| 16 | Liisi | 90 |
| 17 | Johanna | 90 |
| 18 | Anfisa | 90 |
| 19 | Ryōsuke | 97 |
| 20 | Sakchai | 61 |
| 21 | Elbert | 63 |
| 22 | Katelyn | 51 |

Nous pouvons utiliser l'instruction `CASE` pour attribuer une note à chaque étudiant, que nous ajouterons dans une nouvelle colonne nommée `grade`.

Écrivons d'abord l'instruction `CASE`, dans laquelle nous écrivons la répartition pour chaque note. Lorsque `score` est 94 ou plus, la ligne aura la valeur `A`. Si le score est 90 ou plus, elle aura la valeur `A-`, et ainsi de suite.

```sql
  CASE
    WHEN score >= 94 THEN "A"
    WHEN score >= 90 THEN "A-"
    WHEN score >= 87 THEN "B+"
    WHEN score >= 83 THEN "B"
    WHEN score >= 80 THEN "B-"
    WHEN score >= 77 THEN "C+"
    WHEN score >= 73 THEN "C"
    WHEN score >= 70 THEN "C-"
    WHEN score >= 67 THEN "D+"
    WHEN score >= 60 THEN "D"
    ELSE "F"
  END
```

Après avoir écrit l'instruction `CASE`, nous l'ajouterons dans une requête. Ensuite, nous donnerons à la colonne le nom `grade` en utilisant le mot-clé `AS` :

```sql
SELECT *,
  CASE
    WHEN score >= 94 THEN "A"
    WHEN score >= 90 THEN "A-"
    WHEN score >= 87 THEN "B+"
    WHEN score >= 83 THEN "B"
    WHEN score >= 80 THEN "B-"
    WHEN score >= 77 THEN "C+"
    WHEN score >= 73 THEN "C"
    WHEN score >= 70 THEN "C-"
    WHEN score >= 67 THEN "D+"
    WHEN score >= 60 THEN "D"
    ELSE "F"
  END AS grade
FROM students_grades;
```

La table que nous obtenons à partir de cette requête ressemble à ce qui suit – et maintenant chaque étudiant a une note basée sur son score.

| id | name | score | grade |
| -- | -- | -- | -- |
| 1 | Simisola | 60 | D |
| 2 | Ivan | 80 | B- |
| 3 | Metodija | 52 | F |
| 4 | Callum | 98 | A |
| 5 | Leia | 84 | B |
| 6 | Aparecida | 82 | B- |
| 7 | Ursula | 69 | D+ |
| 8 | Ramazan | 78 | C+ |
| 9 | Corona | 87 | B+ |
| 10 | Alise | 57 | F |
| 11 | Galadriel | 89 | B+ |
| 12 | Merel | 99 | A |
| 13 | Cherice | 55 | F |
| 14 | Nithya | 81 | B- |
| 15 | Elşad | 71 | C- |
| 16 | Liisi | 90 | A- |
| 17 | Johanna | 90 | A- |
| 18 | Anfisa | 90 | A- |
| 19 | Ryōsuke | 97 | A |
| 20 | Sakchai | 61 | D |
| 21 | Elbert | 63 | D |
| 22 | Katelyn | 51 | F |

## Exemples plus complexes d'instruction CASE

Nous pouvons également manipuler la table de différentes manières en fonction de nos besoins en utilisant d'autres instructions en plus de l'instruction CASE.

### Exemple 1 d'instruction CASE

Par exemple, nous pouvons utiliser [`ORDER BY`](https://www.freecodecamp.org/news/sql-order-by-statement-example-sytax/) pour trier les lignes afin d'avoir les notes les plus élevées en haut.

```sql
SELECT name,
  CASE
    WHEN score >= 94 THEN "A"
    WHEN score >= 90 THEN "A-"
    WHEN score >= 87 THEN "B+"
    WHEN score >= 83 THEN "B"
    WHEN score >= 80 THEN "B-"
    WHEN score >= 77 THEN "C+"
    WHEN score >= 73 THEN "C"
    WHEN score >= 70 THEN "C-"
    WHEN score >= 67 THEN "D+"
    WHEN score >= 60 THEN "D"
    ELSE "F"
  END AS grade
FROM students_grades
ORDER BY score DESC;
```

Nous trions en fonction de `score` qui est un nombre, au lieu de la colonne `grade`, car l'ordre alphabétique n'est pas le même que l'ordre des notes basé sur leur valeur. Nous utilisons le mot-clé `DESC` pour l'afficher dans l'ordre décroissant, avec la valeur la plus élevée en haut.

La table que nous obtenons ressemble à ce qui suit :

| name | grade |
| --- | --- |
| Merel | A |
| Callum | A |
| Ryōsuke | A |
| Liisi | A- |
| Johanna | A- |
| Anfisa | A- |
| Galadriel | B+ |
| Corona | B+ |
| Leia | B |
| Aparecida | B- |
| Nithya | B- |
| Ivan | B- |
| Ramazan | C+ |
| Elşad | C- |
| Ursula | D+ |
| Elbert | D |
| Sakchai | D |
| Simisola | D |
| Alise | F |
| Cherice | F |
| Metodija | F |
| Katelyn | F |

### Exemple 2 d'instruction CASE

Faisons un peu d'analyse sur ces données. Nous pouvons utiliser [`GROUP BY` et `COUNT`](https://www.freecodecamp.org/news/sql-group-by-clauses-explained/) pour compter combien d'étudiants ont reçu chaque note.

```sql
SELECT 
  CASE
    WHEN score >= 94
      THEN "A"
    WHEN score >= 90 THEN "A-"
    WHEN score >= 87 THEN "B+"
    WHEN score >= 83 THEN "B"
    WHEN score >= 80 THEN "B-"
    WHEN score >= 77 THEN "C+"
    WHEN score >= 73 THEN "C"
    WHEN score >= 70 THEN "C-"
    WHEN score >= 67 THEN "D+"
    WHEN score >= 60 THEN "D"
    ELSE "F"
  END AS grade,
  COUNT(*) AS number_of_students
FROM students_grades
GROUP BY grade
ORDER BY score DESC;

```

Nous utilisons [`ORDER BY`](https://www.freecodecamp.org/news/sql-order-by-statement-example-sytax/) pour trier les notes de la plus élevée à la plus basse, et nous utilisons `score` car c'est une valeur numérique (car le tri par la colonne `grade` utiliserait l'ordre alphabétique, qui n'est pas le même que l'ordre par valeur des notes).

| grade | number_of_students |
| -- | -- |
| A | 3 |
| A- | 3 |
| B+ | 2 |
| B | 1 | 
| B- | 3 |
| C+ | 1 |
| C- | 1 |
| D+ | 1 |
| D | 3 |
| F | 4 |

### Exemple 3 d'instruction CASE

Faisons une analyse un peu différente sur ces données. Nous pouvons utiliser [`GROUP BY` et `COUNT`](https://www.freecodecamp.org/news/sql-group-by-clauses-explained/) et une instruction CASE différente pour compter combien d'étudiants ont réussi l'examen. Ensuite, nous pouvons utiliser [`ORDER BY`](https://www.freecodecamp.org/news/sql-order-by-statement-example-sytax/) pour avoir la colonne dans l'ordre que nous préférons, avec le nombre d'étudiants qui ont réussi en haut.

```sql
SELECT 
  CASE
    WHEN score >= 60
      THEN "passed"
    ELSE "failed"
  END AS result,
  COUNT(*) AS number_of_students
FROM students_grades
GROUP BY result
ORDER BY result DESC;
```

La table que nous obtenons ressemble à ce qui suit. La classe ne s'en sort pas trop mal, avec 18 étudiants sur 22 ayant des notes de passage – mais les 4 autres peuvent avoir besoin d'un peu d'aide.

| result | number_of_students |
| -- | -- |
| passed | 18 |
| failed | 4 |

# Conclusion

L'instruction CASE est un outil puissant que vous pouvez utiliser lorsque vous devez obtenir des valeurs basées sur certaines conditions.

Dans cet article, vous avez appris comment l'utiliser, et vous avez vu quelques exemples de la manière dont vous pouvez l'utiliser pour l'analyse de données.