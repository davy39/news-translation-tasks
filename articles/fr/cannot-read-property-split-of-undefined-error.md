---
title: Impossible de lire la propriété 'split' de Undefined
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:16:00.000Z'
originalURL: https://freecodecamp.org/news/cannot-read-property-split-of-undefined-error
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aa5740569d1a4ca26db.jpg
tags:
- name: error
  slug: error
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: Impossible de lire la propriété 'split' de Undefined
seo_desc: 'If you''ve ever used JavaScript''s split method, there''s a good chance
  that you''ve encountered the following error: TypeError: Cannot read property ''split''
  of undefined.

  There are a few reasons why you would receive this error. Most likely it''s just
  a ...'
---

Si vous avez déjà utilisé la méthode `split` de JavaScript, il est probable que vous ayez rencontré l'erreur suivante : `TypeError: Cannot read property 'split' of undefined`.

Il existe plusieurs raisons pour lesquelles vous pourriez recevoir cette erreur. La plus probable est simplement une incompréhension de base du fonctionnement de `split` et de la manière d'itérer à travers les tableaux.

Par exemple, si vous essayez de soumettre le code suivant pour le défi [Trouver le mot le plus long dans une chaîne](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/find-the-longest-word-in-a-string) :

```js
function findLongestWord(str) { 
  for(let i = 0; i < str.length; i++) {
    const array = str.split(" ");
    array[i].split("");
  }
}

findLongestWord("The quick brown fox jumped over the lazy dog");
```

celui-ci générera l'erreur `TypeError: Cannot read property 'split' of undefined`.

### La méthode `split`

Lorsque `split` est appelée sur une chaîne, elle divise la chaîne en sous-chaînes en fonction du séparateur passé en argument. Si une chaîne vide est passée en argument, `split` traite chaque caractère comme une sous-chaîne. Elle retourne ensuite un tableau contenant les sous-chaînes :

```js
const testStr1 = "Test test 1 2";
const testStr2 = "cupcake pancake";
const testStr3 = "First,Second,Third";

testStr1.split(" "); // [ 'Test', 'test', '1', '2' ]
testStr2.split(""); // [ 'c', 'u', 'p', 'c', 'a', 'k', 'e', ' ', 'p', 'a', 'n', 'c', 'a', 'k', 'e' ]
testStr3.split(","); // [ 'First', 'Second', 'Third' ]

```

Consultez [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split) pour plus de détails sur `split`.

### Le problème expliqué avec des exemples

Savoir ce que la méthode `split` retourne et combien de sous-chaînes vous pouvez attendre est la clé pour résoudre [ce défi](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/find-the-longest-word-in-a-string).

Examinons à nouveau le code ci-dessus et voyons pourquoi il ne fonctionne pas comme prévu :

```js
function findLongestWord(str) { 
  for(let i = 0; i < str.length; i++) {
    const array = str.split(" ");
    array[i].split("");
  }
}

findLongestWord("The quick brown fox jumped over the lazy dog");

```

Diviser `str` en un tableau comme ceci (`const array = str.split(" ");`) fonctionne comme prévu et retourne `[ 'The',   'quick',   'brown',   'fox',   'jumped',   'over',   'the',   'lazy',   'dog' ]`.

Mais regardez de plus près la boucle `for`. Au lieu d'utiliser la longueur de `array` comme condition pour itérer `i`, `str.length` est utilisé à la place.

`str` est "The quick brown fox jumped over the lazy dog", et si vous affichez `str.length` dans la console, vous obtiendrez 44.

La dernière instruction dans le corps de la boucle `for` est ce qui cause l'erreur : `array[i].split("");`. La longueur de `array` est 9, donc `i` dépasserait rapidement la longueur maximale de `array` :

```js
function findLongestWord(str) { 
  for(let i = 0; i < str.length; i++) {
    const array = str.split(" ");
    console.log(array[i]);
    // array[0]: "The"
    // array[1]: "quick"
    // array[2]: "brown"
    // ...
    // array[9]: "dog"
    // array[10]: undefined
    // array[11]: undefined
  }
}

findLongestWord("The quick brown fox jumped over the lazy dog");

```

Appeler `array[i].split("");` pour diviser chaque chaîne en sous-chaînes de caractères est une approche valide, mais cela générera `TypeError: Cannot read property 'split' of undefined` lorsqu'il est passé `undefined`.

### Comment résoudre Trouver le mot le plus long dans une chaîne avec `split`

Passons rapidement en revue quelques étapes de pseudo-code pour résoudre ce problème :

1. Diviser `str` en un tableau de mots individuels
2. Créer une variable pour suivre la longueur du mot le plus long
3. Itérer à travers le tableau de mots et comparer la longueur de chaque mot à la variable mentionnée ci-dessus
4. Si la longueur du mot actuel est supérieure à celle stockée dans la variable, remplacer cette valeur par la longueur du mot actuel
5. Une fois la longueur de chaque mot comparée avec la variable de longueur maximale du mot, retourner ce nombre depuis la fonction

Tout d'abord, diviser `str` en un tableau de mots individuels :

```js
function findLongestWordLength(str) {
  const array = str.split(" ");
}
```

Créer une variable pour garder une trace de la longueur du mot le plus long et l'initialiser à zéro :

```js
function findLongestWordLength(str) {
  const array = str.split(" ");
  let maxWordLength = 0;
}
```

Maintenant que la valeur de `array` est `['The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']`, vous pouvez utiliser `array.length` dans votre boucle `for` :

```js
function findLongestWordLength(str) {
  const array = str.split(" ");
  let maxWordLength = 0;
  
  for (let i = 0; i < array.length; i++) {
    
  }
}
```

Itérer à travers le tableau de mots et vérifier la longueur de chaque mot. N'oubliez pas que les chaînes ont également une méthode `length` que vous pouvez appeler pour obtenir facilement la longueur d'une chaîne :

```js
function findLongestWordLength(str) {
  const array = str.split(" ");
  let maxLength = 0;
  
  for (let i = 0; i < array.length; i++) {
    array[i].length;
  }
}
```

Utiliser une instruction `if` pour vérifier si la longueur du mot actuel (`array[i].length`) est supérieure à `maxLength`. Si c'est le cas, remplacer la valeur de `maxLength` par `array[i].length` :

```js
function findLongestWordLength(str) {
  const array = str.split(" ");
  let maxLength = 0;
  
  for (let i = 0; i < array.length; i++) {
    if (array[i].length > maxLength) {
      maxLength = array[i].length;
    }
  }
}
```

Enfin, retourner `maxLength` à la fin de la fonction, après la boucle `for` :

```js
function findLongestWordLength(str) {
  const array = str.split(" ");
  let maxLength = 0;
  
  for (let i = 0; i < array.length; i++) {
    if (array[i].length > maxLength) {
      maxLength = array[i].length;
    }
  }
    
  return maxLength;
}
```