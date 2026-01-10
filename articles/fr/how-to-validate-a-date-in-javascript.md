---
title: Validations de date JS – Comment valider une date en JavaScript (avec des exemples)
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2023-08-22T19:08:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-validate-a-date-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/js-date-validations.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Validations de date JS – Comment valider une date en JavaScript (avec des
  exemples)
seo_desc: 'There are times when you need to validate a date input in your JavaScript
  applications.

  This article will show you how to perform the following date validations:


  Check if a string is a valid date

  Validate a string in the DD/MM/YYYY format

  Check if t...'
---

Il arrive que vous deviez valider une entrée de date dans vos applications JavaScript.

Cet article vous montrera comment effectuer les validations de date suivantes :

1. Vérifier si une chaîne est une date valide
2. Valider une chaîne au format `JJ/MM/AAAA`
3. Vérifier si la date est dans le passé ou le futur

Valider une valeur de date aide à empêcher les utilisateurs de saisir une date incorrecte. Commençons par valider l'entrée elle-même.

## Comment vérifier si une chaîne est une date valide avec JavaScript

Pour valider si une chaîne est une entrée de date valide, vous devez appeler le constructeur `Date()` et passer la chaîne comme argument.

Si la chaîne est une date valide, le constructeur retourne un objet `Date` contenant la même valeur que la chaîne :

```js
let dateInput = "2019/05/15"; // Format AAAA/MM/JJ

let dateObj = new Date(dateInput);

console.log(dateObj); // 2019-05-15T00:00:00.000Z
```

Si vous passez une date invalide, le constructeur retourne un objet `Invalid Date` :

```js
let dateInput = "2019/15/15"; // Format AAAA/MM/JJ

let dateObj = new Date(dateInput);

console.log(dateObj); // Invalid Date
```

Notez que le constructeur `Date()` nécessite que vous passiez une date au format `AAAA/MM/JJ` ou `MM/JJ/AAAA`. Si vous passez une date au format `JJ/MM/AAAA`, le constructeur retourne également un `Invalid Date`.

Maintenant que vous avez un objet `Date` représentant la chaîne, vous pouvez utiliser la fonction `isNaN()` pour vérifier si l'objet est valide.

Vous pouvez créer une fonction pour vérifier la validité de l'objet `Date` comme suit :

```js
function isDateValid(dateStr) {
  return !isNaN(new Date(dateStr));
}

// JJ/MM/AAAA
console.log(isDateValid("15/05/2019")); // false

// MM/JJ/AAAA
console.log(isDateValid("05/15/2019")); // true

// AAAA/MM/JJ
console.log(isDateValid("2019/05/15")); // true
```

Ici, nous inversons la valeur retournée par la fonction `isNaN()` afin qu'une date valide retourne `true`. Vous pouvez appeler la fonction `isDateValid()` chaque fois que vous devez vérifier si une chaîne retourne une date valide.

Ensuite, voyons comment gérer une chaîne de date au format `JJ/MM/AAAA`.

## Comment valider une date et la convertir au format JJ/MM/AAAA

Si vous souhaitez formater la date en tant que chaîne `JJ/MM/AAAA`, vous devez utiliser une combinaison des méthodes `getDate()`, `getMonth()` et `getFullYear()` pour créer manuellement la chaîne de date.

Tout d'abord, vous validez la chaîne au format `AAAA/MM/JJ` en la passant au constructeur `Date()`.

Ensuite, vous vérifiez si la valeur `Date` n'est pas NaN en utilisant une instruction `if` :

```js
let dateInput = "2019/05/15"; // Format AAAA/MM/JJ

let dateObj = new Date(dateInput);

if (!isNaN(dateObj)) {
  // Convertir dateObj en JJ/MM/AAAA
}
```

Lorsque la `Date` n'est pas un NaN, vous pouvez extraire le jour, le mois et l'année de l'objet en utilisant les méthodes `getDate()`, `getMonth()` et `getFullYear()` :

```js
let dateInput = "2019/05/15"; // Format AAAA/MM/JJ

let dateObj = new Date(dateInput);

if (!isNaN(dateObj)) {
  let day = dateObj.getDate();
  day = day < 10 ? "0" + day : day;
  let month = dateObj.getMonth() + 1;
  month = month < 10 ? "0" + month : month;
  const year = dateObj.getFullYear();

  const resultDate = `${day}/${month}/${year}`;
  console.log(resultDate);  // 15/05/2019
}
```

Ici, vous pouvez voir que la date "2019/05/15" est convertie en "15/05/2019". Remarquez comment vous devez modifier les variables `day` et `month` pour ajouter `0` devant les valeurs si ces valeurs sont des chiffres uniques.

La méthode `getMonth()` retourne un nombre entre 0 et 11 qui représente le mois de la date. Vous devez incrémenter la valeur retournée de 1 pour obtenir la date correcte.

## Que faire si j'obtiens la date au format JJ/MM/AAAA ?

Comme je l'ai dit précédemment, JavaScript ne supporte pas la conversion d'une chaîne au format `JJ/MM/AAAA` en un objet `Date` valide.

Si vous avez une chaîne de date au format `JJ/MM/AAAA`, vous devez alors échanger la position de la date et de l'année avant d'appeler le constructeur `Date()`.

Vous pouvez le faire en utilisant la méthode `split()` pour convertir la chaîne en un tableau, puis échanger la position de la date et de l'année aux index 0 et 2.

Passez le séparateur `/` comme argument à la méthode split comme montré ci-dessous :

```js
let dateInput = "15/05/2019"; // Format JJ/MM/AAAA

let dateArray = dateInput.split("/");

let newDate = `${dateArray[2]}/${dateArray[1]}/${dateArray[0]}`;

console.log(newDate); // 2019/05/15 (AAAA/MM/JJ)
```

La variable `newDate` a la valeur de `dateInput` mais au format `AAAA/MM/JJ`. Vous pouvez passer `newDate` dans le constructeur `Date()` pour voir si c'est une date valide.

## Comment vérifier si une date est dans le passé ou le futur

Pour vérifier si une date est dans le passé ou le futur, vous pouvez utiliser l'opérateur inférieur à `<` pour comparer la date d'entrée avec la date actuelle.

Lorsque le résultat est `true`, alors la date d'entrée est dans le passé :

```js
// La date que vous souhaitez vérifier
const inputDate = new Date('2023-08-20'); 

// Obtenir la date actuelle
const currentDate = new Date();

// Comparer la date d'entrée avec la date actuelle
if (inputDate < currentDate) {
  console.log('La date d\'entrée est dans le passé.');
} else {
  console.log('La date d\'entrée est dans le futur.');
}
```

JavaScript sait comment comparer les objets `Date`, vous n'avez donc pas besoin d'extraire les valeurs et de les comparer manuellement.

## Conclusion

Maintenant, vous avez appris comment valider si une chaîne est une date valide, comment convertir une date au format `JJ/MM/AAAA`, et comment vérifier si une date est dans le passé ou le futur.

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine !