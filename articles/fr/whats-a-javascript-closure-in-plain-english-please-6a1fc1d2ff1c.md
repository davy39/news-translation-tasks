---
title: Qu'est-ce qu'une fermeture JavaScript ? En anglais simple, s'il vous plaît.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-16T06:27:03.000Z'
originalURL: https://freecodecamp.org/news/whats-a-javascript-closure-in-plain-english-please-6a1fc1d2ff1c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*O9r2gYaYeQb7EI5KBrkf3Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce qu'une fermeture JavaScript ? En anglais simple, s'il vous plaît.
seo_desc: 'By Samer Buna

  Every function in JavaScript has a closure. And this is one of the coolest features
  of the JavaScript language. Because without closures, it would be hard to implement
  common structures like callbacks or event handlers.

  You create a clo...'
---

Par Samer Buna

Chaque fonction en JavaScript a une fermeture. Et c'est l'une des fonctionnalités les plus cool du langage JavaScript. Parce que sans les fermetures, il serait difficile de mettre en œuvre des structures courantes comme les rappels ou les gestionnaires d'événements.

Vous créez une fermeture chaque fois que vous définissez une fonction. Ensuite, lorsque vous exécutez des fonctions, leurs fermetures leur permettent d'accéder aux données dans leurs portées.

C'est un peu comme lorsque qu'une voiture est fabriquée (définie), elle vient avec quelques fonctions comme `start`, `accelerate`, `decelerate`. Ces fonctions de voiture sont exécutées par le conducteur chaque fois qu'ils utilisent la voiture. Les fermetures pour ces fonctions sont définies avec la voiture elle-même et elles _ferment_ sur les variables dont elles ont besoin pour fonctionner.

Réduisons cette analogie à la fonction `accelerate`. La définition de la fonction se produit lorsque la voiture est fabriquée :

```js
function accelerate(force) {
  // La voiture est-elle démarrée ?
  // Avons-nous du carburant ?
  // Sommes-nous en mode contrôle de traction ?
  // Beaucoup d'autres vérifications...
  // Si tout est bon, brûler plus de carburant en fonction de
  // la variable force (à quel point nous appuyons sur la pédale d'accélérateur)
}
```

Chaque fois que le conducteur appuie sur la pédale d'accélérateur, cette fonction est exécutée. Remarquez comment cette fonction a besoin d'accéder à beaucoup de variables pour fonctionner, y compris sa propre variable `force`. Mais plus important encore, elle a besoin de variables en dehors de sa portée qui sont contrôlées par d'autres fonctions de la voiture. C'est là que la fermeture de la fonction `accelerate` (que nous obtenons avec la voiture elle-même) devient utile.

Voici ce que la fermeture de la fonction `accelerate` a promis à la fonction `accelerate` elle-même :

> Ok `_accelerate_`, lorsque vous êtes exécutée, vous pouvez accéder à votre variable `_force_`, vous pouvez accéder à la variable `_isCarStarted_`, vous pouvez également accéder à la variable `_fuelLevel_`, et à la variable `_isTractionControlOn_`. Vous pouvez également contrôler la variable `_currentFuelSupply_` que nous envoyons au moteur.

Notez que la fermeture n'a pas donné à la fonction `accelerate` des valeurs _fixes_ pour ces variables, mais plutôt la _permission_ d'accéder à ces valeurs au moment où la fonction accelerate est exécutée.

