---
title: Un guide simple pour vous aider à comprendre les closures en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-16T19:10:53.000Z'
originalURL: https://freecodecamp.org/news/javascript-closures-simplified-d0d23fa06ba4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tKGo4CSTcfWAO6-dTsb03g.jpeg
tags:
- name: closure
  slug: closure
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Un guide simple pour vous aider à comprendre les closures en JavaScript
seo_desc: 'By Prashant Ram

  Closures in JavaScript are one of those concepts that many struggle to get their
  heads around. In the following article, I will explain in clear terms what a closure
  is, and I’ll drive the point home using simple code examples.

  What i...'
---

Par Prashant Ram

Les closures en JavaScript sont l'un de ces concepts que beaucoup ont du mal à comprendre. Dans l'article suivant, je vais expliquer en termes clairs ce qu'est une closure, et je vais illustrer cela avec des exemples de code simples.

### Qu'est-ce qu'une closure ?

Une closure est une fonctionnalité en JavaScript où une fonction interne a accès aux variables de la fonction externe (enclosante) — une chaîne de portée.

La closure a trois chaînes de portée :

* elle a accès à sa propre portée — les variables définies entre ses accolades
* elle a accès aux variables de la fonction externe
* elle a accès aux variables globales

Pour les non-initiés, cette définition peut sembler être un simple jargon !

### **Mais qu'est-ce qu'une closure, vraiment ?**

#### Une closure simple

Examinons un exemple simple de closure en JavaScript :

```js
function outer() {

   var b = 10;
   function inner() {
        
         var a = 20; 
         console.log(a+b);
    }
   return inner;
}
```

Ici, nous avons deux fonctions :

* une fonction externe `outer` qui a une variable `b`, et retourne la fonction `inner`
* une fonction interne `inner` qui a sa propre variable appelée `a`, et accède à une variable `b` de `outer`, dans son corps de fonction

La portée de la variable `b` est limitée à la fonction `outer`, et la portée de la variable `a` est limitée à la fonction `inner`.

Invocons maintenant la fonction `outer()`, et stockons le résultat de la fonction `outer()` dans une variable `X`. Invocons ensuite la fonction `outer()` une deuxième fois et stockons-la dans la variable `Y`.

```js
function outer() {
  var b = 10;
  function inner() {
    var a = 20;
    console.log(a + b);
  }
  return inner;
}

var X = outer(); // outer() invoquée la première fois
var Y = outer(); // outer() invoquée la deuxième fois
```

Examinons étape par étape ce qui se passe lorsque la fonction `outer()` est invoquée pour la première fois :

