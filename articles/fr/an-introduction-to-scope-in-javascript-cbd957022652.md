---
title: Une introduction à la portée en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-01T18:01:35.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-scope-in-javascript-cbd957022652
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4YCJhT2ZeEMP7YxQbgVCyg.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Une introduction à la portée en JavaScript
seo_desc: 'By Cristian Salcescu

  Scope defines the lifetime and visibility of a variable. Variables are not visible
  outside the scope in which they are declared.

  JavaScript has module scope, function scope, block scope, lexical scope and global
  scope.

  Global Sco...'
---

Par Cristian Salcescu

La portée définit la durée de vie et la visibilité d'une variable. Les variables ne sont pas visibles en dehors de la portée dans laquelle elles sont déclarées.

JavaScript a une portée de module, une portée de fonction, une portée de bloc, une portée lexicale et une portée globale.

### Portée globale

Les variables définies en dehors de toute fonction, bloc ou portée de module ont une portée globale. Les variables dans la portée globale peuvent être accessibles de partout dans l'application.

Lorsque le système de modules est activé, il est plus difficile de créer des variables globales, mais on peut toujours le faire. En définissant une variable en HTML, en dehors de toute fonction, une variable globale peut être créée :

```
<script>
  let GLOBAL_DATA = { value : 1};
</script>

console.log(GLOBAL_DATA);
```

Lorsque le système de modules n'est pas en place, il est beaucoup plus facile de créer des variables globales. Une variable déclarée en dehors de toute fonction, dans n'importe quel fichier, est une variable globale.

Les variables globales sont disponibles pendant toute la durée de vie de l'application.

Une autre façon de créer une variable globale est d'utiliser l'objet global `window` n'importe où dans l'application :

```
window.GLOBAL_DATA = { value: 1 };
```

À ce stade, la variable `GLOBAL_DATA` est visible partout.

```
console.log(GLOBAL_DATA)
```

Comme vous pouvez l'imaginer, ces pratiques sont de mauvaises pratiques.

### Portée de module

Avant les modules, une variable déclarée en dehors de toute fonction était une variable globale. Dans les modules, une variable déclarée en dehors de toute fonction est masquée et non disponible pour les autres modules, sauf si elle est explicitement exportée.

L'exportation rend une fonction ou un objet disponible pour d'autres modules. Dans l'exemple suivant, j'export une fonction depuis le fichier de module `sequence.js` :

```
// dans sequence.js
export { sequence, toList, take };
```

L'importation rend une fonction ou un objet, provenant d'autres modules, disponible pour le module actuel.

```
import { sequence, toList, toList } from "./sequence";
```

D'une certaine manière, nous pouvons imaginer un module comme une fonction auto-exécutante qui prend les données d'importation comme entrées et retourne les données d'exportation.

### Portée de fonction

La portée de fonction signifie que les paramètres et les variables définis dans une fonction sont visibles partout dans la fonction, mais ne sont pas visibles en dehors de la fonction.

Considérons la fonction suivante qui s'auto-exécute, appelée IIFE.

```
(function autoexecute() {
    let x = 1;
})();

console.log(x);
//Uncaught ReferenceError: x is not defined
```

IIFE signifie Immediately Invoked Function Expression et est une fonction qui s'exécute immédiatement après sa définition.

Les variables déclarées avec `var` n'ont que la portée de fonction. De plus, les variables déclarées avec `var` sont remontées en haut de leur portée. Ainsi, elles peuvent être accessibles avant d'être déclarées. Regardez le code ci-dessous :

```
function doSomething(){
  console.log(x);
  var x = 1;
}

doSomething(); //undefined
```

Cela ne se produit pas pour `let`. Une variable déclarée avec `let` ne peut être accessible qu'après sa définition.

```
function doSomething(){
  console.log(x);
  let x = 1;
}

doSomething();
//Uncaught ReferenceError: x is not defined
```

Une variable déclarée avec `var` peut être redéclarée plusieurs fois dans la même portée. Le code suivant est correct :

```
function doSomething(){
  var x = 1
  var x = 2;
  console.log(x);
}

doSomething();
```

