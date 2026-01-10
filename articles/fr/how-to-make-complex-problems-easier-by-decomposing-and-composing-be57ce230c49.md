---
title: Comment rendre les problèmes complexes plus faciles en les décomposant et en
  les composant
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-13T14:48:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-complex-problems-easier-by-decomposing-and-composing-be57ce230c49
coverImage: https://cdn-media-1.freecodecamp.org/images/0*4H9f_YZRxP-lUtYx
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment rendre les problèmes complexes plus faciles en les décomposant
  et en les composant
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Our natural way of dealing with complexity is to break it into smaller pieces and
  then put everything back together.

  This...'
---

Par Cristian Salcescu

[**Découvrir Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Notre manière naturelle de gérer la complexité est de la diviser en plus petites parties, puis de tout rassembler.

C'est un processus en deux étapes :

* décomposer le problème en plus petites parties
* composer les petites parties pour résoudre le problème

Nous décomposons en plus petites parties car elles sont plus faciles à comprendre et à implémenter. Les petites parties peuvent être développées en parallèle.

Le processus de décomposition consiste à attribuer des responsabilités et à donner des noms. Cela facilite la discussion et le raisonnement. Une fois qu'une responsabilité est identifiée, nous pouvons la réutiliser.

La composition consiste à combiner les petites parties ensemble et à établir une relation entre elles. Nous décidons de la manière dont ces pièces communiquent, de l'ordre dans lequel elles s'exécutent et de la façon dont les données circulent entre elles.

Nous trouvons un système difficile à comprendre même s'il est divisé en plus petites parties, s'il y a un grand nombre de relations entre ces parties. Pour rendre un système plus facile à comprendre, nous devons minimiser le nombre de connexions possibles entre ses parties.

### Décomposition des objets

Les objets sont plus que de l'état et du comportement travaillant ensemble. Les objets sont des choses avec des responsabilités.

#### Décomposer

Dans [Comment créer une application à trois couches avec React](https://medium.freecodecamp.org/how-to-create-a-three-layer-application-with-react-8621741baca0), je prends une application de liste de tâches et je divise les responsabilités entre les objets suivants :

* `TodoDataService` : responsable de la communication avec l'API Todo du serveur
* `UserDataService` : responsable de la communication avec l'API User du serveur.
* `TodoStore` : le magasin de domaine pour la gestion des tâches. Il est la source unique de vérité concernant les tâches.
* `UserStore` : le magasin de domaine pour la gestion des utilisateurs.
* `TodoListContainer` : le composant conteneur racine affichant la liste des tâches.

Comme vous pouvez le voir, lors de la décomposition, j'attribue des responsabilités et je donne des noms.

#### Composer

Ensuite, je les compose ensemble dans une seule fonction. C'est l'endroit où tous les objets sont créés et les dépendances injectées. Cela s'appelle la Composition Root.

[**Découvrir Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)