1. La variable `b` est créée, sa portée est limitée à la fonction `outer()`, et sa valeur est définie à `10`.
2. La ligne suivante est une déclaration de fonction, donc rien à exécuter.
3. Sur la dernière ligne, `return inner` cherche une variable appelée `inner`, trouve que cette variable `inner` est en fait une fonction, et retourne donc tout le corps de la fonction `inner`.
[Notez que l'instruction `return` n'exécute pas la fonction interne — une fonction n'est exécutée que lorsqu'elle est suivie de `()` — mais plutôt l'instruction `return` retourne tout le corps de la fonction.]
4. Le contenu retourné par l'instruction `return` est stocké dans `X`.
Ainsi, `X` stockera ce qui suit :
 `function inner() {`   
 `var a=20;`   
`console.log(a+b);`   
`}`
5. La fonction `outer()` termine son exécution, et toutes les variables dans la portée de `outer()` n'existent plus.

Cette dernière partie est importante à comprendre. Une fois qu'une fonction a terminé son exécution, toutes les variables qui étaient définies dans la portée de la fonction cessent d'exister.

La durée de vie d'une variable définie à l'intérieur d'une fonction est la durée de vie de l'exécution de la fonction.

Cela signifie que dans `console.log(a+b)`, la variable `b` n'existe que pendant l'exécution de la fonction `outer()`. Une fois que la fonction `outer` a terminé son exécution, la variable `b` n'existe plus.

Lorsque la fonction est exécutée une deuxième fois, les variables de la fonction sont créées à nouveau, et vivent seulement jusqu'à ce que la fonction termine son exécution.

Ainsi, lorsque `outer()` est invoquée la deuxième fois :

1. Une nouvelle variable `b` est créée, sa portée est limitée à la fonction `outer()`, et sa valeur est définie à `10`.
2. La ligne suivante est une déclaration de fonction, donc rien à exécuter.
3. `return inner` retourne tout le corps de la fonction `inner`.
4. Le contenu retourné par l'instruction `return` est stocké dans `Y`.
5. La fonction `outer()` termine son exécution, et toutes les variables dans la portée de `outer()` n'existent plus.

Le point important ici est que lorsque la fonction `outer()` est invoquée la deuxième fois, la variable `b` est créée à nouveau. De plus, lorsque la fonction `outer()` termine son exécution la deuxième fois, cette nouvelle variable `b` cesse à nouveau d'exister.

C'est le point le plus important à réaliser. Les variables à l'intérieur des fonctions n'existent que lorsque la fonction est en cours d'exécution, et cessent d'exister une fois que la fonction a terminé son exécution.

Revenons maintenant à notre exemple de code et examinons `X` et `Y`. Puisque la fonction `outer()` retourne une fonction lors de son exécution, les variables `X` et `Y` sont des fonctions.

Cela peut être facilement vérifié en ajoutant ce qui suit au code JavaScript :

```js
console.log(typeof(X)); // X est de type fonction
console.log(typeof(Y)); // Y est de type fonction
```

Puisque les variables `X` et `Y` sont des fonctions, nous pouvons les exécuter. En JavaScript, une fonction peut être exécutée en ajoutant `()` après le nom de la fonction, comme `X()` et `Y()`.

```js
function outer() {

var b = 10;
   function inner() {
        
         var a = 20; 
         console.log(a+b);
    }
   return inner;
}

var X = outer(); 
var Y = outer(); 
// fin des exécutions de la fonction outer()

X(); // X() invoquée la première fois
X(); // X() invoquée la deuxième fois
X(); // X() invoquée la troisième fois

Y(); // Y() invoquée la première fois
```

Lorsque nous exécutons `X()` et `Y()`, nous exécutons essentiellement la fonction `inner`.

Examinons étape par étape ce qui se passe lorsque `X()` est exécutée la première fois :

1. La variable `a` est créée, et sa valeur est définie à `20`.
2. JavaScript essaie maintenant d'exécuter `a + b`. C'est là que les choses deviennent intéressantes. JavaScript sait que `a` existe puisque c'est lui qui vient de la créer. Cependant, la variable `b` n'existe plus. Puisque `b` fait partie de la fonction externe, `b` n'existerait que pendant l'exécution de la fonction `outer()`. Puisque la fonction `outer()` a terminé son exécution bien avant que nous n'invoquions `X()`, toutes les variables dans la portée de la fonction `outer` cessent d'exister, et donc la variable `b` n'existe plus.

Comment JavaScript gère-t-il cela ?

#### _Closures_

La fonction `inner` peut accéder aux variables de la fonction englobante grâce aux closures en JavaScript. En d'autres termes, la fonction `inner` préserve la chaîne de portée de la fonction englobante au moment où la fonction englobante a été exécutée, et peut ainsi accéder aux variables de la fonction englobante.

Dans notre exemple, la fonction `inner` avait préservé la valeur de `b=10` lorsque la fonction `outer()` a été exécutée, et a continué à la préserver (closure).

Elle se réfère maintenant à sa chaîne de portée et remarque qu'elle a bien la valeur de la variable `b` dans sa chaîne de portée, puisqu'elle avait enfermé la valeur de `b` dans une closure au moment où la fonction `outer` avait été exécutée.

Ainsi, JavaScript connaît `a=20` et `b=10`, et peut calculer `a+b`.

Vous pouvez vérifier cela en ajoutant la ligne de code suivante à l'exemple ci-dessus :

```js
function outer() {

  var b = 10;
  function inner() {
  
    var a = 20;
    console.log(a + b);
  }
  return inner;
}

var X = outer();

console.dir(X); // utilisez console.dir() au lieu de console.log()

```

Ouvrez l'élément Inspect dans Google Chrome et allez dans la Console. Vous pouvez développer l'élément pour voir réellement l'élément `Closure` (affiché dans l'avant-dernière ligne ci-dessous). Remarquez que la valeur de `b=10` est préservée dans la `Closure` même après que la fonction `outer()` ait terminé son exécution.

