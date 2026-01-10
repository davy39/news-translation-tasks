---
title: Comment apprendre Redux d'un point de vue programmation fonctionnelle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T18:14:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-learn-redux-from-a-functional-programming-perspective-720892f704c6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rWN6HdC61ChO2dNs8W8wEQ.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: Redux
  slug: redux
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment apprendre Redux d'un point de vue programmation fonctionnelle
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Redux is a state container that promotes the use of functional programming for managing
  state.

  I would say that the Redux...'
---

Par Cristian Salcescu

[**Découvrir Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Redux est un conteneur d'état qui promeut l'utilisation de la programmation fonctionnelle pour gérer l'état.

Je dirais que l'écosystème Redux a évolué vers un modèle architectural qui donne les meilleures pratiques sur la façon d'organiser une application.

### Fonctions pures

Les fonctions pures produisent la même valeur de sortie, étant donné la même entrée. Les fonctions pures n'ont pas d'effets secondaires.

Les fonctions pures ne mutent pas les données, donc la question est de savoir comment nous pouvons changer l'état et en même temps utiliser des fonctions pures. Redux propose une solution : nous écrivons des fonctions pures et laissons la bibliothèque les appliquer et effectuer le changement d'état.

L'application effectue un changement d'état, mais la mutation est encapsulée derrière le store Redux.

### Immuabilité

Une valeur immuable est une valeur qui, une fois créée, ne peut pas être modifiée.

La valeur de l'état est immuable, donc chaque fois que nous voulons changer l'état, nous devons créer une nouvelle valeur immuable.

La valeur de l'état est immuable mais l'état peut changer. Il n'y a aucun intérêt à utiliser une bibliothèque pour gérer un état qui ne change pas. Nous pouvons utiliser un objet simple pour stocker ce type de données.

### Architecture

Redux suggère que nous divisions une application pratique en les parties suivantes :

* Composants de présentation
* Créateurs d'actions (aka Créateurs d'actions synchrones)
* Réducteurs
* Créateurs d'actions asynchrones
* Utilitaires/API
* Sélecteurs
* Composants conteneurs

[**Découvrir Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)