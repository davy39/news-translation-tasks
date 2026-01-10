---
title: Explorons les objets en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-10T17:37:32.000Z'
originalURL: https://freecodecamp.org/news/lets-explore-objects-in-javascript-4a4ad76af798
coverImage: https://cdn-media-1.freecodecamp.org/images/1*o9elBqm0t6G25Jt1WhkF4w.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Explorons les objets en JavaScript
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Objects are dynamic collections of properties, with a “hidden” property to the object’s
  prototype.

  A property has a key a...'
---

Par Cristian Salcescu

[**Découvrez le JavaScript Fonctionnel**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la Programmation Fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781) !

Les objets sont des collections dynamiques de propriétés, avec une propriété "cachée" vers le prototype de l'objet.

Une propriété a une clé et une valeur.

### Clé de propriété

La clé de propriété est une chaîne unique.

Il existe deux façons d'accéder aux propriétés : la notation par point et la notation par crochets. Lorsque la notation par point est utilisée, la clé de propriété doit être un identifiant valide.

```
let obj = {  message : "A message"}
```

```
obj.message //"A message"obj["message"] //"A message"
```

L'accès à une propriété qui n'existe pas ne générera pas d'erreur, mais retournera `undefined`.

```
obj.otherProperty //undefined
```

JavaScript traite les primitives, les objets et les fonctions comme des objets.

Les objets sont dynamiques par nature et peuvent être utilisés comme des maps.

Les objets héritent d'autres objets. Les fonctions constructeurs et les classes sont une syntaxe sucrée pour créer des objets qui héritent d'autres objets prototypes.

`Object.create()` peut être utilisé pour l'héritage simple et `Object.assign()` pour l'héritage multiple.

Les fonctions de fabrication peuvent construire des objets encapsulés.

Lisez [**Architecture Fonctionnelle avec React et Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2) et apprenez à construire des applications en style fonctionnel.

[**Découvrez le JavaScript Fonctionnel**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la Programmation Fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------) !

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y&source=post_page---------------------------).

Vous pouvez me trouver sur [Medium](https://medium.com/@cristiansalcescu) et [Twitter](https://twitter.com/cristi_salcescu).