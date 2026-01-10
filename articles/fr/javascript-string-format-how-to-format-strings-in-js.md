---
title: Formatage de chaînes JavaScript – Formater des chaînes en JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-11T18:38:41.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-format-how-to-format-strings-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/js-string-format.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Formatage de chaînes JavaScript – Formater des chaînes en JS
seo_desc: 'By Dillion Megida

  JavaScript has many string methods you can use to format strings. In this article,
  I''ll show you some of the most commonly used methods.

  How to Use the toLowerCase() String Method

  As the name implies, you use the toLowerCase() strin...'
---

Par Dillion Megida

JavaScript dispose de nombreuses méthodes de chaîne que vous pouvez utiliser pour formater des chaînes. Dans cet article, je vais vous montrer certaines des méthodes les plus couramment utilisées.

## Comment utiliser la méthode de chaîne `toLowerCase()`

Comme son nom l'indique, vous utilisez la méthode de chaîne `toLowerCase()` pour convertir les chaînes en leur version minuscule.

Cette méthode ne modifie pas la chaîne originale. Elle prend la chaîne originale et retourne une nouvelle chaîne, qui est la version en minuscules.

Voici un exemple :

```js
const string = "HeLLo woRld"

const lowercased = string.toLowerCase()

console.log(string)
// HeLLo woRld

console.log(lowercased)
// hello world
```

Comme vous pouvez le voir, la nouvelle chaîne a toutes ses lettres en minuscules.

## Comment utiliser la méthode de chaîne `toUpperCase()`

Similaire à la première méthode, `toUpperCase` est une méthode de chaîne que vous utilisez pour convertir les chaînes en leur version majuscule.

Elle n'affecte pas non plus la chaîne originale.

Voici un exemple :

```js
const string = "HeLLo woRld"

const uppercased = string.toUpperCase()

console.log(string)
// HeLLo woRld

console.log(uppercased)
// HELLO WORLD
```

En utilisant la chaîne originale, elle retourne une nouvelle chaîne, qui est la version en majuscules.

## Comment utiliser la méthode de chaîne `replace()`

Vous utilisez la méthode de chaîne `replace` pour remplacer une section d'une chaîne par une sous-chaîne. Ainsi, vous pourrez formater la chaîne afin de la modifier.

Voici un exemple de fonctionnement de la méthode `replace` :

```js
const string = "Hello world"

const modified = string.replace("world", "developers")

console.log(string)
// Hello world

console.log(modified)
// Hello developers
```

La méthode `replace`, comme on peut le voir ci-dessus, remplace la sous-chaîne "world" par "developers". Elle n'affecte pas non plus la chaîne originale.

Vous pouvez également utiliser une regex à la place d'une chaîne comme remplaçant :

```js
const string = "Hello world"

const modified = string.replace(/o/g, "--")

console.log(string)
// Hello world

console.log(modified)
// Hell-- w--rld
```

En utilisant un motif regex pour correspondre au caractère "o" globalement, vous pouvez voir la chaîne modifiée contenant des doubles tirets à la place du "o" dans la chaîne.

## Comment utiliser la méthode de chaîne `trim()`

La méthode `trim` modifie les chaînes en supprimant les espaces blancs au début et à la fin d'une chaîne.

Elle ne modifie pas la chaîne originale. Au lieu de cela, elle retourne une nouvelle chaîne avec les espaces blancs supprimés.

Voici un exemple :

```js
const string = "  H ell  o world  "

const modified = string.trim()

console.log(string)
//   H ell  o world 

console.log(modified)
// H ell  o world
```

Vous pouvez voir que seuls les espaces au début et à la fin sont supprimés, et non les espaces entre les lettres.

Les espaces blancs incluent les espaces, les tabulations, les sauts de ligne, etc.

## Conclusion

Il existe plusieurs autres façons de formater ou de modifier des chaînes en JavaScript. Dans cet article, j'ai partagé quatre des méthodes les plus courantes que vous pouvez utiliser : `toUpperCase`, `toLowerCase`, `replace` et `trim`.

Ces méthodes n'affectent pas la chaîne originale mais retournent une nouvelle chaîne formatée d'une manière spécifique.

Vous pouvez en apprendre plus sur [les méthodes de chaîne utiles en JavaScript ici](https://dillionmegida.com/p/10-useful-string-methods-in-javascript/).