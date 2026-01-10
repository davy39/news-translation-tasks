---
title: Opérations CRUD – Définition de Crud en Programmation
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-10-20T21:54:52.000Z'
originalURL: https://freecodecamp.org/news/crud-operations-crud-definition-in-programming
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/cover-template--16-.png
tags:
- name: crud
  slug: crud
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: Opérations CRUD – Définition de Crud en Programmation
seo_desc: 'When interacting with a database or working with an API, you''ll often
  encounter the term CRUD. It is a popular acronym for the four basic operations or
  functions that a model (in the case of an API) or a database management system uses.

  This is an ac...'
---

Lorsque vous interagissez avec une base de données ou travaillez avec une API, vous rencontrerez souvent le terme CRUD. Il s'agit d'un acronyme populaire pour les quatre opérations ou fonctions de base qu'un modèle (dans le cas d'une API) ou un système de gestion de base de données utilise.

Il s'agit d'un acronyme que toute personne apprenant la programmation informatique rencontrera, et il est bon de se familiariser avec sa signification.

Dans cet article, vous apprendrez ce que signifie chaque partie de l'acronyme, ce que font les opérateurs CRUD et comment ils se rapportent aux bases de données et aux API.

## Qu'est-ce que CRUD ?

CRUD est un acronyme pour **C**réer, **R**ecupérer, **M**ettre à jour et **S**upprimer. Chacune de ces opérations effectue des actions différentes, mais elles visent toutes à suivre et gérer les données, provenant d'une base de données, d'une API, ou autre.

Lors de la création d'une base de données ou de la construction d'API, vous voudrez que les utilisateurs puissent manipuler les données disponibles, soit en récupérant ces données, en les mettant à jour, en les supprimant, ou en ajoutant plus de données. Ces opérations sont rendues possibles grâce aux opérations CRUD.

Ces opérations ont des fonctions dans les bases de données, car vous pouvez les mapper à une instruction standard du langage de requête structuré (SQL). De plus, ces opérations peuvent être mappées à une méthode de protocole de transfert hypertexte (HTTP) lors de la travail avec des API RESTful.

En SQL, l'opération Create peut être mappée à la fonction INSERT de la même manière que la méthode POST dans une requête HTTP. Voici un tableau pour résumer à quoi chaque opération CRUD peut être mappée dans une requête HTTP et une fonction SQL :

| Lettre | Opération | Requête HTTP | Fonction SQL |
| --- | --- | --- | --- |
| C | Créer | POST | INSERT |
| R | Lire | GET | SELECT |
| U | Mettre à jour | PATCH/ PUT (si vous avez `id` ou `uuid`) | UPDATE |
| D | Supprimer | DELETE | DELETE |

Avec quelques exemples, comprenons maintenant comment ces acronymes fonctionnent avec SQL et les requêtes HTTP.

## Comment fonctionne l'opération Create

Comme son nom l'indique, vous utilisez l'opération Create pour créer un nouvel enregistrement ou une nouvelle entrée. Cet enregistrement peut être les données d'un utilisateur, un nouvel élément, des informations, ou une nouvelle ligne à ajouter à votre base de données.

Par exemple, supposons que vous avez une base de données ou un tableau d'utilisateurs qui contient le nom, l'âge, le nom d'utilisateur, le mot de passe et l'ID unique de chaque utilisateur. Vous pouvez ajouter un nouvel utilisateur à la base de données ou à la liste des utilisateurs (cela est appelé un nouvel enregistrement ou une nouvelle entrée).

Lorsque vous travaillez avec SQL, cela est mappé à la fonction INSERT. Une simple fonction INSERT ressemble à ceci :

```sql
INSERT INTO table_name (column1, column2, column3, ...)
  VALUES (value1, value2, value3, ...);
```

Dans l'exemple ci-dessus, vous associez les nouvelles valeurs à leurs colonnes respectives via leur nom en utilisant la fonction **INSERT**. Vous pouvez également modifier cela, mais l'accent est mis sur la fonction INSERT.

Lorsque vous travaillez avec des API RESTful, vous utiliserez les méthodes HTTP POST. Par exemple, utilisons l'API Fetch de JavaScript :

```js
fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  body: JSON.stringify({
    title: 'foo',
    body: 'bar',
    userId: 1,
  }),
  headers: {
    'Content-type': 'application/json; charset=UTF-8',
  },
})
  .then((response) => response.json())
  .then((json) => console.log(json));
```

Dans l'exemple ci-dessus, un nouvel objet contenant le `title`, `body` et `userId` du nouveau `post` est ajouté à l'API `[posts](https://jsonplaceholder.typicode.com/posts)`. Le serveur doit retourner un en-tête avec le code de réponse HTTP 201 (CREATED).

## Comment fonctionne l'opération Read

Vous utilisez l'opération Read pour lire une base de données entière ou rechercher une ou plusieurs entrées en fonction de certains paramètres.

Par exemple, si vous avez une base de données d'utilisateurs, vous pouvez récupérer la liste complète des utilisateurs ou obtenir un utilisateur particulier...ou tout ce que vous voulez. L'idée de récupérer peut être appelée LECTURE.

Lorsque vous travaillez avec SQL, cela est mappé à la fonction SELECT. Une simple fonction SELECT ressemble à ceci :

```sql
SELECT * FROM menu;
```

Dans l'exemple ci-dessus, vous sélectionnez toutes les données de la table menu. Vous pouvez également demander des valeurs spécifiques via leurs noms de colonne :

```sql
SELECT CustomerID, FirstName, LastName, Email, PhoneNumber
    FROM   Customer
```

Vous pouvez également utiliser des paramètres et bien plus, mais l'accent est mis sur le fait que vous utiliserez toujours la fonction SELECT.

Lorsque vous travaillez avec des API RESTful, vous utiliserez la méthode HTTP GET. Bien que la plupart du temps, vous n'ayez pas besoin de spécifier la méthode car c'est la méthode par défaut, par exemple, lorsque vous utilisez l'API Fetch de JavaScript :

```js
fetch('https://jsonplaceholder.typicode.com/posts')
  .then((response) => response.json())
  .then((json) => console.log(json));
```

En l'absence d'erreurs, cela retournera les données JSON de l'API, ainsi qu'un code de réponse 200 représentant OK. S'il y a une erreur, il retournera souvent un code de réponse 404 (NOT FOUND).

## Comment fonctionne l'opération Update

Vous utilisez l'opération Update pour modifier des données existantes. C'est comme éditer les données. Peut-être voulez-vous corriger l'orthographe d'un nom de Jon Doe à John Doe.

Lorsque vous travaillez avec SQL, cela est mappé à la fonction UPDATE. Une simple fonction UPDATE ressemble à ceci :

```sql
UPDATE user
  SET user_name = 'John Doe', age = 62
  WHERE item_id = 1;
```

La requête ci-dessus changera le nom et l'âge de l'utilisateur spécifié `id`.

Lorsque vous travaillez avec des API RESTful, vous utiliserez soit les méthodes HTTP PUT ou PATCH.

```js
fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'PUT',
  body: JSON.stringify({
    id: 1,
    title: 'foo',
    body: 'bar',
    userId: 1,
  }),
  headers: {
    'Content-type': 'application/json; charset=UTF-8',
  },
})
  .then((response) => response.json())
  .then((json) => console.log(json));
```

Cela retournera une réponse avec un code de statut 200 (OK) si l'opération est réussie.

## Comment fonctionne l'opération Delete

Comme vous l'avez probablement deviné, vous utilisez cette opération pour supprimer une entrée ou un enregistrement spécifié. C'est l'opposé direct de l'opération Create, mais pour cela, vous spécifierez l'ID (valeur unique) que vous souhaitez supprimer.

Lorsque vous travaillez avec SQL, cela est mappé à la fonction DELETE. Une simple fonction DELETE ressemble à ceci :

```sql
DELETE FROM user WHERE user_name='John Doe';
```

Cela supprimera la ligne avec le nom "John Doe" de la table. Si vous souhaitez supprimer tous les enregistrements de la table, vous pouvez utiliser ce qui suit :

```sql
DELETE FROM user;
```

Lorsque vous travaillez avec des API RESTful, vous utiliserez la méthode DELETE :

```js
fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'DELETE',
});
```

Si elle réussit, cela devrait retourner un code de réponse 204 (NO CONTENT).

## Conclusion

Dans ce tutoriel, vous avez appris ce que signifie chaque opération de l'acronyme CRUD, ce qu'elles font et comment elles fonctionnent avec SQL et les requêtes HTTP.

En résumé, C représente Créer et est utilisé pour créer une nouvelle entrée. R représente Lire et est utilisé pour lire et récupérer des entrées. U représente Mettre à jour et met à jour une entrée. D représente Supprimer et est utilisé pour supprimer une entrée.

Vous pouvez en apprendre davantage sur [les opérations CRUD en JavaScript en construisant une application Todo dans cet article](https://www.freecodecamp.org/news/learn-crud-operations-in-javascript-by-building-todo-app/) écrit par [Joy Shaheb](https://www.freecodecamp.org/news/author/joy/).

Merci d'avoir lu, et amusez-vous bien à coder !