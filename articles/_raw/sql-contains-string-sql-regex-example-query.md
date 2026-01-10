---
title: SQL Contains String – SQL RegEx Example Query
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
seo_title: null
seo_desc: 'Being able to do complex queries can be really useful in SQL.

  In this article, we''ll look at how you can use the Contains String query.

  SQL Patterns

  SQL patterns are useful for pattern matching, instead of using literal comparisons.
  They have a more ...'
---

Being able to do complex queries can be really useful in SQL.

In this article, we'll look at how you can use the `Contains String` query.

# SQL Patterns

SQL patterns are useful for pattern matching, instead of using literal comparisons. They have a more limited syntax than RegEx, but they're more universal through the various SQL versions.

SQL patterns use the `LIKE` and `NOT LIKE` operators and the metacharacters (characters that stand for something other than themselves) `%` and `_`.

The operators are used like this: `column_name LIKE pattern`.

| Character | Meaning |
| -- | -- |
| `%` | Any sequence of characters |
| `_` | Exactly one character |

You can use these characters in a wide variety of use-cases. Here are some examples:

| example pattern | usage |
| -- | -- |
| `re%` | Strings that begin with a specific substring |
| `%re` | Strings that end with a specific substring |
| `%re%` | Strings that have a specific substring anywhere in the string |
| `%re_` | Strings that have a specific substring at a specific position from the end¹ |
| `__re%` | Strings that have a specific substring at a specific position from the beginning² |

¹ (in the example, second to last and third to last characters are determined)  
² (in the example, third and fourth characters are determined)

## Example query

```sql
SELECT name FROM planets
  WHERE name LIKE "%us";
```

 Where `planets` is a table with the data of the solar system's planets.

With this query you would get the below names of the planets that end with "us".

| name |
| --- |
| Venus |
| Uranus |

The `NOT LIKE` operator finds all strings that do not match the pattern.

Let's use it in an example too.

```sql
SELECT name FROM planets
  WHERE name NOT LIKE "%u%";
```

With this query you get all planets whose names don't contain the letter `u`, like below.

| name |
| --- |
| Earth |
| Mars |

## Alternative to the `LIKE` operator in SQL

Depending on the SQL flavour you are using, you might also be able to use the `SIMILAR TO` operator. You can use it in addition to or in place of `LIKE`.

### The SQL `SIMILAR TO` operator

The `SIMILAR TO` operator works in a pretty similar way to the `LIKE` operator, including which metacharacters are available. You can use the `%` operator for any number of characters, and the `_` operator for exactly one character.

Let's take the example used with `LIKE` and let's use it here too.

```sql
SELECT name FROM planets
  WHERE name SIMILAR TO "%us";
```

You can use this operator with `NOT` in front to have the opposite effect. This is how you would write the example we used before using `SIMILAR TO` instead:

```sql
SELECT name FROM planets
  WHERE name NOT SIMILAR TO "%u%";
```

# RegEx in SQL

What about if you need more complex pattern matching? Well, for that you need to use Regular Expressions.

## What is RegEx?

RegEx on its own is a powerful tool that allows for flexible pattern recognition. You can use RegEx in many languages like PHP, Python, and also SQL.

RegEx lets you match patterns by character class (like all letters, or just vowels, or all digits), between alternatives, and other really flexible options. You will see them below.

## What you can do with RegEx

You can do a lot of different things with RegEx patterns. To see a good variety, let's use some of the examples presented in the [RegEx freeCodeCamp Curriculum](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/#regular-expressions). 

Keep in mind that the freeCodeCamp curriculum presents RegEx for JavaScript, so there is not a perfect match, and we need to convert the syntax. Still, it gives you a good overview of basic RegEx features, so let's follow this curriculum so you can get a good idea of what RegEx can do.

### [Match Literal Strings](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-literal-strings)

The easiest way to use RegEx it's to use it to match an exact sequence of characters. 

For example the regex `"Kevin"` will match all strings that contains those letters in that exact sequence, as "**Kevin**", "**Kevin** is great", "this is my friend **Kevin**" and so on.

### [Match a Literal String with Different Possibilities](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-a-literal-string-with-different-possibilities)

