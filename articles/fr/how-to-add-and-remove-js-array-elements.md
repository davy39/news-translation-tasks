---
title: Comment ajouter et supprimer des éléments de tableaux en JavaScript
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2024-03-13T12:34:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-and-remove-js-array-elements
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/mohammad-rahmani-unwXUc_Pqi4-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment ajouter et supprimer des éléments de tableaux en JavaScript
seo_desc: 'Arrays are common data structures in JavaScript, and it is important to
  know how to work with them. Common operations on arrays include adding or removing
  elements from the beginning, end or at a specific index.

  In this article, you will learn how to...'
---

Les tableaux sont des structures de données courantes en JavaScript, et il est important de savoir comment travailler avec eux. Les opérations courantes sur les tableaux incluent l'ajout ou la suppression d'éléments au début, à la fin ou à un index spécifique.

Dans cet article, vous apprendrez à travailler avec les méthodes JavaScript intégrées : `pop`, `push`, `shift` et `unshift`. Vous apprendrez également à travailler avec la méthode `splice` qui vous permet de modifier le tableau original et d'ajouter/supprimer des éléments à un index spécifique.

## Qu'est-ce qu'un tableau en JavaScript ?

Avant de commencer à examiner ces différentes méthodes de tableau, il est important de comprendre ce qu'est un tableau en JavaScript.

Un tableau est un type de structure de données en JavaScript qui est utilisé pour stocker une collection d'éléments pouvant être de différents types. Ces types de données peuvent inclure des chaînes de caractères, des nombres, des booléens (`true` ou `false`), d'autres tableaux et objets (`{}`).

Voici un exemple de tableau de noms :

```js
const names = ["Jessica", "Jacob", "Zach", "Michelle"];
```

Pour accéder à un élément d'un tableau, vous référencez le nom du tableau, suivi d'une paire de crochets contenant l'index de l'élément auquel vous souhaitez accéder.

Les tableaux sont indexés à partir de zéro, ce qui signifie que le premier élément du tableau a un index de 0, le deuxième élément a un index de 1, et ainsi de suite.

Voici un exemple d'accès au deuxième élément du tableau `names` :

```js
names[1]; // "Jacob"
```

Si vous souhaitez accéder au dernier élément d'un tableau, vous pouvez utiliser la longueur du tableau moins 1.

```js
names[names.length - 1]; // "Michelle"
```

## Comment supprimer un élément à la fin du tableau

Si vous souhaitez supprimer un élément à la fin d'un tableau, vous pouvez utiliser la méthode `pop`. La méthode `pop` supprime le dernier élément d'un tableau et retourne cet élément.

Voici un exemple d'utilisation de la méthode `pop` sur le tableau `names` :

```js
const names = ["Jessica", "Jacob", "Zach", "Michelle"];
const removedName = names.pop();

console.log(removedName); // "Michelle"
```

Si vous essayez d'utiliser la méthode `pop` sur un tableau vide, elle retournera `undefined`.

```js
const emptyArray = [];
const removedElement = emptyArray.pop();

console.log(removedElement); // undefined
```

Si vous affichez le tableau `names`, vous verrez les éléments restants.

```js
console.log(names); // ["Jessica", "Jacob", "Zach"]
```

## Comment supprimer un élément au début du tableau

Si vous souhaitez supprimer un élément au début d'un tableau, vous pouvez utiliser la méthode `shift`. La méthode `shift` supprime le premier élément d'un tableau et retourne cet élément.

Voici un exemple d'utilisation de la méthode `shift` sur le tableau `names` :

```js
const names = ["Jessica", "Jacob", "Zach", "Michelle"];
const removedName = names.shift();

console.log(removedName); // "Jessica"
```

Tout comme la méthode `pop`, si vous essayez d'utiliser la méthode `shift` sur un tableau vide, elle retournera `undefined`.

```js
const emptyArray = [];
const removedElement = emptyArray.shift();

console.log(removedElement); // undefined
```

## Comment ajouter un élément à la fin du tableau

Si vous devez ajouter un élément à la fin d'un tableau, vous pouvez utiliser la méthode `push`. La méthode `push` ajoute un ou plusieurs éléments à la fin d'un tableau et retourne la nouvelle longueur du tableau.

Voici un exemple de tableau de langages de programmation :

```js
const programmingLanguages = ["JavaScript", "Python", "Ruby"];
```

Si vous souhaitez ajouter les langages `Go` et `Rust` à la fin du tableau `programmingLanguages`, vous utiliseriez la méthode `push`.

```js
const programmingLanguages = ["JavaScript", "Python", "Ruby"];
const originalLength = programmingLanguages.length; // 3

const newLength = programmingLanguages.push("Go", "Rust");

console.log(newLength); // 5
console.log(programmingLanguages); // ["JavaScript", "Python", "Ruby", "Go", "Rust"]
```

Une chose intéressante que vous pouvez faire avec la méthode `push` est d'ajouter un tableau à la fin d'un autre tableau.

