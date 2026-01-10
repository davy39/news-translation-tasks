---
title: Comment fonctionne la méthode Reduce de JavaScript – Expliqué avec des exemples
  de code
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-19T18:00:44.000Z'
originalURL: https://freecodecamp.org/news/javascript-reduce-method-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Copy-of-Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-10-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment fonctionne la méthode Reduce de JavaScript – Expliqué avec des
  exemples de code
seo_desc: "Introduced alongside other array methods in ECMAScript 5, reduce() offers\
  \ a unique and powerful way to transform arrays into single values. \nIn this article,\
  \ you'll learn about the reduce() method by understanding what it is, its syntax,\
  \ and finally ..."
---

Introduite aux côtés d'autres méthodes de tableau dans ECMAScript 5, `reduce()` offre une manière unique et puissante de transformer des tableaux en valeurs uniques. 

Dans cet article, vous apprendrez à connaître la méthode `reduce()` en comprenant ce qu'elle est, sa syntaxe, et enfin vous verrez quelques cas d'utilisation où vous pouvez l'utiliser efficacement.

Vous pouvez obtenir tout le code source à partir d'[ici](https://github.com/dotslashbit/fcc-article-resources/blob/main/js-reduce-method/index.js).

## Table des matières

* [Comprendre les bases de `reduce()`](#comprendre-les-bases)
* [Pensez-y comme à la sculpture de l'argile](#heading-pensez-y-comme-a-la-sculpture-de-largile)
* [Cas d'utilisation de `reduce()`](#cas-dutilisation)
* [Conclusion](#heading-conclusion)

## Comprendre les bases de `reduce()`

Au cœur de `reduce()`, cette méthode itère à travers chaque élément d'un tableau, appliquant une fonction définie par l'utilisateur (aptement nommée le "réducteur") à la fois à l'élément actuel et à une valeur d'accumulateur.

Cet accumulateur commence avec une valeur initiale que vous fournissez (ou par défaut le premier élément du tableau) et est mis à jour avec la valeur de retour du réducteur à chaque itération. 

En fin de compte, l'état final de l'accumulateur devient la valeur unique retournée par `reduce()`.

### Pensez-y comme à la sculpture de l'argile

Imaginez façonner un morceau d'argile. Vous commencez avec une boule et appliquez répétitivement une pression et une direction, la transformant en la forme souhaitée. 

De manière similaire, `reduce()` prend une valeur initiale (l'argile) et, à travers votre fonction réductrice personnalisée (vos mains de sculpteur), la façonne en le résultat final.

## Cas d'utilisation de `reduce()`

Maintenant, explorons quelques scénarios où `reduce()` excelle :

### Calcul des totaux

**Scénario :** Vous avez un tableau d'objets représentant des produits, et vous souhaitez calculer le prix total de tous les produits.

#### Approche traditionnelle avec une boucle :

```javascript
const products = [
  { name: "Shirt", price: 20 },
  { name: "Shoes", price: 50 },
  { name: "Hat", price: 15 }
];

// Initialiser totalPrice à 0
let totalPrice = 0;

// Parcourir chaque produit et ajouter son prix à totalPrice
for (const product of products) {
  totalPrice += product.price;
}

console.log("Prix total (boucle) :", totalPrice); // Sortie : Prix total (boucle) : 85

```

L'approche traditionnelle initialise une variable `totalPrice` à 0, puis itère à travers chaque produit dans le tableau `products` en utilisant une boucle `for...of`. 

À l'intérieur de la boucle, elle ajoute la propriété `price` du produit actuel à `totalPrice`. 

Après avoir itéré à travers tous les produits, le `totalPrice` final (85) est affiché dans la console.

#### Utilisation de `reduce()` :

```javascript
const products = [
  { name: "Shirt", price: 20 },
  { name: "Shoes", price: 50 },
  { name: "Hat", price: 15 }
];

// Utiliser reduce() avec une valeur initiale de 0 pour totalPrice
const totalPriceReduce = products.reduce((sum, product) => sum + product.price, 0);

console.log("Prix total (reduce) :", totalPriceReduce); // Sortie : Prix total (reduce) : 85

```

La méthode `reduce()` prend une fonction de rappel et une valeur initiale optionnelle (0 dans ce cas). La fonction de rappel reçoit deux arguments : `sum`, l'accumulateur, initialement défini à la valeur initiale (0), et `product`, l'objet produit actuel. 

À l'intérieur de la fonction de rappel, la propriété `price` du `product` actuel est ajoutée à `sum`. La valeur de retour de la fonction de rappel devient le nouveau `sum` pour l'itération suivante. 

Après avoir itéré à travers tous les produits, le `sum` final (85) est retourné et stocké dans `totalPriceReduce`.

**Comparaison :** Les deux approches atteignent le même résultat, mais `reduce()` offre une manière plus concise et fonctionnelle de calculer le prix total. Elle évite le besoin d'une boucle explicite et exprime directement la logique d'addition des prix dans la fonction de rappel.

### Trouver les valeurs minimales ou maximales

**Scénario :** Vous avez un tableau de températures et souhaitez trouver les températures les plus élevées et les plus basses.

#### Approche traditionnelle avec des boucles :

```javascript
const temperatures = [25, 18, 32, 20, 15];

// Initialiser maxTemp et minTemp à des valeurs irréalistes
let maxTemp = -Infinity;
let minTemp = Infinity;

// Parcourir chaque température et mettre à jour maxTemp et minTemp
for (const temp of temperatures) {
  maxTemp = Math.max(maxTemp, temp);
  minTemp = Math.min(minTemp, temp);
}

console.log("Température max (boucle) :", maxTemp); // Sortie : Température max (boucle) : 32
console.log("Température min (boucle) :", minTemp); // Sortie : Température min (boucle) : 15

```

L'approche traditionnelle initialise `maxTemp` à l'infini négatif et `minTemp` à l'infini positif pour s'assurer qu'ils sont mis à jour avec la première température rencontrée.

Elle itère ensuite à travers chaque température dans le tableau `temperatures` en utilisant une boucle `for...of`. À l'intérieur de la boucle, elle utilise `Math.max()` pour comparer la `maxTemp` actuelle avec la température actuelle et met à jour `maxTemp` si nécessaire.

De manière similaire, elle utilise `Math.min()` pour comparer la `minTemp` actuelle et la met à jour si nécessaire. Après avoir itéré à travers toutes les températures, les `maxTemp` (32) et `minTemp` (15) finales sont affichées dans la console.

#### Utilisation de `reduce()` :

```javascript
const temperatures = [25, 18, 32, 20, 15];

// Utiliser reduce() avec des valeurs initiales de -Infinity et Infinity
const maxTempReduce = temperatures.reduce((max, temp) => Math.max(max, temp), -Infinity);
const minTempReduce = temperatures.reduce((min, temp) => Math.min(min, temp), Infinity);

console.log("Température max (reduce) :", maxTempReduce); // Sortie : Température max (reduce) : 32
console.log("Température min (reduce) :", minTempReduce); // Sortie : Température min (reduce) : 15

```

La méthode `reduce()` prend une fonction de rappel et une valeur initiale (infini négatif et positif dans ce cas). La fonction de rappel reçoit deux arguments : `max` ou `min`, l'accumulateur, commençant par les valeurs initiales, et `temp`, la température actuelle. 

À l'intérieur de la fonction de rappel, `Math.max()` ou `Math.min()` est utilisé pour comparer la température actuelle avec l'accumulateur et le mettre à jour en conséquence. 

Après avoir itéré à travers toutes les températures, les températures maximale et minimale finales sont retournées.

**Comparaison :** Les deux approches atteignent le même résultat, mais `reduce()` offre une manière plus concise et fonctionnelle de trouver les valeurs maximale et minimale. Elle utilise le concept d'accumulateur pour comparer et mettre à jour directement les valeurs dans la fonction de rappel.

### Construction d'objets complexes :

**Scénario :** Vous avez un tableau d'étudiants et souhaitez les regrouper par leurs matières dans un seul objet.

#### Approche traditionnelle avec des boucles :

```javascript
const students = [
  { name: "Alice", age: 25, subject: "Math" },
  { name: "Bob", age: 30, subject: "Science" },
  { name: "Charlie", age: 28, subject: "History" },
];

// Initialiser un objet vide pour stocker les groupes de matières
const subjectMap = {};

// Parcourir chaque étudiant et les ajouter à leur groupe de matière respectif
for (const student of students) {
  const subject = student.subject;
  if (!subjectMap

[subject]) {
    subjectMap[subject] = [];
  }
  subjectMap[subject].push(student);
}

console.log("Carte des matières (boucle) :", subjectMap); // Sortie : { Math: [...], Science: [...], History: [...] }

```

Cette approche initialise un objet vide `subjectMap` pour stocker les étudiants regroupés. Elle itère ensuite à travers chaque étudiant dans le tableau `students` en utilisant une boucle `for...of`. 

À l'intérieur de la boucle, elle récupère la `subject` de l'étudiant. Si la `subject` n'existe pas en tant que clé dans `subjectMap`, un nouveau tableau est créé pour cette matière. L'objet étudiant actuel est ensuite ajouté au tableau de matière correspondant dans `subjectMap`.

Après avoir itéré à travers tous les étudiants, l'objet `subjectMap` final contient des groupes d'étudiants basés sur leurs matières.

#### Utilisation de `reduce()` :

```javascript
const students = [
  { name: "Alice", age: 25, subject: "Math" },
  { name: "Bob", age: 30, subject: "Science" },
  { name: "Charlie", age: 28, subject: "History" },
];

// Utiliser reduce() pour construire l'objet subject map
const subjectMapReduce = students.reduce((map, student) => {
  const subject = student.subject;
  map[subject] = map[subject] || [];
  map[subject].push(student);
  return map;
}, {});

console.log("Carte des matières (reduce) :", subjectMapReduce); // Sortie : { Math: [...], Science: [...], History: [...] }

```

La méthode `reduce()` prend une fonction de rappel et une valeur initiale (un objet vide dans ce cas). La fonction de rappel reçoit deux arguments : `map`, l'accumulateur, commençant par l'objet vide initial, et `student`, l'objet étudiant actuel. 

À l'intérieur de la fonction de rappel, la propriété `subject` de l'étudiant actuel est récupérée. Si la `subject` n'existe pas dans `map`, un tableau vide est créé pour elle. L'objet étudiant actuel est ajouté au tableau de matière correspondant dans `map`.

L'objet `map` mis à jour est retourné comme le nouvel accumulateur pour l'itération suivante. Après avoir itéré à travers tous les étudiants, l'objet `map` final contient les étudiants regroupés.

**Comparaison :** Les deux approches atteignent le même résultat, mais `reduce()` offre une manière plus concise et fonctionnelle de construire l'objet. Elle utilise le concept d'accumulateur pour construire directement le `subjectMap` dans la fonction de rappel.

### Aplanir des tableaux multidimensionnels :

**Scénario :** Vous avez une structure de tableau imbriquée et souhaitez créer un tableau à un seul niveau.

#### Approche traditionnelle avec des boucles :

```javascript
const multiArray = [[1, 2], [3, 4], [5]];

// Initialiser un tableau vide pour stocker les éléments aplatis
const flatArray = [];

// Parcourir chaque sous-tableau et ajouter ses éléments à flatArray
for (const subArray of multiArray) {
  for (const element of subArray) {
    flatArray.push(element);
  }
}

console.log("Tableau aplati (boucle) :", flatArray); // Sortie : [1, 2, 3, 4, 5]

```

Cette approche initialise un tableau vide `flatArray` pour stocker les éléments aplatis. Elle itère ensuite à travers chaque sous-tableau dans `multiArray` en utilisant une boucle `for...of` imbriquée. 

À l'intérieur de la boucle interne, chaque élément du sous-tableau actuel est ajouté à `flatArray`. Après avoir itéré à travers tous les sous-tableaux, le `flatArray` final contient tous les éléments dans un seul niveau.

#### Utilisation de `reduce()` :

```javascript
const multiArray = [[1, 2], [3, 4], [5]];

// Utiliser reduce() pour aplatir le tableau multidimensionnel
const flatArrayReduce = multiArray.reduce((accumulator, currentArray) => {
  return accumulator.concat(currentArray);
}, []);

console.log("Tableau aplati (reduce) :", flatArrayReduce); // Sortie : [1, 2, 3, 4, 5]

```

La méthode `reduce()` prend une fonction de rappel et une valeur initiale (un tableau vide `[]` dans ce cas). La fonction de rappel reçoit deux arguments : `accumulator`, l'accumulateur, commençant par le tableau vide initial, et `currentArray`, le sous-tableau actuel en cours de traitement. 

À l'intérieur de la fonction de rappel, la méthode `concat()` est utilisée pour concaténer le `currentArray` avec l'`accumulator`, aplatissant ainsi le tableau. Le résultat de `concat()` devient le nouvel accumulateur pour l'itération suivante. 

Après avoir itéré à travers tous les sous-tableaux, l'`accumulator` final contient tous les éléments du tableau multidimensionnel aplatis en un seul niveau.

**Comparaison :** Les deux approches atteignent le même résultat d'aplatissement du tableau, mais `reduce()` fournit une solution plus élégante et concise. Elle utilise le concept d'accumulateur pour construire progressivement le tableau aplati, évitant le besoin de boucles imbriquées et de l'ajout manuel des éléments.

## Conclusion

En résumé, la méthode `reduce()` en JavaScript fournit une manière concise et puissante de transformer des tableaux en valeurs uniques ou en structures de données complexes. 

En offrant de la flexibilité à travers une fonction réductrice personnalisable et une valeur initiale optionnelle, `reduce()` simplifie les tâches courantes telles que le calcul des totaux, la recherche des extrêmes, le regroupement d'objets et l'aplatissement des tableaux. 

Comprendre `reduce()` permet aux développeurs d'écrire un code plus propre et plus efficace, et ouvre de nouvelles possibilités pour la manipulation de données dans les projets JavaScript.

Si vous avez des commentaires, envoyez-moi un message sur [Twitter](https://twitter.com/introvertedbot) ou [LinkedIn](https://www.linkedin.com/in/sahil-mahapatra/).