---
title: Apprenez ces astuces JavaScript en moins de 5 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-22T18:07:10.000Z'
originalURL: https://freecodecamp.org/news/9-neat-javascript-tricks-e2742f2735c3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nhDglPZmEcmo2KDg7u4gxw.png
tags:
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Apprenez ces astuces JavaScript en moins de 5 minutes
seo_desc: 'By Alcides Queiroz

  Time-saving techniques used by pros


  1. Clearing or truncating an array

  An easy way of clearing or truncating an array without reassigning it is by changing
  its length property value:

  const arr = [11, 22, 33, 44, 55, 66];

  // trunca...'
---

Par Alcides Queiroz

#### Techniques d'économie de temps utilisées par les pros

![Image](https://cdn-media-1.freecodecamp.org/images/QuQa8vSRsqE3AzHx-lx1Sdxf4jKSObxgHKqd)

#### 1. Vider ou tronquer un tableau

Une manière facile de vider ou tronquer un tableau sans le réassigner est de changer la valeur de sa propriété `length` :

```
const arr = [11, 22, 33, 44, 55, 66];
```

```
// tronquer
arr.length = 3;
console.log(arr); //=> [11, 22, 33]
```

```
// vider
arr.length = 0;
console.log(arr); //=> []
console.log(arr[2]); //=> undefined
```

#### 2. Simuler des paramètres nommés avec la destructuration d'objets

Il est très probable que vous utilisiez déjà des objets de configuration lorsque vous devez passer un ensemble variable d'options à une fonction, comme ceci :

```
doSomething({ foo: 'Hello', bar: 'Hey!', baz: 42 });
```

```
function doSomething(config) {  const foo = config.foo !== undefined ? config.foo : 'Hi';  const bar = config.bar !== undefined ? config.bar : 'Yo!';  const baz = config.baz !== undefined ? config.baz : 13;  // ...}
```

C'est un ancien mais efficace modèle, qui tente de simuler des paramètres nommés en JavaScript. L'appel de la fonction semble correct. En revanche, la logique de gestion de l'objet de configuration est inutilement verbeuse. Avec la destructuration d'objets ES2015, vous pouvez contourner cet inconvénient :

```
function doSomething({ foo = 'Hi', bar = 'Yo!', baz = 13 }) {  // ...}
```

Et si vous devez rendre l'objet de configuration optionnel, c'est très simple aussi :

```
function doSomething({ foo = 'Hi', bar = 'Yo!', baz = 13 } = {}) {  // ...}
```

#### 3. Destructuration d'objets pour les éléments de tableau

Assignez les éléments de tableau à des variables individuelles avec la destructuration d'objets :

```
const csvFileLine = '1997,John Doe,US,john@doe.com,New York';
```

```
const { 2: country, 4: state } = csvFileLine.split(',');
```

#### 4. Switch avec des plages

> **NOTE :** Après réflexion, j'ai décidé de différencier cette astuce des autres dans cet article. Ce n'est **PAS** une technique d'économie de temps, **NI** adaptée au code de la vie réelle. **Gardez à l'esprit :** les "If" sont toujours meilleurs dans de telles situations.   
> Contrairement aux autres astuces de cet article, c'est plus une curiosité que quelque chose à vraiment utiliser.   
> Quoi qu'il en soit, **je la garderai dans cet article pour des raisons historiques.**

Voici une astuce simple pour utiliser des plages dans les instructions switch :

```
function getWaterState(tempInCelsius) {  let state;    switch (true) {    case (tempInCelsius <= 0):       state = 'Solid';      break;    case (tempInCelsius > 0 && tempInCelsius < 100):       state = 'Liquid';      break;    default:       state = 'Gas';  }
```

```
  return state;}
```

#### 5. Attendre plusieurs fonctions asynchrones avec async/await

Il est possible d'attendre que plusieurs fonctions asynchrones se terminent en utilisant `Promise.all` :

```
await Promise.all([anAsyncCall(), thisIsAlsoAsync(), oneMore()])
```

#### 6. Créer des objets purs

Vous pouvez créer un objet 100% pur, qui n'héritera d'aucune propriété ou méthode de `Object` (par exemple, `constructor`, `toString()` et ainsi de suite).

```
const pureObject = Object.create(null);
```

```
console.log(pureObject); //=> {}
console.log(pureObject.constructor); //=> undefined
console.log(pureObject.toString); //=> undefined
console.log(pureObject.hasOwnProperty); //=> undefined
```

#### 7. Formater le code JSON

`JSON.stringify` peut faire plus que simplement convertir un objet en chaîne. Vous pouvez également embellir votre sortie JSON avec celui-ci :

```
const obj = {   foo: { bar: [11, 22, 33, 44], baz: { bing: true, boom: 'Hello' } } };
```

```
// Le troisième paramètre est le nombre d'espaces utilisés pour // embellir la sortie JSON.
JSON.stringify(obj, null, 4); // =>"{// =>    "foo": {// =>        "bar": [// =>            11,// =>            22,// =>            33,// =>            44// =>        ],// =>        "baz": {// =>            "bing": true,// =>            "boom": "Hello"// =>        }// =>    }// =>}"
```

#### 8. Supprimer les éléments en double d'un tableau

En utilisant les ensembles ES2015 ainsi que l'opérateur Spread, vous pouvez facilement supprimer les éléments en double d'un tableau :

```
const removeDuplicateItems = arr => [...new Set(arr)];
```

```
removeDuplicateItems([42, 'foo', 42, 'foo', true, true]);//=> [42, "foo", true]
```

#### 9. Aplanir les tableaux multidimensionnels

Aplanir les tableaux est trivial avec l'opérateur Spread :

```
const arr = [11, [22, 33], [44, 55], 66];
```

```
const flatArr = [].concat(...arr); //=> [11, 22, 33, 44, 55, 66]
```

Malheureusement, l'astuce ci-dessus ne fonctionnera qu'avec des tableaux bidimensionnels. Mais avec des appels récursifs, nous pouvons la rendre adaptée aux tableaux de plus de 2 dimensions :

```
function flattenArray(arr) {  const flattened = [].concat(...arr);  return flattened.some(item => Array.isArray(item)) ?     flattenArray(flattened) : flattened;}
```

```
const arr = [11, [22, 33], [44, [55, 66, [77, [88]], 99]]];
```

```
const flatArr = flattenArray(arr); //=> [11, 22, 33, 44, 55, 66, 77, 88, 99]
```

Et voilà ! J'espère que ces petites astuces vous aideront à écrire un meilleur et plus beau JavaScript.