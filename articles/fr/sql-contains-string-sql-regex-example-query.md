---
title: SQL Contient une Chaîne – Exemple de Requête SQL RegEx
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-23T15:30:47.000Z'
originalURL: https://freecodecamp.org/news/sql-contains-string-sql-regex-example-query
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-kei-scampa-2370726.jpg
tags:
- name: Regex
  slug: regex
- name: SQL
  slug: sql
seo_title: SQL Contient une Chaîne – Exemple de Requête SQL RegEx
seo_desc: 'Being able to do complex queries can be really useful in SQL.

  In this article, we''ll look at how you can use the Contains String query.

  SQL Patterns

  SQL patterns are useful for pattern matching, instead of using literal comparisons.
  They have a more ...'
---

Pouvoir effectuer des requêtes complexes peut être vraiment utile en SQL.

Dans cet article, nous allons voir comment utiliser la requête `Contient une Chaîne`.

# Motifs SQL

Les motifs SQL sont utiles pour la correspondance de motifs, au lieu d'utiliser des comparaisons littérales. Ils ont une syntaxe plus limitée que RegEx, mais ils sont plus universels à travers les différentes versions de SQL.

Les motifs SQL utilisent les opérateurs `LIKE` et `NOT LIKE` et les métacaractères (caractères qui représentent autre chose qu'eux-mêmes) `%` et `_`.

Les opérateurs sont utilisés comme ceci : `column_name LIKE pattern`.

| Caractère | Signification |
| -- | -- |
| `%` | Toute séquence de caractères |
| `_` | Exactement un caractère |

Vous pouvez utiliser ces caractères dans une grande variété de cas d'utilisation. Voici quelques exemples :

| Exemple de motif | Utilisation |
| -- | -- |
| `re%` | Chaînes qui commencent par une sous-chaîne spécifique |
| `%re` | Chaînes qui se terminent par une sous-chaîne spécifique |
| `%re%` | Chaînes qui ont une sous-chaîne spécifique n'importe où dans la chaîne |
| `%re_` | Chaînes qui ont une sous-chaîne spécifique à une position spécifique depuis la fin¹ |
| `__re%` | Chaînes qui ont une sous-chaîne spécifique à une position spécifique depuis le début² |

¹ (dans l'exemple, les deuxième et troisième caractères depuis la fin sont déterminés)  
² (dans l'exemple, les troisième et quatrième caractères sont déterminés)

## Exemple de requête

```sql
SELECT name FROM planets
  WHERE name LIKE "%us";
```

Où `planets` est une table avec les données des planètes du système solaire.

Avec cette requête, vous obtiendrez les noms des planètes qui se terminent par "us" comme ci-dessous.

| name |
| --- |
| Venus |
| Uranus |

L'opérateur `NOT LIKE` trouve toutes les chaînes qui ne correspondent pas au motif.

Utilisons-le également dans un exemple.

```sql
SELECT name FROM planets
  WHERE name NOT LIKE "%u%";
```

Avec cette requête, vous obtenez toutes les planètes dont les noms ne contiennent pas la lettre `u`, comme ci-dessous.

| name |
| --- |
| Earth |
| Mars |

## Alternative à l'opérateur `LIKE` en SQL

Selon la version de SQL que vous utilisez, vous pourriez également pouvoir utiliser l'opérateur `SIMILAR TO`. Vous pouvez l'utiliser en plus ou à la place de `LIKE`.

### L'opérateur `SIMILAR TO` en SQL

L'opérateur `SIMILAR TO` fonctionne de manière assez similaire à l'opérateur `LIKE`, y compris les métacaractères disponibles. Vous pouvez utiliser l'opérateur `%` pour n'importe quel nombre de caractères, et l'opérateur `_` pour exactement un caractère.

Prenons l'exemple utilisé avec `LIKE` et utilisons-le ici aussi.

```sql
SELECT name FROM planets
  WHERE name SIMILAR TO "%us";
```

Vous pouvez utiliser cet opérateur avec `NOT` devant pour avoir l'effet opposé. Voici comment vous écririez l'exemple que nous avons utilisé auparavant en utilisant `SIMILAR TO` à la place :

```sql
SELECT name FROM planets
  WHERE name NOT SIMILAR TO "%u%";
```

# RegEx en SQL

Que faire si vous avez besoin d'une correspondance de motifs plus complexe ? Eh bien, pour cela, vous devez utiliser des Expressions Régulières.

## Qu'est-ce que RegEx ?

RegEx est un outil puissant qui permet une reconnaissance de motifs flexible. Vous pouvez utiliser RegEx dans de nombreux langages comme PHP, Python, et aussi SQL.

RegEx vous permet de faire correspondre des motifs par classe de caractères (comme toutes les lettres, ou juste les voyelles, ou tous les chiffres), entre des alternatives, et d'autres options vraiment flexibles. Vous les verrez ci-dessous.

## Ce que vous pouvez faire avec RegEx

Vous pouvez faire beaucoup de choses différentes avec les motifs RegEx. Pour voir une bonne variété, utilisons quelques-uns des exemples présentés dans le [Curriculum RegEx de freeCodeCamp](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/#regular-expressions). 

Gardez à l'esprit que le curriculum freeCodeCamp présente RegEx pour JavaScript, donc il n'y a pas de correspondance parfaite, et nous devons convertir la syntaxe. Néanmoins, cela vous donne un bon aperçu des fonctionnalités de base de RegEx, alors suivons ce curriculum pour que vous puissiez avoir une bonne idée de ce que RegEx peut faire.

### [Correspondre à des Chaînes Littérales](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-literal-strings)

La manière la plus simple d'utiliser RegEx est de l'utiliser pour correspondre à une séquence exacte de caractères. 

Par exemple, le regex `"Kevin"` correspondra à toutes les chaînes qui contiennent ces lettres dans cette séquence exacte, comme "**Kevin**", "**Kevin** est génial", "voici mon ami **Kevin**" et ainsi de suite.

### [Correspondre à une Chaîne Littérale avec Différentes Possibilités](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-a-literal-string-with-different-possibilities)

Une expression régulière peut être utilisée pour correspondre à différentes possibilités en utilisant le caractère `|`. Par exemple, `"yes|no|maybe"` correspondrait à n'importe quelle chaîne qui contient l'une des trois séquences de caractères, comme "**maybe** je vais le faire", "**maybe**lline", "mo**no**logue", "**yes**, je vais le faire", "**no**, je n'aime pas ça", et ainsi de suite.

### [Correspondre à N'importe Quoi avec le Point Joker](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-anything-with-wildcard-period)

Le point joker `.` correspond à n'importe quel caractère, par exemple `"hu."` correspondrait à n'importe quoi qui contient un `h` suivi d'un `u` suivi de n'importe quel caractère, comme "**hug**", "**hum**", "**hub**", "**huh**", mais aussi "**hus**band", "c**hur**ros", "t**hum**b", "s**hut**tle" et ainsi de suite.

### [Correspondre à un Caractère Unique avec Plusieurs Possibilités](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-single-character-with-multiple-possibilities)

Vous pouvez utiliser une _classe de caractères_ (ou _ensemble de caractères_) pour correspondre à un groupe de caractères, par exemple `"b[aiu]g"` correspondrait à n'importe quelle chaîne qui contient un `b`, puis une lettre entre `a`, `i` et `u`, et puis un `g`, comme "**bug**", "**big**", "**bag**", mais aussi "cab**bag**e", "am**big**ous", "lady**bug**", et ainsi de suite.

### [Correspondre aux Lettres de l'Alphabet](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-letters-of-the-alphabet)

Vous avez vu ci-dessus comment correspondre à un groupe de caractères avec des classes de caractères, mais si vous voulez correspondre à une longue liste de lettres, cela représente beaucoup de frappe.

Pour éviter toute cette frappe, vous pouvez définir une plage. Par exemple, vous pouvez correspondre à toutes les lettres entre `a` et `e` avec `"[a-e]"`.

Un regex comme `"[a-e]at"` correspondrait à toutes les chaînes qui ont dans l'ordre une lettre entre `a` et `e`, puis un `a` et puis un `t`, comme "**cat**", "**bat**" et "**eat**", mais aussi "bird**bat**h", "bu**cat**ini", "**dat**e", et ainsi de suite.

### [Correspondre aux Chiffres et Lettres de l'Alphabet](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-numbers-and-letters-of-the-alphabet)

Vous pouvez également utiliser le tiret pour correspondre à des chiffres. Par exemple, `"[0-5]"` correspondrait à n'importe quel chiffre entre `0` et `5`, y compris `0` et `5`.

Vous pouvez également combiner différentes plages ensemble dans un seul ensemble de caractères. Par exemple, `"[a-z0-9]"` correspondrait à toutes les lettres de `a` à `z` et à tous les chiffres de `0` à `5`.

### [Correspondre à des Caractères Uniques Non Spécifiés](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-single-characters-not-specified)

Vous pouvez également utiliser un ensemble de caractères pour exclure certains caractères d'une correspondance, ces ensembles sont appelés _ensembles de caractères négatifs_.

Vous pouvez créer un ensemble de caractères négatif en plaçant un caractère accent circonflexe (`^`) après le crochet ouvrant de la classe de caractères.

Par exemple, `"[^aeiou]"` correspond à tous les caractères qui ne sont pas des voyelles. Il correspondrait à des chaînes comme "rythm" où aucun caractère n'est une voyelle, ou aussi "87 + 14".

### [Correspondre à des Caractères qui Apparaissent Une ou Plusieurs Fois](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-characters-that-occur-one-or-more-times)

Si vous devez correspondre à un caractère spécifique ou à un groupe de caractères qui peut apparaître une ou plusieurs fois, vous pouvez utiliser le caractère `+` après ce caractère.

Par exemple, `"as+i"` correspondrait à des chaînes qui contiennent un `a` suivi d'un ou plusieurs `s` suivi d'un `i`, comme "occ**asi**onal", "**assi**duous" et ainsi de suite.

### [Correspondre à des Caractères qui Apparaissent Zéro ou Plusieurs Fois](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-characters-that-occur-zero-or-more-times)

Si vous pouvez utiliser `+` pour correspondre à un caractère une ou plusieurs fois, il y a aussi `*` pour correspondre à un caractère zéro ou plusieurs fois.

Une expression régulière telle que `"as*i"` correspondrait, en plus de "occ**asi**onal" et "**assi**duous", également à des chaînes comme "**ai**de".

### [Correspondre aux Motifs de Chaîne de Début](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-beginning-string-patterns)

Jusqu'à présent, vous avez vu des moyens de correspondre n'importe où dans la chaîne, sans l'option de dire où la correspondance doit être.

Nous utilisons le caractère `^` pour correspondre au début d'une chaîne, par exemple un regex comme `"^Ricky"` correspondrait à "**Ricky** est mon ami", mais pas à "C'est Ricky".

### [Correspondre aux Motifs de Chaîne de Fin](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-ending-string-patterns)

Tout comme il y a un moyen de correspondre au début d'une chaîne, il y a aussi un moyen de correspondre à la fin d'une chaîne.

Vous pouvez utiliser le caractère `$` pour correspondre à la fin d'une chaîne, donc par exemple `"story$"` correspondrait à n'importe quelle chaîne qui se termine par "story", comme "C'est une histoire sans fin", mais pas à une chaîne comme "Parfois une histoire doit se terminer".

### Correspondre à la Chaîne Entière

Vous pouvez combiner les deux caractères `^` et `$` pour correspondre à une chaîne entière.

Ainsi, en prenant l'un des exemples précédents, écrire `"b[aiu]g"` peut correspondre à la fois à "big" et "bigger", mais si au lieu de cela vous voulez correspondre uniquement à "big", "bag" et "bug", ajouter les deux caractères de début et de fin de chaîne garantit qu'il ne peut pas y avoir d'autres caractères dans la chaîne : `"^b[aiu]g$"`. Ce motif correspondrait uniquement à "big", "bag" et "bug", et il ne correspond pas à "bigger" ou "ambiguous".

### [Correspondre à Toutes les Lettres et Chiffres](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-all-letters-and-numbers)

Vous avez vu précédemment comment correspondre à des caractères avec une classe de caractères.

Il existe quelques classes prédéfinies, appelées classes POSIX, que vous pouvez utiliser à la place. Donc, si vous voulez correspondre à toutes les lettres et chiffres comme avec `"[0-9a-zA-Z]"`, vous pouvez à la place écrire `"[[:alphanum:]]"`.

### [Correspondre à Tout Sauf les Lettres et Chiffres](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-everything-but-letters-and-numbers)

Si au lieu de cela vous voulez correspondre à n'importe quoi qui n'est pas une lettre ou un chiffre, vous pouvez utiliser la classe POSIX `alphanum` avec un ensemble de caractères négatif : `"[^[:alphanum:]]`.

### [Correspondre à Tous les Chiffres](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-all-numbers)

Vous pouvez également utiliser une classe POSIX pour correspondre à tous les chiffres au lieu d'utiliser `"[0-9]"`, comme ceci : `"[[:digit:]]"`.

### [Correspondre à Tous les Non-Chiffres](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-all-non-numbers)

Vous pouvez utiliser la classe POSIX `digit` avec un ensemble de caractères négatif pour correspondre à n'importe quoi qui n'est pas un chiffre, comme ceci : `"[^[:digit:]]"`.

### [Correspondre aux Espaces Blancs](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-whitespace)

Vous pouvez correspondre aux espaces blancs avec la classe POSIX `"[[:blank:]]"` ou `"[[:space:]]"`. La différence entre ces deux classes est que la classe `blank` correspond uniquement aux espaces et aux tabulations, tandis que `space` correspond à tous les caractères blancs, y compris les retours chariot, les nouvelles lignes, les sauts de page et les tabulations verticales.

### [Correspondre aux Caractères Non Blancs](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-non-whitespace-characters)

Vous pouvez correspondre à n'importe quoi qui n'est pas un espace ou une tabulation avec `"[^[:blank:]]"`.

Et vous pouvez correspondre à n'importe quoi qui n'est pas un espace blanc, un retour chariot, une tabulation, un saut de page, un espace ou une tabulation verticale avec `"[^[:space:]]"`.

### [Spécifier le Nombre Supérieur et Inférieur de Correspondances](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/specify-upper-and-lower-number-of-matches)

Vous avez vu précédemment comment correspondre à un ou plusieurs caractères ou à zéro ou plusieurs caractères. Mais parfois, vous voulez correspondre à une certaine plage de motifs.

Pour cela, vous pouvez utiliser des _spécificateurs de quantité_.

Les spécificateurs de quantité sont écrits avec des accolades (`{` et `}`). Vous mettez deux nombres séparés par une virgule dans l'accolade. Le premier est le nombre inférieur de motifs, le second est le nombre supérieur de motifs.

Par exemple, si votre motif est `"Oh{2,4} yes"`, alors il correspondrait à des chaînes comme "Ohh yes" ou "Ohhhh yes", mais pas à "Oh yes" ou "Ohhhhh yes".

### [Spécifier le Nombre Exact de Correspondances](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/specify-exact-number-of-matches)

Vous pouvez également utiliser le spécificateur de quantité pour autre chose qu'une plage pour spécifier un nombre exact de correspondances. Vous pouvez le faire en écrivant un seul nombre à l'intérieur des accolades.

Ainsi, si votre motif est `"Oh{3} yes"`, alors il correspondrait uniquement à "Ohhh yes".

### [Vérifier le Groupement Mixte de Caractères](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/check-for-mixed-grouping-of-characters)

Si vous voulez vérifier des groupes de caractères en utilisant des expressions régulières, vous pouvez le faire en utilisant des parenthèses.

Par exemple, vous pouvez vouloir correspondre à la fois à "Penguin" et "Pumpkin", vous pouvez le faire avec une expression régulière comme celle-ci : `"P(engu|umpk)in"`.

## Résumé des Motifs RegEx

Vous avez vu beaucoup d'options regex ici. Alors maintenant, mettons toutes celles-ci, ainsi que quelques autres, dans des tableaux facilement consultables.

### Motifs RegEx

| motif | description |
| -- | -- |
| `^` | début de chaîne |
| `$` | fin de chaîne |
| `.` | n'importe quel caractère |
| `(  )` | regroupement de caractères |
| `[abc]` | n'importe quel caractère à l'intérieur des crochets |
| `[^abc]` | n'importe quel caractère *non* à l'intérieur des crochets |
| `a|b|c` | a OU b OU c |
| `*` | zéro ou plusieurs du précédent élément |
| `+` | un ou plusieurs du précédent élément |
| `{n}` | n fois le précédent élément |
| `{n,m}` | entre n et m fois le précédent élément |


### Classes Posix

Dans le tableau ci-dessous, vous pouvez voir les classes posix que nous avons vues ci-dessus, ainsi que quelques autres que vous pouvez utiliser pour créer des motifs.

| Classe Posix | similaire à | description |
| -- | -- | --|
| `[:alnum:]` | `[a-zA-Z0-9]` | Caractère alphanumérique |
| `[:alpha:]` | `[a-zA-Z]` | Caractères alphabétiques |
| `[:blank:]` |  | Espaces ou caractères de tabulation |
| `[:cntrl:]` | `[^[:print:]]` | Caractères de contrôle |
| `[:digit:]` | `[0-9]` | Caractères numériques |
| `[:graph:]` | `[^ [:ctrl:]]` | Tous les caractères qui ont une représentation graphique |
| `[:lower:]` | `[a-z]` | Caractères alphabétiques minuscules |
| `[:print:]` |`[[:graph:][:space:]]` | Caractères graphiques ou espaces |
| `[:punct:]` | | Tous les caractères graphiques sauf les lettres et les chiffres |
| `[:space:]` |  | Espace, nouvelle ligne, tabulation, retour chariot |
| `[:upper:]` | `[A-Z]` | Caractères alphabétiques majuscules |
| `[:xdigit:]` | `[0-9a-fA-F]` | Chiffres hexadécimaux |


Rappelez-vous que lorsque vous utilisez une classe POSIX, vous devez toujours la mettre à l'intérieur des crochets d'une classe de caractères (vous aurez donc deux paires de crochets). Par exemple, `"a[[:digit:]]b"` correspond à `a0b`, `a1b` et ainsi de suite.

## Comment utiliser les Motifs RegEx

Ici, vous verrez deux types d'opérateurs, les opérateurs `REGEXP` et les opérateurs POSIX. Sachez simplement que les opérateurs que vous pouvez utiliser dépendent de la version de SQL que vous utilisez.

### Opérateurs RegEx

Les opérateurs RegEx sont généralement insensibles à la casse, ce qui signifie qu'ils ne distinguent pas les lettres majuscules et minuscules. Donc pour eux, `a` est équivalent à `A`. Mais vous pouvez changer ce comportement par défaut, alors ne le prenez pas pour acquis.

| Opérateur | Description |
| -- | -- |
| `REGEXP` | Donne vrai si cela correspond au motif donné |
| `NOT REGEXP` | Donne vrai si la chaîne ne contient pas le motif donné |

### Opérateurs Posix

L'autre type d'opérateurs que vous pourriez avoir à disposition sont les opérateurs POSIX. Au lieu d'être des mots-clés, ceux-ci sont représentés par des ponctuations, et peuvent être sensibles ou insensibles à la casse.

| opérateur | description |
| -- | -- |
| `~` | sensible à la casse, vrai si le motif est contenu dans la chaîne
| `!~` | sensible à la casse, vrai si le motif n'est **pas** contenu dans la chaîne
| `~*` | insensible à la casse, vrai si le motif est contenu dans la chaîne
| `!~*` | insensible à la casse, vrai si le motif n'est **pas** contenu dans la chaîne

### Exemples RegEx et Posix

Voyons comment utiliser ces opérateurs et motifs RegEx dans une requête.

#### Exemple de requête 1

Pour ce premier exemple, vous voulez correspondre à une chaîne dans laquelle le premier caractère est un "s" ou "p" et le deuxième caractère est une voyelle. 

Pour ce faire, vous pouvez utiliser la classe de caractères `[sp]` pour correspondre à la première lettre, et vous pouvez utiliser la classe de caractères `[aeiou]` pour la deuxième lettre de la chaîne.

Vous devez également utiliser le caractère pour correspondre au début de la chaîne, `^`, donc ensemble vous écrirez `"^[sp][aeiou]"`.

Vous écrivez la requête ci-dessous pour obtenir la liste des utilisateurs dont les noms correspondent au motif.

```sql
SELECT name FROM users
  WHERE name REGEXP '^[sp][aeiou]';
```

Et si le comportement par défaut insensible à la casse a été modifié, vous devrez écrire un motif qui permet à la fois les lettres majuscules et minuscules, comme `"^[spSP][aeiouAEIOU]"` et l'utiliser dans la requête comme ci-dessous :

```sql
SELECT name FROM users
  WHERE name REGEXP '^[spSP][aeiouAEIOU]';
```

Ou avec l'opérateur POSIX, dans ce cas, vous pourriez utiliser l'opérateur insensible à la casse, `~*` et vous n'auriez pas besoin d'écrire à la fois les lettres majuscules et minuscules à l'intérieur d'une classe de caractères. Vous pourriez écrire la requête comme ci-dessous.

```
SELECT name FROM users
  WHERE name ~* '^[sp][aeiou]';
```

Comme l'opérateur est par définition insensible à la casse, vous n'avez pas besoin de vous soucier de spécifier à la fois les lettres majuscules et minuscules dans la classe de caractères.

Ces requêtes donneraient une table avec des résultats similaires à ci-dessous :

| name |
| -- |
| Sergio |
| PAUL |
| samantha |
| Seraphina |

#### Exemple de requête 2

En tant que deuxième exemple, disons que vous voulez trouver une [couleur hexadécimale](https://www.freecodecamp.org/news/css-background-color-how-to-change-the-background-color-in-html/#hexadecimal-colors). Vous pouvez utiliser la classe POSIX `[:xdigit:]` pour cela – elle fait la même chose que la classe de caractères `[0-9a-fA-F]`.

Écrire `#[[:xdigit:]]{3}` ou `#[[:xdigit:]]{6}` correspondrait à une couleur hexadécimale sous sa forme abrégée ou longue : le premier correspondrait à des couleurs comme `#398` et le second à des couleurs comme `#00F5C4`.

Vous pourriez les combiner en utilisant le regroupement de caractères et `|` pour avoir un seul motif RegEx qui correspond aux deux, et l'utiliser dans la requête comme ci-dessous :

```sql
SELECR color FROM styles
  WHERE color REGEXP '#([[:xdigit:]]{3}|[[:xdigit:]]{6})';
 
```

```sql
SELECR color FROM styles
  WHERE color ~ '#([[:xdigit:]]{3}|[[:xdigit:]]{6})';
```

Cela donnerait quelque chose comme ci-dessous :

| color |
| --- |
| `#341` |
| `#00fa67 ` |
| `#FF00AB` |

La classe POSIX `[:xdigit:]` inclut déjà les lettres majuscules et minuscules, donc vous n'auriez pas besoin de vous soucier de savoir si l'opérateur est sensible à la casse ou non.

### Note sur l'utilisation des ressources

Selon la taille de vos tables, une requête Contient une Chaîne peut être vraiment intensive en ressources. Soyez prudent lorsque vous les utilisez dans des bases de données de production, car vous ne voulez pas que votre application cesse de fonctionner.

# Conclusion

Les requêtes Contient une Chaîne sont vraiment utiles. Vous avez appris comment les utiliser dans cet article, et vous avez vu quelques exemples. 

Espérons que vous avez ajouté un nouvel outil à votre arsenal, et que vous appréciez l'utiliser ! Faites simplement attention à ne pas faire planter votre application.