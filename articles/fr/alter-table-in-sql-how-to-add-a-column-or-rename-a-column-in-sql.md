---
title: Alter Table en SQL – Comment ajouter ou renommer une colonne en SQL
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-09T15:14:48.000Z'
originalURL: https://freecodecamp.org/news/alter-table-in-sql-how-to-add-a-column-or-rename-a-column-in-sql
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-quang-nguyen-vinh-2138126.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Alter Table en SQL – Comment ajouter ou renommer une colonne en SQL
seo_desc: 'You have created your database and your tables, and after all this work,
  you notice that you need to add or rename a column. Well, you can use the ALTER
  TABLE statement to do so.

  Just keep in mind that you need to be really careful when you do this. ...'
---

Vous avez créé votre base de données et vos tables, et après tout ce travail, vous remarquez que vous devez ajouter ou renommer une colonne. Eh bien, vous pouvez utiliser l'instruction `ALTER TABLE` pour ce faire.

Gardez simplement à l'esprit que vous devez être vraiment prudent lorsque vous faites cela. Si votre table contient beaucoup de lignes, cela peut causer des problèmes de performance pour votre base de données.

Note : Si la syntaxe présentée ici ne fonctionne pas, vérifiez dans la documentation pour l'implémentation de SQL que vous utilisez. La plupart des choses fonctionnent de la même manière, mais il existe quelques différences.

# Comment ajouter une nouvelle colonne avec `ALTER TABLE`

Pour ajouter une nouvelle colonne, vous devez d'abord sélectionner la table avec `ALTER TABLE table_name`, puis écrire le nom de la nouvelle colonne et son type de données avec `ADD column_name datatype`. Ensemble, le code ressemble à ceci :

```sql
ALTER TABLE table_name
ADD column_name datatype;
```

## Exemple d'utilisation de `ALTER TABLE` pour ajouter une nouvelle colonne

Nous avons une base de données d'utilisateurs comme suit :

| id | name | age | state | email |
| -- | -- | -- | -- | -- |
| 1 | Paul | 24 | Michigan | paul@example.com |
| 2 | Molly | 22 | New Jersey | molly@example.com |
| 3 | Robert | 19 | New York | robert@example.com |

Nous en sommes arrivés à un point où nous devons stocker le numéro de document d'identité de nos utilisateurs, nous devons donc ajouter une nouvelle colonne pour cela.

Pour ajouter une nouvelle colonne à notre table `users`, nous devons sélectionner la table avec `ALTER TABLE users` puis spécifier le nom de la nouvelle colonne et son type de données avec `ADD id_number TEXT`. Ensemble, cela ressemble à ceci :

```sql
ALTER TABLE users
ADD id_number TEXT;
```

La table avec une nouvelle colonne ressemblera à ceci :

| id | name | age | state | email | id_number |
| -- | -- | -- | -- | -- | -- |
| 1 | Paul | 24 | Michigan | paul@example.com | NULL |
| 2 | Molly | 22 | New Jersey | molly@example.com | NULL |
| 3 | Robert | 19 | New York | robert@example.com | NULL |

Vous devrez utiliser [une instruction `UPDATE`](https://www.freecodecamp.org/news/sql-update-statement-update-query-in-sql/) pour ajouter les informations manquantes pour les utilisateurs déjà existants une fois qu'elles sont fournies.

### Comment créer une nouvelle colonne avec une valeur par défaut au lieu de NULL

Vous pouvez également créer une colonne avec une valeur par défaut en utilisant le mot-clé `default` suivi de la valeur à utiliser. Les utilisateurs verront alors cette valeur par défaut au lieu d'avoir les valeurs manquantes remplies avec NULL.

Supposons que nous aurons bientôt des utilisateurs internationaux, et nous voulons ajouter une colonne `country`. Tous nos utilisateurs existants sont des États-Unis, nous pouvons donc utiliser cela comme valeur par défaut.

```sql
ALTER TABLE users
ADD country TEXT default "United States";
```

La table ressemblera alors à ceci :

| id | name | age | state | email | id_number | country |
| -- | -- | -- | -- | -- | -- | -- |
| 1 | Paul | 24 | Michigan | paul@example.com | NULL | United States |
| 2 | Molly | 22 | New Jersey | molly@example.com | NULL | United States |
| 3 | Robert | 19 | New York | robert@example.com | NULL | United States |

### Soyez prudent lors de l'ajout de nouvelles colonnes aux tables

Si votre table contient déjà beaucoup de lignes – comme si vous avez déjà beaucoup d'utilisateurs, ou beaucoup de données stockées – l'ajout d'une nouvelle colonne peut être vraiment intensif en ressources. Assurez-vous donc de gérer cette opération avec soin.

# Comment renommer une colonne avec `ALTER TABLE`

Vous pouvez renommer une colonne avec le code suivant. Vous sélectionnez la table avec `ALTER TABLE table_name` puis écrivez quelle colonne renommer et comment la renommer avec `RENAME COLUMN old_name TO new_name`.

```sql
ALTER TABLE table_name
RENAME COLUMN old_name TO new_name;
```

## Exemple de renommage d'une colonne

Regardons la même table que nous avons utilisée dans l'exemple précédent :

| id | name | age | state | email | id_number | country |
| -- | -- | -- | -- | -- | -- | -- |
| 1 | Paul | 24 | Michigan | paul@example.com | NULL | United States |
| 2 | Molly | 22 | New Jersey | molly@example.com | NULL | United States |
| 3 | Robert | 19 | New York | robert@example.com | NULL | United States |

Pour éviter la confusion entre les colonnes `id` et `id_number`, renommons la première en `user_id`.

Nous allons d'abord sélectionner la table avec `ALTER TABLE users` puis déclarer le nom de la colonne pour qu'il change en ce que nous voulons avec `RENAME COLUMN id TO user_id`.

```sql
ALTER TABLE users
RENAME COLUMN id TO user_id;
```

Après avoir utilisé la requête, la table ressemblera à ceci :

| user_id | name | age | state | email | id_number | country |
| -- | -- | -- | -- | -- | -- | -- |
| 1 | Paul | 24 | Michigan | paul@example.com | NULL | United States |
| 2 | Molly | 22 | New Jersey | molly@example.com | NULL | United States |
| 3 | Robert | 19 | New York | robert@example.com | NULL | United States |

### Soyez prudent lors du renommage d'une colonne dans une table

Lorsque vous renommez des colonnes en utilisant `ALTER TABLE`, vous risquez de rompre les dépendances de la base de données.

Si vous utilisez un outil de refactorisation de base de données pour changer le nom d'une colonne au lieu d'utiliser `ALTER TABLE`, il gérera toutes les dépendances et les mettra à jour avec le nouveau nom de colonne.

Si vous avez une petite base de données, vous n'avez peut-être pas à vous en soucier, mais il est important de garder cela à l'esprit.

# Conclusion

Dans cet article, vous avez appris comment utiliser `ALTER TABLE` pour ajouter une colonne et renommer une colonne dans une table.

Rappelez-vous simplement que les deux sont des opérations qui comportent leurs propres risques qu'il est important de connaître. Comme quelqu'un l'a dit, _avec un grand pouvoir viennent de grandes responsabilités_ – et `ALTER TABLE` est un grand pouvoir, alors utilisez-le avec précaution !