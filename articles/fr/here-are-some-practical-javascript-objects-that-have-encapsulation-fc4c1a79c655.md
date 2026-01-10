---
title: Voici quelques objets JavaScript pratiques qui ont l'encapsulation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-05T00:59:03.000Z'
originalURL: https://freecodecamp.org/news/here-are-some-practical-javascript-objects-that-have-encapsulation-fc4c1a79c655
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lMkY1zO_hMbQURoXEMuLgA.png
tags:
- name: coding
  slug: coding
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: technology
  slug: technology
seo_title: Voici quelques objets JavaScript pratiques qui ont l'encapsulation
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Encapsulation means information hiding. It’s about hiding as much as possible of
  the object’s internal parts and exposing...'
---

Par Cristian Salcescu

[**Découvrir JavaScript Fonctionnel**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781) !

L'encapsulation signifie le masquage d'informations. Il s'agit de cacher autant que possible les parties internes de l'objet et d'exposer une interface publique minimale.

La manière la plus simple et la plus élégante de créer de l'encapsulation en JavaScript est d'utiliser des closures. Une closure peut être créée en tant que fonction avec un état privé. Lorsque nous créons plusieurs closures partageant le même état privé, nous créons un objet.

Je vais construire quelques objets qui peuvent être utiles dans une application : Stack, Queue, Event Emitter et Timer. Tous seront construits en utilisant des fonctions de fabrique.

Commençons.

### Pile

La pile est une structure de données avec deux opérations principales : `push` pour ajouter un élément à la collection, et `pop` pour supprimer l'élément le plus récemment ajouté. Elle ajoute et supprime des éléments selon le principe Last In First Out (LIFO).

Regardez l'exemple suivant :

```
let pile = Pile();
pile.push(1);
pile.push(2);
pile.push(3);
pile.pop(); //3
pile.pop(); //2
```

[Implémentons la pile](https://jsfiddle.net/cristi_salcescu/6a1btczx/) en utilisant une fonction de fabrique.

```
function Pile(){
  let liste = [];
  
  function push(valeur){ liste.push(valeur); }
  function pop(){ return liste.pop(); }
  
  return Object.freeze({
    push,
    pop
  });
}
```

L'objet pile a deux méthodes publiques `push()` et `pop()`. L'état interne ne peut être modifié que par ces méthodes.

```
pile.liste; //undefined
```

Je ne peux pas modifier directement l'état interne :

```
pile.liste = 0;//Impossible d'ajouter la propriété liste, l'objet n'est pas extensible
```

Vous pouvez en savoir plus dans le livre [Découvrir JavaScript Fonctionnel](https://www.amazon.com/dp/B07PBQJYYG).

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**React Fonctionnel**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Architecture Fonctionnelle avec React et Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)