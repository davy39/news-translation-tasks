---
title: SQL Injection Expliqué avec des Exemples de Syntaxe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-09T22:35:00.000Z'
originalURL: https://freecodecamp.org/news/sql-injection-explained-with-syntax-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/Screen-Shot-2020-01-13-at-3.13.49-PM-1.png
tags:
- name: SQL
  slug: sql
seo_title: SQL Injection Expliqué avec des Exemples de Syntaxe
seo_desc: 'How SQL Injection Works

  SQL injection is a malicious technique that is meant to compromise or destroy databases.
  It is one of the most common web-hacking techniques.

  SQL injection is performed by placing malicious code in SQL statements via an input....'
---

## Comment fonctionne l'Injection SQL

L'injection SQL est une technique malveillante destinée à compromettre ou détruire des bases de données. C'est l'une des techniques de piratage web les plus courantes.

L'injection SQL est réalisée en plaçant du code malveillant dans des instructions SQL via une entrée.

Vous avez peut-être déjà entendu parler de l'Injection SQL. Elle est immortalisée dans cette célèbre bande dessinée XKCD :

L'exemple suivant est un extrait de code qui récupère un utilisateur d'une base de données en fonction d'un `AccountId`.

```
passedInAccountId = getRequestString("AccountId");
sql = "select * from Accounts where AccountId = " + passedInAccountId;
```

L'injection SQL peut être utilisée pour compromettre ce code en injectant une instruction `1=1;` pour `AccountId`.

`https://www.foo.com/get-user?AccountId="105 OR 1=1;"`

`1=1` s'évaluera toujours à `VRAI`. Cela provoquera l'exécution du code qui affichera l'intégralité de la table des comptes.

Bande dessinée : [https://imgs.xkcd.com/comics/exploits_of_a_mom.png](https://imgs.xkcd.com/comics/exploits_of_a_mom.png)