Les variables déclarées avec `let` ou `const` ne peuvent pas être redéclarées dans la même portée :

```
function doSomething(){
  let x = 1
  let x = 2;
}
//Uncaught SyntaxError: Identifier 'x' has already been declared
```

Peut-être n'avons-nous même pas à nous soucier de cela, car `var` commence à devenir obsolète.

### Portée de bloc

La portée de bloc est définie avec des accolades. Elle est séparée par `{` et `}`.

Les variables déclarées avec `let` et `const` peuvent avoir une portée de bloc. Elles ne peuvent être accessibles que dans le bloc dans lequel elles sont définies.

Considérons le code suivant qui met en évidence la portée de bloc `let` :

```
let x = 1;
{ 
  let x = 2;
}
console.log(x); //1
```

En revanche, la déclaration `var` n'a pas de portée de bloc :

```
var x = 1;
{ 
  var x = 2;
}
console.log(x); //2
```

Un autre problème courant lié à l'absence de portée de bloc est l'utilisation d'une opération asynchrone comme `setTimeout()` dans une boucle. Le code de boucle suivant affiche le nombre 5, cinq fois.

```
(function run(){
    for(var i=0; i<5; i++){
        setTimeout(function logValue(){
            console.log(i);         //5
        }, 100);
    }
})();
```

L'instruction de boucle `for`, avec la déclaration `let`, crée une nouvelle variable locale à la portée de bloc, pour chaque itération. Le code de boucle suivant montre `0 1 2 3 4 5`.

```
(function run(){
  for(let i=0; i<5; i++){
    setTimeout(function log(){
      console.log(i); //0 1 2 3 4
    }, 100);
  }
})();
```

### Portée lexicale

La portée lexicale est la capacité de la fonction interne à accéder à la portée externe dans laquelle elle est définie.

[Considérons le code suivant](https://jsfiddle.net/cristi_salcescu/pcg6fab7/) :

```
(function autorun(){
    let x = 1;
    function log(){
      console.log(x);
    };
    
    function run(fn){
      let x = 100;
      fn();
    }
    
    run(log);//1
})();
```

La fonction `log` est une fermeture. Elle fait référence à la variable `x` de sa fonction parente `autorun()`, et non à celle de la fonction `run()`.

La fonction de fermeture a accès à la portée dans laquelle elle a été créée, et non à la portée dans laquelle elle a été exécutée.

La portée de fonction locale de `autorun()` est la portée lexicale de la fonction `log()`.

### Chaîne de portée

Chaque portée a un lien vers la portée parente. Lorsqu'une variable est utilisée, JavaScript parcourt la chaîne de portée jusqu'à ce qu'il trouve la variable demandée ou jusqu'à ce qu'il atteigne la portée globale, qui est la fin de la chaîne de portée.

[Regardez l'exemple suivant](https://jsfiddle.net/cristi_salcescu/udq46asp/) :

```
let x0 = 0;
(function autorun1(){
 let x1 = 1;
  
 (function autorun2(){
   let x2 = 2;
  
   (function autorun3(){
     let x3 = 3;
      
     console.log(x0 + " " + x1 + " " + x2 + " " + x3);//0 1 2 3
    })();
  })();
})();
```

La fonction interne `autorun3()` a accès à la variable locale `x3`. Elle a également accès aux variables `x1` et `x2` des fonctions externes et à la variable globale `x0`.

Si elle ne trouve pas la variable, elle retournera une erreur en mode strict.

```
"use strict";
x = 1;
console.log(x)
//Uncaught ReferenceError: x is not defined
```

En mode non strict, appelé "mode négligé", il fera une mauvaise chose et créera une variable globale.

```
x = 1;
console.log(x); //1
```

### Conclusion

Les variables définies dans la portée globale sont disponibles partout dans l'application.

Dans un module, une variable déclarée en dehors de toute fonction est masquée et non disponible pour les autres modules, sauf si elle est explicitement exportée.

La portée de fonction signifie que les paramètres et les variables définis dans une fonction sont visibles partout dans la fonction.

Les variables déclarées avec `let` et `const` ont une portée de bloc. `var` n'a pas de portée de bloc.

[**Découvrez Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour plus d'informations sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)