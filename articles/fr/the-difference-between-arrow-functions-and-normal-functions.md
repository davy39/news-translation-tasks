---
title: Fonctions fléchées vs Fonctions régulières en JavaScript – Quelles sont les
  différences ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-13T21:04:00.000Z'
originalURL: https://freecodecamp.org/news/the-difference-between-arrow-functions-and-normal-functions
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/25-arrow-normal-functions.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: JavaScript
  slug: javascript
seo_title: Fonctions fléchées vs Fonctions régulières en JavaScript – Quelles sont
  les différences ?
seo_desc: 'By Dillion Megida

  In JavaScript, there are two types of functions. You have normal functions and arrow
  functions. Let''s explore the difference between them in this article.

  Arrow functions was introduced in ES6. And it introduced a simple and shorter...'
---

Par Dillion Megida

En JavaScript, il existe deux types de fonctions. Vous avez les fonctions normales et les fonctions fléchées. Explorons la différence entre elles dans cet article.

Les fonctions fléchées ont été introduites dans ES6. Et elles ont introduit une manière simple et plus courte de créer des fonctions.

Voici comment créer une fonction normale, avec des arguments, qui retourne quelque chose :

```js
function multiply(num1, num2) {
  const result = num1 * num2
  return result
}
```

Si vous souhaitez transformer cela en une fonction fléchée, voici ce que vous aurez :

```js
const multiply = (num1, num2) => {
  const result = num1 * num2
  return result
}
```

Si l'instruction `return` est la seule instruction dans la fonction, vous pouvez même avoir une expression de fonction plus courte. Par exemple :

```js
const multiply = (num1, num2) => {
  return num1 * num2
}
```

Cette fonction ne contient que l'instruction `return`. Avec les fonctions fléchées, nous pouvons avoir quelque chose de plus court comme ceci :

```js
const multiply = (num1, num2) => num1 * num2
```

Nous omettons les accolades et le mot-clé `return`. Plus court ; une seule ligne.

Mais la syntaxe d'écriture des deux types de fonctions n'est pas la seule différence. Il y a plus, alors examinons-les.

J'ai une [version vidéo de ce sujet](https://youtu.be/M10gzHpIUDw) que vous pouvez également consulter :)

## 1. Pas d'objet `arguments` dans les fonctions fléchées

Une fonction normale a un objet `arguments` auquel vous pouvez accéder dans la fonction :

```js
function print() {
  console.log(arguments)
}
```

L'objet `arguments` est une variable locale qui contient les arguments passés à la fonction lors de l'appel. Essayons-le :

```js
print("hello", 400, false)

// {
//   '0': 'hello',
//   '1': 400,
//   '2': false
// }
```

Comme vous pouvez le voir ici, les trois arguments passés lors de l'appel de `print()` sont contenus dans l'objet `arguments` que nous enregistrons dans la console. Nous pouvons accéder au premier argument avec `arguments[0]`, au deuxième avec `arguments[1]` et au troisième avec `arguments[2]`.

Mais cet objet n'existe pas dans les fonctions fléchées. Essayons-le. Supposons que nous avons `print` utilisant une fonction fléchée :

```js
const print = () => {
  console.log(arguments)
}

print("hello", 400, false)
// Uncaught ReferenceError: arguments is not defined
```

Maintenant, nous avons une erreur de référence : **arguments is not defined**. C'est parce que la variable `arguments` n'existe pas dans les fonctions fléchées.

## 2. Les fonctions fléchées ne créent pas leur propre liaison `this`

Dans les fonctions normales, une variable `this` est créée qui référence les objets qui les appellent. Par exemple :

```js
const obj = {
  name: 'deeecode',
  age: 200,
  print: function() {
    console.log(this)
  }
}

obj.print()
// {
//   name: 'deeecode',
//   age: 200,
//   print: [Function: print]
// }
```

Comme vous pouvez le voir ici, le `this` dans la méthode `print` pointe vers `obj`, qui est l'objet qui appelle la méthode.

Voici un autre exemple :

```js
const obj = {
  name: 'deeecode',
  age: 200,
  print: function() {
    function print2() {
      console.log(this)
    }
    
    print2()
  }
}

obj.print()
// Window
```

Ici, nous avons deux fonctions. La première est `print` qui est une méthode de l'objet `obj`. La seconde est `print2` qui est une fonction déclarée à l'intérieur de `print`. `print2()` est également appelée directement.

Dans ce cas, `print` est appelée par `obj` (`obj.print()`) mais aucun objet n'appelle `print2` (`print2()`). Donc le `this` dans `print2` référencerait l'objet window par défaut.

Voyons maintenant ce qui se passe avec une fonction fléchée.

```js
const obj = {
  name: 'deeecode',
  age: 200,
  print: () => {
    console.log(this)
  }
}

obj.print()
// Window
```

