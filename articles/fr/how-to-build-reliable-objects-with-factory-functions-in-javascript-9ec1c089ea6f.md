---
title: Comment construire des objets fiables avec des fonctions de fabrication en
  JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-25T15:46:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-reliable-objects-with-factory-functions-in-javascript-9ec1c089ea6f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LBX1CRHCljE9BkuxOZUhmg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: Comment construire des objets fiables avec des fonctions de fabrication
  en JavaScript
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  I suggest to take into consideration these ideas for building reliable objects in
  JavaScript:


  Split objects in two: data...'
---

Par Cristian Salcescu

[**Découvrez Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Je suggère de prendre en considération ces idées pour construire des objets fiables en JavaScript :

* Diviser les objets en deux : objets de données et objets de comportement
* Rendre les objets de données immuables
* Exposer le comportement et masquer les données dans les objets de comportement
* Construire des objets de comportement testables

### Objets de données vs Objets de comportement

Essentiellement, il existe deux types d'objets dans une application :

* **Objets de données** — exposent des données
* **Objets de comportement** — exposent un comportement et masquent les données

#### Objets de données

Les objets de données exposent des données. Ils sont utilisés pour structurer et transférer des données à l'intérieur de l'application.

Prenons le cas d'une application de liste de tâches.

Voici à quoi peut ressembler l'objet de données de la tâche, obtenu depuis le serveur :

```js
{ id: 1, title: "This is a title", userId: 10, completed: false }
```

Et voici à quoi peut ressembler un objet de données utilisé pour afficher des informations dans la vue :

```js
{ id: 1, title: "This is a title", userName: "Cristi", completed: false };
```

Comme vous pouvez le voir, les deux objets contiennent uniquement des données. Il y a une petite différence entre eux : l'objet de données pour la vue a `userName` au lieu de `userId`.

Les objets de données sont des objets simples, généralement construits avec des littéraux d'objets.

#### Objets de comportement

Les objets de comportement exposent des méthodes et masquent les données.

Les objets de comportement agissent sur les objets de données. Ils peuvent prendre des objets de données en entrée ou retourner des objets de données.

Je vais prendre le cas de l'objet `TodoStore`. La responsabilité de cet objet est de stocker et de gérer la liste des tâches. Il effectue la synchronisation avec le serveur en utilisant l'objet `dataService`.

Lisez [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2) et apprenez à construire des applications en style fonctionnel.

[**Découvrez Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y&source=post_page---------------------------)**.**

Vous pouvez me trouver sur [Medium](https://medium.com/@cristiansalcescu) et [Twitter](https://twitter.com/cristi_salcescu).