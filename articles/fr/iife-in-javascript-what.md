---
title: 'IIFE en JavaScript : Que sont les Expressions de Fonction Invocables Immédiatement
  ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-04T23:59:00.000Z'
originalURL: https://freecodecamp.org/news/iife-in-javascript-what
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cc9740569d1a4ca3430.jpg
tags:
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: 'IIFE en JavaScript : Que sont les Expressions de Fonction Invocables Immédiatement
  ?'
seo_desc: "Function Statement\nA function created with a function declaration is a\
  \ Function object and has all the properties, methods and behavior of Function objects.\
  \ Example:\n  function statement(item){\n    console.log('Function statement example\
  \ '+ item);\n  ..."
---

## **Déclaration de Fonction**

Une fonction créée avec une déclaration de fonction est un objet Function et possède toutes les propriétés, méthodes et comportements des objets Function. Exemple :

```javascript
  function statement(item){
    console.log('Exemple de déclaration de fonction '+ item);
  }
```

## **Expression de Fonction**

Une expression de fonction est similaire à une déclaration de fonction sauf que le nom de la fonction peut être omis pour créer des fonctions anonymes. Exemple :

```javascript
  var expression = function (item){
    console.log('Exemple d\'expression de fonction '+ item);
  }
```

## **Expressions de Fonction Invocables Immédiatement**

Dès que la fonction est créée, elle s'invoque elle-même sans avoir besoin d'être invoquée explicitement. Dans l'exemple ci-dessous, la variable iife stockera une chaîne de caractères retournée par l'exécution de la fonction.

```javascript
  var iife = function (){
    return 'Exemple d\'Expressions de Fonction Invocables Immédiatement (IIFE) ';
  }();
  console.log(iife); // 'Exemple d\'Expressions de Fonction Invocables Immédiatement (IIFE) '
```

L'instruction avant une IIFE doit toujours se terminer par un ; sinon, elle générera une erreur.

**Mauvais exemple** :

```javascript
var x = 2 //pas de point-virgule, générera une erreur
(function(y){
  return x;
})(x); //Uncaught TypeError: 2 is not a function
```

## **Pourquoi utiliser les Expressions de Fonction Invocables Immédiatement ?**

```javascript
  (function(value){
    var greet = 'Bonjour';
    console.log(greet+ ' ' + value);
  })('IIFE');
```

Dans l'exemple ci-dessus, lorsque le moteur JavaScript exécute le code, il crée un contexte d'exécution global lorsqu'il voit le code et crée un objet fonction en mémoire pour l'IIFE. Et lorsqu'il atteint la ligne `46`, la fonction est invoquée, un nouveau contexte d'exécution est créé à la volée et ainsi la variable greet entre dans ce contexte d'exécution de fonction et non dans le contexte global, ce qui la rend unique. `Cela garantit que le code à l'intérieur de l'IIFE n'interfère pas avec d'autres codes ou ne soit pas interféré par un autre code` et ainsi le code est sécurisé.

#### **Plus d'Informations**

* [Immediately-invoked function expression sur Wikipedia](https://en.wikipedia.org/wiki/Immediately-invoked_function_expression)
* [À quoi sert le point-virgule initial dans les bibliothèques JavaScript ?](https://stackoverflow.com/questions/1873983/what-does-the-leading-semicolon-in-javascript-libraries-do)