---
title: Nouveautés en JavaScript en 2023 – Changements avec des exemples de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-11-29T18:09:51.000Z'
originalURL: https://freecodecamp.org/news/the-biggest-changes-in-javascript-this-year
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/What-s-new.png
tags:
- name: ecmascript
  slug: ecmascript
- name: JavaScript
  slug: javascript
seo_title: Nouveautés en JavaScript en 2023 – Changements avec des exemples de code
seo_desc: "By Nishant Kumar\nECMAScript 2023, the 14th edition of the language, has\
  \ some great changes that will make your programming life easier. \nIn this article,\
  \ I'll go through each of the changes and explain why they're helpful. So let’s\
  \ dive in and see so..."
---

Par Nishant Kumar

ECMAScript 2023, la 14e édition du langage, apporte des changements intéressants qui faciliteront votre vie de programmeur.

Dans cet article, je vais passer en revue chacun de ces changements et expliquer pourquoi ils sont utiles. Alors, plongeons-nous et découvrons quelques nouvelles méthodes que nous avons reçues comme un cadeau de Noël anticipé.

## Object.groupBy

Supposons que vous avez un tableau d'objets et que vous souhaitez les séparer en fonction d'une valeur de propriété, d'un type ou d'une quantité.

```javascript
const inventory = [
  { name: "asparagus", type: "vegetables", quantity: 5 },
  { name: "bananas", type: "fruit", quantity: 0 },
  { name: "goat", type: "meat", quantity: 23 },
  { name: "cherries", type: "fruit", quantity: 5 },
  { name: "fish", type: "meat", quantity: 22 },
];
```

Nous avons maintenant une nouvelle méthode appelée `GroupBy` qui vous permet de faire exactement cela.

Pour l'utiliser, utilisez `Object.groupBy` sur n'importe quel tableau avec des objets, et passez une fonction qui retourne la clé spécifique par laquelle vous souhaitez catégoriser.

Ici, nous avons un tableau d'objets appelé `inventory`. Et une fonction `myCallback` qui prend une quantité comme paramètre et retourne `ok` si la quantité est supérieure à 5, sinon elle retourne `restock`.

Nous passons le tableau inventory et la fonction `myCallback` à Object.groupBy afin qu'il groupe les éléments du tableau par quantité.

```
function myCallback({ quantity }) {
  return quantity > 5 ? "ok" : "restock";
}

const result2 = Object.groupBy(inventory, myCallback);
```

Le résultat sera un objet qui contient la clé qui est la catégorie et les données spécifiées à l'intérieur.

```
{
    "restock": [
        {
            "name": "asparagus",
            "type": "vegetables",
            "quantity": 5
        },
        {
            "name": "bananas",
            "type": "fruit",
            "quantity": 0
        },
        {
            "name": "cherries",
            "type": "fruit",
            "quantity": 5
        }
    ],
    "ok": [
        {
            "name": "goat",
            "type": "meat",
            "quantity": 23
        },
        {
            "name": "fish",
            "type": "meat",
            "quantity": 22
        }
    ]
}
```

## Array.toSliced(), Array.toSorted() et Array.toReversed()

Lorsque nous utilisons des méthodes comme `sort()`, `splice()` et `reverse()`, elles modifient le tableau original. Cela peut parfois poser problème.

Mais en utilisant `toSpliced()`, `toSorted()` et `toReversed()`, nous pouvons épisser, trier et inverser un tableau sans modifier le tableau source. Voici comment cela fonctionne :

```javascript
const numbers = [3, 4, 1, 5, 2];

const splicedNumbers = numbers.toSpliced(1, 1);
const sortedNumbers = numbers.toSorted();
const reversedNumbers = numbers.toReversed();
```

Dans cet exemple, nous utilisons `toSpliced()` pour épisser le tableau, `toSort()` pour trier le tableau et `toReversed()` pour inverser le tableau. Ils fonctionnent comme les méthodes splice, sort et reverse habituelles, mais la différence est qu'ils retourneront un nouveau tableau et ne modifieront pas l'original.

## findLast() et findLastIndex()

Avant ES14, si vous vouliez trouver le dernier élément ou indice dans un tableau qui satisfait une certaine condition, vous deviez d'abord inverser le tableau.

```
function findLastIndexByReversing(arr, target) {
  const reversedArray = arr.slice().reverse();
  const reversedIndex = reversedArray.indexOf(target);

  if (reversedIndex !== -1) {
    const lastIndex = arr.length - 1 - reversedIndex;
    return lastIndex;
  } else {
    return -1; 
  }
}
```

Dans cet exemple, `findLastIndexByReversing` crée une copie inversée du tableau original en utilisant `slice().reverse()`. Ensuite, il utilise `indexOf` pour trouver la première occurrence de l'élément cible dans le tableau inversé. La fonction calcule l'indice correspondant dans le tableau original en soustrayant l'indice inversé de la longueur totale du tableau moins 1. Cela vous donne le dernier indice de l'élément dans le tableau original.

Ou vous pouvez utiliser une boucle for qui commence par la fin.

```
function findLastIndex(arr, target) {
  for (let i = arr.length - 1; i >= 0; i--) {
    if (arr[i] === target) {
      return i;
    }
  }
  return -1;
}
```

Dans cet exemple, la fonction `findLastIndex` prend un tableau `arr` et un élément cible `target`. Elle parcourt le tableau de la fin `arr.length - 1` au début `0`. Si elle trouve l'élément cible, elle retourne l'indice. Si l'élément n'est pas trouvé, elle retourne -1.

Mais maintenant, nous avons une méthode appelée `lastIndexOf()` qui commencera par la fin du tableau et retournera la valeur du premier élément qui satisfait la condition.

```
const fruits = ['apple', 'banana', 'orange', 'banana', 'kiwi'];

const lastIndex = fruits.lastIndexOf('banana');
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-2023-11-29-at-11.09.16-PM.png)
_Sortie montrant `3`_

## Conclusion

Ce sont les changements qui ont été introduits en JavaScript avec ECMAScript 2023.

Merci d'avoir lu, et je vous retrouverai dans le prochain tutoriel.

Si vous souhaitez voir une version vidéo courte de l'article, vous pouvez la consulter ici :

%[https://youtu.be/XSfJZyTKpdA?si=Cl2UfisCzScAFeyR]