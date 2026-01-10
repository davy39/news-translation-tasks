---
title: SQL WHERE – Exemples de clause
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-04T15:32:26.000Z'
originalURL: https://freecodecamp.org/news/sql-where-clause-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-kindel-media-7054757.jpg
tags:
- name: crud
  slug: crud
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: SQL WHERE – Exemples de clause
seo_desc: 'Sometimes when you''re working with SQL, you don''t need to operate on
  an entire range of records. Or it would be really bad if you accidentally changed
  or deleted everything.

  In these cases, you''ll need to select only the part of the records on which ...'
---

Parfois, lorsque vous travaillez avec SQL, vous n'avez pas besoin d'opérer sur une plage complète d'enregistrements. Ou il serait vraiment mauvais si vous modifiiez ou supprimiez accidentellement tout.

Dans ces cas, vous devrez sélectionner uniquement la partie des enregistrements sur laquelle vous souhaitez travailler, ceux qui satisfont une certaine condition. C'est là que la clause `WHERE` de SQL est utile.

# Syntaxe de la clause `WHERE` en SQL

Vous écrivez la clause `WHERE` comme ceci :

```sql
SELECT column1, column2...
FROM table_name
WHERE condition;
```

Notez que ici, je l'ai écrite en utilisant l'instruction `SELECT`, mais son utilisation n'est pas limitée à `SELECT`. Vous pouvez également l'utiliser avec d'autres instructions comme `DELETE` et `UPDATE`.

# Clause `WHERE` en action

Utilisons cette table `users` comme exemple pour montrer comment utiliser la clause `WHERE`.

| id | name | age | state | email |
| -- | ---- | --- | ----- | ----- |
| 1 | Brian | 15 | Michigan | brian@example.com |
| 2 | Leonard | 55 | Mississippi | leonard@example.com |
| 3 | Anvil | 31 | South Dakota | anvil@example.com |
| 4 | Jo | 44 | Maine | jo@example.com |
| 5 | Meredith | 43 | Delaware | meredith@example.com |
| 6 | Cody | 16 | Michigan | cody@example.com |
| 7 | Dilara | 50 | Ohio | dilara@example.com |
| 8 | Corbin | 47 | Wisconsin | corbin@example.com |
| 9 | Gin | 63 | Illinois | gin@example.com |
| 10 | Alice | 50 | Nevada | alice@example.com |
| 11 | Zachary | 21 | Massachusetts | zachery@example.com |
| 12 | Delmar | 56 | Idaho | delmar@example.com |
| 13 | Dennie | 96 | Ohio | dennie@example.com |
| 14 | Aaron | 50 | Florida | aaron@example.com |
| 15 | Busrah | 18 | South Dakota | busrah@example.com |
| 16 | Aveline | 88 | Nevada | aveline@example.com |
| 17 | Aherin | 72 | Arkansas | aherin@example.com |
| 18 | Viola | 66 | Maine | viola@example.com |
| 19 | Nadya | 22 | Florida | nadya@example.com |
| 20 | Izabela | 61 | Arizona | izabela@example.com |

## Exemple de clause `WHERE` avec l'instruction `SELECT`

Lorsque vous voulez vous assurer qu'un certain événement affectera les personnes âgées de 50 ans ou plus, vous pouvez sélectionner uniquement ces utilisateurs avec le code suivant :

```sql
SELECT *
FROM users
WHERE age >= 50;
```

Cela donnera une table comme ci-dessous, qui ne liste que les utilisateurs âgés de 50 ans ou plus :

| id | name | age | state | email |
| -- | ---- | --- | ----- | ----- |
| 2 | Leonard | 55 | Mississippi | leonard@example.com |
| 7 | Dilara | 50 | Ohio | dilara@example.com |
| 9 | Gin | 63 | Illinois | gin@example.com |
| 10 | Alice | 50 | Nevada | alice@example.com |
| 12 | Delmar | 56 | Idaho | delmar@example.com |
| 13 | Dennie | 96 | Ohio | dennie@example.com |
| 14 | Aaron | 50 | Florida | aaron@example.com |
| 16 | Aveline | 88 | Nevada | aveline@example.com |
| 17 | Aherin | 72 | Arkansas | aherin@example.com |
| 18 | Viola | 66 | Maine | viola@example.com |
| 20 | Izabela | 61 | Arizona | izabela@example.com |

