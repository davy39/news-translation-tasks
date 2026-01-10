---
title: Comment créer un store en utilisant des fonctions pures
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-29T17:39:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-store-using-pure-functions-2c19b678552f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1QLyoQuirofEmDT1nE7LeA.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment créer un store en utilisant des fonctions pures
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Pure functions produce the same output value, given the same input. They have no
  side-effects, and are easier to read, un...'
---

Par Cristian Salcescu

[**Découvrir Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Les fonctions pures produisent la même valeur de sortie, étant donné la même entrée. Elles n'ont pas d'effets secondaires et sont plus faciles à lire, comprendre et tester.

Étant donné tout cela, je souhaite créer un store qui cache l'état mais utilise en même temps des fonctions pures.

### Immuabilité

Les fonctions pures ne modifient pas leur entrée. Elles traitent les valeurs d'entrée comme immuables.

Une valeur immuable est une valeur qui, une fois créée, ne peut pas être modifiée.

[Immutable.js](https://facebook.github.io/immutable-js/) fournit des structures de données immuables comme `List`. Une structure de données immuable créera une nouvelle structure de données à chaque action.

Considérez le code suivant :

```
import { List } from "immutable";
const list = List();
const newList = list.push(1);
```

`push()` crée une nouvelle liste qui contient le nouvel élément. Elle ne modifie pas la liste existante.

`delete()` retourne une nouvelle `List` où l'élément à l'index spécifié a été supprimé.

La structure de données `List` offre une belle interface pour travailler avec des listes de manière immuable, donc je vais l'utiliser comme valeur d'état.

### Le Store

Le store gère l'état.

L'état est une donnée qui peut changer. Le store cache cette donnée d'état et offre un ensemble public de méthodes pour travailler avec elle.

Je souhaite créer un store de livres avec les méthodes `add()`, `remove()` et `getBy()`.

Je veux que toutes ces fonctions soient des fonctions pures.

Il y aura deux types de fonctions pures utilisées par le store :

* des fonctions qui liront et filtreront l'état. Je les appellerai getters.
* des fonctions qui modifieront l'état. Je les appellerai setters.

Ces deux types de fonctions prendront l'état comme premier paramètre.

[**Découvrir Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)