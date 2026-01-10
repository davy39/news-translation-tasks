---
title: 'Objets standard JavaScript : Maps'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-standard-objects-maps
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d30740569d1a4ca3660.jpg
tags:
- name: JavaScript
  slug: javascript
- name: maps
  slug: maps
- name: toothbrush
  slug: toothbrush
seo_title: 'Objets standard JavaScript : Maps'
seo_desc: "The Map object is a relatively new standard built-in object that holds\
  \ [key, value] pairs in the order that they're inserted. \nThe keys and values in\
  \ the Map object can be any value (both objects and primitive values are valid).\n\
  Syntax\nnew Map([itera..."
---

L'objet `Map` est un objet intégré standard relativement nouveau qui contient des paires `[clé, valeur]` dans l'ordre où elles sont insérées. 

Les clés et les valeurs dans l'objet `Map` peuvent être de n'importe quel type (à la fois des objets et des valeurs primitives sont valides).

## **Syntaxe**

```javascript
new Map([iterable])
```

## **Paramètres**

**iterable** Un tableau ou un autre objet itérable dont les éléments sont des paires clé-valeur.

## **Exemple**

```javascript
const myMap = new Map();
myMap.set('foo', 1);
myMap.set('bar', 2);
myMap.set('baz', 3);

myMap.get('foo');   // retourne 1
myMap.get('baz');   // retourne 3
myMap.get('hihi');  // retourne undefined

myMap.size;   // 3

console.log(myMap); // Map { 'foo' => 1, 'bar' => 2, 'baz' => 3 }
```

Il est facile de créer une nouvelle `Map` à partir de tableaux 2D existants de paires clé-valeur :

```js
const myArr = [['foo', 1], ['bar', 2], ['baz', 3]];
const arrMap = new Map(myArr);

console.log(arrMap); // Map { 'foo' => 1, 'bar' => 2, 'baz' => 3 }
```

Vous pouvez également convertir un objet en `Map` avec l'aide de `Object.entries` :

```js
const myObj = {
  foo: 1,
  bar: 2,
  baz: 3
}
const objMap = new Map(Object.entries(myObj));

console.log(objMap); // Map { 'foo' => 1, 'bar' => 2, 'baz' => 3 }
```

## **Map.prototype.get**

Retourne la valeur de la clé spécifiée à partir d'un objet `Map`.

## **Syntaxe**

```javascript
myMap.get(key);
```

## **Paramètres**

**key** Requis.

## **Exemple**

```javascript
const myMap = new Map();
myMap.set('foo',1);
myMap.set('bar',2);
myMap.set('baz',3);

myMap.get('foo');   // retourne 1
myMap.get('baz');   // retourne 3
myMap.get('hihi');  // retourne undefined
```

## **Map.prototype.set**

Définir ou met à jour un élément avec la clé et la valeur spécifiées dans un objet `Map`. La méthode `set()` retourne également l'objet `Map`.

## **Syntaxe**

```javascript
myMap.set(key, value);
```

## **Paramètres**

* **key** Requis
* **value** Requis

## **Exemple**

```javascript
const myMap = new Map();

// définit de nouveaux éléments
myMap.set('foo', 1);
myMap.set('bar', 2);
myMap.set('baz', 3);

// Met à jour un élément existant
myMap.set('foo', 100);

myMap.get('foo');   // retourne 100
```

Parce que `set()` retourne l'objet `Map` sur lequel il a opéré, la méthode peut être facilement enchaînée. Par exemple, le code ci-dessus peut être simplifié en :

```js
const myMap = new Map();

// définit de nouveaux éléments
myMap.set('foo', 1)
  .set('bar', 2)
  .set('baz', 3)
  .set('foo', 100); // Met à jour un élément existant

myMap.get('foo');   // retourne 100
```

## **Map.prototype.size**

Retourne le nombre d'éléments dans un objet `Map`.

## **Syntaxe**

```javascript
myMap.size();
```

## **Exemple**

```javascript
const myMap = new Map();
myMap.set('foo',1);
myMap.set('bar',2);
myMap.set('baz',3);


myMap.size(); // 3
```

## **Map.prototype.keys**

Retourne un nouvel objet `Iterator` qui contient les clés pour chaque élément dans l'objet `Map` dans l'ordre d'insertion.

## **Syntaxe**

```javascript
myMap.keys()
```

## **Exemple**

```javascript
const myMap = new Map();
myMap.set('foo',1);
myMap.set('bar',2);
myMap.set('baz',3);


const iterator = myMap.keys();

console.log(iterator.next().value); // 'foo'
console.log(iterator.next().value); // 'bar'
console.log(iterator.next().value); // 'baz'
```