## Exemple de clause `WHERE` avec l'instruction `DELETE`

Disons que Cody a décidé de se retirer de cette liste. Vous pouvez mettre à jour la table en utilisant une instruction `DELETE` avec `WHERE` pour vous assurer que seul l'enregistrement de Cody est supprimé.

```sql
DELETE FROM users
WHERE name IS "Cody";
```

La table `users` ressemblera maintenant à ceci, sans la ligne 6 (où se trouvaient les informations de Cody) :

| id | name | age | state | email |
| -- | ---- | --- | ----- | ----- |
| 1 | Brian | 15 | Michigan | brian@example.com |
| 2 | Leonard | 55 | Mississippi | leonard@example.com |
| 3 | Anvil | 31 | South Dakota | anvil@example.com |
| 4 | Jo | 44 | Maine | jo@example.com |
| 5 | Meredith | 43 | Delaware | meredith@example.com |
| 7 | Dilara | 50 | Ohio | dilara@example.com |
| 8 | Corbin | 47 | Wisconsin | corbin@example.com |
| 9 | Gin | 63 | Illinois | gin@example.com |
| 10 | Alice | 50 | Nevada | alice@example.com |
| 11 | Zachary | 21 | Massachusetts | zachery@example.com |
| 12 | Delmar | 56 | Idaho | delmar@example.com |
| 13 | Dennie | 96 | Ohio | dennie@example.com |
| 14 | Aaron | 50 | Florida | aaron@example.com |
| 15 | Busrah | 18 | South Dakota | busrah@example.com |
| 16 | Aveline | 88 | Nevada | aveline@example.com |
| 17 | Aherin | 72 | Arkansas | aherin@example.com |
| 18 | Viola | 66 | Maine | viola@example.com |
| 19 | Nadya | 22 | Florida | nadya@example.com |
| 20 | Izabela | 61 | Arizona | izabela@example.com |

## Exemple de clause `WHERE` avec l'instruction `UPDATE`

Maintenant, peut-être avez-vous reçu un avis indiquant qu'Anvil a vieilli et a maintenant 32 ans. Vous pouvez modifier l'enregistrement d'Anvil en utilisant l'instruction `UPDATE`, et vous pouvez utiliser `WHERE` pour vous assurer que seul l'enregistrement d'Anvil est mis à jour.

```sql
UPDATE users
SET age = 32
WHERE name IS "Anvil";
```

Maintenant, la table ressemblera à ceci :

| id | name | age | state | email |
| -- | ---- | --- | ----- | ----- |
| 1 | Brian | 15 | Michigan | brian@example.com |
| 2 | Leonard | 55 | Mississippi | leonard@example.com |
| 3 | Anvil | 32 | South Dakota | anvil@example.com |
| 4 | Jo | 44 | Maine | jo@example.com |
| 5 | Meredith | 43 | Delaware | meredith@example.com |
| 7 | Dilara | 50 | Ohio | dilara@example.com |
| 8 | Corbin | 47 | Wisconsin | corbin@example.com |
| 9 | Gin | 63 | Illinois | gin@example.com |
| 10 | Alice | 50 | Nevada | alice@example.com |
| 11 | Zachary | 21 | Massachusetts | zachery@example.com |
| 12 | Delmar | 56 | Idaho | delmar@example.com |
| 13 | Dennie | 96 | Ohio | dennie@example.com |
| 14 | Aaron | 50 | Florida | aaron@example.com |
| 15 | Busrah | 18 | South Dakota | busrah@example.com |
| 16 | Aveline | 88 | Nevada | aveline@example.com |
| 17 | Aherin | 72 | Arkansas | aherin@example.com |
| 18 | Viola | 66 | Maine | viola@example.com |
| 19 | Nadya | 22 | Florida | nadya@example.com |
| 20 | Izabela | 61 | Arizona | izabela@example.com |

