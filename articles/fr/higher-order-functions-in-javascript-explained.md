---
title: Fonctions d'ordre supérieur en JavaScript – Expliquées avec des exemples pratiques
subtitle: ''
author: Sobit Prasad
co_authors: []
series: null
date: '2023-01-03T22:11:58.000Z'
originalURL: https://freecodecamp.org/news/higher-order-functions-in-javascript-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/higher-order-functions-in-javascript-2.png
tags:
- name: functions
  slug: functions
- name: JavaScript
  slug: javascript
seo_title: Fonctions d'ordre supérieur en JavaScript – Expliquées avec des exemples
  pratiques
seo_desc: 'As a web developer, you should always strive to learn new techniques and
  discover ways to work smarter with JavaScript.

  One such technique is using higher order functions. Higher order functions are functions
  that take one or more functions as argume...'
---

En tant que développeur web, vous devriez toujours chercher à apprendre de nouvelles techniques et à découvrir des moyens de travailler plus intelligemment avec JavaScript.

L'une de ces techniques consiste à utiliser des fonctions d'ordre supérieur. Les fonctions d'ordre supérieur sont des fonctions qui prennent une ou plusieurs fonctions comme arguments, ou retournent une fonction comme résultat.

Dans cet article, nous allons approfondir ce qu'est une fonction d'ordre supérieur, les avantages de les utiliser, et comment les utiliser dans des applications pratiques.

## Qu'est-ce qu'une fonction d'ordre supérieur ?

Une fonction d'ordre supérieur est une fonction qui prend une ou plusieurs fonctions comme arguments, ou retourne une fonction comme résultat.

Il existe plusieurs types différents de fonctions d'ordre supérieur comme map et reduce. Nous discuterons de celles-ci plus tard dans ce tutoriel. Mais avant cela, plongeons d'abord profondément dans ce que sont les fonctions d'ordre supérieur.

```js
// Fonction de rappel, passée comme paramètre dans la fonction d'ordre supérieur
function callbackFunction(){
    console.log('Je suis une fonction de rappel');
}

// fonction d'ordre supérieur
function higherOrderFunction(func){
    console.log('Je suis une fonction d'ordre supérieur')
    func()
}

higherOrderFunction(callbackFunction);
```

Dans le code ci-dessus, `higherOrderFunction()` est une fonction d'ordre supérieur car nous passons une fonction de rappel comme paramètre.

L'exemple ci-dessus est assez simple, n'est-ce pas ? Alors développons-le davantage et voyons comment vous pouvez utiliser les fonctions d'ordre supérieur pour écrire un code plus concis et modulaire.

### Comment fonctionnent les fonctions d'ordre supérieur

Supposons que je veux que vous écriviez une fonction qui calcule l'aire et le diamètre d'un cercle. En tant que débutant, la première solution qui nous vient à l'esprit est d'écrire chaque fonction séparée pour calculer l'aire ou le diamètre.

```js
const radius = [1, 2, 3];
```

```js
// fonction pour calculer l'aire du cercle
const calculateArea =  function (radius) {
    const output = [];
    for(let i = 0; i< radius.length; i++){
        output.push(Math.PI * radius[i] * radius[i]);
    }
    return output;
}
```

```js
// fonction pour calculer le diamètre du cercle
const calculateDiameter =  function (radius) {
    const output = [];
    for(let i = 0; i< radius.length; i++){
        output.push(2 * radius[i]);
    }
    return output;
}
```

```js
console.log(calculateArea(radius));
console.log(calculateDiameter(radius))
```

Mais avez-vous remarqué le problème avec le code ci-dessus ? N'écrivons-nous pas presque la même fonction encore et encore avec une logique légèrement différente ? De plus, les fonctions que nous avons écrites ne sont pas réutilisables, n'est-ce pas ?

Alors, voyons comment nous pouvons écrire le même code en utilisant des fonctions d'ordre supérieur :

```js
const radius = [1, 2, 3];
```

```js
// logique pour calculer l'aire
const area = function(radius){
    return Math.PI * radius * radius;
}
```

```js
// logique pour calculer le diamètre
const diameter = function(radius){
    return 2 * radius;
}
```

```js
// une fonction réutilisable pour calculer l'aire, le diamètre, etc
const calculate = function(radius, logic){ 
    const output = [];
    for(let i = 0; i < radius.length; i++){
        output.push(logic(radius[i]))
    }
    return output;
}
```

