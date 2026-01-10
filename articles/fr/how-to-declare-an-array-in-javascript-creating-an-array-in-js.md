---
title: Comment déclarer un tableau en JavaScript – Créer un tableau en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-11-14T21:38:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-declare-an-array-in-javascript-creating-an-array-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/cover-template--2-.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment déclarer un tableau en JavaScript – Créer un tableau en JS
seo_desc: 'In JavaScript, an array is one of the most commonly used data types. It
  stores multiple values and elements in one variable.

  These values can be of any data type — meaning you can store a string, number, boolean,
  and other data types in one variable....'
---

En JavaScript, un tableau est l'un des types de données les plus couramment utilisés. Il stocke plusieurs valeurs et éléments dans **une** seule variable.

Ces valeurs peuvent être de n'importe quel type de données — ce qui signifie que vous pouvez stocker une chaîne de caractères, un nombre, un booléen et d'autres types de données dans une seule variable.

Il existe deux méthodes standard pour déclarer un tableau en JavaScript. Ces méthodes sont soit via le constructeur de tableau, soit via la notation littérale.

Si vous êtes pressé, voici à quoi ressemble un tableau déclaré des deux manières :

```js
// Utilisation du constructeur de tableau
let array = new Array("John Doe", 24, true);

// Utilisation de la notation littérale
let array = ["John Doe", 24, true];
```

Vous pouvez continuer à lire cet article pour bien comprendre ces méthodes ainsi que quelques autres options intéressantes qu'elles possèdent.

## Comment déclarer un tableau avec la notation littérale

C'est la méthode la plus populaire et la plus facile pour créer un tableau. C'est une manière plus courte et plus propre de déclarer un tableau.

Pour déclarer un tableau avec la notation littérale, vous définissez simplement un nouveau tableau en utilisant des crochets vides. Cela ressemble à ceci :

```js
let myArray = [];
```

Vous placerez tous les éléments à l'intérieur des crochets et séparerez chaque élément par une virgule.

```js
let myArray = ["John Doe", 24, true];
```

Les tableaux sont indexés à partir de zéro, ce qui signifie que vous pouvez accéder à chaque élément en commençant par zéro ou afficher l'ensemble du tableau.

```js
console.log(myArray[0]); // 'John Doe'
console.log(myArray[2]); // true
console.log(myArray); // ['John Doe', 24, true]
```

## Comment déclarer un tableau avec le constructeur de tableau

Vous pouvez également utiliser le constructeur de tableau pour créer ou déclarer un tableau. Il y a beaucoup de détails techniques à connaître pour déclarer un tableau avec le constructeur `Array()`.

Tout comme vous pouvez stocker plusieurs valeurs de types de données divers dans une seule variable avec la notation littérale de tableau, vous pouvez faire de même avec le constructeur de tableau.

```js
let myArray = new Array();
console.log(myArray); // []
```

Ce qui précède créera un nouveau tableau vide. Vous pouvez ajouter des valeurs au nouveau tableau en les plaçant entre les crochets, séparées par une virgule.

```js
let myArray = new Array("John Doe", 24, true);
```

Comme vous l'avez appris précédemment, vous pouvez accéder à chaque valeur en utilisant son numéro d'index, qui commence à zéro (0).

```js
console.log(myArray[0]); // 'John Doe'
console.log(myArray[2]); // true
console.log(myArray); // ['John Doe', 24, true]
```

Lors de la déclaration de tableaux avec la méthode du constructeur de tableau, il est important de garder à l'esprit les points suivants.

* Lorsque vous passez un seul chiffre dans un constructeur de tableau, il remplira le tableau avec le nombre de valeurs vides que vous avez entré.

```js
let myArray = new Array(4);
console.log(myArray); // [,,,]
```

Mais lorsque vous passez une seule chaîne de caractères ou tout autre type de données, cela fonctionne bien.

```js
let myArray = new Array(true);
console.log(myArray); // [true]
```

* Il n'est pas obligatoire d'ajouter `new`, car `Array()` et `new Array()` effectuent la même tâche.

```js
let myArray = Array("John Doe", 24, true);
```

## Conclusion

Dans cet article, vous avez appris comment déclarer un tableau en JavaScript. Il est important de savoir que le constructeur de tableau n'est pas vraiment utilisé, car il est bien plus compliqué que d'utiliser la notation littérale de tableau.

Vous pouvez en apprendre plus dans cet article sur [JavaScript Arrays - How to Create an Array in JavaScript](https://www.freecodecamp.org/news/how-to-create-an-array-in-javascript/) par [Jessica Wilkins](https://www.freecodecamp.org/news/author/jessica-wilkins/)

Amusez-vous bien à coder !