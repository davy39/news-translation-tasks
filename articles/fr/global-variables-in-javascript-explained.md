---
title: Variables globales en JavaScript expliquées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T22:41:00.000Z'
originalURL: https://freecodecamp.org/news/global-variables-in-javascript-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d77740569d1a4ca37e7.jpg
tags:
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: Variables globales en JavaScript expliquées
seo_desc: Global variables are declared outside of a function for accessibility throughout
  the program, while local variables are stored within a function using var for use
  only within that function’s scope. If you declare a variable without using var,
  even if...
---

Les variables globales sont déclarées en dehors d'une fonction pour être accessibles dans tout le programme, tandis que les variables locales sont stockées dans une fonction en utilisant `var` pour être utilisées uniquement dans le [scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope) de cette fonction. Si vous déclarez une variable sans utiliser `var`, même si elle est à l'intérieur d'une fonction, elle sera toujours considérée comme globale :

```javascript
var x = 5; // globale

function someThing(y) {
  var z = x + y;
  console.log(z);
}

function someThing(y) {
  x = 5; // toujours globale !
  var z = x + y;
  console.log(z);
}


function someThing(y) {
  var x = 5; // locale
  var z = x + y;
  console.log(z);
}
```

Une variable globale est également un objet de la portée actuelle, comme la fenêtre du navigateur :

```javascript
var dog = "Fluffy";
console.log(dog); // Fluffy;

var dog = "Fluffy";
console.log(window.dog); // Fluffy
```

Il est recommandé de minimiser l'utilisation des variables globales. Puisque la variable peut être accessible n'importe où dans le programme, elles peuvent causer des comportements étranges.

Références :

* [var -Javascript|MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
* [You Don’t Know JavaScript: Scopes & Closures](https://github.com/getify/You-Dont-Know-JS/tree/master/scope%20%26%20closures)

## **[Quelle est la différence entre une variable globale et une variable window.variable en JavaScript ?](https://stackoverflow.com/questions/6349232/whats-the-difference-between-a-global-var-and-a-window-variable-in-javascript)**

La portée des variables JavaScript est soit globale, soit locale. Les variables globales sont déclarées EN DEHORS de la fonction et leur valeur est accessible/modifiable dans tout le programme.

Vous devez TOUJOURS utiliser **var** pour déclarer vos variables (pour les rendre locales) sinon elles seront installées GLOBALLEMENT.

Faites attention avec les variables globales car elles sont risquées. La plupart du temps, vous devriez utiliser des closures pour déclarer vos variables. Exemple :

```javascript
(function(){
  var myVar = true;
})();
```

## **Plus d'informations :**

* [Guide visuel des définitions et de la portée des variables JavaScript](https://www.freecodecamp.org/news/the-visual-guide-to-javascript-variable-definitions-scope-2717ad9f0169/)
* [Introduction aux définitions de variables JavaScript et au hoisting](https://www.freecodecamp.org/news/a-basic-introduction-to-javascript-variable-definitions-and-hoisting-93aa38e742eb/)