```js
console.log(calculate(radius, area));
console.log(calculate(radius, diameter));
```

Maintenant, comme vous pouvez le voir dans le code ci-dessus, nous n'avons écrit qu'une seule fonction `calculate()` pour calculer l'aire et le diamètre du cercle. Nous devons seulement écrire la logique et la passer à `calculate()` et la fonction fera le travail.

Le code que nous avons écrit en utilisant des fonctions d'ordre supérieur est concis et modulaire. Chaque fonction fait son propre travail et nous ne répétons rien ici.

Supposons que dans le futur, si nous voulons écrire un programme pour calculer la circonférence du cercle. Nous pouvons simplement écrire la logique pour calculer la circonférence et la passer à la fonction `calculate()`.

```js
const circumeference = function(radius){
    return 2 * Math.PI * radius;
}
```

```js
console.log(calculate(radius, circumeference));
```

## Comment utiliser les fonctions d'ordre supérieur

Vous pouvez utiliser les fonctions d'ordre supérieur de diverses manières.

Lorsque vous travaillez avec des tableaux, vous pouvez utiliser les fonctions `map()`, `reduce()`, `filter()`, et `sort()` pour manipuler et transformer les données dans un tableau.

Lorsque vous travaillez avec des objets, vous pouvez utiliser la fonction `Object.entries()` pour créer un nouveau tableau à partir d'un objet.

Lorsque vous travaillez avec des fonctions, vous pouvez utiliser la fonction `compose()` pour créer des fonctions complexes à partir de fonctions plus simples.

## Comment utiliser certaines fonctions d'ordre supérieur importantes

Il existe diverses fonctions d'ordre supérieur intégrées, et certaines des plus courantes sont map(), filter() et reduce(). Alors, comprenons chacune d'entre elles en détail.

### **Comment utiliser** `map()` en JavaScript

La fonction `map()` prend un tableau de valeurs et applique une transformation à chaque valeur dans le tableau. Elle ne modifie pas le tableau original. Elle est souvent utilisée pour transformer un tableau de données en un nouveau tableau avec une structure différente.

Comprenons avec l'aide d'exemples.

**Exemple 1** : Supposons que nous voulons ajouter 10 à chaque élément d'un tableau. Nous pouvons utiliser la méthode `map()` pour parcourir chaque élément du tableau et ajouter 10.

```js
const arr = [1, 2, 3, 4, 5];
const output = arr.map((num) => num += 10)
console.log(arr); // [1, 2, 3, 4, 5]
console.log(output); // [11, 12, 13, 14, 15]
```

Dans l'exemple ci-dessus, `arr` est un tableau avec cinq éléments : 1, 2, 3, 4, et 5. `map` est une méthode que nous utilisons pour appliquer une fonction à chaque élément d'un tableau, et elle retourne un nouveau tableau avec les éléments modifiés.

La fonction de rappel qui est passée à `map` utilise la syntaxe de fonction fléchée, et elle prend un seul argument `num`. Cette fonction ajoute 10 à `num` (chaque élément du tableau) et retourne le résultat.

**Exemple 2** : Ici, nous avons un tableau d'utilisateurs. Supposons que nous voulons seulement leurs prénom et nom de famille. Nous pouvons simplement utiliser la méthode `map()` pour les extraire du tableau `users`.

```js
const users = [
    {firstName: 'John', lastName: 'Doe', age: 25},
    {firstName: 'Jane', lastName: 'Doe', age: 30},
    {firstName: 'Jack', lastName: 'Doe', age: 35},
    {firstName: 'Jill', lastName: 'Doe', age: 40},
    {firstName: 'Joe', lastName: 'Doe', age: 45},
]

const result = users.map((user) => user.firstName + ' ' + user.lastName)
console.log(result); // ['John Doe', 'Jane Doe', 'Jack Doe', 'Jill Doe', 'Joe Doe']
```

Dans le code ci-dessus, `users` est un tableau d'objets représentant des utilisateurs. Chaque objet a trois propriétés : `firstName`, `lastName`, et `age`.

Nous parcourons chaque utilisateur en utilisant la méthode `map()` pour extraire les propriétés `firstName` et `lastName`.

La fonction de rappel prend un seul argument `user` qui représente un élément dans le tableau `users` (un objet).

La fonction concatène les propriétés `firstName` et `lastName` de l'objet `user`, et retourne le résultat.

### **Comment utiliser** `filter()` en JavaScript

La fonction `filter()` prend un tableau et retourne un nouveau tableau avec seulement les valeurs qui répondent à certains critères. Elle ne modifie pas non plus le tableau original. Elle est souvent utilisée pour sélectionner un sous-ensemble de données à partir d'un tableau en fonction de certains critères.

**Exemple 1** : Vous pouvez utiliser `filter()` pour retourner seulement les nombres impairs d'un tableau de nombres.

```js
const arr = [1, 2, 3, 4, 5];
const output = arr.filter((num) => num % 2) // filtrer les nombres impairs
console.log(arr); // [1, 2, 3, 4, 5]
console.log(output); // [1, 3, 5]
```

Dans le code ci-dessus, `arr` est un tableau avec cinq éléments : 1, 2, 3, 4, et 5. `filter` est une méthode qui est utilisée pour créer un nouveau tableau avec des éléments qui passent un test spécifié dans une fonction de rappel fournie.

Cette fonction de rappel vérifie si `num` est impair en vérifiant s'il n'est pas divisible par 2 (`num % 2`). Si `num` n'est pas divisible par 2, la fonction retourne `true`, sinon elle retourne `false`.

Lorsque `filter` est appelé sur `arr`, il applique cette fonction à chaque élément du tableau, créant un nouveau tableau avec seulement les éléments qui ont retourné `true` ou qui ont passé la condition spécifiée lorsqu'ils sont passés à la fonction. Le tableau `arr` original reste inchangé et retourne le résultat.

**Exemple 2** : Vous pouvez utiliser `filter()` pour retourner seulement les utilisateurs ayant un âge supérieur à 30 dans un tableau.

```js
const users = [
    {firstName: 'John', lastName: 'Doe', age: 25},
    {firstName: 'Jane', lastName: 'Doe', age: 30},
    {firstName: 'Jack', lastName: 'Doe', age: 35},
    {firstName: 'Jill', lastName: 'Doe', age: 40},
    {firstName: 'Joe', lastName: 'Doe', age: 45},
]

// Trouver les utilisateurs ayant un âge supérieur à 30
const output = users.filter(({age}) => age > 30)
console.log(output); // [{firstName: 'Jack', lastName: 'Doe', age: 35}, {firstName: 'Jill', lastName: 'Doe', age: 40}, {firstName: 'Joe', lastName: 'Doe', age: 45}]
```

Dans le code ci-dessus, `users` est un tableau d'objets représentant des utilisateurs. Chaque objet a trois propriétés : `firstName`, `lastName`, et `age`.

`filter` est appelé sur le tableau `users` et il applique une fonction de rappel à chaque élément du tableau.

La fonction prend un seul argument, un objet déstructuré en une seule propriété `age`. Cette fonction vérifie si `age` est supérieur à 30. Si c'est le cas, la fonction retourne `true`, sinon elle retourne `false`.

Lorsque `filter` est appelé sur `users`, il applique cette fonction à chaque élément du tableau, créant un nouveau tableau avec seulement les éléments qui ont retourné `true` lorsqu'ils sont passés à la fonction et retourne le résultat. Le tableau `users` original reste inchangé.

### **Comment utiliser** `reduce()` en JavaScript

La méthode `reduce()` est un peu écrasante. Si vous avez déjà rencontré la méthode `reduce()` et ne l'avez pas comprise du premier coup, c'est tout à fait normal.

Mais ne vous inquiétez pas – ici, nous allons l'apprendre à travers plusieurs exemples et je vais faire de mon mieux pour vous faire comprendre cette méthode.

Maintenant, un doute qui pourrait vous venir à l'esprit est pourquoi nous utilisons la méthode `reduce()`. Comme il existe déjà de nombreuses méthodes, comment pouvons-nous décider laquelle utiliser et quand ?

Dans le cas de la méthode `reduce()`, vous devriez l'utiliser lorsque vous voulez effectuer une opération sur les éléments d'un tableau et retourner une seule valeur comme résultat. La "valeur unique" fait référence au résultat accumulé de l'application répétée d'une fonction aux éléments d'une séquence.

Par exemple, vous pourriez utiliser `reduce()` pour additionner tous les éléments d'un tableau, pour trouver la valeur maximale ou minimale, pour fusionner plusieurs objets en un seul objet, ou pour regrouper différents éléments dans un tableau.

