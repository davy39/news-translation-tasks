---
title: 'Tutoriel SQL Group By : Count, Sum, Average et les clauses Having expliquées'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-08T18:39:37.000Z'
originalURL: https://freecodecamp.org/news/sql-group-by-clauses-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98d4740569d1a4ca1c42.jpg
tags:
- name: Productivity
  slug: productivity
- name: SQL
  slug: sql
seo_title: 'Tutoriel SQL Group By : Count, Sum, Average et les clauses Having expliquées'
seo_desc: 'By John Mosesman

  The GROUP BY clause is a powerful but sometimes tricky statement to think about.

  Even eight years later, every time I use a GROUP BY I have to stop and think about
  what it''s actually doing.

  In this article we''ll look at how to constr...'
---

Par John Mosesman

La clause `GROUP BY` est une instruction puissante mais parfois délicate à comprendre.

Même huit ans plus tard, chaque fois que j'utilise un `GROUP BY`, je dois m'arrêter et réfléchir à ce qu'il fait réellement.

Dans cet article, nous allons examiner comment construire une clause `GROUP BY`, ce qu'elle fait à votre requête, et comment vous pouvez l'utiliser pour effectuer des agrégations et collecter des informations sur vos données.

Voici ce que nous allons couvrir :

* [Installation de votre base de données](#heading-installation)
* [Configuration des données d'exemple (création des ventes)](#heading-configuration-des-donnees-creation-des-ventes)
* [Comment fonctionne un `GROUP BY` ?](#heading-comment-fonctionne-un-group-by)
* [Écriture des clauses `GROUP BY`](#heading-ecriture-des-clauses-group-by)
* [Agrégations (`COUNT`, `SUM`, `AVG`)](#heading-aggregations-count-sum-avg)
* [Travail avec plusieurs groupes](#heading-travail-avec-plusieurs-groupes)
* [Utilisation de fonctions dans le `GROUP BY`](#heading-utilisation-de-fonctions-dans-le-group-by)
* [Filtrage des groupes avec `HAVING`](#heading-filtrage-des-groupes-avec-having)
* [Agrégats avec regroupement implicite](#heading-aggregats-avec-regroupement-implicite)

## Installation de votre base de données

Avant de pouvoir écrire nos requêtes, nous devons configurer notre base de données.

Pour ces exemples, nous utiliserons PostgreSQL, mais les requêtes et les concepts présentés ici s'appliqueront facilement à tout autre système de base de données moderne (comme MySQL, SQL Server, etc.).

Pour travailler avec notre base de données PostgreSQL, nous pouvons utiliser [psql](https://www.postgresql.org/docs/current/app-psql.html), le programme interactif en ligne de commande de PostgreSQL. Si vous avez un autre client de base de données que vous préférez utiliser, c'est très bien aussi.

Pour commencer, créons notre base de données. Avec [PostgreSQL](https://www.postgresql.org/download/) déjà installé, nous pouvons exécuter la commande `createdb <nom-de-la-base-de-données>` dans notre terminal pour créer une nouvelle base de données. J'ai appelé la mienne `fcc` :

```
$ createdb fcc

```

Ensuite, démarrons la console interactive en utilisant la commande `psql`, et connectons-nous à la base de données que nous venons de créer en utilisant `\c <nom-de-la-base-de-données>` :

```
$ psql
psql (11.5)
Tapez "help" pour obtenir de l'aide.

john=# \c fcc
Vous êtes maintenant connecté à la base de données "fcc" en tant qu'utilisateur "john".
fcc=#

```

> **Note :** J'ai nettoyé la sortie de `psql` dans ces exemples pour la rendre plus facile à lire, donc ne vous inquiétez pas si la sortie montrée ici n'est pas exactement ce que vous avez vu dans votre terminal.

Je vous encourage à suivre ces exemples et à exécuter ces requêtes vous-même. Vous apprendrez et retiendrez beaucoup plus en travaillant à travers ces exemples plutôt qu'en les lisant simplement.

## Configuration des données (création des ventes)

Pour nos exemples, nous utiliserons une table qui stocke les enregistrements de ventes de divers produits dans différents magasins.

Nous appellerons cette table `sales`, et elle sera une représentation simple des ventes en magasin : le nom du magasin, le nom du produit, le prix et l'heure de la vente.

Si nous construisions cette table dans une application réelle, nous établirions des clés étrangères vers d'autres tables (comme `locations` ou `products`). Mais pour illustrer les concepts de `GROUP BY`, nous utiliserons simplement des colonnes de type `TEXT`.

Créons la table et insérons quelques données de ventes :

```sql
CREATE TABLE sales(
  location TEXT,
  product TEXT,
  price DECIMAL,
  sold_at TIMESTAMP
);

INSERT INTO sales(location, product, price, sold_at) VALUES
('HQ', 'Coffee', 2, NOW()),
('HQ', 'Coffee', 2, NOW() - INTERVAL '1 hour'),
('Downtown', 'Bagel', 3, NOW() - INTERVAL '2 hour'),
('Downtown', 'Coffee', 2, NOW() - INTERVAL '1 day'),
('HQ', 'Bagel', 2, NOW() - INTERVAL '2 day'),
('1st Street', 'Bagel', 3, NOW() - INTERVAL '2 day' - INTERVAL '1 hour'),
('1st Street', 'Coffee', 2, NOW() - INTERVAL '3 day'),
('HQ', 'Bagel', 3, NOW() - INTERVAL '3 day' - INTERVAL '1 hour');

```

Nous avons trois magasins : _HQ_, _Downtown_ et _1st Street_.

Nous avons deux produits, _Coffee_ et _Bagel_, et nous insérons ces ventes avec différentes valeurs `sold_at` pour représenter les articles vendus à différents jours et heures.

Il y a des ventes aujourd'hui, certaines hier, et d'autres d'avant-hier.

## Comment fonctionne un `GROUP BY` ?

Pour illustrer le fonctionnement de la clause `GROUP BY`, commençons par un exemple.

Imaginez que nous avons une pièce remplie de personnes nées dans différents pays.

Si nous voulions trouver la **taille moyenne** des personnes dans la pièce **par pays**, nous demanderions d'abord à ces personnes de se séparer en groupes en fonction de leur pays de naissance.

Une fois qu'elles sont séparées en groupes, nous pourrions alors calculer la taille moyenne au sein de chaque groupe.

C'est ainsi que fonctionne la clause `GROUP BY`. D'abord, nous définissons comment nous voulons regrouper les lignes ensemble, puis nous pouvons effectuer des calculs ou des agrégations sur les groupes.

### Plusieurs groupes

Nous pouvons regrouper les données en autant de groupes ou sous-groupes que nous le souhaitons.

Par exemple, après avoir demandé aux personnes de se séparer en groupes en fonction de leur pays de naissance, nous pourrions demander à chacun de ces groupes de pays de se séparer _encore_ en groupes _en fonction de la couleur de leurs yeux_.

En faisant cela, nous avons des groupes de personnes basés sur la combinaison de leur pays de naissance _et_ de la couleur de leurs yeux.

Maintenant, nous pourrions trouver la taille moyenne au sein de chacun de ces groupes plus petits, et nous aurions un résultat plus spécifique : la taille moyenne _par pays et par couleur des yeux_.

Les clauses `GROUP BY` sont souvent utilisées dans des situations où vous pouvez utiliser la phrase _**par** quelque chose_ ou _**pour chaque** quelque chose_ :

* Taille moyenne _par_ pays de naissance
* Nombre total de personnes _pour chaque_ combinaison de couleur des yeux et des cheveux
* Ventes totales _par_ produit

## Écriture des clauses `GROUP BY`

Une clause `GROUP BY` est très facile à écrire : nous utilisons simplement les mots-clés `GROUP BY` puis spécifions le(s) champ(s) par lequel nous voulons regrouper :

```sql
SELECT ...
FROM sales
GROUP BY location;
```

Cette requête simple regroupe nos données de `sales` par la colonne `location`.

Nous avons fait le regroupement, mais que mettons-nous dans notre `SELECT` ?

La chose évidente à sélectionner est notre `location` : nous regroupons par celle-ci, donc nous voulons au moins voir le nom des groupes que nous avons créés :

```sql
SELECT location
FROM sales
GROUP BY location;

```

Le résultat est nos trois magasins :

```
  location
------------
 1st Street
 HQ
 Downtown
(3 rows)

```

Si nous regardons nos données de table brutes (`SELECT * FROM sales;`), nous verrons que nous avons quatre lignes avec un magasin _HQ_, deux lignes avec un magasin _Downtown_, et deux lignes avec un magasin _1st Street_ :

```
 product |  location  | price |          sold_at
---------+------------+-------+----------------------------
 Coffee  | HQ         |     2 | 2020-09-01 09:42:33.085995
 Coffee  | HQ         |     2 | 2020-09-01 08:42:33.085995
 Bagel   | Downtown   |     3 | 2020-09-01 07:42:33.085995
 Coffee  | Downtown   |     2 | 2020-08-31 09:42:33.085995
 Bagel   | HQ         |     2 | 2020-08-30 09:42:33.085995
 Bagel   | 1st Street |     3 | 2020-08-30 08:42:33.085995
 Coffee  | 1st Street |     2 | 2020-08-29 09:42:33.085995
 Bagel   | HQ         |     3 | 2020-08-29 08:42:33.085995
(8 rows)

```

En regroupant sur la colonne `location`, notre base de données prend ces lignes d'entrée et identifie les magasins uniques parmi eux : ces magasins uniques servent de nos _"groupes"_.

Mais qu'en est-il des autres colonnes de notre table ?

Si nous essayons de sélectionner une colonne comme `product` que nous n'avons pas regroupée...

```sql
SELECT
  location,
  product
FROM sales
GROUP BY location;

```

... nous rencontrons cette erreur :

```
ERROR:  column "sales.product" must appear in the GROUP BY clause or be used in an aggregate function

```

Le problème ici est que nous avons pris _huit_ lignes et les avons compressées ou distillées en _trois_.

Nous ne pouvons pas simplement retourner le reste des colonnes comme d'habitude : nous avions huit lignes, et maintenant nous en avons trois.

Que faisons-nous avec les cinq lignes de données restantes ? Les données de laquelle des huit lignes doivent être affichées sur ces trois lignes de magasins distincts ?

Il n'y a pas de réponse claire et définitive ici.

Pour utiliser le reste de nos données de table, nous devons également distiller les données de ces colonnes restantes dans nos trois groupes de magasins.

Cela signifie que nous devons **agréger** ou effectuer un calcul pour produire une sorte d'information de résumé sur nos données restantes.

## Agrégations (`COUNT`, `SUM`, `AVG`)

Une fois que nous avons décidé comment regrouper nos données, nous pouvons ensuite effectuer des agrégations sur les colonnes restantes.

Cela inclut des choses comme le comptage du nombre de lignes par groupe, la somme d'une valeur particulière à travers le groupe, ou la moyenne des informations au sein du groupe.

Pour commencer, trouvons le nombre de ventes _par_ magasin.

Puisque chaque enregistrement dans notre table `sales` est une vente, le nombre de ventes par magasin serait **le nombre de lignes au sein de chaque groupe de magasin.**

Pour ce faire, nous utiliserons la fonction d'agrégation `COUNT()` pour compter le nombre de lignes au sein de chaque groupe :

```sql
SELECT
  location,
  COUNT(*) AS number_of_sales
FROM sales
GROUP BY location;

```

Nous utilisons `COUNT(*)` qui compte toutes les lignes d'entrée pour un groupe.

(`COUNT()` fonctionne également avec des expressions, mais il a un comportement légèrement différent.)

Voici comment la base de données exécute cette requête :

* `FROM sales` — Tout d'abord, récupérer tous les enregistrements de la table `sales`
* `GROUP BY location` — Ensuite, déterminer les groupes de `location` uniques
* `SELECT ...` — Enfin, sélectionner le nom du magasin et le compte du nombre de lignes dans ce groupe

Nous donnons également à ce compte de lignes un alias en utilisant `AS number_of_sales` pour rendre la sortie plus lisible. Cela ressemble à ceci :

```
  location  | number_of_sales
------------+-----------------
 1st Street |               2
 HQ         |               4
 Downtown   |               2
(3 rows)

```

Le magasin _1st Street_ a deux ventes, _HQ_ en a quatre, et _Downtown_ en a deux.

Ici, nous pouvons voir comment nous avons pris les données de colonnes restantes de nos huit lignes indépendantes et les avons distillées en informations de résumé utiles pour chaque magasin : le nombre de ventes.

### `SUM`

De manière similaire, au lieu de compter le nombre de lignes dans un groupe, nous pourrions sommer les informations au sein du groupe — comme le montant total d'argent gagné à partir de ces magasins.

Pour ce faire, nous utiliserons la fonction `SUM()` :

```sql
SELECT
  location,
  SUM(price) AS total_revenue
FROM sales
GROUP BY location;

```

Au lieu de compter le nombre de lignes dans chaque groupe, nous additionnons le montant en dollars de chaque vente, et cela nous montre le revenu total par magasin :

```
  location  | total_revenue
------------+---------------
 1st Street |             5
 HQ         |             9
 Downtown   |             5
(3 rows)

```

### Moyenne (`AVG`)

Trouver le prix de vente moyen par magasin signifie simplement remplacer la fonction `SUM()` par la fonction `AVG()` :

```sql
SELECT
  location,
  AVG(price) AS average_revenue_per_sale
FROM sales
GROUP BY location;

```

## Travail avec plusieurs groupes

Jusqu'à présent, nous avons travaillé avec un seul groupe : le magasin.

Que se passe-t-il si nous voulons subdiviser ce groupe encore plus ?

Similaire au scénario des _"pays de naissance et couleur des yeux"_ avec lequel nous avons commencé, que se passe-t-il si nous voulons trouver le nombre de ventes **par produit et par magasin** ?

Pour ce faire, tout ce que nous avons à faire est d'ajouter la deuxième condition de regroupement à notre instruction `GROUP BY` :

```sql
SELECT ...
FROM sales
GROUP BY location, product;
```

En ajoutant une deuxième colonne dans notre `GROUP BY`, nous subdivisons davantage nos groupes de magasins en groupes de magasins _par produit_.

Parce que nous regroupons également par la colonne `product`, nous pouvons maintenant la retourner dans notre `SELECT` !

(Je vais ajouter quelques clauses `ORDER BY` à ces requêtes pour rendre la sortie plus facile à lire.)

```sql
SELECT
  location,
  product
FROM sales
GROUP BY location, product
ORDER BY location, product;

```

En regardant le résultat de notre nouveau regroupement, nous pouvons voir nos combinaisons uniques de magasin/produit :

```
  location  | product
------------+---------
 1st Street | Bagel
 1st Street | Coffee
 Downtown   | Bagel
 Downtown   | Coffee
 HQ         | Bagel
 HQ         | Coffee
(6 rows)

```

Maintenant que nous avons nos groupes, que voulons-nous faire avec le reste de nos données de colonnes ?

Eh bien, nous pouvons trouver le nombre de ventes _par produit et par magasin_ en utilisant les mêmes fonctions d'agrégation que précédemment :

```sql
SELECT
  location,
  product,
  COUNT(*) AS number_of_sales
FROM sales
GROUP BY location, product
ORDER BY location, product;

```

```
  location  | product | number_of_sales
------------+---------+-----------------
 1st Street | Bagel   |               1
 1st Street | Coffee  |               1
 Downtown   | Bagel   |               1
 Downtown   | Coffee  |               1
 HQ         | Bagel   |               2
 HQ         | Coffee  |               2
(6 rows)

```

> En tant qu'_Exercice Pour Le Lecteur™_ : trouvez le revenu total (somme) de chaque produit par magasin.

## Utilisation de fonctions dans le `GROUP BY`

Ensuite, essayons de trouver le nombre total de ventes **par jour**.

Si nous suivons un schéma similaire à celui que nous avons utilisé avec nos magasins et regroupons par notre colonne `sold_at`...

```sql
SELECT
  sold_at,
  COUNT(*) AS sales_per_day
FROM sales
GROUP BY sold_at
ORDER BY sold_at;

```

... nous pourrions nous attendre à ce que chaque groupe soit chaque jour unique — mais au lieu de cela, nous voyons ceci :

```
          sold_at           | sales_per_day
----------------------------+---------------
 2020-08-29 08:42:33.085995 |             1
 2020-08-29 09:42:33.085995 |             1
 2020-08-30 08:42:33.085995 |             1
 2020-08-30 09:42:33.085995 |             1
 2020-08-31 09:42:33.085995 |             1
 2020-09-01 07:42:33.085995 |             1
 2020-09-01 08:42:33.085995 |             1
 2020-09-01 09:42:33.085995 |             1
(8 rows)

```

Il semble que nos données ne soient pas du tout regroupées — nous obtenons chaque ligne individuellement.

Mais, nos données _sont en fait regroupées !_ Le problème est que chaque ligne `sold_at` est une valeur unique — donc chaque ligne obtient son propre groupe !

Le `GROUP BY` fonctionne correctement, mais ce n'est pas la sortie que nous voulons.

Le coupable est l'information unique d'heure/minute/seconde de l'horodatage. 

Chacun de ces horodatages diffère par les heures, les minutes ou les secondes — donc ils sont chacun placés dans leur propre groupe.

Nous devons convertir chacune de ces valeurs de date et d'heure en une simple date :

* `2020-09-01 08:42:33.085995` => `2020-09-01`
* `2020-09-01 09:42:33.085995` => `2020-09-01`

Convertis en une date, tous les horodatages du même jour retourneront la même valeur de date — et seront donc placés dans le même groupe.

Pour ce faire, nous allons convertir la valeur d'horodatage `sold_at` en une date :

```sql
SELECT
  sold_at::DATE AS date,
  COUNT(*) AS sales_per_day
FROM sales
GROUP BY sold_at::DATE
ORDER BY sold_at::DATE;

```

Dans notre clause `GROUP BY`, nous utilisons `::DATE` pour tronquer la partie horodatage jusqu'au "jour". Cela supprime effectivement les heures/minutes/secondes de l'horodatage et retourne simplement le jour.

Dans notre `SELECT`, nous retournons également cette même expression et lui donnons un alias pour embellir la sortie.

Pour la même raison que nous ne pouvons pas retourner `product` sans le regrouper ou effectuer une sorte d'agrégation sur celui-ci, la base de données ne nous permettra pas de retourner simplement `sold_at` — tout dans le `SELECT` doit soit être dans le `GROUP BY`, soit une sorte d'agrégation sur les groupes résultants.

Le résultat est le _nombre de ventes par jour_ que nous voulions voir à l'origine :

```sql
    date    | sales_per_day
------------+---------------
 2020-08-29 |             2
 2020-08-30 |             2
 2020-08-31 |             1
 2020-09-01 |             3
(4 rows)

```

## Filtrage des groupes avec `HAVING`

Ensuite, voyons comment filtrer nos lignes regroupées.

Pour ce faire, essayons de trouver les jours où nous avons eu _plus d'une vente_.

Sans regroupement, nous filtrerions normalement nos lignes en utilisant une clause `WHERE`. Par exemple :

```sql
SELECT *
FROM sales
WHERE product = 'Coffee';

```

Avec nos groupes, nous pourrions vouloir faire quelque chose comme ceci pour filtrer nos groupes en fonction du nombre de lignes...

```sql
SELECT
  sold_at::DATE AS date,
  COUNT(*) AS sales_per_day
FROM sales
WHERE COUNT(*) > 1      -- filtrer les groupes ?
GROUP BY sold_at::DATE;

```

Malheureusement, cela ne fonctionne pas et nous recevons cette erreur : 

`ERROR:  aggregate functions are not allowed in WHERE`

Les fonctions d'agrégation ne sont pas autorisées dans la clause `WHERE` car la clause `WHERE` est évaluée **avant** la clause `GROUP BY` — il n'y a pas encore de groupes sur lesquels effectuer des calculs.

Mais, il existe un type de clause qui nous permet de filtrer, d'effectuer des agrégations, et qui est évaluée _après_ la clause `GROUP BY` : la clause `HAVING`.

**La clause `HAVING` est comme une clause `WHERE` pour vos groupes.**

Pour trouver les jours où nous avons eu plus d'une vente, nous pouvons ajouter une clause `HAVING` qui vérifie le nombre de lignes dans le groupe :

```sql
SELECT
  sold_at::DATE AS date,
  COUNT(*) AS sales_per_day
FROM sales
GROUP BY sold_at::DATE
HAVING COUNT(*) > 1;

```

Cette clause `HAVING` filtre toutes les lignes où le nombre de lignes dans ce groupe n'est pas supérieur à un, et nous voyons cela dans notre ensemble de résultats :

```
    date    | sales_per_day
------------+---------------
 2020-09-01 |             3
 2020-08-29 |             2
 2020-08-30 |             2
(3 rows)

```

Juste pour être complet, voici l'ordre d'exécution de toutes les parties d'une instruction SQL :

* `FROM` — Récupérer toutes les lignes de la table `FROM`
* `JOIN` — Effectuer les jointures
* `WHERE` — Filtrer les lignes
* `GROUP BY` — Former les groupes
* `HAVING` — Filtrer les groupes
* `SELECT` — Sélectionner les données à retourner
* `ORDER BY` — Ordonner les lignes de sortie
* `LIMIT` — Retourner un certain nombre de lignes

## Agrégats avec regroupement implicite

Le dernier sujet que nous allons aborder est les agrégations qui peuvent être effectuées sans un `GROUP BY` — ou peut-être mieux dit, elles ont un _regroupement implicite_.

Ces agrégations sont utiles dans des scénarios où vous voulez trouver une agrégation particulière à partir d'une table — comme le montant total des revenus ou la plus grande ou la plus petite valeur d'une colonne.

Par exemple, nous pourrions trouver le revenu total à travers _tous les magasins_ en sélectionnant simplement la somme de l'ensemble de la table :

```sql
SELECT SUM(price)
FROM sales;

```

```
 sum
-----
  19
(1 row)

```

Jusqu'à présent, nous avons réalisé 19 $ de ventes à travers tous les magasins (_hourra !_).

Une autre chose utile que nous pourrions interroger est la _première_ ou la _dernière_ occurrence de quelque chose.

Par exemple, quelle est la date de notre première vente ? 

Pour trouver cela, nous utilisons simplement la fonction `MIN()` :

```sql
SELECT MIN(sold_at)::DATE AS first_sale
FROM sales;

```

```
 first_sale
------------
 2020-08-29
(1 row)

```

(Pour trouver la date de la dernière vente, il suffit de substituer `MAX()` à `MIN()`.)

### Utilisation de `MIN` / `MAX`

Bien que ces requêtes simples puissent être utiles en tant que requêtes autonomes, elles font souvent partie de filtres pour des requêtes plus grandes.

Par exemple, essayons de trouver le total des ventes pour le _dernier jour_ où nous avons eu des ventes.

Une façon dont nous pourrions écrire cette requête serait comme ceci :

```sql
SELECT
  SUM(price)
FROM sales
WHERE sold_at::DATE = '2020-09-01';

```

Cette requête fonctionne, mais nous avons évidemment codé en dur la date du `2020-09-01`. 

Le 09/01/2020 peut être la dernière date à laquelle nous avons eu une vente, mais ce ne sera pas toujours cette date. Nous avons besoin d'une solution dynamique.

Cela peut être réalisé en combinant cette requête avec la fonction `MAX()` dans une sous-requête :

```sql
SELECT
  SUM(price)
FROM sales
WHERE sold_at::DATE = (
  SELECT MAX(sold_at::DATE)
  FROM sales
);

```

Dans notre clause `WHERE`, nous trouvons la plus grande date dans notre table en utilisant une sous-requête : `SELECT MAX(sold_at::DATE) FROM sales`. 

Ensuite, nous utilisons cette date maximale comme valeur sur laquelle nous filtrons la table, et nous additionnons le prix de chaque vente.

### Regroupement implicite

Je dis que ce sont des regroupements implicites car si nous essayons de sélectionner une valeur d'agrégation avec une colonne non agrégée comme ceci...

```sql
SELECT
  SUM(price),
  location
FROM sales;

```

... nous obtenons notre erreur familière :

```
ERROR:  column "sales.location" must appear in the GROUP BY clause or be used in an aggregate function

```

## `GROUP BY` est un outil

Comme pour de nombreux autres sujets en développement logiciel, `GROUP BY` est un outil.

Il existe de nombreuses façons d'écrire et de réécrire ces requêtes en utilisant des combinaisons de `GROUP BY`, de fonctions d'agrégation, ou d'autres outils comme `DISTINCT`, `ORDER BY` et `LIMIT`.

Comprendre et travailler avec les `GROUP BY` demandera un peu de pratique, mais une fois que vous l'aurez maîtrisé, vous découvrirez qu'une toute nouvelle série de problèmes sont maintenant résolubles pour vous ! 

Si vous avez aimé cet article, vous pouvez [me suivre sur Twitter](https://twitter.com/johnmosesman) où je parle de bases de données et de la manière de réussir une carrière en tant que développeur.

Merci d'avoir lu !

John