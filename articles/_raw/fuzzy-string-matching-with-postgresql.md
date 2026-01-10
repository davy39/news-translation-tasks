---
title: How to use fuzzy string matching with Postgresql
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
seo_title: null
seo_desc: 'By Peter Gleeson

  It''s a fact - people make typos or simply use alternate spellings on a frequent
  basis.

  Whatever the cause, from a practical point of view, different variants of similar
  strings can pose challenges for software developers. Your applic...'
---

By Peter Gleeson

It's a fact - people make typos or simply use alternate spellings on a frequent basis.

Whatever the cause, from a practical point of view, different variants of similar strings can pose challenges for software developers. Your application needs to be capable of handling these inevitable edge-cases.

Take names, for example. I go by Peter in some places, Pete in others. Amongst other variants, my name can be represented by:

* "Pete Gleeson"
* "Peter J Gleeson"
* "Mr P Gleeson"
* "Gleeson, Peter"

And that's not to mention alternative spellings of my surname, such as "Gleason". All these different variations for just one string - matching them against each other programmatically might not seem obvious.

Luckily, there are solutions out there.

The generic name for these solutions is 'fuzzy string matching'. The 'fuzzy' refers to the fact that the solution does not look for a perfect, position-by-position match when comparing two strings. Instead, they allow some degree of mismatch (or 'fuzziness').

There are solutions available in many different programming languages. Today, we'll explore some options available in Postgresql (or 'Postgres') - a widely used open source SQL dialect with some seriously useful add-on features.

### Setting up

First, make sure you [have Postgres installed on your machine](https://www.postgresql.org/download/).

Then, create a new database in its own directory (you can call it anything you like, here, I called it 'fuzz-demo'). From the command line:

```
$ mkdir fuzz-demo && cd fuzz-demo
$ initdb .
$ pg_ctl -D . start
$ createdb fuzz-demo
```

For this demo, I used a table with details about artists in the Museum of Modern Art. You can [download the artists.csv file from Kaggle.](https://www.kaggle.com/momanyc/museum-collection)

Next, you can start psql (a terminal-based front end for Postgresql):

```
$ psql fuzz-demo
```

Now, create a table called `artists`:

```sql
CREATE TABLE artists (
	artist_id INT,
    name VARCHAR,
    nationality VARCHAR,
    gender VARCHAR,
    birth_year INT,
    death_year INT);
```

Finally, you can use Postgresql's COPY function to copy the contents of artists.csv into the table:

```sql
COPY artists FROM '~/Downloads/artists.csv' DELIMTER ',' CSV HEADER;
```

If everything has worked so far, you should be able to start querying the artists table.

```sql
SELECT * FROM artists LIMIT 10;
```

### Wildcard filters

Say you remember the first name of an artist called Barbara, but cannot quite remember her second name. It began with 'Hep...', but you're not sure how it ended.

Here, you can use a filter and SQL's wildcard operator `%`. This symbol stands in for any number of unspecified characters.

```sql
SELECT
	* 
FROM artists
WHERE name LIKE 'Barbara%'
AND name LIKE '%Hep%';
```

The first part of the filter finds artists whose name begins with 'Barbara', and ends in any combination of characters. 

The second part of the filter finds artists whose name can begin and end with any combination of characters, but must contain the letters 'Hep' in that order.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-95.png)
_The output gives British artist Barbara Hepworth_

But what if you are unsure of the spelling of either name? Filters and wildcards will only get you so far.

### Using trigrams

Luckily, Postgres has a helpful extension with the catchy name pg_trgm. You can enable it from psql using the command below:

```sql
CREATE EXTENSION pg_trgm;
```

This extension brings with it some helpful functions for fuzzy string matching. The underlying principle is the use of trigrams (which sound like something out of Harry Potter).

Trigrams are formed by breaking a string into groups of three consecutive letters. For example, the string "hello" would be represented by the following set of trigrams:

* " h", " he", "hel", "ell", "llo", "lo "

By comparing how similar the set of trigrams are between two strings, it is possible to estimate how similar they are on a scale between 0 and 1. This allows for fuzzy matching, by setting a similarity threshold above which strings are considered to match.

```sql
SELECT
	*
FROM artists
WHERE SIMILARITY(name,'Claud Monay') > 0.4 ;
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-99.png)
_The output is Claude Monet (with the correct spelling!)_

Perhaps you want to see the top five matches?

```sql
SELECT 
	*
FROM artists
ORDER BY SIMILARITY(name,'Lee Casner') DESC
LIMIT 5;
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-108.png)
_The closest match is Lee Krasner, followed by Lee Chesney_

