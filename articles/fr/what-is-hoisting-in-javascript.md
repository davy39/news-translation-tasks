---
title: Qu'est-ce que le Hoisting en JavaScript ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-11T16:12:59.000Z'
originalURL: https://freecodecamp.org/news/what-is-hoisting-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/pexels-pixabay-532079.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce que le Hoisting en JavaScript ?
seo_desc: 'By Zach Snoek

  In JavaScript, hoisting allows you to use functions and variables before they''re
  declared. In this post, we''ll learn what hoisting is and how it works.

  What is hoisting?

  Take a look at the code below and guess what happens when it runs:...'
---

Par Zach Snoek

En JavaScript, le hoisting permet d'utiliser des fonctions et des variables avant qu'elles ne soient déclarées. Dans cet article, nous allons apprendre ce qu'est le hoisting et comment il fonctionne.

## Qu'est-ce que le hoisting ?

Jetez un œil au code ci-dessous et devinez ce qui se passe lorsqu'il s'exécute :

```js
console.log(foo);
var foo = 'foo';
```

Il peut vous surprendre que ce code affiche `undefined` et ne génère pas d'erreur ou ne lance pas d'exception — même si `foo` est assigné après que nous l'ayons `console.log` !

Cela est dû au fait que l'interpréteur JavaScript sépare la déclaration et l'assignation des fonctions et des variables : il "hoiste" vos déclarations en haut de leur portée avant l'exécution.

Ce processus est appelé hoisting, et il nous permet d'utiliser `foo` avant sa déclaration dans notre exemple ci-dessus.

Examinons plus en détail le hoisting des fonctions et des variables pour comprendre ce que cela signifie et comment cela fonctionne.

## Hoisting des variables en JavaScript

Pour rappel, nous **déclarons** une variable avec les instructions `var`, `let` et `const`. Par exemple :

```js
var foo;
let bar;
```

Nous **assignons** une valeur à une variable en utilisant l'opérateur d'assignation :

```jsx
// Déclaration
var foo;
let bar;

// Assignation
foo = 'foo';
bar = 'bar';
```

Dans de nombreux cas, nous pouvons combiner la déclaration et l'assignation en une seule étape :

```js
var foo = 'foo';
let bar = 'bar';
const baz = 'baz';
```

Le hoisting des variables agit différemment selon la manière dont la variable est déclarée. Commençons par comprendre le comportement des variables `var`.

### Hoisting des variables avec `var`

Lorsque l'interpréteur hoiste une variable déclarée avec `var`, il initialise sa valeur à `undefined`. La première ligne de code ci-dessous affichera `undefined` :

```js
console.log(foo); // undefined

var foo = 'bar';

console.log(foo); // "bar"
```

Comme nous l'avons défini précédemment, le hoisting provient de la séparation par l'interpréteur de la déclaration et de l'assignation des variables. Nous pouvons obtenir ce même comportement manuellement en séparant la déclaration et l'assignation en deux étapes :

```js
var foo;

console.log(foo); // undefined

foo = 'foo';

console.log(foo); // "foo"
```

