---
title: JavaScript Sort Array - Comment trier un tableau avec précision
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-03-14T15:14:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-sort-javascript-array-accurately
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/cover-template--5-.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: JavaScript Sort Array - Comment trier un tableau avec précision
seo_desc: 'In programming, situations that need you to sort data will always arise.
  When you sort data, you will always want accurate results because failure to get
  an accurate result can result in malfunctions or bugs within your code.

  In this article, you wil...'
---

En programmation, des situations nécessitant de trier des données se présenteront toujours. Lorsque vous triez des données, vous voulez toujours des résultats précis, car un échec peut entraîner des dysfonctionnements ou des bugs dans votre code.

Dans cet article, vous apprendrez à trier un tableau en JavaScript, les lacunes associées à la méthode `sort()` et comment obtenir des résultats plus précis.

Si vous êtes pressé, la meilleure façon de trier un tableau avec précision est d'utiliser la fonction de comparaison. Vous devez passer une fonction de comparaison à la méthode `sort()`. Cela sera mieux expliqué dans cet article, mais voici un exemple :

```js
const numbersArr = [3, 10, 4, 21, 5, 9, 2, 6, 5, 3, 5];

// Ordre croissant
numbersArr.sort((a, b) => a - b);
console.log(numbersArr); // Sortie : [2,3,3,4,5,5,5,6,9,10,21]

// Ordre décroissant
numbersArr.sort((a, b) => b - a);
console.log(numbersArr); // Sortie : [21,10,9,6,5,5,5,4,3,3,2]
```

Si vous n'êtes pas pressé, comprenons ce qui cause ce dysfonctionnement avec la méthode `sort()` et les différentes façons de résoudre le problème.

## Comment fonctionne la méthode sort() des tableaux en JavaScript

La méthode `sort()` peut être utilisée pour trier les éléments d'un tableau par ordre croissant en se basant par défaut sur les valeurs des codes de caractères Unicode.

Avant d'explorer comment elle trie en fonction des valeurs des codes de caractères Unicode, voyons quelques exemples.

```js
let numArray = [3, 4, 1, 7, 2];
let sortedArr = numArray.sort();
console.log(sortedArr); // Sortie : [1,2,3,4,7]
```

Il est également important que vous sachiez que lorsque vous appliquez la méthode `sort()` à un tableau, elle modifie la position des éléments dans le tableau d'origine. Cela signifie que vous n'avez pas besoin d'assigner une nouvelle variable au tableau trié :

```js
let numArray = [3, 4, 1, 7, 2];
numArray.sort();
console.log(numArray); // Sortie : [1,2,3,4,7]
```

Vous pouvez également appliquer la méthode au tableau lui-même :

```js
let numArray = [3, 4, 1, 7, 2].sort();
console.log(numArray); // Sortie : [1,2,3,4,7]
```

Mais c'est loin d'être le seul sujet de cet article. La méthode `sort()` compare les éléments du tableau en les convertissant en chaînes de caractères, puis en comparant leurs points de code Unicode. Cela signifie que dans certaines situations, le tri pourrait mal se passer en réalité :

```js
let numArray = [3, 10, 4, 21, 5, 9, 2, 6, 5, 3, 5].sort();
console.log(numArray); // Sortie : [10,2,21,3,3,4,5,5,5,6,9]
```

You remarquerez que **10** arrive avant **2**, **21** avant **3**, et ainsi de suite.

## Les lacunes de la méthode sort() de JavaScript et comment trier avec précision

Passons maintenant en revue certaines lacunes de la méthode `sort()` et comment les résoudre. Comprendre ces lacunes et comment les résoudre vous donnera un avantage et vous aidera à éviter certains bugs.

### Comment trier des nombres avec précision en JavaScript

La méthode `sort()` de JavaScript compare les éléments du tableau en les convertissant en chaînes de caractères, puis en comparant leurs points de code Unicode.

Cela peut conduire à des résultats inattendus lors du tri de tableaux de nombres, comme on le voit dans l'exemple où 10, 5 et 80 sont triés comme 10, 5, 80 au lieu de 5, 10, 80.

