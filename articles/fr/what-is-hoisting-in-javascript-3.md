---
title: Qu'est-ce que le Hoisting en JavaScript | Hoisting des Fonctions, Variables
  et Classes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-28T14:54:11.000Z'
originalURL: https://freecodecamp.org/news/what-is-hoisting-in-javascript-3
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/27-hoisting.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce que le Hoisting en JavaScript | Hoisting des Fonctions, Variables
  et Classes
seo_desc: 'By Dillion Megida

  Hoisting is a concept or behavior in JavaScript where the declaration of a function,
  variable, or class goes to the top of the scope they were defined in. What does
  this mean?

  Hoisting is a concept you may find in some programming l...'
---

Par Dillion Megida

Le hoisting est un concept ou un comportement en JavaScript où la déclaration d'une fonction, d'une variable ou d'une classe est déplacée en haut de la portée dans laquelle elles ont été définies. Que signifie cela ?

Le hoisting est un concept que vous pouvez trouver dans certains langages de programmation (comme JavaScript) et pas dans d'autres. C'est un comportement spécial de l'interpréteur JavaScript. Nous allons apprendre comment cela fonctionne dans cet article.

Commençons par les fonctions.

J'ai une [version vidéo de ce sujet](https://youtu.be/o8kXXjZdpqg) que vous pouvez consulter.

## Hoisting des Fonctions

Regardez cet exemple de code :

```js
function printHello() {
  console.log("hello")
}

printHello()
// hello
```

Ici, nous déclarons `printHello`, et nous exécutons la fonction juste après la ligne où elle a été déclarée. Pas d'erreurs ; tout fonctionne !

Maintenant, regardez cet exemple :

```js
printHello()
// hello

function printHello() {
  console.log("hello")
}
```

Ici, nous exécutons `printHello` avant la ligne où la fonction a été déclarée. Et tout fonctionne toujours sans erreurs. Que s'est-il passé ici ? **Le hoisting**.

Avant que l'interpréteur n'exécute tout le code, il hoiste (élève, ou soulève) d'abord la fonction déclarée en haut de la portée dans laquelle elle est définie. Dans ce cas, `printHello` est définie dans la portée globale, donc la fonction est hoistée en haut de la portée globale. Grâce au hoisting, la fonction (y compris la logique) devient accessible même avant la ligne où elle a été déclarée dans le code.

Regardons un autre exemple :

```js
printHello()
// hello

printDillion()
// ReferenceError: printDillion is not defined

function printHello() {
  console.log('hello')

  function printDillion() {
    console.log("dillion")
  }
}
```

Comme vous le voyez ici, nous déclarons `printHello`. Dans cette fonction, nous exécutons d'abord `console.log('hello')` puis nous déclarons une autre fonction appelée `printDillion` qui exécute `console.log('dillion')` lorsqu'elle est appelée.

Avant que `printHello` ne soit déclarée dans le code, nous essayons d'y accéder en exécutant `printHello()`. Elle est accessible (puisqu'elle est hoistée en haut de la portée globale), donc nous avons "hello" imprimé sur la console.

Mais ensuite, nous essayons d'accéder à `printDillion`, et nous obtenons une erreur de référence : **printDillion is not defined**. Le hoisting ne se produit-il pas sur `printDillion` ?

`printDillion` est hoistée, mais elle n'est soulevée qu'en haut de la portée dans laquelle elle a été déclarée. Dans ce cas, elle est déclarée dans une portée locale--dans `printHello`. Par conséquent, elle ne serait accessible que dans la fonction. Mettons à jour notre code :

```js
printHello()
// hello

function printHello() {
  printDillion()
  // dillion

  console.log('hello')

  function printDillion() {
    console.log("dillion")
  }
}
```

Maintenant, nous exécutons `printDillion` dans `printHello` avant la ligne où `printDillion` a été réellement déclarée. Puisque la fonction est hoistée en haut de la portée locale, nous sommes en mesure d'y accéder avant la ligne où elle a été réellement déclarée.

Le hoisting rend tout cela possible pour les déclarations de fonctions. Mais il est également important de noter que **le hoisting ne se produit pas sur les expressions de fonctions**. J'ai expliqué la raison de cela ici : [Déclarations de Fonctions vs Expressions de Fonctions](https://www.freecodecamp.org/news/function-declaration-vs-function-expression/)

Maintenant, regardons le hoisting pour les variables.

## Hoisting des Variables

Vous pouvez déclarer des variables en JavaScript avec les variables `var`, `let` et `const`. Et ces déclarations de variables seraient hoistées, mais se comporteraient différemment. Commençons par `var`.

### Hoisting des variables `var`

Regardez cet exemple :

```js
console.log(name)
// undefined

var name = "Dillion"
```

Ici, nous déclarons une variable appelée `name` avec une valeur de chaîne "Dillion". Mais nous essayons d'accéder à la variable avant la ligne où elle a été déclarée. Mais nous n'obtenons aucune erreur. **Le hoisting a eu lieu**. La déclaration `name` est hoistée en haut, donc l'interpréteur "sait" qu'il y a une variable appelée `name`. Si l'interpréteur ne savait pas, vous obtiendriez **name is not defined**. Essayons :

```js
console.log(name)
// ReferenceError: name is not defined

var myName = "Dillion"
```

Nous avons une variable appelée `myName` mais pas `name`. Nous obtenons l'erreur **name is not defined** lorsque nous essayons d'accéder à `name`. L'interpréteur "ne sait pas" à propos de cette variable.

Revenons à notre exemple ci-dessus :

```
console.log(name)
// undefined

var name = "Dillion"
```

