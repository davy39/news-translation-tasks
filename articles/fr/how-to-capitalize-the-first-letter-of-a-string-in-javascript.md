---
title: Comment mettre en majuscule la première lettre d'une chaîne en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-21T22:22:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-capitalize-the-first-letter-of-a-string-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e8e740569d1a4ca3dc0.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment mettre en majuscule la première lettre d'une chaîne en JavaScript
seo_desc: 'To capitalize the first letter of a random string, you should follow these
  steps:


  Get the first letter of the string;

  Convert the first letter to uppercase;

  Get the remainder of the string;

  Concatenate the first letter capitalized with the remainder...'
---

Pour mettre en majuscule la première lettre d'une chaîne aléatoire, vous devez suivre ces étapes :

1. Obtenez la première lettre de la chaîne ;
2. Convertissez la première lettre en majuscule ;
3. Obtenez le reste de la chaîne ;
4. Concaténez la première lettre en majuscule avec le reste de la chaîne et retournez le résultat ;

## **1. Obtenir la première lettre de la chaîne**

Vous devez utiliser la méthode [charAt()](http://forum.freecodecamp.com/t/javascript-string-prototype-charat/15932), à l'_index 0_, pour sélectionner le premier caractère de la chaîne.

```javascript
var string = "freeCodecamp";

string.charAt(0); // Retourne "f"
```

NOTE : `charAt` est préférable à l'utilisation de `[ ]` ([notation entre crochets](http://forum.freecodecamp.com/t/javascript-string-prototype-touppercase/15950)) car `str.charAt(0)` retourne une chaîne vide (_`''`_) pour `str = ''` au lieu de `undefined` dans le cas de `''[0]`.

## **2. Convertir la première lettre en majuscule**

Vous pouvez utiliser la méthode [toUpperCase()](http://forum.freecodecamp.com/t/javascript-string-prototype-touppercase/15950) et convertir la chaîne appelante en majuscules.

```javascript
var string = "freeCodecamp";

string.charAt(0).toUpperCase(); // Retourne "F"
```

## **3. Obtenir le reste de la chaîne**

Vous pouvez utiliser la méthode [slice()](https://github.com/freecodecamp/freecodecamp/wiki/js-array-prototype-slice) et obtenir le reste de la chaîne (du deuxième caractère, _index 1_, à la fin de la chaîne).

```javascript
var string = "freeCodecamp";

string.slice(1); // Retourne "reeCodecamp"
```

## **4. Retourner le résultat en ajoutant la première lettre et le reste de la chaîne**

Vous devez créer une fonction qui accepte une chaîne comme seul argument et retourne la concaténation de la première lettre en majuscule `string.charAt(0).toUpperCase()` et du reste de la chaîne `string.slice(1)`.

```javascript
var string = "freeCodecamp";

function capitalizeFirstLetter(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

capitalizeFirstLetter(string); // Retourne "FreeCodecamp"
```

Ou vous pouvez ajouter cette fonction à `String.prototype` pour l'utiliser directement sur une chaîne en utilisant le code suivant (_de sorte que la méthode ne soit pas énumérable mais puisse être écrasée ou supprimée plus tard_) :

```javascript
var string = "freeCodecamp";

/* c'est ainsi que les méthodes sont définies dans le prototype de tout objet intégré */
Object.defineProperty(String.prototype, 'capitalizeFirstLetter', {
    value: function () {
        return this.charAt(0).toUpperCase() + this.slice(1);
    },
    writable: true, // afin de pouvoir l'écraser plus tard
    configurable: true // afin de pouvoir la supprimer plus tard
});

string.capitalizeFirstLetter(); // Retourne "FreeCodecamp"
```

### **Source**

[stackoverflow - Capitalize the first letter of string in JavaScript](http://stackoverflow.com/questions/1026069/capitalize-the-first-letter-of-string-in-javascript/1026087#1026087)