A regular expression can be used to match different possibilities using the character `|`. For example `"yes|no|maybe"` would match any string that contains one of the three sequence of characters, such as "**maybe** I will do it", "**maybe**lline", "mo**no**logue", "**yes**, I will do it", "**no**, I don't like it", and so on.

### [Match Anything with the Wildcard Period](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-anything-with-wildcard-period)

The wildcard period `.` matches any character, for example `"hu."` would match anything that contains an `h` followed by an `u` followed by any character, such as "**hug**", "**hum**", "**hub**", "**huh**", but also "**hus**band", "c**hur**ros", "t**hum**b", "s**hut**tle" and so on.

### [Match Single Character with Multiple Possibilities](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-single-character-with-multiple-possibilities)

You can use a _character class_ (or _character set_) to match a group of characters, for example `"b[aiu]g"` would match any string that contains a `b`, then one letter between `a`, `i` and `u`, and then a `g`, such as "**bug**", "**big**", "**bag**", but also "cab**bag**e", "am**big**ous", "lady**bug**", and so on.

### [Match Letters of the Alphabet](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-letters-of-the-alphabet)

You have seen above how you can match a group of characters with character classes, but if you want to match a long list of letters that is a lot of typing.

To avoid all that typing, you can define a range. For example you can match all letters between `a` and `e` with `"[a-e]"`.

A regex like `"[a-e]at"` would match all strings that have in order one letter between `a` and `e`, then an `a` and then a `t`, such as "**cat**", "**bat**" and "**eat**", but also "bird**bat**h", "bu**cat**ini", "**dat**e", and so on.

### [Match Numbers and Letters of the Alphabet](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-numbers-and-letters-of-the-alphabet)

You can also use the hyphen to match numbers. For example `"[0-5]"` would match any number between `0` and `5`, including `0` and `5`.

You can also combine different ranges together in a single character set. For example `"[a-z0-9]"` would match all letters from `a` to `z` and all numbers from `0` to `5`.

### [Match Single Characters Not Specified](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-single-characters-not-specified)

You can also use a character set to exclude some characters from a match, these sets are called _negated character sets_.

You can create a negated character set by placing a caret character (`^`) after the opening bracket of the character class.

For example `"[^aeiou]"` matches all characters that are not vowels. It would match strings like "rythm" where no character is a vowel, or also "87 + 14".

### [Match Characters that Occur One or More Times](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-characters-that-occur-one-or-more-times)

If you need to match a specific character or group of characters that can appear one or more times, you can use the character `+` after this character.

For example, `"as+i"` would match strings that contain one `a` followed by one or more `s` followed by one `i`, such as "occ**asi**onal", "**assi**duous" and so on.

### [Match Characters that Occur Zero or More Times](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-characters-that-occur-zero-or-more-times)

If you can use `+` to match a character one or more times, there is also `*` to match a character zero or more times.

A regular expression such as `"as*i"` would match, other than "occ**asi**onal" and "**assi**duous" also strings such as "**ai**de".

### [Match Beginning String Patterns](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-beginning-string-patterns)

Until now you have seen ways to match anywhere in the string, without the option to say where the match must be.

We use the character `^` to match the beginning of a string, for example a regex such as `"^Ricky"` would match "**Ricky** is my friend", but not "This is Ricky".

### [Match Ending String Patterns](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-ending-string-patterns)

Just as there's a way to match the beginning of a string, there is also a way to match the end of a string.

You can use the character `$` to match the end of a string, so for example `"story$"` would match any string that ends with "story", such as "This is a never ending **story**", but not a string such a "Sometimes a story will have to end".

### Match the Whole String

You can combine the two characters `^` and `$` to match a whole string.

So, taking one of the previous examples, writing `"b[aiu]g"` can match both "big" and "bigger", but if instead you want to match only "big", "bag" and "bug", adding the two beginning and ending string characters ensures that there can't be other characters in the string: `"^b[aiu]g$"`. This pattern would match only "big", "bag" and "bug", and it doesn't match "bigger" or "ambiguous".

### [Match All Letters and Numbers](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-all-letters-and-numbers)

You have seen before how to match characters with a character class.

