---
title: SQL DATE – Fonction, Requête, Format d'Exemple de Timestamp
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-11-15T18:58:58.000Z'
originalURL: https://freecodecamp.org/news/sql-date-function-query-timestamp-example-format
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/date.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: SQL DATE – Fonction, Requête, Format d'Exemple de Timestamp
seo_desc: 'Dates are an integral part of any programming language, and SQL is no exception.
  When you insert data into your SQL database, you can add a date and query the database
  based on that date.

  In this article, you’ll learn about DATE functions in SQL and ...'
---

Les dates sont une partie intégrante de tout langage de programmation, et SQL ne fait pas exception. Lorsque vous insérez des données dans votre base de données SQL, vous pouvez ajouter une date et interroger la base de données en fonction de cette date.

Dans cet article, vous apprendrez les fonctions DATE en SQL et comment interroger une base de données avec des dates. Nous examinerons également quelques fonctions de temps.

## Ce que nous allons couvrir
- [Fonctions de Date en SQL](#heading-fonctions-de-date-en-sql)
  - [ADDDATE()](#heading-adddate)
  - [CURRENT_DATE()](#heading-currentdate)
  - [CURRENT_TIME();](#heading-currenttime)
  - [CURRENT_TIMESTAMP();](#heading-currenttimestamp)
  - [NOW()](#heading-now)
  - [DATE](#heading-date)
  - [DATE_SUB](#heading-datesub)
  - [DATEDIFF](#heading-datediff)
  - [DAY](#heading-day)
  - [MONTH](#heading-month)
  - [YEAR](#heading-year)
- [Comment Interroger une Base de Données Basée sur des Dates](#heading-comment-interroger-une-base-de-donnees-basee-sur-des-dates)
- [Conclusion](#heading-conclusion)


## Fonctions de Date en SQL
### `ADDDATE()`

La fonction ADDDATE() fait ce que le nom implique – elle ajoute un intervalle à une `date` ou `datetime`.

Vous pouvez utiliser la fonction `ADDDATE()` dans ce format : `ADDDATE(date, INTERVAL valeur addunit)`.

- `date` est la date avec laquelle vous travaillez. Pour MySQL, le format de date est AAAA-MM-JJ et est requis.
- `INTERVAL` est un mot-clé requis
- `valeur` est un entier représentant l'intervalle que vous souhaitez ajouter
- `addunit` est ce que l'intervalle doit représenter. C'est-à-dire année, mois, jour, heures, minutes, secondes, et autres unités pertinentes.

Par exemple, l'exécution de la requête ci-dessous retourne '2022-10-22'. Cela signifie que 10 jours ont été ajoutés à '2022-10-12'.

```sql
SELECT ADDDATE("2022-10-12", INTERVAL 10 DAY);
```

![ss1-2](https://www.freecodecamp.org/news/content/images/2022/11/ss1-2.png)

Si vous le souhaitez, vous pouvez l'utiliser avec mois ou année :

![ss2-2](https://www.freecodecamp.org/news/content/images/2022/11/ss2-2.png)

### `CURRENT_DATE()`

La fonction CURRENT_DATE() montre exactement ce qu'elle dit – la date actuelle. Elle retourne la date au format AAAA-MM-JJ.

Par exemple, `SELECT CURRENT_DATE()` retourne la date à laquelle j'ai commencé à écrire cet article :
![ss3-1](https://www.freecodecamp.org/news/content/images/2022/11/ss3-1.png)

### `CURRENT_TIME();`

La fonction CURRENT_TIME montre l'heure actuelle.

```sql
SELECT CURRENT_TIME();
```

![ss4-1](https://www.freecodecamp.org/news/content/images/2022/11/ss4-1.png)

### `CURRENT_TIMESTAMP();`

La fonction current timestamp retourne la date et l'heure actuelles. C'est la combinaison de CURRENT_DATE() et CURRENT_TIME().

```sql
SELECT CURRENT_TIMESTAMP();
```

### `NOW()`

La fonction NOW() retourne la date et l'heure actuelles.

```sql
SELECT NOW();
```

![ss5-1](https://www.freecodecamp.org/news/content/images/2022/11/ss5-1.png)

### `DATE`

Vous pouvez utiliser la fonction DATE pour extraire la partie date d'un timestamp.

```sql
SELECT DATE("2022-11-14 12:00:00");
```

![ss6](https://www.freecodecamp.org/news/content/images/2022/11/ss6.png)

### `DATE_SUB`

La fonction DATE_SUB() soustrait un jour, un mois ou une année d'une date.
Dans la requête ci-dessous, j'ai soustrait 10 jours de la date à laquelle j'ai commencé à écrire cet article :

```sql
SELECT DATE_SUB("2022-11-14", INTERVAL 10 DAY);
```

![ss7](https://www.freecodecamp.org/news/content/images/2022/11/ss7.png)

### `DATEDIFF`

La fonction DATEDIFF() retourne le nombre de jours entre deux dates.

```sql
SELECT DATEDIFF("2023-11-14", "2022-11-14");
```

![ss8](https://www.freecodecamp.org/news/content/images/2022/11/ss8.png)

### `DAY`

Cette fonction retourne le jour dans une date spécifiée.

```sql
SELECT DAY("2022-11-14");
```

![ss9](https://www.freecodecamp.org/news/content/images/2022/11/ss9.png)

### `MONTH`

La fonction MONTH retourne le mois dans une date spécifiée.

```sql
SELECT MONTH("2022-11-14");
```

![ss10](https://www.freecodecamp.org/news/content/images/2022/11/ss10.png)

### `YEAR`

La fonction YEAR retourne l'année dans une date spécifiée.

```sql
SELECT YEAR("2022-11-14");
```

![ss11](https://www.freecodecamp.org/news/content/images/2022/11/ss11.png)

## Comment Interroger une Base de Données Basée sur des Dates
Pour vous montrer comment interroger une base de données en utilisant des dates, j'utiliserai le tableau ci-dessous :

![ss12](https://www.freecodecamp.org/news/content/images/2022/11/ss12.png)

Pour sélectionner une date particulière entre une date et une autre, vous pouvez utiliser les mots-clés `BETWEEN` et `AND` tout en spécifiant les dates.

Dans la requête ci-dessous, je sélectionne tous les éléments ajoutés à la base de données en 2021 :

```sql
SELECT *
FROM brands
WHERE date_added BETWEEN "2021-01-01" AND "2021-12-31";
```

![ss13-1](https://www.freecodecamp.org/news/content/images/2022/11/ss13-1.png)

En combinant les fonctions `DATE_SUB()` et `NOW()`, j'ai pu obtenir les éléments ajoutés à la base de données au cours des 3 derniers mois :

```sql
SELECT *
FROM brands
WHERE date_added > DATE_SUB(NOW(), INTERVAL 3 MONTH);
```

![ss14](https://www.freecodecamp.org/news/content/images/2022/11/ss14.png)

## Conclusion
Cet article vous a montré quelques fonctions importantes que vous pouvez utiliser pour travailler avec des dates et interroger votre base de données dans SQL.

Si vous trouvez l'article utile, n'hésitez pas à le partager avec vos amis et votre famille.

Merci d'avoir lu.