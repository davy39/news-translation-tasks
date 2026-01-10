---
title: 'Introduction aux API JavaScript : La Fonction Reduce'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-19T12:18:14.000Z'
originalURL: https://freecodecamp.org/news/applications-of-the-reduce-function-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dbc740569d1a4ca395f.jpg
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
seo_title: 'Introduction aux API JavaScript : La Fonction Reduce'
seo_desc: 'By Samuel Omole

  As the year begins, I have decided to make a series of articles that explain the
  various APIs (Application Programming Interfaces) in the JavaScript language. In
  each article we will break down a commonly used function in JavaScript a...'
---

Par Samuel Omole

Alors que l'année commence, j'ai décidé de faire une série d'articles qui expliquent les différentes API (Interfaces de Programmation d'Applications) du langage JavaScript. Dans chaque article, nous allons décomposer une fonction couramment utilisée en JavaScript et essayer de passer en revue ses diverses applications.

La première fonction que nous allons examiner est la fonction d'ordre supérieur '**Reduce**'. C'est principalement parce que, parmi toutes les méthodes de tableau JS, il m'a fallu un certain temps pour comprendre comment fonctionne la fonction Reduce.

Cet article suppose que le lecteur comprend d'autres méthodes de tableau comme **Map** et **Filter** car cela aidera à comprendre comment **Reduce** fonctionne.

Afin de bien comprendre l'idée derrière Reduce, nous allons examiner quelques exemples de solutions simples utilisant des boucles **for**, puis implémenter ces mêmes solutions en utilisant la fonction Reduce. Ensuite, nous examinerons quelques cas d'utilisation plus avancés pour la fonction Reduce.

## Exemple 1

Le premier exemple que nous allons examiner est un exemple courant : calculer la somme des éléments d'un tableau. Cela nécessite une solution simple, et l'utilisation d'une boucle **for** devrait ressembler à ceci :

```javascript
const arrayItems = [1,2,3,4,5,6];
let sum = 0;

for (let i = 0; i < arrayItems.length; i++) {
	sum = sum + arrayItems[i];
}
// sum = 21
```

La solution ci-dessus est assez simple, où nous ajoutons chaque élément du tableau et stockons le résultat dans la variable `sum`. La prochaine étape est donc d'implémenter la même solution en utilisant **Reduce**, ce qui devrait ressembler au code ci-dessous :

```javascript
const arrayItems = [1,2,3,4,5,6];

const sum = arrayItems.reduce(function(accumulator, currentItemInArray){
	accumulator = accumulator + currentItemInArray;
    return accumulator;
}, 0);

// sum = 21
```

En regardant les deux exemples ci-dessus, il est assez évident que l'exemple de la boucle **for** semble plus simple, et cela a été la cause de certains débats dans l'écosystème. Mais cet exemple est exagéré, et nous l'utilisons uniquement pour faciliter la compréhension du fonctionnement de la fonction Reduce, alors examinons l'exemple.

Nous devons, avant tout, comprendre ce qu'est la fonction Reduce. Il s'agit d'une méthode qui existe pour chaque tableau JavaScript. Elle nous permet de parcourir chaque élément du tableau et d'exécuter une fonction sur chacun de ces éléments.

Cela est assez similaire au comportement de la fonction **Map**, mais avec une différence : elle nous permet de retourner une valeur de notre fonction dans une itération particulière, qui existera ensuite en tant que paramètre (argument) dans cette fonction lors de l'itération suivante (cette valeur est communément appelée l'**accumulateur**).

Pour expliquer davantage, la fonction Reduce prend 2 arguments :

* Fonction de rappel : Il s'agit d'une fonction qui contient généralement 4 paramètres. Mais pour l'instant, nous nous intéressons uniquement au premier, l'accumulateur, et au second qui est l'élément actuel du tableau lors de cette itération.
* Valeur initiale : Il s'agit de la valeur initiale de l'accumulateur lorsque l'itération commence. Dans l'exemple ci-dessus, la valeur est 0, ce qui signifie que la valeur initiale de l'accumulateur sera 0.

Revenons à notre exemple :

```javascript
const arrayItems = [1,2,3,4,5,6];

const sum = arrayItems.reduce(function(accumulator, currentItemInArray){
	accumulator = accumulator + currentItemInArray;
    return accumulator;
}, 0);

// sum = 21
```

Il peut être davantage décomposé en la fonction de rappel et la valeur initiale :

```javascript
const arrayItems = [1,2,3,4,5,6];

function callbackFunction(accumulator, currentItemInArray){
    accumulator = accumulator + currentItemInArray;
    return accumulator;
}

const initialValue = 0;

const sum = arrayItems.reduce(callbackFunction, initialValue);

// sum = 21
```

La partie délicate pour moi était de comprendre comment fonctionne l'accumulateur. Pour l'expliquer, nous allons passer en revue chaque itération dans la boucle.

### Itération 1

Dans la première itération, puisque notre valeur initiale est 0, notre accumulateur aura une valeur de 0. Ainsi, notre fonction ressemblera à ceci :

```javascript
const arrayItems = [1,2,3,4,5,6];
// 1 est l'élément actuel du tableau

function callbackFunction(accumulator = 0, currentItemInArray = 1){
    accumulator = 0 + 1;
    return accumulator // qui est 1;
}
```

`callbackFunction` retournera une valeur de 1. Cela sera automatiquement utilisé comme valeur suivante pour l'accumulateur dans la deuxième itération.

### Itération 2

```javascript
const arrayItems = [1,2,3,4,5,6];
// 2 est l'élément actuel du tableau

function callbackFunction(accumulator = 1, currentItemInArray = 2){
    accumulator = 1 + 2;
    return accumulator // qui est 3;
}
```

Dans cette itération, notre accumulateur aura une valeur de 1 qui a été retournée dans notre première itération. La `callbackFunction` retournera une valeur de 3 dans cette itération. Cela signifie que notre accumulateur aura une valeur de 3 dans notre troisième itération.

### Itération 3

```js
const arrayItems = [1,2,3,4,5,6];
// 3 est l'élément actuel du tableau

function callbackFunction(accumulator = 3, currentItemInArray = 3){
    accumulator = 3 + 3;
    return accumulator // qui est 6;
}
```

Dans la troisième itération, notre accumulateur aura une valeur de 3 qui a été retournée par la `callbackFunction` dans l'itération 2. La `callbackFunction` retournera une valeur de 6, qui sera utilisée comme valeur de l'accumulateur dans l'itération 4. Ces étapes se répéteront jusqu'à ce que nous arrivions au dernier élément du tableau qui est 6.

Comme je l'ai mentionné précédemment, l'exemple ci-dessus peut être exagéré, alors examinons un problème où l'utilisation de Reduce est plus courante. (Cependant, cela ne signifie pas qu'une boucle **for** ne peut pas être utilisée pour implémenter une solution fonctionnelle).

## Exemple 2

Le deuxième exemple impliquera le comptage du nombre d'occurrences de chaque élément dans un tableau, par exemple :

```js
// Étant donné une entrée
const fruits = ['apples', 'apples', 'bananas', 'oranges', 'apples', 'oranges', 'bananas', 'grapes'];

// devrait donner une sortie de
const count = { 'apples': 3,'oranges': 2,'bananas': 2, 'grapes': 1 };
```

Implémentons la solution, puis passons en revue chaque itération et voyons ce qui se passe :

```js
const fruits = ['apples', 'apples', 'bananas', 'oranges', 'apples', 'oranges', 'bananas', 'grapes'];

function countOccurrence(accumulator, currentFruit){
	const currentFruitCount = accumulator[currentFruit];
    // si le fruit existe en tant que clé dans l'objet, incrémentez sa valeur, sinon ajoutez le fruit en tant que clé à l'objet avec une valeur de 1
    
    if(currentFruitCount) {
    	accumulator[currentFruit] = currentFruitCount + 1;
    } else {
    	accumulator[currentFruit] = 1
    }
    
    return accumulator;
}

const initialValue = {};

const count = fruits.reduce(countOccurrence, initialValue);
```

La solution est écrite pour être aussi verbeuse que possible afin que nous puissions comprendre ce qui se passe dans le code. Comme nous l'avons fait auparavant, passons en revue les premières itérations.

### Itération 1

Dans la première itération, puisque nous avons fait de notre valeur initiale un objet vide, la valeur de `accumulator` sera un objet vide. Cela signifie que la fonction `countOcurrence` ressemblera au code ci-dessous lorsqu'elle est appelée :

```js
const fruits = ['apples', 'apples', 'bananas', 'oranges', 'apples', 'oranges', 'bananas', 'grapes'];

// l'élément actuel est 'apples'

function countOccurrence(accumulator = {}, currentFruit = 'apples'){
    // puisque currentFruit = 'apples' alors accumulator[currentFruit] = accumulator['apples']
    
	const currentFruitCount = accumulator[currentFruit];
    // currentFruitCount sera null puisque accumulator est un objet vide
    
    if(currentFruitCount) {
    	accumulator[currentFruit] = currentFruitCount + 1;
    } else {
        // ce bloc s'exécutera puisque accumulator est vide
        // currentFruit = 'apples'
    	accumulator['apples'] = 1
        // accumulator devrait ressembler à ceci : { 'apples': 1 }
    }
    
    return accumulator // qui est { 'apples': 1 };
}
```

Puisque `accumulator` est un objet vide, `currentFruitCount` sera `null`. Cela signifie que le bloc `else` s'exécutera où une nouvelle clé (apples) avec la valeur de 1 sera ajoutée à l'`accumulator`. Cela sera retourné par la fonction qui sera passé comme valeur de l'accumulateur dans la deuxième itération.

### Itération 2

Dans la deuxième itération, notre `accumulator` aura la valeur de `{ 'apples': 1 }`, qui a été retournée par la fonction `countOccurrence` dans la première itération. Ensuite, la fonction `countOccurrence` ressemblera au code ci-dessous :

```js
const fruits = ['apples', 'apples', 'bananas', 'oranges', 'apples', 'oranges', 'bananas', 'grapes'];

// l'élément actuel est 'apples'

function countOccurrence(accumulator = { 'apples': 1 }, currentFruit = 'apples'){
    // puisque currentFruit = 'apples' alors accumulator[currentFruit] = accumulator['apples']
    
	const currentFruitCount = accumulator[currentFruit];
    // currentFruitCount sera 1 
    
    if(currentFruitCount) {
        // ce bloc s'exécutera puisque currentFruitCount est 1
        // currentFruit = 'apples'
    	accumulator['apples'] = 1 + 1;
        // accumulator devrait ressembler à ceci : { 'apples': 2 }
    } else {
    	accumulator[currentFruit] = 1
    }
    
    return accumulator // qui est { 'apples': 2 };
}
```

Puisque l'`accumulator` contient une clé ('apple') avec la valeur de 1, `currentFruit` sera 1, ce qui signifie que le bloc `if` sera exécuté. Dans ce bloc, la valeur de la clé `apple` sera incrémentée de 1 pour la porter à 2, et cette nouvelle valeur sera mise à jour dans l'objet accumulateur pour le rendre `{ 'apples' : 2 }`. Cette valeur sera retournée par la fonction `countOccurrence` et passée comme valeur pour l'accumulateur dans la troisième itération.

### Itération 3

Pour notre troisième itération, `accumulator` a la valeur de `{ apples: 2 }` qui a été retournée par `countOccurence` lors de la deuxième itération. La fonction `countOccurence` ressemblera au code ci-dessous :

```js
const fruits = ['apples', 'apples', 'bananas', 'oranges', 'apples', 'oranges', 'bananas', 'grapes'];

// l'élément actuel est 'bananas'

function countOccurrence(accumulator = { 'apples': 2 }, currentFruit = 'bananas'){
    // puisque currentFruit = 'bananas' alors accumulator[currentFruit] = accumulator['bananas']
    
	const currentFruitCount = accumulator[currentFruit];
        // currentFruitCount sera null puisque accumulator ne contient pas 'bananas'
    
    if(currentFruitCount) {
        accumulator[currentFruit] = currentFruitCount + 1;
    } else {
        // ce bloc s'exécutera puisque currentFruitCount est null
        // currentFruit = 'bananas'
    	accumulator['bananas'] = 1
    }
    
    return accumulator // qui est { 'apples': 2, 'bananas': 1  };
}
```

Cette itération est similaire à la première : puisque `bananas` n'existe pas dans `accumulator`, il sera ajouté à l'objet et recevra une valeur de `1`, faisant ressembler `accumulator` à ceci : `{ 'apples': 2, 'bananas': 1 }`. Cela deviendra alors la valeur de `accumulator` pour la quatrième itération.

Le processus se répétera jusqu'à ce que la fonction Reduce ait itéré à travers chaque élément du tableau.

## Conclusion

J'espère vraiment que ces exemples étaient suffisamment clairs pour créer un modèle mental de la façon dont la fonction **Reduce** fonctionne.

Si vous lisez ceci et que vous aimeriez voir des exemples plus avancés (comme l'implémentation de la fonction `pipe`), n'hésitez pas à me tweeter et je répondrai dès que possible. De plus, si vous avez d'autres exemples, j'adorerais les voir. Merci !!!