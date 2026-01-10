---
title: Comment mélanger un tableau d'éléments en utilisant JavaScript ou TypeScript
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2023-06-05T23:32:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-shuffle-an-array-of-items-using-javascript-or-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/shuffle.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Comment mélanger un tableau d'éléments en utilisant JavaScript ou TypeScript
seo_desc: 'In this article we''ll be exploring how we can shuffle an array of items
  in multiple different ways using TypeScript, or JavaScript should you prefer.

  Pre-Requisites:


  An understanding of TypeScript or JavaScript

  A basic understanding of For Loops and...'
---

Dans cet article, nous allons explorer comment mélanger un tableau d'éléments de différentes manières en utilisant TypeScript, ou JavaScript si vous préférez.

Prérequis :

* Une compréhension de TypeScript ou JavaScript
* Une compréhension basique des boucles For et des tableaux

Les exemples suivants sont écrits en TypeScript, mais ils fonctionnent de la même manière en JavaScript. Vous devez simplement supprimer la syntaxe `:type` de tous les paramètres de fonction.

## Méthode 1 : Algorithme de tri Fisher-Yates

Le principe de base de cet algorithme est d'itérer sur les éléments, en échangeant chaque élément du tableau avec un élément sélectionné aléatoirement dans la partie non mélangée restante du tableau.

Examinons cela en pratique, cela vous aidera à mieux le visualiser :

```typescript

// déclarer la fonction 
const shuffle = (array: string[]) => { 
  for (let i = array.length - 1; i > 0; i--) { 
    const j = Math.floor(Math.random() * (i + 1)); 
    [array[i], array[j]] = [array[j], array[i]]; 
  } 
  return array; 
}; 
  
// Utilisation 
const myArray = ["apple", "banana", "cherry", "date", "elderberry"]; 
const shuffledArray = shuffle(myArray); 

console.log(shuffledArray); 
```

### Explication

Tout d'abord, vous créez une boucle for. Cela vous permettra de parcourir chaque élément du tableau, en échangeant sa position avec un autre élément du tableau.

Vous créez ensuite la variable `i` en lui assignant la valeur de `longueur du tableau - 1`.

Vous faites cela parce que nous commençons par le dernier élément du tableau, et tous les index de tableau commencent à 0 – donc le dernier index serait 4 (car il y a 5 éléments dans le tableau). 

Si vous essayiez d'accéder à `myArray[i]` avec `i` égal à `5` (la longueur), cela lancerait une exception indiquant qu'il n'y a pas d'élément à l'index 5. Nous soustrayons donc 1 de la longueur.

En commençant par le dernier élément et en travaillant à rebours, vous garantissez que les éléments vers la fin du tableau ont une chance égale d'être échangés avec n'importe quel autre élément.

Si vous deviez mélanger le tableau du début à la fin, les éléments vers le début du tableau auraient une chance plus élevée d'être échangés plusieurs fois, ce qui conduirait à un mélange biaisé ou inégal. Vous créez ensuite une variable `j` qui sera utilisée pour votre pointeur d'index pour le grand échange.

Vous assignez ensuite le tableau à l'index `i` au tableau à l'index `j`, et vice versa. Cela échange les valeurs et les mélange pour chaque élément du tableau.

### Explication de l'affectation par déstructuration de tableau

La syntaxe `[array[i], array[j]] = [array[j], array[i]]` est appelée une _affectation par déstructuration de tableau_. Elle permet l'échange de valeurs entre deux variables ou éléments de tableau sans avoir besoin d'une variable temporaire.

Voici comment fonctionne l'affectation par déstructuration de tableau dans le contexte du mélange d'un tableau en utilisant l'algorithme de mélange Fisher-Yates :

* `array[i]` et `array[j]` représentent deux éléments dans le tableau qui doivent être échangés.
* `[array[j], array[i]]` crée un tableau temporaire contenant les valeurs de `array[j]` et `array[i]`, mais dans l'ordre inverse.
* En assignant `[array[j], array[i]]` à `[array[i], array[j]]`, les valeurs de `array[j]` et `array[i]` sont échangées en place.

Vous pouvez en apprendre davantage sur la déstructuration de tableau [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment). Si nous devions imprimer les étapes de la fonction étape par étape, nous obtiendrions ce qui suit :

```ts
// tableau de départ 
["apple", "banana", "cherry", "date", "elderberry"]; 

// 1ère itération - Échanger elderberry avec date 
i = 4; // elderberry 
j = 3; // date 
[("apple", "banana", "cherry", "elderberry", "date")]; 

// 2ème itération - Échanger elderberry avec apple 
i = 3; // 
elderberry j = 0; // apple 
[("elderberry", "banana", "cherry", "apple", "date")]; 

// 3ème itération - Échanger cherry avec banana 
i = 2; // cherry 
j = 1; // banana 
[("elderberry", "cherry", "banana", "apple", "date")]; 

// 4ème itération - Échanger cherry avec lui-même (reste où il est) 
i = 1; // cherry 
j = 1; // cherry 
[("elderberry", "cherry", "banana", "apple", "date")]; 

Et voilà – nous avons mélangé le tableau en utilisant l'algorithme Fisher-Yates.

## Méthode 2 : Utilisation de la méthode `sort()` avec une fonction de comparaison aléatoire

Si vous n'êtes pas familier avec la fonction de tri JS, j'ai écrit un tutoriel sur son utilisation que vous pouvez trouver [ici](https://www.freecodecamp.org/news/how-does-the-javascript-sort-function-work/).

```ts
const shuffle = (array: string[]) => { 
    return array.sort(() => Math.random() - 0.5); 
}; 

// Utilisation 
const myArray = ["apple", "banana", "cherry", "date", "elderberry"]; 
const shuffledArray = shuffle(myArray); 
console.log(shuffledArray);
```

Il s'agit d'une fonction de tri() simple qui retourne un nombre aléatoire, qui pourrait être négatif, 0 ou positif. La méthode `sort()` compare en interne des paires d'éléments dans le tableau et détermine leur ordre relatif en fonction de la valeur de retour de la fonction de comparaison.

* Si la fonction de comparaison retourne une valeur négative, le premier élément est considéré comme plus petit et doit être placé avant le deuxième élément dans le tableau trié.
* Si la fonction de comparaison retourne une valeur positive, le premier élément est considéré comme plus grand et doit être placé après le deuxième élément dans le tableau trié.
* Si la fonction de comparaison retourne 0, l'ordre relatif des éléments reste inchangé.

### Que retourne `Math.random()` ?

Lorsque vous appelez `Math.random()`, il génère un nombre pseudo-aléatoire, car comme vous le savez peut-être, rien n'est _vraiment_ aléatoire haha. "Pseudo-aléatoire" signifie que les nombres générés semblent être aléatoires mais sont en réalité déterminés par un algorithme déterministique (qui diffère entre les implémentations des moteurs JS). Le nombre qu'il retourne sera toujours un nombre flottant, entre 0 et 1. Les nombres flottants (communément appelés "floats") sont des nombres qui peuvent être positifs ou négatifs et peuvent avoir une partie fractionnaire. Des exemples de nombres à virgule flottante incluent _3.14, -0.5, 1.0, 2.71828_, et ainsi de suite.

### Pourquoi soustrait-on 0.5 du résultat de `Math.random()` ?

En soustrayant 0.5 du résultat de Math.random(), vous introduisez une valeur aléatoire entre -0.5 et 0.5. Cette valeur aléatoire fera en sorte que la fonction de comparaison retourne des valeurs négatives, positives ou nulles de manière aléatoire pour différentes paires d'éléments. Par conséquent, la méthode sort() mélange le tableau de manière aléatoire.

## Méthode 3 : Utilisation de la fonction `Array.map()` de JS

La fonction `.map()` vous permet d'itérer sur chaque élément d'un tableau et de les transformer en nouvelles valeurs basées sur une fonction de mappage fournie. La fonction `map()` retourne un nouveau tableau avec les valeurs transformées, laissant le tableau original inchangé.

```ts
const shuffle = (array: string[]) => { 
    return array.map((a) => ({ sort: Math.random(), value: a }))
        .sort((a, b) => a.sort - b.sort)
        .map((a) => a.value); 
}; 

