---
title: Comment utiliser Join et String_agg dans Microsoft SQL Server
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-22T13:49:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-join-and-string-agg-in-microsoft-sql-server
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/Untitled-design.png
tags:
- name: database
  slug: database
- name: Microsoft
  slug: microsoft
- name: SQL
  slug: sql
seo_title: Comment utiliser Join et String_agg dans Microsoft SQL Server
seo_desc: 'By Thanoshan MV

  In this article, we’ll look at how to use join on more than two tables and aggregate
  the result using the function STRING_AGG() in Microsoft SQL Server.

  If you don’t know about Microsoft SQL Server, I’ll briefly explain to you what it...'
---

Par Thanoshan MV

Dans cet article, nous allons voir comment utiliser join sur plus de deux tables et agréger le résultat en utilisant la fonction `STRING_AGG()` dans Microsoft SQL Server.

Si vous ne connaissez pas Microsoft SQL Server, je vais vous expliquer brièvement ce que c'est 😃. Commençons.

## Qu'est-ce que Microsoft SQL Server ?

Microsoft SQL Server est un système de gestion de base de données relationnelle qui a révolutionné la manière dont les entreprises gèrent les données. Il vous aide à stocker et à gérer des données.

Si vous êtes familier avec d'autres systèmes de gestion de bases de données relationnelles tels que MySQL ou PostgreSQL, alors l'apprentissage de Microsoft SQL Server devrait être assez facile.

Je travaille sur l'[instance par défaut du serveur SQL](https://docs.microsoft.com/en-us/sql/relational-databases/lesson-1-connecting-to-the-database-engine?view=sql-server-ver15#connect).

Maintenant, considérons un problème.

### Le problème : comment obtenir les détails des employés et des projets

Supposons que nous avons trois tables, à savoir `Employee`, `Project` et `EmployeeProject`. L'image ci-dessous est la conception de la base de données relationnelle :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/msssql--1-.png)
_Figure 1 : Conception de la base de données relationnelle pour le problème_

Le problème est d'obtenir tous les détails des employés et leurs projets correspondants.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Employee-1.png)
_Figure 2 : Table Employee_

![Image](https://www.freecodecamp.org/news/content/images/2021/03/EmployeeProject-1.png)
_Figure 3 : Table EmployeeProject_

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Project1.png)
_Figure 4 : Table Project_

Points à considérer : tous les employés de la table `Employee` ne sont pas mappés avec la table `EmployeeProject` et tous les projets de la table `Project` ne sont pas mappés avec la table `EmployeeProject`.

Notre objectif principal est de récupérer tous les détails des employés de la table `Employee`, qu'ils soient mappés avec `EmployeeProject` ou non.

Nous pouvons essayer de résoudre ce problème en utilisant des jointures. Comme vous pouvez le voir, nous devons joindre trois tables pour résoudre ce problème. Tout d'abord, nous devons joindre les tables `Employee` et `EmployeeProject`. Ensuite, nous joindrons la table résultante avec `Project`.

Passons en revue quelques scénarios pour résoudre ce problème.

### Solution #1 : Utiliser Inner Join

Utilisons `INNER JOIN` partout !

```sql
SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId 
FROM Employee AS e INNER JOIN EmployeeProject AS ep 
ON e.Id = ep.EmployeeId
```

Cela nous donnera :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/innerjoin1.png)
_Figure 5_

Considérons la table ci-dessus comme `Employee-EmployeeProject`. Elle contient tous les détails des employés ainsi que leurs identifiants de projet correspondants.

Avec l'aide de `Employee-EmployeeProject`, nous pourrons accéder à la table `Project`. Faisons cela :

```sql
SELECT abc.FirstName, abc.LastName, abc.City, abc.Designation, p.Name AS Project FROM Project AS p 
INNER JOIN
(SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId
FROM Employee AS e INNER JOIN EmployeeProject AS ep
ON e.Id = ep.EmployeeId) AS abc 
ON p.Id = abc.ProjectId
```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/innerjoin2.png)
_Figure 6_

Super ! 😃 Maintenant, nous sommes capables de récupérer les détails des employés ainsi que leurs projets correspondants. Mais notre objectif principal est manquant (c'est-à-dire, obtenir tous les détails des employés) car nous manquons les détails de Sophia Ashley.

Le scénario 1 a fonctionné, mais nous n'avons pas accompli notre objectif. 😶

### Solution #2 : Utiliser Left Join

Obtenons tous les détails des employés, qu'ils soient mappés avec `EmployeeProject` ou non (notre objectif) en utilisant `LEFT JOIN` avec la table `Employee` :

```sql
SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId
```

Cette requête nous donnera :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/leftjoin-emp-empProj-.png)
_Figure 7_

Comme vous pouvez le voir sur la figure ci-dessus, nous sommes capables de récupérer les détails de Sophia Ashley puisque nous utilisons `LEFT JOIN` sur la table `Employee` avec la table `EmployeeProject`.

Considérons la table ci-dessus comme `Employee-EmployeeProject`. Elle contient tous les détails des employés ainsi que leurs identifiants de projet correspondants (y compris `NULL` lorsqu'il n'y a pas de valeur `ProjectId`).

Similaire au scénario 1, nous pouvons maintenant accéder aux noms des projets puisque nous connaissons `ProjectId`. N'oubliez pas, notre objectif est de récupérer tous les détails des employés, qu'ils aient un projet ou non.

Pour nous en assurer, nous devrons récupérer toutes les valeurs de `Employee-EmployeeProject` lors de la jointure avec la table `Project` :

```sql
SELECT abc.FirstName, abc.LastName, abc.City, abc.Designation, p.Name AS Project FROM Project AS p RIGHT JOIN (SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId) AS abc ON p.Id = abc.ProjectId
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Figure-6.png)
_Figure 8_

Super travail ! Nous avons atteint notre objectif. 😃

C'est du bon travail. Mais ce serait encore mieux si nous pouvions regrouper ces lignes et retourner une ligne par employé. C'est notre nouveau souhait ! 😉

Cela nous amène à nous demander comment nous pouvons regrouper ces résultats. Nous pouvons regrouper ces lignes en utilisant `GROUP BY`.

Donc, nous allons `GROUP BY` les résultats des lignes par `FirstName` :

```sql
SELECT abc.FirstName, abc.LastName, abc.City, abc.Designation, p.Name AS Project FROM Project AS p RIGHT JOIN (SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId) AS abc ON p.Id = abc.ProjectId GROUP BY abc.FirstName
```

Et la sortie est :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/groupby-error.png)
_Figure 9_

Qu'est-il arrivé ?

Il dit que la colonne `LastName` est invalide dans la liste de sélection car elle n'est **pas contenue** dans une **fonction d'agrégation** ou la **clause GROUP BY**. Cette erreur est applicable à toutes les colonnes restantes dans la liste sélectionnée sauf `FirstName`.

Lorsque nous essayons de sélectionner les valeurs de `FirstName` et de regrouper par `FirstName`, cela signifie que nous allons regrouper toutes les lignes en fonction de `FirstName` uniquement et sélectionner la colonne `FirstName`. Par exemple, sélectionnons uniquement `FirstName` et regroupons par `FirstName` :

```sql
SELECT abc.FirstName FROM Project AS p RIGHT JOIN 
(SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId) AS abc ON p.Id = abc.ProjectId GROUP BY abc.FirstName
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/groupbyfirstname.png)
_Figure 10_

Comme vous pouvez le voir dans la figure 10, nous avons regroupé toutes les lignes par `FirstName`. Ici, il n'y a pas d'ambiguïté.

Maintenant, sélectionnons `FirstName`, `LastName`, et regroupons toutes les lignes par `FirstName` :

```sql
SELECT abc.FirstName, abc.LastName FROM Project AS p RIGHT JOIN (SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId) AS abc ON p.Id = abc.ProjectId GROUP BY abc.FirstName
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/groupby-error1.png)
_Figure 11_

Si nous vérifions quelles sont les valeurs de `LastName` dans la Figure 8, nous pouvons voir que nous avons deux employés avec le même `FirstName` mais différents `LastName` : James Johnson et James Smith.

Donc, lorsque nous essayons de regrouper toutes les lignes par `FirstName` et de sélectionner les valeurs de `FirstName` et `LastName`, **cela nous conduit à un état d'ambiguïté.**

Imaginez que MSSQL nous demande : « Vous sélectionnez `FirstName`, `LastName` et vous essayez de regrouper toutes les lignes par `FirstName`. Mais le `FirstName` James a deux `LastName` différents, Johnson et Smith. En sélectionnant le nom de famille de James, quel devrait être son `LastName` ? Johnson ? Smith ? ou les deux ? » Il y a une ambiguïté dans MSSQL concernant lequel sélectionner.

Pour résoudre ce problème de FirstName et LastName, nous pouvons soit (option 1) regrouper toutes les lignes par `FirstName` et `LastName`, soit (option 2) enfermer `LastName` dans une [fonction d'agrégation](https://docs.microsoft.com/en-us/sql/t-sql/functions/aggregate-functions-transact-sql?view=sql-server-ver15#:~:text=An%20aggregate%20function%20performs%20a,All%20aggregate%20functions%20are%20deterministic.) pour sélectionner une seule valeur.

Option 1 :

```sql
SELECT abc.FirstName, abc.LastName FROM Project AS p RIGHT JOIN (SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId) AS abc ON p.Id = abc.ProjectId GROUP BY abc.FirstName, abc.LastName
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/option1.png)
_Figure 12_

Option 2 :