## **Map.prototype.values**

Retourne un objet itérateur qui contient les valeurs pour chaque élément dans l'objet `Map` dans l'ordre où elles ont été insérées.

## **Syntaxe**

```javascript
myMap.values()
```

## **Exemple**

```javascript
const myMap = new Map();
myMap.set('foo',1);
myMap.set('bar',2);
myMap.set('baz',3);


const iterator = myMap.values();
console.log(iterator.next().value); // 1
console.log(iterator.next().value); // 2
console.log(iterator.next().value); // 3
```

## **Map.prototype.delete**

Supprime l'élément spécifié d'un objet `Map`. Retourne si la clé a été trouvée et supprimée avec succès.

## **Syntaxe**

```javascript
myMap.delete(key);
```

## **Paramètres**

**key** Requis.

## **Exemple**

```javascript
const myMap = new Map();
myMap.set('foo',1);
myMap.set('bar',2);
myMap.set('baz',3);


myMap.size(); // 3
myMap.has('foo'); // true;

myMap.delete('foo');  // Retourne true. Supprimé avec succès.

myMap.size(); // 2
myMap.has('foo');    // Retourne false. L'élément "foo" n'est plus présent.
```

## **Map.prototype.entries**

Retourne un nouvel objet `Iterator` qui contient les paires `[clé, valeur]` pour chaque élément dans l'objet `Map` dans l'ordre d'insertion.

## **Syntaxe**

```javascript
myMap.entries()
```

## **Exemple**

```javascript
const myMap = new Map();
myMap.set('foo',1);
myMap.set('bar',2);
myMap.set('baz',3);


const iterator = myMap.entries();

console.log(iterator.next().value); // ['foo', 1]
console.log(iterator.next().value); // ['bar', 2]
console.log(iterator.next().value); // ['baz', 3]
```

## **Map.prototype.clear**

Supprime tous les éléments d'un objet `Map` et retourne `undefined`.

## **Syntaxe**

```javascript
myMap.clear();
```

## **Exemple**

```javascript
const myMap = new Map();
myMap.set('foo',1);
myMap.set('bar',2);
myMap.set('baz',3);


myMap.size(); // 3
myMap.has('foo'); // true;

myMap.clear(); 

myMap.size(); // 0
myMap.has('foo'); // false
```

## **Map.prototype.has**

Étant donné une `Map` avec des éléments à l'intérieur, la fonction `has()` vous permet de déterminer si un élément existe ou non à l'intérieur de la Map, en fonction d'une clé que vous passez.

La fonction `has()` retourne un _`Boolean` primitif_ (soit `true` soit `false`), ce qui indique que la Map contient l'élément ou non.

Vous passez un paramètre `key` à la fonction `has()`, qui sera utilisé pour rechercher un élément avec cette clé à l'intérieur de la Map.

Exemple :

```js
// Une Map simple
const campers = new Map();

// ajoute quelques éléments à la map
// la clé de chaque élément est 'camp' et un nombre
campers.set('camp1', 'Bernardo');
campers.set('camp2', 'Andrea');
campers.set('camp3', 'Miguel');

// Maintenant, je veux savoir s'il y a un élément
// avec la clé 'camp4' :
campers.has('camp4');
// la sortie est `false`
```

La `Map` `campers` ne contient actuellement pas d'élément avec une clé `'camp4'`. Par conséquent, l'appel de la fonction `has('camp4')` retournera `false`.

```js
// Si nous ajoutons un élément avec la clé 'camp4' à la map
campers.set('camp4', 'Ana');

// et essayons de rechercher cette clé à nouveau
campers.has('camp4');
// la sortie est `true`
```

Puisque la map contient maintenant un élément avec une clé `'camp4'`, l'appel de la fonction `has('camp4')` retournera `true` cette fois-ci !

Dans un scénario plus réaliste, vous ne pourriez pas ajouter manuellement les éléments à la Map vous-même, donc la fonction `has()` deviendrait vraiment utile dans ces cas.

## **Map.prototype.forEach**

Exécute la fonction passée sur chaque paire clé-valeur dans l'objet `Map`. Retourne `undefined`.

## **Syntaxe**

```javascript
myMap.forEach(callback, thisArg)
```

## **Paramètres**

* **callback** Fonction à exécuter pour chaque élément. 
* **thisArg** Valeur à utiliser comme this lors de l'exécution de callback.

## **Exemple**

```javascript
const myMap = new Map();
myMap.set('foo',1);
myMap.set('bar',2);
myMap.set('baz',3);

function valueLogger(value) {
  console.log(`${value}`);
}

myMap.forEach(valueLogger);
// 1
// 2
// 3
```