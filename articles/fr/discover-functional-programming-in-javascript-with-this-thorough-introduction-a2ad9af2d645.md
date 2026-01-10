---
title: Découvrez la Programmation Fonctionnelle en JavaScript avec cette introduction
  approfondie
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-04T00:53:10.000Z'
originalURL: https://freecodecamp.org/news/discover-functional-programming-in-javascript-with-this-thorough-introduction-a2ad9af2d645
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PU20rbKCMm3C2BLEM24dgg.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: Productivity
  slug: productivity
- name: technology
  slug: technology
seo_title: Découvrez la Programmation Fonctionnelle en JavaScript avec cette introduction
  approfondie
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  JavaScript is the first language to bring Functional Programming to the mainstream.
  It has first-class functions and clos...'
---

Par Cristian Salcescu

[**Découvrez Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la Programmation Fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

JavaScript est le premier langage à avoir introduit la Programmation Fonctionnelle dans le grand public. Il dispose de fonctions de première classe et de fermetures. Elles ouvrent la voie à des modèles de programmation fonctionnelle.

# Fonctions de Première Classe

Les fonctions sont des objets de première classe. Les fonctions peuvent être stockées dans des variables, des objets ou des tableaux, passées en arguments à d'autres fonctions ou retournées par des fonctions.

```javascript
//stockée dans une variable
function doSomething(){
}

//stockée dans une variable
const doSomething = function (){ };

//stockée dans une propriété
const obj = { 
   doSomething : function(){ } 
}

//passée en argument
process(doSomething);

//retournée par une fonction
function createGenerator(){
  return function(){
  }
}
```

## Lambdas

_Un lambda est une fonction qui est utilisée comme une valeur._

En JavaScript, les fonctions sont des objets de première classe, donc toutes les fonctions peuvent être utilisées comme des valeurs. Toutes les fonctions peuvent être des lambdas, avec ou sans nom. Je suggère en fait de privilégier les fonctions nommées.

# Boîte à Outils Fonctionnelle pour les Tableaux

## [Boîte à Outils de Base](https://jsfiddle.net/lorinoata/s5b9m6ut/)

`filter()` sélectionne des valeurs dans une liste en fonction d'une fonction prédicat qui décide quelles valeurs doivent être conservées.

```javascript
const numbers = [1,2,3,4,5,6];
function isEven(number){
  return number % 2 === 0;
}
const evenNumbers = numbers.filter(isEven);
```

Une fonction prédicat est une fonction qui prend une valeur en entrée et retourne `true`/`false` en fonction de si la valeur satisfait la condition. `isEven()` est une fonction prédicat.

[**Découvrez Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la Programmation Fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)