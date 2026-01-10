---
title: Le guide définitif de JavaScript pour votre prochain entretien de développeur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-02T21:21:33.000Z'
originalURL: https://freecodecamp.org/news/the-definitive-javascript-handbook-for-a-developer-interview-44ffc6aeb54e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FfREbc94Ge3K3DYG_tEqaQ.jpeg
tags:
- name: careers
  slug: careers
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: Le guide définitif de JavaScript pour votre prochain entretien de développeur
seo_desc: 'By Gustavo Azevedo

  JavaScript is the most popular programming language and has been since 2014, according
  to Stack Overflow Survey. It is no wonder that over 1/3rd of all developer jobs
  require some JavaScript knowledge. So, if you plan to work as a ...'
---

Par Gustavo Azevedo

JavaScript est le langage de programmation le plus populaire et ce depuis 2014, selon le [Stack Overflow Survey](https://insights.stackoverflow.com/survey/2017#most-popular-technologies). Il n'est donc pas surprenant que plus d'un tiers des emplois de développeur nécessitent une certaine connaissance de JavaScript. Ainsi, si vous prévoyez de travailler en tant que développeur dans un avenir proche, vous devriez être familier avec ce langage extrêmement populaire.

Le but de cet article est de rassembler tous les concepts JavaScript qui sont fréquemment abordés lors des entretiens de développeur. Il a été écrit pour que vous puissiez réviser tout ce que vous devez savoir sur JavaScript en un seul endroit.

### **Types et Coercition**

Il existe 7 types intégrés : `null`, `undefined`, `boolean`, `number`, `string`, `object` et `symbol` (ES6).

Tous ces types sont appelés primitifs, à l'exception de `object`.

```js
typeof 0              // number
typeof true           // boolean
typeof 'Hello'        // string
typeof Math           // object
typeof null           // object  !!
typeof Symbol('Hi')   // symbol (Nouveau ES6)
```

* **Null vs. Undefined**

**Undefined** est l'absence de définition. Il est utilisé comme valeur par défaut pour les variables non initialisées, les arguments de fonction qui n'ont pas été fournis et les propriétés manquantes des objets. Les fonctions retournent `undefined` lorsque rien n'a été explicitement retourné.

**Null** est l'absence de valeur. C'est une valeur d'assignation qui peut être assignée à une variable comme représentation de 'pas de valeur'.

* **Coercition implicite**

Regardez l'exemple suivant :

```js
var name = 'Joey';
if (name) {
  console.log(name + " doesn't share food!")  // Joey doesnt share food!
}
```

Dans ce cas, la variable de chaîne `name` est coercée en true et vous avez 'Joey doesnt share food!' imprimé dans notre console. Mais comment savoir ce qui sera coercé en true et ce qui sera coercé en false ?

Les valeurs falsy sont des valeurs qui seront coercées en `false` lorsqu'une coercition booléenne est forcée.

Valeurs falsy : `""`, `0`, `null`, `undefined`, `NaN`, `false`.

Tout ce qui n'est pas explicitement dans la liste des valeurs falsy est truthy — **coercé en true**.

```js
Boolean(null)         // false
Boolean('hello')      // true 
Boolean('0')          // true 
Boolean(' ')          // true 
Boolean([])           // true 
Boolean(function(){}) // true
```

Oui. Vous avez bien lu. Les tableaux vides, les objets et les fonctions sont coercés en true !

* **Coercition de chaîne et de nombre**

La première chose à laquelle vous devez prêter attention est l'opérateur `+`. Cet opérateur est trompeur car il fonctionne à la fois pour l'addition de nombres et la concaténation de chaînes.

Mais les opérateurs `*`, `/` et `-` sont exclusifs aux opérations numériques. Lorsque ces opérateurs sont utilisés avec une chaîne, ils forcent la chaîne à être coercée en nombre.

```js
1 + "2" = "12"
"" + 1 + 0 = "10"
"" - 1 + 0 = -1
"-9\n" + 5 = "-9\n5"
"-9\n" - 5 = -14
"2" * "3" = 6
4 + 5 + "px" = "9px"
"$" + 4 + 5 = "$45"
"4" - 2 = 2
"4px" - 2 = NaN
null + 1 = 1
undefined + 1 = NaN
```

* **== vs. ====**

Il est largement répandu que `==` vérifie l'égalité et `===` vérifie l'égalité et le type. Eh bien, c'est une idée fausse.

En fait, `==` vérifie l'**égalité avec coercition** et `===` vérifie l'égalité sans coercition — **égalité stricte**.

```js
2 == '2'            // True
2 === '2'           // False
undefined == null   // True
undefined === null  // False
```

La coercition peut être trompeuse. Regardez le code suivant :

Que pensez-vous de la comparaison suivante ?  
`console.log(a == b);` `(1)`

Cette comparaison retourne en fait True. Pourquoi ?  
Ce qui se passe réellement sous le capot est que si vous comparez un `boolean` avec autre chose qu'un `boolean`, JavaScript coerce ce `boolean` en un `number` et compare. `(2)`

Cette comparaison est maintenant entre un `number` et une `string`. JavaScript coerce maintenant cette `string` en un `number` et compare les deux nombres. `(3)`

Dans ce cas, la comparaison finale `0 == 0` est True.

```js
'0' == false   (1)
'0' == 0       (2)
 0  == 0       (3)
```

Pour une compréhension complète de la manière dont de telles comparaisons sont effectuées, vous pouvez consulter la documentation ES5 [ici](http://www.ecma-international.org/ecma-262/5.1/#sec-11.9.3).

Pour un aide-mémoire, vous pouvez cliquer [ici](http://dorey.github.io/JavaScript-Equality-Table/).

Quelques comparaisons trompeuses à surveiller :

```js
false == ""  // true
false == []  // true
false == {}  // false
"" == 0      // true
"" == []     // true
"" == {}     // false
0 == []      // true
0 == {}      // false
0 == null    // false
```

### Valeur vs. Référence

Les valeurs simples (également connues sous le nom de primitives) sont toujours assignées par copie de valeur : `null`, `undefined`, `boolean`, `number`, `string` et `symbol` ES6.

Les valeurs composées créent toujours une copie de la référence lors de l'assignation : objets, qui incluent les tableaux, et fonctions.

```js
var a = 2;        // 'a' contient une copie de la valeur 2.
var b = a;        // 'b' est toujours une copie de la valeur dans 'a'
b++;
console.log(a);   // 2
console.log(b);   // 3
var c = [1,2,3];
var d = c;        // 'd' est une référence à la valeur partagée
d.push( 4 );      // Mutates the referenced value (object)
console.log(c);   // [1,2,3,4]
console.log(d);   // [1,2,3,4]
/* Compound values are equal by reference */
var e = [1,2,3,4];
console.log(c === d);  // true
console.log(c === e);  // false
```

Pour copier une valeur composée par valeur, vous devez **créer** une copie de celle-ci. La référence ne pointe pas vers la valeur originale.

### Portée

La portée fait référence au contexte d'exécution. Elle définit l'accessibilité des variables et des fonctions dans le code.

La **portée globale** est la portée la plus externe. Les variables déclarées en dehors d'une fonction sont dans la portée globale et peuvent être accessibles dans n'importe quelle autre portée. Dans un navigateur, l'objet window est la portée globale.

La **portée locale** est une portée imbriquée dans une autre portée de fonction. Les variables déclarées dans une portée locale sont accessibles dans cette portée ainsi que dans toutes les portées internes.

```js
function outer() {
  let a = 1;
  function inner() {
    let b = 2;
    function innermost() {
      let c = 3;
      console.log(a, b, c);   // 1 2 3
    }
    innermost();
    console.log(a, b);        // 1 2 — 'c' is not defined
  }
  inner();
  console.log(a);             // 1 — 'b' and 'c' are not defined
}
outer();
```

Vous pouvez penser aux portées comme à une série de portes de taille décroissante (de la plus grande à la plus petite). Une personne courte qui passe à travers la plus petite porte — **portée la plus interne** — passera également à travers n'importe quelle porte plus grande — **portées externes**.

Une personne grande qui se coince à la troisième porte, par exemple, aura accès à toutes les portes précédentes — **portées externes** — mais pas aux portes suivantes — **portées internes**.

### Hoisting

Le comportement de "déplacement" des déclarations `var` et `function` en haut de leurs portées respectives pendant la phase de compilation est appelé **hoisting**.

Les déclarations de fonction sont complètement hoistées. Cela signifie qu'une fonction déclarée peut être appelée avant d'être définie.

```js
console.log(toSquare(3));  // 9

function toSquare(n){
  return n*n;
}
```

Les variables sont partiellement hoistées. Les déclarations `var` sont hoistées mais pas leurs assignations.

`let` et `const` ne sont pas hoistés.

```js
{  /* Code original */
  console.log(i);  // undefined
  var i = 10
  console.log(i);  // 10
}

{  /* Phase de compilation */
  var i;
  console.log(i);  // undefined
  i = 10
  console.log(i);  // 10
}
// ES6 let & const
{
  console.log(i);  // ReferenceError: i is not defined
  const i = 10
  console.log(i);  // 10
}
{
  console.log(i);  // ReferenceError: i is not defined
  let i = 10
  console.log(i);  // 10
}
```

### Expression de fonction vs. Déclaration de fonction

* **Expression de fonction**  
Une expression de fonction est créée lorsque l'exécution l'atteint et est utilisable à partir de ce moment — elle n'est pas hoistée.

```js
var sum = function(a, b) {
  return a + b;
}
```

* **Déclaration de fonction**  
Une déclaration de fonction peut être appelée avant et après sa définition — elle est hoistée.

```js
function sum(a, b) {
  return a + b;
}
```

### Variables : var, let et const

Avant ES6, il était seulement possible de déclarer une variable en utilisant `var`. Les variables et fonctions déclarées à l'intérieur d'une autre fonction ne peuvent pas être accessibles par l'une des portées englobantes — elles sont fonction-scopées.

Les variables déclarées à l'intérieur d'une portée de bloc, comme les instructions `if` et les boucles `for`, peuvent être accessibles depuis l'extérieur des accolades ouvrantes et fermantes du bloc.

**Note** : Une variable non déclarée — assignation sans `var`, `let` ou `const` — crée une variable `var` dans la portée globale.

```js
function greeting() {
  console.log(s) // undefined
  if(true) {
    var s = 'Hi';
    undeclaredVar = 'I am automatically created in global scope';
  }
  console.log(s) // 'Hi'
}
console.log(s);  // Error — ReferenceError: s is not defined
greeting();
console.log(undeclaredVar) // 'I am automatically created in global scope'
```

ES6 `let` et `const` sont nouveaux. Ils ne sont pas hoistés et sont des alternatives block-scopées pour la déclaration de variables. Cela signifie qu'une paire d'accolades définit une portée dans laquelle les variables déclarées avec soit let soit const sont confinées.

```js
let g1 = 'global 1'
let g2 = 'global 2'
{   /* Creating a new block scope */
  g1 = 'new global 1'
  let g2 = 'local global 2'
  console.log(g1)   // 'new global 1'
  console.log(g2)   // 'local global 2'
  console.log(g3)   // ReferenceError: g3 is not defined
  let g3 = 'I am not hoisted';
}
console.log(g1)    // 'new global 1'
console.log(g2)    // 'global 2'
```

Une idée fausse courante est que `const` est immutable. Il ne peut pas être réassigné, mais ses propriétés peuvent être **modifiées** !

```js
const tryMe = 'initial assignment';
tryMe = 'this has been reassigned';  // TypeError: Assignment to constant variable.
// You cannot reassign but you can change it...
const array = ['Ted', 'is', 'awesome!'];
array[0] = 'Barney';
array[3] = 'Suit up!';
console.log(array);     // ["Barney", "is", "awesome!", "Suit up!"]
const airplane = {};
airplane.wings = 2;
airplane.passengers = 200;
console.log(airplane);   // {passengers: 200, wings: 2}
```

### Closure

Une **closure** est la combinaison d'une fonction et de l'environnement lexical dans lequel elle a été déclarée. La closure permet à une fonction d'accéder à des variables d'une portée englobante — **environnement** — même après avoir quitté la portée dans laquelle elle a été déclarée.

```js
function sayHi(name){
  var message = `Hi ${name}!`;
  function greeting() {
    console.log(message)
  }
  return greeting
}
var sayHiToJon = sayHi('Jon');
console.log(sayHiToJon)     // 2() { console.log(message) }
console.log(sayHiToJon())   // 'Hi Jon!'
```

L'exemple ci-dessus couvre les deux choses que vous devez savoir sur les closures :

1. Fait référence aux variables dans la portée externe.  
La fonction retournée accède à la variable `message` de la portée englobante.
2. Peut faire référence aux variables de la portée externe même après que la fonction externe a retourné.   
`sayHiToJon` est une référence à la fonction `greeting`, créée lorsque `sayHi` a été exécutée. La fonction `greeting` maintient une référence à sa portée externe — **environnement** — dans laquelle `message` existe.

L'un des principaux avantages des closures est qu'elles permettent **l'encapsulation des données**. Cela fait référence à l'idée que certaines données ne devraient pas être directement exposées. L'exemple suivant l'illustre.

Au moment où `elementary` est créé, la fonction externe a déjà retourné. Cela signifie que la variable `staff` n'existe que dans la closure et ne peut pas être accessible autrement.

```js
function SpringfieldSchool() {
  let staff = ['Seymour Skinner', 'Edna Krabappel'];
  return {
    getStaff: function() { console.log(staff) },
    addStaff: function(name) { staff.push(name) }
  }
}

let elementary = SpringfieldSchool()
console.log(elementary)        // { getStaff: 2, addStaff: 2 }
console.log(staff)             // ReferenceError: staff is not defined
/* Closure allows access to the staff variable */
elementary.getStaff()          // ["Seymour Skinner", "Edna Krabappel"]
elementary.addStaff('Otto Mann')
elementary.getStaff()          // ["Seymour Skinner", "Edna Krabappel", "Otto Mann"]
```

Allons plus loin dans les closures en résolvant l'un des problèmes d'entretien les plus courants sur ce sujet :  
Qu'est-ce qui ne va pas avec le code suivant et comment le corrigeriez-vous ?

```js
const arr = [10, 12, 15, 21];
for (var i = 0; i < arr.length; i++) {
  setTimeout(function() {
    console.log(`The value ${arr[i]} is at index: ${i}`);
  }, (i+1) * 1000);
}
```

En considérant le code ci-dessus, la console affichera quatre messages identiques `"The value undefined is at index: 4"`. Cela se produit parce que chaque fonction exécutée dans la boucle sera exécutée après que toute la boucle ait été complétée, en référence à la dernière valeur stockée dans `i`, qui était 4.

Ce problème peut être résolu en utilisant IIFE, qui crée une portée unique pour chaque itération et stocke chaque valeur dans sa portée.

```js
const arr = [10, 12, 15, 21];
for (var i = 0; i < arr.length; i++) {
  (function(j) {
    setTimeout(function() {
      console.log(`The value ${arr[j]} is at index: ${j}`);
    }, j * 1000);
  })(i)
}
```

Une autre solution serait de déclarer la variable `i` avec `let`, ce qui crée le même résultat.

```js
const arr = [10, 12, 15, 21];
for (let i = 0; i < arr.length; i++) {
  setTimeout(function() {
    console.log(`The value ${arr[i]} is at index: ${i}`);
  }, (i) * 1000);
}
```

### Immediate Invoked Function Expression (IIFE)

Une IIFE est une expression de fonction qui est appelée immédiatement après sa définition. Elle est généralement utilisée lorsque vous souhaitez créer une nouvelle portée de variable.

Les **(parenthèses environnantes)** empêchent de la traiter comme une déclaration de fonction.

Les **parenthèses finales()** exécutent l'expression de fonction.

Avec IIFE, vous appelez la fonction exactement au moment où vous la définissez.

```js
var result = [];
for (var i=0; i < 5; i++) {
  result.push( function() { return i } );
}
console.log( result[1]() ); // 5
console.log( result[3]() ); // 5
result = [];
for (var i=0; i < 5; i++) {
  (function () {
    var j = i; // copy current value of i
    result.push( function() { return j } );
  })();
}
console.log( result[1]() ); // 1
console.log( result[3]() ); // 3
```

Utiliser IIFE :

* Permet d'attacher des données privées à une fonction.
* Crée des environnements frais.
* Évite de polluer l'espace de noms global.

### Contexte

Le **contexte** est souvent confondu avec la portée. Pour clarifier les choses, gardons à l'esprit ce qui suit :  
Le **contexte** est le plus souvent déterminé par la manière dont une fonction est invoquée. Il fait toujours référence à la valeur de `this` dans une partie particulière de votre code.  
La **portée** fait référence à la visibilité des variables.

### Appels de fonction : call, apply et bind

Ces trois méthodes sont utilisées pour attacher `this` à une fonction et la différence réside dans l'invocation de la fonction.

`.call()` invoque la fonction immédiatement et nécessite de passer les arguments sous forme de liste (un par un).

`.apply()` invoque la fonction immédiatement et permet de passer les arguments sous forme de tableau.

`.call()` et `.apply()` sont principalement équivalents et sont utilisés pour emprunter une méthode à un objet. Le choix de l'un ou de l'autre dépend de celui qui est le plus facile pour passer les arguments. Il suffit de décider s'il est plus facile de passer un tableau ou une liste séparée par des virgules d'arguments.

**Astuce rapide** : **A**pply pour **A**rray — **C**all pour **C**omma.

```js
const Snow = {surename: 'Snow'}
const char = {
  surename: 'Stark',
  knows: function(arg, name) {
    console.log(`You know ${arg}, ${name} ${this.surename}`);
  }
}
char.knows('something', 'Bran');              // You know something, Bran Stark
char.knows.call(Snow, 'nothing', 'Jon');      // You know nothing, Jon Snow
char.knows.apply(Snow, ['nothing', 'Jon']);   // You know nothing, Jon Snow
```

**Note** : Si vous passez un tableau comme l'un des arguments d'une fonction call, il traitera ce tableau entier comme un seul élément.   
ES6 permet de disperser un tableau comme arguments avec la fonction call.

```
char.knows.call(Snow, ...["nothing", "Jon"]);  // You know nothing, Jon Snow
```

`.bind()` retourne une nouvelle fonction, avec un certain contexte et des paramètres. Elle est généralement utilisée lorsque vous souhaitez qu'une fonction soit appelée plus tard avec un certain contexte.

Cela est possible grâce à sa capacité à maintenir un contexte donné pour appeler la fonction originale. Cela est utile pour les rappels asynchrones et les événements.

`.bind()` fonctionne comme la fonction call. Elle nécessite de passer les arguments un par un séparés par une virgule.

```js
const Snow = {surename: 'Snow'}
const char = {
  surename: 'Stark',
  knows: function(arg, name) {
    console.log(`You know ${arg}, ${name} ${this.surename}`);}
  }
const whoKnowsNothing = char.knows.bind(Snow, 'nothing');
whoKnowsNothing('Jon');  // You know nothing, Jon Snow
```

### Mot-clé 'this'

Comprendre le mot-clé `this` en JavaScript, et à quoi il fait référence, peut être assez compliqué à certains moments.

La valeur de `this` est généralement déterminée par le contexte d'exécution d'une fonction. Le contexte d'exécution signifie simplement comment une fonction est appelée.

Le mot-clé `this` agit comme un espace réservé, et fera référence à l'objet qui a appelé cette méthode lorsque la méthode est réellement utilisée.

La liste suivante est l'ordre des règles pour déterminer this. Arrêtez-vous à la première qui s'applique :

* **Liaison `new`** — Lorsque le mot-clé `new` est utilisé pour appeler une fonction, `this` est le nouvel objet construit.

```js
function Person(name, age) {
  this.name = name;
  this.age =age;
  console.log(this);
}
const Rachel = new Person('Rachel', 30);   // { age: 30, name: 'Rachel' }
```

* **Liaison explicite** — Lorsque call ou apply sont utilisés pour appeler une fonction, `this` est l'objet qui est passé en argument.  
**Note** : `.bind()` fonctionne un peu différemment. Il crée une nouvelle fonction qui appellera l'originale avec l'objet qui lui a été lié.

```js
function fn() {
  console.log(this);
}
var agent = {id: '007'};
fn.call(agent);    // { id: '007' }
fn.apply(agent);   // { id: '007' }
var boundFn = fn.bind(agent);
boundFn();         // { id: '007' }
```

* **Liaison implicite** — Lorsqu'une fonction est appelée avec un contexte (l'objet contenant), `this` est l'objet dont la fonction est une propriété.  
Cela signifie qu'une fonction est appelée comme une méthode.

```js
var building = {
  floors: 5,
  printThis: function() {
    console.log(this);
  }
}
building.printThis();  // { floors: 5, printThis: function() {...} }
```

* **Liaison par défaut** — Si aucune des règles ci-dessus ne s'applique, `this` est l'objet global (dans un navigateur, c'est l'objet window).  
Cela se produit lorsqu'une fonction est appelée comme une fonction autonome.  
Une fonction qui n'est pas déclarée comme une méthode devient automatiquement une propriété de l'objet global.

```js
function printWindow() {
  console.log(this)
}
printWindow();  // window object
```

**Note** : Cela se produit également lorsqu'une fonction autonome est appelée depuis une portée de fonction externe.

```js
function Dinosaur(name) {
  this.name = name;
  var self = this;
  inner();
  function inner() {
    alert(this);        // window object — la fonction a écrasé le contexte 'this'
    console.log(self);  // {name: 'Dino'} — référence à la valeur stockée du contexte externe
  }
}
var myDinosaur = new Dinosaur('Dino');
```

* **This lexical** — Lorsqu'une fonction est appelée avec une fonction fléchée `=>`, `this` reçoit la valeur `this` de sa portée environnante au moment de sa création. `this` conserve la valeur de son contexte d'origine.

```js
function Cat(name) {
  this.name = name;
  console.log(this);   // { name: 'Garfield' }
  ( () => console.log(this) )();   // { name: 'Garfield' }
}
var myCat = new Cat('Garfield');
```

### Mode strict

JavaScript est exécuté en mode strict en utilisant la directive "use strict". Le mode strict resserre les règles de parsing et de gestion des erreurs de votre code.

Certains de ses avantages sont :

* **Facilite le débogage** — Les erreurs de code qui auraient autrement été ignorées généreront maintenant des erreurs, comme l'assignation à une propriété globale ou non inscriptible.
* **Empêche les variables globales accidentelles** — L'assignation d'une valeur à une variable non déclarée lancera maintenant une erreur.
* **Empêche l'utilisation invalide de delete** — Les tentatives de suppression de variables, de fonctions et de propriétés non supprimables lanceront maintenant une erreur.
* **Empêche les noms de propriété ou les valeurs de paramètre en double** — Les propriétés nommées en double dans un objet ou les arguments dans une fonction lanceront maintenant une erreur. (Ce n'est plus le cas dans ES6)
* **Rend eval() plus sûr** — Les variables et fonctions déclarées à l'intérieur d'une instruction `eval()` ne sont pas créées dans la portée environnante.
* **"Sécurise" JavaScript en éliminant cette coercition** — La référence à une valeur `this` de null ou undefined n'est pas coercée en objet global. Cela signifie que dans les navigateurs, il n'est plus possible de référencer l'objet window en utilisant `this` à l'intérieur d'une fonction.

### **Mot-clé `new`**

Le mot-clé `new` invoque une fonction de manière spéciale. Les fonctions invoquées en utilisant le mot-clé `new` sont appelées **fonctions constructrices**.

Alors, que fait réellement le mot-clé `new` ?

1. Crée un nouvel objet.
2. Définit le **prototype** de l'objet pour qu'il soit le prototype de la **fonction constructrice**.
3. Exécute la fonction constructrice avec `this` comme nouvel objet créé.
4. Retourne l'objet créé. Si le constructeur retourne un objet, cet objet est retourné.

```js
// Afin de mieux comprendre ce qui se passe sous le capot, construisons le mot-clé new 
function myNew(constructor, ...arguments) {
  var obj = {}
  Object.setPrototypeOf(obj, constructor.prototype);
  return constructor.apply(obj, arguments) || obj
}
```

Quelle est la différence entre invoquer une fonction avec le mot-clé `new` et sans lui ?

```js
function Bird() {
  this.wings = 2;
}
/* invoquer comme une fonction normale */
let fakeBird = Bird();
console.log(fakeBird);    // undefined
/* invoquer comme une fonction constructrice */
let realBird= new Bird();
console.log(realBird)     // { wings: 2 }
```

### Prototype et Héritage

Le prototype est l'un des concepts les plus confus en JavaScript et l'une des raisons à cela est qu'il existe deux contextes différents dans lesquels le mot **prototype** est utilisé.

* **Relation de prototype**  
Chaque objet a un objet **prototype**, dont il hérite toutes les propriétés du prototype.  
`.__proto__` est un mécanisme non standard (disponible en ES6) pour récupérer le prototype d'un objet _(*)_. Il pointe vers le "parent" de l'objet — le **prototype de l'objet**.   
Tous les objets normaux héritent également d'une propriété `.constructor` qui pointe vers le constructeur de l'objet. Chaque fois qu'un objet est créé à partir d'une fonction constructrice, la propriété `.__proto__` lie cet objet à la propriété `.prototype` de la fonction constructrice utilisée pour le créer.  
_(*) `Object.getPrototypeOf()`_ est la fonction standard ES5 pour récupérer le prototype d'un objet.
* **Propriété de prototype**   
Chaque fonction a une propriété `.prototype`.   
Elle fait référence à un objet utilisé pour attacher des propriétés qui seront héritées par les objets plus bas dans la chaîne de prototypes. Cet objet contient, par défaut, une propriété `.constructor` qui pointe vers la fonction constructrice originale.   
Chaque objet créé avec une fonction constructrice hérite d'une propriété constructeur qui pointe vers cette fonction.

```js
function Dog(breed, name){
  this.breed = breed,
  this.name = name
}
Dog.prototype.describe = function() {
  console.log(`${this.name} is a ${this.breed}`)
}
const rusty = new Dog('Beagle', 'Rusty');

/* .prototype property points to an object which has constructor and attached 
properties to be inherited by objects created by this constructor. */
console.log(Dog.prototype)  // { describe: 2 , constructor: 2 }

/* Object created from Dog constructor function */
console.log(rusty)   //  { breed: "Beagle", name: "Rusty" }
/* Object inherited properties from constructor function's prototype */
console.log(rusty.describe())   // "Rusty is a Beagle"
/* .__proto__ property points to the .prototype property of the constructor function */ 
console.log(rusty.__proto__)    // { describe: 2 , constructor: 2 }
/* .constructor property points to the constructor of the object */
console.log(rusty.constructor)  // 2 Dog(breed, name) { ... }
```

#### **Chaîne de prototypes**

La chaîne de prototypes est une série de liens entre des objets qui se référencent les uns les autres.

Lors de la recherche d'une propriété dans un objet, le moteur JavaScript essaiera d'abord d'accéder à cette propriété sur l'objet lui-même.

Si elle n'est pas trouvée, le moteur JavaScript recherchera cette propriété sur l'objet dont il a hérité ses propriétés — le **prototype de l'objet**.

Le moteur parcourra la chaîne à la recherche de cette propriété et retournera la première qu'il trouve.

Le dernier objet de la chaîne est le `Object.prototype` intégré, qui a `null` comme **prototype**. Une fois que le moteur atteint cet objet, il retourne `undefined`.

#### Propriétés propres vs héritées

Les objets ont des propriétés propres et des propriétés héritées.

Les propriétés propres sont des propriétés qui ont été définies sur l'objet.

Les propriétés héritées ont été héritées via la chaîne de prototypes.

```js
function Car() { }
Car.prototype.wheels = 4;
Car.prototype.airbags = 1;

var myCar = new Car();
myCar.color = 'black';

/*  Vérifier la propriété incluant la chaîne de prototypes :  */
console.log('airbags' in myCar)  // true
console.log(myCar.wheels)        // 4
console.log(myCar.year)          // undefined

/*  Vérifier la propriété propre :  */
console.log(myCar.hasOwnProperty('airbags'))  // false — Héritée
console.log(myCar.hasOwnProperty('color'))    // true
```

**Object.create(**_obj_**)** — Crée un nouvel objet avec l'objet **prototype** spécifié et les propriétés.

```js
var dog = { legs: 4 };
var myDog = Object.create(dog);

console.log(myDog.hasOwnProperty('legs'))  // false
console.log(myDog.legs)                    // 4
console.log(myDog.__proto__ === dog)       // true
```

#### **Héritage par référence**

Une propriété héritée est une copie par référence de la propriété de l'**objet prototype** dont elle a hérité cette propriété.

Si une propriété d'un objet est mutée sur le prototype, les objets qui ont hérité de cette propriété partageront la même mutation. Mais si la propriété est remplacée, le changement ne sera pas partagé.

```js
var objProt = { text: 'original' };
var objAttachedToProt = Object.create(objProt);
console.log(objAttachedToProt.text)   // original

objProt.text = 'prototype property changed';
console.log(objAttachedToProt.text)   // prototype property changed

objProt = { text: 'replacing property' };
console.log(objAttachedToProt.text)   // prototype property changed
```

#### **Héritage classique vs. Héritage prototypal**

Dans l'héritage classique, les objets héritent de classes — comme un plan ou une description de l'objet à créer — et créent des relations de sous-classe. Ces objets sont créés via des fonctions constructrices en utilisant le mot-clé new.

L'inconvénient de l'héritage classique est qu'il provoque :

* une hiérarchie inflexible
* des problèmes de couplage serré
* des problèmes de classe de base fragile
* des problèmes de duplication
* Et le célèbre problème gorille/banane — "Ce que vous vouliez, c'était une banane, ce que vous avez obtenu, c'était un gorille tenant la banane, et toute la jungle."

Dans l'héritage prototypal, les objets héritent directement d'autres objets. Les objets sont généralement créés via `Object.create()`, des littéraux d'objet ou des fonctions de fabrication.

Il existe trois types différents d'héritage prototypal :

* **Délégation de prototype** — Un prototype délégué est un objet qui est utilisé comme modèle pour un autre objet. Lorsque vous héritez d'un prototype délégué, le nouvel objet obtient une référence au prototype et à ses propriétés.   
Ce processus est généralement accompli en utilisant `Object.create()`.
* **Héritage concaténatif** — Le processus d'héritage des propriétés d'un objet à un autre en copiant les propriétés du prototype de l'objet, sans conserver de référence entre eux.   
Ce processus est généralement accompli en utilisant `Object.assign()`.
* **Héritage fonctionnel** — Ce processus utilise une _fonction de fabrication(*)_ pour créer un objet, puis ajoute de nouvelles propriétés directement à l'objet créé.   
Ce processus a l'avantage de permettre l'encapsulation des données via la fermeture.  
**_(*)Fonction de fabrication_** est une fonction qui n'est pas une classe ou un constructeur qui retourne un objet sans utiliser le mot-clé `new`.

```js
const person = function(name) {
  const message = `Hello! My name is ${name}`;
  return { greeting: () => console.log(message) }
}
const will = person("Will");
will.greeting();     // Hello! My name is Will
```

Vous pouvez trouver un article complet sur ce sujet par [Eric Elliott](https://www.freecodecamp.org/news/the-definitive-javascript-handbook-for-a-developer-interview-44ffc6aeb54e/undefined) [ici](https://medium.com/javascript-scene/master-the-javascript-interview-what-s-the-difference-between-class-prototypal-inheritance-e4cd0a7562e9).

#### Privilégier la composition à l'héritage de classe

De nombreux développeurs s'accordent à dire que l'héritage de classe devrait être évité dans la plupart des cas. Dans ce modèle, vous concevez vos types en fonction de ce qu'ils **sont**, ce qui en fait un modèle très strict.

La composition, en revanche, vous concevez vos types en fonction de ce qu'ils **font**, ce qui le rend plus flexible et réutilisable.

Voici une belle vidéo sur ce sujet par [Mattias Petter Johansson](https://www.freecodecamp.org/news/the-definitive-javascript-handbook-for-a-developer-interview-44ffc6aeb54e/undefined)

%[https://youtu.be/wfMtDGfHWpA]

### JavaScript asynchrone

JavaScript est un langage de programmation mono-thread. Cela signifie que le moteur JavaScript ne peut traiter qu'un morceau de code à la fois. L'une de ses principales conséquences est que lorsque JavaScript rencontre un morceau de code qui prend beaucoup de temps à traiter, il bloquera tout le code qui suit.

JavaScript utilise une structure de données qui stocke des informations sur les fonctions actives nommée **Call Stack**. Une Call Stack est comme une pile de livres. Chaque livre qui entre dans cette pile se place sur le livre précédent. Le dernier livre à entrer dans la pile sera le premier à en être retiré, et le premier livre ajouté à la pile sera le dernier à en être retiré.

La solution pour exécuter des morceaux de code lourds sans bloquer quoi que ce soit est les **fonctions de rappel asynchrones**. Ces fonctions sont exécutées plus tard — **de manière asynchrone**.

Le processus asynchrone commence avec des fonctions de rappel asynchrones placées dans une **Heap ou** région de mémoire. Vous pouvez penser à la Heap comme un **Event Manager**. La Call Stack demande à l'Event Manager d'exécuter une fonction spécifique uniquement lorsqu'un certain événement se produit. Une fois que cet événement se produit, l'Event Manager déplace la fonction vers la Callback Queue. **Note** : Lorsque l'Event Manager gère une fonction, le code qui suit n'est pas bloqué et JavaScript continue son exécution.

L'Event Loop gère l'exécution de plusieurs morceaux de votre code au fil du temps. L'Event Loop surveille la Call Stack et la Callback Queue.

La Call Stack est constamment vérifiée pour savoir si elle est vide ou non. Lorsqu'elle est vide, la Callback Queue est vérifiée pour voir s'il y a une fonction en attente d'être invoquée. Lorsqu'il y a une fonction en attente, la première fonction de la file est poussée dans la Call Stack, qui l'exécutera. Ce processus de vérification est appelé un 'tick' dans l'Event Loop.

Décomposons l'exécution du code suivant pour comprendre comment ce processus fonctionne :

```js
const first = function () {
  console.log('First message')
}
const second = function () {
  console.log('Second message')
}
const third = function() {
  console.log('Third message')
}

first();
setTimeout(second, 0);
third();

// Output:
  // First message
  // Third message
  // Second message
```

1. Initialement, la console du navigateur est vide et la Call Stack et l'Event Manager sont vides.
2. `first()` est ajouté à la Call Stack.
3. `console.log("First message")` est ajouté à la Call Stack.
4. `console.log("First message")` est exécuté et la console du navigateur affiche **"First message"**_._
5. `console.log("First message")` est retiré de la Call Stack.
6. `first()` est retiré de la Call Stack.
7. `setTimeout(second, 0)` est ajouté à la Call Stack.
8. `setTimeout(second, 0)` est exécuté et géré par l'Event Manager. Et après 0ms, l'Event Manager déplace `second()` vers la Callback Queue.
9. `setTimeout(second, 0)` est maintenant terminé et retiré de la Call Stack.
10. `third()` est ajouté à la Call Stack.
11. `console.log("Third message")` est ajouté à la Call Stack.
12. `console.log("Third message")` est exécuté et la console du navigateur affiche **"Third message"**_._
13. `console.log("Third message")` est retiré de la Call Stack.
14. `third()` est retiré de la Call Stack.
15. La Call Stack est maintenant vide et la fonction `second()` est en attente d'être invoquée dans la Callback Queue.
16. L'Event Loop déplace `second()` de la Callback Queue vers la Call Stack.
17. `console.log("Second message")` est ajouté à la Call Stack.
18. `console.log("Second message")` est exécuté et la console du navigateur affiche **"Second message"**.
19. `console.log("Second message")` est retiré de la Call Stack.
20. `second()` est retiré de la Call Stack.

**Note** : La fonction `second()` n'est pas exécutée après 0ms. Le **temps** que vous passez dans la fonction `setTimeout` ne concerne pas le délai de son exécution. L'Event Manager attendra le temps donné avant de déplacer cette fonction dans la Callback Queue. Son exécution n'aura lieu que lors d'un futur 'tick' dans l'Event Loop.

Merci et félicitations pour avoir lu jusqu'à ce point ! Si vous avez des pensées à ce sujet, n'hésitez pas à laisser un commentaire.

Vous pouvez me trouver sur [GitHub](https://github.com/gustavoaz7) ou [Twitter](https://twitter.com/intent/follow?screen_name=gustavoaz7_).