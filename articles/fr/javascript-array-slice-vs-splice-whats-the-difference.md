---
title: 'JavaScript Array Slice vs Splice : la différence expliquée avec un gâteau'
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2020-08-11T16:03:17.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-slice-vs-splice-whats-the-difference
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/dilyara-garifullina-I48gnI1Qs5o-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: 'JavaScript Array Slice vs Splice : la différence expliquée avec un gâteau'
seo_desc: "This title could have been \"how not to get confused between JavaScript's\
  \ splice and slice,\" because I can never remember the difference between the two.\
  \ \nSo I am hoping this trick will help both me and you in the future:\nS (p) lice\
  \ = Slice + (p) => S..."
---

Ce titre aurait pu être "comment ne pas confondre splice et slice en JavaScript", car je n'arrive jamais à me souvenir de la différence entre les deux. 

J'espère donc que cette astuce aidera à la fois moi et vous à l'avenir :


```
S (p) lice = Slice + (p) => Slice + in (p) lace
```
 

## Array.prototype.slice()
Array.prototype.slice() est utilisé pour découper un tableau à partir du point `start` jusqu'au point `end`, en excluant `end`. 

Comme le suggère le nom, il est utilisé pour extraire des éléments d'un tableau. Mais contrairement à la découpe d'un gâteau, découper un tableau ne modifie pas le tableau réel, mais le laisse inchangé (gâteau infini !). 

```JS 
arr.slice(start, [end])

```

Règles
1. Un nouveau tableau est retourné et le tableau original reste inchangé. 
2. Si `end` est omis, end devient la fin (dernier élément) du tableau. 
3. Si `start` est négatif, les éléments sont comptés à partir de la fin.


```JS
const infiniteCake = ['?','?','?','?','?','?']

let myPieceOfCake = infiniteCake.slice(0,1) // ['?']
let yourDoublePieceOfCake = infiniteCake.slice(0,2) // (2) ["?", "?"]
console.log(infiniteCake) //['?','?','?','?','?','?']

```
Comme vous le voyez, `inifinteCake` reste inchangé.


## Array.prototype.splice()
Splice effectue des opérations **en place**, ce qui signifie qu'il modifie le tableau existant. 

En plus de supprimer des éléments, splice est également utilisé pour ajouter des éléments. Splice est la vraie découpe de gâteau du monde réel :

```JS
arr.splice(start, [deleteCount, itemToInsert1, itemToInsert2, ...])
```

Règles
1. Les opérations sont effectuées en place. 
2. Un tableau est retourné avec les éléments supprimés. 
3. Si `start` est négatif, les éléments sont comptés à partir de la fin.
4. Si `deleteCount` est omis, les éléments jusqu'à la fin du tableau sont supprimés.
5. Si les éléments à insérer tels que `itemToInsert1` sont omis, seuls les éléments sont supprimés.


```JS
const cake = ['?','?','?','?','?','?'];
let myPieceOfCake = cake.splice(0, 1) // ["?"]
console.log(cake) // (5) ["?", "?", "?", "?", "?"]

let yourDoublePieceOfCake = cake.splice(0,2) //(2) ["?", "?"]
console.log(cake) //(3) ["?", "?", "?"]

```
Ici, `cake` est modifié et réduit en taille. 


## Exemples de code
```JS
const myArray  = [1,2,3,4,5,6,7] 

console.log(myArray.slice(0))       // [ 1, 2, 3, 4, 5, 6, 7 ]
console.log(myArray.slice(0, 1))    // [ 1 ]
console.log(myArray.slice(1))       // [ 2, 3, 4, 5, 6, 7 ]
console.log(myArray.slice(5))       // [ 6, 7 ]
console.log(myArray.slice(-1))      // [ 7 ]
console.log(myArray)                // [ 1, 2, 3, 4, 5, 6, 7 ]



const secondArray = [10, 20, 30, 40, 50]

console.log(secondArray.splice(0, 1))   // [ 10 ] : supprime 1 élément à partir de l'index 0
console.log(secondArray.splice(-2, 1))  // [ 40 ] : supprime 1 élément à partir de l'index end-2 
console.log(secondArray)                // [ 20, 30, 50 ]
console.log(secondArray.splice(0))      // [ 20, 30, 50 ] : supprime tous les éléments à partir de l'index 0
console.log(secondArray)                // []
console.log(secondArray.splice(2, 0, 60, 70)) // [] : supprime 0 éléments à partir de l'index 2 (n'existe pas donc par défaut 0) et insère ensuite 60, 70
console.log(secondArray)                // [60, 70]
```


## TL;DR
Utilisez `splice` si le tableau original doit être modifié ou si des éléments doivent être ajoutés.

Utilisez `slice` pour supprimer des éléments si le tableau original ne doit pas être modifié.

****

Intéressé par plus de tutoriels et de JSBytes de ma part ? [Inscrivez-vous à ma newsletter.](https://tinyletter.com/shrutikapoor) ou [suivez-moi sur Twitter](https://twitter.com/shrutikapoor08)