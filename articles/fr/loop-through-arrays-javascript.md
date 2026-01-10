---
title: Comment parcourir les tableaux en JavaScript
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-10-31T21:25:00.000Z'
originalURL: https://freecodecamp.org/news/loop-through-arrays-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/Colorful-Bold-Math-Factors-Lesson-and-Quiz.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment parcourir les tableaux en JavaScript
seo_desc: Looping through arrays in JavaScript is a fundamental concept that every
  JavaScript developer should understand. Whether you're a beginner or an experienced
  developer, understanding how to loop through an array is crucial for many programming
  tasks. ...
---

Parcourir les tableaux en JavaScript est un concept fondamental que tout développeur JavaScript devrait comprendre. Que vous soyez débutant ou développeur expérimenté, comprendre comment parcourir un tableau est crucial pour de nombreuses tâches de programmation. 

Dans cet article, nous explorerons les différentes façons de parcourir un tableau en JavaScript pour vous aider à saisir les concepts clés.

## Qu'est-ce qu'un tableau en JavaScript ?

Avant de plonger dans la façon de parcourir réellement les tableaux, commençons par les bases : qu'est-ce qu'un tableau ? 

En JavaScript, un tableau est une structure de données qui vous permet de stocker plusieurs valeurs dans une seule variable. Ces valeurs peuvent être de n'importe quel type de données, y compris des nombres, des chaînes de caractères, des objets et même d'autres tableaux. 

Vous pouvez créer un tableau en utilisant des crochets `[]`, et les éléments individuels sont séparés par des virgules. Voici un exemple de tableau :

```javascript
var fruits = ["apple", "banana", "cherry", "date"];

```

Dans cet exemple, `fruits` est un tableau contenant quatre chaînes de caractères.

### Pourquoi parcourir un tableau ?

Parcourir un tableau est nécessaire lorsque vous souhaitez effectuer des opérations sur les éléments du tableau. Vous pourriez avoir besoin de :

* Afficher les éléments sur une page web.
* Calculer la somme, la moyenne ou d'autres opérations mathématiques sur des valeurs numériques.
* Filtrer des éléments spécifiques qui répondent à certaines conditions.
* Modifier les éléments de quelque manière, comme changer leur format ou leurs valeurs.

Maintenant, explorons les différentes façons de parcourir les tableaux en JavaScript.

## Comment parcourir un tableau en JS

### 1. Utilisation de la boucle `for`

La boucle `for` traditionnelle est l'une des façons les plus simples et les plus polyvalentes de parcourir un tableau. Elle vous permet d'avoir un contrôle complet sur le comportement de la boucle.

```javascript
var fruits = ["apple", "banana", "cherry", "date"];

for (var i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

```

Dans cet exemple, nous commençons avec `i` égal à 0 et nous itérons à travers le tableau jusqu'à ce que `i` soit inférieur à la longueur du tableau `fruits`. Nous accédons à chaque élément en utilisant l'index `i` et nous l'affichons dans la console. Voici ce que cela retournera :

```
apple
banana
cherry
date

```

La boucle commence au premier élément (index 0), qui est "apple", et itère à travers chaque élément suivant, les affichant un par un jusqu'à ce qu'elle atteigne la fin du tableau.

### 2. Utilisation de la méthode `forEach`

La méthode `forEach` est une méthode JavaScript intégrée pour les tableaux qui simplifie le processus de parcours de chaque élément.

```javascript
var fruits = ["apple", "banana", "cherry", "date"];

fruits.forEach(function(fruit) {
    console.log(fruit);
});

```

La méthode `forEach` prend une fonction de rappel comme argument. Cette fonction est exécutée pour chaque élément du tableau, et l'élément est passé comme argument à la fonction. Dans cet exemple, nous affichons simplement chaque `fruit` dans la console :

```
apple
banana
cherry
date

```

### 3. Utilisation d'une boucle `for...of`

La boucle `for...of` est une autre façon moderne de parcourir un tableau. Elle est plus propre et plus concise que la boucle `for` traditionnelle.

```javascript
var fruits = ["apple", "banana", "cherry", "date"];

for (var fruit of fruits) {
    console.log(fruit);
}

```

