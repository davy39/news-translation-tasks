---
title: Tableaux JavaScript - Comment créer un tableau en JavaScript
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-05-16T18:17:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-array-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/jexo-73REk-BB7-Y-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Tableaux JavaScript - Comment créer un tableau en JavaScript
seo_desc: "An array is a type of data structure where you can store an ordered list\
  \ of elements. \nIn this article, I will show you 3 ways you can create an array\
  \ using JavaScript.  I will also show you how to create an array from a string using\
  \ the split() meth..."
---

Un tableau est un type de structure de données où vous pouvez stocker une liste ordonnée d'éléments. 

Dans cet article, je vais vous montrer 3 façons de créer un tableau en utilisant JavaScript. Je vais également vous montrer comment créer un tableau à partir d'une chaîne de caractères en utilisant la méthode `split()`.

## Comment créer un tableau en JavaScript en utilisant l'opérateur d'assignation

La manière la plus courante de créer un tableau en JavaScript serait d'assigner ce tableau à une variable comme ceci :

```js
const books = ["The Great Gatsby", "War and Peace", "Hamlet", "Moby Dick"];
```

Si nous utilisons `console.log` sur le tableau, il nous montrera les 4 éléments listés dans le tableau. 

```js
const books = ["The Great Gatsby", "War and Peace", "Hamlet", "Moby Dick"];

console.log(books);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.11.38-PM.png)

## Comment créer un tableau en JavaScript en utilisant l'opérateur new et le constructeur Array

Une autre façon de créer un tableau est d'utiliser le mot-clé `new` avec le constructeur `Array`. 

Voici la syntaxe de base :

```js
new Array();
```

Si un paramètre numérique est passé entre les parenthèses, cela définira la longueur du nouveau tableau.

Dans cet exemple, nous créons un tableau avec une longueur de 3 emplacements vides.

```js
new Array(3)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-14-at-11.07.33-PM.png)

Si nous utilisons la propriété length sur le nouveau tableau, elle retournera le nombre 3.

```js
new Array(3).length
```

Mais si nous essayons d'accéder à un élément du tableau, il reviendra indéfini car tous ces emplacements sont actuellement vides.

```js
new Array(3)[0]
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-14-at-11.10.02-PM.png)

Nous pouvons modifier notre exemple pour prendre plusieurs paramètres et créer un tableau d'éléments alimentaires.

```js
let myFavoriteFoods = new Array("pizza", "ice cream", "salad");

console.log(myFavoriteFoods); // ["pizza","ice cream","salad"]
console.log(myFavoriteFoods.length); // 3
console.log(myFavoriteFoods[1]); // "ice cream"
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-14-at-11.13.48-PM.png)

## Comment créer un tableau en JavaScript en utilisant Array.of()

Une autre façon de créer un tableau est d'utiliser la méthode `Array.of()`. Cette méthode prend un nombre quelconque d'arguments et crée une nouvelle instance de tableau. 

Voici la syntaxe de base :

```js
Array.of(); 
```

Nous pouvons modifier notre exemple précédent de nourriture pour utiliser la méthode `Array.of()` comme ceci.

```js
let myFavoriteFoods = Array.of("pizza", "ice cream", "salad");

console.log(myFavoriteFoods); // ["pizza","ice cream","salad"]
console.log(myFavoriteFoods.length); // 3
console.log(myFavoriteFoods[1]); // "ice cream"
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-14-at-11.47.54-PM.png)

Cette méthode est très similaire à l'utilisation du constructeur Array. La différence clé est que si vous passez un seul nombre en utilisant `Array.of()`, il retournera un tableau avec ce nombre dedans. Mais le constructeur Array crée x nombre d'emplacements vides pour ce nombre.

Dans cet exemple, il retournerait un tableau avec le nombre 4 dedans.

```js
let myArr = Array.of(4);

console.log(myArr);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-15-at-12.00.27-AM.png)

Mais si je changeais cet exemple pour utiliser le constructeur Array, alors il retournerait un tableau de 4 emplacements vides. 

```js
let myArr = new Array(4);

console.log(myArr);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-15-at-12.02.03-AM.png)

## Comment créer un tableau à partir d'une chaîne de caractères en utilisant la méthode split()

Voici la syntaxe pour la méthode JavaScript `split()`.

```js
str.split(optional-separator, optional-limit)
```

Le séparateur optionnel est un type de motif qui indique à l'ordinateur où chaque division doit se produire.

Le paramètre limite optionnel est un nombre positif qui indique à l'ordinateur combien de sous-chaînes doivent être dans la valeur de tableau retournée.

Dans cet exemple, j'ai la chaîne `"I love freeCodeCamp"`. Si j'utilisais la méthode `split()` sans le séparateur, alors la valeur de retour serait un tableau de la chaîne entière.

```js
const str = 'I love freeCodeCamp';

console.log(str.split());
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-15-at-12.09.10-AM.png)

Si je voulais la modifier pour que la chaîne soit divisée en caractères individuels, alors je devrais ajouter un séparateur. Le séparateur serait une chaîne vide.

```js
const str = "I love freeCodeCamp";

console.log(str.split(""));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-15-at-12.10.58-AM.png)

Remarquez comment les espaces sont considérés comme des caractères dans la valeur de retour.

Si je voulais la modifier pour que la chaîne soit divisée en mots individuels, alors le séparateur serait une chaîne vide avec un espace.

```js
const str = "I love freeCodeCamp";

console.log(str.split(" "));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-15-at-12.11.32-AM.png)

## Conclusion

Dans cet article, je vous ai montré trois façons de créer un tableau en utilisant l'opérateur d'assignation, le constructeur Array et la méthode `Array.of()`. 

La manière la plus courante de créer un tableau en JavaScript serait d'assigner ce tableau à une variable comme ceci :

```js
const books = ["The Great Gatsby", "War and Peace", "Hamlet", "Moby Dick"];
```

Une autre façon de créer un tableau est d'utiliser le mot-clé `new` avec le constructeur `Array`.

```js
new Array();
```

Si un paramètre numérique est passé entre les parenthèses, cela définira la longueur du nouveau tableau avec ce nombre d'emplacements vides.

Par exemple, ce code créera un tableau avec une longueur de 3 emplacements vides.

```js
new Array(3)
```

Nous pouvons également passer plusieurs paramètres comme ceci :

```js
let myFavoriteFoods = new Array("pizza", "ice cream", "salad");

console.log(myFavoriteFoods); // ["pizza","ice cream","salad"]
```

Une autre façon de créer un tableau est d'utiliser la méthode `Array.of()`. Cette méthode prend un nombre quelconque d'arguments et crée une nouvelle instance de tableau.

```js
Array.of(); 
```

Vous pouvez également prendre une chaîne de caractères et créer un tableau en utilisant la méthode `split()`

```js
str.split(optional-separator, optional-limit)
```

J'espère que vous avez apprécié cet article sur les tableaux JavaScript.