```sql
SELECT abc.FirstName, MAX(abc.LastName) AS LastName FROM Project AS p RIGHT JOIN (SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId) AS abc ON p.Id = abc.ProjectId GROUP BY abc.FirstName
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Figure-11.png)
_Figure 13_

Dans le problème de FirstName et LastName ci-dessus, bien que les deux options fonctionnent, l'option 1 a plus de sens que l'option 2.

Pour plus d'informations détaillées sur l'ambiguïté, consultez cette [question et réponse de stack overflow](https://stackoverflow.com/questions/13999817/reason-for-column-is-invalid-in-the-select-list-because-it-is-not-contained-in-e) !

**NOTE :** lorsque vous avez une requête `GROUP BY`, la liste sélectionnée doit faire partie soit des critères de regroupement, soit doit apparaître dans des fonctions d'agrégation telles que `SUM`, `MAX`, `COUNT`, etc.

Revenons à notre souhait, nous allons essayer de `GROUP BY` toutes les lignes par toutes les colonnes :

```sql
SELECT abc.FirstName, abc.LastName, abc.City, abc.Designation, p.Name AS Project FROM Project AS p RIGHT JOIN (SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId) AS abc ON p.Id = abc.ProjectId GROUP BY abc.FirstName, abc.LastName, abc.City, abc.Designation, p.Name
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Figure-12.png)
_Figure 14_

Nous avons réussi à regrouper toutes les lignes mais nous n'avons pas pu récupérer une ligne par employé, car chaque ligne est distincte des autres si nous considérons toutes les colonnes. Cela signifie que les regrouper par toutes les colonnes ne fonctionnera pas.

Selon notre nouvel objectif, nous avons besoin d'enregistrements pour Emma Cooper, James Johnson, James Smith, Maria Garcia et Sophia Ashley (cinq lignes).

`GROUP BY` `FirstName`, `LastName`, `City` et `Designation` nous donnera ces cinq lignes, mais qu'en est-il de `Project` ? Nous ne pouvons pas `GROUP BY` (si nous le faisons, le résultat serait similaire à la figure 14), mais nous pouvons utiliser une fonction d'agrégation (en additionnant) pour agréger `Project`.

En fait, nous pouvons utiliser la fonction d'agrégation `[STRING_AGG()](https://docs.microsoft.com/en-us/sql/t-sql/functions/string-agg-transact-sql?view=sql-server-ver15#syntax)` de MSSQL pour retourner une ligne par employé en concaténant la colonne `Name` dans la table `Project` et `GROUP BY` les colonnes restantes :

```sql
SELECT abc.FirstName, abc.LastName, abc.Designation, STRING_AGG (p.Name, ',') WITHIN GROUP (ORDER BY p.Name) AS Project FROM Project AS p RIGHT JOIN (SELECT e.Id, e.FirstName, e.LastName, e.Designation, e.City, ep.ProjectId FROM Employee AS e LEFT JOIN EmployeeProject AS ep ON e.Id = ep.EmployeeId) AS abc ON p.Id = abc.ProjectId GROUP BY abc.FirstName, abc.LastName, abc.City, abc.Designation
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Figure-13.png)
_Figure 15_

Hourra ! Nous l'avons fait. 😃 😃

Le problème que nous avons discuté dans cet article nous a aidé à comprendre certains des principaux concepts derrière Microsoft SQL Server.

Maintenant, nous avons une compréhension de base de la façon d'utiliser join et `STRING_AGG` dans Microsoft SQL Server.

N'hésitez pas à me faire savoir si vous avez des suggestions ou des questions.

Photo par [MI PHAM](https://unsplash.com/@phammi?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/s/photos/happy?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).

Connectez-vous avec moi sur [Medium](https://mvthanoshan.medium.com/).

**Veuillez soutenir freeCodeCamp dans leur [Campagne de promesse de programme de science des données](https://www.freecodecamp.org/news/building-a-data-science-curriculum-with-advanced-math-and-machine-learning/).**

Merci 😇

**Bon codage ❤️**

### Pour explorer plus loin

1. `[STRING_AGG](https://docs.microsoft.com/en-us/sql/t-sql/functions/string-agg-transact-sql?view=sql-server-ver15)` [(Transact-SQL) – Microsoft Docs](https://docs.microsoft.com/en-us/sql/t-sql/functions/string-agg-transact-sql?view=sql-server-ver15)
2. [Fonctions d'agrégation – Microsoft Docs](https://docs.microsoft.com/en-us/sql/t-sql/functions/aggregate-functions-transact-sql?view=sql-server-ver15)
3. [Un aperçu de la](https://www.sqlshack.com/string_agg-function-in-sql/) [fonction `STRING_AGG`](https://www.sqlshack.com/string_agg-function-in-sql/)[dans SQL – SQLShack](https://www.sqlshack.com/string_agg-function-in-sql/)
4. [Un guide approfondi sur `GROUP BY`](https://www.freecodecamp.org/news/sql-group-by-clauses-explained/)