The default threshold is 0.3. You can use the `%` operator in this case as shorthand for fuzzy matching names against a potential match:

```sql
SELECT
	*
FROM artists
WHERE name % 'Andrey Deran';
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-100.png)
_The output gives two artists, including one Andre Derain_

Perhaps you only have an idea of one part of the name. The `%` operator lets you compare against elements of an array, so you can match against any part of the name. The next query uses Postgres' `STRING_TO_ARRAY` function to split the artists' full names into arrays of separate names.

```sql
SELECT
	*
FROM artists
WHERE 'Cadinsky' % ANY(STRING_TO_ARRAY(name,' '));
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-101.png)
_The output gives two rows, including Vasily Kandinsky_

### Phonetic algorithms

Another approach to fuzzy string matching comes from a group of algorithms called phonetic algorithms.

These are algorithms which use sets of rules to represent a string using a short code. The code contains the key information about how the string should sound if read aloud. By comparing these shortened codes, it is possible to fuzzy match strings which are spelled differently but sound alike.

Postgres comes with an extension that lets you make use of some of these algorithms. You can enable it with the following command:

```sql
CREATE EXTENSION fuzzystrmatch;
```

One example is an algorithm called Soundex. Its origins go back over 100 years - it was first patented in 1918 and was used in the 20th century for analysing US census data.

Soundex works by converting strings into four letter codes which describe how they sound. For example, the Soundex representations of 'flower' and 'flour' are both F460.

The query below finds the record which sounds like the name 'Damian Hurst'.

```sql
SELECT
	*
FROM artists
WHERE nationality IN ('American', 'British')
AND SOUNDEX(name) = SOUNDEX('Damian Hurst');
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-102.png)
_The result includes British artist Damien Hirst (with the correct spelling)_

Another algorithm is one called metaphone. This works on a similar basis to Soundex, in that it converts strings into a code representation using a set of rules.

The metaphone algorithm will return codes of different lengths (unlike Soundex, which always returns four characters). You can pass an argument to the `METAPHONE` function indicating the maximum length code you want it to return.

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
_The metaphone of each artist is produced._

Because both metaphone and Soundex return strings as outputs, you can use them in other fuzzy string matching functions. This combined approach can yield powerful results. The example below finds the five closest matches for the name Si Tomlee.

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
_The top result is American artist Cy Twombly._

Here, a trigram-only approach would not have helped much, as there is little overlap between 'Cy Twombly' and 'Si Tomlee'. In fact, these only have a `SIMILARITY` score of 0.05, even though they sound similar when read aloud.

Due to their historical origins, neither of these algorithms works well with names or words of non-English language origin. However, there are more internationally-focused versions.

One example is the double metaphone algorithm. This uses a more sophisticated set of rules for producing metaphones. It can provide alternative encodings for English and non-English origin strings.

As an example, see the query below. It compares the double metaphone outputs for different spellings of Spanish artist Joan Miró:

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
_Both the correct spelling and misspelling produce JNMR and ANMR as metaphones_

### Going the distance

Finally, another approach to fuzzy string matching in Postgres is to calculate the 'distance' between strings. There are several ways to do this. Postgres provides functionality to calculate the Levenshtein distance.

At a high level, the Levenshtein distance between two strings is the minimum number of edits required to transform one string into the other. Edits are considered at the character level, and can include:

* substitutions,
* deletions, and
* insertions

For example, the Levenshtein distance between the words 'bigger' and 'better' is 3, because you can transform 'bigger' into 'better' by substituting 'igg' for 'ett'.

Meanwhile, the Levenshtein distance between 'biggest' and 'best' is also 3, because you can transform 'biggest' into 'best' by deleting the letters 'igg'.

See below for a query which finds the artists with the smallest Levenshtein distances from the name 'Freda Kallo'.

```sql
SELECT
	*,
    LEVENSHTEIN(name, 'Freda Kallo')
FROM artists
ORDER BY LEVENSHTEIN(name, 'Freda Kallo') ASC
LIMIT 5
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-107.png)
_Mexican artist Frida Kahlo is the closest match, followed by Fred Niblo, Fred Taylor and Frank Gallo_

### Thanks for reading!

Hopefully this overview of fuzzy string matching in Postgresql has given you some new insights and ideas for your next project.

There are of course other methods for fuzzy string matching not covered here, and in other programming languages.

For example, if you use Python, take a look at the [fuzzywuzzy package](https://github.com/seatgeek/fuzzywuzzy). Or if you prefer R, you can use the inbuilt `agrep()` function, or try out the [stringdist package](https://cran.r-project.org/web/packages/stringdist/index.html).

