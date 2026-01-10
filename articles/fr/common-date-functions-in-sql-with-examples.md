---
title: Comment écrire les fonctions de date courantes en SQL avec des exemples
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2023-03-13T16:49:25.000Z'
originalURL: https://freecodecamp.org/news/common-date-functions-in-sql-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-bich-tran-760710.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Comment écrire les fonctions de date courantes en SQL avec des exemples
seo_desc: 'When querying data from a database, you will frequently encounter the date
  datatype. Depending on what you want to achieve, you may need to extract subset
  information from the date column, perform some operation, and so on.

  SQL provides a variety of ...'
---

Lors de l'interrogation de données à partir d'une base de données, vous rencontrerez fréquemment le type de données date. Selon ce que vous voulez accomplir, vous pourriez avoir besoin d'extraire des sous-ensembles d'informations de la colonne de date, d'effectuer certaines opérations, et ainsi de suite.

SQL propose une variété de fonctions de date qui peuvent vous aider dans votre tâche. Dans ce tutoriel, nous examinerons diverses fonctions de date courantes en SQL et quelques exemples pour montrer comment elles fonctionnent. Sans plus tarder, commençons.

Remarque : Il existe de nombreuses variantes de SQL, et les fonctions pour accomplir une tâche spécifique peuvent différer d'une variante à l'autre. Ce tutoriel se concentrera sur trois des variantes SQL les plus populaires : **PostgreSQL, MySQL et SQL Server**. Nous commencerons par les fonctions PostgreSQL, puis nous présenterons les variantes des autres systèmes si elles diffèrent de PostgreSQL.

## Types de données de date

Les types de données de date sont l'un des types de données intégrés en SQL que vous utilisez pour stocker des valeurs de date. Une valeur de date est généralement stockée dans tous les systèmes de gestion de bases de données ou variantes au format timestamp, c'est-à-dire `YYYY-MM-DD HH:MM:SS` – par exemple `2022-01-01 10:08:56`.

Avant de commencer, nous utiliserons cette table que nous avons créée pour expliquer la fonction dont nous parlerons plus loin dans l'article. Vous pouvez la créer en utilisant la requête suivante. Notez que la variante SQL que nous utilisons est PostgreSQL.

```sql
DROP TABLE IF EXISTS student;

CREATE TABLE student (
  student_id SERIAL PRIMARY KEY,
  student_name VARCHAR(30),
  admitted_date DATE
);

INSERT INTO student VALUES (11, 'Ibrahim', '2012-10-01');
INSERT INTO student VALUES (7, 'Taiwo', '2013-12-01');
INSERT INTO student VALUES (9, 'Nurain', '2012-11-21');
INSERT INTO student VALUES (8, 'Joel', '2012-10-31');
INSERT INTO student VALUES (10, 'Mustapha', '2015-11-01');
INSERT INTO student VALUES (5, 'Muritadoh', '2011-09-01');
INSERT INTO student VALUES (2, 'Yusuf', '2022-05-03');
INSERT INTO student VALUES (3, 'Habeebah', '2012-11-01');
INSERT INTO student VALUES (1, 'Tomiwa', '2013-04-01');
INSERT INTO student VALUES (4, 'Gbadebo', '2008-10-01');
INSERT INTO student VALUES (12, 'Tolu', '2009-11-21');


SELECT * FROM student;
```

## Fonctions de date SQL courantes

Examinons les fonctions de date courantes avec lesquelles vous travaillerez au quotidien.

### Comment utiliser la fonction `Now()`

Vous utilisez la fonction `Now()` pour renvoyer le timestamp actuel (date + heure) du système informatique où le système de gestion de base de données est actuellement hébergé. Dans PostgreSQL, elle inclut également le fuseau horaire du timestamp comme indiqué ci-dessous.

