---
title: function.prototype.bind et function.prototype.length en JavaScript expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-01T22:01:00.000Z'
originalURL: https://freecodecamp.org/news/function-prototype-bind-and-function-prototype-length-in-javascript-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e57740569d1a4ca3c94.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: function.prototype.bind et function.prototype.length en JavaScript expliqués
seo_desc: 'Function Bind

  bind is a method on the prototype of all functions in JavaScript. It allows you
  to create a new function from an existing function, change the new function’s this
  context, and provide any arguments you want the new function to be called...'
---

## Liaison de fonction

`bind` est une méthode sur le prototype de toutes les fonctions en JavaScript. Elle permet de créer une nouvelle fonction à partir d'une fonction existante, de changer le contexte `this` de la nouvelle fonction et de fournir les arguments que vous souhaitez que la nouvelle fonction utilise lors de son appel. Les arguments fournis à `bind` précéderont tous les arguments passés à la nouvelle fonction lorsqu'elle est appelée.

### **Utilisation de `bind` pour changer `this` dans une fonction**

Le premier argument fourni à `bind` est le contexte `this` auquel la fonction sera liée. Si vous ne souhaitez pas changer la valeur de `this`, passez `null` comme premier argument.

Vous êtes chargé d'écrire du code pour mettre à jour le nombre de participants à leur arrivée à une conférence. Vous créez une simple page web qui a un bouton qui, lorsqu'il est cliqué, incrémente la propriété `numOfAttendees` sur l'objet conférence. Vous utilisez jQuery pour ajouter un gestionnaire de clic à votre bouton, mais après avoir cliqué sur le bouton, l'objet conférence n'a pas changé. Votre code pourrait ressembler à ceci.

```javascript
var nodevember = {
  numOfAttendees: 0,
  incrementNumOfAttendees: function() {
    this.numOfAttendees++;
  }
  // autres propriétés
};

$('.add-attendee-btn').on('click', nodevember.incrementNumOfAttendees);
```

Ceci est un problème courant lors de l'utilisation de jQuery et JavaScript. Lorsque vous cliquez sur le bouton, le mot-clé `this` dans la méthode que vous avez passée à la méthode `on` de jQuery fait référence au bouton et non à l'objet conférence. Vous pouvez lier le contexte `this` de votre méthode pour résoudre le problème.

```javascript
var nodevember = {
  numOfAttendees: 0,
  incrementNumOfAttendees: function() {
    this.numOfAttendees++;
  }
  // autres propriétés
};

$('.add-attendee-btn').on('click', nodevember.incrementNumOfAttendees.bind(nodevember));
```

Maintenant, lorsque le bouton est cliqué, `this` fait référence à l'objet `nodevember`.

### **Fournir des arguments à une fonction avec `bind`**

Chaque argument passé à `bind` après le premier précédera les arguments passés lors de l'appel de la fonction. Cela permet de pré-appliquer des arguments à une fonction. Dans l'exemple ci-dessous, `combineStrings` prend deux chaînes et les concatène. `bind` est ensuite utilisé pour créer une fonction qui fournit toujours « Cool » comme première chaîne.

```javascript
function combineStrings(str1, str2) {
  return str1 + " " + str2
}

var makeCool = combineStrings.bind(null, "Cool");

makeCool("trick"); // "Cool trick"
```

Le guide sur [cette référence](https://guide.freecodecamp.org/javascript/this-reference) contient plus d'informations sur la manière dont la référence du mot-clé `this` peut changer.

Plus de détails sur la méthode `bind` peuvent être trouvés sur la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind) de Mozilla.

## **Longueur de fonction**

La propriété `length` sur l'objet fonction contient le nombre d'arguments attendus par la fonction lors de son appel.

```javascript
function noArgs() { }

function oneArg(a) { }

console.log(noArgs.length); // 0

console.log(oneArg.length); // 1
```

### **Syntaxe ES2015**

ES2015, ou ES6 comme on l'appelle communément, a introduit l'opérateur rest et les paramètres de fonction par défaut. Ces deux ajouts changent la manière dont la propriété `length` fonctionne.

Si l'opérateur rest ou les paramètres par défaut sont utilisés dans une déclaration de fonction, la propriété `length` n'inclura que le nombre d'arguments avant un opérateur rest ou un paramètre par défaut.

```javascript
function withRest(...args) { }

function withArgsAndRest(a, b, ...args) { }

function withDefaults(a, b = 'I am the default') { }

console.log(withRest.length); // 0

console.log(withArgsAndRest.length); // 2

console.log(withDefaults.length); // 1
```

Plus d'informations sur `Function.length` peuvent être trouvées sur la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/length) de Mozilla.