---
title: Opérations CRUD – Qu'est-ce que CRUD ?
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-06-15T16:51:42.000Z'
originalURL: https://freecodecamp.org/news/crud-operations-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/crud.png
tags:
- name: api
  slug: api
- name: beginners guide
  slug: beginners-guide
- name: crud
  slug: crud
- name: database
  slug: database
- name: User Interface
  slug: user-interface
seo_title: Opérations CRUD – Qu'est-ce que CRUD ?
seo_desc: 'Despite being commonly pronounced /krʌd/, CRUD is not a word. It’s an abbreviation
  that stands for Create, Read, Update, and Delete or Destroy.

  In this article, I will show you what CRUD means, and what the individual terms
  mean and do. I will also s...'
---

Malgré le fait qu'il soit couramment prononcé `/krʌd/`, CRUD n'est pas un mot. C'est une abréviation qui signifie Create, Read, Update, et Delete ou Destroy.

Dans cet article, je vais vous montrer ce que signifie CRUD, et ce que signifient les termes individuels et ce qu'ils font. Je vais également vous montrer comment les opérations de création, de lecture, de mise à jour et de suppression fonctionnent dans le monde réel.

## Ce que nous allons couvrir
- [Qu'est-ce que CRUD ?](#heading-qu-est-ce-que-crud)
- [Qu'est-ce que l'opération `CREATE` et comment fonctionne-t-elle ?](#heading-qu-est-ce-que-l-operation-create-et-comment-fonctionne-t-elle)
- [Qu'est-ce que l'opération `READ` et comment fonctionne-t-elle ?](#heading-qu-est-ce-que-l-operation-read-et-comment-fonctionne-t-elle)
- [Qu'est-ce que l'opération `UPDATE` et comment fonctionne-t-elle ?](#heading-qu-est-ce-que-l-operation-update-et-comment-fonctionne-t-elle)
- [Qu'est-ce que l'opération `DELETE` et comment fonctionne-t-elle ?](#heading-qu-est-ce-que-l-operation-delete-et-comment-fonctionne-t-elle)
- [Conclusion](#heading-conclusion)

## Qu'est-ce que CRUD ?

CRUD fait référence aux quatre opérations de base qu'une application logicielle doit être capable de performer – Create, Read, Update, et Delete.

Dans de telles applications, les utilisateurs doivent être capables de **créer des données**, avoir accès aux données dans l'interface utilisateur en **lisant** les données, **mettre à jour** ou **éditer** les données, et **supprimer** les données.

Dans les applications complètes, les applications CRUD se composent de 3 parties : une API (ou serveur), une base de données et une interface utilisateur (UI).

L'API contient le code et les méthodes, la base de données stocke et aide l'utilisateur à récupérer les informations, tandis que l'interface utilisateur aide les utilisateurs à interagir avec l'application.

Vous pouvez créer une application CRUD avec n'importe quel langage de programmation. Et l'application n'a pas besoin d'être full stack – vous pouvez créer une application CRUD avec JavaScript côté client.

En fait, l'application avec laquelle je vais vous montrer comment les opérations de création, de lecture, de mise à jour et de suppression fonctionnent est faite avec JavaScript côté client.

Chaque lettre de l'acronyme CRUD a une méthode de requête HTTP correspondante.
| **Opération CRUD**| **Méthode de requête HTTP**|
| ----------- | ----------- |
| Create| POST |
| Read | GET|
| Update| PUT ou PATCH|
| Delete | DELETE|

## Qu'est-ce que l'opération `CREATE` et comment fonctionne-t-elle ?

Dans CRUD, l'opération de création fait ce que le nom implique. Cela signifie créer une entrée. Cette entrée pourrait être un compte, des informations utilisateur, un post, ou une tâche.

Comme je l'ai souligné plus tôt, le protocole HTTP qui implémente une opération `CREATE` est la méthode POST.

Dans une base de données SQL, créer signifie `INSERT`. Dans une base de données NoSQL comme MongoDB, vous créez avec la méthode `insert()`.

Dans une interface utilisateur, ce GIF ci-dessous montre comment l'opération `CREATE` fonctionne :
![create-op](https://www.freecodecamp.org/news/content/images/2022/06/create-op.gif)

## Qu'est-ce que l'opération `READ` et comment fonctionne-t-elle ?

L'opération `READ` signifie obtenir l'accès aux entrées ou aux données dans l'interface utilisateur. C'est-à-dire, les voir. Encore une fois, l'entrée pourrait être n'importe quoi, des informations utilisateur aux posts sur les réseaux sociaux, et autres.

Cet accès pourrait signifier que l'utilisateur obtient l'accès aux entrées créées juste après les avoir créées, ou les recherche. La recherche est implémentée pour permettre à l'utilisateur de filtrer les entrées dont il n'a pas besoin.

Le protocole HTTP qui implémente une opération `READ` est la méthode GET.

Dans une base de données SQL, lire signifie `SELECT` une entrée. Dans une base de données NoSQL comme MongoDB, vous lisez avec la méthode `find()` ou `findById()`.
![read-operation](https://www.freecodecamp.org/news/content/images/2022/06/read-operation.png)


## Qu'est-ce que l'opération `UPDATE` et comment fonctionne-t-elle ?

`UPDATE` est l'opération qui vous permet de modifier des données existantes. C'est-à-dire, éditer les données.

Contrairement à `READ`, l'opération `UPDATE` modifie les données existantes en y apportant des changements.

PUT et PATCH sont les protocoles HTTP avec lesquels vous pouvez implémenter une opération `UPDATE`, selon ce dont vous avez besoin.

`PUT` doit être utilisé lorsque vous voulez que l'entrée entière soit mise à jour, et PATCH si vous ne voulez pas que l'entrée entière soit modifiée.

Dans une base de données SQL, vous utilisez `UPDATE` pour mettre à jour une entrée. Dans une base de données NoSQL comme MongoDB, vous pouvez implémenter une fonctionnalité de mise à jour avec la méthode `findByIdAndUpdate()`.

Dans une interface utilisateur, ce GIF ci-dessous montre comment l'opération `UPDATE` fonctionne :
![update-op](https://www.freecodecamp.org/news/content/images/2022/06/update-op.gif)

## Qu'est-ce que l'opération `DELETE` et comment fonctionne-t-elle ?

Supprimer signifie se débarrasser d'une entrée de l'interface utilisateur et de la base de données.

`DELETE` est le protocole HTTP pour implémenter une opération `DELETE`.

Dans une base de données SQL, `DELETE` est utilisé pour supprimer une entrée. Dans une base de données NoSQL comme MongoDB, vous pouvez implémenter la suppression avec la méthode `findByIdAndDelete()`.
![delete-op](https://www.freecodecamp.org/news/content/images/2022/06/delete-op.gif)


## Conclusion

Cet article vous a montré ce que signifie CRUD et ce que chaque opération individuelle dans une application CRUD fait.

Vous pouvez penser à CRUD de cette manière :
- Vous créez un compte sur les réseaux sociaux et remplissez vos informations - `CREATE`
- Vous obtenez l'accès aux informations que vous avez entrées et les gens peuvent vous rechercher – `READ`
- Vous obtenez un nouvel emploi chez Google et changez votre statut d'emploi en employé – `UPDATE`
- Vous en avez assez de la toxicité des réseaux sociaux et supprimez votre compte - `DELETE`

Pour apprendre comment vous pouvez créer votre propre application CRUD, consultez [ce tutoriel](https://www.freecodecamp.org/news/learn-crud-operations-in-javascript-by-building-todo-app/) de Joy Shaheb de freeCodeCamp.

Continuez à coder 👋