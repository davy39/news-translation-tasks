---
title: JavaScript Uppercase – Comment mettre une chaîne en majuscules en JS avec .toUpperCase
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-02-28T19:25:42.000Z'
originalURL: https://freecodecamp.org/news/javascript-uppercase-how-to-capitalize-a-string-in-js-with-touppercase
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/toUpperCase.png
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript Uppercase – Comment mettre une chaîne en majuscules en JS avec
  .toUpperCase
seo_desc: 'While working with strings in JavaScript, you can perform different operations
  on them.

  The operations you might perform on strings include capitalization, conversion to
  lowercase, adding symbols within words, and many more.

  In this article, I will s...'
---

Lorsqu'on travaille avec des chaînes de caractères en JavaScript, on peut effectuer différentes opérations sur celles-ci.

Les opérations que vous pourriez effectuer sur les chaînes incluent la mise en majuscules, la conversion en minuscules, l'ajout de symboles au sein des mots, et bien plus encore.

Dans cet article, je vais vous montrer comment convertir une chaîne de caractères en lettres majuscules avec la méthode de chaîne `.toUpperCase()`.

## Syntaxe de base de la méthode `.toUpperCase()`

Pour utiliser la méthode `.toUpperCase()`, affectez la chaîne que vous souhaitez convertir en majuscules à une variable, puis ajoutez `.toUpperCase()` devant celle-ci.

## Comment mettre une chaîne en majuscules avec .toUpperCase

Comme déjà mentionné, vous pouvez affecter une chaîne à une variable et utiliser ensuite la méthode `.toUpperCase()` pour la mettre en majuscules.

```js
const name = "freeCodeCamp";
const uppercase = name.toUpperCase();
console.log(uppercase);

// Résultat : FREECODECAMP
```

Vous pouvez également écrire une fonction et retourner `.toUpperCase()` dans celle-ci, de sorte qu'un paramètre spécifié sera mis en majuscules lorsque la fonction est appelée.

```js
function changeToUpperCase(founder) {
  return founder.toUpperCase();
}

// appel de la fonction
const result = changeToUpperCase("Quincy Larson");

// affichage du résultat dans la console
console.log(result);

// Résultat : QUINCY LARSON
```

**Dans le script ci-dessus :**
- J'ai défini une fonction nommée `changeToUpperCase` avec un paramètre `founder`
- avec l'instruction return à l'intérieur de la fonction, j'ai indiqué à la fonction que ce que je veux qu'elle fasse est de convertir en lettres majuscules tout paramètre que je spécifie lorsque je l'appelle
- J'ai ensuite assigné l'appel de la fonction - `changeToUpperCase` à une variable nommée `result`
- avec l'aide de la variable, j'ai pu afficher le résultat de la fonction dans la console

## Conclusion

Vous pouvez utiliser la méthode `.toUpperCase()`, également connue sous le nom de `String.prototype.toUpperCase()`, lorsque vous devez mettre des chaînes de caractères en majuscules dans vos projets JavaScript.

Si vous trouvez cet article utile, veuillez le partager avec vos amis et votre famille.