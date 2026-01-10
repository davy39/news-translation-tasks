---
title: Comment fonctionne la méthode Filter de JavaScript – Expliqué avec des exemples
  de code
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-15T23:08:24.000Z'
originalURL: https://freecodecamp.org/news/javascript-filter-method
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Copy-of-Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-9-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment fonctionne la méthode Filter de JavaScript – Expliqué avec des
  exemples de code
seo_desc: "JavaScript's filter method serves as a powerful tool for selectively extracting\
  \ elements from arrays based on certain conditions. \nIntroduced alongside other\
  \ array methods in ECMAScript 5, the filter method has since become a fundamental\
  \ feature in J..."
---

La méthode `filter` de JavaScript est un outil puissant pour extraire sélectivement des éléments d'un tableau en fonction de certaines conditions. 

Introduite avec d'autres méthodes de tableau dans ECMAScript 5, la méthode `filter` est depuis devenue une fonctionnalité fondamentale en programmation JavaScript.

Dans cet article, nous allons approfondir la méthode `filter` de JavaScript, en explorant sa syntaxe, sa fonctionnalité et ses cas d'utilisation courants.

## Table des matières

* [Les bases de la méthode `filter`](#heading-les-bases-de-la-methode-filter)
* [Syntaxe de la méthode `filter`](#heading-syntaxe-de-la-methode-filter)
* [Cas d'utilisation courants de la méthode `filter`](#heading-cas-dutilisation-courants-de-la-methode-filter)
* [Conclusion](#heading-conclusion)

## Les bases de la méthode `filter`

La méthode `filter` en JavaScript est conçue comme une fonction d'ordre supérieur qui itère sur chaque élément d'un tableau, permettant aux développeurs d'appliquer une condition spécifique pour filtrer les éléments. 

La méthode `filter` ne modifie pas le tableau original, mais crée et retourne un nouveau tableau contenant uniquement les éléments qui répondent à la condition spécifiée.

## Syntaxe de la méthode `filter`

La syntaxe de la méthode `filter` est relativement simple :

```javascript
const newArray = array.filter(callback(element[, index[, array]])[, thisArg]);

```

* `array` : Le tableau original à partir duquel les éléments seront filtrés.
* `callback` : Une fonction qui est exécutée sur chaque élément du tableau.
* `element` : L'élément actuel en cours de traitement dans le tableau.
* `index` (optionnel) : L'index de l'élément actuel en cours de traitement.
* `array` (optionnel) : Le tableau sur lequel `filter` a été appelé.
* `thisArg` (optionnel) : Un objet optionnel auquel `this` peut faire référence dans la fonction `callback`.

## Cas d'utilisation courants de la méthode `filter`

### Filtrer en fonction d'une condition

**Scénario :** Vous avez un tableau de nombres et vous souhaitez filtrer uniquement les nombres pairs.

#### Sans Filter :

```javascript
const numbers = [1, 2, 3, 4, 5];
const evenNumbers = [];
for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] % 2 === 0) {
    evenNumbers.push(numbers[i]);
  }
}
// evenNumbers: [2, 4]

```

Dans l'approche traditionnelle, vous itéreriez sur chaque élément du tableau `numbers` en utilisant une boucle et vérifieriez manuellement si chaque nombre est pair avant de le pousser dans le tableau `evenNumbers`.

#### Avec Filter :

```javascript
const numbers = [1, 2, 3, 4, 5];
const evenNumbers = numbers.filter(num => num % 2 === 0);
// evenNumbers: [2, 4]

```

En utilisant la méthode `filter`, vous pouvez passer une fonction de rappel qui teste chaque élément (`num`) du tableau `numbers` et ne conserve que ceux qui satisfont la condition d'être pair. Cela donne un moyen concis et lisible de filtrer le tableau.

### Filtrer les valeurs Null ou Undefined

**Scénario :** Vous avez un tableau contenant à la fois des nombres et des valeurs `null` ou `undefined`, et vous souhaitez filtrer ces valeurs `null` ou `undefined`.

#### Sans Filter :

```javascript
const values = [10, null, 20, undefined, 30];
const filteredValues = [];
for (let i = 0; i < values.length; i++) {
  if (values[i] !== null && values[i] !== undefined) {
    filteredValues.push(values[i]);
  }
}
// filteredValues: [10, 20, 30]

```

Dans l'approche traditionnelle, vous itéreriez sur chaque élément du tableau `values` et vérifieriez manuellement si chaque élément n'est pas `null` ou `undefined` avant de le pousser dans le tableau `filteredValues`.

#### Avec Filter :

```javascript
const values = [10, null, 20, undefined, 30];
const filteredValues = values.filter(value => value !== null && value !== undefined);
// filteredValues: [10, 20, 30]

```

En utilisant la méthode `filter`, vous pouvez fournir une fonction de rappel concise qui filtre les valeurs `null` ou `undefined` du tableau, ce qui donne un code plus propre et plus maintenable.

### Filtrer les objets en fonction des valeurs de propriété

**Scénario :** Vous avez un tableau d'objets représentant des produits, et vous souhaitez filtrer les produits dont les prix sont supérieurs à 50 $.

#### Sans Filter :

```javascript
const products = [
  { id: 1, name: 'Product 1', price: 40 },
  { id: 2, name: 'Product 2', price: 60 },
  { id: 3, name: 'Product 3', price: 30 }
];
const expensiveProducts = [];
for (let i = 0; i < products.length; i++) {
  if (products[i].price > 50) {
    expensiveProducts.push(products[i]);
  }
}
// expensiveProducts: [{ id: 2, name: 'Product 2', price: 60 }]

```

Dans l'approche conventionnelle, vous itéreriez sur chaque objet produit dans le tableau `products` et vérifieriez manuellement si le prix de chaque produit est supérieur à 50 $ avant de le pousser dans le tableau `expensiveProducts`.

#### Avec Filter :

```javascript
const products = [
  { id: 1, name: 'Product 1', price: 40 },
  { id: 2, name: 'Product 2', price: 60 },
  { id: 3, name: 'Product 3', price: 30 }
];
const expensiveProducts = products.filter(product => product.price > 50);
// expensiveProducts: [{ id: 2, name: 'Product 2', price: 60 }]

```

En utilisant la méthode `filter`, vous pouvez fournir une fonction de rappel succincte qui filtre les produits dont les prix sont supérieurs à 50 $, ce qui donne un code plus propre et plus expressif.

## Conclusion

La méthode `filter` en JavaScript offre un moyen concis et efficace d'extraire sélectivement des éléments de tableaux en fonction de conditions spécifiées. Comprendre sa syntaxe, sa fonctionnalité, ses cas d'utilisation courants et les meilleures pratiques permet aux développeurs d'écrire un code plus propre et plus maintenable.

En utilisant la méthode `filter`, les développeurs peuvent rationaliser leurs tâches de manipulation de tableaux et améliorer l'efficacité globale de leurs applications JavaScript.

Si vous avez des commentaires, vous pouvez m'envoyer un message sur [Twitter](https://twitter.com/introvertedbot) ou [LinkedIn](https://www.linkedin.com/in/sahil-mahapatra/).