Maintenant, comprenons tout cela avec l'aide d'exemples.

**Exemple 1** : Utilisation de `reduce()` pour additionner tous les éléments d'un tableau :

```js
const numbers = [1, 2, 3, 4, 5];

const sum = numbers.reduce((total, currentValue) => {
    return total + currentValue;
}, 0)

console.log(sum); // 15
```

Dans cet exemple, la méthode `reduce()` est appelée sur le tableau `numbers` et reçoit une fonction de rappel qui prend deux arguments : `total` et `currentValue`.

L'argument `total` est l'accumulation des valeurs qui ont été retournées par la fonction jusqu'à présent, et `currentValue` est l'élément actuel en cours de traitement dans le tableau.

La méthode `reduce()` prend également une valeur initiale comme deuxième argument, dans ce cas `0`, qui est utilisée comme valeur initiale de `total` pour la première itération.

À chaque itération, la fonction ajoute la valeur actuelle au total et retourne la nouvelle valeur du total.

La méthode `reduce()` utilise ensuite la valeur retournée comme `total` pour l'itération suivante, jusqu'à ce qu'elle ait traité tous les éléments du tableau.

Enfin, elle retourne la valeur finale du total, qui est la somme de tous les éléments du tableau.

**Exemple 2** : Utilisation de `reduce()` pour trouver la valeur maximale dans un tableau :

```js
let numbers = [5, 20, 100, 60, 1];
const maxValue = numbers.reduce((max, curr) => {
    if(curr > max) max = curr;
    return max;
});
console.log(maxValue); // 100
```

Dans cet exemple, nous avons à nouveau deux arguments `max` et `curr` dans la fonction de rappel. Remarquez que nous n'avons pas passé le deuxième paramètre dans la méthode `reduce()` cette fois. Donc, la valeur par défaut sera le premier élément du tableau.

La fonction de rappel vérifie d'abord si l'élément actuel `curr` est supérieur à la valeur maximale actuelle `max`. Si c'est le cas, elle met à jour la valeur de `max` pour qu'elle soit l'élément actuel. Si ce n'est pas le cas, `max` n'est pas mis à jour. Enfin, la fonction retourne la valeur de `max`.

Dans ce cas, la méthode `reduce()` commencera par définir `max` à 5 et `curr` à 20. Elle vérifiera ensuite si 20 est supérieur à 5, ce qui est le cas, donc elle mettra à jour `max` à 20.

Elle définira ensuite `curr` à 100 et vérifiera si 100 est supérieur à 20, ce qui est le cas, donc elle mettra à jour `max` à 100.

Elle continuera ce processus jusqu'à ce qu'elle ait traité tous les éléments du tableau. La valeur finale de `max` sera la valeur maximale dans le tableau, qui est 100 dans ce cas.

**Exemple 3** : Utilisation de `reduce()` pour fusionner différents objets en un seul objet :

```js
const obj1 = { a: 1, b: 2 };
const obj2 = { c: 3, d: 4 };
const obj3 = { e: 5, f: 6 };
const mergedObj = [obj1, obj2, obj3].reduce((acc, curr) => {
    return { ...acc, ...curr };
}, {});
console.log(mergedObj); // { a: 1, b: 2, c: 3, d: 4, e: 5, f: 6 }
```

Dans cet exemple, nous avons deux arguments `acc` et `curr` dans la fonction de rappel. `acc` représente l'objet fusionné actuel qui a été créé jusqu'à présent, tandis que `curr` représente l'objet actuel en cours de traitement dans le tableau.

La fonction utilise l'opérateur de propagation (`...`) pour créer un nouvel objet qui combine les propriétés de l'objet fusionné actuel `acc` et de l'objet actuel `curr`. Elle retourne ensuite cet nouvel objet.

Dans ce cas, la méthode `reduce()` commencera par définir `acc` à un objet vide (qui est la valeur passée comme deuxième argument à `reduce()`). Elle définira ensuite `curr` à `obj1`, et créera un nouvel objet qui combine les propriétés de l'objet vide et `obj1`. Elle définira ensuite `curr` à `obj2` et créera un nouvel objet qui combine les propriétés de l'objet fusionné précédent et `obj2`. Elle continuera ce processus jusqu'à ce qu'elle ait traité tous les objets du tableau.

