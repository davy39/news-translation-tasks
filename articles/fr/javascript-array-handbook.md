---
title: Guide des tableaux JavaScript – Apprenez comment fonctionnent les méthodes
  de tableau JS avec des exemples et une feuille de triche
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2023-08-31T14:22:03.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/JavaScript-Array-for-Beginners-Cover.png
tags:
- name: arrays
  slug: arrays
- name: handbook
  slug: handbook
- name: JavaScript
  slug: javascript
seo_title: Guide des tableaux JavaScript – Apprenez comment fonctionnent les méthodes
  de tableau JS avec des exemples et une feuille de triche
seo_desc: 'In programming, an array is a data structure that contains a collection
  of elements. Arrays are very useful because you can store, access, and manipulate
  multiple elements in a single array.

  In this handbook, you''ll learn how to work with arrays in J...'
---

En programmation, un tableau est une structure de données qui contient une collection d'éléments. Les tableaux sont très utiles car vous pouvez stocker, accéder et manipuler plusieurs éléments dans un seul tableau.

Dans ce guide, vous apprendrez à travailler avec des tableaux en JavaScript. Nous couvrirons les règles spécifiques que vous devez suivre lors de la création d'un tableau, ainsi que comment utiliser les méthodes de tableau pour manipuler et transformer votre tableau comme vous le souhaitez.

## Table des matières

