---
title: Somme d'un tableau en JS – Comment additionner les nombres d'un tableau JavaScript
date: '2023-03-31T17:45:12.000Z'
author: Dionysia Lemonaki
authorURL: https://www.freecodecamp.org/news/author/dionysialemonaki/
originalURL: https://freecodecamp.org/news/how-to-add-numbers-in-javascript-arrays
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-chelsey-horne-4506938.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_desc: 'An array in JavaScript is an object that allows you to store an ordered
  collection of multiple values under a single variable name and manipulate those
  values in numerous ways.

  In this article, you will learn how to calculate the sum of all the numbe...'
---


Un tableau en JavaScript est un objet qui vous permet de stocker une collection ordonnée de plusieurs valeurs sous un seul nom de variable et de manipuler ces valeurs de nombreuses façons.

<!-- more -->

Dans cet article, vous apprendrez à calculer la somme de tous les nombres d'un tableau donné en utilisant plusieurs approches différentes.

Plus précisément, je vais vous montrer comment trouver la somme de tous les nombres d'un tableau en utilisant :

-   Une boucle `for`
-   La méthode `forEach()`
-   La méthode `reduce()`

C'est parti !

## Comment calculer la somme d'un tableau à l'aide d'une boucle `for` en JavaScript

L'une des façons les plus simples de calculer la somme de tous les nombres d'un tableau est d'utiliser une boucle `for`. Elle effectue une itération un nombre `n` de fois.

Regardons l'exemple suivant :

```
// create an array
let myNums = [1, 2, 3, 4, 5];

// create a variable for the sum and initialize it
let sum = 0;

// iterate over each item in the array
for (let i = 0; i < myNums.length; i++ ) {
  sum += myNums[i];
}

console.log(sum) // 15
```

Dans l'exemple ci-dessus, j'ai d'abord créé un tableau nommé `myNums` qui stocke cinq valeurs.

J'ai ensuite déclaré une variable nommée `sum` et je l'ai initialisée avec une valeur de `0` – cette variable stockera le résultat des calculs dans la boucle `for`.

Ensuite, j'ai utilisé la boucle `for` pour itérer sur tous les éléments jusqu'à la fin du tableau `myNums`.

J'ai également réassigné la valeur de la variable `sum` en utilisant l'opérateur d'affectation après addition, en ajoutant sa valeur actuelle et l'élément actuel du tableau.

Pour en savoir plus sur la boucle `for` en JavaScript, consultez [cet article][1].

## Comment calculer la somme d'un tableau à l'aide de la méthode `forEach()` en JavaScript

Une autre façon de calculer la somme d'un tableau consiste à utiliser la méthode intégrée `forEach()` de JavaScript. Elle itère sur un tableau et appelle une fonction pour chaque élément.

Regardons l'exemple suivant :

```
// create an array
const myNums = [1,2,3,4,5];

// create a variable for the sum and initialize it
let sum = 0;

// calculate sum using forEach() method
myNums.forEach( num => {
  sum += num;
})

console.log(sum) // 15
```

Dans l'exemple ci-dessus, j'ai créé un tableau `myNums`. J'ai également déclaré une variable nommée `sum` et je l'ai initialisée avec une valeur de `0`.

Ensuite, j'ai utilisé la méthode `forEach()` pour itérer sur chaque élément du tableau.

À chaque itération, j'ai réassigné la valeur de la variable `sum` en ajoutant sa valeur actuelle et la valeur de l'élément actuel du tableau.

Pour en savoir plus sur la fonction `forEach()`, consultez [cet article][2].

## Comment calculer la somme d'un tableau à l'aide de la méthode `reduce()` en JavaScript

Une autre façon de calculer la somme d'un tableau consiste à utiliser la méthode `reduce()`, introduite avec ES6.

La méthode `reduce()` réduit tous les éléments d'un tableau en une seule valeur.

Regardons l'exemple suivant :

```
// create an array
const myNums = [1,2,3,4,5];

// use reduce() method to find the sum
var sum = myNums.reduce((accumulator, currentValue) => {
  return accumulator + currentValue
},0);

console.log(sum) // 15
```

La méthode `reduce()` prend une fonction de rappel (callback) définie par l'utilisateur comme premier argument obligatoire. La fonction est appelée sur chaque élément du tableau.

La fonction de rappel accepte les deux paramètres obligatoires suivants :

-   L'`accumulator` (accumulateur), qui est la variable qui stocke la dernière valeur retournée par l'appel de fonction précédent.
-   La `currentValue` (valeur actuelle), qui représente l'élément actuel du tableau.

Le deuxième argument de la méthode `reduce()` est l'`initialValue` (valeur initiale), qui est `0`. L'`initialValue` représente la valeur initiale de l'`accumulator`.

Pour en savoir plus sur la méthode `reduce()`, consultez [cet article][3].

## Conclusion

Et voilà ! Vous avez appris trois façons de calculer la somme d'un tableau en JavaScript.

Pour en savoir plus sur JavaScript, consultez [ce cours complet de JavaScript pour débutants][4].

Merci de votre lecture, et bon codage !

[1]: https://www.freecodecamp.org/news/javascript-for-loops/
[2]: https://www.freecodecamp.org/news/javascript-foreach-how-to-loop-through-an-array-in-js/
[3]: https://www.freecodecamp.org/news/reduce-f47a7da511a9/
[4]: https://www.freecodecamp.org/news/full-javascript-course-for-beginners/