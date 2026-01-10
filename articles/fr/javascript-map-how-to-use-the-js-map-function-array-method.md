---
title: JavaScript Map – Comment utiliser la fonction JS .map() (Méthode de tableau)
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-03-31T17:20:19.000Z'
originalURL: https://freecodecamp.org/news/javascript-map-how-to-use-the-js-map-function-array-method
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/javascript-map-function.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: JavaScript Map – Comment utiliser la fonction JS .map() (Méthode de tableau)
seo_desc: "Sometimes you may need to take an array and apply some procedure to its\
  \ elements so that you get a new array with modified elements. \nInstead of manually\
  \ iterating over the array using a loop, you can simply use the built-in Array.map()\
  \ method.\nHere'..."
---

Parfois, vous pouvez avoir besoin de prendre un tableau et d'appliquer une procédure à ses éléments afin d'obtenir un nouveau tableau avec des éléments modifiés. 

Au lieu d'itérer manuellement sur le tableau en utilisant une boucle, vous pouvez simplement utiliser la méthode intégrée `Array.map()`.

### Voici un Scrim interactif sur comment utiliser la fonction JS .map()

<iframe src="https://scrimba.com/scrim/co93c4bf0af8e0ed2e162b818?pl=pKwWeHY&embed=freecodecamp,mini-header" width="100%" height="420"></iframe>

La méthode `Array.map()` vous permet d'itérer sur un tableau et de modifier ses éléments en utilisant une fonction de rappel. La fonction de rappel sera ensuite exécutée sur chacun des éléments du tableau.

Par exemple, supposons que vous avez l'élément de tableau suivant :

```js
let arr = [3, 4, 5, 6];
```

Maintenant, imaginez que vous devez multiplier chacun des éléments du tableau par `3`. Vous pourriez envisager d'utiliser une boucle `for` comme suit :

```js
let arr = [3, 4, 5, 6];

for (let i = 0; i < arr.length; i++){
  arr[i] = arr[i] * 3;
}

console.log(arr); // [9, 12, 15, 18]
```

Mais vous pouvez en fait utiliser la méthode `Array.map()` pour obtenir le même résultat. Voici un exemple :

```js
let arr = [3, 4, 5, 6];

let modifiedArr = arr.map(function(element){
    return element *3;
});

console.log(modifiedArr); // [9, 12, 15, 18]
```

La méthode `Array.map()` est couramment utilisée pour appliquer des modifications aux éléments, qu'il s'agisse de multiplier par un nombre spécifique comme dans le code ci-dessus, ou d'effectuer toute autre opération que vous pourriez nécessiter pour votre application.

## Comment utiliser map() sur un tableau d'objets

Par exemple, vous pouvez avoir un tableau d'objets qui stocke les valeurs `firstName` et `lastName` de vos amis comme suit :

```js
let users = [
  {firstName : "Susan", lastName: "Steward"},
  {firstName : "Daniel", lastName: "Longbottom"},
  {firstName : "Jacob", lastName: "Black"}
];


```

Vous pouvez utiliser la méthode `map()` pour itérer sur le tableau et joindre les valeurs de `firstName` et `lastName` comme suit :

```js
let users = [
  {firstName : "Susan", lastName: "Steward"},
  {firstName : "Daniel", lastName: "Longbottom"},
  {firstName : "Jacob", lastName: "Black"}
];

let userFullnames = users.map(function(element){
    return `${element.firstName} ${element.lastName}`;
})

console.log(userFullnames);
// ["Susan Steward", "Daniel Longbottom", "Jacob Black"]
```

La méthode `map()` passe plus qu'un simple élément. Voyons tous les arguments passés par `map()` à la fonction de rappel.

### Voici un scrim interactif sur l'utilisation de map() pour itérer sur un tableau d'objets :

<iframe src="https://scrimba.com/scrim/cLwqQ7uE?pl=pKwWeHY&embed=freecodecamp,mini-header" width="100%" height="420"></iframe>

## La syntaxe complète de la méthode map()

La syntaxe de la méthode `map()` est la suivante :

```js
arr.map(function(element, index, array){  }, this);
```

La fonction de rappel `function()` est appelée sur chaque élément du tableau, et la méthode `map()` passe toujours l'`element` actuel, l'`index` de l'élément actuel, et l'objet `array` entier à celle-ci.

L'argument `this` sera utilisé à l'intérieur de la fonction de rappel. Par défaut, sa valeur est `undefined`. Par exemple, voici comment changer la valeur de `this` en nombre `80` :

```js
let arr = [2, 3, 5, 7]

arr.map(function(element, index, array){
	console.log(this) // 80
}, 80);
```

Vous pouvez également tester les autres arguments en utilisant `console.log()` si vous êtes intéressé :

```js
let arr = [2, 3, 5, 7]

arr.map(function(element, index, array){
    console.log(element);
    console.log(index);
    console.log(array);
    return element;
}, 80);
```

### Voici un scrim interactif qui passe en revue la syntaxe complète :

<iframe src="https://scrimba.com/scrim/c7wmmJcv?pl=pKwWeHY&embed=freecodecamp,mini-header" width="100%" height="420"></iframe>

Et c'est tout ce que vous devez savoir sur la méthode `Array.map()`. Le plus souvent, vous n'utiliserez que l'argument `element` à l'intérieur de la fonction de rappel tout en ignorant le reste. C'est ce que je fais habituellement dans mes projets quotidiens :)

## **Merci d'avoir lu ce tutoriel**

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez réellement avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine !