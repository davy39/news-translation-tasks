---
title: 'Les Boucles JavaScript Expliquées : For Loop, While Loop, Do...while Loop,
  et Plus'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-15T21:53:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-loops-explained-for-loop-for
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c92740569d1a4ca32f7.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
- name: toothbrush
  slug: toothbrush
seo_title: 'Les Boucles JavaScript Expliquées : For Loop, While Loop, Do...while Loop,
  et Plus'
seo_desc: 'Loops are used in JavaScript to perform repeated tasks based on a condition.
  Conditions typically return true or false. A loop will continue running until the
  defined condition returns false.

  for Loop

  Syntax

  for (initialization; condition; finalExpre...'
---

Les boucles sont utilisées en JavaScript pour effectuer des tâches répétées basées sur une condition. Les conditions retournent généralement `true` ou `false`. Une boucle continuera à s'exécuter jusqu'à ce que la condition définie retourne `false`.

## Boucle `for`

### **Syntaxe**

```js
for (initialisation; condition; expressionFinale) {
  // code
}
```

La boucle `for` se compose de trois expressions optionnelles, suivies d'un bloc de code :

* `initialisation` - Cette expression s'exécute avant la première itération de la boucle, et est généralement utilisée pour créer un compteur.
* `condition` - Cette expression est vérifiée à chaque fois avant l'exécution de la boucle. Si elle évalue à `true`, l'`instruction` ou le code dans la boucle est exécuté. Si elle évalue à `false`, la boucle s'arrête. Et si cette expression est omise, elle évalue automatiquement à `true`.
* `expressionFinale` - Cette expression est exécutée après chaque itération de la boucle. Cela est généralement utilisé pour incrémenter un compteur, mais peut être utilisé pour le décrémenter.

N'importe laquelle de ces trois expressions ou le code dans le bloc de code peut être omise.

Les boucles `for` sont couramment utilisées pour exécuter du code un nombre défini de fois. De plus, vous pouvez utiliser `break` pour sortir de la boucle plus tôt, avant que l'expression `condition` n'évalue à `false`.

### **Exemples**

1. Itérer à travers les entiers de 0 à 8 :

```js
for (let i = 0; i < 9; i++) {
  console.log(i);
}

// Sortie :
// 0
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
```

2. Utiliser `break` pour sortir d'une boucle `for` avant que `condition` ne soit `false` :

```js
for (let i = 1; i < 10; i += 2) {
  if (i === 7) {
    break;
  }
  console.log('Nombre total d'éléphants : ' + i);
}

// Sortie :
// Nombre total d'éléphants : 1
// Nombre total d'éléphants : 3
// Nombre total d'éléphants : 5
```

### Piège Courant : **Dépassement des Limites d'un Tableau**

Lors de l'itération sur un tableau, il est facile de dépasser accidentellement les limites du tableau.

Par exemple, votre boucle peut essayer de référencer le 4ème élément d'un tableau avec seulement 3 éléments :

```js
const arr = [ 1, 2, 3 ];

for (let i = 0; i <= arr.length; i++) {
  console.log(arr[i]);
}

// Sortie :
// 1
// 2
// 3
// undefined
```

Il y a deux façons de corriger ce code : définir `condition` à `i < arr.length` ou `i <= arr.length - 1`.

## Boucle `for...in`

### Syntaxe

```js
for (propriété in objet) {
  // code
}
```

La boucle `for...in` itère sur les propriétés d'un objet. Pour chaque propriété, le code dans le bloc de code est exécuté.

### Exemples

1. Itérer sur les propriétés d'un objet et logger son nom et sa valeur dans la console :

```js
const capitals = {
  a: "Athens",
  b: "Belgrade",
  c: "Cairo"
};

for (let key in capitals) {
  console.log(key + ": " + capitals[key]);
}

// Sortie :
// a: Athens
// b: Belgrade
// c: Cairo
```

### Piège Courant : **Comportement Inattendu lors de l'Itération sur un Tableau**

Bien que vous puissiez utiliser une boucle `for...in` pour itérer sur un tableau, il est recommandé d'utiliser une boucle `for` ou `for...of` à la place.

La boucle `for...in` peut itérer sur des tableaux et des objets de type tableau, mais elle peut ne pas toujours accéder aux index du tableau dans l'ordre.

De plus, la boucle `for...in` retourne toutes les propriétés et les propriétés héritées pour un tableau ou un objet de type tableau, ce qui peut conduire à un comportement inattendu.

Par exemple, cette boucle simple fonctionne comme prévu :

```js
const array = [1, 2, 3];

for (const i in array) {
  console.log(i);
}

// 0
// 1
// 2
```

Mais si quelque chose comme une bibliothèque JS que vous utilisez modifie directement le prototype `Array`, une boucle `for...in` itérera également sur cela :

```js
const array = [1, 2, 3];

Array.prototype.someMethod = true;

for (const i in array) {
  console.log(i);
}

// 0
// 1
// 2
// someMethod
```

Bien que la modification directe de prototypes en lecture seule comme `Array` ou `Object` va à l'encontre des bonnes pratiques, cela pourrait poser problème avec certaines bibliothèques ou bases de code.

De plus, puisque `for...in` est conçu pour les objets, il est beaucoup plus lent avec les tableaux que les autres boucles.

En résumé, rappelez-vous simplement d'utiliser les boucles `for...in` uniquement pour itérer sur des objets, pas sur des tableaux.

## Boucle `for...of`

### Syntaxe

```js
for (variable of objet) {
  // code
}
```

La boucle `for...of` itère sur les valeurs de nombreux types d'itérables, y compris les tableaux, et les types de collections spéciales comme `Set` et `Map`. Pour chaque valeur dans l'objet itérable, le code dans le bloc de code est exécuté.

### Exemples

1. Itérer sur un tableau :

```js
const arr = [ "Fred", "Tom", "Bob" ];

for (let i of arr) {
  console.log(i);
}

// Sortie :
// Fred
// Tom
// Bob
```

2. Itérer sur une `Map` :

```js
const m = new Map();
m.set(1, "black");
m.set(2, "red");

for (let n of m) {
  console.log(n);
}

// Sortie :
// [1, black]
// [2, red]
```

3. Itérer sur un `Set` :

```js
const s = new Set();
s.add(1);
s.add("red");

for (let n of s) {
  console.log(n);
}

// Sortie :
// 1
// red
```

## Boucle `while`

### Syntaxe

```js
while (condition) {
  // instruction
}
```

La boucle `while` commence par évaluer `condition`. Si `condition` évalue à `true`, le code dans le bloc de code est exécuté. Si `condition` évalue à `false`, le code dans le bloc de code n'est pas exécuté et la boucle se termine.

### Exemples :

1. Tant qu'une variable est inférieure à 10, logger sa valeur dans la console et l'incrémenter de 1 :

```js
let i = 1;

while (i < 10) {
  console.log(i);
  i++;
}

// Sortie :
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9
```

## Boucle `do...while`

### Syntaxe :

```js
do {
  // instruction
} while (condition);
```

La boucle `do...while` est étroitement liée à la boucle `while`. Dans une boucle `do...while`, `condition` est vérifiée à la fin de chaque itération de la boucle, plutôt qu'au début avant l'exécution de la boucle.

Cela signifie que le code dans une boucle `do...while` est garanti de s'exécuter au moins une fois, même si l'expression `condition` évalue déjà à `true`.

### Exemple :

1. Tant qu'une variable est inférieure à 10, logger sa valeur dans la console et l'incrémenter de 1 :

```js
let i = 1;

do {
  console.log(i);
  i++;
} while (i < 10);

// Sortie :
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9
```

2. Ajouter à un tableau, même si `condition` évalue à `true` :

```js
const myArray = [];
let i = 10;

do {
  myArray.push(i);
  i++;
} while (i < 10);

console.log(myArray);

// Sortie :
// [10]
```