1. [Comment fonctionnent les tableaux en JavaScript](#heading-comment-fonctionnent-les-tableaux-en-javascript)
2. [Comment créer un tableau en JavaScript](#heading-comment-creer-un-tableau-en-javascript)
3. [Comment accéder aux éléments d'un tableau](#heading-comment-acceder-aux-elements-dun-tableau)
4. [La propriété length du tableau](#heading-la-propriete-length-du-tableau)
5. [Comment ajouter des éléments à un tableau](#heading-comment-ajouter-des-elements-a-un-tableau)
6. [Comment supprimer un élément d'un tableau](#heading-comment-supprimer-un-element-dun-tableau)
7. [Comment vérifier si une variable est un tableau](#heading-comment-verifier-si-une-variable-est-un-tableau)
8. [Comment itérer ou boucler sur un tableau](#heading-comment-iterer-ou-boucler-sur-un-tableau)
9. [Comment convertir un tableau en une chaîne de caractères](#heading-comment-convertir-un-tableau-en-une-chaine-de-caracteres)
10. [Comment comparer deux tableaux](#heading-comment-comparer-deux-tableaux)
11. [Comment copier un tableau](#heading-comment-copier-un-tableau)
12. [Comment fusionner deux tableaux en un seul](#heading-comment-fusionner-deux-tableaux-en-un-seul)
13. [Comment rechercher dans un tableau](#heading-comment-rechercher-dans-un-tableau)
14. [Comment trier un tableau](#heading-comment-trier-un-tableau)
15. [Comment créer des tableaux multidimensionnels](#heading-comment-creer-des-tableaux-multidimensionnels)
16. [Feuille de triche des méthodes de tableau JavaScript](#heading-feuille-de-triche-des-methodes-de-tableau-javascript)
17. [Conclusion](#heading-conclusion)

## Comment fonctionnent les tableaux en JavaScript

En JavaScript, un tableau est implémenté comme un objet qui peut contenir un groupe d'éléments, de valeurs ou de données comme une collection ordonnée. Cela signifie que vous pouvez accéder à un élément d'un tableau en utilisant sa position dans la collection. Vous verrez pourquoi cela est important dans la section suivante.

Un tableau peut contenir des éléments de différents types de données, et la taille du tableau n'est pas fixe. Cela signifie que vous pouvez ajouter autant d'éléments que vous le souhaitez à un tableau.

## Comment créer un tableau en JavaScript

Il existe deux façons de créer un tableau en JavaScript :

* En utilisant les crochets `[]`
* En utilisant le constructeur `Array()`

Les crochets `[]` sont une notation littérale utilisée pour créer un tableau. Les éléments du tableau sont définis à l'intérieur des crochets, chaque élément étant séparé par une virgule `,`.

L'exemple suivant montre comment créer un tableau nommé `myArray` qui contient trois éléments de types différents : un nombre, une chaîne de caractères et un booléen.

```js
let myArray = [29, 'Nathan', true];

```

Et voici comment créer un tableau avec 3 éléments de type nombre :

```js
let myNumbers = [5, 10, 15];

```

Vous pouvez spécifier autant d'éléments que vous le souhaitez à l'intérieur des crochets.

Une autre façon de créer un tableau est d'utiliser le constructeur `Array()`, qui fonctionne comme les crochets :

```js
let myArray = Array(29, 'Nathan', true);

// ou
let myNumbers = new Array(5, 10, 15);

```

Notez que la fonction constructeur peut être appelée avec ou sans l'opérateur `new`. Les deux créent un objet tableau sans problème.

Dans la plupart des exemples de code et des bases de code, vous verrez probablement les développeurs utiliser les crochets pour créer un tableau plutôt que d'utiliser le constructeur. Cela est dû au fait qu'il est plus rapide de taper `[]` au lieu de `Array()`.

## Comment accéder aux éléments d'un tableau

Comme je l'ai dit précédemment, un tableau est une collection ordonnée, donc vous pouvez accéder à un élément à partir de sa position (également connue sous le nom de numéro d'index) dans le tableau.

Pour accéder à un élément d'un tableau, vous devez spécifier le nom du tableau suivi de crochets. À l'intérieur des crochets, spécifiez l'index de l'élément auquel vous souhaitez accéder.

Par exemple, voici comment vous accédez au premier élément de `myArray` :

```js
let myArray = [29, 'Nathan', true];

console.log(myArray[0]); // 29
console.log(myArray[1]); // Nathan
console.log(myArray[2]); // true

```

Le numéro d'index du tableau commence à 0 et augmente de 1 pour chaque élément ajouté au tableau.

Si vous essayez d'accéder à un numéro d'index auquel aucune valeur n'a encore été attribuée, JavaScript retournera `undefined` comme montré ci-dessous :

```js
let myArray = [29, 'Nathan', true];

console.log(myArray[3]); // undefined
console.log(myArray[4]); // undefined
console.log(myArray[100]); // undefined

```

Vous pouvez également remplacer un élément à un certain numéro d'index par un nouvel élément en utilisant l'opérateur d'affectation `=`.

L'exemple suivant montre comment remplacer le troisième élément (booléen) par une chaîne de caractères :

```js
let myArray = [29, 'Nathan', true];

// Remplacer le troisième élément
myArray[2] = 'Sebhastian';

console.log(myArray); // [ 29, 'Nathan', 'Sebhastian' ]

```

Dans l'exemple ci-dessus, vous pouvez voir que la valeur booléenne `true` est remplacée par la chaîne de caractères 'Sebhastian'. Ensuite, examinons la propriété `length`.

## La propriété `length` du tableau

La propriété `length` montre combien d'éléments un tableau contient. Vous pouvez accéder à cette propriété en utilisant la notation par point `.` comme montré ci-dessous :

```js
let myArray = [29, 'Nathan', true];

console.log(myArray.length); // 3

let animals = ['Dog', 'Cat'];

console.log(animals.length); // 2

```

La propriété `length` est mise à jour chaque fois que vous ajoutez ou supprimez des éléments d'un tableau.

## Comment ajouter des éléments à un tableau

Pour ajouter un ou plusieurs éléments à un tableau, vous pouvez utiliser les méthodes `push()` et `unshift()` du tableau.

La méthode `push()` ajoute de nouveaux éléments à la fin du tableau, tandis que la méthode `unshift()` insère de nouveaux éléments au début du tableau :

```js
let animals = ['Dog', 'Cat'];

animals.push('Horse', 'Fish');

console.log(animals);
// [ 'Dog', 'Cat', 'Horse', 'Fish' ]

animals.unshift('Bird');

console.log(animals);
// [ 'Bird', 'Dog', 'Cat', 'Horse', 'Fish' ]

```

Ici, notez que vous pouvez utiliser une virgule pour séparer les éléments que vous souhaitez ajouter au tableau.

Ensuite, voyons comment vous pouvez supprimer des éléments d'un tableau.

## Comment supprimer un élément d'un tableau

Pour supprimer un élément d'un tableau, vous pouvez utiliser les méthodes `shift()` et `pop()`, selon la position de l'élément que vous souhaitez supprimer.

Utilisez la méthode `shift()` pour supprimer le premier élément, et utilisez `pop()` pour supprimer le dernier élément du tableau :

```js
let animals = ['Dog', 'Cat', 'Horse', 'Fish'];

animals.shift();

console.log(animals);
// [ 'Cat', 'Horse', 'Fish' ]

animals.pop();

console.log(animals);
// [ 'Cat', 'Horse' ]

```

Les méthodes `shift()` et `pop()` ne peuvent supprimer qu'un seul élément à la fois. Si vous souhaitez supprimer un élément au milieu d'un tableau, vous devez utiliser la méthode `splice()`.

### Comment utiliser `splice()` pour supprimer ou ajouter des éléments

La méthode `splice()` du tableau est utilisée pour supprimer ou ajouter des éléments à des positions spécifiques. Vous utilisez cette méthode lorsque `push`, `pop`, `shift` et `unshift` ne peuvent pas faire le travail.

Pour supprimer des éléments en utilisant la méthode `splice()`, vous devez spécifier deux arguments : le numéro d'index pour commencer la manipulation du tableau, et le nombre d'éléments à supprimer.

Par exemple, supposons que vous souhaitez supprimer deux éléments aux index 1 et 2 dans le tableau `animals`. Voici comment faire :

```js
let animals = ['Dog', 'Cat', 'Horse', 'Fish'];

animals.splice(1, 2);

console.log(animals);
// [ 'Dog', 'Fish' ]

```

Le `splice(1, 2)` signifie commencer la manipulation du tableau à l'index 1, puis supprimer 2 éléments à partir de là.

Pour ajouter des éléments en utilisant `splice()`, vous devez spécifier les éléments à ajouter après le deuxième argument.

Par exemple, voici comment j'ajoute une valeur de chaîne 'Bird' et 'Squid' à l'index 1 :

```js
let animals = ['Dog', 'Cat'];

animals.splice(1, 0, 'Bird', 'Squid');

console.log(animals);
// [ 'Dog', 'Bird', 'Squid', 'Cat' ]

```

Si vous ne souhaitez pas supprimer d'éléments, vous pouvez passer `0` comme deuxième argument à la méthode `splice()`. Vous spécifiez ensuite les éléments que vous souhaitez ajouter.

La méthode `splice()` peut être déroutante la première fois que vous la voyez, mais ne vous inquiétez pas ! Vous mémoriserez son fonctionnement avec plus de pratique.

## Comment vérifier si une variable est un tableau

Pour vérifier si une variable est un tableau, vous pouvez utiliser la méthode `Array.isArray()` qui teste si l'argument donné à la méthode est un tableau ou non.

Cette méthode retourne `true` lorsque vous passez un tableau, et `false` pour autre chose :

```js
let myArray = [1, 2, 3];
let notAnArray = 'Hello!';

console.log(Array.isArray(myArray)); // true
console.log(Array.isArray(notAnArray)); // false

```

Notez que vous devez spécifier la classe `Array` lorsque vous appelez la méthode `isArray()`.

Cela est dû au fait que `isArray()` est une méthode statique, donc vous ne pouvez l'appeler que directement depuis la classe qui définit la méthode.

## Comment itérer ou boucler sur un tableau

Il existe 4 façons d'itérer sur un tableau en JavaScript, selon la méthode que vous utilisez :

1. En utilisant une boucle `for`
2. En utilisant une boucle `while`
3. En utilisant la boucle `for...in`
4. En utilisant la boucle `for...of`
5. En utilisant la méthode `forEach()`

Apprenons comment utiliser ces 4 méthodes avec des exemples.

### 1. Comment utiliser une boucle for

Pour itérer sur un tableau en utilisant une boucle `for`, vous devez utiliser la propriété `length` du tableau comme expression de condition.

Dans l'exemple suivant, une boucle `for` continuera à s'exécuter tant que la variable `i` est inférieure à la longueur du tableau :

```js
let animals = ['dog', 'bird', 'cat', 'horse'];

for (let i = 0; i < animals.length; i++) {
  console.log(animals[i]);
}

```

Vous pouvez manipuler les éléments du tableau à l'intérieur du corps de la boucle `for`.

### 2. Comment utiliser une boucle while

Une autre façon d'itérer sur un tableau est d'utiliser une boucle `while`. Vous devez utiliser une variable et la longueur du tableau pour contrôler quand l'itération s'arrête, comme la boucle `for` précédemment :

```js
let animals = ['dog', 'bird', 'cat', 'horse'];

let i = 0;

while (i < animals.length) {
  console.log(animals[i]);
  i++;
}

```

À l'intérieur de la boucle while, vous devez incrémenter la variable `i` de un pour éviter une boucle infinie.

### 3. Comment utiliser une boucle for...in

La boucle `for...in` est une autre syntaxe que vous pouvez utiliser pour itérer sur un tableau. Cette boucle retourne la position d'index du tableau, donc vous pouvez l'utiliser comme ceci :

```js
let animals = ['dog', 'bird', 'cat', 'horse'];

for (i in animals) {
  console.log(animals[i]);
}

```

La boucle `for...in` est plus concise par rapport à une boucle `for` ou `while`, mais il est préférable d'utiliser une boucle `for...of` lors de l'itération sur un tableau.

### 4. Comment utiliser une boucle for...of

La boucle `for...of` peut être utilisée pour itérer sur un tableau. Elle retourne l'élément du tableau à chaque itération :

```js
let animals = ['dog', 'bird', 'cat', 'horse'];

for (element of animals) {
  console.log(element);
}

```

Alors que la boucle `for...in` retourne la position d'index, la boucle `for...of` retourne l'élément directement.

### 5. Comment utiliser la méthode `forEach()`

L'objet tableau JavaScript lui-même possède une méthode appelée `forEach()` que vous pouvez utiliser pour itérer sur un tableau de la position 0 à la dernière position.

La méthode accepte une fonction de rappel qui est exécutée à chaque itération. Pour chaque itération, la méthode passe également l'élément du tableau et la position d'index. Voici un exemple d'utilisation de la méthode :

```js
let animals = ['dog', 'bird', 'cat', 'horse'];

animals.forEach(function (element, index) {
  console.log(`${index}: ${element}`);
});

```

La sortie sera :

```txt
0: dog
1: bird
2: cat
3: horse

```

Et c'est ainsi que vous itérez sur un tableau en utilisant la méthode `forEach()`. Vous pouvez utiliser n'importe quelle méthode que vous préférez.

## Comment convertir un tableau en une chaîne de caractères

Pour convertir un tableau en une chaîne de caractères, vous pouvez utiliser la méthode `toString()` ou `join()`.

La méthode `toString()` convertit un tableau donné en une chaîne de caractères, avec les éléments séparés par une virgule :

```js
const animals = ['cat', 'bird', 'fish'];

console.log(animals.toString()); // "cat,bird,fish"

```

La méthode `join()` convertit également un tableau en une chaîne de caractères, mais vous pouvez passer un séparateur de chaîne spécifique comme argument.

L'exemple suivant montre comment utiliser une barre oblique `/` et une chaîne vide comme séparateur de chaîne :

```js
const animals = ['cat', 'bird', 'fish'];

console.log(animals.join()); // "cat,bird,fish"

console.log(animals.join('/')); // "cat/bird/fish"

console.log(animals.join('')); // "catbirdfish"

```

En coulisses, la méthode `toString()` appelle en réalité la méthode `join()` pour créer la chaîne.

## Comment comparer deux tableaux

Les tableaux JavaScript sont traités comme des objets. Ainsi, lorsque vous comparez deux tableaux, la comparaison regardera la référence — c'est-à-dire l'adresse de l'emplacement mémoire qui stocke ce tableau — au lieu des valeurs réelles.

La comparaison de deux tableaux retournera `false` même lorsqu'ils contiennent les mêmes éléments :

```js
let arrayOne = [7, 8, 9];
let arrayTwo = [7, 8, 9];

console.log(arrayOne === arrayTwo); // false

```

Cela est dû au fait que `arrayOne` et `arrayTwo` sont des objets différents stockés dans des emplacements mémoire différents.

La seule façon pour qu'une comparaison de tableaux retourne `true` est lorsque les deux variables font référence au même objet tableau. Dans l'exemple ci-dessous, la variable `arrayTwo` est une référence à `arrayOne` :

```js
let arrayOne = [7, 8, 9];
let arrayTwo = arrayOne;

console.log(arrayOne === arrayTwo); // true

```

Mais cela ne fonctionnera pas lorsque vous devez comparer deux tableaux de références différentes. Une façon de comparer les tableaux est de convertir le tableau en un objet JSON.

### Comparer les tableaux en les convertissant en objet JSON

Avant de comparer deux tableaux différents, vous devez les convertir en objets JSON en appelant la méthode `JSON.stringify()`.

Vous pouvez ensuite comparer les deux chaînes séquentielles comme suit :

```js
let arrayOne = [7, 8, 9];
let arrayTwo = [7, 8, 9];

console.log(JSON.stringify(arrayOne) === JSON.stringify(arrayTwo)); // true

```

Mais cette solution compare les tableaux indirectement, et avoir les mêmes valeurs dans des ordres différents retournera `false` au lieu de `true`.

Pour comparer les éléments de deux tableaux de manière programmatique, vous devez utiliser une autre solution.

### Comment comparer les tableaux avec la méthode `every()`

Une autre façon de comparer deux tableaux est d'utiliser la combinaison de la propriété `length` et de la méthode `every()`.

Tout d'abord, vous comparez la longueur des tableaux afin que la comparaison ne retourne pas `true` lorsque le deuxième tableau contient plus d'éléments que le premier tableau.

Après cela, vous testez si l'élément du premier tableau est égal à l'élément du deuxième tableau, à la même position d'index. Utilisez l'opérateur `&&` pour joindre la comparaison comme montré ci-dessous :

```js
let arrayOne = [7, 8, 9];
let arrayTwo = [7, 8, 9];

let result =
  arrayOne.length === arrayTwo.length &&
  arrayOne.every(function (element, index) {
    // comparer si l'élément correspond au même index
    return element === arrayTwo[index];
  });

console.log(result); // true

```

De cette façon, vous comparez si l'élément à un index spécifique est vraiment égal ou non.

Cependant, cette solution nécessite que les deux tableaux aient des éléments égaux à un certain index afin de retourner `true`.

Si vous ne vous souciez pas de l'ordre et souhaitez simplement que les deux tableaux aient les mêmes éléments, vous devez utiliser la méthode `includes()` au lieu de l'opérateur d'égalité `===`.

### Comment comparer les tableaux avec la méthode `includes()`

Afin de comparer les éléments de tableau qui sont dans le désordre, vous pouvez utiliser la combinaison des méthodes `every()` et `includes()`.

La méthode `includes()` teste si un tableau contient un élément spécifique que vous avez spécifié comme argument :

```js
let arrayOne = [7, 8, 9];
let arrayTwo = [9, 7, 8];

let result =
  arrayOne.length === arrayTwo.length &&
  arrayOne.every(function (element) {
    return arrayTwo.includes(element);
  });

console.log(result); // true

```

Une alternative à la méthode `includes()` est d'utiliser la méthode `indexOf()`, qui retourne l'index de l'élément spécifié.

Lorsque l'élément n'est pas trouvé, la méthode `indexOf()` retourne `-1`. Cela signifie que vous devez faire en sorte que `every()` retourne `true` lorsque `indexOf(element) !== -1` comme montré ci-dessous :

```js
let arrayOne = [7, 8, 9];
let arrayTwo = [9, 7, 8];

let result =
  arrayOne.length === arrayTwo.length &&
  arrayOne.every(function (element) {
    return arrayTwo.indexOf(element) !== -1;
  });

console.log(result); // true

```

Comme vous pouvez le voir, comparer des tableaux n'est pas simple. Vous devez utiliser les méthodes fournies par l'objet tableau de manière créative.

Mais ne vous inquiétez pas ! La plupart du temps, vous n'avez pas besoin de comparer des objets tableau lors du développement d'une application web. Ensuite, apprenons comment vous pouvez copier un tableau.

## Comment copier un tableau

Une façon de copier un tableau est d'utiliser la méthode `slice()`, qui est fournie exactement pour copier un tableau.

Vous devez simplement appeler la méthode et assigner le tableau retourné à une nouvelle variable comme ceci :

```js
let arrayOne = [7, 8, 9];
let arrayTwo = arrayOne.slice();

console.log(arrayOne); // [ 7, 8, 9 ]
console.log(arrayTwo); // [ 7, 8, 9 ]

```

Mais gardez à l'esprit que la méthode `slice()` retourne une copie superficielle, ce qui signifie que les valeurs de la copie sont des références au tableau original.

Une copie superficielle ne posera pas de problème lorsque votre tableau contient des valeurs primitives comme des chaînes de caractères, des nombres ou des booléens. Mais cela pourrait devenir un problème lorsque vous copiez un tableau d'objets.

Pour vous montrer ce que je veux dire, voyez l'exemple ci-dessous :

```js
let arrayOne = [{ name: 'Jack', age: 25 }];
let arrayTwo = arrayOne.slice();

console.log(arrayOne); // [ { name: 'Jack', age: 25 } ]
console.log(arrayTwo); // [ { name: 'Jack', age: 25 } ]

arrayTwo[0].name = 'Nathan';

console.log(arrayOne); // [ { name: 'Nathan', age: 25 } ]
console.log(arrayTwo); // [ { name: 'Nathan', age: 25 } ]

```

Remarquez-vous ce qui ne va pas ? Le code ci-dessus modifie uniquement la propriété `name` de `arrayTwo`, mais il change les deux tableaux !

Cela est dû au fait que `arrayTwo` est une copie superficielle de `arrayOne`. Pour éviter ce comportement, vous devez effectuer une copie profonde afin que les valeurs de `arrayTwo` soient déconnectées du tableau original.

### Comment créer une copie profonde d'un tableau

Pour créer une copie profonde d'un tableau, vous devez copier le tableau en utilisant les méthodes `JSON.parse()` et `JSON.stringify()` au lieu d'utiliser la méthode `slice()`.

La méthode `JSON.stringify()` transforme le tableau en une chaîne JSON, et `JSON.parse()` convertit cette chaîne en un tableau.

Parce que la copie est créée à partir d'une chaîne JSON, il n'y a plus de connexion avec le tableau original :

```js
let arrayOne = [{ name: 'Jack', age: 25 }];
let arrayTwo = JSON.parse(JSON.stringify(arrayOne));

console.log(arrayOne); // [ { name: 'Jack', age: 25 } ]
console.log(arrayTwo); // [ { name: 'Jack', age: 25 } ]

arrayTwo[0].name = 'Nathan';

console.log(arrayOne); // [ { name: 'Jack', age: 25 } ]
console.log(arrayTwo); // [ { name: 'Nathan', age: 25 } ]

```

Ici, vous pouvez voir que la modification de la propriété de `arrayTwo` ne change pas la même propriété dans `arrayOne`. Bon travail !

## Comment fusionner deux tableaux en un seul

JavaScript fournit la méthode `concat()` que vous pouvez utiliser pour fusionner deux ou plusieurs tableaux en un seul. L'exemple suivant montre comment fusionner les tableaux `cats` et `birds` en un seul tableau nommé `animals` :

```js
let cats = ['tiger', 'cat'];
let birds = ['owl', 'eagle'];

let animals = cats.concat(birds);

console.log(animals); // [ 'tiger', 'cat', 'owl', 'eagle' ]
console.log(cats); // [ 'tiger', 'cat' ]
console.log(birds); // [ 'owl', 'eagle' ]

```

À première vue, la syntaxe de la méthode `concat()` semble fusionner le tableau `birds` dans le tableau `cats`. Mais comme vous pouvez le voir à partir des journaux de la console, le tableau `cats` est en réalité inchangé.

Pour rendre le code plus intuitif, vous pouvez appeler la méthode `concat()` à partir d'un tableau vide au lieu de l'appeler à partir du tableau `cats` :

```js
let cats = ['tiger', 'cat'];
let birds = ['owl', 'eagle'];

let animals = [].concat(cats, birds);

```

Bien que cette syntaxe soit plus intuitive, vous rencontrerez probablement la syntaxe `cats.concat(birds)` dans de nombreux codes sources JavaScript. Quelle syntaxe utiliser ? C'est à vous et à votre équipe de décider.

La méthode `concat()` vous permet de fusionner autant de tableaux que vous le souhaitez. L'exemple suivant fusionne trois tableaux en un seul :

```js
let cats = ['tiger', 'cat'];
let birds = ['owl', 'eagle'];
let dogs = ['wolf', 'dog'];

let animals = [].concat(cats, birds, dogs);
console.log(animals); // [ 'tiger', 'cat', 'owl', 'eagle', 'wolf', 'dog' ]

```

Vous avez maintenant appris à fusionner des tableaux en utilisant la méthode `concat()`. Regardons comment vous pouvez fusionner des tableaux avec l'opérateur de propagation ensuite.

### Comment fusionner des tableaux avec l'opérateur de propagation

L'opérateur de propagation `...` peut être utilisé pour développer les éléments des tableaux que vous souhaitez fusionner. Vous devez mettre les éléments développés dans un nouveau tableau comme suit :

```js
let cats = ['tiger', 'cat'];
let birds = ['owl', 'eagle'];

let animals = [...cats, ...birds];
console.log(animals); // [ 'tiger', 'cat', 'owl', 'eagle' ]

```

Ici, vous pouvez voir que les éléments des tableaux `cats` et `birds` sont développés dans un autre tableau, et ce tableau est assigné comme valeur de la variable `animals`.

La méthode `concat()` et l'opérateur de propagation peuvent être utilisés pour fusionner plusieurs tableaux sans problème.

## Comment rechercher dans un tableau

Il existe trois façons de rechercher dans un tableau, selon le résultat que vous souhaitez obtenir :

1. Trouver si un élément existe dans un tableau
2. Trouver la position d'index d'un élément dans un tableau
3. Trouver la valeur qui répond à certains critères dans un tableau

Apprenons ensemble ces trois façons de rechercher dans un tableau. Ne vous inquiétez pas, elles sont simples.

### 1. Comment trouver si un élément existe dans un tableau

Si vous souhaitez simplement savoir si un certain élément existe dans un tableau, vous pouvez utiliser la méthode `includes()`. L'exemple suivant recherche la valeur de chaîne 'e' dans un tableau de chaînes :

```js
let letters = ['a', 'b', 'c', 'd'];

console.log(letters.include('e')); // false

```

La méthode `includes()` retourne `true` lorsque l'élément est trouvé, ou `false` lorsqu'il ne l'est pas.

### 2. Comment trouver la position d'index d'un élément dans un tableau

Parfois, vous pouvez vouloir obtenir la position d'index de l'élément. Vous devez utiliser la méthode `indexOf()` dans ce cas :

```js
let letters = ['a', 'b', 'c', 'd'];

console.log(letters.indexOf('c')); // 2

```

Ici, la méthode `indexOf()` est appelée sur le tableau `letters` pour rechercher l'index de la valeur 'c'. La méthode retourne `-1` lorsque l'élément n'est pas trouvé, mais dans ce cas, elle retourne `2` car la lettre c est à l'index 2 (rappelons que JS utilise un indexage basé sur zéro, ce qui signifie que le compte commence à 0, et non à 1).

### 3. Comment trouver des éléments qui répondent à certains critères dans un tableau

Pour trouver des éléments qui répondent à certains critères, vous devez utiliser la méthode `filter()`.

La méthode `filter()` est une méthode intégrée disponible pour les objets de tableau JavaScript qui peut vous aider à filtrer un tableau. La syntaxe de la méthode est la suivante :

```js
arrayObject.filter(callback, thisContext);

```

La méthode a deux paramètres :

* `callback` (**Requis**) – La fonction de filtrage qui sera exécutée pour chaque valeur de tableau
* `thisContext` (**Optionnel**) – La valeur du mot-clé `this` à l'intérieur du `callback`

Le paramètre `thisContext` est optionnel et généralement non nécessaire. Vous devez simplement définir la fonction `callback`, qui acceptera trois arguments :

* L'élément `currentElement` en cours de traitement dans la méthode
* L'`index` de l'élément qui commence à `0`
* et l'objet `array` où vous appelez `filter()`

```js
filterCallback(currentElement, index, array){
  // ...
}

```

La fonction de rappel doit inclure un motif de validation qui retourne soit `true` soit `false`.

#### Exemples de méthode de filtrage

Voyons un exemple de `filter()` en action. Supposons que vous avez un tableau appelé `stockPrices` comme suit :

```js
let stockPrices = [3, 7, 2, 15, 4, 9, 21, 14];

```

Vous souhaitez filtrer les prix pour inclure uniquement ceux supérieurs à 5.

Voici comment faire avec la méthode `filter()` :

```js
let stockPrices = [3, 7, 2, 15, 4, 9, 21, 14];

let filteredPrices = stockPrices.filter(function (currentElement) {
  return currentElement > 5;
});

console.log(filteredPrices); // [7, 15, 9, 21, 14]

```

La méthode `filter()` évalue le `currentElement` et retourne soit `true` soit `false`.

Si votre fonction de rappel retourne `true`, le `currentElement` sera ajouté au tableau de résultats :

* Lors de la première itération, le `currentElement` est `3` donc le rappel retourne `false`
* Lors de la deuxième itération, le `currentElement` est `7` donc le rappel retourne `true` et la valeur est poussée dans le tableau de résultats
* L'itération continuera jusqu'au dernier élément
* Le tableau résultant est assigné à la variable `filteredPrices`

Et c'est ainsi que la méthode fonctionne. Ensuite, voyons comment utiliser la méthode `filter()` pour filtrer un tableau d'objets.

#### Comment filtrer un tableau d'objets

La méthode `filter()` peut également être utilisée sur un tableau d'objets.

Supposons que vous avez un tableau d'objets contenant des prix de stocks imaginaires et leurs symboles comme montré ci-dessous :

```js
let stocks = [
  {
    code: 'GOOGL',
    price: 1700,
  },
  {
    code: 'AAPL',
    price: 130,
  },
  {
    code: 'MSFT',
    price: 219,
  },
  {
    code: 'TSLA',
    price: 880,
  },
  {
    code: 'FB',
    price: 267,
  },
  {
    code: 'AMZN',
    price: 3182,
  },
];

```

Maintenant, vous devez filtrer le tableau pour qu'il ne contienne que les stocks avec une valeur `price` inférieure à 1000. Voici comment faire :

```js
let filteredStocks = stocks.filter(function (currentElement) {
  return currentElement.price < 1000;
});

```

La valeur de `filteredStocks` sera la suivante :

```txt
0: {code: "AAPL", price: 130}
1: {code: "MSFT", price: 219}
2: {code: "TSLA", price: 880}
3: {code: "FB", price: 267}

```

Enfin, vous pouvez également écrire la fonction de rappel en utilisant la syntaxe de fonction fléchée comme ceci :

```js
let filteredStocks = stocks.filter(
  currentElement => currentElement.price < 1000
);

```

Lorsque vous avez des critères de filtrage simples, l'utilisation de la syntaxe de fonction fléchée peut vous aider à écrire un code plus propre.

## Comment trier un tableau

Pour trier un tableau, vous pouvez utiliser la méthode `sort()` fournie, qui trie un tableau par ordre croissant par défaut :

```js
let numbers = [5, 2, 4, 1];

numbers.sort();

console.log(numbers); // [ 1, 2, 4, 5 ]

```

Si vous souhaitez trier un tableau par ordre décroissant, vous pouvez appeler la méthode `reverse()` après la méthode `sort()` comme montré ci-dessous :

```js
let numbers = [5, 2, 4, 1];

numbers.sort().reverse();

console.log(numbers); // [ 5, 4, 2, 1 ]

```

La méthode `reverse()` inversera le tableau, donc le premier élément du tableau devient le dernier, le dernier devient le premier, et ainsi de suite.

## Comment créer des tableaux multidimensionnels

Un tableau multidimensionnel est un tableau qui contient un autre tableau. Pour en créer un, vous devez écrire un tableau à l'intérieur d'un littéral de tableau (les crochets)

L'exemple suivant montre comment vous pouvez créer un tableau à deux dimensions :

```js
let numbers = [[5, 6, 7]];

```

Pour accéder au tableau, vous devez simplement appeler la variable avec deux indices de tableau. Le premier index est pour le tableau externe, et le deuxième index est pour le tableau interne :

```js
let numbers = [[5, 6, 7]];
console.log(numbers[0][0]); // 5
console.log(numbers[0][1]); // 6
console.log(numbers[0][2]); // 7

```

Comme vous pouvez le voir dans l'exemple ci-dessus, le tableau `[5, 6, 7]` est stocké à l'index `0` du tableau externe `[]`. Vous pouvez ajouter plus d'éléments à l'intérieur du tableau comme suit :

```js
let numbers = [[5, 6, 7], [10], [20]];
console.log(numbers[1][0]); // 10
console.log(numbers[2][0]); // 20

```

Un tableau multidimensionnel n'est pas obligé d'avoir la même longueur de tableau, comme on peut le voir ci-dessus. Bien que vous puissiez créer même un tableau à trois ou quatre dimensions, il n'est pas recommandé de créer plus qu'un tableau à deux dimensions car cela sera déroutant.

Remarquez à quel point il est difficile de lire et d'accéder à la valeur `[23]` à l'intérieur du tableau à trois dimensions ci-dessous :

```js
let numbers = [[5, 6, 7, [23]]];
console.log(numbers[0][3][0]); // 23

```

Enfin, vous pouvez toujours utiliser les méthodes de l'objet `Array` JavaScript comme `push()`, `shift()` et `unshift()` pour manipuler le tableau multidimensionnel :

```js
let numbers = [[5, 6, 7, [23]]];
numbers.push([50]);
console.log(numbers); // [[5, 6, 7, [23]], [50]]

numbers.shift();
console.log(numbers); // [[50]]

numbers.unshift('13');
console.log(numbers); // ["13", [50]]

```

Un tableau multidimensionnel n'a pas de méthodes uniques par rapport à un tableau à une dimension. Souvent, il est utilisé pour stocker un groupe de données liées en un seul tableau.

L'exemple suivant montre comment regrouper les valeurs `name` et `age` sous un tableau multidimensionnel :

```js
let users = [
  ['Nathan', 28],
  ['Jack', 23],
  ['Alex', 30],
];

```

Sauf si vous devez utiliser un tableau, il est préférable d'utiliser un tableau d'objets pour stocker un groupe de données liées :

```js
let users = [
  { name: 'Nathan', age: 28 },
  { name: 'Jack', age: 23 },
  { name: 'Alex', age: 30 },
];

```

Idéalement, vous devriez utiliser uniquement des tableaux à une dimension dans votre projet. Utilisez une structure à deux dimensions si vous en avez vraiment besoin, mais n'allez jamais au-delà ou vous aurez du mal à manipuler le tableau plus tard.

## Feuille de triche des méthodes de tableau JavaScript

Les débutants sont souvent submergés par le nombre de méthodes qu'un tableau possède, donc j'ai préparé une feuille de triche qui peut vous aider à obtenir un aperçu rapide de ce que fait une méthode.

La feuille de triche contient une courte description et un exemple rapide de ce que fait une méthode. Vous pouvez la télécharger ici :

%[https://twitter.com/nsebhastian/status/1696034185398645024]

## Conclusion

Félicitations pour avoir terminé ce guide JavaScript sur les tableaux. J'espère que ce tutoriel vous a aidé à comprendre comment créer, copier et manipuler un tableau en JavaScript.

Si vous avez apprécié cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous aurez vraiment l'impression de comprendre ce que vous faites avec JavaScript._

Jusqu'à la prochaine fois !