```js
let numArr = [10, 5, 80].sort();
console.log(numArr); // Sortie : [10, 5, 80]
```

Pour pallier cette lacune, vous pouvez fournir une fonction de comparaison qui définit l'ordre de tri souhaité.

Pour trier un tableau de nombres, la fonction de comparaison doit soustraire le deuxième nombre du premier nombre.

Cela donnera un nombre négatif si le premier nombre est plus petit que le second, un nombre positif si le premier nombre est plus grand que le second, et 0 si les deux nombres sont égaux.

Voici un exemple :

```js
let numArr = [10, 5, 80];

numArr.sort((a, b) => a - b);
console.log(numArr); // Sortie : [5, 10, 80]
```

En fournissant une fonction de comparaison qui définit l'ordre de tri correct, nous pouvons nous assurer que le tableau est trié avec précision.

Vous pouvez également trier les éléments de votre tableau par ordre décroissant en soustrayant le premier nombre du second :

```js
let numArr = [10, 5, 80];

numArr.sort((a, b) => b - a);
console.log(numArr); // Sortie : [80, 10, 5]
```

### Comment trier des chaînes de caractères avec précision

La méthode `sort()` peut également être utilisée pour trier un tableau de chaînes de caractères, mais l'ordre de tri peut ne pas être précis dans tous les cas.

Par exemple, les chaînes "a", "A" et "b" seraient triées comme "A", "a", "b" au lieu de "a", "A", "b", car le "A" majuscule a un point de code Unicode inférieur au "a" minuscule.

```js
let stringsArr = ["a", "A", "b"].sort();
console.log(stringsArr); // Sortie : ["A","a","b"]
```

Pour pallier cette lacune, vous pouvez fournir une fonction de comparaison qui définit l'ordre de tri souhaité.

Pour trier un tableau de chaînes dans un ordre alphabétique insensible à la casse, la fonction de comparaison doit convertir les deux chaînes en minuscules à l'aide de la méthode `toLowerCase()` et ensuite les comparer à l'aide des opérateurs `<` et `>`.

Voici un exemple :

```js
let stringsArr = ["a", "A", "b"];

stringsArr.sort((a, b) => a.toLowerCase() < b.toLowerCase() ? -1 : 1);
console.log(stringsArr); // Sortie : ["a", "A", "b"]
```

En fournissant une fonction de comparaison qui définit l'ordre de tri correct, nous pouvons nous assurer que le tableau de chaînes est trié avec précision.

Vous pouvez trier dans l'ordre inverse en alternant les valeurs de `-1` et `1` :

```js
let stringsArr = ["a", "A", "b"];

stringsArr.sort((a, b) => a.toLowerCase() < b.toLowerCase() ? 1 : -1);
console.log(stringsArr); // Sortie : ["b", "A", "a"]
```

### Comment éviter de modifier le tableau original lors du tri

L'une des lacunes de la méthode `sort()` est qu'elle trie les éléments sur place, ce qui signifie qu'elle modifie le tableau d'origine.

Cela peut être problématique si vous devez préserver l'ordre d'origine des éléments ou si vous devez trier un grand tableau plusieurs fois.

Pour éviter de modifier le tableau d'origine, vous pouvez faire une copie du tableau à l'aide de la méthode `slice()` avant de le trier.

Voici un exemple :

```js
let originalArray = [2, 1, 3];
let sortedArray = originalArray.slice().sort((a, b) => a - b);

console.log(originalArray); // Sortie : [2, 1, 3]
console.log(sortedArray); // Sortie : [1, 2, 3]
```

## Conclusion 🎉

Dans cet article, vous avez appris à trier un tableau en JavaScript, les diverses lacunes de la méthode `sort()` et comment les corriger.

Il y a plus à savoir sur la méthode sort et ce qu'elle peut faire, mais comprendre que la fonction de comparaison existe vous aidera à gérer de nombreuses difficultés.

Bon codage !

Vous pouvez accéder à plus de 195 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.