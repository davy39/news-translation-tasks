---
title: 'Objets standard JavaScript : les tableaux'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T17:41:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-standard-objects-arrays
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/very-large-array.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: 'Objets standard JavaScript : les tableaux'
seo_desc: 'Surely you''ve heard that, in JavaScript, everything is an object. Strings,
  numbers, functions, arrays, and, well, objects are considered objects.

  In this tutorial we''ll take a deep dive into the Array "global" or "standard built-in"
  object, along wit...'
---

Vous avez sûrement entendu dire qu'en JavaScript, tout est un objet. Les chaînes de caractères, les nombres, les fonctions, les tableaux, et bien sûr, les objets sont considérés comme des objets.

Dans ce tutoriel, nous allons plonger en profondeur dans l'objet "global" ou "standard intégré" **Array**, ainsi que les méthodes qui lui sont associées.

## Qu'est-ce qu'un tableau ?

En JavaScript, un tableau est un objet de type liste qui stocke des valeurs séparées par des virgules. Ces valeurs peuvent être de n'importe quel type – chaînes de caractères, nombres, objets, ou même fonctions.

Les tableaux commencent par un crochet ouvrant (`[`) et se terminent par un crochet fermant (`]`), utilisant des nombres comme index des éléments.

### Comment créer un tableau :

```js
const shoppingList = ['Pain', 'Fromage', 'Pommes'];
```

### Accéder à une valeur dans un tableau avec la notation entre crochets

```js
const shoppingList = ['Pain', 'Fromage', 'Pommes'];

console.log(shoppingList[1])
// Fromage
```

L'objet standard de tableau possède un certain nombre de méthodes utiles, dont certaines sont listées ci-dessous.

## Array.prototype.isArray()

La méthode `Array.isArray()` retourne `true` si un objet est un tableau, `false` si ce n'est pas le cas.

### Syntaxe

```text
Array.isArray(obj)
```

### **Paramètres**

**obj** L'objet à vérifier.

### Exemples de .isArray()

```text
// tous les appels suivants retournent true
Array.isArray([]);
Array.isArray([1]);
Array.isArray(new Array());
// Petit fait méconnu : Array.prototype lui-même est un tableau :
Array.isArray(Array.prototype); 

// tous les appels suivants retournent false
Array.isArray();
Array.isArray({});
Array.isArray(null);
Array.isArray(undefined);
Array.isArray(17);
Array.isArray('Array');
Array.isArray(true);
Array.isArray(false);
Array.isArray({ __proto__: Array.prototype });
```

## **Array.prototype.length**

`length` est une propriété des tableaux en JavaScript qui retourne ou définit le nombre d'éléments dans un tableau donné.

La propriété `length` d'un tableau peut être retournée comme suit.

```js
let desserts = ["Gâteau", "Tarte", "Brownies"];
console.log(desserts.length); // 3
```

L'opérateur d'affectation, en conjonction avec la propriété `length`, peut être utilisé pour définir le nombre d'éléments dans un tableau comme suit.

```js
let cars = ["Saab", "BMW", "Volvo"];
cars.length = 2;
console.log(cars.length); // 2
```

## Array.prototype.push

La méthode `push()` est utilisée pour ajouter un ou plusieurs nouveaux éléments à la fin d'un tableau. Elle retourne également la nouvelle longueur du tableau. Si aucun argument n'est fourni, elle retournera simplement la longueur actuelle du tableau. 

### **Syntaxe**

```javascript
arr.push([element1[, ...[, elementN]]])
```

### **Paramètres**

* **elementN** Les éléments à ajouter à la fin du tableau.

### **Valeur de retour**

La nouvelle longueur du tableau sur lequel la méthode a été appelée.

## **Exemple :**

```javascript
let myStarkFamily = ['John', 'Robb', 'Sansa', 'Bran'];
```

Supposons que vous avez un tableau des enfants de la maison Stark de Game of Thrones. Cependant, l'un des membres, **Arya**, est manquant. Connaissant le code ci-dessus, vous pourriez l'ajouter en assignant `'Arya'` au tableau à l'index après le dernier index comme suit :

```javascript
myStarkFamily[4] = 'Arya';
```

Le problème avec cette solution est qu'elle ne peut pas gérer les cas généraux. Si vous ne connaissiez pas à l'avance la longueur du tableau, vous ne pouvez pas ajouter de nouveaux éléments de cette manière. C'est pour cela que `push()` existe. Nous n'avons pas besoin de connaître la longueur du tableau. Nous ajoutons simplement notre élément à la fin du tableau.

```javascript
myStarkFamily.push('Arya');
console.log(myStarkFamily);  // ['John', 'Robb', 'Sansa', 'Bran', 'Arya']

let newLength = myStarkFamily.push('Rickon');  // Oups ! J'ai oublié Rickon
console.log(newLength);  // 6
console.log(myStarkFamily);  // ['John', 'Robb', 'Sansa', 'Bran', 'Arya', 'Rickon']
```

## Array.prototype.reverse

La méthode JavaScript `.reverse()` inversera l'ordre des éléments dans le tableau.

**Syntaxe**

```javascript
  let array = [1, 2, 3, 4, 5];
  array.reverse();
```

## **Description**

`.reverse()` inverse l'index des éléments d'un tableau.

## **Exemples**

**Utiliser `.reverse()` pour inverser les éléments d'un tableau**

```javascript
  let array = [1, 2, 3, 4, 5];
  console.log(array);
  // La console affichera 1, 2, 3, 4, 5

  array.reverse();

  console.log(array);
  /* La console affichera 5, 4, 3, 2, 1 et
  la variable array contient maintenant le tableau [5, 4, 3, 2, 1] */
```

## Array.prototype.indexOf

La méthode `indexOf()` retourne le premier index auquel un élément donné peut être trouvé dans le tableau. Si l'élément n'est pas présent, elle retourne -1.

La méthode `indexOf()` prend un élément que vous souhaitez rechercher comme paramètre, parcourt les éléments d'un tableau, et retourne le premier index où l'élément peut être trouvé. Si l'élément n'est pas dans le tableau, `indexOf` retourne -1.

**Syntaxe**

```javascript
  arr.indexOf(searchElement[, fromIndex])
```

**Paramètres**

* **searchElement** : L'élément que vous recherchez.
* **fromIndex** (Optionnel) : L'index à partir duquel vous souhaitez commencer la recherche. Si le `fromIndex` est supérieur ou égal à la longueur du tableau, le tableau n'est pas recherché et la méthode retourne -1. Si le fromIndex est un nombre négatif, il est considéré comme un décalage depuis la fin du tableau (le tableau est toujours recherché vers l'avant à partir de là). La valeur par défaut est 0, ce qui signifie que le tableau entier est recherché.
* L'index du tableau à partir duquel vous souhaitez commencer la recherche. La valeur par défaut est 0, ce qui signifie que la recherche commence à partir du premier index du tableau. Si `fromIndex` est supérieur ou égal à la longueur du tableau, alors la méthode ne recherche pas le tableau et retourne -1.

### Exemples

```javascript
var array = [1, 2, 4, 1, 7]

array.indexOf(1); // 0
array.indexOf(7); // 4
array.indexOf(6); // -1
array.indexOf('1'); // -1
array.indexOf('hello'); // -1
array.indexOf(1, 2); // 3
array.indexOf(1, -3); // 3
```

## Array.prototype.findIndex

La méthode `findIndex()` parcourt un tableau et teste chaque élément par rapport à la fonction de test qui est passée en paramètre. Elle retourne l'index du premier élément du tableau qui retourne vrai par rapport aux fonctions de test. Si aucun élément ne retourne vrai, `findIndex()` retourne -1.

Notez que `findIndex()` ne mute pas le tableau sur lequel elle est appelée.

**Syntaxe**

```text
arr.findIndex(callback(element, index, array), [thisArg])
```

##### **Paramètres**

`callback` : Fonction à exécuter sur chaque valeur dans le tableau, qui prend trois arguments : 

* `element` : L'élément actuel en cours de traitement dans le tableau.
* `index` : L'index de l'élément actuel en cours de traitement dans le tableau.
* `array` : Le tableau sur lequel findIndex() a été appelé.

`thisArg` (Optionnel) : Un objet à utiliser comme `this` lors de l'exécution de la fonction de rappel.

### Exemples

Cet exemple trouvera l'élément correspondant dans le tableau et retournera l'index de celui-ci.

```javascript
let items = [
    {name: 'livres', quantity: 2},
    {name: 'films', quantity: 1},
    {name: 'jeux', quantity: 5}
];

function findMovies(item) { 
    return item.name === 'films';
}

console.log(items.findIndex(findMovies));

// L'index du 2ème élément dans le tableau est retourné,
// donc cela donnera '1'
```

L'exemple suivant montre la sortie de chaque paramètre optionnel de la fonction de rappel. Cela retournera `-1` car aucun des éléments ne retournera vrai à partir de la fonction de rappel.

```javascript
function showInfo(element, index, array) {
  console.log('element = ' + element + ', index = ' + index + ', array = ' + array);
  return false;
}

console.log('return = ' + [4, 6, 8, 12].findIndex(showInfo));

// Sortie
//  element = 4, index = 0, array = 4,6,8,12
//  element = 6, index = 1, array = 4,6,8,12
//  element = 8, index = 2, array = 4,6,8,12
//  element = 12, index = 3, array = 4,6,8,12
//  return = -1
```

## Array.prototype.find

La méthode `find()` parcourt un tableau et teste chaque élément par rapport à la fonction de test qui est passée en paramètre. Elle retourne la valeur du premier élément du tableau qui retourne vrai par rapport aux fonctions de test. Si aucun élément ne retourne vrai, `find()` retourne `undefined`.

Notez que `find()` ne mute pas le tableau sur lequel elle est appelée.

### Syntaxe

```text
arr.find(callback(element, index, array), [thisArg])
```

##### **Paramètres**

`callback` : Fonction à exécuter sur chaque valeur dans le tableau. Elle prend trois arguments :

* `element` : L'élément actuel en cours de traitement dans le tableau.
* `index` : L'index de l'élément actuel en cours de traitement dans le tableau.
* `array` : Le tableau sur lequel find a été appelé.

`thisArg` (Optionnel) : Un objet à utiliser comme `this` lors de l'exécution de la fonction de rappel.

### Exemples

Cet exemple trouvera l'élément correspondant dans le tableau et retournera l'objet de celui-ci.

```javascript
let items = [
    {name: 'livres', quantity: 2},
    {name: 'films', quantity: 1},
    {name: 'jeux', quantity: 5}
];

function findMovies(item) { 
    return item.name === 'films';
}

console.log(items.find(findMovies));

// Sortie
//  { name: 'films', quantity: 1 }
```

L'exemple suivant montre la sortie de chaque paramètre optionnel de la fonction de rappel. Cela retournera `undefined` car aucun des éléments ne retournera vrai à partir de la fonction de rappel.

```javascript
function showInfo(element, index, array) {
  console.log('element = ' + element + ', index = ' + index + ', array = ' + array);
  return false;
}

console.log('return = ' + [4, 6, 8, 12].find(showInfo));

// Sortie
//  element = 4, index = 0, array = 4,6,8,12
//  element = 6, index = 1, array = 4,6,8,12
//  element = 8, index = 2, array = 4,6,8,12
//  element = 12, index = 3, array = 4,6,8,12
//  return = undefined
```

## Array.prototype.join

La méthode JavaScript `.join()` combinera tous les éléments d'un tableau en une seule chaîne de caractères.

**Syntaxe**

```javascript
  const array = ["Lorem", "Ipsum", "Dolor", "Sit"];
  const str = array.join([separator]);
```

### Paramètres

**separator** Optionnel. Spécifie la chaîne de caractères à utiliser pour séparer chaque élément du tableau original. Si le séparateur n'est pas une chaîne de caractères, il sera converti en une chaîne de caractères. Si le paramètre séparateur n'est pas fourni, les éléments du tableau sont séparés par une virgule par défaut. Si le séparateur est une chaîne vide `""`, tous les éléments du tableau sont joints sans caractère de séparation entre eux.

### Description

`.join()` joint tous les éléments d'un tableau en une seule chaîne de caractères. Si l'un des éléments du tableau est `undefined` ou `null`, cet élément est converti en la chaîne vide `""`.

### Exemples

**Utilisation de `.join()` de quatre manières différentes**

```javascript
const array = ["Lorem", "Ipsum", "Dolor" ,"Sit"];

const join1 = array.join();           /* assigne "Lorem,Ipsum,Dolor,Sit" à la variable join1
                                     (car aucun séparateur n'a été fourni, .join()
                                     a utilisé une virgule par défaut) */
const join2 = array.join(", ");       // assigne "Lorem, Ipsum, Dolor, Sit" à la variable join2
const join3 = array.join(" + ");      // assigne "Lorem + Ipsum + Dolor + Sit" à la variable join3
const join4 = array.join("");         // assigne "LoremIpsumDolorSit" à la variable join4
```

## **Array.prototype.concat**

La méthode `.concat()` retourne un nouveau tableau composé des éléments du tableau sur lequel vous l'appelez, suivi des éléments des arguments dans l'ordre où ils sont passés.

Vous pouvez passer plusieurs arguments à la méthode `.concat()`. Les arguments peuvent être des tableaux, ou des types de données comme des booléens, des chaînes de caractères, et des nombres.

### **Syntaxe**

```javascript
const newArray = array.concat(value1, value2, value3...);
```

### **Exemples**

#### **Concaténation de deux tableaux**

```javascript
const cold = ['Bleu', 'Vert', 'Violet'];
const warm = ['Rouge', 'Orange', 'Jaune'];

const result = cold.concat(warm);

console.log(result);
// résultats en ['Bleu', 'Vert', 'Violet', 'Rouge', 'Orange', 'Jaune'];
```

#### **Concaténation de valeur à un tableau**

```javascript
const odd = [1, 3, 5, 7, 9];
const even = [0, 2, 4, 6, 8];

const oddAndEvenAndTen = odd.concat(even, 10);

console.log(oddAndEvenAndTen);
// résultats en [1, 3, 5, 7, 9, 0, 2, 4, 6, 8, 10];
```

## Array.prototype.slice

La méthode JavaScript `.slice()` retournera un nouvel objet tableau qui sera un segment (une tranche) du tableau original. Le tableau original n'est pas modifié.

**Syntaxe**

```javascript
  array.slice()
  arr.slice(startIndex)
  arr.slice(startIndex, endIndex) 
```

### Paramètres

* **startIndex** L'index basé sur zéro où la tranche doit commencer. Si la valeur est omise, elle commencera à 0.
* **endIndex** La tranche se terminera **avant** cet index basé sur zéro. Un index négatif est utilisé pour décaler depuis la fin du tableau. Si la valeur est omise, le segment sera tranché jusqu'à la fin du tableau.

### Exemples

```javascript
  const array = ['livres', 'jeux', 'tasse', 'sandwich', 'sac', 'téléphone', 'cactus']
  
  const everything = array.slice()
  // everything = ['livres', 'jeux', 'tasse', 'sandwich', 'sac', 'téléphone', 'cactus']
  
  const kitchen = array.slice(2, 4)
  // kitchen = ['tasse', 'sandwich']
  
  const random = array.slice(4)
  // random = ['sac', 'téléphone', 'cactus']
  
  const noPlants = array.slice(0, -1)
  // noPlats = ['livres', 'jeux', 'tasse', 'sandwich', 'sac', 'téléphone']
  
  // array sera toujours égal à ['livres', 'jeux', 'tasse', 'sandwich', 'sac', 'téléphone', 'cactus']
```

#### 

## **Array.prototype.splice**

La méthode splice est similaire à [Array.prototype.slice](https://guide.freecodecamp.org/javascript/standard-objects/array/array-prototype-slice), mais contrairement à `slice()`, elle mute le tableau sur lequel elle est appelée. Elle diffère également en ce sens qu'elle peut être utilisée pour ajouter des valeurs à un tableau ainsi que pour les supprimer.

### **Paramètres**

`splice()` peut prendre un ou plusieurs paramètres détaillés ci-dessous.

#### **splice(start)**

Si un seul paramètre est inclus, alors `splice(start)` supprimera tous les éléments du tableau à partir de `start` jusqu'à la fin du tableau.

```js
let exampleArray = ['first', 'second', 'third', 'fourth'];
exampleArray.splice(2);
// exampleArray est maintenant ['first', 'second'];
```

Si `start` est négatif, il comptera à rebours depuis la fin du tableau.

```js
let exampleArray = ['first', 'second', 'third', 'fourth'];
exampleArray.splice(-1);
// exampleArray est maintenant ['first', 'second', 'third'];
```

#### **splice(start, deleteCount)**

Si un deuxième paramètre est inclus, alors `splice(start, deleteCount)` supprimera `deleteCount` éléments du tableau, en commençant par `start`.

```js
let exampleArray = ['first', 'second', 'third', 'fourth'];
exampleArray.splice(1, 2);
// exampleArray est maintenant ['first', 'fourth'];
```

#### **splice(start, deleteCount, newElement1, newElement2, )**

Si plus de deux paramètres sont inclus, les paramètres supplémentaires seront de nouveaux éléments qui sont ajoutés au tableau. L'emplacement de ces éléments ajoutés commencera à `start`.

Des éléments peuvent être ajoutés sans supprimer d'éléments en passant `0` comme deuxième paramètre.

```js
let exampleArray = ['first', 'second', 'third', 'fourth'];
exampleArray.splice(1, 0, 'new 1', 'new 2');
// exampleArray est maintenant ['first', 'new 1', 'new 2', 'second', 'third', 'fourth']
```

Les éléments peuvent également être remplacés.

```js
let exampleArray = ['first', 'second', 'third', 'fourth'];
exampleArray.splice(1, 2, 'new second', 'new third');
// exampleArray est maintenant ['first', 'new second', 'new third', 'fourth']
```

### **Valeur de retour**

En plus de modifier le tableau sur lequel elle est appelée, `splice()` retourne également un tableau contenant les valeurs supprimées. C'est un moyen de couper un tableau en deux tableaux différents.

```js
let exampleArray = ['first', 'second', 'third', 'fourth'];
let newArray = exampleArray.splice(1, 2);
// exampleArray est maintenant ['first', 'fourth']
// newArray est ['second', 'third']
```

## **Array.prototype.filter**

La méthode filter prend un tableau comme entrée. Elle prend chaque élément dans le tableau et applique une instruction conditionnelle contre celui-ci. Si cette condition retourne vrai, l'élément est "poussé" vers le tableau de sortie.

Une fois que chaque élément du tableau d'entrée est "filtré" de cette manière, elle produit un nouveau tableau contenant chaque élément qui a retourné vrai.

Dans l'exemple ci-dessous, il y a un tableau qui contient plusieurs objets. Normalement, pour parcourir ce tableau, vous pourriez utiliser une boucle for.

Dans ce cas, nous voulons obtenir tous les étudiants dont les notes sont supérieures ou égales à 90.

```javascript
const students = [
  { name: 'Quincy', grade: 96 },
  { name: 'Jason', grade: 84 },
  { name: 'Alexis', grade: 100 },
  { name: 'Sam', grade: 65 },
  { name: 'Katie', grade: 90 }
];
//Définir un tableau pour pousser les objets étudiants.
let studentsGrades = []
for (var i = 0; i < students.length; i++) {
  //Vérifier si la note est supérieure à 90
  if (students[i].grade >= 90) {
    //Ajouter un étudiant au tableau studentsGrades.
    studentsGrades.push(students[i])
  }
}

console.log(studentsGrades); // [ { name: 'Quincy', grade: 96 }, { name: 'Alexis', grade: 100 }, { name: 'Katie', grade: 90 } ]
```

Cette boucle for fonctionne, mais elle est assez longue. Elle peut également devenir fastidieuse à écrire pour de nombreux tableaux que vous devez parcourir.

C'est un excellent cas d'utilisation pour filter !

Voici le même exemple utilisant filter :

```javascript
const students = [
  { name: 'Quincy', grade: 96 },
  { name: 'Jason', grade: 84 },
  { name: 'Alexis', grade: 100 },
  { name: 'Sam', grade: 65 },
  { name: 'Katie', grade: 90 }
];

const studentGrades = students.filter(function (student) {
  //Cela teste si student.grade est supérieur ou égal à 90. Il retourne l'objet "student" si cette condition est remplie.
  return student.grade >= 90;
});

console.log(studentGrades); // [ { name: 'Quincy', grade: 96 }, { name: 'Alexis', grade: 100 }, { name: 'Katie', grade: 90 } ]
```

La méthode filter est beaucoup plus rapide à écrire et plus propre à lire tout en accomplissant la même chose. En utilisant la syntaxe ES6, nous pouvons même répliquer la boucle for de 6 lignes avec filter :

```javascript
const students = [
  { name: 'Quincy', grade: 96 },
  { name: 'Jason', grade: 84 },
  { name: 'Alexis', grade: 100 },
  { name: 'Sam', grade: 65 },
  { name: 'Katie', grade: 90 }
];

const studentGrades = students.filter(student => student.grade >= 90);
console.log(studentGrades); // [ { name: 'Quincy', grade: 96 }, { name: 'Alexis', grade: 100 }, { name: 'Katie', grade: 90 } ]
```

Filter est très utile et un excellent choix par rapport aux boucles for pour filtrer les tableaux contre des instructions conditionnelles.

## **Array.prototype.forEach**

La méthode `.forEach()` est utilisée pour itérer à travers chaque élément d'un tableau. La méthode est appelée sur l'objet tableau et reçoit une fonction qui est appelée sur chaque élément du tableau.

```javascript
let arr = [1, 2, 3, 4, 5];

arr.forEach(number => console.log(number * 2));

// 2
// 4
// 6
// 8
// 10
```

La fonction de rappel peut également prendre un deuxième paramètre d'un index au cas où vous auriez besoin de référencer l'index de l'élément actuel dans le tableau.

```javascript
let arr = [1, 2, 3, 4, 5];

arr.forEach((number, i) => console.log(`${number} est à l'index ${i}`));

// '1 est à l'index 0'
// '2 est à l'index 1'
// '3 est à l'index 2'
// '4 est à l'index 3'
// '5 est à l'index 4'
```

## **Array.prototype.reduce**

La méthode `reduce()` réduit un tableau de valeurs à une seule valeur. Elle a été appelée le couteau suisse, ou multi-outil, des méthodes de transformation de tableaux. D'autres, comme `map()` et `filter()`, fournissent des transformations plus spécifiques, tandis que `reduce()` peut être utilisée pour transformer des tableaux en toute sortie que vous désirez.

### **Syntaxe**

```js
arr.reduce(callback[, initialValue])
```

L'argument `callback` est une fonction qui sera appelée une fois pour chaque élément du tableau. Cette fonction prend quatre arguments, mais souvent seuls les deux premiers sont utilisés.

* _accumulator_ - la valeur retournée de l'itération précédente
* _currentValue_ - l'élément actuel dans le tableau
* _index_ - l'index de l'élément actuel
* _array_ - le tableau original sur lequel reduce a été appelé
* L'argument `initialValue` est optionnel. Si fourni, il sera utilisé comme valeur initiale de l'accumulateur dans le premier appel à la fonction de rappel (voir l'exemple 2 ci-dessous).

### **Exemple 1**

Transformer un tableau d'entiers en la somme de tous les entiers dans le tableau.

```js
const numbers = [1,2,3]; 
const sum = numbers.reduce(function(total, current){
    return total + current;
});
console.log(sum); 
```

Cela affichera `6` dans la console.

### **Exemple 2**

Transformer un tableau de chaînes de caractères en un seul objet qui montre combien de fois chaque chaîne apparaît dans le tableau. Remarquez que cet appel à reduce passe un objet vide `{}` comme paramètre `initialValue`. Cela sera utilisé comme valeur initiale de l'accumulateur (le premier argument) passé à la fonction de rappel.

```js
const pets = ['chien', 'poulet', 'chat', 'chien', 'poulet', 'poulet', 'lapin'];

const petCounts = pets.reduce(function(obj, pet){
    if (!obj[pet]) {
        obj[pet] = 1;
    } else {
        obj[pet]++;
    }
    return obj;
}, {});

console.log(petCounts); 
```

Sortie :

```js
 { 
    chien: 2, 
    poulet: 3, 
    chat: 1, 
    lapin: 1 
 }
```

## **Array.prototype.sort**

Cette méthode trie les éléments d'un tableau en place et retourne le tableau.

La méthode `sort()` suit l'**ordre ASCII** !

```js
let myArray = ['#', '!'];
let sortedArray = myArray.sort();   // ['!', '#'] car dans la table ASCII "!" est avant "#"

myArray = ['a', 'c', 'b'];
console.log(myArray.sort()); // ['a', 'b', 'c']
console.log(myArray) // ['a', 'b', 'c']

myArray = ['b', 'a', 'aa'];
console.log(myArray.sort());   // ['a', 'aa', 'b']

myArray = [1, 2, 13, 23];
console.log(myArray.sort());   // [1, 13, 2, 23] les nombres sont traités comme des chaînes de caractères !
```

### Utilisation avancée

La méthode `sort()` peut également accepter un paramètre : `array.sort(compareFunction)`

### **Par exemple**

```js
function compare(a, b){
  if (a < b){return -1;}
  if (a > b){return 1;}
  if (a === b){return 0;}
}

let myArray = [1, 2, 23, 13];
console.log(myArray.sort()); // [ 1, 13, 2, 23 ]
console.log(myArray.sort(compare));   // [ 1, 2, 13, 23 ]

myArray = [3, 4, 1, 2];
sortedArray = myArray.sort(function(a, b){.....});   // cela dépend de la fonction compare
```

## Array.prototype.some()

La méthode JavaScript `.some()` prendra une fonction de rappel pour tester chaque élément dans le tableau ; une fois que le rappel retourne `true`, alors `.some()` retournera true immédiatement.

**Syntaxe**

```javascript
  var arr = [1, 2, 3, 4];
  arr.some(callback[, thisArg]);
```

## **Fonction de rappel**

**Syntaxe**

```javascript
  var isEven = function isEven(currentElement, index, array) {
      if(currentElement % 2 === 0) {
          return true;
      } else {
          return false;
      }
  }
```

Voir wiki sur [Opérateurs arithmétiques](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Arithmetic_Operators) pour voir l'opérateur de reste `%`

**A 3 arguments**

currentElement

* il s'agit d'une variable qui représente l'élément qui est passé à la fonction de rappel.

index

* il s'agit de la valeur d'index de l'élément actuel commençant à 0

array

* le tableau sur lequel `.some()` a été appelé.

La fonction de rappel doit implémenter un cas de test.

### thisArg

Il s'agit d'un paramètre optionnel et plus d'informations peuvent être trouvées sur le [MDN

### Description

`.some()` exécutera la fonction de rappel pour chaque élément du tableau. Une fois que le rappel retourne vrai, `.some()` retournera `true`. Si le rappel retourne une [valeur fausse](https://developer.mozilla.org/en-US/docs/Glossary/Falsy) pour _chaque_ élément du tableau, alors `.some()` retourne false.

`.some()` ne changera/pas mutera le tableau qui l'a appelé.

### Exemples

**Passer une fonction à `.some()`**

```javascript
const isEven = function isEven(currentElement, index, array) {
  if(currentElement % 2 === 0) {
      return true;
  } else {
      return false;
  }
}

const arr1 = [1, 2, 3, 4, 5, 6];
arr1.some(isEven);  // retourne true
const arr2 = [1, 3, 5, 7];
arr2.some(isEven);  // retourne false
```

**Fonction anonyme**

```javascript
const arr3 = ['Free', 'Code', 'Camp', 'The Amazing'];
arr3.some(function(curr, index, arr) {
  if (curr === 'The Amazing') {
      return true;
  } 
}); // retourne true

const arr4 = [1, 2, 14, 5, 17, 9];
arr4.some(function(curr, index, arr) {
  return curr > 20;
  });  // retourne false

// Fonctions fléchées ES6
arr4.some((curr) => curr >= 14)  // retourne true
```

## Array.prototype.every

La méthode `every()` teste si chaque élément du tableau passe le test fourni.

**Syntaxe**

```javascript
  arr.every(callback[, thisArg])
```

### Paramètres

1. Le **callback** prend jusqu'à trois arguments :

* **currentValue** (requis) – L'élément actuel dans le tableau.
* **index** (optionnel) – L'index ou l'élément actuel dans le tableau.
* **array** (optionnel) – Le tableau sur lequel la méthode `every` a été appelée.

2.  **thisArg** est optionnel. Il s'agit de la valeur utilisée comme `this` dans le callback.

## **Description**

La méthode `every` appelle la fonction `callback` une fois pour chaque élément du tableau, dans l'ordre des index croissants, jusqu'à ce que la fonction `callback` retourne false. Si un élément qui fait que `callback` retourne false est trouvé, la méthode every retourne immédiatement `false`. Sinon, la méthode every retourne `true`.

La fonction de rappel n'est pas appelée pour les éléments manquants du tableau.

En plus des objets tableau, la méthode every peut être utilisée par tout objet qui a une propriété length et qui a des noms de propriétés indexés numériquement. `every` ne mute pas le tableau sur lequel elle est appelée.

## **Exemples**

```javascript
  function isBigEnough(element, index, array) {
    return element >= 10;
  }
  [12, 5, 8, 130, 44].every(isBigEnough);   // false
  [12, 54, 18, 130, 44].every(isBigEnough); // true

  // Définir la fonction de rappel.
  function CheckIfEven(value, index, ar) {
      document.write(value + " ");

      if (value % 2 == 0)
          return true;
      else
          return false;
  }

  // Créer un tableau.
  var numbers = [2, 4, 5, 6, 8];

  // Vérifier si la fonction de rappel retourne true pour toutes les
  // valeurs du tableau.
  if (numbers.every(CheckIfEven))
      document.write("Tous sont pairs.");
  else
      document.write("Certains ne sont pas pairs.");

  // Sortie :
  // 2 4 5 Certains ne sont pas pairs.
```

## **Array.prototype.map**

La méthode `.map()` parcourt le tableau donné et exécute la fonction fournie sur chaque élément. Elle retourne un nouveau tableau qui contient les résultats de l'appel de la fonction sur chaque élément.

### **Exemples**

**ES5**

```js
var arr = [1, 2, 3, 4];
var newArray = arr.map(function(element) { return element * 2});
console.log(newArray); // [2, 4, 6, 8]
```

**ES6**

```js
const arr = [1, 2, 3, 4];
const newArray = arr.map(element => element * 2);
console.log(newArray);
//[2, 4, 6, 8]
```

## **Array.prototype.includes**

La méthode `includes()` détermine si un tableau inclut une valeur. Elle retourne true ou false.

Elle prend deux arguments :

1. `searchValue` - L'élément à rechercher dans le tableau.
2. `fromIndex` - La position dans le tableau à partir de laquelle commencer la recherche pour le `searchValue` fourni. Si une valeur négative est fournie, elle commence à partir de la longueur du tableau moins la valeur négative.

### **Exemple**

```js
const a = [1, 2, 3];
a.includes(2); // true 
a.includes(4); // false
```

## **Array.prototype.toLocaleString**

La méthode `toLocaleString()` retourne une chaîne de caractères représentant les éléments d'un tableau. Tous les éléments sont convertis en chaînes de caractères en utilisant leurs méthodes toLocaleString. Le résultat de l'appel de cette fonction est destiné à être spécifique à la locale.

##### **Syntaxe :**

```text
arr.toLocaleString();
```

##### **Paramètres**

* `locales` (Optionnel) - argument contenant soit une chaîne de caractères soit un tableau de balises de langue [BCP 47 language tag](http://tools.ietf.org/html/rfc5646).
* `options` (Optionnel) - objet avec des propriétés de configuration

##### **Valeur de retour**

Une chaîne de caractères représentant les éléments du tableau séparés par une chaîne de caractères spécifique à la locale (comme une virgule ",")

### Exemples

```javascript
const number = 12345;
const date = new Date();
const myArray = [number, date, 'foo'];
const myString = myArray.toLocaleString(); 

console.log(myString); 
// SORTIE '12345,10/25/2017, 4:20:02 PM,foo'
```

Différentes sorties pourraient être affichées en fonction de l'identifiant de langue et de région (la locale).

```javascript
const number = 54321;
const date = new Date();
const myArray = [number, date, 'foo'];
const myJPString = myArray.toLocaleString('ja-JP');

console.log(myJPString);
// SORTIE '54321,10/26/2017, 5:20:02 PM,foo'
```

Et avec cela, vous devriez savoir tout ce qui est nécessaire pour créer et manipuler des tableaux en JavaScript. Maintenant, allez de l'avant et manipulez des tableaux !

## Plus d'informations sur les tableaux :

* [Qu'est-ce qu'un tableau JavaScript ?](https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-array/)
* [Fonctions de tableau JavaScript expliquées avec des exemples](https://www.freecodecamp.org/news/javascript-map-reduce-and-filter-explained-with-examples/)
* [Guide ultime de Reduce](https://www.freecodecamp.org/news/the-ultimate-guide-to-javascript-array-methods-reduce/)
* [Guide ultime de Map](https://www.freecodecamp.org/news/the-ultimate-guide-to-javascript-array-methods-map/)
* [Longueur des tableaux JavaScript expliquée](https://www.freecodecamp.org/news/javascript-array-length/)

## Plus d'informations sur les fonctions de rappel

Une chose que vous avez sans doute remarquée est que de nombreuses méthodes de tableau utilisent des fonctions de rappel. Consultez ces articles pour plus d'informations à leur sujet :

* [Qu'est-ce qu'une fonction de rappel en JavaScript ?](https://www.freecodecamp.org/news/what-is-a-callback-function-in-javascript/)
* [Comment éviter l'enfer des rappels](https://www.freecodecamp.org/news/how-to-deal-with-nested-callbacks-and-avoid-callback-hell-1bc8dc4a2012/)