# Opérateurs que vous pouvez utiliser avec une clause `WHERE` pour sélectionner des enregistrements

Vous pouvez utiliser des opérateurs comme `=`, `>`, `<`, `>=`, `<=`, `<>` (ou `!=` selon votre version SQL), `BETWEEN`, `LIKE`, `IN`.

Nous avons déjà vu `>=`, "supérieur ou égal à", en action dans les exemples ci-dessus.

`=` signifie "égal à", `>` signifie "supérieur à", `<` signifie "inférieur à", `<=` signifie "inférieur ou égal à", `<>` (ou `!=`) signifie "différent de".

Les quatre opérateurs, *supérieur à*, *inférieur à*, *supérieur ou égal à*, et *inférieur ou égal à*, sont principalement utiles lorsque l'on traite avec des nombres.

Les deux opérateurs, *égal à*, et *différent de*, sont utiles à la fois avec des nombres et d'autres types de données.

## Comment utiliser l'opérateur `BETWEEN` en SQL

`BETWEEN` vous permet de spécifier une plage de nombres. Par exemple, `WHERE age BETWEEN 24 and 51` sélectionnera tous les enregistrements dans cette plage d'âge.

```sql
SELECT * FROM users
WHERE age BETWEEN 24 AND 51;
```

Il y a 7 utilisateurs dont l'âge se situe dans cette plage :

| id | name | age | state | email |
| ---- | ---- | ---- | ---- | ---- |
| 3 | Anvil | 32 | South Dakota | anvil@example.com |
| 4 | Jo | 44 | Maine | jo@example.com |
| 5 | Meredith | 43 | Delaware | meredith@example.com |
| 7 | Dilara | 50 | Ohio | dilara@example.com |
| 8 | Corbin | 47 | WIsconsin | corbin@example.com |
| 10 | Alice | 50 | Nevada | alice@example.com |
| 14 | Aaron | 50 | Florida | aaron@example.com |

## Comment utiliser l'opérateur `LIKE` en SQL

`LIKE` vous permet de spécifier un motif. Par exemple, `WHERE name LIKE "A%"` sélectionnera tous les enregistrements où le nom commence par un A.

```sql
SELECT * FROM users
WHERE name LIKE "A%";
```

Il y a 5 utilisateurs dont le nom commence par A dans notre liste :

| id | name | age | state | email |
| -- | -- | -- | -- | -- |
| 3 | Anvil | 32 |South Dakota | anvil@example.com |
| 10 | Alice | 50 | Nevada | alice@example.com |
| 14 | Aaron | 50 | Florida | aaron@example.com |
| 16 | Aveline | 88 | Nevada | aveline@example.com |
| 17 | Aherin | 72 | Arkansas | aherin@example.com |

### Comment créer un motif à utiliser avec `LIKE`

Vous pouvez créer un motif en utilisant les caractères `%` et `_`. Le caractère `%` représente un nombre quelconque de caractères (zéro, un ou plusieurs). Le caractère `_` représente exactement un caractère.

Par exemple, `"_ook"` pourrait être "book", "look", "nook". Mais `"%ook"` pourrait aussi être "ook" ou "phonebook".

## Comment utiliser l'opérateur `IN` en SQL

`IN` vous permet de choisir parmi une liste de possibilités. Par exemple, voyons quels utilisateurs se trouvent sur la côte Est.

```sql
SELECT * FROM users
WHERE state IN ("Maine", "New Hampshire", "Massachusetts", "Rhode Island", "Connecticut", "New York", "New Jersey", "Delaware", "Maryland", "Virginia", "North Carolina", "South Carolina", "Georgia", "Florida");
```