Avec la boucle `for...of`, vous n'avez pas besoin de gérer manuellement une variable d'index comme dans la boucle `for` ou d'écrire une fonction de rappel séparée comme dans `forEach`. Vous itérez directement à travers les éléments du tableau.

```
apple
banana
cherry
date

```

Cela retournera chaque élément de notre tableau l'un après l'autre, tout comme les autres méthodes.

### 4. Utilisation d'une boucle `for...in` (Non recommandé pour les tableaux)

Bien que la boucle `for...in` soit adaptée pour itérer sur les propriétés d'un objet, elle n'est pas recommandée pour les tableaux. Elle peut également itérer sur des propriétés non indexées dans le prototype du tableau, ce qui peut entraîner des résultats inattendus.

```javascript
var fruits = ["apple", "banana", "cherry", "date"];

for (var index in fruits) {
    console.log(fruits[index]);
}

```

Il est plus sûr d'utiliser la boucle `for`, `forEach`, ou `for...of` lorsque vous travaillez avec des tableaux.

Bien que cette méthode fonctionne, elle peut avoir un comportement inattendu si le tableau a des propriétés supplémentaires au-delà des éléments indexés. Dans ce cas, c'est sûr car le tableau "fruits" est un tableau simple sans propriétés ajoutées, donc la sortie sera la même que précédemment :

```
apple
banana
cherry
date

```

### 5. Utilisation de la méthode `map`

La méthode `map` est utilisée pour créer un nouveau tableau en appliquant une fonction donnée à chaque élément du tableau original. Elle est utile lorsque vous souhaitez transformer les éléments d'un tableau et obtenir le résultat dans un nouveau tableau.

```javascript
var fruits = ["apple", "banana", "cherry", "date"];

var capitalizedFruits = fruits.map(function(fruit) {
    return fruit.toUpperCase();
});

console.log(capitalizedFruits);

```

Dans cet exemple, nous utilisons la méthode `map` pour créer un nouveau tableau `capitalizedFruits` en utilisant la méthode `map` pour transformer le tableau original "fruits". Elle convertira chaque élément du tableau "fruits" en majuscules, puis affichera le nouveau tableau dans la console. Voici la sortie :

```
[ 'APPLE', 'BANANA', 'CHERRY', 'DATE' ]

```

La méthode `map` applique la fonction de transformation (`fruit.toUpperCase()`) à chaque élément du tableau "fruits" et retourne un nouveau tableau avec les éléments transformés. Dans ce cas, elle met en majuscules chaque nom de fruit, résultant en un tableau de noms de fruits en majuscules.

### 6. Utilisation de la méthode `filter`

La méthode `filter` crée un nouveau tableau avec tous les éléments qui passent un test spécifié par une fonction de rappel. Elle est utile pour sélectionner les éléments qui répondent à certains critères.

```javascript
var numbers = [1, 2, 3, 4, 5, 6];

var evenNumbers = numbers.filter(function(number) {
    return number % 2 === 0;
});

console.log(evenNumbers);

```

La méthode `filter` crée ici un nouveau tableau nommé `evenNumbers` en utilisant la méthode `filter` sur le tableau original "numbers". Elle filtrera et inclura uniquement les nombres pairs du tableau "numbers". Voici la sortie :

```
[ 2, 4, 6 ]

```

La méthode `filter` applique la fonction donnée à chaque élément du tableau "numbers" et inclut les éléments dans le nouveau tableau si la fonction retourne `true`. Dans ce cas, elle vérifie si chaque nombre est pair (divisible par 2), et en conséquence, elle inclut uniquement les nombres pairs dans le tableau `evenNumbers`.

### 7. Utilisation de la méthode `reduce`

La méthode `reduce` est utilisée pour combiner les valeurs d'un tableau, résultant en une seule valeur. Elle est idéale pour effectuer des calculs sur les éléments d'un tableau, comme trouver la somme de tous les nombres.

```javascript
var numbers = [1, 2, 3, 4, 5];

var sum = numbers.reduce(function(total, currentNumber) {
    return total + currentNumber;
}, 0);

console.log(sum);


```

