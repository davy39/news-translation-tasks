---
title: Comment utiliser la méthode at() des tableaux JavaScript
subtitle: ''
author: Natalie Pina
co_authors: []
series: null
date: '2023-08-21T14:41:05.000Z'
originalURL: https://freecodecamp.org/news/javascript-at-method
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Grey-Minimalist-Tips-Blog-Banner.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser la méthode at() des tableaux JavaScript
seo_desc: 'One of JavaScript''s most exciting new features is the at() method. The
  at() method is a new addition to the Array prototype in JavaScript. You can use
  this method to access elements in an array using a numeric index.

  The at() method takes an integer ...'
---

L'une des nouvelles fonctionnalités les plus passionnantes de JavaScript est la méthode `at()`. La méthode `at()` est une nouvelle addition au prototype `Array` en JavaScript. Vous pouvez utiliser cette méthode pour accéder aux éléments d'un tableau en utilisant un index numérique.

La méthode `at()` prend une valeur entière et retourne l'élément à cet index. La valeur peut être un entier positif ou négatif. Les entiers négatifs comptent à partir du dernier élément du tableau.

## Syntaxe de la méthode `at()`

Voici la syntaxe – elle est assez simple :

```javascript
arr.at(index)

```

## Comment fonctionne la méthode `at()` de JavaScript

Comment cette méthode fonctionne-t-elle, pourriez-vous demander ? La méthode `at()` prend un seul paramètre, qui est l'index de l'élément à accéder.

L'index doit être une valeur entière positive ou négative. Les entiers négatifs compteront à rebours à partir du dernier élément du tableau, et les entiers positifs compteront à partir du début du tableau.

 Par exemple, étant donné le tableau suivant :

```javascript
const rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'purple'];

```

Pour accéder au premier élément du tableau (rappelons que les tableaux en JS sont indexés à zéro), vous pouvez faire ceci :

```javascript
const color = rainbow.at(0); // red

```

Pour accéder au dernier élément du tableau, vous feriez ceci :

```javascript
const lastColor = rainbow.at(-1); // purple

```

Dans l'exemple ci-dessus, l'index `-1` est traité comme un index relatif à la fin du tableau, et pointera vers le dernier élément du tableau.

### Qu'est-ce que l'indexation relative ?

L'indexation relative est une technique utilisée pour indexer des éléments ou des valeurs par leur position en relation avec un point de référence ou un autre élément.

Plutôt que de s'appuyer sur des indices numériques fixes qui attribuent des positions spécifiques aux éléments, l'indexation relative vous permet d'indiquer des positions basées sur la relation avec d'autres éléments, s'adaptant dynamiquement. L'indexation relative est devenue une solution beaucoup plus facile avec `at()`.

### Exemple de cas d'utilisation

Les tableaux sont utilisés pour stocker des collections de données. Les développeurs ont souvent besoin de récupérer des éléments spécifiques d'un tableau pour utiliser leurs valeurs afin d'afficher des informations. Lors du traitement des données, vous pouvez vouloir modifier, transformer ou effectuer des calculs sur des points de données spécifiques dans un tableau.

Considérons un exemple concret où la méthode `at()` pourrait être utile. Imaginez que vous construisez une application météo qui affiche les prévisions pour la semaine à venir. Vous avez un tableau contenant les températures hebdomadaires :

```javascript
const temperatureForecast = [70, 71, 75, 80, 77, 88, 90];

```

Le premier élément du tableau est la température pour aujourd'hui et il est suivi des 6 prochains jours. Vous voulez afficher la température à venir pour demain. Pour accéder à la température de demain, vous voulez obtenir la valeur à l'index 1.

Voici comment vous pouvez utiliser `at()` pour accéder à la température :

```javascript
const temperatureForecast = [70, 71, 75, 80, 77, 88, 90];

const tomorrowsTemperature = temperatureForecast.at(1);

console.log(`The high for tomorrow is ${tomorrowsTemperature}°F.`); 
// The high for tomorrow is 71°F.
```

Lors de la présentation de données aux utilisateurs, il existe de nombreux scénarios où vous souhaitez afficher l'élément le plus récent ou le plus récent d'un tableau. Cela est courant dans les fils d'actualité, les applications de chat ou les journaux d'activité.

### Essayez-le :

Je vous encourage à jouer avec cette méthode pour apprendre en faisant. J'ai créé un terrain de jeu CodePen. Changez les valeurs dans le tableau et les valeurs passées dans `at()`, essayez de voir si vous pouvez deviner le résultat :

