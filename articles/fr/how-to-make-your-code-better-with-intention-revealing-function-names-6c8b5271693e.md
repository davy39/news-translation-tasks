---
title: Comment améliorer votre code avec des noms de fonctions révélant l'intention
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-24T00:13:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-code-better-with-intention-revealing-function-names-6c8b5271693e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C0YINGVSuF-kLTCynyBwCw.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment améliorer votre code avec des noms de fonctions révélant l'intention
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Code is a way to communicate with developers reading it. Functions with intention-revealing
  names are easier to read. We ...'
---

Par Cristian Salcescu

[**Découvrir Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Le code est un moyen de communiquer avec les développeurs qui le lisent. Les fonctions avec des noms révélant l'intention sont plus faciles à lire. Nous lisons le nom de la fonction et pouvons comprendre son but. Le nom de la fonction est notre outil pour exprimer l'intention d'un morceau de code.

Examinons une [liste d'opérations effectuées dans un style fonctionnel](https://jsfiddle.net/cristi_salcescu/pujuve88/) avec l'utilisation de fonctions anonymes.

```
function getTodos(users){
  return todos
    .filter(todo => !todo.completed && todo.type === "RE")
    .map(todo => ({
      title : todo.title,
      userName : users[todo.userId].name
    }))
    .sort((todo1, todo2) =>  
      todo1.userName.localeCompare(todo2.userName));
}
```

Maintenant, vérifiez la même fonctionnalité refactorisée en utilisant des fonctions avec des noms révélant l'intention.

```
function isTopPriority(todo){
  return !todo.completed && todo.type === "RE";
}

function ascByUserName(todo1, todo2){
  return todo1.userName.localeCompare(todo2.userName);
}
  
function getTodos(users){
  function toViewModel(todo){
    return {
      title : todo.title,
      userName : users[todo.userId].name
    }
  }
  return todos.filter(isTopPriority)
              .map(toViewModel).sort(ascByUserName);
}
```

Les noms de fonctions donnent de la clarté au code. Avec un bon nom de fonction, vous n'avez qu'à lire le nom — vous n'avez pas besoin d'analyser son code pour comprendre ce qu'il fait.

> _Il est largement estimé que les développeurs passent 70% du temps de maintenance du code à le lire pour le comprendre._

> _Kyle Simpson dans [Functional-Light JavaScript](https://www.amazon.com/Functional-Light-JavaScript-Pragmatic-Balanced-FP-ebook/dp/B0787DBFKH/ref=sr_1_1?ie=UTF8&qid=1519405569&sr=8-1&keywords=kyle+simpson+functional&dpID=41de4aNCSQL&preST=_SX342_QL70_&dpSrc=srch)_

[**Découvrir Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)