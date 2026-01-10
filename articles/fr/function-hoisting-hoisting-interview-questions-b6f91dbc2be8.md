---
title: Hoisting de Fonctions & Questions d'Entretien sur le Hoisting
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-06T22:20:40.000Z'
originalURL: https://freecodecamp.org/news/function-hoisting-hoisting-interview-questions-b6f91dbc2be8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*v7kHrep8UBwgPvFz0gWutw.jpeg
tags:
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Hoisting de Fonctions & Questions d'Entretien sur le Hoisting
seo_desc: 'By Bhuvan Malik

  This is a part 2 for my previous article on Hoisting titled “A guide to JavaScript
  variable hoisting ? with let and const”. So make sure you read that before diving
  into this one.

  Previously I talked about variable hoisting only becau...'
---

Par Bhuvan Malik

Ceci est la partie 2 de mon précédent article sur le Hoisting intitulé « [Un guide sur le hoisting des variables JavaScript ? avec let et const](https://medium.freecodecamp.org/what-is-variable-hoisting-differentiating-between-var-let-and-const-in-es6-f1a70bb43d) ». Assurez-vous donc de le lire avant de plonger dans celui-ci.

Précédemment, j'ai parlé uniquement du hoisting des variables car le hoisting des fonctions en JavaScript n'est pas le même que le hoisting des variables, il est unique à sa manière. Je vais développer le hoisting des fonctions dans cet article, ainsi que quelques questions d'entretien courantes et délicates sur le hoisting (variables et fonctions) que toute personne passant des entretiens JavaScript est presque certaine de rencontrer.

Espérons qu'après avoir terminé ces 2 parties, vous serez prêt à cocher le Hoisting de votre liste de préparation JavaScript !

Commençons.

### Hoisting de Fonctions

Il existe 2 façons de créer des fonctions en JavaScript, via la **Déclaration de Fonction** et via l'**Expression de Fonction**. Voyons ce que sont ces méthodes et comment le hoisting les affecte.

#### Déclaration de Fonction

La **déclaration de fonction** définit une fonction avec les paramètres spécifiés.  
Syntaxe :

```
function name(param1, param2, ...) {  [instructions]}
```

En JavaScript, les déclarations de fonctions hoistent les définitions de fonctions.

Par conséquent, ces fonctions peuvent être **utilisées** avant d'être déclarées.  
Exemple :

```
hoisted() // sortie : "Hoisted"
```

```
function hoisted() {  console.log('Hoisted')}
```

En coulisses, voici comment l'interpréteur JavaScript voit le code ci-dessus :

```
// Code hoisté
function hoisted() {  console.log('Hoisted')}
```

```
// Reste du code
hoisted() // sortie : "Hoisted"
```

Ce comportement est vrai si vous avez des déclarations de fonctions dans la Portée Globale ou la Portée Fonctionnelle (basiquement la Portée Locale en JavaScript).

Cela peut être utile car vous pouvez utiliser votre logique de haut niveau au début du code, le rendant plus lisible et compréhensible.

**Note :** Ne jamais utiliser de déclarations de fonctions à l'intérieur de blocs if/else.

#### Expression de Fonction

Le mot-clé `**function**` peut également être utilisé pour définir une fonction à l'intérieur d'une expression.  
Syntaxe :

```
const myFunction = function [name](param1, param2, ...) {  [instructions]}
```

Le `[name]` est optionnel, donc celles-ci peuvent être des fonctions anonymes. Nous pouvons également utiliser des fonctions fléchées comme ceci :

```
const myFunction = (param1, param2, ...) => {  [instructions]}
```

Les expressions de fonctions en JavaScript ne sont pas hoistées.

Par conséquent, vous ne pouvez pas utiliser d'expressions de fonctions avant de les définir.  
Exemple :

```
notHoisted() // TypeError: notHoisted is not a function
```

```
const notHoisted = function() {  console.log('foo')}
```

C'est tout ce qu'il faut garder à l'esprit pour créer des fonctions du point de vue du hoisting.   
Passons maintenant à quelques questions d'entretien !

### Questions d'Entretien sur le Hoisting

Le hoisting et son comportement erratique sont un sujet brûlant lors des entretiens. En utilisant les connaissances de mon [article précédent](https://medium.freecodecamp.org/what-is-variable-hoisting-differentiating-between-var-let-and-const-in-es6-f1a70bb43d) et de celui-ci, on peut naviguer à travers toutes les questions sur le sujet. Cela dit, regardons quelques questions courantes.

#### Question 1

```
var a = 1;
```

```
function b() {  a = 10;  return;
```

```
  function a() {}}
```

```
b();
```

```
console.log(a);
```

**Sortie : 1,** Qu'est-ce que?! ?

C'est parce que l'instruction `function a() {}` a maintenant créé un `a` local qui a une portée fonctionnelle/locale. Ce nouveau `a` est maintenant hoisté en haut de sa fonction englobante `b()` avec sa déclaration et sa définition. Voici ce qui se passe en coulisses :

```
var a = 1;
```

```
function b() {  // Hoisté  function a() {}
```

```
  a = 10;  return;}
```

```
b();
```

```
console.log(a)
```

Par conséquent, l'instruction `a = 10;` ne change plus la valeur du `a` global qui reste à 1, mais change plutôt le `a` local d'une fonction à une valeur entière de 10. Puisque nous loggons le `a` global, la sortie est 1.

Si l'instruction `function a() {}` n'avait pas été là, la sortie aurait été 10.

#### Question 2

```
function foo(){    function bar() {        return 3;    }    return bar();    function bar() {        return 8;    }}alert(foo());
```

**Sortie : 8**

Les deux fonctions `bar()` sont des déclarations de fonctions et seront donc hoistées en haut de la portée locale de `foo()`. Cependant, la fonction `bar()` retournant 8 sera hoistée après celle retournant 3. Par conséquent, celle retournant 8 sera exécutée.

En coulisses :

```
function foo(){    //Hoisté avant    function bar() {        return 3;    }    // Hoisté après    function bar() {        return 8;    }
```

```
    return bar();    }alert(foo());
```

#### Question 3

```
function parent() {    var hoisted = "I'm a variable";    function hoisted() {        return "I'm a function";    }    return hoisted(); }console.log(parent());
```

**Sortie : « TypeError: hoisted is not a function »**

Celle-ci est délicate. C'est Fonction contre Variable ! Décomposons-la.

Nous savons que lorsqu'il s'agit de hoisting de variables, seule la déclaration (avec une valeur de « undefined ») est hoistée, pas la définition !

Dans le cas des déclarations de fonctions, les définitions sont également hoistées !

Maintenant, dans un tel cas de multiples déclarations (variable et fonction dans la même portée) avec le même identifiant, le hoisting des variables est simplement **IGNORÉ**. L'interpréteur rencontre la déclaration de fonction et la hoiste.   
Enfin, l'instruction d'assignation de variable (qui n'a pas été hoistée) est exécutée et « I'm a variable » est assignée à `hoisted`, qui est une simple valeur de chaîne et non une fonction. D'où l'erreur !

Voici ce qui se passe en coulisses pour ce problème :

```
function parent() {
```

```
    // Déclaration de fonction hoistée avec la définition    function hoisted() {        return "I'm a function";    }
```

```
    // Déclaration ignorée, assignation d'une chaîne    hoisted = "I'm a variable"; 
```

```
    return hoisted(); 
```

```
}console.log(parent());
```

#### Question 4

```
alert(foo());function foo() {  var bar = function() {    return 3;  };  return bar();  var bar = function() {    return 8;  };}
```

**Sortie : 3**

Celle-ci est facile. La fonction `foo()` elle-même sera hoistée dans la portée globale car c'est une déclaration de fonction. En ce qui concerne l'intérieur de `foo()`, c'est un cas clair d'expression de fonction pour les deux fonctions `bar()`.

La deuxième fonction `bar()` ne sera pas lue par l'interpréteur à l'avance (pas de hoisting). La première sera exécutée et retournée.

#### Question 5

```
var myVar = 'foo';
```

```
(function() {  console.log('Original value was: ' + myVar);  var myVar = 'bar';  console.log('New value is: ' + myVar);})();
```

**Sortie : « Original value was: undefined », « New value is: bar »**

Dans celle-ci, encore une fois, la valeur globale de `myVar` (`'foo'`) est hors de propos. C'est parce que la variable `myVar` est déclarée et définie à l'intérieur de la portée locale de la fonction et est donc hoistée en haut de l'[IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE) avec une valeur de 'undefined' qui est loggée en premier. La valeur 'bar' est ensuite assignée et loggée par la suite.

Cela conclut le Hoisting en JavaScript de mon côté. ?

J'espère que [les deux](https://medium.freecodecamp.org/what-is-variable-hoisting-differentiating-between-var-let-and-const-in-es6-f1a70bb43d) articles vous sont utiles.

Veuillez consulter l'article ci-dessous si vous souhaitez apprendre les fonctions fléchées et autres fonctionnalités ES6 liées aux fonctions.

[**JavaScript ES6 Functions: The Good Parts**](https://medium.freecodecamp.org/es6-functions-9f61c72b1e86)  
[_ES6 offre quelques fonctionnalités fonctionnelles cool qui rendent la programmation en JavaScript beaucoup plus flexible. Parlons demedium.freecodecamp.org](https://medium.freecodecamp.org/es6-functions-9f61c72b1e86)

Paix ✌️