---
title: Un guide de base sur les fermetures (Closures) en JavaScript
subtitle: ''
author: Parathan Thiyagalingam
co_authors: []
series: null
date: '2019-05-03T18:47:26.000Z'
originalURL: https://freecodecamp.org/news/a-basic-guide-to-closures-in-javascript-9fc8b7e3463e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Nm0GW5PgM1okjXAZz_aQrQ.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Un guide de base sur les fermetures (Closures) en JavaScript
seo_desc: The Closure is a collection of all variables in scope at the time of function
  creation. To use closure, create a function inside another function which is called
  a Nested Function. The inner function will have access to the variables in the outer
  fun...
---

La fermeture (Closure) est une collection de toutes les variables dans la portée au moment de la création de la fonction. Pour utiliser une fermeture, créez une fonction à l'intérieur d'une autre fonction, appelée fonction imbriquée (Nested Function). La fonction interne aura accès aux variables de la portée de la fonction externe (**Closure** aide à accéder à la portée de la fonction externe), même après que la fonction externe a retourné. Les fermetures sont créées chaque fois qu'une fonction est créée.

Avant de continuer pour comprendre les fermetures, obtenons d'abord une vue d'ensemble de la chaîne de portée (Scope Chain) en JavaScript.

Normalement, il existe 2 types de portée :

* Portée globale (Global Scope)
* Portée locale (Local Scope)

Dans la version ES5, une variable à l'intérieur d'une fonction n'est pas visible à l'extérieur. Mais les variables à l'intérieur d'un bloc (conditions comme if ou while) sont également visibles à l'extérieur.

De cela, ES5 a une portée de fonction. Il n'y a pas de portée de bloc.

> Modifié le : 9 mai 2019

> Selon **ES5**, l'utilisation de fonctions était le seul moyen de déclarer une portée de bloc dans le code.

> Mais, dans ES6, cela a été simplifié par les mots-clés **let** et **const** qui fournissent une portée de bloc.

> Quoi qu'il en soit, il est préférable d'avoir une connaissance de la manière dont JavaScript a évolué étape par étape.

Continuons cela dans la version ES5 :

```javascript
var a = 10;
function app(){
   var b = 2;
   console.log(a); // 10
   console.log(b); // 2
}
console.log(b); //   ReferenceError: b is not defined
app();
```

Comme nous le savons déjà, **a** est une variable globale et **b** est une variable locale qui est **spécifique** à la fonction app.

Nous ne pouvons pas obtenir la valeur d'une variable locale en dehors de la portée locale.

#### Utilisation d'une fonction imbriquée — Fonction à l'intérieur d'une fonction

```js
var a = 10;
function app(){
     var b = 2;
     var d = 3;
  function add(){
     var c = a + b;
   }
 return add;
}
var x = app();
console.dir(x);
```

Ici, app est la fonction parente et add est la fonction enfant.

* Plutôt que d'utiliser console.log, **console.dir** est utilisé pour afficher toutes les propriétés d'un objet JavaScript spécifié, ce qui aide les développeurs à obtenir les propriétés de cet objet.
* La variable x est assignée à la fonction app et la fonction app retourne la fonction add. Par conséquent, nous pourrions voir toutes les propriétés de l'objet de la fonction add.

Si vous regardez la console dans le navigateur, vous pourriez voir l'objet Closure à l'intérieur du tableau Scopes.

![Image](https://cdn-media-1.freecodecamp.org/images/QT8fuXZHAuL9OPxS3M2v7nI2hF7c4rX1zt3U)

Puisque la fonction interne **add** accède aux variables de la fonction externe **b & d**, ces 2 variables seront ajoutées à l'objet Closure pour référence.

Regardons l'exemple suivant pour Closure :

```js
var a = 10;
var startFunc;
function app(){
      var b = 2;
   function add(){
      var c = a + b;
      console.log(c);
   }
   startFunc = add();
}
app(); // Invoquer la fonction app
startFunc; 
// comme la fonction app invoquée ci-dessus assignera la fonction add à startFunc et affichera la valeur de c
```

* Une fonction globale appelée startFunc est assignée à la fonction add qui est une fonction enfant de la fonction parente app.
* Cela n'est possible qu'après l'invocation de la fonction app, sinon startFunc agira comme une variable globale sans aucune valeur assignée.

#### Application des fermetures en JavaScript

La plupart d'entre nous utilisent les fermetures lors du codage, mais nous ne comprenons pas pourquoi nous les utilisons. JavaScript n'a pas les modificateurs d'accès comme **private, public, protected** comme les autres langages de programmation orientés objet. Nous devons donc utiliser des fonctions pour protéger l'espace de noms du code externe dans ES5.

En particulier dans les fonctions, l'**expression de fonction immédiatement invoquée (IIFE)** est celle qui est exécutée immédiatement après la déclaration. Vous n'avez pas besoin d'invoquer la fonction après sa déclaration.

IIFE permet d'écrire le **modèle de module** (l'un des modèles de conception) en JavaScript.

La définition de la syntaxe de IIFE est :

```
(function(){
             // variables et portée à l'intérieur de la fonction 
})();
```

Prenons un exemple :

```js
var studnetEnrollment = (function () {
    // variables privées que personne ne peut changer
    // sauf la fonction déclarée ci-dessous.
     var count = 0;
     var prefix = "S";
    // retourne une expression de fonction nommée
     function innerFunc() {
         count = count + 1;
         return prefix + count;
     };
 return innerFunc;
})();
var x = studnetEnrollment(); // S1
console.log(x);
var y = studnetEnrollment(); // S2 
console.log(y);
```

count et prefix sont les 2 variables privées qui ne peuvent pas être modifiées par quiconque et ne sont accessibles qu'à la fonction interne (ici innerFunc). Cet accès n'est possible que grâce à la fonctionnalité appelée Closure.

* La première fois, lorsque la fonction studentEnrollment est appelée, la variable count à l'intérieur de la fonction est incrémentée de 1 par la fonction innerFunc.
* La deuxième fois, le count est incrémenté de la valeur précédente de count qui est 1 à 2.
* Cela est possible grâce à la fonctionnalité Closure.

#### Conclusion

La fermeture (Closure) est une collection de variables dans une fonction externe qui donne accès à la portée de la fonction interne pour protéger l'espace de noms global.

Les fermetures permettent aux développeurs d'écrire un code propre comme les langages OOP qui ne confondent pas les noms de variables globales et locales dans la version ES5.

Bon codage...!!!!!