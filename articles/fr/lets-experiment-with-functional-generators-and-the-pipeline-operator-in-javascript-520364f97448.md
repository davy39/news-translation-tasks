---
title: Expérimentons avec les générateurs fonctionnels et l'opérateur de pipeline
  en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-11T00:13:36.000Z'
originalURL: https://freecodecamp.org/news/lets-experiment-with-functional-generators-and-the-pipeline-operator-in-javascript-520364f97448
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RJoQmQ7L6UZKQ14lYCN6EA.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Expérimentons avec les générateurs fonctionnels et l'opérateur de pipeline
  en JavaScript
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!


  A generator is a function that returns the next value from the sequence each time
  it is called.


  Combining functional ge...'
---

Par Cristian Salcescu

[**Découvrez le JavaScript Fonctionnel**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la Programmation Fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

> *Un générateur est une fonction qui retourne la valeur suivante de la séquence chaque fois qu'elle est appelée.*

Combiner les générateurs fonctionnels avec l'opérateur de pipeline et des fonctions pures avec des noms révélant l'intention, permet d'écrire du code de manière plus expressive, sans créer de listes intermédiaires :

```js
import { sequence, filter, map, take, toList } from "./sequence";

const filteredTodos =
  sequence(todos) 
  |> filter(isPriorityTodo) 
  |> map(toTodoView)
  |> take(10)  
  |> toList;
```

Voyons comment.

Je vais commencer par un simple générateur fonctionnel qui donne le prochain entier chaque fois qu'il est appelé. Il commence à 0.

```js
function sequence() {
  let count = 0;
  return function() {
    const result = count;
    count += 1;
    return result;
  }
}

const nextNumber = sequence();
nextNumber(); //0
nextNumber(); //1
nextNumber(); //2
```

`nextNumber()` est un générateur infini. `nextNumber()` est également une fonction de fermeture.

### Générateur fini

Les générateurs peuvent être finis. Vérifiez l'exemple suivant où `sequence()` crée un générateur qui retourne des nombres consécutifs à partir d'un intervalle spécifique. À la fin de la séquence, il retourne `undefined` :

```js
function sequence(from, to){
 let count = from;
 return function(){
   if(count< to){
      const result = count;
      count += 1;
      return result;
    }
  }
}

const nextNumber = sequence(10, 15);
nextNumber(); //10
nextNumber(); //12
nextNumber(); //13
nextNumber(); //14
nextNumber(); //undefined
```

### toList()

Lorsqu'on travaille avec des générateurs, on peut vouloir créer une liste avec toutes les valeurs de la séquence. Pour cette situation, nous avons besoin d'une nouvelle fonction `toList()` qui prend un générateur et retourne toutes les valeurs de la séquence sous forme de tableau. La séquence doit être finie.

```js
function toList(sequence) {
  const arr = [];
  let value = sequence();
  while (value !== undefined) {
    arr.push(value);
    value = sequence();
  }
  return arr;
}
```

Utilisons-le avec le générateur précédent.

```js
const numbers = toList(sequence(10, 15));
//[10,11,12,13,14]
```

### L'opérateur de pipeline

Un pipeline est une série de transformations de données où la sortie d'une transformation est l'entrée de la suivante.

L'opérateur de pipeline `|>` nous permet d'écrire des transformations de données de manière plus expressive. L'opérateur de pipeline fournit un sucre syntaxique pour les appels de fonctions avec un seul argument. Considérez le code suivant :

```js
const shortText = shortenText(capitalize("this is a long text"));

function capitalize(text) {
  return text.charAt(0).toUpperCase() + text.slice(1);
}

function shortenText(text) {
  return text.substring(0, 8).trim();
}
```

Avec l'opérateur de pipeline, la transformation peut s'écrire comme ceci :

```js
const shortText = "this is a long text" 
  |> capitalize 
  |> shortenText;
  //This is
```

À l'heure actuelle, l'opérateur de pipeline est expérimental. Vous pouvez l'essayer en utilisant Babel :

* dans le fichier `package.json`, ajoutez le plugin pipeline de babel :

```json
{
  "dependencies": {
    "@babel/plugin-syntax-pipeline-operator": "7.2.0"
  }
}
```

* dans le fichier de configuration `.babelrc`, ajoutez :

```
{
  "plugins": [["@babel/plugin-proposal-pipeline-operator", {
             "proposal": "minimal" }]]
}
```

### Générateurs sur des collections

Dans [Rendez votre code plus facile à lire avec la Programmation Fonctionnelle](https://medium.freecodecamp.org/make-your-code-easier-to-read-with-functional-programming-94fb8cc69f9d), j'avais un exemple de traitement d'une liste de `todos`. Voici le code :

```js
function isPriorityTodo(task) {
  return task.type === "RE" && !task.completed;
}

function toTodoView(task) {
  return Object.freeze({ id: task.id, desc: task.desc });
}

const filteredTodos = todos.filter(isPriorityTodo).map(toTodoView);
```

Dans cet exemple, la liste `todos` subit deux transformations. D'abord, une liste filtrée est créée, puis une deuxième liste avec les valeurs mappées est créée.

Avec les générateurs, nous pouvons faire les deux transformations et créer une seule liste. Pour cela, nous avons besoin d'un générateur `sequence()` qui donne la valeur suivante d'une collection.

```js
function sequence(list) {
  let index = 0;
  return function() {
    if (index < list.length) {
      const result = list[index];
      index += 1;
      return result;
    }
  };
}
```

#### filter() et map()

Ensuite, nous avons besoin de deux décorateurs `filter()` et `map()`, qui fonctionnent avec des générateurs fonctionnels.

`filter()` prend un générateur et crée un nouveau générateur qui ne retourne que les valeurs de la séquence qui satisfont la fonction prédicat.

`map()` prend un générateur et crée un nouveau générateur qui retourne la valeur mappée.

Voici les implémentations :

```js
function filter(predicate) {
  return function(sequence) {
    return function filteredSequence() {
      const value = sequence();
      if (value !== undefined) {
        if (predicate(value)) {
          return value;
        } else {
          return filteredSequence();
        }
      }
    };
  };
}

function map(mapping) {
  return function(sequence) {
    return function() {
      const value = sequence();
      if (value !== undefined) {
        return mapping(value);
      }
    };
  };
}
```

J'aimerais utiliser ces décorateurs avec l'opérateur de pipeline. Donc, au lieu de créer `filter(sequence, predicate){ }` avec deux paramètres, j'ai créé une version currifiée de celui-ci, qui sera utilisée comme ceci : `filter(predicate)(sequence)`. De cette manière, cela fonctionne bien avec l'opérateur de pipeline.

Maintenant que nous avons la boîte à outils, composée des fonctions `sequence`, `filter`, `map` et `toList`, pour travailler avec des générateurs sur des collections, nous pouvons les mettre toutes dans un module (`"./sequence"`). Voir ci-dessous comment réécrire le code précédent en utilisant cette boîte à outils et l'opérateur de pipeline :

```js
import { sequence, filter, map, take, toList } from "./sequence";

const filteredTodos =
  sequence(todos) 
  |> filter(isPriorityTodo) 
  |> map(toTodoView) 
  |> toList;
```

Voici un [test de performance](https://jsperf.com/functional-generators-vs-array-methods/1) mesurant la différence entre l'utilisation des méthodes de tableau et l'utilisation des générateurs fonctionnels. Il semble que l'approche avec les générateurs fonctionnels soit 15-20 % plus lente.

#### reduce()

Prenons un autre exemple qui calcule le prix des fruits d'une liste de courses.

```js
function addPrice(totalPrice, line){
   return totalPrice + (line.units * line.price);
}

function areFruits(line){
   return line.type === "FRT";
}

let fruitsPrice = shoppingList.filter(areFruits).reduce(addPrice,0);
```

Comme vous pouvez le voir, cela nous oblige à créer d'abord une liste filtrée, puis à calculer le total sur cette liste. Réécrivons le calcul avec des générateurs fonctionnels et évitons la création de la liste filtrée.

Nous avons besoin d'une nouvelle fonction dans la boîte à outils : `reduce()`. Elle prend un générateur et réduit la séquence à une seule valeur.

```js
function reduce(accumulator, startValue) {
  return function(sequence) {
    let result = startValue;
    let value = sequence();
    while (value !== undefined) {
      result = accumulator(result, value);
      value = sequence();
    }
    return result;
  };
}
```

`reduce()` a une exécution immédiate.

Voici le code réécrit avec des générateurs :

```js
import { sequence, filter, reduce } from "./sequence";

const fruitsPrice = sequence(shoppingList) 
  |> filter(areFruits) 
  |> reduce(addPrice, 0);
```

#### take()

Un autre scénario courant est de ne prendre que les `n` premiers éléments d'une séquence. Pour ce cas, nous avons besoin d'un nouveau décorateur `take()`, qui reçoit un générateur et crée un nouveau générateur qui retourne uniquement les `n` premiers éléments de la séquence.

```js
function take(n) {
  return function(sequence) {
    let count = 0;
    return function() {
      if (count < n) {
        count += 1;
        return sequence();
      }
    };
  };
}
```

Encore une fois, il s'agit de la version currifiée de `take()` qui doit être appelée comme ceci : `take(n)(sequence)`.

Voici comment vous pouvez utiliser `take()` sur une séquence infinie de nombres :

```js
import { sequence, toList, filter, take } from "./sequence";

function isEven(n) {
  return n % 2 === 0;
}

const first3EvenNumbers = sequence()  
  |> filter(isEven) 
  |> take(3) 
  |> toList;
  //[0, 2, 4]
```

J'ai refait le [test de performance](https://jsperf.com/functional-generators-vs-array-methods/4) précédent et j'ai utilisé `take()` pour ne traiter que les 100 premiers éléments. Il s'avère que la version avec les générateurs fonctionnels est beaucoup plus rapide (environ 170 fois plus rapide).

```js
let filteredTodos = todos
 .filter(isPriorityTodo)
 .slice(0, 100)
 .map(toTodoView);
//320 ops/sec

let filteredTodos =
const filteredTodos =
  sequence(todos) 
  |> filter(isPriorityTodo) 
  |> map(toTodoView)
  |> take(100)
  |> toList;
//54000 ops/sec
```

### Générateurs personnalisés

Nous pouvons créer n'importe quel générateur personnalisé et l'utiliser avec la boîte à outils et l'opérateur de pipeline. Créons le générateur personnalisé Fibonacci :

```js
function fibonacciSequence() {
  let a = 0;
  let b = 1;
  return function() {
    const aResult = a;
    a = b;
    b = aResult + b;
    return aResult;
  };
}

const fibonacci = fibonacciSequence();
fibonacci();
fibonacci();
fibonacci();
fibonacci();
fibonacci();

const firstNumbers = fibonacciSequence()  
  |> take(10) 
  |> toList;
  //[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Conclusion

L'opérateur de pipeline rend la transformation des données plus expressive.

Les générateurs fonctionnels peuvent être créés sur des séquences finies ou infinies de valeurs.

Avec les générateurs, nous pouvons faire du traitement de listes sans créer de listes intermédiaires à chaque étape.

Vous pouvez vérifier tous les exemples sur [codesandbox](https://codesandbox.io/s/rj2r9mxl0n).

[**Découvrez le JavaScript Fonctionnel**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la Programmation Fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Architecture Fonctionnelle avec React et Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)