![Image](https://cdn-media-1.freecodecamp.org/images/VBcoedHEMM5cpIF4A1yTVFxTEn6ZzgYvTAGW)
_La variable b=10 est préservée dans la Closure, Closures en JavaScript_

Revenons maintenant à la définition des closures que nous avons vue au début et voyons si elle a maintenant plus de sens.

Ainsi, la fonction interne a trois chaînes de portée :

* accès à sa propre portée — variable `a`
* accès aux variables de la fonction `outer` — variable `b`, qu'elle a enfermée
* accès à toute variable globale qui peut être définie

### Closures en action

Pour bien comprendre les closures, enrichissons l'exemple en ajoutant trois lignes de code :

```js
function outer() {

  var b = 10;
  var c = 100;
  
  function inner() {
  
    var a = 20;
    console.log("a= " + a + " b= " + b);
    
    a++;
    b++;
    
  }
  return inner;
}

var X = outer(); // outer() invoquée la première fois
var Y = outer();  // outer() invoquée la deuxième fois
// fin des exécutions de la fonction outer()

X(); // X() invoquée la première fois
X(); // X() invoquée la deuxième fois
X(); // X() invoquée la troisième fois

Y(); // Y() invoquée la première fois

```

Lorsque vous exécutez ce code, vous verrez la sortie suivante dans la `console.log` :

```
a=20 b=10
a=20 b=11
a=20 b=12
a=20 b=10
```

Examinons ce code étape par étape pour voir exactement ce qui se passe et pour voir les closures en action !

```js
var X = outer();  // outer() invoquée la première fois
```

La fonction `outer()` est invoquée la première fois. Les étapes suivantes ont lieu :

1. La variable `b` est créée, et est définie à `10`
La variable `c` est créée, et définie à `100`
Appelons cela `b(premiere_fois)` et `c(premiere_fois)` pour notre propre référence.
2. La fonction `inner` est retournée et assignée à `X`
À ce stade, la variable `b` est enfermée dans la chaîne de portée de la fonction `inner` en tant que closure avec `b=10`, puisque `inner` utilise la variable `b`.
3. La fonction `outer` termine son exécution, et toutes ses variables cessent d'exister. La variable `c` n'existe plus, bien que la variable `b` existe en tant que closure dans `inner`.

```js
var Y= outer();  // outer() invoquée la deuxième fois
```

1. La variable `b` est créée à nouveau et est définie à `10`
La variable `c` est créée à nouveau.
Notez que même si `outer()` a été exécutée une fois auparavant, les variables `b` et `c` ont cessé d'exister une fois que la fonction a terminé son exécution, elles sont créées en tant que nouvelles variables.
Appelons celles-ci `b(deuxieme_fois)` et `c(deuxieme_fois)` pour notre propre référence.
2. La fonction `inner` est retournée et assignée à `Y`
À ce stade, la variable `b` est enfermée dans la chaîne de portée de la fonction `inner` en tant que closure avec `b(deuxieme_fois)=10`, puisque `inner` utilise la variable `b`.
3. La fonction `outer` termine son exécution, et toutes ses variables cessent d'exister.
La variable `c(deuxieme_fois)` n'existe plus, bien que la variable `b(deuxieme_fois)` existe en tant que closure dans `inner`.

Voyons maintenant ce qui se passe lorsque les lignes de code suivantes sont exécutées :

```js
X(); // X() invoquée la première fois
X(); // X() invoquée la deuxième fois
X(); // X() invoquée la troisième fois

Y(); // Y() invoquée la première fois
```

Lorsque `X()` est invoquée la première fois,

1. la variable `a` est créée, et définie à `20`
2. la valeur de `a=20`, la valeur de `b` est celle de la closure. `b(premiere_fois)`, donc `b=10`
3. les variables `a` et `b` sont incrémentées de `1`
4. `X()` termine son exécution et toutes ses variables internes — la variable `a` — cessent d'exister.
Cependant, `b(premiere_fois)` a été préservée en tant que closure, donc `b(premiere_fois)` continue d'exister.

Lorsque `X()` est invoquée la deuxième fois,

1. la variable `a` est créée à nouveau, et définie à `20`
Toute valeur précédente de la variable `a` n'existe plus, puisqu'elle a cessé d'exister lorsque `X()` a terminé son exécution la première fois.
2. la valeur de `a=20`
la valeur de `b` est prise à partir de la valeur de la closure — `b(premiere_fois)`
Notez également que nous avions incrémenté la valeur de `b` de `1` à partir de l'exécution précédente, donc `b=11`
3. les variables `a` et `b` sont incrémentées de `1` à nouveau
4. `X()` termine son exécution et toutes ses variables internes — la variable `a` — cessent d'exister
Cependant, `b(premiere_fois)` est préservée puisque la closure continue d'exister.

Lorsque `X()` est invoquée la troisième fois,

1. la variable `a` est créée à nouveau, et définie à `20`
Toute valeur précédente de la variable `a` n'existe plus, puisqu'elle a cessé d'exister lorsque `X()` a terminé son exécution la première fois.
2. la valeur de `a=20`, la valeur de `b` est celle de la closure — `b(premiere_fois)`
Notez également que nous avions incrémenté la valeur de `b` de `1` dans l'exécution précédente, donc `b=12`
3. les variables `a` et `b` sont incrémentées de `1` à nouveau
4. `X()` termine son exécution, et toutes ses variables internes — la variable `a` — cessent d'exister
Cependant, `b(premiere_fois)` est préservée puisque la closure continue d'exister

Lorsque Y() est invoquée la première fois,

1. la variable `a` est créée à nouveau, et définie à `20`
2. la valeur de `a=20`, la valeur de `b` est celle de la closure — `b(deuxieme_fois)`, donc `b=10`
3. les variables `a` et `b` sont incrémentées de `1`
4. `Y()` termine son exécution, et toutes ses variables internes — la variable `a` — cessent d'exister
Cependant, `b(deuxieme_fois)` a été préservée en tant que closure, donc `b(deuxieme_fois)` continue d'exister.

### Remarques finales

Les closures sont l'un de ces concepts subtils en JavaScript qui sont difficiles à saisir au début. Mais une fois que vous les comprenez, vous réalisez que les choses n'auraient pas pu être autrement.

Espérons que ces explications étape par étape vous ont vraiment aidé à comprendre le concept des closures en JavaScript !

**Autres articles :**

* [Comment utiliser les Promesses en JavaScript](https://www.freecodecamp.org/news/promises-in-javascript-explained-277b98850de/)
* [Comment créer une animation Sprite simple en JavaScript](https://medium.com/@prashantramnyc/how-to-build-a-simple-sprite-animation-in-javascript-b764644244aa)