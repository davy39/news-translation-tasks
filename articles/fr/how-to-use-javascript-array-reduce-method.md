---
title: Comment utiliser la méthode Array reduce() de JavaScript – Expliqué avec des
  exemples
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2023-11-29T18:30:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-javascript-array-reduce-method
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/js-reduce.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser la méthode Array reduce() de JavaScript – Expliqué avec
  des exemples
seo_desc: "Hello again, friends! The reduce() method is one of the most confusing\
  \ Array methods in JavaScript. So in this article, I’m going to help you clearly\
  \ see how the method works. \nI'm also going to show some examples that'll help\
  \ you understand how and ..."
---

Bonjour à tous, amis ! La méthode `reduce()` est l'une des méthodes de tableau les plus déroutantes en JavaScript. Donc, dans cet article, je vais vous aider à comprendre clairement comment cette méthode fonctionne.

Je vais également vous montrer quelques exemples qui vous aideront à comprendre comment et où vous pourriez vouloir utiliser cette méthode. Ne vous inquiétez pas ! `reduce()` est en fait simple une fois que vous comprenez comment cela fonctionne.

## Comment fonctionne la méthode `reduce()`

La méthode `reduce()` tire son nom de la fonctionnalité qu'elle offre, qui est d'itérer et de "réduire" les valeurs d'un tableau en une seule valeur.

Le moyen le plus simple de comprendre comment la méthode `reduce()` fonctionne est à travers un exemple, alors regardons d'abord un exemple facile.

Supposons que vous avez un tableau d'objets qui contiennent une propriété `name` et `price` comme suit :

```js
const items = [
  { name: 'Apple', price: 1 },
  { name: 'Orange', price: 2 },
  { name: 'Mango', price: 3 },
];
```

Ensuite, vous devez obtenir la somme de la propriété `price` et obtenir le prix total. Vous pouvez faire cela en utilisant la méthode `forEach()` comme suit :

```js
const items = [
  { name: 'Apple', price: 1 },
  { name: 'Orange', price: 2 },
  { name: 'Mango', price: 3 },
];

let totalPrice = 0;

items.forEach(item => {
  totalPrice += item.price;
})

console.log(totalPrice); // 6
```

Tout d'abord, nous déclarons la variable `totalPrice` et lui attribuons la valeur `0`. Ensuite, nous appelons la méthode `forEach()` pour itérer sur le tableau `items`, en ajoutant le prix de chaque article à `totalPrice`.

Le code ci-dessus fonctionne, mais puisque nous cherchons à obtenir une seule valeur à partir du tableau, la méthode `reduce()` serait plus adaptée à la tâche.

La méthode `reduce()` fonctionne de manière similaire à la méthode `forEach()`, avec la capacité supplémentaire de collecter le résultat de chaque itération en une seule valeur.

Essayons d'obtenir le prix total en utilisant la méthode `reduce()`. Tout d'abord, vous devez appeler la méthode `reduce()` et passer deux paramètres à la fonction de rappel : `accumulator` et `item`.

```js
const totalPrice = items.reduce((accumulator, item) => {
  return accumulator += item.price;
}, 0)
```

Le paramètre `accumulator` est la valeur unique qui sera retournée par la méthode `reduce()`. Il contiendra la valeur retournée par la fonction de rappel à chaque itération.

Le paramètre `item` est simplement l'élément du tableau, qui changera à chaque itération comme dans la méthode `forEach()`.

Lors de la première itération, le paramètre `accumulator` contiendra la valeur que vous avez passée comme deuxième argument de la méthode `reduce()`. Dans le cas ci-dessus, c'est `0`.

Lorsque nous utilisons la méthode `forEach()`, nous faisons des affectations d'addition `+=` à la variable `totalPrice`, nous la déclarons donc en utilisant le mot-clé `let`. Mais lorsque vous utilisez la méthode `reduce()`, vous pouvez utiliser le mot-clé `const` car nous n'affectons une valeur à `totalPrice` qu'une seule fois.

Et c'est essentiellement comment la méthode `reduce()` fonctionne. Elle itère sur chaque élément de votre tableau, et chaque itération retourne une seule valeur, qui est l'`accumulator`.

Lorsque l'itération est terminée, la valeur de l'`accumulator` sera retournée par la méthode.

## Quand utiliser la méthode `reduce()`

Comme montré ci-dessus, la méthode `reduce()` est recommandée lorsque vous avez besoin d'obtenir une seule valeur à partir de l'itération sur votre tableau.

Cela inclut :

* Résumer vos valeurs en une seule valeur
* Regrouper des éléments similaires ensemble
* Supprimer les doublons d'un tableau

La valeur unique retournée par la méthode peut également être un tableau d'objets, contenant donc plusieurs valeurs.

Vous avez vu comment faire la somme des valeurs dans la section précédente, alors regardons quelques exemples de regroupement d'éléments et de suppression des doublons ensuite.

### Comment regrouper des éléments similaires ensemble

Supposons que vous avez à nouveau un tableau d'objets, mais cette fois, les objets ont des propriétés `name` et `category` :

```js
const items = [
  { name: 'Apple', category: 'Fruit' },
  { name: 'Onion', category: 'Vegetable' },
  { name: 'Orange', category: 'Fruit' },
  { name: 'Lettuce', category: 'Vegetable' },
];
```

Maintenant, vous voulez regrouper ces éléments en fonction de leur valeur `category`. Vous pouvez utiliser la méthode `reduce()` et retourner une seule valeur d'objet.

Tout d'abord, vous appelez la méthode reduce et passez un objet vide `{}` comme valeur initiale de l'`accumulator` :

```js
const groupedItems = items.reduce((accumulator, item) => {

}, {})
```

Ensuite, vous vérifiez si l'objet accumulator a déjà une propriété avec le même nom que la `category` de votre objet `item`.

