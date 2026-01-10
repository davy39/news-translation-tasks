---
title: 'Comment corriger TypeError : Impossible de lire la propriété ''push'' de undefined
  en JavaScript'
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-10-11T23:18:26.000Z'
originalURL: https://freecodecamp.org/news/fix-typeerror-cannot-read-property-push-of-undefined-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/cover-template--13-.png
tags:
- name: error
  slug: error
- name: JavaScript
  slug: javascript
seo_title: 'Comment corriger TypeError : Impossible de lire la propriété ''push''
  de undefined en JavaScript'
seo_desc: 'When working with JavaScript arrays, you have to be careful that you are
  not calling the push(), pop(), shift(), unShift(), or splice() methods on a variable
  that is meant to be an array but has a value of undefined.

  If you mistakenly do this, you''ll...'
---

Lorsque vous travaillez avec des tableaux JavaScript, vous devez veiller à ne pas appeler les méthodes `push()`, `pop()`, `shift()`, `unShift()` ou `splice()` sur une variable censée être un tableau mais qui a une valeur `undefined`.

Si vous faites cela par erreur, vous obtiendrez cette erreur :

![](https://paper-attachments.dropbox.com/s_E70A1833F8285C7F5412DCD9531F13EA1E92CB215392E2D976AD0B6D0DFB9AA0_1665231049694_image.png align="left")

Si vous appelez `pop()` ou l'une de ces autres méthodes au lieu de push (comme dans l'exemple ci-dessus), l'erreur mentionnera 'pop' (ou l'autre méthode que vous utilisez) à la place. Cela signifie que l'approche que vous apprendrez dans cet article fonctionnera pour toutes les méthodes.

Pour bien comprendre cet article et cette erreur, il est essentiel de souligner les différentes raisons qui peuvent déclencher ce problème :

* Vous appelez la méthode sur une variable précédemment définie sur `undefined`.
    
* Vous appelez la méthode sur une variable avant qu'elle n'ait été initialisée avec un tableau.
    
* Vous appelez la méthode sur un élément de tableau plutôt que sur le tableau lui-même.
    
* Vous appelez la méthode sur une propriété d'objet qui n'existe pas ou qui a une valeur `undefined`.
    

N'oubliez pas que cette méthode peut être `push()`, `pop()`, `shift()`, `unShift()` ou `splice()`. Analysons maintenant chaque scénario et apprenons comment corriger l'erreur.

## Appeler la méthode sur une variable qui a été précédemment définie sur `undefined`

Lorsque vous travaillez avec des variables et des types de données comme les chaînes de caractères, nous avons tendance à assigner aux variables des valeurs comme `undefined` et `null` avant de passer la valeur d'origine. Parfois, nous faisons cela lors de l'appel de fonctions ou de la gestion de certaines actions.

Pour les tableaux, cela ne fonctionne pas de cette façon – sinon, vous obtiendrez l'erreur :

```js
let myArray = undefined;

myArray.push("John Doe"); // Uncaught TypeError: Cannot read properties of undefined (reading 'push')

console.log(myArray);
```

Pour corriger cela, vous devez déclarer que la variable est un tableau avant que les méthodes de tableau comme `push()`, `pop()`, et d'autres puissent fonctionner dessus :

```js
let myArray = [];

myArray.push("John Doe");

console.log(myArray); // ["John Doe"]
```

**Note :** Lorsqu'une variable est déclarée, elle n'est pas reconnue comme une variable de tableau tant qu'elle n'est pas initialisée à l'aide du constructeur `Array` ou de la notation littérale de tableau (`[]`).

## Appeler la méthode sur une variable avant qu'elle n'ait été initialisée avec un tableau

Comme vous venez de l'apprendre ci-dessus, une autre façon de déclarer des variables est de les créer sans leur assigner de valeur.

```js
let myArray;

myArray.push("John Doe"); // Uncaught TypeError: Cannot read properties of undefined (reading 'push')

console.log(myArray);
```

Cela fonctionne bien pour les types de données comme les chaînes de caractères, les nombres et autres, mais ne fonctionne pas bien pour un tableau. Vous devez initialiser les tableaux avec le constructeur `Array` ou une notation littérale de tableau (`[]`).

```js
let myArray = [];

// Ou

let myArray = new Array();
```

Notre code ressemblera maintenant à ceci :

```js
let myArray = [];

myArray.push("John Doe");

console.log(myArray); // ["John Doe"]
```

## Appeler la méthode sur un élément de tableau plutôt que sur le tableau lui-même

Les méthodes de tableau sont censées être appelées sur le tableau lui-même (c'est-à-dire le tableau ou la variable utilisée pour stocker le tableau) et non sur un élément du tableau.

```js
// Exemple de tableaux
let myArray = [12, 13, 17];
let myArray2 = [];
let myArray3 = new Array();

// Exemple d'éléments de tableau
myArray[0];
myArray[1];
myArray[2];
```

Vous pourriez vouloir ajouter un élément à une position particulière d'un tableau et penser qu'attacher la méthode `push()` ou `unShift()` directement à l'élément résoudra le problème. Malheureusement, vous obtiendrez l'erreur « cannot read property 'push' of undefined » :

```js
let myArray = [12, 13, 17];

myArray[3].push(15); // Uncaught TypeError: Cannot read properties of undefined (reading 'push')

console.log(myArray);
```

Pour corriger cela, vous devez appeler la méthode push sur la variable elle-même et non sur son élément :

```js
let myArray = [12, 13, 17];

myArray.push(15);

console.log(myArray); // [12,13,17,15]
```

## Appeler la méthode sur une propriété d'objet qui n'existe pas ou qui a une valeur `undefined`

Un dernier scénario pourrait être celui où vous essayez d'appeler la méthode sur une propriété d'objet qui n'existe pas ou dont la valeur est définie sur `undefined` :

```js
const user = { name: 'John Doe', scores: undefined };
const user2 = { name: 'John Doe' };

user.scores.push(50);
user2.scores.push(50); 
// Uncaught TypeError: Cannot read properties of undefined (reading 'push')
```

Dans le scénario ci-dessus, il y a deux objets : le premier objet a une paire clé-valeur `scores` dont la valeur est définie sur `undefined`, mais il est censé recevoir des valeurs de tableau. Tandis que pour le second objet, `scores` n'existe pas. Les deux situations peuvent provoquer des erreurs.

Pour corriger cela, tout ce que vous avez à faire est d'**initialiser** la clé, afin qu'elle attende des valeurs de tableau en utilisant le littéral de tableau :

```js
const user = { name: "John Doe", scores: [] };

user.scores.push(50);

console.log(user);
```

## Conclusion

Dans cet article, vous avez appris comment corriger l'erreur « Cannot read properties of undefined », qui se produit lorsque vous attachez ces méthodes de tableau à des variables qui ne sont pas déclarées ou initialisées en tant que variables.

Bon codage !