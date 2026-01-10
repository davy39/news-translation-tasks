---
title: JavaScript split() une chaîne – Méthode JS pour convertir une chaîne en tableau
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-01-10T21:24:30.000Z'
originalURL: https://freecodecamp.org/news/javascript-split-a-string-string-to-array-js-method
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/pankaj-patel-1IW4HQuauSU-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: JavaScript split() une chaîne – Méthode JS pour convertir une chaîne en
  tableau
seo_desc: "If you need to split up a string into an array of substrings, then you\
  \ can use the JavaScript split() method. \nIn this article, I will go over the JavaScript\
  \ split() method and provide code examples. \nBasic Syntax of the split() method\n\
  Here is the sy..."
---

Si vous devez diviser une chaîne en un tableau de sous-chaînes, vous pouvez utiliser la méthode `split()` de JavaScript. 

Dans cet article, je vais passer en revue la méthode `split()` de JavaScript et fournir des exemples de code. 

## Syntaxe de base de la méthode split()

Voici la syntaxe de la méthode `split()` de JavaScript.

```js
str.split(séparateur-optionnel, limite-optionnelle)
```

Le séparateur optionnel est un type de motif qui indique à l'ordinateur où chaque division doit se produire. 

Le paramètre limite optionnel est un nombre positif qui indique à l'ordinateur combien de sous-chaînes doivent se trouver dans la valeur de tableau retournée.

## Exemples de code de la méthode split() de JavaScript

Dans ce premier exemple, j'ai la chaîne `"I love freeCodeCamp"`. Si j'utilisais la méthode `split()` sans le séparateur, la valeur retournée serait un tableau contenant la chaîne entière.

```js
const str = 'I love freeCodeCamp';

str.split();
// la valeur retournée est ["I love freeCodeCamp"]
```

### Exemples utilisant le paramètre séparateur optionnel

Si je voulais modifier cela pour que la chaîne soit divisée en caractères individuels, je devrais ajouter un séparateur. Le séparateur serait une chaîne vide.

```js
const str = 'I love freeCodeCamp';

str.split('');
// valeur retournée ["I", " ", "l", "o", "v", "e", " ", "f", "r", "e", "e", "C", "o", "d", "e", "C", "a", "m", "p"]
```

Remarquez comment les espaces sont considérés comme des caractères dans la valeur retournée.

Si je voulais modifier cela pour que la chaîne soit divisée en mots individuels, le séparateur serait une chaîne vide avec un espace.

```js
const str = 'I love freeCodeCamp';

str.split(' ');
// valeur retournée ["I", "love", "freeCodeCamp"]
```

### Exemples utilisant le paramètre limite optionnel

Dans cet exemple, je vais utiliser le paramètre limite pour retourner un tableau contenant uniquement le premier mot de la phrase `"I love freeCodeCamp"`.

```js
const str = 'I love freeCodeCamp';

str.split(' ',1);
// valeur retournée ["I"]
```

Si je change la limite pour qu'elle soit zéro, la valeur retournée serait un tableau vide.

```js
const str = 'I love freeCodeCamp';

str.split(' ',0);
// valeur retournée []
```

## Devriez-vous utiliser la méthode split() pour inverser une chaîne ?

L'exercice d'inversion d'une chaîne est un défi de codage très populaire. Une méthode courante pour le résoudre implique l'utilisation de la méthode `split()`. 

Dans cet exemple, nous avons la chaîne "freeCodeCamp". Si nous voulions inverser le mot, nous pourrions enchaîner les méthodes `split()`, `reverse()` et `join()` pour retourner la nouvelle chaîne inversée.

```js
const str = 'freeCodeCamp';

str.split('').reverse().join('');
// valeur retournée "pmaCedoCeerf"
```

La partie `.split('')` divise la chaîne en un tableau de caractères.

La partie `.reverse()` inverse le tableau de caractères en place.

La partie `.join('')` joint les caractères du tableau et retourne une nouvelle chaîne.

Cette approche semble fonctionner correctement pour cet exemple. Mais il existe des cas particuliers où cela ne fonctionnerait pas.

Examinons l'exemple fourni dans la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split).

Si nous essayions d'inverser la chaîne "mañana mañana", cela pourrait conduire à des résultats inattendus.

```js
const str = 'mañana mañana'
const reversedStr = str.split('').reverse().join('')

console.log(reversedStr)
// la valeur retournée serait "anañam anañam"
```

Remarquez comment le tilde(~) est placé sur la lettre `"a"` au lieu de `"n"` dans le mot inversé. Cela se produit parce que notre chaîne contient ce qu'on appelle un graphème. 

Un groupe de graphèmes est une série de symboles combinés pour produire un seul caractère que les humains peuvent lire à l'écran. Lorsque nous essayons d'inverser la chaîne en utilisant ces types de caractères, l'ordinateur peut mal interpréter ces caractères et produire une version incorrecte de la chaîne inversée.

Si nous isolons simplement la méthode split, vous pouvez voir comment l'ordinateur divise chaque caractère individuel.

```js
const str = 'mañana mañana'

console.log(str.split(''))
//["m", "a", "ñ", "a", "n", "a", " ", "m", "a", "ñ", "a", "n", "a"]
```

Il existe des [packages](https://github.com/mathiasbynens/esrever) que vous pouvez utiliser dans vos projets pour corriger ce problème et inverser correctement la chaîne si vous utilisez ces caractères spéciaux. 

## Conclusion

La méthode `split()` de JavaScript est utilisée pour diviser une chaîne en un tableau de sous-chaînes.

Voici la syntaxe de la méthode `split()` de JavaScript.

```js
str.split(séparateur-optionnel, limite-optionnelle)
```

Le séparateur optionnel est un type de motif qui indique à l'ordinateur où chaque division doit se produire. 

Le paramètre limite optionnel est un nombre positif qui indique à l'ordinateur combien de sous-chaînes doivent se trouver dans la valeur de tableau retournée.

Vous pourriez utiliser la méthode split pour inverser une chaîne, mais il existe des cas particuliers où cela ne fonctionnerait pas. Si votre chaîne contient des groupes de graphèmes, le résultat pourrait produire un mot inversé incorrectement. 

Vous pourriez également choisir d'utiliser la syntaxe de décomposition pour diviser la chaîne avant de l'inverser.

```js
const str = 'mañana mañana'
console.log([...str].reverse().join(""))
```

J'espère que vous avez apprécié cet article et je vous souhaite bonne chance dans votre apprentissage de JavaScript.