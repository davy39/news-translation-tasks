---
title: Fonctions fléchées JavaScript vs Fonctions régulières
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2024-01-16T22:19:05.000Z'
originalURL: https://freecodecamp.org/news/regular-vs-arrow-functions-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-6.53.58-PM.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: functions
  slug: functions
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Fonctions fléchées JavaScript vs Fonctions régulières
seo_desc: 'In JavaScript, there are two main ways of writing functions. You can create
  functions using the regular function syntax. Or you can use the arrow function syntax.

  In this article, you will learn how to use both options. You''ll also learn about
  the di...'
---

En JavaScript, il existe deux principales façons d'écrire des fonctions. Vous pouvez créer des fonctions en utilisant la syntaxe de fonction régulière. Ou vous pouvez utiliser la syntaxe de fonction fléchée.

Dans cet article, vous apprendrez à utiliser les deux options. Vous apprendrez également les différences entre les deux et quand il est approprié d'utiliser chacune d'elles.

## Table des matières

* [Syntaxe des fonctions régulières vs Syntaxe des fonctions fléchées](#syntaxe-des-fonctions-regulieres-vs-syntaxe-des-fonctions-flechees)
    
* [Comment accéder aux arguments passés aux fonctions](#comment-acceder-aux-arguments-passes-aux-fonctions)
    
* [Paramètres nommés dupliqués](#parametres-nommes-dupliques)
    
* [Hoisting des fonctions](#hoisting-des-fonctions)
    
* [Comment gérer la liaison de "this" dans les fonctions](#comment-gerer-la-liaison-de-this-dans-les-fonctions)
    
* [Comment utiliser les fonctions comme constructeurs](#comment-utiliser-les-fonctions-comme-constructeurs)
    
* [Alors, laquelle devez-vous utiliser ?](#alors-laquelle-devez-vous-utiliser)
    

## Syntaxe des fonctions régulières vs Syntaxe des fonctions fléchées

Pour comprendre la différence entre les deux options, commençons par examiner leur syntaxe.

### Syntaxe des fonctions régulières

La manière ordinaire de déclarer des fonctions en JavaScript est d'utiliser le mot-clé `function`. Voici un exemple :

```javascript
function sayHello(name) {
  return 'Hello ' + name
}
```

Pour retourner une valeur d'une fonction régulière, vous devez explicitement utiliser le mot-clé `return`. Sinon, la fonction retournera `undefined`.

### Syntaxe des fonctions fléchées

Les fonctions fléchées ont été introduites avec ECMAScript 6 (ES6). Elles vous offrent une manière plus concise de définir des fonctions en JavaScript.

En utilisant la même fonction `sayHello` de l'exemple précédent, voyons comment la créer avec la syntaxe de fonction fléchée.

```javascript
const sayHello = (name) => {
  return 'Hello ' + name
}
```

Contrairement aux fonctions régulières, vous n'avez pas à utiliser un retour explicite s'il n'y a qu'une seule instruction comme dans l'exemple ci-dessus. Vous pouvez écrire la fonction sur une seule ligne comme ceci.

```javascript
const sayHello = (name) => 'Hello ' + name
```

Remarquez comment les accolades sont également supprimées pour retourner implicitement le résultat de l'expression. Vous pouvez même supprimer les parenthèses si il n'y a qu'un seul argument. Voir l'exemple ci-dessous :

```javascript
const sayHello = name => 'Hello ' + name
```

Le `name` est le seul argument que la fonction prend. Et cela signifie que vous pouvez supprimer les parenthèses de l'argument et cela fonctionnera toujours bien.

## Comment accéder aux arguments passés aux fonctions

JavaScript fournit un moyen d'accéder à tous les arguments passés à une fonction. Mais la manière dont vous accédez à ces arguments dépend du type de fonction avec lequel vous travaillez.

### Comment accéder aux arguments avec les fonctions régulières

Vous pouvez accéder à tous les arguments passés à une fonction régulière en utilisant l'objet `arguments`. L'objet `arguments` est un objet de type tableau qui contient tous les arguments passés à la fonction.

Exemple :

```javascript
function logNumbers(num1, num2) {
  console.log(arguments)
}

logNumbers(8, 24)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-11-at-5.01.51-PM.png align="left")

*Résultats de journalisation de l'objet arguments*

Comme vous pouvez le voir à partir du résultat de la journalisation, l'objet `arguments` contient les deux nombres passés en arguments à la fonction `logNumbers`.

### Comment accéder aux arguments avec les fonctions fléchées

L'objet `arguments` n'est pas disponible dans les fonctions fléchées. Si vous essayez d'y accéder dans les fonctions fléchées, JavaScript lancera une erreur de référence.

```javascript
const logNumbers = (num1, num2) => {
  console.log(arguments)
}

logNumbers(8, 24) // Uncaught ReferenceError: arguments is not defined
```

Pour accéder aux arguments passés à une fonction fléchée, vous pouvez utiliser la syntaxe des paramètres restants (`...`).

Exemple :

```javascript
const logNumbers = (...args) => {
  console.log(args)
}

logNumbers(8, 24)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-11-at-11.13.39-PM.png align="left")

*Résultats de journalisation pour les arguments d'une fonction fléchée*

En utilisant la syntaxe des paramètres restants (`...`), vous obtenez l'accès à tous les arguments passés à la fonction `logNumbers`.

## Paramètres nommés dupliqués

Une autre différence entre les fonctions régulières et les fonctions fléchées est la manière dont elles gèrent les doublons dans les paramètres nommés.

### Paramètres nommés dupliqués dans les fonctions régulières

Lorsque une fonction régulière a des noms dupliqués dans les paramètres, le dernier paramètre avec le nom dupliqué prendra le dessus. Voyons un exemple :

```javascript
function exampleFunction(a, b, a) {
  console.log(a, b)
}

exampleFunction("first", "second", "third")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-9.50.00-AM.png align="left")

*Résultats de journalisation pour les paramètres nommés dupliqués*

Dans l'exemple ci-dessus, l'argument `third` remplace la valeur de l'argument `first` parce que le dernier paramètre dupliqué est celui qui prend le dessus.

Mais en mode "strict", l'utilisation d'un paramètre nommé dupliqué entraînera une erreur de syntaxe.

```javascript
"use strict"

function exampleFunction(a, b, a) {
  console.log(a, b)
}

exampleFunction("first", "second", "third")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-10.29.11-AM.png align="left")

*Le mode strict n'autorise pas l'utilisation d'un nom de paramètre plus d'une fois*

### Paramètres nommés dupliqués dans les fonctions fléchées

Les fonctions fléchées n'autorisent pas l'utilisation du même nom de paramètre plus d'une fois dans la liste des paramètres. Faire cela entraînera une erreur de syntaxe.

Exemple :

```javascript
const exampleFunction = (a, b, a) => {
  console.log(a, b)
}

exampleFunction("first", "second", "third")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-10.29.11-AM-1.png align="left")

*Les fonctions fléchées n'autorisent pas les noms de paramètres dupliqués*

## Hoisting des fonctions

Le hoisting en JavaScript est un comportement où les variables et les fonctions sont déplacées en haut de leur portée contenant pendant la compilation, avant que le code ne soit exécuté.

### Hoisting dans les fonctions régulières

Les fonctions régulières sont hissées en haut. Et vous pouvez y accéder et les appeler même avant qu'elles ne soient déclarées.

```javascript
regularFunction()

function regularFunction() {
  console.log("This is a regular function.")
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-11.50.43-AM.png align="left")

*Résultat de journalisation de l'appel de la fonction régulière avant sa déclaration*

L'exemple ci-dessus montre l'appel d'une fonction régulière avant sa déclaration. Et cela fonctionne bien sans lancer d'erreur grâce au hoisting des fonctions.

### Hoisting dans les fonctions fléchées

Les fonctions fléchées, en revanche, ne peuvent pas être accessibles avant leur initialisation.

```javascript
arrowFunction()

const arrowFunction = () => {
  console.log("This is an arrow function.")
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-12.07.39-PM.png align="left")

*Résultat de journalisation de l'appel de la fonction fléchée avant sa déclaration*

Contrairement aux fonctions régulières, tenter d'appeler une fonction fléchée avant sa déclaration entraînera une erreur de référence, comme vous pouvez le voir à partir de la sortie ci-dessus.

## Comment gérer la liaison de `this` dans les fonctions

Les fonctions régulières ont leur propre contexte `this`. Et celui-ci est déterminé dynamiquement en fonction de la manière dont vous appelez ou exécutez la fonction.

Les fonctions fléchées, en revanche, n'ont pas leur propre contexte `this`. Au lieu de cela, elles capturent la valeur `this` du contexte lexical environnant dans lequel la fonction fléchée a été créée.

Les deux scénarios suivants utilisent à la fois des fonctions régulières et des fonctions fléchées. Vous verrez comment le contexte `this` est déterminé.

### 1. Définir la valeur `this` lors d'un appel de fonction simple

Pour les fonctions régulières, un simple appel de fonction définit la valeur `this` sur l'objet `window` (ou sur `undefined` si vous utilisez le mode "strict") :

```javascript
function myRegularFunction() {
  console.log(this)
}
    
myRegularFunction()
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-4.15.11-PM.png align="left")

*Une simple invocation d'une fonction régulière définit* `this` sur l'objet window

```javascript
"use strict"

function myFunction() {
  console.log(this)
}
    
myFunction() // udefined
```

Avec les fonctions fléchées, un simple appel de fonction définit la valeur `this` sur le contexte environnant, que vous utilisiez le mode strict ou non. Dans l'exemple ci-dessous, le contexte environnant est l'objet window global.

```javascript
const myArrowFunction = () => {
  console.log(this);
};

myArrowFunction()
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-4.15.11-PM-1.png align="left")

*Une simple invocation d'une fonction fléchée définit* `this` sur l'objet window

### 2. Lors de l'invocation ou de l'appel d'une méthode sur un objet

Lorsque vous invoquez une méthode dont la valeur est une fonction régulière, la valeur `this` est définie sur l'objet sur lequel la méthode est appelée. Mais lorsque la valeur de la méthode est une fonction fléchée, la valeur `this` est définie sur l'objet window global.

```javascript
const myObject = {
  regularExample: function() {
    console.log("REGULAR: ", this)
  },
    
  arrowExample: () => {
    console.log("ARROW: ", this)
  }
}
    
myObject.regularExample()
myObject.arrowExample()
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-5.46.04-PM.png align="left")

*Résultat de journalisation pour une méthode avec une fonction régulière et une autre avec une fonction fléchée*

Alors que la méthode avec la fonction régulière journalise l'objet dans la console, celle avec la fonction fléchée journalise l'objet window global à la place.

## Comment utiliser les fonctions comme constructeurs

Pour les fonctions régulières, vous pouvez créer une nouvelle instance en utilisant le mot-clé `new`. Et cela définit la valeur `this` sur la nouvelle instance que vous avez créée.

Pour les fonctions fléchées, vous ne pouvez pas les utiliser comme constructeurs. Cela est dû au fait que la valeur de `this` dans les fonctions fléchées est lexicalement scopée, c'est-à-dire déterminée par le contexte d'exécution environnant. Ce comportement ne les rend pas adaptées pour être utilisées comme constructeurs.

Voici un exemple :

```javascript
function RegularFuncBird(name, color) {
  this.name = name
  this.species = color
  console.log(this)
}

const ArrowFuncBird = (name, color) => {
  this.name = name
  this.color = color
  console.log(this)
}

new RegularFuncBird("Parrot", "blue") 
new ArrowFuncBird("Parrot", "blue")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-5.53.17-PM.png align="left")

*Résultats de journalisation pour la tentative d'utilisation de fonctions régulières et fléchées comme constructeurs*

Le constructeur `RegularFuncBird` fonctionne bien avec le mot-clé `new`, mais `ArrowFuncBird` entraîne une erreur de type.

## Alors, laquelle devez-vous utiliser ?

Il n'y a pas de réponse simple à cette question. Que vous utilisiez une fonction régulière ou une fonction fléchée dépend du cas d'utilisation spécifique.

Il est recommandé d'utiliser une fonction régulière dans l'un des cas suivants :

* lorsque vous devez utiliser un constructeur avec le mot-clé `new`
    
* lorsque vous avez besoin que la liaison `this` soit dynamiquement scopée
    
* lorsque vous souhaitez utiliser l'objet `arguments`
    

Et vous pouvez utiliser des fonctions fléchées dans l'un des cas suivants :

* lorsque vous voulez une syntaxe plus concise pour la fonction
    
* lorsque vous devez maintenir la portée lexicale de `this`
    
* pour les fonctions non-méthodes (dans la plupart des cas)
    

Comme vous l'avez appris dans cet article, les deux sont des moyens valides de définir des fonctions en JavaScript. Rappelez-vous que le choix entre elles n'est pas toujours une question de préférence personnelle. Plutôt, cela dépend du type de comportement que vous attendez de la fonction.

Merci d'avoir lu et bon codage !