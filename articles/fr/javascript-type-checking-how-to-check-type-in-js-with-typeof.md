---
title: Vérification de type JavaScript – Comment vérifier le type en JS avec typeof()
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-12-09T22:16:19.000Z'
originalURL: https://freecodecamp.org/news/javascript-type-checking-how-to-check-type-in-js-with-typeof
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/cover-template.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Vérification de type JavaScript – Comment vérifier le type en JS avec typeof()
seo_desc: 'JavaScript is a dynamically typed (or loosely typed) programming language.
  It allows you to declare variables without specifying or defining the variable type.

  You can create a variable in JavaScript without defining the type of value you can
  store i...'
---

JavaScript est un langage de programmation à typage dynamique (ou à typage faible). Il vous permet de déclarer des variables sans spécifier ou définir le type de variable.

Vous pouvez créer une variable en JavaScript sans définir le type de valeur que vous pouvez stocker dans la variable. Cela peut affecter votre programme et causer des bugs pendant l'exécution car le type peut changer.

Par exemple, une variable peut être déclarée et assignée à un nombre. Mais à mesure que vous écrivez plus de code, les valeurs peuvent être déplacées, et vous pourriez assigner la même variable à une chaîne de caractères ou un booléen. Cela affecterait votre code lorsqu'il s'exécute :

```js
let myVariable = 45; // => number
myVariable = 'John Doe'; // => string
myVariable = false; // => boolean
```

Comme vous pouvez le voir dans l'exemple ci-dessus, une variable en JavaScript peut changer de type tout au long de l'exécution d'un programme. Cela peut être difficile à suivre en tant que programmeur. C'est l'une des raisons pour lesquelles TypeScript est considéré comme un sur-ensemble de JavaScript.

Pour valider les variables en vérifiant leurs types en JavaScript, vous pouvez utiliser l'opérateur `typeof`. La vérification de type en JavaScript n'est pas simple pour les types de données non primitifs et les valeurs spécifiques. C'est pourquoi la vérification de type peut devenir ennuyeuse, surtout pour les développeurs JS inexpérimentés.

Dans cet article, vous apprendrez comment utiliser l'opérateur `typeof`, les instances où vous ne devriez pas utiliser `typeof`, et la meilleure façon de vérifier le type en JavaScript pour de telles instances.

## Types de données JavaScript

En JavaScript, les types de données sont classés en deux groupes : vous avez les types de données primitifs et non primitifs. À part l'objet, qui est un type de données non primitif, tous les autres types de données sont primitifs.

Ces types de données incluent :

1. String
   
2. Number
   
3. Boolean (true et false)
   
4. null
   
5. undefined
   
6. Symbol

À ce stade, vous pourriez penser que j'ai omis les tableaux et les fonctions. Mais non, je ne l'ai pas fait. C'est parce qu'ils sont tous les deux des objets.

## Comment vérifier le type avec l'opérateur `typeof` en JavaScript

L'opérateur `typeof` accepte un seul opérande (un opérateur unaire) et détermine le type de l'opérande.

Il existe deux façons d'utiliser l'opérateur `typeof`. Vous pouvez évaluer une seule valeur ou une expression :

```js
typeof(expression);

// Ou

typeof value;
```

L'opérateur `typeof` retournera le type sous forme de chaîne, ce qui signifie "number", "string", "boolean", et bien plus encore.

```js
let myVariable = 45;
console.log(typeof myVariable); // retourne "number"
console.log(typeof(myVariable)); // retourne "number"

console.log(typeof 45); // retourne "number"
console.log(typeof(45)); // retourne "number"
```

