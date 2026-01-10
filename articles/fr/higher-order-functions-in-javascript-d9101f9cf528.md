---
title: 'Fonctions d''ordre supérieur : Comment utiliser Filter, Map et Reduce pour
  un code plus maintenable'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-18T15:31:55.000Z'
originalURL: https://freecodecamp.org/news/higher-order-functions-in-javascript-d9101f9cf528
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1uudsYisszFlHUxPiMMpbw.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Fonctions d''ordre supérieur : Comment utiliser Filter, Map et Reduce
  pour un code plus maintenable'
seo_desc: 'By Guido Schmitz

  Higher order functions can help you to step up your JavaScript game by making your
  code more declarative. That is, short, simple, and readable.

  A Higher Order Function is any function that returns a function when executed, takes
  a fu...'
---

Par Guido Schmitz

Les fonctions d'ordre supérieur peuvent vous aider à améliorer votre maîtrise de JavaScript en rendant votre code plus déclaratif. C'est-à-dire, court, simple et lisible.

Une fonction d'ordre supérieur est une fonction qui retourne une fonction lorsqu'elle est exécutée, prend une fonction comme un ou plusieurs de ses arguments, ou les deux. Si vous avez utilisé l'une des méthodes de tableau comme `map` ou `filter`, ou passé une fonction de rappel à `$.get` de jQuery, vous avez déjà travaillé avec des fonctions d'ordre supérieur.

Lorsque vous utilisez `Array.map`, vous fournissez une fonction comme seul argument, qu'elle applique à chaque élément contenu dans le tableau.

```javascript
var arr = [ 1, 2, 3 ];

var arrDoubled = arr.map(function(num) {
  return num * 2;
});

console.log(arrDoubled); // [ 2, 4, 6 ]
```

Les fonctions d'ordre supérieur peuvent également retourner une fonction. Par exemple, vous pouvez créer une fonction appelée `multiplyBy` qui prend un nombre et retourne une fonction qui multiplie un autre nombre que vous fournissez par le premier nombre fourni. Vous pouvez utiliser cette approche pour créer une fonction `multiplyByTwo` à passer à `Array.map`. Cela vous donnera le même résultat que vous avez vu ci-dessus.

```javascript
function multiplyBy(num1) {
  return function(num2) {
    return num1 * num2;
  }
}

var multiplyByTwo = multiplyBy(2);

var arr = [ 1, 2, 3 ];

var arrDoubled = arr.map(multiplyByTwo);

console.log(arrDoubled); // [ 2, 4, 6 ]
```

Savoir quand et comment utiliser ces fonctions est essentiel. Elles rendent votre code plus facile à comprendre et à maintenir. Cela facilite également la combinaison des fonctions entre elles. Cela s'appelle la composition, et je n'entrerai pas dans les détails ici. Dans cet article, je vais couvrir les trois fonctions d'ordre supérieur les plus utilisées en JavaScript. Il s'agit de `.filter()`, `.map()` et `.reduce()`.

## Filtrer

Imaginez écrire un morceau de code qui accepte une liste de personnes où vous voulez filtrer les personnes qui sont égales ou au-dessus de l'âge de 18 ans.

Notre liste ressemble à celle ci-dessous :

```
const people = [ { name: 'John Doe', age: 16 }, { name: 'Thomas Calls', age: 19 }, { name: 'Liam Smith', age: 20 }, { name: 'Jessy Pinkman', age: 18 },];
```