Bien que le hoisting ait eu lieu ici, la valeur de `name` est undefined lorsque nous y accédons avant la ligne de déclaration. Avec les variables déclarées `var`, la déclaration de la variable est hoistée mais avec une valeur par défaut de `undefined`. La valeur réelle est initialisée lorsque la ligne de déclaration est exécutée.

En accédant à la variable après cette ligne, nous obtenons la valeur réelle :

```
console.log(name)
// undefined

var name = "Dillion"

console.log(name)
// Dillion
```

Supposons que nous ayons déclaré `name` dans une fonction :

```js
print()

console.log(name)
// ReferenceError: name is not defined

function print() {
  var name = "Dillion"
}
```

Ici, nous obtenons une erreur de référence : **name is not defined**. Rappelez-vous, les variables sont hoistées mais **uniquement en haut de la portée dans laquelle elles ont été déclarées**. Dans ce cas, `name` est déclarée dans `print`, donc elle sera hoistée en haut de cette portée locale. Essayons d'y accéder dans la fonction :

```js
print()

function print() {
  console.log(name)
  // undefined

  var name = "Dillion"
}
```

En essayant d'accéder à `name` dans la fonction, même si c'est au-dessus de la ligne de déclaration, nous n'obtenons pas d'erreur. C'est parce que `name` est hoistée, mais n'oubliez pas, **avec une valeur par défaut de `undefined`**.

### Hoisting des variables `let`

Bien que les variables déclarées avec `let` soient également hoistées, elles ont un comportement différent. Regardons un exemple :

```js
console.log(name)
// ReferenceError: Cannot access 'name' before initialization

let name = "Dillion"
```

Ici, nous obtenons une erreur de référence : **Cannot access 'name' before initialization**. Remarquez-vous que l'erreur ne dit pas **name is not defined** ? C'est parce que l'interpréteur est "au courant" d'une variable `name` parce que la variable est hoistée.

"Cannot access 'name' before initialization" se produit parce que les variables déclarées avec `let` n'ont pas de valeur par défaut lorsqu'elles sont hoistées. Comme nous l'avons vu avec `var`, les variables ont une valeur par défaut de `undefined` jusqu'à ce que la ligne où la déclaration/initialisation est exécutée. Mais avec `let`, les variables ne sont pas initialisées.

Les variables sont hoistées en haut de la portée dans laquelle elles sont déclarées (locale, globale ou bloc), mais ne sont pas accessibles parce qu'elles n'ont pas été initialisées. Ce concept est également appelé [Temporal Dead Zone](https://dillionmegida.com/p/temporal-dead-zone-in-javascript).

Elles ne peuvent être accessibles qu'après que la ligne d'initialisation a été exécutée :

```js
let name = "Dillion"

console.log(name)
// Dillion
```

En accédant à `name` après la ligne où elle a été déclarée et initialisée, nous n'obtenons aucune erreur.

### Hoisting des variables `const`

Tout comme `let`, les variables déclarées avec `const` sont hoistées, mais pas accessibles. Par exemple :

```js
console.log(name)
// ReferenceError: Cannot access 'name' before initialization

const name = "Dillion"
```

Le même concept de **temporal dead zone** s'applique aux variables `const`. Ces variables sont hoistées en haut de la portée dans laquelle elles sont définies (locale, globale ou bloc), mais elles restent inaccessibles jusqu'à ce que les variables soient initialisées avec une valeur.

```js
const name = "Dillion"

console.log(name)
// Dillion
```

En accédant à la variable après qu'elle a été initialisée avec une valeur (comme vous le voyez ci-dessus), tout fonctionne bien.

Passons au hoisting des classes.

## Hoisting des Classes

Les classes en JavaScript sont également hoistées. Regardons un exemple :

```js
const Dog = new Animal("Bingo")
// ReferenceError: Cannot access 'Animal' before initialization

class Animal {
  constructor(name) {
    this.name = name
  }
}
```

Ici, nous déclarons une classe appelée `Animal`. Nous essayons d'accéder à cette classe (instancier un objet `Dog`) avant qu'elle ne soit déclarée. Nous obtenons une erreur de référence : **Cannot access 'Animal' before initialization**. À quelle erreur cela vous fait-il penser ?

Tout comme les variables `let` et `const`, les classes sont hoistées en haut de la portée dans laquelle elles sont définies, mais inaccessibles jusqu'à ce qu'elles soient initialisées. Nous n'obtenons pas "Animal is not defined", ce qui montre que l'interpréteur "sait" qu'il y a une classe `Animal` (grâce au hoisting). Mais nous ne pouvons pas accéder à cette classe jusqu'à ce que la ligne d'initialisation soit exécutée.

Mettons à jour le code :

```js
class Animal {
  constructor(name) {
    this.name = name
  }
}

const Dog = new Animal("Bingo")

console.log(Dog)
// { name: 'Bingo' }
```

Après que `Animal` a été initialisée, elle devient accessible, donc nous pouvons instancier l'objet `Dog` à partir de la classe sans erreurs.

## Conclusion

Dans certains codebases, vous pouvez trouver un code similaire à ceci :

```js
function1()
function2()
function3()

// lignes de code
// lignes de code

function function1() {...}
function function2() {...}
function function3() {...}
```

Les trois fonctions ici sont appelées en haut mais réellement déclarées dans le code en bas. Cela est possible, grâce au hoisting. Les fonctions sont hoistées en haut de la portée globale (qui est où elles ont été définies) avec leur logique, donc elles deviennent accessibles/exécutables même avant la ligne où elles ont été définies.

C'est différent pour les autres. Les variables `var` sont hoistées mais avec une valeur par défaut de `undefined`. Les variables `let` et `const`, et les classes sont hoistées mais inaccessibles car elles n'ont pas d'initialisation par défaut.

Si vous avez aimé cet article, veuillez le partager avec d'autres 🤟🏾