---
title: Boucles For imbriquées en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:19:00.000Z'
originalURL: https://freecodecamp.org/news/nesting-for-loops-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a97740569d1a4ca2681.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
- name: toothbrush
  slug: toothbrush
- name: Tutorial
  slug: tutorial
seo_title: Boucles For imbriquées en JavaScript
seo_desc: 'If you''re having trouble understanding freeCodeCamp''s Nesting For Loops
  challenge, don''t worry. We got your back.

  In this problem you have to complete the multiplyAll() function, and takes a multi-dimensional
  array as an argument. Remember that a mul...'
---

Si vous avez du mal à comprendre le défi [Nesting For Loops](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/nesting-for-loops) de freeCodeCamp, ne vous inquiétez pas. Nous sommes là pour vous aider.

Dans ce problème, vous devez compléter la fonction `multiplyAll()`, qui prend un tableau multidimensionnel comme argument. Rappelez-vous qu'un tableau multidimensionnel, parfois appelé tableau 2D, est simplement un tableau de tableaux, par exemple, `[[1,2], [3,4], [5,6]]`.

Dans l'éditeur à droite, `multiplyAll()` est définie comme suit :

```js
function multiplyAll(arr) {
  var product = 1;
  // Only change code below this line

  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);

```

Vous devez compléter la fonction afin qu'elle multiplie la variable `product` par chaque nombre dans les sous-tableaux du paramètre `arr`, qui est un tableau multidimensionnel.

Il existe de nombreuses façons différentes de résoudre ce problème, mais nous nous concentrerons sur la méthode la plus simple en utilisant des boucles `for`.

## Configuration de vos boucles `for`

Parce que `arr` est un tableau multidimensionnel, vous aurez besoin de deux boucles `for` : une pour parcourir chaque sous-tableau, et une autre pour parcourir les éléments de chaque sous-tableau.

### Parcourir les tableaux internes

Pour ce faire, configurez une boucle `for` comme vous l'avez fait dans les défis précédents :

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);

```

Notez que nous utilisons `let` au lieu de `var` pour la boucle et pour déclarer `product`. Dans ce défi, vous ne remarquerez pas de différence entre les deux, mais en général, il est bon de pratiquer l'utilisation de `const` et `let` de ES6 chaque fois que possible. Vous pouvez en lire plus sur les raisons [dans cet article](https://www.freecodecamp.org/news/var-let-and-const-whats-the-difference/).

Maintenant, journalisez chaque sous-tableau dans la console :

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);

```

Parce que vous appelez `multiplyAll()` avec `[[1,2],[3,4],[5,6,7]]` en bas, vous devriez voir ce qui suit :

```
[ 1, 2 ]
[ 3, 4 ]
[ 5, 6, 7 ]
```

### Parcourir les éléments de chaque sous-tableau

Maintenant, vous devez parcourir chaque nombre dans les sous-tableaux que vous venez de journaliser dans la console.

Supprimez `console.log(arr[i]);` et créez une autre boucle `for` à l'intérieur de celle que vous venez d'écrire :

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      
    }
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);

```

Rappelez-vous que, pour la boucle interne, nous devons vérifier la `.length` de `arr[i]` puisque `arr[i]` est l'un des sous-tableaux que nous avons vus précédemment.

Maintenant, journalisez `arr[i][j]` dans la console pour voir chacun des éléments individuels :

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      console.log(arr[i][j]);
    }
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);

```

```
1
2
3
4
5
6
7
```

Enfin, multipliez `product` par chaque élément de chaque sous-tableau :

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      product *= arr[i][j];
    }
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);
```

Si vous journalisez `product` dans la console, vous verrez la bonne réponse pour chaque cas de test :

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      product *= arr[i][j];
    }
  }
  // Only change code above this line
  console.log(product);
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);
```

```
6  // [[1], [2], [3]]
5040  // [[1, 2], [3, 4], [5, 6, 7]]
54  // [[5, 1], [0.2, 4, 0.5], [3, 9]]
```

## Un examen plus approfondi

Si vous n'êtes toujours pas sûr de pourquoi le code ci-dessus fonctionne, ne vous inquiétez pas – vous n'êtes pas seul. Travailler avec des boucles imbriquées est compliqué, et même les développeurs expérimentés peuvent être confus.

Dans des cas comme celui-ci, il peut être utile de journaliser quelque chose de plus détaillé dans la console. Revenez à votre code et journalisez ``Sub-array ${i}: ${arr[i]}`` dans la console juste avant la boucle `for` interne :

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    console.log(`Sub-array ${i}: ${arr[i]}`);
    for (let j = 0; j < arr[i].length; j++) {
      product *= arr[i][j];
    }
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);
```

Dans la boucle `for` externe, chaque itération parcourt les sous-tableaux dans `arr`. Vous devriez voir ceci dans la console :

```
Sub-array 0: 1,2
Sub-array 1: 3,4
Sub-array 2: 5,6,7
```

Notez que nous utilisons [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) ci-dessus. ``Sub-array ${i}: ${arr[i]}`` est la même chose que `'Sub-array ' + i + ': ' + arr[i]`, juste beaucoup plus facile à écrire.

Maintenant, dans la boucle `for` interne, journalisez ``Element ${j}: ${arr[i][j]}`` dans la console :

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    console.log(`Sub-array ${i}: ${arr[i]}`);
    for (let j = 0; j < arr[i].length; j++) {
      console.log(`Element ${j}: ${arr[i][j]}`);
      product *= arr[i][j];
    }
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);
```

La boucle `for` interne parcourt chaque élément de chaque sous-tableau (`arr[i]`), donc vous devriez voir ceci dans la console :

```
Sub-array 0: 1,2
Element 0: 1
Element 1: 2
Sub-array 1: 3,4
Element 0: 3
Element 1: 4
Sub-array 2: 5,6,7
Element 0: 5
Element 1: 6
Element 2: 7
```

La première itération de `i` récupère le premier sous-tableau, `[1, 2]`. Ensuite, la première itération de `j` parcourt chaque élément de ce sous-tableau :

```
// i est 0
arr[0] // [1, 2];

// j est 0
arr[0][0] // 1
// j est 1
arr[0][1] // 2

-----

// i est 1
arr[1] // [3, 4]

// j est 0
arr[1][0] // 3
// j est 1
arr[1][1] // 4

...
```

Cet exemple est assez simple, mais `arr[i][j]` peut encore être difficile à comprendre sans journaliser plusieurs choses dans la console.

Une amélioration rapide que nous pouvons apporter est de déclarer une variable `subArray` dans la boucle `for` externe et de la définir égale à `arr[i]` :

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    const subArray = arr[i];
    for (let j = 0; j < arr[i].length; j++) {
      product *= arr[i][j];
    }
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);

```

Ensuite, apportez quelques ajustements au code pour utiliser la nouvelle variable `subArray` au lieu de `arr[i]` :

```js
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    const subArray = arr[i];
    for (let j = 0; j < subArray.length; j++) {
      product *= subArray[j];
    }
  }
  // Only change code above this line
  return product;
}

multiplyAll([[1,2],[3,4],[5,6,7]]);

```

Cela devrait être tout ce que vous devez savoir sur les tableaux multidimensionnels et les boucles `for` imbriquées. Maintenant, sortez et itérez avec les meilleurs d'entre eux !