La valeur finale de `acc` sera l'objet fusionné, qui contiendra toutes les propriétés des objets originaux.

**Exemple 4** : Utilisation de `reduce()` pour regrouper des objets dans un tableau. Par exemple, regrouper des produits dans un panier d'achat selon leur nom de marque.

```js
const shoppingCart = [
    {name: 'Apple', price: 1.99, quantity: 3},
    {name: 'Apple', price: 1.99, quantity: 3},
    {name: 'Xiomi', price: 2.99, quantity: 2},
    {name: 'Samsung', price: 3.99, quantity: 1},
    {name: 'Tesla', price: 3.99, quantity: 1},
    {name: 'Tesla', price: 4.99, quantity: 4},
    {name: 'Nokia', price: 4.99, quantity: 4},
]

const products = shoppingCart.reduce((productGroup, product) => {
    const name = product.name;
    if(productGroup[name] == null) {
        productGroup[name] = [];
    }
    productGroup[name].push(product);

    return productGroup;
}, {});

console.log(products);
```

```json
// SORTIE
{
  Apple: [
    { name: 'Apple', price: 1.99, quantity: 3 },
    { name: 'Apple', price: 1.99, quantity: 3 }
  ],
  Xiomi: [ { name: 'Xiomi', price: 2.99, quantity: 2 } ],
  Samsung: [ { name: 'Samsung', price: 3.99, quantity: 1 } ],
  Tesla: [
    { name: 'Tesla', price: 3.99, quantity: 1 },
    { name: 'Tesla', price: 4.99, quantity: 4 }
  ],
  Nokia: [ { name: 'Nokia', price: 4.99, quantity: 4 } ]
}
```

Dans cet exemple, nous avons le tableau `shoppingCart` représentant différents produits et deux arguments `productGroup` et `product` dans la fonction de rappel.

L'argument `productGroup` représente le groupe actuel de produits qui ont été trouvés jusqu'à présent, tandis que l'argument `product` représente le produit actuel en cours de traitement dans le tableau.

La fonction obtient d'abord le nom du produit actuel en utilisant `product.name`. Elle vérifie ensuite s'il existe déjà un groupe pour ce nom de produit dans l'objet `productGroup` en utilisant l'instruction `if`. Si ce n'est pas le cas, elle crée un nouveau groupe en initialisant la propriété `productGroup[name]` à un tableau vide.

Enfin, la fonction pousse le produit actuel dans le groupe en utilisant la méthode `push()`, et retourne l'objet `productGroup` mis à jour.

Après que la méthode `reduce()` ait traité tous les éléments du tableau `shoppingCart`, l'objet `productGroup` résultant contiendra des clés pour chaque nom de produit, et des valeurs qui sont des tableaux de produits avec ce nom.

## Avantages des fonctions d'ordre supérieur

L'utilisation de fonctions d'ordre supérieur présente certains avantages importants pour les développeurs web.

Premièrement, les fonctions d'ordre supérieur peuvent aider à améliorer la lisibilité de votre code en le rendant plus concis et facile à comprendre. Cela peut aider à accélérer le processus de développement et à faciliter le débogage du code.

Deuxièmement, les fonctions d'ordre supérieur peuvent aider à organiser votre code en morceaux plus petits, ce qui le rend plus facile à maintenir et à étendre.

## Conclusion

Cet article a exploré ce qu'est une fonction d'ordre supérieur, les avantages de les utiliser, et comment les utiliser dans des applications pratiques.

En utilisant des fonctions d'ordre supérieur, les développeurs web peuvent travailler plus intelligemment en organisant leur code en morceaux plus petits et en le rendant plus lisible et plus facile à déboguer.

Maintenant, chaque fois que vous essayez d'utiliser les méthodes map(), filter() et reduce() et que vous êtes confus, rappelez-vous simplement ce qui suit :

* Utilisez map lorsque vous voulez transformer un tableau
    
* Utilisez filter pour sélectionner un sous-ensemble de données à partir d'un tableau, et
    
* Utilisez reduce lorsque vous voulez retourner une seule valeur comme résultat.
    

Pour plus de lectures sur les fonctions d'ordre supérieur, consultez cette vidéo géniale d'Akshay Saini sur [YouTube](https://www.youtube.com/watch?v=HkWxvB1RJq0).