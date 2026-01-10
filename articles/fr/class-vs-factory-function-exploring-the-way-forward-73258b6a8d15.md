---
title: 'Class vs Factory function: explorer la voie à suivre'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-25T05:23:38.000Z'
originalURL: https://freecodecamp.org/news/class-vs-factory-function-exploring-the-way-forward-73258b6a8d15
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2g8eIVimndik43W_Jl_OCA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Class vs Factory function: explorer la voie à suivre'
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  ECMAScript 2015 (aka ES6) comes with the class syntax, so now we have two competing
  patterns for creating objects. In ord...'
---

Par Cristian Salcescu

[**Découvrir Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres de Programmation Fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

ECMAScript 2015 (aka ES6) introduit la syntaxe `class`, donc maintenant nous avons deux modèles concurrents pour créer des objets. Afin de les comparer, je vais créer la même définition d'objet (TodoModel) en tant que classe, puis en tant que fonction factory.

**[TodoModel en tant que Classe](https://jsfiddle.net/cristi_salcescu/m9dhpzfx/)**

```
class TodoModel {
    constructor(){
        this.todos = [];
        this.lastChange = null;
    }
    
    addToPrivateList(){
        console.log("addToPrivateList"); 
    }
    add() { console.log("add"); }
    reload(){}
}
```

**[TodoModel en tant que Fonction Factory](https://jsfiddle.net/cristi_salcescu/bcta6yyv/)**

```
function TodoModel(){
    var todos = [];
    var lastChange = null;
        
    function addToPrivateList(){
        console.log("addToPrivateList"); 
    }
    function add() { console.log("add"); }
    function reload(){}
    
    return Object.freeze({
        add,
        reload
    });
}
```

### Encapsulation

La première chose que nous remarquons est que tous les membres, champs et méthodes d'un objet de classe sont publics.

```
var todoModel = new TodoModel();
console.log(todoModel.todos);     //[]
console.log(todoModel.lastChange) //null
todoModel.addToPrivateList();     //addToPrivateList
```

Le manque d'encapsulation peut créer des problèmes de sécurité. Prenons l'exemple d'un objet global qui peut être modifié directement depuis la Console de Développement.

Lors de l'utilisation d'une fonction factory, seules les méthodes que nous exposons sont publiques, tout le reste est encapsulé.

```
var todoModel = TodoModel();
console.log(todoModel.todos);     //undefined
console.log(todoModel.lastChange) //undefined
todoModel.addToPrivateList();     //taskModel.addToPrivateList
                                    n'est pas une fonction
```

### this

Les problèmes de perte de contexte de `this` sont toujours présents lors de l'utilisation de classes. Par exemple, `this` perd son contexte dans les fonctions imbriquées. Ce n'est pas seulement ennuyeux pendant le codage, mais c'est aussi une source constante de bugs.

```
class TodoModel {
    constructor(){
        this.todos = [];
    }
    
    reload(){ 
        setTimeout(function log() { 
           console.log(this.todos);    //undefined
        }, 0);
    }
}
todoModel.reload();                   //undefined
```

ou `this` perd son contexte lorsque la méthode est utilisée comme callback, comme sur un événement DOM.

```
$("#btn").click(todoModel.reload);    //undefined
```

Il n'y a pas de tels problèmes lors de l'utilisation d'une fonction factory, car elle n'utilise pas `this` du tout.

```
function TodoModel(){
    var todos = [];
        
    function reload(){ 
        setTimeout(function log() { 
           console.log(todos);        //[]
       }, 0);
    }
}
todoModel.reload();                   //[]
$("#btn").click(todoModel.reload);    //[]
```

#### this et arrow function

La fonction fléchée résout partiellement les problèmes de perte de contexte de `this` dans les classes, mais crée en même temps un nouveau problème :

* `this` ne perd plus son contexte dans les fonctions imbriquées
* `this` perd son contexte lorsque la méthode est utilisée comme callback
* la fonction fléchée favorise l'utilisation de fonctions anonymes

[J'ai refactorisé le `TodoModel` en utilisant la fonction fléchée](https://jsfiddle.net/cristi_salcescu/y0k18og2/). Il est important de noter que lors du processus de refactorisation vers la fonction fléchée, nous pouvons perdre quelque chose de très important pour la lisibilité, le nom de la fonction. [Regardez par exemple](https://jsfiddle.net/cristi_salcescu/y0k18og2/) :

```
//utiliser le nom de la fonction pour exprimer l'intention
setTimeout(function renderTodosForReview() { 
      /* code */ 
}, 0);

//versus utiliser une fonction anonyme
setTimeout(() => { 
      /* code */ 
}, 0);
```

[**Découvrir Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres de Programmation Fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)