Rappelez-vous que le premier `console.log(foo)` affiche `undefined` parce que `foo` est hoisté et reçoit une valeur par défaut (pas parce que la variable n'est jamais déclarée). L'utilisation d'une variable non déclarée lancera une `ReferenceError` :

```js
console.log(foo); // Uncaught ReferenceError: foo is not defined
```

L'utilisation d'une variable non déclarée avant son assignation lancera également une `ReferenceError` parce qu'aucune déclaration n'a été hoistée :

```js
console.log(foo); // Uncaught ReferenceError: foo is not defined
foo = 'foo';      // Assigner une variable non déclarée est valide
```

À ce stade, vous pourriez penser : "Hmm, c'est un peu étrange que JavaScript nous permette d'accéder à des variables avant qu'elles ne soient déclarées." Ce comportement est une partie inhabituelle de JavaScript et peut entraîner des erreurs. Utiliser une variable avant sa déclaration n'est généralement pas souhaitable.

Heureusement, les variables `let` et `const`, introduites dans ECMAScript 2015, se comportent différemment.

### Hoisting des variables avec `let` et `const`

Les variables déclarées avec `let` et `const` sont hoistées mais ne sont pas initialisées avec une valeur par défaut. Accéder à une variable `let` ou `const` avant qu'elle ne soit déclarée entraînera une `ReferenceError` :

```js
console.log(foo); // Uncaught ReferenceError: Cannot access 'foo' before initialization

let foo = 'bar';  // Même comportement pour les variables déclarées avec const
```

Remarquez que l'interpréteur hoiste toujours `foo` : le message d'erreur nous indique que la variable est initialisée quelque part.

### La zone morte temporelle

La raison pour laquelle nous obtenons une erreur de référence lorsque nous essayons d'accéder à une variable `let` ou `const` avant sa déclaration est due à la zone morte temporelle (TDZ).

La TDZ commence au début de la portée englobante de la variable et se termine lorsqu'elle est déclarée. Accéder à la variable dans cette TDZ lance une `ReferenceError`.

Voici un exemple avec un bloc explicite qui montre le début et la fin de la TDZ de `foo` :

```js
{
 	// Début de la TDZ de foo
  	let bar = 'bar';
	console.log(bar); // "bar"

	console.log(foo); // ReferenceError car nous sommes dans la TDZ

	let foo = 'foo';  // Fin de la TDZ de foo
}
```

La TDZ est également présente dans les paramètres de fonction par défaut, qui sont évalués de gauche à droite. Dans l'exemple suivant, `bar` est dans la TDZ jusqu'à ce que sa valeur par défaut soit définie :

```js
function foobar(foo = bar, bar = 'bar') {
  console.log(foo);
}
foobar(); // Uncaught ReferenceError: Cannot access 'bar' before initialization
```

Mais ce code fonctionne car nous pouvons accéder à `foo` en dehors de sa TDZ :

```jsx
function foobar(foo = 'foo', bar = foo) {
  console.log(bar);
}
foobar(); // "foo"
```

### `typeof` dans la zone morte temporelle

L'utilisation d'une variable `let` ou `const` comme opérande de l'opérateur `typeof` dans la TDZ lancera une erreur :

```js
console.log(typeof foo); // Uncaught ReferenceError: Cannot access 'foo' before initialization
let foo = 'foo';
```

Ce comportement est cohérent avec les autres cas de `let` et `const` dans la TDZ que nous avons vus. La raison pour laquelle nous obtenons une `ReferenceError` ici est que `foo` est déclaré mais non initialisé — nous devons être conscients que nous l'utilisons avant son initialisation ([source : Axel Rauschmayer](https://2ality.com/2015/10/why-tdz.html)).

Cependant, ce n'est pas le cas lors de l'utilisation d'une variable `var` avant sa déclaration, car elle est initialisée avec `undefined` lorsqu'elle est hoistée :

```jsx
console.log(typeof foo); // "undefined"
var foo = 'foo';
```

De plus, il est surprenant que nous puissions vérifier le type d'une variable qui n'existe pas sans erreur. `typeof` retourne en toute sécurité une chaîne :

```js
console.log(typeof foo); // "undefined"
```

En fait, l'introduction de `let` et `const` a rompu la garantie de `typeof` de toujours retourner une valeur de chaîne pour n'importe quel opérande.

## Hoisting des fonctions en JavaScript

Les déclarations de fonctions sont également hoistées. Le hoisting des fonctions nous permet d'appeler une fonction avant qu'elle ne soit définie. Par exemple, le code suivant s'exécute avec succès et affiche `"foo"` :

```js
foo(); // "foo"

function foo() {
	console.log('foo');
}
```

Notez que seules les déclarations de fonctions sont hoistées, pas les expressions de fonctions. Cela devrait avoir du sens : comme nous venons de l'apprendre, les assignations de variables ne sont pas hoistées.

Si nous essayons d'appeler la variable à laquelle l'expression de fonction a été assignée, nous obtiendrons une `TypeError` ou une `ReferenceError`, selon la portée de la variable :

```js
foo(); // Uncaught TypeError: foo is not a function
var foo = function () { }

bar(); // Uncaught ReferenceError: Cannot access 'bar' before initialization
let bar = function () { }

baz(); // Uncaught ReferenceError: Cannot access 'baz' before initialization
const baz = function () { }
```

Cela diffère de l'appel d'une fonction qui n'est jamais déclarée, ce qui lance une `ReferenceError` différente :

```js
foo(); // Uncaught ReferenceError: baz is not defined
```

## Comment utiliser le hoisting en JavaScript

### Hoisting des variables

En raison de la confusion que le hoisting de `var` peut créer, il est préférable d'éviter d'utiliser des variables avant qu'elles ne soient déclarées. Si vous écrivez du code dans un [projet greenfield](https://en.wikipedia.org/wiki/Greenfield_project), vous devriez utiliser `let` et `const` pour imposer cela.

Si vous travaillez dans une base de code plus ancienne ou devez utiliser `var` pour une autre raison, [MDN recommande](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#var_hoisting) d'écrire les déclarations `var` aussi près que possible du haut de leur portée. Cela rendra la portée de vos variables plus claire.

Vous pouvez également envisager d'utiliser la règle `no-use-before-define` [ESLint](https://eslint.org/docs/rules/no-use-before-define) qui garantira que vous n'utilisez pas une variable avant sa déclaration.

### Hoisting des fonctions

Le hoisting des fonctions est utile car nous pouvons cacher l'implémentation des fonctions plus bas dans le fichier et laisser le lecteur se concentrer sur ce que le code fait. En d'autres termes, nous pouvons ouvrir un fichier et voir ce que le code fait sans d'abord comprendre comment il est implémenté.

Prenons l'exemple suivant :

```js
resetScore();
drawGameBoard();
populateGameBoard();
startGame();

function resetScore() {
	console.log("Réinitialisation du score");
}

function drawGameBoard() {
	console.log("Dessin du plateau");
}

function populateGameBoard() {
	console.log("Remplissage du plateau");
}

function startGame() {
	console.log("Démarrage du jeu");
}
```

Nous avons immédiatement une idée de ce que fait ce code sans avoir à lire toutes les déclarations de fonctions.

Cependant, l'utilisation de fonctions avant leur déclaration est une question de préférence personnelle. Certains développeurs, comme Wes Bos, préfèrent éviter cela et placer les fonctions dans des modules qui peuvent être importés selon les besoins ([source : Wes Bos](https://wesbos.com/javascript/03-the-tricky-bits/hoisting)).

Le guide de style d'Airbnb va plus loin et encourage les expressions de fonctions nommées plutôt que les déclarations pour éviter les références avant la déclaration :

> Les déclarations de fonctions sont hoistées, ce qui signifie qu'il est facile — trop facile — de référencer la fonction avant qu'elle ne soit définie dans le fichier. Cela nuit à la lisibilité et à la maintenabilité.
> 
> Si vous trouvez qu'une fonction est suffisamment grande ou complexe pour interférer avec la compréhension du reste du fichier, alors peut-être est-il temps de l'extraire dans son propre module ! ([Source : Guide de style JavaScript d'Airbnb](https://airbnb.io/javascript/#functions--declarations))

## Conclusion

Merci d'avoir lu cet article, et j'espère qu'il vous a aidé à comprendre le hoisting en JavaScript. N'hésitez pas à me contacter sur [LinkedIn](https://www.linkedin.com/in/zach-snoek-5b327b179/) si vous souhaitez vous connecter ou si vous avez des questions !