Il est important de savoir que vous devez toujours utiliser la méthode d'expression (sous la forme d'une fonction) lors de l'évaluation d'une [expression](https://flaviocopes.com/javascript-expressions/) plutôt que d'une seule valeur. Par exemple :

```js
console.log(typeof(typeof 45)); // retourne "string"
```

Le code ci-dessus retourne une chaîne parce que la sortie de `typeof 45` est évaluée comme "number" (qui est retournée comme une chaîne), puis la sortie de `typeof("number")` est évaluée comme "string".

Un autre exemple est si votre nombre contient un trait d'union :

```js
// Utilisation de l'expression
console.log(typeof(123-4567-890)); // retourne "number"

// Utilisation de la valeur unique
console.log(typeof 123-4567-890); // retourne NaN
```

La méthode de valeur unique retournera `NaN` (Not a Number) parce qu'elle évaluera d'abord `typeof 123`, qui retournera une chaîne, "number". Cela signifie que vous avez maintenant `"number" - 4567-890`, qui ne peut pas être soustrait et retournera `NaN`.

### Comment vérifier le type de données Number

Explorons maintenant les instances possibles qui retourneront le type de données number.

Il existe différentes valeurs possibles que JavaScript considère comme un nombre, telles que les entiers positifs et négatifs, zéro, les nombres à virgule flottante et l'infini :

```js
console.log(typeof 33); // retourne "number"
console.log(typeof -23); // retourne "number"
console.log(typeof 0); // retourne "number"
console.log(typeof 1.2345); // retourne "number"
console.log(typeof Infinity); // retourne "number"
```

Il est également important de savoir que des valeurs comme NaN, même si cela signifie Not-a-Number, retourneront toujours un type de "number". De plus, les fonctions mathématiques auront le type de données number :

```js
console.log(typeof NaN); // retourne "number"
console.log(typeof Math.LOG2E); // retourne "number"
```

Enfin, lorsque vous utilisez le constructeur `Number()` pour typer explicitement une chaîne qui contient un nombre en un nombre ou même une valeur comme une chaîne réelle qui ne peut pas être typée en un entier, il retournera toujours un nombre comme son type de données :

```js
// Typage de la valeur en nombre
console.log(typeof Number(`123`)); // retourne "number"

// La valeur ne peut pas être typée en entier
console.log(typeof Number(`freeCodeCamp`)); // retourne "number"
```

Enfin, lorsque vous utilisez des méthodes comme parseInt() et parseFloat(), qui convertissent une chaîne en un nombre et arrondissent également un nombre, son type de données sera number :

```js
console.log(typeof parseInt(`123`)); // retourne "number"
console.log(typeof parseFloat(`123.456`)); // retourne "number"
```

### Comment vérifier le type de données String

Il existe quelques instances qui retourneront "string". Ces instances sont la chaîne vide, une chaîne de caractères (ceci peut également être un nombre), et plusieurs mots :

```js
console.log(typeof ''); // retourne "string"
console.log(typeof 'freeCodeCamp'); // retourne "string"
console.log(typeof 'freeCodeCamp offre les meilleures ressources gratuites'); // retourne "string"
console.log(typeof '123'); // retourne "string"
```

De plus, lorsque vous utilisez le constructeur `String()` avec n'importe quelle valeur :

```js
console.log(typeof String(123)); // retourne "string"
```

### Comment vérifier le type de données Boolean

Lorsque vous vérifiez les valeurs `true` et `false`, il retournera toujours le type "boolean". De plus, lorsque vous vérifiez quelque chose qui utilise le constructeur `Boolean()` :

```js
console.log(typeof true); // retourne "boolean"
console.log(typeof false); // retourne "boolean"
console.log(typeof Boolean(0)); // retourne "boolean"
```

De plus, lorsque vous utilisez l'opérateur double not (`!!`), qui fonctionne comme le constructeur `Boolean()`, "boolean" sera retourné :

```js
console.log(typeof !!(0)); // retourne "boolean"
```

### Comment vérifier le type de données Symbol

Lorsque vous utilisez le constructeur `Symbol()`, le type de données "symbol" sera retourné même si aucune valeur n'est passée. De plus, lorsque vous passez un paramètre ou utilisez le symbole `Symbol.iterator`, qui spécifie l'itérateur par défaut pour un objet :

```js
console.log(typeof Symbol()); // retourne "symbol"
console.log(typeof Symbol('parameter')); // retourne "symbol"
console.log(typeof Symbol.iterator); // retourne "symbol"
```

### Comment vérifier le type de données Undefined

Une variable est dite `undefined` lorsque vous la déclarez sans initier une valeur. Lorsque vous vérifiez undefined, une variable déclarée sans valeur (undefined), et une variable non définie, elles retourneront toujours "undefined" :

```js
// Utilisation du mot-clé undefined
console.log(typeof undefined); // retourne "undefined"

// variable est déclarée mais undefined (n'a pas de valeur intentionnellement)
let a;
console.log(typeof a); // retourne "undefined"

// Utilisation de la variable undefined
console.log(typeof v); // retourne "undefined"
```

Jusqu'à présent, vous avez appris comment vérifier les types de tous les types de données primitifs sauf null. C'est un peu délicat et je l'ai couvert en détail dans mon article sur [Null Checking in JavaScript Explained](https://www.freecodecamp.org/news/how-to-check-for-null-in-javascript/).

Mais je vais brièvement passer en revue comment vérifier `null` dans cet article pour que vous puissiez comprendre les bases.

### Comment vérifier le type de données Object

Certaines instances retourneront toujours "object", bien que celle de `null` soit un [bug historique](https://www.turbinelabs.com/blog/the-odd-history-of-javascripts-null) qui ne peut pas être corrigé, tandis que la fonction a sa raison technique.

```js
console.log(typeof null);
console.log(typeof [1, 2, 3, "freeCodeCamp"]);
console.log(typeof { age: 12, name: "John Doe" });
console.log(typeof [1, 2, 3, 4, 5, 6]);
```

Comme vous pouvez le voir dans l'exemple ci-dessus, un tableau retournera toujours "object" lorsque vous utilisez l'opération `typeof`. Cela peut ne pas être très agréable, mais techniquement, un Array est un type spécial d'objet :

```js
console.log(typeof [1, 2, 3, 'freeCodeCamp']);
```

Dans ES6, la méthode `Array.isArray` a été introduite, ce qui vous permet de détecter un Array facilement :

```js
console.log(Array.isArray([1, 2, 3, "freeCodeCamp"])); // retourne true
console.log(Array.isArray({ age: 12, name: "John Doe" })); // retourne false
```

De plus, avant l'introduction de ES6, l'opérateur `instanceof` est utilisé pour détecter un Array :

```js
const isArray = (input) => {
    return input instanceof Array;
};

console.log(isArray([1, 2, 3, 'freeCodeCamp'])); // retourne true
```

### Comment vérifier le type de données Null

Lorsque vous utilisez l'opérateur `typeof` pour vérifier la valeur `null`, il retourne "object" à cause d'un [bug historique](https://www.turbinelabs.com/blog/the-odd-history-of-javascripts-null) qui ne peut pas être corrigé.

**Note :** Ne confondez pas null avec undefined. Une variable est appelée `null` si elle contient intentionnellement la valeur `null`. En revanche, une variable est `undefined` lorsque vous la déclarez sans initier une valeur.

Une façon très simple de détecter `null` est d'utiliser la comparaison stricte :

```js
const isNull = (input) => {
    return input === null;
}

let myVar = null;
console.log(isNull(myVar)); // retourne true
```

Vous pouvez lire cet article sur [Null Checking in JavaScript Explained](https://www.freecodecamp.org/news/how-to-check-for-null-in-javascript/) pour plus d'options et d'explications détaillées.

## Une solution générique pour la vérification de type en JavaScript

Dans un article précédent de [Tapas Adhikary](https://www.freecodecamp.org/news/author/tapas/) sur [How to Check the Type of a Variable or Object in JS](https://www.freecodecamp.org/news/javascript-typeof-how-to-check-the-type-of-a-variable-or-object-in-js/), il a ajouté et expliqué une solution générique que vous pouvez utiliser pour vérifier le type plus précisément :

```js
const typeCheck = (value) => {
    const return_value = Object.prototype.toString.call(value);
    const type = return_value.substring(
    return_value.indexOf(" ") + 1,
    return_value.indexOf("]")
    );

    return type.toLowerCase();
};
```

Testons cela :

```js
console.log(typeCheck([])); // retourne 'array'
console.log(typeCheck(new Date())); // retourne 'date'
console.log(typeCheck(new String("freeCodeCamp"))); // retourne 'string'
console.log(typeCheck(new Boolean(true))); // retourne 'boolean'
console.log(typeCheck(null)); // retourne 'null'
```

## Conclusion

Dans cet article, vous avez appris comment vérifier les types en JavaScript avec l'opérateur `typeof`.

Vous avez également appris les limitations et comment utiliser d'autres méthodes pour surmonter ces limitations. N'oubliez pas que pour la plupart des types de données primitifs, vous pouvez toujours utiliser l'opérateur `typeof`.

Amusez-vous bien à coder !