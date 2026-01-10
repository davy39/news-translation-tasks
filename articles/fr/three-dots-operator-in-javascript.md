---
title: '... en JavaScript – l''opérateur trois points en JS'
date: '2022-08-10T23:38:25.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/three-dots-operator-in-javascript
posteditor: ''
proofreader: ''
author: Joel Olawanle
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/cover-template--1-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_desc: 'The three dots operator in JavaScript is one of the significant updates
  that was shipped with ES6.

  This operator (...) helps you achieve many things that previously required many
  lines of code, unfamiliar syntax, and more.

  In this short article, you ...'
---


Par Joel Olawanle

<!-- more -->

L'opérateur trois points en JavaScript est l'une des mises à jour majeures introduites avec ES6.

Cet opérateur (`...`) vous permet de réaliser de nombreuses choses qui nécessitaient auparavant de nombreuses lignes de code, une syntaxe peu familière, et plus encore.

Dans ce court article, vous apprendrez ce que signifie l'opérateur trois points et ce qu'il fait. Nous passerons en revue quelques exemples pour montrer les cas d'utilisation possibles, et nous verrons comment vous aviez l'habitude d'effectuer ces opérations. De cette façon, vous verrez ce que les trois points vous offrent en tant que développeur JavaScript.

L'opérateur trois points a deux significations différentes en JavaScript. La syntaxe est très similaire, mais vous utilisez chacune d'elles dans des contextes différents. Ces deux utilisations différentes du `...` sont les opérateurs spread et rest.

## Comment utiliser l'opérateur spread en JavaScript

En JavaScript, vous utilisez l'opérateur spread pour étendre un itérable à l'intérieur d'un récepteur spécifié, comme son nom l'indique.

Ce récepteur peut être n'importe quoi, comme un objet, un tableau, etc. Et l'itérable peut être tout ce que nous pouvons parcourir, y compris une chaîne de caractères, un tableau, un objet, et ainsi de suite.

### Syntaxe de l'opérateur spread :

```
const newArray = ['firstItem', ...oldArray];
```

Voyons maintenant différents cas dans lesquels nous pouvons utiliser l'opérateur spread.

### Comment copier un tableau avec l'opérateur spread

Lorsque nous voulons copier les éléments d'un tableau particulier dans un nouveau tableau sans affecter le tableau d'origine, nous pouvons utiliser l'opérateur spread.

Voici un exemple :

```
let studentNames = ["Daniel", "Jane", "Joe"];

let names = [...studentNames];

console.log(names); // ["Daniel","Jane","Joe"]
```

Cela nous épargne le temps que nous utiliserions pour écrire une boucle :

```
let studentNames = ["Daniel", "Jane", "Joe"];

let names = [];

studentNames.map((name) => {
    names.push(name);
});

console.log(names); // ["Daniel","Jane","Joe"]
```

### Comment copier un objet avec l'opérateur spread

Comme nous l'avons fait avec les tableaux, vous pouvez également utiliser un objet comme récepteur pour l'opérateur spread.

```
let user = { name: "John Doe", age: 10 };

let copiedUser = { ...user };
console.log(copiedUser); // { name: "John Doe", age: 10 }
```

Alors qu'une ancienne façon de faire cela aurait été d'utiliser la méthode `Object.assign()` de cette manière :

```
let user = { name: "John Doe", age: 10 };

let copiedUser = Object.assign({}, user);
console.log(copiedUser); // { name: "John Doe", age: 10 }
```

### Comment concaténer ou fusionner des tableaux avec l'opérateur spread

Lorsque nous avons deux tableaux ou plus que nous voulons fusionner dans un nouveau tableau, nous pouvons facilement le faire avec l'opérateur spread. Il nous permet de copier les éléments d'un tableau :

```
let maleNames = ["Daniel", "Peter", "Joe"];
let femaleNames = ["Sandra", "Lucy", "Jane"];

let allNames = [...maleNames, ...femaleNames];

console.log(allNames); // ["Daniel","Peter","Joe","Sandra","Lucy","Jane"]
```

Il est également important de savoir que nous pouvons utiliser la même approche pour autant de tableaux que nous le souhaitons. Nous pouvons également ajouter des éléments individuels au sein du tableau :

```
let maleNames = ["Daniel", "Peter", "Joe"];
let femaleNames = ["Sandra", "Lucy", "Jane"];
let otherNames = ["Bill", "Jill"];

let moreNames = [...otherNames, ...femaleNames, ...maleNames];
let names = [...moreNames, "Ben", "Fred"];
```

Cela nous évite d'utiliser une syntaxe compliquée comme la méthode `concat()` :

```
let maleNames = ["Daniel", "Peter", "Joe"];
let femaleNames = ["Sandra", "Lucy", "Jane"];
let otherNames = ["Bill", "Jill"];

let allNames = femaleNames.concat(maleNames);
let moreNames = femaleNames.concat(maleNames, otherNames);
```

### Comment concaténer ou fusionner des objets avec l'opérateur spread

Nous pouvons également concaténer des objets de manière similaire à ce que nous avons fait pour les tableaux avec l'opérateur spread :

```
let userName = { name: "John Doe" };
let userSex = { sex: "Male" };

let user = { ...userName, ...userSex };

console.log(user); // { name: "John Doe", sex: "Male" }
```

