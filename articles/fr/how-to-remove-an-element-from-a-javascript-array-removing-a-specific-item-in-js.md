---
title: Comment supprimer un élément d'un tableau JavaScript – Supprimer un élément
  spécifique en JS
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2022-08-31T17:00:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-an-element-from-a-javascript-array-removing-a-specific-item-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/vinicius-amnx-amano-dbOV1qSiL-c-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment supprimer un élément d'un tableau JavaScript – Supprimer un élément
  spécifique en JS
seo_desc: 'You will often need to remove an element from an array in JavaScript, whether
  it''s for a queue data structure, or maybe from your React State.

  In the first half of this article you will learn all the methods that allow you
  to remove an element from a...'
---

Vous aurez souvent besoin de supprimer un élément d'un tableau en JavaScript, que ce soit pour une structure de données de type file d'attente, ou peut-être depuis votre État React.

Dans la première moitié de cet article, vous apprendrez toutes les méthodes qui vous permettent de supprimer un élément d'un tableau sans modifier le tableau original. En fait, c'est ce que vous voudrez faire le plus souvent. Par exemple, si vous ne voulez pas modifier votre État React. Ou si le tableau est utilisé dans d'autres parties de votre code, et le modifier causerait des problèmes inattendus.

Toujours mieux d'éviter les mutations !

Mais, pour être complet, la deuxième moitié de l'article listera les méthodes pour supprimer un élément d'un tableau en place. Ces méthodes modifient effectivement le tableau lui-même.

Vous pouvez trouver ici un résumé pratique du contenu de l'article, si vous souhaitez naviguer vers une section en particulier.

