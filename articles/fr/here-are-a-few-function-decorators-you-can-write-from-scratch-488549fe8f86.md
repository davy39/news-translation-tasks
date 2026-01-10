---
title: Voici quelques décorateurs de fonction que vous pouvez écrire à partir de zéro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-03T09:56:39.000Z'
originalURL: https://freecodecamp.org/news/here-are-a-few-function-decorators-you-can-write-from-scratch-488549fe8f86
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Qw0e4LC2Fri7dFkBY0N1cA.jpeg
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
seo_title: Voici quelques décorateurs de fonction que vous pouvez écrire à partir
  de zéro
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!


  A function decorator is a higher-order function that takes one function as an argument
  and returns another function, and...'
---

Par Cristian Salcescu

[**Découvrir JavaScript Fonctionnel**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

> Un **décorateur de fonction** est une fonction d'ordre supérieur qui prend une fonction comme argument et retourne une autre fonction, et la fonction retournée est une variation de la fonction argument — [Javascript Allongé](https://leanpub.com/javascript-allonge/read#decorators)

Écrivons quelques décorateurs de fonction courants trouvés dans des bibliothèques comme [underscore.js](http://underscorejs.org/#functions), [lodash.js](https://lodash.com/docs/4.17.5) ou [ramda.js](http://ramdajs.com/docs/).

### once()

* [once(fn)](https://jsfiddle.net/cristi_salcescu/zpLeLp0v/) : crée une version de la fonction qui ne s'exécute qu'une seule fois. C'est utile pour une fonction d'initialisation, où nous voulons nous assurer qu'elle ne s'exécute qu'une seule fois, peu importe le nombre de fois où elle est appelée depuis différents endroits.

```
function once(fn){
  let returnValue;
  let canRun = true;
  return function runOnce(){
      if(canRun) {
          returnValue = fn.apply(this, arguments);
          canRun = false;
      }
      return returnValue;
  }
}

var processonce = once(process);
processonce(); //process
processonce(); //
```

`once()` est une fonction qui retourne une autre fonction. La fonction retournée `runOnce()` est une [fermeture](https://medium.freecodecamp.org/why-you-should-give-the-closure-function-another-chance-31253e44cfa0). Il est également important de noter comment la fonction originale a été appelée — en passant la valeur actuelle de `this` et tous les `arguments` : `fn.apply(this, arguments)`.

> Si vous voulez mieux comprendre les fermetures, consultez [Pourquoi vous devriez donner une autre chance à la fonction Closure](https://medium.freecodecamp.org/why-you-should-give-the-closure-function-another-chance-31253e44cfa0).

### after()

* [after(count, fn)](https://jsfiddle.net/cristi_salcescu/4evuoxe6/) : crée une version de la fonction qui ne s'exécute qu'après un certain nombre d'appels. C'est utile, par exemple, lorsque nous voulons nous assurer que la fonction ne s'exécute qu'après que toutes les tâches asynchrones ont été terminées.

```
function after(count, fn){
   let runCount = 0;
   return function runAfter(){
      runCount = runCount + 1;
      if (runCount >= count) {
         return fn.apply(this, arguments);        
      }
   }
}

function logResult() { console.log("les appels sont terminés"); }

let logResultAfter2Calls = after(2, logResult);
setTimeout(function logFirstCall() { 
      console.log("le 1er appel est terminé"); 
      logResultAfter2Calls(); 
}, 3000);

setTimeout(function logSecondCall() { 
      console.log("le 2ème appel est terminé"); 
      logResultAfter2Calls(); 
}, 4000);
```

Remarquez comment j'utilise `after()` pour créer une nouvelle fonction `logResultAfter2Calls()` qui exécutera le code original de `logResult()` uniquement après le deuxième appel.

### throttle()

* [throttle(fn, wait)](https://jsfiddle.net/cristi_salcescu/5tdv0eq6/) : crée une version de la fonction qui, lorsqu'elle est invoquée à plusieurs reprises, appellera la fonction originale une fois toutes les `wait` millisecondes. C'est utile pour limiter les événements qui se produisent plus rapidement.

```
function throttle(fn, interval) {
    let lastTime;
    return function throttled() {
        let timeSinceLastExecution = Date.now() - lastTime;
        if(!lastTime || (timeSinceLastExecution >= interval)) {
            fn.apply(this, arguments);
            lastTime = Date.now();
        }
    };
}

let throttledProcess = throttle(process, 1000);
$(window).mousemove(throttledProcess);
```

Dans cet exemple, le déplacement de la souris générera beaucoup d'événements `mousemove`, mais l'appel de la fonction originale `process()` ne se produira qu'une fois par seconde.

[**Découvrir JavaScript Fonctionnel**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Architecture Fonctionnelle avec React et Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**