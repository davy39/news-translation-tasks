---
title: Fonctions d'ordre supérieur en JavaScript – Atteignez de nouveaux sommets dans
  votre code JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-12T21:44:55.000Z'
originalURL: https://freecodecamp.org/news/higher-order-functions-in-javascript-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/spacex-uj3hvdfQujI-unsplash.jpg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Fonctions d'ordre supérieur en JavaScript – Atteignez de nouveaux sommets
  dans votre code JS
seo_desc: 'By Dave Gray

  What is a Higher Order Function?

  Let''s look at the name, and consider how we talk about things.

  We dig down into the details, but sometimes we want a high level view of things.

  This high level view indicates more abstraction. We go down ...'
---

Par Dave Gray

## Qu'est-ce qu'une fonction d'ordre supérieur ?

Examinons le nom et réfléchissons à la manière dont nous parlons des choses.

Nous creusons _dans_ les détails, mais parfois nous voulons une vue _d'ensemble_ des choses.

Cette vue d'ensemble indique une plus grande abstraction. Nous descendons dans les détails, mais nous nous élevons vers un point de vue plus abstrait.

Les fonctions d'ordre supérieur sont exactement cela : un niveau d'abstraction plus élevé que vos fonctions typiques.

### Comment pouvons-nous définir une fonction d'ordre supérieur ?

Les fonctions d'ordre supérieur sont des fonctions qui effectuent des opérations sur d'autres fonctions.

Dans cette définition, _opérations_ peut signifier prendre une ou plusieurs fonctions comme argument OU retourner une fonction comme résultat. Elle n'a pas besoin de faire les deux. Faire l'un ou l'autre qualifie une fonction comme fonction d'ordre supérieur.

## Examinons un exemple de fonction d'ordre supérieur

Sans une fonction d'ordre supérieur, si je veux ajouter un à chaque nombre dans un tableau et l'afficher dans la console, je peux faire ce qui suit :

```
const numbers = [1, 2, 3, 4, 5];

function addOne(array) {
  for (let i = 0; i < array.length; i++) {
    console.log(array[i] + 1);
  }
}

addOne(numbers);

```

La fonction `addOne()` accepte un tableau, ajoute un à chaque nombre dans le tableau et l'affiche dans la console. Les valeurs originales restent inchangées dans le tableau, mais la fonction fait quelque chose pour chaque valeur.

Cependant, en utilisant ce qui est peut-être la fonction d'ordre supérieur la plus courante, `forEach()`, nous pouvons simplifier ce processus :

```
const numbers = [1, 2, 3, 4, 5];

numbers.forEach((number) => console.log(number + 1));

```

**Whoa.**

Nous avons abstrait la définition et l'appel de la fonction dans le code original ci-dessus en une seule ligne !

Nous appliquons `forEach()` au tableau nommé "numbers". Il y a une fonction anonyme au début de `forEach()` qui accepte chaque élément du tableau - un à la fois.

Avec le tableau nommé numbers, il est logique de nommer chaque élément du tableau "number" bien que nous aurions pu le nommer "element" ou "el" ou même "whatever".

La fonction fléchée anonyme enregistre la valeur du nombre + 1 dans la console.

La fonction d'ordre supérieur `forEach()` applique une fonction à chaque élément d'un tableau.

## Un autre exemple de fonction d'ordre supérieur

Sans une fonction d'ordre supérieur, si je voulais créer un nouveau tableau qui ne contient que les nombres impairs du tableau numbers, je pourrais faire ce qui suit :

```
const numbers = [1, 2, 3, 4, 5];

function isOdd(array, oddArr = []) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] % 2 !== 0) {
      oddArr.push(array[i]);
    }
  }
  return oddArr;
}

const oddArray = isOdd(numbers);
console.log(oddArray);

```

La fonction `isOdd()` accepte un tableau et a un deuxième paramètre optionnel pour un tableau. Si non fourni, le tableau a une valeur par défaut de tableau vide.

La fonction vérifie chaque nombre dans le tableau pour voir s'il est un nombre impair. Si le nombre est impair, il l'ajoute au tableau du deuxième paramètre. Après que tous les nombres soient vérifiés, le tableau du deuxième paramètre est retourné.

