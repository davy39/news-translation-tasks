---
title: 5 Conseils JavaScript Qui Vous Feront Gagner du Temps
subtitle: ''
author: Gaël Thomas
co_authors: []
series: null
date: '2020-11-19T16:54:42.000Z'
originalURL: https://freecodecamp.org/news/time-saving-javascript-tips
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/time-saving-javascript-tips.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: tips
  slug: tips
seo_title: 5 Conseils JavaScript Qui Vous Feront Gagner du Temps
seo_desc: 'I''ve always wanted to create videos around my programming hobby. But I''m
  not a native English speaker, and I was scared to try.

  But a few weeks ago, while I was preparing some JavaScript tips to start my YouTube
  journey, I wrote this list of time-sav...'
---

J'ai toujours voulu créer des vidéos autour de ma passion pour la programmation. Mais je ne suis pas un locuteur natif anglais, et j'avais peur d'essayer.

Mais il y a quelques semaines, alors que je préparais quelques conseils JavaScript pour commencer mon aventure YouTube, j'ai écrit cette liste de conseils pour gagner du temps. J'espère qu'ils vous aideront comme ils m'ont aidé.

Dans cet article, je vais partager avec vous 5 conseils utiles en JavaScript (êtes-vous prêt à plonger ? 😀).

Et maintenant, devinez quoi ? Certains de ces conseils sont sur [ma chaîne YouTube](https://www.youtube.com/channel/UCSRuzHhjUaAnBb6_rmlr10g)📹 ! (voici [la playlist](https://www.youtube.com/playlist?list=PL-P9AMQZdy2aj3uLhjHagEsfTOrVqF7AR).


## Destructuration d'Objets

La destructuration est une fonctionnalité introduite dans ES6. C'est l'une des fonctionnalités que vous utiliserez quotidiennement une fois que vous saurez comment.

Elle vous aide à gérer trois problèmes principaux :

- **Répétition.** Chaque fois que vous voulez extraire une propriété d'un objet et créer une nouvelle variable, vous créez une nouvelle ligne.

```javascript
const user = {
  firstName: "John",
  lastName: "Doe",
  password: "123",
};

// Wow... devrions-nous afficher
// le mot de passe de John comme ça ?

const firstName = user.firstName;
const lastName = user.lastName;
const password = user.password;
```

- **Accessibilité.** Chaque fois que vous voulez accéder à une propriété d'un objet, vous devez écrire le chemin pour y accéder. (**exemple :** `user.firstName`, `user.family.sister`, etc.).
- **Utilisation.** Par exemple, lorsque vous créez une nouvelle fonction et que vous ne travaillez qu'avec une seule propriété d'un objet.

Maintenant que vous avez vu quels sont ces trois problèmes avec les objets, comment pensez-vous pouvoir les résoudre ?

### Comment Résoudre le Problème de Répétition

```javascript
const user = {
  firstName: "John",
  lastName: "Doe",
  password: "123",
};

const { firstName, lastName, password } = user;

console.log(firstName, lastName, password);
// Résultat : 'John', 'Doe', '123'
```

La destructuration est le processus d'extraction d'une propriété d'un objet par sa clé. En prenant une clé existante dans votre objet, puis en la plaçant entre deux accolades (`{ firstName }`), vous dites à JavaScript :

"Hey JavaScript, je veux créer une variable avec le même nom que ma propriété. Je veux créer une variable `firstName` pour la propriété `firstName` de mon objet."

> **Note :** Si vous voulez destructurer un objet, vous devez toujours utiliser une clé existante. Sinon, cela ne fonctionnera pas.

### Comment Résoudre le Problème d'Accessibilité

```javascript
const user = {
  firstName: "John",
  lastName: "Doe",
  password: "123",
  family: {
    sister: {
      firstName: "Maria",
    },
  },
};

// Nous accédons à l'objet imbriqué `sister`
// et nous extrayons la propriété `firstName`
const { firstName } = user.family.sister;

console.log(firstName);
// Résultat : 'Maria'
```

Lorsque vous travaillez avec des objets imbriqués, cela peut devenir assez répétitif et prendre beaucoup de temps pour accéder à la même propriété plusieurs fois.

En utilisant la destructuration, en une seule ligne, vous pouvez réduire le chemin de la propriété à une seule variable.

### Comment Résoudre le Problème d'Utilisation

Maintenant que vous savez comment destructurer un objet, laissez-moi vous montrer comment extraire des propriétés directement dans la définition des paramètres de votre fonction.

Si vous connaissez React, vous êtes probablement déjà familier avec cela.

```javascript
function getUserFirstName({ firstName }) {
  return firstName;
}

const user = {
  firstName: "John",
  lastName: "Doe",
  password: "123",
};

console.log(getUserFirstName(user));
// Résultat : 'John'
```

Dans l'exemple ci-dessus, nous avons une fonction `getUserFirstName`, et nous savons qu'elle n'utilisera qu'une seule propriété de notre objet, `firstName`.

Plutôt que de passer l'objet entier ou de créer une nouvelle variable, nous pouvons destructurer les paramètres de la fonction de l'objet.

## Comment Fusionner des Objets en ES6

En programmation, vous devez souvent résoudre des problèmes avec des structures de données. Grâce à [l'opérateur de décomposition](https://herewecode.io/blog/spread-operator-in-javascript/) introduit dans ES6, les manipulations d'objets et de tableaux sont plus simples.

```javascript
const user = {
  firstName: "John",
  lastName: "Doe",
  password: "123",
};

const userJob = {
  jobName: "Developer",
  jobCountry: "France",
  jobTimePerWeekInHour: "35",
};
```

Imaginons que nous avons deux objets :

- **User.** Un objet définissant des informations générales sur l'utilisateur.
- **UserJob.** Un objet définissant les informations professionnelles de l'utilisateur.

Nous voulons créer un seul objet qui ne contient que les propriétés de ces deux objets.

```javascript
const user = {
  firstName: "John",
  lastName: "Doe",
  password: "123",
};

const userJob = {
  jobName: "Developer",
  jobCountry: "France",
  jobTimePerWeekInHour: "35",
};

const myNewUserObject = {
  ...user,
  ...userJob,
};

console.log(myNewUserObject);
// Résultat :
//{
//  firstName: 'John',
//  lastName: 'Doe',
//  password: '123',
//  jobName: 'Developer',
//  jobCountry: 'France',
//  jobTimePerWeekInHour: '35'
//}
```

En utilisant l'opérateur de décomposition (`...`), nous pouvons extraire toutes les propriétés d'un objet vers un autre.

```javascript
const user = {
  firstName: "John",
  lastName: "Doe",
  password: "123",
};

const myNewUserObject = {
  ...user,
  // Nous extrayons :
  // - firstName
  // - lastName
  // - password
  // et nous les envoyons à
  // un nouvel objet `{}`
};
```

### Comment Fusionner des Tableaux

```javascript
const girlNames = ["Jessica", "Emma", "Amandine"];
const boyNames = ["John", "Terry", "Alexandre"];

const namesWithSpreadSyntax = [...girlNames, ...boyNames];

console.log(namesWithSpreadSyntax);
// Résultat : ['Jessica', 'Emma', 'Amandine', 'John', 'Terry', 'Alexandre']
```

Comme pour les objets, l'opérateur de décomposition (`...`) extrait tous les éléments d'un tableau vers un autre.

```javascript
const girlNames = ["Jessica", "Emma", "Amandine"];

const newNewArray = [
  ...girlNames,
  // Nous extrayons :
  // - 'Jessica'
  // - 'Emma'
  // - 'Amandine'
  // et nous les envoyons à
  // un nouveau tableau `[]`
];
```

### Comment Supprimer les Doublons dans un Tableau

Parce que les tableaux sont des listes, vous pouvez avoir plusieurs éléments de la même valeur. Si vous voulez supprimer les doublons dans votre tableau, vous pouvez suivre l'un des exemples ci-dessous.

L'un d'eux ne sera qu'une seule ligne grâce à ES6, mais je laisse l'exemple "ancien" pour que vous puissiez comparer.

#### Comment supprimer les doublons dans un tableau "à l'ancienne"

```javascript
const animals = ["owl", "frog", "canary", "duck", "duck", "goose", "owl"];

const uniqueAnimalsWithFilter = animals.filter(
  // Exemple de paramètres : 'owl', 0, ['owl', 'frog', 'canary', 'duck', 'duck', 'goose', 'owl']
  (animal, index, array) => array.indexOf(animal) == index
);

console.log(uniqueAnimalsWithSet);
// Résultat : ['owl', 'frog', 'canary', 'duck', 'goose']
```

Dans l'exemple ci-dessus, nous voulons nettoyer le tableau `animals` en supprimant tous les doublons.

Nous pouvons le faire en utilisant la fonction `filter` avec `indexOf` à l'intérieur.

La fonction `filter` prend tous les éléments du tableau `animals` (`animals.filter`). Ensuite, pour chaque occurrence, elle fournit :

- la valeur actuelle (**exemple :** `duck`)
- l'index (**exemple :** 0)
- le tableau initial (**exemple :** le tableau `animals` => `['owl', 'frog', 'canary', 'duck', 'duck', 'goose', 'owl']`)

Nous appliquerons `indexOf` sur le tableau original pour chaque occurrence et donnerons comme paramètre la variable `animal` (la valeur actuelle).

`indexOf` retournera le premier index de la valeur actuelle (**exemple :** pour 'owl' l'index est 0).

Ensuite, à l'intérieur du filter, nous comparons la valeur de `indexOf` à l'index actuel. Si c'est la même, nous retournons `true` sinon `false`.

`filter` créera un nouveau tableau avec seulement les éléments où la valeur retournée était `true`.

Donc, dans notre cas : `['owl', 'frog', 'canary', 'duck', 'goose']`.


### Comment supprimer les doublons dans un tableau "à la nouvelle manière"

Bien, la méthode "ancienne" est intéressante à comprendre, mais elle est longue et un peu difficile. Alors, découvrons la nouvelle méthode maintenant :

```javascript
const animals = ["owl", "frog", "canary", "duck", "duck", "goose", "owl"];

const uniqueAnimalsWithSet = [...new Set(animals)];

console.log(uniqueAnimalsWithSet);
// Résultat : ['owl', 'frog', 'canary', 'duck', 'goose']
```

Décortiquons les différentes étapes :

```javascript
// 1
const animals = ["owl", "frog", "canary", "duck", "duck", "goose", "owl"];

// 2
const animalsSet = new Set(animals);

console.log(animalsSet);
// Résultat : Set { 'owl', 'frog', 'canary', 'duck', 'goose' }

// 3
const uniqueAnimalsWithSet = [...animalsSet];

console.log(uniqueAnimalsWithSet);
// Résultat : ['owl', 'frog', 'canary', 'duck', 'goose']
```

Nous avons un tableau `animals`, et nous le convertissons en un `Set`, qui est un type spécial d'objet dans ES6.

Ce qui est différent avec lui, c'est qu'il vous permet de créer une collection de valeurs uniques.

> **Note :** `Set` est une collection de valeurs uniques, mais ce n'est pas un `Array`.

Une fois que nous avons notre objet `Set` avec des valeurs uniques, nous devons le reconvertir en tableau.

Pour cela, nous utilisons les opérateurs de décomposition pour le destructurer et envoyer toutes les propriétés à un nouveau `Array`.

Parce que l'objet `Set` a des propriétés uniques, notre nouveau tableau aura également uniquement des valeurs uniques.

## Comment Utiliser les Opérateurs Ternaires

Avez-vous déjà entendu parler d'une manière d'écrire de petites conditions en une seule ligne ?

Si ce n'est pas le cas, il est temps de supprimer beaucoup de vos blocs `if` et `else` et de les convertir en petites opérations ternaires.

Regardons un exemple avec `console.log` pour commencer. L'idée est de vérifier la valeur d'une variable et d'afficher conditionnellement une sortie.

```javascript
const colour = "blue";

if (colour === "blue") {
  console.log(`It's blue!`);
} else {
  console.log(`It's not blue!`);
}
```

Cet exemple est un cas typique où vous pouvez utiliser [l'opérateur ternaire](https://herewecode.io/blog/ternary-operator-in-javascript/) pour réduire ces 5 lignes `if` et `else` à une seule !

**Une ligne pour les gouverner tous !**

```javascript
const colour = "blue";

colour === "blue" ? console.log(`It's blue!`) : console.log(`It's not blue!`);
// [condition] ? [if] : [else]
```

Les opérateurs ternaires remplacent `if` et `else` pour les petites conditions.

> **Note :** Il n'est pas recommandé de créer des conditions complexes avec des opérateurs ternaires car cela peut réduire la lisibilité.

Ci-dessous se trouve un autre exemple qui utilise des opérateurs ternaires, mais cette fois dans le `return` d'une fonction.

```javascript
function sayHelloToAnne(name) {
  return name === "Anne" ? "Hello, Anne!" : "It's not Anne!";
}

console.log(sayHelloToAnne("Anne"));
// Résultat : 'Hello, Anne!'

console.log(sayHelloToAnne("Gael"));
// Résultat : "It's not Anne!"
```

## Vous Voulez Contribuer ? Voici Comment.

Vous êtes les bienvenus pour contribuer à ce dépôt GitHub. Toute contribution est appréciée et cela aidera chacun d'entre nous à améliorer nos compétences en JavaScript.
[GitHub : JavaScript Awesome Tips](https://github.com/gael-thomas/javascript-awesome-tips)

## Conclusion

J'espère que vous avez appris de nouvelles choses sur JavaScript en lisant cet article.

Si vous voulez plus de contenu comme celui-ci, vous pouvez [me suivre sur Twitter](https://twitter.com/gaelgthomas/) où je tweete sur le développement web, l'amélioration personnelle et mon parcours en tant que développeur full stack !