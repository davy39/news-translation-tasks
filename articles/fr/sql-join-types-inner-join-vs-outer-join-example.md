---
title: Types de Jointures SQL – Exemple de Jointure Interne VS Jointure Externe
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-24T00:08:46.000Z'
originalURL: https://freecodecamp.org/news/sql-join-types-inner-join-vs-outer-join-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-pixabay-269399.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Types de Jointures SQL – Exemple de Jointure Interne VS Jointure Externe
seo_desc: "In a relational database, all information should only be present once.\
  \ But you might have information that's separated into different tables that's related\
  \ to each other. \nAnd you might want to put this related information together to\
  \ analyse its dat..."
---

Dans une base de données relationnelle, toutes les informations ne doivent être présentes qu'une seule fois. Mais vous pouvez avoir des informations séparées dans différentes tables qui sont liées entre elles. 

Et vous pouvez vouloir rassembler ces informations liées pour analyser leurs données – c'est-à-dire que vous pouvez vouloir joindre toutes les données (ou une partie d'entre elles) ensemble. Dans ce cas, vous devrez utiliser l'instruction `JOIN` de SQL. Voyons comment cela fonctionne.

## Qu'est-ce qu'une JOINTURE en SQL ?

L'opérateur JOIN vous permet de combiner des informations liées de diverses manières, comme je l'ai brièvement expliqué ci-dessus. Il existe divers types de jointures, divisés en deux catégories principales – les jointures INTERNES et les jointures EXTERNES.

La plus grande différence entre une JOINTURE INTERNE et une JOINTURE EXTERNE est que la jointure interne ne conservera que les informations des deux tables qui sont liées entre elles (dans la table résultante). Une Jointure Externe, en revanche, conservera également les informations qui ne sont pas liées à l'autre table dans la table résultante.

Voyons comment les JOINTURES INTERNES et les JOINTURES EXTERNES fonctionnent en détail pour mieux les comprendre.

## Comment utiliser une JOINTURE INTERNE en SQL

