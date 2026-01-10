---
title: 'JavaScript Ajouter à un Tableau : un Guide JS sur la Méthode Push'
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-04-19T13:57:49.000Z'
originalURL: https://freecodecamp.org/news/javascript-append-to-array-a-js-guide-to-the-push-method-2
coverImage: https://cdn-media-2.freecodecamp.org/w1280/604b89aba7946308b768767f.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: 'JavaScript Ajouter à un Tableau : un Guide JS sur la Méthode Push'
seo_desc: 'Sometimes you need to append one or more new values at the end of an array.
  In this situation the push() method is what you need.

  The push() method will add one or more arguments at the end of an array in JavaScript:

  let arr = [0, 1, 2, 3];

  arr.push(...'
---

Parfois, vous devez ajouter une ou plusieurs nouvelles valeurs à la fin d'un tableau. Dans cette situation, la méthode `push()` est ce dont vous avez besoin.

La méthode `push()` ajoutera un ou plusieurs arguments à la fin d'un tableau en JavaScript :

```javascript
let arr = [0, 1, 2, 3];
arr.push(4);
console.log(arr); // [0, 1, 2, 3, 4]
```

Cette méthode accepte un nombre illimité d'arguments, et vous pouvez ajouter autant d'éléments que vous le souhaitez à la fin du tableau.

```
let arr = [0, 1, 2, 3];
arr.push(4, 5, 6, 7, 8, 9);
console.log(arr); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

La méthode `push()` retourne également la nouvelle longueur du tableau.

```
let arr = [0, 1, 2, 3];
let newLength = arr.push(4);
console.log(newLength); // 5
```

## Exemples de `push` en JavaScript et erreurs courantes

### Comment réassigner le tableau

Réassigner le tableau avec le résultat de `push` est une erreur courante.

```javascript
let arr = [0, 1, 2, 3];
arr = arr.push(4);
console.log(arr); // 5
```

Pour éviter cette erreur, vous devez vous souvenir que `push` modifie le tableau et retourne la nouvelle longueur. Si vous réassignez la variable avec la valeur de retour de `push()`, vous écrasez la valeur du tableau.

### Comment ajouter le contenu d'un tableau à la fin d'un autre

Si vous souhaitez ajouter le contenu d'un tableau à la fin d'un autre, `push` est une méthode possible à utiliser. `push` ajoutera comme nouveaux éléments tout ce que vous utilisez comme argument. Cela est également valable pour un autre tableau, donc le tableau doit être décompressé avec l'opérateur de décomposition :

```javascript
let arr1 = [0, 1, 2, 3];
let arr2 = [4, 5, 6, 7];
arr1.push(...arr2);
console.log(arr1); // [0, 1, 2, 3, 4, 5, 6, 7]
```

### Comment utiliser `push` sur un objet de type tableau

Il existe des objets similaires aux tableaux (comme l'objet `arguments` – l'objet qui permet d'accéder à tous les arguments d'une fonction), mais qui n'ont pas toutes les méthodes que possèdent les tableaux.

Pour pouvoir utiliser `push` ou d'autres méthodes de tableau sur ces objets, ils doivent d'abord être convertis en tableaux.

```
function myFunc() {
   let args = [...arguments];
   args.push(4);
   return args;
}

console.log(myFunc(0, 1, 2, 3)); // [0, 1, 2, 3, 4]
```

Si vous ne convertissez pas d'abord l'objet de type tableau `arguments` en un tableau, le code s'arrêtera avec une erreur `TypeError: arguments.push is not a function`.

## Conclusion

Si vous travaillez avec des tableaux, ne manquez pas `push`. Il ajoute un ou plusieurs éléments à la fin d'un tableau et retourne la nouvelle longueur du tableau.