```javascript
SELECT NOW();
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-58.png align="left")

La fonction pour obtenir le timestamp actuel dans MySQL est également la même que dans PostgreSQL – `Now()`. Mais dans SQL Server, vous utilisez la fonction `CURRENT_TIMESTAMP`.

### Comment utiliser la fonction `current_date`

Cette fonction, comme son nom l'indique, obtient la date actuelle du système informatique sur lequel la base de données SQL s'exécute. Lors de la récupération de la date actuelle dans PostgreSQL, vous n'avez pas besoin d'utiliser de parenthèses, comme vous pouvez le voir ci-dessous :

```sql
SELECT current_date;
```

Dans MySQL, vous utilisez la fonction `[CURDATE](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_curdate)()` pour obtenir la date actuelle, mais SQL Server utilise `[GETDATE](https://learn.microsoft.com/en-us/sql/t-sql/functions/getdate-transact-sql?view=sql-server-ver16) ()`.

### Comment utiliser les fonctions `Extract()` ou `Date_Part()`

Vous utilisez les fonctions Extract ou date part pour extraire une certaine partie ou unité d'une date ou d'une colonne de date.

Commençons par la fonction Extract. Sa syntaxe ressemble à ceci :

```sql
EXTRACT(unit FROM date/date_column)
```

La partie unit de la fonction Extract est une unité que vous pouvez extraire d'une date telle que `DAY`, `WEEK`, `YEAR`, `QUARTER`, etc. Cliquez [ici](https://dev.mysql.com/doc/refman/8.0/en/expressions.html#temporal-intervals) pour voir la liste des unités que vous pouvez extraire d'une date ou d'une colonne de date en SQL.

Supposons par exemple que dans la table student ci-dessus que nous avons créée plus tôt, vous souhaitiez extraire l'année où les étudiants ont été admis de la colonne admitted\_date ; vous pouvez y parvenir en utilisant la fonction `EXTRACT()` comme indiqué ci-dessous.

```javascript
SELECT 
	*,
	EXTRACT(YEAR FROM admitted_date) As "Year of Admission"
FROM student;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-59.png align="left")

La fonction `EXTRACT()` n'est disponible que dans PostgreSQL et MySQL et fonctionne de manière similaire. Une autre fonction qui fonctionne comme `EXTRACT()` est `DATEPART()` et elle est également disponible dans PostgreSQL et SQL Server. Voyons comment fonctionne la fonction `DATEPART()`.

La syntaxe de Datepart dans PostgreSQL semble un peu différente de celle utilisée par SQL Server dans la mesure où elle comporte un trait de soulignement entre date et part. Vous devez également passer l'unité entre guillemets simples comme indiqué ci-dessous :

```sql
SELECT DATE_PART('Year', admitted_date)
FROM student;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-60.png align="left")

Pour SQL Server, il n'y aura pas de trait de soulignement entre date et part, et l'unité ne sera pas entourée de guillemets simples. Par exemple, le résultat ci-dessus peut être généré dans SQL Server comme indiqué ci-dessous.

```javascript
SELECT DATEPART(YEAR, admitted_date)
FROM student;
```

### Comment ajouter des intervalles ou des parties aux dates

Les intervalles sont des unités que vous pouvez ajouter à une date – par exemple un intervalle de jours, un intervalle de temps, et ainsi de suite.

Par exemple, supposons que vous vouliez ajouter un intervalle de 1 jour à toutes les dates d'une table particulière. Dans PostgreSQL, il n'y a pas de fonction dédiée que vous pouvez utiliser pour ajouter un intervalle à une date particulière. Au lieu de cela, vous pouvez le faire en utilisant des opérations arithmétiques.

La syntaxe pour y parvenir est indiquée ci-dessous :

```javascript
SELECT date/date_column + INTERVAL "# unit"
```

Où # est un entier tel que 3, 4, etc., et unit peut être Days, Year, etc. Cliquez [ici](https://dev.mysql.com/doc/refman/8.0/en/expressions.html#temporal-intervals) pour une liste des unités qui peuvent être passées comme intervalle.

Supposons, par exemple, que vous souhaitiez ajouter un intervalle de 3 jours à la colonne `admitted_date` dans la table student. Vous pouvez le faire dans PostgreSQL en utilisant la requête suivante :