Dans cet exemple, nous avons un tableau de `programmingLanguages` et un tableau de `newLanguages`. Nous pouvons utiliser la méthode `push` et la [syntaxe de décomposition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) pour ajouter le tableau `newLanguages` à la fin du tableau `programmingLanguages`.

```js
const programmingLanguages = ["JavaScript", "Python", "Ruby"];
const newLanguages = ["Go", "Rust"];

const newLength = programmingLanguages.push(...newLanguages);

console.log(newLength); // 5
console.log(programmingLanguages); // ["JavaScript", "Python", "Ruby", "Go", "Rust"]
```

## Comment ajouter un élément au début du tableau

Si vous souhaitez ajouter un élément au début d'un tableau, vous pouvez utiliser la méthode `unshift`. La méthode `unshift` ajoute un ou plusieurs éléments au début d'un tableau et retourne la nouvelle longueur du tableau.

Voici un exemple d'utilisation de la méthode `unshift` pour ajouter trois nouveaux langages de programmation au début du tableau `programmingLanguages`.

```js
const programmingLanguages = ["JavaScript", "Python", "Ruby"];
const originalLength = programmingLanguages.length; // 3

const newLength = programmingLanguages.unshift("Go", "Rust", "C#");

console.log(newLength); // 6
console.log(programmingLanguages); // ["Go", "Rust", "C#", "JavaScript", "Python", "Ruby"]
```

## Comment ajouter et supprimer des éléments à un index spécifique

Un index est la position d'un élément dans le tableau. Le premier élément du tableau a un index de 0, le deuxième élément a un index de 1, et ainsi de suite.

Pour ajouter des éléments à un index spécifique, vous pouvez utiliser la méthode `splice`. La méthode `splice` vous permet d'ajouter et de supprimer des éléments à un index spécifique dans un tableau.

Dans cet exemple, nous avons une liste de villes américaines.

```js
const cities = ["New York", "Los Angeles", "Chicago", "Houston"];
```

Si nous voulons ajouter la ville de `San Francisco` au deuxième index du tableau `cities`, nous utiliserions la méthode `splice`.

```js
const cities = ["New York", "Los Angeles", "Chicago", "Houston"];

cities.splice(1, 0, "San Francisco");

console.log(cities); // ["New York", "San Francisco", "Los Angeles", "Chicago", "Houston"]
```

Le premier argument de la méthode `splice` est l'index où vous souhaitez ajouter ou supprimer des éléments. Dans ce cas, nous voulons ajouter notre ville à l'index 1.

Le deuxième argument est le nombre d'éléments à supprimer. Dans ce cas, nous ne cherchons pas à supprimer d'éléments, donc nous passons 0.

Le troisième argument est l'élément ou les éléments que vous souhaitez ajouter. C'est là que nous passons la ville de `San Francisco`.

```js
cities.splice(1, 0, "San Francisco");
```

Si nous voulons supprimer des éléments à un index spécifique, nous pouvons également utiliser la méthode `splice`.

Dans cet exemple, nous voulons supprimer la ville de `Los Angeles` du tableau `cities`. Nous pouvons utiliser la méthode `indexOf` pour trouver l'index de `Los Angeles` puis utiliser la méthode `splice` pour la supprimer.

La méthode `indexOf` retourne le premier index auquel un élément donné peut être trouvé dans le tableau, ou -1 s'il n'est pas présent.

```js
const cities = ["New York", "Los Angeles", "Chicago", "Houston"];

const index = cities.indexOf("Los Angeles");

if (index !== -1) {
  cities.splice(index, 1);
}

console.log(cities); // ["New York", "Chicago", "Houston"]
```

Le premier argument de `index` est l'index où nous voulons supprimer l'élément. Le deuxième argument de 1 est le nombre d'éléments que nous voulons supprimer.

```js
cities.splice(index, 1);
```

Nous enveloppons cela dans une instruction `if` pour vérifier si l'index de `Los Angeles` n'est pas égal à -1. -1 représente que l'élément n'est pas présent dans le tableau.

Si la ville est présente dans le tableau, alors nous pouvons utiliser la méthode `splice` pour la supprimer.

```js
if (index !== -1) {
  cities.splice(index, 1);
}
```

## Conclusion

Dans cet article, vous avez appris à travailler avec les méthodes JavaScript intégrées `pop`, `push`, `shift` et `unshift`. Ces méthodes sont utiles lorsque vous souhaitez ajouter ou supprimer des éléments au début ou à la fin d'un tableau.

Vous avez également appris à travailler avec la méthode `splice` qui vous permet de modifier le tableau original et d'ajouter/supprimer des éléments à un index spécifique.

Toutes les méthodes que nous avons couvertes dans cet article modifient le tableau original. Cela signifie que le tableau original est changé après avoir utilisé ces méthodes.

J'espère que vous avez trouvé cet article utile et bon codage !