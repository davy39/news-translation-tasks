---
title: Déclaration de fonction vs Expression de fonction
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-26T12:11:48.000Z'
originalURL: https://freecodecamp.org/news/function-declaration-vs-function-expression
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/26-function-declaration-vs-expression.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: JavaScript
  slug: javascript
seo_title: Déclaration de fonction vs Expression de fonction
seo_desc: 'By Dillion Megida

  When creating functions, you can use two approaches: declaration and expression.
  What''s the difference?

  When talking about functions in JavaScript, you would often hear function declarations
  and function expressions. Though these ap...'
---

Par Dillion Megida

Lors de la création de fonctions, vous pouvez utiliser deux approches : **déclaration** et **expression**. Quelle est la différence ?

Lorsque l'on parle de fonctions en JavaScript, on entend souvent parler de déclarations de fonctions et d'expressions de fonctions. Bien que ces approches soient presque similaires, elles présentent des différences notables.

Nous allons examiner les différences dans cet article.

J'ai [une version vidéo de ce sujet](https://www.youtube.com/watch?v=cozcCZjkjto) que vous pouvez également consulter.

## Déclaration de fonction

Pour déclarer une fonction, vous utilisez le mot-clé `function` et spécifiez un nom pour la fonction. Par exemple :

```js
function generateIntro(name) {
  return `Hi, my name is ${name}`
}

const dillion = generateIntro("Dillion")
console.log(dillion)

// Hi, my name is Dillion
```

Ici, nous avons "déclaré" une fonction appelée `generateIntro`. Vous voyez que nous utilisons le mot-clé `function` suivi du nom de la fonction : "generateIntro".

Maintenant, regardons l'expression de fonction.

## Expression de fonction

Ici, vous créez une expression de fonction et l'assignez à une variable qui peut être appelée. Vous pouvez faire cela de deux manières.

### Expressions de fonction avec le mot-clé `function`

Une façon de faire cela est d'utiliser le mot-clé function sans nom, ce qui en fait une fonction anonyme. Voici comment :

```js
const generateIntro = function(name) {
  return `Hi, my name is ${name}`
}

const dillion = generateIntro("Dillion")
console.log(dillion)

// Hi, my name is Dillion
```

Comme vous le voyez ici, nous avons le mot-clé `function` sans nom pour la fonction. Cela en fait une expression, que vous devez assigner à une variable (comme nous l'avons fait pour `generateIntro` ici).

**Note :** vous pouvez utiliser `const`, `let` ou `var` pour déclarer la variable. Vous pouvez en apprendre plus sur les différences entre ces mots-clés [dans cet article](https://www.freecodecamp.org/news/differences-between-var-let-const-javascript/)

Si nous utilisons le mot-clé `function` sans nom, nous créons une expression de fonction, que nous devons assigner à une variable, sinon nous obtenons une erreur. Voici ce que je veux dire :

```js
function(name) {
  return `Hi, my name is ${name}`
}

// SyntaxError: Function statements require a function name
```

Nous obtenons une erreur : **SyntaxError: Function statements require a function name**. Sans l'assigner à une variable, JavaScript suppose qu'il s'agit d'une instruction, et comme le dit l'erreur, vous devez fournir un nom de fonction.

Mais lorsque vous l'assignez à une variable, vous assignez l'expression, et lorsque vous appelez la variable (`variable()`), elle exécutera la logique de l'expression de fonction qui lui est assignée.

### Expressions de fonction fléchées

Vous pouvez également créer des expressions de fonction avec des fonctions fléchées. Les fonctions fléchées, introduites dans ES6, vous permettent d'écrire des fonctions de manière concise. Mais **les fonctions fléchées ne peuvent pas être déclarées ; elles ne peuvent être que des expressions**. Voici un exemple :

```js
const generateIntro = (name) => {
  return `Hi, my name is ${name}`
}

const dillion = generateIntro("Dillion")
console.log(dillion)

// Hi, my name is Dillion
```

La fonction fléchée ici est `(args) => {...}`. Il s'agit d'une expression de fonction que nous avons assignée à `generateIntro`.

Pour le reste de cet article, je me concentrerai sur les expressions de fonction créées avec le mot-clé `function`, mais sachez que cela s'applique également aux fonctions fléchées.

## Déclarations de fonction vs Expressions de fonction

Alors, quelle est la différence entre ces façons de créer des fonctions et pourquoi est-ce important ?

C'est important car ces fonctions ont des comportements différents. Et selon ce que vous voulez réaliser, l'une peut être préférée à l'autre.

### 1. Les fonctions exprimées ne peuvent pas être utilisées avant l'initialisation

Vous pouvez utiliser une fonction déclarée avant la ligne où elle a été initialisée. Voici ce que je veux dire :

```js
const result = sum(20, 50)
console.log(result)

console.log("hello")

function sum(num1, num2) {
  return num1 + num2
}

// 70
// "hello"
```

Comme vous le voyez ici, nous avons utilisé `sum` à la ligne 1, qui est en fait avant la ligne où elle a été déclarée. Ce qui se passe ici est le **hoisting**. `sum` est remontée en haut du code avant que le code entier ne soit exécuté. Cela rend `sum` accessible avant la ligne où elle a été réellement créée dans le code.

En ce qui concerne le hoisting, **toutes les fonctions et variables sont remontées**. Mais les fonctions créées avec des expressions de fonction ne peuvent pas être "utilisées" avant leur initialisation.

Voyons un exemple utilisant une expression de fonction créée avec le mot-clé `function` :

```js
const result = sum(20, 50)
console.log(result)

console.log("hello")

const sum = function(num1, num2) {
  return num1 + num2
}

// ReferenceError: Cannot access 'sum' before initialization
```

Nous obtenons une erreur : **ReferenceError: Cannot access 'sum' before initialization**. Nous obtenons cette erreur car lorsque vous déclarez des variables avec `let` ou `const` (comme nous l'avons fait pour `sum` ici), elles sont remontées, mais sans initialisation par défaut. Vous pouvez en apprendre plus sur ce qui se passe ici dans cet article : [le comportement de hoisting dans let et const](https://www.freecodecamp.org/news/javascript-let-and-const-hoisting/)

Disons que nous créons la variable avec `var` à la place :

```js
const result = sum(20, 50)
console.log(result)

console.log("hello")

var sum = function(num1, num2) {
  return num1 + num2
}

// TypeError: sum is not a function
```

Maintenant, nous obtenons une nouvelle erreur : **TypeError: sum is not a function**. Bien que les variables `var` soient remontées, elles sont remontées avec une initialisation par défaut de `undefined`. Ainsi, tenter de l'appeler comme une fonction, c'est-à-dire `undefined()`, lance l'erreur que "sum is not a function".

La même erreur se produirait si c'était une fonction fléchée.

Par conséquent, **seules les fonctions déclarées peuvent être utilisées avant l'initialisation**.

### 2. Les fonctions exprimées doivent être assignées pour être utilisées plus tard

Avec les fonctions déclarées, vous avez déjà le nom : `function name...`. Vous pouvez donc utiliser la fonction plus tard : `name()`. Mais avec les expressions de fonction, il n'y a pas de nom comme nous l'avons vu. Il serait impossible d'utiliser une telle fonction plus tard, sauf si nous l'assignons à une variable :

```js
const printName = function(firstname, lastname) {
  console.log(`${firstname} ${lastname}`)
}
```

Ici, nous avons assigné l'expression de fonction à `printName`. Maintenant, nous pouvons utiliser cette logique de fonction plus tard en appelant `printName()`.

### 3. Les fonctions anonymes sont utiles pour les opérations anonymes

Il existe des cas où vous n'avez pas besoin d'utiliser une fonction plus tard. Vous pouvez exécuter la fonction instantanément. Dans de tels cas, vous n'avez pas besoin de nom, vous pouvez donc utiliser une expression de fonction au lieu d'une déclaration.

Voyons quelques exemples.

#### Expressions de fonction immédiatement invoquées (IIFE)

Les IIFE sont des fonctions qui sont immédiatement invoquées après leur création. Voici un exemple :

```js
(function() {
  console.log('deeecode')
})()

// deeecode
```

Ou l'équivalent en fonction fléchée :

```js

(() => {
  console.log('deeecode')
})()

// deeecode
```

Il s'agit d'une IIFE où nous créons une fonction qui exécute `console.log('deeecode')`. Immédiatement après avoir créé la fonction, nous l'exécutons comme vous le voyez à la fin (`()`). Ici, nous n'avons pas l'intention d'utiliser la fonction plus tard, donc une expression de fonction fonctionne bien.

L'utilisation d'une déclaration de fonction ici ne lancera pas d'erreur, mais le nom de la fonction sera inaccessible :

```js
(function print(){
  console.log('deeecode')
})()

print()

// deeecode
// ReferenceError: print is not defined
```

En utilisant une déclaration de fonction, l'IIFE est exécutée, mais vous ne pouvez pas accéder au nom de la fonction en dehors des parenthèses.

#### Fonctions de rappel

Lorsque vous utilisez des fonctions de rappel, vous pouvez également passer des fonctions anonymes (expressions de fonction). Par exemple, en utilisant la méthode `forEach` des tableaux qui attend une fonction de rappel, nous pouvons utiliser une fonction anonyme.

La syntaxe de la méthode `forEach` est :

```js
array.forEach(callbackFn)
```

`forEach` parcourt chaque élément d'un tableau et exécute la fonction de rappel sur eux. Voyons comment nous utilisons une expression de fonction pour cela :

```js
const array = [1, 2, 3]

array.forEach(function(value) {
  console.log(value)
})

// 1
// 2
// 3
```

Comme vous le voyez ici, nous avons passé une expression de fonction (fonction anonyme) comme argument à `forEach`.

Vous pouvez passer une déclaration de fonction à la place, et la fonction de rappel fonctionnera. Mais, comme nous l'avons vu précédemment, vous ne pourrez pas accéder à la fonction plus tard :

```js
const array = [1, 2, 3]

array.forEach(function print(value) {
  console.log(value)
})

// 1
// 2
// 3

// ReferenceError: print is not defined
```

Comme vous le voyez ici, `print` est déclarée et utilisée comme fonction de rappel, mais vous ne pouvez pas accéder à `print` par la suite.

## Conclusion

Les déclarations de fonction et les expressions de fonction sont des termes que vous entendrez souvent autour des fonctions en JavaScript. Vous pouvez utiliser des expressions de fonction pour effectuer une logique similaire aux déclarations de fonction, mais il est important de noter les différences.

Dans cet article, nous avons vu comment les expressions de fonction diffèrent des déclarations de fonction.

Si vous avez aimé cet article, n'hésitez pas à le partager :)