%[https://codepen.io/nataliepina/pen/RwedQNj?editors=1010]

## Problèmes que la méthode `at()` résout

Avant son introduction, pour accéder aux éléments de tableau par leur index, vous deviez effectuer des calculs manuels.

Il a été une pratique courante d'utiliser la propriété `length` d'un tableau pour calculer le nombre d'éléments dans le tableau, puis de soustraire de la longueur pour cibler un index. Par exemple, pour accéder au dernier élément d'un tableau, vous pouvez utiliser `array[array.length - 1]`.

### `slice()` vs la propriété `length` vs `at()`

Examinons une comparaison entre trois méthodes différentes qui nous permettent d'accéder aux éléments d'un tableau. Remarquez la quantité de code requise pour chacune, la lisibilité du code et la complexité entre les méthodes.

```javascript
const animals = ["panda", "zebra", "penguin"];

// avec slice()
const animal = animals.slice(-2, -1); // 'zebra'

// avec la propriété length
const animal = animals[animals.length - 2]; // 'zebra'

// avec at()
const animal = animals.at(-2); // 'zebra'
```

En utilisant la méthode `at()`, l'accès au dernier élément d'un tableau est aussi simple que `array.at(-1)`. Cette méthode offre une solution bien plus lisible et intuitive.

La lisibilité est améliorée avec la syntaxe de la méthode `at()`, car son intention est bien décrite avec le mot "at". Par exemple, `array.at(0)` peut être lu comme "le tableau **at** l'index zéro".

En revanche, une alternative comme `array.slice(0, 1)` manque de la même clarté. Une meilleure lisibilité réduit la charge cognitive et rend le code plus facile à comprendre d'un coup d'œil.

De plus, l'adoption de la méthode `at()` s'aligne bien avec d'autres méthodes de tableau comme `map()` et `filter()`, favorisant un style de codage cohésif et orienté vers la programmation fonctionnelle dans tout votre code.

La méthode `at()` atténue les risques en fournissant un moyen simple d'accéder aux éléments. Avec `at()`, il est moins probable de faire des erreurs d'indexation ou des erreurs de décalage d'un qui surviennent couramment lors de la manipulation d'index numériques. La syntaxe claire de la méthode réduit la probabilité d'introduire des bugs liés à la manipulation d'index.

La méthode `at()` effectue automatiquement une vérification des limites, ce qui signifie qu'elle garantit que l'index est dans la plage valide pour le tableau. La méthode `length` n'offre aucune vérification des limites. Avec la vérification des limites, si un index hors limite est fourni, la méthode retournera `undefined` sans lever d'erreur.

Effectuer des vérifications manuelles avec `length` tend à être sujet aux erreurs et plus difficile à déboguer. Bien que l'indexation manuelle vous permette d'accéder aux éléments, elle nécessite une séquence de code plus longue pour le faire.

Le besoin de calculer les index, d'effectuer des soustractions et de gérer les cas particuliers ajoute des caractères supplémentaires et de la complexité à votre code. Cette approche peut introduire des erreurs subtiles qui peuvent être difficiles à identifier et à corriger.

Pour accéder à un seul élément, l'utilisation de `.slice()` introduit une complexité inutile. La méthode nécessite de spécifier à la fois les index de début et de fin, ce qui est peu pratique lorsque vous n'avez besoin que d'un seul élément.

L'utilisation de `array.slice()` est idéale pour les scénarios où vous souhaitez récupérer une plage d'éléments. Si vous n'avez besoin que d'un seul élément, l'utilisation directe de l'indexation de tableau est plus efficace.

Bien que `slice()` et `length` aient leurs utilisations, la méthode `at()` offre une solution convaincante pour l'accès aux éléments de tableau.

## Support des navigateurs pour `at()`

Étant donné que cette méthode est nouvelle, elle n'est pas encore prise en charge par tous les navigateurs. Actuellement, elle est prise en charge par tous les principaux navigateurs comme Chrome, FireFox et Safari. Elle n'est pas encore prise en charge par Edge ou Internet Explorer (r.i.p).

Gardez à l'esprit que vous pouvez utiliser un [polyfill](https://developer.mozilla.org/en-US/docs/Glossary/Polyfill) pour gérer les navigateurs sans cette capacité. Grâce au support des principaux navigateurs déjà, il ne devrait pas s'écouler longtemps avant que le support complet soit disponible.

## Résumé

L'ajout de `at()` est un atout précieux pour l'ensemble des méthodes de tableau de JavaScript. Il permet un moyen simple et direct d'accéder aux éléments de tableau en utilisant une valeur d'index.

Avec `at()`, vous pouvez fournir une valeur entière positive ou négative pour récupérer un élément dans un tableau, en comptant vers l'avant ou vers l'arrière respectivement. Il est pris en charge par tous les principaux navigateurs tels que Chrome, Firefox et Safari.

Essayez cette nouvelle méthode et partagez vos réflexions. Bon codage !