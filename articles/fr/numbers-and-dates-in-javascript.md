---
title: Comment travailler avec les nombres et les dates en JavaScript
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2022-09-16T15:42:30.000Z'
originalURL: https://freecodecamp.org/news/numbers-and-dates-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Frame-388--1-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment travailler avec les nombres et les dates en JavaScript
seo_desc: 'Numbers, dates, and timers are important parts of JavaScript. And you''ll
  need to know how to work with them when writing your code.

  We often ignore these topics as many articles don''t discuss them. So here, we''ll
  dive deep into the techniques you can...'
---

Les nombres, les dates et les temporisateurs sont des parties importantes de JavaScript. Et vous devrez savoir comment travailler avec eux lors de l'écriture de votre code.

Nous ignorons souvent ces sujets car de nombreux articles n'en parlent pas. Alors ici, nous allons plonger profondément dans les techniques que vous pouvez utiliser et apprendre quelques choses intéressantes que vous pouvez utiliser dans votre prochain projet.

## Comment travailler avec les nombres en JS

Un nombre est un objet **wrapper primitif** utilisé pour convertir le type de données en nombre. Tout d'abord, nous verrons comment convertir une chaîne en nombre en utilisant l'objet wrapper `Number`.

```js
let str = "23";
console.log(typeof str); // string

let num = Number(str);
console.log(typeof num); // number
```

L'exemple ci-dessus montre comment vous pouvez convertir une chaîne en nombre.

Il existe une autre façon de faire cela en utilisant la coercition de type. Nous devons simplement ajouter le symbole `+` avant la chaîne, ce qui convertira la chaîne en nombre.

```js
let str = "23";
console.log(typeof str); // string

// réassigner la variable str
str = +"23";
console.log(typeof str);  // number
```

Ainsi, d'après l'exemple ci-dessus, nous pouvons voir qu'il existe deux méthodes pour convertir une chaîne en nombre. Mais nous préférons généralement la méthode `Number()` car elle est plus claire quant à ce que nous faisons et elle est également plus précise.

### Comment utiliser parseInt() et parseFloat()

Nous avons une fonction `parseInt()` qui peut analyser uniquement les parties entières d'une chaîne. Mais la chaîne doit commencer par un entier. Nous ne pouvons analyser que la première occurrence d'un entier dans une chaîne. Essayons de comprendre avec un exemple.

**Nous pouvons utiliser l'analyse de deux manières différentes :**

* Number.parseInt()

* parseInt()

La première méthode est meilleure car elle est plus précise.

```js
let padding = "22px";
console.log(Number.parseInt(padding)); // 22

let margin = "16px 12px";
console.log(Number.parseInt(margin)); // 16

let body = "container 12px";
console.log(Number.parseInt(body)); // NaN
```

D'après l'exemple ci-dessus, vous pouvez voir que vous ne pouvez analyser que la première occurrence d'un entier dans une chaîne et que la chaîne doit commencer par un nombre.

Vous pouvez également analyser des nombres flottants avec les mêmes règles avec `parseFloat()`.

```js
let padding = "2.5rem";
console.log(Number.parseFloat(padding)); // 2.5

let margin = "1.5rem 2.5rem";
console.log(Number.parseFloat(margin)); // 1.5

let body = "container 1rem";
console.log(Number.parseFloat(body)); // NaN
```

C'est ainsi que vous extrayez des entiers ou des nombres flottants d'une chaîne. Alors, où pouvons-nous l'utiliser ? Si vous êtes familier avec HTML et CSS, vous pouvez utiliser parseInt() pour extraire la taille de texte mentionnée en HTML/CSS avec l'aide de JavaScript. Après avoir extrait ces informations, vous pouvez manipuler le texte et changer la taille d'un élément en termes de remplissage, de marg, et ainsi de suite.

### Comment utiliser l'objet `Math`

Math est un objet intégré qui possède différentes méthodes et fonctions pour vous aider à effectuer des calculs mathématiques.

Gardez simplement à l'esprit que Math fonctionne uniquement avec le type Number.

Il existe de nombreuses méthodes et fonctions dans Math. Mais nous n'en verrons que quelques-unes dans ce tutoriel. Pour explorer davantage, vous pouvez visiter [la documentation ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math).

```js
let num = 16;
console.log(Math.sqrt(num)); 
// Donne la racine carrée d'un nombre.

let arr = ['1',4,7,20,32,35,41,'45'];
console.log(Math.max(...arr)); // 45
// ...arr déstructure le tableau en place.
// max utilise la coercition de type pour convertir une chaîne en nombre 
// et retourne le nombre maximum dans un tableau.

console.log(Math.min(...arr)); // 1
// min retourne le plus petit entier dans un tableau
```

Il existe 4 méthodes mathématiques qui peuvent être très déroutantes pour les débutants. Mais ici, nous allons les simplifier autant que possible pour bien les comprendre.

Ces 4 méthodes sont :

* `trunc()`

* `floor()`

* `round()`

* `ceil()`

#### Math.trunc()

Cette méthode supprime uniquement la partie décimale d'un entier. Peu importe la longueur de la partie décimale.

```js
let height = 23.4;
let width = 23.6;

console.log(Math.trunc(height)); // 23
console.log(Math.trunc(width)); // 23
```

#### Math.floor()

Lorsque nous utilisons la méthode floor sur un nombre flottant, elle arrondit à l'entier inférieur le plus proche.