- [Comment supprimer un élément d'un tableau sans modifier le tableau](#heading-comment-supprimer-un-element-dun-tableau-sans-modifier-le-tableau)
    - [Supprimer le premier élément d'un tableau avec `slice`](#heading-supprimer-le-premier-element-dun-tableau-avec-slice)
    - [Supprimer le dernier élément d'un tableau avec `slice`](#heading-supprimer-le-dernier-element-dun-tableau-avec-slice)
    - [Supprimer un élément à n'importe quelle position d'un tableau avec `slice` et `concat`](#heading-supprimer-un-element-a-nimporte-quelle-position-dun-tableau-avec-slice-et-concat)
    - [Supprimer un élément d'une certaine valeur avec `filter`](#heading-supprimer-un-element-dune-certaine-valeur-avec-filter)
    - [Supprimer un élément d'un tableau avec une boucle `for` et `push`](#heading-supprimer-un-element-dun-tableau-avec-une-boucle-for-et-push)
    - [Supprimer le premier élément d'un tableau avec la destructuration et l'opérateur rest](#heading-supprimer-le-premier-element-dun-tableau-avec-la-destructuration-et-loperateur-rest)
- [Comment supprimer un élément d'un tableau en modifiant le tableau](#heading-comment-supprimer-un-element-dun-tableau-en-modifiant-le-tableau)
    - [Supprimer le dernier élément d'un tableau avec `pop`](#heading-supprimer-le-dernier-element-dun-tableau-avec-pop)
    - [Supprimer le premier élément d'un tableau avec `shift`](#heading-supprimer-le-premier-element-dun-tableau-avec-shift)
    - [Supprimer un élément à n'importe quel index avec `splice`](#heading-supprimer-un-element-a-nimporte-quel-index-avec-splice)
- [Conclusion](#heading-conclusion)


## Comment supprimer un élément d'un tableau sans modifier le tableau

Si vous avez un tableau d'entrée, comme un paramètre de fonction, les bonnes pratiques dictent que vous ne devriez pas modifier le tableau. Au lieu de cela, vous devriez en créer un nouveau.

Il existe plusieurs méthodes que vous pouvez utiliser pour supprimer un élément spécifique d'un tableau sans modifier le tableau.

Pour éviter de modifier le tableau, un nouveau tableau sera créé sans l'élément que vous souhaitez supprimer.

Vous pourriez utiliser des méthodes comme :

* `Array.prototype.slice()`
* `Array.prototype.slice()` avec `Array.prototype.concat()`
* `Array.prototype.filter()`
* Une boucle `for` et `Array.prototype.push()`

Voyons en détail comment vous pourriez utiliser chacune de ces méthodes pour supprimer un élément d'un tableau sans modifier l'original.

### Supprimer le premier élément d'un tableau avec `slice`

Si vous voulez supprimer le premier élément d'un tableau, vous pouvez utiliser `Array.prototype.slice()` sur un tableau nommé `arr` comme ceci : `arr.slice(1)`.

Voici un exemple complet, dans lequel vous voulez supprimer le premier élément d'un tableau contenant les six premières lettres de l'alphabet.

```javascript
// le tableau de départ
const arrayOfLetters = ['a', 'b', 'c', 'd', 'e', 'f'];

// ici le tableau est copié, sans le premier élément
const copyWithoutFirstElement = arrayOfLetters.slice(1);

// arrayOfLetters est inchangé
console.log(arrayOfLetters) // ['a', 'b', 'c', 'd', 'e', 'f']

// et copyWithoutFirstElement contient les lettres de b à f
console.log(copyWithoutFirstElement) // ['b', 'c', 'd', 'e', 'f']
```

La méthode `slice` peut prendre un seul nombre comme argument, et dans ce cas, elle copie à partir de cet index jusqu'à la fin du tableau. Donc, utiliser `arrayOfLetters.slice(1)` créera une copie du tableau `arrayOfLetters` qui exclut le premier élément.

### Supprimer le dernier élément d'un tableau avec `slice`

Si l'élément que vous voulez supprimer est le dernier élément du tableau, vous pouvez utiliser `Array.prototype.slice()` sur un tableau nommé `arr` de cette manière : `arr.slice(0, -1)`.

Voici un exemple complet utilisant le même tableau d'alphabet que ci-dessus, commençant par un tableau des six premières lettres de l'alphabet.

```javascript
const arrayOfLetters = ['a', 'b', 'c', 'd', 'e', 'f'];
const copyWithoutLastElement = arrayOfLetters.slice(0, -1);

// arrayOfLetters est inchangé
console.log(arrayOfLetters) // ['a', 'b', 'c', 'd', 'e', 'f']

console.log(copyWithoutLastElement) // ['a', 'b', 'c', 'd', 'e']
```

La méthode `slice` prend jusqu'à deux paramètres. Le premier index de `slice` indique à partir de quel index commencer la copie, et le deuxième argument indique jusqu'à quel élément copier – mais il n'est pas inclusif.

`slice` accepte un index négatif pour compter depuis la fin. Cela signifie que l'écriture de `-1` signifierait le dernier index. Donc de `0` à `-1` signifie créer une copie à partir de l'index `0` jusqu'à (mais sans inclure) le dernier index. Le résultat final est que le dernier élément n'est pas inclus dans la copie.

### Supprimer un élément à n'importe quelle position d'un tableau avec `slice` et `concat`

Si vous voulez créer une copie qui manque d'un élément à n'importe quel index, vous pouvez utiliser `Array.prototype.slice` et `Array.prototype.concat` ensemble de cette manière : `arrayOfLetters.slice(0, n).concat(arrayOfLetters.slice(n+1))` où `n` est l'index de l'élément que vous voulez supprimer.

```javascript
const arrayOfLetters = ['a', 'b', 'c', 'd', 'e', 'f'];

const halfBeforeTheUnwantedElement = arrayOfLetters.slice(0, 2)

const halfAfterTheUnwantedElement = arrayOfLetters.slice(3);

const copyWithoutThirdElement = halfBeforeTheUnwantedElement.concat(halfAfterTheUnwantedElement);

// arrayOfLetters est inchangé
console.log(arrayOfLetters) // ['a', 'b', 'c', 'd', 'e', 'f']

console.log(copyWithoutThirdElement) // ['a', 'b', 'd', 'e', 'f']
```

Cette utilisation de `slice` est une façon de combiner les deux utilisations précédentes.

La première utilisation de `slice` créera un tableau à partir du début jusqu'à juste avant l'élément que vous voulez supprimer.

La deuxième utilisation de `slice` crée un tableau à partir de l'élément que vous voulez supprimer jusqu'à la fin du tableau.

Les deux tableaux sont concaténés ensemble avec `concat` pour former un tableau similaire à celui de départ, mais sans un élément particulier.

### Supprimer un élément d'une certaine valeur avec `filter`

Si vous voulez supprimer un élément avec une certaine valeur, vous pouvez utiliser `Array.prototype.filter()`. Prenons le même `arrayOfLetters` et créons une copie sans le `d`.

```javascript
const arrayOfLetters = ['a', 'b', 'c', 'd', 'e', 'f'];

const arrayWithoutD = arrayOfLetters.filter(function (letter) {
    return letter !== 'd';
});

// arrayOfLetters est inchangé
console.log(arrayOfLetters); // ['a', 'b', 'c', 'd', 'e', 'f']

console.log(arrayWithoutD); // ['a', 'b', 'c', 'e', 'f']
```

`filter` prend une fonction de rappel, et teste tous les éléments du tableau avec cette fonction de rappel. Il conserve les éléments pour lesquels la fonction de rappel retourne `true` (ou une valeur vraie) et exclut les éléments pour lesquels la fonction de rappel retourne `false` (ou une valeur fausse).

Dans ce cas, la fonction de rappel vérifie `letter !== "d"` donc elle retourne `false` pour la lettre `d` et `true` pour toutes les autres, résultant en un tableau qui n'inclut pas la lettre `d`.

La fonction de rappel de `filter` est passée trois arguments, dans l'ordre : l'élément lui-même, l'index de l'élément, et le tableau entier.

Vous pouvez créer des conditions plus complexes que cet exemple, aussi complexes que vous le souhaitez.

### Supprimer un élément d'un tableau avec une boucle `for` et `push`

Une méthode finale pour supprimer un élément d'un tableau sans modifier le tableau original est d'utiliser la méthode `push`.

Avec ces étapes simples :

1. Créer un tableau vide
2. Parcourir le tableau original
3. Pousser dans le tableau vide les éléments que vous voulez conserver

```javascript
const arrayOfLetters = ['a', 'b', 'c', 'd', 'e', 'f'];

const arrayWithoutB = [];

for (let i = 0; i < arrayOfLetters.length; i++) {
    if (arrayOfLetters[i] !== 'b') {
        arrayWithoutB.push(arrayOfLetters[i]);
    }
}

// arrayOfLetters est inchangé
console.log(arrayOfLetters); // ['a', 'b', 'c', 'd', 'e', 'f']

console.log(arrayWithoutB); // ['a', 'c', 'd', 'e', 'f']
```

La condition de l'instruction `if` peut vérifier à la fois l'index (`i`) et la valeur de l'élément pour des instructions plus complexes.

### Supprimer le premier élément d'un tableau avec la destructuration et l'opérateur rest

La destructuration de tableau et l'opérateur rest sont deux concepts un peu déroutants.

Je suggère cet article qui couvre [comment destructurer un tableau](https://www.freecodecamp.org/news/array-and-object-destructuring-in-javascript/) si vous voulez approfondir ce sujet.

Vous pouvez supprimer le premier élément en utilisant la destructuration – disons d'un tableau nommé `arr` – et créer un nouveau tableau nommé `newArr` de cette manière : `const [ , ...newArr] = arr;`.

Maintenant, voyons un exemple pratique sur la façon d'utiliser la destructuration et l'opérateur rest.

```
const arrayOfFruits = ['olive', 'apricot', 'cherry', 'peach', 'plum', 'mango'];

const [ , ...arrayOfCulinaryFruits] = arrayOfFruits;

// arrayOfFruits est inchangé
console.log(arrayOfFruits); // ['olive', 'apricot', 'cherry', 'peach', 'plum', 'mango']

console.log(arrayOfCulinaryFruits); // ['apricot', 'cherry', 'peach', 'plum', 'mango']
```

Mettre une virgule avant l'opérateur rest dit d'éviter le premier élément dans le tableau, et tous les autres sont copiés dans le tableau `arrayOfCulinaryFruits`.

## Comment supprimer un élément d'un tableau en modifiant le tableau

Dans certains cas, il peut être approprié de modifier le tableau original. Dans ces cas, vous pouvez également utiliser l'une des méthodes suivantes qui modifient le tableau.

* `Array.prototype.pop()`
* `Array.prototype.shift()`
* `Array.prototype.splice()`

### Supprimer le dernier élément d'un tableau avec `pop`

Vous pouvez supprimer le dernier élément d'un tableau avec `Array.prototype.pop()`.

Si vous avez un tableau nommé `arr`, cela ressemble à `arr.pop()`.

```javascript
const arrayOfNumbers = [1, 2, 3, 4];

const previousLastElementOfTheArray = arrayOfNumbers.pop();

console.log(arrayOfNumbers); // [1, 2, 3]

console.log(previousLastElementOfTheArray); // 4
```

La méthode `pop` est utilisée sur le tableau, et elle modifie le tableau en supprimant le dernier élément du tableau.

La méthode `pop` retourne également l'élément supprimé.

### Supprimer le premier élément d'un tableau avec `shift`

La méthode `shift` peut être utilisée sur un tableau pour supprimer le premier élément d'un tableau.

Si vous avez un tableau nommé `arr`, elle peut être utilisée de cette manière : `arr.shift()`.

```javascript
const arrayOfNumbers = [1, 2, 3, 4];

const previousFirstElementOfTheArray = arrayOfNumbers.shift();

console.log(arrayOfNumbers); // [2, 3, 4]

console.log(previousFirstElementOfTheArray); // 1
```

La méthode `shift` supprime le premier élément du tableau.

Elle retourne également l'élément supprimé.

### Supprimer un élément à n'importe quel index avec `splice`

Vous pouvez supprimer l'élément à n'importe quel index en utilisant la méthode `splice`.

Si vous avez un tableau nommé `arr`, elle peut être utilisée de cette manière pour supprimer un élément à n'importe quel index : `arr.splice(n, 1)`, avec `n` étant l'index de l'élément à supprimer.

```javascript
const arrayOfNumbers = [1, 2, 3, 4];

const previousSecondElementOfTheArray = arrayOfNumbers.splice(1, 1);

console.log(arrayOfNumbers); // [1, 3, 4]

console.log(previousSecondElementOfTheArray); // [2]
```

La méthode `splice` peut accepter de nombreux arguments.

Pour supprimer un élément à n'importe quel index, vous devez donner à `splice` deux arguments : le premier argument est l'index de l'élément à supprimer, le deuxième argument est le nombre d'éléments à supprimer.

Donc, si vous avez un tableau nommé `arr`, afin de supprimer un élément à l'index 4, la façon d'utiliser la méthode `splice` serait : `arr.splice(4, 1)`.

La méthode `splice` retourne ensuite un tableau contenant les éléments supprimés.

## Conclusion

Il existe de nombreuses façons différentes de faire la même chose en JavaScript.

Dans cet article, vous avez appris neuf méthodes différentes pour supprimer un élément d'un tableau. Six d'entre elles ne modifient pas le tableau original, et trois le font.

Vous utiliserez probablement toutes ces méthodes à un moment ou à un autre, et peut-être apprendrez-vous encore plus de méthodes pour faire cette même chose.

Amusez-vous !