Les fermetures sont étroitement liées aux [portées de fonction](https://edgecoders.com/function-scopes-and-block-scopes-in-javascript-25bbd7f293d7#.juf2mvr1i), donc comprendre comment ces portées fonctionnent vous aidera à comprendre les fermetures. En bref, la chose la plus importante à comprendre sur les portées est que lorsque vous _exécutez_ une fonction, une portée de fonction privée est créée et utilisée pour le processus d'exécution de cette fonction.

Ensuite, ces portées de fonction deviennent imbriquées lorsque vous exécutez des fonctions à partir de fonctions (ce que vous ferez tout le temps).

Une fermeture est créée lorsque vous _définissez_ une fonction — pas lorsque vous l'exécutez. Ensuite, chaque fois que vous exécutez cette fonction, sa fermeture déjà définie lui donne accès à toutes les portées de fonction disponibles autour d'elle.

D'une certaine manière, vous pouvez penser aux portées comme temporaires (la portée globale est la seule exception à cela), tandis que vous pouvez penser aux fermetures elles-mêmes comme permanentes.

![Image](https://cdn-media-1.freecodecamp.org/images/HgBIWZNKeo1S0jKBgNj4BLPmZDOqTi-gt3Np)
_Une fermeture telle que rapportée dans les outils de développement Chrome_

Pour vraiment comprendre les fermetures et le rôle qu'elles jouent en JavaScript, vous devez d'abord comprendre quelques autres concepts simples sur les fonctions JavaScript et leurs portées.

Avant de commencer, notez que j'ai également créé un laboratoire interactif pour cela, que vous pouvez parcourir [ici](https://jscomplete.com/what-are-closures-in-javascript).

### 1 — Les fonctions sont assignées par référence de valeur

Lorsque vous mettez une fonction dans une variable comme ceci :

```js
function sayHello() {
  console.log("hello");
};
var func = sayHello;
```

Vous assigner à la variable `func` une référence à la fonction `sayHello`, _pas_ une copie. Ici, `func` est simplement un alias pour `sayHello`. Tout ce que vous faites sur l'alias, vous le ferez en réalité sur la fonction originale. Par exemple :

```js
func.answer = 42;
console.log(sayHello.answer); // affiche 42
```

La propriété `answer` a été définie directement sur `func` et lue en utilisant `sayHello`, ce qui fonctionne.

Vous pouvez également exécuter `sayHello` en exécutant l'alias `func` :

```js
func() // affiche "hello"
```

### 2 — Les portées ont une durée de vie

Lorsque vous appelez une fonction, vous créez une portée pendant l'exécution de cette fonction. Ensuite, cette portée disparaît.

Lorsque vous appelez la fonction une deuxième fois, vous créez une nouvelle portée différente pendant la deuxième exécution. Ensuite, cette deuxième portée disparaît également.

```js
function printA() {
  console.log(answer);
  var answer = 1;
};
printA(); // cela crée une portée qui est jetée immédiatement après
printA(); // cela crée une nouvelle portée différente qui est également jetée immédiatement après;
```

Ces deux portées qui ont été créées dans l'exemple ci-dessus sont différentes. La variable `answer` ici n'est pas partagée entre elles du tout.

Chaque portée de fonction a une durée de vie. Elles sont créées et jetées immédiatement. La seule exception à ce fait est la portée globale, qui ne disparaît pas tant que l'application est en cours d'exécution.

### 3 — Les fermetures couvrent plusieurs portées

#### Lorsque vous définissez une fonction, une fermeture est créée

Contrairement aux portées, les fermetures sont créées lorsque vous _définissez_ une fonction, pas lorsque vous l'exécutez. Les fermetures ne disparaissent pas non plus après avoir exécuté cette fonction.

Vous pouvez accéder aux données dans une fermeture longtemps après qu'une fonction est définie et après qu'elle est exécutée également.

Une fermeture englobe tout ce à quoi la fonction définie peut accéder. Cela signifie la portée de la fonction définie, et toutes les portées imbriquées entre la portée globale et la portée de la fonction définie plus la portée globale elle-même.

```js
var G = 'G';
// Définir une fonction et créer une fermeture
function functionA() {
  var A = 'A'
  
  // Définir une fonction et créer une fermeture
  function functionB() {
    var B = 'B'
    console.log(A, B, G);
  }
  
  functionB();  // affiche A, B, G
  // la fermeture de functionB n'est pas jetée
  A = 42;
  functionB();  // affiche 42, B, G
}
functionA();
```

Lorsque nous définissons `functionB` ici, sa fermeture créée nous permettra d'accéder à la portée de `functionB` plus la portée de `functionA` plus la portée globale.

Chaque fois que nous exécutons `functionB`, nous pouvons accéder aux variables `B`, `A`, et `G` à travers sa fermeture précédemment créée. Cependant, cette fermeture ne nous donne pas une copie de ces variables mais plutôt une référence à elles. Donc si, par exemple, la valeur de la variable `A` est modifiée à un moment donné après la création de la fermeture de `functionB`, lorsque nous exécutons `functionB` après cela, nous verrons la nouvelle valeur, pas l'ancienne. Le deuxième appel à `functionB` affiche `42, B, G` parce que la valeur de la variable `A` a été changée en 42 et la fermeture nous a donné une référence à `A`, pas une copie.

#### Ne confondez pas les fermetures avec les portées

Il est courant de confondre les fermetures avec les portées, alors assurons-nous de ne pas faire cela.

```js
// portée : globale
var a = 1;
void function one() {
  // portée : one
  // fermeture : [one, global]
  var b = 2;
  
  void function two() {
    // portée : two
    // fermeture : [two, one, global]
    var c = 3;
    
    void function three() {
      // portée : three
      // fermeture : [three, two, one, global]
      var d = 4;
      console.log(a + b + c + d); // affiche 10
    }();
  }();  
}();
```

Dans l'exemple simple ci-dessus, nous avons trois fonctions et elles sont toutes définies et immédiatement invoquées, donc elles créent toutes des portées et des fermetures.

La portée de la fonction `one()` est son corps. Sa fermeture nous donne accès à sa portée ainsi qu'à la portée globale.

La portée de la fonction `two()` est son corps. Sa fermeture nous donne accès à sa portée plus la portée de la fonction `one()` plus la portée globale

Et de même, la fermeture de la fonction `three()` nous donne accès à toutes les portées de l'exemple. C'est pourquoi nous avons pu accéder à toutes les variables dans la fonction `three()`.

Mais la relation entre les portées et les fermetures n'est pas toujours simple comme cela. Les choses deviennent différentes lorsque la définition et l'invocation des fonctions se produisent dans des portées différentes. Laissez-moi expliquer cela avec un exemple :

```js
var v = 1;
var f1 = function () {
  console.log(v);
}
var f2 = function() {
  var v = 2;
  f1(); // Cela affichera-t-il 1 ou 2 ?
};
f2();
```

Que pensez-vous que l'exemple ci-dessus affichera ? Le code est simple, `f1()` affiche la valeur de `v`, qui est 1 dans la portée globale, mais nous exécutons `f1()` à l'intérieur de `f2()`, qui a un `v` différent égal à 2. Ensuite, nous exécutons `f2()`.

_Ce code affichera-t-il 1 ou 2 ?_

Si vous êtes tenté de dire 2, vous serez surpris. Ce code affichera en réalité 1. La raison est que les portées et les fermetures sont différentes. La ligne `console.log` utilisera la fermeture de `f1()`, qui est créée lorsque nous définissons `f1()`, ce qui signifie que la fermeture de `f1()` nous donne accès uniquement à la portée de `f1()` plus la portée globale. La portée où nous exécutons `f1()` n'affecte pas cette fermeture. En fait, la fermeture de `f1()` ne nous donnera pas du tout accès à la portée de `f2()`. Si vous supprimez la variable globale `v` et exécutez ce code, vous obtiendrez une erreur de référence :

```js
var f1 = function () {
  console.log(v);
}
var f2 = function() {
  var v = 2;
  f1(); // ReferenceError: v is not defined
};
f2();
```

C'est très important à comprendre et à retenir.

### 4 — Les fermetures ont un accès en lecture et en écriture

Puisque les fermetures nous donnent des références aux variables dans les portées, l'accès qu'elles nous donnent signifie à la fois lecture et écriture, pas seulement lecture.

Jetez un coup d'œil à cet exemple :

```js
function outer() {
  let a = 42;
function inner() {
    a = 43;
  }
inner();
  console.log(a);
}
outer();
```

La fonction `inner()` ici, lorsqu'elle est définie, crée une fermeture qui nous donne accès à la variable `a`. Nous pouvons lire et modifier cette variable, et si nous la modifions, nous modifierons la variable `a` réelle dans la portée de `outer()`.

Ce code affichera _43_ parce que nous avons utilisé la fermeture de la fonction `inner()` pour modifier la variable de la fonction `outer()`.

C'est en fait pourquoi nous pouvons changer les variables globales partout. Toutes les fermetures nous donnent à la fois un accès en lecture et en écriture à toutes les variables globales.

### 5 — Les fermetures peuvent partager des portées

Puisque les fermetures nous donnent accès aux portées imbriquées au moment où nous définissons des fonctions, lorsque nous définissons plusieurs fonctions dans la même portée, cette portée est partagée entre toutes les fermetures créées, et bien sûr, à cause de cela, la portée globale est toujours partagée entre toutes les fermetures.

```js
function parent() {
  let a = 10;
  
  function double() {
    a = a+a;
   console.log(a);
  };
  
  function square() {
    a = a*a;
   console.log(a);
  }
  
  return { double, square }
}
let { double, square } = parent();
double(); // affiche 20
square(); // affiche 400
double(); // affiche 800
```

Dans l'exemple ci-dessus, nous avons une fonction `parent()` avec une variable `a` définie à 10. Nous définissons deux fonctions dans la portée de cette fonction `parent()`, `double()` et `square()`. Les fermetures créées pour `double()` et `square()` partagent toutes deux la portée de la fonction `parent()`. Puisque `double()` et `square()` modifient tous deux la valeur de `a`, lorsque nous exécutons les trois dernières lignes, nous doublons `a` (ce qui fait `a` = 20), puis nous mettons au carré cette valeur doublée (ce qui fait `a` = 400), puis nous doublons cette valeur mise au carré (ce qui fait `a` = 800).

### Un dernier test

Vérifions maintenant votre compréhension des fermetures jusqu'à présent. Avant d'exécuter le code suivant, essayez de deviner ce qu'il affichera :

```js
let a = 1;
const function1 = function() {
  console.log(a);
  a = 2
}
a = 3;
const function2 = function() {
  console.log(a);
}
function1();
function2();
```

J'espère que vous avez compris et j'espère que ces concepts simples vous aideront à vraiment comprendre le rôle significatif que jouent les fermetures de fonction en JavaScript.

Merci d'avoir lu.

Apprendre React ou Node ? Consultez mes livres :

* [Learn React.js by Building Games](http://amzn.to/2peYJZj)
* [Node.js Beyond the Basics](http://amzn.to/2FYfYru)