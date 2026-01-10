---
title: Comment accéder aux propriétés d'un tableau d'objets en JavaScript
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2024-02-29T00:59:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-access-properties-from-an-array-of-objects-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/david-rangel-4m7gmLNr3M0-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment accéder aux propriétés d'un tableau d'objets en JavaScript
seo_desc: 'When you''re working with JavaScript applications, it''s common to work
  with arrays, nested arrays, and an array of objects. But a lot of beginners sometimes
  struggle with knowing how to access properties from these different data structures.

  In this a...'
---

Lorsque vous travaillez avec des applications JavaScript, il est courant de manipuler des tableaux, des tableaux imbriqués et des tableaux d'objets. Mais beaucoup de débutants ont parfois du mal à savoir comment accéder aux propriétés de ces différentes structures de données.

Dans cet article, nous allons discuter de la manière d'accéder aux propriétés de divers tableaux et examiner quelques exemples de code.

## Qu'est-ce qu'un tableau en JavaScript ?

Un tableau est un type de structure de données en JavaScript qui est utilisé pour stocker une collection d'éléments pouvant être de différents types.

Vous pouvez avoir un tableau de chaînes de caractères, comme ceci :

```js
const fruits = ["apple", "banana", "mango", "orange"];
```

Vous pouvez avoir un tableau de nombres :

```js
const numbers = [1, 2, 3, 4, 5];
```

Vous pouvez avoir un tableau imbriqué de tableaux comme ceci :

```js
const nestedArray = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];
```

Vous pouvez également avoir un tableau de types de données mixtes :

```js
const mixedArray = ["apple", 1, "banana", 2, "mango", 3];
```

## Comment accéder aux éléments d'un tableau en JavaScript

Pour accéder à un élément d'un tableau, vous référencez le nom du tableau, suivi d'une paire de crochets contenant l'index de l'élément auquel vous souhaitez accéder.

Voici un exemple d'accès au premier élément du tableau `fruits` :

```js
const fruits = ["apple", "banana", "mango", "orange"];
console.log(fruits[0]); // apple
```

Les tableaux sont indexés à partir de zéro, ce qui signifie que le premier élément du tableau a un index de 0, le deuxième élément a un index de 1, et ainsi de suite.

Si vous souhaitez accéder au dernier élément d'un tableau, vous pouvez utiliser la longueur du tableau moins 1.

```js
const fruits = ["apple", "banana", "mango", "orange"];
console.log(fruits[fruits.length - 1]); // orange
```

Parfois, cela peut devenir confus lorsque vous traitez un tableau imbriqué de tableaux. Mais la syntaxe reste la même lorsque vous souhaitez accéder à un élément d'un tableau imbriqué.

Voici un exemple d'accès au premier élément du premier tableau dans le `nestedArray` :

```js
const nestedNumberArray = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];
console.log(nestedNumberArray[0][0]); // 1
```

`nestedNumberArray[0]` pointe vers ce tableau ici :

```js
[1, 2, 3];
```

Pour accéder au premier élément de ce tableau, vous utilisez une autre paire de crochets avec l'index de l'élément auquel vous souhaitez accéder.

```js
nestedNumberArray[0][0];
```

## Comment accéder aux propriétés d'un tableau d'objets en JavaScript

Il est fréquent de rencontrer un tableau d'objets en JavaScript.

Voici un exemple avec un tableau de développeurs. Chaque développeur a un nom, un âge et un tableau de langages de programmation qu'il connaît.

```js
const developers = [
  { name: "John", age: 25, languages: ["JavaScript", "Python"] },
  { name: "Kelly", age: 37, languages: ["Ruby", "Python", "C", "C++"] },
  { name: "Zack", age: 45, languages: ["Go", "C#"] },
];
```

Si vous souhaitez accéder au nom du premier développeur, vous pouvez utiliser la syntaxe suivante :

```js
console.log(developers[0].name); // John
```

Ici, nous utilisons une combinaison de notation par point et par crochets pour accéder à la propriété name du premier objet développeur dans le tableau `developers`.

`developers[0]` est le premier objet développeur

```js
{ name: "John", age: 25, languages: ["JavaScript", "Python"] }
```

Ensuite, nous utilisons la notation par point (`developers[0].name`) pour accéder à la propriété `name` de cet objet.

## Comment trouver une valeur spécifique dans un tableau d'objets en JavaScript

Si nous cherchons un objet spécifique dans un tableau d'objets, nous pouvons utiliser la méthode `find`. La méthode `find` retourne le premier élément du tableau qui satisfait la fonction de test fournie. Si aucun élément ne passe le test, `undefined` est retourné.

Voici un exemple d'utilisation de la méthode `find` pour un tableau de nombres :

```js
const numbers = [1, 2, 3, 4, 5];

const foundNumber = numbers.find((number) => number > 3); // 4
```

L'exemple suivant parcourt le tableau de nombres et retourne le premier nombre supérieur à 3. Dans ce cas, la méthode `find` retourne le nombre 4.

Nous pouvons appliquer le même concept pour trouver un objet spécifique dans un tableau d'objets.

Dans l'exemple suivant, nous cherchons l'objet développeur avec le nom "Kelly".

```js
const developers = [
  { name: "John", age: 25, languages: ["JavaScript", "Python"] },
  { name: "Kelly", age: 37, languages: ["Ruby", "Python", "C", "C++"] },
  { name: "Zack", age: 45, languages: ["Go", "C#"] },
];

developers.find((developer) => developer.name === "Kelly");
```

Dans cet exemple, `developer` représente chaque objet dans le tableau. La méthode `find` parcourra le tableau `developers` et retournera le premier objet développeur dont le nom est "Kelly".

```js
{ name: "Kelly", age: 37, languages: ["Ruby", "Python", "C", "C++"] }
```

## Conclusion

J'espère que vous avez trouvé cet article utile pour apprendre à propos des tableaux et comment accéder à leurs propriétés.

Nous avons examiné quelques exemples de tableaux ainsi que la manière d'accéder aux éléments de tableaux imbriqués et de tableaux d'objets.

Nous avons également appris à propos de la méthode `find` et comment l'utiliser pour trouver un objet spécifique dans un tableau d'objets.

Maintenant, vous devriez avoir une meilleure compréhension de la manière de travailler avec des tableaux et des objets en JavaScript.

Bon codage ! 🚀