// Utilisation 
const myArray = ["apple", "banana", "cherry", "date","elderberry"]; const shuffledArray = shuffle(myArray); 
console.log(shuffledArray); 
```

Ici, vous parcourez le tableau et utilisez la même fonction `Math.random()` que dans l'exemple précédent dans la fonction `map()`, retournant un tableau d'objets avec un numéro de tri et une valeur. Vous pouvez ensuite utiliser la fonction `sort()` pour trier le tableau en fonction de ces valeurs, avant d'appeler à nouveau la fonction `map()` pour créer un tableau de valeurs (c'est-à-dire les noms de chaînes).

```ts

const shuffle = (array: string[]) => { 
  const shuffled = array.slice(); 
  let currentIndex = shuffled.length; 
  let temporaryValue, randomIndex; 
  while (currentIndex !== 0) { 
    randomIndex = Math.floor(Math.random() * currentIndex); 
    currentIndex -= 1; 
    temporaryValue = shuffled[currentIndex]; 
    shuffled[currentIndex] = shuffled[randomIndex]; 
    shuffled[randomIndex] = temporaryValue; 
  }
  return shuffled; 
}; 

// Utilisation 
const myArray = ["apple", "banana", "cherry", "date", "elderberry"]; const shuffledArray = shuffle(myArray); 
console.log(shuffledArray);

```

## Conclusion

Je recommande la méthode de l'algorithme Fisher-Yates, car elle a une faible complexité temporelle, car elle dépend uniquement de la taille du tableau. Sa complexité temporelle peut être vue comme _`O(n)`_, ce qui implique que doubler la taille de l'entrée doublera approximativement le temps d'exécution. De même, si la taille de l'entrée est réduite de moitié, le temps d'exécution sera approximativement réduit de moitié également.

Sans entrer dans trop de détails :

* `O` représente l'ordre de croissance ou la classe de complexité.
* `n` fait référence à la taille de l'entrée, généralement représentée par la variable `n`.

Cela signifie que la complexité de la fonction change lorsque la taille de l'entrée (n) change – par exemple : Complexité x 2 (2 éléments dans le tableau) vs Complexité x 10 (10 éléments dans le tableau). Ainsi, plus le tableau est grand, plus la complexité et le temps nécessaire pour mélanger sont grands.

Cela vaut la peine de le noter lors du mélange de grands tableaux. Il pourrait être intéressant de regarder d'autres méthodes, ou peut-être de diviser le tableau et d'exécuter le mélange en parallèle avant de le réassembler.

Cette méthode permet également un mélange plus facile de n'importe quel type de tableau, pas seulement `string[]`. Elle fonctionnerait également très bien lors de l'utilisation des génériques TypeScript. Cela permet à n'importe quel type de tableau d'être passé à la fonction et mélangé.

```ts
const shuffle = <T>(array: T[]) => { 
  for (let i = array.length - 1; i > 0; i--) { 
    const j = Math.floor(Math.random() * (i + 1)); 
    [array[i], array[j]] = [array[j], array[i]]; 
  }
  return array; 
}; 

const strings = ["apple", "banana", "cherry", "date", "elderberry"]; 
const users = [ { name: "John", surname: "Doe" }, { name: "Jane", surname: "Doe" }];

const shuffledArray = shuffle(strings); 
const shuffledObjects = shuffle(users); 

console.log(shuffledArray); 
console.log(shuffledObjects); 
```

J'espère que vous avez trouvé cet article utile et que vous avez appris comment mélanger facilement un tableau d'éléments. Vous pourriez utiliser cela pour plusieurs cas d'utilisation tels que :

* Mélanger une playlist de chansons
* Mélanger une liste de membres d'équipe pour déterminer un système de rotation
* Créer un quiz de questions aléatoires / randomiser l'ordre des échantillons de données, par exemple des avis clients / feedback.

Comme toujours, n'hésitez pas à [me suivre sur Twitter @gweaths](http://twitter.com/gweaths).