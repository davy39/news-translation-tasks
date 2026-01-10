---
title: Tutoriel sur les opérateurs SQL – Exemples de requêtes avec opérateurs binaires,
  de comparaison, arithmétiques et logiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-18T15:18:03.000Z'
originalURL: https://freecodecamp.org/news/sql-operators-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9931740569d1a4ca1e5b.jpg
tags:
- name: data
  slug: data
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Tutoriel sur les opérateurs SQL – Exemples de requêtes avec opérateurs
  binaires, de comparaison, arithmétiques et logiques
seo_desc: 'By John Mosesman

  At its core, the internet and all its applications are just data.

  Every email, tweet, selfie, bank transaction, and more is just data sitting in a
  database somewhere.

  For that data to be useful, we have to be able to retrieve it. How...'
---

Par John Mosesman

Au cœur d'Internet et de toutes ses applications, il n'y a que des données.

Chaque email, tweet, selfie, transaction bancaire, etc., n'est qu'une donnée stockée quelque part dans une base de données.

Pour que ces données soient utiles, nous devons pouvoir les récupérer. Cependant, simplement récupérer les données ne suffit pas – les données doivent _également_ être utiles et pertinentes pour notre situation.

Au niveau de la base de données, nous demandons des informations spécifiques à la base de données en écrivant une **[requête SQL](https://en.wikipedia.org/wiki/SQL)**. Cette requête SQL spécifie les données que nous voulons recevoir _et_ le format dans lequel nous voulons les recevoir.

Dans cet article, nous examinerons toutes les méthodes les plus courantes pour filtrer une requête SQL.

Voici ce que nous allons couvrir :

* [Installation de votre base de données](#heading-installation)
* [Création d'utilisateurs](#heading-creation-dutilisateurs)
* [Insertion d'utilisateurs](#heading-insertion-dutilisateurs)
* [Filtrage des données avec `WHERE`](#heading-filtrage-des-donnees-avec-where)
* [Opérateurs logiques (`AND` / `OR` / `NOT`)](#heading-operateurs-logiques-and-or-not)
* [Opérateurs de comparaison (`<`, `>`, `<=`, `>=`)](#heading-operateurs-de-comparaison-lt-gt-lte-gte)
* [Opérateurs arithmétiques (`+`, `-`, `*`, `/`, `%`)](#heading-operateurs-arithmetiques)
* [Opérateurs d'existence (`IN` / `NOT IN`)](#heading-operateurs-dexistence-in-not-in)
* [Correspondance partielle avec `LIKE`](#heading-correspondance-partielle-avec-like)
* [Gestion des données manquantes (`NULL`)](#heading-gestion-des-donnees-manquantes-null)
* [Utilisation de `IS NULL` et `IS NOT NULL`](#heading-utilisation-de-is-null-et-is-not-null)
* [Opérateurs de comparaison avec dates et heures](#heading-operateurs-de-comparaison-avec-dates-et-heures)
* [Existence avec `EXISTS` / `NOT EXISTS`](#heading-existence-avec-exists-not-exists)
* [Opérateurs binaires](#heading-operateurs-binaires)
* [Conclusion](#heading-conclusion)

## Installation de votre base de données

Pour filtrer nos données, nous devons d'abord en avoir.

Pour ces exemples, nous utiliserons PostgreSQL, mais les requêtes et concepts présentés ici s'appliqueront facilement à tout autre système de base de données moderne (comme MySQL, SQL Server, etc.).

Pour travailler avec notre base de données PostgreSQL, nous pouvons utiliser [`psql`](https://www.postgresql.org/docs/current/app-psql.html) – le programme interactif en ligne de commande de PostgreSQL. Si vous avez un autre client de base de données que vous préférez utiliser, c'est très bien aussi !

Pour commencer, créons notre base de données. Avec PostgreSQL déjà [installé](https://www.postgresql.org/download/), nous pouvons exécuter la commande `psql` `createdb <nom-de-la-base-de-données>` dans notre terminal pour créer une nouvelle base de données. J'ai appelé la mienne `fcc` :

```bash
$ createdb fcc

```

Ensuite, démarrons la console interactive en utilisant la commande `psql` et connectons-nous à la base de données que nous venons de créer en utilisant `\c <nom-de-la-base-de-données>` :

```bash
$ psql
psql (11.5)
Tapez "help" pour obtenir de l'aide.

john=# \c fcc
Vous êtes maintenant connecté à la base de données "fcc" en tant qu'utilisateur "john".
fcc=#

```

## Création d'utilisateurs

Maintenant que nous avons une base de données, créons une table de base de données pour modéliser un utilisateur potentiel dans notre système fictif.

Nous appellerons cette table `users`, et chaque ligne de cette table représentera l'un de nos utilisateurs.

Cette table `users` aura des colonnes que nous nous attendons à trouver pour décrire un utilisateur – des choses comme un nom, un email et un âge.

Dans notre session `psql`, créons la table `users` :

```sql
CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT NOT NULL,
  age INTEGER NOT NULL
);
```

La sortie montre `CREATE TABLE` ce qui signifie que la création de notre table a réussi.

> **Note :** J'ai nettoyé la sortie `psql` dans ces exemples pour faciliter la lecture, donc ne vous inquiétez pas si la sortie montrée ici n'est pas exactement ce que vous avez vu dans votre terminal.

Regardons le contenu de notre table users :

```sql
SELECT * FROM users;

 id | first_name | last_name | email | age
----+------------+-----------+-------+-----
(0 lignes)

```

Nous n'avons inséré aucune donnée dans notre table, donc nous voyons simplement la structure de la table vide.

Si vous n'êtes pas familier avec les requêtes SQL, celle que nous venons d'exécuter, `SELECT * FROM users`, est l'une des plus simples que vous puissiez écrire.

Le mot-clé `SELECT` spécifie quelle(s) colonne(s) vous souhaitez retourner (`*` signifie "toutes les colonnes"), et le mot-clé `FROM` spécifie quelle table vous souhaitez sélectionner (dans ce cas `users`).

Ainsi, `SELECT * FROM users` signifie vraiment _retourner toutes les lignes et toutes les colonnes de la table `users`._

Si nous voulions retourner des colonnes spécifiques de la table `users`, nous pourrions remplacer `SELECT *` par les colonnes que nous voulons retourner – par exemple `SELECT id, name FROM users`.

## Insertion d'utilisateurs

Une table vide n'est pas très intéressante, alors insérons quelques données dans notre table afin de pouvoir pratiquer des requêtes dessus :

```sql
INSERT INTO users(first_name, last_name, email, age) VALUES
('John', 'Smith', 'johnsmith@gmail.com', 25),
('Jane', 'Doe', 'janedoe@Gmail.com', 28),
('Xavier', 'Wills', 'xavier@wills.io', 35),
('Bev', 'Scott', 'bev@bevscott.com', 16),
('Bree', 'Jensen', 'bjensen@corp.net', 42),
('John', 'Jacobs', 'jjacobs@corp.net', 56),
('Rick', 'Fuller', 'fullman@hotmail.com', 16);
```

Si nous exécutons cette instruction d'insertion dans notre session `psql`, nous voyons la sortie `INSERT 0 7`. Cela signifie que nous avons réussi à insérer 7 nouvelles lignes dans notre table.

Si nous exécutons à nouveau notre requête `SELECT * FROM users`, nous verrons maintenant ces données :

```sql
SELECT * FROM users;

id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Jacobs    | jjacobs@corp.net    |  56
  2 | Rick       | Fuller    | fullman@hotmail.com |  16
  3 | Bree       | Jensen    | bjensen@corp.net    |  42
  4 | Bev        | Scott     | bev@bevscott.com    |  16
  5 | Xavier     | Wills     | xavier@wills.io     |  35
  6 | Jane       | Doe       | janedoe@Gmail.com   |  28
  7 | John       | Smith     | johnsmith@gmail.com |  25
(7 lignes)

```

## Filtrage des données avec `WHERE`

Jusqu'à présent, nous avons simplement retourné toutes les lignes de notre table. C'est le comportement par défaut de la requête. Pour retourner un ensemble plus sélectif de lignes, nous devons **filtrer les lignes en utilisant une clause `WHERE`.**

Il existe de nombreuses façons de filtrer nos lignes en utilisant une clause `WHERE`. L'opérateur le plus simple que nous pouvons utiliser est l'opérateur d'égalité : `=`.

Supposons que nous voulions trouver les utilisateurs dont le prénom est "John" :

```sql
SELECT *
FROM users
WHERE first_name = 'John';

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Jacobs    | jjacobs@corp.net    |  56
  7 | John       | Smith     | johnsmith@gmail.com |  25
(2 lignes)

```

Ici, nous avons ajouté le mot-clé `WHERE` à notre requête suivi d'une instruction d'égalité : `first_name = 'John'`.

Notre base de données regarde d'abord le mot-clé `FROM` pour déterminer quelles données récupérer. Ainsi, la base de données lira cette requête, verra `FROM users`, et ira chercher toutes les lignes de la table `users` sur le disque.

Une fois que toutes les lignes ont été récupérées de la table `users`, elle exécute la clause `WHERE` contre chaque ligne et ne retourne que les lignes où la valeur de la colonne `first_name` est égale à "John".

Dans nos données, il y a deux lignes qui correspondent à ce prénom.

Si nous voulions trouver un "John" particulier dans notre système, nous pourrions interroger en fonction d'une colonne que nous savons être unique – comme notre colonne `id`.

Pour trouver spécifiquement la ligne "John Jacobs", nous pourrions interroger par son ID :

```sql
SELECT *
FROM users
WHERE id = 1;

 id | first_name | last_name |      email       | age
----+------------+-----------+------------------+-----
  1 | John       | Jacobs    | jjacobs@corp.net |  56
(1 ligne)

```

Ici, un seul enregistrement correspondait à la condition `id = 1`, donc nous n'avons obtenu qu'une seule ligne.

### Opérateurs logiques (`AND` / `OR` / `NOT`)

Nous pouvons filtrer par plus que l'opérateur d'égalité. Nous pouvons également utiliser les opérateurs logiques booléens que l'on trouve dans la plupart des langages de programmation : _et, ou,_ et _non_.

Dans de nombreux langages de programmation, _et_ et _ou_ sont représentés par `&&` et `||`. En SQL, ils sont simplement `AND` et `OR`.

Au lieu d'interroger par ID, essayons de trouver l'enregistrement de la personne nommée "John Smith". Pour ce faire, nous pouvons utiliser un `AND` dans notre clause `WHERE` pour rechercher à la fois la condition du prénom et du nom de famille :

```sql
SELECT *
FROM users
WHERE first_name = 'John'
  AND last_name = 'Smith';
  
 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  7 | John       | Smith     | johnsmith@gmail.com |  25
(1 ligne)

```

Pour trouver les personnes avec un prénom "John" _ou_ un nom de famille "Doe" :

```sql
SELECT *
FROM users
WHERE first_name = 'John'
  OR last_name = 'Doe';

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Jacobs    | jjacobs@corp.net    |  56
  6 | Jane       | Doe       | janedoe@Gmail.com   |  28
  7 | John       | Smith     | johnsmith@gmail.com |  25
(3 lignes)

```

Ici, notre résultat contenait à la fois les _Johns_ ainsi que Jane _Doe_.

Ces conditions `AND` et `OR` peuvent également être enchaînées. Supposons que nous voulions trouver quelqu'un nommé exactement "John Smith", _ou_ quelqu'un avec un nom de famille "Doe" :

```sql
SELECT *
FROM users
WHERE
(
  first_name = 'John'
  AND last_name = 'Smith'
)
OR last_name = 'Doe';

 id | first_name  | last_name |        email        | age
----+------------+-----------+---------------------+-----
  6 | Jane       | Doe       | janedoe@Gmail.com   |  28
  7 | John       | Smith     | johnsmith@gmail.com |  25
(2 lignes)

```

Si nous voulions inverser cette condition et trouver les utilisateurs qui ne s'appellent pas "John Smith" et qui n'ont pas non plus un nom de famille "Doe", nous pourrions ajouter l'opérateur `NOT` :

```sql
SELECT *
FROM users
WHERE NOT
(
  (
    first_name = 'John'
    AND last_name = 'Smith'
  )
  OR last_name = 'Doe'
);
 
 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  4 | Bev        | Scott     | bev@bevscott.com    |  16
  5 | Bree       | Jensen    | bjensen@corp.net    |  42
  6 | John       | Jacobs    | jjacobs@corp.net    |  56
  7 | Rick       | Fuller    | fullman@hotmail.com |  16
  3 | Xavier     | Wills     | xavier@wills.io     |  35
(5 lignes)
```

> **Note :** chacun a son propre style personnel de la façon dont il aime formater les requêtes – faites ce qui a du sens pour vous !

### Opérateurs de comparaison (`<`, `>`, `<=`, `>=`)

Similaire à d'autres langages de programmation, SQL possède également les opérateurs de comparaison : `<`, `>`, `<=`, `>=`.

Pratiquons l'utilisation de ces opérateurs contre la colonne `age` de nos utilisateurs.

Supposons que nous voulions trouver les utilisateurs qui ont _dix-huit ans ou plus_ :

```sql
SELECT * FROM users WHERE age >= 18;

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Jacobs    | jjacobs@corp.net    |  56
  3 | Bree       | Jensen    | bjensen@corp.net    |  42
  5 | Xavier     | Wills     | xavier@wills.io     |  35
  6 | Jane       | Doe       | janedoe@Gmail.com   |  28
  7 | John       | Smith     | johnsmith@gmail.com |  25
(5 lignes)

```

Et les utilisateurs qui ont plus de 25 ans, mais moins de ou égal à 35 ans ?

```sql
SELECT * FROM users WHERE age > 25 AND age <= 35;

 id | first_name | last_name |       email       | age
----+------------+-----------+-------------------+-----
  5 | Xavier     | Wills     | xavier@wills.io   |  35
  6 | Jane       | Doe       | janedoe@Gmail.com |  28
(2 lignes)

```

### Opérateurs arithmétiques (`+`, `-`, `*`, `/`, `%`)

Nous pouvons également effectuer des calculs mathématiques sur nos données.

Notre table `users` a une colonne `age`, que se passe-t-il si nous voulions trouver _la moitié_ de l'âge de chaque personne ?

```sql
SELECT
  *,
  age / 2 AS half_of_their_age
FROM users;

 id | first_name | last_name |        email        | age | half_of_their_age
----+------------+-----------+---------------------+-----+-------------------
  1 | John       | Jacobs    | jjacobs@corp.net    |  56 |                28
  2 | Rick       | Fuller    | fullman@hotmail.com |  16 |                 8
  3 | Bree       | Jensen    | bjensen@corp.net    |  42 |                21
  4 | Bev        | Scott     | bev@bevscott.com    |  16 |                 8
  5 | Xavier     | Wills     | xavier@wills.io     |  35 |                17
  6 | Jane       | Doe       | janedoe@Gmail.com   |  28 |                14
  7 | John       | Smith     | johnsmith@gmail.com |  25 |                12
(7 lignes)

```

Ici, nous sélectionnons toutes les colonnes de la table (en utilisant `SELECT *`), et nous sélectionnons également un nouveau calcul d'agrégation : `age / 2`. Nous donnons également à cette valeur un nom descriptif (`half_of_their_age`) avec un alias en utilisant le mot-clé `AS`.

Nous pouvons également trouver qui a un âge qui est un _nombre pair_ en utilisant l'opérateur modulo ou reste (`%`) :

```sql
SELECT * FROM users WHERE (age % 2) = 0;

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Jacobs    | jjacobs@corp.net    |  56
  2 | Rick       | Fuller    | fullman@hotmail.com |  16
  3 | Bree       | Jensen    | bjensen@corp.net    |  42
  4 | Bev        | Scott     | bev@bevscott.com    |  16
  6 | Jane       | Doe       | janedoe@Gmail.com   |  28
(5 lignes)

```

Nous pouvons trouver qui a un âge qui est un _nombre impair_ en changeant notre condition `=` en "différent de" en utilisant `!=` ou `<>` :

```sql
SELECT * FROM users WHERE (age % 2) <> 0;

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  5 | Xavier     | Wills     | xavier@wills.io     |  35
  7 | John       | Smith     | johnsmith@gmail.com |  25
(2 lignes)

```

### Opérateurs d'existence (`IN` / `NOT IN`)

Si nous voulions vérifier qu'une valeur de colonne existe dans une liste de valeurs, nous pouvons utiliser `IN` ou `NOT IN` :

```sql
SELECT *
FROM users
WHERE first_name IN ('John', 'Jane', 'Rick');

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Smith     | johnsmith@gmail.com |  25
  2 | Jane       | Doe       | janedoe@Gmail.com   |  28
  6 | John       | Jacobs    | jjacobs@corp.net    |  56
  7 | Rick       | Fuller    | fullman@hotmail.com |  16
(4 lignes)

```

De même, nous pouvons utiliser `NOT IN` pour nier cette condition :

```sql
SELECT *
FROM users
WHERE first_name NOT IN ('John', 'Jane', 'Rick');

 id | first_name | last_name |      email       | age
----+------------+-----------+------------------+-----
  3 | Xavier     | Wills     | xavier@wills.io  |  35
  4 | Bev        | Scott     | bev@bevscott.com |  16
  5 | Bree       | Jensen    | bjensen@corp.net |  42
(3 lignes)

```

### Correspondance partielle avec `LIKE`

Parfois, nous pouvons vouloir rechercher des lignes en fonction d'une recherche partielle.

Supposons, par exemple, que nous voulions trouver tous les utilisateurs qui se sont inscrits à notre application en utilisant une adresse Gmail. Nous pouvons faire une correspondance partielle contre une colonne en utilisant le mot-clé `LIKE`. Nous pouvons également spécifier un caractère générique (ou "correspond à tout") dans la chaîne de correspondance en utilisant `%`.

Pour trouver les utilisateurs avec un email qui se termine par `gmail.com` :

```sql
SELECT *
FROM users
WHERE email LIKE '%gmail.com';

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Smith     | johnsmith@gmail.com |  25
(1 ligne)

```

La chaîne `%gmail.com` signifie "correspond à tout ce qui se termine par `gmail.com`".

Si nous regardons nos données d'utilisateurs, nous remarquerons que nous avons en fait deux utilisateurs avec une adresse `gmail.com` :

```
('John', 'Smith', 'johnsmith@gmail.com', 25),
('Jane', 'Doe', 'janedoe@Gmail.com', 28),

```

Cependant, l'email de Jane a un "G" majuscule dans son adresse email. Notre requête précédente n'a pas capté cet enregistrement car elle correspondait _exactement_ à `gmail.com` avec un "g" minuscule.

Pour faire une correspondance insensible à la casse, nous devons simplement substituer `LIKE` par `ILIKE` :

```sql
SELECT *
FROM users
WHERE email ILIKE '%gmail.com';

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Smith     | johnsmith@gmail.com |  25
  2 | Jane       | Doe       | janedoe@Gmail.com   |  28
(2 lignes)

```

Le symbole générique `%` au début de la chaîne signifie que tout ce qui se termine par "gmail.com" sera retourné. Cela pourrait être `bob.jones+12345@gmail.com` ou `asdflkasdflkj@gmail.com` – tant que cela se termine par `gmail.com`.

Nous pouvons également ajouter autant de caractères génériques (`%`) que nous le souhaitons.

Par exemple, le terme de recherche `%j%o%` retournera tous les emails qui suivent le motif `<n'importe quoi>` suivi d'un `j`, suivi de `<n'importe quoi>`, suivi d'un `o`, suivi de `<n'importe quoi>` :

```sql
SELECT * FROM users WHERE email ILIKE '%j%o%';

 id | first_name | last_name |        email        | age
----+------------+-----------+---------------------+-----
  1 | John       | Smith     | johnsmith@gmail.com |  25
  2 | Jane       | Doe       | janedoe@Gmail.com   |  28
  5 | Bree       | Jensen    | bjensen@corp.net    |  42
  6 | John       | Jacobs    | jjacobs@corp.net    |  56
(4 lignes)

```

## Gestion des données manquantes (`NULL`)

Ensuite, regardons comment nous traitons les lignes avec des colonnes qui ont des données manquantes.

Pour cela, ajoutons une autre colonne à notre table `users` : `first_paid_at`.

Cette nouvelle colonne sera un `TIMESTAMP` (similaire à un `datetime` dans d'autres langages), et elle représentera la première date et heure à laquelle un utilisateur nous a payé de l'argent pour notre application. Peut-être voulons-nous leur envoyer une belle carte ou des fleurs à l'anniversaire de l'utilisation de notre application ?

Nous pourrions supprimer notre table `users` en utilisant `DROP TABLE users;` et la recréer, mais cela supprimerait également toutes les données de notre table.

Pour modifier une table sans la supprimer et perdre les données, nous pouvons utiliser `ALTER TABLE` :

```sql
ALTER TABLE users ADD COLUMN first_paid_at TIMESTAMP; 
```

Cette commande retourne le résultat `ALTER TABLE`, donc notre requête `ALTER` a réussi.

Si nous interrogeons notre table `users` maintenant, nous remarquerons que cette nouvelle colonne n'a aucune donnée :

```sql
SELECT * FROM users;

 id | first_name | last_name |        email        | age | first_paid_at
----+------------+-----------+---------------------+-----+---------------
  1 | John       | Smith     | johnsmith@gmail.com |  25 |
  2 | Jane       | Doe       | janedoe@Gmail.com   |  28 |
  3 | Xavier     | Wills     | xavier@wills.io     |  35 |
  4 | Bev        | Scott     | bev@bevscott.com    |  16 |
  5 | Bree       | Jensen    | bjensen@corp.net    |  42 |
  6 | John       | Jacobs    | jjacobs@corp.net    |  56 |
  7 | Rick       | Fuller    | fullman@hotmail.com |  16 |
(7 lignes)

```

Notre colonne `first_paid_at` est vide, et le résultat de notre requête `psql` la montre comme une colonne vide. Cette colonne n'est pas techniquement vide – elle contient une valeur spéciale que `psql` choisit de ne pas afficher dans sa sortie : `NULL`.

[`NULL`](https://en.wikipedia.org/wiki/Null_(SQL)) est une valeur spéciale dans les bases de données. C'est l'absence ou le manque de valeur, et il ne se comporte pas comme nous nous y attendrions.

Pour illustrer cela, regardons les simples instructions `SELECT` ci-dessous :

```sql
SELECT
  1 = 1,
  1 = 2;

 ?column? | ?column?
----------+----------
 t        | f
(1 ligne)

```

Ici, nous avons simplement sélectionné `1 = 1` et `1 = 2`. Comme nous nous y attendons, le résultat de ces deux instructions est `t` et `f` (ou `TRUE` et `FALSE`). `1` est égal à `1`, et `1` n'est pas égal à `2`.

Maintenant, essayons la même chose avec `NULL` :

```sql
SELECT 1 = NULL;

 ?column?
----------

(1 ligne)

```

Nous pourrions nous attendre à ce que cette valeur soit `FALSE`, mais la valeur de retour est en fait `NULL`.

Pour visualiser ces `NULL` un peu mieux, définissons comment `psql` affiche les valeurs `NULL` en utilisant l'option `\pset` :

```sql
fcc=# \pset null 'NULL'
Affichage de NULL est "NULL".

```

Maintenant, si nous exécutons à nouveau cette requête, nous verrons la sortie `NULL` que nous attendons :

```sql
SELECT 1 = NULL;

 ?column?
----------
 NULL
(1 ligne)

```

Donc `1` n'est pas égal à `NULL`, qu'en est-il de `NULL = NULL` ?

```sql
SELECT NULL = NULL;

 ?column?
----------
 NULL
(1 ligne)

```

Étrangement, `NULL` n'est pas égal à `NULL`.

Cela aide à penser à `NULL` comme une valeur inconnue. Une valeur inconnue est-elle égale à `1` ? Eh bien, nous ne savons pas – c'est inconnu. Une valeur inconnue est-elle égale à une valeur inconnue ? Encore une fois, c'est inconnu. De cette manière, `NULL` a un peu plus de sens.

### Utilisation de `IS NULL` et `IS NOT NULL`

Nous ne pouvons pas utiliser l'opérateur d'égalité avec `NULL`, mais nous pouvons utiliser deux opérateurs spécialement conçus pour cela : `IS NULL` et `IS NOT NULL`.

```sql
SELECT
  NULL IS NULL,
  NULL IS NOT NULL;

 ?column? | ?column?
----------+----------
 t        | f
(1 ligne)

```

Ces valeurs sont celles que nous attendons : `NULL IS NULL` est vrai, et `NULL IS NOT NULL` est faux.

C'est bien et étrange, mais comment utilisons-nous cela ?

Tout d'abord, obtenons quelques données dans notre colonne `first_paid_at` :

```sql
UPDATE users SET first_paid_at = NOW() WHERE id = 1;
UPDATE 1

UPDATE users SET first_paid_at = (NOW() - INTERVAL '1 month') WHERE id = 2;
UPDATE 1

UPDATE users SET first_paid_at = (NOW() - INTERVAL '1 year') WHERE id = 3;
UPDATE 1

```

Dans ces instructions `UPDATE` ci-dessus, nous avons défini trois colonnes `first_paid_at` pour différents utilisateurs : l'ID d'utilisateur 1 à l'heure actuelle (`NOW()`), l'ID d'utilisateur 2 à un mois en arrière, et l'ID d'utilisateur 3 à un an en arrière.

Tout d'abord, trouvons les utilisateurs qui nous ont payé et ceux qui ne l'ont pas fait :

```sql
SELECT *
FROM users
WHERE first_paid_at IS NULL;

 id | first_name | last_name |        email        | age | first_paid_at
----+------------+-----------+---------------------+-----+---------------
  4 | Bev        | Scott     | bev@bevscott.com    |  16 | NULL
  5 | Bree       | Jensen    | bjensen@corp.net    |  42 | NULL
  6 | John       | Jacobs    | jjacobs@corp.net    |  56 | NULL
  7 | Rick       | Fuller    | fullman@hotmail.com |  16 | NULL
(4 lignes)

SELECT *
FROM users
WHERE first_paid_at IS NOT NULL;

 id | first_name | last_name |        email        | age |       first_paid_at
----+------------+-----------+---------------------+-----+----------------------------
  1 | John       | Smith     | johnsmith@gmail.com |  25 | 2020-08-11 20:49:17.230517
  2 | Jane       | Doe       | janedoe@Gmail.com   |  28 | 2020-07-11 20:49:17.233124
  3 | Xavier     | Wills     | xavier@wills.io     |  35 | 2019-08-11 20:49:17.23488
(3 lignes)

```

### Opérateurs de comparaison avec dates et heures

Maintenant que nous avons quelques données, utilisons nos mêmes opérateurs de comparaison contre ce nouveau champ `TIMESTAMP`.

Essayons de trouver les utilisateurs qui nous ont payé pour la première fois au cours de la semaine passée. Pour ce faire, nous pouvons prendre l'heure actuelle, `NOW()`, et soustraire une semaine en utilisant le mot-clé `INTERVAL` :

```sql
SELECT *
FROM users
WHERE first_paid_at > (NOW() - INTERVAL '1 week');

 id | first_name | last_name |        email        | age |       first_paid_at
----+------------+-----------+---------------------+-----+----------------------------
  1 | John       | Smith     | johnsmith@gmail.com |  25 | 2020-08-11 20:49:17.230517
(1 ligne)

```

Nous pourrions également utiliser un autre intervalle, comme il y a trois mois :

```sql
SELECT *
FROM users
WHERE first_paid_at < (NOW() - INTERVAL '3 months');

 id | first_name | last_name |      email      | age |       first_paid_at
----+------------+-----------+-----------------+-----+---------------------------
  3 | Xavier     | Wills     | xavier@wills.io |  35 | 2019-08-11 20:49:17.23488
(1 ligne)

```

Essayons de trouver les utilisateurs qui nous ont payé pour la première fois entre un et six mois en arrière.

Nous pourrions combiner nos conditions à nouveau en utilisant `AND`, mais au lieu d'utiliser les opérateurs _inférieur à_ et _supérieur à_, utilisons le mot-clé `BETWEEN` :

```sql
SELECT *
FROM users
WHERE first_paid_at BETWEEN (NOW() - INTERVAL '6 month')
  AND (NOW() - INTERVAL '1 month');
  
 id | first_name | last_name |       email       | age |       first_paid_at
----+------------+-----------+-------------------+-----+----------------------------
  2 | Jane       | Doe       | janedoe@Gmail.com |  28 | 2020-07-11 20:49:17.233124
(1 ligne)

```

### Existence avec `EXISTS` / `NOT EXISTS`

Une autre façon de vérifier l'existence est d'utiliser `EXISTS` et `NOT EXISTS`.

Ces opérateurs filtrent les lignes en vérifiant l'existence (ou la non-existence) d'une condition. Cette condition est généralement une requête contre une autre table.

Pour configurer cela, créons une nouvelle table appelée `posts`. Cette table contiendra les posts qu'un utilisateur peut faire dans notre système.

```sql
CREATE TABLE posts(
  id SERIAL PRIMARY KEY,
  body TEXT NOT NULL,
  user_id INTEGER REFERENCES users NOT NULL
);

```

C'est une table simple. Elle ne contient qu'un ID, un champ pour stocker le texte du post (`body`), et une référence à l'utilisateur qui a écrit le post (`user_id`).

Insérons quelques données dans cette nouvelle table :

```sql
INSERT INTO posts(body, user_id) VALUES
('Here is post 1', 1),
('Here is post 2', 1),
('Here is post 3', 2),
('Here is post 4', 3);

```

Dans les données que nous avons insérées dans la table `posts`, l'ID d'utilisateur 1 a deux posts, l'ID d'utilisateur 2 a un post, et l'ID d'utilisateur 3 a également un post.

Pour trouver les utilisateurs qui ont des posts, nous pouvons utiliser `EXISTS`.

Le mot-clé `EXISTS` prend une sous-requête. Si _quelque chose_ est retourné de cette sous-requête (même une ligne avec juste la valeur `NULL`), la base de données inclura cette ligne dans le jeu de résultats.

[D'après la documentation PostgreSQL](https://www.postgresql.org/docs/current/functions-subquery.html#FUNCTIONS-SUBQUERY-EXISTS) sur `EXISTS` :

> L'argument de EXISTS est une instruction SELECT arbitraire, ou sous-requête. La sous-requête est évaluée pour déterminer si elle retourne des lignes. Si elle retourne au moins une ligne, le résultat de EXISTS est "vrai" ; si la sous-requête ne retourne aucune ligne, le résultat de EXISTS est "faux".

`EXISTS` recherche simplement l'_existence_ d'une ligne de la sous-requête – peu importe ce qu'elle contient.

Voici un exemple d'utilisateurs qui ont des posts en utilisant `EXISTS` :

```sql
SELECT *
FROM users
WHERE EXISTS (
  SELECT 1
  FROM posts
  WHERE posts.user_id = users.id
);

 id | first_name | last_name |        email        | age |       first_paid_at
----+------------+-----------+---------------------+-----+----------------------------
  1 | John       | Smith     | johnsmith@gmail.com |  25 | 2020-08-11 20:49:17.230517
  2 | Jane       | Doe       | janedoe@Gmail.com   |  28 | 2020-07-11 20:49:17.233124
  3 | Xavier     | Wills     | xavier@wills.io     |  35 | 2019-08-11 20:49:17.23488
(3 lignes)

```

Comme nous nous y attendions, nous avons obtenu les utilisateurs 1, 2 et 3.

Notre sous-requête `EXISTS` vérifie un enregistrement `posts` où l'`user_id` du post correspond à la colonne `id` de la table `users`. Nous avons retourné `1` dans notre `SELECT` parce que nous pouvons retourner n'importe quoi ici – la base de données veut simplement voir que quelque chose a été retourné.

De même, nous pourrions trouver les utilisateurs qui n'ont aucun post en changeant `EXISTS` en `NOT EXISTS` :

```sql
SELECT *
FROM users
WHERE NOT EXISTS (
  SELECT 1
  FROM posts
  WHERE posts.user_id = users.id
);

 id | first_name | last_name |        email        | age | first_paid_at
----+------------+-----------+---------------------+-----+---------------
  4 | Bev        | Scott     | bev@bevscott.com    |  16 | NULL
  5 | Bree       | Jensen    | bjensen@corp.net    |  42 | NULL
  6 | John       | Jacobs    | jjacobs@corp.net    |  56 | NULL
  7 | Rick       | Fuller    | fullman@hotmail.com |  16 | NULL
(4 lignes)

```

Enfin, nous pourrions également réécrire cette requête pour utiliser `IN` ou `NOT IN` au lieu de `EXISTS` ou `NOT EXISTS`, comme ceci :

```sql
SELECT *
FROM users
WHERE users.id IN (
  SELECT user_id
  FROM posts
);

```

Cela fonctionne techniquement, mais en règle générale, si vous testez l'_existence_ d'un autre enregistrement, il est _généralement_ plus performant d'utiliser `EXISTS`. Les opérateurs `IN` et `NOT IN` sont généralement mieux utilisés pour vérifier une valeur contre une liste statique comme nous l'avons fait précédemment :

```sql
SELECT *
FROM users
WHERE first_name IN ('John', 'Jane', 'Rick');

```

### Opérateurs binaires

Bien que dans la pratique les opérateurs binaires ne soient pas souvent utilisés, pour être complet, regardons un exemple simple.

Si nous voulions (pour une raison quelconque) regarder l'âge de nos utilisateurs en binaire et jouer à inverser ces bits, nous pourrions utiliser une variété d'opérateurs binaires.

Par exemple, regardons l'opérateur binaire "et" : `&`.

```sql
SELECT age::bit(8) & '11111111' FROM users;

 ?column?
----------
 00010000
 00101010
 00111000
 00010000
 00011001
 00011100
 00100011
(7 lignes)
```

Pour effectuer un calcul binaire, nous devons d'abord convertir notre colonne `age` d'un entier en binaire – dans cet exemple, nous la convertissons en une chaîne binaire de huit bits en utilisant `::bit(8)`.

Ensuite, nous pouvons "et" le résultat de notre âge en format binaire avec une autre chaîne binaire, `11111111`. Puisqu'un `ET` binaire ne retourne 1 que si les deux bits sont des 1, cette chaîne de tous les 1 garde la sortie intéressante.

Presque tous les autres opérateurs binaires utilisent le même format :

```sql
SELECT age::bit(8) | '11111111' FROM users;    -- OU binaire
SELECT age::bit(8) # '11111111' FROM users;    -- XOR binaire
SELECT age::bit(8) << '00000001' FROM users;   -- décalage binaire à gauche
SELECT age::bit(8) >> '00000001' FROM users;   -- décalage binaire à droite
```

L'opérateur binaire "non" (`~`) est un peu différent en ce sens qu'il est appliqué à un seul terme – similaire à l'opérateur régulier `NOT` :

```sql
SELECT ~age::bit(8) FROM users;

 ?column?
----------
 11101111
 11010101
 11000111
 11101111
 11100110
 11100011
 11011100
(7 lignes)
```

Et enfin, le plus utile des opérateurs binaires : la concaténation.

Une utilisation courante de cet opérateur est de combiner des chaînes de texte ensemble. Par exemple, si nous voulions construire une propriété calculée d'un "nom complet" pour les utilisateurs, nous pourrions utiliser la concaténation :

```sql
SELECT first_name || ' ' || last_name AS name
FROM users;

     name
--------------
 Bev Scott
 Bree Jensen
 John Jacobs
 Rick Fuller
 John Smith
 Jane Doe
 Xavier Wills
(7 lignes)
```

Ici, nous concaténons (ou "combinons") le `first_name`, un espace (`' '`), et la propriété `last_name` pour construire une valeur `name`.

## Conclusion

Voilà un aperçu de pratiquement tous les opérateurs de filtrage de requêtes que vous aurez jamais besoin d'utiliser !

Il existe quelques autres opérateurs que nous n'avons pas couverts ici, mais ces opérateurs sont soit rarement utilisés, soit utilisés exactement de la même manière que ci-dessus – donc ils ne devraient pas vous poser de problème.

Si vous avez aimé cet article, j'écris des choses similaires [sur mon blog ici.](https://johnmosesman.com/)

Merci d'avoir lu !

John