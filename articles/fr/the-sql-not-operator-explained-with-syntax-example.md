---
title: L'opérateur SQL NOT expliqué avec un exemple de syntaxe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-30T21:25:00.000Z'
originalURL: https://freecodecamp.org/news/the-sql-not-operator-explained-with-syntax-example
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9fbc740569d1a4ca4439.jpg
tags:
- name: SQL
  slug: sql
seo_title: L'opérateur SQL NOT expliqué avec un exemple de syntaxe
seo_desc: 'You can use the  NOT  operator in the  WHERE  clause of  SELECT  statement.
  You use it when you want to select a condition that is not true.

  Here is a code example that selects all persons that are not male:

  SELECT Id, Name, DateOfBirth, Gender

  FROM ...'
---

Vous pouvez utiliser l'opérateur `NOT` dans la clause `WHERE` d'une instruction `SELECT`. Vous l'utilisez lorsque vous souhaitez sélectionner une condition qui n'est pas vraie.

Voici un exemple de code qui sélectionne toutes les personnes qui ne sont pas de sexe masculin :

```
SELECT Id, Name, DateOfBirth, Gender
FROM Person
WHERE NOT Gender = "M"

```