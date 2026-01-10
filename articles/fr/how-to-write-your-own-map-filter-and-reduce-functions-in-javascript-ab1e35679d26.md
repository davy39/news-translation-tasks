---
title: Comment écrire vos propres fonctions map, filter et reduce en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-21T00:05:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-your-own-map-filter-and-reduce-functions-in-javascript-ab1e35679d26
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5PyeGXp9J3PpUTHCv9drnQ.jpeg
tags:
- name: ES6
  slug: es6
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment écrire vos propres fonctions map, filter et reduce en JavaScript
seo_desc: 'By Hemand Nair

  A sneak peek into functional programming and higher order functions in Javascript.


  _Photo by [Unsplash](https://unsplash.com/photos/pgSkeh0yl8o?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target=...'
---

Par Hemand Nair

#### Un aperçu de la programmation fonctionnelle et des fonctions d'ordre supérieur en JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/8rPml1LfKKppm-gvbSSoKziPC-RHoF0CsVKg)
_Photo par [Unsplash](https://unsplash.com/photos/pgSkeh0yl8o?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Christopher Robin Ebbinghaus</a> sur <a href="https://unsplash.com/search/photos/javascript?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Chaque fois que j'entends parler de programmation fonctionnelle, la première chose qui me vient à l'esprit est les fonctions d'ordre supérieur. Pour ceux qui ne connaissent pas les fonctions d'ordre supérieur, voici ce que dit Wikipédia :

Une [**fonction d'ordre supérieur**](https://en.wikipedia.org/wiki/Higher-order_function) est une fonction qui fait au moins l'une des choses suivantes :

* Prend une ou plusieurs fonctions comme arguments,
* Retourne une fonction comme résultat.

Les fonctions d'ordre supérieur peuvent être mieux décrites par les fonctions map, filter et reduce. JavaScript possède par défaut sa propre implémentation de ces fonctions. Aujourd'hui, nous allons écrire nos propres fonctions map, filter et reduce.

**Note : Gardez à l'esprit que ces implémentations des méthodes map, filter et reduce peuvent ne pas refléter les implémentations natives de leurs homologues JavaScript.**

#### Map

D'après [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) :

> La méthode `**map()**` crée un nouveau tableau avec les résultats de l'appel d'une fonction fournie sur chaque élément du tableau appelant.

Cela semble assez simple. Maintenant, voyons le `map()` de JavaScript en action !

```
let arr = [1, 2, 3, 4, 5];
```

```
// passer une fonction à map
const squareArr = arr.map(num => num ** 2);
```

```
console.log(squareArr); // affiche [1, 4, 9, 16, 25]
```

Alors, que s'est-il passé ? Nous avons écrit une fonction qui retourne le carré d'un nombre et avons passé cette fonction comme argument à notre `map()`. Voyons étape par étape comment créer notre propre fonction map.

1. Créer un tableau vide `mapArr`.
2. Parcourir les éléments du tableau.
3. Appeler la fonction `mapFunc` avec l'élément actuel comme argument.
4. Pousser le résultat de la fonction `mapFunc` dans le tableau `mapArr`.
5. Retourner le tableau `mapArr` après avoir parcouru tous les éléments.

Maintenant, écrivons notre implémentation de `map()`

```
// map prend un tableau et une fonction comme argument
function map(arr, mapFunc) {    const mapArr = []; // tableau vide        // boucle à travers le tableau    for(let i=0;i<arr.length;i++) {        const result = mapFunc(arr[i], i, arr);        mapArr.push(result);    }    return mapArr;}
```

Maintenant, si vous appelez le nouveau `map()` dans le code de l'exemple précédent,

```
const squareArr2 = map(arr, num => num ** 2);
```

```
console.log(squareArr2); // affiche [1, 4, 9, 16, 25]
```

Plutôt cool, n'est-ce pas ? Passons à `filter()` ensuite.

#### **Filter**

D'après [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) :

> La méthode `**filter()**` crée un nouveau tableau avec tous les éléments qui passent le test implémenté par la fonction fournie.

Voyons un exemple :

```
let arr = [1, 2, 3, 4, 5];
```

```
// passer une fonction à filter
const oddArr = arr.filter(num => num % 2 === 0);
```

```
console.log(oddArr); // affiche [2, 4]
```

La fonction filter a pris une fonction qui retournera `true` si un nombre est pair. La méthode `filter()` « filtre » le tableau d'entrée en fonction de si l'élément est vrai ou faux. Passons étape par étape comment fonctionne `filter()`.

1. Créer un tableau vide `filterArr`.
2. Parcourir les éléments du tableau.
3. Appeler la fonction `filterFunc` avec l'élément actuel comme argument.
4. Si le résultat est vrai, pousser l'élément dans le tableau `filterArr`.
5. Retourner le tableau `filterArr` après avoir parcouru tous les éléments.

Il est temps d'écrire notre propre `filter()`

```
// filter prend un tableau et une fonction comme argument
function filter(arr, filterFunc) {    const filterArr = []; // tableau vide        // boucle à travers le tableau    for(let i=0;i<arr.length;i++) {        const result = filterFunc(arr[i], i, arr);        // pousser l'élément actuel si le résultat est vrai        if(result)             filterArr.push(arr[i]);     }    return filterArr;}
```

Voyons si notre nouveau `filter()` fonctionne avec l'exemple précédent :

```
const oddArr2 = filter(arr, num => num % 2 === 0);
```

```
console.log(oddArr2); // affiche [2, 4]
```

Propre ! J'ai gardé le meilleur et le plus difficile pour la fin. Passons à `reduce()` ensuite.

#### **Reduce**

D'après [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce) :

> La méthode `**reduce()**` exécute une fonction **reducer** (que vous fournissez) sur chaque membre du tableau, résultant en une seule valeur de sortie.

Cela a du sens ? Non ? Voici un exemple pour vous aider à comprendre :

```
let arr = [1, 2, 3, 4];
const sumReducer = (accumulator, currentValue) => accumulator + currentValue;
```

```
// 1 + 2 + 3 + 4
const sum = arr.reduce(sumReducer);
console.log(sum);
// affiche 10
```

```
// 5 + 1 + 2 + 3 + 4
const sum2 = arr.reduce(sumReducer, 5);
console.log(sum2);
// affiche 15
```

Commencez-vous à avoir une idée ? Clarifions. Avant de creuser trop profondément dans la méthode `reduce()`, vous pourriez avoir besoin de vous familiariser avec la fonction reducer.

Si vous avez utilisé [**redux**](https://redux.js.org) dans le passé, vous pourriez avoir une idée de ce qu'est une fonction reducer. Dans l'exemple ci-dessus, la fonction reducer est écrite comme la somme entre l'accumulateur et la valeur actuelle. Lorsque vous passez la fonction reducer à la méthode `reduce()`, elle parcourra chaque nombre dans le tableau et l'ajoutera à l'accumulateur (0 au début), qui devient lui-même le nouvel accumulateur pour l'itération suivante. Cela continue jusqu'à la fin du tableau et retourne l'accumulateur comme résultat.

Si je devais afficher la valeur de l'accumulateur à chaque étape pour l'exemple ci-dessus, ce serait comme ceci :

* Avant le début de l'itération, `accumulator = 0`
* 1ère itération, `accumulator += 1; // accumulator = 1`
* 2ème itération, `accumulator += 2; // accumulator = 3`
* 3ème itération, `accumulator += 3; // accumulator = 6`
* 4ème itération, `accumulator += 4; // accumulator = 10`

La valeur retournée par votre fonction **reducer** est assignée à l'accumulateur, dont la valeur est mémorisée à travers chaque itération du tableau. Elle devient finalement la valeur résultante unique et finale.

Si vous êtes encore bloqué à un moment donné, essayez d'écrire quelques opérations avec la méthode `reduce()` intégrée. Dès que vous vous sentez prêt, passez aux étapes suivantes pour implémenter votre `reduce()` personnalisé :

1. Initialiser la variable `accumulator` avec 0 ou la valeur `initialValue` de l'argument `reduce()`.
2. Parcourir les éléments du tableau.
3. Appeler la fonction `reducer` avec l'`accumulator` et l'élément actuel comme arguments.
4. Retourner `accumulator` après avoir parcouru tous les éléments.

Très bien, il est temps de coder.

```
// reducer prend un tableau, reducer() et initialValue comme argument
function reduce(arr, reducer, initialValue) {    let accumulator = initialValue === undefined ? 0 : initialValue        // boucle à travers le tableau    for(let i=0;i<arr.length;i++)        accumulator = reducer(accumulator, arr[i], i, arr);    return accumulator;}
```

Eh bien, c'était plus facile que prévu. Voyons si cela fonctionne.

```
const sum = reduce(arr, sumReducer);
```

```
console.log(sum); // affiche 10
```

```
const sum2 = reduce(arr, sumReducer, 5);
```

```
console.log(sum2);// affiche 15
```

Fonctionne à merveille !

**C'est tout :)**

Laissez un commentaire ci-dessous si vous avez des questions.