There are a few predefined classes, called POSIX classes, that you can use instead. So if you want to match all letters and numbers like with `"[0-9a-zA-Z]"` you can instead write `"[[:alphanum:]]"`.

### [Match Everything But Letters and Numbers](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-everything-but-letters-and-numbers)

If instead you want to match anything that is not a letter of a number, you can use the `alphanum` POSIX class together with a negated character set: `"[^[:alphanum:]]`.

### [Match All Numbers](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-all-numbers)

You can also use a POSIX class to match all numbers instead of using `"[0-9]"`, like so: `"[[:digit:]]"`.

### [Match All Non-Numbers](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-all-non-numbers)

You can use the `digit` POSIX class with a negated character set to match anything that is not a number, like so: `"[^[:digit:]]"`.

### [Match Whitespace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-whitespace)

You can match whitespace with the POSIX class `"[[:blank:]]"` or `"[[:space:]]"`. The difference between these two classes is that the class `blank` matches only spaces and tabs, while `space` matches all blank characters, including carriage returns, new lines, form feeds, and vertical tabs.

### [Match Non-Whitespace Characters](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/match-non-whitespace-characters)

You can match anything that is not a space or tab with `"[^[:blank:]]"`.

And you can match anything that is not a whitespace, carriage return, tab, form feed, space, or vertical tab with `"[^[:space:]]"`.

### [Specify Upper and Lower Number of Matches](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/specify-upper-and-lower-number-of-matches)

You have seen before how to match one or more or zero or more characters. But sometimes you want to match a certain range of patterns.

For this you can use _quantity specifiers_.

Quantity specifiers are written with curly brackets (`{` and `}`). You put two numbers separated by a comma in the curly bracket. The first is the lower number of patterns, the second is the upper number of patterns.

For example, if your pattern is `"Oh{2,4} yes"`, then it would match strings like "Ohh yes" or "Ohhhh yes", but not "Oh yes" or "Ohhhhh yes".

### [Specify Exact Number of Matches](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/specify-exact-number-of-matches)

You can also use the quantity specifier other than for a range to specify an exact number of matches. You can do this by writing a single number inside the curly brackets.

So, if your pattern is `"Oh{3} yes"`, then it would match only "Ohhh yes".

### [Check For Mixed Grouping of Characters](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/check-for-mixed-grouping-of-characters)

If you want to check for groups of characters using regular expressions you can do so using parenthesis.

For example, you may want to match both "Penguin" and "Pumpkin", you can do so with a regular expression like this: `"P(engu|umpk)in"`.

## Summary of RegEx patterns

You have seen a lot of regex options here. So now let's put all of these, along with a few others, into easily consultable tables.

### RegEx patterns

| pattern | description |
| -- | -- |
| `^` | beginning of string |
| `$` | end of string |
| `.` | any character |
| `(  )` | grouping characters |
| `[abc]` | any character inside the square brackets |
| `[^abc]` | any character *not* inside the square brackets |
| `a|b|c` | a OR b OR c |
| `*` | zero or more of the preceding element |
| `+` | one or more of the preceding element |
| `{n}` | n times the preceding element |
| `{n,m}` | between n and m times the preceding element |


### Posix classes

In the table below you can see the posix classes we saw above, as well as some others that you can use to create patterns.

| Posix class | similar to | description |
| -- | -- | --|
| `[:alnum:]` | `[a-zA-Z0-9]` | Aphanumeric character |
| `[:alpha:]` | `[a-zA-Z]` | Alphabetic characters |
| `[:blank:]` |  | Spaces or tab characters |
| `[:cntrl:]` | `[^[:print:]]` | Control characters |
| `[:digit:]` | `[0-9]` | Numeric characters |
| `[:graph:]` | `[^ [:ctrl:]]` | All characters that have graphic rapresentation |
| `[:lower:]` | `[a-z]` | Lowercase alphabetic characters |
| `[:print:]` |`[[:graph:][:space:]]` | Graphic or spaces characters |
| `[:punct:]` | | All graphic characters except letters and digits |
| `[:space:]` |  | Space, new line, tab, carriage return |
| `[:upper:]` | `[A-Z]` | Uppercase alphabetic characters |
| `[:xdigit:]` | `[0-9a-fA-F]` | Hexadecimal digits |


