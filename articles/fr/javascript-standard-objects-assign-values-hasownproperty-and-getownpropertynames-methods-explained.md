---
title: 'Objets standard JavaScript : méthodes assign, values, hasOwnProperty et getOwnPropertyNames
  expliquées'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-standard-objects-assign-values-hasownproperty-and-getownpropertynames-methods-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d0c740569d1a4ca359c.jpg
tags:
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: 'Objets standard JavaScript : méthodes assign, values, hasOwnProperty et
  getOwnPropertyNames expliquées'
seo_desc: 'In JavaScript, the Object data type is used to store key value pairs, and
  like the Array data type, contain many useful methods. These are some useful methods
  you''ll use while working with objects.

  Object Assign Method

  The Object.assign() method is u...'
---

En JavaScript, le type de données `Object` est utilisé pour stocker des paires clé-valeur, et comme le type de données `Array`, il contient de nombreuses méthodes utiles. Voici quelques méthodes utiles que vous utiliserez en travaillant avec des objets.

## Méthode Object.assign

La méthode `Object.assign()` est utilisée pour :

1. ajouter des propriétés et des valeurs à un objet existant,
2. créer une nouvelle copie d'un objet existant, ou
3. combiner plusieurs objets existants en un seul objet.

La méthode `Object.assign()` nécessite un `targetObject` comme paramètre et peut accepter un nombre illimité de `sourceObjects` comme paramètres supplémentaires.

Il est important de noter ici que le paramètre `targetObject` sera toujours modifié. Si ce paramètre pointe vers un objet existant, cet objet sera à la fois modifié et copié.

Si vous souhaitez créer une copie d'un objet sans modifier cet objet original, vous pouvez passer un objet vide `{}` comme premier paramètre (`targetObject`) et l'objet à copier comme deuxième paramètre (`sourceObject`).

Si les objets passés comme paramètres à `Object.assign()` partagent les mêmes propriétés (ou clés), les valeurs de propriétés qui apparaissent plus tard dans la liste des paramètres écraseront celles qui sont apparues plus tôt.

**Syntaxe**

```javascript
Object.assign(targetObject, ...sourceObject);
```

**Valeur de retour**

`Object.assign()` retourne le `targetObject`.

### Exemples

Modification et copie de `targetObject` :

```javascript
let obj = {name: 'Dave', age: 30};

let objCopy = Object.assign(obj, {coder: true});

console.log(obj); // { name: 'Dave', age: 30, coder: true }
console.log(objCopy); // { name: 'Dave', age: 30, coder: true }
```

Copie de `targetObject` sans modification :

```javascript
let obj = {name: 'Dave', age: 30};

let objCopy = Object.assign({}, obj, {coder: true});

console.log(obj); // { name: 'Dave', age: 30 }
console.log(objCopy); // { name: 'Dave', age: 30, coder: true }
```

Objets avec les mêmes propriétés :

```javascript
let obj = {name: 'Dave', age: 30, favoriteColor: 'blue'};

let objCopy = Object.assign({}, obj, {coder: true, favoriteColor: 'red'});

console.log(obj); // { name: 'Dave', age: 30, favoriteColor: 'blue' }
console.log(objCopy); // { name: 'Dave', age: 30, favoriteColor: 'red', coder: true }
```

## Méthode Object.values

La méthode `Object.values()` prend un objet comme paramètre et retourne un tableau de ses valeurs. Cela la rend utile pour l'enchaînement avec des méthodes courantes de `Array` comme `.map()`, `.forEach()`, et `.reduce()`.

**Syntaxe**

```text
Object.values(targetObject);
```

**Valeur de retour**

Un tableau des valeurs de l'objet passé (`targetObject`).

### Exemples

```js
const obj = { 
  firstName: 'Quincy',
  lastName: 'Larson' 
}

const values = Object.values(obj);

console.log(values); // ["Quincy", "Larson"]
```

Si l'objet que vous passez a des nombres comme clés, alors `Object.values()` retournera les valeurs selon l'ordre numérique des clés :

```js
const obj1 = { 0: 'first', 1: 'second', 2: 'third' };
const obj2 = { 100: 'apple', 12: 'banana', 29: 'pear' };

console.log(Object.values(obj1)); // ["first", "second", "third"]
console.log(Object.values(obj2)); // ["banana", "pear", "apple"]
```

Si quelque chose d'autre qu'un objet est passé à `Object.values()`, il sera converti en objet avant d'être retourné comme un tableau :

