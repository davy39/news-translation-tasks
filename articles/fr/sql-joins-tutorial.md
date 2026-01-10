---
title: 'Tutoriel sur les jointures SQL : Cross Join, Full Outer Join, Inner Join,
  Left Join et Right Join.'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-28T15:30:47.000Z'
originalURL: https://freecodecamp.org/news/sql-joins-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98fc740569d1a4ca1d31.jpg
tags:
- name: data analytics
  slug: data-analytics
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: 'Tutoriel sur les jointures SQL : Cross Join, Full Outer Join, Inner Join,
  Left Join et Right Join.'
seo_desc: 'By John Mosesman

  SQL joins allow our relational database management systems to be, well, relational.

  Joins allow us to re-construct our separated database tables back into the relationships
  that power our applications.

  In this article, we''ll look at ...'
---

Par John Mosesman

Les jointures SQL permettent à nos systèmes de gestion de bases de données relationnelles d'être, eh bien, _relationnels_.

Les jointures nous permettent de reconstruire nos tables de base de données séparées en relations qui alimentent nos applications.

Dans cet article, nous examinerons chaque type de jointure en SQL et comment les utiliser.

Voici ce que nous allons couvrir :

* [Qu'est-ce qu'une jointure ?](#heading-quest-ce-quune-jointure)
* [Installation de votre base de données](#heading-installation-de-votre-base-de-donnees)
* `[CROSS JOIN](#heading-cross-join)` 
* [Configuration de nos données d'exemple (réalisateurs et films)](#heading-creation-des-realisateurs-et-des-films)
* `[FULL OUTER JOIN](#heading-full-outer-join)`
* `[INNER JOIN](#heading-inner-join)`
* [`LEFT JOIN` / `RIGHT JOIN`](#heading-left-join-right-join)
* [Filtrage en utilisant `LEFT JOIN`](#heading-filtrage-en-utilisant-left-join)
* [Jointures multiples](#heading-jointures-multiples)
* [Jointures avec conditions supplémentaires](#heading-jointures-avec-conditions-supplementaires)
* [La réalité sur l'écriture de requêtes avec des jointures](#heading-la-realite-sur-lecriture-de-requetes-avec-des-jointures)

(_Alerte spoiler_ : nous couvrirons cinq types différents, mais vous n'avez vraiment besoin d'en connaître que deux !)

## Qu'est-ce qu'une jointure ?

Une **jointure** est une opération qui combine deux lignes en une seule ligne.

Ces lignes proviennent généralement de deux tables différentes, mais ce n'est pas obligatoire.

Avant de voir comment écrire la jointure elle-même, examinons à quoi ressemble le résultat d'une jointure.

Prenons par exemple un système qui stocke des informations sur les utilisateurs et leurs adresses.

Les lignes de la table qui stocke les informations sur les utilisateurs pourraient ressembler à ceci :

```
 id |     name     |        email        | age
----+--------------+---------------------+-----
  1 | John Smith   | johnsmith@gmail.com |  25
  2 | Jane Doe     | janedoe@Gmail.com   |  28
  3 | Xavier Wills | xavier@wills.io     |  3
...
(7 rows)
```

Et les lignes de la table qui stocke les informations d'adresse pourraient ressembler à ceci :

```
 id |      street       |     city      | state | user_id
----+-------------------+---------------+-------+---------
  1 | 1234 Main Street  | Oklahoma City | OK    |       1
  2 | 4444 Broadway Ave | Oklahoma City | OK    |       2
  3 | 5678 Party Ln     | Tulsa         | OK    |       3
(3 rows)
```

Nous pourrions écrire des requêtes séparées pour récupérer à la fois les informations sur les utilisateurs et les informations d'adresse, mais idéalement, nous pourrions écrire _une seule requête_ et recevoir tous les utilisateurs et leurs adresses dans le même ensemble de résultats.

C'est exactement ce qu'une jointure nous permet de faire !

Nous verrons comment écrire ces jointures bientôt, mais si nous joignons nos informations utilisateur à nos informations d'adresse, nous pourrions obtenir un résultat comme ceci :

```
 id |     name     |        email        | age | id |      street       |     city      | state | user_id
----+--------------+---------------------+-----+----+-------------------+---------------+-------+---------
  1 | John Smith   | johnsmith@gmail.com |  25 |  1 | 1234 Main Street  | Oklahoma City | OK    |       1
  2 | Jane Doe     | janedoe@Gmail.com   |  28 |  2 | 4444 Broadway Ave | Oklahoma City | OK    |       2
  3 | Xavier Wills | xavier@wills.io     |  35 |  3 | 5678 Party Ln     | Tulsa         | OK    |       3
(3 rows)

```

Ici, nous voyons tous nos utilisateurs et leurs adresses dans un seul ensemble de résultats.

Outre la production d'un ensemble de résultats combiné, une autre utilisation importante des jointures est de tirer des informations supplémentaires dans notre requête que nous pouvons filtrer.

Par exemple, si nous voulions envoyer du courrier physique à tous les utilisateurs qui vivent à Oklahoma City, nous pourrions utiliser cet ensemble de résultats joint et filtrer en fonction de la colonne `city`.

Maintenant que nous connaissons le but des jointures, commençons à en écrire quelques-unes !

## Installation de votre base de données

Avant de pouvoir écrire nos requêtes, nous devons configurer notre base de données.

Pour ces exemples, nous utiliserons PostgreSQL, mais les requêtes et les concepts présentés ici se traduiront facilement à tout autre système de base de données moderne (comme MySQL, SQL Server, etc.).

Pour travailler avec notre base de données PostgreSQL, nous pouvons utiliser [`psql`](https://www.postgresql.org/docs/current/app-psql.html), le programme interactif en ligne de commande de PostgreSQL. Si vous avez un autre client de base de données que vous aimez utiliser, c'est bien aussi.

Pour commencer, créons notre base de données. Avec PostgreSQL déjà [installé](https://www.postgresql.org/download/), nous pouvons exécuter la commande `createdb <nom-de-la-base-de-donnees>` dans notre terminal pour créer une nouvelle base de données. J'ai appelé la mienne `fcc` :

```bash
$ createdb fcc

```

Ensuite, démarrons la console interactive en utilisant la commande `psql` et connectons-nous à la base de données que nous venons de créer en utilisant `\c <nom-de-la-base-de-donnees>` :

```bash
$ psql
psql (11.5)
Type "help" for help.

john=# \c fcc
You are now connected to database "fcc" as user "john".
fcc=#

```

> **Note :** J'ai nettoyé la sortie de `psql` dans ces exemples pour la rendre plus facile à lire, donc ne vous inquiétez pas si la sortie montrée ici n'est pas exactement ce que vous avez vu dans votre terminal.

Je vous encourage à suivre ces exemples et à exécuter ces requêtes vous-même. Vous apprendrez et retendrez bien plus en travaillant à travers ces exemples plutôt qu'en les lisant simplement.

Passons maintenant aux jointures !

## `CROSS JOIN` 

Le type de jointure le plus simple que nous pouvons faire est un `CROSS JOIN` ou _"produit cartésien"_.

Cette jointure prend chaque ligne d'une table et la joint avec chaque ligne de l'autre table.

Si nous avions deux listes, l'une contenant `1, 2, 3` et l'autre contenant `A, B, C`, le produit cartésien de ces deux listes serait ceci :

```
1A, 1B, 1C
2A, 2B, 2C
3A, 3B, 3C

```

Chaque valeur de la première liste est associée à chaque valeur de la deuxième liste.

Écrivons ce même exemple sous forme de requête SQL.

Tout d'abord, créons deux tables très simples et insérons quelques données :

```sql
CREATE TABLE letters(
  letter TEXT
);

INSERT INTO letters(letter) VALUES ('A'), ('B'), ('C');

CREATE TABLE numbers(
  number TEXT
);

INSERT INTO numbers(number) VALUES (1), (2), (3);

```

Nos deux tables, `letters` et `numbers`, n'ont qu'une seule colonne : un simple champ de texte.

Maintenant, joignons-les avec un `CROSS JOIN` :

```sql
SELECT *
FROM letters
CROSS JOIN numbers;

```

```
 letter | number
--------+--------
 A      | 1
 A      | 2
 A      | 3
 B      | 1
 B      | 2
 B      | 3
 C      | 1
 C      | 2
 C      | 3
(9 rows)


```

C'est le type de jointure le plus simple que nous pouvons faire, mais même dans cet exemple simple, nous pouvons voir la jointure à l'œuvre : les deux lignes séparées (une de `letters` et une de `numbers`) ont été _jointes_ pour former une seule ligne.

Bien que ce type de jointure soit souvent discuté comme un simple exemple académique, il a au moins un bon cas d'utilisation : couvrir des plages de dates.

### `CROSS JOIN` avec des plages de dates

Un bon cas d'utilisation d'un `CROSS JOIN` est de prendre chaque ligne d'une table et de l'appliquer à chaque jour d'une plage de dates.

Supposons, par exemple, que vous construisiez une application qui suit les tâches quotidiennes, comme se brosser les dents, prendre le petit-déjeuner ou se doucher.

Si vous vouliez générer un enregistrement _pour chaque tâche_ et _pour chaque jour_ de la semaine dernière, vous pourriez utiliser un `CROSS JOIN` contre une plage de dates.

Pour créer cette plage de dates, nous pouvons utiliser la fonction `[generate_series](https://www.postgresql.org/docs/current/functions-srf.html)` :

```sql
SELECT generate_series(
  (CURRENT_DATE - INTERVAL '5 day'),
  CURRENT_DATE,
  INTERVAL '1 day'
)::DATE AS day;

```

La fonction `generate_series` prend trois paramètres.

Le premier paramètre est la valeur de départ. Dans cet exemple, nous utilisons `CURRENT_DATE - INTERVAL '5 day'`. Cela retourne la date actuelle moins cinq jours, ou "il y a cinq jours".

Le deuxième paramètre est la date actuelle (`CURRENT_DATE`).

Le troisième paramètre est l'"intervalle de pas" ou combien nous voulons incrémenter la valeur chaque fois. Puisque ce sont des tâches quotidiennes, nous utiliserons l'intervalle d'un jour (`INTERVAL '1 day'`).

En mettant tout ensemble, cela génère une série de dates commençant il y a cinq jours, se terminant aujourd'hui, et allant un jour à la fois.

Enfin, nous supprimons la partie heure en convertissant la sortie de ces valeurs en date en utilisant `::DATE`, et nous aliasons cette colonne en utilisant `AS day` pour rendre la sortie un peu plus belle.

La sortie de cette requête est les cinq derniers jours plus aujourd'hui :

```
    day
------------
 2020-08-19
 2020-08-20
 2020-08-21
 2020-08-22
 2020-08-23
 2020-08-24
(6 rows)

```

Revenons à notre exemple de tâches par jour, créons une table simple pour contenir les tâches que nous voulons accomplir et insérons quelques tâches :

```sql
CREATE TABLE tasks(
  name TEXT
);

INSERT INTO tasks(name) VALUES
('Brush teeth'),
('Eat breakfast'),
('Shower'),
('Get dressed');

```

Notre table `tasks` n'a qu'une seule colonne, `name`, et nous avons inséré quatre tâches dans cette table.

Maintenant, faisons un `CROSS JOIN` de nos tâches avec la requête pour générer les dates :

```sql
SELECT
  tasks.name,
  dates.day
FROM tasks
CROSS JOIN
(
  SELECT generate_series(
    (CURRENT_DATE - INTERVAL '5 day'),
    CURRENT_DATE,
    INTERVAL '1 day'
  )::DATE	AS day
) AS dates

```

(Puisque notre requête de génération de dates n'est pas une table réelle, nous l'écrivons simplement comme une sous-requête.)

De cette requête, nous retournons le nom de la tâche et le jour, et l'ensemble de résultats ressemble à ceci :

```
     name      |    day
---------------+------------
 Brush teeth   | 2020-08-19
 Brush teeth   | 2020-08-20
 Brush teeth   | 2020-08-21
 Brush teeth   | 2020-08-22
 Brush teeth   | 2020-08-23
 Brush teeth   | 2020-08-24
 Eat breakfast | 2020-08-19
 Eat breakfast | 2020-08-20
 Eat breakfast | 2020-08-21
 Eat breakfast | 2020-08-22
 ...
 (24 rows)

```

Comme nous nous y attendions, nous obtenons une ligne pour chaque tâche pour chaque jour de notre plage de dates.

Le `CROSS JOIN` est la jointure la plus simple que nous pouvons faire, mais pour examiner les prochains types, nous aurons besoin d'une configuration de table plus réaliste.

## Création de réalisateurs et de films

Pour illustrer les types de jointures suivants, nous utiliserons l'exemple des _films_ et des _réalisateurs de films_.

Dans cette situation, un film a un réalisateur, mais un film n'est pas _obligé_ d'avoir un réalisateur, imaginez un nouveau film étant annoncé mais le choix du réalisateur n'a pas encore été confirmé.

Notre table `directors` stockera le nom de chaque réalisateur, et la table `movies` stockera le nom du film ainsi qu'une référence au réalisateur du film (s'il en a un).

Créons ces deux tables et insérons quelques données :

```sql
CREATE TABLE directors(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

INSERT INTO directors(name) VALUES
('John Smith'),
('Jane Doe'),
('Xavier Wills')
('Bev Scott'),
('Bree Jensen');

CREATE TABLE movies(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  director_id INTEGER REFERENCES directors 
);

INSERT INTO movies(name, director_id) VALUES
('Movie 1', 1),
('Movie 2', 1),
('Movie 3', 2),
('Movie 4', NULL),
('Movie 5', NULL);

```

Nous avons cinq réalisateurs, cinq films, et trois de ces films ont des réalisateurs assignés. Le réalisateur ID 1 a deux films, et le réalisateur ID 2 en a un.

## `FULL OUTER JOIN`

Maintenant que nous avons des données avec lesquelles travailler, examinons le `FULL OUTER JOIN`.

Un `FULL OUTER JOIN` a quelques similitudes avec un `CROSS JOIN`, mais il a quelques différences clés.

La première différence est qu'un `FULL OUTER JOIN` nécessite une **condition de jointure**.

Une condition de jointure spécifie comment les lignes entre les deux tables sont liées les unes aux autres et selon quels critères elles doivent être jointes.

Dans notre exemple, notre table `movies` a une référence au réalisateur via la colonne `director_id`, et cette colonne correspond à la colonne `id` de la table `directors`. Ce sont les deux colonnes que nous utiliserons comme condition de jointure.

Voici comment nous écrivons cette jointure entre nos deux tables :

```sql
SELECT *
FROM movies
FULL OUTER JOIN directors
  ON directors.id = movies.director_id;

```

Remarquez la condition de jointure que nous avons spécifiée qui associe le film à son réalisateur : `ON movies.director_id = directors.id`.

Notre ensemble de résultats ressemble à un produit cartésien étrange :

```
  id  |  name   | director_id |  id  |     name
------+---------+-------------+------+--------------
    1 | Movie 1 |           1 |    1 | John Smith
    2 | Movie 2 |           1 |    1 | John Smith
    3 | Movie 3 |           2 |    2 | Jane Doe
    4 | Movie 4 |        NULL | NULL | NULL
    5 | Movie 5 |        NULL | NULL | NULL
 NULL | NULL    |        NULL |    5 | Bree Jensen
 NULL | NULL    |        NULL |    4 | Bev Scott
 NULL | NULL    |        NULL |    3 | Xavier Wills
(8 rows)

```

Les premières lignes que nous voyons sont celles où le film avait un réalisateur, et notre condition de jointure a été évaluée à vrai.

Cependant, après ces lignes, nous voyons chacune des lignes restantes _de chaque table_, mais avec des valeurs `NULL` là où l'autre table n'avait pas de correspondance.

> **Note :** si vous n'êtes pas familier avec les valeurs `NULL`, [voir mon explication ici](https://www.freecodecamp.org/news/sql-operators-tutorial/#dealing-with-missing-data-null-) dans ce tutoriel sur les opérateurs SQL.

Nous voyons également une autre différence entre le `CROSS JOIN` et le `FULL OUTER JOIN` ici. Un `FULL OUTER JOIN` retourne une ligne distincte de chaque table, contrairement au `CROSS JOIN` qui en a plusieurs.

## `INNER JOIN`

Le type de jointure suivant, `INNER JOIN`, est l'un des types de jointures les plus couramment utilisés.

Une jointure interne **ne retourne que les lignes où la condition de jointure est vraie.**

Dans notre exemple, une jointure interne entre nos tables `movies` et `directors` ne retournerait que les enregistrements où le film a été assigné à un réalisateur.

La syntaxe est essentiellement la même qu'avant :

```sql
SELECT *
FROM movies
INNER JOIN directors
  ON directors.id = movies.director_id;

```

Notre résultat montre les trois films qui ont un réalisateur :

```
 id |  name   | director_id | id |    name
----+---------+-------------+----+------------
  1 | Movie 1 |           1 |  1 | John Smith
  2 | Movie 2 |           1 |  1 | John Smith
  3 | Movie 3 |           2 |  2 | Jane Doe
(3 rows)

```

Puisqu'une jointure interne n'inclut que les lignes qui correspondent à la condition de jointure, _l'ordre des deux tables dans la jointure n'a pas d'importance._

Si nous inversons l'ordre des tables dans la requête, nous obtenons le même résultat :

```sql
SELECT *
FROM directors
INNER JOIN movies
  ON movies.director_id = directors.id;

```

```
 id |    name    | id |  name   | director_id
----+------------+----+---------+-------------
  1 | John Smith |  1 | Movie 1 |           1
  1 | John Smith |  2 | Movie 2 |           1
  2 | Jane Doe   |  3 | Movie 3 |           2
(3 rows)

```

Puisque nous avons listé la table `directors` en premier dans cette requête et que nous avons sélectionné toutes les colonnes (`SELECT *`), nous voyons les données des colonnes `directors` en premier, puis les colonnes de `movies`, mais les données résultantes sont les mêmes.

C'est une propriété utile des jointures internes, mais ce n'est pas vrai pour tous les types de jointures, comme notre prochain type.

## `LEFT JOIN` / `RIGHT JOIN`

Ces deux prochains types de jointures utilisent un modificateur (`LEFT` ou `RIGHT`) qui affecte les données de quelle table sont incluses dans l'ensemble de résultats.

> **Note :** le `LEFT JOIN` et le `RIGHT JOIN` peuvent également être appelés `LEFT OUTER JOIN` et `RIGHT OUTER JOIN`.

Ces jointures sont utilisées dans les requêtes où nous voulons retourner toutes les données d'une table particulière et, _si elles existent_, les données de la table associée également.

Si les données associées n'existent pas, nous obtenons toujours toutes les données de la table "primaire".

C'est une requête pour des informations sur une chose particulière et des informations bonus si ces informations bonus existent.

Cela sera simple à comprendre avec un exemple. Trouvons tous les films et leurs réalisateurs, mais nous ne nous soucions pas s'ils ont un réalisateur ou non, c'est un bonus :

```sql
SELECT *
FROM movies
LEFT JOIN directors
  ON directors.id = movies.director_id;

```

La requête suit notre même modèle qu'avant, nous avons simplement spécifié la jointure comme un `LEFT JOIN`.

Dans cet exemple, la table `movies` est la table "de gauche".

Si nous écrivons la requête sur une seule ligne, cela rend cela un peu plus facile à voir :

```sql
... FROM movies LEFT JOIN directors ...

```

**Un left join retourne tous les enregistrements de la table "de gauche".**

Un left join retourne toutes les lignes de la table "de droite" **qui correspondent à la condition de jointure.**

Les lignes de la table "de droite" qui **ne correspondent pas à la condition de jointure sont retournées comme `NULL`.**

```
 id |  name   | director_id |  id  |    name
----+---------+-------------+------+------------
  1 | Movie 1 |           1 |    1 | John Smith
  2 | Movie 2 |           1 |    1 | John Smith
  3 | Movie 3 |           2 |    2 | Jane Doe
  4 | Movie 4 |        NULL | NULL | NULL
  5 | Movie 5 |        NULL | NULL | NULL
(5 rows)

```

En regardant cet ensemble de résultats, nous pouvons voir pourquoi ce type de jointure est utile pour les requêtes de type _"tout cela et, si cela existe, un peu de cela"_.

### `RIGHT JOIN`

Le `RIGHT JOIN` fonctionne exactement comme le `LEFT JOIN`, sauf que les règles concernant les deux tables sont inversées.

Dans un right join, toutes les lignes de la table "de droite" sont retournées. La table "de gauche" est retournée conditionnellement en fonction de la condition de jointure.

Utilisons la même requête que ci-dessus mais substituons `LEFT JOIN` par `RIGHT JOIN` :

```sql
SELECT *
FROM movies
RIGHT JOIN directors
  ON directors.id = movies.director_id;

```

```
  id  |  name   | director_id | id |     name
------+---------+-------------+----+--------------
    1 | Movie 1 |           1 |  1 | John Smith
    2 | Movie 2 |           1 |  1 | John Smith
    3 | Movie 3 |           2 |  2 | Jane Doe
 NULL | NULL    |        NULL |  5 | Bree Jensen
 NULL | NULL    |        NULL |  4 | Bev Scott
 NULL | NULL    |        NULL |  3 | Xavier Wills
(6 rows)

```

Notre ensemble de résultats retourne maintenant chaque ligne de `directors` et, si elle existe, les données de `movies`.

Tout ce que nous avons fait est de changer quelle table nous considérons comme la "principale", celle dont nous voulons voir toutes les données, indépendamment du fait que ses données associées existent.

### `LEFT JOIN` / `RIGHT JOIN` dans les applications de production

Dans une application de production, je n'utilise jamais que `LEFT JOIN` et je n'utilise jamais `RIGHT JOIN`.

Je fais cela parce que, à mon avis, un `LEFT JOIN` rend la requête plus facile à lire et à comprendre.

Lorsque j'écris des requêtes, j'aime penser à commencer avec un ensemble de résultats "de base", disons tous les films, puis à inclure (ou à soustraire) des groupes de choses à partir de cette base.

Parce que j'aime commencer avec une base, le `LEFT JOIN` correspond à cette ligne de pensée. Je veux toutes les lignes de ma table de base (la table "de gauche"), et je veux conditionnellement les lignes de la table "de droite".

En pratique, je ne pense pas avoir jamais vu un `RIGHT JOIN` dans une application de production. Il n'y a rien de mal avec un `RIGHT JOIN`, je pense simplement que cela rend la requête plus difficile à comprendre.

### Réécrire `RIGHT JOIN`

Si nous voulions inverser notre scénario ci-dessus et retourner tous les réalisateurs et conditionnellement leurs films, nous pouvons facilement réécrire le `RIGHT JOIN` en un `LEFT JOIN`.

Tout ce que nous devons faire est d'inverser l'ordre des tables dans la requête, et de changer `RIGHT` en `LEFT` :

```sql
SELECT *
FROM directors
LEFT JOIN movies
  ON movies.director_id = directors.id;

```

> **Note :** J'aime mettre la table qui est jointe (la table "de droite", dans l'exemple ci-dessus `movies`) en premier dans la condition de jointure (`ON movies.director_id = ...`), mais ce n'est que ma préférence personnelle.

## Filtrage en utilisant `LEFT JOIN`

Il y a deux cas d'utilisation pour utiliser un `LEFT JOIN` (ou `RIGHT JOIN`).

Le premier cas d'utilisation que nous avons déjà couvert : retourner toutes les lignes d'une table et conditionnellement d'une autre.

Le deuxième cas d'utilisation est de retourner les lignes de la première table **où les données de la deuxième table ne sont pas présentes.**

Le scénario serait le suivant : trouver les réalisateurs _qui n'appartiennent pas à un film._

Pour ce faire, nous commencerons par un `LEFT JOIN` et notre table `directors` sera la table principale ou "de gauche" :

```sql
SELECT *
FROM directors
LEFT JOIN movies
  ON movies.director_id = directors.id;

```

Pour un réalisateur qui n'appartient pas à un film, les colonnes de la table `movies` sont `NULL` :

```
 id |     name     |  id  |  name   | director_id
----+--------------+------+---------+-------------
  1 | John Smith   |    1 | Movie 1 |           1
  1 | John Smith   |    2 | Movie 2 |           1
  2 | Jane Doe     |    3 | Movie 3 |           2
  5 | Bree Jensen  | NULL | NULL    |        NULL
  4 | Bev Scott    | NULL | NULL    |        NULL
  3 | Xavier Wills | NULL | NULL    |        NULL
(6 rows)

```

Dans notre exemple, les réalisateurs ID 3, 4 et 5 n'appartiennent pas à un film.

Pour filtrer notre ensemble de résultats à ces lignes uniquement, nous pouvons ajouter une clause `WHERE` pour ne retourner que les lignes où les données du film sont `NULL` :

```sql
SELECT *
FROM directors
LEFT JOIN movies
  ON movies.director_id = directors.id
WHERE movies.id IS NULL;

```

```
 id |     name     |  id  | name | director_id
----+--------------+------+------+-------------
  5 | Bree Jensen  | NULL | NULL |        NULL
  4 | Bev Scott    | NULL | NULL |        NULL
  3 | Xavier Wills | NULL | NULL |        NULL
(3 rows)

```

Et voici nos trois réalisateurs sans film !

Il est courant d'utiliser la colonne `id` de la table pour filtrer (`WHERE movies.id IS NULL`), mais toutes les colonnes de la table `movies` sont `NULL`, donc n'importe laquelle d'entre elles fonctionnerait.

(Puisque nous savons que toutes les colonnes de la table `movies` seront `NULL`, dans la requête ci-dessus, nous pourrions simplement écrire `SELECT directors.*` au lieu de `SELECT *` pour ne retourner que toutes les informations du réalisateur.)

### Utilisation de `LEFT JOIN` pour trouver des correspondances

Dans notre requête précédente, nous avons trouvé des réalisateurs qui _n'appartenaient pas_ à des films.

En utilisant notre même structure, nous pourrions trouver des réalisateurs qui _appartiennent_ à des films en changeant notre condition `WHERE` pour rechercher des lignes où les données du film ne sont _pas_ `NULL` :

```sql
SELECT *
FROM directors
LEFT JOIN movies
  ON movies.director_id = directors.id
WHERE movies.id IS NOT NULL;

```

```
 id |    name    | id |  name   | director_id
----+------------+----+---------+-------------
  1 | John Smith |  1 | Movie 1 |           1
  1 | John Smith |  2 | Movie 2 |           1
  2 | Jane Doe   |  3 | Movie 3 |           2
(3 rows)

```

Cela peut sembler pratique, mais nous venons en fait de réimplémenter `INNER JOIN` !

## Jointures multiples

Nous avons vu comment joindre deux tables ensemble, mais qu'en est-il de plusieurs jointures à la suite ?

C'est en fait assez simple, mais pour illustrer cela, nous avons besoin d'une troisième table : `tickets`.

Cette table représentera les billets vendus pour un film :

```sql
CREATE TABLE tickets(
  id SERIAL PRIMARY KEY,
  movie_id INTEGER REFERENCES movies NOT NULL
);

INSERT INTO tickets(movie_id) VALUES (1), (1), (3);

```

La table `tickets` a simplement un `id` et une référence au film : `movie_id`.

Nous avons également inséré deux billets vendus pour le film ID 1, et un billet vendu pour le film ID 3.

Maintenant, joignons `directors` à `movies`, puis `movies` à `tickets` !

```sql
SELECT *
FROM directors
INNER JOIN movies
  ON movies.director_id = directors.id
INNER JOIN tickets
  ON tickets.movie_id = movies.id;

```

Puisque ce sont des jointures internes, l'ordre dans lequel nous écrivons les jointures n'a pas d'importance. Nous aurions pu commencer par `tickets`, puis joindre `movies`, et ensuite joindre `directors`.

Cela revient à ce que vous essayez de requêter et à ce qui rend la requête la plus compréhensible.

Dans notre ensemble de résultats, nous remarquerons que nous avons encore réduit les lignes qui sont retournées :

```
 id |    name    | id |  name   | director_id | id | movie_id
----+------------+----+---------+-------------+----+----------
  1 | John Smith |  1 | Movie 1 |           1 |  1 |        1
  1 | John Smith |  1 | Movie 1 |           1 |  2 |        1
  2 | Jane Doe   |  3 | Movie 3 |           2 |  3 |        3
(3 rows)

```

Cela a du sens car nous avons ajouté un autre `INNER JOIN`. En effet, cela ajoute une autre condition _"ET"_ à notre requête.

Notre requête dit essentiellement : _"retourner tous les réalisateurs qui appartiennent à des films **qui ont également** des ventes de billets."_

Si, au lieu de cela, nous voulions trouver des réalisateurs qui appartiennent à des films _qui peuvent ne pas avoir encore de ventes de billets_, nous pourrions substituer notre dernier `INNER JOIN` par un `LEFT JOIN` :

```sql
SELECT *
FROM directors
JOIN movies
  ON movies.director_id = directors.id
LEFT JOIN tickets
  ON tickets.movie_id = movies.id;

```

Nous pouvons voir que `Movie 2` est maintenant de retour dans l'ensemble de résultats :

```
 id |    name    | id |  name   | director_id |  id  | movie_id
----+------------+----+---------+-------------+------+----------
  1 | John Smith |  1 | Movie 1 |           1 |    1 |        1
  1 | John Smith |  1 | Movie 1 |           1 |    2 |        1
  2 | Jane Doe   |  3 | Movie 3 |           2 |    3 |        3
  1 | John Smith |  2 | Movie 2 |           1 | NULL |     NULL
(4 rows)

```

Ce film n'avait aucune vente de billets, donc il était précédemment exclu de l'ensemble de résultats en raison du `INNER JOIN`.

Je laisserai cela comme un _Exercice Pour Le Lecteur™_, mais comment trouveriez-vous des réalisateurs qui appartiennent à des films qui **n'ont** aucune vente de billets ?

### Ordre d'exécution des jointures

En fin de compte, nous ne nous soucions pas vraiment de l'ordre dans lequel les jointures sont exécutées.

L'une des différences clés entre SQL et les autres langages de programmation modernes est que SQL est un langage **déclaratif**.

Cela signifie que nous spécifions le résultat que nous voulons, mais nous ne spécifions pas les détails d'exécution, ces détails sont laissés au planificateur de requêtes de la base de données. Nous spécifions les jointures que nous voulons et les conditions sur elles, et le planificateur de requêtes gère le reste.

Mais, en réalité, la base de données ne joint pas trois tables ensemble en même temps. Au lieu de cela, elle joindra probablement les deux premières tables ensemble en un résultat intermédiaire, puis joindra cet ensemble de résultats intermédiaire à la troisième table.

(**Note :** Ceci est une explication quelque peu simplifiée.)

Ainsi, lorsque nous travaillons avec plusieurs jointures dans des requêtes, nous pouvons simplement les considérer comme une série de jointures entre deux tables, bien que l'une de ces tables puisse devenir assez grande.

## Jointures avec conditions supplémentaires

Le dernier sujet que nous aborderons est une jointure avec des conditions supplémentaires.

Similaire à une clause `WHERE`, nous pouvons ajouter autant de conditions que nous le souhaitons à nos conditions de jointure.

Par exemple, si nous voulions trouver des films avec des réalisateurs qui ne sont **pas** nommés "John Smith", nous pourrions ajouter cette condition supplémentaire à notre jointure avec un `AND` :

```sql
SELECT *
FROM movies
INNER JOIN directors
  ON directors.id = movies.director_id
  AND directors.name <> 'John Smith';
```

Nous pouvons utiliser n'importe quel opérateur que nous mettrions dans une clause `WHERE` dans cette condition de jointure.

Nous obtenons également le même résultat à partir de cette requête si nous mettons la condition dans une clause `WHERE` à la place :

```sql
SELECT *
FROM movies
INNER JOIN directors
  ON directors.id = movies.director_id
WHERE directors.name <> 'John Smith';
```

Il y a quelques différences subtiles qui se produisent sous le capot ici, mais pour les besoins de cet article, l'ensemble de résultats est le même.

(Si vous n'êtes pas familier avec toutes les façons dont vous pouvez filtrer une requête SQL, consultez l'[article mentionné précédemment ici](https://www.freecodecamp.org/news/sql-operators-tutorial/).)

## La réalité sur l'écriture de requêtes avec des jointures

En réalité, je me retrouve à n'utiliser des jointures que de trois manières différentes :

#### `INNER JOIN`

Le premier cas d'utilisation concerne les enregistrements où la relation entre deux tables **existe**. Cela est satisfait par le `INNER JOIN`.

Ce sont des situations comme trouver "_des films qui ont des réalisateurs_" ou "_des utilisateurs avec des publications_".

#### `LEFT JOIN`

Le deuxième cas d'utilisation concerne les enregistrements d'une table, et si la relation existe, les enregistrements d'une deuxième table. Cela est satisfait par le `LEFT JOIN`.

Ce sont des situations comme "_des films avec des réalisateurs s'ils en ont un_" ou "_des utilisateurs avec des publications s'ils en ont_".

#### `LEFT JOIN` exclusion

Le troisième cas d'utilisation le plus courant est notre deuxième cas d'utilisation pour un `LEFT JOIN` : trouver des enregistrements dans une table qui **n'ont pas** de relation dans la deuxième table.

Ce sont des situations comme "_des films sans réalisateurs_" ou "_des utilisateurs sans publications_".

### Deux types de jointures très utiles

Je ne pense pas avoir jamais utilisé un `FULL OUTER JOIN` ou un `RIGHT JOIN` dans une application de production. Le cas d'utilisation ne se présente tout simplement pas assez souvent ou la requête peut être écrite de manière plus claire (dans le cas du `RIGHT JOIN`).

J'ai occasionnellement utilisé un `CROSS JOIN` pour des choses comme la répartition des enregistrements sur une plage de dates (comme nous l'avons vu au début), mais ce scénario ne se présente pas non plus trop souvent.

Donc, bonne nouvelle ! Il n'y a vraiment que deux types de jointures que vous devez comprendre pour 99,9 % des cas d'utilisation que vous rencontrerez : `INNER JOIN` et `LEFT JOIN` !

Si vous avez aimé cet article, vous pouvez [me suivre sur twitter](https://twitter.com/johnmosesman) où je parle de bases de données et de tous les autres sujets liés au développement.

Merci d'avoir lu !

John

**P.S.** un conseil supplémentaire pour avoir lu jusqu'à la fin : la plupart des systèmes de bases de données vous permettront d'écrire simplement `JOIN` à la place de `INNER JOIN`, cela vous fera économiser un peu de frappe. :)