**Note :** Dans une situation où une clé possède une autre propriété, la dernière propriété écrase la première instance :

```
let userName = { name: "John Doe" };
let userSex = { sex: "Female", name: "Jane Doe" };

let user = { ...userName, ...userSex }; // { name: "Jane Doe", sex: "Female" }
```

### Comment récupérer des éléments uniques avec la méthode Set

Une situation importante où vous utiliserez l'opérateur spread est lorsque vous essayez de récupérer des éléments uniques d'un tableau vers un autre.

Par exemple, supposons que nous ayons un tableau de fruits dans lequel nous avons répété certains fruits, et que nous voulions extraire ces fruits dans un nouveau tableau en évitant la répétition. Nous pouvons utiliser la méthode `Set()` aux côtés de l'opérateur spread pour les lister dans un nouveau tableau :

```
let fruits = ["Mango", "Apple", "Mango", "Banana", "Mango"];

let uniqueFruits = [...new Set(fruits)];
console.log(uniqueFruits); // ["Mango","Apple","Banana"]
```

### Comment passer des éléments de tableau dans des appels de fonction avec l'opérateur spread

Lorsque vous avez une fonction qui prend des nombres et que vous avez ces nombres comme éléments d'un tableau :

```
let scores = [12, 33, 6]

const addAll = (a, b, c) => {
    console.log(a + b + c);
};
```

Vous pouvez utiliser l'opérateur spread pour passer ces éléments dans l'appel de fonction en tant qu'arguments :

```
let scores = [12, 33, 6]

const addAll = (a, b, c) => {
    console.log(a + b + c);
};

addAll(...scores); // 51
```

Une ancienne méthode pour faire cela aurait été d'utiliser la méthode `apply()` :

```
let scores = [12, 33, 6]

const addAll = (a, b, c) => {
    console.log(a + b + c);
};

addAll.apply(null, scores); // 51
```

### Comment diviser des chaînes de caractères en caractères à l'aide de l'opérateur spread

Supposons que nous ayons une chaîne de caractères. Nous pouvons utiliser l'opérateur spread pour la diviser en caractères :

```
let myString = "freeCodeCamp";

const splitString = [...myString];

console.log(splitString); // ["f","r","e","e","C","o","d","e","C","a","m","p"]
```

Ceci est similaire à la méthode `split()` :

```
let myString = "freeCodeCamp";

const splitString = myString.split('');

console.log(splitString); // ["f","r","e","e","C","o","d","e","C","a","m","p"]
```

## Comment utiliser l'opérateur rest en JavaScript

D'un autre côté, l'opérateur rest vous permet de combiner n'importe quel nombre d'arguments dans un tableau, puis d'en faire ce que vous voulez. Il utilise un tableau pour représenter un nombre infini d'arguments.

### Syntaxe de l'opérateur rest

```
const func = (first, ...rest) => {};
```

Un exemple parfait pour illustrer cela serait si nous avions une liste de nombres et que nous voulions utiliser le premier nombre comme multiplicateur. Nous voulons ensuite mettre la valeur multipliée des nombres restants dans un tableau :

```
const multiplyArgs = (multiplier, ...otherArgs) => {
    return otherArgs.map((number) => {
    return number * multiplier;
    });
};

let multipiedArray = multiplyArgs(6, 5, 7, 9);

console.log(multipiedArray); // [30,42,54]
```

Voici une bonne représentation de l'opérateur rest et de ce à quoi ressemble sa valeur :

```
const multiplyArgs = (multiplier, ...otherArgs) => {
    console.log(multiplier); // 6
    console.log(otherArgs); // [5,7,9]
};

multiplyArgs(6, 5, 7, 9);
```

**Note :** Le paramètre rest doit être le dernier paramètre formel.

```
const multiplyArgs = (multiplier, ...otherArgs, lastNumber) => {
    console.log(lastNumber); // Uncaught SyntaxError: Rest parameter must be last formal parameter
};

multiplyArgs(6, 5, 7, 9);
```

## Différence entre les opérateurs spread et rest en JavaScript

À ce stade, vous pourriez être confus car les deux méthodes semblent assez similaires. Mais l'équipe JS a fait un excellent travail avec le nommage, car il définit ce que fait chaque utilisation de `...`.

Nous utilisons l'opérateur spread pour étendre (répartir) les valeurs d'un tableau ou des itérables dans, par exemple, un tableau ou un objet.

Tandis que nous utilisons l'opérateur rest pour rassembler les éléments restants passés dans une fonction sous forme de tableau.

```
const myFunction = (name1, ...rest) => { // opérateur rest utilisé ici
    console.log(name1);
    console.log(rest);
};

let names = ["John", "Jane", "John", "Joe", "Joel"];
myFunction(...names); // opérateur spread utilisé ici
```

## Conclusion

Dans cet article, vous avez appris ce que signifie l'opérateur trois points en JavaScript. Vous avez également vu les différents cas où vous pouvez utiliser l'opérateur trois points ainsi que ses deux significations/cas d'utilisation différents.

Bon code !

Vous pouvez accéder à plus de 200 de mes articles en [visitant mon site web][1]. Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.

[1]: https://joelolawanle.com/contents