```sql
SELECT 
	*,
	admitted_date + INTERVAL '3 Days' AS "3_daysadded"
FROM student;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-93.png align="left")

Maintenant que vous avez vu comment ajouter des intervalles aux dates dans PostgreSQL, voyons comment cela se fait dans MySQL et SQL Server. Dans MySQL et SQL Server, il existe des fonctions que vous pouvez utiliser pour ajouter des intervalles aux dates.

Dans MySQL, le nom de la fonction est `DATE_ADD()` et la syntaxe est indiquée ci-dessous :

```javascript
DATE_ADD(date/date_column, INTERVAL value unit)
```

Par exemple, vous pouvez obtenir la table ci-dessus en utilisant MySQL en tapant le code suivant :

```javascript
SELECT *,
	DATE_ADD(admitted_date, INTERVAL 3 DAY) AS "3_daysadded"
FROM student;
```

Dans SQL Server, la fonction que vous utilisez est similaire à celle de MySQL mais avec une petite différence. La syntaxe de la fonction utilisée est indiquée ci-dessous :

```javascript
DATEADD (datepart/unit , number , date/date_column)
```

Vous pouvez reproduire la table ci-dessus dans SQL Server comme ceci :

```sql
SELECT *,
	DATEADD (day , 3 , admitted_date) AS "3_daysadded"
FROM student;
```

### Comment soustraire des intervalles aux dates

La soustraction d'intervalles aux dates dans PostgreSQL fonctionne comme l'ajout d'intervalles, sauf que l'opérateur passe de plus à moins. Par exemple, supposons que vous souhaitiez soustraire 3 jours de la colonne admitted\_date. Vous pouvez le faire en utilisant le code ci-dessous :

```sql
SELECT 
	*,
	admitted_date - INTERVAL '3 Days' AS "3_dayssubtracted"
FROM student;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-95.png align="left")

Dans MySQL, vous utilisez la fonction DATESUB pour soustraire des intervalles de la date. Vous pouvez reproduire la table ci-dessus dans MySQL en utilisant la requête suivante :

```javascript
SELECT *,
	DATE_SUB(admitted_date, INTERVAL 3 DAY) AS "3_dayssubtracted"
FROM student;
```

Dans SQL Server, vous utilisez toujours la fonction DATEADD, mais au lieu de spécifier une valeur positive dans le paramètre de la fonction, vous utilisez une valeur négative. Cela ressemble à ceci :

```sql
SELECT *,
	DATEADD (day , -3 , admitted_date) AS "3_dayssubtracted"
FROM student;
```

### Comment soustraire deux dates

Pour soustraire deux dates dans PostgreSQL, il n'y a pas non plus de fonction dédiée. Mais vous pouvez utiliser des opérateurs arithmétiques pour obtenir le résultat souhaité.

```sql
SELECT '2012-10-31'::date -'2012-05-01'::date AS days;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-96.png align="left")

Dans MySQL, il existe une fonction appelée `[DATE_DIFF](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_datediff)()` que vous pouvez utiliser pour y parvenir, tandis que pour SQL Server, vous utilisez la fonction `[DATEDIFF](https://learn.microsoft.com/en-us/sql/t-sql/functions/datediff-transact-sql?view=sql-server-ver16)()`. Cliquez ici pour en savoir plus.

## Conclusion

Dans ce tutoriel, vous avez appris certaines fonctions de date courantes que vous utiliserez lorsque vous travaillerez avec des dates en SQL.

Vous avez appris comment obtenir le timestamp actuel, obtenir la date actuelle, extraire des parties d'une date, et comment ajouter ou soustraire des dates. Vous avez également appris comment chaque fonction de date diffère selon les variantes de SQL.

Merci de votre lecture. Vous pouvez consulter les ressources ci-dessous pour en savoir plus sur les fonctions de date dans les trois différentes variantes SQL abordées dans cet article.

1. [Fonctions de base de données Microsoft SQL](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver16)
    
2. [Fonctions et opérateurs date/heure Postgres](https://www.postgresql.org/docs/current/functions-datetime.html)
    
3. [Manuel de référence des fonctions date et heure MySQL](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html)