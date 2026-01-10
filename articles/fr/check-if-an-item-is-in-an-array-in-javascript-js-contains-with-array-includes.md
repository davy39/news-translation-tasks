---
title: Vérifier si un élément est dans un tableau en JavaScript – JS Contains avec
  Array.includes()
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-28T22:28:00.000Z'
originalURL: https://freecodecamp.org/news/check-if-an-item-is-in-an-array-in-javascript-js-contains-with-array-includes
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/pankaj-patel-1IW4HQuauSU-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Vérifier si un élément est dans un tableau en JavaScript – JS Contains
  avec Array.includes()
seo_desc: "You can use the includes() method in JavaScript to check if an item exists\
  \ in an array. You can also use it to check if a substring exists within a string.\
  \ \nIt returns true if the item is found in the array/string and false if the item\
  \ doesn't exist...."
---

Vous pouvez utiliser la méthode `includes()` en JavaScript pour vérifier si un élément existe dans un tableau. Vous pouvez également l'utiliser pour vérifier si une sous-chaîne existe dans une chaîne de caractères. 

Elle retourne `true` si l'élément est trouvé dans le tableau/chaîne et `false` si l'élément n'existe pas.

Dans cet article, vous verrez comment utiliser la méthode `includes()` en JavaScript pour vérifier si un élément est dans un tableau, et si une sous-chaîne existe dans une chaîne de caractères. 

## Comment vérifier si un élément est dans un tableau en JavaScript en utilisant `Array.includes()`

Voici la syntaxe pour utiliser la méthode `includes()` afin de vérifier si un élément est dans un tableau : 

```txt
array.includes(item, fromIndex)
```

Décomposons la syntaxe ci-dessus :

`array` désigne le nom du tableau qui sera parcouru pour vérifier si un élément existe.

La méthode `includes()` prend deux paramètres – `item` et `fromIndex`. 

* `item` est l'élément particulier que vous recherchez. 
* `fromIndex`, qui est un paramètre optionnel, spécifie l'index à partir duquel commencer la recherche. Si vous n'incluez pas ce paramètre, l'index par défaut sera défini à 0 (le premier index). 

Voici quelques exemples pour montrer comment utiliser la méthode `includes()` afin de vérifier si un élément existe dans un tableau :

```javascript
const nums = [ 1, 3, 5, 7];
console.log(nums.includes(3));
// true
```

Dans l'exemple ci-dessus, nous avons créé un tableau appelé `nums` avec quatre nombres – 1, 3, 5, 7. 

En utilisant la notation par point, nous avons attaché la méthode `includes()` au tableau `nums`.

Dans le paramètre de la méthode `includes()`, nous avons passé 3. C'est l'élément que nous voulons rechercher. 

Nous avons obtenu `true` car 3 existe dans le tableau `nums`. 

Essayons de rechercher un nombre qui n'existe pas dans le tableau. 

```javascript
const nums = [ 1, 3, 5, 7];
console.log(nums.includes(8));
// false

```

Comme prévu, nous avons obtenu `false` dans l'exemple ci-dessus car 8 n'est pas un élément du tableau `nums`. 

## Comment vérifier si un élément est dans un tableau en JavaScript en utilisant `Array.includes()` à partir d'un index spécifié

Dans la dernière section, nous avons vu comment vérifier si un élément existait dans un tableau sans utiliser le deuxième paramètre de la méthode `includes()`. 

Pour rappel, le deuxième paramètre est utilisé pour spécifier l'index à partir duquel commencer la recherche d'un élément dans un tableau. 

L'index d'un tableau commence à 0. Ainsi, le premier élément est 0, le deuxième élément est 1, le troisième élément est 2, et ainsi de suite. 

Voici un exemple pour montrer comment nous pouvons utiliser le deuxième paramètre de la méthode `includes()` :

```javascript
const nums = [ 1, 3, 5, 7];
console.log(nums.includes(3,2));
// false
```

L'exemple ci-dessus a retourné `false` même si nous avions 3 comme élément dans le tableau. Voici pourquoi :

En utilisant le deuxième paramètre, nous avons dit à la méthode `includes()` de rechercher le nombre 3 mais en commençant à l'index 2 : `nums.includes(3,2)`.

Voici le tableau : [ 1, 3, 5, 7]

Index 0 = 1.

Index 1 = 3.

Index 2 = 5.

Index 3 = 7.

Ainsi, en commençant par le deuxième index qui est 5, nous n'avons que 5 et 7 ([5,7]) à parcourir. C'est pourquoi la recherche de 3 à partir de l'index 2 a retourné `false`.

Si vous changez l'index pour commencer la recherche à 1, vous obtiendrez `true` car 3 peut être trouvé dans cette plage. C'est-à-dire :

```javascript
const nums = [ 1, 3, 5, 7];
console.log(nums.includes(3,1));
// true
```

## Comment vérifier si une sous-chaîne est dans une chaîne en JavaScript en utilisant la méthode `includes()`

De manière similaire aux exemples précédents, vous devez attacher la méthode `includes()` au nom de la chaîne à parcourir en utilisant la notation par point. 

Voici à quoi ressemble la syntaxe :

```txt
string.includes(substring, fromIndex)
```

Voici un exemple :

```javascript
const bio = "I am a web developer";
console.log(bio.includes("web"));
// true
```

Dans l'exemple ci-dessus, la variable `bio` avait une valeur de "I am a web developer". 

En utilisant la méthode `includes()`, nous avons recherché la sous-chaîne "web". 

Nous avons obtenu `true` car "web" est dans la chaîne `bio`.

Vous pouvez également utiliser le deuxième paramètre pour spécifier où la recherche commencera, mais notez que chaque caractère dans une chaîne représente un index et que les espaces entre chaque sous-chaîne représentent également un index.

Voici un exemple pour démontrer cela :

```javascript
let bio = "I am a web developer";
console.log(bio.includes("web",9));
// false
```

Nous obtenons `false` car l'index 9 est le e dans "web". 

En commençant par l'index 9, la chaîne ressemblerait à ceci : "eb developer". La sous-chaîne "web" n'existe pas dans la chaîne, donc `false` est retourné.

## Résumé

Dans cet article, nous avons parlé de la méthode `includes()` en JavaScript. Vous l'utilisez pour vérifier si un élément existe dans un tableau. Vous pouvez également l'utiliser pour vérifier si une sous-chaîne peut être trouvée dans une chaîne de caractères.

Nous avons vu des exemples qui expliquaient son utilisation pour vérifier un élément dans un tableau à partir du premier index, puis un autre exemple à partir d'un index spécifié.

Enfin, nous avons vu comment utiliser la méthode `includes()` pour vérifier si une sous-chaîne existe dans une chaîne à partir du premier index et à partir d'un index spécifié. 

Bon codage !