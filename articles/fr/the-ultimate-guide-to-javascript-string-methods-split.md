---
title: Le guide ultime des méthodes de chaîne JavaScript - Split
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-10T18:06:00.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-javascript-string-methods-split
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f74740569d1a4ca42ac.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Le guide ultime des méthodes de chaîne JavaScript - Split
seo_desc: 'The split() method separates an original string into an array of substrings,
  based on a separator string that you pass as input. The original string is not altered
  by split().

  Syntax

  const splitStr = str.split(separator, limit);



  separator - a strin...'
---

La méthode `split()` sépare une chaîne de caractères originale en un tableau de sous-chaînes, en fonction d'une chaîne `separator` que vous passez en entrée. La chaîne de caractères originale n'est pas altérée par `split()`.

## Syntaxe

```js
const splitStr = str.split(separator, limit);
```

* `separator` - une chaîne indiquant où chaque séparation doit se produire
* `limit` - un nombre pour la quantité de séparations à trouver

## Exemples :

```js
const str = "Bonjour. Je suis une chaîne. Vous pouvez me séparer.";
const splitStr = str.split("."); // Va séparer str à chaque caractère de point

console.log(splitStr); // [ "Bonjour", " Je suis une chaîne", " Vous pouvez me séparer", "" ]
console.log(str); // "Bonjour. Je suis une chaîne. Vous pouvez me séparer."
```

Puisque nous avons utilisé le point (`.`) comme chaîne `separator`, les chaînes dans le tableau de sortie ne contiennent pas le point  les chaînes séparées en sortie n'incluent pas le `separator` d'entrée lui-même.

Vous pouvez opérer sur des chaînes directement, sans les stocker comme variables :

```js
"Bonjour... Je suis une autre chaîne... continuez à apprendre!".split("..."); // [ "Bonjour", " Je suis une autre chaîne", " continuez à apprendre!" ]
```

De plus, le séparateur de chaîne n'a pas besoin d'être un seul caractère, il peut être n'importe quelle combinaison de caractères :

```js
const names = "Kratos- Atreus- Freya- Hela- Thor- Odin";
const namesArr = names.split("- "); // Remarquez que le séparateur est un tiret et un espace
const firstThreeNames = names.split("- ", 3);

console.log(namesArr) // [ "Kratos", "Atreus", "Freya", "Hela", "Thor", "Odin" ]
console.log(firstThreeNames); // [ "Kratos", "Atreus", "Freya" ]
```

## Utilisations courantes de `split`

La méthode `split()` est très utile une fois que vous maîtrisez les bases. Voici quelques cas d'utilisation courants pour `split()` :

### Créer un tableau de mots à partir d'une phrase :

```js
const sentence = "Mesdames et messieurs nous flottons dans l'espace.";
const words = sentence.split(" "); // Séparer la phrase à chaque espace entre les mots

console.log(words); // [ "Mesdames", "et", "messieurs", "nous", "flottons", "dans", "l'espace." ]
```

### Créer un tableau de lettres dans un mot :

```js
const word = "espace";
const letters = word.split("");

console.log(letters); // [ "e", "s", "p", "a", "c", "e" ]
```

### Inverser les lettres dans un mot :

Parce que la méthode `split()` retourne un tableau, elle peut être combinée avec des méthodes de tableau comme `reverse()` et `join()` :

```js
const word = "flotte";
const reversedWord = word.split("").reverse().join("");

console.log(reversedWord); // "ettolf"
```

C'est tout ce que vous devez savoir pour `split()` les chaînes avec les meilleurs !