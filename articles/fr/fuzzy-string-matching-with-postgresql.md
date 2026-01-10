---
title: Comment utiliser la correspondance floue de chaînes avec PostgreSQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-16T11:27:00.000Z'
originalURL: https://freecodecamp.org/news/fuzzy-string-matching-with-postgresql
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca063740569d1a4ca4858.jpg
tags:
- name: algorithms
  slug: algorithms
- name: backend
  slug: backend
- name: database
  slug: database
- name: nlp
  slug: nlp
- name: postgres
  slug: postgres
- name: SQL
  slug: sql
seo_title: Comment utiliser la correspondance floue de chaînes avec PostgreSQL
seo_desc: 'By Peter Gleeson

  It''s a fact - people make typos or simply use alternate spellings on a frequent
  basis.

  Whatever the cause, from a practical point of view, different variants of similar
  strings can pose challenges for software developers. Your applic...'
---

Par Peter Gleeson

C'est un fait - les gens font des fautes de frappe ou utilisent simplement des orthographes alternatives de manière fréquente.

Quelle qu'en soit la cause, d'un point de vue pratique, différentes variantes de chaînes similaires peuvent poser des défis pour les développeurs de logiciels. Votre application doit être capable de gérer ces cas particuliers inévitables.

Prenons les noms, par exemple. Je suis appelé Peter dans certains endroits, Pete dans d'autres. Parmi d'autres variantes, mon nom peut être représenté par :

* "Pete Gleeson"
* "Peter J Gleeson"
* "Mr P Gleeson"
* "Gleeson, Peter"

Et cela sans mentionner les orthographes alternatives de mon nom de famille, comme "Gleason". Toutes ces différentes variations pour une seule chaîne - les faire correspondre les unes aux autres de manière programmatique peut ne pas sembler évident.

Heureusement, il existe des solutions.

Le nom générique de ces solutions est 'fuzzy string matching'. Le terme 'fuzzy' fait référence au fait que la solution ne recherche pas une correspondance parfaite, position par position, lors de la comparaison de deux chaînes. Au lieu de cela, elles permettent un certain degré de non-correspondance (ou 'flou').

Il existe des solutions disponibles dans de nombreux langages de programmation différents. Aujourd'hui, nous allons explorer certaines options disponibles dans PostgreSQL (ou 'Postgres') - un dialecte SQL open source largement utilisé avec des fonctionnalités supplémentaires sérieusement utiles.

### Installation

Tout d'abord, assurez-vous d'avoir Postgres installé sur votre machine (https://www.postgresql.org/download/).

Ensuite, créez une nouvelle base de données dans son propre répertoire (vous pouvez l'appeler comme vous le souhaitez, ici, je l'ai appelée 'fuzz-demo'). Depuis la ligne de commande :

```
$ mkdir fuzz-demo && cd fuzz-demo
$ initdb .
$ pg_ctl -D . start
$ createdb fuzz-demo
```

Pour cette démonstration, j'ai utilisé une table avec des détails sur les artistes du Museum of Modern Art. Vous pouvez télécharger le fichier artists.csv depuis Kaggle (https://www.kaggle.com/momanyc/museum-collection).

Ensuite, vous pouvez démarrer psql (un frontal basé sur le terminal pour PostgreSQL) :

```
$ psql fuzz-demo
```

Maintenant, créez une table appelée `artists` :

```sql
CREATE TABLE artists (
	artist_id INT,
    name VARCHAR,
    nationality VARCHAR,
    gender VARCHAR,
    birth_year INT,
    death_year INT);
```

Enfin, vous pouvez utiliser la fonction COPY de PostgreSQL pour copier le contenu de artists.csv dans la table :

```sql
COPY artists FROM '~/Downloads/artists.csv' DELIMTER ',' CSV HEADER;
```

Si tout a fonctionné jusqu'à présent, vous devriez pouvoir commencer à interroger la table des artistes.

```sql
SELECT * FROM artists LIMIT 10;
```

### Filtres avec caractères génériques

Supposons que vous vous souvenez du prénom d'une artiste appelée Barbara, mais que vous ne vous souvenez pas tout à fait de son deuxième prénom. Il commençait par 'Hep...', mais vous n'êtes pas sûr de la fin.

Ici, vous pouvez utiliser un filtre et l'opérateur générique `%` de SQL. Ce symbole représente n'importe quel nombre de caractères non spécifiés.

```sql
SELECT
	* 
FROM artists
WHERE name LIKE 'Barbara%'
AND name LIKE '%Hep%';
```

La première partie du filtre trouve les artistes dont le nom commence par 'Barbara' et se termine par n'importe quelle combinaison de caractères.

La deuxième partie du filtre trouve les artistes dont le nom peut commencer et se terminer par n'importe quelle combinaison de caractères, mais doit contenir les lettres 'Hep' dans cet ordre.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-95.png)
_La sortie donne l'artiste britannique Barbara Hepworth_

Mais que faire si vous n'êtes pas sûr de l'orthographe de l'un ou l'autre nom ? Les filtres et les caractères génériques ne vous mèneront que jusqu'à un certain point.

### Utilisation des trigrams

Heureusement, Postgres dispose d'une extension utile avec le nom accrocheur pg_trgm. Vous pouvez l'activer depuis psql en utilisant la commande ci-dessous :

```sql
CREATE EXTENSION pg_trgm;
```

Cette extension apporte avec elle quelques fonctions utiles pour la correspondance floue de chaînes. Le principe sous-jacent est l'utilisation de trigrams (qui sonnent comme quelque chose sorti de Harry Potter).

Les trigrams sont formés en divisant une chaîne en groupes de trois lettres consécutives. Par exemple, la chaîne "hello" serait représentée par l'ensemble suivant de trigrams :

* " h", " he", "hel", "ell", "llo", "lo "

En comparant la similarité de l'ensemble des trigrams entre deux chaînes, il est possible d'estimer leur similarité sur une échelle entre 0 et 1. Cela permet une correspondance floue, en fixant un seuil de similarité au-dessus duquel les chaînes sont considérées comme correspondantes.

```sql
SELECT
	*
FROM artists
WHERE SIMILARITY(name,'Claud Monay') > 0.4 ;
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-99.png)
_La sortie est Claude Monet (avec l'orthographe correcte !)_

Peut-être voulez-vous voir les cinq meilleures correspondances ?

```sql
SELECT 
	*
FROM artists
ORDER BY SIMILARITY(name,'Lee Casner') DESC
LIMIT 5;
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-108.png)
_La meilleure correspondance est Lee Krasner, suivie de Lee Chesney_