En utilisant une fonction fléchée pour `print`, cette fonction ne crée pas automatiquement une variable `this`. Par conséquent, toute référence à `this` pointerait vers ce que `this` était avant que la fonction ne soit créée.

Comme vous pouvez le voir dans le résultat, `this` pointait vers l'objet `Window` avant que `print` ne soit créée.

Voyons un autre exemple :

```js
const obj = {
  name: 'deeecode',
  age: 200,
  print: function() {
    const print2 = () => {
      console.log(this)
    }
    
    print2()
  }
}

obj.print()
// {
//   name: 'deeecode',
//   age: 200,
//   print: [Function: print]
// }
```

Ici, nous avons `print` comme une fonction normale, ce qui signifie qu'une variable `this` est automatiquement créée. Ensuite, nous avons `print2` qui est une fonction fléchée.

Parce que `obj` appelle `print` (comme dans `obj.print()`), le `this` dans `print` pointerait vers `obj`.

Puisque `print2` est une fonction fléchée, elle ne crée pas sa propre variable `this`. Par conséquent, toute référence à `this` pointerait vers la valeur qu'elle avait avant que la fonction ne soit créée. Dans ce cas où `obj` appelle `print`, `this` pointait vers `obj` avant que `print2` ne soit créée. Comme vous pouvez le voir dans les résultats, en enregistrant `this` depuis `print2`, `obj` est le résultat.

