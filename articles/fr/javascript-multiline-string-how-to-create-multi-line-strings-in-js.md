---
title: Chaînes de caractères multilingues en JavaScript – Comment créer des chaînes
  de caractères sur plusieurs lignes en JS
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-08-10T15:54:42.000Z'
originalURL: https://freecodecamp.org/news/javascript-multiline-string-how-to-create-multi-line-strings-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-mateusz-dach-2811648.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Chaînes de caractères multilingues en JavaScript – Comment créer des chaînes
  de caractères sur plusieurs lignes en JS
seo_desc: 'In this article, you will learn three different ways to create multiline
  strings in JavaScript.

  I will first explain the basics of strings in JavaScript and go over how to use
  template literals. Then, you will learn how to create a string that spans ...'
---

Dans cet article, vous apprendrez trois façons différentes de créer des chaînes de caractères multilingues en JavaScript.

Je vais d'abord expliquer les bases des chaînes de caractères en JavaScript et passer en revue comment utiliser les littéraux de gabarit. Ensuite, vous apprendrez comment créer une chaîne de caractères qui s'étend sur plusieurs lignes à l'aide d'exemples de code tout au long du processus.

Voici ce que nous allons couvrir :

1. [Qu'est-ce qu'une chaîne de caractères en JavaScript ?](#definition)
    1. [Qu'est-ce qu'un littéral de gabarit ? Pourquoi et comment utiliser les littéraux de gabarit](#template-literal)
2. [Comment créer des chaînes de caractères multilingues](#multiline)
    1. [Comment créer des chaînes de caractères multilingues avec des littéraux de gabarit](#multiline-template)
    2. [Comment créer des chaînes de caractères multilingues en utilisant l'opérateur `+`](#operator-1)
    3. [Comment créer des chaînes de caractères multilingues en utilisant l'opérateur `\`](#operator-2)

## Qu'est-ce qu'une chaîne de caractères en JavaScript ? Une introduction sur comment créer une chaîne de caractères en JS <a name="definition"></a>

Les chaînes de caractères sont un moyen efficace de communiquer par le texte.

Une chaîne de caractères est une séquence ordonnée de valeurs de caractères. Plus précisément, une chaîne de caractères est une séquence d'un ou plusieurs caractères qui peuvent être des lettres, des nombres ou des symboles (tels que des marques de ponctuation).

Il existe trois façons de créer une chaîne de caractères en JavaScript :

- En utilisant des guillemets simples.
- En utilisant des guillemets doubles.
- En utilisant des backticks.

Voici comment créer une chaîne de caractères en utilisant des **guillemets simples** :

```js
// chaîne de caractères créée en utilisant des guillemets simples ('')
let favePhrase = 'Hello World!';
```

Voici comment créer une chaîne de caractères en utilisant des **guillemets doubles** :

```js
// chaîne de caractères créée en utilisant des guillemets doubles ("")
let favePhrase = "Hello World!";
```

Voici comment créer une chaîne de caractères en utilisant des **backticks** :

```js
// chaîne de caractères créée en utilisant des backticks (``)
let favePhrase = `Hello World!`;
```

La dernière façon de créer des chaînes de caractères en JavaScript est connue sous le nom de **littéral de gabarit**.

J'ai créé une variable nommée `favePhrase`.

À l'intérieur de la variable, j'ai stocké la chaîne de caractères `Hello World!`, que j'ai créée de trois manières différentes.

Pour voir la sortie de la chaîne de caractères dans la console du navigateur, passez le nom de la variable à `console.log();`.

Par exemple, si je voulais voir la sortie de la chaîne de caractères créée avec des guillemets doubles, je ferais ce qui suit :

```js
// chaîne de caractères créée en utilisant des guillemets doubles ("")
let favePhrase = "Hello World!";

// imprimer la chaîne de caractères dans la console
console.log(favePhrase);

// sortie

// Hello World!
```

La création de chaînes de caractères en utilisant des guillemets simples ou doubles fonctionne de la même manière, il n'y a donc aucune différence entre les deux.

Vous pouvez choisir d'utiliser l'un ou l'autre ou les deux tout au long d'un fichier. Cela dit, il est bon de rester cohérent dans tout votre fichier.

Lors de la création d'une chaîne de caractères, assurez-vous que le type de guillemets que vous utilisez est le même des deux côtés.

```js
// Ne faites pas cela
let favePhrase = 'Hello World!";

console.log(favePhrase);

// sortie

// Uncaught SyntaxError: Invalid or unexpected token (at test.js:2:18)
```

Une autre chose à noter est que vous pouvez utiliser un type de guillemet à l'intérieur d'un autre.

Par exemple, vous pourriez utiliser des guillemets doubles à l'intérieur de guillemets simples, comme ceci :

```js
let favePhrase = 'My fave phrase is "Hello World"!';
```

Assurez-vous que les guillemets intérieurs ne correspondent pas aux guillemets extérieurs, car cela entraînerait une erreur :

```js
// Ne faites pas cela
let favePhrase = 'My fave phrase is 'Hello World'! ';

console.log(favePhrase)


// sortie

//Uncaught SyntaxError: Unexpected identifier (at test.js:2:38)
```

La même chose se produit lorsque vous essayez d'utiliser une apostrophe à l'intérieur de guillemets simples :

```js
// Ne faites pas cela
let favePhrase = 'My fave phrase is "Hello world"! Isn't it awesome?';

console.log(favePhrase);

// sortie

// Uncaught SyntaxError: Unexpected identifier (at test.js:3:56)
```

J'ai utilisé des guillemets doubles à l'intérieur de guillemets simples, et cela a fonctionné. Cependant, lorsque j'ai introduit l'apostrophe, le code s'est cassé.

La façon de faire fonctionner cela est d'échapper les guillemets simples en utilisant le caractère d'échappement `\` :

```js
let favePhrase = 'My fave phrase is \'Hello World\'! ';

console.log(favePhrase);

// sortie

// My fave phrase is 'Hello World'! 
```

Et pour faire fonctionner l'apostrophe, vous devriez faire ce qui suit :

```js
let favePhrase = 'My fave phrase is "Hello world"! Isn\'t it awesome?';

console.log(favePhrase);

// sortie

// My fave phrase is "Hello world"! Isn't it awesome?
```

### Qu'est-ce qu'un littéral de gabarit en JavaScript ? Pourquoi et comment utiliser les littéraux de gabarit en JavaScript <a name="template-literal"></a>

Plus tôt, vous avez vu que pour créer un littéral de gabarit, vous devez utiliser des backticks.

Les littéraux de gabarit ont été introduits avec ES6, et ils vous permettent d'effectuer des opérations plus complexes en utilisant des chaînes de caractères.

L'une de ces opérations est la possibilité d'intégrer une variable en ligne à l'intérieur d'une chaîne de caractères, comme ceci :

```js
let firstName = 'John';
let lastName = 'Doe';

console.log(`Hi! My first name is ${firstName} and my last name is ${lastName}!`);

// sortie

//Hi! My first name is John and my last name is Doe!
```

Dans l'exemple ci-dessus, j'ai créé deux variables, `firstName` et `lastName`, et j'ai stocké le prénom et le nom de famille d'une personne, respectivement.

Ensuite, en utilisant `console.log()`, j'ai imprimé une chaîne de caractères créée avec des backticks, également connue sous le nom de littéral de gabarit.

À l'intérieur de cette chaîne de caractères, j'ai intégré ces deux variables.

Pour ce faire, j'ai enveloppé les noms des variables dans `${}` - cela est également connu sous le nom d'**interpolation de chaînes de caractères** qui vous permet d'introduire n'importe quelles variables sans avoir à les concaténer comme ceci :

```js
let firstName = 'John';
let lastName = 'Doe';

console.log("Hi! My first name is " + firstName + " and my last name is " + lastName + "!");

// sortie

// Hi! My first name is John and my last name is Doe!
```

Une autre chose que les littéraux de gabarit vous permettent de faire est d'utiliser des guillemets simples, des guillemets doubles et des apostrophes à l'intérieur sans avoir besoin de les échapper :

```js
let favePhrase = `My fave phrase is "Hello World" ! Isn't it awesome?`

console.log(favePhrase);

// sortie

// My fave phrase is "Hello World" ! Isn't it awesome?
```

Les littéraux de chaînes de caractères vous permettent également de créer des chaînes de caractères multilingues, ce que vous apprendrez à faire dans la section suivante.

## Comment créer des chaînes de caractères multilingues en JavaScript <a name="multiline"></a>

Il existe trois façons de créer des chaînes de caractères qui s'étendent sur plusieurs lignes :

- En utilisant des littéraux de gabarit.
- En utilisant l'opérateur `+` – l'opérateur de concaténation JavaScript.
- En utilisant l'opérateur `\` – l'opérateur de barre oblique inverse JavaScript et le caractère d'échappement.

Si vous choisissez d'utiliser des guillemets simples ou doubles au lieu de littéraux de gabarit pour créer une chaîne de caractères qui s'étend sur plusieurs lignes, vous devriez utiliser soit l'opérateur `+`, soit l'opérateur `\`.

### Comment créer des chaînes de caractères multilingues avec des littéraux de gabarit en JavaScript <a name="multiline-template"></a>

Les littéraux de gabarit vous permettent de créer une chaîne de caractères qui s'étend sur plusieurs lignes :

```js
let learnCoding = `How to start learning web development?
- Learn HTML
- Learn CSS
- Learn JavaScript
Use freeCodeCamp to learn all the above and much, much more !
`

console.log(learnCoding);


// sortie

// How to start learning web development?
// - Learn HTML
// - Learn CSS
// - Learn JavaScript
// Use freeCodeCamp to learn all the above and much, much more !
```

L'utilisation de littéraux de gabarit est la manière la plus simple de créer des chaînes de caractères multilingues.

### Comment créer des chaînes de caractères multilingues en utilisant l'opérateur `+` en JavaScript <a name="operator-1"></a>

En prenant le même exemple de la section précédente, voici comment vous le réécririez en utilisant l'opérateur `+` :

```js
let learnCoding = 'How to start learning web development?' +
' - Learn HTML' +
' - Learn CSS' +
' - Learn JavaScript' +
' Use freeCodeCamp to learn all the above and much, much more!'


console.log(learnCoding);

// sortie

// How to start learning web development?  - Learn HTML - Learn CSS - Learn JavaScript Use freeCodeCamp to learn all the above and much, much more!
```

Vous devriez également inclure le caractère de nouvelle ligne `\n` pour faire apparaître les phrases sur une nouvelle ligne :

```js
let learnCoding = 'How to start learning web development?\n' +
' - Learn HTML\n' +
' - Learn CSS\n' +
' - Learn JavaScript\n' +
' Use freeCodeCamp to learn all the above and much, much more!'


console.log(learnCoding);

// sortie

//How to start learning web development?
// - Learn HTML
// - Learn CSS
// - Learn JavaScript
// Use freeCodeCamp to learn all the above and much, much more!
```

### Comment créer des chaînes de caractères multilingues en utilisant l'opérateur `\` en JavaScript <a name="operator-2"></a>

Si vous vouliez utiliser l'opérateur `\`, voici comment vous réécririez l'exemple de la section précédente :

```js
let learnCoding = 'How to start learning web development? \n \
 - Learn HTML \n \
 - Learn CSS\n  \
 - Learn JavaScript \n \
Use freeCodeCamp to learn all the above and much, much more!'
 

console.log(learnCoding);

// sortie

// let learnCoding = 'How to start learning web development? \n \
// - Learn HTML \n \
// - Learn CSS\n  \
// - Learn JavaScript \n \
//Use freeCodeCamp to learn all the above and much, much more!'


console.log(learnCoding);
```


Dans cet exemple, j'ai créé une chaîne de caractères multilingue en utilisant des guillemets simples.

J'ai d'abord dû utiliser le caractère de nouvelle ligne `\n` suivi de l'opérateur `\` pour faire en sorte que la chaîne de caractères s'étende sur plusieurs lignes.

Assurez-vous de placer l'opérateur `\` après le caractère de nouvelle ligne `\n`.

## Conclusion

Et voilà ! Vous savez maintenant comment créer des chaînes de caractères multilingues en JavaScript.

Pour en savoir plus sur JavaScript, rendez-vous sur la [Certification Algorithmes et Structures de Données JavaScript](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) de freeCodeCamp.

C'est un programme gratuit, bien pensé et structuré où vous apprendrez de manière interactive. À la fin, vous construirez également 5 projets pour obtenir votre certification et consolider vos connaissances.

Merci d'avoir lu !