Dans cet exemple, nous allons calculer la somme de tous les nombres dans le tableau "numbers" en utilisant la méthode `reduce`. Elle initialise la `sum` avec `0`, puis elle itère à travers chaque élément du tableau, l'ajoutant à l'`accumulator`. Voici la sortie :

```
15

```

La méthode `reduce` combine les valeurs du tableau en appliquant la fonction fournie (dans ce cas, l'addition) à chaque élément et au total. Ainsi, elle additionne effectivement tous les nombres du tableau "numbers", résultant en une somme de `15`.

#### Effectuer des calculs plus complexes avec `reduce`

La méthode `reduce` peut également gérer des calculs plus complexes. Par exemple, vous pouvez l'utiliser pour traiter un tableau d'objets et extraire des informations spécifiques ou calculer un résultat plus complexe.

```javascript
var purchases = [
    { item: "Widget", price: 10 },
    { item: "Gadget", price: 25 },
    { item: "Doodad", price: 15 }
];

var totalPrice = purchases.reduce(function(accumulator, currentPurchase) {
    return accumulator + currentPurchase.price;
}, 0);

console.log("Total Price:", totalPrice);

```

Dans cet exemple, nous avons un tableau d'objets représentant des achats. Nous utilisons la méthode `reduce` pour calculer le prix total en accumulant la propriété `price` de chaque objet d'achat.

La polyvalence de la méthode `reduce` en fait un outil précieux pour gérer diverses calculs complexes et tâches de manipulation de données lors de la manipulation de tableaux en JavaScript. En fournissant une manière flexible de traiter les éléments de tableau, elle simplifie et rationalise les opérations, vous faisant gagner du temps et des efforts.

### 8. Utilisation des méthodes `some` et `every`

La méthode `some` vérifie si au moins un élément du tableau satisfait une condition donnée, tandis que la méthode `every` vérifie si tous les éléments répondent à une condition.

```javascript
var numbers = [1, 2, 3, 4, 5];

var isGreaterThanThree = numbers.some(function(number) {
    return number > 3;
});

var allGreaterThanZero = numbers.every(function(number) {
    return number > 0;
});

console.log(isGreaterThanThree);  // true
console.log(allGreaterThanZero);  // true

```

Dans cet exemple, le code vérifie deux conditions sur le tableau "numbers" en utilisant les méthodes `some` et `every`. Voici les résultats :

1. `isGreaterThanThree` est `true` car au moins un élément du tableau "numbers" (par exemple, `4` et `5`) est supérieur à `3`.

2. `allGreaterThanZero` est également `true` car tous les éléments du tableau "numbers" sont supérieurs à `0`.

Ainsi, le code affiche correctement `true` pour les deux conditions :

```
true
true

```

La méthode `some` vérifie si au moins un élément satisfait la condition, tandis que la méthode `every` vérifie si tous les éléments répondent à la condition. Dans ce cas, les deux conditions sont remplies, donc la sortie est `true` pour les deux vérifications.

Si seulement une des conditions est remplie, le code affichera toujours le résultat en conséquence. Supposons qu'une seule condition est remplie, par exemple, `isGreaterThanThree`, et que la condition `allGreaterThanZero` n'est pas remplie. Dans ce cas, le code ressemblerait à ceci :

```javascript
var numbers = [1, 2, 3, 4, 5];

var isGreaterThanThree = numbers.some(function(number) {
    return number > 3;
});

var allGreaterThanZero = numbers.every(function(number) {
    return number > 0;
});

console.log(isGreaterThanThree);  // true
console.log(allGreaterThanZero);  // false

```

Dans ce scénario :

* `isGreaterThanThree` est `true` car au moins un élément est supérieur à `3`.
* `allGreaterThanZero` est `false` car tous les éléments ne sont pas supérieurs à `0`.

Le code affichera correctement `true` pour la condition `isGreaterThanThree` et `false` pour la condition `allGreaterThanZero` :

```
true
false

```

La sortie reflétera les résultats de chaque vérification de condition individuelle.

### 9. Utilisation de `for...in` avec des objets

Lorsque vous avez un tableau d'objets, vous pouvez utiliser la boucle `for...in` pour itérer à travers les propriétés de chaque objet.

```javascript
var people = [
    { name: "Alice", age: 25 },
    { name: "Bob", age: 30 },
    { name: "Charlie", age: 35 }
];

for (var person of people) {
    for (var key in person) {
        console.log(key + ": " + person[key]);
    }
}

```

Dans cet exemple, nous parcourons un tableau d'objets, "people", et pour chaque objet (person), nous itérons davantage à travers ses propriétés en utilisant une boucle `for...in` imbriquée pour afficher toutes les propriétés et leurs valeurs.

Voici la sortie :

```
name: Alice
age: 25
name: Bob
age: 30
name: Charlie
age: 35

```

### 10. Utilisation de la boucle `for...of` avec des objets

La boucle `for...of` peut également être utilisée avec des tableaux d'objets pour itérer à travers les objets eux-mêmes.

```javascript
var people = [
    { name: "Alice", age: 25 },
    { name: "Bob", age: 30 },
    { name: "Charlie", age: 35 }
];

for (var person of people) {
    console.log("Name: " + person.name + ", Age: " + person.age);
}

```

Dans cet exemple, la boucle `for...of` itère à travers chaque objet (person) dans le tableau "people" et affiche une chaîne qui inclut le nom et l'âge de la personne, créant une sortie bien formatée.

Voici la sortie :

```
Name: Alice, Age: 25
Name: Bob, Age: 30
Name: Charlie, Age: 35

```

## Comment combiner les méthodes de tableau

L'une des forces de JavaScript est sa capacité à enchaîner plusieurs méthodes de tableau pour accomplir des tâches plus complexes de manière efficace. 

Passons en revue un exemple de la façon de filtrer certains éléments d'un tableau en utilisant la méthode `filter` puis de transformer les éléments restants en utilisant la méthode `map`.

```javascript
var numbers = [1, 2, 3, 4, 5, 6];

// D'abord, filtrons les nombres pairs.
var evenNumbers = numbers.filter(function(number) {
    return number % 2 === 0;
});

// Maintenant, doublons chacun des nombres pairs en utilisant la méthode map.
var doubledEvenNumbers = evenNumbers.map(function(number) {
    return number * 2;
});

console.log("Original Numbers: " + numbers); // [1, 2, 3, 4, 5, 6]
console.log("Even Numbers: " + evenNumbers);   // [2, 4, 6]
console.log("Doubled Even Numbers: " + doubledEvenNumbers); // [4, 8, 12]

```

Dans cet exemple, nous commençons avec un tableau de `numbers`, et nous voulons effectuer les étapes suivantes :

1. Filtrer les nombres pairs.
2. Doubler chacun des nombres pairs.

Nous y parvenons en utilisant d'abord la méthode `filter` pour créer un nouveau tableau `evenNumbers` contenant uniquement les nombres pairs du tableau `numbers`. Ensuite, nous utilisons la méthode `map` pour doubler chaque élément du tableau `evenNumbers`, résultant en le tableau `doubledEvenNumbers`.

En combinant ces deux méthodes de tableau, nous avons effectivement filtré et transformé le tableau original pour obtenir le résultat souhaité.

Voici la sortie :

```
Original Numbers: 1,2,3,4,5,6
Even Numbers: 2,4,6
Doubled Even Numbers: 4,8,12

```

Cette approche est non seulement plus lisible, mais aussi plus efficace que d'obtenir le même résultat avec des boucles traditionnelles. Elle tire parti de la nature fonctionnelle de JavaScript et de la puissance des méthodes de tableau, rendant votre code plus propre et plus facile à maintenir.

## Conclusion

Parcourir les tableaux en JavaScript est une compétence fondamentale pour tout développeur. Que vous préfériez la boucle `for` traditionnelle, la boucle concise `for...of`, ou les méthodes de tableau pratiques comme `forEach`, le choix dépend de votre cas d'utilisation spécifique et de votre style de codage. Chaque méthode a ses avantages, il est donc important de les comprendre toutes.

En maîtrisant les différentes façons de parcourir les tableaux, vous serez mieux équipé pour travailler avec les tableaux dans vos applications JavaScript. Que vous manipuliez des données, affichiez des informations sur une page web, ou effectuiez des calculs complexes, ces techniques de parcours de tableau sont des outils essentiels dans votre boîte à outils JavaScript.