Remember that when using a POSIX class, you always need to put it inside the square brackets of a character class (so you'll have two pair of square brackets). For example, `"a[[:digit:]]b"` matches `a0b`, `a1b` and so on.

## How to use RegEx patterns

Here you will see two kind of operators, `REGEXP` operators and POSIX operators. Just be aware that which operators you can use depends on the flavour of SQL you are using.

### RegEx operators

RegEx operators are usually case insensitive, meaning that they don't distinguish between uppercase and lowercase letters. So for them, `a` is equivalent to `A`. But you can change this default behaviour, so don't take it for granted.

| Operator | Description |
| -- | -- |
| `REGEXP` | Gives true if it matches the given pattern |
| `NOT REGEXP` | Gives true if the string doesn't contain the given pattern |

### Posix operators

The other kind of operators you could have available are POSIX operators. Instead of being keywords, these are represented with punctuation, and can be case sensitive or insensitive.

| operator | description |
| -- | -- |
| `~` | case sensitive, true if the pattern is contained in the string
| `!~` | case sensitive, true if the pattern is **not** contained in the string
| `~*` | case insensitive, true if the pattern is contained in the string
| `!~*` | case insensitive, true if the pattern is **not** contained in the string

### RegEx and Posix Examples

Let's see how to use these operators and RegEx patterns in a query.

#### Example query 1

For this first example, you want to match a string in which the first character is an "s" or "p" and the second character is a vowel. 

To do this, you can use the character class `[sp]` to match the first letter, and you can use the character class `[aeiou]` for the second letter in the string.

You also need to use the character to match the start of the string, `^`, so all together you'll write `"^[sp][aeiou]"`.

You write the query below to get back the list of users whose names match the pattern.

```sql
SELECT name FROM users
  WHERE name REGEXP '^[sp][aeiou]';
```

And if the default case insensitive behaviour was changed, you would need to write a pattern that allows both uppercase and lowercase letters, like `"^[spSP][aeiouAEIOU]"` and use it in the query as below:

```sql
SELECT name FROM users
  WHERE name REGEXP '^[spSP][aeiouAEIOU]';
```

Or with the POSIX operator, in this case you could use the case insensitive operator, `~*` and you would not need to write both upper case and lower case letters inside a character class. You could write the query as below.

```
SELECT name FROM users
  WHERE name ~* '^[sp][aeiou]';
```

As the operator is by definition case insensitive, you don't need to worry about specifying both uppercase and lowercase letters in the character class.

These queries would give back a table with results similar to below:

| name |
| -- |
| Sergio |
| PAUL |
| samantha |
| Seraphina |

#### Example query 2

As a second example, let's say you want to find a [hexadecimal color](https://www.freecodecamp.org/news/css-background-color-how-to-change-the-background-color-in-html/#hexadecimal-colors). You can use the POSIX class `[:xdigit:]` for this – it does the same as the character class `[0-9a-fA-F]`.

Writing `#[[:xdigit:]]{3}` or `#[[:xdigit:]]{6}` would match a hexadecimal color in its shorthand or longhand form: the first one would match colors like `#398` and the second one colors like `#00F5C4`.

You could combine them using character grouping and `|` to have one single RegEx pattern that matches both, and use it in the query as below:

```sql
SELECR color FROM styles
  WHERE color REGEXP '#([[:xdigit:]]{3}|[[:xdigit:]]{6})';
 
```

```sql
SELECR color FROM styles
  WHERE color ~ '#([[:xdigit:]]{3}|[[:xdigit:]]{6})';
```

This would give back something like below:

| color |
| --- |
| `#341` |
| `#00fa67 ` |
| `#FF00AB` |

The POSIX class `[:xdigit:]` already includes both uppercase and lowercase letters, so you would not need to worry about if the operator is case sensitive or not.

### Note on resource use

Depending on the size of your tables, a Contains String query can be really resource-intensive. Be careful when you're using them in production databases, as you don't want to have your app stop working.

# Conclusion

The Contains String queries are really useful. You have learned how to use them in this article, and you've seen a few examples. 

Hopefully you have added a new tool to your arsenal, and you enjoy using it! Just be careful not to crash your app.

