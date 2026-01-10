---
title: Concepts JavaScript à connaître avant d'apprendre Node.js
subtitle: ''
author: Musab Habeeb
co_authors: []
series: null
date: '2023-09-19T15:12:57.000Z'
originalURL: https://freecodecamp.org/news/javascript-concepts-to-know-before-learning-node-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/JavaScript-Concepts-to-master-before-Node.js.png
tags:
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: Concepts JavaScript à connaître avant d'apprendre Node.js
seo_desc: 'Before Node.js came into existence, JavaScript could only be run on the
  browser. It could only be used as a scripting language for frontend web development.

  Then, Node.js came to free JavaScript from this confinement. It made JavaScript
  ubiquitous (m...'
---

Avant l'existence de Node.js, JavaScript ne pouvait être exécuté que dans le navigateur. Il ne pouvait être utilisé que comme langage de script pour le développement web frontend.

Ensuite, Node.js est arrivé pour libérer JavaScript de cette confinement. Il a rendu JavaScript omniprésent (ce qui signifie qu'il peut maintenant être exécuté partout).

Node.js est un environnement d'exécution JavaScript qui permet aux développeurs JavaScript d'écrire des outils en ligne de commande et des scripts côté serveur en dehors d'un navigateur.

Apprendre Node.js permet aux développeurs JavaScript d'écrire du code côté serveur et du code pour des systèmes embarqués. Cela ouvre des opportunités dans le développement backend et la programmation matérielle.

Mais, avant de plonger dans Node.js, un développeur JavaScript doit apprendre et comprendre certains concepts JavaScript.

Dans cet article, vous allez apprendre les concepts JavaScript que vous devez comprendre avant d'apprendre Node.js.

Avant de continuer avec l'article, vérifiez les prérequis.

## Prérequis

Pour suivre cet article, vous devez avoir quelques connaissances de base sur :

* JavaScript

* La console du navigateur (c'est là que vous exécuterez votre code).

Maintenant que nous avons cela hors de notre chemin, plongeons dans l'article, en commençant par les expressions.

## Expressions

Une expression est une unité ou un bloc de code qui évalue une valeur.

Il existe cinq catégories de base d'expressions en JavaScript : les expressions primaires, les expressions arithmétiques, les expressions de chaîne, les expressions logiques et les expressions du côté gauche.

### Expressions primaires

Les expressions primaires consistent en des mots-clés de base en JavaScript. Un exemple courant est le mot-clé `this` :

```js
this['item'];

this.item;
```

Plus tard dans cet article, vous en apprendrez davantage sur le mot-clé `this`.

### Expressions arithmétiques

Un opérateur arithmétique prend des valeurs numériques comme opérandes et retourne une valeur numérique. Les opérandes et l'opérateur constituent l'expression arithmétique :

```js
2 + 3;

2 * 3;

2 ** 3;
```

### Expressions de chaîne

Lorsque les chaînes sont concaténées, elles forment des expressions de chaîne :

```js
console.log('Mon nom est' + 'Peter');
```

### Expressions logiques

Les expressions logiques sont des expressions dans lesquelles diverses valeurs sont comparées :

```js
10 > 2;
2 < 10;
c === 2 || d === 10;
```

### Expressions du côté gauche

Les expressions du côté gauche sont des expressions où des valeurs sont assignées à une variable :

```js
// variables
a = 2;

// propriétés d'objet
obj = {};
obj.name = 'Paul';
```

## Types de données

Il existe 8 types de données en JavaScript : String, Number, Boolean, Object, Null, Undefined, Symbol et BigInt.

### String

Le type string représente des données textuelles. Une chaîne est entourée d'une apostrophe ou d'une guillemet.

Chaque élément d'une chaîne occupe une certaine position dans la chaîne. Le premier élément est à l'index 0, et le deuxième et le troisième sont aux index 1 et 2 respectivement.

Voici un exemple de chaîne :

```js
let name = 'Yusuf';
let newName = "Joseph";
```

### Number

Les types de nombres sont stockés en format 64 bits, également connus sous le nom de nombres à virgule flottante en double précision.

Ils consistent en des nombres qui sont dans la plage de -(2<sup>53</sup> - 1) et (2<sup>53</sup> - 1), ces deux nombres étant inclus. Ces deux nombres sont connus sous le nom de `MIN_SAFE_INTEGER` et `MAX_SAFE_INTEGER` respectivement.

Les nombres qui dépassent cette plage appartiennent à un autre type de données appelé BigInt.

Voici un exemple d'entier positif, d'un flottant et d'un entier négatif :

```js
let number = 15;
let anotherNumber = 1.5;
let lastNumber = -3;
```

### Boolean

Le type booléen est logique et n'a que deux valeurs : vrai ou faux. Il est couramment utilisé dans les boucles et les instructions conditionnelles.

Dans l'exemple ci-dessous, j'ai déclaré des variables et leur ai assigné une valeur de vrai et faux respectivement.

Ensuite, j'ai créé une instruction conditionnelle qui retourne 1 si la variable `bool` est vraie ou -1 si elle est fausse. Elle retourne zéro si elle n'est ni vraie ni fausse.

```js
let positive = true;
let negative = false;
let bool = false;

// instruction conditionnelle
if (bool) {
    return 1;
} else if (bool) {
    return -1;
} else {
    return 0;
}
```

### Object

Un type d'objet vous permet de stocker des collections de données. Les données sont stockées dans une paire d'accolades et un format de paire clé-valeur. Les clés d'objet doivent être textuelles (par exemple une chaîne).

Un objet peut stocker n'importe quel autre type de données, comme une chaîne, un nombre, des tableaux, des booléens, etc.

Dans l'exemple ci-dessous, j'ai créé un objet nommé `myObject`, et lui ai donné trois clés avec leurs valeurs correspondantes :

```js
let myObject = {
    name: "Gabriel",
    number: 15,
    developer: [true, "Daniel", 1]
}
```

### Null

Les types de données Null sont des types de données spéciaux. Ils ont la valeur null, ce qui signifie que la valeur est inconnue ou vide :

```js
let unknown = null;
```

### Undefined

Contrairement à null, undefined signifie qu'une variable est déclarée et non assignée à une valeur. Une variable peut également être assignée à undefined spécifiquement :

```js
let name = undefined;

let newName;
console.log(newName);
```

### Symbol

Les symboles sont utilisés pour créer des valeurs uniques. Ils sont créés en appelant la fonction `Symbol()`. Chaque fois que la fonction `Symbol()` est invoquée, elle crée une nouvelle valeur unique.

Les symboles sont gardés cachés ou privés et ne peuvent être utilisés qu'en interne. Par exemple, ils peuvent être utilisés comme clés dans un objet. Lorsque vous essayez d'obtenir la liste des clés dans un objet où un symbole fait partie de ses clés, la clé de symbole ne sera pas affichée.

Vous pouvez passer un paramètre à la fonction symbole pour servir de description pour le symbole lors de son débogage dans la console :

```js
let firstSymbol = Symbol();

let anotherSymbol = Symbol(anotherSymbol);
```

### BigInt

BigInt est un type spécial de nombre qui fournit un support pour des nombres avec une longueur qu'un type de nombre normal ne peut pas contenir (comme des nombres qui dépassent la limite d'entier sûr).

Il peut être créé en ajoutant n à la fin d'un entier ou en passant un nombre dans la fonction `BigInt` :

```js
let bigNumber = 175337823472347884278247898427427427642n;
let newBigNumber = BigInt(1624743724724724898718247248744774227422n);

let anotherBigNumber = BigInt(14);
```

## Classes

Une classe JavaScript est un modèle pour créer des objets. Elle contient des données et des fonctions qui manipulent les données.

Les classes ont été introduites dans JavaScript dans la version ECMAScript 2015 (ES6) de JavaScript.

Les fonctions utilisées dans les classes sont appelées méthodes.

Il existe une syntaxe de base pour déclarer des classes qui ressemble à ceci :

```js
class TemplateClass {
    constructor() {...};
    method() {...};
    method() {...};
}
```

À partir de la syntaxe, vous pouvez créer une classe nommée `Visitor` :

```js
class Visitor {
    constructor(name) {
        this.name = name;
    }
    introduce() {
        console.log(`Mon nom est ${this.name} et je suis un visiteur`)
    }
}
```

Vous pouvez créer une nouvelle classe à partir de cette classe en utilisant la syntaxe de nouvelle classe. La classe nouvellement créée peut accéder à toute méthode de sa classe parente :

```js
let visitor = new Visitor("Jeff");

// visitor peut appeler la méthode introduce dans sa classe parente.
visitor.introduce();
```

## Variables

Une variable est un stockage nommé pour les données JavaScript. Les variables JavaScript peuvent être déclarées de trois manières :

* En utilisant le mot-clé `var`

* En utilisant le mot-clé `let`

* En utilisant le mot-clé `const`

### Comment déclarer des variables en utilisant le mot-clé `var`

Les variables déclarées avec le mot-clé `var` sont fonctionnelles et peuvent être redéclarées :

```js
var num = 1;

// num peut être redéclarée
var num = 2;
```

### Comment déclarer des variables en utilisant le mot-clé `let`

Les variables déclarées avec le mot-clé `let` sont bloquées et ne peuvent pas être redéclarées - elles ne peuvent être réassignées :

```js
let fruit = "banana";

// fruit ne peut être réassignée
fruit = "orange";
```

### Comment déclarer des variables en utilisant le mot-clé `const`

Les variables déclarées avec le mot-clé const sont bloquées et ne peuvent pas être redéclarées ou réassignées (ce qui signifie qu'elles sont constantes) :

```js
const bestStudent = "Daniel";
```

## Fonctions

Une fonction est un bloc de code qui effectue une tâche spécifique. Elle peut être déclarée en utilisant le mot-clé `function` :

```js
function doSomething() {
    return "Fait quelque chose";
}
```

Une fonction prend des entrées appelées arguments et produit des résultats.

Pour exécuter une fonction, vous invoquerez la fonction en appelant le nom de la fonction avec des parenthèses :

```js
function addNumbers(a, b) {
    return a + b;
}

addNumbers();
```

Vous pouvez assigner une fonction à une variable et appeler la variable lorsque vous voulez invoquer la fonction :

```js
function addNumbers(a, b) {
    return a + b;
}

let numberAddition = addNumbers(2, 3)
numberAddition();
```

## Fonctions fléchées

Les fonctions fléchées sont une manière concise et compacte d'écrire une fonction. Elles ont certaines limitations délibérées dans leur utilisation :

* Elles ne peuvent pas être utilisées comme méthode.

* Elles ne peuvent pas être utilisées comme constructeur.

* Les fonctions fléchées ne peuvent pas utiliser yield dans leur propre corps.

Voici la syntaxe pour une fonction fléchée :

```js
const doSomething = () => {
    return "Faire quelque chose";
}
```

Une fonction fléchée peut également prendre un argument.

```js
const multiplyNumbers = (a, b) => {
    return a * b;
}
```

## Mot-clé `this`

Le mot-clé `this` en JavaScript fait référence à un objet qui exécute une fonction ou un code.

Le mot-clé `this` peut être utilisé dans différents contextes - le contexte dans lequel le mot-clé `this` est utilisé détermine à quoi il fait référence.

Le mot-clé `this` peut être utilisé :

* Dans une méthode d'objet.

* Seul.

* Dans les liaisons de méthodes d'objet.

### Comment utiliser le mot-clé `this` dans une méthode d'objet

Le mot-clé `this` fait référence à l'objet chaque fois qu'il est utilisé comme méthode d'objet :

```js
intro : function() {
    return "Mon nom est" + this.name "et, je suis un" + this.occupation;
}
```

### Comment utiliser le mot-clé `this` seul

Lorsque `this` est utilisé seul, il fait référence à l'objet global :

```js
let wes = this;
```

### Comment utiliser le mot-clé `this` dans les liaisons de méthodes d'objet

Lorsque `this` est utilisé dans une méthode d'objet, il fait référence à l'objet :

```js
let student = {
  firstName  : "Juliana",
  lastName   : "Carpe",
  myFunction : function() {
    return this;
  }
};
```

## Boucles

Les boucles sont utiles pour exécuter un bloc de code un certain nombre de fois en fonction de certaines conditions spécifiées. Il existe différents types de boucles en JavaScript :

* Boucles `for`

* Boucles `for ... in`

* Boucles `for ... of`

* Boucles `while`

* Boucles `do ... while`

### Comment utiliser les boucles `for`

Les boucles `for` sont utilisées pour exécuter un bloc de code un certain nombre de fois :

```js
for (let i = 0; i < 5; i++) {
    return i;
}
```

### Comment utiliser les boucles `for ... in`

Les boucles `for ... in` sont utilisées pour parcourir les propriétés d'un objet :

```js
for (let prop in obj) {
    return obj.prop;
}
```

### Comment utiliser les boucles `for ... of`

Les boucles `for ... of` sont utilisées pour parcourir les valeurs des objets itérables comme les tableaux, les chaînes, les maps, etc. :

```js
let numArr = [2, 4, 6, 8]
for (let val of numArr) {
    return val ** 2
}
```

### Comment utiliser les boucles `while`

Les boucles `while` sont utilisées pour exécuter un bloc de code tant qu'une certaine condition reste vraie :

```js
while (i < 20) {
    return i;
    i++;
}
```

### Comment utiliser les boucles `do ... while`

Les boucles `do ... while` exécutent d'abord un bloc de code sans aucune condition. Tant qu'une certaine condition reste vraie, elle continue à exécuter le bloc de code :

```js
let i = 3;
do {
    return i;
    i++;
} 
while (i < 4)
```

## Portées

La portée est le contexte actuel d'exécution. C'est là que les variables et les expressions peuvent être accessibles.

Il existe un arrangement hiérarchique de la portée en JavaScript. Cela permet aux portées inférieures d'accéder aux portées supérieures.

Les portées en JavaScript sont :

* Portée globale

* Portée de module

* Portée de fonction

* Portée de bloc

La portée globale est la portée par défaut pour tous les codes exécutés en mode script, tandis que la portée de module est la portée par défaut pour tous les codes exécutés en mode module.

La portée de fonction est créée par les fonctions, tandis que la portée de bloc est créée par les variables.

Voici un exemple de portée de fonction et de portée de bloc :

```js
// portée de fonction
function introduce(name) {
    let age = 12;
    console.log(`Mon nom est ${name}`);
    console.log(`J'ai ${age} ans`);
}

let firstAge = 13

// portée de bloc
if (firstAge === 13) {
    let secondAge = 20;
    console.log(`J'ai ${secondAge} ans`);
}
```

## Tableaux

Un tableau est un type spécial d'objet qui stocke des données sous une forme ordonnée.

Les tableaux peuvent être déclarés de deux manières :

* En utilisant des crochets.

* En utilisant le constructeur `Array()`.

### Comment déclarer des tableaux en utilisant des crochets

C'est la manière courante de créer un tableau. Cela se fait en enveloppant les éléments du tableau dans une paire de crochets :

```js
  let array = [1, 3, "a", "c"];
```

### Comment déclarer des tableaux en utilisant le constructeur `Array()`

Le constructeur `Array()` fait la même chose que la notation entre crochets. Il peut être appelé avec ou sans le mot-clé `new` :

```js
  let anotherArray = Array(1, 2, 3, "go");
```

### Comment accéder aux éléments de tableau

Les éléments de tableau peuvent être accessibles de trois manières :

* en utilisant leur index.

* en utilisant la propriété `length` du tableau.

* en utilisant une boucle

#### Comment accéder à un élément de tableau en utilisant son index

Vous appelez le nom du tableau avec un crochet contenant l'index que vous souhaitez accéder :

```js
 let newArray = ["Idris", "Daniel", "Joseph"];

  // Pour accéder au premier élément
  let firstElement = newArray[0]; 
  console.log(firstElement);  // Idris

  // Pour accéder au deuxième élément 
  let secondElement = newArray[1];  
  console.log(secondElement);  // Joseph
```

### Comment accéder à un élément de tableau en utilisant la propriété `length` du tableau

Vous pouvez obtenir la longueur du tableau en utilisant la propriété `length`. Ensuite, vous soustrayez un nombre pour obtenir l'index de l'élément que vous souhaitez accéder :

```javascript
let newArray = ["Idris", "Daniel", "Joseph"];

  let length = newArray.length;

  let firstElement = newArray[length - 3]; 
  console.log(firstElement);  // Idris

  let secondElement = newArray[length - 2];
  console.log(secondElement);  // Joseph
```

#### Comment accéder à un élément de tableau en utilisant une boucle

Les éléments de tableau peuvent être accessibles en utilisant des boucles. Vous pouvez utiliser une boucle `for`, une boucle `while` ou une boucle `for ... of` :

```js
  let newArray = ["Idris", "Daniel", "Joseph"];
  for (let i = 0; i < newArray.length; i++) {
      return newArray[i]
  }
```

### Méthodes importantes de tableau

Il existe plus de quinze méthodes de tableau en JavaScript. Dans cet article, vous apprendrez celles qui sont les plus utiles dans Node.js :

* `push()` et `pop()`

* `shift()` et `unshift()`

* `map()`

* `sort()`

* `forEach()`

#### Comment utiliser les méthodes `push()` et `pop()`

La méthode `push()` est utilisée pour ajouter un élément à la fin d'un tableau, tandis que la méthode `pop()` est utilisée pour supprimer un élément de la fin d'un tableau :

```js
let arr = [1, 2, 3, 9]

arr.push(21);

console.log(arr)    // [1, 2, 3, 9, 21]

arr.pop()

console.log(arr)    // [1, 2, 3, 9]
```

#### Comment utiliser les méthodes `unshift()` et `shift()`

La méthode `unshift()` est utilisée pour ajouter un élément au début d'un tableau, tandis que la méthode `shift()` est utilisée pour supprimer un élément du début d'un tableau :

```js
let arr = [1, 2, 3];

arr.unshift(0);

console.log(arr);	// [0, 1, 2, 3]

arr.shift();

connsole.log(arr);	// [1, 2, 3]
```

#### Comment utiliser la méthode `map()`

La méthode `map()` parcourt les éléments d'un tableau et appelle une fonction sur chaque élément du tableau. Elle retourne un nouveau tableau qui contient le résultat de chaque appel de fonction :

```javascript
let fruits = ["Apple", "Grape", "Cashew"];

let mappedFruits = fruits.map(item => item + "s");
console.log(mappedFruits); // ["Apples", "Grapes", "Cashews"]
```

#### Comment utiliser la méthode `sort()`

La méthode `sort()` trie un tableau en place et retourne le même tableau sous une forme triée.

L'ordre par défaut de la méthode `sort()` est l'ordre croissant. Les chaînes sont triées par ordre alphabétique :

```javascript
let numbers = [8, 7, 5];
let fruits = ["Apple", "Grape", "Cashew"];

let sortedNumbers = numbers.sort();
let sortedFruits = fruits.sort()

console.log(sortedNumbers);  // [5, 7, 8]
console.log(sortedFruits);  // ["Apple", "Cashew", "Grape"]
```

#### Comment utiliser la méthode forEach()

La méthode `forEach()` parcourt le tableau et appelle une fonction pour chaque élément du tableau :

```javascript
let fruits = ["Apple", "Grape", "Cashew"];

fruits.forEach(fruit => console.log(fruit));
//  "Apple"
//  "Grape"
//  "Cashew"
```

## Littéraux de gabarit

Les littéraux de gabarit sont enfermés dans des backticks, tout comme les chaînes sont enfermées dans des guillemets. Ils vous permettent de stocker des chaînes multilignes et également d'interpoler des chaînes avec des expressions intégrées.

L'exemple ci-dessous montre un littéral de gabarit de base :

```js
let basic = `J'écris des codes`
```

Vous pouvez écrire un littéral de gabarit qui stocke des chaînes multilignes comme ceci :

```js
let multiLine = `J'écris des codes                     
		Je débogue des codes`;
```

Vous pouvez utiliser le signe dollar et les accolades pour intégrer des expressions dans les littéraux de gabarit.

Dans l'exemple ci-dessous, la fonction `myName` est intégrée dans la variable display avec un littéral de gabarit :

```js
function myName(Musab, Habeeb) {        
    alert("Musab Habeeb");    
}    

let display = `Cela affiche mon nom ${myName()}`
```

## Mode strict

JavaScript est un langage négligé dans le sens où il vous permet d'écrire du code qui n'est pas autorisé dans d'autres langages. Certains du code que vous écrivez en JavaScript contient des erreurs, mais JavaScript ne génère pas d'erreur.

Le mode strict fait ce qui suit :

* Il génère des erreurs pour les erreurs silencieuses de JavaScript.

* Il corrige les erreurs qui rendent difficile pour les moteurs JavaScript d'effectuer des optimisations.

* Il interdit certaines syntaxes susceptibles d'être définies dans les futures versions de l'ECMAScript.

Le mode strict fonctionne dans un fichier de script entier et des fonctions, mais il ne fonctionne pas dans les portées de bloc.

Pour invoquer le mode script, vous ajouterez la syntaxe `"use strict";` en haut du code auquel vous souhaitez l'appliquer. Vous pouvez appliquer le mode strict à un script comme ceci :

```js
"use strict";

let name = "Musab";

console.log(name);
```

De plus, vous pouvez appliquer le mode strict à une fonction comme ceci :

```js
function sayHi(name) {
    "use strict";
    console.log(`Salut ${name}`);
}
```

## Conclusion

Enfin, vous avez terminé l'apprentissage des concepts JavaScript que vous devez comprendre avant d'apprendre Node.js.

Tous ces concepts sont des concepts importants qu'un développeur JavaScript aspirant à apprendre Node.js devrait comprendre. Comprendre ces concepts rendra l'apprentissage de Node.js plus facile.

Mais, pour comprendre ces concepts en profondeur, vous pouvez faire plus de recherches sur chacun d'eux et lire d'autres articles. Continuez à apprendre, continuez à construire.