Regardons un exemple de fonction de premier ordre qui sélectionne les personnes qui sont au-dessus de l'âge de 18 ans. J'utilise une [fonction fléchée](https://hacks.mozilla.org/2015/06/es6-in-depth-arrow-functions) qui fait partie de la norme ECMAScript ou ES6 en abrégé. C'est simplement une manière plus courte de définir une fonction et permet de sauter la saisie de function et return, ainsi que certaines parenthèses, accolades et un point-virgule.

```
const peopleAbove18 = (collection) => {  const results = [];   for (let i = 0; i < collection.length; i++) {    const person = collection[i];     if (person.age >= 18) {      results.push(person);    }  }
```

```
  return results;};
```

Maintenant, que se passe-t-il si nous voulons sélectionner toutes les personnes qui sont entre 18 et 20 ans ? Nous pourrions créer une autre fonction.

```
const peopleBetween18And20 = (collection) => {  const results = [];   for (let i = 0; i < collection.length; i++) {    const person = collection[i];     if (person.age >= 18 && person.age <= 20) {      results.push(person);    }  }
```

```
  return results;};
```

Vous reconnaissez peut-être déjà beaucoup de code répétitif ici. Cela pourrait être abstrait en une solution plus généralisée. Ces deux fonctions ont quelque chose en commun. Elles parcourent toutes deux une liste et la filtrent selon une condition donnée.

> « Une fonction d'ordre supérieur est une fonction qui prend une ou plusieurs fonctions comme arguments. »
> — [Closurebridge](https://clojurebridge.github.io/community-docs/docs/clojure/higher-order-function/)

Nous pouvons améliorer notre fonction précédente en utilisant une approche plus déclarative, `.filter()`.

```
const peopleAbove18 = (collection) => {  return collection    .filter((person) => person.age >= 18);}
```

C'est tout ! Nous pouvons réduire beaucoup de code supplémentaire en utilisant cette fonction d'ordre supérieur. Cela rend également notre code plus lisible. Nous ne nous soucions pas de la manière dont les choses sont filtrées, nous voulons simplement qu'elles soient filtrées. Je parlerai de la combinaison des fonctions plus tard dans cet article.

## Map

Prenons la même liste de personnes et un tableau de noms qui indique si la personne aime boire du café.

```
const coffeeLovers = ['John Doe', 'Liam Smith', 'Jessy Pinkman'];
```

La manière impérative serait comme suit :

```
const addCoffeeLoverValue = (collection) => {  const results = [];   for (let i = 0; i < collection.length; i++) {    const person = collection[i];
```

```
    if (coffeeLovers.includes(person.name)) {      person.coffeeLover = true;    } else {      person.coffeeLover = false;    }     results.push(person);  }   return results;};
```

Nous pourrions utiliser `.map()` pour rendre cela plus déclaratif.

```
const incrementAge = (collection) => {  return collection.map((person) => {    person.coffeeLover = coffeeLovers.includes(person.name);     return person;  });};
```

Encore une fois, `.map()` est une fonction d'ordre supérieur. Elle permet à une fonction d'être passée comme argument.

## Reduce

Je parie que vous allez aimer cette fonction lorsque vous saurez quand et comment l'utiliser. 
Le côté intéressant de `.reduce()` est que la plupart des fonctions ci-dessus peuvent être réalisées avec elle.

Prenons d'abord un exemple simple. Nous voulons additionner tous les âges des personnes. Encore une fois, nous allons voir comment cela peut être fait en utilisant l'approche impérative. Il s'agit essentiellement de parcourir la collection et d'incrémenter une variable avec l'âge.

```
const sumAge = (collection) => {  let num = 0;   collection.forEach((person) => {    num += person.age;  });   return num;}
```

Et l'approche déclarative utilisant `.reduce()`.

```
const sumAge = (collection) => collection.reduce((sum, person) => { return sum + person.age;}, 0);
```

Nous pouvons même utiliser `.reduce()` pour créer notre propre implémentation de `.map()` et `.filter()`.

```
const map = (collection, fn) => {  return collection.reduce((acc, item) => {    return acc.concat(fn(item));  }, []);}
```

```
const filter = (collection, fn) => {  return collection.reduce((acc, item) => {    if (fn(item)) {      return acc.concat(item);    }     return acc;  }, []);}
```

Cela peut être difficile à comprendre au début. Mais ce que `.reduce()` fait essentiellement, c'est commencer avec une collection et une variable avec une valeur initiale. Vous parcourez ensuite la collection et ajoutez les valeurs à la variable.

## Combiner map, filter et reduce

Super, que ces fonctions existent. Mais le bon côté, c'est qu'elles existent sur le prototype de Array en JavaScript. Cela signifie que ces fonctions peuvent être utilisées ensemble ! Cela facilite la création de fonctions réutilisables et réduit la quantité de code nécessaire pour écrire certaines fonctionnalités.

Nous avons donc parlé de l'utilisation de `.filter()` pour filtrer les personnes qui sont égales ou en dessous de l'âge de 18 ans. `.map()` pour ajouter la propriété `coffeeLover`, et `.reduce()` pour enfin créer une somme de l'âge de tout le monde combiné. 
Écrivons du code qui combine réellement ces trois étapes.

```
const people = [ { name: 'John Doe', age: 16 }, { name: 'Thomas Calls', age: 19 }, { name: 'Liam Smith', age: 20 }, { name: 'Jessy Pinkman', age: 18 },];
```

```
const coffeeLovers = ['John Doe', 'Liam Smith', 'Jessy Pinkman'];
```

```
const ageAbove18 = (person) => person.age >= 18;const addCoffeeLoverProperty = (person) => { person.coffeeLover = coffeeLovers.includes(person.name);  return person;}
```

```
const ageReducer = (sum, person) => { return sum + person.age;}, 0);
```

```
const coffeeLoversAbove18 = people .filter(ageAbove18) .map(addCoffeeLoverProperty);
```

```
const totalAgeOfCoffeeLoversAbove18 = coffeeLoversAbove18 .reduce(ageReducer);
```

```
const totalAge = people .reduce(ageReducer);
```

Si vous le faites de manière impérative, vous finirez par écrire beaucoup de code répétitif.

L'état d'esprit de création de fonctions avec `.map()`, `.reduce()` et `.filter()` améliorera la qualité du code que vous écrirez. Mais cela ajoute également beaucoup de lisibilité. Vous n'avez pas à penser à ce qui se passe à l'intérieur d'une fonction. C'est facile à comprendre.

Merci d'avoir lu ! :)

Dites bonjour sur [Twitter](https://twitter.com/guidsen)