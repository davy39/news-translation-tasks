---
title: Format de date SQL Server et Convert SQL Server expliqués avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-19T23:04:00.000Z'
originalURL: https://freecodecamp.org/news/sql-date-format-and-sql-server-convert
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f2d740569d1a4ca4137.jpg
tags:
- name: SQL
  slug: sql
seo_title: Format de date SQL Server et Convert SQL Server expliqués avec des exemples
seo_desc: 'What does SQL Convert do?

  It converts from one data type to another data type.

  Syntax

  CONVERT (_New Data Type, Expression, Style_)


  New Data Type:  New data type to be converted too. For example: nvarchar, integer,
  decimal, date

  Expression:  Data to ...'
---

## Que fait SQL Convert ?

Il convertit d'un type de données à un autre type de données.

### Syntaxe

`CONVERT (_Nouveau Type de Données, Expression, Style_)`

* **Nouveau Type de Données :** Nouveau type de données à convertir. Par exemple : nvarchar, integer, decimal, date
* **Expression :** Données à convertir.
* **Style :** Format. Par exemple : Le style 110 est le format de date USA mm-dd-yyyy

### Exemple : Convertir un nombre décimal en un entier

`SELECT CONVERT(INT, 23.456) as IntegerNumber`

![convertir un nombre décimal en nombre entier](https://user-images.githubusercontent.com/12566249/31314884-6c94db4a-ac57-11e7-842f-710fad511131.png)

Remarque : Le résultat est tronqué.

### Exemple : Convertir une chaîne en une date

`SELECT CONVERT(DATE, '20161030') as Date`

![convertir une chaîne en un type de date](https://user-images.githubusercontent.com/12566249/31314912-c25bbb52-ac57-11e7-880d-6d81041b1728.png)

### Exemple : Convertir un décimal en une chaîne

`SELECT CONVERT(nvarchar, 20.123) as StringData`

![convertir un décimal en une chaîne](https://user-images.githubusercontent.com/12566249/31314923-fb04e410-ac57-11e7-9646-94061e1f0ec2.png)

### Exemple : Convertir un nombre entier en un nombre décimal

`SELECT CONVERT(DECIMAL (15,3), 13) as DecimalNumber`

![convertir un entier en un nombre décimal](https://user-images.githubusercontent.com/12566249/31314932-1c8668ca-ac58-11e7-8cee-4d57fc523704.png)

### Exemple : Convertir une chaîne en format de date USA

`SELECT CONVERT(DATE, '20171030' , 110) To_USA_DateFormat`

![convertir une chaîne en format de date USA](https://user-images.githubusercontent.com/12566249/31314937-35155d06-ac58-11e7-9d5d-823b66c41d0d.png)

###