---
title: JavaScript Inverser un Tableau – Tutoriel avec Exemple de Code JS
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-01-18T18:02:07.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-reverse-tutorial-with-example-js-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/js-reverse.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: JavaScript Inverser un Tableau – Tutoriel avec Exemple de Code JS
seo_desc: "Reversing an array with certain restrictions is one of the most common\
  \ challenges you will find in job interviews and coding quizzes. \nThis tutorial\
  \ will show you five ways to reverse an array in JavaScript with and without the\
  \ reverse method, along ..."
---

Inverser un tableau avec certaines restrictions est l'un des défis les plus courants que vous rencontrerez lors des entretiens d'embauche et des quiz de codage. 

Ce tutoriel vous montrera **cinq** façons d'inverser un tableau en JavaScript avec et sans la méthode `reverse`, accompagnées d'extraits de code que vous pouvez utiliser.

## Comment inverser un tableau en JavaScript avec la méthode Reverse

Lorsque vous devez inverser un tableau en JavaScript, vous pouvez utiliser la méthode `reverse`, qui placera le dernier élément en premier et le premier élément en dernier :

```js
let numbers = [1, 2, 3, 4, 5];
let reversedNumbers = numbers.reverse();

console.log(reversedNumbers);
// [5, 4, 3, 2, 1]
```

Mais gardez à l'esprit que la méthode `reverse` modifiera également le tableau original :

```js
let numbers = [1, 2, 3, 4, 5];
let reversedNumbers = numbers.reverse();

console.log(reversedNumbers);
// [5, 4, 3, 2, 1]

console.log(numbers);
// [5, 4, 3, 2, 1]
```

Certains défis de codage peuvent vous demander de préserver le tableau original, alors voyons comment vous pouvez inverser un tableau sans modifier l'original.

## Comment inverser un tableau en JavaScript avec l'opérateur Spread

Vous pouvez utiliser une combinaison de l'[opérateur spread](https://sebhastian.com/javascript-spread-operator/) et de la méthode `reverse` pour inverser un tableau sans modifier l'original. 

Tout d'abord, vous placez les éléments retournés par l'opérateur spread dans un nouveau tableau en encadrant la syntaxe spread avec des crochets `[]` :

```js
[...numbers]
```

Ensuite, vous appelez la méthode `reverse` sur le tableau. De cette façon, la méthode `reverse` sera exécutée sur le nouveau tableau au lieu de l'original :

```js
let numbers = [1, 2, 3, 4, 5];
let reversedNumbers = [...numbers].reverse();

console.log(reversedNumbers);
// [5, 4, 3, 2, 1]

console.log(numbers);
// [1, 2, 3, 4, 5]
```

Remarque : la méthode `spread` est une syntaxe ES6. Lorsque vous devez supporter des navigateurs plus anciens ou que vous souhaitez utiliser la syntaxe ES5, vous pouvez combiner les méthodes `slice` et `reverse`. Regardons cela maintenant.

## Comment inverser un tableau en JavaScript avec les méthodes Slice et Reverse 

[La méthode `slice`](https://sebhastian.com/javascript-array-slice/) est utilisée pour retourner les éléments sélectionnés sous forme de nouveau tableau. Lorsque vous appelez la méthode sans aucun argument, elle retournera un nouveau tableau identique à l'original (du premier élément au dernier).

Ensuite, vous appelez la méthode `reverse` sur le nouveau tableau retourné. C'est pourquoi le tableau original n'est pas inversé :

```js
let numbers = [1, 2, 3, 4, 5];
let reversedNumbers = numbers.slice().reverse();

console.log(reversedNumbers);
// [5, 4, 3, 2, 1]

console.log(numbers);
// [1, 2, 3, 4, 5]
```

## Comment inverser un tableau en JavaScript sans la méthode Reverse

Parfois, lors d'un entretien d'embauche, on vous demandera d'inverser un tableau sans utiliser la méthode `reverse`. Pas de problème ! Vous pouvez utiliser une combinaison d'une [boucle `for`](https://sebhastian.com/javascript-for-loop/) et de la méthode `push` d'un tableau comme dans l'exemple ci-dessous :

```js
let numbers = [1, 2, 3, 4, 5];
let reversedNumbers = [];

for(let i = numbers.length -1; i >= 0; i--) {
  reversedNumbers.push(numbers[i]);
}

console.log(reversedNumbers);
```

## Comment écrire votre propre fonction Reverse en JS

Enfin, supposons que vous devez écrire votre propre fonction reverse qui doit inverser un tableau sans créer de copie. Cela peut sembler compliqué au premier abord, mais ne vous inquiétez pas, car c'est en fait assez facile.

Ce que vous devez faire ici, c'est échanger le premier et le dernier élément du tableau, puis le deuxième et l'avant-dernier élément, et ainsi de suite jusqu'à ce que vous ayez échangé tous les éléments.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/js-array-reverse-function-1.png)
_Une fonction pour inverser un tableau_

Écrivons une fonction pour faire exactement cela.

Écrivez la fonction `customReverse` et stockez à la fois le premier index à `0` et le dernier index en utilisant `array.length - 1` comme variables. 

```js
function customReverse(originalArray) {

  let leftIndex = 0;
  let rightIndex = originalArray.length - 1;
}
```

Ensuite, créez [une boucle `while`](https://sebhastian.com/javascript-while-loop/) qui s'exécute tant que le `leftIndex` est inférieur au `rightIndex`. 

À l'intérieur de cette boucle, échangez la valeur du `leftIndex` et du `rightIndex`. Vous pouvez stocker temporairement l'une des valeurs dans une variable temporaire :

```js
while (leftIndex < rightIndex) {

  // Échangez les éléments
  let temp = originalArray[leftIndex];
  originalArray[leftIndex] = originalArray[rightIndex];
  originalArray[rightIndex] = temp;
}
```

Enfin, déplacez le `leftIndex` vers le haut et le `rightIndex` vers le bas. Lorsque la boucle `while` se répète, elle échangera le deuxième et l'avant-dernier élément, et ainsi de suite :

```js
  function customReverse(originalArray) {

  let leftIndex = 0;
  let rightIndex = originalArray.length - 1;

  while (leftIndex < rightIndex) {

    // Échangez les éléments avec une variable temporaire
    let temp = originalArray[leftIndex];
    originalArray[leftIndex] = originalArray[rightIndex];
    originalArray[rightIndex] = temp;

    // Déplacez les index vers le milieu
    leftIndex++;
    rightIndex--;
  }
}
```

La boucle s'arrêtera dès qu'il n'y aura plus d'éléments à inverser. Pour les tableaux de taille impaire, la valeur de `leftIndex` et `rightIndex` sera égale, donc plus d'échange. Pour les tableaux de taille paire, le `leftIndex` sera supérieur au `rightIndex`.

Vous pouvez tester la fonction pour voir si elle fonctionne correctement comme ceci :

```js
let myArray = [1, 2, 3, 4, 5];

customReverse(myArray);

console.log(myArray);

// la sortie est [5, 4, 3, 2, 1]
```

## Conclusion

Félicitations ! Vous avez appris non seulement comment inverser un tableau en JavaScript, mais aussi comment écrire votre propre fonction reverse.

Si vous avez aimé cet article et que vous souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine !