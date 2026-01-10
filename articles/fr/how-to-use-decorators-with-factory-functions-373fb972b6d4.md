---
title: Comment utiliser les Décorateurs avec les Fonctions de Fabrication
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-30T00:26:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-decorators-with-factory-functions-373fb972b6d4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3ALgV0tL7sOWLtReXTVDJg.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Comment utiliser les Décorateurs avec les Fonctions de Fabrication
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  Method decorators are a tool for reusing common logic. They are complementary to
  Object Oriented Programming. Decorators ...'
---

Par Cristian Salcescu

[**Découvrir JavaScript Fonctionnel**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la Programmation Fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

Les décorateurs de méthodes sont un outil pour réutiliser la logique commune. Ils sont complémentaires à la Programmation Orientée Objet. Les décorateurs encapsulent la responsabilité partagée par différents objets.

[Considérons le code suivant](https://jsfiddle.net/cristi_salcescu/0tv3y06p/) :

```
function TodoStore(currentUser){
  let todos = [];
  
  function add(todo){
    let start = Date.now();
    if(currentUser.isAuthenticated()){
      todos.push(todo);
    } else {
      throw "Not authorized to perform this operation";
    }
            
    let duration = Date.now() - start;
    console.log("add() duration : " + duration);
  }
    
  return Object.freeze({
    add
  });  
}
```

L'intention de la méthode `add()` est d'ajouter de nouvelles tâches à l'état interne. En plus de cela, la méthode doit vérifier l'autorisation de l'utilisateur et journaliser la durée d'exécution. Ces deux choses sont des préoccupations secondaires et peuvent en fait se répéter dans d'autres méthodes.

Imaginons que nous pouvons encapsuler ces responsabilités secondaires dans des fonctions. Ensuite, nous pouvons écrire le code de la manière suivante :

```
function TodoStore(){
  let todos = [];
  
  function add(todo){
    todos.push(todo);
  }
    
  return Object.freeze({
     add:compose(logDuration,authorize)(add) 
  }); 
}
```

Maintenant, la méthode `add()` ajoute simplement la `todo` à la liste. Les autres responsabilités sont implémentées en décorant la méthode.

`logDuration()` et `authorize()` sont des décorateurs.

> Un **décorateur de fonction** est une fonction d'ordre supérieur qui prend une fonction comme argument et retourne une autre fonction, et la fonction retournée est une variation de la fonction argument.

> Reginald Braithwaite dans [Javascript Allongé](https://leanpub.com/javascript-allonge/read#decorators)

### Journaliser la Durée

Un scénario courant est la journalisation de la durée d'un appel de méthode. [Le décorateur suivant](https://jsfiddle.net/cristi_salcescu/z8hh356e/) journalise la durée d'un appel synchrone.

```
function logDuration(fn){
  return function decorator(...args){
    let start = Date.now();
    let result = fn.apply(this, args);
    let duration = Date.now() - start;
    console.log(fn.name + "() duration : " + duration);
    return result;
  }
}
```

Remarquez comment la fonction originale a été appelée — en passant la valeur actuelle de `this` et tous les arguments : `fn.apply(this, args)`.

[**Découvrir JavaScript Fonctionnel**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la Programmation Fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Architecture Fonctionnelle avec React et Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)