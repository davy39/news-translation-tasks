---
title: Les Promesses JavaScript Expliquées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-15T22:03:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-promises-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ddb740569d1a4ca3a03.jpg
tags:
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
- name: toothbrush
  slug: toothbrush
seo_title: Les Promesses JavaScript Expliquées
seo_desc: 'What is a promise in JavaScript?

  JavaScript is single threaded, meaning that two bits of script cannot run at the
  same time; they have to run one after another. A Promise is an object that represents
  the eventual completion (or failure) of an asynchr...'
---

## **Qu'est-ce qu'une promesse en JavaScript ?**

JavaScript est mono-thread, ce qui signifie que deux morceaux de script ne peuvent pas s'exécuter en même temps ; ils doivent s'exécuter l'un après l'autre. Une Promesse est un objet qui représente l'achèvement éventuel (ou l'échec) d'une opération asynchrone, et sa valeur résultante.

```javascript
var promise = new Promise(function(resolve, reject) {
  // faire quelque chose, puis...

  if (/* tout a fonctionné */) {
    resolve("Voilà, ça a marché !");
  }
  else {
    reject(Error("C'est cassé"));
  }
});
```

## **Une Promesse existe dans l'un de ces états**

* En attente : état initial, ni remplie ni rejetée.
* Remplie : l'opération s'est terminée avec succès.
* Rejetée : l'opération a échoué.

L'objet Promise fonctionne comme un proxy pour une valeur pas nécessairement connue lorsque la promesse est créée. Il vous permet d'associer des gestionnaires à la valeur de succès éventuelle d'une action asynchrone ou à la raison de l'échec. 

Cela permet aux méthodes asynchrones de retourner des valeurs comme les méthodes synchrones : au lieu de retourner immédiatement la valeur finale, la méthode asynchrone retourne une promesse pour fournir la valeur à un moment donné dans le futur.

## **Utilisation de 'Then' (Chaînage de Promesses)**

Pour prendre plusieurs appels asynchrones et les synchroniser les uns après les autres, vous pouvez utiliser le chaînage de promesses. Cela permet d'utiliser une valeur de la première promesse dans des rappels ultérieurs.

```javascript
Promise.resolve('some')
  .then(function(string) { // <-- Cela se produira après que la Promesse ci-dessus soit résolue (retournant la valeur 'some')
    return new Promise(function(resolve, reject) {
      setTimeout(function() {
        string += 'thing';
        resolve(string);
      }, 1);
    });
  })
  .then(function(string) { // <-- Cela se produira après que le nouveau Promise ci-dessus soit résolu
    console.log(string); // <-- Affiche 'something' dans la console
  });
```

## **API des Promesses**

Il y a 4 méthodes statiques dans la classe Promise :

* Promise.resolve
* Promise.reject
* Promise.all
* Promise.race

## **Les Promesses peuvent être enchaînées ensemble**

Lors de l'écriture de Promesses pour résoudre un problème particulier, vous pouvez les enchaîner pour former une logique.

```javascript
var add = function(x, y) {
  return new Promise((resolve,reject) => {
    var sum = x + y;
    if (sum) {
      resolve(sum);
    }
    else {
      reject(Error("Impossible d'additionner les deux valeurs !"));
    }
  });
};

var subtract = function(x, y) {
  return new Promise((resolve, reject) => {
    var sum = x - y;
    if (sum) {
      resolve(sum);
    }
    else {
      reject(Error("Impossible de soustraire les deux valeurs !"));
    }
  });
};

// Début du chaînage de promesses
add(2,2)
  .then((added) => {
    // added = 4
    return subtract(added, 3);
  })
  .then((subtracted) => {
    // subtracted = 1
    return add(subtracted, 5);
  })
  .then((added) => {
    // added = 6
    return added * 2;    
  })
  .then((result) => {
    // result = 12
    console.log("Mon résultat est ", result);
  })
  .catch((err) => {
    // Si une partie de la chaîne est rejetée, affiche le message d'erreur.
    console.log(err);
  });
```