```js
let height = 23.4;
let width = 23.6;

console.log(Math.floor(height)); // 23
console.log(Math.floor(width)); // 23
```

#### Math.round()

Math.round() arrondit à l'entier le plus proche d'un nombre à virgule flottante. Si la partie décimale (le nombre après la virgule) est inférieure à 5, elle arrondit vers le bas. Si la partie décimale est supérieure à 5, elle arrondit vers le haut. Vous pouvez voir comment cela fonctionne ici :

```js
let height = 23.4;
let width = 23.6;

console.log(Math.round(height)); // 23
console.log(Math.round(width)); // 24
```

#### Math.ceil()

Math.ceil() arrondit à l'entier supérieur suivant du nombre à virgule flottante. C'est totalement l'opposé de Math.floor().

```js
let height = 23.4;
let width = 23.6;

console.log(Math.ceil(height)); // 24
console.log(Math.ceil(width)); // 24
```

Lorsque nous effectuons des opérations sur des nombres à virgule flottante en JavaScript, nous rencontrons souvent le problème de la précision décimale. Examinons l'exemple ci-dessous :

```js
let operation = 0.1 / 0.3;
console.log(operation); // 0.33333333333333337
```

Nous avons obtenu beaucoup de décimales récurrentes ici. Nous pouvons contrôler ces décimales récurrentes et spécifier combien de décimales nous voulons en utilisant la méthode `toFixed()`.

```js
let operation = 0.1 / 0.3;
console.log(operation); // 0.33333333333333337
console.log(operation.toFixed(1)); // 0.3
console.log(operation.toFixed(2)); // 0.33
```

## Comment travailler avec les dates en JS

Une date est un objet en JavaScript. Nous pouvons calculer une date à l'aide du constructeur `new Date()`. Maintenant, un objet date contient un nombre qui est en millisecondes (nous comptons les millisecondes à partir du 1er janvier 1970).

```js
let now = new Date();
console.log(now); // date actuelle

console.log(new Date() / 1000); // millisecondes depuis le 1er janvier 1970
```

Il existe principalement quatre façons de créer une date :

```js
// 1
let now = new Date();
console.log(now);

// 2
now = new Date("Aug 31 2022 11:45:45");
console.log(now);

// 3
now = new Date("Nov 14 2022");
console.log(now);

// 4
let birth = "01-05-1998";
console.log(new Date(birth)); // 05 Jan 1998
```

* Vous voudrez utiliser la première méthode lorsque vous travaillez avec la date actuelle et que vous souhaitez changer dynamiquement les dates et l'heure dans votre application.

* Vous pouvez utiliser la deuxième méthode lorsque vous souhaitez travailler avec des dates fournies par l'utilisateur ou des dates passées stockées.

* La troisième méthode est une alternative simple à la deuxième méthode et est un peu plus simple.

* Si vous souhaitez convertir une chaîne au format date/heure, vous pouvez opter pour la quatrième méthode.

Vous pouvez utiliser l'une de ces méthodes. Parce que si nous voulons extraire des informations concernant cette date, vous avez une méthode prédéfinie à utiliser que vous ne pouvez pas utiliser avec des chaînes.

Lorsque nous créons un nouvel objet Date(), il y a 7 nombres qui sont l'année, le mois, le jour, l'heure, la minute, la seconde et la milliseconde dans cet ordre.

Il existe de nombreuses méthodes que nous pouvons utiliser pour obtenir différentes informations.

* `getFullYear()`

* `getMonth()`

* `getDate()`

* `getDay()`

* `getHours()`

* `getMinutes()`

* `getSeconds()`

* `getTime()`

```js
let now = new Date();

console.log(now.getFullYear()); // donne l'année complète.
console.log(now.getMonth()); // donne le numéro du mois en commençant par 0.
console.log(now.getDate()); // donne la date.
console.log(now.getDay()); // donne le jour avec lundi comme 0 et ainsi de suite.
console.log(now.getHours()); // donne les heures au format 24 heures.
console.log(now.getMinutes()); // donne les minutes
console.log(now.getSeconds()); // donne les secondes
console.log(now.getTime()); // donne le temps écoulé depuis le 1er janvier 1970 jusqu'à maintenant en millisecondes
```

### Comment effectuer des opérations sur les dates

Nous pouvons effectuer différentes opérations sur les dates. Si nous avons deux dates et que nous voulons trouver la différence entre ces dates, nous pouvons effectuer une soustraction. Mais lorsque nous obtenons le résultat, nous l'obtenons sous la forme d'un timestamp que nous devons convertir en jours.

```js
let present = new Date('Aug 31 2020');
let past = new Date('Aug 31 1990');
let days  = present - past;
console.log(days); // timestamp
console.log(Math.abs(new Date(days)/(1000*60*60*24))); // Nombre de jours
```

Si vous voulez un calcul plus précis pour les dates, vous pouvez utiliser [**moment.js**](https://momentjs.com/) – mais cela peut ne pas être nécessaire pour des projets et des applications simples.

## Conclusion

J'espère que vous comprenez maintenant comment fonctionnent les nombres et les dates en JavaScript. Merci d'avoir lu !

Vous pouvez me suivre sur :

* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/)

* [Twitter](https://twitter.com/Kedar__98)

* [Instagram](https://www.instagram.com/kedar_98/)