Le seuil par défaut est 0,3. Vous pouvez utiliser l'opérateur `%` dans ce cas comme raccourci pour la correspondance floue des noms avec une correspondance potentielle :

```sql
SELECT
	*
FROM artists
WHERE name % 'Andrey Deran';
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-100.png)
_La sortie donne deux artistes, dont un Andre Derain_

Peut-être n'avez-vous qu'une idée d'une partie du nom. L'opérateur `%` vous permet de comparer avec les éléments d'un tableau, donc vous pouvez faire correspondre avec n'importe quelle partie du nom. La requête suivante utilise la fonction `STRING_TO_ARRAY` de Postgres pour diviser les noms complets des artistes en tableaux de noms séparés.

```sql
SELECT
	*
FROM artists
WHERE 'Cadinsky' % ANY(STRING_TO_ARRAY(name,' '));
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-101.png)
_La sortie donne deux lignes, dont Vasily Kandinsky_

### Algorithmes phonétiques

Une autre approche de la correspondance floue de chaînes provient d'un groupe d'algorithmes appelés algorithmes phonétiques.

Ce sont des algorithmes qui utilisent des ensembles de règles pour représenter une chaîne à l'aide d'un code court. Le code contient les informations clés sur la façon dont la chaîne doit sonner si elle est lue à voix haute. En comparant ces codes raccourcis, il est possible de faire correspondre de manière floue des chaînes qui sont orthographiées différemment mais qui sonnent de manière similaire.

Postgres dispose d'une extension qui vous permet d'utiliser certains de ces algorithmes. Vous pouvez l'activer avec la commande suivante :

```sql
CREATE EXTENSION fuzzystrmatch;
```

Un exemple est un algorithme appelé Soundex. Ses origines remontent à plus de 100 ans - il a été breveté pour la première fois en 1918 et a été utilisé au 20e siècle pour analyser les données du recensement américain.

Soundex fonctionne en convertissant les chaînes en codes de quatre lettres qui décrivent leur son. Par exemple, les représentations Soundex de 'flower' et 'flour' sont toutes deux F460.

La requête ci-dessous trouve l'enregistrement qui sonne comme le nom 'Damian Hurst'.

```sql
SELECT
	*
FROM artists
WHERE nationality IN ('American', 'British')
AND SOUNDEX(name) = SOUNDEX('Damian Hurst');
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-102.png)
_Le résultat inclut l'artiste britannique Damien Hirst (avec l'orthographe correcte)_

Un autre algorithme est appelé metaphone. Cela fonctionne sur une base similaire à Soundex, en ce sens qu'il convertit les chaînes en une représentation de code en utilisant un ensemble de règles.

L'algorithme metaphone retournera des codes de différentes longueurs (contrairement à Soundex, qui retourne toujours quatre caractères). Vous pouvez passer un argument à la fonction `METAPHONE` indiquant la longueur maximale du code que vous souhaitez qu'elle retourne.

```sql
SELECT
	artist_id,
    name,
    METAPHONE(name,10)
