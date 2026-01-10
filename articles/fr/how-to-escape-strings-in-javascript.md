---
title: Comment échapper une chaîne de caractères en JavaScript – Exemple d'échappement
  JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-02-02T19:05:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-escape-strings-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/cover-template.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment échapper une chaîne de caractères en JavaScript – Exemple d'échappement
  JS
seo_desc: 'In JavaScript, a string is a data type representing a sequence of characters
  that may consist of letters, numbers, symbols, words, or sentences.

  Strings are used to represent text-based data and are mostly defined using either
  single quotes ('') or do...'
---

En JavaScript, une chaîne de caractères est un type de données représentant une séquence de caractères qui peut être composée de lettres, de nombres, de symboles, de mots ou de phrases.

Les chaînes de caractères sont utilisées pour représenter des données textuelles et sont principalement définies en utilisant soit des guillemets simples (`'`), soit des guillemets doubles (`"`).

```js
let name1 = 'John Doe';
let name2 = "John Doe";
```

Étant donné que ces guillemets sont utilisés pour délimiter les chaînes de caractères, vous devez être prudent lorsque vous utilisez des apostrophes et des guillemets dans les chaînes.

Lorsque vous essayez de les utiliser à l'intérieur d'une chaîne, cela mettra fin à la chaîne, et JavaScript tentera d'analyser le reste de la chaîne prévue comme du code. Cela générera une erreur.

```js
let quote = "He said, "I learned from freeCodeCamp!"";
```

Cela générera une erreur, comme le montre ci-dessous :

```js
Uncaught SyntaxError: Unexpected identifier 'I'
```

En JavaScript, si vous devez inclure des guillemets ou des apostrophes dans une chaîne de caractères, il existe trois principales façons de corriger l'erreur. Ces méthodes sont :

* En utilisant la syntaxe de chaîne opposée

* En utilisant un caractère d'échappement

* En utilisant des littéraux de gabarit

## Comment utiliser la syntaxe de chaîne opposée pour échapper une chaîne en JavaScript

En JavaScript, vous pouvez utiliser la syntaxe de chaîne opposée `'` ou `"` pour échapper une chaîne. Pour ce faire, vous devez envelopper la chaîne dans la syntaxe opposée à celle que vous essayez d'échapper.

```js
let quote = 'He said, "I learned from freeCodeCamp!"';
console.log(quote); // He said, "I learned from freeCodeCamp!"

let apostrophe = "It's a beautiful day";
console.log(apostrophe); // It's a beautiful day
```

Cela signifie que si vous utilisez des guillemets doubles pour envelopper votre chaîne, vous pouvez utiliser une apostrophe à l'intérieur de la chaîne. De même, si vous enveloppez votre chaîne avec des guillemets simples, vous pouvez utiliser des guillemets doubles à l'intérieur de la chaîne.

Mais il y a des limitations à cela, car que faire si vous devez utiliser un guillemet et une apostrophe dans la même chaîne ? Vous pouvez alors utiliser un caractère d'échappement (`\`).

## Comment utiliser le caractère d'échappement (`\`) pour échapper une chaîne en JavaScript

En JavaScript, vous pouvez échapper une chaîne en utilisant le caractère `\` (barre oblique inverse). La barre oblique inverse indique que le caractère suivant doit être traité comme un caractère littéral plutôt que comme un caractère spécial ou un délimiteur de chaîne.

Voici un exemple d'échappement d'une chaîne en JavaScript :

```js
let quote = "He said, \"I learned from freeCodeCamp!\"";
console.log(quote); // He said, "I learned from freeCodeCamp!"

let apostrophe = 'It\'s a beautiful day';
console.log(apostrophe); // It's a beautiful day
```

## Comment utiliser les littéraux de gabarit pour échapper une chaîne en JavaScript

En JavaScript, vous pouvez également utiliser des littéraux de gabarit (également connus sous le nom de chaînes de gabarit) pour échapper une chaîne.

Les littéraux de gabarit sont des littéraux de chaîne qui vous permettent d'intégrer des expressions à l'intérieur d'une chaîne, en utilisant la syntaxe `${expression}`.

```js
let quote = `He said, "I learned from freeCodeCamp!"`;
console.log(quote); // He said, "I learned from freeCodeCamp!"
```

Avec les littéraux de gabarit, vous n'avez pas besoin d'utiliser des barres obliques inverses pour échapper les caractères. Au lieu de cela, vous enveloppez simplement la chaîne avec des backticks ( )

## Conclusion

Dans cet article, vous avez appris comment échapper une chaîne de caractères en JavaScript. Cela vous aidera à éviter d'utiliser des caractères Unicode pour ajouter des guillemets et des apostrophes dans les chaînes.

Vous pouvez accéder à plus de 180 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.