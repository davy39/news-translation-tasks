---
title: SQL Left Join – Exemple de syntaxe de jointure
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-26T20:29:12.000Z'
originalURL: https://freecodecamp.org/news/sql-left-join-example-join-statement-syntax
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-pixabay-262347.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: SQL Left Join – Exemple de syntaxe de jointure
seo_desc: In a Relational Database, tables are often related to each other in a way
  that allows their information to only be written once in the whole database. Then,
  when you need to analyze the data, you'll need to combine the info from those related
  tables....
---

Dans une base de données relationnelle, les tables sont souvent liées les unes aux autres de manière à ce que leurs informations ne soient écrites qu'une seule fois dans toute la base de données. Ensuite, lorsque vous devez analyser les données, vous devrez combiner les informations de ces tables liées.

Pour ce faire en SQL, vous pouvez utiliser les instructions `JOIN`. L'instruction `LEFT JOIN` est l'une des [différentes instructions `JOIN` disponibles](https://www.freecodecamp.org/news/sql-join-types-inner-join-vs-outer-join-example/). Lorsque vous l'utilisez pour joindre deux tables, elle conserve toutes les lignes de la première table (la table de gauche), même s'il n'y a pas de correspondance sur la deuxième table.

Vous pouvez utiliser `JOIN` dans une requête `SELECT` pour joindre deux tables, `table_1` et `table_2`, comme ceci :

```sql
SELECT columns
FROM table_1
LEFT OUTER JOIN table_2
ON relation;
```

```sql
SELECT columns
FROM table_1
LEFT JOIN table_2
ON relation;
```

Tout d'abord, vous écrivez quelles colonnes seront présentes dans la table jointe. Vous pouvez spécifier à quelle table appartient la colonne en préférant le nom de la table au nom de la colonne. Cela est nécessaire si certaines colonnes ont le même nom (comme `table_1.column_1` et `table_2.column_1`) avec `SELECT <columns>`.

Ensuite, vous écrivez le nom de la première table comme `FROM table_1`.

Après cela, vous écrivez le nom de la deuxième table comme `LEFT OUTER JOIN table_2` ou `LEFT JOIN table_2` (en omettant le mot-clé `OUTER`).

Et à la fin, vous écrivez la relation à utiliser pour faire correspondre les lignes, par exemple `ON table_1.column_A = table_2.column_B`. Souvent, la relation est par id, mais elle peut être avec n'importe quelle colonne.

# Exemple de SQL LEFT JOIN

Supposons que vous avez une base de données de livres dans laquelle vous avez deux tables, une avec des livres, l'autre avec des auteurs. Pour éviter de répéter toutes les informations sur l'auteur pour chaque livre, ces informations sont dans leur propre table, et les livres n'ont que la colonne `author_name`.


| book_id | title | author_name | publ_year |
| --- | --- | --- | --- |
| 1 | Uno, nessuno e centomila | Luigi Pirandello | 1926 |
| 2 | Il visconte dimezzato | Italo Calvino | 1952 |
| 3 | Le tigri di Mompracem | Emilio Salgari | 1900 |
| 4 | Il giorno della civetta | Leonardo Sciascia | 1961 |
| 5 | A ciascuno il suo | Leonardo Sciascia | 1966 |
| 6 | Il fu Mattia Pascial | Luigi Pirandello | 1904 |
| 7 | I Malavoglia | Giovanni Verga | 1881 |

| author_id | name | year_of_birth | place_of_birth | trivia |
| --- | --- | --- | --- | --- |
| 1 | Luigi Pirandello | 1867 | Agrigento | Prix Nobel de Littérature en 1934 |
| 2 | Giovanni Verga | 1840 | Vizzini | était Sénateur du Royaume d'Italie de 1920 à 1922 |
| 3 | Italo Svevo | 1861 | Trieste | son vrai nom était Aron Hector Schmitz |
| 4 | Cesare Pavese | 1908 | Santo Stefano Belbo | NULL |
| 5 | Giuseppe Tomasi di Lampedusa | 1896 | Palermo | était prince de Lampedusa de 1934 à 1957 |

Nous pouvons joindre ces deux tables en fonction des noms des auteurs. En utilisant la table `books` comme table de gauche, vous pouvez écrire le code suivant pour les joindre :

```sql
SELECT books.title AS book_title, books.publ_year, books.author_name, authors.year_of_birth, authors.place_of_birth
   FROM books
   LEFT JOIN authors
   ON books.author_name = authors.name
;
```

Décomposons cela.

Dans la première ligne, vous choisissez quelles colonnes afficher dans la table finale. C'est aussi l'endroit où décider si certaines colonnes auront un nom différent dans la table résultante en utilisant `AS` comme avec `books.title AS book_title`.

La deuxième ligne, `FROM books`, indique quelle est la première table à considérer, également appelée table de gauche.

Ensuite, la troisième ligne, `LEFT JOIN authors`, indique quelle autre table considérer.

`ON books.author_name = authors.name` indique de faire correspondre les tables en utilisant les lignes `books.author_name` et `authors.name`.

Après cette requête, vous obtiendrez la table ci-dessous, où les lignes qui n'ont pas obtenu d'informations de la table des auteurs affichent simplement `NULL`.

| book_title | publ_year | author_name | year_of_birth | place_of_birth |
| --- | --- | --- | --- | --- |
| Uno, nessuno e centomila | 1926 | Luigi Pirandello | 1867 | Agrigento |
| Il visconte dimezzato | 1952 | Italo Calvino | NULL | NULL |
| Le tigri di Mompracem | 1900 | Emilio Salgari | NULL | NULL |
| Il giorno della civetta | 1961 | Leonardo Sciascia | NULL | NULL |
| A ciascuno il suo | 1966 | Leonardo Sciascia | NULL | NULL |
| Il fu Mattia Pascal | 1904 | Luigi Pirandello | 1867 | Agrigento |
| I Malavoglia | 1881 | Giovanni Verga | 1840 | Vizzini |

Notez que les auteurs non présents dans la table `books` ne sont pas dans cette table jointe. Cela est dû au fait que, comme je l'ai dit précédemment, seules les lignes non liées de la table de gauche (dans ce cas `books`) sont conservées, et non celles de la table de droite/deuxième table.

## Un exemple plus complexe de LEFT JOIN

Voyons une autre façon dont vous pouvez utiliser `JOIN` avec d'autres fonctionnalités SQL pour faire de l'analyse de données.

Vous pourriez vouloir voir combien de livres de chaque auteur sont présents dans la base de données. Vous pourriez utiliser la requête suivante pour ce faire :

```sql
SELECT authors.name AS author_name,
    SUM(
      CASE
        WHEN books.title LIKE '%'
          THEN 1
        ELSE 0
      END
    ) as number_of_books
  FROM authors
  LEFT JOIN books
  ON books.author_name = authors.name
  GROUP BY authors.name
  ORDER BY number_of_books DESC
;

```

#### Décomposition du code

Ligne 1 : avec `SELECT`, vous listez les colonnes que vous voulez dans la table résultante.

Ligne 2 : [`SUM` est une fonction d'agrégation](https://www.freecodecamp.org/news/sql-group-by-clauses-explained/#aggregations-count-sum-avg-) utilisée en conjonction avec GROUP BY. Les valeurs des lignes qui sont regroupées ensemble sont ensuite additionnées.

Lignes 3-7 : vous utilisez l'instruction [CASE](https://www.freecodecamp.org/news/case-statement-in-sql-example-query/) pour obtenir différents résultats en fonction d'une condition. Dans ce cas, une ligne est comptée comme 1 si elle contient un titre de livre, sinon elle est comptée comme 0. Et ici, nous utilisons `LIKE` pour vérifier si la cellule contient des caractères (en savoir plus dans cet [article sur Contains String](https://www.freecodecamp.org/news/sql-contains-string-sql-regex-example-query)).

Ligne 8 : cela donne un nom de `number_of_books` à la colonne qui est créée pour la SUM.

Ligne 9 : la table de gauche/première table dans ce cas est `authors`.

Ligne 10 : la table de droite/deuxième table dans ce cas est `books`.

Ligne 11 : cela joint les deux tables en utilisant les noms des auteurs.

Ligne 12 : les lignes sont [regroupées par nom d'auteur](https://www.freecodecamp.org/news/sql-group-by-clauses-explained/) - toutes les lignes avec la même valeur dans cette colonne seront représentées par une seule ligne.

Ligne 13 : nous utilisons [order by](https://www.freecodecamp.org/news/sql-order-by-statement-example-sytax/) pour arranger dans l'ordre décroissant en utilisant le nombre de livres.

La requête vous donnera la table ci-dessous. Notez que vous voyez ici seulement les auteurs qui sont présents dans la table `authors`. Les auteurs mentionnés dans la table `books` sans entrée dans la table `authors` ne sont pas présents ici. Cela est dû au fait que les lignes non liées de la table `books` n'ont pas été conservées.

| author_name | number_of_books |
| -- | -- |
| Luigi Pirandello | 2 |
| Giovanni Verga | 1 |
| Cesare Pavese | 0 |
| Giuseppe Tomasi di Lampedusa | 0 |
| Italo Svevo | 0 |

Si la table `authors` est mise à jour pour inclure tous les auteurs mentionnés dans la table `books`, comme ceci :

| author_id | name | year_of_birth | place_of_birth | trivia |
| --- | --- | --- | --- | --- |
| 1 | Luigi Pirandello | 1867 | Agrigento | Prix Nobel de Littérature en 1934 |
| 2 | Giovanni Verga | 1840 | Vizzini | était Sénateur du Royaume d'Italie de 1920 à 1922 |
| 3 | Italo Svevo | 1861 | Trieste | son vrai nom était Aron Hector Schmitz |
| 4 | Cesare Pavese | 1908 | Santo Stefano Belbo | NULL |
| 5 | Giuseppe Tomasi di Lampedusa | 1896 | Palermo | était prince de Lampedusa de 1934 à 1957 |
| 6 | Italo Calvino | 1923 | Santiago de las Vegas | NULL |
| 7 | Emilio Salgari | 1862 | Verona | NULL |
| 8 | Leonardo Sciascia | 1921 | Racalmuto | NULL |

Alors la table de la requête ci-dessus donnerait en fait le nombre de livres pour tous les auteurs.

| author_name | number_of_books |
| -- | -- |
| Leonardo Sciascia | 2 |
| Luigi Pirandello | 2 |
| Emilio Salgari | 1 |
| Giovanni Verga | 1 |
| Giovanni Verga | 1 |
| Cesare Pavese | 0 |
| Giuseppe Tomasi di Lampedusa | 0 |
| Italo Svevo | 0 |

# Conclusion

Dans une base de données relationnelle, les données doivent être écrites une seule fois, donc nous nous retrouvons souvent avec plusieurs tables liées les unes aux autres. `LEFT JOIN` est un allié vraiment utile lorsque nous devons analyser des données et joindre des informations de différentes tables. Profitez de l'interrogation de votre base de données en utilisant cet outil puissant.