L'opérateur `IN` vérifie si la valeur dans la colonne `state` est égale à l'une des valeurs de la liste des États de la côte Est.

Seuls six des utilisateurs vivent sur la côte Est :

| id | name | age | state | email |
| -- | ---- | --- | ----- | ----- |
| 4 | Jo | 44 | Maine | jo@example.com |
| 5 | Meredith | 43 | Delaware | meredith@example.com |
| 11 | Zachery | 21 | Massachusetts | zachery@example.com |
| 14 | Aaron | 50 | Florida | aaron@example.com |
| 18 | Viola | 66 | Maine | viola@example.com |
| 19 | Nadya | 22 | Florida | nadya@example.com |

## N'oublions pas les opérateurs `IS`, `NOT`, `AND`, `OR`

Nous avons déjà utilisé l'opérateur `IS` dans l'un de nos exemples ci-dessus. Comme `WHERE name IS "Cody"`, il vérifie si une colonne a cette valeur exacte.

Vous pouvez utiliser `NOT` devant une condition pour la rendre opposée. Par exemple, `WHERE age NOT BETWEEN 24 AND 51` sélectionnerait uniquement les utilisateurs de moins de 24 ans et de plus de 51 ans. En utilisant ce critère, 12 utilisateurs sont sélectionnés :

| id | name | age | state | email |
| -- | ---- | --- | ----- | ----- |
| 1 | Brian | 15 | Michigan | brian@example.com |
| 2 | Leonard | 55 | Mississippi | leonard@example.com |
| 9 | Gin | 63 | Illinois | gin@example.com |
| 11 | Zachary | 21 | Massachusetts | zachery@example.com |
| 12 | Delmar | 56 | Idaho | delmar@example.com |
| 13 | Dennie | 96 | Ohio | dennie@example.com |
| 15 | Busrah | 18 | South Dakota | busrah@example.com |
| 16 | Aveline | 88 | Nevada | aveline@example.com |
| 17 | Aherin | 72 | Arkansas | aherin@example.com |
| 18 | Viola | 66 | Maine | viola@example.com |
| 19 | Nadya | 22 | Florida | nadya@example.com |
| 20 | Izabela | 61 | Arizona | izabela@example.com |

Vous utilisez `AND` pour combiner des conditions de sorte que les deux doivent être vraies, par exemple `WHERE name LIKE "A%" AND age > 70` sélectionnerait les utilisateurs dont le nom commence par A **et** qui ont plus de 70 ans. Seuls 2 utilisateurs satisfont ce critère :

| id | name | age | state | email |
| -- | -- | -- | -- | -- |
| 16 | Aveline | 88 | Nevada | aveline@example.com |
| 17 | Aherin | 72 | Arkansas | aherin@example.com |

Vous pouvez utiliser `OR` pour combiner des conditions de sorte que seule l'une des deux doit être vraie. Par exemple, `WHERE name LIKE "A%" OR age > 70` sélectionnerait les utilisateurs dont le nom commence par A **ou** qui ont plus de 70 ans (seule l'une des deux parties doit être vraie, mais les deux peuvent aussi être vraies).

Il y a 6 utilisateurs dont le nom commence par A ou qui ont plus de 70 ans (ou les deux).

| id | name | age | state | email |
| -- | -- | -- | -- | -- |
| 3 | Anvil | 32 |South Dakota | anvil@example.com |
| 10 | Alice | 50 | Nevada | alice@example.com |
| 13 | Dennie | 96 | Ohio | dennie@example.com |
| 14 | Aaron | 50 | Florida | aaron@example.com |
| 16 | Aveline | 88 | Nevada | aveline@example.com |
| 17 | Aherin | 72 | Arkansas | aherin@example.com |

# Conclusion

Il est vraiment important de spécifier sur quels enregistrements vous souhaitez opérer dans vos tables.

Avec cet article, vous avez appris comment le faire en utilisant la clause `WHERE`.

Merci d'avoir lu !