Vous pouvez en apprendre plus sur [`this` dans mon article ici](https://dillionmegida.com/p/this-demystified/)

## 3. Les fonctions fléchées ne peuvent pas être utilisées comme constructeurs

Avec les fonctions normales, vous pouvez créer des constructeurs qui servent de fonction spéciale pour instancier un objet à partir d'une classe.

Voici un exemple d'une classe `Animal` dont nous instancions deux objets :

```js
class Animal {
  constructor(name, numOfLegs) {
    this.name = name
    this.numOfLegs = numOfLegs
  }
  
  sayName() {
    console.log(`My name is ${this.name}`)
  }
}

const Dog = new Animal("Bingo", 4)
const Bird = new Animal("Steer", 2)

Dog.sayName()
// My name is Bingo

Bird.sayName()
// My name is Steer
```

Ici, nous avons le constructeur `Animal` qui peut être instancié avec différents paramètres. Dans le constructeur, deux arguments sont requis : `name` et `noOfLegs`.

Dans le cas de `Dog`, nous créons une nouvelle instance de `Animal` en utilisant "Bingo" comme `name` et **4** comme `noOfLegs`.

Dans le cas de `Bird`, nous créons une nouvelle instance de `Animal` en utilisant "Steer" comme `name` et **2** comme `noOfLegs`.

En appelant `sayName` sur `Dog` et `Bird`, vous pouvez voir comment la méthode fonctionne actuellement avec chaque objet. La variable `this` pointe vers les objets et le champ `name` est obtenu à partir de chacun d'eux.

La variable `this` est très importante pour les classes et les constructeurs. Dans le point 2, nous avons vu que les fonctions fléchées ne peuvent pas créer leur propre `this`. Pour cette raison, les fonctions fléchées ne peuvent pas non plus être utilisées comme constructeurs.

Essayons et voyons ce qui se passe :

```js
class Animal {
  constructor = (name, numOfLegs) => {
    this.name = name
    this.numOfLegs = numOfLegs
  }
  
  sayName() {
    console.log(`My name is ${this.name}`)
  }
}

// Uncaught SyntaxError: Classes may not have a field named 'constructor'
```

Ici, nous avons une fonction fléchée utilisée pour le `constructor`. Mais, nous obtenons une SyntaxError : **Classes may not have a field named 'constructor'**.

Parce que les fonctions fléchées impliquent des expressions qui sont assignées à des variables, JavaScript voit maintenant `constructor` comme un champ. Et dans les classes, vous ne pouvez pas avoir un champ nommé `constructor` car c'est un nom réservé.

Cependant, nous pouvons utiliser des fonctions fléchées pour les méthodes dans la classe sans obtenir d'erreurs. Par exemple :

```js
class Animal {
  constructor (name, numOfLegs){
    this.name = name
    this.numOfLegs = numOfLegs
  }
    
  sayName = () => {
    console.log(`My name is ${this.name}`)
  }
}
  
const Dog = new Animal("Bingo", 4)

Dog.sayName()
// My name is Bingo
```

Ici, nous avons une fonction normale pour le `constructor`, et une fonction fléchée pour la méthode `sayName`. `sayName` est un champ. Et nous n'obtenons pas d'erreurs.

En appelant `sayName()` sur `Dog`, nous obtenons toujours "My name is Bingo". Bien que `sayName` en tant que fonction fléchée ne crée pas son propre `this`, rappelez-vous que toute référence à `this` pointerait vers la valeur qu'elle avait avant que la fonction fléchée ne soit créée. Dans ce cas, la valeur de `this` pointait vers `Dog` avant que `sayName` ne soit créée.

## 4. Les fonctions fléchées ne peuvent pas être déclarées

En ce qui concerne les fonctions, vous devez comprendre **la déclaration de fonction** et **l'expression de fonction**.

Les déclarations de fonction impliquent le mot-clé `function` et un nom pour la fonction. Par exemple :

```js
function printHello() {
  console.log("hello")
}
```

`printHello` est une **fonction déclarée**. Mais, regardez cet exemple :

```js
const printHello = function() {
  console.log("hello")
}
```

Dans ce cas, `printHello` n'est pas une fonction déclarée. Nous avons une fonction anonyme (sans nom) du côté droit de l'opérateur d'assignation. Cette fonction est une **expression de fonction**, qui est assignée à la variable `printHello`.

Bien que le mot-clé `function` soit utilisé, aucun nom n'est assigné, ce qui en fait une expression et non une déclaration. Pour prouver que ce n'est pas une déclaration, essayez ce qui suit :

```js
function() {
 console.log("hello")
}
```

Parce que cette expression n'est pas assignée à une variable, vous obtenez une erreur : **SyntaxError: Function statements require a function name**

Revenons aux fonctions fléchées. Les fonctions normales peuvent être déclarées lorsque vous utilisez le mot-clé function et un nom, mais les fonctions fléchées ne peuvent pas être déclarées. Elles ne peuvent être que des expressions car elles sont anonymes :

```js
const printHello = () => {
  console.log("hello")
}
```

Comme vous pouvez le voir ici, nous avons une fonction anonyme (commencant par `() => ...`) qui est assignée à la variable `printHello`. `printHello` n'est pas une fonction déclarée ici. C'est une variable qui contient la valeur évaluée de l'expression de fonction.

## 5. Les fonctions fléchées ne peuvent pas être accessibles avant l'initialisation

Le hoisting est un concept où une variable ou une fonction est élevée au sommet de sa portée globale ou locale avant que tout le code ne soit exécuté. Cela rend possible l'accès à une telle variable/fonction avant l'initialisation. Voici un exemple de fonction :

```js
printName()

console.log("hello")

function printName() {
  console.log("i am dillion")
}

// i am dillion
// hello
```

Comme vous pouvez le voir ici, nous avons appelé `printName` avant qu'elle ne soit réellement déclarée dans le code. Mais nous n'obtenons aucune erreur. `printName()` est exécutée (enregistrant "i am dillion" dans la console) avant `console.log("hello")`.

Ce qui se passe ici est le hoisting.

La fonction `printName` est élevée au sommet de la portée globale (la portée dans laquelle elle est déclarée) avant que tout le code ne soit exécuté, ce qui permet d'exécuter la fonction plus tôt.

Mais tous les types de fonctions ne peuvent pas être accessibles avant l'initialisation. Toutes les fonctions et variables en JavaScript sont élevées, mais **seules les fonctions déclarées peuvent être accessibles avant l'initialisation**.

Voici un exemple avec une fonction fléchée :

```js
printName()

console.log("hello")

const printName = () => {
  console.log("i am dillion")
}

// ReferenceError: Cannot access 'printName' before initialization
```

En exécutant ce code, vous obtenez une erreur : **ReferenceError: Cannot access 'printName' before initialization**. 

Comme nous l'avons vu dans le point 4, `printName` n'est pas une fonction déclarée. C'est une variable, déclarée avec `const` à laquelle est assignée une expression de fonction. Les variables déclarées avec `let` et `const` sont élevées, mais elles ne peuvent pas être accessibles avant la ligne où elles sont initialisées.

Supposons que nous utilisions `var` pour notre fonction fléchée :

```js
printName()

console.log("hello")

var printName = () => {
  console.log("i am dillion")
}

// TypeError: printName is not a function
```

Ici, nous avons déclaré la variable `printName` avec `var`. L'erreur que nous obtenons maintenant est **TypeError: printName is not a function**. La raison en est que les variables déclarées avec `var` sont élevées et accessibles, mais elles ont une valeur par défaut de `undefined`. Donc, tenter d'accéder à `printName` avant la ligne où elle est initialisée avec l'expression de fonction est interprété comme `undefined()`, et comme vous le savez, "undefined is not a function".

Vous pouvez en apprendre plus sur [les différences de hoisting entre var, let et const ici](https://www.freecodecamp.org/news/javascript-let-and-const-hoisting/)

## Conclusion

Bien que les fonctions fléchées vous permettent d'écrire des fonctions de manière plus concise, elles ont également des limitations. Comme nous l'avons vu dans cet article, certains des comportements qui se produisent dans les fonctions normales ne se produisent pas dans les fonctions fléchées.

Si vous souhaitez créer des constructeurs, conserver le comportement normal de `this` ou avoir vos fonctions élevées, alors les fonctions fléchées ne sont pas la bonne approche.

Si vous avez aimé cet article, veuillez le partager avec d'autres :)