---
title: Exemple JavaScript String.Split() avec RegEx
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-26T18:31:08.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-split-example-with-regex
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/string-split-with-regex.png
tags:
- name: JavaScript
  slug: javascript
- name: Regex
  slug: regex
seo_title: Exemple JavaScript String.Split() avec RegEx
seo_desc: 'By Dillion Megida

  In JavaScript, you use RegEx to match patterns in characters. Combining this with
  the .split() string method gives you more splitting powers.

  The string constructor has many useful methods, one of which is the split() method.
  You us...'
---

Par Dillion Megida

En JavaScript, vous utilisez RegEx pour faire correspondre des motifs dans les caractères. Combiner cela avec la méthode de chaîne `.split()` vous donne plus de puissance pour diviser.

Le constructeur de chaîne possède [de nombreuses méthodes utiles](https://dillionmegida.com/p/10-useful-string-methods-in-javascript/), dont la méthode `split()`. Vous utilisez cette méthode pour diviser une chaîne en un tableau de sous-chaînes en utilisant un point de rupture. 

Voici comment elle est souvent utilisée :

```js
const string = "How is everything going?"

const breakpoint = " "

const splitted = string.split(breakpoint);

// [ 'How', 'is', 'everything', 'going?' ]
```

En utilisant un espace (" ") comme point de rupture, la méthode `split` divise la chaîne à ces points de rupture.

Le point de rupture ici est un caractère fixe. Que faire si vous souhaitez diviser en fonction d'un motif ? Comme un caractère numérique ou un symbole-espace ? Alors vous pouvez utiliser la méthode `split` avec regex pour y parvenir.

## Comment utiliser RegEx avec .split en JavaScript

La méthode `split` accepte un argument – un point de rupture. Ce point de rupture détermine les points auxquels la division doit se produire. Ce point de rupture peut être une chaîne ou un motif regex.

Voici un exemple utilisant un motif regex :

```js
const string = "How is $everything g$oing?"

const breakpoint = /\$e|\$o/

const splitted = string.split(breakpoint)

// [ 'How is ', 'verything g', 'ing?' ]
```

Le motif regex correspond au signe dollar suivi de la lettre "e" (`$e`) ou au signe dollar suivi de la lettre o (`$o`). 

La méthode split utilise les caractères qui correspondent à ce motif comme point de rupture, et comme vous pouvez le voir, le "$e" dans "$everything" et le "$o" dans "g$oing" ont servi de point de rupture pour diviser la chaîne en sous-chaînes.

Vous n'avez pas besoin d'appliquer le drapeau global `g` dans le regex, car la méthode split recherche déjà toutes les occurrences du motif regex comme point de rupture.

## Conclusion

Vous n'êtes pas obligé d'utiliser uniquement des chaînes littérales pour diviser des chaînes en un tableau avec la méthode `split`. Vous pouvez utiliser des regex comme points de rupture qui correspondent à plus de caractères pour diviser une chaîne.

La méthode `replace` dans les chaînes prend également en charge les motifs regex. Consultez cet article : [JavaScript String.Replace() Example with RegEx](https://www.freecodecamp.org/news/javascript-string-replace-example-with-regex/)