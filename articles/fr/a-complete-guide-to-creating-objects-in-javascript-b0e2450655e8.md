---
title: Comment créer des objets en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-28T07:58:05.000Z'
originalURL: https://freecodecamp.org/news/a-complete-guide-to-creating-objects-in-javascript-b0e2450655e8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*S6zT7E9uySUcbD69OPQR8A.jpeg
tags:
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment créer des objets en JavaScript
seo_desc: 'By Kaashan Hussain

  We all deal with objects in one way or another while writing code in a programming
  language. In JavaScript, objects provide a way for us to store, manipulate, and
  send data over the network.

  There are many ways in which objects in ...'
---

Par Kaashan Hussain

Nous traitons tous des objets d'une manière ou d'une autre lors de l'écriture de code dans un langage de programmation. En JavaScript, les objets fournissent un moyen de stocker, manipuler et envoyer des données sur le réseau.

Il existe de nombreuses façons dont les objets en JavaScript diffèrent des objets dans d'autres langages de programmation grand public, comme Java. J'essaierai de couvrir cela dans un autre sujet. Ici, concentrons-nous uniquement sur les différentes façons dont JavaScript nous permet de créer des objets.

En JavaScript, pensez aux objets comme une collection de paires 'clé:valeur'. Cela nous amène à la première et la plus populaire façon de créer des objets en JavaScript.

Commençons.

#### 1. Créer des objets en utilisant la syntaxe littérale d'objet

C'est vraiment simple. Tout ce que vous avez à faire est de placer vos paires clé-valeur séparées par ':' à l'intérieur d'un ensemble d'accolades ({ }) et votre objet est prêt à être servi (ou consommé), comme ci-dessous :

```js
const person = {
  firstName: 'testFirstName',
  lastName: 'testLastName'
};
```

C'est la manière la plus simple et la plus populaire de créer des objets en JavaScript.

#### 2. Créer des objets en utilisant le mot-clé 'new'

Cette méthode de création d'objets ressemble à la façon dont les objets sont créés dans les langages basés sur les classes, comme Java. Au fait, à partir d'ES6, les classes sont natives en JavaScript également et nous verrons comment créer des objets en définissant des classes à la fin de cet article. Donc, pour créer un objet en utilisant le mot-clé 'new', vous avez besoin d'une fonction constructeur.

Voici 2 façons d'utiliser le motif du mot-clé 'new' :

**a) Utiliser le mot-clé 'new' avec la fonction constructeur Object intégrée**

Pour créer un objet, utilisez le mot-clé new avec le constructeur `Object()`, comme ceci :

```js
const person = new Object();
```

Maintenant, pour ajouter des propriétés à cet objet, nous devons faire quelque chose comme ceci :

```js
person.firstName = 'testFirstName';
person.lastName = 'testLastName';
```

Vous avez peut-être compris que cette méthode est un peu plus longue à taper. De plus, cette pratique n'est pas recommandée car il y a une résolution de portée qui se produit en coulisses pour trouver si la fonction constructeur est intégrée ou définie par l'utilisateur.

**b) Utiliser 'new' avec une fonction constructeur définie par l'utilisateur**

L'autre problème avec l'approche utilisant la fonction constructeur 'Object' provient du fait que chaque fois que nous créons un objet, nous devons ajouter manuellement les propriétés à l'objet créé.

Que se passerait-il si nous devions créer des centaines d'objets personne ? Vous pouvez imaginer la douleur maintenant. Donc, pour éviter d'ajouter manuellement des propriétés aux objets, nous créons des fonctions personnalisées (ou définies par l'utilisateur). Nous créons d'abord une fonction constructeur, puis utilisons le mot-clé 'new' pour obtenir des objets :

```js
function Person(fname, lname) {
  this.firstName = fname;
  this.lastName = lname;
}
```

Maintenant, chaque fois que vous voulez un objet 'Person', faites simplement ceci :

```js
const personOne = new Person('testFirstNameOne', 'testLastNameOne');
const personTwo = new Person('testFirstNameTwo', 'testLastNameTwo');
```

#### 3. Utiliser Object.create() pour créer de nouveaux objets

Ce motif est très pratique lorsque nous devons créer des objets à partir d'autres objets existants et non directement en utilisant la syntaxe du mot-clé 'new'. Voyons comment utiliser ce motif. Comme indiqué sur [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create) :

> La méthode `**Object.create()**` crée un nouvel objet, en utilisant un objet existant comme prototype de l'objet nouvellement créé.

Pour comprendre la méthode `**Object.create**`, rappelez-vous simplement qu'elle prend deux paramètres. Le premier paramètre est un objet obligatoire qui sert de prototype au nouvel objet à créer. Le deuxième paramètre est un objet optionnel qui contient les propriétés à ajouter au nouvel objet.

Nous n'approfondirons pas les prototypes et les chaînes d'héritage pour l'instant afin de rester concentrés sur le sujet. Mais comme point rapide, vous pouvez penser aux prototypes comme des objets à partir desquels d'autres objets peuvent emprunter des propriétés/méthodes dont ils ont besoin.

Imaginez que vous avez une organisation représentée par `orgObject`

```
const orgObject = { company: 'ABC Corp' };
```

Et vous voulez créer des employés pour cette organisation. Clairement, vous voulez tous les objets employés.

```js
const employee = Object.create(orgObject, { name: { value: 'EmployeeOne' } });

console.log(employee); // { company: "ABC Corp" }
console.log(employee.name); // "EmployeeOne"
```

#### 4. Utiliser Object.assign() pour créer de nouveaux objets

Que faire si nous voulons créer un objet qui doit avoir des propriétés de plus d'un objet ? `Object.assign()` vient à notre aide.

Comme indiqué sur [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign) :

> La méthode `Object**.**assign**()**` est utilisée pour copier les valeurs de toutes les propriétés énumérables propres d'un ou plusieurs objets sources vers un objet cible. Elle retournera l'objet cible.

La méthode `Object**_._**assign` peut prendre n'importe quel nombre d'objets comme paramètres. Le premier paramètre est l'objet qu'elle créera et retournera. Les autres objets qui lui sont passés seront utilisés pour copier les propriétés dans le nouvel objet. Comprenons-le en étendant l'exemple précédent que nous avons vu.

Supposons que vous avez deux objets comme ci-dessous :

```js
const orgObject = { company: 'ABC Corp' }
const carObject = { carName: 'Ford' }
```

Maintenant, vous voulez un objet employé de 'ABC Corp' qui conduit une voiture 'Ford'. Vous pouvez faire cela avec l'aide de `Object.assign` comme ci-dessous :

`const employee = Object.assign({}, orgObject, carObject);`

Maintenant, vous obtenez un objet `employee` qui a `company` et `carName` comme propriétés.

```js
console.log(employee); // { carName: "Ford", company: "ABC Corp" }
```

#### 5. Utiliser les classes ES6 pour créer des objets

Vous remarquerez que cette méthode est similaire à l'utilisation de 'new' avec une fonction constructeur définie par l'utilisateur. Les fonctions constructeur sont maintenant remplacées par des classes car elles sont supportées par les spécifications ES6. Voyons le code maintenant.

```js
class Person {
  constructor(fname, lname) {
    this.firstName = fname;
    this.lastName = lname;
  }
}

const person = new Person('testFirstName', 'testLastName');

console.log(person.firstName); // testFirstName
console.log(person.lastName); // testLastName


```

Ce sont toutes les façons que je connais pour créer des objets en JavaScript. J'espère que vous avez apprécié cet article et que vous comprenez maintenant comment créer des objets.

_Merci d'avoir pris le temps de lire cet article. Si vous avez aimé cet article et qu'il vous a été utile, veuillez cliquer sur le bouton d'applaudissement ? pour montrer votre soutien. Continuez à apprendre !_