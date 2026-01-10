---
title: Instruction SQL DELETE - Comment supprimer une ligne ou une table, expliqué
  avec des exemples de syntaxe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-09T21:38:00.000Z'
originalURL: https://freecodecamp.org/news/sql-delete-statement-row-table
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ed0740569d1a4ca3f52.jpg
tags:
- name: SQL
  slug: sql
seo_title: Instruction SQL DELETE - Comment supprimer une ligne ou une table, expliqué
  avec des exemples de syntaxe
seo_desc: 'To delete a record in a table you use the  DELETE  statement.

  Be careful. You can delete all records of the table or just a few. Use the  WHERE  condition
  to specify which records do you want to delete. The syntax is:

  DELETE FROM table_name

  WHERE con...'
---

Pour supprimer un enregistrement dans une table, vous utilisez l'instruction `DELETE`.

Soyez prudent. Vous pouvez supprimer tous les enregistrements de la table ou seulement quelques-uns. Utilisez la condition `WHERE` pour spécifier quels enregistrements vous souhaitez supprimer. La syntaxe est :

```
DELETE FROM nom_de_la_table
WHERE condition;
```

Voici un exemple de suppression dans la table Person de l'enregistrement avec l'Id 3 :

```
DELETE FROM Person
WHERE Id = 3;
```

Utilisation de DELETE pour supprimer tous les enregistrements d'une table donnée

```
DELETE * FROM Person
;
```

Ou, selon votre SGBDR, vous pourriez utiliser l'instruction TRUNCATE TABLE qui supprime tous les enregistrements d'une table et, selon votre SGBDR, peut ou non permettre un rollback. DELETE est du DML et TRUNCATE est du DDL.

```
TRUNCATE TABLE Person;
```