Cela est utile pour suivre un paradigme de _Programmation Fonctionnelle_. En créant des fonctions pour manipuler des données, vous pouvez les enchaîner pour assembler un résultat final. Si à un moment donné dans la chaîne de fonctions une valeur est _rejetée_, la chaîne passera à la gestionnaire `catch()` la plus proche.

Pour plus d'informations sur la Programmation Fonctionnelle : [Programmation Fonctionnelle](https://en.wikipedia.org/wiki/Functional_programming)

## **Générateurs de Fonctions**

Dans les versions récentes, JavaScript a introduit plus de façons de gérer nativement les Promesses. L'une de ces façons est le générateur de fonctions. Les générateurs de fonctions sont des fonctions "pausables". Lorsqu'ils sont utilisés avec des Promesses, les générateurs peuvent rendre l'utilisation beaucoup plus facile à lire et apparaître "synchrones".

```javascript
const myFirstGenerator = function* () {
  const one = yield 1;
  const two = yield 2;
  const three = yield 3;

  return 'Terminé !';
}

const gen = myFirstGenerator();
```

Voici notre premier générateur, que vous pouvez voir par la syntaxe `function*`. La variable `gen` que nous avons déclarée n'exécutera pas `myFirstGenerator`, mais indiquera plutôt que "ce générateur est prêt à être utilisé".

```javascript
console.log(gen.next());
// Retourne { value: 1, done: false }
```

Lorsque nous exécutons `gen.next()`, il reprendra le générateur et continuera. Comme c'est la première fois que nous appelons `gen.next()`, il exécutera `yield 1` et mettra en pause jusqu'à ce que nous appelions à nouveau `gen.next()`. Lorsque `yield 1` est appelé, il nous retournera la `value` qui a été cédée et si le générateur est `done` ou non.

```javascript
console.log(gen.next());
// Retourne { value: 2, done: false }

console.log(gen.next());
// Retourne { value: 3, done: false }

console.log(gen.next());
// Retourne { value: 'Terminé !', done: true }

console.log(gen.next());
// Lèvera une erreur
```

Alors que nous continuons à appeler `gen.next()`, il continuera à passer au `yield` suivant et mettra en pause à chaque fois. Une fois qu'il n'y a plus de `yield`, il procédera à l'exécution du reste du générateur, qui dans ce cas retourne simplement `'Terminé !'`. Si vous appelez à nouveau `gen.next()`, il lèvera une erreur car le générateur est terminé.

Maintenant, imaginez si chaque `yield` dans cet exemple était une `Promise`, le code lui-même apparaîtrait extrêmement synchrone.

### **Promise.all(iterable) est très utile pour plusieurs requêtes vers différentes sources**

La méthode Promise.all(iterable) retourne une seule Promesse qui se résout lorsque toutes les promesses dans l'argument itérable sont résolues ou lorsque l'argument itérable ne contient aucune promesse. Elle est rejetée avec la raison de la première promesse qui est rejetée.

```javascript
var promise1 = Promise.resolve(catSource);
var promise2 = Promise.resolve(dogSource);
var promise3 = Promise.resolve(cowSource);

Promise.all([promise1, promise2, promise3]).then(function(values) {
  console.log(values);
});
// sortie attendue : Array ["catData", "dogData", "cowData"]
```

## Plus d'informations sur les Promesses :

* [Comment fonctionnent réellement les promesses JavaScript](https://www.freecodecamp.org/news/how-javascript-promises-actually-work-from-the-inside-out-76698bb7210b/)
* [Comment implémenter les promesses en JavaScript](https://www.freecodecamp.org/news/how-to-implement-promises-in-javascript-1ce2680a7f51/)
* [Comment utiliser les promesses en JavaScript](https://www.freecodecamp.org/news/how-javascript-promises-actually-work-from-the-inside-out-76698bb7210b/)
* [Comment écrire une promesse JavaScript](https://www.freecodecamp.org/news/how-to-write-a-javascript-promise-4ed8d44292b8/)