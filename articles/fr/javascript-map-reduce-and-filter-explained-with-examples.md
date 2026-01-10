---
title: JavaScript Map, Reduce, et Filter - Fonctions de tableau JS expliquées avec
  des exemples de code
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-11-10T17:53:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-map-reduce-and-filter-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f75740569d1a4ca42b1.jpg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
seo_title: JavaScript Map, Reduce, et Filter - Fonctions de tableau JS expliquées
  avec des exemples de code
seo_desc: Map, reduce, and filter are all array methods in JavaScript. Each one will
  iterate over an array and perform a transformation or computation. Each will return
  a new array based on the result of the function. In this article, you will learn
  why and ho...
---

Map, reduce et filter sont toutes des méthodes de tableau en JavaScript. Chacune va itérer sur un tableau et effectuer une transformation ou un calcul. Chacune retournera un nouveau tableau basé sur le résultat de la fonction. Dans cet article, vous apprendrez pourquoi et comment utiliser chacune d'entre elles.

Voici un résumé amusant par Steven Luscher :

%[https://twitter.com/steveluscher/status/741089564329054208]

## Map

La méthode `map()` est utilisée pour créer un nouveau tableau à partir d'un tableau existant, en appliquant une fonction à chacun des éléments du premier tableau.

### Syntaxe

```javascript
var new_array = arr.map(function callback(element, index, array) {
    // Retourne la valeur pour new_array
}[, thisArg])
```

Dans le callback, seul l'élément `element` du tableau est requis. Habituellement, une action est effectuée sur la valeur et ensuite une nouvelle valeur est retournée.

### Exemple

Dans l'exemple suivant, chaque nombre d'un tableau est doublé.

```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(item => item * 2);
console.log(doubled); // [2, 4, 6, 8]
```

## Filter

La méthode `filter()` prend chaque élément d'un tableau et applique une instruction conditionnelle. Si cette condition retourne vrai, l'élément est ajouté au tableau de sortie. Si la condition retourne faux, l'élément n'est pas ajouté au tableau de sortie.

### Syntaxe

```javascript
var new_array = arr.filter(function callback(element, index, array) {
    // Retourne vrai ou faux
}[, thisArg])
```

La syntaxe pour `filter` est similaire à `map`, sauf que la fonction de callback doit retourner `true` pour garder l'élément, ou `false` sinon. Dans le callback, seul l'`element` est requis.

### Exemples

Dans l'exemple suivant, les nombres impairs sont "filtrés", ne laissant que les nombres pairs.

```javascript
const numbers = [1, 2, 3, 4];
const evens = numbers.filter(item => item % 2 === 0);
console.log(evens); // [2, 4]
```

Dans l'exemple suivant, `filter()` est utilisé pour obtenir tous les étudiants dont les notes sont supérieures ou égales à 90.

```javascript
const students = [
  { name: 'Quincy', grade: 96 },
  { name: 'Jason', grade: 84 },
  { name: 'Alexis', grade: 100 },
  { name: 'Sam', grade: 65 },
  { name: 'Katie', grade: 90 }
];

const studentGrades = students.filter(student => student.grade >= 90);
return studentGrades; // [ { name: 'Quincy', grade: 96 }, { name: 'Alexis', grade: 100 }, { name: 'Katie', grade: 90 } ]
```

## Reduce

La méthode `reduce()` réduit un tableau de valeurs à une seule valeur. Pour obtenir la valeur de sortie, elle exécute une fonction de réduction sur chaque élément du tableau.

### **Syntaxe**

```javascript
arr.reduce(callback[, initialValue])
```

L'argument `callback` est une fonction qui sera appelée une fois pour chaque élément du tableau. Cette fonction prend quatre arguments, mais souvent seuls les deux premiers sont utilisés.

* _accumulator_ - la valeur retournée de l'itération précédente
* _currentValue_ - l'élément actuel dans le tableau
* _index_ - l'index de l'élément actuel
* _array_ - le tableau original sur lequel reduce a été appelé
* L'argument `initialValue` est facultatif. S'il est fourni, il sera utilisé comme valeur initiale de l'accumulateur dans le premier appel à la fonction de callback.

### Exemples

L'exemple suivant additionne tous les nombres dans un tableau de nombres.

```javascript
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce(function (result, item) {
  return result + item;
}, 0);
console.log(sum); // 10
```

Dans l'exemple suivant, `reduce()` est utilisé pour transformer un tableau de chaînes en un seul objet qui montre combien de fois chaque chaîne apparaît dans le tableau. Remarquez que cet appel à reduce passe un objet vide `{}` comme paramètre `initialValue`. Cela sera utilisé comme valeur initiale de l'accumulateur (le premier argument) passé à la fonction de callback.

```javascript
var pets = ['dog', 'chicken', 'cat', 'dog', 'chicken', 'chicken', 'rabbit'];

var petCounts = pets.reduce(function(obj, pet){
    if (!obj[pet]) {
        obj[pet] = 1;
    } else {
        obj[pet]++;
    }
    return obj;
}, {});

console.log(petCounts); 

/*
Sortie :
 { 
    dog: 2, 
    chicken: 3, 
    cat: 1, 
    rabbit: 1 
 }
 */
```

## Explication vidéo

Consultez la vidéo ci-dessous de la chaîne YouTube freeCodeCamp.org. Elle couvre les méthodes de tableau discutées, ainsi que quelques autres.

%[https://www.youtube.com/watch?v=Urwzk6ILvPQ]