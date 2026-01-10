---
title: Instruction SQL UPDATE – Requête de mise à jour en SQL
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-06T21:25:14.000Z'
originalURL: https://freecodecamp.org/news/sql-update-statement-update-query-in-sql
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-thirdman-5961549.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Instruction SQL UPDATE – Requête de mise à jour en SQL
seo_desc: "Once you have created a table in a database, it will rarely need to stay\
  \ the same forever. You will likely need to modify the records in it. \nAnd to help\
  \ you do that, there is a useful statement, aptly named UPDATE, that you can use\
  \ to change the rec..."
---

Une fois que vous avez créé une table dans une base de données, elle n'aura rarement besoin de rester la même pour toujours. Vous devrez probablement modifier les enregistrements qu'elle contient.

Et pour vous aider à le faire, il existe une instruction utile, appelée à juste titre `UPDATE`, que vous pouvez utiliser pour modifier les enregistrements selon vos besoins.

Note : Si la syntaxe présentée ici ne fonctionne pas, consultez la documentation pour l'implémentation de SQL que vous utilisez. La plupart des choses fonctionnent de la même manière, mais il existe quelques différences.

# Syntaxe SQL UPDATE

Pour utiliser la méthode `UPDATE`, vous déterminez d'abord quelle table vous devez mettre à jour avec `UPDATE table_name`. Ensuite, vous écrivez le type de changement que vous souhaitez apporter à l'enregistrement avec l'instruction `SET`. Enfin, vous utilisez [une clause `WHERE`](https://www.freecodecamp.org/news/sql-where-clause-examples/) pour sélectionner les enregistrements à modifier.

**Il est vraiment important d'utiliser cette clause `WHERE`**, sinon vous allez apporter la même modification à toute la table.

```sql
UPDATE table_name
SET changement à apporter
WHERE clause pour sélectionner les enregistrements à modifier;
```

# Exemple SQL UPDATE

Nous avons une table nommée `users` qui ressemble à ceci :

| id(PK) | name | age | state | email |
| --- | --- | --- | --- | --- |
| 1 | Paul | 24 | Michigan | paul@example.com |
| 2 | Molly | NULL | New Jersey | NULL |
| 3 | Robert | 19 | New York | NULL |

Il y a quelques enregistrements incomplets dans cette table. Lorsque les utilisateurs nous fournissent les informations manquantes, nous pouvons les ajouter en utilisant des instructions `UPDATE`.

L'utilisateur Robert manque d'une adresse email. Toutes les lignes sélectionnées par la clause `WHERE` seront mises à jour, donc nous devons être prudents : nous pourrions sélectionner l'enregistrement à mettre à jour en utilisant la colonne name, mais les noms ne sont pas uniques – nous pourrions avoir plusieurs Roberts dans notre table.

La meilleure façon de sélectionner une ligne à mettre à jour (pour vous assurer de ne mettre à jour que la ligne que vous souhaitez) est d'utiliser la colonne `PRIMARY KEY` dans laquelle les valeurs sont toujours uniques. Dans ce cas, il s'agit de la colonne nommée `id`.

Donc, mettons à jour l'adresse email en utilisant cette requête :

```sql
UPDATE users
SET email="robert@example.com"
WHERE id=3;
```

Maintenant, la table ressemblera à ceci :

| id(PK) | name | age | state | email |
| --- | --- | --- | --- | --- |
| 1 | Paul | 24 | Michigan | paul@example.com |
| 2 | Molly | NULL | New Jersey | NULL |
| 3 | Robert | 19 | New York | robert@example.com |

## Comment mettre à jour plusieurs colonnes en même temps

Molly manque de valeurs dans deux colonnes différentes. Nous pouvons utiliser une seule instruction `UPDATE`, en séparant les affectations par des virgules, comme ceci :

```sql
UPDATE users
SET age=22, email="molly@example.com"
WHERE id=2;
```

La table ressemblera maintenant à ceci :

| id(PK) | name | age | state | email |
| --- | --- | --- | --- | --- |
| 1 | Paul | 24 | Michigan | paul@example.com |
| 2 | Molly | 22 | New Jersey | molly@example.com |
| 3 | Robert | 19 | New York | robert@example.com |

# Assurez-vous de ne modifier que les enregistrements que vous souhaitez modifier

Ceci est une préoccupation de sécurité. Nos exemples n'ont que quelques lignes, mais dans une situation réelle, cela pourrait être la base de données d'une application ou d'un site web avec des centaines, des milliers, voire des millions d'utilisateurs. Et vous ne voulez pas causer des problèmes à autant de personnes.

Donc, avant d'exécuter une requête `UPDATE`, envoyez une requête `SELECT` avec la même clause `WHERE`. Si elle retourne l'enregistrement que vous souhaitez mettre à jour, allez-y. Sinon, vous devez modifier la clause `WHERE`.

Par exemple, avant d'envoyer la mise à jour pour l'utilisateur Molly, nous aurions pu envoyer une instruction `SELECT` pour vérifier que la clause que nous avons utilisée, `WHERE id=2`, est la bonne :

```sql
SELECT * FROM users
WHERE id=2;
```

Cette requête retourne l'enregistrement ci-dessous, donc vous pouvez procéder avec la requête `UPDATE` pour compléter les données.

| id(PK) | name | age | state | email |
| --- | --- | --- | --- | --- |
| 2 | Molly | NULL | New Jersey | NULL |

# Conclusion

Une fois que vous avez créé vos tables et ajouté des enregistrements, il y aura toujours des moments où vous devrez mettre à jour une ligne. Cet article a expliqué comment faire cela en utilisant l'instruction SQL `UPDATE`.

Merci d'avoir lu !