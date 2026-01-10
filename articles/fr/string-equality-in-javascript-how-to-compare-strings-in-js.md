---
title: Égalité des chaînes en JavaScript – Comment comparer des chaînes en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-12-22T18:57:16.000Z'
originalURL: https://freecodecamp.org/news/string-equality-in-javascript-how-to-compare-strings-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/cover-template--3-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Égalité des chaînes en JavaScript – Comment comparer des chaînes en JS
seo_desc: 'When writing code or building a solution, you might need to compare two
  strings to see if they are the same before proceeding with an operation.

  For example, when a user signs in, you''ll want to compare the username the provide
  to the one in your dat...'
---

Lorsque vous écrivez du code ou construisez une solution, vous pourriez avoir besoin de comparer deux chaînes pour voir si elles sont identiques avant de poursuivre une opération.

Par exemple, lorsqu'un utilisateur se connecte, vous voudrez comparer le nom d'utilisateur qu'il fournit avec celui de votre base de données pour voir s'ils correspondent.

En JavaScript, vous pouvez comparer des chaînes en fonction de leur valeur, de leur longueur, de la casse des caractères, et bien plus encore. Dans cet article, vous apprendrez comment comparer des chaînes en JavaScript.

## Comment comparer des chaînes en JavaScript avec l'opérateur d'égalité stricte

L'égalité stricte, ou triple égalité (`===`) comme le suggère son symbole, est une comparaison plus détaillée que l'égalité lâche (`==`). Elle ne vérifie pas seulement si les valeurs sont les mêmes, mais vérifie également les opérandes :

```js
let a = 12;
let b = '12';

// Égalité lâche
console.log(a == b); // true
// Égalité stricte
console.log(a === b); // false
```

L'opérateur strict est le mieux adapté pour comparer des chaînes en JavaScript car il vérifie que les opérandes et les valeurs sont identiques, puis retourne un résultat booléen.

```js
let string1 = "freeCodeCamp";
let string2 = "codeCamp";

console.log(string1 === string2); // false
```

Vous pouvez également comparer directement une chaîne à une variable et une chaîne à une chaîne si vous le souhaitez :

```js
let string1 = "freeCodeCamp";

console.log(string1 === "codeCamp"); // false
console.log(string1 === "freeCodeCamp"); // true
console.log("codeCamp" === "freeCodeCamp"); // false
```

### Comment effectuer une comparaison insensible à la casse

Lors de la comparaison avec l'opérateur d'égalité stricte, il est essentiel de savoir que cette comparaison est sensible à la casse. Cela signifie que `freeCodeCamp` n'est pas égal à `FreeCodeCamp` car la première lettre f est en minuscule pour l'un et en majuscule pour l'autre.

```js
console.log("freeCodeCamp" === "FreeCodeCamp"); // false
```

Pour éviter des situations comme celle-ci, vous pouvez effectuer des comparaisons insensibles à la casse. Cela signifie que vous convertissez les chaînes que vous comparez à la même casse :

```js
let string1 = "freeCodeCamp";
let string2 = "FreeCodeCamp";

console.log(string1.toLowerCase() == string2.toLowerCase()); // true
console.log(string1.toUpperCase() == string2.toUpperCase()); // true
```

## Comment comparer des chaînes en JavaScript avec la propriété `.length`

En JavaScript, lorsque vous attachez la propriété `.length` à une variable, elle retourne la longueur de la chaîne :

```js
let string1 = "freeCodeCamp";

console.log(string1.length); // 12
```

Cela signifie que vous pouvez utiliser la propriété length pour comparer avec soit l'égalité (lâche ou stricte), supérieur à (>), ou inférieur à (<) pour vérifier si les deux longueurs sont les mêmes ou si l'une est plus grande que l'autre.

```js
let string1 = "freeCodeCamp";
let string2 = "codeCamp";

console.log(string1.length > string2.length); // true
console.log(string1.length < string2.length); // false
console.log(string1.length == string2.length); // false
console.log(string1.length === string2.length); // false
```

## Comment comparer des chaînes en JavaScript avec la méthode `localeCompare()`

La méthode `localeCompare()` peut comparer des chaînes en fonction des paramètres de locale actuels du navigateur.

Cette méthode peut être assez délicate, mais il est important de savoir que cette méthode compare chaque caractère des deux chaînes et retourne un nombre qui peut être "-1", "1", ou "0".

* -1 : La chaîne de gauche vient alphabétiquement avant la chaîne de droite.
  
* 1 : La chaîne de gauche vient alphabétiquement après la chaîne de droite.
  
* 0 : Cela signifie que les deux chaînes sont égales.
  

```js
let string1 = "freeCodeCamp";
let string2 = "codeCamp";

console.log(string1.localeCompare(string2)); // 1
```

Cela retourne "1" car "f" vient après "c" dans la première comparaison de caractères.

```js
let string1 = "freeCodeCamp";
let string2 = "codeCamp";

console.log(string2.localeCompare(string1)); // -1
```

Cela retourne maintenant "-1" car "c", qui est le premier caractère de `string2` à gauche, vient avant "f". Lorsque les deux chaînes sont égales, elle retourne "0" indépendamment de leurs positions :

```js
let string1 = "freeCodeCamp";
let string2 = "freeCodeCamp";

console.log(string2.localeCompare(string1)); // 0
```

### Comment effectuer une comparaison insensible à la casse

Il est également important de souligner que lorsque vous utilisez la méthode `localeCompare()`, elle est sensible à la casse. Cela signifie qu'elle retournera soit "1" soit "-1" en fonction de la position, même si les deux chaînes sont identiques mais avec une casse différente :

```js
let string1 = "freeCodeCamp";
let string2 = "FreeCodeCamp";

console.log(string2.localeCompare(string1)); // 1
```

Vous pouvez corriger cela en introduisant des options et une locale à la méthode `localeCompare()`. Cette méthode vous permet de définir une locale et également des options que vous pouvez utiliser pour convertir les deux chaînes à des cas similaires, afin d'effectuer une comparaison insensible à la casse.

```js
let string1 = "freeCodeCamp";
let string2 = "FreeCodeCamp";

console.log(string2.localeCompare(string1, "en", { sensitivity: "base" })); // 0
```

Vous pouvez lire plus sur la méthode [localeCompare()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare) dans la documentation MDN.

## Conclusion

Dans cet article, vous avez appris comment comparer des chaînes en JavaScript en utilisant les opérateurs d'égalité et la méthode `localeCompare()`.

N'hésitez pas à utiliser vos méthodes préférées, mais vous devriez principalement utiliser `localeCompare()` lorsque la comparaison implique une locale et certaines comparaisons spécifiques qui impliquent une locale.

Amusez-vous bien à coder !