---
title: SQL Injection Explained with Syntax Examples
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
seo_title: null
seo_desc: 'How SQL Injection Works

  SQL injection is a malicious technique that is meant to compromise or destroy databases.
  It is one of the most common web-hacking techniques.

  SQL injection is performed by placing malicious code in SQL statements via an input....'
---

## How SQL Injection Works

SQL injection is a malicious technique that is meant to compromise or destroy databases. It is one of the most common web-hacking techniques.

SQL injection is performed by placing malicious code in SQL statements via an input.

You may have heard of SQL Injection before. It is immortalized in this famous XKCD comic:

The following example is a code snippet that will retrieve a user from a database based on an  `AccountId` .

```
passedInAccountId = getRequestString("AccountId");
sql = "select * from Accounts where AccountId = " + passedInAccountId;

```

SQL injection can be used to compromise this code by injecting a  `1=1;`  statement for  `AccountId` .

`https://www.foo.com/get-user?AccountId="105 OR 1=1;"`

`1=1`  will always evaluate to  `TRUE` . This will cause the executed code to output all of the Accounts table.

Comic: [https://imgs.xkcd.com/comics/exploits_of_a_mom.png](https://imgs.xkcd.com/comics/exploits_of_a_mom.png)

