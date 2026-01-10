---
title: Deux façons de confirmer la fin d'une chaîne en JavaScript
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2017-02-06T13:18:27.000Z'
originalURL: https://freecodecamp.org/news/two-ways-to-confirm-the-ending-of-a-string-in-javascript-62b4677034ac
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bvdSF4jzFsH7foKJYEoNaA.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Deux façons de confirmer la fin d'une chaîne en JavaScript
seo_desc: 'In this article, I’ll explain how to solve freeCodeCamp’s “Confirm the
  Ending” challenge. This involves checking whether a string ends with specific sequence
  of characters.

  There are the two approaches I’ll cover:


  using the substr() method

  using end...'
---

Dans cet article, je vais expliquer comment résoudre le défi "[Confirm the Ending](https://www.freecodecamp.com/challenges/confirm-the-ending)" de freeCodeCamp. Cela implique de vérifier si une chaîne se termine par une séquence spécifique de caractères.

Voici les deux approches que je vais aborder :

1. utiliser la méthode substr()
2. utiliser la méthode endsWith()

### Description du défi algorithmique

> _Vérifiez si une chaîne (premier argument, `str`) se termine par la chaîne cible donnée (deuxième argument, `target`)._  
>   
> _Ce défi peut être résolu avec la méthode `.endsWith()`, qui a été introduite dans ES2015. Mais pour les besoins de ce défi, nous aimerions que vous utilisiez l'une des méthodes de sous-chaîne JavaScript à la place._

```js
function confirmEnding(string, target) {
  return string;
}
confirmEnding("Bastian", "n");
```

### Cas de test fournis

```js
confirmEnding("Bastian", "n") devrait retourner true.

confirmEnding("Connor", "n") devrait retourner false.

confirmEnding("Walking on water and developing software from a specification are easy if both are frozen", "specification") devrait retourner false.

largestOfFour([[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]]) devrait retourner [9, 35, 97, 1000000].

confirmEnding("He has to give me a new name", "name") devrait retourner true.
confirmEnding("Open sesame", "same") devrait retourner true.

confirmEnding("Open sesame", "pen") devrait retourner false.

confirmEnding("If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing", "mountain") devrait retourner false.

N'utilisez pas la méthode intégrée .endsWith() pour résoudre le défi.
```

### Approche #1 : Confirmer la fin d'une chaîne avec les fonctions intégrées — avec substr()

Pour cette solution, vous utiliserez la méthode String.prototype.substr() :

* La méthode `**substr()**` retourne les caractères d'une chaîne commençant à l'emplacement spécifié jusqu'au nombre de caractères spécifié.

Pourquoi utilisez-vous `string.substr(-target.length)` ?

Si la longueur de target est négative, la méthode substr() commencera le comptage à partir de la fin de la chaîne, ce qui est ce que vous voulez dans ce défi de code.

Vous ne voulez pas utiliser `string.substr(-1)` pour obtenir le dernier élément de la chaîne, car si la cible est plus longue qu'une lettre :

```
confirmEnding("Open sesame", "same")
```

… la cible ne sera pas retournée du tout.

Ainsi, ici, `string.substr(-target.length)` obtiendra le dernier index de la chaîne 'Bastian' qui est 'n'.

Ensuite, vous vérifiez si `string.substr(-target.length)` est égal à la cible (vrai ou faux).

```js

function confirmEnding(string, target) {
  // Étape 1. Utilisez la méthode substr
  if (string.substr(-target.length) === target) {
  
  // Que représente "if (string.substr(-target.length) === target)" ?
  // La chaîne est 'Bastian' et la cible est 'n' 
  // target.length = 1 donc -target.length = -1
  // if ('Bastian'.substr(-1) === 'n')
  // if ('n' === 'n')
  
  // Étape 2. Retournez un booléen (vrai ou faux)
    return true;
  } else {
    return false;
  }
}

confirmEnding('Bastian', 'n');
```

Sans commentaires :

```js

function confirmEnding(string, target) {
  if (string.substr(-target.length) === target) {
    return true;
  } else {
    return false;
  }
}
confirmEnding('Bastian', 'n');
```

Vous pouvez utiliser un **opérateur ternaire** comme raccourci pour l'instruction if :

```
(string.substr(-target.length) === target) ? true : false;
```

Cela peut être lu comme :

```
if (string.substr(-target.length) === target) {
    return true;
} else {
    return false;
}
```

Vous retournez ensuite l'opérateur ternaire dans votre fonction :

```js

function confirmEnding(string, target) {
  return (string.substr(-target.length) === target) ? true : false;
}
confirmEnding('Bastian', 'n');
```

Vous pouvez également refactoriser votre code pour le rendre plus concis en retournant simplement la condition :

```js
function confirmEnding(string, target) {
  return string.substr(-target.length) === target;
}
confirmEnding('Bastian', 'n');
```

### Approche #2 : Confirmer la fin d'une chaîne avec les fonctions intégrées — avec endsWith()

Pour cette solution, vous utiliserez la méthode String.prototype.endsWith() :

* La méthode `endsWith()` détermine si une chaîne se termine par les caractères d'une autre chaîne, retournant `true` ou `false` selon le cas. Cette méthode est sensible à la casse.

```js
function confirmEnding(string, target) {
  // Nous retournons la méthode avec la cible comme paramètre
  // Le résultat sera un booléen (vrai/faux)
  return string.endsWith(target); // 'Bastian'.endsWith('n')
}
confirmEnding('Bastian', 'n');
```

J'espère que vous avez trouvé cela utile. Cela fait partie de ma série d'articles "How to Solve FCC Algorithms" sur les défis algorithmiques de freeCodeCamp, où je propose plusieurs solutions et explique étape par étape ce qui se passe sous le capot.

[**Trois façons de répéter une chaîne en JavaScript**  
_Dans cet article, je vais expliquer comment résoudre le défi "Repeat a string repeat a string" de freeCodeCamp. Cela implique…_](https://www.freecodecamp.org/news/three-ways-to-repeat-a-string-in-javascript-2a9053b93a2d/)

[**Trois façons d'inverser une chaîne en JavaScript**  
_Cet article est basé sur le script algorithmique de base de Free Code Camp « Inverser une chaîne »_](https://www.freecodecamp.org/news/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb/)

[**Trois façons de factoriser un nombre en JavaScript**  
_Cet article est basé sur le script algorithmique de base de Free Code Camp « Factoriser un nombre »_](https://www.freecodecamp.org/news/how-to-factorialize-a-number-in-javascript-9263c89a4b38/)

[**Deux façons de vérifier les palindromes en JavaScript**  
_Cet article est basé sur le script algorithmique de base de Free Code Camp « Vérifier les palindromes »._](https://www.freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7/)

[**Trois façons de trouver le mot le plus long dans une chaîne en JavaScript**  
_Cet article est basé sur le script algorithmique de base de Free Code Camp « Trouver le mot le plus long dans une chaîne »._](https://www.freecodecamp.org/news/three-ways-to-find-the-longest-word-in-a-string-in-javascript-a2fb04c9757c/)

[**Trois façons de mettre en majuscule une phrase en JavaScript**  
_Cet article est basé sur le script algorithmique de base de Free Code Camp « Mettre en majuscule une phrase »._](https://www.freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27/)

Si vous avez votre propre solution ou des suggestions, partagez-les ci-dessous dans les commentaires.

Ou vous pouvez me suivre sur [**Medium**](https://medium.com/@sonya.moisset)**, [Twitter](https://twitter.com/SonyaMoisset), [Github](https://github.com/SonyaMoisset)** et [**LinkedIn**](https://www.linkedin.com/in/sonyamoisset), juste après avoir cliqué sur le cœur vert ci-dessous ;-)

#RestezCurieux, #ContinuezÀCoder & #FaitesQueÇaArrive !

### Ressources supplémentaires

* [Méthode substr() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substr)
* [Méthode endsWith() — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith)
* [Opérateur ternaire — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)