```js
const str = 'hello';

console.log(Object.values(str)); // ["h", "e", "l", "l", "o"]
```

## Méthode Object.hasOwnProperty

La méthode `Object.hasOwnProperty()` retourne un [booléen](https://www.freecodecamp.org/news/p/6bce9cb3-38ff-45d1-a56b-322354699b01/www.freecodecamp.org/news/booleans-in-javascript-explained-how-to-use-booleans-in-javascript/) indiquant si l'objet possède la propriété spécifiée.

C'est une méthode pratique pour vérifier si un objet a la propriété spécifiée ou non, car elle retourne vrai/faux en conséquence.

**Syntaxe**

`Object.hasOwnProperty(prop)`

**Valeur de retour**

```js
true
// ou
false
```

### Exemples

Utilisation de `Object.hasOwnProperty()` pour tester si une propriété existe ou non dans un objet donné :

```js
const course = {
  name: 'freeCodeCamp',
  feature: 'is awesome',
}

const student = {
  name: 'enthusiastic student',
}

course.hasOwnProperty('name');  // retourne true
course.hasOwnProperty('feature');   // retourne true

student.hasOwnProperty('name');  // retourne true
student.hasOwnProperty('feature'); // retourne false
```

## Méthode Object.getOwnPropertyNames

La méthode `Object.getOwnPropertyNames()` prend un objet comme paramètre et retourne un tableau de toutes ses propriétés.

**Syntaxe**

```text
Object.getOwnPropertyNames(obj)
```

**Valeur de retour**

Un tableau de chaînes de caractères des propriétés de l'objet passé.

### Exemples

```js
const obj = { firstName: 'Quincy', lastName: 'Larson' }

console.log(Object.getOwnPropertyNames(obj)); // ["firstName", "lastName"]
```

Si quelque chose d'autre qu'un objet est passé à `Object.getOwnPropertyNames()`, il sera converti en objet avant d'être retourné comme un tableau :

```js
const arr = ['1', '2', '3'];

console.log(Object.getOwnPropertyNames(arr)); // ["0", "1", "2", "length"]
```

## Promise.prototype.then

Une fonction `Promise.prototype.then` accepte deux arguments et retourne une Promise.

Le premier argument est une fonction requise qui accepte un argument. L'accomplissement réussi d'une Promise déclenchera cette fonction.

Le deuxième argument est une fonction optionnelle qui accepte également un argument. Une erreur lancée ou un rejet de la Promise déclenchera cette fonction.

```javascript
   function onResolved (resolvedValue) {
     /*
     * accès aux valeurs résolues de la promesse
     */
   }
 
  function onRejected(rejectedReason) {
     /*
     * accès aux raisons de rejet de la promesse
     */
   }

  promiseReturningFunction(paramList)
     .then( // fonction then
       onResolved,
       [onRejected]
     );
```

`Promise.prototype.then` vous permet d'effectuer de nombreuses activités asynchrones en séquence. Vous faites cela en attachant une fonction `then` à une autre séparée par un opérateur de point.

```javascript
   promiseReturningFunction(paramList)
   .then( // première fonction then
     function(arg1) {
       // ...
       return someValue;
     }
   )
   ...
   .then( // n-ième fonction then
     function(arg2) {
       // ...
       return otherValue;
     }
   )
```

## Map.prototype.entries

Retourne un nouvel objet `Iterator` qui contient les paires `[key, value]` pour chaque élément dans l'objet `Map` dans l'ordre d'insertion.

## Syntaxe

```javascript
myMap.entries()
```

## Exemple

```javascript
const myMap = new Map();
myMap.set('foo',1);
myMap.set('bar',2);
myMap.set('baz',3);


var iterator = myMap.entries();

console.log(iterator.next().value); // ['foo', 1]
console.log(iterator.next().value); // ['bar', 2]
console.log(iterator.next().value); // ['baz', 3]
```

## Plus d'informations sur les objets en JavaScript :

* [Comment créer des objets en JavaScript](https://www.freecodecamp.org/news/a-complete-guide-to-creating-objects-in-javascript-b0e2450655e8/)
* [Comment parcourir les objets en JavaScript](https://www.freecodecamp.org/news/how-to-loop-through-objects-in-javascript-a80b7d2478ac/)

## Plus d'informations sur les booléens :

* [Les booléens en JavaScript](https://www.freecodecamp.org/news/p/6bce9cb3-38ff-45d1-a56b-322354699b01/www.freecodecamp.org/news/booleans-in-javascript-explained-how-to-use-booleans-in-javascript/)