FROM artists
WHERE nationality = 'American'
LIMIT 5;
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-103.png)
_Le metaphone de chaque artiste est produit._

Parce que metaphone et Soundex retournent des chaînes comme sorties, vous pouvez les utiliser dans d'autres fonctions de correspondance floue de chaînes. Cette approche combinée peut donner des résultats puissants. L'exemple ci-dessous trouve les cinq correspondances les plus proches pour le nom Si Tomlee.

```sql
SELECT
	*
FROM artists
WHERE nationality = 'American'
ORDER BY SIMILARITY(
	METAPHONE(name,10),
    METAPHONE('Si Tomlee',10)
    ) DESC
LIMIT 5;
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-104.png)
_Le meilleur résultat est l'artiste américain Cy Twombly._

Ici, une approche basée uniquement sur les trigrams n'aurait pas beaucoup aidé, car il y a peu de chevauchement entre 'Cy Twombly' et 'Si Tomlee'. En fait, ceux-ci n'ont qu'un score de `SIMILARITY` de 0,05, même s'ils sonnent de manière similaire lorsqu'ils sont lus à voix haute.

En raison de leurs origines historiques, aucun de ces algorithmes ne fonctionne bien avec les noms ou les mots d'origine non anglaise. Cependant, il existe des versions plus axées sur l'international.

Un exemple est l'algorithme double metaphone. Celui-ci utilise un ensemble de règles plus sophistiqué pour produire des metaphones. Il peut fournir des encodages alternatifs pour les chaînes d'origine anglaise et non anglaise.

Par exemple, voir la requête ci-dessous. Elle compare les sorties double metaphone pour différentes orthographes de l'artiste espagnol Joan Miró :

```sql
SELECT
	'Joan Miró' AS name, 
    DMETAPHONE('Joan Miró'),
    DMETAPHONE_ALT('Joan Miró')
UNION SELECT
	'Juan Mero' AS name,
    DMETAPHONE('Juan Mero'),
    DMETAPHONE_ALT('Juan Mero');
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-106.png)
_L'orthographe correcte et la mauvaise orthographe produisent toutes deux JNMR et ANMR comme metaphones_

### Calculer la distance

Enfin, une autre approche de la correspondance floue de chaînes dans Postgres consiste à calculer la 'distance' entre les chaînes. Il existe plusieurs façons de faire cela. Postgres fournit une fonctionnalité pour calculer la distance de Levenshtein.

À un niveau élevé, la distance de Levenshtein entre deux chaînes est le nombre minimum d'éditions requises pour transformer une chaîne en une autre. Les éditions sont considérées au niveau du caractère et peuvent inclure :

* substitutions,
* suppressions, et
* insertions

Par exemple, la distance de Levenshtein entre les mots 'bigger' et 'better' est 3, car vous pouvez transformer 'bigger' en 'better' en substituant 'igg' par 'ett'.

Pendant ce temps, la distance de Levenshtein entre 'biggest' et 'best' est également 3, car vous pouvez transformer 'biggest' en 'best' en supprimant les lettres 'igg'.

Voir ci-dessous pour une requête qui trouve les artistes avec les plus petites distances de Levenshtein par rapport au nom 'Freda Kallo'.

```sql
SELECT
	*,
    LEVENSHTEIN(name, 'Freda Kallo')
FROM artists
ORDER BY LEVENSHTEIN(name, 'Freda Kallo') ASC
LIMIT 5
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-107.png)
_L'artiste mexicaine Frida Kahlo est la meilleure correspondance, suivie de Fred Niblo, Fred Taylor et Frank Gallo_

### Merci d'avoir lu !

Espérons que cet aperçu de la correspondance floue de chaînes dans PostgreSQL vous a donné de nouvelles perspectives et idées pour votre prochain projet.

Il existe bien sûr d'autres méthodes pour la correspondance floue de chaînes non couvertes ici, et dans d'autres langages de programmation.

Par exemple, si vous utilisez Python, jetez un coup d'œil au package fuzzywuzzy (https://github.com/seatgeek/fuzzywuzzy). Ou si vous préférez R, vous pouvez utiliser la fonction intégrée `agrep()`, ou essayer le package stringdist (https://cran.r-project.org/web/packages/stringdist/index.html).