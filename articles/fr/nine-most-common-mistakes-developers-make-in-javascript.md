---
title: Les neuf erreurs les plus courantes que les développeurs commettent en JavaScript
  (et comment les corriger)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-25T17:37:21.000Z'
originalURL: https://freecodecamp.org/news/nine-most-common-mistakes-developers-make-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a0e740569d1a4ca2335.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: 'self-improvement '
  slug: self-improvement
seo_title: Les neuf erreurs les plus courantes que les développeurs commettent en
  JavaScript (et comment les corriger)
seo_desc: 'By Dipto Karmakar

  JavaScript is a scripting language used in webpages to add functionality and interactivity.
  For a beginner coming from a different programming language, JavaScript is quite
  easy to understand. With a few tutorials, you should be abl...'
---

Par Dipto Karmakar

JavaScript est un [langage de script](https://en.wikipedia.org/wiki/Scripting_language) utilisé dans les pages web pour ajouter des fonctionnalités et de l'interactivité. Pour un débutant venant d'un autre langage de programmation, JavaScript est assez facile à comprendre. Avec quelques tutoriels, vous devriez pouvoir commencer à l'utiliser tout de suite.

Cependant, il y a quelques erreurs courantes que de nombreux programmeurs débutants commettent. Dans cet article, nous aborderons neuf erreurs courantes (ou mauvaises pratiques) et leurs solutions pour vous aider à devenir un meilleur développeur JS.

## Confondre les opérateurs d'assignation (=) et d'égalité (==, ===)

Comme son nom l'indique, l'[opérateur d'assignation](https://www.w3resource.com/javascript/operators/assignment-operator.php#:~:text=Assignment%20Operators,value%20of%20its%20right%20operand.&text=That%20is%2C%20a%20%3D%20b%20assigns,shown%20in%20the%20following%20table.) (=) est utilisé pour assigner des valeurs aux variables. Les développeurs le confondent souvent avec l'opérateur d'égalité.

Voici un exemple :

```javascript
const name = "javascript";
if ((name = "nodejs")) {
    console.log(name);
}
// sortie - nodejs
```

Dans ce cas, la variable name et la chaîne 'nodejs' ne sont pas comparées. Au lieu de cela, 'nodejs' est assigné à name et 'nodejs' est affiché dans la console.

En JavaScript, le double signe égal (==) et le triple signe égal (===) sont appelés opérateurs de comparaison.

Pour le code ci-dessus, voici la manière appropriée de comparer les valeurs :

```javascript
const name = "javascript";
if (name == "nodejs") {
    console.log(name);
}
// aucune sortie
// OU
if (name === "nodejs") {
    console.log(name);
}
// aucune sortie
```

La différence entre ces opérateurs de comparaison est que le double égal effectue une comparaison **lâche** tandis que le triple égal effectue une comparaison **stricte**.

Dans une comparaison lâche, seules les valeurs sont comparées. Mais dans une comparaison stricte, les valeurs et le type de données sont comparés.

Le code suivant l'explique mieux :

```javascript
const number = "1";
console.log(number == 1);
// vrai
console.log(number === 1);
// faux
```

La variable number a été assignée avec une valeur de chaîne de 1. Lorsqu'elle est comparée avec 1 (de type nombre) en utilisant le double égal, elle retourne vrai car les deux valeurs sont 1.

Mais lorsqu'elle est comparée en utilisant le triple égal, elle retourne faux car chaque valeur a un type de données différent.

## S'attendre à ce que les callbacks soient synchrones

Les callbacks sont l'une des façons dont JavaScript gère les opérations asynchrones. Cependant, les promesses et async/await sont des méthodes préférables pour gérer les opérations asynchrones car plusieurs callbacks conduisent à [l'enfer des callbacks](http://callbackhell.com/).

Les callbacks ne sont pas **synchrones**. Ils sont utilisés comme une fonction à appeler après une opération lorsque l'exécution différée est terminée.

Un exemple est la fonction globale `setTimeout` qui reçoit une fonction de callback comme premier argument et une durée (en ms) comme deuxième argument comme suit :

```javascript
function callback() {
    console.log("Je suis le premier");
}
setTimeout(callback, 300);
console.log("Je suis le dernier");
// sortie
// Je suis le dernier
// Je suis le premier
```

Après 300 millisecondes, la fonction de callback est appelée. Mais avant qu'elle ne se termine, le reste du code s'exécute. C'est la raison pour laquelle le dernier console.log a été exécuté en premier.

Une erreur courante que commettent les développeurs est de mal interpréter les callbacks comme synchrones. Par exemple, un callback qui retourne une valeur qui serait utilisée pour d'autres opérations.

Voici cette erreur :

```javascript
function addTwoNumbers() {
    let firstNumber = 5;
    let secondNumber;
    setTimeout(function () {
        secondNumber = 10;
    }, 200);
    console.log(firstNumber + secondNumber);
}
addTwoNumbers();
// NaN
```

`NaN` est la sortie car `secondNumber` est indéfini. Au moment de l'exécution de `firstNumber + secondNumber`, `secondNumber` est toujours indéfini car la fonction `setTimeout` exécuterait le callback après `200ms`.

La meilleure façon d'aborder cela est d'exécuter le reste du code dans la fonction de callback :

```javascript
function addTwoNumbers() {
    let firstNumber = 5;
    let secondNumber;
    setTimeout(function () {
        secondNumber = 10;
        console.log(firstNumber + secondNumber);
    }, 200);
}
addTwoNumbers();
// 15
```

## Mauvaise référence à `this`

`this` est un concept [souvent mal compris](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) en JavaScript. Pour utiliser `this` en JavaScript, vous devez vraiment comprendre comment il fonctionne car il opère un peu différemment par rapport à d'autres langages.

Voici un exemple d'une erreur courante lors de l'utilisation de `this` :

```javascript
const obj = {
    name: "JavaScript",
    printName: function () {
        console.log(this.name);
    },
    printNameIn2Secs: function () {
        setTimeout(function () {
            console.log(this.name);
        }, 2000);
    },
};
obj.printName();
// JavaScript
obj.printNameIn2Secs();
// undefined
```

Le premier résultat est **`JavaScript`** car `this.name` pointe correctement vers la propriété name de l'objet. Le deuxième résultat est `**undefined**` car `this` a perdu la référence aux propriétés de l'objet (y compris name).

Cela est dû au fait que `this` dépend de l'objet appelant la fonction dans laquelle il se trouve. Il y a une variable `this` dans chaque fonction mais l'objet auquel elle pointe est déterminé par l'objet qui l'appelle.

Le `this` dans `obj.printName()` pointe directement vers `obj`. Le `this` dans `obj.printNameIn2Secs` pointe directement vers `obj`. Mais le `this` dans la fonction de callback de `setTimeout` ne pointe vers aucun objet car aucun objet ne l'a appelé.

Pour qu'un objet ait appelé `setTimeout`, quelque chose comme `obj.setTimeout...` serait exécuté. Puisqu'il n'y a pas d'objet appelant cette fonction, l'objet par défaut (qui est `window`) est utilisé.

`name` n'existe pas sur window, ce qui entraîne `undefined`.

Les meilleures façons de conserver la référence à `this` dans `setTimeout` sont d'utiliser `bind`, `call`, `apply` ou les fonctions fléchées (introduites dans ES6). Contrairement aux fonctions normales, les fonctions fléchées ne créent pas leur propre `this`.

Donc, ce qui suit conservera sa référence à `this` :

```javascript
const obj = {
    name: "JavaScript",
    printName: function () {
        console.log(this.name);
    },
    printNameIn2Secs: function () {
        setTimeout(() => {
            console.log(this.name);
        }, 2000);
    },
};
obj.printName();
// JavaScript
obj.printNameIn2Secs();
// JavaScript
```

## Négliger la mutabilité des objets

Contrairement aux types de données primitifs comme les chaînes de caractères, les nombres, etc., en JavaScript, les objets sont des types de données de référence. Par exemple, dans les objets clé-valeur :

```javascript
const obj1 = {
    name: "JavaScript",
};
const obj2 = obj1;
obj2.name = "programming";
console.log(obj1.name);
// programming
```

`obj1` et `obj2` possèdent la même référence vers l'emplacement en mémoire où l'objet est stocké.

Dans les tableaux :

```javascript
const arr1 = [2, 3, 4];
const arr2 = arr1;
arr2[0] = "javascript";
console.log(arr1);
// ['javascript', 3, 4]
```

Une erreur courante que commettent les développeurs est de négliger cette nature de JavaScript, ce qui entraîne des erreurs inattendues. Par exemple, si 5 objets ont la même référence vers le même objet, l'un des objets peut interférer avec les propriétés dans une base de code à grande échelle.

Lorsque cela se produit, toute tentative d'accès aux propriétés originales retournerait undefined ou pourrait lancer une erreur.

La meilleure pratique pour cela est de toujours créer de nouvelles références pour de nouveaux objets lorsque vous souhaitez dupliquer un objet. Pour ce faire, l'opérateur rest (`...` introduit dans ES6) est une solution parfaite.

Par exemple, dans les objets clé-valeur :

```javascript
const obj1 = {
    name: "JavaScript",
};
const obj2 = { ...obj1 };
console.log(obj2);
// {name: 'JavaScript' }
obj2.name = "programming";
console.log(obj.name);
// 'JavaScript'
```

Dans les tableaux :

```javascript
const arr1 = [2, 3, 4];
const arr2 = [...arr1];
console.log(arr2);
// [2,3,4]
arr2[0] = "javascript";
console.log(arr1);
// [2, 3, 4]
```

## Enregistrer des tableaux et des objets dans le stockage du navigateur

Parfois, lors de l'utilisation de JavaScript, les développeurs peuvent vouloir tirer parti du `localStorage` pour enregistrer des valeurs. Mais une erreur courante est d'essayer d'enregistrer des [tableaux et des objets](https://www.tutorialspoint.com/javascript/javascript_arrays_object.htm) tels quels dans le `localStorage`. `localStorage` n'accepte que les chaînes de caractères.

En tentant d'enregistrer des objets, JavaScript convertit l'objet en une chaîne de caractères. Le résultat est `[Object Object]` pour les objets et une chaîne séparée par des virgules pour les éléments de tableau.

Par exemple :

```javascript
const obj = { name: "JavaScript" };
window.localStorage.setItem("test-object", obj);
console.log(window.localStorage.getItem("test-object"));
// [Object Object]
const arr = ["JavaScript", "programming", 45];
window.localStorage.setItem("test-array", arr);
console.log(window.localStorage.getItem("test-array"));
// JavaScript, programming, 45
```

Lorsque les objets sont enregistrés de cette manière, il devient difficile d'y accéder. Par exemple, accéder à l'objet comme `.name` entraînerait une erreur. Cela est dû au fait que `[Object Object]` est maintenant une chaîne de caractères, sans propriété `name`.

Une meilleure façon d'enregistrer des objets et des tableaux dans le stockage local est d'utiliser `JSON.stringify` (pour convertir les objets en chaînes de caractères) et `JSON.parse` (pour convertir les chaînes de caractères en objets). De cette manière, l'accès aux objets devient facile.

La version correcte du code ci-dessus serait :

```javascript
const obj = { name: "JavaScript" };
window.localStorage.setItem("test-object", JSON.stringify(obj));
const objInStorage = window.localStorage.getItem("test-object");
console.log(JSON.parse(objInStorage));
// {name: 'JavaScript'}
const arr = ["JavaScript", "programming", 45];
window.localStorage.setItem("test-array", JSON.stringify(arr));
const arrInStorage = window.localStorage.getItem("test-array");
console.log(JSON.parse(arrInStorage));
// JavaScript, programming, 45
```

## Ne pas utiliser les valeurs par défaut

Définir des [valeurs par défaut](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters) dans les variables dynamiques est une très bonne pratique pour prévenir les erreurs inattendues. Voici un exemple d'une erreur courante :

```javascript
function addTwoNumbers(a, b) {
    console.log(a + b);
}
addTwoNumbers();
// NaN
```

Le résultat est `NaN` car `a` est `undefined` et `b` est `undefined`. En utilisant des valeurs par défaut, des erreurs comme celle-ci peuvent être évitées. Par exemple :

```javascript
function addTwoNumbers(a, b) {
    if (!a) a = 0;
    if (!b) b = 0;
    console.log(a + b);
}
addTwoNumbers();
// 0
```

Alternativement, la fonction de valeur par défaut introduite dans ES6 peut être utilisée comme suit :

```javascript
function addTwoNumbers(a = 0, b = 0) {
    console.log(a + b);
}
addTwoNumbers();
// 0
```

Cet exemple, bien que minimal, souligne l'importance des valeurs par défaut. De plus, les développeurs peuvent fournir des erreurs ou des messages d'avertissement lorsque les valeurs attendues ne sont pas fournies.

## Nom incorrect des variables

Oui, les développeurs commettent encore cette erreur. Nommer est difficile, mais les développeurs n'ont vraiment pas le choix. Les commentaires sont une bonne pratique en programmation, et il en va de même pour le nommage des [variables](https://en.wikipedia.org/wiki/Variable_(computer_science)).

Par exemple :

```javascript
function total(discount, p) {
    return p * discount
}
```

La variable `discount` est correcte, mais qu'en est-il de `p` ou `total` ? Total de quoi ? Une meilleure pratique pour ce qui précède serait :

```javascript
function totalPrice(discount, price) {
    return discount * price
}
```

Nommer correctement les variables est important car un développeur peut ne jamais être le seul développeur sur une base de code à un moment donné ou dans le futur.

Nommer correctement les variables permettra aux contributeurs de comprendre facilement comment un projet fonctionne.

## Vérification des valeurs booléennes

```javascript
const isRaining = false
if(isRaining) {
    console.log('Il pleut')
} else {
    console.log('Il ne pleut pas')
}
// Il ne pleut pas
```

Il est courant de vérifier les [valeurs booléennes](https://www.w3schools.com/js/js_booleans.asp) comme le montre le code ci-dessus. Bien que cela soit acceptable, des erreurs se produisent lors du test de certaines valeurs.

En JavaScript, une comparaison lâche de `0` et `false` retourne `true` et `1` et `true` retourne `true`. Cela signifie que si `isRaining` était `1`, `isRaining` serait `true`.

C'est aussi une erreur souvent commise dans les objets. Par exemple :

```javascript
const obj = {
    name: 'JavaScript',
    number: 0
}
if(obj.number) {
    console.log('la propriété number existe')
} else {
    console.log('la propriété number n'existe pas')
}
// la propriété number n'existe pas
```

Bien que la propriété `number` existe, `obj.number` retourne `0`, qui est une valeur `falsy`, donc le bloc `else` est exécuté.

À moins d'être sûr de la plage de valeurs qui serait utilisée, les valeurs booléennes et les propriétés dans les objets doivent être testées comme ceci :

```javascript
if(a === false)...
if(object.hasOwnProperty(property))...
```

## Confondre l'addition et la concaténation

Le signe plus `(+)` a deux fonctions en JavaScript : l'addition et la concaténation. L'addition est pour les nombres et la concaténation est pour les chaînes de caractères. Certains développeurs utilisent souvent incorrectement cet opérateur.

Par exemple :

```javascript
const num1 = 30;
const num2 = "20";
const num3 = 30;
const word1 = "Java"
const word2 = "Script"
console.log(num1 + num2);
// 3020
console.log(num1 + num3);
// 60
console.log(word1 + word2);
// JavaScript
```

Lors de l'addition de chaînes de caractères et de nombres, JavaScript convertit les nombres en chaînes de caractères et concatène toutes les valeurs. Pour l'addition de nombres, une opération mathématique est effectuée.

## Conclusion

Il existe, bien sûr, plus d'erreurs (certaines triviales, d'autres sérieuses) que celles listées ci-dessus. Alors assurez-vous simplement de rester à jour avec les développements du langage.

Étudier et éviter ces erreurs vous aidera à construire de meilleures applications web et outils plus fiables.