---
title: Insert Into SQL – Exemple de l'instruction SQL Insert
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-06T16:10:39.000Z'
originalURL: https://freecodecamp.org/news/insert-into-sql-sql-insert-statement-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-markus-spiske-177598.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Insert Into SQL – Exemple de l'instruction SQL Insert
seo_desc: 'If you''ve created an empty table in your database you''ll need to add
  records to it. In this article you will learn how you can add records to your tables
  using the INSERT statement in SQL.

  Keep in mind that if the syntax presented here doesn''t work, ...'
---

Si vous avez créé une table vide dans votre base de données, vous devrez y ajouter des enregistrements. Dans cet article, vous apprendrez comment ajouter des enregistrements à vos tables en utilisant l'instruction `INSERT` en SQL.

Gardez à l'esprit que si la syntaxe présentée ici ne fonctionne pas, vous pouvez vérifier dans la documentation de l'implémentation de SQL que vous utilisez. La plupart des choses fonctionnent de la même manière, mais il existe quelques différences.

# Syntaxe de l'instruction SQL `INSERT`

Une instruction `INSERT` spécifie dans quelle table vous souhaitez ajouter un enregistrement. Vous écrivez la commande `INSERT INTO table_name`, puis le mot-clé `VALUES` suivi des valeurs que vous souhaitez ajouter dans chaque colonne entre parenthèses et séparées par des virgules, comme ci-dessous :

```sql
INSERT INTO table_name
VALUES (value1, value2, value3...);
```

Les valeurs seront ajoutées aux colonnes dans l'ordre dans lequel les colonnes ont été définies dans la table.

## Comment donner une valeur aux colonnes sélectionnées

Supposons que vous souhaitiez donner une valeur à seulement quelques colonnes – par exemple, si vous souhaitez éviter de définir manuellement l'`id` pour qu'il soit fait automatiquement. Vous utiliseriez la syntaxe ci-dessous :

```sql
INSERT INTO table_name(column1, column2...)
VALUES (value1, value2...);
```

Les valeurs seront attribuées aux colonnes dans l'ordre dans lequel elles sont écrites entre parenthèses.

# Exemples de l'instruction SQL `INSERT`

Créons une table, puis nous utiliserons `INSERT` pour ajouter les premiers enregistrements.

Le code ci-dessous créera une table nommée `users` qui comporte 5 colonnes. Nous aurons une colonne `id` qui sera la `PRIMARY KEY` (la colonne qui aura toujours des valeurs uniques et nous permettra d'identifier de manière unique une ligne), puis les colonnes `name`, `age`, `state` et `email`.

```sql
CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,  age INTEGER, state TEXT, email TEXT);
```

Ajoutons le premier enregistrement à cette table en utilisant la première syntaxe que nous avons vue.

Nous ajouterons l'utilisateur `Paul` avec un `id` de `1`, un `age` de `24`, de l'état de `Michigan`, et avec une adresse email de `paul@example.com` en utilisant la requête ci-dessous :

```sql
INSERT INTO users
VALUES (1, "Paul", 24, "Michigan", "paul@example.com");
```

Cela rendra la table comme suit :

| id(PK) | name | age | state | email |
| --- | --- | --- | --- | --- |
| 1 | Paul | 24 | Michigan | paul@example.com |

Avec cette syntaxe, vous devez avoir une valeur pour chaque colonne, sinon cela générera une erreur et ne fonctionnera pas.

Maintenant, ajoutons quelques autres enregistrements, en utilisant le deuxième type de syntaxe vu ci-dessus.

```sql
INSERT INTO users (name, state)
VALUES ("Molly", "New Jersey");

INSERT INTO users (name, state, age)
VALUES ("Robert", "New York", 19);
```

Dans ce cas, la première valeur est attribuée à la première colonne mentionnée, donc `"Molly"` est attribué à la colonne `name`, et `"New Jersey"` à la colonne `state`. Ensuite, pour l'autre enregistrement, la colonne `name` reçoit la valeur `"Robert"`, la colonne `state` obtient `"New York"`, la colonne `age` est attribuée `19`.

Que se passe-t-il pour les colonnes auxquelles aucune valeur n'a été attribuée ? La colonne avec un type `INTEGER PRIMARY KEY AUTOINCREMENT` est mise à jour automatiquement, garantissant que chaque ligne a une valeur unique. Lorsque aucune valeur n'est spécifiée pour les autres colonnes, elles reçoivent une valeur `NULL`.

Maintenant, la table ressemble à ce qui suit. Notez que la colonne `id` a été mise à jour pour avoir des valeurs uniques dans chaque ligne, même si nous n'avons pas explicitement attribué de valeur. Les autres colonnes auxquelles aucune valeur n'a été attribuée ont une valeur `NULL`.

| id(PK) | name | age | state | email |
| --- | --- | --- | --- | --- |
| 1 | Paul | 24 | Michigan | paul@example.com |
| 2 | Molly | NULL | New Jersey | NULL |
| 3 | Robert | 19 | New York | NULL |

# Conclusion

Lorsque vous créez une table dans votre base de données, elle est vide. Cet article explique comment ajouter des enregistrements à une table, ce qui est un bon point de départ pour créer une base de données.