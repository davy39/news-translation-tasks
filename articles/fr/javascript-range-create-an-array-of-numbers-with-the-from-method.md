---
title: JavaScript Range – Comment créer un tableau de nombres avec .from() en JS ES6
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-12-14T21:15:06.000Z'
originalURL: https://freecodecamp.org/news/javascript-range-create-an-array-of-numbers-with-the-from-method
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/cover-template--1-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript Range – Comment créer un tableau de nombres avec .from() en
  JS ES6
seo_desc: 'The .from() method is a static method of the Array object in JavaScript
  ES6. It creates a new, shallow-copied Array instance from an array-like or iterable
  object like map and set.

  This method returns an array from any object with a length property. ...'
---

La méthode `.from()` est une méthode statique de l'objet `Array` en JavaScript ES6. Elle crée une nouvelle instance de tableau, copiée superficiellement, à partir d'un objet de type tableau ou itérable comme `map` et `set`.

Cette méthode retourne un tableau à partir de n'importe quel objet avec une propriété length. Vous pouvez l'utiliser pour créer un tableau de nombres dans une plage spécifiée.

Dans cet article, vous apprendrez ce qu'est la méthode statique `.from()`, comment elle fonctionne et comment vous pouvez créer une plage de nombres en JavaScript.

Au cas où vous seriez pressé, voici une méthode pour vous aider à obtenir la plage :

```js
const arrayRange = (start, stop, step) =>
    Array.from(
    { length: (stop - start) / step + 1 },
    (value, index) => start + index * step
    );

console.log(arrayRange(1, 5, 1)); // [1,2,3,4,5]
```

Vous pouvez continuer à lire cet article court pour comprendre comment cela fonctionne.

## Comment la méthode `.from()` fonctionne en JavaScript

La méthode `Array.from()` retourne un tableau à partir de n'importe quel objet de type tableau ou itérable. La méthode prend un paramètre obligatoire et deux autres paramètres optionnels :

```js
// Syntaxe
Array.from(arraylike, mapFunc, thisArg)
```

* `arraylike` - Un objet de type tableau ou itérable à convertir en tableau.
    
* `mapFunc` - Ce paramètre est optionnel. La fonction Map est appelée sur chaque élément.
    
* `thisArg` - Cette valeur est utilisée lors de l'exécution de `mapFunc` en tant que `this`. Elle est également optionnelle.
    

Pour voir comment cela fonctionne, créons un tableau à partir d'une chaîne de caractères en utilisant la méthode `Array.from()` :

```js
let newArray = Array.from("freeCodeCamp");

console.log(newArray); // ["f","r","e","e","C","o","d","e","C","a","m","p"]
```

Dans l'exemple ci-dessus, la méthode `Array.from()` a retourné un tableau de la chaîne de caractères. Vous pouvez également utiliser la méthode pour retourner un tableau à partir de n'importe quel objet avec une propriété length qui spécifie le nombre d'éléments dans l'objet.

```js
let arrayLike = {0: 1, 1: 2, 2: 3, length: 3};
let newArray = Array.from(arrayLike);

console.log(newArray); // [1,2,3]
```

Vous pouvez également introduire la fonction map qui est appelée pour chaque élément. Par exemple, si vous voulez manipuler chaque élément du tableau en multipliant chacun par un nombre spécifique :

```js
let arrayLike = {0: 1, 1: 2, 2: 3, length: 3};
let newArray = Array.from(arrayLike, x => x * 2);

console.log(newArray); // [2,4,6]
```

**Note :** `.from()` est une méthode statique, c'est pourquoi elle utilise le nom de la classe `Array`. Vous ne pouvez l'utiliser que comme `Array.from()` et non comme `myArray.from()`, où `myArray` est un tableau. Cela retournera undefined.

## Comment créer une séquence de nombres avec la méthode `.from()`

La méthode `Array.from()` vous permet de créer une séquence de nombres en utilisant la fonction map :

```js
let newArray = Array.from({ length: 7 }, (value, index) => index);

console.log(newArray); // [0,1,2,3,4,5,6]
```

La méthode ci-dessus crée un tableau de 7 éléments qui sont par défaut initialisés avec `undefined`. Mais en utilisant la fonction map, la valeur de l'index est maintenant utilisée au lieu de sa valeur réelle de undefined.

Si vous utilisez sa valeur réelle, vous obtiendrez un tableau de 7 éléments (basé sur la longueur) avec la valeur undefined :

```js
let newArray = Array.from({ length: 7 }, (value, index) => value);

console.log(newArray); 
// retourne [undefined,undefined,undefined,undefined,undefined,undefined,undefined]
```

## Comment créer une plage de nombres avec la méthode `.from`

Vous savez maintenant comment créer un tableau avec une séquence de nombres. Mais lorsque vous créez une plage, vous voulez que ces nombres commencent à une valeur spécifiée et se terminent à une valeur spécifiée. Par exemple, les nombres dans la plage de 4 à 8 seraient 4, 5, 6, 7, 8.

Vous pouvez également spécifier si vous voulez un tableau de nombres impairs ou pairs dans une plage spécifiée. Tout cela peut être réalisé avec la méthode `Array.from()`.

```js
const arrayRange = (start, stop, step) =>
    Array.from(
    { length: (stop - start) / step + 1 },
    (value, index) => start + index * step
    );
```

Dans le code ci-dessus, la longueur de l'objet de type tableau est définie en soustrayant le dernier nombre du premier nombre dans la plage et en divisant par le pas plus un. Cela donnera le nombre exact d'éléments dans le tableau.

Dans la fonction map, le nombre de départ est ajouté à l'index de chaque élément (rappelez-vous, la valeur est toujours undefined) et multiplié par la valeur du pas. Cette fonction map s'exécute pour chaque élément et aide à calculer la valeur de chaque élément.

Essayons la méthode avec quelques exemples :

```js
// Générer des nombres entre la plage 2 et 7
let range = arrayRange(2, 7, 1);
console.log(range); // [2,3,4,5,6,7]

// Générer des nombres pairs entre la plage 2 et 7
let evenRange = arrayRange(2, 7, 2);
console.log(evenRange); // [2,4,6]

// Générer des nombres impairs entre la plage 1 et 5
let oddRange = arrayRange(1, 5, 2);
console.log(oddRange); // [1,3,5]
```

## Conclusion

Dans cet article, vous avez appris comment créer un tableau de nombres avec la méthode `Array.from()`. Vous avez également appris comment fonctionne la méthode `Array.from()`.

Gardez à l'esprit qu'il existe d'autres options pour créer une plage de nombres en JavaScript – nous nous sommes concentrés sur `.from()` dans ce tutoriel.

Amusez-vous bien à coder !