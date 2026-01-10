---
title: JavaScript Remplacer – Comment remplacer une chaîne ou une sous-chaîne en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-02-28T02:24:34.000Z'
originalURL: https://freecodecamp.org/news/javascript-replace-how-to-replace-a-string-or-substring-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/cover-template--3-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript Remplacer – Comment remplacer une chaîne ou une sous-chaîne
  en JS
seo_desc: 'When working with JavaScript, you might need to replace a string or substring
  with a new one.

  For example, you might want to replace a certain string (like "color” — American
  English) or substring in a larger text or document with a different string ...'
---

Lorsque vous travaillez avec JavaScript, vous pourriez avoir besoin de remplacer une chaîne ou une sous-chaîne par une nouvelle.

Par exemple, vous pourriez vouloir remplacer une certaine chaîne (comme "color" — anglais américain) ou une sous-chaîne dans un texte ou un document plus grand par une autre chaîne ("colour" — anglais britannique). Vous pourriez également vouloir remplacer certains caractères ou symboles d'une chaîne pour vous assurer que votre programme fonctionnera.

Dans cet article, vous apprendrez à utiliser la méthode `replace()` de JavaScript pour remplacer une chaîne ou une sous-chaîne.

## Comment remplacer une chaîne ou une sous-chaîne avec la méthode `replace()`

En JavaScript, vous pouvez utiliser la méthode `replace()` pour remplacer une chaîne ou une sous-chaîne dans une chaîne. La méthode `replace()` retourne une nouvelle chaîne avec le remplacement. La méthode `replace()` prend deux arguments :

1. Le premier argument est la chaîne ou l'expression régulière à remplacer.
   
2. Le second argument est la chaîne qui remplacera la chaîne ou l'expression régulière correspondante.
   

```js
// Syntaxe
string.replace(searchValue, replaceValue)
```

Dans la syntaxe ci-dessus, `string` est la chaîne sur laquelle vous souhaitez effectuer le remplacement. Le paramètre `searchValue` est soit une chaîne, soit une expression régulière que vous souhaitez rechercher dans la `string`. Le paramètre `replaceValue` est la chaîne qui remplacera le `searchValue`.

**Note :** Seule la première occurrence sera remplacée. Si vous souhaitez remplacer toutes les occurrences, vous devrez utiliser la méthode `replaceAll()`.

## Exemples de la méthode `replace()` pour les chaînes JavaScript

Supposons que vous avez une chaîne qui utilise "color", qui est de l'anglais américain, et que vous souhaitez changer "color" en "colour", la forme britannique. Voici un exemple de la façon dont vous pouvez faire cela :

```js
let originalString = "The color of the sky changes throughout the day.";

let newString = originalString.replace("color", "colour");

console.log(newString);
```

Cela remplacera "color" dans la chaîne et retournera une nouvelle chaîne assignée à la variable `newString`.

```bash
"The colour of the sky changes throughout the day."
```

Dans une situation où vous avez plus d'une occurrence d'une telle sous-chaîne, vous pouvez utiliser la méthode replaceAll :

```js
let originalString = "The color of the sky changes throughout the day, and sometimes the color of the clouds creates a beautiful contrast. The color of a flower can indicate its species, and the color of clothing can affect someone's mood.";

let newString = originalString.replaceAll("color", "colour");

console.log(newString);
```

Cela remplacera toutes les occurrences de "color" dans la chaîne et retournera une nouvelle chaîne assignée à la variable `newString`.

```bash
"The colour of the sky changes throughout the day, and sometimes the colour of the clouds creates a beautiful contrast. The colour of a flower can indicate its species, and the colour of clothing can affect someone's mood."
```

## Comment remplacer plusieurs chaînes et sous-chaînes avec la méthode `replace()`

Parfois, vous pourriez vouloir changer plus d'une chaîne ou sous-chaîne dans une variable de chaîne. Par exemple, dans le texte ci-dessous, vous pourriez vouloir changer "color" en "colour" et "JS" en "JavaScript".

```js
let originalString = "Using JS, you can change the color of a webpage's background, text, and elements."
```

Vous pouvez le faire en enchaînant autant de méthodes `replace()` que nécessaire :

```js
let originalString = "Using JS, you can change the color of a webpage's background, text, and elements.";

let newString = originalString
    .replace("color", "colour")
    .replace("JS", "JavaScript");

console.log(newString);
```

Cela retournera une nouvelle chaîne avec les deux occurrences remplacées :

```js
"Using JavaScript, you can change the colour of a webpage's background, text, and elements."
```

De plus, vous pourriez vouloir remplacer plusieurs chaînes ou sous-chaînes par une seule chaîne. Par exemple, vous pourriez vouloir remplacer "quick", "fox" et "brown" par une seule chaîne — "hello" :

```js
let originalString = "The quick brown fox jumps over the lazy dog.";
let newString = originalString.replace(/quick|brown|fox/g, "hello");

console.log(newString); // Résultat : "The hello hello hello jumps over the lazy dog."
```

## Comment utiliser `replace()` avec des expressions régulières

En JavaScript, vous pouvez utiliser la méthode `replace()` avec des expressions régulières pour remplacer des chaînes et des sous-chaînes avec plus de flexibilité et de puissance. Par exemple :

```js
let originalString = "Today is a sunny day. I love sunny days!";
let newString = originalString.replace(/sunny/g, "cloudy");

console.log(newString); // Résultat : "Today is a cloudy day. I love cloudy days!"
```

Dans cet exemple, l'expression régulière `/sunny/g` correspond à toutes les occurrences de la sous-chaîne "sunny" dans `originalString`. Le drapeau `g` spécifie que toutes les correspondances doivent être remplacées. La chaîne de remplacement "cloudy" remplace toutes les sous-chaînes correspondantes, ce qui donne la `newString` "Today is a cloudy day. I love cloudy days!"

Les expressions régulières peuvent également être utilisées pour correspondre à des motifs ou à des groupes de caractères. Par exemple :

```js
let originalString = "My phone number is (123) 456-7890";
let newString = originalString.replace(/\D/g, "");

console.log(newString); // Résultat : "1234567890"
```

Dans l'exemple ci-dessus, l'expression régulière `/\D/g` correspond à tous les caractères non numériques dans `originalString`. La classe de caractères `\D` correspond à tout caractère qui n'est pas un chiffre. Le drapeau `g` spécifie que toutes les correspondances doivent être remplacées.

## Remplacement sensible à la casse avec des expressions régulières

Les expressions régulières vous permettent d'effectuer des opérations de recherche et de remplacement avancées. Par exemple, en utilisant le drapeau `i`, vous pouvez remplacer uniquement les chaînes et sous-chaînes dont la casse correspond parfaitement :

```js
const originalString = "I love JavaScript and javascript loves me";
const newString = originalString.replace(/JavaScript/i, "Python");

console.log(newString); // Résultat : "I love Python and javascript loves me"
```

Dans cet exemple, la méthode `replace()` remplace la première occurrence du mot "JavaScript" par "Python" dans la variable `originalString`. Le drapeau `/i` est utilisé pour effectuer une recherche insensible à la casse.

## Conclusion

Dans cet article, vous avez appris comment remplacer une chaîne ou une sous-chaîne en JavaScript avec la méthode `replace()` et les différentes situations dans lesquelles la méthode `replace()` peut fonctionner.

Espérons que cet article vous a donné une meilleure compréhension de l'utilisation des méthodes `replace()` et `replaceAll()` en JavaScript.

Amusez-vous bien en codant !

Vous pouvez accéder à plus de 188 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.