La jointure interne ne conservera que les informations des deux tables jointes qui sont liées. Si vous imaginez les deux tables comme un [diagramme de Venn](https://en.wikipedia.org/wiki/Venn_diagram), la table résultant d'une JOINTURE INTERNE sera la partie surlignée en vert ci-dessous où elles se chevauchent :

![Deux cercles, l'un étiqueté table 1 et l'autre étiqueté table 2, avec une section commune. La section commune est colorée en vert.](https://www.freecodecamp.org/news/content/images/2021/08/i-1.PNG)
_Représentation du diagramme de Venn pour la Jointure Interne_

Voici la syntaxe pour une jointure interne :

```sql
SELECT * FROM table1
    JOIN table2
    ON relation;
```

Nous verrons comment cela fonctionne ci-dessous avec un exemple.

## Comment utiliser une JOINTURE EXTERNE en SQL

Si vous souhaitez conserver toutes les données, et pas seulement les données liées entre elles, vous pouvez utiliser une jointure EXTERNE. 

Il existe trois types de Jointures Externes : `LEFT JOIN`, `RIGHT JOIN`, et `FULL JOIN`. Les différences entre elles concernent les données non liées qu'elles conservent – elles peuvent provenir de la première table, de la seconde, ou des deux. Les cellules sans données à remplir auront une valeur de `NULL`.

Note : `LEFT JOIN` est principalement implémenté dans toutes les versions de SQL. Mais ce n'est pas le cas pour `RIGHT JOIN` et `FULL JOIN`, qui ne sont pas implémentés dans diverses versions de SQL.

Voyons comment chacune fonctionne individuellement. Ensuite, nous verrons comment elles fonctionnent toutes avec des exemples ci-dessous.

### LEFT OUTER JOIN en SQL

La LEFT OUTER JOIN, ou simplement Left Join, conservera les données non liées de la table de gauche (la première).

Vous pouvez l'imaginer avec un diagramme de Venn avec deux cercles, la table résultante étant la partie surlignée en vert qui inclut à la fois la partie commune/chevauchante, et le reste du cercle de gauche.

![Deux cercles avec une partie superposée. Le cercle de gauche est étiqueté comme table 1, le cercle de droite est étiqueté comme table 2. La partie superposée et le reste du cercle de la table 1 sont colorés en vert.](https://www.freecodecamp.org/news/content/images/2021/08/t1-1.PNG)
_Représentation du diagramme de Venn pour la Jointure Externe Gauche_

La syntaxe ressemble à ce qui suit. Vous verrez qu'elle est similaire à la syntaxe de la Jointure Interne, mais avec le mot-clé `LEFT` ajouté.

```sql
SELECT columns
  FROM table1
  LEFT JOIN table2
  ON relation;
```

### RIGHT OUTER JOIN en SQL

La RIGHT OUTER JOIN, ou simplement Right Join, conservera les données de la deuxième table qui ne sont pas liées à la première table.

Vous pouvez l'imaginer avec un diagramme de Venn avec deux cercles, la table résultante étant la partie surlignée en vert qui inclut à la fois la partie chevauchante, et le reste du cercle de droite.

![Deux cercles avec une partie superposée. Le cercle de gauche est étiqueté comme table 1, le cercle de droite est étiqueté comme table 2. La partie superposée et le reste du cercle de la table 2 sont colorés en vert.](https://www.freecodecamp.org/news/content/images/2021/08/t2-1.PNG)
_Représentation du diagramme de Venn pour la Jointure Externe Droite_

La syntaxe est la suivante, la seule différence est le mot-clé `RIGHT`.

```sql
SELECT columns
  FROM table1
  RIGHT JOIN table2
  ON relation;
```

### FULL OUTER JOIN en SQL

Vous pouvez penser à la FULL OUTER JOIN comme à la combinaison d'une Jointure Gauche et d'une Jointure Droite. Elle conservera toutes les lignes des deux tables, et les données manquantes seront remplies avec `NULL`.

Vous pouvez l'imaginer avec un diagramme de Venn avec deux cercles, la table résultante étant la partie surlignée en vert qui inclut tout : la partie chevauchante, le cercle de gauche, et le cercle de droite.

![Deux cercles avec une partie superposée. Le cercle de gauche est étiqueté comme table 1, le cercle de droite est étiqueté comme table 2. Tout est coloré en vert.](https://www.freecodecamp.org/news/content/images/2021/08/t1t2-1.PNG)
_Représentation du diagramme de Venn pour la Jointure Externe Complète_

La syntaxe est la suivante, en utilisant le mot-clé `FULL`.

```sql
SELECT columns
  FROM table1
  FULL JOIN table2
  ON relation;
```

## Exemples d'opérateur JOIN en SQL

Une base de données possible pour une clinique vétérinaire pourrait avoir une table pour les animaux de compagnie et une pour les propriétaires. Puisqu'un propriétaire pourrait avoir plusieurs animaux de compagnie, la table des animaux de compagnie aura une colonne `owner_id` qui pointe vers la table des propriétaires.

| id  | name   | age | owner_id |
| --- | ---    | --- | ---      |
| 1   | Fido   | 7   | 1        | 
| 2   | Missy  | 3   | 1        |
| 3   | Sissy  | 10  | 2        |
| 4   | Copper | 1   | 3        |
| 5   | Hopper | 2   | 0        |

| id | name | phone_number |
| --- | --- | --- |
| 1 | Johnny | 4567823 |
| 2 | Olly | 7486513 |
| 3 | Ilenia | 3481365 |
| 4 | Luise | 1685364 |

Vous pourriez utiliser une requête simple pour obtenir une table avec le nom de l'animal et le nom du propriétaire côte à côte. Faisons-le avec tous les différents opérateurs JOIN.

### Exemple de JOINTURE INTERNE en SQL

Faisons-le d'abord en utilisant `JOIN`.

Dans ce cas, vous `SELECT` la colonne `name` de la table `pets` (et la renommez `pet_name`). Ensuite, vous sélectionnez la colonne `name` de la table `owners`, et la renommez `owner`. Cela ressemblerait à ceci : `SELECT pets.name AS pet_name, owners.name AS owner`.

Vous utiliserez `FROM` pour dire que les colonnes proviennent de la table `pets`, et `JOIN` pour dire que vous voulez la joindre avec la table `owners`, en utilisant cette syntaxe : `FROM pets JOIN owner`.

Et enfin, vous direz que vous voulez joindre deux lignes ensemble lorsque la colonne `owner_id` dans la table `pets` est égale à la colonne `id` dans la table `owner` avec `ON pets.owner_id = owners.id`.

Voici le tout ensemble :

```sql
SELECT pets.name AS pet_name, owners.name AS owner
  FROM pets
  JOIN owners
  ON pets.owner_id = owners.id;
```

Vous obtiendrez une table comme ci-dessous, où seuls les animaux de compagnie connectés à un propriétaire et les propriétaires connectés à un animal de compagnie sont inclus.

| pet_name | owner |
| --- | --- |
| Fido | Johnny |
| Missy | Johnny |
| Sissy | Olly |
| Copper | Ilenia |

### Exemple de LEFT JOIN en SQL

Faisons la même requête en utilisant `LEFT JOIN` pour que vous puissiez voir la différence. La requête est la même, à l'exception de l'ajout du mot-clé `LEFT`.

```sql
SELECT pets.name AS pet_name, owners.name AS owner
  FROM pets
  LEFT JOIN owners
  ON pets.owner_id = owners.id;
```

Dans ce cas, les lignes de la table de gauche, `pets`, sont toutes conservées, et lorsque des données sont manquantes provenant de la table `owners`, elles sont remplies avec `NULL`.

| pet_name | owner |
| --- | --- |
| Fido | Johnny |
| Missy | Johnny |
| Sissy | Olly |
| Copper | Ilenia |
| Hopper | NULL |

Il semble qu'il y ait un animal de compagnie qui n'est pas enregistré avec un propriétaire.

### Exemple de RIGHT JOIN en SQL

Si vous faites la même requête en utilisant `RIGHT JOIN`, vous obtiendrez un résultat différent.

```sql
SELECT pets.name AS pet_name, owners.name AS owner
  FROM pets
  RIGHT JOIN owners
  ON pets.owner_id = owners.id;
```

Dans ce cas, toutes les lignes de la table de droite, `owners`, sont conservées, et si une valeur est manquante, elle est remplie avec `NULL`.

| pet_name | owner |
| --- | --- |
| Fido | Johnny |
| Missy | Johnny |
| Sissy | Olly |
| Copper | Ilenia |
| NULL | Louise |

Il semble qu'il y ait un propriétaire qui n'a pas d'animal de compagnie enregistré.

### Exemple de FULL JOIN en SQL

Vous pourriez faire la même requête à nouveau, en utilisant `FULL JOIN`.

```sql
SELECT pets.name AS pet_name, owners.name AS owner
  FROM pets
  FULL JOIN owners
  ON pets.owner_id = owners.id;
```

La table résultante est à nouveau différente – dans ce cas, toutes les lignes des deux tables sont conservées.

| pet_name | owner |
| --- | --- |
| Fido | Johnny |
| Missy | Johnny |
| Sissy | Olly |
| Copper | Ilenia |
| Hopper | NULL |
| NULL | Louise |

Il semble qu'il y ait un animal de compagnie sans propriétaire et un propriétaire sans animal de compagnie dans notre base de données.

# Conclusion

Dans une base de données relationnelle, toutes les données doivent être écrites une seule fois. Pour analyser ces données, vous avez besoin de quelque chose pour joindre les données liées ensemble. 

Dans cet article, vous avez appris comment utiliser l'opérateur JOIN pour ce faire. J'espère qu'il vous sera utile, amusez-vous !