Alors oui, c'est beaucoup à suivre.

Si nous utilisons la fonction d'ordre supérieur, `filter()`, nous pouvons abstraire tellement :

```
const numbers = [1, 2, 3, 4, 5];

const oddArray = numbers.filter((number) => number % 2 !== 0);
console.log(oddArray);

```

**OUI !**

Excusez-moi de m'enthousiasmer, mais c'est une grande amélioration.

Nous commençons par définir le nouveau tableau `oddArray` car l'application de `filter()` créera un nouveau tableau. La fonction d'ordre supérieur retournera chaque élément qui répond à la condition définie dans la fonction anonyme qu'elle reçoit. La fonction anonyme est une fois de plus appliquée à chaque élément du tableau numbers.

## Puisque nous sommes sur une lancée – Un autre exemple de fonction d'ordre supérieur

Nous en sommes arrivés là, et je pense que vous commencez à voir pourquoi les fonctions d'ordre supérieur sont si bonnes !

Regardons un autre exemple...

Dans notre exemple `forEach()`, nous avons ajouté un à chaque nombre dans le tableau et enregistré chaque valeur dans la console. Mais qu'en est-il de créer un nouveau tableau avec ces nouvelles valeurs à la place ? Sans une fonction d'ordre supérieur, je pourrais faire ce qui suit :

```
const numbers = [1, 2, 3, 4, 5];

function addOneMore(array, newArr = []) {
  for (let i = 0; i < array.length; i++) {
    newArr.push(array[i] + 1);
  }
  return newArr;
}

const newArray = addOneMore(numbers);
console.log(newArray);

```

La fonction `addOneMore()` accepte une fois de plus un tableau et a un tableau comme deuxième paramètre qui a une valeur par défaut de vide. Un est ajouté à chaque élément du tableau numbers existant et le résultat est poussé vers le nouveau tableau qui est retourné.

Nous abstraisons cela avec la fonction d'ordre supérieur, `map()` :

```
const numbers = [1, 2, 3, 4, 5];

const newArray = numbers.map((number) => number + 1);
console.log(numbers);

```

Nous commençons par définir le newArray car `map()` crée un nouveau tableau. Comme `forEach()`, `map()` applique une fonction anonyme à chaque élément du tableau numbers. Cependant, `map()` crée un nouveau tableau dans le processus.

## Juste un dernier exemple

Que se passe-t-il si nous voulions trouver le total de toutes les valeurs dans le tableau numbers ?

Sans une fonction d'ordre supérieur, je pourrais faire ceci :

```
const numbers = [1, 2, 3, 4, 5];

function getTotalValue(array) {
  let total = 0;
  for (let i = 0; i < array.length; i++) {
    total += array[i];
  }
  return total;
}

const totalValue = getTotalValue(numbers);
console.log(totalValue);

```

La fonction `getTotalValue()` accepte un tableau, définit la variable total comme égale à zéro et parcourt le tableau tout en ajoutant chaque élément à la variable total. Enfin, elle retourne le total.

Avec la fonction d'ordre supérieur `reduce()`, ce processus peut encore une fois être abstrait :

```
const numbers = [1, 2, 3, 4, 5];

const totalValue = numbers.reduce((sum, number) => sum + number);
console.log(totalValue);

```

La fonction d'ordre supérieur `reduce()` attend deux paramètres dans la fonction anonyme à l'intérieur.

Le premier paramètre est un accumulateur et le deuxième paramètre est un élément du tableau numbers.

Le paramètre accumulateur (sum dans l'exemple ci-dessus) garde une trace du total lorsque `reduce()` applique la fonction anonyme à chaque élément du tableau.

## Conclusion

Les fonctions d'ordre supérieur fournissent un niveau d'abstraction plus élevé pour les fonctions.

Elles ont le potentiel d'élever votre code JavaScript à de nouveaux sommets !

Je vous laisse avec un tutoriel de ma chaîne YouTube qui applique les fonctions d'ordre supérieur aux données JSON.

%[https://youtu.be/7BeT6lsudL4]