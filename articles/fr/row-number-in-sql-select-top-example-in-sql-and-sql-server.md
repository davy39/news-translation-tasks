---
title: ROW_NUMBER en SQL – Exemple de sélection des premiers résultats en SQL et SQL
  Server
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-02-08T19:14:49.000Z'
originalURL: https://freecodecamp.org/news/row-number-in-sql-select-top-example-in-sql-and-sql-server
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/ROW_NUMBER-in-SQL
seo_title: ROW_NUMBER en SQL – Exemple de sélection des premiers résultats en SQL
  et SQL Server
---

Select-Top-Example-in-SQL-and-SQL-Server.png
tags:
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
seo_title: null
seo_desc: "SQL, ou langage de requête structuré, nous permet de collecter des données à partir d'une base de données \
  \ à travers des requêtes. Il nous permet également d'insérer, de mettre à jour et de supprimer ces données. \n\
  Dans cet article de blog, nous allons nous concentrer sur la manière de récupérer des données et de limiter les résultats en utilisant\
  \ SQL. \nPourquoi devriez-vous..."
---

SQL, ou langage de requête structuré, nous permet de collecter des données à partir d'une base de données à travers des requêtes. Il nous permet également d'insérer, de mettre à jour et de supprimer ces données. 

Dans cet article de blog, nous allons nous concentrer sur la manière de récupérer des données et de limiter les résultats en utilisant SQL. 

## Pourquoi devriez-vous limiter les résultats des requêtes SQL ?

Une base de données est généralement une énorme collection de données. Parfois, nous n'avons pas besoin de récupérer tous les résultats. Pour limiter les résultats, nous pouvons optimiser la requête. 

Limiter les résultats des requêtes est important pour les performances de la base de données. Récupérer un grand nombre de résultats lorsqu'ils ne sont pas nécessaires entraîne une charge supplémentaire sur la base de données et impacte l'expérience utilisateur. 

## Comment limiter les résultats des requêtes en SQL

La syntaxe est différente pour SQL Server, Oracle et MySQL pour limiter les données.

* MySQL utilise `LIMIT`.
* ORACLE utilise `FETCH FIRST`.
* MS Access et SQL Server utilisent `TOP`.

Nous verrons des exemples de fonctionnement de chacun d'eux en détail ci-dessous.

### Base de données de démonstration

Nous avons la table suivante nommée `students` avec leurs détails comme vous pouvez le voir ci-dessous :

<table>
<thead>
<tr>
<th>ID</th>
<th>Nom</th>
<th>Genre</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Ryan</td>
<td>M</td>
</tr>
<tr>
<td>2</td>
<td>Joanna</td>
<td>F</td>
</tr>
<tr>
<td>3</td>
<td>Miranda Andersen</td>
<td>F</td>
</tr>
<tr>
<td>4</td>
<td>Dalia Mata</td>
<td>F</td>
</tr>
<tr>
<td>5</td>
<td>Lilianna Boyd</td>
<td>F</td>
</tr>
<tr>
<td>6</td>
<td>Lexie Sharp</td>
<td>M</td>
</tr>
<tr>
<td>7</td>
<td>Jazlene Cordova</td>
<td>F</td>
</tr>
<tr>
<td>8</td>
<td>Brycen Werner</td>
<td>M</td>
</tr>
<tr>
<td>9</td>
<td>Karissa Turner</td>
<td>F</td>
</tr>
<tr>
<td>10</td>
<td>Aisha Dodson</td>
<td>F</td>
</tr>
<tr>
<td>11</td>
<td>Aydin Reeves</td>
<td>M</td>
</tr>
</tbody>
</table>

### Comment limiter une requête en MySQL

Voici la syntaxe pour MySQL.

```sql
SELECT  (expression)
FROM 
    table_name
LIMIT 5;

```

Par exemple, nous allons sélectionner les 5 premiers enregistrements de la table.

Utilisons notre table `students` pour cette démonstration.

```mysql
-- récupérer les 5 premières valeurs de la table

SELECT * FROM students
LIMIT 5;
```

Résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-7.png)

### Comment combiner LIMIT avec ORDER BY

Lorsque vous combinez LIMIT avec ORDER BY, vous pouvez obtenir des résultats plus significatifs. Par exemple, nous pouvons utiliser cela pour trouver les 5 meilleurs étudiants ayant obtenu plus de 70 % à leur examen.

Trions notre table `students` avec la colonne `name` et choisissons les 5 premiers résultats. Vous pouvez faire cela comme suit :

```sql
SELECT * FROM students
order by name
LIMIT 5;
```

Résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-13.png)

### Comment limiter les résultats – Syntaxe Oracle

Voici la syntaxe équivalente pour notre premier exemple en Oracle.

```sql
SELECT * FROM students
FETCH FIRST 5 ROWS ONLY;
```

Dans les anciennes versions d'Oracle, vous pouvez utiliser ROWNUM pour restreindre le nombre de lignes retournées par une requête.

Exemple :

```sql
SELECT * FROM 
students 
WHERE ROWNUM < 5;
```

### Comment limiter les résultats en SQL – Syntaxe MS Access

Voici la syntaxe équivalente pour notre premier exemple en MS Access.

```sql
SELECT TOP 5 * FROM students;

```

## Conclusion

La fonctionnalité LIMIT peut être très puissante pour l'optimisation des requêtes lorsqu'elle est combinée avec le tri. Les requêtes efficaces sont plus légères pour le système et plus rapides pour l'utilisateur. Il est toujours recommandé de limiter les résultats lorsque cela est applicable.