---
title: Explorons Slice(), Splice() & la syntaxe de propagation (Spread Syntax) en
  JavaScript
subtitle: ''
author: Parathan Thiyagalingam
co_authors: []
series: null
date: '2019-01-25T16:43:18.000Z'
originalURL: https://freecodecamp.org/news/lets-explore-slice-splice-spread-syntax-in-javascript-e242a6f21e60
coverImage: https://cdn-media-1.freecodecamp.org/images/1*btQyN4AbhZ-RWQQser8y5A.jpeg
tags:
- name: coding
  slug: coding
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Explorons Slice(), Splice() & la syntaxe de propagation (Spread Syntax)
  en JavaScript
seo_desc: 'I came across this freeCodeCamp challenge and got stuck for some time thinking
  about how I could find a way to solve it. They already mentioned solving using Slice
  & Splice. I was confused at that time when to use Slice and when to use Splice.

  Here, ...'
---

Je suis tombé sur ce défi [freeCodeCamp](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-algorithm-scripting/slice-and-splice) et j'ai été bloqué un moment en réfléchissant à la manière de le résoudre. Ils ont déjà mentionné la résolution en utilisant Slice et Splice. J'étais confus à ce moment-là sur quand utiliser Slice et quand utiliser Splice.

Ici, je vais partager comment je l'ai résolu avec ces méthodes.

Slice et Splice sont tous deux utilisés pour manipuler des tableaux. Voyons comment ils le font.

### Slice :

La méthode Slice prend 2 arguments.

**1er Argument** : Spécifie à partir d'où la sélection doit commencer.

Par exemple :

```javascript
var arr1 = [1,5,8,9];
arr1.slice(1); // [5,8,9]
```

À partir du premier index (5), il retournera les éléments.

**2ème Argument** : Spécifie à quel niveau le point final doit être. Si vous ne mettez pas cela dans les parenthèses lors de l'appel de la méthode slice, il retournera les éléments de l'index de départ à la fin du tableau.

```javascript
var arr1 = [1,5,8,9];
console.log(arr1.slice(1,3));
//[ 5, 8 ]
```

Si vous mettez un nombre négatif lors de l'appel, la sélection sera faite à partir de la fin du tableau.

```javascript
var arr1 = [1,5,8,9];
console.log(arr1.slice(-2));
//[ 8, 9 ]
```

**Note : Slice retourne toujours les éléments sélectionnés du tableau.**

**Slice ne changera pas le tableau. Le tableau reste intact. Voir l'exemple ci-dessous :**

```javascript
var arr1 = [1,5,8,9];
arr1.slice(2);
console.log(arr1);
// [ 1, 5, 8, 9 ]
```

Même si vous avez apporté des modifications au tableau, cela ne l'affectera pas. Il retournera le tableau original tel qu'il était au début.

### **Splice :**

Il peut prendre plusieurs arguments.

Cela signifie,

**1er Argument** : Spécifie à quelle position un nouvel élément ou un élément existant doit être ajouté/supprimé. Si la valeur est négative, la position sera comptée à partir de la fin du tableau.

**2ème Argument** : Le nombre d'éléments à supprimer à partir de la position de départ. Si c'est 0, alors aucun élément ne sera supprimé. Si ce n'est pas passé, il supprimera tous les éléments à partir de la position de départ.

```javascript
var arr1 = [1,5,8,9];
console.log(arr1.splice(1,2));
// [ 5, 8 ]
```

**3ème Argument -> nème Argument** : La valeur des éléments que vous souhaitez ajouter au tableau.

```javascript
var arr1 = [1,5,8,9];
console.log(arr1.splice(1,2,'Hi','Medium'));
// [5,8]
```

Vous pourriez penser que nous avons ajouté 'Hi', 'Medium' au tableau mais cela ne s'affiche pas ici... N'est-ce pas ?

Oui, nous avons affiché **arr1.splice(1,2,'Hi','Medium').**

**Note :**

* **Splice retournera uniquement les éléments supprimés du tableau.**
* **Splice modifiera le tableau original**

```javascript
var arr1 = [1,5,8,9];
arr1.splice(1,2,'Hi','Medium');
console.log(arr1);
// [ 1, 'Hi', 'Medium', 9 ]
```

### **Syntaxe de propagation (Spread Syntax) :**

**Définition** : Permet à un itérable tel qu'une expression de tableau ou une chaîne d'être développé dans des endroits où zéro ou plusieurs arguments (pour les appels de fonction) ou éléments (pour les littéraux de tableau) sont attendus, ou une expression d'objet d'être développée dans des endroits où zéro ou plusieurs paires clé-valeur (pour les littéraux d'objet) sont attendues.

Prenons un exemple pour cela :

```javascript
var arr1 = [1,3,6,7];
var arr2 = [5,arr1,8,9];
console.log(arr2);
// [ 5, [ 1, 3, 6, 7 ], 8, 9 ]
```

Je veux que cela soit dans un seul tableau comme **[ 5, 1, 3, 6, 7, 8, 9 ].**

Je peux utiliser cette syntaxe de propagation pour résoudre cela :

```javascript
var arr1 = [1,3,6,7];
var arr2 = [5,...arr1,8,9];
console.log(arr2);
//[ 5, 1, 3, 6, 7, 8, 9 ]
```

Un autre usage principal de la syntaxe de propagation est lors de la copie d'un tableau :

```javascript
var arr = [1, 2, 3];
var arr2 = arr;
arr2.push(4);

console.log(arr2);
// [ 1, 2, 3, 4 ]

console.log(arr);
// [ 1, 2, 3, 4 ]
```

J'ai ajouté "**4**" à **arr2** seulement. Mais cela a également modifié arr.

Nous pouvons résoudre cela en utilisant la syntaxe de propagation comme suit...

```javascript
var arr = [1, 2, 3];
var arr2 = [...arr]; // comme arr.slice()
arr2.push(4);

console.log(arr2);
// [ 1, 2, 3, 4 ]

console.log(arr);
// [ 1, 2, 3]
```

Vous pouvez vous référer à la documentation [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) pour plus d'informations sur la syntaxe de propagation.

**Alors, jetons un coup d'œil au défi.**

```javascript
function frankenSplice(arr1, arr2, n) {

// C'est vivant. C'est vivant !

let array2Copy = [...arr2];

array2Copy.splice(n,0, ...arr1);

             //console.log(array2Copy);

return array2Copy;

}

frankenSplice([1, 2, 3], [4, 5, 6], 1);
```

La condition principale de ce défi est "ne pas altérer arr1/arr2 après l'exécution de la fonction".

Donc, j'ai créé une **copie du tableau arr2**, et en utilisant la méthode **splice**, j'ai ajouté arr1 à l'intérieur de la copie de arr2 qui est nommée **array2Copy.**

#### **Conclusion finale :**

-> La méthode Slice

* retournera les éléments sélectionnés du tableau
* prend 2 arguments
* ne modifie pas le tableau original

-> La méthode Splice

* retournera les éléments supprimés du tableau
* prend plusieurs arguments
* modifie le tableau original

C'est mon premier tutoriel sur la programmation — merci de l'avoir lu ! Vos commentaires m'aideront à améliorer mes compétences en programmation et en écriture.

Bon codage !

Connectez-vous avec moi via [Twitter](https://twitter.com/parathantl)