Si ce n'est pas le cas, déclarez cette propriété comme un tableau vide comme suit :

```js
const category = item.category;
if (!accumulator[category]) {
  accumulator[category] = []
}
```

Après cela, ajoutez la propriété `item.name` à la propriété `accumulator[category]`, et retournez l'`accumulator` comme ceci :

```js
accumulator[category].push(item.name);
return accumulator
```

Et c'est tout. Maintenant vous avez un objet qui regroupe les éléments en fonction de la valeur `category` :

```js
const items = [
  { name: 'Apple', category: 'Fruit' },
  { name: 'Onion', category: 'Vegetable' },
  { name: 'Orange', category: 'Fruit' },
  { name: 'Lettuce', category: 'Vegetable' },
];

const groupedItems = items.reduce((accumulator, item) => {
  const category = item.category;
  if (!accumulator[category]) {
    accumulator[category] = []
  }
  accumulator[category].push(item.name);
  return accumulator
}, {})

console.log(groupedItems);
// { Fruit: [ 'Apple', 'Orange' ], Vegetable: [ 'Onion', 'Lettuce' ] }
```

Ensuite, voyons comment supprimer les doublons en utilisant la méthode `reduce()` :

### Comment supprimer les doublons en utilisant la méthode `reduce()`

Pour supprimer les doublons en utilisant la méthode `reduce()`, vous devez déclarer un tableau comme valeur de l'`accumulator`.

À chaque itération, vérifiez si l'`item` est déjà inclus dans l'`accumulator` en utilisant la méthode `includes()`.

Si l'`item` n'est pas déjà inclus, ajoutez l'`item` dans l'`accumulator`. Voir l'exemple ci-dessous :

```js
const items = [1, 2, 3, 1, 2, 3, 7, 8, 7];

const noDuplicateItems = items.reduce((accumulator, item) => {
  if (!accumulator.includes(item)) {
    accumulator.push(item);
  }
  return accumulator;
}, []);

console.log(noDuplicateItems); 
// [ 1, 2, 3, 7, 8 ]
```

Ici, vous pouvez voir que la méthode `reduce()` retourne un tableau (sans doublons) au lieu d'une seule valeur.

## Pourquoi la valeur initiale de l'accumulateur est importante

Dans tous les exemples ci-dessus, vous avez vu comment nous avons ajouté une valeur initiale pour l'accumulateur comme deuxième argument passé à la méthode `reduce()`.

Si vous n'ajoutez pas la valeur initiale de l'accumulateur, alors `reduce()` prendra le premier élément de votre tableau comme valeur initiale de l'accumulateur.

Vous pouvez tester cela en enregistrant la valeur de l'`accumulator` à l'intérieur de la fonction de rappel comme suit :

```js
const items = [
  { name: 'Apple', price: 1 },
  { name: 'Orange', price: 2 },
  { name: 'Mango', price: 3 },
];

const totalPrice = items.reduce((accumulator, item) => {
  console.log(accumulator); // log the accumulator
  return accumulator += item.price;
}, 0)
```

Exécutez le code ci-dessus, et vous obtiendrez le résultat suivant :

```txt
0
1
3
```

Dans la première itération, l'`accumulator` utilise la valeur initiale que nous avons passée comme deuxième argument à la méthode `reduce()`, qui est `0`.

Si vous retirez `0` du code, alors la sortie sera :

```txt
{ name: 'Apple', price: 1 }
[object Object]2
```

Parce que nous n'avons pas fourni de valeur initiale pour l'`accumulator`, la méthode prend la valeur que nous avons placée à l'index 0 comme valeur initiale de l'`accumulator`.

Selon le contenu de votre tableau, la valeur initiale peut être un objet, un tableau ou une seule valeur. Compter sur la valeur du tableau comme valeur initiale de l'accumulateur est considéré comme une mauvaise pratique car cela peut entraîner des bugs, vous devez donc toujours définir la valeur initiale de l'accumulateur.

## Paramètres complets du rappel `reduce()`

Une dernière chose avant de conclure l'article. Dans tous les exemples ci-dessus, nous définissons 2 paramètres pour la fonction de rappel, mais la méthode `reduce()` passe en réalité 4 arguments à la fonction de rappel :

* La valeur de l'`accumulator`
* La valeur de l'`item`
* L'`index` de l'élément actuel dans l'itération
* Le `tableau` à partir duquel vous appelez la méthode elle-même

La syntaxe complète de la méthode est la suivante :

```js
Array.reduce((accumulator, item, index, array) => {
  // TODO: Définir le processus pour chaque itération ici
}, initialAccumulatorValue)
```

Dans la plupart des cas, vous n'avez besoin que des deux premiers paramètres, mais si vous avez besoin des valeurs d'index et de tableau, elles sont toujours disponibles.

## Conclusion

Et voilà ! À première vue, la méthode `reduce()` semble plus compliquée que d'autres méthodes de tableau JavaScript comme `forEach()` et `filter()`. Mais une fois que vous comprenez le concept de réducteur et d'accumulateur, la méthode est en fait assez simple.

En termes de programmation, une fonction "réductrice" retourne toujours une seule valeur, donc la méthode `reduce()` itère sur les valeurs définies dans votre tableau et les réduit en une seule valeur.

À l'intérieur de la fonction de rappel de la méthode `reduce()`, vous pouvez effectuer n'importe quelle opération dont vous avez besoin pour obtenir un certain résultat, comme résumer et regrouper certaines valeurs, ou supprimer les doublons.

Cela est fait avec l'aide de l'"accumulateur", qui stocke la valeur retournée par l'itération précédente. Vous définissez la valeur initiale de l'accumulateur en passant un deuxième argument à la méthode `reduce()`.

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine !