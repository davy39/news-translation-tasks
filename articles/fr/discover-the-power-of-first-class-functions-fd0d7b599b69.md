---
title: Découvrez la puissance des fonctions de première classe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-26T16:47:18.000Z'
originalURL: https://freecodecamp.org/news/discover-the-power-of-first-class-functions-fd0d7b599b69
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Q1WNr4yLLdQuQs01--TCKg.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Découvrez la puissance des fonctions de première classe
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  In JavaScript, functions are first-class objects, which means they can be:


  stored in a variable, object, or array

  passed...'
---

Par Cristian Salcescu

[**Découvrez JavaScript Fonctionnel**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781) !

En JavaScript, les fonctions sont des objets de première classe, ce qui signifie qu'elles peuvent être :

* stockées dans une variable, un objet ou un tableau
* passées comme argument à une fonction
* retournées par une fonction

### Stocker une fonction

Les fonctions peuvent être stockées de trois manières :

* stocker dans une variable : `let fn = function doSomething() {}`
* stocker dans un objet : `let obj = { doSomething : function(){} }`
* stocker dans un tableau : `arr.push(function doSomething() {})`

Dans le premier et le troisième exemple, j'ai utilisé une expression de fonction nommée.

L'expression de fonction définit une fonction dans le cadre d'une expression plus large. La ligne de code ne commence pas par `function`.

### Fonction en tant qu'argument

Dans l'exemple suivant, la fonction `doSomething` est envoyée comme argument à `doAction()`.

```
doAction(function doSomething(){});
```

`doSomething` est une fonction de rappel.

Une fonction de rappel est une fonction passée comme argument à une autre fonction.

#### Fonctions d'ordre supérieur

> Une fonction d'ordre supérieur est une fonction qui prend une autre fonction comme entrée, retourne une fonction ou fait les deux.

Vous pouvez en savoir plus dans le livre [Discover Functional JavaScript](https://www.amazon.com/dp/B07PBQJYYG).

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Architecture Fonctionnelle avec React et Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)