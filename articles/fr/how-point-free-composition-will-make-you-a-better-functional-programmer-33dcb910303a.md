---
title: Comment la composition point-free fera de vous un meilleur programmeur fonctionnel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-14T22:32:33.000Z'
originalURL: https://freecodecamp.org/news/how-point-free-composition-will-make-you-a-better-functional-programmer-33dcb910303a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*a5N4vokpfnlmUnnJMou9zw.jpeg
tags:
- name: coding
  slug: coding
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment la composition point-free fera de vous un meilleur programmeur
  fonctionnel
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!


  "Point-free style — aims to reduce some of the visual clutter by removing unnecessary
  parameter-argument mapping." - Kyl...'
---

Par Cristian Salcescu

[**Découvrir Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

> "Le style point-free vise à réduire une partie du désordre visuel en supprimant la correspondance inutile entre les paramètres et les arguments." - Kyle Simpson dans [Functional-Light JavaScript](https://www.amazon.com/Functional-Light-JavaScript-Pragmatic-Balanced-FP-ebook/dp/B0787DBFKH/ref=sr_1_1?ie=UTF8&qid=1519405569&sr=8-1&keywords=kyle+simpson+functional&dpID=41de4aNCSQL&preST=_SX342_QL70_&dpSrc=srch)

Considérez le code suivant :

```
let newBooks = books.filter(point => isTechnology(point))
```

Maintenant, regardez le même code après avoir éliminé les points (paramètres/arguments) :

```
let newBooks = books.filter(isTechnology)
```

### Point-free dans les opérations de liste

Effectuons des opérations de liste dans un style point-free.

Supposons que nous devons trouver les titres de technologie dans une liste de livres, préparer l'objet livre avec toutes les informations pour la vue et trier les livres par le nom de l'auteur.

[Voici](https://jsfiddle.net/cristi_salcescu/j2mzyvau/) à quoi ressemblerait le code :

```
function getBooks(){
  return books.filter(isTechnology)
              .map(toBookView)
              .sort(ascByAuthor);
}

// Petites fonctions avec points
function isTechnology(book){
   return book.type === "T";
}

function toBookView(book){
  return Object.freeze({
    title : book.title,
    author : authors[book.authorID].name
  });
}
  
function ascByAuthor(book1, book2){
  if(book1.author < book2.author) return -1;
  if(book1.author > book2.author) return 1;
  return 0;
}
```

Les rappels `isTechnology()`, `toBookView()`, `ascByAuthor()` sont de petites fonctions avec des noms révélant l'intention. Elles ne sont pas construites dans un style point-free.

Le code assemblant toutes ces fonctions dans `getBooks()` est point-free.

#### Décomposition et composition

Notre manière naturelle de traiter un problème est de le diviser en plus petites parties, puis de tout réassembler.

Nous divisons la tâche plus grande en plusieurs fonctions effectuant des tâches plus petites. Ensuite, nous recombinons ces petites fonctions pour résoudre le problème initial.

Relisons les exigences :

> Nous devons trouver les titres de technologie dans une liste de livres, préparer l'objet livre avec toutes les informations pour la vue et trier les livres par le nom de l'auteur.

Nous avons créé :

* `isTechnology()` prédicat pour vérifier s'il s'agit d'un livre de technologie
* `toViewBook()` pour construire un objet avec toutes les informations pour la vue
* `ascByAuthorname()` pour trier deux livres par ordre croissant selon le nom de l'auteur
* `getBooks()` pour combiner toutes ces petites fonctions ensemble dans un style point-free

```
function getBooks(){
  return books.filter(isTechnology)
              .map(toBookView)
              .sort(ascByAuthor);
}
```

### Étapes vers la composition point-free

Il n'y a pas de rappel anonyme supplémentaire lors de la composition point-free. Pas de mot-clé `function`, pas de syntaxe de flèche `=&`gt;. Tout ce que nous voyons sont des noms de fonctions.

* Dans la plupart des cas, extrayez les rappels dans des fonctions nommées.
* Dans les cas simples, utilisez simplement une fonction utilitaire de la boîte à outils pour créer le rappel à la volée. [Regardez](#2428) la fonction `prop()`, par exemple.
* Écrivez la fonction de coordination dans un style point-free.

#### Petites fonctions

La conséquence de l'écriture de code de cette manière est un grand nombre de petites fonctions avec des noms révélant l'intention. Nommer ces petites fonctions prend du temps, mais si cela est bien fait, cela rendra le code plus facile à lire.

Il y aura deux types de fonctions :

* Fonctions effectuant une tâche : elles sont pures ou des fonctions de fermeture. Habituellement, elles ne sont pas construites dans un style point-free, mais ont plutôt de bons noms.
* Fonctions coordonnant de nombreuses tâches : joindre ces petites tâches dans un style point-free les rend plus faciles à lire.

#### Tout n'est pas point-free

Je ne vise pas à ce que tout soit point-free. Je vise le point-free à des endroits spécifiques, surtout lors de la composition de fonctions.

[**Découvrir Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)